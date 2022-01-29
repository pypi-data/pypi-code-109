# coding: utf-8

"""
    Component Database API

    The API that provides access to Component Database data.  # noqa: E501

    The version of the OpenAPI document: 3.13.0
    Contact: djarosz@anl.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cdbApi.configuration import Configuration


class PropertyMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'metadata_key': 'str',
        'metadata_value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'metadata_key': 'metadataKey',
        'metadata_value': 'metadataValue'
    }

    def __init__(self, id=None, metadata_key=None, metadata_value=None, local_vars_configuration=None):  # noqa: E501
        """PropertyMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._metadata_key = None
        self._metadata_value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.metadata_key = metadata_key
        self.metadata_value = metadata_value

    @property
    def id(self):
        """Gets the id of this PropertyMetadata.  # noqa: E501


        :return: The id of this PropertyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PropertyMetadata.


        :param id: The id of this PropertyMetadata.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def metadata_key(self):
        """Gets the metadata_key of this PropertyMetadata.  # noqa: E501


        :return: The metadata_key of this PropertyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._metadata_key

    @metadata_key.setter
    def metadata_key(self, metadata_key):
        """Sets the metadata_key of this PropertyMetadata.


        :param metadata_key: The metadata_key of this PropertyMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metadata_key is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_key is not None and len(metadata_key) > 32):
            raise ValueError("Invalid value for `metadata_key`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_key is not None and len(metadata_key) < 1):
            raise ValueError("Invalid value for `metadata_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._metadata_key = metadata_key

    @property
    def metadata_value(self):
        """Gets the metadata_value of this PropertyMetadata.  # noqa: E501


        :return: The metadata_value of this PropertyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._metadata_value

    @metadata_value.setter
    def metadata_value(self, metadata_value):
        """Sets the metadata_value of this PropertyMetadata.


        :param metadata_value: The metadata_value of this PropertyMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metadata_value is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_value is not None and len(metadata_value) > 256):
            raise ValueError("Invalid value for `metadata_value`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_value is not None and len(metadata_value) < 0):
            raise ValueError("Invalid value for `metadata_value`, length must be greater than or equal to `0`")  # noqa: E501

        self._metadata_value = metadata_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PropertyMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyMetadata):
            return True

        return self.to_dict() != other.to_dict()
