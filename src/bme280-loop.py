import bme280
import sys
import urllib2
from time import sleep
from config import baseURL

def BME280_data():
	# Reading from BME280 and storing the temperature, humidity & pressure
	temperature, pressure, humidity = bme280.readBME280All()
	return temperature, pressure, humidity

try:
	temp, press, humi = BME280_data()

	# If Reading is valid
	if isinstance(humi, float) and isinstance(temp, float) and isinstance(press, float):
		# Formatting to two decimal places
		humi = '%.2f' % humi
		temp = '%.2f' % temp
		press = '%.2f' % press
		# Sending the data to thingspeak
		conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (temp, humi, press))
		print conn.read()
		# Closing the connection
		conn.close()

	else:
		print 'Error'

	# BME280 requires few seconds to give a reading, but lets log every 10 mins (10min = 300) 
	sleep(600) 

except:
	break
