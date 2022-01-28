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
from printnanny_api_client.models.paginated_printer_profile_list import PaginatedPrinterProfileList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedPrinterProfileList(unittest.TestCase):
    """PaginatedPrinterProfileList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedPrinterProfileList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_printer_profile_list.PaginatedPrinterProfileList()  # noqa: E501
        if include_optional :
            return PaginatedPrinterProfileList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.printer_profile.PrinterProfile(
                        id = 56, 
                        user = 56, 
                        octoprint_device = 56, 
                        axes_e_inverted = True, 
                        axes_e_speed = -2147483648, 
                        axes_x_speed = -2147483648, 
                        axes_x_inverted = True, 
                        axes_y_inverted = True, 
                        axes_y_speed = -2147483648, 
                        axes_z_inverted = True, 
                        axes_z_speed = -2147483648, 
                        extruder_count = -2147483648, 
                        extruder_nozzle_diameter = 1.337, 
                        extruder_shared_nozzle = True, 
                        heated_bed = True, 
                        heated_chamber = True, 
                        model = '', 
                        name = '', 
                        octoprint_key = '', 
                        volume_custom_box = {
                            'key' : null
                            }, 
                        volume_depth = 1.337, 
                        volume_formfactor = '', 
                        volume_height = 1.337, 
                        volume_origin = '', 
                        volume_width = 1.337, 
                        url = '', )
                    ]
            )
        else :
            return PaginatedPrinterProfileList(
        )

    def testPaginatedPrinterProfileList(self):
        """Test PaginatedPrinterProfileList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
