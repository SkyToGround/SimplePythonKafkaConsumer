#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from FB_Tables import NDArray
import flatbuffers
from BaseDataParser import BaseDataParser
import numpy as np
import struct

# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class ParseNDArray_fb(BaseDataParser):
    def __init__(self):
        param_list = ["flatbuffer", "name", "id", "timestamp", "dims_length", "dims", "data_type", "data_bytes", "epics_epoch", "epics_nsec", "attributes"]
        super(ParseNDArray_fb, self).__init__(param_list)
        self.type_list = ["int8", "uint8", "int16", "uint16", "int32", "uint32", "float32", "float64", "c_string"]
        self.struct_char = ["b", "B", "h", "H", "i", "I", "f", "d", "s"]
        self.numpy_arr_type = [np.int8, np.uint8, np.int16, np.uint16, np.int32, np.uint32, np.float32, np.float64]
        self.img = None
        plt.ion()
    
    def GetAttrValueStr(self, attr):
        nr_of_bytes = attr.PDataLength()
        np_buffer = np.empty([nr_of_bytes, ], dtype = np.uint8)
        for i in range(nr_of_bytes):
            np_buffer[i] = attr.PData(i)
        data_buffer = np_buffer.tobytes()
        unpack_string = self.struct_char[attr.DataType()]
        return str(struct.unpack(unpack_string, data_buffer)[0])
    
    def GetDataArr(self, fb_arr):
        nr_of_bytes = fb_arr.PDataLength()
        dim_list = [fb_arr.Dims(0), ]
        for i in range(1, fb_arr.DimsLength()):
            dim_list.append(fb_arr.Dims(i))
        np_buffer = np.empty([nr_of_bytes, ], dtype = np.uint8)
        for i in range(nr_of_bytes):
            np_buffer[i] = fb_arr.PData(i)
        data_arr = np.fromstring(np_buffer.tobytes(), dtype = self.numpy_arr_type[fb_arr.DataType()]).reshape(dim_list)
        return data_arr

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
            attr_list.append(c_attr.PName().decode("utf-8") + " : " + self.GetAttrValueStr(c_attr) + " <%s>" % self.type_list[c_attr.DataType()])
        ret_dict["attributes"] = attr_list
        data = self.GetDataArr(arr)
        if (self.img == None):
            self.img = plt.imshow(data)
        else:
            self.img.set_array(data)
        plt.pause(0.001)
        
        return ret_dict
