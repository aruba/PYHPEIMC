#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import json
import requests


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#auth = None


"""
This section contains functions which operate at the device level.
"""
def get_dev_details(ip_address, auth, url):
    """Takes string input of IP address to issue RESTUL call to HP IMC\n

    :param ip_address: string object of dotted decimal notation of IPv4 address

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: dictionary of device details

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_details('10.101.0.1', auth.creds, auth.url)
    {'categoryId': '0',
 'contact': 'changed this too',
 'devCategoryImgSrc': 'router',
 'id': '15',
 'ip': '10.101.0.1',
 'label': 'router.lab.local',
 'link': {'@href': 'http://10.101.0.203:8080/imcrs/plat/res/device/15',
  '@op': 'GET',
  '@rel': 'self'},
 'location': 'changed this too',
 'mac': '00:1b:d4:47:1e:68',
 'mask': '255.255.255.0',
 'parentId': '1',
 'status': '1',
 'statusDesc': 'Normal',
 'symbolDesc': '',
 'symbolId': '1026',
 'symbolLevel': '2',
 'symbolName': 'router.lab.local',
 'symbolType': '3',
 'sysDescription': '',
 'sysName': 'Cisco2811.lab.local',
 'sysOid': '1.3.6.1.4.1.9.1.576',
 'topoIconName': 'iconroute',
 'typeName': 'Cisco 2811'}

    >>> get_dev_details('8.8.8.8', auth.creds, auth.url)

    """

    get_dev_details_url = "/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" + \
                          str(ip_address) + "&start=0&size=1000&orderBy=id&desc=false&total=false"
    f_url = url + get_dev_details_url
        # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_details = (json.loads(r.text))
            if len(dev_details) == 0:
                print("Device not found")
                return "Device not found"
            elif type(dev_details['device']) == list:
                for i in dev_details['device']:
                    if i['ip'] == ip_address:
                        dev_details = i
                        return dev_details
            elif type(dev_details['device']) == dict:
                return dev_details['device']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_details: An Error has occured"


def get_dev_interface(devid, auth, url):
    """
    Function takes devid as input to RESTFUL call to HP IMC platform and returns list of device interfaces

    :param devid: requires devid as the only input

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass


    :return: list object which contains a dictionary per interface

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_interface('15', auth.creds, auth.url)
    [{'adminStatus': '2',
  'adminStatusDesc': 'Down',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Service-Engine1/0',
  'ifIndex': '1',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '100000000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 1 second(s) 610 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:46',
  'mtu': '1500',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '00:1b:d4:47:1e:78',
  'showStatus': '-1',
  'statusDesc': 'Disabled'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'inside',
  'ifDescription': 'FastEthernet0/0',
  'ifIndex': '2',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '100000000',
  'ipHash': {'item': ['10.101.0.1', '255.255.255.0']},
  'lastChange': '19 day(s) 20 hour(s) 33 minute(s) 3 second(s) 470 millisecond(s)',
  'lastChangeTime': '2016-07-07 17:51:31',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1b:d4:47:1e:68',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'WAN',
  'ifDescription': 'FastEthernet0/1',
  'ifIndex': '3',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '100000000',
  'ipHash': {'item': ['74.58.140.80', '255.255.255.0']},
  'lastChange': '17 day(s) 21 hour(s) 13 minute(s) 33 second(s) 790 millisecond(s)',
  'lastChangeTime': '2016-07-05 18:32:03',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1b:d4:47:1e:69',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '2',
  'adminStatusDesc': 'Down',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Serial0/0/0',
  'ifIndex': '4',
  'ifType': '32',
  'ifTypeDesc': 'FRAMERELAY',
  'ifspeed': '1544000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 1 second(s) 580 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:46',
  'mtu': '1500',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '',
  'showStatus': '-1',
  'statusDesc': 'Disabled'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'VoIP-Null0',
  'ifIndex': '5',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '10000000000',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 41 second(s) 300 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:26',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Null0',
  'ifIndex': '6',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '10000000000',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Foreign Exchange Station 0/1/0',
  'ifIndex': '8',
  'ifType': '102',
  'ifTypeDesc': 'VOICEFXS',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 33 second(s) 190 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:18',
  'mtu': '0',
  'operationStatus': '5',
  'operationStatusDesc': 'Dormant',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Foreign Exchange Station 0/1/1',
  'ifIndex': '9',
  'ifType': '102',
  'ifTypeDesc': 'VOICEFXS',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 31 second(s) 340 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:16',
  'mtu': '0',
  'operationStatus': '5',
  'operationStatusDesc': 'Dormant',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Foreign Exchange Station 0/1/2',
  'ifIndex': '10',
  'ifType': '102',
  'ifTypeDesc': 'VOICEFXS',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 33 second(s) 190 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:18',
  'mtu': '0',
  'operationStatus': '5',
  'operationStatusDesc': 'Dormant',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Foreign Exchange Station 0/1/3',
  'ifIndex': '11',
  'ifType': '102',
  'ifTypeDesc': 'VOICEFXS',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 33 second(s) 190 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:18',
  'mtu': '0',
  'operationStatus': '5',
  'operationStatusDesc': 'Dormant',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'POTS line from Telco',
  'ifDescription': 'Foreign Exchange Office 0/2/0',
  'ifIndex': '12',
  'ifType': '101',
  'ifTypeDesc': 'VOICEFXO',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 33 second(s) 480 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:18',
  'mtu': '0',
  'operationStatus': '5',
  'operationStatusDesc': 'Dormant',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '2',
  'adminStatusDesc': 'Down',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Foreign Exchange Office 0/2/1',
  'ifIndex': '13',
  'ifType': '101',
  'ifTypeDesc': 'VOICEFXO',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 33 second(s) 360 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:18',
  'mtu': '0',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '',
  'showStatus': '-1',
  'statusDesc': 'Disabled'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Over IP Peer: 2147483647',
  'ifIndex': '14',
  'ifType': '104',
  'ifTypeDesc': 'VOICEOVERIP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 46 second(s) 180 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:31',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Loopback0',
  'ifIndex': '15',
  'ifType': '24',
  'ifTypeDesc': 'SOFTWARELOOPBACK',
  'ifspeed': '8000000000',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 59 second(s) 600 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:44',
  'mtu': '1514',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 2',
  'ifIndex': '17',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 18 second(s) 480 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:03',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 3',
  'ifIndex': '18',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 18 second(s) 490 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:03',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 2000',
  'ifIndex': '19',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 18 second(s) 520 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:03',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/1',
  'ifIndex': '20',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20001',
  'ifIndex': '21',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 460 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/2',
  'ifIndex': '22',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20002',
  'ifIndex': '23',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 560 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/3',
  'ifIndex': '24',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20003',
  'ifIndex': '25',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 570 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/4',
  'ifIndex': '26',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20004',
  'ifIndex': '27',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 600 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/5',
  'ifIndex': '28',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20005',
  'ifIndex': '29',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 620 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/50',
  'ifIndex': '30',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20006',
  'ifIndex': '31',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 630 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/51',
  'ifIndex': '32',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20007',
  'ifIndex': '33',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 650 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/52',
  'ifIndex': '34',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20008',
  'ifIndex': '35',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 660 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/53',
  'ifIndex': '36',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20009',
  'ifIndex': '37',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 680 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/54',
  'ifIndex': '38',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20010',
  'ifIndex': '39',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 700 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/55',
  'ifIndex': '40',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20011',
  'ifIndex': '41',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 720 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/56',
  'ifIndex': '42',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20012',
  'ifIndex': '43',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 740 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/70',
  'ifIndex': '44',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20013',
  'ifIndex': '45',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 760 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'users_gateway',
  'ifDescription': 'FastEthernet0/0.15',
  'ifIndex': '48',
  'ifType': '135',
  'ifTypeDesc': 'L2VLAN',
  'ifspeed': '100000000',
  'ipHash': {'item': ['10.101.15.1', '255.255.255.0']},
  'lastChange': '19 day(s) 20 hour(s) 33 minute(s) 3 second(s) 460 millisecond(s)',
  'lastChangeTime': '2016-07-07 17:51:31',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1b:d4:47:1e:68',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'phones_gateway',
  'ifDescription': 'FastEthernet0/0.16',
  'ifIndex': '49',
  'ifType': '135',
  'ifTypeDesc': 'L2VLAN',
  'ifspeed': '100000000',
  'ipHash': {'item': ['10.101.16.1', '255.255.255.0']},
  'lastChange': '19 day(s) 20 hour(s) 33 minute(s) 35 second(s) 880 millisecond(s)',
  'lastChangeTime': '2016-07-07 17:52:03',
  'mtu': '1500',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1b:d4:47:1e:68',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/6',
  'ifIndex': '50',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20014',
  'ifIndex': '51',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 930 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/7',
  'ifIndex': '52',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20015',
  'ifIndex': '53',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 950 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '3',
  'adminStatusDesc': 'Testing',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'EFXS 50/0/8',
  'ifIndex': '54',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 0 second(s) 0 millisecond(s)',
  'lastChangeTime': '2016-01-25 18:31:26',
  'mtu': '0',
  'operationStatus': '4',
  'operationStatusDesc': 'Unknown',
  'phyAddress': '',
  'showStatus': '4',
  'statusDesc': 'Unknown'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'Voice Encapsulation (POTS) Peer: 20016',
  'ifIndex': '55',
  'ifType': '103',
  'ifTypeDesc': 'VOICEENCAP',
  'ifspeed': '0',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 19 second(s) 960 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:04',
  'mtu': '0',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '',
  'showStatus': '2',
  'statusDesc': 'Down'},
 {'adminStatus': '2',
  'adminStatusDesc': 'Down',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': '',
  'ifDescription': 'NVI0',
  'ifIndex': '56',
  'ifType': '1',
  'ifTypeDesc': 'OTHER',
  'ifspeed': '56000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 23 second(s) 340 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:08',
  'mtu': '1514',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '',
  'showStatus': '-1',
  'statusDesc': 'Disabled'}]"""

    get_dev_interface_url = "/imcrs/plat/res/device/" + str(devid) + \
                            "/interface?start=0&size=1000&desc=false&total=false"
    f_url = url + get_dev_interface_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            int_list = (json.loads(r.text))['interface']
            return int_list
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_interface: An Error has occured"


def get_dev_run_config(devid, auth, url):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current running config
    file as known by the HP IMC Base Platform ICC module for the target device.

    :param devid:  int or str value of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str which contains the entire content of the target device running configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"

    :rtype: str

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>get_dev_run_config('10', auth.creds, auth.url)
    '\r\n#\r\n version 5.20.99, Release 2221P20\r\n#\r\n sysname HP_5500EI\r\n#\r\n undo voice vlan mac-address 0001-e300-0000\r\n undo voice vlan mac-address 0003-6b00-0000\r\n undo voice vlan mac-address 0004-0d00-0000\r\n undo voice vlan mac-address 0060-b900-0000\r\n undo voice vlan mac-address 00d0-1e00-0000\r\n undo voice vlan mac-address 00e0-7500-0000\r\n undo voice vlan mac-address 00e0-bb00-0000\r\n voice vlan mac-address 0000-0000-0000 mask ff00-0000-0000\r\n undo voice vlan security enable\r\n#\r\n dhcp relay server-group 0 ip 10.10.10.212\r\n dhcp relay server-group 1 ip 10.101.0.20\r\n#\r\n irf domain 1\r\n irf mac-address persistent always\r\n irf auto-update enable\r\n irf link-delay 20\r\n irf member 1 priority 32\r\n#\r\n domain default enable dot1x \r\n#\r\n telnet server enable \r\n#\r\n irf-port load-sharing mode destination-mac source-mac \r\n#\r\n lldp compliance cdp\r\n#\r\n port-security enable \r\n#\r\n dot1x authentication-method pap\r\n#\r\n portal server SCEP2 ip 10.3.10.220 url http://10.3.10.220:8080/byod/deploy.jsf\r\n portal server onboarding ip 10.3.10.220 key cipher $c$3$E6rgxrTGAF/JCCdkVDwgCg2mMS78hHb4FXNNJm8= url http://10.3.10.220:8080/byod\r\n portal server SCEP ip 10.3.10.220 key cipher $c$3$pcK4ileNw1O1wdhJvGFR6m+m08igGg3FH8pv+cw= url http://10.3.10.220:8080/byod/deploy.jsf\r\n portal free-rule 0 source ip 10.10.101.0 mask 255.255.255.0 destination ip 10.3.1.220 mask 255.255.255.255\r\n portal free-rule 1 source ip 10.10.101.0 mask 255.255.255.0 destination ip 10.10.10.212 mask 255.255.255.255\r\n portal free-rule 2 source ip any destination ip 10.101.254.1 mask 255.255.255.255\r\n portal free-rule 3 source ip 10.10.105.0 mask 255.255.255.0 destination ip 10.10.10.212 mask 255.255.255.255\r\n portal free-rule 4 source ip 10.10.10.212 mask 255.255.255.255 destination ip any\r\n portal free-rule 5 source ip 10.101.0.200 mask 255.255.255.255 destination ip any\r\n portal free-rule 6 source ip 10.3.10.220 mask 255.255.255.255 destination ip any\r\n#\r\n mac-authentication domain dot1x\r\n#\r\n poe legacy enable pse 4\r\n#\r\n multicast routing-enable\r\n#\r\n password-recovery enable\r\n#\r\nacl number 2001 match-order auto\r\n rule 0 permit source 10.101.0.201 0 \r\nacl number 2500\r\n rule 1 permit \r\n#\r\nacl number 3000\r\n rule 1 deny ip source 10.101.0.200 0 destination 10.0.0.0 0.255.255.255 \r\n rule 2 permit ip source 10.101.0.200 0 \r\nacl number 3001 match-order auto\r\n rule 0 permit ip source 10.101.0.201 0 \r\nacl number 3015\r\n rule 0 permit udp destination-port eq snmp \r\n rule 5 permit udp destination-port eq dns \r\n rule 10 permit udp destination-port eq bootpc \r\n rule 15 permit udp destination-port eq bootps \r\n rule 20 permit tcp destination-port eq klogin \r\n rule 25 permit tcp destination-port eq kshell \r\nacl number 3500 match-order auto\r\n description ACL for blocking allowing internet access and email. Blocking all other internal addresses.\r\n rule 0 permit ip destination 0.0.0.0 0 \r\n rule 20 permit ip destination 10.101.0.200 0 \r\n rule 25 permit ip destination 10.101.0.201 0 \r\n rule 15 deny ip destination 192.168.0.0 0.0.255.255 \r\n rule 10 deny ip destination 172.16.0.0 0.15.255.255 \r\n rule 5 deny ip destination 10.0.0.0 0.255.255.255 \r\n#\r\nacl number 4000\r\n rule 0 permit source-mac 000a-9c51-33a8 000a-9c51-33a8\r\n#\r\nigmp-snooping\r\n#\r\nvlan 1\r\n name default\r\n#\r\nvlan 2\r\n name TenantABC\r\n#\r\nvlan 3\r\n description management\r\n name management\r\n#\r\nvlan 10\r\n description mgmt\r\n name mgmt\r\n igmp-snooping enable\r\n#\r\nvlan 11\r\n description simulate remote branch network\r\n name remotebranch\r\n#\r\nvlan 12\r\n description competitive testing network\r\n name competitive\r\n#\r\nvlan 13\r\n#\r\nvlan 15\r\n name users\r\n#\r\nvlan 16\r\n name phones\r\n#\r\nvlan 20\r\n description servers\r\n name servers\r\n#\r\nvlan 50\r\n#\r\nvlan 101\r\n description onboarding\r\n name onboarding\r\n#\r\nvlan 102\r\n name guest\r\n#\r\nvlan 103\r\n description guestmobile\r\n name guestmobile\r\n#\r\nvlan 105\r\n name scep\r\n#\r\nvlan 106\r\n name scepreg\r\n#\r\nvlan 110\r\n name NewVLAN\r\n#\r\nvlan 201\r\n#\r\nvlan 203\r\n#\r\nvlan 500\r\n name VLAN500\r\n#\r\nvlan 503\r\n name VLAN503\r\n#\r\nvlan 1010\r\n description FBRA Management VLAN\r\n name FBRAMGMT\r\n#\r\nvlan 1011\r\n description FBRA Servers VLAN\r\n name fbraservers\r\n#\r\nvlan 1012\r\n description FBRA Employee VLAN\r\n name FBRAemployee\r\n#\r\nvlan 1013\r\n description FBRA Guest VLAN\r\n name FBRAguest\r\n#\r\nvlan 1014\r\n description FBRA Registration VLAN\r\n name FBRAregistration\r\n#\r\nvlan 1015\r\n description FBRA Voice VLAN\r\n name FBRAvoice\r\n#\r\nvlan 2000\r\n name vsr240\r\n#\r\nvlan 2001\r\n name vsr241-1\r\n#\r\nvlan 2002\r\n name vsr-241-2\r\n#\r\nvlan 2003\r\n name vsr-242-1\r\n#\r\nvlan 2004\r\n name vsr-242-2\r\n#\r\nvlan 2005 to 2010\r\n#\r\nvlan 3010\r\n name ProvisionBranchVLAN10\r\n#\r\nradius scheme system\r\n server-type extended\r\n primary authentication 127.0.0.1 1645\r\n primary accounting 127.0.0.1 1646\r\n user-name-format without-domain\r\nradius scheme imcradius\r\n server-type extended\r\n primary authentication 10.3.10.220\r\n primary accounting 10.3.10.220\r\n key authentication cipher $c$3$rXKVE9pG05Lda2xcSpl6nrsYCkmBIW0kAdwEACg=\r\n key accounting cipher $c$3$YxLxR9RhvNJw1iP5DFdb+UiU0pVBWUBZ6ZU8m7g=\r\n user-name-format without-domain\r\n nas-ip 10.10.3.1\r\nradius scheme dot1x\r\n#\r\ndomain dot1x \r\n authentication default radius-scheme imcradius\r\n authorization default radius-scheme imcradius\r\n accounting default radius-scheme imcradius\r\n authentication login radius-scheme imcradius\r\n authorization login radius-scheme imcradius\r\n accounting login radius-scheme imcradius\r\n authentication lan-access radius-scheme imcradius\r\n authorization lan-access radius-scheme imcradius\r\n authentication portal radius-scheme imcradius\r\n authorization portal radius-scheme imcradius\r\n accounting portal radius-scheme imcradius\r\n access-limit disable \r\n state active \r\n idle-cut disable \r\n self-service-url disable \r\n accounting optional \r\ndomain system \r\n access-limit disable \r\n state active \r\n idle-cut disable \r\n self-service-url disable \r\n#\r\ntraffic classifier testaug15 operator and\r\ntraffic classifier For_Class operator and\r\n if-match dscp ef \r\n#\r\ntraffic behavior testaug15\r\ntraffic behavior For_Behav\r\n#\r\nqos policy test\r\n classifier testaug15 behavior testaug15\r\nqos policy Forrester_Test\r\n#\r\ndhcp server ip-pool sdn\r\n network 10.10.50.0 mask 255.255.255.0\r\n gateway-list 10.10.50.1 \r\n dns-list 10.101.254.1 10.10.10.212 \r\n#\r\ndhcp server ip-pool test\r\n option 242 ascii MCIPADD=192.168.42.1,MCPORT=1719,HTTPSRVR=192.168.42.1\r\n#\r\ndhcp server ip-pool vlan50\r\n network 10.101.50.0 mask 255.255.255.0\r\n gateway-list 10.101.50.1 \r\n dns-list 10.101.0.10 10.101.254.1 \r\n domain-name haw.int\r\n#\r\nuser-group system\r\n group-attribute allow-guest\r\nuser-group -interf\r\n#\r\nlocal-user admin\r\n password cipher $c$3$FUUTGlnspoBc+K32yEiJj/Hl9PCPF/f7Lxey\r\n authorization-attribute level 3\r\n service-type ssh telnet terminal\r\nlocal-user guest2\r\n password cipher $c$3$sCYBbRfLfr+n3G5W9GC98SK+MwENLiGsMw==\r\nlocal-user manager\r\n password cipher $c$3$H/4OBJArNH0CwNirmMs/iwez3yRyz3sitOY=\r\n authorization-attribute level 2\r\n service-type telnet terminal\r\nlocal-user monitor\r\n password cipher $c$3$bzWaOZUhgl+QJtl+3jQlFp2huhq5Wjn4V8o=\r\n authorization-attribute level 1\r\n service-type telnet terminal\r\nlocal-user wlanguest\r\n password cipher $c$3$iQp0DA8paeQufqntOUuKT6/FSjarGR/uY4HzLw==\r\n#\r\n stp instance 0 root primary\r\n stp enable\r\n#\r\npoe-profile powerdown 1\r\n#\r\ninterface Bridge-Aggregation1\r\n#\r\ninterface Bridge-Aggregation2\r\n port link-type trunk\r\n port trunk permit vlan all\r\n link-aggregation mode dynamic\r\n#\r\ninterface Bridge-Aggregation110\r\n#\r\ninterface NULL0\r\n#\r\ninterface LoopBack0\r\n ip address 192.168.1.221 255.255.255.255 \r\n#\r\ninterface LoopBack1\r\n ip address 172.16.3.10 255.255.255.255 \r\n#\r\ninterface Vlan-interface1\r\n ip address 10.101.0.221 255.255.255.0 \r\n igmp enable\r\n pim dm\r\n#\r\ninterface Vlan-interface2\r\n ip address 10.101.2.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface3\r\n ip address 10.10.3.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface10\r\n description mgmt\r\n ip address 10.10.10.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface11\r\n description remote_branch\r\n ip address 10.10.11.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface12\r\n description competitive\r\n ip address 10.10.12.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface13\r\n ip address 10.10.13.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface15\r\n ip address 10.101.15.254 255.255.255.0 \r\n#\r\ninterface Vlan-interface20\r\n description server router\r\n ip address 10.3.10.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface50\r\n ip address 10.102.1.2 255.255.255.0 \r\n#\r\ninterface Vlan-interface101\r\n description guest\r\n ip address 10.10.101.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n portal server onboarding method direct\r\n portal domain dot1x \r\n#\r\ninterface Vlan-interface102\r\n ip address 10.10.102.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface103\r\n ip address 10.10.103.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface105\r\n description scep\r\n ip address 10.10.105.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n portal server SCEP2 method direct\r\n portal domain dot1x \r\n#\r\ninterface Vlan-interface106\r\n ip address 10.10.106.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface201\r\n ip address 10.10.201.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface203\r\n ip address 10.10.203.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface500\r\n ip address 10.10.50.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface1010\r\n#\r\ninterface Vlan-interface2000\r\n ip address 172.16.2.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2001\r\n ip address 172.16.3.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2002\r\n ip address 172.16.4.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2003\r\n ip address 172.16.5.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2004\r\n ip address 172.16.6.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2007\r\n ip address 172.16.7.1 255.255.255.0 \r\n#\r\ninterface GigabitEthernet1/0/15\r\n port link-mode route\r\n description \' \'\r\n ip address 172.16.0.2 255.255.255.0 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/16\r\n port link-mode route\r\n description R1Br4Core - HP_5500EI\r\n ip address 172.16.11.1 255.255.255.252 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/17\r\n port link-mode route\r\n description R1Br3Core - HP_5500EI\r\n ip address 172.16.12.1 255.255.255.252 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/22\r\n port link-mode route\r\n ip address 10.20.10.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 1\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter interval 20\r\n#\r\ninterface GigabitEthernet2/0/23\r\n port link-mode route\r\n ip address 10.20.1.254 255.255.255.0 \r\n#\r\ninterface GigabitEthernet1/0/1\r\n port link-mode bridge\r\n description VMSynology - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/2\r\n port link-mode bridge\r\n description SynologyDS - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n lldp voice-vlan 2\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/3\r\n port link-mode bridge\r\n description I\'m a NMS Weenie\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/4\r\n port link-mode bridge\r\n description \' \'\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/5\r\n port link-mode bridge\r\n description ESX55-10.101.0.7 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/6\r\n port link-mode bridge\r\n description ESX55-10.101.0.6 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/7\r\n port link-mode bridge\r\n description ESX55-10.101.0.7 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/8\r\n port link-mode bridge\r\n description ESX55-10.101.0.6 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan 1 to 2 110 500 to 503\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n packet-filter 2500 inbound\r\n packet-filter 2500 outbound\r\n packet-filter 4000 inbound\r\n packet-filter 4000 outbound\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/9\r\n port link-mode bridge\r\n description \' \'\r\n#\r\ninterface GigabitEthernet1/0/10\r\n port link-mode bridge\r\n description Sentry3_5133a8 - HP_5500EI\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/11\r\n port link-mode bridge\r\n description Sentry3_5146c3 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp disable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/12\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/13\r\n port link-mode bridge\r\n description \' \'\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/14\r\n port link-mode bridge\r\n description HP-5406zl - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/18\r\n port link-mode bridge\r\n description Aruba3600 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/19\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/20\r\n port link-mode bridge\r\n description HP-3500yl-24G - HP_5500EI\r\n port access vlan 3010\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/21\r\n port link-mode bridge\r\n description \' \'\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/23\r\n port link-mode bridge\r\n description HP830_LSW - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp compliance admin-status cdp txrx\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/24\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/25\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/26\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/27\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/28\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet2/0/1\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/2\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/3\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/4\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/5\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/6\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/7\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/8\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/9\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/10\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/11\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/12\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/13\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/14\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/15\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/16\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan 1 502 to 503\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/17\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/18\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/19\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/20\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/21\r\n port link-mode bridge\r\n description HP_5500EI - HP_5500EI\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/22\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/24\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/25\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/26\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/27\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/28\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface Ten-GigabitEthernet1/1/1\r\n#\r\ninterface Ten-GigabitEthernet1/1/2\r\n#\r\ninterface Ten-GigabitEthernet2/1/1\r\n#\r\ninterface Ten-GigabitEthernet2/1/2\r\n#\r\ninterface Tunnel0\r\n#\r\nospf 1 router-id 10.101.0.221 \r\n area 0.0.0.0 \r\n  network 192.168.1.221 0.0.0.0 \r\n  network 172.16.0.0 0.0.255.255 \r\n  network 10.0.0.0 0.255.255.255 \r\n#\r\npim\r\n#\r\nnqa entry 1 1\r\n type voice\r\n  data-fill aaa\r\n  data-size 100\r\n  destination ip 10.12.10.10\r\n  destination port 1000\r\n  frequency 300000\r\n  probe packet-number 10\r\n  probe packet-timeout 3000\r\n  source ip 10.10.10.1\r\n  source port 1000\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 2 2\r\n type voice\r\n  data-fill aaa\r\n  data-size 100\r\n  destination ip 10.11.10.10\r\n  destination port 1000\r\n  frequency 300000\r\n  probe packet-number 10\r\n  probe packet-timeout 3000\r\n  source ip 10.10.10.1\r\n  source port 1000\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 3 3\r\n type tcp\r\n  destination ip 10.12.10.10\r\n  destination port 7\r\n  frequency 300000\r\n  probe count 10\r\n  source ip 10.101.0.221\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 4 4\r\n type tcp\r\n  destination ip 10.11.10.1\r\n  destination port 7\r\n  frequency 300000\r\n  probe count 10\r\n  source ip 10.101.0.221\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry admin nqatest\r\n type ftp\r\n#\r\nnqa entry admin test\r\n type icmp-echo\r\n#\r\nnqa entry admin testnqa\r\n type dns\r\n#\r\nnqa entry dns 1\r\n type dns\r\n  destination ip 4.2.2.2\r\n  resolve-target www.google.com\r\n#\r\nnqa entry ping 1\r\n#\r\n ip route-static 0.0.0.0 0.0.0.0 10.101.0.1\r\n ip route-static 0.0.0.0 0.0.0.0 10.101.254.1\r\n#\r\n info-center source SHELL channel 2 log level notifications\r\n info-center source ACL channel 2\r\n info-center source ACL channel 5\r\n info-center loghost 10.101.0.117 channel 5\r\n info-center loghost 10.101.0.200 channel 5\r\n info-center loghost 10.101.0.201\r\n info-center loghost 10.101.0.205\r\n#\r\n snmp-agent\r\n snmp-agent local-engineid 8000002B03001EC1DCFC41\r\n snmp-agent community read sec \r\n snmp-agent community read public  acl 2500\r\n snmp-agent community read secret  acl 2001\r\n snmp-agent community write private  acl 2500\r\n snmp-agent sys-info contact admin@lab.local\r\n snmp-agent sys-info location LAB\r\n snmp-agent sys-info version all\r\n snmp-agent group v3 SNMPv3Group authentication write-view ViewDefault\r\n snmp-agent target-host trap address udp-domain 10.10.10.222 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.10.12.13 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.190 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.191 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.192 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.195 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.20 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.200 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.201 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.202 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.203 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.205 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.21 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.220 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.222 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.235 params securityname public v2c\r\n snmp-agent usm-user v3 test managerpriv cipher authentication-mode md5 $c$3$vPQENBFY7mnHycVSEjB5QuolgAIiTMjclfJqg7ExE3hbPg==\r\n snmp-agent usm-user v3 v3user SNMPv3Group cipher authentication-mode sha $c$3$IRXOFGMEkuajbSoJDlTGgQ9mDfb9Z4Dj1x0i7/+Wbai7vFmNByI= privacy-mode aes128 $c$3$HkyPCeXzfROwHK4hK6xQMqI3PF9qXeBJGK6Xjcyl4iV9RA==\r\n#\r\n command-alias enable\r\n command-alias mapping display show\r\n command-alias mapping save wr\r\n command-alias mapping undo no\r\n command-alias mapping reboot reload\r\n command-alias mapping header banner\r\n command-alias mapping reset clear\r\n command-alias mapping acl access-list\r\n command-alias mapping port switchport\r\n command-alias mapping stp spanning-tree\r\n command-alias mapping snmp-agent snmp-server\r\n command-alias mapping user-interface line\r\n command-alias mapping return end\r\n command-alias mapping quit exit\r\n command-alias mapping sysname hostname\r\n command-alias mapping delete erase\r\n command-alias mapping info-center logging\r\n#\r\n dhcp server forbidden-ip 10.101.50.1 \r\n#\r\n dhcp enable \r\n#\r\n nqa schedule 1 1 start-time now lifetime forever \r\n nqa schedule 2 2 start-time now lifetime forever \r\n nqa schedule 3 3 start-time now lifetime forever \r\n nqa schedule 4 4 start-time now lifetime forever \r\n nqa server enable\r\n#\r\n ntp-service unicast-server 10.101.0.1\r\n ntp-service unicast-peer 10.101.0.220\r\n#\r\n ssh server enable\r\n sftp server enable\r\n#\r\n rmon event 1 description 3COM_RMON_EVENT trap public owner 3COM_4800G\r\n#\r\n ftp server enable\r\n#\r\n sflow agent ip 10.10.3.1\r\n sflow source ip 10.101.0.221\r\n sflow collector 1 ip 10.101.0.203 description "IMC 7.2"\r\n sflow collector 3 ip 10.101.0.205 description IMCAIO\r\n#\r\n load xml-configuration \r\n#\r\n load tr069-configuration\r\n#\r\nuser-interface aux 0\r\n authentication-mode scheme\r\nuser-interface aux 1\r\nuser-interface vty 0 4\r\n authentication-mode scheme\r\nuser-interface vty 5 15\r\n#\r\nirf-port 1/1\r\n port group interface Ten-GigabitEthernet1/1/1 mode normal\r\n#\r\nirf-port 1/2\r\n port group interface Ten-GigabitEthernet1/1/2 mode normal\r\n#\r\nirf-port 2/1\r\n port group interface Ten-GigabitEthernet2/1/1 mode normal\r\n#\r\nirf-port 2/2\r\n port group interface Ten-GigabitEthernet2/1/2 mode normal\r\n#\r\nreturn'


    """
    # checks to see if the imc credentials are already available
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devid) + "/currentRun"
    f_url = url + get_dev_run_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # print (r.status_code)
    try:
        if r.status_code == 200:
            try:
                run_conf = (json.loads(r.text))['content']
                return run_conf
            except:
                return "This features is no supported on this device"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_run_config: An Error has occured"


def get_dev_start_config(devId, auth, url):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current startup config
    file as known by the HP IMC Base Platform ICC module for the target device.

    :param devId:  int or str value of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str which contains the entire content of the target device startup configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"

    :retype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_start_config('10', auth.creds, auth.url)
    '\r\n#\r\n version 5.20.99, Release 2221P20\r\n#\r\n sysname HP_5500EI\r\n#\r\n undo voice vlan mac-address 0001-e300-0000\r\n undo voice vlan mac-address 0003-6b00-0000\r\n undo voice vlan mac-address 0004-0d00-0000\r\n undo voice vlan mac-address 0060-b900-0000\r\n undo voice vlan mac-address 00d0-1e00-0000\r\n undo voice vlan mac-address 00e0-7500-0000\r\n undo voice vlan mac-address 00e0-bb00-0000\r\n voice vlan mac-address 0000-0000-0000 mask ff00-0000-0000\r\n undo voice vlan security enable\r\n#\r\n dhcp relay server-group 0 ip 10.10.10.212\r\n dhcp relay server-group 1 ip 10.101.0.20\r\n#\r\n irf domain 1\r\n irf mac-address persistent always\r\n irf auto-update enable\r\n irf link-delay 20\r\n irf member 1 priority 32\r\n#\r\n domain default enable dot1x \r\n#\r\n telnet server enable \r\n#\r\n irf-port load-sharing mode destination-mac source-mac \r\n#\r\n lldp compliance cdp\r\n#\r\n port-security enable \r\n#\r\n dot1x authentication-method pap\r\n#\r\n portal server SCEP2 ip 10.3.10.220 url http://10.3.10.220:8080/byod/deploy.jsf\r\n portal server onboarding ip 10.3.10.220 key cipher $c$3$E6rgxrTGAF/JCCdkVDwgCg2mMS78hHb4FXNNJm8= url http://10.3.10.220:8080/byod\r\n portal server SCEP ip 10.3.10.220 key cipher $c$3$pcK4ileNw1O1wdhJvGFR6m+m08igGg3FH8pv+cw= url http://10.3.10.220:8080/byod/deploy.jsf\r\n portal free-rule 0 source ip 10.10.101.0 mask 255.255.255.0 destination ip 10.3.1.220 mask 255.255.255.255\r\n portal free-rule 1 source ip 10.10.101.0 mask 255.255.255.0 destination ip 10.10.10.212 mask 255.255.255.255\r\n portal free-rule 2 source ip any destination ip 10.101.254.1 mask 255.255.255.255\r\n portal free-rule 3 source ip 10.10.105.0 mask 255.255.255.0 destination ip 10.10.10.212 mask 255.255.255.255\r\n portal free-rule 4 source ip 10.10.10.212 mask 255.255.255.255 destination ip any\r\n portal free-rule 5 source ip 10.101.0.200 mask 255.255.255.255 destination ip any\r\n portal free-rule 6 source ip 10.3.10.220 mask 255.255.255.255 destination ip any\r\n#\r\n mac-authentication domain dot1x\r\n#\r\n poe legacy enable pse 4\r\n#\r\n multicast routing-enable\r\n#\r\n password-recovery enable\r\n#\r\nacl number 2001 match-order auto\r\n rule 0 permit source 10.101.0.201 0 \r\nacl number 2500\r\n rule 1 permit \r\n#\r\nacl number 3000\r\n rule 1 deny ip source 10.101.0.200 0 destination 10.0.0.0 0.255.255.255 \r\n rule 2 permit ip source 10.101.0.200 0 \r\nacl number 3001 match-order auto\r\n rule 0 permit ip source 10.101.0.201 0 \r\nacl number 3015\r\n rule 0 permit udp destination-port eq snmp \r\n rule 5 permit udp destination-port eq dns \r\n rule 10 permit udp destination-port eq bootpc \r\n rule 15 permit udp destination-port eq bootps \r\n rule 20 permit tcp destination-port eq klogin \r\n rule 25 permit tcp destination-port eq kshell \r\nacl number 3500 match-order auto\r\n description ACL for blocking allowing internet access and email. Blocking all other internal addresses.\r\n rule 0 permit ip destination 0.0.0.0 0 \r\n rule 20 permit ip destination 10.101.0.200 0 \r\n rule 25 permit ip destination 10.101.0.201 0 \r\n rule 15 deny ip destination 192.168.0.0 0.0.255.255 \r\n rule 10 deny ip destination 172.16.0.0 0.15.255.255 \r\n rule 5 deny ip destination 10.0.0.0 0.255.255.255 \r\n#\r\nacl number 4000\r\n rule 0 permit source-mac 000a-9c51-33a8 000a-9c51-33a8\r\n#\r\nigmp-snooping\r\n#\r\nvlan 1\r\n name default\r\n#\r\nvlan 2\r\n name TenantABC\r\n#\r\nvlan 3\r\n description management\r\n name management\r\n#\r\nvlan 10\r\n description mgmt\r\n name mgmt\r\n igmp-snooping enable\r\n#\r\nvlan 11\r\n description simulate remote branch network\r\n name remotebranch\r\n#\r\nvlan 12\r\n description competitive testing network\r\n name competitive\r\n#\r\nvlan 13\r\n#\r\nvlan 15\r\n name users\r\n#\r\nvlan 16\r\n name phones\r\n#\r\nvlan 20\r\n description servers\r\n name servers\r\n#\r\nvlan 50\r\n#\r\nvlan 101\r\n description onboarding\r\n name onboarding\r\n#\r\nvlan 102\r\n name guest\r\n#\r\nvlan 103\r\n description guestmobile\r\n name guestmobile\r\n#\r\nvlan 105\r\n name scep\r\n#\r\nvlan 106\r\n name scepreg\r\n#\r\nvlan 110\r\n name NewVLAN\r\n#\r\nvlan 201\r\n#\r\nvlan 203\r\n#\r\nvlan 500\r\n name VLAN500\r\n#\r\nvlan 503\r\n name VLAN503\r\n#\r\nvlan 1010\r\n description FBRA Management VLAN\r\n name FBRAMGMT\r\n#\r\nvlan 1011\r\n description FBRA Servers VLAN\r\n name fbraservers\r\n#\r\nvlan 1012\r\n description FBRA Employee VLAN\r\n name FBRAemployee\r\n#\r\nvlan 1013\r\n description FBRA Guest VLAN\r\n name FBRAguest\r\n#\r\nvlan 1014\r\n description FBRA Registration VLAN\r\n name FBRAregistration\r\n#\r\nvlan 1015\r\n description FBRA Voice VLAN\r\n name FBRAvoice\r\n#\r\nvlan 2000\r\n name vsr240\r\n#\r\nvlan 2001\r\n name vsr241-1\r\n#\r\nvlan 2002\r\n name vsr-241-2\r\n#\r\nvlan 2003\r\n name vsr-242-1\r\n#\r\nvlan 2004\r\n name vsr-242-2\r\n#\r\nvlan 2005 to 2010\r\n#\r\nvlan 3010\r\n name ProvisionBranchVLAN10\r\n#\r\nradius scheme system\r\n server-type extended\r\n primary authentication 127.0.0.1 1645\r\n primary accounting 127.0.0.1 1646\r\n user-name-format without-domain\r\nradius scheme imcradius\r\n server-type extended\r\n primary authentication 10.3.10.220\r\n primary accounting 10.3.10.220\r\n key authentication cipher $c$3$rXKVE9pG05Lda2xcSpl6nrsYCkmBIW0kAdwEACg=\r\n key accounting cipher $c$3$YxLxR9RhvNJw1iP5DFdb+UiU0pVBWUBZ6ZU8m7g=\r\n user-name-format without-domain\r\n nas-ip 10.10.3.1\r\nradius scheme dot1x\r\n#\r\ndomain dot1x \r\n authentication default radius-scheme imcradius\r\n authorization default radius-scheme imcradius\r\n accounting default radius-scheme imcradius\r\n authentication login radius-scheme imcradius\r\n authorization login radius-scheme imcradius\r\n accounting login radius-scheme imcradius\r\n authentication lan-access radius-scheme imcradius\r\n authorization lan-access radius-scheme imcradius\r\n authentication portal radius-scheme imcradius\r\n authorization portal radius-scheme imcradius\r\n accounting portal radius-scheme imcradius\r\n access-limit disable \r\n state active \r\n idle-cut disable \r\n self-service-url disable \r\n accounting optional \r\ndomain system \r\n access-limit disable \r\n state active \r\n idle-cut disable \r\n self-service-url disable \r\n#\r\ntraffic classifier testaug15 operator and\r\ntraffic classifier For_Class operator and\r\n if-match dscp ef \r\n#\r\ntraffic behavior testaug15\r\ntraffic behavior For_Behav\r\n#\r\nqos policy test\r\n classifier testaug15 behavior testaug15\r\nqos policy Forrester_Test\r\n#\r\ndhcp server ip-pool sdn\r\n network 10.10.50.0 mask 255.255.255.0\r\n gateway-list 10.10.50.1 \r\n dns-list 10.101.254.1 10.10.10.212 \r\n#\r\ndhcp server ip-pool test\r\n option 242 ascii MCIPADD=192.168.42.1,MCPORT=1719,HTTPSRVR=192.168.42.1\r\n#\r\ndhcp server ip-pool vlan50\r\n network 10.101.50.0 mask 255.255.255.0\r\n gateway-list 10.101.50.1 \r\n dns-list 10.101.0.10 10.101.254.1 \r\n domain-name haw.int\r\n#\r\nuser-group system\r\n group-attribute allow-guest\r\nuser-group -interf\r\n#\r\nlocal-user admin\r\n password cipher $c$3$FUUTGlnspoBc+K32yEiJj/Hl9PCPF/f7Lxey\r\n authorization-attribute level 3\r\n service-type ssh telnet terminal\r\nlocal-user guest2\r\n password cipher $c$3$sCYBbRfLfr+n3G5W9GC98SK+MwENLiGsMw==\r\nlocal-user manager\r\n password cipher $c$3$H/4OBJArNH0CwNirmMs/iwez3yRyz3sitOY=\r\n authorization-attribute level 2\r\n service-type telnet terminal\r\nlocal-user monitor\r\n password cipher $c$3$bzWaOZUhgl+QJtl+3jQlFp2huhq5Wjn4V8o=\r\n authorization-attribute level 1\r\n service-type telnet terminal\r\nlocal-user wlanguest\r\n password cipher $c$3$iQp0DA8paeQufqntOUuKT6/FSjarGR/uY4HzLw==\r\n#\r\n stp instance 0 root primary\r\n stp enable\r\n#\r\npoe-profile powerdown 1\r\n#\r\ninterface Bridge-Aggregation1\r\n#\r\ninterface Bridge-Aggregation2\r\n port link-type trunk\r\n port trunk permit vlan all\r\n link-aggregation mode dynamic\r\n#\r\ninterface Bridge-Aggregation110\r\n#\r\ninterface NULL0\r\n#\r\ninterface LoopBack0\r\n ip address 192.168.1.221 255.255.255.255 \r\n#\r\ninterface LoopBack1\r\n ip address 172.16.3.10 255.255.255.255 \r\n#\r\ninterface Vlan-interface1\r\n ip address 10.101.0.221 255.255.255.0 \r\n igmp enable\r\n pim dm\r\n#\r\ninterface Vlan-interface2\r\n ip address 10.101.2.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface3\r\n ip address 10.10.3.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface10\r\n description mgmt\r\n ip address 10.10.10.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface11\r\n description remote_branch\r\n ip address 10.10.11.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface12\r\n description competitive\r\n ip address 10.10.12.1 255.255.255.0 \r\n dhcp select relay\r\n#\r\ninterface Vlan-interface13\r\n ip address 10.10.13.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface15\r\n ip address 10.101.15.254 255.255.255.0 \r\n#\r\ninterface Vlan-interface20\r\n description server router\r\n ip address 10.3.10.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface50\r\n ip address 10.102.1.2 255.255.255.0 \r\n#\r\ninterface Vlan-interface101\r\n description guest\r\n ip address 10.10.101.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n portal server onboarding method direct\r\n portal domain dot1x \r\n#\r\ninterface Vlan-interface102\r\n ip address 10.10.102.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface103\r\n ip address 10.10.103.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface105\r\n description scep\r\n ip address 10.10.105.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n portal server SCEP2 method direct\r\n portal domain dot1x \r\n#\r\ninterface Vlan-interface106\r\n ip address 10.10.106.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface201\r\n ip address 10.10.201.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface203\r\n ip address 10.10.203.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface500\r\n ip address 10.10.50.1 255.255.255.0 \r\n dhcp relay server-select 0\r\n#\r\ninterface Vlan-interface1010\r\n#\r\ninterface Vlan-interface2000\r\n ip address 172.16.2.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2001\r\n ip address 172.16.3.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2002\r\n ip address 172.16.4.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2003\r\n ip address 172.16.5.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2004\r\n ip address 172.16.6.1 255.255.255.0 \r\n#\r\ninterface Vlan-interface2007\r\n ip address 172.16.7.1 255.255.255.0 \r\n#\r\ninterface GigabitEthernet1/0/15\r\n port link-mode route\r\n description \' \'\r\n ip address 172.16.0.2 255.255.255.0 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/16\r\n port link-mode route\r\n description R1Br4Core - HP_5500EI\r\n ip address 172.16.11.1 255.255.255.252 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/17\r\n port link-mode route\r\n description R1Br3Core - HP_5500EI\r\n ip address 172.16.12.1 255.255.255.252 \r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet1/0/22\r\n port link-mode route\r\n ip address 10.20.10.1 255.255.255.0 \r\n dhcp select relay\r\n dhcp relay server-select 1\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter interval 20\r\n#\r\ninterface GigabitEthernet2/0/23\r\n port link-mode route\r\n ip address 10.20.1.254 255.255.255.0 \r\n#\r\ninterface GigabitEthernet1/0/1\r\n port link-mode bridge\r\n description VMSynology - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/2\r\n port link-mode bridge\r\n description SynologyDS - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n lldp voice-vlan 2\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/3\r\n port link-mode bridge\r\n description I\'m a NMS Weenie\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/4\r\n port link-mode bridge\r\n description \' \'\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/5\r\n port link-mode bridge\r\n description ESX55-10.101.0.7 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/6\r\n port link-mode bridge\r\n description ESX55-10.101.0.6 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/7\r\n port link-mode bridge\r\n description ESX55-10.101.0.7 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/8\r\n port link-mode bridge\r\n description ESX55-10.101.0.6 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan 1 to 2 110 500 to 503\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n packet-filter 2500 inbound\r\n packet-filter 2500 outbound\r\n packet-filter 4000 inbound\r\n packet-filter 4000 outbound\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/9\r\n port link-mode bridge\r\n description \' \'\r\n#\r\ninterface GigabitEthernet1/0/10\r\n port link-mode bridge\r\n description Sentry3_5133a8 - HP_5500EI\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/11\r\n port link-mode bridge\r\n description Sentry3_5146c3 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp disable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/12\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/13\r\n port link-mode bridge\r\n description \' \'\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/14\r\n port link-mode bridge\r\n description HP-5406zl - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp management-address-tlv 10.101.0.221\r\n lldp compliance admin-status cdp txrx\r\n lldp management-address-format string\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/18\r\n port link-mode bridge\r\n description Aruba3600 - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/19\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/20\r\n port link-mode bridge\r\n description HP-3500yl-24G - HP_5500EI\r\n port access vlan 3010\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/21\r\n port link-mode bridge\r\n description \' \'\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/23\r\n port link-mode bridge\r\n description HP830_LSW - HP_5500EI\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n lldp compliance admin-status cdp txrx\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/24\r\n port link-mode bridge\r\n description \' \'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n poe enable\r\n stp edged-port enable\r\n sflow sampling-rate 1000 \r\n sflow flow collector 1\r\n sflow flow max-header 512\r\n sflow counter interval 20\r\n sflow counter collector 1\r\n#\r\ninterface GigabitEthernet1/0/25\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/26\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/27\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet1/0/28\r\n port link-mode bridge\r\n description \' \'\r\n shutdown\r\n broadcast-suppression pps 3000\r\n undo jumboframe enable\r\n stp edged-port enable\r\n#\r\ninterface GigabitEthernet2/0/1\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/2\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/3\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/4\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/5\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/6\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/7\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/8\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan all\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/9\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/10\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/11\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/12\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/13\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/14\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/15\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/16\r\n port link-mode bridge\r\n description \'\'\r\n port link-type trunk\r\n port trunk permit vlan 1 502 to 503\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/17\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/18\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/19\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/20\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/21\r\n port link-mode bridge\r\n description HP_5500EI - HP_5500EI\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/22\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/24\r\n port link-mode bridge\r\n description \'\'\r\n lldp compliance admin-status cdp txrx\r\n#\r\ninterface GigabitEthernet2/0/25\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/26\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/27\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface GigabitEthernet2/0/28\r\n port link-mode bridge\r\n shutdown\r\n#\r\ninterface Ten-GigabitEthernet1/1/1\r\n#\r\ninterface Ten-GigabitEthernet1/1/2\r\n#\r\ninterface Ten-GigabitEthernet2/1/1\r\n#\r\ninterface Ten-GigabitEthernet2/1/2\r\n#\r\ninterface Tunnel0\r\n#\r\nospf 1 router-id 10.101.0.221 \r\n area 0.0.0.0 \r\n  network 192.168.1.221 0.0.0.0 \r\n  network 172.16.0.0 0.0.255.255 \r\n  network 10.0.0.0 0.255.255.255 \r\n#\r\npim\r\n#\r\nnqa entry 1 1\r\n type voice\r\n  data-fill aaa\r\n  data-size 100\r\n  destination ip 10.12.10.10\r\n  destination port 1000\r\n  frequency 300000\r\n  probe packet-number 10\r\n  probe packet-timeout 3000\r\n  source ip 10.10.10.1\r\n  source port 1000\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 2 2\r\n type voice\r\n  data-fill aaa\r\n  data-size 100\r\n  destination ip 10.11.10.10\r\n  destination port 1000\r\n  frequency 300000\r\n  probe packet-number 10\r\n  probe packet-timeout 3000\r\n  source ip 10.10.10.1\r\n  source port 1000\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 3 3\r\n type tcp\r\n  destination ip 10.12.10.10\r\n  destination port 7\r\n  frequency 300000\r\n  probe count 10\r\n  source ip 10.101.0.221\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry 4 4\r\n type tcp\r\n  destination ip 10.11.10.1\r\n  destination port 7\r\n  frequency 300000\r\n  probe count 10\r\n  source ip 10.101.0.221\r\n  tos 10\r\n  ttl 10\r\n#\r\nnqa entry admin nqatest\r\n type ftp\r\n#\r\nnqa entry admin test\r\n type icmp-echo\r\n#\r\nnqa entry admin testnqa\r\n type dns\r\n#\r\nnqa entry dns 1\r\n type dns\r\n  destination ip 4.2.2.2\r\n  resolve-target www.google.com\r\n#\r\nnqa entry ping 1\r\n#\r\n ip route-static 0.0.0.0 0.0.0.0 10.101.0.1\r\n ip route-static 0.0.0.0 0.0.0.0 10.101.254.1\r\n#\r\n info-center source SHELL channel 2 log level notifications\r\n info-center source ACL channel 2\r\n info-center source ACL channel 5\r\n info-center loghost 10.101.0.117 channel 5\r\n info-center loghost 10.101.0.200 channel 5\r\n info-center loghost 10.101.0.201\r\n info-center loghost 10.101.0.205\r\n#\r\n snmp-agent\r\n snmp-agent local-engineid 8000002B03001EC1DCFC41\r\n snmp-agent community read sec \r\n snmp-agent community read public  acl 2500\r\n snmp-agent community read secret  acl 2001\r\n snmp-agent community write private  acl 2500\r\n snmp-agent sys-info contact admin@lab.local\r\n snmp-agent sys-info location LAB\r\n snmp-agent sys-info version all\r\n snmp-agent group v3 SNMPv3Group authentication write-view ViewDefault\r\n snmp-agent target-host trap address udp-domain 10.10.10.222 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.10.12.13 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.190 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.191 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.192 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.195 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.20 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.200 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.201 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.202 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.203 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.101.0.205 params securityname public\r\n snmp-agent target-host trap address udp-domain 10.101.0.21 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.220 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.222 params securityname public v2c\r\n snmp-agent target-host trap address udp-domain 10.3.10.235 params securityname public v2c\r\n snmp-agent usm-user v3 test managerpriv cipher authentication-mode md5 $c$3$vPQENBFY7mnHycVSEjB5QuolgAIiTMjclfJqg7ExE3hbPg==\r\n snmp-agent usm-user v3 v3user SNMPv3Group cipher authentication-mode sha $c$3$IRXOFGMEkuajbSoJDlTGgQ9mDfb9Z4Dj1x0i7/+Wbai7vFmNByI= privacy-mode aes128 $c$3$HkyPCeXzfROwHK4hK6xQMqI3PF9qXeBJGK6Xjcyl4iV9RA==\r\n#\r\n command-alias enable\r\n command-alias mapping display show\r\n command-alias mapping save wr\r\n command-alias mapping undo no\r\n command-alias mapping reboot reload\r\n command-alias mapping header banner\r\n command-alias mapping reset clear\r\n command-alias mapping acl access-list\r\n command-alias mapping port switchport\r\n command-alias mapping stp spanning-tree\r\n command-alias mapping snmp-agent snmp-server\r\n command-alias mapping user-interface line\r\n command-alias mapping return end\r\n command-alias mapping quit exit\r\n command-alias mapping sysname hostname\r\n command-alias mapping delete erase\r\n command-alias mapping info-center logging\r\n#\r\n dhcp server forbidden-ip 10.101.50.1 \r\n#\r\n dhcp enable \r\n#\r\n nqa schedule 1 1 start-time now lifetime forever \r\n nqa schedule 2 2 start-time now lifetime forever \r\n nqa schedule 3 3 start-time now lifetime forever \r\n nqa schedule 4 4 start-time now lifetime forever \r\n nqa server enable\r\n#\r\n ntp-service unicast-server 10.101.0.1\r\n ntp-service unicast-peer 10.101.0.220\r\n#\r\n ssh server enable\r\n sftp server enable\r\n#\r\n rmon event 1 description 3COM_RMON_EVENT trap public owner 3COM_4800G\r\n#\r\n ftp server enable\r\n#\r\n sflow agent ip 10.10.3.1\r\n sflow source ip 10.101.0.221\r\n sflow collector 1 ip 10.101.0.203 description "IMC 7.2"\r\n sflow collector 3 ip 10.101.0.205 description IMCAIO\r\n#\r\n load xml-configuration \r\n#\r\n load tr069-configuration\r\n#\r\nuser-interface aux 0\r\n authentication-mode scheme\r\nuser-interface aux 1\r\nuser-interface vty 0 4\r\n authentication-mode scheme\r\nuser-interface vty 5 15\r\n#\r\nirf-port 1/1\r\n port group interface Ten-GigabitEthernet1/1/1 mode normal\r\n#\r\nirf-port 1/2\r\n port group interface Ten-GigabitEthernet1/1/2 mode normal\r\n#\r\nirf-port 2/1\r\n port group interface Ten-GigabitEthernet2/1/1 mode normal\r\n#\r\nirf-port 2/2\r\n port group interface Ten-GigabitEthernet2/1/2 mode normal\r\n#\r\nreturn'



    """
    # checks to see if the imc credentials are already available
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devId) + "/currentStart"
    f_url = url + get_dev_run_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if r.status_code == 200:
            try:
                start_conf = (json.loads(r.text))['content']
                return start_conf
            except:
                return "Start Conf not supported on this device"

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_run_config: An Error has occured"




"""
This section contains functions which operate at the interface level
"""

def get_all_interface_details(devId, auth, url):
    """
    function takes the devId of a specific device and the ifindex value assigned to a specific interface
    and issues a RESTFUL call to get the interface details
    file as known by the HP IMC Base Platform ICC module for the target device.

    :param devId:  int or str value of the devId of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dict objects which contains the details of all interfaces on the target device

    :retype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>get_all_interface_details('10', auth.creds, auth.url)
    [{'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'VMSynology - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/1',
  'ifIndex': '1',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '5 day(s) 12 hour(s) 50 minute(s) 41 second(s) 750 millisecond(s)',
  'lastChangeTime': '2016-06-23 10:10:05',
  'mtu': '9216',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:17',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'SynologyDS - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/2',
  'ifIndex': '2',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '5 day(s) 13 hour(s) 22 minute(s) 55 second(s) 710 millisecond(s)',
  'lastChangeTime': '2016-06-23 10:42:19',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:18',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': "I'm a NMS Weenie",
  'ifDescription': 'GigabitEthernet1/0/3',
  'ifIndex': '3',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 48 second(s) 670 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:58',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:19',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': "' '",
  'ifDescription': 'GigabitEthernet1/0/4',
  'ifIndex': '4',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 48 second(s) 840 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:58',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:1a',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'ESX55-10.101.0.7 - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/5',
  'ifIndex': '5',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 5 minute(s) 8 second(s) 590 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:23:18',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:1b',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'ESX55-10.101.0.6 - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/6',
  'ifIndex': '6',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 10 minute(s) 47 second(s) 800 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:28:57',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:1c',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'ESX55-10.101.0.7 - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/7',
  'ifIndex': '7',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 5 minute(s) 8 second(s) 940 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:23:18',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:1d',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'ESX55-10.101.0.6 - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/8',
  'ifIndex': '8',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 10 minute(s) 48 second(s) 150 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:28:58',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:1e',
  'showStatus': '1',
  'statusDesc': 'Up'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': "' '",
  'ifDescription': 'GigabitEthernet1/0/9',
  'ifIndex': '9',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '1000000000',
  'lastChange': '0 day(s) 0 hour(s) 0 minute(s) 25 second(s) 930 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:18:35',
  'mtu': '9216',
  'operationStatus': '2',
  'operationStatusDesc': 'Down',
  'phyAddress': '00:1e:c1:dc:fc:1f',
  'showStatus': '2',
  'statusDesc': 'Down'},
 {'adminStatus': '1',
  'adminStatusDesc': 'Up',
  'appointedSpeed': '-1',
  'filterTrapStatus': '0',
  'ifAlias': 'Sentry3_5133a8 - HP_5500EI',
  'ifDescription': 'GigabitEthernet1/0/10',
  'ifIndex': '10',
  'ifType': '6',
  'ifTypeDesc': 'ETHERNETCSMACD',
  'ifspeed': '100000000',
  'lastChange': '0 day(s) 0 hour(s) 1 minute(s) 46 second(s) 760 millisecond(s)',
  'lastChangeTime': '2016-06-17 21:19:56',
  'mtu': '1536',
  'operationStatus': '1',
  'operationStatusDesc': 'Up',
  'phyAddress': '00:1e:c1:dc:fc:20',
  'showStatus': '1',
  'statusDesc': 'Up'}]

     """

    get_all_interface_details_url = "/imcrs/plat/res/device/" + str(devId) + "/interface/?start=0&size=1000&desc=false&total=false"
    f_url = url + get_all_interface_details_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_details = (json.loads(r.text))
            return dev_details['interface']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_interface_details: An Error has occured"






def get_interface_details(devId, ifIndex, auth, url):
    """
    function takes the devId of a specific device and the ifindex value assigned to a specific interface
    and issues a RESTFUL call to get the interface details
    file as known by the HP IMC Base Platform ICC module for the target device.

    :param devId:  int or str value of the devId of the target device

    :param ifIndex: int or str value of the ifIndex of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: dict which contains the details of the target interface"

    :retype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>get_interface_details('10', '1', auth.creds, auth.url)
    {'adminStatus': '1',
     'adminStatusDesc': 'Up',
     'appointedSpeed': '-1',
     'filterTrapStatus': '0',
     'ifAlias': 'VMSynology - HP_5500EI',
     'ifDescription': 'GigabitEthernet1/0/1',
     'ifIndex': '1',
     'ifType': '6',
     'ifTypeDesc': 'ETHERNETCSMACD',
     'ifspeed': '1000000000',
     'lastChange': '5 day(s) 12 hour(s) 50 minute(s) 41 second(s) 750 millisecond(s)',
     'lastChangeTime': '2016-06-23 10:10:05',
     'mtu': '9216',
     'operationStatus': '1',
     'operationStatusDesc': 'Up',
     'phyAddress': '00:1e:c1:dc:fc:17',
     'showStatus': '1',
     'statusDesc': 'Up'}

     """

    get_interface_details_url = "/imcrs/plat/res/device/" + str(devId) + "/interface/" + str(ifIndex)
    f_url = url + get_interface_details_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_details = (json.loads(r.text))
            return dev_details
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_interface_details: An Error has occured"



def set_inteface_down(devid, ifindex, auth, url):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to " shut" the specifie
    d interface on the target device.
    :param devid: int or str value of the target device

    :param ifindex: int or str value of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP status code 204 with no values.

    :rtype:int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>set_inteface_down('10', '9', auth.creds, auth.url)
    204
    """
    set_int_down_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/down"
    f_url = url + set_int_down_url
    try:
        r = requests.put(f_url, auth=auth,
                         headers=HEADERS)  # creates the URL using the payload variable as the contents
        print(r.status_code)
        if r.status_code == 204:
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " set_inteface_down: An Error has occured"


def set_inteface_up(devid, ifindex, auth, url):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to "undo shut" the spec
    ified interface on the target device.

    :param devid: int or str value of the target device

    :param ifindex: int or str value of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP status code 204 with no values.

    :rype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>set_inteface_up('10', '9', auth.creds, auth.url)
    204

    """
    set_int_up_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/up"
    f_url = url + set_int_up_url
    try:
        r = requests.put(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
        if r.status_code == 204:
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " set_inteface_up: An Error has occured"


def get_dev_mac_learn(devid, auth, url):
    '''
    function takes devid of specific device and issues a RESTFUL call to gather the current IP-MAC learning entries on
    the target device.

    :param devid: int value of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dict objects which contain the mac learn table of target device id

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_mac_learn('10', auth.creds, auth.url)
    [{'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/1',
  'ifIndex': '1',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/1',
  'learnIp': '10.101.0.50',
  'learnMac': '00:11:32:11:da:57',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/2',
  'ifIndex': '2',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/2',
  'learnIp': '10.101.0.51',
  'learnMac': '00:11:32:10:03:8b',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/3',
  'ifIndex': '3',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/3',
  'learnIp': '10.101.0.10',
  'learnMac': '14:58:d0:60:61:04',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/4',
  'ifIndex': '4',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/4',
  'learnIp': '10.101.0.11',
  'learnMac': '14:58:d0:60:a4:e6',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/5',
  'ifIndex': '5',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/5',
  'learnIp': '',
  'learnMac': '00:50:56:59:dd:d8',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/5',
  'ifIndex': '5',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/5',
  'learnIp': '10.101.0.100',
  'learnMac': '00:50:56:66:7d:73',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/5',
  'ifIndex': '5',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/5',
  'learnIp': '10.101.0.7',
  'learnMac': 'c4:34:6b:b9:dd:d8',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/6',
  'ifIndex': '6',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/6',
  'learnIp': '',
  'learnMac': '00:50:56:59:4f:bc',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/6',
  'ifIndex': '6',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/6',
  'learnIp': '10.101.0.113',
  'learnMac': '00:50:56:64:8e:db',
  'vlanId': '1'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/6',
  'ifIndex': '6',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/6',
  'learnIp': '10.101.0.20',
  'learnMac': '00:50:56:b5:7f:66',
  'vlanId': '1'}]
    '''
    get_dev_mac_learn_url='/imcrs/res/access/ipMacLearn/'+str(devid)
    f_url = url+get_dev_mac_learn_url
    try:
        r = requests.get(f_url, auth=auth, headers=HEADERS)
        if r.status_code == 200:
            if len(r.text) < 1:
                mac_learn_query = {}
                return mac_learn_query
            else:
                mac_learn_query = (json.loads(r.text))['ipMacLearnResult']
                return mac_learn_query
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_mac_learn: An Error has occured"



def run_dev_cmd(devid, cmd_list, auth, url):
    '''
    Function takes devid of target device and a sequential list of strings which define the specific commands to be run
    on the target device and returns a str object containing the output of the commands.
    :param devid: int devid of the target device

    :param cmd_list: list of strings

    :return: str containing the response of the commands

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> cmd_list = ['display version']

    >>> run_dev_cmd('10', cmd_list, auth.creds, auth.url)
    {'cmdlist': {'cmd': 'display version'},
 'content': 'HPE Comware Platform Software\r\nComware Software, Version 5.20.99, Release 2221P20\r\nCopyright (c) 2010-2015 Hewlett Packard Enterprise Development LP\r\nHP A5500-24G-PoE+ EI Switch with 2 Interface Slots uptime is 3 weeks, 2 days, 12 hours, 58 minutes\r\n\r\nHP A5500-24G-PoE+ EI Switch with 2 Interface Slots with 1 Processor\r\n256M    bytes SDRAM\r\n32768K  bytes Flash Memory\r\n\r\nHardware Version is REV.C\r\nCPLD Version is 002\r\nBootrom Version is 721\r\n[SubSlot 0] 24GE+4SFP+POE Hardware Version is REV.C\r\n[SubSlot 1] 2 CX4 Hardware Version is REV.A\r\n',
 'deviceId': '10',
 'success': 'true'}
    '''
    run_dev_cmd_url = '/imcrs/icc/confFile/executeCmd'
    f_url = url + run_dev_cmd_url
    cmd_list = _make_cmd_list(cmd_list)
    payload = '''{ "deviceId" : "'''+str(devid) + '''",
                   "cmdlist" : { "cmd" :
                   ['''+ cmd_list + ''']

                   }
                   }'''
    r = requests.post(f_url, data=payload, auth=auth, headers=HEADERS)
    if r.status_code == 200:
        if len(r.text) < 1:
            return ''
        else:
            return json.loads(r.text)

def _make_cmd_list(cmd_list):
    '''
    Helper function to easily create the proper json formated string from a list of strs
    :param cmd_list: list of strings
    :return: str json formatted
    '''
    cmd = ''
    for i in cmd_list:
         cmd= cmd+ '"' + i + '",'
    cmd = cmd[:-1]
    return cmd
