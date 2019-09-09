# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_transform.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_transform.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\022DataTransformProto'),
  serialized_pb=_b('\n\x14\x64\x61ta_transform.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\x84\x06\n\rDataTransform\x12\x14\n\x0cmissing_fill\x18\x01 \x01(\x08\x12\x1e\n\x16missing_replace_method\x18\x02 \x01(\t\x12\x15\n\rmissing_value\x18\x03 \x03(\t\x12m\n\x15missing_replace_value\x18\x04 \x03(\x0b\x32N.com.webank.ai.fate.core.mlmodel.buffer.DataTransform.MissingReplaceValueEntry\x12\x17\n\x0foutlier_replace\x18\x05 \x01(\x08\x12\x1e\n\x16outlier_replace_method\x18\x06 \x01(\t\x12\x15\n\routlier_value\x18\x07 \x03(\t\x12m\n\x15outlier_replace_value\x18\x08 \x03(\x0b\x32N.com.webank.ai.fate.core.mlmodel.buffer.DataTransform.OutlierReplaceValueEntry\x12\x10\n\x08is_scale\x18\t \x01(\x08\x12\x14\n\x0cscale_method\x18\n \x01(\t\x12i\n\x13scale_replace_value\x18\x0b \x03(\x0b\x32L.com.webank.ai.fate.core.mlmodel.buffer.DataTransform.ScaleReplaceValueEntry\x1a:\n\x18MissingReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a:\n\x18OutlierReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1am\n\x16ScaleReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.com.webank.ai.fate.core.mlmodel.buffer.ScaleObject:\x02\x38\x01\"z\n\x0bScaleObject\x12\x12\n\nfeat_upper\x18\x0c \x01(\x02\x12\x12\n\nfeat_lower\x18\r \x01(\x02\x12\x11\n\tout_upper\x18\x0e \x01(\x02\x12\x11\n\tout_lower\x18\x0f \x01(\x02\x12\x0c\n\x04mean\x18\x10 \x01(\x02\x12\x0f\n\x07std_var\x18\x11 \x01(\x02\x42\x14\x42\x12\x44\x61taTransformProtob\x06proto3')
)




_DATATRANSFORM_MISSINGREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='MissingReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.MissingReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.MissingReplaceValueEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.MissingReplaceValueEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=666,
)

_DATATRANSFORM_OUTLIERREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='OutlierReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.OutlierReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.OutlierReplaceValueEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.OutlierReplaceValueEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=726,
)

_DATATRANSFORM_SCALEREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='ScaleReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.ScaleReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.ScaleReplaceValueEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.ScaleReplaceValueEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=728,
  serialized_end=837,
)

_DATATRANSFORM = _descriptor.Descriptor(
  name='DataTransform',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missing_fill', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.missing_fill', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_replace_method', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.missing_replace_method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.missing_value', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.missing_replace_value', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_replace', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.outlier_replace', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_replace_method', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.outlier_replace_method', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.outlier_value', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.outlier_replace_value', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_scale', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.is_scale', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_method', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.scale_method', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransform.scale_replace_value', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATATRANSFORM_MISSINGREPLACEVALUEENTRY, _DATATRANSFORM_OUTLIERREPLACEVALUEENTRY, _DATATRANSFORM_SCALEREPLACEVALUEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=837,
)


_SCALEOBJECT = _descriptor.Descriptor(
  name='ScaleObject',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feat_upper', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.feat_upper', index=0,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feat_lower', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.feat_lower', index=1,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_upper', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.out_upper', index=2,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_lower', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.out_lower', index=3,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.mean', index=4,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std_var', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleObject.std_var', index=5,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=839,
  serialized_end=961,
)

_DATATRANSFORM_MISSINGREPLACEVALUEENTRY.containing_type = _DATATRANSFORM
_DATATRANSFORM_OUTLIERREPLACEVALUEENTRY.containing_type = _DATATRANSFORM
_DATATRANSFORM_SCALEREPLACEVALUEENTRY.fields_by_name['value'].message_type = _SCALEOBJECT
_DATATRANSFORM_SCALEREPLACEVALUEENTRY.containing_type = _DATATRANSFORM
_DATATRANSFORM.fields_by_name['missing_replace_value'].message_type = _DATATRANSFORM_MISSINGREPLACEVALUEENTRY
_DATATRANSFORM.fields_by_name['outlier_replace_value'].message_type = _DATATRANSFORM_OUTLIERREPLACEVALUEENTRY
_DATATRANSFORM.fields_by_name['scale_replace_value'].message_type = _DATATRANSFORM_SCALEREPLACEVALUEENTRY
DESCRIPTOR.message_types_by_name['DataTransform'] = _DATATRANSFORM
DESCRIPTOR.message_types_by_name['ScaleObject'] = _SCALEOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataTransform = _reflection.GeneratedProtocolMessageType('DataTransform', (_message.Message,), dict(

  MissingReplaceValueEntry = _reflection.GeneratedProtocolMessageType('MissingReplaceValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORM_MISSINGREPLACEVALUEENTRY,
    __module__ = 'data_transform_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransform.MissingReplaceValueEntry)
    ))
  ,

  OutlierReplaceValueEntry = _reflection.GeneratedProtocolMessageType('OutlierReplaceValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORM_OUTLIERREPLACEVALUEENTRY,
    __module__ = 'data_transform_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransform.OutlierReplaceValueEntry)
    ))
  ,

  ScaleReplaceValueEntry = _reflection.GeneratedProtocolMessageType('ScaleReplaceValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORM_SCALEREPLACEVALUEENTRY,
    __module__ = 'data_transform_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransform.ScaleReplaceValueEntry)
    ))
  ,
  DESCRIPTOR = _DATATRANSFORM,
  __module__ = 'data_transform_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransform)
  ))
_sym_db.RegisterMessage(DataTransform)
_sym_db.RegisterMessage(DataTransform.MissingReplaceValueEntry)
_sym_db.RegisterMessage(DataTransform.OutlierReplaceValueEntry)
_sym_db.RegisterMessage(DataTransform.ScaleReplaceValueEntry)

ScaleObject = _reflection.GeneratedProtocolMessageType('ScaleObject', (_message.Message,), dict(
  DESCRIPTOR = _SCALEOBJECT,
  __module__ = 'data_transform_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ScaleObject)
  ))
_sym_db.RegisterMessage(ScaleObject)


DESCRIPTOR._options = None
_DATATRANSFORM_MISSINGREPLACEVALUEENTRY._options = None
_DATATRANSFORM_OUTLIERREPLACEVALUEENTRY._options = None
_DATATRANSFORM_SCALEREPLACEVALUEENTRY._options = None
# @@protoc_insertion_point(module_scope)