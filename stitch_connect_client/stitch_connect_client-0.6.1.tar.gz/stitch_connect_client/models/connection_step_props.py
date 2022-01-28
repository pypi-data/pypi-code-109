# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class ConnectionStepProps(object):
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
        "name": "str",
        "is_required": "bool",
        "is_credential": "bool",
        "property_type": "str",
        "json_schema": "list[ConnectionStepPropsJsonSchema]",
        "provided": "bool",
    }

    attribute_map = {
        "name": "name",
        "is_required": "is_required",
        "is_credential": "is_credential",
        "property_type": "property_type",
        "json_schema": "json_schema",
        "provided": "provided",
    }

    def __init__(
        self,
        name=None,
        is_required=None,
        is_credential=None,
        property_type=None,
        json_schema=None,
        provided=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ConnectionStepProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_required = None
        self._is_credential = None
        self._property_type = None
        self._json_schema = None
        self._provided = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_required is not None:
            self.is_required = is_required
        if is_credential is not None:
            self.is_credential = is_credential
        if property_type is not None:
            self.property_type = property_type
        if json_schema is not None:
            self.json_schema = json_schema
        if provided is not None:
            self.provided = provided

    @property
    def name(self):
        """Gets the name of this ConnectionStepProps.  # noqa: E501

        The name of the property.  # noqa: E501

        :return: The name of this ConnectionStepProps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionStepProps.

        The name of the property.  # noqa: E501

        :param name: The name of this ConnectionStepProps.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_required(self):
        """Gets the is_required of this ConnectionStepProps.  # noqa: E501

        If true, the property is required for complete configuration.  # noqa: E501

        :return: The is_required of this ConnectionStepProps.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this ConnectionStepProps.

        If true, the property is required for complete configuration.  # noqa: E501

        :param is_required: The is_required of this ConnectionStepProps.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def is_credential(self):
        """Gets the is_credential of this ConnectionStepProps.  # noqa: E501

        If true, the property is a credential or otherwise sensitive data.   # noqa: E501

        :return: The is_credential of this ConnectionStepProps.  # noqa: E501
        :rtype: bool
        """
        return self._is_credential

    @is_credential.setter
    def is_credential(self, is_credential):
        """Sets the is_credential of this ConnectionStepProps.

        If true, the property is a credential or otherwise sensitive data.   # noqa: E501

        :param is_credential: The is_credential of this ConnectionStepProps.  # noqa: E501
        :type: bool
        """

        self._is_credential = is_credential

    @property
    def property_type(self):
        """Gets the property_type of this ConnectionStepProps.  # noqa: E501

        Indicates the type of the property. Possible values are: user_provided - Indicates the property must be set by the user. read_only - Indicates the property is read-only and is not settable by the Generally, this is an internal field set inside of Stitch. system_provided_by_default - Indicates the property used to be system_provided: true, but can now be set by the API consumer. These are generally properties associated with OAuth for generating refresh and access tokens. user_provided_advanced - Indicates the property is set by the user but may be configured by the Stitch support team in the event that the integration is failing to work properly. Note: Use caution when setting these properties, as using incorrect values can put the source into a non-functioning state.   # noqa: E501

        :return: The property_type of this ConnectionStepProps.  # noqa: E501
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """Sets the property_type of this ConnectionStepProps.

        Indicates the type of the property. Possible values are: user_provided - Indicates the property must be set by the user. read_only - Indicates the property is read-only and is not settable by the Generally, this is an internal field set inside of Stitch. system_provided_by_default - Indicates the property used to be system_provided: true, but can now be set by the API consumer. These are generally properties associated with OAuth for generating refresh and access tokens. user_provided_advanced - Indicates the property is set by the user but may be configured by the Stitch support team in the event that the integration is failing to work properly. Note: Use caution when setting these properties, as using incorrect values can put the source into a non-functioning state.   # noqa: E501

        :param property_type: The property_type of this ConnectionStepProps.  # noqa: E501
        :type: str
        """

        self._property_type = property_type

    @property
    def json_schema(self):
        """Gets the json_schema of this ConnectionStepProps.  # noqa: E501

        Note: Data will only be returned for this array if property_type: user_provided or property_type: system_provided_by_default. If property_type: read_only, this property will be null. An array containing: type - A string indicating the expected data type of the property's value. For example: boolean pattern - A string indicating the expected pattern of the property's value. For example: ^\\\\d+$ anyOf - A series of arrays containing key-value pairs for the type and format combinations Stitch will accept as the property's value   # noqa: E501

        :return: The json_schema of this ConnectionStepProps.  # noqa: E501
        :rtype: list[ConnectionStepPropsJsonSchema]
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        """Sets the json_schema of this ConnectionStepProps.

        Note: Data will only be returned for this array if property_type: user_provided or property_type: system_provided_by_default. If property_type: read_only, this property will be null. An array containing: type - A string indicating the expected data type of the property's value. For example: boolean pattern - A string indicating the expected pattern of the property's value. For example: ^\\\\d+$ anyOf - A series of arrays containing key-value pairs for the type and format combinations Stitch will accept as the property's value   # noqa: E501

        :param json_schema: The json_schema of this ConnectionStepProps.  # noqa: E501
        :type: list[ConnectionStepPropsJsonSchema]
        """

        self._json_schema = json_schema

    @property
    def provided(self):
        """Gets the provided of this ConnectionStepProps.  # noqa: E501

        If true, the property has been provided. For properties where property_type: user_provided, this indicates that the user has provided the property.   # noqa: E501

        :return: The provided of this ConnectionStepProps.  # noqa: E501
        :rtype: bool
        """
        return self._provided

    @provided.setter
    def provided(self, provided):
        """Sets the provided of this ConnectionStepProps.

        If true, the property has been provided. For properties where property_type: user_provided, this indicates that the user has provided the property.   # noqa: E501

        :param provided: The provided of this ConnectionStepProps.  # noqa: E501
        :type: bool
        """

        self._provided = provided

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, ConnectionStepProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionStepProps):
            return True

        return self.to_dict() != other.to_dict()
