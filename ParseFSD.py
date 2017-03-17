#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import flatbuffers
from FSD import FastSamplingData
from BaseDataParser import BaseDataParser

class ParseFSD(BaseDataParser):
    def __init__(self):
        param_list = ["flatbuffer", "pv", "value", "value_type", "timestamp", "dimensions", "arr_length"]
        super(ParseFSD, self).__init__(param_list)
    
    def ExtractValue(self, fb_object):
        ret_str = "Unknown"
        if (fb_object.PvType() == PV.PV.NTScalarInt):
            val_obj = NTScalarInt.NTScalarInt()
        else:
            return "Unknown"
        
        val_obj.Init(fb_object.Pv().Bytes, fb_object.Pv().Pos)
        ret_str = str(val_obj.Value())
        return ret_str

    def my_fb_parser(self, data):
        ret_dict = {}
        try:
            fb_obj = FastSamplingData.FastSamplingData.GetRootAsFastSamplingData(bytearray(data), 0)
        except:
            ret_dict["flatbuffer"] = "Failed"
            return ret_dict
        ret_dict["flatbuffer"] = "Success"
        ret_dict["pv"] = fb_obj.Pv()
        ret_dict["value"] = "n/a"
        ret_dict["value_type"] = str(fb_obj.DataType())
        ret_dict["timestamp"] = str(fb_obj.Timestamp())
        dims_str = str(fb_obj.Dimensions(0))
        for i in range(1, fb_obj.DimensionsLength()):
            dims_str += "x" + str(fb_obj.Dimensions(i))
        ret_dict["dimensions"] = dims_str
        
        # ret_dict["fwdinfo.seq"] = str(fb_obj.Fwdinfo().Seq())
        # ret_dict["fwdinfo.ts_data"] = str(fb_obj.Fwdinfo().TsData())
        # ret_dict["fwdinfo.ts_fwd"] = str(fb_obj.Fwdinfo().TsFwd())
        # ret_dict["fwdinfo.fwdix"] = str(fb_obj.Fwdinfo().Fwdix())
        # ret_dict["fwdinfo.teamid"] = str(fb_obj.Fwdinfo().Teamid())
        return ret_dict
