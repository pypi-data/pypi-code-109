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


class ItemHierarchy(object):
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
        'item': 'Item',
        'derived_item': 'Item',
        'child_items': 'list[ItemHierarchy]',
        'element_id': 'int',
        'element_name': 'str',
        'sort_order': 'float',
        'derived_element_name': 'str'
    }

    attribute_map = {
        'item': 'item',
        'derived_item': 'derivedItem',
        'child_items': 'childItems',
        'element_id': 'elementId',
        'element_name': 'elementName',
        'sort_order': 'sortOrder',
        'derived_element_name': 'derivedElementName'
    }

    def __init__(self, item=None, derived_item=None, child_items=None, element_id=None, element_name=None, sort_order=None, derived_element_name=None, local_vars_configuration=None):  # noqa: E501
        """ItemHierarchy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item = None
        self._derived_item = None
        self._child_items = None
        self._element_id = None
        self._element_name = None
        self._sort_order = None
        self._derived_element_name = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if derived_item is not None:
            self.derived_item = derived_item
        if child_items is not None:
            self.child_items = child_items
        if element_id is not None:
            self.element_id = element_id
        if element_name is not None:
            self.element_name = element_name
        if sort_order is not None:
            self.sort_order = sort_order
        if derived_element_name is not None:
            self.derived_element_name = derived_element_name

    @property
    def item(self):
        """Gets the item of this ItemHierarchy.  # noqa: E501


        :return: The item of this ItemHierarchy.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this ItemHierarchy.


        :param item: The item of this ItemHierarchy.  # noqa: E501
        :type: Item
        """

        self._item = item

    @property
    def derived_item(self):
        """Gets the derived_item of this ItemHierarchy.  # noqa: E501


        :return: The derived_item of this ItemHierarchy.  # noqa: E501
        :rtype: Item
        """
        return self._derived_item

    @derived_item.setter
    def derived_item(self, derived_item):
        """Sets the derived_item of this ItemHierarchy.


        :param derived_item: The derived_item of this ItemHierarchy.  # noqa: E501
        :type: Item
        """

        self._derived_item = derived_item

    @property
    def child_items(self):
        """Gets the child_items of this ItemHierarchy.  # noqa: E501


        :return: The child_items of this ItemHierarchy.  # noqa: E501
        :rtype: list[ItemHierarchy]
        """
        return self._child_items

    @child_items.setter
    def child_items(self, child_items):
        """Sets the child_items of this ItemHierarchy.


        :param child_items: The child_items of this ItemHierarchy.  # noqa: E501
        :type: list[ItemHierarchy]
        """

        self._child_items = child_items

    @property
    def element_id(self):
        """Gets the element_id of this ItemHierarchy.  # noqa: E501


        :return: The element_id of this ItemHierarchy.  # noqa: E501
        :rtype: int
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this ItemHierarchy.


        :param element_id: The element_id of this ItemHierarchy.  # noqa: E501
        :type: int
        """

        self._element_id = element_id

    @property
    def element_name(self):
        """Gets the element_name of this ItemHierarchy.  # noqa: E501


        :return: The element_name of this ItemHierarchy.  # noqa: E501
        :rtype: str
        """
        return self._element_name

    @element_name.setter
    def element_name(self, element_name):
        """Sets the element_name of this ItemHierarchy.


        :param element_name: The element_name of this ItemHierarchy.  # noqa: E501
        :type: str
        """

        self._element_name = element_name

    @property
    def sort_order(self):
        """Gets the sort_order of this ItemHierarchy.  # noqa: E501


        :return: The sort_order of this ItemHierarchy.  # noqa: E501
        :rtype: float
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ItemHierarchy.


        :param sort_order: The sort_order of this ItemHierarchy.  # noqa: E501
        :type: float
        """

        self._sort_order = sort_order

    @property
    def derived_element_name(self):
        """Gets the derived_element_name of this ItemHierarchy.  # noqa: E501


        :return: The derived_element_name of this ItemHierarchy.  # noqa: E501
        :rtype: str
        """
        return self._derived_element_name

    @derived_element_name.setter
    def derived_element_name(self, derived_element_name):
        """Sets the derived_element_name of this ItemHierarchy.


        :param derived_element_name: The derived_element_name of this ItemHierarchy.  # noqa: E501
        :type: str
        """

        self._derived_element_name = derived_element_name

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
        if not isinstance(other, ItemHierarchy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemHierarchy):
            return True

        return self.to_dict() != other.to_dict()
