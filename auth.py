import ldap
from getpass import getpass as gpw

dc = 'ldap://192.168.10.19'
base = 'OU=Employees,OU=Users,OU=OSI Inc,DC=osisoft,DC=int'
scope = ldap.SCOPE_SUBTREE
filters = "sAMAccountName="+raw_input("Enter username to search: ")
attr = ['givenName', 'sn', 'mail', 'l', 'c', 'department']

ld = ldap.initialize(dc)

ld.set_option(ldap.OPT_REFERRALS,0)

user = raw_input("Enter your email: ")
pw = gpw()

ld.simple_bind_s(user, pw)

results = ld.search_s(base, scope, filters, attr)

