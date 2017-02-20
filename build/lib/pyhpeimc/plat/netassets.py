#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import requests
import json



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}


def get_dev_asset_details(ipaddress, auth, url):
    """Takes in ipaddress as input to fetch device assett details from HP IMC RESTFUL API

    :param ipaddress: IP address of the device you wish to gather the asset details

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: object of type list containing the device asset details, with each asset contained in a dictionary

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.netassets import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_asset_details('10.101.0.1', auth.creds, auth.url)
Out[46]:
[{'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=1',
  'assetNumber': '',
  'boardNum': 'FHK1119F1DX',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '0',
  'desc': '2811 chassis',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': 'System Bootstrap, Version 12.4(13r)T11, RELEASE SOFTWARE (fc1)',
  'hardVersion': 'V04 ',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': 'CISCO2811',
  'name': '2811 chassis',
  'phyClass': '3',
  'phyIndex': '1',
  'physicalFlag': '0',
  'relPos': '-1',
  'remark': '',
  'serialNum': 'FHK1119F1DX',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '15.1(4)M, RELEASE SOFTWARE (fc1)',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.3.436'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=14',
  'assetNumber': '',
  'boardNum': 'FOC11063NZ4',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '13',
  'desc': '2nd generation two port FXO voice interface daughtercard',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': 'V01 ',
  'isFRU': '1',
  'mfgName': 'Cisco',
  'model': 'VIC2-2FXO',
  'name': '2nd generation two port FXO voice interface daughtercard on Slot 0 SubSlot 2',
  'phyClass': '9',
  'phyIndex': '14',
  'physicalFlag': '2',
  'relPos': '0',
  'remark': '',
  'serialNum': 'FOC11063NZ4',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.9.3.114'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=30',
  'assetNumber': '',
  'boardNum': 'FOC11163P04',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '29',
  'desc': '40GB IDE Disc Daughter Card',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': '',
  'isFRU': '1',
  'mfgName': 'Cisco',
  'model': ' ',
  'name': '40GB IDE Disc Daughter Card on Slot 1 SubSlot 0',
  'phyClass': '9',
  'phyIndex': '30',
  'physicalFlag': '2',
  'relPos': '0',
  'remark': '',
  'serialNum': 'FOC11163P04',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.9.15.25'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=25',
  'assetNumber': '',
  'boardNum': '',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '3',
  'desc': 'AIM Container Slot 0',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': '',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': '',
  'name': 'AIM Container Slot 0',
  'phyClass': '5',
  'phyIndex': '25',
  'physicalFlag': '0',
  'relPos': '6',
  'remark': '',
  'serialNum': '',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.5.2'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=26',
  'assetNumber': '',
  'boardNum': '',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '3',
  'desc': 'AIM Container Slot 1',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': '',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': '',
  'name': 'AIM Container Slot 1',
  'phyClass': '5',
  'phyIndex': '26',
  'physicalFlag': '0',
  'relPos': '7',
  'remark': '',
  'serialNum': '',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.5.2'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=2',
  'assetNumber': '',
  'boardNum': '',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '1',
  'desc': 'C2811 Chassis Slot',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': '',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': '',
  'name': 'C2811 Chassis Slot 0',
  'phyClass': '5',
  'phyIndex': '2',
  'physicalFlag': '0',
  'relPos': '0',
  'remark': '',
  'serialNum': '',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.5.1'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=27',
  'assetNumber': '',
  'boardNum': '',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '1',
  'desc': 'C2811 Chassis Slot',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': '',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': '',
  'name': 'C2811 Chassis Slot 1',
  'phyClass': '5',
  'phyIndex': '27',
  'physicalFlag': '0',
  'relPos': '1',
  'remark': '',
  'serialNum': '',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.5.1'},
 {'alias': '',
  'asset': 'http://kontrolissues.thruhere.net:8086/imcrs/netasset/asset/detail?devId=15&phyIndex=3',
  'assetNumber': '',
  'boardNum': 'FOC11152G90',
  'bom': '',
  'buildInfo': '',
  'cleiCode': '',
  'containedIn': '2',
  'desc': 'c2811 Motherboard with 2FE and integrated VPN',
  'devId': '15',
  'deviceIp': '10.101.0.1',
  'deviceName': 'router.lab.local',
  'firmwareVersion': '',
  'hardVersion': 'V04 ',
  'isFRU': '2',
  'mfgName': 'Cisco',
  'model': '',
  'name': 'c2811 Motherboard with 2FE and integrated VPN on Slot 0',
  'phyClass': '9',
  'phyIndex': '3',
  'physicalFlag': '0',
  'relPos': '0',
  'remark': '',
  'serialNum': 'FOC11152G90',
  'serverDate': '2016-01-26T15:20:40-05:00',
  'softVersion': '15.1(4)M',
  'vendorType': '1.3.6.1.4.1.9.12.3.1.9.3.129'}]



    """
    get_dev_asset_url = "/imcrs/netasset/asset?assetDevice.ip=" + str(ipaddress)
    f_url = url + get_dev_asset_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_asset_info = (json.loads(r.text))
            if len(dev_asset_info) > 0:
                dev_asset_info = dev_asset_info['netAsset']
            if type(dev_asset_info) == dict:
                dev_asset_info = [dev_asset_info]
            if type(dev_asset_info) == list:
                dev_asset_info[:] = [dev for dev in dev_asset_info if dev.get('deviceIp') == ipaddress]
            return dev_asset_info
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_dev_asset_details: An Error has occured'

def get_dev_asset_details_all(auth, url):
    """Takes no input to fetch device assett details from HP IMC RESTFUL API

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionatires containing the device asset details

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.netassets import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")
    #Output in test system too long to include. Provided for example only
    #>>> get_dev_asset_details_all( auth.creds, auth.url)

    """
    # checks to see if the imc credentials are already available
    get_dev_asset_details_all_url = "/imcrs/netasset/asset?start=0&size=15000"
    f_url = url + get_dev_asset_details_all_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_asset_info = (json.loads(r.text))['netAsset']
            return dev_asset_info
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_dev_asset_details: An Error has occured'



