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
    :param auth:
    :param url:
    :return:
    '''
    if folder == None:
        get_cfg_template_url = "/imcrs/icc/confFile/list"
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
    :param auth:
    :param url:
    :return:
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
    :param auth:
    :param url:
    :return:
    '''
    file_id = get_template_id(template_name, auth, url)
    delete_cfg_template_url = "/imcrs/icc/confFile/"+str(file_id)
    print (delete_cfg_template_url)
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
    :param auth:
    :param url:
    :return: str numerical id of the folder
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
    :param auth:
    :param url:
    :return: str numerical id of the folder
    """
    object_list = get_cfg_template(auth=auth, url=url)
    for object in object_list:
        if object['confFileName'] == template_name:
            return object['confFileId']
    return "template not found"

