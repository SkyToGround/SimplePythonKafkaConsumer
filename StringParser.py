#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from BaseDataParser import BaseDataParser

class StringParser(BaseDataParser):
    def __init__(self):
        param_list = ["nr_of_strings", "nr_of_words", "string"]
        self.nr_of_strings = 0
        super(StringParser, self).__init__(extra_params = param_list)
    
    def GetAttrValueStr(self, attr):
        
        return "n/a"

    def my_fb_parser(self, data):
        ret_dict = {}
        self.nr_of_strings += 1
        ret_dict["nr_of_strings"] = self.nr_of_strings
        ret_dict["nr_of_words"] = len(data.split(bytes(" ", "utf-8")))
        ret_dict["string"] = data
        
        return ret_dict
