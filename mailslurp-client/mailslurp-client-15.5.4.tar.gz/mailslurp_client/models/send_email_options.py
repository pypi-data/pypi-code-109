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


class SendEmailOptions(object):
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
        'to_contacts': 'list[str]',
        'to_group': 'str',
        'to': 'list[str]',
        '_from': 'str',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'subject': 'str',
        'reply_to': 'str',
        'body': 'str',
        'html': 'bool',
        'is_html': 'bool',
        'charset': 'str',
        'attachments': 'list[str]',
        'template_variables': 'dict(str, object)',
        'template': 'str',
        'send_strategy': 'str',
        'use_inbox_name': 'bool',
        'add_tracking_pixel': 'bool'
    }

    attribute_map = {
        'to_contacts': 'toContacts',
        'to_group': 'toGroup',
        'to': 'to',
        '_from': 'from',
        'cc': 'cc',
        'bcc': 'bcc',
        'subject': 'subject',
        'reply_to': 'replyTo',
        'body': 'body',
        'html': 'html',
        'is_html': 'isHTML',
        'charset': 'charset',
        'attachments': 'attachments',
        'template_variables': 'templateVariables',
        'template': 'template',
        'send_strategy': 'sendStrategy',
        'use_inbox_name': 'useInboxName',
        'add_tracking_pixel': 'addTrackingPixel'
    }

    def __init__(self, to_contacts=None, to_group=None, to=None, _from=None, cc=None, bcc=None, subject=None, reply_to=None, body=None, html=None, is_html=None, charset=None, attachments=None, template_variables=None, template=None, send_strategy=None, use_inbox_name=None, add_tracking_pixel=None, local_vars_configuration=None):  # noqa: E501
        """SendEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to_contacts = None
        self._to_group = None
        self._to = None
        self.__from = None
        self._cc = None
        self._bcc = None
        self._subject = None
        self._reply_to = None
        self._body = None
        self._html = None
        self._is_html = None
        self._charset = None
        self._attachments = None
        self._template_variables = None
        self._template = None
        self._send_strategy = None
        self._use_inbox_name = None
        self._add_tracking_pixel = None
        self.discriminator = None

        if to_contacts is not None:
            self.to_contacts = to_contacts
        if to_group is not None:
            self.to_group = to_group
        if to is not None:
            self.to = to
        if _from is not None:
            self._from = _from
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        if subject is not None:
            self.subject = subject
        if reply_to is not None:
            self.reply_to = reply_to
        if body is not None:
            self.body = body
        if html is not None:
            self.html = html
        if is_html is not None:
            self.is_html = is_html
        if charset is not None:
            self.charset = charset
        if attachments is not None:
            self.attachments = attachments
        if template_variables is not None:
            self.template_variables = template_variables
        if template is not None:
            self.template = template
        if send_strategy is not None:
            self.send_strategy = send_strategy
        if use_inbox_name is not None:
            self.use_inbox_name = use_inbox_name
        if add_tracking_pixel is not None:
            self.add_tracking_pixel = add_tracking_pixel

    @property
    def to_contacts(self):
        """Gets the to_contacts of this SendEmailOptions.  # noqa: E501

        Optional list of contact IDs to send email to. Manage your contacts via the API or dashboard. When contacts are used the email is sent to each contact separately so they will not see other recipients.  # noqa: E501

        :return: The to_contacts of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_contacts

    @to_contacts.setter
    def to_contacts(self, to_contacts):
        """Sets the to_contacts of this SendEmailOptions.

        Optional list of contact IDs to send email to. Manage your contacts via the API or dashboard. When contacts are used the email is sent to each contact separately so they will not see other recipients.  # noqa: E501

        :param to_contacts: The to_contacts of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._to_contacts = to_contacts

    @property
    def to_group(self):
        """Gets the to_group of this SendEmailOptions.  # noqa: E501

        Optional contact group ID to send email to. You can create contacts and contact groups in the API or dashboard and use them for email campaigns. When contact groups are used the email is sent to each contact separately so they will not see other recipients  # noqa: E501

        :return: The to_group of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._to_group

    @to_group.setter
    def to_group(self, to_group):
        """Sets the to_group of this SendEmailOptions.

        Optional contact group ID to send email to. You can create contacts and contact groups in the API or dashboard and use them for email campaigns. When contact groups are used the email is sent to each contact separately so they will not see other recipients  # noqa: E501

        :param to_group: The to_group of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._to_group = to_group

    @property
    def to(self):
        """Gets the to of this SendEmailOptions.  # noqa: E501

        List of destination email addresses. Each email address must be RFC 5322 format. Even single recipients must be in array form. Maximum recipients per email depends on your plan. If you need to send many emails try using contacts or contact groups or use a non standard sendStrategy to ensure that spam filters are not triggered (many recipients in one email can affect your spam rating). Be cautious when sending emails that your recipients exist. High bounce rates (meaning a high percentage of emails cannot be delivered because an address does not exist) can result in account freezing.  # noqa: E501

        :return: The to of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendEmailOptions.

        List of destination email addresses. Each email address must be RFC 5322 format. Even single recipients must be in array form. Maximum recipients per email depends on your plan. If you need to send many emails try using contacts or contact groups or use a non standard sendStrategy to ensure that spam filters are not triggered (many recipients in one email can affect your spam rating). Be cautious when sending emails that your recipients exist. High bounce rates (meaning a high percentage of emails cannot be delivered because an address does not exist) can result in account freezing.  # noqa: E501

        :param to: The to of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this SendEmailOptions.  # noqa: E501

        Optional from address. Email address is RFC 5322 format and may include a display name and email in angle brackets (`my@address.com` or `My inbox <my@address.com>`). If no sender is set the source inbox address will be used for this field. If you set `useInboxName` to `true` the from field will include the inbox name as a display name: `inbox_name <inbox@address.com>`. For this to work use the name field when creating an inbox. Beware of potential spam penalties when setting the from field to an address not used by the inbox. Your emails may get blocked by services if you impersonate another address. To use a custom email addresses use a custom domain. You can create domains with the DomainController. The domain must be verified in the dashboard before it can be used.  # noqa: E501

        :return: The _from of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendEmailOptions.

        Optional from address. Email address is RFC 5322 format and may include a display name and email in angle brackets (`my@address.com` or `My inbox <my@address.com>`). If no sender is set the source inbox address will be used for this field. If you set `useInboxName` to `true` the from field will include the inbox name as a display name: `inbox_name <inbox@address.com>`. For this to work use the name field when creating an inbox. Beware of potential spam penalties when setting the from field to an address not used by the inbox. Your emails may get blocked by services if you impersonate another address. To use a custom email addresses use a custom domain. You can create domains with the DomainController. The domain must be verified in the dashboard before it can be used.  # noqa: E501

        :param _from: The _from of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def cc(self):
        """Gets the cc of this SendEmailOptions.  # noqa: E501

        Optional list of cc destination email addresses  # noqa: E501

        :return: The cc of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SendEmailOptions.

        Optional list of cc destination email addresses  # noqa: E501

        :param cc: The cc of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this SendEmailOptions.  # noqa: E501

        Optional list of bcc destination email addresses  # noqa: E501

        :return: The bcc of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SendEmailOptions.

        Optional list of bcc destination email addresses  # noqa: E501

        :param bcc: The bcc of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def subject(self):
        """Gets the subject of this SendEmailOptions.  # noqa: E501

        Optional email subject line  # noqa: E501

        :return: The subject of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendEmailOptions.

        Optional email subject line  # noqa: E501

        :param subject: The subject of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def reply_to(self):
        """Gets the reply_to of this SendEmailOptions.  # noqa: E501

        Optional replyTo header  # noqa: E501

        :return: The reply_to of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this SendEmailOptions.

        Optional replyTo header  # noqa: E501

        :param reply_to: The reply_to of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def body(self):
        """Gets the body of this SendEmailOptions.  # noqa: E501

        Optional contents of email. If body contains HTML then set `isHTML` to true to ensure that email clients render it correctly. You can use moustache template syntax in the email body in conjunction with `toGroup` contact variables or `templateVariables` data. If you need more templating control consider creating a template and using the `template` property instead of the body.  # noqa: E501

        :return: The body of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendEmailOptions.

        Optional contents of email. If body contains HTML then set `isHTML` to true to ensure that email clients render it correctly. You can use moustache template syntax in the email body in conjunction with `toGroup` contact variables or `templateVariables` data. If you need more templating control consider creating a template and using the `template` property instead of the body.  # noqa: E501

        :param body: The body of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def html(self):
        """Gets the html of this SendEmailOptions.  # noqa: E501

        Optional HTML flag to indicate that contents is HTML. Set's a `content-type: text/html` for email. (Deprecated: use `isHTML` instead.)  # noqa: E501

        :return: The html of this SendEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this SendEmailOptions.

        Optional HTML flag to indicate that contents is HTML. Set's a `content-type: text/html` for email. (Deprecated: use `isHTML` instead.)  # noqa: E501

        :param html: The html of this SendEmailOptions.  # noqa: E501
        :type: bool
        """

        self._html = html

    @property
    def is_html(self):
        """Gets the is_html of this SendEmailOptions.  # noqa: E501

        Optional HTML flag. If true the `content-type` of the email will be `text/html`. Set to true when sending HTML to ensure proper rending on email clients  # noqa: E501

        :return: The is_html of this SendEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this SendEmailOptions.

        Optional HTML flag. If true the `content-type` of the email will be `text/html`. Set to true when sending HTML to ensure proper rending on email clients  # noqa: E501

        :param is_html: The is_html of this SendEmailOptions.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def charset(self):
        """Gets the charset of this SendEmailOptions.  # noqa: E501

        Optional charset  # noqa: E501

        :return: The charset of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this SendEmailOptions.

        Optional charset  # noqa: E501

        :param charset: The charset of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def attachments(self):
        """Gets the attachments of this SendEmailOptions.  # noqa: E501

        Optional list of attachment IDs to send with this email. You must first upload each attachment separately via method call or dashboard in order to obtain attachment IDs. This way you can reuse attachments with different emails once uploaded. There are several ways to upload that support `multi-part form`, `base64 file encoding`, and octet stream binary uploads. See the `UploadController` for available methods.   # noqa: E501

        :return: The attachments of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this SendEmailOptions.

        Optional list of attachment IDs to send with this email. You must first upload each attachment separately via method call or dashboard in order to obtain attachment IDs. This way you can reuse attachments with different emails once uploaded. There are several ways to upload that support `multi-part form`, `base64 file encoding`, and octet stream binary uploads. See the `UploadController` for available methods.   # noqa: E501

        :param attachments: The attachments of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def template_variables(self):
        """Gets the template_variables of this SendEmailOptions.  # noqa: E501

        Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values if found.  # noqa: E501

        :return: The template_variables of this SendEmailOptions.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._template_variables

    @template_variables.setter
    def template_variables(self, template_variables):
        """Sets the template_variables of this SendEmailOptions.

        Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values if found.  # noqa: E501

        :param template_variables: The template_variables of this SendEmailOptions.  # noqa: E501
        :type: dict(str, object)
        """

        self._template_variables = template_variables

    @property
    def template(self):
        """Gets the template of this SendEmailOptions.  # noqa: E501

        Optional template ID to use for body. Will override body if provided. When using a template make sure you pass the corresponding map of `templateVariables`. You can find which variables are needed by fetching the template itself or viewing it in the dashboard.  # noqa: E501

        :return: The template of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this SendEmailOptions.

        Optional template ID to use for body. Will override body if provided. When using a template make sure you pass the corresponding map of `templateVariables`. You can find which variables are needed by fetching the template itself or viewing it in the dashboard.  # noqa: E501

        :param template: The template of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def send_strategy(self):
        """Gets the send_strategy of this SendEmailOptions.  # noqa: E501

        How an email should be sent based on its recipients  # noqa: E501

        :return: The send_strategy of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        """Sets the send_strategy of this SendEmailOptions.

        How an email should be sent based on its recipients  # noqa: E501

        :param send_strategy: The send_strategy of this SendEmailOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["SINGLE_MESSAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and send_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `send_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(send_strategy, allowed_values)
            )

        self._send_strategy = send_strategy

    @property
    def use_inbox_name(self):
        """Gets the use_inbox_name of this SendEmailOptions.  # noqa: E501

        Use name of inbox as sender email address name. Will construct RFC 5322 email address with `Inbox name <inbox@address.com>` if the inbox has a name.  # noqa: E501

        :return: The use_inbox_name of this SendEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_inbox_name

    @use_inbox_name.setter
    def use_inbox_name(self, use_inbox_name):
        """Sets the use_inbox_name of this SendEmailOptions.

        Use name of inbox as sender email address name. Will construct RFC 5322 email address with `Inbox name <inbox@address.com>` if the inbox has a name.  # noqa: E501

        :param use_inbox_name: The use_inbox_name of this SendEmailOptions.  # noqa: E501
        :type: bool
        """

        self._use_inbox_name = use_inbox_name

    @property
    def add_tracking_pixel(self):
        """Gets the add_tracking_pixel of this SendEmailOptions.  # noqa: E501

        Add tracking pixel to email  # noqa: E501

        :return: The add_tracking_pixel of this SendEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._add_tracking_pixel

    @add_tracking_pixel.setter
    def add_tracking_pixel(self, add_tracking_pixel):
        """Sets the add_tracking_pixel of this SendEmailOptions.

        Add tracking pixel to email  # noqa: E501

        :param add_tracking_pixel: The add_tracking_pixel of this SendEmailOptions.  # noqa: E501
        :type: bool
        """

        self._add_tracking_pixel = add_tracking_pixel

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
        if not isinstance(other, SendEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
