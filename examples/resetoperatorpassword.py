from pyhpeimc.auth import *
from pyhpeimc.plat.operator import *



#auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")
auth = IMCAuth("http://", "kontrolissues.thruhere.net", "8086", "admin", "admin")

set_operator_password('cyoung', password='newpass',auth=auth.creds,url=auth.url,)