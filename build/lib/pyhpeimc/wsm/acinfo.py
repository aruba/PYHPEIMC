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
import json
import requests



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_ac_info_all(auth, url):
    """
    function takes no input as input to RESTFUL call to HP IMC
    :return:list of dictionatires contraining the Access Controller information as known by HPE IMC Wireless Services
    Manager module.
    """
    get_ac_info_all_url = "/imcrs/wlan/acInfo/queryAcBasicInfo"
    f_url = url + get_ac_info_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['acBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ac_info_all: An Error has occured"