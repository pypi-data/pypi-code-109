# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.api.pulp_ansible_api_v2_collections_versions_api import PulpAnsibleApiV2CollectionsVersionsApi  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException


class TestPulpAnsibleApiV2CollectionsVersionsApi(unittest.TestCase):
    """PulpAnsibleApiV2CollectionsVersionsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_ansible.api.pulp_ansible_api_v2_collections_versions_api.PulpAnsibleApiV2CollectionsVersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        """
        pass


if __name__ == '__main__':
    unittest.main()
