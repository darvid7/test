# coding: utf-8

"""
    Uber API

    Move your app forward with the Uber API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PriceEstimate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'product_id': 'str',
        'currency_code': 'str',
        'display_name': 'str',
        'estimate': 'str',
        'low_estimate': 'float',
        'high_estimate': 'float',
        'surge_multiplier': 'float'
    }

    attribute_map = {
        'product_id': 'product_id',
        'currency_code': 'currency_code',
        'display_name': 'display_name',
        'estimate': 'estimate',
        'low_estimate': 'low_estimate',
        'high_estimate': 'high_estimate',
        'surge_multiplier': 'surge_multiplier'
    }

    def __init__(self, product_id=None, currency_code=None, display_name=None, estimate=None, low_estimate=None, high_estimate=None, surge_multiplier=None):  # noqa: E501
        """PriceEstimate - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._currency_code = None
        self._display_name = None
        self._estimate = None
        self._low_estimate = None
        self._high_estimate = None
        self._surge_multiplier = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if currency_code is not None:
            self.currency_code = currency_code
        if display_name is not None:
            self.display_name = display_name
        if estimate is not None:
            self.estimate = estimate
        if low_estimate is not None:
            self.low_estimate = low_estimate
        if high_estimate is not None:
            self.high_estimate = high_estimate
        if surge_multiplier is not None:
            self.surge_multiplier = surge_multiplier

    @property
    def product_id(self):
        """Gets the product_id of this PriceEstimate.  # noqa: E501

        Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles  # noqa: E501

        :return: The product_id of this PriceEstimate.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PriceEstimate.

        Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles  # noqa: E501

        :param product_id: The product_id of this PriceEstimate.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def currency_code(self):
        """Gets the currency_code of this PriceEstimate.  # noqa: E501

        [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code.  # noqa: E501

        :return: The currency_code of this PriceEstimate.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PriceEstimate.

        [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code.  # noqa: E501

        :param currency_code: The currency_code of this PriceEstimate.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def display_name(self):
        """Gets the display_name of this PriceEstimate.  # noqa: E501

        Display name of product.  # noqa: E501

        :return: The display_name of this PriceEstimate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PriceEstimate.

        Display name of product.  # noqa: E501

        :param display_name: The display_name of this PriceEstimate.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def estimate(self):
        """Gets the estimate of this PriceEstimate.  # noqa: E501

        Formatted string of estimate in local currency of the start location. Estimate could be a range, a single number (flat rate) or \"Metered\" for TAXI.  # noqa: E501

        :return: The estimate of this PriceEstimate.  # noqa: E501
        :rtype: str
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this PriceEstimate.

        Formatted string of estimate in local currency of the start location. Estimate could be a range, a single number (flat rate) or \"Metered\" for TAXI.  # noqa: E501

        :param estimate: The estimate of this PriceEstimate.  # noqa: E501
        :type: str
        """

        self._estimate = estimate

    @property
    def low_estimate(self):
        """Gets the low_estimate of this PriceEstimate.  # noqa: E501

        Lower bound of the estimated price.  # noqa: E501

        :return: The low_estimate of this PriceEstimate.  # noqa: E501
        :rtype: float
        """
        return self._low_estimate

    @low_estimate.setter
    def low_estimate(self, low_estimate):
        """Sets the low_estimate of this PriceEstimate.

        Lower bound of the estimated price.  # noqa: E501

        :param low_estimate: The low_estimate of this PriceEstimate.  # noqa: E501
        :type: float
        """

        self._low_estimate = low_estimate

    @property
    def high_estimate(self):
        """Gets the high_estimate of this PriceEstimate.  # noqa: E501

        Upper bound of the estimated price.  # noqa: E501

        :return: The high_estimate of this PriceEstimate.  # noqa: E501
        :rtype: float
        """
        return self._high_estimate

    @high_estimate.setter
    def high_estimate(self, high_estimate):
        """Sets the high_estimate of this PriceEstimate.

        Upper bound of the estimated price.  # noqa: E501

        :param high_estimate: The high_estimate of this PriceEstimate.  # noqa: E501
        :type: float
        """

        self._high_estimate = high_estimate

    @property
    def surge_multiplier(self):
        """Gets the surge_multiplier of this PriceEstimate.  # noqa: E501

        Expected surge multiplier. Surge is active if surge_multiplier is greater than 1. Price estimate already factors in the surge multiplier.  # noqa: E501

        :return: The surge_multiplier of this PriceEstimate.  # noqa: E501
        :rtype: float
        """
        return self._surge_multiplier

    @surge_multiplier.setter
    def surge_multiplier(self, surge_multiplier):
        """Sets the surge_multiplier of this PriceEstimate.

        Expected surge multiplier. Surge is active if surge_multiplier is greater than 1. Price estimate already factors in the surge multiplier.  # noqa: E501

        :param surge_multiplier: The surge_multiplier of this PriceEstimate.  # noqa: E501
        :type: float
        """

        self._surge_multiplier = surge_multiplier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PriceEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other