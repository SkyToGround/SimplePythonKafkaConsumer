# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FSD

import flatbuffers

class int8(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsint8(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = int8()
        x.Init(buf, n + offset)
        return x

    # int8
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # int8
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # int8
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def int8Start(builder): builder.StartObject(1)
def int8AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def int8StartValueVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def int8End(builder): return builder.EndObject()
