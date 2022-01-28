# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3919
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


class DateAttributes(object):
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
        'irregular': 'bool',
        'irregular_session': 'bool',
        'new_hours': 'bool',
        'activity': 'str',
        'first_open': 'str',
        'last_open': 'str',
        'first_close': 'str',
        'last_close': 'str'
    }

    attribute_map = {
        'irregular': 'irregular',
        'irregular_session': 'irregularSession',
        'new_hours': 'newHours',
        'activity': 'activity',
        'first_open': 'firstOpen',
        'last_open': 'lastOpen',
        'first_close': 'firstClose',
        'last_close': 'lastClose'
    }

    required_map = {
        'irregular': 'required',
        'irregular_session': 'required',
        'new_hours': 'required',
        'activity': 'optional',
        'first_open': 'optional',
        'last_open': 'optional',
        'first_close': 'optional',
        'last_close': 'optional'
    }

    def __init__(self, irregular=None, irregular_session=None, new_hours=None, activity=None, first_open=None, last_open=None, first_close=None, last_close=None, local_vars_configuration=None):  # noqa: E501
        """DateAttributes - a model defined in OpenAPI"
        
        :param irregular:  (required)
        :type irregular: bool
        :param irregular_session:  (required)
        :type irregular_session: bool
        :param new_hours:  (required)
        :type new_hours: bool
        :param activity: 
        :type activity: str
        :param first_open: 
        :type first_open: str
        :param last_open: 
        :type last_open: str
        :param first_close: 
        :type first_close: str
        :param last_close: 
        :type last_close: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._irregular = None
        self._irregular_session = None
        self._new_hours = None
        self._activity = None
        self._first_open = None
        self._last_open = None
        self._first_close = None
        self._last_close = None
        self.discriminator = None

        self.irregular = irregular
        self.irregular_session = irregular_session
        self.new_hours = new_hours
        self.activity = activity
        self.first_open = first_open
        self.last_open = last_open
        self.first_close = first_close
        self.last_close = last_close

    @property
    def irregular(self):
        """Gets the irregular of this DateAttributes.  # noqa: E501


        :return: The irregular of this DateAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._irregular

    @irregular.setter
    def irregular(self, irregular):
        """Sets the irregular of this DateAttributes.


        :param irregular: The irregular of this DateAttributes.  # noqa: E501
        :type irregular: bool
        """
        if self.local_vars_configuration.client_side_validation and irregular is None:  # noqa: E501
            raise ValueError("Invalid value for `irregular`, must not be `None`")  # noqa: E501

        self._irregular = irregular

    @property
    def irregular_session(self):
        """Gets the irregular_session of this DateAttributes.  # noqa: E501


        :return: The irregular_session of this DateAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._irregular_session

    @irregular_session.setter
    def irregular_session(self, irregular_session):
        """Sets the irregular_session of this DateAttributes.


        :param irregular_session: The irregular_session of this DateAttributes.  # noqa: E501
        :type irregular_session: bool
        """
        if self.local_vars_configuration.client_side_validation and irregular_session is None:  # noqa: E501
            raise ValueError("Invalid value for `irregular_session`, must not be `None`")  # noqa: E501

        self._irregular_session = irregular_session

    @property
    def new_hours(self):
        """Gets the new_hours of this DateAttributes.  # noqa: E501


        :return: The new_hours of this DateAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._new_hours

    @new_hours.setter
    def new_hours(self, new_hours):
        """Sets the new_hours of this DateAttributes.


        :param new_hours: The new_hours of this DateAttributes.  # noqa: E501
        :type new_hours: bool
        """
        if self.local_vars_configuration.client_side_validation and new_hours is None:  # noqa: E501
            raise ValueError("Invalid value for `new_hours`, must not be `None`")  # noqa: E501

        self._new_hours = new_hours

    @property
    def activity(self):
        """Gets the activity of this DateAttributes.  # noqa: E501


        :return: The activity of this DateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this DateAttributes.


        :param activity: The activity of this DateAttributes.  # noqa: E501
        :type activity: str
        """
        if (self.local_vars_configuration.client_side_validation and
                activity is not None and len(activity) > 100):
            raise ValueError("Invalid value for `activity`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                activity is not None and len(activity) < 0):
            raise ValueError("Invalid value for `activity`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                activity is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', activity)):  # noqa: E501
            raise ValueError(r"Invalid value for `activity`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._activity = activity

    @property
    def first_open(self):
        """Gets the first_open of this DateAttributes.  # noqa: E501


        :return: The first_open of this DateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._first_open

    @first_open.setter
    def first_open(self, first_open):
        """Sets the first_open of this DateAttributes.


        :param first_open: The first_open of this DateAttributes.  # noqa: E501
        :type first_open: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_open is not None and len(first_open) > 100):
            raise ValueError("Invalid value for `first_open`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_open is not None and len(first_open) < 0):
            raise ValueError("Invalid value for `first_open`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_open is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', first_open)):  # noqa: E501
            raise ValueError(r"Invalid value for `first_open`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._first_open = first_open

    @property
    def last_open(self):
        """Gets the last_open of this DateAttributes.  # noqa: E501


        :return: The last_open of this DateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._last_open

    @last_open.setter
    def last_open(self, last_open):
        """Sets the last_open of this DateAttributes.


        :param last_open: The last_open of this DateAttributes.  # noqa: E501
        :type last_open: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_open is not None and len(last_open) > 100):
            raise ValueError("Invalid value for `last_open`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_open is not None and len(last_open) < 0):
            raise ValueError("Invalid value for `last_open`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_open is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', last_open)):  # noqa: E501
            raise ValueError(r"Invalid value for `last_open`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._last_open = last_open

    @property
    def first_close(self):
        """Gets the first_close of this DateAttributes.  # noqa: E501


        :return: The first_close of this DateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._first_close

    @first_close.setter
    def first_close(self, first_close):
        """Sets the first_close of this DateAttributes.


        :param first_close: The first_close of this DateAttributes.  # noqa: E501
        :type first_close: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_close is not None and len(first_close) > 100):
            raise ValueError("Invalid value for `first_close`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_close is not None and len(first_close) < 0):
            raise ValueError("Invalid value for `first_close`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_close is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', first_close)):  # noqa: E501
            raise ValueError(r"Invalid value for `first_close`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._first_close = first_close

    @property
    def last_close(self):
        """Gets the last_close of this DateAttributes.  # noqa: E501


        :return: The last_close of this DateAttributes.  # noqa: E501
        :rtype: str
        """
        return self._last_close

    @last_close.setter
    def last_close(self, last_close):
        """Sets the last_close of this DateAttributes.


        :param last_close: The last_close of this DateAttributes.  # noqa: E501
        :type last_close: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_close is not None and len(last_close) > 100):
            raise ValueError("Invalid value for `last_close`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_close is not None and len(last_close) < 0):
            raise ValueError("Invalid value for `last_close`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_close is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', last_close)):  # noqa: E501
            raise ValueError(r"Invalid value for `last_close`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._last_close = last_close

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
        if not isinstance(other, DateAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateAttributes):
            return True

        return self.to_dict() != other.to_dict()
