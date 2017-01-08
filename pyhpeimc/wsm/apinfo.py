# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the access point information
capabilities of the HPE IMC WSM Module using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS


def get_ap_info_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC
    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single wireless
    access point which has been
    discovered in the HPE IMC WSM module

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.apinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_ap_info = get_ap_info_all(auth.creds, auth.url)

    >>> assert type(all_ap_info) is list

    >>> assert len(all_ap_info[0]) == 19

    >>> assert 'acDevId' in all_ap_info[0]

    >>> assert 'acIpAddress' in all_ap_info[0]

    >>> assert 'acLabel' in all_ap_info[0]

    >>> assert 'apAlias' in all_ap_info[0]

    >>> assert 'connectType' in all_ap_info[0]

    >>> assert 'hardwareVersion' in all_ap_info[0]

    >>> assert 'ipAddress' in all_ap_info[0]

    >>> assert 'isFit' in all_ap_info[0]

    >>> assert 'label' in all_ap_info[0]

    >>> assert 'location' in all_ap_info[0]

    >>> assert 'macAddress' in all_ap_info[0]

    >>> assert 'onlineClientCount' in all_ap_info[0]

    >>> assert 'onlineStatus' in all_ap_info[0]

    >>> assert 'serialId' in all_ap_info[0]

    >>> assert 'softwareVersion' in all_ap_info[0]

    >>> assert 'ssids' in all_ap_info[0]

    >>> assert 'status' in all_ap_info[0]

    >>> assert 'type' in all_ap_info[0]

    >>> assert 'sysName' in all_ap_info[0]

    """
    f_url = url + "/imcrs/wlan/apInfo/queryApBasicInfo"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            if len(response.text) > 0:
                return json.loads(response.text)['apBasicInfo']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ap_info_all: An Error has occured"


def get_ap_info(ipaddress, auth, url):
    """
    function takes input of ipaddress to RESTFUL call to HP IMC

    :param ipaddress: The current IP address of the Access Point at time of query.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: Dictionary object with the details of the target access point

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.apinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ap_info = get_ap_info('10.101.0.170',auth.creds, auth.url)

    >>> assert type(ap_info) is dict

    >>> assert len(ap_info) == 20

    >>> assert 'acDevId' in ap_info

    >>> assert 'acIpAddress' in ap_info

    >>> assert 'acLabel' in ap_info

    >>> assert 'apAlias' in ap_info

    >>> assert 'connectType' in ap_info

    >>> assert 'hardwareVersion' in ap_info

    >>> assert 'ipAddress' in ap_info

    >>> assert 'isFit' in ap_info

    >>> assert 'label' in ap_info

    >>> assert 'location' in ap_info

    >>> assert 'locationList' in ap_info

    >>> assert 'macAddress' in ap_info

    >>> assert 'onlineClientCount' in ap_info

    >>> assert 'serialId' in ap_info

    >>> assert 'softwareVersion' in ap_info

    >>> assert 'ssids' in ap_info

    >>> assert 'status' in ap_info

    >>> assert 'sysName' in ap_info

    >>> assert 'type' in ap_info

    """
    get_ap_info_url = "/imcrs/wlan/apInfo/queryApBasicInfoByCondition?ipAddress=" + str(ipaddress)
    f_url = url + get_ap_info_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            if len(response.text) > 0:
                return json.loads(response.text)['apBasicInfo']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ap_info_all: An Error has occured"
