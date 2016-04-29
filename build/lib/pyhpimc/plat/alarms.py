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
from __main__ import *

HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

auth = IMCAuth('http://','10.101.0.201','8080', 'admin','admin')



def get_dev_alarms(devId, auth=auth.creds, url=auth.url):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the current alarms for the target
    device.
    :param devId: int or str value of the target device
    :return:list of dictionaries containing the alarms for this device
    """
    # checks to see if the imc credentials are already available
    get_dev_alarm_url = "/imcrs/fault/alarm?operatorName=admin&deviceId=" + \
                        str(devId) + "&desc=false"
    f_url = url + get_dev_alarm_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    try:
        if r.status_code == 200:
            dev_alarm = (json.loads(r.text))
            if 'alarm' in dev_alarm:
                return dev_alarm['alarm']
            else:
                return "Device has no alarms"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_dev_alarms: An Error has occured'
