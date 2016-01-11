import csv
from pyhpeimc.auth import *
from pyhpeimc.plat.groups import *


auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

def import_custom_views(filename):
    """
    Function which takes in a csv files as input to the create_custom_views function from the pyhpeimc python module
    available at https://github.com/HPNetworking/HP-Intelligent-Management-Center
    :param filename: user-defined filename which contains two column named "name" and "upperview" as input into the
    create_custom_views function from the pyhpeimc module.
    :return: returns output of the create_custom_vies function (str) for each item in the CSV file.
    """
    with open(filename) as csvfile:
        # decodes file as csv as a python dictionary
        reader = csv.DictReader(csvfile)
        for view in reader:
            # loads each row of the CSV as a JSON string
            name = view['name']
            upperview = view['upperview']
            if len(upperview) is 0:
                upperview = None
            create_custom_views(name,upperview,auth=auth.creds, url=auth.url)


import_custom_views('custom_views.csv')