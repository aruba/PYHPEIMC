#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the alarms capabilities
of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS
from pyhpeimc.plat.device import get_dev_details


def get_dev_alarms(auth, url, devid=None, devip=None):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the current
    alarms for the target device.

    :param devid: int or str value of the target device

    :param devip: str of ipv4 address of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:list of dictionaries containing the alarms for this device

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.alarms import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> dev_alarms = get_dev_alarms(auth.creds, auth.url, devip='10.101.0.221')

    >>> assert 'ackStatus' in dev_alarms[0]

    """
    # checks to see if the imc credentials are already available
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/fault/alarm?operatorName=admin&deviceId=" + \
                        str(devid) + "&desc=false"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_alarm = (json.loads(response.text))
            if 'alarm' in dev_alarm:
                return dev_alarm['alarm']
            else:
                return "Device has no alarms"
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_dev_alarms: An Error has occured'


def get_realtime_alarm(username, auth, url):
    """Takes in no param as input to fetch RealTime Alarms from HP IMC RESTFUL API

    :param username OpeatorName, String type. Required. Default Value "admin". Checks the operator
     has the privileges to view the Real-Time Alarms.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:list of dictionaries where each element of the list represents a single alarm as
    pulled  from the the current list of realtime alarms in the HPE IMC Platform

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.alarms import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> real_time_alarm = get_realtime_alarm('admin', auth.creds, auth.url)

    >>> assert type(real_time_alarm) is list

    >>> assert 'faultDesc' in real_time_alarm[0]

    """
    f_url = url + "/imcrs/fault/faultRealTime?operatorName=" + username
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        realtime_alarm_list = (json.loads(response.text))
        return realtime_alarm_list['faultRealTime']['faultRealTimeList']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_realtime_alarm: An Error has occured'


def get_alarms(username, auth, url):
    """Takes in no param as input to fetch RealTime Alarms from HP IMC RESTFUL API

    :param username OpeatorName, String type. Required. Default Value "admin". Checks the operator
     has the privileges to view the Real-Time Alarms.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:list of dictionaries where each element of the list represents a single alarm as
    pulled  from the the current list of browse alarms in the HPE IMC Platform

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.alarms import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_alarms = get_alarms('admin', auth.creds, auth.url)

    >>> assert (type(all_alarms)) is list

    >>> assert 'ackStatus' in all_alarms[0]

    """
    f_url = url + "/imcrs/fault/alarm?operatorName=" + username + \
                     "&recStatus=0&ackStatus=0&timeRange=0&size=50&desc=true"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            alarm_list = (json.loads(response.text))
            return alarm_list['alarm']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_alarms: An Error has occured'

def get_alarm_details(alarm_id, auth, url):
    """
    function to take str input of alarm_id, issues a REST call to the IMC REST interface and
    returns a dictionary object which contains the  details of a specific alarm.
    :param alarm_id: str number which represents the internal ID of a specific alarm
    :param auth:
    :param url:
    :return:
    """
    f_url = url + "/imcrs/fault/alarm/" + str(alarm_id)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        alarm_details = json.loads(response.text)
        return alarm_details
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_alarm_details: An Error has occured'


def acknowledge_alarm(alarm_id, auth, url):
    """
    Function tasks input of str of alarm ID and sends to REST API. Function will acknowledge
    designated alarm in the IMC alarm database.
    :param alarm_id: str of alarm ID
    param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
    :return: integer HTTP response code

    :rtype int
    """
    f_url = url + "/imcrs/fault/alarm/acknowledge/"+str(alarm_id)
    response = requests.put(f_url, auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_alarms: An Error has occured'


def recover_alarm(alarm_id, auth, url):
    """
    Function tasks input of str of alarm ID and sends to REST API. Function will acknowledge
    designated alarm in the IMC alarm database.
    :param alarm_id: str of alarm ID
    param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
    :return: integer HTTP response code

    :rtype int
    """
    f_url = url + "/imcrs/fault/alarm/recover/" + str(alarm_id)
    response = requests.put(f_url, auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + 'recover_alarm: An Error has occured'


