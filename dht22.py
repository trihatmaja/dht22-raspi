import Adafruit_DHT as dht
import time
from influxdb import InfluxDBClient

def writeDB(tmp, hum):
  json_body = [
        {
            "measurement": "temperature_humidity",
            "tags": {
                "host": "10.10.1.100",
                "datacenter": "DC-1"
            },
            "fields": {
                "temperature": '{0:0.2f}'.format(tmp),
                "humidity": '{0:0.2f}'.format(hum),
            }
        }
  ]

  client = InfluxDBClient('localhost', 8086, "", "", "raspi_temp")
  client.write_points(json_body)

def main():
    while True:
	h,t = dht.read_retry(dht.DHT22, 4)
	writeDB(t, h)
	print ('Temp={0:0.2f}*C  Humidity={1:0.2f}%'.format(t, h))
	time.sleep(5)

if __name__ == '__main__':
    main()
