import json
from enum import Enum
from typing import Annotated, Generic, Literal, Optional, TypeVar, Union

import duckdb
from pydantic import BaseModel, Extra, Field, parse_raw_as
from rich import print

__all__ = ["parse_sql"]

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


class StatementType(Enum):
    SELECT_NODE = "SELECT_NODE"


class LogicalTypeId(Enum):
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    VARCHAR = "VARCHAR"


class ValueType(Base):
    id: LogicalTypeId
    type_info: Optional[object]


class Value(Base, Generic[T]):
    type: ValueType
    value: T
    is_null: bool


class ColumnRefExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/columnref_expression.hpp#L28
    """

    type: Literal["COLUMN_REF"]
    clazz: Literal["COLUMN_REF"] = Field(alias="class")

    column_names: list[str]


class Star(Base):
    type: Literal["STAR"]
    clazz: Literal["STAR"] = Field(alias="class")

    alias: str
    columns: object

    replace_list: list[object]
    relation_name: str
    exclude_list: list[object]


class Constant(Base):
    type: Literal["CONSTANT"]
    clazz: Literal["CONSTANT"] = Field(alias="class")

    alias: str
    value: Value


class CastExpression(ParsedExpression):
    """
    https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/cast_expression.hpp#L22-L26
    """

    type: Literal["CAST"]
    clazz: Literal["CAST"] = Field(alias="class")
    child: "Select"
    cast_type: ValueType
    try_cast: bool


Select = Annotated[
    Union["Function", ColumnRefExpression, Star, Constant, CastExpression],
    Field(discriminator="type"),
]


class Comparison(Base):
    clazz: Literal["COMPARISON"] = Field(alias="class")
    type: Literal["GREATERTHAN", "EQUAL"]
    alias: str
    left: Select
    right: Select


class Conjunction(Base):
    clazz: Literal["CONJUNCTION"] = Field(alias="class")
    type: Literal["AND"]
    alias: str
    children: list["Clause"]


Clause = Annotated[Union[Comparison, Conjunction], Field(discriminator="class")]

Conjunction.update_forward_refs()


class BaseTable(Base):
    type: Literal["BASE_TABLE"]
    alias: str
    sample: Optional[int]
    schema_name: str
    table_name: str
    catalog_name: str
    column_name_alias: Optional[list[str]]


class EmptyTable(Base):
    type: Literal["EMPTY"]
    alias: str
    sample: Optional[int]


class OrderModifier(Base):
    type: Literal["ORDER_MODIFIER"]
    orders: list[object]


class Function(Base):
    clazz: Literal["FUNCTION"] = Field(alias="class")
    type: Literal["FUNCTION"]
    schema_name: str = Field(alias="schema")
    function_name: str
    catalog: str
    alias: str
    is_operator: bool
    children: list[Select]
    distinct: bool
    order_bys: OrderModifier
    export_state: bool
    filter: Optional[object]


class TableFunction(Base):
    type: Literal["TABLE_FUNCTION"]
    alias: str
    function: Function
    sample: Optional[int]
    column_name_alias: Optional[list[str]]


class AggregrateHandling(Enum):
    STANDARD_HANDLING = "STANDARD_HANDLING"


class Statement(Base):
    type: StatementType
    modifiers: list[object]
    cte_map: dict
    select_list: list[Select]
    where_clause: Optional[Clause]
    sample: Optional[int]
    qualify: Optional[list[object]]
    having: Optional[list[object]]
    group_sets: Optional[list[object]]
    group_expressions: Optional[list[object]]
    aggregate_handling: Optional[AggregrateHandling]
    from_table: Annotated[
        Union[BaseTable, EmptyTable, TableFunction], Field(discriminator="type")
    ]


class ErrorResponse(Base):
    error: Literal[True]
    error_message: str
    error_type: str


class SuccessResponse(Base):
    error: Literal[False]
    statements: list[Statement]


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
Comparison.update_forward_refs()

# print(schema_json_of(Root))
