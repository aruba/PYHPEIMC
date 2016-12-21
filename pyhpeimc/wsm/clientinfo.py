#!/usr/bin/env python3
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the client information capabilities of the
HPE IMC WSM Module using the RESTful API

"""

# This section imports required libraries
import json
import requests



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_client_info_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents one client as discovered by the HPE IMC
    Wireless Services Management module.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.clientinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_client_info = get_client_info_all(auth.creds, auth.url)

    >>> assert type(all_client_info) is list

    >>> assert len(all_client_info[0])  == 16

    >>> assert 'acDevId' in all_client_info[0]

    >>> assert 'acLabel' in all_client_info[0]

    >>> assert 'apIpAddress' in all_client_info[0]

    >>> assert 'apLabel' in all_client_info[0]

    >>> assert 'apMacAddress' in all_client_info[0]

    >>> assert 'apSerialId' in all_client_info[0]

    >>> assert 'channel' in all_client_info[0]

    >>> assert 'ipAddress' in all_client_info[0]

    >>> assert 'location' in all_client_info[0]

    >>> assert 'mac' in all_client_info[0]

    >>> assert 'radioType' in all_client_info[0]

    >>> assert 'signalStrength' in all_client_info[0]

    >>> assert 'ssid' in all_client_info[0]

    >>> assert 'upTime' in all_client_info[0]

    >>> assert 'userName' in all_client_info[0]



    """
    get_client_info_all_url = "/imcrs/wlan/clientInfo/queryAllClientBasicInfo"
    f_url = url + get_client_info_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['clientBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_client_info_all: An Error has occured"


def get_client_online_history_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC
:param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents one client as discovered by the HPE IMC
    Wireless Services Management module.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.clientinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> online_client_info = get_client_online_history_all(auth.creds, auth.url)

    >>> assert type(online_client_info) is list

    >>> assert len(online_client_info[0]) == 21

    >>> assert 'acDevId' in online_client_info[0]

    >>> assert 'apName' in online_client_info[0]

    >>> assert 'apSerialId' in online_client_info[0]

    >>> assert 'authenMode' in online_client_info[0]

    >>> assert 'channel' in online_client_info[0]

    >>> assert 'ciphers' in online_client_info[0]

    >>> assert 'faultTime' in online_client_info[0]

    >>> assert 'ip' in online_client_info[0]

    >>> assert 'loginTime' in online_client_info[0]

    >>> assert 'mac' in online_client_info[0]

    >>> assert 'onlineTime' in online_client_info[0]

    >>> assert 'position' in online_client_info[0]

    >>> assert 'radioId' in online_client_info[0]

    >>> assert 'radioType' in online_client_info[0]

    >>> assert 'rxByte' in online_client_info[0]

    >>> assert 'rxNoise' in online_client_info[0]

    >>> assert 'rxSnr' in online_client_info[0]

    >>> assert 'singalStrength' in online_client_info[0]

    >>> assert 'ssid' in online_client_info[0]

    >>> assert 'txByte' in online_client_info[0]

    >>> assert 'userName' in online_client_info[0]

    """
    get_client_online_history_all_url = "/imcrs/wlan/clientInfo/queryClientOnlineHistoryInfo"
    f_url = url + get_client_online_history_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['clientOnlineHistoryInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_client_online_history_all: An Error has occured"