Wanted to add more funcionalities, atm just added profilePath and set spn abuse (TODO clean my dirty code, be careful).

# LDAP shell
This project is a fork of ldap_shell (https://github.com/SecureAuthCorp/impacket/blob/master/impacket/examples/ldap_shell.py).


## Installation
These tools are only compatible with Python 3.5+. Clone the repository from GitHub, install the dependencies and you should be good to go:

```bash
git clone https://github.com/z-Riocool/ldap_shell.git
cd ldap_shell
python3 -m pip install .
```

## Usage
### Connection options
```
ldap_shell domain.local/user:password
ldap_shell domain.local/user:password -dc-ip 192.168.1.2
ldap_shell domain.local/user -hashes aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404e1
export KRB5CCNAME=/home/user/ticket.ccache
ldap_shell -k -no-pass domain.local/user
```

### Enumeration
* Remember that you can dump information about the domain (dump command) in .json or .html format, usefull:

![ldap_shell dump](https://github.com/LaresLLC/LDAP-Pwn-Them-All---Tools/blob/main/Impacket_ldap_shell_v2/ldap_output.png)

### Functionality
```
Get Info
    dump - Dumps the domain.
    search query [attributes,] - Search users and groups by name, distinguishedName and sAMAccountName.
    get_user_groups user - Retrieves all groups for a specified user.
    get_group_users group - Retrieves all members of a group.
    get_laps_password computer - Retrieves the LAPS passwords associated with a given computer (sAMAccountName).
    get_maq user - Get ms-DS-MachineAccountQuota for current user.
Abuse ACL
    add_user_to_group user group - Adds a user to a group.
    del_user_from_group user group - Delete a user from a group.
    change_password user [password] - Attempt to change a given user's password. Requires LDAPS.
    set_rbcd target grantee - Grant the grantee (sAMAccountName) the ability to perform RBCD to the target (sAMAccountName).
    clear_rbcd target - Clear the resource based constrained delegation configuration information.
    set_dcsync user - If you have write access to the domain object, assign the DS-Replication right to the selected user.
    del_dcsync user - Delete DS-Replication right to the selected user.
    set_genericall target grantee - Grant full control of a given target object (sAMAccountName) to the grantee (sAMAccountName).
    set_owner target grantee - Abuse WriteOwner privilege.
    dacl_modify - Modify ACE (add/del). Usage: target, grantee, add/del and mask name or ObjectType for ACE modified.
    set_dontreqpreauth user true/false - Set the don't require pre-authentication flag to true or false.
    get_ntlm user - Shadow Credentials method to abuse GenericAll, GenericWrite and AllExtendedRights privilege
    write_gpo_dacl user gpoSID - Write a full control ACE to the gpo for the given user. The gpoSID attribute format is {value}.
Misc
    switch_user user password/NTLM - Switch user shell.
    add_computer computer [password] - Adds a new computer to the domain with the specified password. Requires LDAPS.
    del_computer computer - Remove a computer from the domain.
    add_user new_user [parent] - Creates a new user.
    disable_account user - Disable the user's account.
    enable_account user - Enable the user's account.
exit - Terminates this session.
```
## TODO
- [x] del_computer - Delete computer
- [x] set_dcsync - If you have write access to the domain object, assign the DS-Replication right to the selected user
- [x] del_dcsync - Delete DS-Replication right to the selected user
- [x] shadow_credantional - inherited [pywhisker](https://github.com/ShutdownRepo/pywhisker)
- [x] get_all_laps - Get all LAPS passwords
- [x] set_owner - Abuse WriteOwner privilege
- [x] dacl_modify - Set GenericAll, WriteDacl, WriteProperties or set MASK of privilege
- [x] set_profilePath - Set profilePath user attribute, usefull to relay
- [x] unset_profilePath - clean relay
- [x] set_kerberoast - set SPN to targeted Kerberoasting
- [ ] Improve the output
- [ ] get_gpos - Enumerate GPOs
- [ ] get_passpolicy - Enumerate password policy
- [ ] del_user - Delete user
- [ ] Just more functionalities

## License
Apache

## Authors
* [Riocool](https://t.me/riocool)

## Credits
* [Impacket](https://github.com/SecureAuthCorp/impacket)
* [saber-nyan](https://saber-nyan.com)

