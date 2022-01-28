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
import datetime

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_access_policy_response_list import PaginatedAccessPolicyResponseList  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestPaginatedAccessPolicyResponseList(unittest.TestCase):
    """PaginatedAccessPolicyResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedAccessPolicyResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.paginated_access_policy_response_list.PaginatedAccessPolicyResponseList()  # noqa: E501
        if include_optional :
            return PaginatedAccessPolicyResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulpcore.models.access_policy_response.AccessPolicyResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        permissions_assignment = [
                            None
                            ], 
                        statements = [
                            None
                            ], 
                        viewset_name = '0', 
                        customized = True, )
                    ]
            )
        else :
            return PaginatedAccessPolicyResponseList(
        )

    def testPaginatedAccessPolicyResponseList(self):
        """Test PaginatedAccessPolicyResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
