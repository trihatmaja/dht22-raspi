import Adafruit_DHT as dht
import time
from influxdb import InfluxDBClient

def get_serial():
    cpu_serial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpu_serial = line[10:26]
        f.close()
    except:
        cpu_serial = "ERROR000000000"

    return cpu_serial

def write_db(tmp, hum, device_id):
  json_body = [
        {
            "measurement": "temperature",
            "tags": {
                "device_id": str(device_id),
            },
            "fields": {
                "celcius": str('{0:0.2f}'.format(tmp)),
                "humidity": str('{0:0.2f}'.format(hum)),
            }
        }
  ]

  client = InfluxDBClient('localhost', 8086, "", "", "raspi_temp")
  client.write_points(json_body)

def main():
    device_id = get_serial()
    while True:
	h,t = dht.read_retry(dht.DHT22, 4)
	write_db(t, h, device_id)
	print ('Temp={0:0.2f}*C  Humidity={1:0.2f}%'.format(t, h))
	time.sleep(5)

if __name__ == '__main__':
    main()
