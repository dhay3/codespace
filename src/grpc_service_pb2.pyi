from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetJsonReply(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class SubscribeReply(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ConfigReply(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ReportEvent(_message.Message):
    __slots__ = ()
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    JSON_TEXT_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    stream_name: str
    event_name: str
    json_text: str
    def __init__(self, token_id: _Optional[str] = ..., stream_name: _Optional[str] = ..., event_name: _Optional[str] = ..., json_text: _Optional[str] = ...) -> None: ...

class GetReportRequest(_message.Message):
    __slots__ = ()
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ()
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    password: str
    def __init__(self, user_name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginReply(_message.Message):
    __slots__ = ()
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ()
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class LogoutReply(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ()
    STREAM_NAME_FIELD_NUMBER: _ClassVar[int]
    stream_name: str
    def __init__(self, stream_name: _Optional[str] = ...) -> None: ...

class CliConfigArgs(_message.Message):
    __slots__ = ()
    REQID_FIELD_NUMBER: _ClassVar[int]
    CLI_FIELD_NUMBER: _ClassVar[int]
    ReqId: int
    cli: str
    def __init__(self, ReqId: _Optional[int] = ..., cli: _Optional[str] = ...) -> None: ...

class CliConfigReply(_message.Message):
    __slots__ = ()
    RESREQID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ResReqId: int
    output: str
    errors: str
    def __init__(self, ResReqId: _Optional[int] = ..., output: _Optional[str] = ..., errors: _Optional[str] = ...) -> None: ...

class DisplayCmdArgs(_message.Message):
    __slots__ = ()
    REQID_FIELD_NUMBER: _ClassVar[int]
    CLI_FIELD_NUMBER: _ClassVar[int]
    ReqId: int
    cli: str
    def __init__(self, ReqId: _Optional[int] = ..., cli: _Optional[str] = ...) -> None: ...

class DisplayCmdReply(_message.Message):
    __slots__ = ()
    RESREQID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ResReqId: int
    output: str
    errors: str
    def __init__(self, ResReqId: _Optional[int] = ..., output: _Optional[str] = ..., errors: _Optional[str] = ...) -> None: ...
