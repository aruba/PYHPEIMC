#!/usr/bin/env python3
# author: @netmanchris

""" Copyright 2015 Hewlett Packard Enterprise Development LP

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   """

# This section imports required libraries
import requests
import json
import sys
import time
import subprocess
import csv
import os
import ipaddress
import pysnmp
from requests.auth import HTTPDigestAuth
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902
from pyhpeimc.auth import IMCAuth


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

auth = None #IMCAuth('http://','10.101.0.201','8080', 'admin','admin')

def get_dev_asset_details(ipaddress, auth=auth.creds, url=auth.url):
    """Takes in ipaddress as input to fetch device assett details from HP IMC RESTFUL API
    :param ipaddress: IP address of the device you wish to gather the asset details
    :return: object of type list containing the device asset details

    Example:
        auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")
        get_dev_asset_details("10.101.0.1", auth.creds, auth.url)

    """
    # checks to see if the imc credentials are already available
    auth= None
    url = None
    get_dev_asset_url = "/imcrs/netasset/asset?assetDevice.ip=" + str(ipaddress)
    f_url = url + get_dev_asset_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_asset_info = (json.loads(r.text))
            if len(dev_asset_info) > 0:
                dev_asset_info = dev_asset_info['netAsset']
            if type(dev_asset_info) == dict:
                dev_asset_info = [dev_asset_info]
            if type(dev_asset_info) == list:
                dev_asset_info[:] = [dev for dev in dev_asset_info if dev.get('deviceIp') == ipaddress]
            return dev_asset_info
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_dev_asset_details: An Error has occured'

