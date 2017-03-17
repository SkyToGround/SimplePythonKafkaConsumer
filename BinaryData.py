#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from BaseDataParser import BaseDataParser
import codecs
import binascii
from curses.ascii import isprint

def printable(input):
    return ''.join(char for char in input if isprint(char))

class BinaryData(BaseDataParser):
    def __init__(self):
        param_list = ["raw", "as_str"]
        super(BinaryData, self).__init__(extra_params = param_list)
    
    def GetAttrValueStr(self, attr):
        
        return "n/a"

    def my_fb_parser(self, data):
        ret_dict = {}
        #ret_dict["raw"] = str(type(data))#':'.join(x.encode('hex') for x in data)
        ret_dict["raw"] = binascii.hexlify(data)
        
        
        ret_dict["as_str"] = printable(str(data))
        
        return ret_dict
