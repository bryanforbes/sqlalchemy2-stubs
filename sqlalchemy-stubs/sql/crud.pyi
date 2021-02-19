from typing import Any

from . import coercions as coercions
from . import dml as dml
from . import elements as elements
from . import roles as roles
from .. import exc as exc
from .. import util as util

REQUIRED: Any

class _multiparam_column(elements.ColumnElement):
    index: Any = ...
    key: Any = ...
    original: Any = ...
    default: Any = ...
    type: Any = ...
    def __init__(self, original: Any, index: Any) -> None: ...
    def compare(self, other: Any, **kw: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
