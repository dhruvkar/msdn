import ldap
from getpass import getpass as gpw
from config import *

dc = 'ldap://192.168.10.19'
base = 'OU=Employees,OU=Users,OU=OSI Inc,DC=osisoft,DC=int'
scope = ldap.SCOPE_SUBTREE
filters = "sAMAccountName="+raw_input("Enter username to search: ")
attr = ['givenName', 'sn', 'mail', 'l', 'c', 'department']

ld = ldap.initialize(dc)

ld.set_option(ldap.OPT_REFERRALS,0)

ld.simple_bind_s(user, pw)

results = ld.search_s(base, scope, filters, attr)

'''
def (dc, base, 

'''

