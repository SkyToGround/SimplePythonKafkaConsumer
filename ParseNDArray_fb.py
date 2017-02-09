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
hasSavedOne = False

class ParseNDArray_fb(BaseDataParser):
    def __init__(self):
        param_list = ["flatbuffer", "id", "timestamp", "dims_length", "dims", "data_type", "data_bytes", "epics_epoch", "epics_nsec", "attributes"]
        super(ParseNDArray_fb, self).__init__(param_list)
        self.type_list = [u"int8", u"uint8", u"int16", u"uint16", u"int32", u"uint32", u"float32", u"float64", u"c_string"]
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
        raw_data = fb_arr.PData_as_numpy_array()
        dim_list = [fb_arr.Dims(0), ]
        for i in range(1, fb_arr.DimsLength()):
            dim_list.append(fb_arr.Dims(i))
        data_arr = raw_data.view(self.numpy_arr_type[fb_arr.DataType()]).reshape(dim_list)
        return data_arr

    def my_fb_parser(self, data):
        global hasSavedOne
        if (not hasSavedOne):
            out_file = open("someNDArray.data", "wb")
            out_file.write(data)
            out_file.close()
            hasSavedOne = True
        ret_dict = {}
        try:
            arr = NDArray.NDArray.GetRootAsNDArray(bytearray(data), 0)
        except:
            ret_dict["flatbuffer"] = "Failed"
            return ret_dict
        ret_dict["flatbuffer"] = "Success"
        ret_dict["timestamp"] = arr.TimeStamp()
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
            attr_list.append(c_attr.PName().decode("utf-8") + u" : " + self.GetAttrValueStr(c_attr) + u" <%s>" % self.type_list[c_attr.DataType()])
        ret_dict["attributes"] = attr_list
        data = self.GetDataArr(arr)
        # if (arr.DimsLength() == 3):
        #     #data = np.rollaxis(data, 0, 3)
        #     data = data.transpose()
        if (self.img == None):
            self.img = plt.imshow(data)
            self.im_dims = dims_str
        else:
            if (self.im_dims == dims_str):
                self.img.set_array(data)
            else:
                self.im_dims = dims_str
                plt.clf()
                self.img = plt.imshow(data)
        plt.pause(0.001)
        
        return ret_dict
