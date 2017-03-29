import csv
from pyhpeimc.auth import *
from pyhpeimc.plat.operator import *



#auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")
auth = IMCAuth("http://", "kontrolissues.thruhere.net", "8086", "admin", "admin")


def import_operator(filename='imc_operator_list.csv'):
    with open(filename) as csvfile:
        # decodes file as csv as a python dictionary
        reader = csv.DictReader(csvfile)
        try:
            for operator in reader:
                # loads each row of the CSV as a JSON string
                create_operator(operator, url=auth.url, auth=auth.creds)
        except:
            pass


import_operator()






