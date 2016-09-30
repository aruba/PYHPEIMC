#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import json
import requests



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_ap_info_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC
    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single wireless access point which has been
    discovered in the HPE IMC WSM module

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.wsm.apinfo import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_ap_info_all(auth.creds, auth.url)
    [{'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': 'Campus A Floor 1 Conference Room',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': 'Campus A Floor 1 Conference Room',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': 'CN1BD3209B',
  'softwareVersion': '',
  'ssids': ['fammai', 'famyoung', 'HP_BYOD_830', 'HPLAB'],
  'status': '1',
  'sysName': 'ap1_0006',
  'type': 'MSM460-AM'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': '26020e_1_0002',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': '210235A42MB095000401',
  'softwareVersion': '',
  'ssids': ['fammai', 'famyoung', 'HP_BYOD_830', 'HPLAB'],
  'status': '1',
  'sysName': '26020e_1_0002',
  'type': 'WA2620E-AGN'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': '26020e_1',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': '(26020E_1)',
  'softwareVersion': '',
  'ssids': ['fammai', 'famyoung', 'HP_BYOD_830', 'HPLAB'],
  'status': '1',
  'sysName': '26020e_1',
  'type': 'WA2620E-AGN'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.105',
  'isFit': '1',
  'label': 'msm525_ap4',
  'location': 'UWW',
  'locationList': 'UWW',
  'macAddress': '78:48:59:49:18:C0',
  'onlineClientCount': '3',
  'onlineStatus': '1',
  'serialId': 'CN48GTH03G',
  'softwareVersion': 'V100R005B09D045',
  'ssids': ['famyoung', 'HP_BYOD_830'],
  'status': '1',
  'sysName': 'msm525_ap4',
  'type': '525-WW'},
 {'acDevId': '238',
  'acIpAddress': '10.101.0.236',
  'acLabel': 'Aruba7010',
  'apAlias': 'ac:a3:1e:cd:cf:04',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.148',
  'isFit': '1',
  'label': 'ac:a3:1e:cd:cf:04',
  'location': 'Lab',
  'locationList': 'Lab',
  'macAddress': 'AC:A3:1E:CD:CF:04',
  'onlineClientCount': '0',
  'onlineStatus': '1',
  'serialId': 'ac:a3:1e:cd:cf:04',
  'softwareVersion': '',
  'status': '1',
  'sysName': 'ac:a3:1e:cd:cf:04',
  'type': '325'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': 'msm525_ap2',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': 'CN48GTH01Q',
  'softwareVersion': '',
  'ssids': ['famyoung', 'HP_BYOD_830'],
  'status': '1',
  'sysName': 'msm525_ap2',
  'type': '525-WW'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': 'ap1',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': '(AP1)',
  'softwareVersion': '',
  'ssids': ['fammai', 'famyoung', 'HP_BYOD_830', 'HPLAB'],
  'status': '1',
  'sysName': 'ap1',
  'type': 'MSM460-AM'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.110',
  'isFit': '1',
  'label': 'msm525_ap1',
  'location': '',
  'macAddress': '78:48:59:49:10:C0',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': 'CN48GTH016',
  'softwareVersion': '',
  'ssids': ['famyoung', 'HP_BYOD_830'],
  'status': '1',
  'sysName': 'msm525_ap1',
  'type': '525-WW'},
 {'acDevId': '68',
  'acIpAddress': '10.101.0.235',
  'acLabel': 'aruba3600.lab.local',
  'apAlias': 'd8:c7:c8:c2:52:4e',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.106',
  'isFit': '1',
  'label': 'd8:c7:c8:c2:52:4e',
  'location': 'Lab',
  'locationList': 'Lab',
  'macAddress': 'D8:C7:C8:C2:52:4E',
  'onlineClientCount': '0',
  'onlineStatus': '1',
  'serialId': 'd8:c7:c8:c2:52:4e',
  'softwareVersion': '',
  'status': '1',
  'sysName': 'd8:c7:c8:c2:52:4e',
  'type': '105'},
 {'acDevId': '238',
  'acIpAddress': '10.101.0.236',
  'acLabel': 'Aruba7010',
  'apAlias': 'ac:a3:1e:cd:cc:c4',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.107',
  'isFit': '1',
  'label': 'ac:a3:1e:cd:cc:c4',
  'location': 'Lab',
  'locationList': 'Lab',
  'macAddress': 'AC:A3:1E:CD:CC:C4',
  'onlineClientCount': '0',
  'onlineStatus': '1',
  'serialId': 'ac:a3:1e:cd:cc:c4',
  'softwareVersion': '',
  'status': '1',
  'sysName': 'ac:a3:1e:cd:cc:c4',
  'type': '325'},
 {'acDevId': '238',
  'acIpAddress': '10.101.0.236',
  'acLabel': 'Aruba7010',
  'apAlias': 'ac:a3:1e:ca:6c:9c',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.149',
  'isFit': '1',
  'label': 'ac:a3:1e:ca:6c:9c',
  'location': 'Lab',
  'locationList': 'Lab',
  'macAddress': 'AC:A3:1E:CA:6C:9C',
  'onlineClientCount': '0',
  'onlineStatus': '1',
  'serialId': 'ac:a3:1e:ca:6c:9c',
  'softwareVersion': '',
  'status': '1',
  'sysName': 'ac:a3:1e:ca:6c:9c',
  'type': '115'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '1',
  'hardwareVersion': '',
  'ipAddress': '10.101.0.107',
  'isFit': '1',
  'label': 'msm525_ap3',
  'location': 'UWW',
  'locationList': 'UWW',
  'macAddress': '78:48:59:49:16:40',
  'onlineClientCount': '2',
  'onlineStatus': '1',
  'serialId': 'CN48GTH031',
  'softwareVersion': 'V100R005B09D045',
  'ssids': ['famyoung', 'HP_BYOD_830'],
  'status': '1',
  'sysName': 'msm525_ap3',
  'type': '525-WW'},
 {'acDevId': '31',
  'acIpAddress': '10.10.10.5',
  'acLabel': 'HP830_WSC',
  'apAlias': '',
  'connectType': '3',
  'hardwareVersion': '',
  'ipAddress': '',
  'isFit': '1',
  'label': 'ap1_0005',
  'location': '',
  'macAddress': '',
  'onlineClientCount': '0',
  'onlineStatus': '0',
  'serialId': 'CN1BD320BF',
  'softwareVersion': '',
  'ssids': ['fammai', 'famyoung', 'HP_BYOD_830', 'HPLAB', 'SCEP_TEST'],
  'status': '1',
  'sysName': 'ap1_0005',
  'type': 'MSM460-AM'}]
    """
    get_ap_info_all_url = "/imcrs/wlan/apInfo/queryApBasicInfo"
    f_url = url + get_ap_info_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['apBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ap_info_all: An Error has occured"

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

    >>> get_ap_info('10.101.0.105',auth.creds, auth.url)
    {'acDevId': '31',
 'acIpAddress': '10.10.10.5',
 'acLabel': 'HP830_WSC',
 'apAlias': '',
 'connectType': '1',
 'hardwareVersion': '',
 'ipAddress': '10.101.0.105',
 'isFit': '1',
 'label': 'msm525_ap4',
 'location': 'UWW',
 'locationList': 'UWW',
 'macAddress': '78:48:59:49:18:C0',
 'onlineClientCount': '3',
 'onlineStatus': '1',
 'serialId': 'CN48GTH03G',
 'softwareVersion': 'V100R005B09D045',
 'ssids': ['famyoung', 'HP_BYOD_830'],
 'status': '1',
 'sysName': 'msm525_ap4',
 'type': '525-WW'}
    """
    get_ap_info_url = "/imcrs/wlan/apInfo/queryApBasicInfoByCondition?ipAddress=" + str(ipaddress)
    f_url = url + get_ap_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['apBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ap_info_all: An Error has occured"


