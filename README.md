# Engel Virtual Assistant Engine

Engel is a Telegram bot-based virtual assistant. It's designed to run as a Linux system service, becoming capable of executing everything without restrictions. Use it under a strict access policy, otherwise your operating system might become easily compromised by attackers.



### Prerequisites

* Python 3.x
* Python3-pip
* Make
* At
* Virtualenv

```
apt-get update && sudo apt-get install python3 python3-pip make at -y
python3 -m pip install virtualenv
python3 -m pip install --upgrade pip
```

### Installing

Clone the project, and run make install

```bash
$make
$make install

```
Set your API key and config values in /opt/etc/engel/config

run engel

```
sudo service engel start
```

## Configuring the RSSH

Sometimes you need to access your machine via ssh but the machine is behind a NAT, making it impossible to access within a normal ssh query. One solution is to leave a tunnel opened in the target machine to a public server, a digital ocean droplet or any other VPS might be useful for this, however there is a big security risk in leaving that connection opened as well as this might catch the attention of your network manager if there is a monitoring system running.

You have to configure the connection string in the config file, have your root user assigned an ssh key with an empty passphrase and this key allowed in the remote server.

```bash
[RSSH]
# Example configuration
RemotePort = 1337
SshPort = 22
RemoteUser = user
RemoteServer = 255.255.255.255
```

where **remote port** represents the port in the server you will use to access your machine, the **ssh port** is the port you have configured in your machine, 22 is the default. remoteUser and remoteServer represent the user and address of the server you'll be forwarding the ssh connection.

## Built With

* Python 3.x

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Kirebyte/Engel/tags).

## Authors

* **KireByte** - *Initial work*

See also the list of [contributors](https://github.com/Kirebyte/Engel/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL V3

## Acknowledgments

* Keyrah Engel
