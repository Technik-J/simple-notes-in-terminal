# Simple Notes in Terminal

Wrote this terminal tool to help me write notes in terminal. It writes to home directory in a simple markdown file with timestamps. You can change the location in `config_file.py`.

## Install
* Clone this repository.
* Add this aliases. Change path to yours, if you didn't clone to your home directory.
```shell
alias note='/usr/bin/python3 $HOME/simple-notes-in-terminal/simple-notes.py'
alias snote='/usr/bin/python3 $HOME/simple-notes-in-terminal/simple-notes.py --simple'
```

## Example

```shell
$ snote This is a simple note

$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:        18.04
Codename:       bionic

$ note lsb_release -a
Comment: distro info

$ lsb_release -a | note Output of the command
```

Output file will look like this 
```shell
$ cat notes.md
###### 03.07.2019 12:03:38
This is a simple note
###### 03.07.2019 12:04:16
​```shell
lsb_release -a # distro isfo
​```
###### 03.07.2019 12:06:04
Output of the command
​```shell
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:        18.04
Codename:       bionic

​```
```