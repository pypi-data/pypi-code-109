# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.27.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501
from intrinio_sdk.models.zacks_sales_surprise_summary import ZacksSalesSurpriseSummary  # noqa: F401,E501


class ApiResponseSecurityZacksSalesSurprises(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sales_surprises': 'list[ZacksSalesSurpriseSummary]',
        'security': 'SecuritySummary',
        'next_page': 'str'
    }

    attribute_map = {
        'sales_surprises': 'sales_surprises',
        'security': 'security',
        'next_page': 'next_page'
    }

    def __init__(self, sales_surprises=None, security=None, next_page=None):  # noqa: E501
        """ApiResponseSecurityZacksSalesSurprises - a model defined in Swagger"""  # noqa: E501

        self._sales_surprises = None
        self._security = None
        self._next_page = None
        self.discriminator = None

        if sales_surprises is not None:
            self.sales_surprises = sales_surprises
        if security is not None:
            self.security = security
        if next_page is not None:
            self.next_page = next_page

    @property
    def sales_surprises(self):
        """Gets the sales_surprises of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501


        :return: The sales_surprises of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: list[ZacksSalesSurpriseSummary]
        """
        return self._sales_surprises
        
    @property
    def sales_surprises_dict(self):
        """Gets the sales_surprises of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501


        :return: The sales_surprises of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: list[ZacksSalesSurpriseSummary]
        """

        result = None

        value = self.sales_surprises
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'sales_surprises': value }

        
        return result
        

    @sales_surprises.setter
    def sales_surprises(self, sales_surprises):
        """Sets the sales_surprises of this ApiResponseSecurityZacksSalesSurprises.


        :param sales_surprises: The sales_surprises of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :type: list[ZacksSalesSurpriseSummary]
        """

        self._sales_surprises = sales_surprises

    @property
    def security(self):
        """Gets the security of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501

        The Security resolved from the given identifier  # noqa: E501

        :return: The security of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501

        The Security resolved from the given identifier as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The security of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: SecuritySummary
        """

        result = None

        value = self.security
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this ApiResponseSecurityZacksSalesSurprises.

        The Security resolved from the given identifier  # noqa: E501

        :param security: The security of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

    @property
    def next_page(self):
        """Gets the next_page of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :return: The next_page of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: str
        """
        return self._next_page
        
    @property
    def next_page_dict(self):
        """Gets the next_page of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501

        The token required to request the next page of the data. If null, no further results are available. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The next_page of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.next_page
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'next_page': value }

        
        return result
        

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ApiResponseSecurityZacksSalesSurprises.

        The token required to request the next page of the data. If null, no further results are available.  # noqa: E501

        :param next_page: The next_page of this ApiResponseSecurityZacksSalesSurprises.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseSecurityZacksSalesSurprises):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
