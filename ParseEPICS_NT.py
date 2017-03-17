#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import flatbuffers
from BrightnESS.FlatBufs.f141_epics_nt import EpicsPV, PV, NTScalarInt
from BaseDataParser import BaseDataParser

class ParseEPICS_NT(BaseDataParser):
    def __init__(self):
        param_list = ["flatbuffer", "pv", "value", "value_type", "timestamp.seconds", "timestamp.nsec", "fwdinfo.seq", "fwdinfo.ts_data", "fwdinfo.ts_fwd", "fwdinfo.fwdix", "fwdinfo.teamid", "fwdinfo2.seq_data", "fwdinfo2.seq_fwd", "fwdinfo2.ts_data", "fwdinfo2.ts_fwd", "fwdinfo2.fwdix", "fwdinfo2.teamid"]
        super(ParseEPICS_NT, self).__init__(param_list)
    
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
            fb_obj = EpicsPV.EpicsPV.GetRootAsEpicsPV(bytearray(data), 0)
        except:
            ret_dict["flatbuffer"] = "Failed"
            return ret_dict
        ret_dict["flatbuffer"] = "Success"
        ret_dict["pv"] = fb_obj.Name()
        ret_dict["value"] = self.ExtractValue(fb_obj)
        ret_dict["value_type"] = str(fb_obj.PvType())
        ret_dict["timestamp.seconds"] = str(fb_obj.TimeStamp().SecondsPastEpoch())
        ret_dict["timestamp.nsec"] = str(fb_obj.TimeStamp().Nanoseconds())
        # ret_dict["fwdinfo.seq"] = str(fb_obj.Fwdinfo().Seq())
        # ret_dict["fwdinfo.ts_data"] = str(fb_obj.Fwdinfo().TsData())
        # ret_dict["fwdinfo.ts_fwd"] = str(fb_obj.Fwdinfo().TsFwd())
        # ret_dict["fwdinfo.fwdix"] = str(fb_obj.Fwdinfo().Fwdix())
        # ret_dict["fwdinfo.teamid"] = str(fb_obj.Fwdinfo().Teamid())
        return ret_dict
