from typing import Any
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import TypeVar

from .base import Connection
from .interfaces import _DBAPICursor
from .interfaces import Dialect
from .interfaces import ExecutionContext
from .result import MergedResult
from .result import Result
from .result import ResultMetaData
from .result import Row
from .row import LegacyRow

_TCursorResult = TypeVar("_TCursorResult", bound=CursorResult)

MD_INDEX: int
MD_RESULT_MAP_INDEX: int
MD_OBJECTS: int
MD_LOOKUP_KEY: int
MD_RENDERED_NAME: int
MD_PROCESSOR: int
MD_UNTRANSLATED: int

class CursorResultMetaData(ResultMetaData):
    returns_rows: bool = ...
    case_sensitive: bool = ...
    def __init__(
        self, parent: BaseCursorResult, cursor_description: Any
    ) -> None: ...

class LegacyCursorResultMetaData(CursorResultMetaData): ...

class ResultFetchStrategy:
    alternate_cursor_description: Any = ...
    def soft_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def hard_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def yield_per(
        self, result: Any, dbapi_cursor: _DBAPICursor, num: int
    ) -> None: ...
    def fetchone(
        self, result: Any, dbapi_cursor: _DBAPICursor, hard_close: bool = ...
    ) -> Any: ...
    def fetchmany(
        self,
        result: Any,
        dbapi_cursor: _DBAPICursor,
        size: Optional[Any] = ...,
    ) -> Sequence[Any]: ...
    def fetchall(self, result: Any) -> Sequence[Any]: ...
    def handle_exception(
        self, result: Any, dbapi_cursor: _DBAPICursor, err: Any
    ) -> None: ...

class NoCursorFetchStrategy(ResultFetchStrategy):
    def soft_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def hard_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def fetchone(
        self, result: Any, dbapi_cursor: _DBAPICursor, hard_close: bool = ...
    ) -> Any: ...
    def fetchmany(
        self,
        result: Any,
        dbapi_cursor: _DBAPICursor,
        size: Optional[Any] = ...,
    ) -> Sequence[Any]: ...
    def fetchall(self, result: Any, dbapi_cursor: _DBAPICursor) -> Sequence[Any]: ...  # type: ignore[override]

class NoCursorDQLFetchStrategy(NoCursorFetchStrategy): ...
class NoCursorDMLFetchStrategy(NoCursorFetchStrategy): ...

class CursorFetchStrategy(ResultFetchStrategy):
    def soft_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def hard_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def handle_exception(
        self, result: Any, dbapi_cursor: _DBAPICursor, err: Any
    ) -> None: ...
    def yield_per(
        self, result: Any, dbapi_cursor: _DBAPICursor, num: int
    ) -> None: ...
    def fetchone(
        self, result: Any, dbapi_cursor: _DBAPICursor, hard_close: bool = ...
    ) -> Any: ...
    def fetchmany(
        self,
        result: Any,
        dbapi_cursor: _DBAPICursor,
        size: Optional[Any] = ...,
    ) -> Sequence[Any]: ...
    def fetchall(self, result: Any, dbapi_cursor: _DBAPICursor) -> Sequence[Any]: ...  # type: ignore[override]

class BufferedRowCursorFetchStrategy(CursorFetchStrategy):
    def __init__(
        self,
        dbapi_cursor: _DBAPICursor,
        execution_options: Any,
        growth_factor: int = ...,
        initial_buffer: Optional[Any] = ...,
    ) -> None: ...
    @classmethod
    def create(cls, result: Any) -> BufferedRowCursorFetchStrategy: ...
    def yield_per(
        self, result: Any, dbapi_cursor: _DBAPICursor, num: int
    ) -> None: ...
    def soft_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def hard_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def fetchone(
        self, result: Any, dbapi_cursor: _DBAPICursor, hard_close: bool = ...
    ) -> Any: ...
    def fetchmany(
        self,
        result: Any,
        dbapi_cursor: _DBAPICursor,
        size: Optional[Any] = ...,
    ) -> Sequence[Any]: ...
    def fetchall(self, result: Any, dbapi_cursor: _DBAPICursor) -> Sequence[Any]: ...  # type: ignore[override]

class FullyBufferedCursorFetchStrategy(CursorFetchStrategy):
    alternate_cursor_description: Any = ...
    def __init__(
        self,
        dbapi_cursor: _DBAPICursor,
        alternate_description: Optional[Any] = ...,
        initial_buffer: Optional[Any] = ...,
    ) -> None: ...
    def yield_per(
        self, result: Any, dbapi_cursor: _DBAPICursor, num: int
    ) -> None: ...
    def soft_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def hard_close(self, result: Any, dbapi_cursor: _DBAPICursor) -> None: ...
    def fetchone(
        self, result: Any, dbapi_cursor: _DBAPICursor, hard_close: bool = ...
    ) -> Any: ...
    def fetchmany(
        self,
        result: Any,
        dbapi_cursor: _DBAPICursor,
        size: Optional[Any] = ...,
    ) -> Sequence[Any]: ...
    def fetchall(self, result: Any, dbapi_cursor: _DBAPICursor) -> Sequence[Any]: ...  # type: ignore[override]

class _NoResultMetaData(ResultMetaData):
    returns_rows: bool = ...
    @property
    def keys(self) -> NoReturn: ...

class BaseCursorResult:
    out_parameters: Any = ...
    closed: bool = ...
    context: ExecutionContext = ...
    dialect: Dialect = ...
    cursor: Any = ...
    cursor_strategy: CursorFetchStrategy = ...
    connection: Connection = ...
    def __init__(
        self,
        context: ExecutionContext,
        cursor_strategy: CursorFetchStrategy,
        cursor_description: Any,
    ): ...
    @property
    def inserted_primary_key_rows(self) -> Any: ...
    @property
    def inserted_primary_key(self) -> Row: ...
    def last_updated_params(self) -> Any: ...
    def last_inserted_params(self) -> Any: ...
    @property
    def returned_defaults_rows(self) -> List[Row]: ...
    @property
    def returned_defaults(self) -> Optional[Row]: ...
    def lastrow_has_defaults(self) -> bool: ...
    def postfetch_cols(self) -> bool: ...
    def prefetch_cols(self) -> bool: ...
    def supports_sane_rowcount(self) -> bool: ...
    def supports_sane_multi_rowcount(self) -> bool: ...
    def rowcount(self) -> int: ...
    @property
    def lastrowid(self) -> Any: ...
    @property
    def returns_rows(self) -> bool: ...
    @property
    def is_insert(self) -> bool: ...

class CursorResult(BaseCursorResult, Result):
    def merge(self, *others: Any) -> MergedResult: ...
    def close(self) -> None: ...
    def yield_per(self: _TCursorResult, num: Any) -> _TCursorResult: ...

class LegacyCursorResult(CursorResult):
    def close(self) -> None: ...

ResultProxy = LegacyCursorResult

class BufferedRowResultProxy(ResultProxy): ...
class FullyBufferedResultProxy(ResultProxy): ...
class BufferedColumnRow(LegacyRow): ...
class BufferedColumnResultProxy(ResultProxy): ...
