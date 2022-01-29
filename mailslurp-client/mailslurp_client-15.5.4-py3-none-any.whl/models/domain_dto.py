# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class DomainDto(object):
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
        'id': 'str',
        'user_id': 'str',
        'domain': 'str',
        'verification_token': 'str',
        'dkim_tokens': 'list[str]',
        'is_verified': 'bool',
        'domain_name_records': 'list[DomainNameRecord]',
        'catch_all_inbox_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'domain': 'domain',
        'verification_token': 'verificationToken',
        'dkim_tokens': 'dkimTokens',
        'is_verified': 'isVerified',
        'domain_name_records': 'domainNameRecords',
        'catch_all_inbox_id': 'catchAllInboxId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'domain_type': 'domainType'
    }

    def __init__(self, id=None, user_id=None, domain=None, verification_token=None, dkim_tokens=None, is_verified=None, domain_name_records=None, catch_all_inbox_id=None, created_at=None, updated_at=None, domain_type=None, local_vars_configuration=None):  # noqa: E501
        """DomainDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._domain = None
        self._verification_token = None
        self._dkim_tokens = None
        self._is_verified = None
        self._domain_name_records = None
        self._catch_all_inbox_id = None
        self._created_at = None
        self._updated_at = None
        self._domain_type = None
        self.discriminator = None

        self.id = id
        self.user_id = user_id
        self.domain = domain
        self.verification_token = verification_token
        self.dkim_tokens = dkim_tokens
        self.is_verified = is_verified
        self.domain_name_records = domain_name_records
        if catch_all_inbox_id is not None:
            self.catch_all_inbox_id = catch_all_inbox_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.domain_type = domain_type

    @property
    def id(self):
        """Gets the id of this DomainDto.  # noqa: E501


        :return: The id of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainDto.


        :param id: The id of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this DomainDto.  # noqa: E501


        :return: The user_id of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DomainDto.


        :param user_id: The user_id of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def domain(self):
        """Gets the domain of this DomainDto.  # noqa: E501

        Custom domain name  # noqa: E501

        :return: The domain of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainDto.

        Custom domain name  # noqa: E501

        :param domain: The domain of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def verification_token(self):
        """Gets the verification_token of this DomainDto.  # noqa: E501

        Verification tokens  # noqa: E501

        :return: The verification_token of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._verification_token

    @verification_token.setter
    def verification_token(self, verification_token):
        """Sets the verification_token of this DomainDto.

        Verification tokens  # noqa: E501

        :param verification_token: The verification_token of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and verification_token is None:  # noqa: E501
            raise ValueError("Invalid value for `verification_token`, must not be `None`")  # noqa: E501

        self._verification_token = verification_token

    @property
    def dkim_tokens(self):
        """Gets the dkim_tokens of this DomainDto.  # noqa: E501

        Unique token DKIM tokens  # noqa: E501

        :return: The dkim_tokens of this DomainDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._dkim_tokens

    @dkim_tokens.setter
    def dkim_tokens(self, dkim_tokens):
        """Sets the dkim_tokens of this DomainDto.

        Unique token DKIM tokens  # noqa: E501

        :param dkim_tokens: The dkim_tokens of this DomainDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and dkim_tokens is None:  # noqa: E501
            raise ValueError("Invalid value for `dkim_tokens`, must not be `None`")  # noqa: E501

        self._dkim_tokens = dkim_tokens

    @property
    def is_verified(self):
        """Gets the is_verified of this DomainDto.  # noqa: E501

        Whether domain has been verified or not. If the domain is not verified after 72 hours there is most likely an issue with the domains DNS records.  # noqa: E501

        :return: The is_verified of this DomainDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this DomainDto.

        Whether domain has been verified or not. If the domain is not verified after 72 hours there is most likely an issue with the domains DNS records.  # noqa: E501

        :param is_verified: The is_verified of this DomainDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_verified is None:  # noqa: E501
            raise ValueError("Invalid value for `is_verified`, must not be `None`")  # noqa: E501

        self._is_verified = is_verified

    @property
    def domain_name_records(self):
        """Gets the domain_name_records of this DomainDto.  # noqa: E501

        List of DNS domain name records (C, MX, TXT) etc that you must add to the DNS server associated with your domain provider.  # noqa: E501

        :return: The domain_name_records of this DomainDto.  # noqa: E501
        :rtype: list[DomainNameRecord]
        """
        return self._domain_name_records

    @domain_name_records.setter
    def domain_name_records(self, domain_name_records):
        """Sets the domain_name_records of this DomainDto.

        List of DNS domain name records (C, MX, TXT) etc that you must add to the DNS server associated with your domain provider.  # noqa: E501

        :param domain_name_records: The domain_name_records of this DomainDto.  # noqa: E501
        :type: list[DomainNameRecord]
        """
        if self.local_vars_configuration.client_side_validation and domain_name_records is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_name_records`, must not be `None`")  # noqa: E501

        self._domain_name_records = domain_name_records

    @property
    def catch_all_inbox_id(self):
        """Gets the catch_all_inbox_id of this DomainDto.  # noqa: E501

        The optional catch all inbox that will receive emails sent to the domain that cannot be matched.  # noqa: E501

        :return: The catch_all_inbox_id of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._catch_all_inbox_id

    @catch_all_inbox_id.setter
    def catch_all_inbox_id(self, catch_all_inbox_id):
        """Sets the catch_all_inbox_id of this DomainDto.

        The optional catch all inbox that will receive emails sent to the domain that cannot be matched.  # noqa: E501

        :param catch_all_inbox_id: The catch_all_inbox_id of this DomainDto.  # noqa: E501
        :type: str
        """

        self._catch_all_inbox_id = catch_all_inbox_id

    @property
    def created_at(self):
        """Gets the created_at of this DomainDto.  # noqa: E501


        :return: The created_at of this DomainDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DomainDto.


        :param created_at: The created_at of this DomainDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainDto.  # noqa: E501


        :return: The updated_at of this DomainDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainDto.


        :param updated_at: The updated_at of this DomainDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def domain_type(self):
        """Gets the domain_type of this DomainDto.  # noqa: E501

        Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails.  # noqa: E501

        :return: The domain_type of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this DomainDto.

        Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails.  # noqa: E501

        :param domain_type: The domain_type of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain_type is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_type`, must not be `None`")  # noqa: E501
        allowed_values = ["HTTP_INBOX", "SMTP_DOMAIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and domain_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `domain_type` ({0}), must be one of {1}"  # noqa: E501
                .format(domain_type, allowed_values)
            )

        self._domain_type = domain_type

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
        if not isinstance(other, DomainDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainDto):
            return True

        return self.to_dict() != other.to_dict()
