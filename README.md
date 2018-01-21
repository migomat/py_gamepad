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

## Com port setup on VirtualBox
  In that particular example I'm using VirtualBox. Host: Windows 7, Guest: Ubuntu(light dustribution) linux
```
How to add a physical serial port.
In Guest Settings for Serial Ports set as follow
Port1: Checked
Port Number: COM1
Port Mode: Host Device
Windows Host:
Port/File Path: COM1:
Note the colon in COM1: (not semicolon). I have experienced the guest could become unstable without it. 
For a host port number higher than 9, the naming \\.\comX where X is the port number, is required. This can also be used for a one digit port number.
Linux Host:
Port/File Path: /dev/ttyS1
For other COM port than 1 replace the digit with port number.
```
