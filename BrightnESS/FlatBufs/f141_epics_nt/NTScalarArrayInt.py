# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class NTScalarArrayInt(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNTScalarArrayInt(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NTScalarArrayInt()
        x.Init(buf, n + offset)
        return x

    # NTScalarArrayInt
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NTScalarArrayInt
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # NTScalarArrayInt
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def NTScalarArrayIntStart(builder): builder.StartObject(1)
def NTScalarArrayIntAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def NTScalarArrayIntStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def NTScalarArrayIntEnd(builder): return builder.EndObject()
