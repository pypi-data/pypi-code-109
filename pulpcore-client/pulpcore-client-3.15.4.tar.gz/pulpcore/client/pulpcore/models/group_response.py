# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class GroupResponse(object):
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
        'name': 'str',
        'pulp_href': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'pulp_href': 'pulp_href',
        'id': 'id'
    }

    def __init__(self, name=None, pulp_href=None, id=None, local_vars_configuration=None):  # noqa: E501
        """GroupResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._pulp_href = None
        self._id = None
        self.discriminator = None

        self.name = name
        if pulp_href is not None:
            self.pulp_href = pulp_href
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this GroupResponse.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupResponse.

        Name  # noqa: E501

        :param name: The name of this GroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 150):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")  # noqa: E501

        self._name = name

    @property
    def pulp_href(self):
        """Gets the pulp_href of this GroupResponse.  # noqa: E501


        :return: The pulp_href of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this GroupResponse.


        :param pulp_href: The pulp_href of this GroupResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def id(self):
        """Gets the id of this GroupResponse.  # noqa: E501


        :return: The id of this GroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupResponse.


        :param id: The id of this GroupResponse.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, GroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupResponse):
            return True

        return self.to_dict() != other.to_dict()
