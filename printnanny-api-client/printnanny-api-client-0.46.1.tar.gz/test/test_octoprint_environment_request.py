# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.octoprint_environment_request import OctoprintEnvironmentRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestOctoprintEnvironmentRequest(unittest.TestCase):
    """OctoprintEnvironmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoprintEnvironmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.octoprint_environment_request.OctoprintEnvironmentRequest()  # noqa: E501
        if include_optional :
            return OctoprintEnvironmentRequest(
                os = printnanny_api_client.models.octoprint_platform_request.OctoprintPlatformRequest(
                    id = '0', 
                    platform = '0', 
                    bits = '0', ), 
                python = printnanny_api_client.models.octoprint_python_request.OctoprintPythonRequest(
                    version = '0', 
                    pip = '0', 
                    virtualenv = '0', ), 
                hardware = printnanny_api_client.models.octoprint_hardware_request.OctoprintHardwareRequest(
                    cores = 56, 
                    freq = 1.337, 
                    ram = 56, ), 
                pi_support = printnanny_api_client.models.octoprint_pi_support_request.OctoprintPiSupportRequest(
                    model = '0', 
                    throttle_state = '0', 
                    octopi_version = '0', )
            )
        else :
            return OctoprintEnvironmentRequest(
                os = printnanny_api_client.models.octoprint_platform_request.OctoprintPlatformRequest(
                    id = '0', 
                    platform = '0', 
                    bits = '0', ),
                python = printnanny_api_client.models.octoprint_python_request.OctoprintPythonRequest(
                    version = '0', 
                    pip = '0', 
                    virtualenv = '0', ),
                hardware = printnanny_api_client.models.octoprint_hardware_request.OctoprintHardwareRequest(
                    cores = 56, 
                    freq = 1.337, 
                    ram = 56, ),
                pi_support = printnanny_api_client.models.octoprint_pi_support_request.OctoprintPiSupportRequest(
                    model = '0', 
                    throttle_state = '0', 
                    octopi_version = '0', ),
        )

    def testOctoprintEnvironmentRequest(self):
        """Test OctoprintEnvironmentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
