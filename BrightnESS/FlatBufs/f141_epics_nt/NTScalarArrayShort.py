# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class NTScalarArrayShort(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNTScalarArrayShort(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NTScalarArrayShort()
        x.Init(buf, n + offset)
        return x

    # NTScalarArrayShort
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NTScalarArrayShort
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # NTScalarArrayShort
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def NTScalarArrayShortStart(builder): builder.StartObject(1)
def NTScalarArrayShortAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def NTScalarArrayShortStartValueVector(builder, numElems): return builder.StartVector(2, numElems, 2)
def NTScalarArrayShortEnd(builder): return builder.EndObject()