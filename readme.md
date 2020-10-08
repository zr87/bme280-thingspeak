# Bosch BME280 

Simple python job script to send sensor data to Thingspeak api.
Written to run on a Raspberry Pi Zero

### Get started

The `job.py` script uses the `config.py` script to import the api url to send get requests.

0. for wiring the bme280 sensor to a raspberry check this [tutorial](
https://app.getpocket.com/read/1364761076)

1. rename `config.py.sample` to `config.py` and fill your Thingspeak api key

2. add `job.py` to crontab to schedule frequency for sending data (check this [tutorial](https://www.raspberrypi.org/documentation/linux/usage/cron.md) on how to add scripts to the crontab).

### Credits

 - this script uses [Matt Hawkins](https://bitbucket.org/%7B18a352f1-8fe1-4b70-9e9c-cd29f663fafc%7D/)'s bme280 [script](  
https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py) to read out data from the sensor


