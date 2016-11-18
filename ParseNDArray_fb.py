#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from FB_Tables import NDArray
import flatbuffers
from BaseDataParser import BaseDataParser

class ParseNDArray_fb(BaseDataParser):
    def __init__(self):
        param_list = ["flatbuffer", "name", "id", "timestamp", "dims_length", "dims", "data_type", "data_bytes", "epics_epoch", "epics_nsec", "attributes"]
        super(ParseNDArray_fb, self).__init__(param_list)
        self.type_list = ["int8", "uint8", "int16", "uint16", "int32", "uint32", "float32", "float64", "c_string"]
    
    def GetAttrValueStr(self, attr):
        
        return "n/a"

    def my_fb_parser(self, data):
        ret_dict = {}
        try:
            arr = NDArray.NDArray.GetRootAsNDArray(bytearray(data), 0)
        except:
            ret_dict["flatbuffer"] = "Failed"
            return ret_dict
        ret_dict["flatbuffer"] = "Success"
        ret_dict["timestamp"] = arr.TimeStamp()
        ret_dict["name"] = arr.Name()
        ret_dict["id"] = arr.Id()
        ret_dict["dims_length"] = arr.DimsLength()
        dims_str = str(arr.Dims(0))
        for i in range(1, arr.DimsLength()):
            dims_str += "x" + str(arr.Dims(i))
        ret_dict["dims"] = dims_str
        ret_dict["data_type"] = self.type_list[arr.DataType()]
        ret_dict["data_bytes"] = arr.PDataLength()
        e_ts = arr.EpicsTS()
        ret_dict["epics_epoch"] = e_ts.SecPastEpoch()
        ret_dict["epics_nsec"] = e_ts.Nsec()
        
        attr_list = []
        nr_of_attr = arr.PAttributeListLength()
        for j in range(nr_of_attr):
            c_attr = arr.PAttributeList(j)
            attr_list.append(c_attr.PName().decode("utf-8") + " : " + self.GetAttrValueStr(c_attr) + "<%s>" % self.type_list[c_attr.DataType()])
        ret_dict["attributes"] = attr_list
        
        return ret_dict
