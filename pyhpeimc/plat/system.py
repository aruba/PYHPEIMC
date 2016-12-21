#!/usr/bin/env python3
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the system configuration capabilities
of the HPE IMC NMS platform using the RESTful API

"""


# This section imports required libraries
import json
import requests


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#auth = None


"""
This section contains functions which operate at the system level
"""


def get_system_vendors(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single vendor

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.system import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> vendors = get_system_vendors(auth.creds, auth.url)

      >>> assert type(vendors) is list

      >>> assert 'name' in vendors[0]


    """
    get_system_vendors_url = '/imcrs/plat/res/vendor?start=0&size=10000&orderBy=id&desc=false&total=false'
    f_url = url + get_system_vendors_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            system_vendors = (json.loads(r.text))
            return system_vendors['deviceVendor']
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " get_dev_details: An Error has occured"


def get_system_category(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device category

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> categories = get_system_category(auth.creds, auth.url)

      >>> assert type(categories) is list

      >>> assert 'name' in categories[0]


    """
    get_system_category_url = '/imcrs/plat/res/category?start=0&size=10000&orderBy=id&desc=false&total=false'
    f_url = url + get_system_category_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            system_category = (json.loads(r.text))
            return system_category['deviceCategory']
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " get_dev_details: An Error has occured"


def get_system_device_models(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n
:rtype: list

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device model


      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> device_models = get_system_device_models(auth.creds, auth.url)

      >>> assert type(device_models) is list

      >>> assert 'virtualDeviceName' in device_models[0]

    """
    get_system_device_model_url = '/imcrs/plat/res/model?start=0&size=10000&orderBy=id&desc=false&total=false'
    f_url = url + get_system_device_model_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            system_device_model = (json.loads(r.text))
            return system_device_model['deviceModel']
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " get_dev_details: An Error has occured"


def get_system_series(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device series

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> series = get_system_series(auth.creds, auth.url)

      >>> assert type(series) is list

      >>> assert 'name' in series[0]



    """
    get_system_series_url = '/imcrs/plat/res/series?managedOnly=false&start=0&size=10000&orderBy=id&desc=false&total=false'
    f_url = url + get_system_series_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            system_series = (json.loads(r.text))
            return system_series['deviceSeries']
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " get_dev_series: An Error has occured"