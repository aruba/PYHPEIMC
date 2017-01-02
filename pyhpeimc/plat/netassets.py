#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the netassets capabilities
of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS

from pyhpeimc.plat.device import get_dev_details


def get_dev_asset_details(ipaddress, auth, url):
    """Takes in ipaddress as input to fetch device assett details from HP IMC RESTFUL API

    :param ipaddress: IP address of the device you wish to gather the asset details

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: object of type list containing the device asset details, with each asset contained
    in a dictionary

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.netassets import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> single_asset = get_dev_asset_details('10.101.0.1', auth.creds, auth.url)

    >>> assert type(single_asset) is list

    >>> assert 'name' in single_asset[0]

    """
    ipaddress = get_dev_details(ipaddress, auth, url)
    if isinstance(ipaddress, dict):
        ipaddress = ipaddress['ip']
    else:
        print("Asset Doesn't Exist")
        return 403
    f_url = url + "/imcrs/netasset/asset?assetDevice.ip=" + str(ipaddress)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_asset_info = (json.loads(response.text))
            if len(dev_asset_info) > 0:
                dev_asset_info = dev_asset_info['netAsset']
            if isinstance(dev_asset_info, dict):
                dev_asset_info = [dev_asset_info]
            if isinstance(dev_asset_info, list):
                dev_asset_info[:] = [dev for dev in dev_asset_info if dev.get('deviceIp') ==
                                     ipaddress]
            return dev_asset_info
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_dev_asset_details: An Error has occured'


def get_dev_asset_details_all(auth, url):
    """Takes no input to fetch device assett details from HP IMC RESTFUL API

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionatires containing the device asset details

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.netassets import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_assets = get_dev_asset_details_all( auth.creds, auth.url)

    >>> assert type(all_assets) is list

    >>> assert 'asset' in all_assets[0]

    """
    f_url = url + "/imcrs/netasset/asset?start=0&size=15000"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_asset_info = (json.loads(response.text))['netAsset']
            return dev_asset_info
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_dev_asset_details: An Error has occured'
