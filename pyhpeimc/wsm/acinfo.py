# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the access controller
capabilities of the HPE IMC WSM Module using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS


def get_ac_info_all(auth, url):
    """
    function takes no input as input to RESTFUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single wireless
    controller which has been discovered in the HPE IMC WSM module

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.acinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ac_info_all = get_ac_info_all(auth.creds, auth.url)

    """
    f_url = url + "/imcrs/wlan/acInfo/queryAcBasicInfo"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            if len(response.text) > 0:
                return json.loads(response.text)['acBasicInfo']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ac_info_all: An Error has occured"
