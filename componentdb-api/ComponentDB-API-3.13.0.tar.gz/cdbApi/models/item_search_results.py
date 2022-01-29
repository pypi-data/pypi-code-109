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


class ItemSearchResults(object):
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
        'item_domain_catalog_results': 'list[SearchResult]',
        'item_domain_inventory_results': 'list[SearchResult]',
        'item_domain_machine_design_results': 'list[SearchResult]'
    }

    attribute_map = {
        'item_domain_catalog_results': 'itemDomainCatalogResults',
        'item_domain_inventory_results': 'itemDomainInventoryResults',
        'item_domain_machine_design_results': 'itemDomainMachineDesignResults'
    }

    def __init__(self, item_domain_catalog_results=None, item_domain_inventory_results=None, item_domain_machine_design_results=None, local_vars_configuration=None):  # noqa: E501
        """ItemSearchResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_domain_catalog_results = None
        self._item_domain_inventory_results = None
        self._item_domain_machine_design_results = None
        self.discriminator = None

        if item_domain_catalog_results is not None:
            self.item_domain_catalog_results = item_domain_catalog_results
        if item_domain_inventory_results is not None:
            self.item_domain_inventory_results = item_domain_inventory_results
        if item_domain_machine_design_results is not None:
            self.item_domain_machine_design_results = item_domain_machine_design_results

    @property
    def item_domain_catalog_results(self):
        """Gets the item_domain_catalog_results of this ItemSearchResults.  # noqa: E501


        :return: The item_domain_catalog_results of this ItemSearchResults.  # noqa: E501
        :rtype: list[SearchResult]
        """
        return self._item_domain_catalog_results

    @item_domain_catalog_results.setter
    def item_domain_catalog_results(self, item_domain_catalog_results):
        """Sets the item_domain_catalog_results of this ItemSearchResults.


        :param item_domain_catalog_results: The item_domain_catalog_results of this ItemSearchResults.  # noqa: E501
        :type: list[SearchResult]
        """

        self._item_domain_catalog_results = item_domain_catalog_results

    @property
    def item_domain_inventory_results(self):
        """Gets the item_domain_inventory_results of this ItemSearchResults.  # noqa: E501


        :return: The item_domain_inventory_results of this ItemSearchResults.  # noqa: E501
        :rtype: list[SearchResult]
        """
        return self._item_domain_inventory_results

    @item_domain_inventory_results.setter
    def item_domain_inventory_results(self, item_domain_inventory_results):
        """Sets the item_domain_inventory_results of this ItemSearchResults.


        :param item_domain_inventory_results: The item_domain_inventory_results of this ItemSearchResults.  # noqa: E501
        :type: list[SearchResult]
        """

        self._item_domain_inventory_results = item_domain_inventory_results

    @property
    def item_domain_machine_design_results(self):
        """Gets the item_domain_machine_design_results of this ItemSearchResults.  # noqa: E501


        :return: The item_domain_machine_design_results of this ItemSearchResults.  # noqa: E501
        :rtype: list[SearchResult]
        """
        return self._item_domain_machine_design_results

    @item_domain_machine_design_results.setter
    def item_domain_machine_design_results(self, item_domain_machine_design_results):
        """Sets the item_domain_machine_design_results of this ItemSearchResults.


        :param item_domain_machine_design_results: The item_domain_machine_design_results of this ItemSearchResults.  # noqa: E501
        :type: list[SearchResult]
        """

        self._item_domain_machine_design_results = item_domain_machine_design_results

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
        if not isinstance(other, ItemSearchResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemSearchResults):
            return True

        return self.to_dict() != other.to_dict()
