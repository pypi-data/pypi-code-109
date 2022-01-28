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


class CloudiotDevice(object):
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
        'num_id': 'int',
        'command_topic': 'str',
        'event_topic': 'str',
        'config_topic': 'str',
        'state_topic': 'str',
        'gcp_resource': 'str',
        'gcp_project_id': 'str',
        'gcp_region': 'str',
        'gcp_cloudiot_device_registry': 'str',
        'mqtt_bridge_hostname': 'str',
        'mqtt_bridge_port': 'int',
        'mqtt_client_id': 'str',
        'name': 'str',
        'id': 'str',
        'device': 'int'
    }

    attribute_map = {
        'num_id': 'num_id',
        'command_topic': 'command_topic',
        'event_topic': 'event_topic',
        'config_topic': 'config_topic',
        'state_topic': 'state_topic',
        'gcp_resource': 'gcp_resource',
        'gcp_project_id': 'gcp_project_id',
        'gcp_region': 'gcp_region',
        'gcp_cloudiot_device_registry': 'gcp_cloudiot_device_registry',
        'mqtt_bridge_hostname': 'mqtt_bridge_hostname',
        'mqtt_bridge_port': 'mqtt_bridge_port',
        'mqtt_client_id': 'mqtt_client_id',
        'name': 'name',
        'id': 'id',
        'device': 'device'
    }

    def __init__(self, num_id=None, command_topic=None, event_topic=None, config_topic=None, state_topic=None, gcp_resource=None, gcp_project_id=None, gcp_region=None, gcp_cloudiot_device_registry=None, mqtt_bridge_hostname=None, mqtt_bridge_port=None, mqtt_client_id=None, name=None, id=None, device=None, local_vars_configuration=None):  # noqa: E501
        """CloudiotDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._num_id = None
        self._command_topic = None
        self._event_topic = None
        self._config_topic = None
        self._state_topic = None
        self._gcp_resource = None
        self._gcp_project_id = None
        self._gcp_region = None
        self._gcp_cloudiot_device_registry = None
        self._mqtt_bridge_hostname = None
        self._mqtt_bridge_port = None
        self._mqtt_client_id = None
        self._name = None
        self._id = None
        self._device = None
        self.discriminator = None

        self.num_id = num_id
        self.command_topic = command_topic
        self.event_topic = event_topic
        self.config_topic = config_topic
        self.state_topic = state_topic
        self.gcp_resource = gcp_resource
        self.gcp_project_id = gcp_project_id
        self.gcp_region = gcp_region
        self.gcp_cloudiot_device_registry = gcp_cloudiot_device_registry
        self.mqtt_bridge_hostname = mqtt_bridge_hostname
        self.mqtt_bridge_port = mqtt_bridge_port
        self.mqtt_client_id = mqtt_client_id
        self.name = name
        self.id = id
        self.device = device

    @property
    def num_id(self):
        """Gets the num_id of this CloudiotDevice.  # noqa: E501


        :return: The num_id of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._num_id

    @num_id.setter
    def num_id(self, num_id):
        """Sets the num_id of this CloudiotDevice.


        :param num_id: The num_id of this CloudiotDevice.  # noqa: E501
        :type num_id: int
        """
        if self.local_vars_configuration.client_side_validation and num_id is None:  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_id is not None and num_id > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_id is not None and num_id < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._num_id = num_id

    @property
    def command_topic(self):
        """Gets the command_topic of this CloudiotDevice.  # noqa: E501


        :return: The command_topic of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._command_topic

    @command_topic.setter
    def command_topic(self, command_topic):
        """Sets the command_topic of this CloudiotDevice.


        :param command_topic: The command_topic of this CloudiotDevice.  # noqa: E501
        :type command_topic: str
        """
        if self.local_vars_configuration.client_side_validation and command_topic is None:  # noqa: E501
            raise ValueError("Invalid value for `command_topic`, must not be `None`")  # noqa: E501

        self._command_topic = command_topic

    @property
    def event_topic(self):
        """Gets the event_topic of this CloudiotDevice.  # noqa: E501


        :return: The event_topic of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._event_topic

    @event_topic.setter
    def event_topic(self, event_topic):
        """Sets the event_topic of this CloudiotDevice.


        :param event_topic: The event_topic of this CloudiotDevice.  # noqa: E501
        :type event_topic: str
        """
        if self.local_vars_configuration.client_side_validation and event_topic is None:  # noqa: E501
            raise ValueError("Invalid value for `event_topic`, must not be `None`")  # noqa: E501

        self._event_topic = event_topic

    @property
    def config_topic(self):
        """Gets the config_topic of this CloudiotDevice.  # noqa: E501


        :return: The config_topic of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._config_topic

    @config_topic.setter
    def config_topic(self, config_topic):
        """Sets the config_topic of this CloudiotDevice.


        :param config_topic: The config_topic of this CloudiotDevice.  # noqa: E501
        :type config_topic: str
        """
        if self.local_vars_configuration.client_side_validation and config_topic is None:  # noqa: E501
            raise ValueError("Invalid value for `config_topic`, must not be `None`")  # noqa: E501

        self._config_topic = config_topic

    @property
    def state_topic(self):
        """Gets the state_topic of this CloudiotDevice.  # noqa: E501


        :return: The state_topic of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._state_topic

    @state_topic.setter
    def state_topic(self, state_topic):
        """Sets the state_topic of this CloudiotDevice.


        :param state_topic: The state_topic of this CloudiotDevice.  # noqa: E501
        :type state_topic: str
        """
        if self.local_vars_configuration.client_side_validation and state_topic is None:  # noqa: E501
            raise ValueError("Invalid value for `state_topic`, must not be `None`")  # noqa: E501

        self._state_topic = state_topic

    @property
    def gcp_resource(self):
        """Gets the gcp_resource of this CloudiotDevice.  # noqa: E501


        :return: The gcp_resource of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_resource

    @gcp_resource.setter
    def gcp_resource(self, gcp_resource):
        """Sets the gcp_resource of this CloudiotDevice.


        :param gcp_resource: The gcp_resource of this CloudiotDevice.  # noqa: E501
        :type gcp_resource: str
        """
        if self.local_vars_configuration.client_side_validation and gcp_resource is None:  # noqa: E501
            raise ValueError("Invalid value for `gcp_resource`, must not be `None`")  # noqa: E501

        self._gcp_resource = gcp_resource

    @property
    def gcp_project_id(self):
        """Gets the gcp_project_id of this CloudiotDevice.  # noqa: E501


        :return: The gcp_project_id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_project_id

    @gcp_project_id.setter
    def gcp_project_id(self, gcp_project_id):
        """Sets the gcp_project_id of this CloudiotDevice.


        :param gcp_project_id: The gcp_project_id of this CloudiotDevice.  # noqa: E501
        :type gcp_project_id: str
        """
        if self.local_vars_configuration.client_side_validation and gcp_project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `gcp_project_id`, must not be `None`")  # noqa: E501

        self._gcp_project_id = gcp_project_id

    @property
    def gcp_region(self):
        """Gets the gcp_region of this CloudiotDevice.  # noqa: E501


        :return: The gcp_region of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_region

    @gcp_region.setter
    def gcp_region(self, gcp_region):
        """Sets the gcp_region of this CloudiotDevice.


        :param gcp_region: The gcp_region of this CloudiotDevice.  # noqa: E501
        :type gcp_region: str
        """
        if self.local_vars_configuration.client_side_validation and gcp_region is None:  # noqa: E501
            raise ValueError("Invalid value for `gcp_region`, must not be `None`")  # noqa: E501

        self._gcp_region = gcp_region

    @property
    def gcp_cloudiot_device_registry(self):
        """Gets the gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501


        :return: The gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_cloudiot_device_registry

    @gcp_cloudiot_device_registry.setter
    def gcp_cloudiot_device_registry(self, gcp_cloudiot_device_registry):
        """Sets the gcp_cloudiot_device_registry of this CloudiotDevice.


        :param gcp_cloudiot_device_registry: The gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501
        :type gcp_cloudiot_device_registry: str
        """
        if self.local_vars_configuration.client_side_validation and gcp_cloudiot_device_registry is None:  # noqa: E501
            raise ValueError("Invalid value for `gcp_cloudiot_device_registry`, must not be `None`")  # noqa: E501

        self._gcp_cloudiot_device_registry = gcp_cloudiot_device_registry

    @property
    def mqtt_bridge_hostname(self):
        """Gets the mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_bridge_hostname

    @mqtt_bridge_hostname.setter
    def mqtt_bridge_hostname(self, mqtt_bridge_hostname):
        """Sets the mqtt_bridge_hostname of this CloudiotDevice.


        :param mqtt_bridge_hostname: The mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501
        :type mqtt_bridge_hostname: str
        """
        if self.local_vars_configuration.client_side_validation and mqtt_bridge_hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `mqtt_bridge_hostname`, must not be `None`")  # noqa: E501

        self._mqtt_bridge_hostname = mqtt_bridge_hostname

    @property
    def mqtt_bridge_port(self):
        """Gets the mqtt_bridge_port of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_bridge_port of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._mqtt_bridge_port

    @mqtt_bridge_port.setter
    def mqtt_bridge_port(self, mqtt_bridge_port):
        """Sets the mqtt_bridge_port of this CloudiotDevice.


        :param mqtt_bridge_port: The mqtt_bridge_port of this CloudiotDevice.  # noqa: E501
        :type mqtt_bridge_port: int
        """
        if self.local_vars_configuration.client_side_validation and mqtt_bridge_port is None:  # noqa: E501
            raise ValueError("Invalid value for `mqtt_bridge_port`, must not be `None`")  # noqa: E501

        self._mqtt_bridge_port = mqtt_bridge_port

    @property
    def mqtt_client_id(self):
        """Gets the mqtt_client_id of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_client_id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_client_id

    @mqtt_client_id.setter
    def mqtt_client_id(self, mqtt_client_id):
        """Sets the mqtt_client_id of this CloudiotDevice.


        :param mqtt_client_id: The mqtt_client_id of this CloudiotDevice.  # noqa: E501
        :type mqtt_client_id: str
        """
        if self.local_vars_configuration.client_side_validation and mqtt_client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `mqtt_client_id`, must not be `None`")  # noqa: E501

        self._mqtt_client_id = mqtt_client_id

    @property
    def name(self):
        """Gets the name of this CloudiotDevice.  # noqa: E501


        :return: The name of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudiotDevice.


        :param name: The name of this CloudiotDevice.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this CloudiotDevice.  # noqa: E501


        :return: The id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudiotDevice.


        :param id: The id of this CloudiotDevice.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def device(self):
        """Gets the device of this CloudiotDevice.  # noqa: E501


        :return: The device of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this CloudiotDevice.


        :param device: The device of this CloudiotDevice.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

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
        if not isinstance(other, CloudiotDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudiotDevice):
            return True

        return self.to_dict() != other.to_dict()
