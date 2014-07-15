#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import ldap
LDAP_HOST = '172.16.27.27'
LDAP_BASE_DN = 'dc=dawn,dc=cn'
MGR_CRED = 'cn=admin,dc=dawn,dc=cn'            #MGE_CRED = 'dawn\admin'
MGR_PASSWD = '123456'
STOOGE_FILTER = 'uid=dawn_zhou'

class LDAPAdmim:
    def __init__(self, ldap_host=None, ldap_base_dn=None, mgr_cred=None, mgr_passwd=None):
        if not ldap_host:
            ldap_host = LDAP_HOST
        if not ldap_base_dn:
            ldap_base_dn = LDAP_BASE_DN
        if not mgr_cred:
            mgr_cred = MGR_CRED
        if not mgr_passwd:
            mgr_passwd = MGR_PASSWD
        self.ldapconn = ldap.open(ldap_host)               #  self.ldapconn = ldap.initialize(ldap_host)
        self.ldapconn.simple_bind(mgr_cred, mgr_passwd)
        self.ldap_base_dn = ldap_base_dn

    def list(self, stooge_filter=None, attrib=None):
        if not stooge_filter:
            stooge_filter = STOOGE_FILTER
        s = self.ldapconn.search_s(self.ldap_base_dn, ldap.SCOPE_SUBTREE, stooge_filter, attrib)
        print "Here is the complete list of stooges:"
        stooge_list = []
        for stooge in s:
            attrib_dict = stooge[1]
            for a in attrib_dict:
                out = "%s: %s" % (a, attrib_dict[a])
                print out
                stooge_list.append(out)
        return stooge_list

    def add(self, stooge_name, stooge_ou, stooge_info):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        stooge_attrib = [(k, v) for (k, v) in stooge_info.items()]
        print "Adding stooge %s with ou=%s" % (stooge_name, stooge_ou)
        self.ldapconn.add_s(stooge_dn, stooge_attrib)

    def modify(self, stooge_name, stooge_ou, stooge_attrib):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        print "Modifying stooge %s with ou=%s" % (stooge_name, stooge_ou)
        self.ldapconn.modify_s(stooge_dn, stooge_attrib)

        """
        http://www.grotan.com/ldap/python-ldap-samples.html#modify
        # import needed modules
        import ldap
        import ldap.modlist as modlist

        # Open a connection
        l = ldap.initialize("ldaps://localhost.localdomain:636/")

        # Bind/authenticate with a user with apropriate rights to add objects
        l.simple_bind_s("cn=manager,dc=example,dc=com","secret")

        # The dn of our existing entry/object
        dn="cn=replica,dc=example,dc=com"

        # Some place-holders for old and new values
        old = {'description':'User object for replication using slurpd'}
        new = {'description':'Bind object used for replication using slurpd'}

        # Convert place-holders for modify-operation using modlist-module
        ldif = modlist.modifyModlist(old,new)

        # Do the actual modification
        l.modify_s(dn,ldif)

        # Its nice to the server to disconnect and free resources when done
        l.unbind_s()
      """

    def delete(self, stooge_name, stooge_ou):
        stooge_dn = 'cn=%s,ou=%s,%s' % (stooge_name, stooge_ou, self.ldap_base_dn)
        print "Deleting stooge %s with ou=%s" % (stooge_name, stooge_ou)
        self.ldapconn.delete_s(stooge_dn)


a = LDAPAdmim()
a.list()