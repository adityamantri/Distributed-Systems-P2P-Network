# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataverse.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataverse.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0f\x64\x61taverse.proto\"o\n\x12ImageUploadRequest\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\x12\n\n\x02Id\x18\x02 \x01(\t\x12*\n\nStatusCode\x18\x03 \x01(\x0e\x32\x16.ImageUploadStatusCode\x12\x10\n\x08Username\x18\x04 \x01(\t\"p\n\x13ImageUploadResponse\x12\n\n\x02Id\x18\x01 \x01(\t\x12*\n\nStatusCode\x18\x02 \x01(\x0e\x32\x16.ImageUploadStatusCode\x12\x0f\n\x07Message\x18\x03 \x01(\t\x12\x10\n\x08Username\x18\x04 \x01(\t\"3\n\rSearchRequest\x12\x10\n\x08\x46ilename\x18\x01 \x01(\t\x12\x10\n\x08Username\x18\x02 \x01(\t\"W\n\x0eSearchResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\t\x12\x17\n\x0fnodeConnections\x18\x02 \x03(\t\x12\x0f\n\x07\x43ontent\x18\x03 \x01(\x0c\x12\x0c\n\x04\x46ile\x18\x04 \x01(\t\"\x1f\n\rConfigRequest\x12\x0e\n\x06Server\x18\x01 \x01(\t\" \n\x0e\x43onfigResponse\x12\x0e\n\x06Status\x18\x01 \x01(\t*H\n\x15ImageUploadStatusCode\x12\x06\n\x02Ok\x10\x00\x12\n\n\x06\x46\x61iled\x10\x01\x12\x0b\n\x07Unknown\x10\x02\x12\x0e\n\nInProgress\x10\x03\x32\x9c\x01\n\x07Greeter\x12\x37\n\x06Upload\x12\x13.ImageUploadRequest\x1a\x14.ImageUploadResponse\"\x00(\x01\x12+\n\x06Search\x12\x0e.SearchRequest\x1a\x0f.SearchResponse\"\x00\x12+\n\x06\x43onfig\x12\x0e.ConfigRequest\x1a\x0f.ConfigResponse\"\x00\x62\x06proto3'
)

_IMAGEUPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='ImageUploadStatusCode',
  full_name='ImageUploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ok', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InProgress', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=455,
  serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_IMAGEUPLOADSTATUSCODE)

ImageUploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_IMAGEUPLOADSTATUSCODE)
Ok = 0
Failed = 1
Unknown = 2
InProgress = 3



_IMAGEUPLOADREQUEST = _descriptor.Descriptor(
  name='ImageUploadRequest',
  full_name='ImageUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='ImageUploadRequest.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Id', full_name='ImageUploadRequest.Id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='ImageUploadRequest.StatusCode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Username', full_name='ImageUploadRequest.Username', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=19,
  serialized_end=130,
)


_IMAGEUPLOADRESPONSE = _descriptor.Descriptor(
  name='ImageUploadResponse',
  full_name='ImageUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='ImageUploadResponse.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='ImageUploadResponse.StatusCode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Message', full_name='ImageUploadResponse.Message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Username', full_name='ImageUploadResponse.Username', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=132,
  serialized_end=244,
)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Filename', full_name='SearchRequest.Filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Username', full_name='SearchRequest.Username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=246,
  serialized_end=297,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='found', full_name='SearchResponse.found', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeConnections', full_name='SearchResponse.nodeConnections', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Content', full_name='SearchResponse.Content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='File', full_name='SearchResponse.File', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=299,
  serialized_end=386,
)


_CONFIGREQUEST = _descriptor.Descriptor(
  name='ConfigRequest',
  full_name='ConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Server', full_name='ConfigRequest.Server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=388,
  serialized_end=419,
)


_CONFIGRESPONSE = _descriptor.Descriptor(
  name='ConfigResponse',
  full_name='ConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Status', full_name='ConfigResponse.Status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=421,
  serialized_end=453,
)

_IMAGEUPLOADREQUEST.fields_by_name['StatusCode'].enum_type = _IMAGEUPLOADSTATUSCODE
_IMAGEUPLOADRESPONSE.fields_by_name['StatusCode'].enum_type = _IMAGEUPLOADSTATUSCODE
DESCRIPTOR.message_types_by_name['ImageUploadRequest'] = _IMAGEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['ImageUploadResponse'] = _IMAGEUPLOADRESPONSE
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['ConfigRequest'] = _CONFIGREQUEST
DESCRIPTOR.message_types_by_name['ConfigResponse'] = _CONFIGRESPONSE
DESCRIPTOR.enum_types_by_name['ImageUploadStatusCode'] = _IMAGEUPLOADSTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageUploadRequest = _reflection.GeneratedProtocolMessageType('ImageUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADREQUEST,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:ImageUploadRequest)
  })
_sym_db.RegisterMessage(ImageUploadRequest)

ImageUploadResponse = _reflection.GeneratedProtocolMessageType('ImageUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADRESPONSE,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:ImageUploadResponse)
  })
_sym_db.RegisterMessage(ImageUploadResponse)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREQUEST,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:ConfigRequest)
  })
_sym_db.RegisterMessage(ConfigRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGRESPONSE,
  '__module__' : 'dataverse_pb2'
  # @@protoc_insertion_point(class_scope:ConfigResponse)
  })
_sym_db.RegisterMessage(ConfigResponse)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=530,
  serialized_end=686,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='Greeter.Upload',
    index=0,
    containing_service=None,
    input_type=_IMAGEUPLOADREQUEST,
    output_type=_IMAGEUPLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='Greeter.Search',
    index=1,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Config',
    full_name='Greeter.Config',
    index=2,
    containing_service=None,
    input_type=_CONFIGREQUEST,
    output_type=_CONFIGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
