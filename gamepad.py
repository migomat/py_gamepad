import evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)

gamepad = InputDevice('/dev/input/event0')

print('capabilites:')
#print(gamepad.capabilities())
print('capabilites: verbose=True')
#print(gamepad.capabilities(verbose=True))
#print(gamepad.leds(verbose=True))#wyswietla liste dostepnych led ktorymi mozna mrugac
#print(gamepad.active_keys(verbose=True))
for event in gamepad.read_loop():
    if event.code == 16:
        if event.value==-1:
            print('dpad_left')
        elif event.value==1:
            print('dpad_right')
    elif event.code == 17:
        if event.value==-1:
            print('dpad_up')
        elif event.value==1:
            print('dpad_down')
    elif event.value==1:
        if event.code==288:
            print('triangle')
        elif event.code==289:
            print('circle')
        elif event.code==291:
            print('square')
        elif event.code==290:
            print('cross')
        elif event.code==297:
            print('start')
        elif event.code==296:
            print('select')
        elif event.code==292:
            print('l1')
        elif event.code==294:
            print('l2')
        elif event.code==293:
            print('r1')
        elif event.code==295:
            print('r2')
        elif event.code==299:
            print('r_tog')
        elif event.code==298:
            print('l_tog')
        
   # else:
        #print('unrecognizable button')
        #print(event.code)
       # print(event)
   