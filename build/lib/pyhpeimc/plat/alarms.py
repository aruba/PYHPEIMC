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

    >>> get_dev_alarms('10', auth.creds.auth.url)
    [{'OID': '1.3.6.1.6.3.1.1.5.3.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/23 is UP.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160612',
  'alarmLevel': '5',
  'alarmLevelDesc': 'Info',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467765645',
  'faultTimeDesc': '2016-07-05 20:40:45',
  'holdInfo': '',
  'id': '160612',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=85;Interface Description=GigabitEthernet2/0/23;Interface Admin Status=1;Interface Operate Status=1',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467765645',
  'recTimeDesc': '2016-07-05 20:40:45',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.2.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/23 is DOWN.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160539',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467747889',
  'faultTimeDesc': '2016-07-05 15:44:49',
  'holdInfo': '',
  'id': '160539',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=85;Interface Description=GigabitEthernet2/0/23;Interface Admin Status=1;Interface Operate Status=2',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467765645',
  'recTimeDesc': '2016-07-05 20:40:45',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.2.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/20 is DOWN.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160524',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467747461',
  'faultTimeDesc': '2016-07-05 15:37:41',
  'holdInfo': '',
  'id': '160524',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=82;Interface Description=GigabitEthernet2/0/20;Interface Admin Status=1;Interface Operate Status=2',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467854218',
  'recTimeDesc': '2016-07-06 21:16:58',
  'recUserName': 'admin',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.2.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet1/0/21 is DOWN.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160496',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467745458',
  'faultTimeDesc': '2016-07-05 15:04:18',
  'holdInfo': '',
  'id': '160496',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=21;Interface Description=GigabitEthernet1/0/21;Interface Admin Status=1;Interface Operate Status=2',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467854218',
  'recTimeDesc': '2016-07-06 21:16:58',
  'recUserName': 'admin',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.3.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/20 is UP.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160487',
  'alarmLevel': '5',
  'alarmLevelDesc': 'Info',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467742807',
  'faultTimeDesc': '2016-07-05 14:20:07',
  'holdInfo': '',
  'id': '160487',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=82;Interface Description=GigabitEthernet2/0/20;Interface Admin Status=1;Interface Operate Status=1',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467742807',
  'recTimeDesc': '2016-07-05 14:20:07',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.2.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/19 is DOWN.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160485',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467742775',
  'faultTimeDesc': '2016-07-05 14:19:35',
  'holdInfo': '',
  'id': '160485',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=81;Interface Description=GigabitEthernet2/0/19;Interface Admin Status=1;Interface Operate Status=2',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467854218',
  'recTimeDesc': '2016-07-06 21:16:58',
  'recUserName': 'admin',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.3.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet2/0/19 is UP.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160484',
  'alarmLevel': '5',
  'alarmLevelDesc': 'Info',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467742742',
  'faultTimeDesc': '2016-07-05 14:19:02',
  'holdInfo': '',
  'id': '160484',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=81;Interface Description=GigabitEthernet2/0/19;Interface Admin Status=1;Interface Operate Status=1',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467742742',
  'recTimeDesc': '2016-07-05 14:19:02',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.3.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet1/0/21 is UP.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160447',
  'alarmLevel': '5',
  'alarmLevelDesc': 'Info',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467736157',
  'faultTimeDesc': '2016-07-05 12:29:17',
  'holdInfo': '',
  'id': '160447',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=21;Interface Description=GigabitEthernet1/0/21;Interface Admin Status=1;Interface Operate Status=1',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467736157',
  'recTimeDesc': '2016-07-05 12:29:17',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.2.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet1/0/21 is DOWN.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160446',
  'alarmLevel': '2',
  'alarmLevelDesc': 'Major',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467736125',
  'faultTimeDesc': '2016-07-05 12:28:45',
  'holdInfo': '',
  'id': '160446',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=21;Interface Description=GigabitEthernet1/0/21;Interface Admin Status=1;Interface Operate Status=2',
  'parentId': '160438',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467736157',
  'recTimeDesc': '2016-07-05 12:29:17',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'},
 {'OID': '1.3.6.1.6.3.1.1.5.3.0',
  'ackStatus': '1',
  'ackStatusDesc': 'Acknowledged',
  'ackTime': '1467854226',
  'ackTimeDesc': '2016-07-06 21:17:06',
  'ackUserName': 'admin',
  'alarmCategory': '3',
  'alarmCategoryDesc': 'Interface/Link Status Alarm',
  'alarmDesc': 'The interface GigabitEthernet1/0/21 is UP.',
  'alarmDetail': 'http://kontrolissues.thruhere.net:8086/imcrs/fault/alarm/160444',
  'alarmLevel': '5',
  'alarmLevelDesc': 'Info',
  'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'deviceName': 'HP_5500EI',
  'faultTime': '1467736092',
  'faultTimeDesc': '2016-07-05 12:28:12',
  'holdInfo': '',
  'id': '160444',
  'originalType': '1',
  'originalTypeDesc': 'Trap',
  'paras': '*Interface Index=21;Interface Description=GigabitEthernet1/0/21;Interface Admin Status=1;Interface Operate Status=1',
  'parentId': '0',
  'recStatus': '1',
  'recStatusDesc': 'Recovered',
  'recTime': '1467736092',
  'recTimeDesc': '2016-07-05 12:28:12',
  'recUserName': '$SYSTEM',
  'remark': '',
  'somState': '0'}]
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

    >>> get_realtime_alarm('alarm', auth.creds, auth.url)
    [ {'deviceDisplay': '10.10.10.5',
  'faultDesc': 'The device(MAC Address:   F4 B7 E2 95 A0 CD) is detected to be flooding the network. Attack Frame Type: Probe Request.',
  'faultTime': '1469422319',
  'id': '185253',
  'severity': '3',
  'userAckType': '0',
  'userAckUserName': ''},
 {'deviceDisplay': '10.10.10.5',
  'faultDesc': 'The device(MAC Address:   F4 B7 E2 95 A0 CD) is detected to be flooding the network. Attack Frame Type: Probe Request.',
  'faultTime': '1469421710',
  'id': '185202',
  'severity': '3',
  'userAckType': '0',
  'userAckUserName': ''}]


    """
    get_realtime_alarm_url = "/imcrs/fault/faultRealTime?operatorName=" + username
    f_url = url + get_realtime_alarm_url
    print (f_url)
    r = requests.get(f_url, auth=auth, headers=headers)
    try:
        print (r.status_code)
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

    >>>get_alarms('admin', auth.creds, auth.url)

    >>>get_alarms('admin', auth.creds, auth.url)
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



