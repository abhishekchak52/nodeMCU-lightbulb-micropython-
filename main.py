import machine
import time
import urequests

led = machine.Pin(2, machine.Pin.OUT) # Onboard LED
led2 = machine.Pin(16, machine.Pin.OUT) #Builtin LED

# Boot sequence
led.off()
time.sleep(1)
led2.off()
time.sleep(1)

led.on()
led2.on()

# Main program loop
while True:
	state = urequests.get('https://light-switch-toggle.herokuapp.com/state').json()['state']

	if state == 'off':
		led.on()
		led2.on()
	elif state == 'on':
		led.off()
		led2.off()
	# time.sleep(0.5)

