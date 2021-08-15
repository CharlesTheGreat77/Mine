# Mine
Just a Fun script to scan for vulnerable devices

```
      .--.
     /.-. '----------.
     \'-' .--"--""-"-'
MINE  '--'

// Searches
SSH - libssh-0.6 version for Authenticaion Bypass
SMB - EternalBlue Vulnerable Devices
ADB - Android Debugging Bridge
Telnet - No Authentication enabled
VNC - No Authentication enabled
FTP - No Authentication enabled.
Cameras - Open Cameras (no Authentication)
    Yamcam
    WebcamXP/7
    Android IP Camera Servers
    Security DVRs

```
* PLEASE do NOT start exploiting or gaining access to unauthorized devices. 
It IS against the law you noobs. 

# Requirements

Python3 

Linux/Ubuntu/iSh etc.
```
$ apt install python3
```
Windows
```
https://www.python.org/downloads/
```

# Install
```
$ pip3 install -r requirements.txt
```

# Usage
```
$ python3 mine.py
```

# Screenshot

![Image description](https://github.com/CharlesTheGreat77/Mine/blob/main/D42D5809-913E-4EE3-BEF2-696A1078EA68.jpeg)

# Output
Results are saved as targets.txt

Format: <IP Address>:<Port>
```
cat targets.txt
```
output: 123.43.29.27:8080

Format: <IP Address>
```
cat targets.txt | tr ':' ' ' | awk '{print $1}'
```
output: 123.32.38.182
