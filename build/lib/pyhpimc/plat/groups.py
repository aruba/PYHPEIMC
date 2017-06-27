'''Copyright 2015 Chris Young

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

#   IMC Server Build Project 1.0
#  Chris Young a.k.a Darth
#
# Hewlett Packard Company    Revision 1.0
#
# Change History.... 3/19/15
#

# This series of functions is intended to help automate the build of an IMC server using
# the eAPI function. The eAPI is available natively on the IMC enterprise edition
# and can be added to the standard edition through the purchase of the
# eAPI addon license.

# This section imports required libraries
import requests
import json



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}


"""
This section deals with HPE IMC Custom View functions
"""

def get_custom_views(auth, url,name=None,headers=HEADERS):
    """
    function requires no input and returns a list of dictionaries of custom views from an HPE IMC. Optional name
    argument will return only the specified view.
    :param name: str containing the name of the desired custom view
    :return: list of dictionaties containing attributes of the custom views
    """
    if name is None:
        get_custom_view_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=false'
    elif name is not None:
        get_custom_view_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&name='+name+'&desc=false&total=false'
    f_url = url + get_custom_view_url
    r = requests.get(f_url, auth=auth, headers=headers)
    try:
        if r.status_code == 200:
            custom_view_list = (json.loads(r.text))["customView"]
            if type(custom_view_list) == dict:
                custom_view_list = [custom_view_list]
                return custom_view_list
            else:
                return custom_view_list
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_custom_views: An Error has occured'


def create_custom_views(auth, url,name=None, upperview=None):
    """
    function takes no input and issues a RESTFUL call to get a list of custom views from HPE IMC. Optioanl Name input
    will return only the specified view.
    :param name: string containg the name of the desired custom view
    :return: list of dictionaries containing attributes of the custom views.
    """
    create_custom_views_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=false'
    f_url = url + create_custom_views_url
    if upperview is None:
        payload = '''{ "name": "''' + name + '''",
         "upLevelSymbolId" : ""}'''
        print (payload)
    else:
        parentviewid = get_custom_views(auth, url, upperview)[0]['symbolId']
        payload = '''{ "name": "'''+name+ '''",
        "upLevelSymbolId" : "'''+str(parentviewid)+'''"}'''
        print (payload)
    r = requests.post(f_url, data = payload, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 201:
            return 'View ' + name +' created successfully'
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_custom_views: An Error has occured'


def delete_custom_view(auth, url, name):
    """
    function takes input of auth, url, and name and issues a RESTFUL call to delete a specific of custom views from HPE
    IMC.
    :param name: string containg the name of the desired custom view
    :return:
    """
    view_id  = get_custom_views(auth, url,name )[0]['symbolId']
    delete_custom_view_url = '/imcrs/plat/res/view/custom/'+str(view_id)
    f_url = url + delete_custom_view_url
    r = requests.delete(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 204:
            return 'View ' + name +' deleted successfully'
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' delete_custom_view: An Error has occured'