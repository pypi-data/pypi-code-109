# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graphscope/proto/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from graphscope.proto import error_codes_pb2 as graphscope_dot_proto_dot_error__codes__pb2
from graphscope.proto import op_def_pb2 as graphscope_dot_proto_dot_op__def__pb2
from graphscope.proto import types_pb2 as graphscope_dot_proto_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='graphscope/proto/message.proto',
  package='gs.rpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1egraphscope/proto/message.proto\x12\x06gs.rpc\x1a\"graphscope/proto/error_codes.proto\x1a\x1dgraphscope/proto/op_def.proto\x1a\x1cgraphscope/proto/types.proto\"w\n\x15\x43onnectSessionRequest\x12\x18\n\x10\x63leanup_instance\x18\x01 \x01(\x08\x12 \n\x18\x64\x61ngling_timeout_seconds\x18\x02 \x01(\x05\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x11\n\treconnect\x18\x04 \x01(\x08\"\xad\x01\n\x16\x43onnectSessionResponse\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12)\n\x0c\x63luster_type\x18\x03 \x01(\x0e\x32\x13.gs.rpc.ClusterType\x12\x15\n\rengine_config\x18\x04 \x01(\t\x12\x15\n\rpod_name_list\x18\x05 \x03(\t\x12\x13\n\x0bnum_workers\x18\x06 \x01(\x05\x12\x11\n\tnamespace\x18\x07 \x01(\t\"\x12\n\x10HeartBeatRequest\"\x13\n\x11HeartBeatResponse\"E\n\x0eRunStepRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x1f\n\x07\x64\x61g_def\x18\x02 \x01(\x0b\x32\x0e.gs.rpc.DagDef\"{\n\x0fRunStepResponse\x12!\n\x07results\x18\x01 \x03(\x0b\x32\x10.gs.rpc.OpResult\x12\x1a\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x0c.gs.rpc.Code\x12\x11\n\terror_msg\x18\x03 \x01(\t\x12\x16\n\x0e\x66ull_exception\x18\x04 \x01(\x0c\"&\n\x10\x46\x65tchLogsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"@\n\x11\x46\x65tchLogsResponse\x12\x14\n\x0cinfo_message\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\")\n\x13\x43loseSessionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\x16\n\x14\x43loseSessionResponseb\x06proto3'
  ,
  dependencies=[graphscope_dot_proto_dot_error__codes__pb2.DESCRIPTOR,graphscope_dot_proto_dot_op__def__pb2.DESCRIPTOR,graphscope_dot_proto_dot_types__pb2.DESCRIPTOR,])




_CONNECTSESSIONREQUEST = _descriptor.Descriptor(
  name='ConnectSessionRequest',
  full_name='gs.rpc.ConnectSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cleanup_instance', full_name='gs.rpc.ConnectSessionRequest.cleanup_instance', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dangling_timeout_seconds', full_name='gs.rpc.ConnectSessionRequest.dangling_timeout_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='gs.rpc.ConnectSessionRequest.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reconnect', full_name='gs.rpc.ConnectSessionRequest.reconnect', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=258,
)


_CONNECTSESSIONRESPONSE = _descriptor.Descriptor(
  name='ConnectSessionResponse',
  full_name='gs.rpc.ConnectSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='gs.rpc.ConnectSessionResponse.session_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_type', full_name='gs.rpc.ConnectSessionResponse.cluster_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='engine_config', full_name='gs.rpc.ConnectSessionResponse.engine_config', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pod_name_list', full_name='gs.rpc.ConnectSessionResponse.pod_name_list', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_workers', full_name='gs.rpc.ConnectSessionResponse.num_workers', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='gs.rpc.ConnectSessionResponse.namespace', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=434,
)


_HEARTBEATREQUEST = _descriptor.Descriptor(
  name='HeartBeatRequest',
  full_name='gs.rpc.HeartBeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=454,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartBeatResponse',
  full_name='gs.rpc.HeartBeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=475,
)


_RUNSTEPREQUEST = _descriptor.Descriptor(
  name='RunStepRequest',
  full_name='gs.rpc.RunStepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='gs.rpc.RunStepRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dag_def', full_name='gs.rpc.RunStepRequest.dag_def', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=546,
)


_RUNSTEPRESPONSE = _descriptor.Descriptor(
  name='RunStepResponse',
  full_name='gs.rpc.RunStepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='gs.rpc.RunStepResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='gs.rpc.RunStepResponse.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='gs.rpc.RunStepResponse.error_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_exception', full_name='gs.rpc.RunStepResponse.full_exception', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=671,
)


_FETCHLOGSREQUEST = _descriptor.Descriptor(
  name='FetchLogsRequest',
  full_name='gs.rpc.FetchLogsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='gs.rpc.FetchLogsRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=673,
  serialized_end=711,
)


_FETCHLOGSRESPONSE = _descriptor.Descriptor(
  name='FetchLogsResponse',
  full_name='gs.rpc.FetchLogsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_message', full_name='gs.rpc.FetchLogsResponse.info_message', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='gs.rpc.FetchLogsResponse.error_message', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=777,
)


_CLOSESESSIONREQUEST = _descriptor.Descriptor(
  name='CloseSessionRequest',
  full_name='gs.rpc.CloseSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='gs.rpc.CloseSessionRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=779,
  serialized_end=820,
)


_CLOSESESSIONRESPONSE = _descriptor.Descriptor(
  name='CloseSessionResponse',
  full_name='gs.rpc.CloseSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=844,
)

_CONNECTSESSIONRESPONSE.fields_by_name['cluster_type'].enum_type = graphscope_dot_proto_dot_types__pb2._CLUSTERTYPE
_RUNSTEPREQUEST.fields_by_name['dag_def'].message_type = graphscope_dot_proto_dot_op__def__pb2._DAGDEF
_RUNSTEPRESPONSE.fields_by_name['results'].message_type = graphscope_dot_proto_dot_op__def__pb2._OPRESULT
_RUNSTEPRESPONSE.fields_by_name['code'].enum_type = graphscope_dot_proto_dot_error__codes__pb2._CODE
DESCRIPTOR.message_types_by_name['ConnectSessionRequest'] = _CONNECTSESSIONREQUEST
DESCRIPTOR.message_types_by_name['ConnectSessionResponse'] = _CONNECTSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['HeartBeatRequest'] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['HeartBeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['RunStepRequest'] = _RUNSTEPREQUEST
DESCRIPTOR.message_types_by_name['RunStepResponse'] = _RUNSTEPRESPONSE
DESCRIPTOR.message_types_by_name['FetchLogsRequest'] = _FETCHLOGSREQUEST
DESCRIPTOR.message_types_by_name['FetchLogsResponse'] = _FETCHLOGSRESPONSE
DESCRIPTOR.message_types_by_name['CloseSessionRequest'] = _CLOSESESSIONREQUEST
DESCRIPTOR.message_types_by_name['CloseSessionResponse'] = _CLOSESESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectSessionRequest = _reflection.GeneratedProtocolMessageType('ConnectSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTSESSIONREQUEST,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ConnectSessionRequest)
  })
_sym_db.RegisterMessage(ConnectSessionRequest)

ConnectSessionResponse = _reflection.GeneratedProtocolMessageType('ConnectSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTSESSIONRESPONSE,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ConnectSessionResponse)
  })
_sym_db.RegisterMessage(ConnectSessionResponse)

HeartBeatRequest = _reflection.GeneratedProtocolMessageType('HeartBeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUEST,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.HeartBeatRequest)
  })
_sym_db.RegisterMessage(HeartBeatRequest)

HeartBeatResponse = _reflection.GeneratedProtocolMessageType('HeartBeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.HeartBeatResponse)
  })
_sym_db.RegisterMessage(HeartBeatResponse)

RunStepRequest = _reflection.GeneratedProtocolMessageType('RunStepRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNSTEPREQUEST,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.RunStepRequest)
  })
_sym_db.RegisterMessage(RunStepRequest)

RunStepResponse = _reflection.GeneratedProtocolMessageType('RunStepResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNSTEPRESPONSE,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.RunStepResponse)
  })
_sym_db.RegisterMessage(RunStepResponse)

FetchLogsRequest = _reflection.GeneratedProtocolMessageType('FetchLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHLOGSREQUEST,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.FetchLogsRequest)
  })
_sym_db.RegisterMessage(FetchLogsRequest)

FetchLogsResponse = _reflection.GeneratedProtocolMessageType('FetchLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHLOGSRESPONSE,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.FetchLogsResponse)
  })
_sym_db.RegisterMessage(FetchLogsResponse)

CloseSessionRequest = _reflection.GeneratedProtocolMessageType('CloseSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESESSIONREQUEST,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.CloseSessionRequest)
  })
_sym_db.RegisterMessage(CloseSessionRequest)

CloseSessionResponse = _reflection.GeneratedProtocolMessageType('CloseSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESESSIONRESPONSE,
  '__module__' : 'graphscope.proto.message_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.CloseSessionResponse)
  })
_sym_db.RegisterMessage(CloseSessionResponse)


# @@protoc_insertion_point(module_scope)
