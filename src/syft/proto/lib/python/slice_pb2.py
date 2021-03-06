# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/slice.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/slice.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1cproto/lib/python/slice.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"\xee\x01\n\x05Slice\x12\x12\n\x05start\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x11\n\x04stop\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x11\n\x04step\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12\x16\n\thas_start\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x15\n\x08has_stop\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x15\n\x08has_step\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12!\n\x02id\x18\x07 \x01(\x0b\x32\x15.syft.core.common.UIDB\x08\n\x06_startB\x07\n\x05_stopB\x07\n\x05_stepB\x0c\n\n_has_startB\x0b\n\t_has_stopB\x0b\n\t_has_stepb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_SLICE = _descriptor.Descriptor(
    name="Slice",
    full_name="syft.lib.python.Slice",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="start",
            full_name="syft.lib.python.Slice.start",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="stop",
            full_name="syft.lib.python.Slice.stop",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="step",
            full_name="syft.lib.python.Slice.step",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_start",
            full_name="syft.lib.python.Slice.has_start",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_stop",
            full_name="syft.lib.python.Slice.has_stop",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="has_step",
            full_name="syft.lib.python.Slice.has_step",
            index=5,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.Slice.id",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_start",
            full_name="syft.lib.python.Slice._start",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_stop",
            full_name="syft.lib.python.Slice._stop",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_step",
            full_name="syft.lib.python.Slice._step",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_start",
            full_name="syft.lib.python.Slice._has_start",
            index=3,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_stop",
            full_name="syft.lib.python.Slice._has_stop",
            index=4,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_step",
            full_name="syft.lib.python.Slice._has_step",
            index=5,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=89,
    serialized_end=327,
)

_SLICE.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SLICE.oneofs_by_name["_start"].fields.append(_SLICE.fields_by_name["start"])
_SLICE.fields_by_name["start"].containing_oneof = _SLICE.oneofs_by_name["_start"]
_SLICE.oneofs_by_name["_stop"].fields.append(_SLICE.fields_by_name["stop"])
_SLICE.fields_by_name["stop"].containing_oneof = _SLICE.oneofs_by_name["_stop"]
_SLICE.oneofs_by_name["_step"].fields.append(_SLICE.fields_by_name["step"])
_SLICE.fields_by_name["step"].containing_oneof = _SLICE.oneofs_by_name["_step"]
_SLICE.oneofs_by_name["_has_start"].fields.append(_SLICE.fields_by_name["has_start"])
_SLICE.fields_by_name["has_start"].containing_oneof = _SLICE.oneofs_by_name[
    "_has_start"
]
_SLICE.oneofs_by_name["_has_stop"].fields.append(_SLICE.fields_by_name["has_stop"])
_SLICE.fields_by_name["has_stop"].containing_oneof = _SLICE.oneofs_by_name["_has_stop"]
_SLICE.oneofs_by_name["_has_step"].fields.append(_SLICE.fields_by_name["has_step"])
_SLICE.fields_by_name["has_step"].containing_oneof = _SLICE.oneofs_by_name["_has_step"]
DESCRIPTOR.message_types_by_name["Slice"] = _SLICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Slice = _reflection.GeneratedProtocolMessageType(
    "Slice",
    (_message.Message,),
    {
        "DESCRIPTOR": _SLICE,
        "__module__": "proto.lib.python.slice_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Slice)
    },
)
_sym_db.RegisterMessage(Slice)


# @@protoc_insertion_point(module_scope)
