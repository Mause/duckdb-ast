from enum import Enum
from typing import Generic, Literal, Optional, TypeVar, Union

from pydantic import BaseModel, Extra, Field

__all__ = [
    "AggregateHandling",
    "BaseExpression",
    "BaseTableRef",
    "BetweenExpression",
    "CaseCheck",
    "CaseExpression",
    "CastExpression",
    "CatalogEntry",
    "CollateExpression",
    "ColumnRefExpression",
    "CommonTableExpressionInfo",
    "CommonTableExpressionMap",
    "ComparisonExpression",
    "ConjunctionExpression",
    "ConstantExpression",
    "DecimalTypeInfo",
    "EmptyTableRef",
    "ErrorResponse",
    "ExtraTypeInfo",
    "FunctionExpression",
    "ListTypeInfo",
    "LogicalType",
    "LogicalTypeId",
    "OperatorExpression",
    "OrderByNode",
    "OrderByNullType",
    "OrderModifier",
    "OrderType",
    "ParsedExpression",
    "ParsedExpressionSubclasses",
    "QueryNode",
    "ResultModifier",
    "ResultModifierType",
    "Root",
    "SampleMethod",
    "SampleOptions",
    "SelectNode",
    "SelectNode",
    "StandardEntry",
    "StarExpression",
    "StructTypeInfo",
    "SubqueryExpression",
    "SubqueryRef",
    "SuccessResponse",
    "TableFunctionRef",
    "TableRef",
    "TableRefSubclasses",
    "TypeCatalogEntry",
    "UserTypeInfo",
    "Value",
]

T = TypeVar("T")


class Base(BaseModel):
    """
    Base model with config
    """

    class Config:
        extra = Extra.forbid


class BaseExpression(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/base_expression.hpp#L18
    """

    type: str
    clazz: str = Field(alias="class")
    alias: str


class ParsedExpression(BaseExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/parsed_expression.hpp#L34
    """


class LogicalTypeId(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/types.hpp#L246
    """

    INVALID = "INVALID"
    NULL = "NULL"
    UNKNOWN = "UNKNOWN"
    ANY = "ANY"
    USER = "USER"
    BOOLEAN = "BOOLEAN"
    TINYINT = "TINYINT"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    DATE = "DATE"
    TIME = "TIME"
    TIMESTAMP_SEC = "TIMESTAMP_SEC"
    TIMESTAMP_MS = "TIMESTAMP_MS"
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMP_NS = "TIMESTAMP_NS"
    DECIMAL = "DECIMAL"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    BLOB = "BLOB"
    INTERVAL = "INTERVAL"
    UTINYINT = "UTINYINT"
    USMALLINT = "USMALLINT"
    UINTEGER = "UINTEGER"
    UBIGINT = "UBIGINT"
    TIMESTAMP_TZ = "TIMESTAMP WITH TIME ZONE"
    TIME_TZ = "TIME_TZ"
    BIT = "BIT"

    HUGEINT = "HUGEINT"
    POINTER = "POINTER"
    VALIDITY = "VALIDITY"
    UUID = "UUID"

    STRUCT = "STRUCT"
    LIST = "LIST"
    MAP = "MAP"
    TABLE = "TABLE"
    ENUM = "ENUM"
    AGGREGATE_STATE = "AGGREGATE_STATE"
    LAMBDA = "LAMBDA"
    UNION = "UNION"


class CatalogEntry(Base):
    """
    Abstract base class of an entry in the catalog

    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/catalog/catalog_entry.hpp#L25
    """


class StandardEntry(CatalogEntry):
    """
    A StandardEntry is a catalog entry that is a member of a schema

    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/catalog/standard_entry.hpp#L17
    """


class TypeCatalogEntry(StandardEntry):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/catalog/catalog_entry/type_catalog_entry.hpp#L20
    """

    user_type: "LogicalType"


class ExtraTypeInfo(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/common/types.cpp#L766
    """

    type: str
    alias: str
    catalog_entry: Optional[TypeCatalogEntry]


class ListTypeInfo(ExtraTypeInfo):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/common/types.cpp#L991
    """

    type: Literal["LIST_TYPE_INFO"]
    child_type: "LogicalType"


class DecimalTypeInfo(ExtraTypeInfo):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/common/types.cpp#L868
    """

    type: Literal["DECIMAL_TYPE_INFO"]
    width: int
    scale: int


class StructTypeInfo(ExtraTypeInfo):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/common/types.cpp#L1040
    """

    type: Literal["STRUCT_TYPE_INFO"]
    child_types: list[Union[str, "LogicalType"]]


class UserTypeInfo(ExtraTypeInfo):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/common/types.cpp#L1263
    """

    type: Literal["USER_TYPE_INFO"]
    user_type_name: str


class LogicalType(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/types.hpp#L298
    """

    id: LogicalTypeId
    type_info: Optional[
        Union[ListTypeInfo, DecimalTypeInfo, UserTypeInfo, StructTypeInfo]
    ] = Field(discriminator="type")


StructTypeInfo.update_forward_refs()


class Value(Base, Generic[T]):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/types/value.hpp#L30
    """

    type: LogicalType
    value: T
    is_null: bool


class ColumnRefExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/columnref_expression.hpp#L28
    """

    type: Literal["COLUMN_REF"]
    clazz: Literal["COLUMN_REF"] = Field(alias="class")

    column_names: list[str]


class StarExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/star_expression.hpp
    """

    type: Literal["STAR"]
    clazz: Literal["STAR"] = Field(alias="class")

    columns: bool

    replace_list: dict[str, "ParsedExpressionSubclasses"]
    relation_name: str
    exclude_list: list[str]
    expr: Optional["ParsedExpressionSubclasses"]


class ConstantExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/constant_expression.hpp#L17
    """

    type: Literal["CONSTANT"]
    clazz: Literal["CONSTANT"] = Field(alias="class")

    value: Value


class CastExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/cast_expression.hpp#L22-L26
    """

    type: Literal["CAST"]
    clazz: Literal["CAST"] = Field(alias="class")
    child: "ParsedExpressionSubclasses"
    cast_type: LogicalType
    try_cast: bool


class ComparisonExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/comparison_expression.hpp#L16
    """

    clazz: Literal["COMPARISON"] = Field(alias="class")
    type: Literal[
        "GREATERTHAN",
        "EQUAL",
        "NOTEQUAL",
        "GREATERTHANOREQUALTO",
        "NOT_DISTINCT_FROM",
        "DISTINCT_FROM",
        "LESSTHANOREQUALTO",
        "LESSTHAN",
    ]
    left: "ParsedExpressionSubclasses"
    right: "ParsedExpressionSubclasses"


class ConjunctionExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/conjunction_expression.hpp#L17
    """

    clazz: Literal["CONJUNCTION"] = Field(alias="class")
    type: Literal["AND", "OR"]
    children: list["ParsedExpressionSubclasses"]


class OperatorExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/operator_expression.hpp#L18
    """

    clazz: Literal["OPERATOR"] = Field(alias="class")
    type: Literal["IS_NULL", "IN", "NOT", "IS_NOT_NULL", "COMPARE_NOT_IN"]
    children: list["ParsedExpressionSubclasses"]


class SubqueryExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/subquery_expression.hpp#L18
    """

    type: Literal["SUBQUERY"]
    clazz: Literal["SUBQUERY"] = Field(alias="class")

    child: Optional["ParsedExpressionSubclasses"]
    comparison_type: Literal["INVALID", "EQUAL"]
    subquery: "SelectNode"
    subquery_type: Literal["SCALAR", "ANY", "EXISTS"]


class CaseCheck(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/case_expression.hpp#L16
    """

    when_expr: "ParsedExpressionSubclasses"
    then_expr: "ParsedExpressionSubclasses"


class CollateExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/collate_expression.hpp#L16
    """

    type: Literal["COLLATE"]
    clazz: Literal["COLLATE"] = Field(alias="class")

    child: "ParsedExpressionSubclasses"
    collation: str


class CaseExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/case_expression.hpp#L25
    """

    type: Literal["CASE"]
    clazz: Literal["CASE"] = Field(alias="class")

    case_checks: list[CaseCheck]
    else_expr: "ParsedExpressionSubclasses"


class BetweenExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/between_expression.hpp#L15
    """

    clazz: Literal["BETWEEN"] = Field(alias="class")
    type: Literal["COMPARE_BETWEEN"]

    input: "ParsedExpressionSubclasses"
    lower: "ParsedExpressionSubclasses"
    upper: "ParsedExpressionSubclasses"


class ParsedExpressionSubclasses(Base):
    """Union of ParsedExpression subclasses"""

    __root__: Union[
        "FunctionExpression",
        ColumnRefExpression,
        StarExpression,
        ConstantExpression,
        CastExpression,
        ComparisonExpression,
        ConjunctionExpression,
        SubqueryExpression,
        OperatorExpression,
        CaseExpression,
        CollateExpression,
        BetweenExpression,
    ] = Field(discriminator="type")


class SampleMethod(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/parsed_data/sample_options.hpp#L18
    """

    SYSTEM_SAMPLE = "System"
    BERNOULLI_SAMPLE = "Bernoulli"
    RESERVOIR_SAMPLE = "Reservoir"


class SampleOptions(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/parsed_data/sample_options.hpp#L22
    """

    sample_size: Value
    is_percentage: bool
    method: SampleMethod
    seed: int = -1


class TableRef(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/tableref.hpp#L20
    """

    alias: str
    sample: Optional[SampleOptions]


class BaseTableRef(TableRef):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/tableref/basetableref.hpp
    """

    type: Literal["BASE_TABLE"]

    schema_name: str
    table_name: str
    catalog_name: str
    column_name_alias: Optional[list[str]]


class EmptyTableRef(TableRef):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/tableref/emptytableref.hpp#L15
    """

    type: Literal["EMPTY"]


class OrderType(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/enums/order_type.hpp#L16
    """

    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OrderByNullType(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/enums/order_type.hpp#L18
    """

    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    NULLS_FIRST = "NULLS_FIRST"
    NULLS_LAST = "NULLS_LAST"


class OrderByNode(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/result_modifier.hpp#L60
    """

    type: OrderType
    null_order: OrderByNullType
    expression: "ParsedExpressionSubclasses"


class OrderModifier(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/result_modifier.hpp#L101
    """

    type: Literal["ORDER_MODIFIER"]
    orders: list[OrderByNode]


class FunctionExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/expression/function_expression.hpp#L17
    """

    clazz: Literal["FUNCTION"] = Field(alias="class")
    type: Literal["FUNCTION"]
    schema_name: str = Field(alias="schema")
    function_name: str
    catalog: str
    is_operator: bool
    children: list[ParsedExpressionSubclasses]
    distinct: bool
    order_bys: OrderModifier
    export_state: bool
    filter: Optional[ParsedExpressionSubclasses]


class TableFunctionRef(TableRef):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/tableref/table_function_ref.hpp#L19
    """

    type: Literal["TABLE_FUNCTION"]

    function: FunctionExpression
    column_name_alias: Optional[list[str]]


class AggregateHandling(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/common/enums/aggregate_handling.hpp#L16
    """

    # standard handling as in the SELECT clause
    STANDARD_HANDLING = "STANDARD_HANDLING"

    # aggregates allowed: any aggregates in this node will result in an error
    NO_AGGREGATES_ALLOWED = "NO_AGGREGATES_ALLOWED"

    # force aggregates: any non-aggregate select list entry will become a GROUP
    FORCE_AGGREGATES = "FORCE_AGGREGATES"


class ResultModifierType(Enum):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/result_modifier.hpp#L22
    """

    LIMIT_MODIFIER = "LIMIT_MODIFIER"
    ORDER_MODIFIER = "ORDER_MODIFIER"
    DISTINCT_MODIFIER = "DISTINCT_MODIFIER"
    LIMIT_PERCENT_MODIFIER = "LIMIT_PERCENT_MODIFIER"


class ResultModifier(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/result_modifier.hpp#L33
    """

    type: ResultModifierType


class CommonTableExpressionInfo(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/common_table_expression_info.hpp#L17
    """

    aliases: list[str]
    query: "SelectNode"


class CommonTableExpressionMap(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/query_node.hpp#L32
    """

    map: dict[str, CommonTableExpressionInfo]


class QueryNode(Base):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/query_node.hpp#L47
    """

    type: str
    modifiers: list[ResultModifier]

    cte_map: CommonTableExpressionMap


class SubqueryRef(TableRef):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/tableref/subqueryref.hpp#L16
    """

    type: Literal["SUBQUERY"]

    subquery: "SelectNode"
    column_name_alias: list[str]


class TableRefSubclasses(Base):
    "Union of TableRef subclasses"
    __root__: Union[BaseTableRef, EmptyTableRef, TableFunctionRef, SubqueryRef] = Field(
        discriminator="type"
    )


GroupingSet = set[int]


class SelectNode(QueryNode):
    """
    https://github.com/duckdb/duckdb/blob/56a94e3a49128b4471dce0d58d2b78cd93a39483/src/include/duckdb/parser/query_node/select_node.hpp#L22
    """

    type: Literal["SELECT_NODE"]
    select_list: list[ParsedExpressionSubclasses]
    where_clause: Optional[ParsedExpressionSubclasses]
    sample: Optional[SampleOptions]
    qualify: Optional[ParsedExpressionSubclasses]
    having: Optional[ParsedExpressionSubclasses]
    group_sets: Optional[list[GroupingSet]]
    group_expressions: Optional[list[ParsedExpressionSubclasses]]
    aggregate_handling: Optional[AggregateHandling]
    from_table: TableRefSubclasses


class ErrorResponse(Base):
    "Error shape for when parsing fails"
    error: Literal[True]
    error_message: str
    error_type: str


class SuccessResponse(Base):
    "Returned when parsing succeeds"
    error: Literal[False]
    statements: list[SelectNode]


class Root(Base):
    "Union of possible responses"
    __root__: Union[ErrorResponse, SuccessResponse] = Field(discriminator="error")


CastExpression.update_forward_refs()
ComparisonExpression.update_forward_refs()
ListTypeInfo.update_forward_refs()
StarExpression.update_forward_refs()
ConjunctionExpression.update_forward_refs()
TypeCatalogEntry.update_forward_refs()
SubqueryExpression.update_forward_refs()
OperatorExpression.update_forward_refs()
CaseExpression.update_forward_refs()
CaseCheck.update_forward_refs()
SubqueryRef.update_forward_refs()
CollateExpression.update_forward_refs()
CommonTableExpressionInfo.update_forward_refs()
BetweenExpression.update_forward_refs()
ParsedExpressionSubclasses.update_forward_refs()
