from typing import Any
from typing import Optional

from . import Connector as Connector
from ..util import warn_deprecated as warn_deprecated

class MxODBCConnector(Connector):
    driver: str = ...
    supports_sane_multi_rowcount: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    supports_native_decimal: bool = ...
    @classmethod
    def dbapi(cls): ...
    def on_connect(self): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def do_executemany(
        self,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Optional[Any] = ...,
    ) -> None: ...
    def do_execute(
        self,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Optional[Any] = ...,
    ) -> None: ...
