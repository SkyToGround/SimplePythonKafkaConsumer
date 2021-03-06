# SimplePythonKafkaConsumer
A very simple Python application used to consume Kafka messages. Displays information about those messages using curses. It is relatively easy to extend functionality by writing your own parser that inherits from `BaseDataParser`. 

## Requirements
This application uses PyKafka for Kafka consumer functionality. Download it from here:
[https://github.com/Parsely/pykafka](https://github.com/Parsely/pykafka).

For the `ParseNDArray_fb` parser, flatbuffers is required which can be downloaded from: [https://github.com/google/flatbuffers](https://github.com/google/flatbuffers). The visualisation functionality in `ParseNDArray_fb` also requires `matplotlib` to be installed.

All other libraries should be included in a standard Python installation. The application has been tested with Python 2.7 and Python 3.5 and should work with all versions in between.

## Running the application
The following arguments are possible/required:

* `-b` Broker to connect to (required).
* `-t` Topic to subscribe to (required).
* `-p` Parser to use, defaults to "BaseDataParser".
* `-d` Debug mode, usefull when writing new parsers.

Some examples of running the application follows:

    python3.5 ConsumerTest.py -b 10.4.0.215:9092 -t ad_topic -p StringParser

    python3.5 ConsumerTest.py -b 10.4.0.215:9092 -t ad_topic
    
    python3.5 ConsumerTest.py -d -b 10.4.0.215:9092 -t ad_topic

## Extending the functionality
Use `StrinParser.py` and `ParseNDArray_fb.py` as templates for writing your own parsers.

