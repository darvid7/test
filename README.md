# swagger-client
Move your app forward with the Uber API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.EstimatesApi()
start_latitude = 1.2 # float | Latitude component of start location.
start_longitude = 1.2 # float | Longitude component of start location.
end_latitude = 1.2 # float | Latitude component of end location.
end_longitude = 1.2 # float | Longitude component of end location.

try:
    # Price Estimates
    api_response = api_instance.estimates_price_get(start_latitude, start_longitude, end_latitude, end_longitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EstimatesApi->estimates_price_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.uber.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EstimatesApi* | [**estimates_price_get**](docs/EstimatesApi.md#estimates_price_get) | **GET** /estimates/price | Price Estimates
*EstimatesApi* | [**estimates_time_get**](docs/EstimatesApi.md#estimates_time_get) | **GET** /estimates/time | Time Estimates
*ProductsApi* | [**products_get**](docs/ProductsApi.md#products_get) | **GET** /products | Product Types
*UserApi* | [**history_get**](docs/UserApi.md#history_get) | **GET** /history | User Activity
*UserApi* | [**me_get**](docs/UserApi.md#me_get) | **GET** /me | User Profile


## Documentation For Models

 - [Activities](docs/Activities.md)
 - [Activity](docs/Activity.md)
 - [Error](docs/Error.md)
 - [PriceEstimate](docs/PriceEstimate.md)
 - [Product](docs/Product.md)
 - [ProductList](docs/ProductList.md)
 - [Profile](docs/Profile.md)


## Documentation For Authorization


## apikey

- **Type**: API key
- **API key parameter name**: server_token
- **Location**: URL query string


## Author


