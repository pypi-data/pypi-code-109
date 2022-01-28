# @file test_git_dependency.py
# Unit test suite for the GitDependency class.
#
##
# Copyright (c) Microsoft Corporation
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
##
import os
import sys
import unittest
import logging
import tempfile
import pkg_resources
from edk2toollib.utility_functions import RunCmd, RemoveTree
from edk2toolext.environment import environment_descriptor_files as EDF
from edk2toolext.environment.extdeptypes.nuget_dependency import NugetDependency
from edk2toolext.environment import version_aggregator
from edk2toolext.bin import nuget

test_dir = None
good_version = "5.2.0"
bad_version = "5.2.13.1.2"
missing_version = "5.200.13"

hw_package_name = "NuGet.CommandLine"
hw_json_template = '''
{
  "scope": "global",
  "type": "nuget",
  "name": "NuGet.CommandLine",
  "source": "https://api.nuget.org/v3/index.json",
  "version": "%s"
}
'''


def prep_workspace():
    global test_dir
    # if test temp dir doesn't exist
    if test_dir is None or not os.path.isdir(test_dir):
        test_dir = tempfile.mkdtemp()
        logging.debug("temp dir is: %s" % test_dir)
    else:
        clean_workspace()
        test_dir = tempfile.mkdtemp()


def clean_workspace():
    global test_dir
    if test_dir is None:
        return

    if os.path.isdir(test_dir):
        RemoveTree(test_dir)
        test_dir = None


class TestNugetDependency(unittest.TestCase):
    def setUp(self):
        prep_workspace()
        self.saved_nuget_path = os.getenv(NugetDependency.NUGET_ENV_VAR_NAME)

    @classmethod
    def setUpClass(cls):
        logger = logging.getLogger('')
        logger.addHandler(logging.NullHandler())
        unittest.installHandler()

    @classmethod
    def tearDownClass(cls):
        clean_workspace()

    def tearDown(self):
        # we need to reset the version aggregator each time
        version_aggregator.GetVersionAggregator().Reset()

        if self.saved_nuget_path is not None:
            os.environ[NugetDependency.NUGET_ENV_VAR_NAME] = self.saved_nuget_path

        # Fix the nuget.exe is missing....download again
        requirement = pkg_resources.Requirement.parse("edk2-pytool-extensions")
        nuget_file_path = os.path.join("edk2toolext", "bin", "NuGet.exe")
        nuget_path = pkg_resources.resource_filename(requirement, nuget_file_path)

        if not os.path.isfile(nuget_path):
            nuget.DownloadNuget()

    def test_can_get_nuget_path(self):
        nuget_cmd = NugetDependency.GetNugetCmd()
        nuget_cmd += ["locals", "global-packages", "-list"]
        ret = RunCmd(nuget_cmd[0], ' '.join(nuget_cmd[1:]), outstream=sys.stdout)
        self.assertEqual(ret, 0)  # make sure we have a zero return code

    def test_missing_nuget(self):

        if NugetDependency.NUGET_ENV_VAR_NAME in os.environ:
            del os.environ[NugetDependency.NUGET_ENV_VAR_NAME]

        # delete the package file
        original = NugetDependency.GetNugetCmd()[-1]  # get last item which will be exe path
        os.remove(original)
        path = NugetDependency.GetNugetCmd()
        self.assertIsNone(path)  # Should not be found

    def test_nuget_env_var(self):
        if NugetDependency.NUGET_ENV_VAR_NAME in os.environ:
            del os.environ[NugetDependency.NUGET_ENV_VAR_NAME]

        # set the env var to our path
        os.environ[NugetDependency.NUGET_ENV_VAR_NAME] = test_dir
        nuget.DownloadNuget(test_dir)  # download to test dir
        found_path = NugetDependency.GetNugetCmd()[-1]

        # done with env testing.  clean up
        del os.environ[NugetDependency.NUGET_ENV_VAR_NAME]
        self.assertIsNotNone(found_path)
        path_should_be = os.path.join(test_dir, "NuGet.exe")
        self.assertTrue(os.path.samefile(found_path, path_should_be))

    def test_nuget_env_var_with_space(self):
        if NugetDependency.NUGET_ENV_VAR_NAME in os.environ:
            del os.environ[NugetDependency.NUGET_ENV_VAR_NAME]

        # set the env var to our path
        my_test_dir = os.path.join(test_dir, "my folder")
        os.makedirs(my_test_dir)
        os.environ[NugetDependency.NUGET_ENV_VAR_NAME] = my_test_dir
        nuget.DownloadNuget(my_test_dir)  # download to test dir
        found_path = NugetDependency.GetNugetCmd()[-1]

        # done with env testing.  clean up
        del os.environ[NugetDependency.NUGET_ENV_VAR_NAME]

        self.assertIsNotNone(found_path)
        path_should_be = os.path.join(my_test_dir, "NuGet.exe")
        self.assertTrue(os.path.samefile(found_path.strip('"'), path_should_be))

    # good case
    def test_download_good_nuget(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % good_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)
        ext_dep.fetch()
        self.assertTrue(ext_dep.verify())
        self.assertEqual(ext_dep.version, good_version)
        # make sure we clean up after ourselves
        ext_dep.clean()

    # bad case
    def test_download_bad_nuget(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % bad_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)
        with self.assertRaises((RuntimeError, ValueError)):  # we can throw a value error if we hit the cache
            # we should throw an exception because we don't know how to parse the version
            ext_dep.fetch()
        self.assertFalse(ext_dep.verify())

    def test_normalize_version(self):
        version1 = "5.10.05.0"
        proper_version1 = "5.10.5"
        self.assertEqual(proper_version1, NugetDependency.normalize_version(version1))
        version2 = "6.10"
        proper_version2 = "6.10.0"
        self.assertEqual(proper_version2, NugetDependency.normalize_version(version2))
        version3 = "6"
        proper_version3 = "6.0.0"
        self.assertEqual(proper_version3, NugetDependency.normalize_version(version3))
        version4 = "6-beta"
        proper_version4 = "6.0.0-beta"
        self.assertEqual(proper_version4, NugetDependency.normalize_version(version4))
        version5 = "3.2.1.-alpha"
        proper_version5 = "3.2.1-alpha"
        self.assertEqual(proper_version5, NugetDependency.normalize_version(version5))
        version6 = "3.2.1.0-rc1"
        proper_version6 = "3.2.1-rc1"
        self.assertEqual(proper_version6, NugetDependency.normalize_version(version6))
        # try some bad cases
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("not a number")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("6.0-beta-beta")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("6.0-bad")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("6.0-")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("--")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("6-")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version("")
        with self.assertRaises(ValueError):
            NugetDependency.normalize_version(bad_version)

    # missing case
    def test_download_missing_nuget(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % missing_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)
        with self.assertRaises(RuntimeError):
            ext_dep.fetch()
        self.assertFalse(ext_dep.verify())
        self.assertEqual(ext_dep.version, missing_version)

    def test_cache_path_not_found(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % good_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)

        ext_dep.global_cache_path = "not_a_real_path"
        self.assertFalse(ext_dep._fetch_from_cache(hw_package_name))

    def test_bad_cached_package(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % good_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)

        #
        # Create a cache with a bad cached package.
        #
        # First, create the cache.
        cache_dir = os.path.join(test_dir, 'nuget_test_bad_cache')
        os.mkdir(cache_dir)
        ext_dep.global_cache_path = cache_dir
        # Then create the directories inside the cache that should hold the contents.
        package_cache_dir = os.path.join(cache_dir, hw_package_name.lower(), good_version)
        os.makedirs(package_cache_dir)
        # There are no package directories inside the cache.
        self.assertFalse(ext_dep._fetch_from_cache(hw_package_name))

        # Create a directory that doesn't match the heuristic.
        test_cache_contents = os.path.join(package_cache_dir, "contents", "blah")
        os.makedirs(test_cache_contents)
        self.assertFalse(ext_dep._fetch_from_cache(hw_package_name))

    def test_good_cached_package(self):
        ext_dep_file_path = os.path.join(test_dir, "hw_ext_dep.json")
        with open(ext_dep_file_path, "w+") as ext_dep_file:
            ext_dep_file.write(hw_json_template % good_version)

        ext_dep_descriptor = EDF.ExternDepDescriptor(ext_dep_file_path).descriptor_contents
        ext_dep = NugetDependency(ext_dep_descriptor)

        #
        # Create a cache with a good cached package.
        #
        # First, create the cache.
        cache_dir = os.path.join(test_dir, 'nuget_test_good_cache')
        os.mkdir(cache_dir)
        ext_dep.global_cache_path = cache_dir
        # Then create the directories inside the cache that should hold the contents.
        package_cache_dir = os.path.join(cache_dir, hw_package_name.lower(), good_version)
        os.makedirs(package_cache_dir)

        # Create a directory that doesn't match the heuristic.
        test_cache_contents = os.path.join(package_cache_dir, hw_package_name, "working_blah")
        os.makedirs(test_cache_contents)
        self.assertTrue(ext_dep._fetch_from_cache(hw_package_name))

        # Make sure that the contents were copied correctly.
        final_path = os.path.join(ext_dep.contents_dir, "working_blah")
        self.assertTrue(os.path.isdir(final_path))
        self.assertTrue(ext_dep.verify())


if __name__ == '__main__':
    unittest.main()
