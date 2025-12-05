from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EID_UNSET: _ClassVar[ExtensionID]
    EID_EXPERIMENTAL: _ClassVar[ExtensionID]
EID_UNSET: ExtensionID
EID_EXPERIMENTAL: ExtensionID

class Extension(_message.Message):
    __slots__ = ()
    REGISTERED_EXT_FIELD_NUMBER: _ClassVar[int]
    MASTER_ARBITRATION_FIELD_NUMBER: _ClassVar[int]
    registered_ext: RegisteredExtension
    master_arbitration: MasterArbitration
    def __init__(self, registered_ext: _Optional[_Union[RegisteredExtension, _Mapping]] = ..., master_arbitration: _Optional[_Union[MasterArbitration, _Mapping]] = ...) -> None: ...

class RegisteredExtension(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    id: ExtensionID
    msg: bytes
    def __init__(self, id: _Optional[_Union[ExtensionID, str]] = ..., msg: _Optional[bytes] = ...) -> None: ...

class MasterArbitration(_message.Message):
    __slots__ = ()
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ELECTION_ID_FIELD_NUMBER: _ClassVar[int]
    role: Role
    election_id: Uint128
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., election_id: _Optional[_Union[Uint128, _Mapping]] = ...) -> None: ...

class Uint128(_message.Message):
    __slots__ = ()
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: int
    low: int
    def __init__(self, high: _Optional[int] = ..., low: _Optional[int] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
