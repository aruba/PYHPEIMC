#!/usr/bin/env python3
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the alarms capabilities
of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json
import requests
from pyhpeimc.plat.device import *

HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}


headers = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_dev_alarms(auth, url,devid= None, devip= None):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the current alarms for the target
    device.

    :param devId: int or str value of the target device

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
    get_dev_alarm_url = "/imcrs/fault/alarm?operatorName=admin&deviceId=" + \
                        str(devid) + "&desc=false"
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


def get_realtime_alarm(username, auth, url):
    """Takes in no param as input to fetch RealTime Alarms from HP IMC RESTFUL API

    :param username OpeatorName, String type. Required. Default Value "admin". Checks the operator
     has the privileges to view the Real-Time Alarms.

    :param devId: int or str value of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:list of dictionaries where each element of the list represents a single alarm as pulled from the the current
     list of realtime alarms in the HPE IMC Platform

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.alarms import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> real_time_alarm = get_realtime_alarm('admin', auth.creds, auth.url)

    >>> assert type(real_time_alarm) is list

    >>> assert 'faultDesc' in real_time_alarm[0]

    """
    get_realtime_alarm_url = "/imcrs/fault/faultRealTime?operatorName=" + username
    f_url = url + get_realtime_alarm_url
    r = requests.get(f_url, auth=auth, headers=headers)
    try:
        realtime_alarm_list = (json.loads(r.text))
        return realtime_alarm_list['faultRealTime']['faultRealTimeList']
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + ' get_realtime_alarm: An Error has occured'


def get_alarms(username, auth, url):
    """Takes in no param as input to fetch RealTime Alarms from HP IMC RESTFUL API

    :param username OpeatorName, String type. Required. Default Value "admin". Checks the operator
     has the privileges to view the Real-Time Alarms.

    :param devId: int or str value of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:list of dictionaries where each element of the list represents a single alarm as pulled from the the current
     list of browse alarms in the HPE IMC Platform

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.alarms import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_alarms = get_alarms('admin', auth.creds, auth.url)

    >>> assert (type(all_alarms)) is list

    >>> assert 'ackStatus' in all_alarms[0]

    """
    get_alarms_url = "/imcrs/fault/alarm?operatorName=" + username + "&recStatus=0&ackStatus=0&timeRange=0&size=50&desc=true"
    f_url = url + get_alarms_url
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    try:
        if r.status_code == 200:
            alarm_list = (json.loads(r.text))
            return alarm_list['alarm']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_alarms: An Error has occured'



