import evdev
import serial
from bitarray import bitarray

arduino_port = serial.Serial('/dev/ttyS0',115200, timeout=3.0)
from evdev import InputDevice, categorize, ecodes, KeyEvent
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
#import RPi.GPIO as GPIO

for device in devices:
    print(device.fn, device.name, device.phys)

gamepad = InputDevice('/dev/input/event6')
dataframe = bitarray('00000000')


#print('capabilites:')
#print(gamepad.capabilities())
#print('capabilites: verbose=True')
#print(gamepad.capabilities(verbose=True))
#print(gamepad.leds(verbose=True))#wyswietla liste dostepnych led ktorymi mozna mrugac
#print(gamepad.active_keys(verbose=True))
for event in gamepad.read_loop():
    #print(event)
   # try:
    #    arduinofeedback=arduino_port.readline()
    #    print('value_readed:')
    #    print(arduinofeedback)
   # except:
    #    pass
    if event.code == 16:
        if event.value==-1:
            print('dpad_left')
            dataframe=dataframe|bitarray('00000100')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==1:
            print('dpad_right')
            dataframe=dataframe|bitarray('00001000')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==0:
            print('dpad_rl_released')
            dataframe=dataframe & bitarray('11110011')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
    elif event.code == 17:
        if event.value==-1:
            print('dpad_up')
            dataframe=dataframe | bitarray('00000001')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==1:
            print('dpad_down')
            dataframe=dataframe | bitarray('00000010')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==0:
            print('dpad_updown_released')
            dataframe=dataframe & bitarray('11111100')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
    
    elif event.code==288:
        print('triangle')
    elif event.code==289:
        print('circle')
    elif event.code==291:
        if event.value==1:
            print('square')
            dataframe=dataframe | bitarray('00000010')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==0:
            print('square_released')
            dataframe=dataframe & bitarray('11111100')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
    elif event.code==290:
        if event.value==1:
            print('cross')
            dataframe=dataframe | bitarray('00000001')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
        elif event.value==0:
            print('cross_released')
            dataframe=dataframe & bitarray('11111100')
            print(dataframe)
            arduino_port.write(dataframe.tobytes())
            
    elif event.code==297:
        if event.value==1:
            print('start')
            dataframe = bitarray('00000000')
            arduino_port.write(dataframe.tobytes())
    elif event.code==296:
        if event.value==1:
            print('select')
    elif event.code==292:
        if event.value==1:
            print('l1')
    elif event.code==294:
        if event.value==1:
            print('l2')
    elif event.code==293:
        if event.value==1:
            print('r1')
    elif event.code==295:
        if event.value==1:
            print('r2')
    elif event.code==299:
        if event.value==1:
            print('r_tog')
    elif event.code==298:
        if event.value==1:
            print('l_tog')
