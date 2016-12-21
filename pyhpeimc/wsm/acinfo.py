#!/usr/bin/env python3
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the access controller
capabilities of the HPE IMC WSM Module using the RESTful API

"""


# This section imports required libraries
import json
import requests



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_ac_info_all(auth, url):
    """
    function takes no input as input to RESTFUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single wireless controller which has been
    discovered in the HPE IMC WSM module

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.acinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ac_info_all = get_ac_info_all(auth.creds, auth.url)

    >>> assert type(ac_info_all) is list

    >>> assert len(ac_info_all[0]) == 12

    >>> assert 'hardwareVersion' in ac_info_all[0]

    >>> assert 'ipAddress' in ac_info_all[0]

    >>> assert 'label' in ac_info_all[0]

    >>> assert 'macAddress' in ac_info_all[0]

    >>> assert 'onlineApCount' in ac_info_all[0]

    >>> assert 'onlineClientCount' in ac_info_all[0]

    >>> assert 'pingStatus' in ac_info_all[0]

    >>> assert 'serialId' in ac_info_all[0]

    >>> assert 'softwareVersion' in ac_info_all[0]

    >>> assert 'status' in ac_info_all[0]

    >>> assert 'sysName' in ac_info_all[0]

    >>> assert 'type' in ac_info_all[0]
    
    """
    get_ac_info_all_url = "/imcrs/wlan/acInfo/queryAcBasicInfo"
    f_url = url + get_ac_info_all_url
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['acBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ac_info_all: An Error has occured"