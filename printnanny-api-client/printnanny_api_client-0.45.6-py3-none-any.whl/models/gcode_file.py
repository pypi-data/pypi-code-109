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


class GcodeFile(object):
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
        'user': 'int',
        'name': 'str',
        'file': 'str',
        'file_hash': 'str',
        'octoprint_device': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'name': 'name',
        'file': 'file',
        'file_hash': 'file_hash',
        'octoprint_device': 'octoprint_device',
        'url': 'url'
    }

    def __init__(self, id=None, user=None, name=None, file=None, file_hash=None, octoprint_device=None, url=None, local_vars_configuration=None):  # noqa: E501
        """GcodeFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user = None
        self._name = None
        self._file = None
        self._file_hash = None
        self._octoprint_device = None
        self._url = None
        self.discriminator = None

        self.id = id
        self.user = user
        self.name = name
        self.file = file
        self.file_hash = file_hash
        self.octoprint_device = octoprint_device
        self.url = url

    @property
    def id(self):
        """Gets the id of this GcodeFile.  # noqa: E501


        :return: The id of this GcodeFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GcodeFile.


        :param id: The id of this GcodeFile.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user(self):
        """Gets the user of this GcodeFile.  # noqa: E501


        :return: The user of this GcodeFile.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GcodeFile.


        :param user: The user of this GcodeFile.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def name(self):
        """Gets the name of this GcodeFile.  # noqa: E501


        :return: The name of this GcodeFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GcodeFile.


        :param name: The name of this GcodeFile.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def file(self):
        """Gets the file of this GcodeFile.  # noqa: E501


        :return: The file of this GcodeFile.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this GcodeFile.


        :param file: The file of this GcodeFile.  # noqa: E501
        :type file: str
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def file_hash(self):
        """Gets the file_hash of this GcodeFile.  # noqa: E501


        :return: The file_hash of this GcodeFile.  # noqa: E501
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this GcodeFile.


        :param file_hash: The file_hash of this GcodeFile.  # noqa: E501
        :type file_hash: str
        """
        if self.local_vars_configuration.client_side_validation and file_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `file_hash`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_hash is not None and len(file_hash) > 255):
            raise ValueError("Invalid value for `file_hash`, length must be less than or equal to `255`")  # noqa: E501

        self._file_hash = file_hash

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this GcodeFile.  # noqa: E501


        :return: The octoprint_device of this GcodeFile.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this GcodeFile.


        :param octoprint_device: The octoprint_device of this GcodeFile.  # noqa: E501
        :type octoprint_device: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def url(self):
        """Gets the url of this GcodeFile.  # noqa: E501


        :return: The url of this GcodeFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GcodeFile.


        :param url: The url of this GcodeFile.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, GcodeFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GcodeFile):
            return True

        return self.to_dict() != other.to_dict()
