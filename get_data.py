# This script gets the data from the sensor
from websocket import create_connection
import json


def get_pulse_data_from_websocket():
  #return 250  # for testing
  ws = create_connection("ws://agilegw.local:8080/ws/device/ble987BF3738084/PULSE/subscribe")
  #print "Receiving..."
  result =  ws.recv()
  #print "Received '%s'" % result
  ws.close()

  try:
		result = json.loads(result)
  except ValueError:
		print("No data available. Please setup oximeter first. Did you connect the AGILE? Is the sensor turned on? Got Message:", result)
		print("TODO: consider running a reconnect script or something here")
		exit()
  else:
		#Data Format '[{"deviceID":"dummy001122334455","componentID":"DummyData","value":"24","unit":"dum","format":"","lastUpdate":1495723678802}]'
		value = result.get('value')
			
		#print("pulse sensor value:")
		#print value
		
		return value


