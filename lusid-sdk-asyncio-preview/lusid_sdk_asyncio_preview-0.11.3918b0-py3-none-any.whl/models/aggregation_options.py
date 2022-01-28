# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3918
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_asyncio.configuration import Configuration


class AggregationOptions(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'use_ansi_like_syntax': 'bool',
        'allow_partial_entitlement_success': 'bool'
    }

    attribute_map = {
        'use_ansi_like_syntax': 'useAnsiLikeSyntax',
        'allow_partial_entitlement_success': 'allowPartialEntitlementSuccess'
    }

    required_map = {
        'use_ansi_like_syntax': 'optional',
        'allow_partial_entitlement_success': 'optional'
    }

    def __init__(self, use_ansi_like_syntax=None, allow_partial_entitlement_success=None, local_vars_configuration=None):  # noqa: E501
        """AggregationOptions - a model defined in OpenAPI"
        
        :param use_ansi_like_syntax:  Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).
        :type use_ansi_like_syntax: bool
        :param allow_partial_entitlement_success:  In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded.
        :type allow_partial_entitlement_success: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._use_ansi_like_syntax = None
        self._allow_partial_entitlement_success = None
        self.discriminator = None

        if use_ansi_like_syntax is not None:
            self.use_ansi_like_syntax = use_ansi_like_syntax
        if allow_partial_entitlement_success is not None:
            self.allow_partial_entitlement_success = allow_partial_entitlement_success

    @property
    def use_ansi_like_syntax(self):
        """Gets the use_ansi_like_syntax of this AggregationOptions.  # noqa: E501

        Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).  # noqa: E501

        :return: The use_ansi_like_syntax of this AggregationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_ansi_like_syntax

    @use_ansi_like_syntax.setter
    def use_ansi_like_syntax(self, use_ansi_like_syntax):
        """Sets the use_ansi_like_syntax of this AggregationOptions.

        Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).  # noqa: E501

        :param use_ansi_like_syntax: The use_ansi_like_syntax of this AggregationOptions.  # noqa: E501
        :type use_ansi_like_syntax: bool
        """

        self._use_ansi_like_syntax = use_ansi_like_syntax

    @property
    def allow_partial_entitlement_success(self):
        """Gets the allow_partial_entitlement_success of this AggregationOptions.  # noqa: E501

        In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded.  # noqa: E501

        :return: The allow_partial_entitlement_success of this AggregationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partial_entitlement_success

    @allow_partial_entitlement_success.setter
    def allow_partial_entitlement_success(self, allow_partial_entitlement_success):
        """Sets the allow_partial_entitlement_success of this AggregationOptions.

        In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded.  # noqa: E501

        :param allow_partial_entitlement_success: The allow_partial_entitlement_success of this AggregationOptions.  # noqa: E501
        :type allow_partial_entitlement_success: bool
        """

        self._allow_partial_entitlement_success = allow_partial_entitlement_success

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AggregationOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregationOptions):
            return True

        return self.to_dict() != other.to_dict()
