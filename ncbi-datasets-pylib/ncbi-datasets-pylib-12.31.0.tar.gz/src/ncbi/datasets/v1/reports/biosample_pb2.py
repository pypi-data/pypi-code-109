# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ncbi/datasets/v1/reports/biosample.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ncbi.datasets.v1.reports import common_pb2 as ncbi_dot_datasets_dot_v1_dot_reports_dot_common__pb2
from ncbi.datasets.options import report_pb2 as ncbi_dot_datasets_dot_options_dot_report__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ncbi/datasets/v1/reports/biosample.proto',
  package='ncbi.datasets.v1.reports',
  syntax='proto3',
  serialized_options=b'Z\030ncbi/datasets/v1/reports\370\001\001\302\363\030\341\001\n\020BioSample Report\022\023BioSampleDescriptor\032V<p>NCBI BioSample reports in<a href=\"https://jsonlines.readthedocs.io/\">JSON Lines</a>\032.format. This report is a work-in-progress.</p>\"\013Orientation\"\013SeqRangeSet\"\005Range\"\017LineageOrganism',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(ncbi/datasets/v1/reports/biosample.proto\x12\x18ncbi.datasets.v1.reports\x1a%ncbi/datasets/v1/reports/common.proto\x1a\"ncbi/datasets/options/report.proto\"\x99\x08\n\x13\x42ioSampleDescriptor\x12\x46\n\taccession\x18\x01 \x01(\tB(\xc2\xf3\x18$\n\taccession\x12\tAccession2\x0cSAMN20055006R\taccession\x12\x43\n\x0clast_updated\x18\x02 \x01(\tB \xc2\xf3\x18\x1c\n\x0clast-updated\x12\x0cLast updatedR\x0blastUpdated\x12S\n\x10publication_date\x18\x03 \x01(\tB(\xc2\xf3\x18$\n\x10publication-date\x12\x10Publication dateR\x0fpublicationDate\x12O\n\x0fsubmission_date\x18\x04 \x01(\tB&\xc2\xf3\x18\"\n\x0fsubmission-date\x12\x0fSubmission dateR\x0esubmissionDate\x12\x65\n\nsample_ids\x18\x05 \x03(\x0b\x32%.ncbi.datasets.v1.reports.BioSampleIdB\x1f\xc2\xf3\x18\x1b\n\x04ids-\x12\x13Sample Identifiers R\tsampleIds\x12r\n\x0b\x64\x65scription\x18\x06 \x01(\x0b\x32..ncbi.datasets.v1.reports.BioSampleDescriptionB \xc2\xf3\x18\x1c\n\x0c\x64\x65scription-\x12\x0c\x44\x65scription R\x0b\x64\x65scription\x12T\n\x05owner\x18\x07 \x01(\x0b\x32(.ncbi.datasets.v1.reports.BioSampleOwnerB\x14\xc2\xf3\x18\x10\n\x06owner-\x12\x06Owner R\x05owner\x12,\n\x06models\x18\x08 \x03(\tB\x14\xc2\xf3\x18\x10\n\x06models\x12\x06ModelsR\x06models\x12\x66\n\x0b\x62ioprojects\x18\t \x03(\x0b\x32$.ncbi.datasets.v1.reports.BioProjectB\x1e\xc2\xf3\x18\x1a\n\x0b\x62ioproject-\x12\x0b\x42ioProject R\x0b\x62ioprojects\x12\x41\n\x07package\x18\n \x01(\tB\'\xc2\xf3\x18#\n\x07package\x12\x07Package2\x0fMIGS.ba.air.4.0R\x07package\x12j\n\nattributes\x18\x0b \x03(\x0b\x32,.ncbi.datasets.v1.reports.BioSampleAttributeB\x1c\xc2\xf3\x18\x18\n\nattribute-\x12\nAttribute R\nattributes\x12Y\n\x06status\x18\x0c \x01(\x0b\x32).ncbi.datasets.v1.reports.BioSampleStatusB\x16\xc2\xf3\x18\x12\n\x07status-\x12\x07Status R\x06status\"\xce\x01\n\x14\x42ioSampleDescription\x12(\n\x05title\x18\x01 \x01(\tB\x12\xc2\xf3\x18\x0e\n\x05title\x12\x05TitleR\x05title\x12Z\n\x08organism\x18\x02 \x01(\x0b\x32\".ncbi.datasets.v1.reports.OrganismB\x1a\xc2\xf3\x18\x16\n\torganism-\x12\tOrganism R\x08organism\x12\x30\n\x07\x63omment\x18\x03 \x01(\tB\x16\xc2\xf3\x18\x12\n\x07\x63omment\x12\x07\x43ommentR\x07\x63omment\"\x98\x01\n\x0e\x42ioSampleOwner\x12$\n\x04name\x18\x01 \x01(\tB\x10\xc2\xf3\x18\x0c\n\x04name\x12\x04NameR\x04name\x12`\n\x08\x63ontacts\x18\x02 \x03(\x0b\x32*.ncbi.datasets.v1.reports.BioSampleContactB\x18\xc2\xf3\x18\x14\n\x08\x63ontact-\x12\x08\x43ontact R\x08\x63ontacts\"4\n\x10\x42ioSampleContact\x12 \n\x03lab\x18\x01 \x01(\tB\x0e\xc2\xf3\x18\n\n\x03lab\x12\x03LabR\x03lab\"d\n\x12\x42ioSampleAttribute\x12$\n\x04name\x18\x01 \x01(\tB\x10\xc2\xf3\x18\x0c\n\x04name\x12\x04NameR\x04name\x12(\n\x05value\x18\x02 \x01(\tB\x12\xc2\xf3\x18\x0e\n\x05value\x12\x05ValueR\x05value\"\xc2\x01\n\x0b\x42ioSampleId\x12=\n\x02\x64\x62\x18\x01 \x01(\tB-\xc2\xf3\x18)\n\x02\x64\x62\x12\x08\x44\x61tabase2\x19Wellcome Sanger InstituteR\x02\x64\x62\x12\x35\n\x05label\x18\x02 \x01(\tB\x1f\xc2\xf3\x18\x1b\n\x05label\x12\x05Label2\x0bSample nameR\x05label\x12=\n\x05value\x18\x03 \x01(\tB\'\xc2\xf3\x18#\n\x05value\x12\x05Value2\x13\x43OG-UK/ALDP-17A6A8CR\x05value\"k\n\x0f\x42ioSampleStatus\x12\x32\n\x06status\x18\x01 \x01(\tB\x1a\xc2\xf3\x18\x16\n\x06status\x12\x06Status2\x04liveR\x06status\x12$\n\x04when\x18\x02 \x01(\tB\x10\xc2\xf3\x18\x0c\n\x04when\x12\x04WhenR\x04whenB\x83\x02Z\x18ncbi/datasets/v1/reports\xf8\x01\x01\xc2\xf3\x18\xe1\x01\n\x10\x42ioSample Report\x12\x13\x42ioSampleDescriptor\x1aV<p>NCBI BioSample reports in<a href=\"https://jsonlines.readthedocs.io/\">JSON Lines</a>\x1a.format. This report is a work-in-progress.</p>\"\x0bOrientation\"\x0bSeqRangeSet\"\x05Range\"\x0fLineageOrganismb\x06proto3'
  ,
  dependencies=[ncbi_dot_datasets_dot_v1_dot_reports_dot_common__pb2.DESCRIPTOR,ncbi_dot_datasets_dot_options_dot_report__pb2.DESCRIPTOR,])




_BIOSAMPLEDESCRIPTOR = _descriptor.Descriptor(
  name='BioSampleDescriptor',
  full_name='ncbi.datasets.v1.reports.BioSampleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accession', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.accession', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030$\n\taccession\022\tAccession2\014SAMN20055006', json_name='accession', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.last_updated', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\034\n\014last-updated\022\014Last updated', json_name='lastUpdated', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publication_date', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.publication_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030$\n\020publication-date\022\020Publication date', json_name='publicationDate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submission_date', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.submission_date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\"\n\017submission-date\022\017Submission date', json_name='submissionDate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_ids', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.sample_ids', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\033\n\004ids-\022\023Sample Identifiers ', json_name='sampleIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.description', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\034\n\014description-\022\014Description ', json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.owner', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\020\n\006owner-\022\006Owner ', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='models', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.models', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\020\n\006models\022\006Models', json_name='models', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bioprojects', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.bioprojects', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\032\n\013bioproject-\022\013BioProject ', json_name='bioprojects', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.package', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030#\n\007package\022\007Package2\017MIGS.ba.air.4.0', json_name='package', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.attributes', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\030\n\nattribute-\022\nAttribute ', json_name='attributes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='ncbi.datasets.v1.reports.BioSampleDescriptor.status', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\022\n\007status-\022\007Status ', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=146,
  serialized_end=1195,
)


_BIOSAMPLEDESCRIPTION = _descriptor.Descriptor(
  name='BioSampleDescription',
  full_name='ncbi.datasets.v1.reports.BioSampleDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='ncbi.datasets.v1.reports.BioSampleDescription.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\016\n\005title\022\005Title', json_name='title', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organism', full_name='ncbi.datasets.v1.reports.BioSampleDescription.organism', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\026\n\torganism-\022\tOrganism ', json_name='organism', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='ncbi.datasets.v1.reports.BioSampleDescription.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\022\n\007comment\022\007Comment', json_name='comment', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1198,
  serialized_end=1404,
)


_BIOSAMPLEOWNER = _descriptor.Descriptor(
  name='BioSampleOwner',
  full_name='ncbi.datasets.v1.reports.BioSampleOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ncbi.datasets.v1.reports.BioSampleOwner.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\014\n\004name\022\004Name', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contacts', full_name='ncbi.datasets.v1.reports.BioSampleOwner.contacts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\024\n\010contact-\022\010Contact ', json_name='contacts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1407,
  serialized_end=1559,
)


_BIOSAMPLECONTACT = _descriptor.Descriptor(
  name='BioSampleContact',
  full_name='ncbi.datasets.v1.reports.BioSampleContact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lab', full_name='ncbi.datasets.v1.reports.BioSampleContact.lab', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\n\n\003lab\022\003Lab', json_name='lab', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1561,
  serialized_end=1613,
)


_BIOSAMPLEATTRIBUTE = _descriptor.Descriptor(
  name='BioSampleAttribute',
  full_name='ncbi.datasets.v1.reports.BioSampleAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ncbi.datasets.v1.reports.BioSampleAttribute.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\014\n\004name\022\004Name', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ncbi.datasets.v1.reports.BioSampleAttribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\016\n\005value\022\005Value', json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1615,
  serialized_end=1715,
)


_BIOSAMPLEID = _descriptor.Descriptor(
  name='BioSampleId',
  full_name='ncbi.datasets.v1.reports.BioSampleId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='db', full_name='ncbi.datasets.v1.reports.BioSampleId.db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030)\n\002db\022\010Database2\031Wellcome Sanger Institute', json_name='db', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='ncbi.datasets.v1.reports.BioSampleId.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\033\n\005label\022\005Label2\013Sample name', json_name='label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ncbi.datasets.v1.reports.BioSampleId.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030#\n\005value\022\005Value2\023COG-UK/ALDP-17A6A8C', json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1718,
  serialized_end=1912,
)


_BIOSAMPLESTATUS = _descriptor.Descriptor(
  name='BioSampleStatus',
  full_name='ncbi.datasets.v1.reports.BioSampleStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ncbi.datasets.v1.reports.BioSampleStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\026\n\006status\022\006Status2\004live', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='when', full_name='ncbi.datasets.v1.reports.BioSampleStatus.when', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\302\363\030\014\n\004when\022\004When', json_name='when', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1914,
  serialized_end=2021,
)

_BIOSAMPLEDESCRIPTOR.fields_by_name['sample_ids'].message_type = _BIOSAMPLEID
_BIOSAMPLEDESCRIPTOR.fields_by_name['description'].message_type = _BIOSAMPLEDESCRIPTION
_BIOSAMPLEDESCRIPTOR.fields_by_name['owner'].message_type = _BIOSAMPLEOWNER
_BIOSAMPLEDESCRIPTOR.fields_by_name['bioprojects'].message_type = ncbi_dot_datasets_dot_v1_dot_reports_dot_common__pb2._BIOPROJECT
_BIOSAMPLEDESCRIPTOR.fields_by_name['attributes'].message_type = _BIOSAMPLEATTRIBUTE
_BIOSAMPLEDESCRIPTOR.fields_by_name['status'].message_type = _BIOSAMPLESTATUS
_BIOSAMPLEDESCRIPTION.fields_by_name['organism'].message_type = ncbi_dot_datasets_dot_v1_dot_reports_dot_common__pb2._ORGANISM
_BIOSAMPLEOWNER.fields_by_name['contacts'].message_type = _BIOSAMPLECONTACT
DESCRIPTOR.message_types_by_name['BioSampleDescriptor'] = _BIOSAMPLEDESCRIPTOR
DESCRIPTOR.message_types_by_name['BioSampleDescription'] = _BIOSAMPLEDESCRIPTION
DESCRIPTOR.message_types_by_name['BioSampleOwner'] = _BIOSAMPLEOWNER
DESCRIPTOR.message_types_by_name['BioSampleContact'] = _BIOSAMPLECONTACT
DESCRIPTOR.message_types_by_name['BioSampleAttribute'] = _BIOSAMPLEATTRIBUTE
DESCRIPTOR.message_types_by_name['BioSampleId'] = _BIOSAMPLEID
DESCRIPTOR.message_types_by_name['BioSampleStatus'] = _BIOSAMPLESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BioSampleDescriptor = _reflection.GeneratedProtocolMessageType('BioSampleDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLEDESCRIPTOR,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleDescriptor)
  })
_sym_db.RegisterMessage(BioSampleDescriptor)

BioSampleDescription = _reflection.GeneratedProtocolMessageType('BioSampleDescription', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLEDESCRIPTION,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleDescription)
  })
_sym_db.RegisterMessage(BioSampleDescription)

BioSampleOwner = _reflection.GeneratedProtocolMessageType('BioSampleOwner', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLEOWNER,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleOwner)
  })
_sym_db.RegisterMessage(BioSampleOwner)

BioSampleContact = _reflection.GeneratedProtocolMessageType('BioSampleContact', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLECONTACT,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleContact)
  })
_sym_db.RegisterMessage(BioSampleContact)

BioSampleAttribute = _reflection.GeneratedProtocolMessageType('BioSampleAttribute', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLEATTRIBUTE,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleAttribute)
  })
_sym_db.RegisterMessage(BioSampleAttribute)

BioSampleId = _reflection.GeneratedProtocolMessageType('BioSampleId', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLEID,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleId)
  })
_sym_db.RegisterMessage(BioSampleId)

BioSampleStatus = _reflection.GeneratedProtocolMessageType('BioSampleStatus', (_message.Message,), {
  'DESCRIPTOR' : _BIOSAMPLESTATUS,
  '__module__' : 'ncbi.datasets.v1.reports.biosample_pb2'
  # @@protoc_insertion_point(class_scope:ncbi.datasets.v1.reports.BioSampleStatus)
  })
_sym_db.RegisterMessage(BioSampleStatus)


DESCRIPTOR._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['accession']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['last_updated']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['publication_date']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['submission_date']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['sample_ids']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['description']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['owner']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['models']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['bioprojects']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['package']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['attributes']._options = None
_BIOSAMPLEDESCRIPTOR.fields_by_name['status']._options = None
_BIOSAMPLEDESCRIPTION.fields_by_name['title']._options = None
_BIOSAMPLEDESCRIPTION.fields_by_name['organism']._options = None
_BIOSAMPLEDESCRIPTION.fields_by_name['comment']._options = None
_BIOSAMPLEOWNER.fields_by_name['name']._options = None
_BIOSAMPLEOWNER.fields_by_name['contacts']._options = None
_BIOSAMPLECONTACT.fields_by_name['lab']._options = None
_BIOSAMPLEATTRIBUTE.fields_by_name['name']._options = None
_BIOSAMPLEATTRIBUTE.fields_by_name['value']._options = None
_BIOSAMPLEID.fields_by_name['db']._options = None
_BIOSAMPLEID.fields_by_name['label']._options = None
_BIOSAMPLEID.fields_by_name['value']._options = None
_BIOSAMPLESTATUS.fields_by_name['status']._options = None
_BIOSAMPLESTATUS.fields_by_name['when']._options = None
# @@protoc_insertion_point(module_scope)
