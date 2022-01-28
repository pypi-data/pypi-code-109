# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class OctoprintFile(object):
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
        'path': 'str',
        'display': 'str',
        'origin': 'str',
        'size': 'int',
        'date': 'int'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'display': 'display',
        'origin': 'origin',
        'size': 'size',
        'date': 'date'
    }

    def __init__(self, name=None, path=None, display=None, origin=None, size=None, date=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._path = None
        self._display = None
        self._origin = None
        self._size = None
        self._date = None
        self.discriminator = None

        self.name = name
        self.path = path
        self.display = display
        self.origin = origin
        self.size = size
        self.date = date

    @property
    def name(self):
        """Gets the name of this OctoprintFile.  # noqa: E501


        :return: The name of this OctoprintFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoprintFile.


        :param name: The name of this OctoprintFile.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this OctoprintFile.  # noqa: E501


        :return: The path of this OctoprintFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OctoprintFile.


        :param path: The path of this OctoprintFile.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def display(self):
        """Gets the display of this OctoprintFile.  # noqa: E501


        :return: The display of this OctoprintFile.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this OctoprintFile.


        :param display: The display of this OctoprintFile.  # noqa: E501
        :type display: str
        """

        self._display = display

    @property
    def origin(self):
        """Gets the origin of this OctoprintFile.  # noqa: E501


        :return: The origin of this OctoprintFile.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OctoprintFile.


        :param origin: The origin of this OctoprintFile.  # noqa: E501
        :type origin: str
        """

        self._origin = origin

    @property
    def size(self):
        """Gets the size of this OctoprintFile.  # noqa: E501


        :return: The size of this OctoprintFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OctoprintFile.


        :param size: The size of this OctoprintFile.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def date(self):
        """Gets the date of this OctoprintFile.  # noqa: E501


        :return: The date of this OctoprintFile.  # noqa: E501
        :rtype: int
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this OctoprintFile.


        :param date: The date of this OctoprintFile.  # noqa: E501
        :type date: int
        """

        self._date = date

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
        if not isinstance(other, OctoprintFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintFile):
            return True

        return self.to_dict() != other.to_dict()
