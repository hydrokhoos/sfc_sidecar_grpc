# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"\x1b\n\x0b\x44\x61taRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\"S\n\x0c\x44\x61taResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x16\n\x0eprocessed_data\x18\x02 \x01(\x0c\x12\x1b\n\x13processed_timestamp\x18\x03 \x01(\t25\n\x07Service\x12*\n\x0bProcessData\x12\x0c.DataRequest\x1a\r.DataResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DATAREQUEST']._serialized_start=17
  _globals['_DATAREQUEST']._serialized_end=44
  _globals['_DATARESPONSE']._serialized_start=46
  _globals['_DATARESPONSE']._serialized_end=129
  _globals['_SERVICE']._serialized_start=131
  _globals['_SERVICE']._serialized_end=184
# @@protoc_insertion_point(module_scope)