#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from pykafka import KafkaClient
from pykafka.common import OffsetType
import argparse
import signal
import time
import struct

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help = "Broker to connect to.", type = str)
    parser.add_argument("-t", help = "Topic to subscribe to.", type = str)
    parser.add_argument("-p", help = "Name of the file holding the parser. Defaults to \"BaseDataParser\".", type = str)
    parser.add_argument("-d", help = "Run in debug mode. Will not clean up curses-library on exit so that error messages can be seen.", action="store_true")
    args = parser.parse_args()
    
    class_name_str = "BaseDataParser"
    if(args.p != None):
        class_name_str = args.p
    
    if (args.b == None or args.t == None):
        print("Broker and topic must be given as arguments.")
        exit(0)
    client = KafkaClient(hosts=args.b)
    topic = client.topics[bytes(args.t, "utf-8")]
    #consumer = topic.get_simple_consumer(fetch_message_max_bytes = 1024 * 1024 * 50)
    consumer = topic.get_simple_consumer(fetch_message_max_bytes = 1024 * 1024 * 50, consumer_group=bytes("mygroup", "utf-8"), auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True, consumer_timeout_ms=50)
    #consumer.
    
    parser = None
    
    try:
        exec("from %s import %s" % (class_name_str, class_name_str))
    except Exception as e:
        print("Unable to import parser with name \"%s\"." % class_name_str)
        print("Got error: " + str(e))
        exit(1)
    
    try:
        parser = eval("%s()" % class_name_str)
        if (not args.d):
            parser.debug = False
    except Exception as e:
        try:
            del parser
        except:
            pass
        print("Unable to instantiate \"%s\"" % class_name_str)
        print("Got error: " + str(e))
        exit(1)
    
    while (True):
        try:
            msg = consumer.consume(block = True)
            if (msg != None):
                parser.parse_data(msg.value, msg.offset)
            else:
                parser.no_data()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()