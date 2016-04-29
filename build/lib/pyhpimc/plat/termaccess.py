#!/usr/bin/env python3
# author: @netmanchris

""" Copyright 2015 Hewlett Packard Enterprise Development LP

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   """

# This section imports required libraries
import json
import requests


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#command creates dummy IMCAuth object. Should be overwritten in script calling these functions



def get_real_time_locate(ipAddress, auth, url):
    """
    function takes the ipAddress of a specific host and issues a RESTFUL call to get the device and interface that the
    target host is currently connected to.
    :param ipAddress: str value valid IPv4 IP address
    :return: dictionary containing hostIp, devId, deviceIP, ifDesc, ifIndex
    """
    real_time_locate_url = "/imcrs/res/access/realtimeLocate?type=2&value=" + str(ipAddress) + "&total=false"
    f_url = url + real_time_locate_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            response =  json.loads(r.text)
            if 'realtimeLocation' in response:
                return json.loads(r.text)['realtimeLocation']
            else:
                return json.loads(r.text)

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_real_time_locate: An Error has occured"


def get_ip_mac_arp_list(devId, auth,url):
    """
    function takes devid of specific device and issues a RESTFUL call to get the IP/MAC/ARP list from the target device.
    :param devId: int or str value of the target device.
    :return: list of dictionaries containing the IP/MAC/ARP list of the target device.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    ip_mac_arp_list_url = "/imcrs/res/access/ipMacArp/" + str(devId)
    f_url = url + ip_mac_arp_list_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            macarplist = (json.loads(r.text))
            if len(macarplist) > 1:
                return macarplist['ipMacArp']
            else:
                return ['this function is unsupported']

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_mac_arp_list: An Error has occured"


#this section deals with the IP Address Manager functions with terminal access of HPE IMC Base platform

def get_ip_scope(auth, url,scopeId=None):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE IMC server. If the
    optional scopeId parameter is included, this will automatically return only the desired scope id.
    :param scopeId: integer of the desired scope id ( optional )
    :param auth:
    :return:
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    if scopeId is None:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope"
        f_url = url + get_ip_scope_url
        r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
        try:
            if r.status_code == 200:
                ipscopelist = (json.loads(r.text))
                return ipscopelist


        except requests.exceptions.RequestException as e:
                return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"





def add_ip_scope(auth, url,startIp, endIp, name, description):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope to terminal access
    in the HPE IMC base platform
    :param startIp: str Start of IP address scope ex. '10.101.0.1'
    :param endIp: str End of IP address scope ex. '10.101.0.254'
    :param name: str Name of the owner of this IP scope  ex. 'admin'
    :param description: str description of the Ip scope
    :return:
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()

    add_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    f_url = url + add_ip_scope_url
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s" }'''
               %(str(startIp), str(endIp), str(name), str(description)))
    r = requests.post(f_url, auth=auth, headers=HEADERS, data=payload) # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print ("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"


    #Add host to IP scope
    #http://10.101.0.203:8080/imcrs/res/access/assignedIpScope/ip?ipScopeId=1
    '''{
      "ip": "10.101.0.1",
      "name": "Cisco2811.lab.local",
      "description": "Cisco 2811",
      "parentId": "1"
    }'''