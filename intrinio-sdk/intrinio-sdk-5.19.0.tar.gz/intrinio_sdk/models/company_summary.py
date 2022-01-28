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


class CompanySummary(object):
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
        'id': 'str',
        'ticker': 'str',
        'name': 'str',
        'lei': 'str',
        'cik': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ticker': 'ticker',
        'name': 'name',
        'lei': 'lei',
        'cik': 'cik'
    }

    def __init__(self, id=None, ticker=None, name=None, lei=None, cik=None):  # noqa: E501
        """CompanySummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ticker = None
        self._name = None
        self._lei = None
        self._cik = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if name is not None:
            self.name = name
        if lei is not None:
            self.lei = lei
        if cik is not None:
            self.cik = cik

    @property
    def id(self):
        """Gets the id of this CompanySummary.  # noqa: E501

        The Intrinio ID of the company  # noqa: E501

        :return: The id of this CompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this CompanySummary.  # noqa: E501

        The Intrinio ID of the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this CompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this CompanySummary.

        The Intrinio ID of the company  # noqa: E501

        :param id: The id of this CompanySummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this CompanySummary.  # noqa: E501

        The stock market ticker symbol associated with the company's common stock securities  # noqa: E501

        :return: The ticker of this CompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this CompanySummary.  # noqa: E501

        The stock market ticker symbol associated with the company's common stock securities as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this CompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ticker
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
            result = { 'ticker': value }

        
        return result
        

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CompanySummary.

        The stock market ticker symbol associated with the company's common stock securities  # noqa: E501

        :param ticker: The ticker of this CompanySummary.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def name(self):
        """Gets the name of this CompanySummary.  # noqa: E501

        The company's common name  # noqa: E501

        :return: The name of this CompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this CompanySummary.  # noqa: E501

        The company's common name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this CompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this CompanySummary.

        The company's common name  # noqa: E501

        :param name: The name of this CompanySummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def lei(self):
        """Gets the lei of this CompanySummary.  # noqa: E501

        The Legal Entity Identifier (LEI) assigned to the company  # noqa: E501

        :return: The lei of this CompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._lei
        
    @property
    def lei_dict(self):
        """Gets the lei of this CompanySummary.  # noqa: E501

        The Legal Entity Identifier (LEI) assigned to the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The lei of this CompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.lei
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
            result = { 'lei': value }

        
        return result
        

    @lei.setter
    def lei(self, lei):
        """Sets the lei of this CompanySummary.

        The Legal Entity Identifier (LEI) assigned to the company  # noqa: E501

        :param lei: The lei of this CompanySummary.  # noqa: E501
        :type: str
        """

        self._lei = lei

    @property
    def cik(self):
        """Gets the cik of this CompanySummary.  # noqa: E501

        The Central Index Key (CIK) assigned to the company  # noqa: E501

        :return: The cik of this CompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._cik
        
    @property
    def cik_dict(self):
        """Gets the cik of this CompanySummary.  # noqa: E501

        The Central Index Key (CIK) assigned to the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The cik of this CompanySummary.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.cik
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
            result = { 'cik': value }

        
        return result
        

    @cik.setter
    def cik(self, cik):
        """Sets the cik of this CompanySummary.

        The Central Index Key (CIK) assigned to the company  # noqa: E501

        :param cik: The cik of this CompanySummary.  # noqa: E501
        :type: str
        """

        self._cik = cik

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
        if not isinstance(other, CompanySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
