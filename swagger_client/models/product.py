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


class Product(object):
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
        'description': 'str',
        'display_name': 'str',
        'capacity': 'int',
        'image': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'description': 'description',
        'display_name': 'display_name',
        'capacity': 'capacity',
        'image': 'image'
    }

    def __init__(self, product_id=None, description=None, display_name=None, capacity=None, image=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._description = None
        self._display_name = None
        self._capacity = None
        self._image = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if capacity is not None:
            self.capacity = capacity
        if image is not None:
            self.image = image

    @property
    def product_id(self):
        """Gets the product_id of this Product.  # noqa: E501

        Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.  # noqa: E501

        :return: The product_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Product.

        Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.  # noqa: E501

        :param product_id: The product_id of this Product.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501

        Description of product.  # noqa: E501

        :return: The description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.

        Description of product.  # noqa: E501

        :param description: The description of this Product.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this Product.  # noqa: E501

        Display name of product.  # noqa: E501

        :return: The display_name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Product.

        Display name of product.  # noqa: E501

        :param display_name: The display_name of this Product.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def capacity(self):
        """Gets the capacity of this Product.  # noqa: E501

        Capacity of product. For example, 4 people.  # noqa: E501

        :return: The capacity of this Product.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Product.

        Capacity of product. For example, 4 people.  # noqa: E501

        :param capacity: The capacity of this Product.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def image(self):
        """Gets the image of this Product.  # noqa: E501

        Image URL representing the product.  # noqa: E501

        :return: The image of this Product.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Product.

        Image URL representing the product.  # noqa: E501

        :param image: The image of this Product.  # noqa: E501
        :type: str
        """

        self._image = image

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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other