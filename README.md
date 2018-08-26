# DHT22 for Raspiberry PI

This code is used for DHT22 for raspberry pi and send the temperature and humidity to influxdb

### Installation

This code need [Adafruit Lib](https://github.com/adafruit/Adafruit_Python_DHT) and [InfluxDB Client](https://github.com/influxdata/influxdb-python)

Install the dependencies.

```sh
# install adafruit python dht
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo apt-get update
$ sudo apt-get install build-essential python-dev
$ sudo python setup.py install

# install influxdb client for python in debian
$ sudo apt-get install python-influxdb
```

### Running code

Run this code using this command

```sh
python dht22.py
```

### Wiring

See reference

### Todos

 - Write Test
 - Add Web Interface
 - Add API

### Reference

 - [DHT TUTORIAL from rototron](https://www.rototron.info/dht22-tutorial-for-raspberry-pi/)
