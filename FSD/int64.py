# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FSD

import flatbuffers

class int64(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsint64(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = int64()
        x.Init(buf, n + offset)
        return x

    # int64
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # int64
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # int64
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def int64Start(builder): builder.StartObject(1)
def int64AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def int64StartValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def int64End(builder): return builder.EndObject()
