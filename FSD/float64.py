# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FSD

import flatbuffers

class float64(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsfloat64(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = float64()
        x.Init(buf, n + offset)
        return x

    # float64
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # float64
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # float64
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def float64Start(builder): builder.StartObject(1)
def float64AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def float64StartValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def float64End(builder): return builder.EndObject()
