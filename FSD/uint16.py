# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FSD

import flatbuffers

class uint16(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsuint16(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = uint16()
        x.Init(buf, n + offset)
        return x

    # uint16
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # uint16
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # uint16
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def uint16Start(builder): builder.StartObject(1)
def uint16AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def uint16StartValueVector(builder, numElems): return builder.StartVector(2, numElems, 2)
def uint16End(builder): return builder.EndObject()