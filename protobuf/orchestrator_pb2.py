# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orchestrator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='orchestrator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12orchestrator.proto\"0\n\x1dSudokuDesignEvaluationRequest\x12\x0f\n\x07version\x18\x01 \x01(\x03\"*\n\x19SudokuDesignEvaluationJob\x12\r\n\x05\x66ield\x18\x01 \x03(\x05\"\\\n\x1cSudokuDesignEvaluationResult\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08solution\x18\x02 \x03(\x05\x12\x1a\n\x12minimal_unsolvable\x18\x03 \x03(\x05\"*\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"z\n\nParameters\x12\x19\n\x11number_of_answers\x18\x01 \x01(\x05\x12#\n\x1breturn_only_optimal_answers\x18\x02 \x01(\x08\x12,\n\x15\x61\x64\x64itional_parameters\x18\x03 \x03(\x0b\x32\r.KeyValuePair\"=\n\tSolverJob\x12\x0f\n\x07program\x18\x01 \x01(\t\x12\x1f\n\nparameters\x18\x02 \x01(\x0b\x32\x0b.Parameters\"*\n\x0b\x43ostElement\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ost\x18\x02 \x01(\x05\"Q\n\tAnswerset\x12\r\n\x05\x61toms\x18\x01 \x03(\t\x12\x1b\n\x05\x63osts\x18\x02 \x03(\x0b\x32\x0c.CostElement\x12\x18\n\x10is_known_optimal\x18\x03 \x01(\x08\"D\n\x11ResultDescription\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x10\n\x08messages\x18\x03 \x03(\t\"]\n\x15SolveResultAnswersets\x12\'\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32\x12.ResultDescription\x12\x1b\n\x07\x61nswers\x18\x02 \x03(\x0b\x32\n.Answerset\"\x16\n\x05\x45mpty\x12\r\n\x05\x65mpty\x18\x01 \x01(\x03\x32\x80\x01\n\'SudokuDesignEvaluationRequestDataBroker\x12U\n\x17requestSudokuEvaluation\x12\x1e.SudokuDesignEvaluationRequest\x1a\x1a.SudokuDesignEvaluationJob2f\n$SudokuDesignEvaluationProblemEncoder\x12>\n\x14\x65valuateSudokuDesign\x12\x1a.SudokuDesignEvaluationJob\x1a\n.SolverJob2<\n\rOneshotSolver\x12+\n\x05solve\x12\n.SolverJob\x1a\x16.SolveResultAnswersets2w\n#SudokuDesignEvaluationResultDecoder\x12P\n\x17processEvaluationResult\x12\x16.SolveResultAnswersets\x1a\x1d.SudokuDesignEvaluationResult2i\n%SudokuDesignEvaluationResultProcessor\x12@\n\x17processEvaluationResult\x12\x1d.SudokuDesignEvaluationResult\x1a\x06.Emptyb\x06proto3')
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
  serialized_start=22,
  serialized_end=70,
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
  serialized_start=72,
  serialized_end=114,
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
  serialized_start=116,
  serialized_end=208,
)


_KEYVALUEPAIR = _descriptor.Descriptor(
  name='KeyValuePair',
  full_name='KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyValuePair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyValuePair.value', index=1,
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
  serialized_start=210,
  serialized_end=252,
)


_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_answers', full_name='Parameters.number_of_answers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_only_optimal_answers', full_name='Parameters.return_only_optimal_answers', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_parameters', full_name='Parameters.additional_parameters', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=254,
  serialized_end=376,
)


_SOLVERJOB = _descriptor.Descriptor(
  name='SolverJob',
  full_name='SolverJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='program', full_name='SolverJob.program', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='SolverJob.parameters', index=1,
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
  serialized_start=378,
  serialized_end=439,
)


_COSTELEMENT = _descriptor.Descriptor(
  name='CostElement',
  full_name='CostElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='CostElement.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='CostElement.cost', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=441,
  serialized_end=483,
)


_ANSWERSET = _descriptor.Descriptor(
  name='Answerset',
  full_name='Answerset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='atoms', full_name='Answerset.atoms', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='costs', full_name='Answerset.costs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_known_optimal', full_name='Answerset.is_known_optimal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=485,
  serialized_end=566,
)


_RESULTDESCRIPTION = _descriptor.Descriptor(
  name='ResultDescription',
  full_name='ResultDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ResultDescription.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='ResultDescription.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='ResultDescription.messages', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=568,
  serialized_end=636,
)


_SOLVERESULTANSWERSETS = _descriptor.Descriptor(
  name='SolveResultAnswersets',
  full_name='SolveResultAnswersets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='SolveResultAnswersets.description', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answers', full_name='SolveResultAnswersets.answers', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=638,
  serialized_end=731,
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
  serialized_start=733,
  serialized_end=755,
)

_PARAMETERS.fields_by_name['additional_parameters'].message_type = _KEYVALUEPAIR
_SOLVERJOB.fields_by_name['parameters'].message_type = _PARAMETERS
_ANSWERSET.fields_by_name['costs'].message_type = _COSTELEMENT
_SOLVERESULTANSWERSETS.fields_by_name['description'].message_type = _RESULTDESCRIPTION
_SOLVERESULTANSWERSETS.fields_by_name['answers'].message_type = _ANSWERSET
DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationRequest'] = _SUDOKUDESIGNEVALUATIONREQUEST
DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationJob'] = _SUDOKUDESIGNEVALUATIONJOB
DESCRIPTOR.message_types_by_name['SudokuDesignEvaluationResult'] = _SUDOKUDESIGNEVALUATIONRESULT
DESCRIPTOR.message_types_by_name['KeyValuePair'] = _KEYVALUEPAIR
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['SolverJob'] = _SOLVERJOB
DESCRIPTOR.message_types_by_name['CostElement'] = _COSTELEMENT
DESCRIPTOR.message_types_by_name['Answerset'] = _ANSWERSET
DESCRIPTOR.message_types_by_name['ResultDescription'] = _RESULTDESCRIPTION
DESCRIPTOR.message_types_by_name['SolveResultAnswersets'] = _SOLVERESULTANSWERSETS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SudokuDesignEvaluationRequest = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONREQUEST,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationRequest)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationRequest)

SudokuDesignEvaluationJob = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationJob', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONJOB,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationJob)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationJob)

SudokuDesignEvaluationResult = _reflection.GeneratedProtocolMessageType('SudokuDesignEvaluationResult', (_message.Message,), dict(
  DESCRIPTOR = _SUDOKUDESIGNEVALUATIONRESULT,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:SudokuDesignEvaluationResult)
  ))
_sym_db.RegisterMessage(SudokuDesignEvaluationResult)

KeyValuePair = _reflection.GeneratedProtocolMessageType('KeyValuePair', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEPAIR,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:KeyValuePair)
  ))
_sym_db.RegisterMessage(KeyValuePair)

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

SolverJob = _reflection.GeneratedProtocolMessageType('SolverJob', (_message.Message,), dict(
  DESCRIPTOR = _SOLVERJOB,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:SolverJob)
  ))
_sym_db.RegisterMessage(SolverJob)

CostElement = _reflection.GeneratedProtocolMessageType('CostElement', (_message.Message,), dict(
  DESCRIPTOR = _COSTELEMENT,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:CostElement)
  ))
_sym_db.RegisterMessage(CostElement)

Answerset = _reflection.GeneratedProtocolMessageType('Answerset', (_message.Message,), dict(
  DESCRIPTOR = _ANSWERSET,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:Answerset)
  ))
_sym_db.RegisterMessage(Answerset)

ResultDescription = _reflection.GeneratedProtocolMessageType('ResultDescription', (_message.Message,), dict(
  DESCRIPTOR = _RESULTDESCRIPTION,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:ResultDescription)
  ))
_sym_db.RegisterMessage(ResultDescription)

SolveResultAnswersets = _reflection.GeneratedProtocolMessageType('SolveResultAnswersets', (_message.Message,), dict(
  DESCRIPTOR = _SOLVERESULTANSWERSETS,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:SolveResultAnswersets)
  ))
_sym_db.RegisterMessage(SolveResultAnswersets)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'orchestrator_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)



_SUDOKUDESIGNEVALUATIONREQUESTDATABROKER = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationRequestDataBroker',
  full_name='SudokuDesignEvaluationRequestDataBroker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=758,
  serialized_end=886,
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


_SUDOKUDESIGNEVALUATIONPROBLEMENCODER = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationProblemEncoder',
  full_name='SudokuDesignEvaluationProblemEncoder',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=888,
  serialized_end=990,
  methods=[
  _descriptor.MethodDescriptor(
    name='evaluateSudokuDesign',
    full_name='SudokuDesignEvaluationProblemEncoder.evaluateSudokuDesign',
    index=0,
    containing_service=None,
    input_type=_SUDOKUDESIGNEVALUATIONJOB,
    output_type=_SOLVERJOB,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUDOKUDESIGNEVALUATIONPROBLEMENCODER)

DESCRIPTOR.services_by_name['SudokuDesignEvaluationProblemEncoder'] = _SUDOKUDESIGNEVALUATIONPROBLEMENCODER


_ONESHOTSOLVER = _descriptor.ServiceDescriptor(
  name='OneshotSolver',
  full_name='OneshotSolver',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=992,
  serialized_end=1052,
  methods=[
  _descriptor.MethodDescriptor(
    name='solve',
    full_name='OneshotSolver.solve',
    index=0,
    containing_service=None,
    input_type=_SOLVERJOB,
    output_type=_SOLVERESULTANSWERSETS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ONESHOTSOLVER)

DESCRIPTOR.services_by_name['OneshotSolver'] = _ONESHOTSOLVER


_SUDOKUDESIGNEVALUATIONRESULTDECODER = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationResultDecoder',
  full_name='SudokuDesignEvaluationResultDecoder',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=1054,
  serialized_end=1173,
  methods=[
  _descriptor.MethodDescriptor(
    name='processEvaluationResult',
    full_name='SudokuDesignEvaluationResultDecoder.processEvaluationResult',
    index=0,
    containing_service=None,
    input_type=_SOLVERESULTANSWERSETS,
    output_type=_SUDOKUDESIGNEVALUATIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUDOKUDESIGNEVALUATIONRESULTDECODER)

DESCRIPTOR.services_by_name['SudokuDesignEvaluationResultDecoder'] = _SUDOKUDESIGNEVALUATIONRESULTDECODER


_SUDOKUDESIGNEVALUATIONRESULTPROCESSOR = _descriptor.ServiceDescriptor(
  name='SudokuDesignEvaluationResultProcessor',
  full_name='SudokuDesignEvaluationResultProcessor',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  serialized_start=1175,
  serialized_end=1280,
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