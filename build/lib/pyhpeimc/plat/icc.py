#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import json
import requests


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}




def get_cfg_template(auth, url, folder = None):
    '''
    Function takes no input and returns a list of dictionaries containing the configuration templates in the root folder
    of the icc configuration template library.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: List of Dictionaries containing folders and configuration files in the ICC library.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    #Get list of folders and files in root of ICC Configuration Library
    >>>get_cfg_template(auth.creds, auth.url)
    [{'appliedDevices': '',
  'cfgFileParent': '-1',
  'confFileDesc': 'Stores predefined configuration.',
  'confFileId': '1',
  'confFileName': 'Default Folder',
  'confFilePath': '/',
  'confFileType': '-1',
  'createAt': '2016-01-26 23:36:18',
  'createBy': '$SYSTEM',
  'defaultConfFile': '1',
  'defaultConfFileDesc': 'Default config file, cannot delete.',
  'modifyAt': '2016-01-26 23:36:18.483',
  'syncType': '0'},
 {'appliedDevices': '',
  'cfgFileParent': '-1',
  'confFileDesc': 'Folder to Store AutoDeployment Plan related configuration templates',
  'confFileId': '57',
  'confFileName': 'ADP_Configs',
  'confFilePath': '\\',
  'confFileType': '-1',
  'createAt': '2016-01-27 14:44:50',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'syncType': '0'},
 {'appliedDevices': '',
  'cfgFileParent': '-1',
  'confFileDesc': 'Juniper SNMP Strings',
  'confFileId': '62',
  'confFileName': 'JuniperSNMP.cfg',
  'confFilePath': '\\',
  'confFileType': '2',
  'confFileTypeDesc': 'Segment',
  'createAt': '2016-07-08 13:36:45',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'syncType': '0'},
 {'appliedDevices': '',
  'cfgFileParent': '-1',
  'confFileDesc': '',
  'confFileId': '61',
  'confFileName': 'SSHNAT.cfg',
  'confFilePath': '\\',
  'confFileType': '2',
  'confFileTypeDesc': 'Segment',
  'createAt': '2016-06-22 10:02:07',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'modifyAt': '2016-06-22 10:05:48',
  'syncType': '0'},
 {'appliedDevices': 'HP 5900-AF-48XGT-4QSFP+',
  'cfgFileParent': '-1',
  'confFileDesc': 'SNMP. Tempalte for V2c for Comware Device',
  'confFileId': '59',
  'confFileName': '10.20.10.10_running_20160610095951.cfg',
  'confFilePath': '\\',
  'confFileType': '2',
  'confFileTypeDesc': 'Segment',
  'createAt': '2016-06-10 13:21:32',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'modifyAt': '2016-06-10 13:24:15',
  'syncType': '0'}]

    #Get list of Folders in Files in a specific folder of the ICC Configuration Library
    >>>get_cfg_template(auth.creds, auth.url, folder='ADP_Configs')
[{'appliedDevices': 'HP 5900-AF-48XGT-4QSFP+',
  'cfgFileParent': '57',
  'confFileDesc': '5900 ADP Config with Netconf - Ansible Ready',
  'confFileId': '60',
  'confFileName': '5900ADP_w_Netconf.cfg',
  'confFilePath': '\\ADP_Configs',
  'confFileType': '1',
  'confFileTypeDesc': 'File',
  'createAt': '2016-06-21 12:01:14',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'syncType': '0'},
 {'appliedDevices': '',
  'cfgFileParent': '57',
  'confFileDesc': '5900_Initial Config for ADP process',
  'confFileId': '58',
  'confFileName': '5900_Initial.cfg',
  'confFilePath': '\\ADP_Configs',
  'confFileType': '1',
  'confFileTypeDesc': 'File',
  'createAt': '2016-01-27 14:47:59',
  'createBy': 'admin',
  'defaultConfFile': '2',
  'defaultConfFileDesc': 'Useful config file.',
  'modifyAt': '2016-01-28 14:37:21',
  'syncType': '0'}]

    '''
    if folder == None:
        get_cfg_template_url = "/imcrs/icc/confFile/list"
    else:
        folder_id = get_folder_id(folder, auth, url)
        get_cfg_template_url = "/imcrs/icc/confFile/list/"+str(folder_id)
    f_url = url + get_cfg_template_url
    r = requests.get(f_url,auth=auth, headers=HEADERS)
    #print (r.status_code)
    try:
        if r.status_code == 200:
            cfg_template_list = (json.loads(r.text))
            return cfg_template_list['confFile']

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_cfg_template: An Error has occured"



def create_cfg_segment(filename, filecontent, description, auth, url):
    '''
    Takes a str into var filecontent which represents the entire content of a configuration segment, or partial
    configuration file. Takes a str into var description which represents the description of the configuration segment
    :param filename: str containing the name of the configuration segment.

    :param filecontent: str containing the entire contents of the configuration segment

    :param description: str contrianing the description of the configuration segment

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: If successful, Boolena of type True

    :rtype: Boolean

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> filecontent = """ snmp-agent\r\n snmp-agent community write ${ SNMP Write}\r\n snmp-agent community read
                           ${SNMP Read}\r\n snmp-agent sys-info version v2c \r\n snmp-agent target-host trap address
                           udp-domain 10.101.0.203 params securityname public\r\n snmp-agent trap enable arp \r\n
                           snmp-agent trap enable radius \r\n"""
     >>> create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template', auth.creds, auth.url)
     True

    '''
    payload = {"confFileName": filename,
               "confFileType": "2",
               "cfgFileParent": "-1",
               "confFileDesc": description,
               "content": filecontent}
    create_cfg_segment_url = "/imcrs/icc/confFile"
    f_url = url + create_cfg_segment_url
    # creates the URL using the payload variable as the contents
    r = requests.post(f_url,data= (json.dumps(payload)), auth=auth, headers=HEADERS)
    try:
        if r.status_code == 201:
            return True
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " create_cfg_segment: An Error has occured"



def delete_cfg_template(template_name, auth, url):
    '''Uses the get_template_id() funct to gather the template_id to craft a url which is sent to the IMC server using
    a Delete Method
    :param template_name: str containing the entire contents of the configuration segment

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: If successful, Boolean of type True

    :rtype: Boolean

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)
    True
    '''
    file_id = get_template_id(template_name, auth, url)
    delete_cfg_template_url = "/imcrs/icc/confFile/"+str(file_id)
    f_url = url + delete_cfg_template_url
    # creates the URL using the payload variable as the contents
    r = requests.delete(f_url, auth=auth, headers=HEADERS)
    #print (r.status_code)
    try:
        if r.status_code == 204:
            return True
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " delete_cfg_template: An Error has occured"

def get_folder_id(folder_name, auth, url):
    """
    Helper function takes str input of folder name and returns str numerical id of the folder.
    :param folder_name: str name of the folder

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str numerical id of the folder

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>get_folder_id('Default Folder', auth.creds, auth.url)
    '1'
    """
    object_list = get_cfg_template(auth=auth, url=url)
    for object in object_list:
        if object['confFileName'] == folder_name:
            return object['confFileId']
    return "Folder not found"

def get_template_id(template_name, auth, url):
    """
    Helper function takes str input of folder name and returns str numerical id of the folder.
    :param folder_name: str name of the folder

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str numerical id of the folder

    :rtype: str

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>>get_template_id('CW7SNMP.cfg', auth.creds, auth.url)
    '64'
    """
    object_list = get_cfg_template(auth=auth, url=url)
    for object in object_list:
        if object['confFileName'] == template_name:
            return object['confFileId']
    return "template not found"

