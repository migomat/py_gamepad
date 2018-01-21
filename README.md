# py_gamepad
Reading Wireless gamepad input and translate it on GIPO

linux console:
```
sudo apt-get install python3-dev
sudo apt-get install python3-pip
```


```
pip3 install bitarray
pip3 install evdev
pip3 install serial
```
## 1. Searching for gamepad
before connecting gamepad gamepad
```
ls /dev/input
```

console result: 
`mietek@mietek-VirtualBox:~$ ls /dev/input/
by-id    event0  event2  event4  event6  js1   mouse0
by-path  event1  event3  event5  js0     mice  mouse1`

afer connecting gamepad
```
ls /dev/input
```
console result: 
`mietek@mietek-VirtualBox:~$ ls /dev/input/
by-id    event0  event2  event4  event6  js0  js2   mouse0
by-path  event1  event3  event5  event7  js1  mice  mouse1`

in that case gamepad is connected as 'event7'

## 2. Searching for COMx port




## Stuff that might help to understand the code
1. bitarray
https://pypi.python.org/pypi/bitarray/

2. bit mainipulation
https://www.tutorialspoint.com/python/bitwise_operators_example.htm

3. converting int to bytes
https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python

4. Serial.readBytes 
https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytes/


