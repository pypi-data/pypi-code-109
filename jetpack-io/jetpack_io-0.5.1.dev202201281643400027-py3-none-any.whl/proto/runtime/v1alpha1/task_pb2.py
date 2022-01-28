# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jetpack/proto/runtime/v1alpha1/task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jetpack.proto.runtime.v1alpha1 import remote_pb2 as jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jetpack/proto/runtime/v1alpha1/task.proto',
  package='task',
  syntax='proto3',
  serialized_options=b'\n\010com.taskB\tTaskProtoP\001Z2go.jetpack.io/proto/jetpack/proto/runtime/v1alpha1\242\002\003TXX\252\002\004Task\312\002\004Task\342\002\020Task\\GPBMetadata\352\002\004Task',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)jetpack/proto/runtime/v1alpha1/task.proto\x12\x04task\x1a+jetpack/proto/runtime/v1alpha1/remote.proto\"\x91\x03\n\rPersistedTask\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x10qualified_symbol\x18\x02 \x01(\tR\x0fqualifiedSymbol\x12!\n\x0c\x65ncoded_args\x18\x03 \x01(\x0cR\x0b\x65ncodedArgs\x12\x1a\n\x08manifest\x18\x04 \x01(\x0cR\x08manifest\x12\x32\n\x06status\x18\x05 \x01(\x0e\x32\x1a.task.PersistedTask.StatusR\x06status\x12&\n\x06result\x18\x06 \x01(\x0b\x32\x0e.remote.ResultR\x06result\x12\x19\n\x08\x61pp_name\x18\x07 \x01(\tR\x07\x61ppName\"\x8e\x01\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07WAITING\x10\x02\x12\t\n\x05READY\x10\x03\x12\x0b\n\x07RUNNING\x10\x04\x12\r\n\tSUCCEEDED\x10\x05\x12\x0e\n\nCANCELLING\x10\x06\x12\r\n\tCANCELLED\x10\x07\x12\x0b\n\x07\x46\x41ILING\x10\x08\x12\n\n\x06\x46\x41ILED\x10\tBy\n\x08\x63om.taskB\tTaskProtoP\x01Z2go.jetpack.io/proto/jetpack/proto/runtime/v1alpha1\xa2\x02\x03TXX\xaa\x02\x04Task\xca\x02\x04Task\xe2\x02\x10Task\\GPBMetadata\xea\x02\x04Taskb\x06proto3'
  ,
  dependencies=[jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.DESCRIPTOR,])



_PERSISTEDTASK_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='task.PersistedTask.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELLING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILING', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=356,
  serialized_end=498,
)
_sym_db.RegisterEnumDescriptor(_PERSISTEDTASK_STATUS)


_PERSISTEDTASK = _descriptor.Descriptor(
  name='PersistedTask',
  full_name='task.PersistedTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.PersistedTask.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qualified_symbol', full_name='task.PersistedTask.qualified_symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='qualifiedSymbol', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encoded_args', full_name='task.PersistedTask.encoded_args', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='encodedArgs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='task.PersistedTask.manifest', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='manifest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='task.PersistedTask.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='task.PersistedTask.result', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='result', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='task.PersistedTask.app_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='appName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERSISTEDTASK_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=498,
)

_PERSISTEDTASK.fields_by_name['status'].enum_type = _PERSISTEDTASK_STATUS
_PERSISTEDTASK.fields_by_name['result'].message_type = jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2._RESULT
_PERSISTEDTASK_STATUS.containing_type = _PERSISTEDTASK
DESCRIPTOR.message_types_by_name['PersistedTask'] = _PERSISTEDTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersistedTask = _reflection.GeneratedProtocolMessageType('PersistedTask', (_message.Message,), {
  'DESCRIPTOR' : _PERSISTEDTASK,
  '__module__' : 'jetpack.proto.runtime.v1alpha1.task_pb2'
  # @@protoc_insertion_point(class_scope:task.PersistedTask)
  })
_sym_db.RegisterMessage(PersistedTask)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
