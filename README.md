# check_tasmota


Nagios plugin to check availability of [Tasmota](https://tasmota.github.io/docs/) devices. Checks if the ESPHome device is online

## Installation

The installation requires Python 3.

I usually install additional plugins under `/usr/local/nagios/libexec`.

```
mkdir -p /usr/local/nagios/libexec
cd /usr/local/nagios/libexec
wget https://raw.githubusercontent.com/mdiazgoncalves/check_tasmota/main/check_tasmota.py
chmod +x check_tasmota.py
```

The [requests](https://github.com/psf/requests) module is required.

To install Requests, simply run this simple command in your terminal of choice:

```
python -m pip install requests
```

## Parameters

```
usage: check_tasmota.py [-h] [-U username] [-P password] <hostname>

Check Tasmota node availability

positional arguments:
  <hostname>            The hostname/ip of the device

optional arguments:
  -h, --help            show this help message and exit
  -U username, --username username
                        the tasmota api username
  -P password, --password password
                        the tasmota api password

```

## Support

Feel free to submit any issues and PR's'.

## License

The project is licensed under GPL license. Happy monitoring.
