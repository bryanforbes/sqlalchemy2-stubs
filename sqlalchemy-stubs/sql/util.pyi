from typing import Any
from typing import Optional

from . import coercions as coercions
from . import operators as operators
from . import roles as roles
from . import visitors as visitors
from .base import ColumnSet as ColumnSet
from .ddl import sort_tables as sort_tables
from .elements import BindParameter as BindParameter
from .elements import ColumnClause as ColumnClause
from .elements import ColumnElement as ColumnElement
from .elements import Grouping as Grouping
from .elements import Label as Label
from .elements import Null as Null
from .elements import UnaryExpression as UnaryExpression
from .schema import Column as Column
from .selectable import Alias as Alias
from .selectable import FromClause as FromClause
from .selectable import FromGrouping as FromGrouping
from .selectable import Join as Join
from .selectable import ScalarSelect as ScalarSelect
from .selectable import SelectBase as SelectBase
from .selectable import TableClause as TableClause
from .traversals import HasCacheKey as HasCacheKey
from .. import exc as exc
from .. import util as util

join_condition: Any

def find_join_source(clauses: Any, join_to: Any): ...
def find_left_clause_that_matches_given(clauses: Any, join_from: Any): ...
def find_left_clause_to_join_from(
    clauses: Any, join_to: Any, onclause: Any
): ...
def visit_binary_product(fn: Any, expr: Any) -> None: ...
def find_tables(
    clause: Any,
    check_columns: bool = ...,
    include_aliases: bool = ...,
    include_joins: bool = ...,
    include_selects: bool = ...,
    include_crud: bool = ...,
): ...
def unwrap_order_by(clause: Any): ...
def unwrap_label_reference(element: Any): ...
def expand_column_list_from_order_by(collist: Any, order_by: Any): ...
def clause_is_present(clause: Any, search: Any): ...
def tables_from_leftmost(clause: Any) -> None: ...
def surface_selectables(clause: Any) -> None: ...
def surface_selectables_only(clause: Any) -> None: ...
def extract_first_column_annotation(column: Any, annotation_name: Any): ...
def selectables_overlap(left: Any, right: Any): ...
def bind_values(clause: Any): ...

class _repr_base:
    def trunc(self, value: Any): ...

class _repr_row(_repr_base):
    row: Any = ...
    max_chars: Any = ...
    def __init__(self, row: Any, max_chars: int = ...) -> None: ...

class _repr_params(_repr_base):
    params: Any = ...
    ismulti: Any = ...
    batches: Any = ...
    max_chars: Any = ...
    def __init__(
        self,
        params: Any,
        batches: Any,
        max_chars: int = ...,
        ismulti: Optional[Any] = ...,
    ) -> None: ...

def adapt_criterion_to_null(crit: Any, nulls: Any): ...
def splice_joins(left: Any, right: Any, stop_on: Optional[Any] = ...): ...
def reduce_columns(columns: Any, *clauses: Any, **kw: Any): ...
def criterion_as_pairs(
    expression: Any,
    consider_as_foreign_keys: Optional[Any] = ...,
    consider_as_referenced_keys: Optional[Any] = ...,
    any_operator: bool = ...,
): ...

class ClauseAdapter(visitors.ReplacingExternalTraversal):
    __traverse_options__: Any = ...
    selectable: Any = ...
    include_fn: Any = ...
    exclude_fn: Any = ...
    equivalents: Any = ...
    adapt_on_names: Any = ...
    def __init__(
        self,
        selectable: Any,
        equivalents: Optional[Any] = ...,
        include_fn: Optional[Any] = ...,
        exclude_fn: Optional[Any] = ...,
        adapt_on_names: bool = ...,
        anonymize_labels: bool = ...,
    ) -> None: ...
    def replace(self, col: Any): ...

class ColumnAdapter(ClauseAdapter):
    columns: Any = ...
    adapt_required: Any = ...
    allow_label_resolve: Any = ...
    def __init__(
        self,
        selectable: Any,
        equivalents: Optional[Any] = ...,
        adapt_required: bool = ...,
        include_fn: Optional[Any] = ...,
        exclude_fn: Optional[Any] = ...,
        adapt_on_names: bool = ...,
        allow_label_resolve: bool = ...,
        anonymize_labels: bool = ...,
    ) -> None: ...
    class _IncludeExcludeMapping:
        parent: Any = ...
        columns: Any = ...
        def __init__(self, parent: Any, columns: Any) -> None: ...
        def __getitem__(self, key: Any): ...
    def wrap(self, adapter: Any): ...
    def traverse(self, obj: Any): ...
    adapt_clause: Any = ...
    adapt_list: Any = ...
    def adapt_check_present(self, col: Any): ...
