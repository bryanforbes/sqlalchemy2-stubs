from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import TypeVar

from ..util import langhelpers

_ET = TypeVar("_ET", bound=ExternalTraversal)
_T = TypeVar("_T")

class TraversibleType(type):
    def __init__(cls, clsname: Any, bases: Any, clsdict: Any) -> None: ...

class Traversible(metaclass=TraversibleType): ...

class _InternalTraversalType(type):
    def __init__(cls, clsname: Any, bases: Any, clsdict: Any) -> None: ...

class InternalTraversal(object, metaclass=_InternalTraversalType):
    def dispatch(self, visit_symbol: Any) -> Optional[Callable[..., Any]]: ...
    def run_generated_dispatch(
        self,
        target: Any,
        internal_dispatch: Any,
        generate_dispatcher_name: Any,
    ) -> Any: ...
    def generate_dispatch(
        self,
        target_cls: Any,
        internal_dispatch: Any,
        generate_dispatcher_name: Any,
    ) -> Any: ...
    dp_has_cache_key: langhelpers._symbol = ...
    dp_has_cache_key_list: langhelpers._symbol = ...
    dp_clauseelement: langhelpers._symbol = ...
    dp_fromclause_canonical_column_collection: langhelpers._symbol = ...
    dp_clauseelement_tuples: langhelpers._symbol = ...
    dp_clauseelement_list: langhelpers._symbol = ...
    dp_clauseelement_tuple: langhelpers._symbol = ...
    dp_executable_options: langhelpers._symbol = ...
    dp_fromclause_ordered_set: langhelpers._symbol = ...
    dp_string: langhelpers._symbol = ...
    dp_string_list: langhelpers._symbol = ...
    dp_anon_name: langhelpers._symbol = ...
    dp_boolean: langhelpers._symbol = ...
    dp_operator: langhelpers._symbol = ...
    dp_type: langhelpers._symbol = ...
    dp_plain_dict: langhelpers._symbol = ...
    dp_dialect_options: langhelpers._symbol = ...
    dp_string_clauseelement_dict: langhelpers._symbol = ...
    dp_string_multi_dict: langhelpers._symbol = ...
    dp_annotations_key: langhelpers._symbol = ...
    dp_plain_obj: langhelpers._symbol = ...
    dp_named_ddl_element: langhelpers._symbol = ...
    dp_prefix_sequence: langhelpers._symbol = ...
    dp_table_hint_list: langhelpers._symbol = ...
    dp_setup_join_tuple: langhelpers._symbol = ...
    dp_statement_hint_list: langhelpers._symbol = ...
    dp_unknown_structure: langhelpers._symbol = ...
    dp_dml_ordered_values: langhelpers._symbol = ...
    dp_dml_values: langhelpers._symbol = ...
    dp_dml_multi_values: langhelpers._symbol = ...
    dp_propagate_attrs: langhelpers._symbol = ...

class ExtendedInternalTraversal(InternalTraversal):
    dp_ignore: langhelpers._symbol = ...
    dp_inspectable: langhelpers._symbol = ...
    dp_multi: langhelpers._symbol = ...
    dp_multi_list: langhelpers._symbol = ...
    dp_has_cache_key_tuples: langhelpers._symbol = ...
    dp_inspectable_list: langhelpers._symbol = ...

class ExternalTraversal:
    __traverse_options__: Any = ...
    def traverse_single(self, obj: Any, **kw: Any) -> Any: ...
    def iterate(self, obj: Any) -> Iterator[Any]: ...
    def traverse(self, obj: _T) -> _T: ...
    @property
    def visitor_iterator(self) -> Iterator[Any]: ...
    def chain(self: _ET, visitor: Any) -> _ET: ...

class CloningExternalTraversal(ExternalTraversal):
    def copy_and_process(self, list_: Iterable[_T]) -> List[_T]: ...
    def traverse(self, obj: _T) -> _T: ...

class ReplacingExternalTraversal(CloningExternalTraversal):
    def replace(self, elem: Any) -> Optional[Any]: ...
    def traverse(self, obj: _T) -> _T: ...

Visitable = Traversible
VisitableType = TraversibleType
ClauseVisitor = ExternalTraversal
CloningVisitor = CloningExternalTraversal
ReplacingCloningVisitor = ReplacingExternalTraversal

def iterate(obj: Any, opts: Dict[str, Any] = ...) -> Iterator[Any]: ...
def traverse_using(
    iterator: Iterator[Any], obj: _T, visitors: Dict[str, Callable[..., Any]]
) -> _T: ...
def traverse(
    obj: _T, opts: Dict[str, Any], visitors: Dict[str, Callable[..., Any]]
) -> _T: ...
def cloned_traverse(
    obj: _T, opts: Dict[str, Any], visitors: Dict[str, Callable[..., Any]]
) -> _T: ...
def replacement_traverse(
    obj: _T, opts: Dict[str, Any], replace: Callable[[Any], Any]
) -> _T: ...
