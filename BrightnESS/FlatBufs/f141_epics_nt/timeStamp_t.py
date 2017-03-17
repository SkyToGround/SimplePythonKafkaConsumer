# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class timeStamp_t(object):
    __slots__ = ['_tab']

    # timeStamp_t
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # timeStamp_t
    def SecondsPastEpoch(self): return self._tab.Get(flatbuffers.number_types.Uint64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # timeStamp_t
    def Nanoseconds(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))

def CreatetimeStamp_t(builder, secondsPastEpoch, nanoseconds):
    builder.Prep(8, 16)
    builder.Pad(4)
    builder.PrependInt32(nanoseconds)
    builder.PrependUint64(secondsPastEpoch)
    return builder.Offset()