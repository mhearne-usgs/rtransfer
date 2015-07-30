Introduction
------------

rtransfer is a project designed to make it easier to transfer files to and from remote systems
with "service" accounts - that is, accounts from which applications are installed and run.  Normally,
to retrieve files underneath these user accounts, a user has to:

 - ssh to the remote machine
 - sudo cp the file from the service account to the user account
 - scp the file from the remote system to the desktop system.

With rget, those three steps are combined into one. (See usage below)

There are three commands that are installed with this package:
 - rget A program for retrieving files from a service account on a remote system
 - rput A program for transferring local files to a service account on a remote system
 - rcfg A program for configuring the remote systems.

For details about the usage of each of these programs, see below, but generally these three programs work like this:

 - Use rcfg to define:
   * A short, easy to remember "alias" for each remote system
   * The path to the user's home directory on that remote system
   * The name of the service account
- Use rget to fetch files from these remote systems.
- Use rput to transfer files to these remote systems.

Installation and Dependencies
-----------------------------
To install this package:

pip install git+git://github.com/mhearne-usgs/rtransfer.git

This last command will install rget in your path.

Uninstalling and Updating
-------------------------

To uninstall:

pip uninstall rtransfer

To update:

pip install -U git+git://github.com/mhearne-usgs/rtransfer.git


Usage for rget
--------
<pre>
usage: rget [-h] remotehost files [files ...]

Retrieve files from a remote system with a service account.
    In order to avoid the sequence of ssh and scp commands required to copy files from 
    a "service" account on a remote system to a directory on your local system, this program
    automates as much of that as possible.
    Examples:

    To copy files from a system:
    rget mysystem /home/service/file1.txt /home/service/file2.txt
    
    Copying files from service account to remote user 
    (you will be prompted for sudo password on igskaecgvmdvlsp)

    [sudo] password for user:
    Copying remote files from your home directory on mysystem to local directory.
    

positional arguments:
  remotehost  Remote system name (or alias) where files should be retrieved from
  files       Remote files under system account to be retrieved.

optional arguments:
  -h, --help  show this help message and exit
</pre>

Usage for rput
--------------
<pre>
usage: rput [-h] arguments [arguments ...]

Transfer files to a remote system with a service account.
    In order to avoid the sequence of ssh and scp commands required to copy files from 
    a directory on your local system to a "service" account on a remote system, this program
    automates as much of that as possible.
    Examples:

    To copy files to a remote system:
    rput file.txt file2.txt mysystem /home/service/data
    
    Copying files from remote user to service account 
    (you will be prompted for sudo password on igskaecgvmdvlsp)

    [sudo] password for mhearne:
    Copying remote files from your home directory on mysystem to service account folder.
    

positional arguments:
  arguments   Input list of arguments - last two must be alias and remote folder

optional arguments:
  -h, --help  show this help message and exit
</pre>

Usage for rcfg
--------------
<pre>
usage: rcfg [-h] [-l] [-d DELETE]

Configure systems for use by rget and rput.
    To configure a system:
    rcfg
    Enter the alias for a remote host to configure: mysystem
    Enter the domain name of the remote host: mysystem.com
    What is the home directory for mhearne on mysystem.com? /home/AD/myuser 
    What is the name of the service account on mysystem.com? service
    Do you have more hosts to configure? y/[n] n
    

optional arguments:
  -h, --help            show this help message and exit
  -l, --listconfig      List configured remote accounts.
  -d DELETE, --delete DELETE
                        delete configured remote account.
</pre>

