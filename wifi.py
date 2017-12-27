def connect():
	""" Connects to wifi with the stored credentials """
	import network 

	ssid = "Default"
	password = "@24310143#"

	station = network.WLAN(network.STA_IF)

	if station.isconnected() == True:
		print("Already connected")
		return

	station.active(True)
	station.connect(ssid,password)

	while station.isconnected() == False:
		pass

	# print("Connection successful")
	# print(station.ifconfig())