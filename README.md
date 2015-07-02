Introduction
------------

rtransfer is a project designed to make it easier to transfer files to and from remote systems
with "service" accounts - that is, accounts from which applications are installed and run.  Normally,
to retrieve files underneath these user accounts, a user has to:

 - ssh to the remote machine
 - sudo cp the file from the service account to the user account
 - scp the file from the remote system to the desktop system.



Installation and Dependencies
-----------------------------
To install this package:

pip install git+git://https://github.com/mhearne-usgs/rtransfer.git

This last command will install rget in your path.

Uninstalling and Updating
-------------------------

To uninstall:

pip uninstall rtransfer

To update:

pip install -U git+git://https://github.com/mhearne-usgs/rtransfer.git


Usage for rget
--------
<pre>
usage: rget [-h] [-r REMOTEHOST] [-f FILES [FILES ...]] [-c] [-l]

Retrieve files from a remote system with a service account.
    In order to avoid the sequence of ssh and scp commands required to copy files from 
    a "service" account on a remote system to a directory on your local system, this program
    automates as much of that as possible.
    Examples:

    To configure a system:
    rget -c
    Enter the alias for a remote host to configure: mysystem
    Enter the domain name of the remote host: mysystem.com
    What is the home directory for mhearne on mysystem.com? /home/AD/mhearne 
    What is the name of the service account on mysystem.com? service
    Do you have more hosts to configure? y/[n] n

    To copy files from that system:
    rget -r mysystem -f file1.txt file2.txt
    
    Copying files from service account to remote user 
    (you will be prompted for sudo password on igskaecgvmdvlsp)

    [sudo] password for mhearne:
    Copying remote files from your home directory on igskaecgvmdvlsp to local directory.
    

optional arguments:
  -h, --help            show this help message and exit
  -r REMOTEHOST, --remotehost REMOTEHOST
                        Remote system name (or alias) where files should be retrieved from
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Remote files under system account to be retrieved.
  -c, --config          Configure remote accounts.
  -l, --listconfig      List configured remote accounts.
</pre>

