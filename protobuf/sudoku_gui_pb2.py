# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sudoku-gui.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sudoku-gui.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10sudoku-gui.proto\"0\n\x1dSudokuDesignEvaluationRequest\x12\x0f\n\x07version\x18\x01 \x01(\x03\"*\n\x19SudokuDesignEvaluationJob\x12\r\n\x05\x66ield\x18\x01 \x03(\x05\"\\\n\x1cSudokuDesignEvaluationResult\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08solution\x18\x02 \x03(\x05\x12\x1a\n\x12minimal_unsolvable\x18\x03 \x03(\x05\"\x16\n\x05\x45mpty\x12\r\n\x05\x65mpty\x18\x01 \x01(\x03\x32\x80\x01\n\'SudokuDesignEvaluationRequestDataBroker\x12U\n\x17requestSudokuEvaluation\x12\x1e.SudokuDesignEvaluationRequest\x1a\x1a.SudokuDesignEvaluationJob2i\n%SudokuDesignEvaluationResultProcessor\x12@\n\x17processEvaluationResult\x12\x1d.SudokuDesignEvaluationResult\x1a\x06.Emptyb\x06proto3')
)




_SUDOKUDESIGNEVALUATIONREQUEST = _descriptor.Descriptor(
  name='SudokuDesignEvaluationRequest',
  full_name='SudokuDesignEvaluationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='SudokuDesignEvaluationRequest.version', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=20,
  serialized_end=68,
)


_SUDOKUDESIGNEVALUATIONJOB = _descriptor.Descriptor(
  name='SudokuDesignEvaluationJob',
  full_name='SudokuDesignEvaluationJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='SudokuDesignEvaluationJob.field', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=70,
  serialized_end=112,
)


_SUDOKUDESIGNEVALUATIONRESULT = _descriptor.Descriptor(
  name='SudokuDesignEvaluationResult',
  full_name='SudokuDesignEvaluationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SudokuDesignEvaluationResult.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution', full_name='SudokuDesignEvaluationResult.solution', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimal_unsolvable', full_name='SudokuDesignEvaluationResult.minimal_unsolvable', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=114,
  serialized_end=206,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='Empty.empty', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=208,
  serialized_end=230,
)

DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationRequest'] = _SUDOKUDESIGNEVALUATIONREQUEST
DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationJob'] = _SUDOKUDESIGNEVALUATIONJOB
DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationResult'] = _SUDOKUDESIGNEVALUATIONRESULT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SudokuDesignEvaluationRequest = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONREQUEST,
  __module__ = 'sudoku_gui_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationRequest)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationRequest)

SudokuDesignEvaluationJob = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationJob', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONJOB,
  __module__ = 'sudoku_gui_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationJob)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationJob)

SudokuDesignEvaluationResult = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationResult', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONRESULT,
  __module__ = 'sudoku_gui_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationResult)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationResult)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'sudoku_gui_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)



_SUDOKUDESIGNEVALUATIONREQUESTDATABROKER = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationRequestDataBroker',
  full_name='SudokuDesignEvaluationRequestDataBroker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=233,
  serialized_end=361,
  methods=[
  _descriptor.MethodDescriptor(
    name='requestSudokuEvaluation',
    full_name='SudokuDesignEvaluationRequestDataBroker.requestSudokuEvaluation',
    index=0,
    containing_service=None,
    input_type=_SUDOKUDESIGNEVALUATIONREQUEST,
    output_type=_SUDOKUDESIGNEVALUATIONJOB,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUDOKUDESIGNEVALUATIONREQUESTDATABROKER)

DESCRIPTOR.services_by_name['SudokuDesignEvaluationRequestDataBroker'] = _SUDOKUDESIGNEVALUATIONREQUESTDATABROKER


_SUDOKUDESIGNEVALUATIONRESULTPROCESSOR = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationResultProcessor',
  full_name='SudokuDesignEvaluationResultProcessor',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=363,
  serialized_end=468,
  methods=[
  _descriptor.MethodDescriptor(
    name='processEvaluationResult',
    full_name='SudokuDesignEvaluationResultProcessor.processEvaluationResult',
    index=0,
    containing_service=None,
    input_type=_SUDOKUDESIGNEVALUATIONRESULT,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUDOKUDESIGNEVALUATIONRESULTPROCESSOR)

DESCRIPTOR.services_by_name['SudokuDesignEvaluationResultProcessor'] = _SUDOKUDESIGNEVALUATIONRESULTPROCESSOR

# @@protoc_insertion_point(module_scope)