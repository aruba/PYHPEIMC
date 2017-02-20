#!/usr/bin/env python3
# author: @netmanchris



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

    >>> get_ac_info_all(auth.creds, auth.url)
    [{'hardwareVersion': '',
  'ipAddress': '10.10.10.5',
  'label': 'HP830_WSC',
  'macAddress': 'd0:7e:28:80:40:0c',
  'onlineApCount': '2',
  'onlineClientCount': '5',
  'pingStatus': '1',
  'serialId': '',
  'softwareVersion': 'Release 3507P51',
  'status': '3',
  'sysName': 'HP830_WSC',
  'type': 'HP 830-24P'},
 {'hardwareVersion': '',
  'ipAddress': '10.101.0.235',
  'label': 'aruba3600.lab.local',
  'macAddress': '',
  'onlineApCount': '1',
  'onlineClientCount': '0',
  'pingStatus': '1',
  'serialId': '',
  'softwareVersion': '',
  'status': '1',
  'sysName': 'Aruba3600',
  'type': 'Aruba 3600'},
 {'hardwareVersion': '',
  'ipAddress': '10.101.0.236',
  'label': 'Aruba7010',
  'macAddress': '',
  'onlineApCount': '4',
  'onlineClientCount': '0',
  'pingStatus': '0',
  'serialId': '',
  'softwareVersion': '',
  'status': '5',
  'sysName': 'Aruba7010',
  'type': 'Aruba 7010 Controller'},
 {'hardwareVersion': '',
  'ipAddress': '10.101.0.241',
  'label': 'SG9483N00P',
  'macAddress': '',
  'onlineApCount': '0',
  'onlineClientCount': '0',
  'pingStatus': '0',
  'serialId': '',
  'softwareVersion': '',
  'status': '5',
  'sysName': 'SG9483N00P',
  'type': 'HP MultiService Controllers MSM760'}]

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