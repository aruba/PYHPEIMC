#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import requests
import json

HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}


headers = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_dev_alarms(devId, auth, url):
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

    >>> dev_alarms = get_dev_alarms('10', auth.creds, auth.url)

    >>> type(dev_alarms)
    <class 'list'>

    >>> assert 'ackStatus' in dev_alarms[0]

    """
    # checks to see if the imc credentials are already available
    get_dev_alarm_url = "/imcrs/fault/alarm?operatorName=admin&deviceId=" + \
                        str(devId) + "&desc=false"
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

    >>> type(real_time_alarm)
    <class 'list'>
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

    >>> type(all_alarms)
    <class 'list'>
    >>> assert 'ackStatus' in all_alarms[0]


    [{'OID': '1.3.6.1.4.1.11.2.14.11.15.2.75.5.3.1.6.7',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '1001',
  'alarmCategoryDesc': 'Wireless Device Alarm',
  'alarmDesc': 'The device(MAC Address:   F4 B7 E2 95 A0 CD) is detected to be flooding the network. Attack Frame Type: Probe Request.',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187616',
  'alarmLevel': '3',
  'alarmLevelDesc': 'Minor',
  'deviceId': '31',
  'deviceIp': '10.10.10.5',
  'deviceName': 'HP830_WSC',
  'faultTime': '1469471298',
  'faultTimeDesc': '2016-07-25 14:28:18',
  'holdInfo': '',
  'id': '187616',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Attack MAC=  F4 B7 E2 95 A0 CD;Attack Frame Type=Probe Request',
  'parentId': '0',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.2.2.6.1',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '15',
  'alarmCategoryDesc': 'Other Alarms from NMS',
  'alarmDesc': 'iMC alarm system has received 100 alarms about the event (hh3cPeriodicalTrap) of device ADP_Initial_Config(10.20.10.10) from 2016-07-25 12:56:01 to 2016-07-25 14:36:01.',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187625',
  'alarmLevel': '4',
  'alarmLevelDesc': 'Warning',
  'deviceId': '0',
  'deviceIp': '127.0.0.1',
  'deviceName': 'NMS',
  'faultTime': '1469471761',
  'faultTimeDesc': '2016-07-25 14:36:01',
  'id': '187625',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': 'Start Time=2016-07-25 12:56:01;Stop Time=2016-07-25 14:36:01;Times=100;*Repeat Event Name=hh3cPeriodicalTrap;*Device IP=10.20.10.10;Device Name=ADP_Initial_Config',
  'parentId': '173953',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.2.2.6.1',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '15',
  'alarmCategoryDesc': 'Other Alarms from NMS',
  'alarmDesc': 'iMC alarm system has received 100 alarms about the event (Some ambient device interferes) of device HP830_WSC(10.10.10.5) from 2016-07-25 14:07:06 to 2016-07-25 14:40:21.',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187626',
  'alarmLevel': '4',
  'alarmLevelDesc': 'Warning',
  'deviceId': '0',
  'deviceIp': '127.0.0.1',
  'deviceName': 'NMS',
  'faultTime': '1469472021',
  'faultTimeDesc': '2016-07-25 14:40:21',
  'id': '187626',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': 'Start Time=2016-07-25 14:07:06;Stop Time=2016-07-25 14:40:21;Times=100;*Repeat Event Name=Some ambient device interferes;*Device IP=10.10.10.5;Device Name=HP830_WSC',
  'parentId': '173953',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.3.2.6.11',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '9',
  'alarmCategoryDesc': 'Traffic Analysis and Audit Alarm',
  'alarmDesc': 'The in direction of interface GigabitEthernet1/0/23 on device 192.168.1.221 at 2016-07-25 14:32:00 is greater than the baseline(2.87 Mbps).',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187631',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '67',
  'deviceIp': '10.101.0.203',
  'deviceName': 'HPEIMC72WIN2K12R2',
  'faultTime': '1469472140',
  'faultTimeDesc': '2016-07-25 14:42:20',
  'holdInfo': '',
  'id': '187631',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': '*UNBA Server Name=NMS;*UNBA Server IP=127.0.0.1;*Alarm Object Name=The in direction of interface GigabitEthernet1/0/23 on device 192.168.1.221;Alarm Occur Time=2016-07-25 14:32:00;Current Flow Speed=48.38 Mbps;Alarm Severity=2;Threshold Speed=2.87 Mbps;Device IP=192.168.1.221;Interface Index=23;Interface Name=GigabitEthernet1/0/23;Flow Direction=1',
  'parentId': '0',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.3.2.6.11',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '9',
  'alarmCategoryDesc': 'Traffic Analysis and Audit Alarm',
  'alarmDesc': 'The out direction of interface GigabitEthernet1/0/2 on device 192.168.1.221 at 2016-07-25 14:32:00 is greater than the baseline(1.78 Mbps).',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187632',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '67',
  'deviceIp': '10.101.0.203',
  'deviceName': 'HPEIMC72WIN2K12R2',
  'faultTime': '1469472140',
  'faultTimeDesc': '2016-07-25 14:42:20',
  'holdInfo': '',
  'id': '187632',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': '*UNBA Server Name=NMS;*UNBA Server IP=127.0.0.1;*Alarm Object Name=The out direction of interface GigabitEthernet1/0/2 on device 192.168.1.221;Alarm Occur Time=2016-07-25 14:32:00;Current Flow Speed=48.79 Mbps;Alarm Severity=2;Threshold Speed=1.78 Mbps;Device IP=192.168.1.221;Interface Index=2;Interface Name=GigabitEthernet1/0/2;Flow Direction=0',
  'parentId': '0',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.2.2.6.1',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '15',
  'alarmCategoryDesc': 'Other Alarms from NMS',
  'alarmDesc': 'iMC alarm system has received 100 alarms about the event (Some ambient AP interferes) of device HP830_WSC(10.10.10.5) from 2016-07-25 14:14:00 to 2016-07-25 14:47:55.',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187637',
  'alarmLevel': '4',
  'alarmLevelDesc': 'Warning',
  'deviceId': '0',
  'deviceIp': '127.0.0.1',
  'deviceName': 'NMS',
  'faultTime': '1469472475',
  'faultTimeDesc': '2016-07-25 14:47:55',
  'id': '187637',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': 'Start Time=2016-07-25 14:14:00;Stop Time=2016-07-25 14:47:55;Times=100;*Repeat Event Name=Some ambient AP interferes;*Device IP=10.10.10.5;Device Name=HP830_WSC',
  'parentId': '173953',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.4.1.25506.4.2.2.2.6.1',
  'ackStatus': '0',
  'ackStatusDesc': 'Unacknowledged',
  'ackTime': '0',
  'ackTimeDesc': '',
  'ackUserName': '',
  'alarmCategory': '15',
  'alarmCategoryDesc': 'Other Alarms from NMS',
  'alarmDesc': 'iMC alarm system has received 100 alarms about the event (Some ambient device interferes) of device HP830_WSC(10.10.10.5) from 2016-07-25 14:40:21 to 2016-07-25 15:15:50.',
  'alarmDetail': 'http://10.101.0.203:8080/imcrs/fault/alarm/187654',
  'alarmLevel': '4',
  'alarmLevelDesc': 'Warning',
  'deviceId': '0',
  'deviceIp': '127.0.0.1',
  'deviceName': 'NMS',
  'faultTime': '1469474150',
  'faultTimeDesc': '2016-07-25 15:15:50',
  'id': '187654',
  'originalType': '3',
  'originalTypeDesc': 'iMC',
  'paras': 'Start Time=2016-07-25 14:40:21;Stop Time=2016-07-25 15:15:50;Times=100;*Repeat Event Name=Some ambient device interferes;*Device IP=10.10.10.5;Device Name=HP830_WSC',
  'parentId': '173953',
  'recStatus': '0',
  'recStatusDesc': 'Unrecovered',
  'recTime': '0',
  'recTimeDesc': '',
  'recUserName': '',
  'remark': '',
  'somState': '0'}]
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



