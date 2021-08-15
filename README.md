# Mine
Just a Fun script to scan for vulnerable devices

```
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
          MINE '--'
```
# Requirements

Python3 

Linux/Ubuntu etc.
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

# Output
Results are saved as targets.txt

Format: <IP Address>:<Port>
```
cat targets.txt
```
output: 123.43.29.27:8080

Format: <IP Address>
```
cat targets.txt | awk '{print $1}'
```
output: 123.32.38.182
