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


class PolymorphicEvent(object):
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
        'created_dt': 'datetime',
        'model': 'EventModel',
        'event_type': 'TestEventType',
        'status': 'EventStatus',
        'source': 'EventSource',
        'user': 'int',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'model': 'model',
        'event_type': 'event_type',
        'status': 'status',
        'source': 'source',
        'user': 'user',
        'device': 'device'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, id=None, created_dt=None, model=None, event_type=None, status=None, source=None, user=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PolymorphicEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._model = None
        self._event_type = None
        self._status = None
        self._source = None
        self._user = None
        self._device = None
        self.discriminator = 'model'

        self.id = id
        self.created_dt = created_dt
        self.model = model
        self.event_type = event_type
        if status is not None:
            self.status = status
        self.source = source
        self.user = user
        self.device = device

    @property
    def id(self):
        """Gets the id of this PolymorphicEvent.  # noqa: E501


        :return: The id of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolymorphicEvent.


        :param id: The id of this PolymorphicEvent.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PolymorphicEvent.  # noqa: E501


        :return: The created_dt of this PolymorphicEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PolymorphicEvent.


        :param created_dt: The created_dt of this PolymorphicEvent.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def model(self):
        """Gets the model of this PolymorphicEvent.  # noqa: E501


        :return: The model of this PolymorphicEvent.  # noqa: E501
        :rtype: EventModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PolymorphicEvent.


        :param model: The model of this PolymorphicEvent.  # noqa: E501
        :type model: EventModel
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def event_type(self):
        """Gets the event_type of this PolymorphicEvent.  # noqa: E501


        :return: The event_type of this PolymorphicEvent.  # noqa: E501
        :rtype: TestEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PolymorphicEvent.


        :param event_type: The event_type of this PolymorphicEvent.  # noqa: E501
        :type event_type: TestEventType
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def status(self):
        """Gets the status of this PolymorphicEvent.  # noqa: E501


        :return: The status of this PolymorphicEvent.  # noqa: E501
        :rtype: EventStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolymorphicEvent.


        :param status: The status of this PolymorphicEvent.  # noqa: E501
        :type status: EventStatus
        """

        self._status = status

    @property
    def source(self):
        """Gets the source of this PolymorphicEvent.  # noqa: E501


        :return: The source of this PolymorphicEvent.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PolymorphicEvent.


        :param source: The source of this PolymorphicEvent.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def user(self):
        """Gets the user of this PolymorphicEvent.  # noqa: E501


        :return: The user of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PolymorphicEvent.


        :param user: The user of this PolymorphicEvent.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def device(self):
        """Gets the device of this PolymorphicEvent.  # noqa: E501


        :return: The device of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PolymorphicEvent.


        :param device: The device of this PolymorphicEvent.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, PolymorphicEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolymorphicEvent):
            return True

        return self.to_dict() != other.to_dict()
