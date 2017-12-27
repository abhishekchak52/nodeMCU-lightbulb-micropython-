def connect():
	""" Connects to wifi with the stored credentials """
	import network 
	import credentials
	

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