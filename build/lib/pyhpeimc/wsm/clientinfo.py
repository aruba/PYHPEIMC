#!/usr/bin/env python3
# author: @netmanchris



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

    >>> get_client_info_all(auth.creds, auth.url)
    [{'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apIpAddress': '10.101.0.107',
  'apLabel': 'msm525_ap3',
  'apMacAddress': '78:48:59:49:16:40',
  'apSerialId': 'CN48GTH031',
  'channel': '40',
  'ipAddress': '0.0.0.0',
  'location': 'UWW',
  'mac': '10:40:f3:ee:f0:be',
  'radioType': '32',
  'signalStrength': '-76',
  'ssid': 'famyoung',
  'upTime': '2551',
  'userName': ''},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apIpAddress': '10.101.0.105',
  'apLabel': 'msm525_ap4',
  'apMacAddress': '78:48:59:49:18:C0',
  'apSerialId': 'CN48GTH03G',
  'channel': '11',
  'ipAddress': '0.0.0.0',
  'location': 'UWW',
  'mac': '24:0a:64:6d:55:79',
  'radioType': '16',
  'signalStrength': '-71',
  'ssid': 'famyoung',
  'upTime': '402790',
  'userName': ''},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apIpAddress': '10.101.0.107',
  'apLabel': 'msm525_ap3',
  'apMacAddress': '78:48:59:49:16:40',
  'apSerialId': 'CN48GTH031',
  'channel': '1',
  'ipAddress': '0.0.0.0',
  'location': 'UWW',
  'mac': '3c:4a:92:5b:c2:43',
  'radioType': '16',
  'signalStrength': '-43',
  'ssid': 'famyoung',
  'upTime': '422422',
  'userName': ''},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apIpAddress': '10.101.0.105',
  'apLabel': 'msm525_ap4',
  'apMacAddress': '78:48:59:49:18:C0',
  'apSerialId': 'CN48GTH03G',
  'channel': '48',
  'ipAddress': '0.0.0.0',
  'location': 'UWW',
  'mac': 'b0:34:95:3f:3c:01',
  'radioType': '32',
  'signalStrength': '-48',
  'ssid': 'famyoung',
  'upTime': '404164',
  'userName': ''},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apIpAddress': '10.101.0.105',
  'apLabel': 'msm525_ap4',
  'apMacAddress': '78:48:59:49:18:C0',
  'apSerialId': 'CN48GTH03G',
  'channel': '11',
  'ipAddress': '0.0.0.0',
  'location': 'UWW',
  'mac': 'f4:b8:5e:00:e6:45',
  'radioType': '16',
  'signalStrength': '-82',
  'ssid': 'famyoung',
  'upTime': '335436',
  'userName': ''}]
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

    >>> get_client_online_history_all(auth.creds, auth.url)
    [{'acDevId': '31',
  'apName': 'msm525_ap3',
  'apSerialId': 'CN48GTH031',
  'authenMode': '2',
  'channel': '36',
  'ciphers': '16',
  'faultTime': '2016-06-21 12:15:13',
  'ip': '0.0.0.0',
  'loginTime': '2016-06-21 12:03:13',
  'mac': '00:23:12:0c:24:9f',
  'onlineTime': '00:12:00',
  'position': 'UWW',
  'radioId': '1',
  'radioType': '32',
  'rxByte': '32',
  'rxNoise': '-104',
  'rxSnr': '29',
  'singalStrength': '-66',
  'ssid': 'famyoung',
  'txByte': '3',
  'userName': ''},
 {'acDevId': '31',
  'apName': 'msm525_ap3',
  'apSerialId': 'CN48GTH031',
  'authenMode': '2',
  'channel': '36',
  'ciphers': '16',
  'faultTime': '2016-06-21 15:06:13',
  'ip': '0.0.0.0',
  'loginTime': '2016-06-21 14:42:13',
  'mac': '00:23:12:0c:24:9f',
  'onlineTime': '00:24:00',
  'position': 'UWW',
  'radioId': '1',
  'radioType': '32',
  'rxByte': '37',
  'rxNoise': '-103',
  'rxSnr': '28',
  'singalStrength': '-67',
  'ssid': 'famyoung',
  'txByte': '3',
  'userName': ''}]

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