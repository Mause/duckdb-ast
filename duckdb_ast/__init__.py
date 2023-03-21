import json
from enum import Enum
from typing import Generic, Literal, Optional, TypeVar, Union

import duckdb
from pydantic import BaseModel, Extra, Field, parse_raw_as, schema_of
from rich import print

__all__ = [
    "AggregrateHandling",
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
    "get_schema",
    "ListTypeInfo",
    "LogicalType",
    "LogicalTypeId",
    "OperatorExpression",
    "OrderByNode",
    "OrderByNullType",
    "OrderModifier",
    "OrderType",
    "parse_sql",
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
    class Config:
        extra = Extra.forbid


class BaseExpression(Base):
    type: str
    clazz: str = Field(alias="class")
    alias: str


class ParsedExpression(BaseExpression):
    pass


class LogicalTypeId(Enum):
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
    pass


class StandardEntry(CatalogEntry):
    pass


class TypeCatalogEntry(StandardEntry):
    user_type: "LogicalType"


class ExtraTypeInfo(Base):
    type: str
    alias: str
    catalog_entry: Optional[TypeCatalogEntry]


class ListTypeInfo(ExtraTypeInfo):
    type: Literal["LIST_TYPE_INFO"]
    child_type: "LogicalType"


class DecimalTypeInfo(ExtraTypeInfo):
    type: Literal["DECIMAL_TYPE_INFO"]
    width: int
    scale: int


class StructTypeInfo(ExtraTypeInfo):
    type: Literal["STRUCT_TYPE_INFO"]
    child_types: list[Union[str, "LogicalType"]]


class UserTypeInfo(ExtraTypeInfo):
    type: Literal["USER_TYPE_INFO"]
    user_type_name: str


class LogicalType(Base):
    id: LogicalTypeId
    type_info: Optional[
        Union[ListTypeInfo, DecimalTypeInfo, UserTypeInfo, StructTypeInfo]
    ] = Field(discriminator="type")


StructTypeInfo.update_forward_refs()


class Value(Base, Generic[T]):
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
    clazz: Literal["CONJUNCTION"] = Field(alias="class")
    type: Literal["AND", "OR"]
    children: list["ParsedExpressionSubclasses"]


class OperatorExpression(ParsedExpression):
    clazz: Literal["OPERATOR"] = Field(alias="class")
    type: Literal["IS_NULL", "IN", "NOT", "IS_NOT_NULL", "COMPARE_NOT_IN"]
    children: list["ParsedExpressionSubclasses"]


class SubqueryExpression(ParsedExpression):
    type: Literal["SUBQUERY"]
    clazz: Literal["SUBQUERY"] = Field(alias="class")

    child: Optional["ParsedExpressionSubclasses"]
    comparison_type: Literal["INVALID", "EQUAL"]
    subquery: "SelectNode"
    subquery_type: Literal["SCALAR", "ANY", "EXISTS"]


class CaseCheck(Base):
    when_expr: "ParsedExpressionSubclasses"
    then_expr: "ParsedExpressionSubclasses"


class CollateExpression(ParsedExpression):
    type: Literal["COLLATE"]
    clazz: Literal["COLLATE"] = Field(alias="class")

    child: "ParsedExpressionSubclasses"
    collation: str


class CaseExpression(ParsedExpression):
    type: Literal["CASE"]
    clazz: Literal["CASE"] = Field(alias="class")

    case_checks: list[CaseCheck]
    else_expr: "ParsedExpressionSubclasses"


class BetweenExpression(ParsedExpression):
    clazz: Literal["BETWEEN"] = Field(alias="class")
    type: Literal["COMPARE_BETWEEN"]

    input: "ParsedExpressionSubclasses"
    lower: "ParsedExpressionSubclasses"
    upper: "ParsedExpressionSubclasses"


class ParsedExpressionSubclasses(Base):
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
    SYSTEM_SAMPLE = "System"
    BERNOULLI_SAMPLE = "Bernoulli"
    RESERVOIR_SAMPLE = "Reservoir"


class SampleOptions(Base):
    sample_size: Value
    is_percentage: bool
    method: SampleMethod
    seed: int = -1


class TableRef(Base):
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
    type: Literal["EMPTY"]


class OrderType(Enum):
    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OrderByNullType(Enum):
    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    NULLS_FIRST = "NULLS_FIRST"
    NULLS_LAST = "NULLS_LAST"


class OrderByNode(Base):
    type: OrderType
    null_order: OrderByNullType
    expression: "ParsedExpressionSubclasses"


class OrderModifier(Base):
    type: Literal["ORDER_MODIFIER"]
    orders: list[OrderByNode]


class FunctionExpression(ParsedExpression):
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
    type: Literal["TABLE_FUNCTION"]

    function: FunctionExpression
    column_name_alias: Optional[list[str]]


class AggregrateHandling(Enum):
    STANDARD_HANDLING = "STANDARD_HANDLING"


class ResultModifierType(Enum):
    LIMIT_MODIFIER = "LIMIT_MODIFIER"
    ORDER_MODIFIER = "ORDER_MODIFIER"
    DISTINCT_MODIFIER = "DISTINCT_MODIFIER"
    LIMIT_PERCENT_MODIFIER = "LIMIT_PERCENT_MODIFIER"


class ResultModifier(Base):
    type: ResultModifierType


class CommonTableExpressionInfo(Base):
    aliases: list[str]
    query: "SelectNode"


class CommonTableExpressionMap(Base):
    map: dict[str, CommonTableExpressionInfo]


class QueryNode(Base):
    type: str
    modifiers: list[ResultModifier]

    cte_map: CommonTableExpressionMap


class SubqueryRef(TableRef):
    type: Literal["SUBQUERY"]

    subquery: "SelectNode"
    column_name_alias: list[str]


class TableRefSubclasses(Base):
    __root__: Union[BaseTableRef, EmptyTableRef, TableFunctionRef, SubqueryRef] = Field(
        discriminator="type"
    )


GroupingSet = set[int]


class SelectNode(QueryNode):
    type: Literal["SELECT_NODE"]
    select_list: list[ParsedExpressionSubclasses]
    where_clause: Optional[ParsedExpressionSubclasses]
    sample: Optional[SampleOptions]
    qualify: Optional[ParsedExpressionSubclasses]
    having: Optional[ParsedExpressionSubclasses]
    group_sets: Optional[list[GroupingSet]]
    group_expressions: Optional[list[ParsedExpressionSubclasses]]
    aggregate_handling: Optional[AggregrateHandling]
    from_table: TableRefSubclasses


class ErrorResponse(Base):
    error: Literal[True]
    error_message: str
    error_type: str


class SuccessResponse(Base):
    error: Literal[False]
    statements: list[SelectNode]


def escape_sql(sql):
    return sql.replace('"', '""').replace("'", "''")


def parse_sql(sql: str) -> ErrorResponse | SuccessResponse:
    duckdb.install_extension("json")
    duckdb.load_extension("json")

    inner = f"select json_serialize_sql('{escape_sql(sql)}')"
    (ast,) = duckdb.execute(inner).fetchone()
    print(json.loads(ast))
    print()
    return parse_raw_as(Root, ast).__root__


class Root(Base):
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


def get_schema():
    return schema_of(Root)
