import json
from enum import Enum
from typing import Annotated, Generic, Literal, Optional, TypeVar, Union

import duckdb
from pydantic import BaseModel, Extra, Field, parse_raw_as, schema_of
from rich import print

__all__ = ["parse_sql", "get_schema"]

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
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    VARCHAR = "VARCHAR"
    LIST = "LIST"
    STRUCT = "STRUCT"
    DECIMAL = "DECIMAL"
    USER = "USER"
    DOUBLE = "DOUBLE"


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
        Annotated[
            Union[ListTypeInfo, DecimalTypeInfo, UserTypeInfo, StructTypeInfo],
            Field(discriminator="type"),
        ]
    ]


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

    replace_list: dict[str, "Select"]
    relation_name: str
    exclude_list: list[str]
    expr: Optional["Select"]


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
    child: "Select"
    cast_type: LogicalType
    try_cast: bool


class ComparisonExpression(ParsedExpression):
    clazz: Literal["COMPARISON"] = Field(alias="class")
    type: Literal["GREATERTHAN", "EQUAL"]
    left: "Select"
    right: "Select"


class ConjunctionExpression(ParsedExpression):
    clazz: Literal["CONJUNCTION"] = Field(alias="class")
    type: Literal["AND", "OR"]
    children: list["Select"]


Select = Annotated[
    Union[
        "FunctionExpression",
        ColumnRefExpression,
        StarExpression,
        ConstantExpression,
        CastExpression,
        ComparisonExpression,
        ConjunctionExpression,
    ],
    Field(discriminator="type"),
]


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


class OrderModifier(Base):
    type: Literal["ORDER_MODIFIER"]
    orders: list[object]


class FunctionExpression(ParsedExpression):
    clazz: Literal["FUNCTION"] = Field(alias="class")
    type: Literal["FUNCTION"]
    schema_name: str = Field(alias="schema")
    function_name: str
    catalog: str
    is_operator: bool
    children: list[Select]
    distinct: bool
    order_bys: OrderModifier
    export_state: bool
    filter: Optional[Select]


class TableFunctionRef(TableRef):
    type: Literal["TABLE_FUNCTION"]

    function: FunctionExpression
    column_name_alias: Optional[list[str]]


class AggregrateHandling(Enum):
    STANDARD_HANDLING = "STANDARD_HANDLING"


class QueryNode(Base):
    type: str
    modifiers: list[object]

    cte_map: dict


TableRefSubclasses = Annotated[
    Union[BaseTableRef, EmptyTableRef, TableFunctionRef], Field(discriminator="type")
]


GroupingSet = set[int]


class SelectNode(QueryNode):
    type: Literal["SELECT_NODE"]
    select_list: list[Select]
    where_clause: Optional[Select]
    sample: Optional[SampleOptions]
    qualify: Optional[Select]
    having: Optional[Select]
    group_sets: Optional[list[GroupingSet]]
    group_expressions: Optional[list[Select]]
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
    return sql.replace('"', '""')


def parse_sql(sql: str) -> "Root":
    duckdb.install_extension("json")
    duckdb.load_extension("json")

    inner = f"select json_serialize_sql('{escape_sql(sql)}')"
    (ast,) = duckdb.execute(inner).fetchone()
    print(json.loads(ast))
    print()
    return parse_raw_as(Root, ast)


Root = Annotated[Union[ErrorResponse, SuccessResponse], Field(discriminator="error")]


CastExpression.update_forward_refs()
ComparisonExpression.update_forward_refs()
ListTypeInfo.update_forward_refs()
StarExpression.update_forward_refs()
ConjunctionExpression.update_forward_refs()
TypeCatalogEntry.update_forward_refs()


def get_schema():
    return schema_of(Root)
