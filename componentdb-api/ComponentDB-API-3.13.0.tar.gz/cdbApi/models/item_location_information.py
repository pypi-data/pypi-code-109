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


class ItemLocationInformation(object):
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
        'locatable_item': 'LocatableItem',
        'location_item': 'ItemDomainLocation',
        'housing_item': 'Item',
        'location_string': 'str',
        'location_details': 'str',
        'housing_string': 'str',
        'location_single_node_hierarchy': 'ItemHierarchy',
        'housing_single_node_hierarchy': 'ItemHierarchy'
    }

    attribute_map = {
        'locatable_item': 'locatableItem',
        'location_item': 'locationItem',
        'housing_item': 'housingItem',
        'location_string': 'locationString',
        'location_details': 'locationDetails',
        'housing_string': 'housingString',
        'location_single_node_hierarchy': 'locationSingleNodeHierarchy',
        'housing_single_node_hierarchy': 'housingSingleNodeHierarchy'
    }

    def __init__(self, locatable_item=None, location_item=None, housing_item=None, location_string=None, location_details=None, housing_string=None, location_single_node_hierarchy=None, housing_single_node_hierarchy=None, local_vars_configuration=None):  # noqa: E501
        """ItemLocationInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locatable_item = None
        self._location_item = None
        self._housing_item = None
        self._location_string = None
        self._location_details = None
        self._housing_string = None
        self._location_single_node_hierarchy = None
        self._housing_single_node_hierarchy = None
        self.discriminator = None

        if locatable_item is not None:
            self.locatable_item = locatable_item
        if location_item is not None:
            self.location_item = location_item
        if housing_item is not None:
            self.housing_item = housing_item
        if location_string is not None:
            self.location_string = location_string
        if location_details is not None:
            self.location_details = location_details
        if housing_string is not None:
            self.housing_string = housing_string
        if location_single_node_hierarchy is not None:
            self.location_single_node_hierarchy = location_single_node_hierarchy
        if housing_single_node_hierarchy is not None:
            self.housing_single_node_hierarchy = housing_single_node_hierarchy

    @property
    def locatable_item(self):
        """Gets the locatable_item of this ItemLocationInformation.  # noqa: E501


        :return: The locatable_item of this ItemLocationInformation.  # noqa: E501
        :rtype: LocatableItem
        """
        return self._locatable_item

    @locatable_item.setter
    def locatable_item(self, locatable_item):
        """Sets the locatable_item of this ItemLocationInformation.


        :param locatable_item: The locatable_item of this ItemLocationInformation.  # noqa: E501
        :type: LocatableItem
        """

        self._locatable_item = locatable_item

    @property
    def location_item(self):
        """Gets the location_item of this ItemLocationInformation.  # noqa: E501


        :return: The location_item of this ItemLocationInformation.  # noqa: E501
        :rtype: ItemDomainLocation
        """
        return self._location_item

    @location_item.setter
    def location_item(self, location_item):
        """Sets the location_item of this ItemLocationInformation.


        :param location_item: The location_item of this ItemLocationInformation.  # noqa: E501
        :type: ItemDomainLocation
        """

        self._location_item = location_item

    @property
    def housing_item(self):
        """Gets the housing_item of this ItemLocationInformation.  # noqa: E501


        :return: The housing_item of this ItemLocationInformation.  # noqa: E501
        :rtype: Item
        """
        return self._housing_item

    @housing_item.setter
    def housing_item(self, housing_item):
        """Sets the housing_item of this ItemLocationInformation.


        :param housing_item: The housing_item of this ItemLocationInformation.  # noqa: E501
        :type: Item
        """

        self._housing_item = housing_item

    @property
    def location_string(self):
        """Gets the location_string of this ItemLocationInformation.  # noqa: E501


        :return: The location_string of this ItemLocationInformation.  # noqa: E501
        :rtype: str
        """
        return self._location_string

    @location_string.setter
    def location_string(self, location_string):
        """Sets the location_string of this ItemLocationInformation.


        :param location_string: The location_string of this ItemLocationInformation.  # noqa: E501
        :type: str
        """

        self._location_string = location_string

    @property
    def location_details(self):
        """Gets the location_details of this ItemLocationInformation.  # noqa: E501


        :return: The location_details of this ItemLocationInformation.  # noqa: E501
        :rtype: str
        """
        return self._location_details

    @location_details.setter
    def location_details(self, location_details):
        """Sets the location_details of this ItemLocationInformation.


        :param location_details: The location_details of this ItemLocationInformation.  # noqa: E501
        :type: str
        """

        self._location_details = location_details

    @property
    def housing_string(self):
        """Gets the housing_string of this ItemLocationInformation.  # noqa: E501


        :return: The housing_string of this ItemLocationInformation.  # noqa: E501
        :rtype: str
        """
        return self._housing_string

    @housing_string.setter
    def housing_string(self, housing_string):
        """Sets the housing_string of this ItemLocationInformation.


        :param housing_string: The housing_string of this ItemLocationInformation.  # noqa: E501
        :type: str
        """

        self._housing_string = housing_string

    @property
    def location_single_node_hierarchy(self):
        """Gets the location_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501


        :return: The location_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501
        :rtype: ItemHierarchy
        """
        return self._location_single_node_hierarchy

    @location_single_node_hierarchy.setter
    def location_single_node_hierarchy(self, location_single_node_hierarchy):
        """Sets the location_single_node_hierarchy of this ItemLocationInformation.


        :param location_single_node_hierarchy: The location_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501
        :type: ItemHierarchy
        """

        self._location_single_node_hierarchy = location_single_node_hierarchy

    @property
    def housing_single_node_hierarchy(self):
        """Gets the housing_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501


        :return: The housing_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501
        :rtype: ItemHierarchy
        """
        return self._housing_single_node_hierarchy

    @housing_single_node_hierarchy.setter
    def housing_single_node_hierarchy(self, housing_single_node_hierarchy):
        """Sets the housing_single_node_hierarchy of this ItemLocationInformation.


        :param housing_single_node_hierarchy: The housing_single_node_hierarchy of this ItemLocationInformation.  # noqa: E501
        :type: ItemHierarchy
        """

        self._housing_single_node_hierarchy = housing_single_node_hierarchy

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
        if not isinstance(other, ItemLocationInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemLocationInformation):
            return True

        return self.to_dict() != other.to_dict()
