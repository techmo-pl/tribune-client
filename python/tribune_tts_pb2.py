# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tribune_tts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tribune_tts.proto',
  package='techmo.tribune',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11tribune_tts.proto\x12\x0etechmo.tribune\"%\n\x11ListVoicesRequest\x12\x10\n\x08language\x18\x01 \x01(\t\";\n\x12ListVoicesResponse\x12%\n\x06voices\x18\x01 \x03(\x0b\x32\x15.techmo.tribune.Voice\"S\n\x11SynthesizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .techmo.tribune.SynthesizeConfig\"}\n\x10SynthesizeConfig\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x31\n\x0c\x61udio_config\x18\x02 \x01(\x0b\x32\x1b.techmo.tribune.AudioConfig\x12$\n\x05voice\x18\x03 \x01(\x0b\x32\x15.techmo.tribune.Voice\"\x9b\x01\n\x0b\x41udioConfig\x12\x35\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32\x1d.techmo.tribune.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\r\n\x05pitch\x18\x03 \x01(\x02\x12\r\n\x05range\x18\x04 \x01(\x02\x12\x0c\n\x04rate\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\"=\n\x05Voice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06gender\x18\x02 \x01(\x0e\x32\x16.techmo.tribune.Gender\"d\n\x12SynthesizeResponse\x12(\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x19.techmo.tribune.AudioData\x12$\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x15.techmo.tribune.Error\"7\n\tAudioData\x12\x19\n\x11sample_rate_hertz\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"E\n\x05\x45rror\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.techmo.tribune.ErrorCode\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t**\n\rAudioEncoding\x12\t\n\x05PCM16\x10\x00\x12\x0e\n\nOGG_VORBIS\x10\x01*/\n\x06Gender\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\x08\n\x04MALE\x10\x02*_\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07LICENCE\x10\x01\x12\x16\n\x12TEXT_NORMALIZATION\x10\x02\x12\x11\n\rTRANSCRIPTION\x10\x03\x12\r\n\tSYNTHESIS\x10\x04\x32\x8f\x02\n\x03TTS\x12S\n\nListVoices\x12!.techmo.tribune.ListVoicesRequest\x1a\".techmo.tribune.ListVoicesResponse\x12^\n\x13SynthesizeStreaming\x12!.techmo.tribune.SynthesizeRequest\x1a\".techmo.tribune.SynthesizeResponse0\x01\x12S\n\nSynthesize\x12!.techmo.tribune.SynthesizeRequest\x1a\".techmo.tribune.SynthesizeResponseb\x06proto3')
)

_AUDIOENCODING = _descriptor.EnumDescriptor(
  name='AudioEncoding',
  full_name='techmo.tribune.AudioEncoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PCM16', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OGG_VORBIS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=800,
  serialized_end=842,
)
_sym_db.RegisterEnumDescriptor(_AUDIOENCODING)

AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='techmo.tribune.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=844,
  serialized_end=891,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='techmo.tribune.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_NORMALIZATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSCRIPTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNTHESIS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=893,
  serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
PCM16 = 0
OGG_VORBIS = 1
UNSPECIFIED = 0
FEMALE = 1
MALE = 2
UNKNOWN = 0
LICENCE = 1
TEXT_NORMALIZATION = 2
TRANSCRIPTION = 3
SYNTHESIS = 4



_LISTVOICESREQUEST = _descriptor.Descriptor(
  name='ListVoicesRequest',
  full_name='techmo.tribune.ListVoicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='techmo.tribune.ListVoicesRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=74,
)


_LISTVOICESRESPONSE = _descriptor.Descriptor(
  name='ListVoicesResponse',
  full_name='techmo.tribune.ListVoicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voices', full_name='techmo.tribune.ListVoicesResponse.voices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=76,
  serialized_end=135,
)


_SYNTHESIZEREQUEST = _descriptor.Descriptor(
  name='SynthesizeRequest',
  full_name='techmo.tribune.SynthesizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='techmo.tribune.SynthesizeRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='techmo.tribune.SynthesizeRequest.config', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=220,
)


_SYNTHESIZECONFIG = _descriptor.Descriptor(
  name='SynthesizeConfig',
  full_name='techmo.tribune.SynthesizeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='techmo.tribune.SynthesizeConfig.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_config', full_name='techmo.tribune.SynthesizeConfig.audio_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice', full_name='techmo.tribune.SynthesizeConfig.voice', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=347,
)


_AUDIOCONFIG = _descriptor.Descriptor(
  name='AudioConfig',
  full_name='techmo.tribune.AudioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_encoding', full_name='techmo.tribune.AudioConfig.audio_encoding', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='techmo.tribune.AudioConfig.sample_rate_hertz', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='techmo.tribune.AudioConfig.pitch', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='techmo.tribune.AudioConfig.range', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate', full_name='techmo.tribune.AudioConfig.rate', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='techmo.tribune.AudioConfig.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=350,
  serialized_end=505,
)


_VOICE = _descriptor.Descriptor(
  name='Voice',
  full_name='techmo.tribune.Voice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='techmo.tribune.Voice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='techmo.tribune.Voice.gender', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=507,
  serialized_end=568,
)


_SYNTHESIZERESPONSE = _descriptor.Descriptor(
  name='SynthesizeResponse',
  full_name='techmo.tribune.SynthesizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='techmo.tribune.SynthesizeResponse.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='techmo.tribune.SynthesizeResponse.error', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=670,
)


_AUDIODATA = _descriptor.Descriptor(
  name='AudioData',
  full_name='techmo.tribune.AudioData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='techmo.tribune.AudioData.sample_rate_hertz', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='techmo.tribune.AudioData.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=672,
  serialized_end=727,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='techmo.tribune.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='techmo.tribune.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='techmo.tribune.Error.description', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=798,
)

_LISTVOICESRESPONSE.fields_by_name['voices'].message_type = _VOICE
_SYNTHESIZEREQUEST.fields_by_name['config'].message_type = _SYNTHESIZECONFIG
_SYNTHESIZECONFIG.fields_by_name['audio_config'].message_type = _AUDIOCONFIG
_SYNTHESIZECONFIG.fields_by_name['voice'].message_type = _VOICE
_AUDIOCONFIG.fields_by_name['audio_encoding'].enum_type = _AUDIOENCODING
_VOICE.fields_by_name['gender'].enum_type = _GENDER
_SYNTHESIZERESPONSE.fields_by_name['audio'].message_type = _AUDIODATA
_SYNTHESIZERESPONSE.fields_by_name['error'].message_type = _ERROR
_ERROR.fields_by_name['code'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['ListVoicesRequest'] = _LISTVOICESREQUEST
DESCRIPTOR.message_types_by_name['ListVoicesResponse'] = _LISTVOICESRESPONSE
DESCRIPTOR.message_types_by_name['SynthesizeRequest'] = _SYNTHESIZEREQUEST
DESCRIPTOR.message_types_by_name['SynthesizeConfig'] = _SYNTHESIZECONFIG
DESCRIPTOR.message_types_by_name['AudioConfig'] = _AUDIOCONFIG
DESCRIPTOR.message_types_by_name['Voice'] = _VOICE
DESCRIPTOR.message_types_by_name['SynthesizeResponse'] = _SYNTHESIZERESPONSE
DESCRIPTOR.message_types_by_name['AudioData'] = _AUDIODATA
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.enum_types_by_name['AudioEncoding'] = _AUDIOENCODING
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListVoicesRequest = _reflection.GeneratedProtocolMessageType('ListVoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListVoicesRequest)
  })
_sym_db.RegisterMessage(ListVoicesRequest)

ListVoicesResponse = _reflection.GeneratedProtocolMessageType('ListVoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListVoicesResponse)
  })
_sym_db.RegisterMessage(ListVoicesResponse)

SynthesizeRequest = _reflection.GeneratedProtocolMessageType('SynthesizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZEREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeRequest)
  })
_sym_db.RegisterMessage(SynthesizeRequest)

SynthesizeConfig = _reflection.GeneratedProtocolMessageType('SynthesizeConfig', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZECONFIG,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeConfig)
  })
_sym_db.RegisterMessage(SynthesizeConfig)

AudioConfig = _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCONFIG,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.AudioConfig)
  })
_sym_db.RegisterMessage(AudioConfig)

Voice = _reflection.GeneratedProtocolMessageType('Voice', (_message.Message,), {
  'DESCRIPTOR' : _VOICE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.Voice)
  })
_sym_db.RegisterMessage(Voice)

SynthesizeResponse = _reflection.GeneratedProtocolMessageType('SynthesizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZERESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeResponse)
  })
_sym_db.RegisterMessage(SynthesizeResponse)

AudioData = _reflection.GeneratedProtocolMessageType('AudioData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIODATA,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.AudioData)
  })
_sym_db.RegisterMessage(AudioData)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.Error)
  })
_sym_db.RegisterMessage(Error)



_TTS = _descriptor.ServiceDescriptor(
  name='TTS',
  full_name='techmo.tribune.TTS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=991,
  serialized_end=1262,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListVoices',
    full_name='techmo.tribune.TTS.ListVoices',
    index=0,
    containing_service=None,
    input_type=_LISTVOICESREQUEST,
    output_type=_LISTVOICESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SynthesizeStreaming',
    full_name='techmo.tribune.TTS.SynthesizeStreaming',
    index=1,
    containing_service=None,
    input_type=_SYNTHESIZEREQUEST,
    output_type=_SYNTHESIZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Synthesize',
    full_name='techmo.tribune.TTS.Synthesize',
    index=2,
    containing_service=None,
    input_type=_SYNTHESIZEREQUEST,
    output_type=_SYNTHESIZERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TTS)

DESCRIPTOR.services_by_name['TTS'] = _TTS

# @@protoc_insertion_point(module_scope)
