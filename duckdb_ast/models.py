from enum import Enum
from typing import Annotated, Generic, Literal, Optional, TypeVar, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel

__all__ = [
    "AggregateHandling",
    "Base",
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
    "DistinctModifier",
    "EmptyTableRef",
    "ErrorResponse",
    "ExpressionType",
    "ExtraTypeInfo",
    "FunctionExpression",
    "JoinRef",
    "LambdaExpression",
    "LimitModifier",
    "LimitPercentModifier",
    "ListTypeInfo",
    "LogicalType",
    "LogicalTypeId",
    "OperatorExpression",
    "OrderByNode",
    "OrderByNullType",
    "OrderedDict",
    "OrderModifier",
    "OrderType",
    "Pair",
    "ParameterExpression",
    "ParsedExpression",
    "ParsedExpressionSubclasses",
    "PositionalReferenceExpression",
    "QueryNode",
    "QueryNodeSubclasses",
    "RecursiveCTENode",
    "ResultModifier",
    "ResultModifierSubclasses",
    "Root",
    "SampleMethod",
    "SampleOptions",
    "SelectNode",
    "SelectStatement",
    "SetOperationNode",
    "StandardEntry",
    "StarExpression",
    "StatementType",
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
    "WindowBoundary",
    "WindowExpression",
]

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Base(BaseModel):
    """
    Base model with config
    """

    model_config = ConfigDict(extra="forbid")
    query_location: Optional[int] = None


class Pair(BaseModel, Generic[K, V]):
    key: K
    value: V


class OrderedDict(RootModel[list[Pair[K, V]]], Generic[K, V]):
    pass


class BaseExpression(Base):
    """
    .. gh_link:: src/include/duckdb/parser/base_expression.hpp#L18
    """

    type: str
    clazz: str = Field(alias="class")
    alias: str


class ParsedExpression(BaseExpression):
    """
    .. gh_link:: src/include/duckdb/parser/parsed_expression.hpp#L34
    """


class LogicalTypeId(Enum):
    """
    .. gh_link:: src/include/duckdb/common/types.hpp#L185
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
    .. gh_link:: src/include/duckdb/catalog/catalog_entry.hpp#L25
    """


class StandardEntry(CatalogEntry):
    """
    .. gh_link:: src/include/duckdb/catalog/standard_entry.hpp#L17
    """


class TypeCatalogEntry(StandardEntry):
    """
    .. gh_link:: src/include/duckdb/catalog/catalog_entry/type_catalog_entry.hpp#L18
    """

    user_type: "LogicalType"


class ExtraTypeInfo(Base):
    """
    .. gh_link:: src/include/duckdb/common/extra_type_info.hpp#L31
    """

    type: str
    alias: str
    catalog_entry: Optional[TypeCatalogEntry] = None
    modifiers: list["Value"]


class ListTypeInfo(ExtraTypeInfo):
    """
    .. gh_link:: src/include/duckdb/common/extra_type_info.hpp#L105
    """

    type: Literal["LIST_TYPE_INFO"]
    child_type: "LogicalType"


class DecimalTypeInfo(ExtraTypeInfo):
    """
    .. gh_link:: src/include/duckdb/common/extra_type_info.hpp#L66
    """

    type: Literal["DECIMAL_TYPE_INFO"]
    width: int
    scale: int


class UserTypeInfo(ExtraTypeInfo):
    """
    .. gh_link:: src/include/duckdb/common/extra_type_info.hpp#L163
    """

    type: Literal["USER_TYPE_INFO"]
    user_type_name: str
    schema_name: str = Field(alias="schema")
    catalog: str
    user_type_modifiers: list["Value"]


class LogicalType(Base):
    """
    .. gh_link:: src/include/duckdb/common/types.hpp#L238
    """

    id: LogicalTypeId
    type_info: Optional[
        Union[ListTypeInfo, DecimalTypeInfo, UserTypeInfo, "StructTypeInfo"]
    ] = Field(discriminator="type")


class FirstSecond(BaseModel, Generic[K, V]):
    first: K
    second: V


class StructTypeInfo(ExtraTypeInfo):
    """
    .. gh_link:: src/include/duckdb/common/extra_type_info.hpp#L124
    """

    type: Literal["STRUCT_TYPE_INFO"]
    child_types: list[FirstSecond[str, LogicalType]]


class Value(Base, Generic[T]):
    """
    .. gh_link:: src/include/duckdb/common/types/value.hpp#L30
    """

    type: LogicalType
    value: Optional[T] = None
    is_null: bool


class ColumnRefExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/columnref_expression.hpp#L18
    """

    type: Literal["COLUMN_REF"]
    clazz: Literal["COLUMN_REF"] = Field(alias="class")

    column_names: list[str]


class ConstantExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/constant_expression.hpp#L17
    """

    type: Literal["VALUE_CONSTANT"]
    clazz: Literal["CONSTANT"] = Field(alias="class")

    value: Value


class CastExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/cast_expression.hpp#L17
    """

    type: Literal["OPERATOR_CAST"]
    clazz: Literal["CAST"] = Field(alias="class")
    child: "ParsedExpressionSubclasses"
    cast_type: LogicalType
    try_cast: bool


class ComparisonExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/comparison_expression.hpp#L16
    """

    clazz: Literal["COMPARISON"] = Field(alias="class")
    type: Literal[
        "COMPARE_GREATERTHAN",
        "COMPARE_EQUAL",
        "COMPARE_EQUAL",
        "COMPARE_NOTEQUAL",
        "COMPARE_GREATERTHANOREQUALTO",
        "COMPARE_NOT_DISTINCT_FROM",
        "COMPARE_DISTINCT_FROM",
        "COMPARE_LESSTHANOREQUALTO",
        "COMPARE_LESSTHAN",
    ]
    left: "ParsedExpressionSubclasses"
    right: "ParsedExpressionSubclasses"


class ConjunctionExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/conjunction_expression.hpp#L17
    """

    clazz: Literal["CONJUNCTION"] = Field(alias="class")
    type: Literal["CONJUNCTION_AND", "CONJUNCTION_OR"]
    children: list["ParsedExpressionSubclasses"]


class ExpressionType(Enum):
    """
    .. gh_link:: src/include/duckdb/common/enums/expression_type.hpp#L18
    """

    INVALID = "INVALID"

    # explicitly cast left as right (right is integer in ValueType enum)
    OPERATOR_CAST = "OPERATOR_CAST"
    # logical not operator
    OPERATOR_NOT = "OPERATOR_NOT"
    # is null operator
    OPERATOR_IS_NULL = "OPERATOR_IS_NULL"
    # is not null operator
    OPERATOR_IS_NOT_NULL = "OPERATOR_IS_NOT_NULL"

    # -----------------------------
    # Comparison Operators
    # -----------------------------
    # equal operator between left and right
    COMPARE_EQUAL = "COMPARE_EQUAL"
    # compare initial boundary
    COMPARE_BOUNDARY_START = "COMPARE_BOUNDARY_START"
    # inequal operator between left and right
    COMPARE_NOTEQUAL = "COMPARE_NOTEQUAL"
    # less than operator between left and right
    COMPARE_LESSTHAN = "COMPARE_LESSTHAN"
    # greater than operator between left and right
    COMPARE_GREATERTHAN = "COMPARE_GREATERTHAN"
    # less than equal operator between left and right
    COMPARE_LESSTHANOREQUALTO = "COMPARE_LESSTHANOREQUALTO"
    # greater than equal operator between left and right
    COMPARE_GREATERTHANOREQUALTO = "COMPARE_GREATERTHANOREQUALTO"
    # IN operator [left IN (right1, right2, ...)]
    COMPARE_IN = "COMPARE_IN"
    # NOT IN operator [left NOT IN (right1, right2, ...)]
    COMPARE_NOT_IN = "COMPARE_NOT_IN"
    # IS DISTINCT FROM operator
    COMPARE_DISTINCT_FROM = "COMPARE_DISTINCT_FROM"

    COMPARE_BETWEEN = "COMPARE_BETWEEN"
    COMPARE_NOT_BETWEEN = "COMPARE_NOT_BETWEEN"
    # IS NOT DISTINCT FROM operator
    COMPARE_NOT_DISTINCT_FROM = "COMPARE_NOT_DISTINCT_FROM"
    # compare final boundary
    COMPARE_BOUNDARY_END = "COMPARE_BOUNDARY_END"

    # -----------------------------
    # Conjunction Operators
    # -----------------------------
    CONJUNCTION_AND = "CONJUNCTION_AND"
    CONJUNCTION_OR = "CONJUNCTION_OR"

    # -----------------------------
    # Values
    # -----------------------------
    VALUE_CONSTANT = "VALUE_CONSTANT"
    VALUE_PARAMETER = "VALUE_PARAMETER"
    VALUE_TUPLE = "VALUE_TUPLE"
    VALUE_TUPLE_ADDRESS = "VALUE_TUPLE_ADDRESS"
    VALUE_NULL = "VALUE_NULL"
    VALUE_VECTOR = "VALUE_VECTOR"
    VALUE_SCALAR = "VALUE_SCALAR"
    VALUE_DEFAULT = "VALUE_DEFAULT"

    # -----------------------------
    # Aggregates
    # -----------------------------
    AGGREGATE = "AGGREGATE"
    BOUND_AGGREGATE = "BOUND_AGGREGATE"
    GROUPING_FUNCTION = "GROUPING_FUNCTION"

    # -----------------------------
    # Window Functions
    # -----------------------------
    WINDOW_AGGREGATE = "WINDOW_AGGREGATE"

    WINDOW_RANK = "WINDOW_RANK"
    WINDOW_RANK_DENSE = "WINDOW_RANK_DENSE"
    WINDOW_NTILE = "WINDOW_NTILE"
    WINDOW_PERCENT_RANK = "WINDOW_PERCENT_RANK"
    WINDOW_CUME_DIST = "WINDOW_CUME_DIST"
    WINDOW_ROW_NUMBER = "WINDOW_ROW_NUMBER"

    WINDOW_FIRST_VALUE = "WINDOW_FIRST_VALUE"
    WINDOW_LAST_VALUE = "WINDOW_LAST_VALUE"
    WINDOW_LEAD = "WINDOW_LEAD"
    WINDOW_LAG = "WINDOW_LAG"
    WINDOW_NTH_VALUE = "WINDOW_NTH_VALUE"

    # -----------------------------
    # Functions
    # -----------------------------
    FUNCTION = "FUNCTION"
    BOUND_FUNCTION = "BOUND_FUNCTION"

    # -----------------------------
    # Operators
    # -----------------------------
    CASE_EXPR = "CASE_EXPR"
    OPERATOR_NULLIF = "OPERATOR_NULLIF"
    OPERATOR_COALESCE = "OPERATOR_COALESCE"
    ARRAY_EXTRACT = "ARRAY_EXTRACT"
    ARRAY_SLICE = "ARRAY_SLICE"
    STRUCT_EXTRACT = "STRUCT_EXTRACT"
    ARRAY_CONSTRUCTOR = "ARRAY_CONSTRUCTOR"
    ARROW = "ARROW"

    # -----------------------------
    # Subquery IN/EXISTS
    # -----------------------------
    SUBQUERY = "SUBQUERY"

    # -----------------------------
    # Parser
    # -----------------------------
    STAR = "STAR"
    TABLE_STAR = "TABLE_STAR"
    PLACEHOLDER = "PLACEHOLDER"
    COLUMN_REF = "COLUMN_REF"
    FUNCTION_REF = "FUNCTION_REF"
    TABLE_REF = "TABLE_REF"

    # -----------------------------
    # Miscellaneous
    # -----------------------------
    CAST = "CAST"
    BOUND_REF = "BOUND_REF"
    BOUND_COLUMN_REF = "BOUND_COLUMN_REF"
    BOUND_UNNEST = "BOUND_UNNEST"
    COLLATE = "COLLATE"
    LAMBDA = "LAMBDA"
    POSITIONAL_REFERENCE = "POSITIONAL_REFERENCE"
    BOUND_LAMBDA_REF = "BOUND_LAMBDA_REF"


class OperatorExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/operator_expression.hpp#L19
    """

    clazz: Literal["OPERATOR"] = Field(alias="class")
    type: Literal[
        "OPERATOR_IS_NULL",
        "OPERATOR_IN",
        "OPERATOR_NOT",
        "OPERATOR_IS_NOT_NULL",
        "COMPARE_NOT_IN",
        "COMPARE_IN",
        "ARRAY_EXTRACT",
        "ARRAY_SLICE",
        "STRUCT_EXTRACT",
    ]
    children: list["ParsedExpressionSubclasses"]


class WindowBoundary(Enum):
    """
    .. gh_link:: src/include/duckdb/parser/expression/window_expression.hpp#L16
    """

    INVALID = "INVALID"
    UNBOUNDED_PRECEDING = "UNBOUNDED_PRECEDING"
    UNBOUNDED_FOLLOWING = "UNBOUNDED_FOLLOWING"
    CURRENT_ROW_RANGE = "CURRENT_ROW_RANGE"
    CURRENT_ROW_ROWS = "CURRENT_ROW_ROWS"
    EXPR_PRECEDING_ROWS = "EXPR_PRECEDING_ROWS"
    EXPR_FOLLOWING_ROWS = "EXPR_FOLLOWING_ROWS"
    EXPR_PRECEDING_RANGE = "EXPR_PRECEDING_RANGE"
    EXPR_FOLLOWING_RANGE = "EXPR_FOLLOWING_RANGE"


class WindowExcludeMode(Enum):
    """
    .. gh_link:: src/include/duckdb/parser/expression/window_expression.hpp#L29
    """

    NO_OTHER = "NO_OTHER"
    CURRENT_ROW = "CURRENT_ROW"
    GROUP = "GROUP"
    TIES = "TIES"


class WindowExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/window_expression.hpp#L35
    """

    clazz: Literal["WINDOW"] = Field(alias="class")
    type: Literal[
        "WINDOW_AGGREGATE",
        "WINDOW_ROW_NUMBER",
        "WINDOW_FIRST_VALUE",
        "WINDOW_LAST_VALUE",
        "WINDOW_NTH_VALUE",
        "WINDOW_RANK",
        "WINDOW_RANK_DENSE",
        "WINDOW_PERCENT_RANK",
        "WINDOW_CUME_DIST",
        "WINDOW_LEAD",
        "WINDOW_LAG",
        "WINDOW_NTILE",
    ]

    # Catalog of the aggregate function
    catalog: str
    # Schema of the aggregate function
    schema_name: str = Field(alias="schema")
    # Name of the aggregate function
    function_name: str
    # The child expression of the main window function
    children: list["ParsedExpressionSubclasses"]
    # The set of expressions to partition by
    partitions: list["ParsedExpressionSubclasses"]
    # The set of ordering clauses
    orders: list["OrderByNode"]
    # Expression representing a filter, only used for aggregates
    filter_expr: Optional["ParsedExpressionSubclasses"] = None
    # True to ignore NULL values
    ignore_nulls: bool
    # The window boundaries
    start: WindowBoundary = WindowBoundary.INVALID
    end: WindowBoundary = WindowBoundary.INVALID

    start_expr: Optional["ParsedExpressionSubclasses"] = None
    end_expr: Optional["ParsedExpressionSubclasses"] = None
    # Offset and default expressions for WINDOW_LEAD and WINDOW_LAG functions
    offset_expr: Optional["ParsedExpressionSubclasses"] = None
    default_expr: Optional["ParsedExpressionSubclasses"] = None

    exclude_clause: WindowExcludeMode = WindowExcludeMode.NO_OTHER
    distinct: bool


class SubqueryExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/subquery_expression.hpp#L18
    """

    type: Literal["SUBQUERY"]
    clazz: Literal["SUBQUERY"] = Field(alias="class")

    child: Optional["ParsedExpressionSubclasses"] = None
    comparison_type: Literal["INVALID", "COMPARE_EQUAL"]
    subquery: "SelectStatement"
    subquery_type: Literal["SCALAR", "ANY", "EXISTS", "INVALID", "NOT_EXISTS"]


class CaseCheck(Base):
    """
    .. gh_link:: src/include/duckdb/parser/expression/case_expression.hpp#L16
    """

    when_expr: "ParsedExpressionSubclasses"
    then_expr: "ParsedExpressionSubclasses"


class CollateExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/collate_expression.hpp#L16
    """

    type: Literal["COLLATE"]
    clazz: Literal["COLLATE"] = Field(alias="class")

    child: "ParsedExpressionSubclasses"
    collation: str


class CaseExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/case_expression.hpp#L25
    """

    type: Literal["CASE_EXPR"]
    clazz: Literal["CASE"] = Field(alias="class")

    case_checks: list[CaseCheck]
    else_expr: "ParsedExpressionSubclasses"


class BetweenExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/between_expression.hpp#L15
    """

    clazz: Literal["BETWEEN"] = Field(alias="class")
    type: Literal["COMPARE_BETWEEN"]

    input: "ParsedExpressionSubclasses"
    lower: "ParsedExpressionSubclasses"
    upper: "ParsedExpressionSubclasses"


class PositionalReferenceExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/positional_reference_expression.hpp#L14
    """

    type: Literal["POSITIONAL_REFERENCE"]
    clazz: Literal["POSITIONAL_REFERENCE"] = Field(alias="class")
    index: int


class ParameterExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/parameter_expression.hpp#L30
    """

    type: Literal["VALUE_PARAMETER"]
    clazz: Literal["PARAMETER"] = Field(alias="class")
    identifier: str


class LambdaExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/lambda_expression.hpp#L20
    """

    type: Literal["LAMBDA"]
    clazz: Literal["LAMBDA"] = Field(alias="class")
    lhs: "ParsedExpressionSubclasses"
    # params: Optional[List['ParsedExpressionSubclasses']] not included in serialization
    expr: "ParsedExpressionSubclasses"


class ParsedExpressionSubclasses(
    RootModel[
        Annotated[
            Union[
                "FunctionExpression",
                ColumnRefExpression,
                "StarExpression",
                ConstantExpression,
                CastExpression,
                ComparisonExpression,
                ConjunctionExpression,
                LambdaExpression,
                ParameterExpression,
                PositionalReferenceExpression,
                SubqueryExpression,
                OperatorExpression,
                CaseExpression,
                CollateExpression,
                BetweenExpression,
                WindowExpression,
            ],
            Field(discriminator="type"),
        ]
    ]
):
    """Union of :class:`ParsedExpression` subclasses"""


class StarExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/star_expression.hpp#L17
    """

    type: Literal["STAR"]
    clazz: Literal["STAR"] = Field(alias="class")

    columns: bool

    replace_list: OrderedDict[str, ParsedExpressionSubclasses]
    relation_name: str
    exclude_list: list[str]
    expr: Optional["ParsedExpressionSubclasses"] = None
    unpacked: bool


class SampleMethod(Enum):
    """
    .. gh_link:: src/include/duckdb/parser/parsed_data/sample_options.hpp#L18
    """

    SYSTEM_SAMPLE = "System"
    BERNOULLI_SAMPLE = "Bernoulli"
    RESERVOIR_SAMPLE = "Reservoir"


class SampleOptions(Base):
    """
    .. gh_link:: src/include/duckdb/parser/parsed_data/sample_options.hpp#L23
    """

    sample_size: Value
    is_percentage: bool
    method: SampleMethod
    seed: int = -1


class TableRef(Base):
    """
    .. gh_link:: src/include/duckdb/parser/tableref.hpp#L20
    """

    alias: str
    sample: Optional[SampleOptions] = None


class BaseTableRef(TableRef):
    """
    .. gh_link:: src/include/duckdb/parser/tableref/basetableref.hpp#L16
    """

    type: Literal["BASE_TABLE"]

    schema_name: str
    table_name: str
    catalog_name: str
    column_name_alias: Optional[list[str]] = None


class EmptyTableRef(TableRef):
    """
    .. gh_link:: src/include/duckdb/parser/tableref/emptytableref.hpp#L15
    """

    type: Literal["EMPTY"]


class JoinRef(TableRef):
    """
    .. gh_link:: src/include/duckdb/parser/tableref/joinref.hpp#L21
    """

    type: Literal["JOIN"]

    right: "TableRefSubclasses"
    left: "TableRefSubclasses"
    join_type: Literal[
        "INVALID",  # invalid join type
        "LEFT",  # left
        "RIGHT",  # right
        "INNER",  # inner
        "OUTER",  # outer
        "SEMI",  # SEMI join returns left side row ONLY if it has a join partner, no duplicates
        "ANTI",  # ANTI join returns left side row ONLY if it has NO join partner, no duplicates
        "MARK",  # MARK join returns marker indicating whether or not there is a join partner (true), there is no join
        # partner (false)
        "SINGLE",  # SINGLE join is like LEFT OUTER JOIN, BUT returns at most one join partner per entry on the LEFT side
        # (and NULL if no partner is found)
    ]
    ref_type: Literal["CROSS", "ASOF", "NATURAL", "REGULAR", "DEPENDENT", "POSITIONAL"]
    condition: Optional["ParsedExpressionSubclasses"] = None
    using_columns: list[str]
    delim_flipped: bool
    duplicate_eliminated_columns: list[str]


class OrderType(Enum):
    """
    .. gh_link:: src/include/duckdb/common/enums/order_type.hpp#L16
    """

    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OrderByNullType(Enum):
    """
    .. gh_link:: src/include/duckdb/common/enums/order_type.hpp#L18
    """

    INVALID = "INVALID"
    ORDER_DEFAULT = "ORDER_DEFAULT"
    NULLS_FIRST = "NULLS_FIRST"
    NULLS_LAST = "NULLS_LAST"


class OrderByNode(Base):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L69
    """

    type: OrderType
    null_order: OrderByNullType
    expression: "ParsedExpressionSubclasses"


class OrderModifier(Base):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L121
    """

    type: Literal["ORDER_MODIFIER"]
    orders: list[OrderByNode]


class FunctionExpression(ParsedExpression):
    """
    .. gh_link:: src/include/duckdb/parser/expression/function_expression.hpp#L17
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
    filter: Optional[ParsedExpressionSubclasses] = None


class TableFunctionRef(TableRef):
    """
    .. gh_link:: src/include/duckdb/parser/tableref/table_function_ref.hpp#L18
    """

    type: Literal["TABLE_FUNCTION"]

    function: FunctionExpression
    column_name_alias: Optional[list[str]] = None


class AggregateHandling(Enum):
    """
    .. gh_link:: src/include/duckdb/common/enums/aggregate_handling.hpp#L16
    """

    # standard handling as in the SELECT clause
    STANDARD_HANDLING = "STANDARD_HANDLING"

    # aggregates allowed: any aggregates in this node will result in an error
    NO_AGGREGATES_ALLOWED = "NO_AGGREGATES_ALLOWED"

    # force aggregates: any non-aggregate select list entry will become a GROUP
    FORCE_AGGREGATES = "FORCE_AGGREGATES"


class ResultModifier(Base):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L33
    """

    type: str


class LimitModifier(ResultModifier):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L98
    """

    type: Literal["LIMIT_MODIFIER"]

    limit: "ParsedExpressionSubclasses"
    offset: "ParsedExpressionSubclasses"


class DistinctModifier(ResultModifier):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L144
    """

    type: Literal["DISTINCT_MODIFIER"]

    distinct_on_targets: list["ParsedExpressionSubclasses"]


class LimitPercentModifier(ResultModifier):
    """
    .. gh_link:: src/include/duckdb/parser/result_modifier.hpp#L165
    """

    type: Literal["LIMIT_PERCENT_MODIFIER"]

    limit: "ParsedExpressionSubclasses"
    offset: "ParsedExpressionSubclasses"


class ResultModifierSubclasses(
    RootModel[
        Annotated[
            Union[LimitPercentModifier, DistinctModifier, LimitModifier, OrderModifier],
            Field(discriminator="type"),
        ]
    ]
):
    "Union of :class:`ResultModifier` subclasses"


class CommonTableExpressionInfo(Base):
    """
    .. gh_link:: src/include/duckdb/parser/common_table_expression_info.hpp#L18
    """

    aliases: list[str]
    query: "SelectStatement"
    materialized: Literal[
        "CTE_MATERIALIZE_DEFAULT", "CTE_MATERIALIZE_ALWAYS", "CTE_MATERIALIZE_NEVER"
    ]


class CommonTableExpressionMap(Base):
    """
    .. gh_link:: src/include/duckdb/parser/query_node.hpp#L32
    """

    map: OrderedDict[str, CommonTableExpressionInfo]


class QueryNode(Base):
    """
    .. gh_link:: src/include/duckdb/parser/query_node.hpp#L47
    """

    type: str
    modifiers: list[ResultModifierSubclasses]

    cte_map: CommonTableExpressionMap


class SubqueryRef(TableRef):
    """
    .. gh_link:: src/include/duckdb/parser/tableref/subqueryref.hpp#L16
    """

    type: Literal["SUBQUERY"]

    subquery: "SelectStatement"
    column_name_alias: list[str]


class TableRefSubclasses(
    RootModel[
        Annotated[
            Union[BaseTableRef, EmptyTableRef, TableFunctionRef, SubqueryRef, JoinRef],
            Field(discriminator="type"),
        ]
    ]
):
    "Union of :class:`TableRef` subclasses"


GroupingSet = set[int]


class SelectNode(QueryNode):
    """
    .. gh_link:: src/include/duckdb/parser/query_node/select_node.hpp#L22
    """

    type: Literal["SELECT_NODE"]
    select_list: list[ParsedExpressionSubclasses]
    where_clause: Optional[ParsedExpressionSubclasses] = None
    sample: Optional[SampleOptions] = None
    qualify: Optional[ParsedExpressionSubclasses] = None
    having: Optional[ParsedExpressionSubclasses] = None
    group_sets: Optional[list[GroupingSet]] = None
    group_expressions: Optional[list[ParsedExpressionSubclasses]] = None
    aggregate_handling: Optional[AggregateHandling] = None
    from_table: TableRefSubclasses


class ErrorResponse(Base):
    "Error shape for when parsing fails"

    error: Literal[True]
    error_message: str
    error_type: str
    error_subtype: Optional[str] = None
    position: Optional[int] = None


class SetOperationNode(QueryNode):
    """
    .. gh_link:: src/include/duckdb/parser/query_node/set_operation_node.hpp#L18
    """

    type: Literal["SET_OPERATION_NODE"]
    setop_type: Literal["NONE", "UNION", "EXCEPT", "INTERSECT", "UNION_BY_NAME"]

    left: "QueryNodeSubclasses"
    right: "QueryNodeSubclasses"
    setop_all: bool = True


class RecursiveCTENode(QueryNode):
    """
    .. gh_link:: src/include/duckdb/parser/query_node/recursive_cte_node.hpp#L17
    """

    type: Literal["RECURSIVE_CTE_NODE"]

    cte_name: str
    union_all: bool
    left: "QueryNodeSubclasses"
    right: "QueryNodeSubclasses"
    aliases: list[str]


class CTENode(QueryNode):
    """
    .. gh_link:: src/include/duckdb/parser/query_node/cte_node.hpp#L17
    """

    type: Literal["CTE_NODE"]

    cte_name: str
    query: "QueryNodeSubclasses"
    child: "QueryNodeSubclasses"
    aliases: list[str]


class QueryNodeSubclasses(
    RootModel[
        Annotated[
            Union[SelectNode, SetOperationNode, CTENode, RecursiveCTENode],
            Field(discriminator="type"),
        ]
    ]
):
    "Union of :class:`QueryNode` subclasses"


class StatementType(Enum):
    """
    .. gh_link:: src/include/duckdb/common/enums/statement_type.hpp#L19
    """

    SELECT = "SELECT"
    INVALID_STATEMENT = "INVALID_STATEMENT"  # invalid statement type
    SELECT_STATEMENT = "SELECT_STATEMENT"  # select statement type
    INSERT_STATEMENT = "INSERT_STATEMENT"  # insert statement type
    UPDATE_STATEMENT = "UPDATE_STATEMENT"  # update statement type
    CREATE_STATEMENT = "CREATE_STATEMENT"  # create statement type
    DELETE_STATEMENT = "DELETE_STATEMENT"  # delete statement type
    PREPARE_STATEMENT = "PREPARE_STATEMENT"  # prepare statement type
    EXECUTE_STATEMENT = "EXECUTE_STATEMENT"  # execute statement type
    ALTER_STATEMENT = "ALTER_STATEMENT"  # alter statement type
    TRANSACTION_STATEMENT = "TRANSACTION_STATEMENT"  # transaction statement type,
    COPY_STATEMENT = "COPY_STATEMENT"  # copy type
    ANALYZE_STATEMENT = "ANALYZE_STATEMENT"  # analyze type
    VARIABLE_SET_STATEMENT = "VARIABLE_SET_STATEMENT"  # variable set statement type
    CREATE_FUNC_STATEMENT = "CREATE_FUNC_STATEMENT"  # create func statement type
    EXPLAIN_STATEMENT = "EXPLAIN_STATEMENT"  # explain statement type
    DROP_STATEMENT = "DROP_STATEMENT"  # DROP statement type
    EXPORT_STATEMENT = "EXPORT_STATEMENT"  # EXPORT statement type
    PRAGMA_STATEMENT = "PRAGMA_STATEMENT"  # PRAGMA statement type
    SHOW_STATEMENT = "SHOW_STATEMENT"  # SHOW statement type
    VACUUM_STATEMENT = "VACUUM_STATEMENT"  # VACUUM statement type
    CALL_STATEMENT = "CALL_STATEMENT"  # CALL statement type
    SET_STATEMENT = "SET_STATEMENT"  # SET statement type
    LOAD_STATEMENT = "LOAD_STATEMENT"  # LOAD statement type
    RELATION_STATEMENT = "RELATION_STATEMENT"
    EXTENSION_STATEMENT = "EXTENSION_STATEMENT"
    LOGICAL_PLAN_STATEMENT = "LOGICAL_PLAN_STATEMENT"
    ATTACH_STATEMENT = "ATTACH_STATEMENT"
    DETACH_STATEMENT = "DETACH_STATEMENT"
    MULTI_STATEMENT = "MULTI_STATEMENT"


class SelectStatement(Base):
    """
    .. gh_link:: src/include/duckdb/parser/statement/select_statement.hpp#L24
    """

    node: "QueryNodeSubclasses"


class SuccessResponse(Base):
    "Returned when parsing succeeds"

    error: Literal[False]
    statements: list[SelectStatement]


class Root(
    RootModel[
        Annotated[Union[ErrorResponse, SuccessResponse], Field(discriminator="error")]
    ]
):
    "Union of possible responses"


CastExpression.model_rebuild()
ComparisonExpression.model_rebuild()
ListTypeInfo.model_rebuild()
StarExpression.model_rebuild()
ConjunctionExpression.model_rebuild()
TypeCatalogEntry.model_rebuild()
SubqueryExpression.model_rebuild()
OperatorExpression.model_rebuild()
CaseExpression.model_rebuild()
CaseCheck.model_rebuild()
SubqueryRef.model_rebuild()
CollateExpression.model_rebuild()
CommonTableExpressionInfo.model_rebuild()
BetweenExpression.model_rebuild()
SetOperationNode.model_rebuild()
SelectStatement.model_rebuild()
RecursiveCTENode.model_rebuild()
WindowExpression.model_rebuild()
JoinRef.model_rebuild()
StructTypeInfo.model_rebuild()
LogicalType.model_rebuild()
ParsedExpressionSubclasses.model_rebuild()
LambdaExpression.model_rebuild()
