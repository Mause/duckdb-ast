# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_generation 1'] = {
    '$ref': '#/definitions/Root',
    'definitions': {
        'AggregateHandling': {
            'description': 'src/include/duckdb/common/enums/aggregate_handling.hpp#L16',
            'enum': [
                'STANDARD_HANDLING',
                'NO_AGGREGATES_ALLOWED',
                'FORCE_AGGREGATES'
            ],
            'title': 'AggregateHandling'
        },
        'BaseTableRef': {
            'additionalProperties': False,
            'description': '''Represents a TableReference to a base table in the schema
src/include/duckdb/parser/tableref/basetableref.hpp#L16''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_name': {
                    'title': 'Catalog Name',
                    'type': 'string'
                },
                'column_name_alias': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Column Name Alias',
                    'type': 'array'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'schema_name': {
                    'title': 'Schema Name',
                    'type': 'string'
                },
                'table_name': {
                    'title': 'Table Name',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'BASE_TABLE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'alias',
                'type',
                'schema_name',
                'table_name',
                'catalog_name'
            ],
            'title': 'BaseTableRef',
            'type': 'object'
        },
        'BetweenExpression': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/expression/between_expression.hpp#L15',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'enum': [
                        'BETWEEN'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'input': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'lower': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'COMPARE_BETWEEN'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'upper': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'input',
                'lower',
                'upper'
            ],
            'title': 'BetweenExpression',
            'type': 'object'
        },
        'CaseCheck': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/expression/case_expression.hpp#L16',
            'properties': {
                'then_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'when_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                }
            },
            'required': [
                'when_expr',
                'then_expr'
            ],
            'title': 'CaseCheck',
            'type': 'object'
        },
        'CaseExpression': {
            'additionalProperties': False,
            'description': '''The CaseExpression represents a CASE expression in the query
src/include/duckdb/parser/expression/case_expression.hpp#L25''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'case_checks': {
                    'items': {
                        '$ref': '#/definitions/CaseCheck'
                    },
                    'title': 'Case Checks',
                    'type': 'array'
                },
                'class': {
                    'enum': [
                        'CASE'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'else_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'CASE_EXPR'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'case_checks',
                'else_expr'
            ],
            'title': 'CaseExpression',
            'type': 'object'
        },
        'CastExpression': {
            'additionalProperties': False,
            'description': '''CastExpression represents a type cast from one SQL type to another SQL type
src/include/duckdb/parser/expression/cast_expression.hpp#L17''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'cast_type': {
                    '$ref': '#/definitions/LogicalType'
                },
                'child': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'class': {
                    'enum': [
                        'CAST'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'try_cast': {
                    'title': 'Try Cast',
                    'type': 'boolean'
                },
                'type': {
                    'enum': [
                        'OPERATOR_CAST'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'child',
                'cast_type',
                'try_cast'
            ],
            'title': 'CastExpression',
            'type': 'object'
        },
        'CollateExpression': {
            'additionalProperties': False,
            'description': '''CollateExpression represents a COLLATE statement
src/include/duckdb/parser/expression/collate_expression.hpp#L16''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'child': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'class': {
                    'enum': [
                        'COLLATE'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'collation': {
                    'title': 'Collation',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'COLLATE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'child',
                'collation'
            ],
            'title': 'CollateExpression',
            'type': 'object'
        },
        'ColumnRefExpression': {
            'additionalProperties': False,
            'description': '''Represents a reference to a column from either the FROM clause or from an
alias
src/include/duckdb/parser/expression/columnref_expression.hpp#L18''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'enum': [
                        'COLUMN_REF'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'column_names': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Column Names',
                    'type': 'array'
                },
                'type': {
                    'enum': [
                        'COLUMN_REF'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'column_names'
            ],
            'title': 'ColumnRefExpression',
            'type': 'object'
        },
        'CommonTableExpressionInfo': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/common_table_expression_info.hpp#L17',
            'properties': {
                'aliases': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Aliases',
                    'type': 'array'
                },
                'materialized': {
                    'enum': [
                        'CTE_MATERIALIZE_DEFAULT',
                        'CTE_MATERIALIZE_ALWAYS',
                        'CTE_MATERIALIZE_NEVER'
                    ],
                    'title': 'Materialized',
                    'type': 'string'
                },
                'query': {
                    '$ref': '#/definitions/SelectStatement'
                }
            },
            'required': [
                'aliases',
                'query',
                'materialized'
            ],
            'title': 'CommonTableExpressionInfo',
            'type': 'object'
        },
        'CommonTableExpressionMap': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/query_node.hpp#L32',
            'properties': {
                'map': {
                    '$ref': '#/definitions/OrderedDict_str__CommonTableExpressionInfo_'
                }
            },
            'required': [
                'map'
            ],
            'title': 'CommonTableExpressionMap',
            'type': 'object'
        },
        'ComparisonExpression': {
            'additionalProperties': False,
            'description': '''ComparisonExpression represents a boolean comparison (e.g. =, >=, <>). Always returns a boolean
and has two children.
src/include/duckdb/parser/expression/comparison_expression.hpp#L16''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'enum': [
                        'COMPARISON'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'left': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'right': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'COMPARE_GREATERTHAN',
                        'COMPARE_EQUAL',
                        'COMPARE_NOTEQUAL',
                        'COMPARE_GREATERTHANOREQUALTO',
                        'COMPARE_NOT_DISTINCT_FROM',
                        'COMPARE_DISTINCT_FROM',
                        'COMPARE_LESSTHANOREQUALTO',
                        'COMPARE_LESSTHAN'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'left',
                'right'
            ],
            'title': 'ComparisonExpression',
            'type': 'object'
        },
        'ConjunctionExpression': {
            'additionalProperties': False,
            'description': '''Represents a conjunction (AND/OR)
src/include/duckdb/parser/expression/conjunction_expression.hpp#L17''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'children': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'enum': [
                        'CONJUNCTION'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'CONJUNCTION_AND',
                        'CONJUNCTION_OR'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'children'
            ],
            'title': 'ConjunctionExpression',
            'type': 'object'
        },
        'ConstantExpression': {
            'additionalProperties': False,
            'description': '''ConstantExpression represents a constant value in the query
src/include/duckdb/parser/expression/constant_expression.hpp#L17''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'enum': [
                        'CONSTANT'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'VALUE_CONSTANT'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/definitions/Value'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'value'
            ],
            'title': 'ConstantExpression',
            'type': 'object'
        },
        'DecimalTypeInfo': {
            'additionalProperties': False,
            'description': '''Decimal Type
src/common/types.cpp#L868''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    '$ref': '#/definitions/TypeCatalogEntry'
                },
                'scale': {
                    'title': 'Scale',
                    'type': 'integer'
                },
                'type': {
                    'enum': [
                        'DECIMAL_TYPE_INFO'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'width': {
                    'title': 'Width',
                    'type': 'integer'
                }
            },
            'required': [
                'type',
                'alias',
                'width',
                'scale'
            ],
            'title': 'DecimalTypeInfo',
            'type': 'object'
        },
        'DistinctModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L119',
            'properties': {
                'distinct_on_targets': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Distinct On Targets',
                    'type': 'array'
                },
                'type': {
                    'enum': [
                        'DISTINCT_MODIFIER'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'distinct_on_targets'
            ],
            'title': 'DistinctModifier',
            'type': 'object'
        },
        'EmptyTableRef': {
            'additionalProperties': False,
            'description': '''Represents a cross product
src/include/duckdb/parser/tableref/emptytableref.hpp#L15''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'type': {
                    'enum': [
                        'EMPTY'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'alias',
                'type'
            ],
            'title': 'EmptyTableRef',
            'type': 'object'
        },
        'ErrorResponse': {
            'additionalProperties': False,
            'description': 'Error shape for when parsing fails',
            'properties': {
                'error': {
                    'enum': [
                        True
                    ],
                    'title': 'Error',
                    'type': 'boolean'
                },
                'error_message': {
                    'title': 'Error Message',
                    'type': 'string'
                },
                'error_type': {
                    'title': 'Error Type',
                    'type': 'string'
                }
            },
            'required': [
                'error',
                'error_message',
                'error_type'
            ],
            'title': 'ErrorResponse',
            'type': 'object'
        },
        'FunctionExpression': {
            'additionalProperties': False,
            'description': '''Represents a function call
src/include/duckdb/parser/expression/function_expression.hpp#L17''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog': {
                    'title': 'Catalog',
                    'type': 'string'
                },
                'children': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'enum': [
                        'FUNCTION'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'distinct': {
                    'title': 'Distinct',
                    'type': 'boolean'
                },
                'export_state': {
                    'title': 'Export State',
                    'type': 'boolean'
                },
                'filter': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'function_name': {
                    'title': 'Function Name',
                    'type': 'string'
                },
                'is_operator': {
                    'title': 'Is Operator',
                    'type': 'boolean'
                },
                'order_bys': {
                    '$ref': '#/definitions/OrderModifier'
                },
                'schema': {
                    'title': 'Schema',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'FUNCTION'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'schema',
                'function_name',
                'catalog',
                'is_operator',
                'children',
                'distinct',
                'order_bys',
                'export_state'
            ],
            'title': 'FunctionExpression',
            'type': 'object'
        },
        'JoinRef': {
            'additionalProperties': False,
            'description': '''Represents a JOIN between two expressions
src/include/duckdb/parser/tableref/joinref.hpp#L21''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'condition': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'join_type': {
                    'enum': [
                        'INNER'
                    ],
                    'title': 'Join Type',
                    'type': 'string'
                },
                'left': {
                    '$ref': '#/definitions/TableRefSubclasses'
                },
                'ref_type': {
                    'enum': [
                        'CROSS'
                    ],
                    'title': 'Ref Type',
                    'type': 'string'
                },
                'right': {
                    '$ref': '#/definitions/TableRefSubclasses'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'type': {
                    'enum': [
                        'JOIN'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'using_columns': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Using Columns',
                    'type': 'array'
                }
            },
            'required': [
                'alias',
                'type',
                'right',
                'left',
                'join_type',
                'ref_type',
                'using_columns'
            ],
            'title': 'JoinRef',
            'type': 'object'
        },
        'LimitModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L137',
            'properties': {
                'limit': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'offset': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'LIMIT_MODIFIER'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'limit',
                'offset'
            ],
            'title': 'LimitModifier',
            'type': 'object'
        },
        'LimitPercentModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L81',
            'properties': {
                'limit': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'offset': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'LIMIT_PERCENT_MODIFIER'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'limit',
                'offset'
            ],
            'title': 'LimitPercentModifier',
            'type': 'object'
        },
        'ListTypeInfo': {
            'additionalProperties': False,
            'description': '''List Type
src/common/types.cpp#L991''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    '$ref': '#/definitions/TypeCatalogEntry'
                },
                'child_type': {
                    '$ref': '#/definitions/LogicalType'
                },
                'type': {
                    'enum': [
                        'LIST_TYPE_INFO'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'alias',
                'child_type'
            ],
            'title': 'ListTypeInfo',
            'type': 'object'
        },
        'LogicalType': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/common/types.hpp#L298',
            'properties': {
                'id': {
                    '$ref': '#/definitions/LogicalTypeId'
                },
                'type_info': {
                    'discriminator': {
                        'mapping': {
                            'DECIMAL_TYPE_INFO': '#/definitions/DecimalTypeInfo',
                            'LIST_TYPE_INFO': '#/definitions/ListTypeInfo',
                            'STRUCT_TYPE_INFO': '#/definitions/StructTypeInfo',
                            'USER_TYPE_INFO': '#/definitions/UserTypeInfo'
                        },
                        'propertyName': 'type'
                    },
                    'oneOf': [
                        {
                            '$ref': '#/definitions/ListTypeInfo'
                        },
                        {
                            '$ref': '#/definitions/DecimalTypeInfo'
                        },
                        {
                            '$ref': '#/definitions/UserTypeInfo'
                        },
                        {
                            '$ref': '#/definitions/StructTypeInfo'
                        }
                    ],
                    'title': 'Type Info'
                }
            },
            'required': [
                'id'
            ],
            'title': 'LogicalType',
            'type': 'object'
        },
        'LogicalTypeId': {
            'description': '''SQL Types
src/include/duckdb/common/types.hpp#L246''',
            'enum': [
                'INVALID',
                'NULL',
                'UNKNOWN',
                'ANY',
                'USER',
                'BOOLEAN',
                'TINYINT',
                'SMALLINT',
                'INTEGER',
                'BIGINT',
                'DATE',
                'TIME',
                'TIMESTAMP_SEC',
                'TIMESTAMP_MS',
                'TIMESTAMP',
                'TIMESTAMP_NS',
                'DECIMAL',
                'FLOAT',
                'DOUBLE',
                'CHAR',
                'VARCHAR',
                'BLOB',
                'INTERVAL',
                'UTINYINT',
                'USMALLINT',
                'UINTEGER',
                'UBIGINT',
                'TIMESTAMP WITH TIME ZONE',
                'TIME_TZ',
                'BIT',
                'HUGEINT',
                'POINTER',
                'VALIDITY',
                'UUID',
                'STRUCT',
                'LIST',
                'MAP',
                'TABLE',
                'ENUM',
                'AGGREGATE_STATE',
                'LAMBDA',
                'UNION'
            ],
            'title': 'LogicalTypeId'
        },
        'OperatorExpression': {
            'additionalProperties': False,
            'description': '''Represents a built-in operator expression
src/include/duckdb/parser/expression/operator_expression.hpp#L18''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'children': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'enum': [
                        'OPERATOR'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'OPERATOR_IS_NULL',
                        'OPERATOR_IN',
                        'OPERATOR_NOT',
                        'OPERATOR_IS_NOT_NULL',
                        'COMPARE_NOT_IN',
                        'COMPARE_IN',
                        'ARRAY_EXTRACT',
                        'ARRAY_SLICE',
                        'STRUCT_EXTRACT'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'children'
            ],
            'title': 'OperatorExpression',
            'type': 'object'
        },
        'OrderByNode': {
            'additionalProperties': False,
            'description': '''Single node in ORDER BY statement
src/include/duckdb/parser/result_modifier.hpp#L60''',
            'properties': {
                'expression': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'null_order': {
                    '$ref': '#/definitions/OrderByNullType'
                },
                'type': {
                    '$ref': '#/definitions/OrderType'
                }
            },
            'required': [
                'type',
                'null_order',
                'expression'
            ],
            'title': 'OrderByNode',
            'type': 'object'
        },
        'OrderByNullType': {
            'description': 'src/include/duckdb/common/enums/order_type.hpp#L18',
            'enum': [
                'INVALID',
                'ORDER_DEFAULT',
                'NULLS_FIRST',
                'NULLS_LAST'
            ],
            'title': 'OrderByNullType'
        },
        'OrderModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L101',
            'properties': {
                'orders': {
                    'items': {
                        '$ref': '#/definitions/OrderByNode'
                    },
                    'title': 'Orders',
                    'type': 'array'
                },
                'type': {
                    'enum': [
                        'ORDER_MODIFIER'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'orders'
            ],
            'title': 'OrderModifier',
            'type': 'object'
        },
        'OrderType': {
            'description': 'src/include/duckdb/common/enums/order_type.hpp#L16',
            'enum': [
                'INVALID',
                'ORDER_DEFAULT',
                'ASCENDING',
                'DESCENDING'
            ],
            'title': 'OrderType'
        },
        'OrderedDict_str__CommonTableExpressionInfo_': {
            'items': {
                '$ref': '#/definitions/Pair_str__CommonTableExpressionInfo_'
            },
            'title': 'OrderedDict[str, CommonTableExpressionInfo]',
            'type': 'array'
        },
        'OrderedDict_str__LogicalType_': {
            'items': {
                '$ref': '#/definitions/Pair_str__LogicalType_'
            },
            'title': 'OrderedDict[str, LogicalType]',
            'type': 'array'
        },
        'OrderedDict_str__ParsedExpressionSubclasses_': {
            'items': {
                '$ref': '#/definitions/Pair_str__ParsedExpressionSubclasses_'
            },
            'title': 'OrderedDict[str, ParsedExpressionSubclasses]',
            'type': 'array'
        },
        'Pair_str__CommonTableExpressionInfo_': {
            'properties': {
                'key': {
                    'title': 'Key',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/definitions/CommonTableExpressionInfo'
                }
            },
            'required': [
                'key',
                'value'
            ],
            'title': 'Pair[str, CommonTableExpressionInfo]',
            'type': 'object'
        },
        'Pair_str__LogicalType_': {
            'properties': {
                'key': {
                    'title': 'Key',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/definitions/LogicalType'
                }
            },
            'required': [
                'key',
                'value'
            ],
            'title': 'Pair[str, LogicalType]',
            'type': 'object'
        },
        'Pair_str__ParsedExpressionSubclasses_': {
            'properties': {
                'key': {
                    'title': 'Key',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                }
            },
            'required': [
                'key',
                'value'
            ],
            'title': 'Pair[str, ParsedExpressionSubclasses]',
            'type': 'object'
        },
        'ParsedExpressionSubclasses': {
            'additionalProperties': False,
            'description': 'Union of ParsedExpression subclasses',
            'discriminator': {
                'mapping': {
                    'ARRAY_EXTRACT': '#/definitions/OperatorExpression',
                    'ARRAY_SLICE': '#/definitions/OperatorExpression',
                    'CASE_EXPR': '#/definitions/CaseExpression',
                    'COLLATE': '#/definitions/CollateExpression',
                    'COLUMN_REF': '#/definitions/ColumnRefExpression',
                    'COMPARE_BETWEEN': '#/definitions/BetweenExpression',
                    'COMPARE_DISTINCT_FROM': '#/definitions/ComparisonExpression',
                    'COMPARE_EQUAL': '#/definitions/ComparisonExpression',
                    'COMPARE_GREATERTHAN': '#/definitions/ComparisonExpression',
                    'COMPARE_GREATERTHANOREQUALTO': '#/definitions/ComparisonExpression',
                    'COMPARE_IN': '#/definitions/OperatorExpression',
                    'COMPARE_LESSTHAN': '#/definitions/ComparisonExpression',
                    'COMPARE_LESSTHANOREQUALTO': '#/definitions/ComparisonExpression',
                    'COMPARE_NOTEQUAL': '#/definitions/ComparisonExpression',
                    'COMPARE_NOT_DISTINCT_FROM': '#/definitions/ComparisonExpression',
                    'COMPARE_NOT_IN': '#/definitions/OperatorExpression',
                    'CONJUNCTION_AND': '#/definitions/ConjunctionExpression',
                    'CONJUNCTION_OR': '#/definitions/ConjunctionExpression',
                    'FUNCTION': '#/definitions/FunctionExpression',
                    'OPERATOR_CAST': '#/definitions/CastExpression',
                    'OPERATOR_IN': '#/definitions/OperatorExpression',
                    'OPERATOR_IS_NOT_NULL': '#/definitions/OperatorExpression',
                    'OPERATOR_IS_NULL': '#/definitions/OperatorExpression',
                    'OPERATOR_NOT': '#/definitions/OperatorExpression',
                    'STAR': '#/definitions/StarExpression',
                    'STRUCT_EXTRACT': '#/definitions/OperatorExpression',
                    'SUBQUERY': '#/definitions/SubqueryExpression',
                    'VALUE_CONSTANT': '#/definitions/ConstantExpression',
                    'WINDOW_AGGREGATE': '#/definitions/WindowExpression',
                    'WINDOW_CUME_DIST': '#/definitions/WindowExpression',
                    'WINDOW_FIRST_VALUE': '#/definitions/WindowExpression',
                    'WINDOW_LAG': '#/definitions/WindowExpression',
                    'WINDOW_LAST_VALUE': '#/definitions/WindowExpression',
                    'WINDOW_LEAD': '#/definitions/WindowExpression',
                    'WINDOW_NTH_VALUE': '#/definitions/WindowExpression',
                    'WINDOW_NTILE': '#/definitions/WindowExpression',
                    'WINDOW_PERCENT_RANK': '#/definitions/WindowExpression',
                    'WINDOW_RANK': '#/definitions/WindowExpression',
                    'WINDOW_RANK_DENSE': '#/definitions/WindowExpression',
                    'WINDOW_ROW_NUMBER': '#/definitions/WindowExpression'
                },
                'propertyName': 'type'
            },
            'oneOf': [
                {
                    '$ref': '#/definitions/FunctionExpression'
                },
                {
                    '$ref': '#/definitions/ColumnRefExpression'
                },
                {
                    '$ref': '#/definitions/StarExpression'
                },
                {
                    '$ref': '#/definitions/ConstantExpression'
                },
                {
                    '$ref': '#/definitions/CastExpression'
                },
                {
                    '$ref': '#/definitions/ComparisonExpression'
                },
                {
                    '$ref': '#/definitions/ConjunctionExpression'
                },
                {
                    '$ref': '#/definitions/SubqueryExpression'
                },
                {
                    '$ref': '#/definitions/OperatorExpression'
                },
                {
                    '$ref': '#/definitions/CaseExpression'
                },
                {
                    '$ref': '#/definitions/CollateExpression'
                },
                {
                    '$ref': '#/definitions/BetweenExpression'
                },
                {
                    '$ref': '#/definitions/WindowExpression'
                }
            ],
            'title': 'ParsedExpressionSubclasses'
        },
        'QueryNodeSubclasses': {
            'additionalProperties': False,
            'description': 'Union of QueryNode subclasses',
            'discriminator': {
                'mapping': {
                    'RECURSIVE_CTE_NODE': '#/definitions/RecursiveCTENode',
                    'SELECT_NODE': '#/definitions/SelectNode',
                    'SET_OPERATION_NODE': '#/definitions/SetOperationNode'
                },
                'propertyName': 'type'
            },
            'oneOf': [
                {
                    '$ref': '#/definitions/SelectNode'
                },
                {
                    '$ref': '#/definitions/SetOperationNode'
                },
                {
                    '$ref': '#/definitions/RecursiveCTENode'
                }
            ],
            'title': 'QueryNodeSubclasses'
        },
        'RecursiveCTENode': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/query_node/recursive_cte_node.hpp#L17',
            'properties': {
                'aliases': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Aliases',
                    'type': 'array'
                },
                'cte_map': {
                    '$ref': '#/definitions/CommonTableExpressionMap'
                },
                'cte_name': {
                    'title': 'Cte Name',
                    'type': 'string'
                },
                'left': {
                    '$ref': '#/definitions/QueryNodeSubclasses'
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/definitions/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'right': {
                    '$ref': '#/definitions/QueryNodeSubclasses'
                },
                'type': {
                    'enum': [
                        'RECURSIVE_CTE_NODE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'union_all': {
                    'title': 'Union All',
                    'type': 'boolean'
                }
            },
            'required': [
                'type',
                'modifiers',
                'cte_map',
                'cte_name',
                'union_all',
                'left',
                'right',
                'aliases'
            ],
            'title': 'RecursiveCTENode',
            'type': 'object'
        },
        'ResultModifierSubclasses': {
            'additionalProperties': False,
            'description': 'Union of ResultModifier subclasses',
            'discriminator': {
                'mapping': {
                    'DISTINCT_MODIFIER': '#/definitions/DistinctModifier',
                    'LIMIT_MODIFIER': '#/definitions/LimitModifier',
                    'LIMIT_PERCENT_MODIFIER': '#/definitions/LimitPercentModifier',
                    'ORDER_MODIFIER': '#/definitions/OrderModifier'
                },
                'propertyName': 'type'
            },
            'oneOf': [
                {
                    '$ref': '#/definitions/LimitPercentModifier'
                },
                {
                    '$ref': '#/definitions/DistinctModifier'
                },
                {
                    '$ref': '#/definitions/LimitModifier'
                },
                {
                    '$ref': '#/definitions/OrderModifier'
                }
            ],
            'title': 'ResultModifierSubclasses'
        },
        'Root': {
            'additionalProperties': False,
            'description': 'Union of possible responses',
            'discriminator': {
                'mapping': {
                    False: '#/definitions/SuccessResponse',
                    True: '#/definitions/ErrorResponse'
                },
                'propertyName': 'error'
            },
            'oneOf': [
                {
                    '$ref': '#/definitions/ErrorResponse'
                },
                {
                    '$ref': '#/definitions/SuccessResponse'
                }
            ],
            'title': 'Root'
        },
        'SampleMethod': {
            'description': 'src/include/duckdb/parser/parsed_data/sample_options.hpp#L18',
            'enum': [
                'System',
                'Bernoulli',
                'Reservoir'
            ],
            'title': 'SampleMethod'
        },
        'SampleOptions': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/parsed_data/sample_options.hpp#L22',
            'properties': {
                'is_percentage': {
                    'title': 'Is Percentage',
                    'type': 'boolean'
                },
                'method': {
                    '$ref': '#/definitions/SampleMethod'
                },
                'sample_size': {
                    '$ref': '#/definitions/Value'
                },
                'seed': {
                    'default': -1,
                    'title': 'Seed',
                    'type': 'integer'
                }
            },
            'required': [
                'sample_size',
                'is_percentage',
                'method'
            ],
            'title': 'SampleOptions',
            'type': 'object'
        },
        'SelectNode': {
            'additionalProperties': False,
            'description': '''SelectNode represents a standard SELECT statement
src/include/duckdb/parser/query_node/select_node.hpp#L22''',
            'properties': {
                'aggregate_handling': {
                    '$ref': '#/definitions/AggregateHandling'
                },
                'cte_map': {
                    '$ref': '#/definitions/CommonTableExpressionMap'
                },
                'from_table': {
                    '$ref': '#/definitions/TableRefSubclasses'
                },
                'group_expressions': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Group Expressions',
                    'type': 'array'
                },
                'group_sets': {
                    'items': {
                        'items': {
                            'type': 'integer'
                        },
                        'type': 'array',
                        'uniqueItems': True
                    },
                    'title': 'Group Sets',
                    'type': 'array'
                },
                'having': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/definitions/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'qualify': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'select_list': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Select List',
                    'type': 'array'
                },
                'type': {
                    'enum': [
                        'SELECT_NODE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'where_clause': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                }
            },
            'required': [
                'type',
                'modifiers',
                'cte_map',
                'select_list',
                'from_table'
            ],
            'title': 'SelectNode',
            'type': 'object'
        },
        'SelectStatement': {
            'additionalProperties': False,
            'description': '''SelectStatement is a typical SELECT clause
src/include/duckdb/parser/statement/select_statement.hpp#L24''',
            'properties': {
                'node': {
                    '$ref': '#/definitions/QueryNodeSubclasses'
                }
            },
            'required': [
                'node'
            ],
            'title': 'SelectStatement',
            'type': 'object'
        },
        'SetOperationNode': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/query_node/set_operation_node.hpp#L18',
            'properties': {
                'cte_map': {
                    '$ref': '#/definitions/CommonTableExpressionMap'
                },
                'left': {
                    '$ref': '#/definitions/QueryNodeSubclasses'
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/definitions/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'right': {
                    '$ref': '#/definitions/QueryNodeSubclasses'
                },
                'setop_type': {
                    'enum': [
                        'NONE',
                        'UNION',
                        'EXCEPT',
                        'INTERSECT',
                        'UNION_BY_NAME'
                    ],
                    'title': 'Setop Type',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'SET_OPERATION_NODE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'modifiers',
                'cte_map',
                'setop_type',
                'left',
                'right'
            ],
            'title': 'SetOperationNode',
            'type': 'object'
        },
        'StarExpression': {
            'additionalProperties': False,
            'description': '''Represents a * expression in the SELECT clause
src/include/duckdb/parser/expression/star_expression.hpp#L17''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'enum': [
                        'STAR'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'columns': {
                    'title': 'Columns',
                    'type': 'boolean'
                },
                'exclude_list': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Exclude List',
                    'type': 'array'
                },
                'expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'relation_name': {
                    'title': 'Relation Name',
                    'type': 'string'
                },
                'replace_list': {
                    '$ref': '#/definitions/OrderedDict_str__ParsedExpressionSubclasses_'
                },
                'type': {
                    'enum': [
                        'STAR'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'columns',
                'replace_list',
                'relation_name',
                'exclude_list'
            ],
            'title': 'StarExpression',
            'type': 'object'
        },
        'StructTypeInfo': {
            'additionalProperties': False,
            'description': '''Struct Type
src/common/types.cpp#L1040''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    '$ref': '#/definitions/TypeCatalogEntry'
                },
                'child_types': {
                    '$ref': '#/definitions/OrderedDict_str__LogicalType_'
                },
                'type': {
                    'enum': [
                        'STRUCT_TYPE_INFO'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'alias',
                'child_types'
            ],
            'title': 'StructTypeInfo',
            'type': 'object'
        },
        'SubqueryExpression': {
            'additionalProperties': False,
            'description': '''Represents a subquery
src/include/duckdb/parser/expression/subquery_expression.hpp#L18''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'child': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'class': {
                    'enum': [
                        'SUBQUERY'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'comparison_type': {
                    'enum': [
                        'INVALID',
                        'COMPARE_EQUAL'
                    ],
                    'title': 'Comparison Type',
                    'type': 'string'
                },
                'subquery': {
                    '$ref': '#/definitions/SelectStatement'
                },
                'subquery_type': {
                    'enum': [
                        'SCALAR',
                        'ANY',
                        'EXISTS',
                        'INVALID',
                        'NOT_EXISTS'
                    ],
                    'title': 'Subquery Type',
                    'type': 'string'
                },
                'type': {
                    'enum': [
                        'SUBQUERY'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'comparison_type',
                'subquery',
                'subquery_type'
            ],
            'title': 'SubqueryExpression',
            'type': 'object'
        },
        'SubqueryRef': {
            'additionalProperties': False,
            'description': '''Represents a subquery
src/include/duckdb/parser/tableref/subqueryref.hpp#L16''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'column_name_alias': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Column Name Alias',
                    'type': 'array'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'subquery': {
                    '$ref': '#/definitions/SelectStatement'
                },
                'type': {
                    'enum': [
                        'SUBQUERY'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'alias',
                'type',
                'subquery',
                'column_name_alias'
            ],
            'title': 'SubqueryRef',
            'type': 'object'
        },
        'SuccessResponse': {
            'additionalProperties': False,
            'description': 'Returned when parsing succeeds',
            'properties': {
                'error': {
                    'enum': [
                        False
                    ],
                    'title': 'Error',
                    'type': 'boolean'
                },
                'statements': {
                    'items': {
                        '$ref': '#/definitions/SelectStatement'
                    },
                    'title': 'Statements',
                    'type': 'array'
                }
            },
            'required': [
                'error',
                'statements'
            ],
            'title': 'SuccessResponse',
            'type': 'object'
        },
        'TableFunctionRef': {
            'additionalProperties': False,
            'description': '''Represents a Table producing function
src/include/duckdb/parser/tableref/table_function_ref.hpp#L19''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'column_name_alias': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Column Name Alias',
                    'type': 'array'
                },
                'function': {
                    '$ref': '#/definitions/FunctionExpression'
                },
                'sample': {
                    '$ref': '#/definitions/SampleOptions'
                },
                'type': {
                    'enum': [
                        'TABLE_FUNCTION'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'alias',
                'type',
                'function'
            ],
            'title': 'TableFunctionRef',
            'type': 'object'
        },
        'TableRefSubclasses': {
            'additionalProperties': False,
            'description': 'Union of TableRef subclasses',
            'discriminator': {
                'mapping': {
                    'BASE_TABLE': '#/definitions/BaseTableRef',
                    'EMPTY': '#/definitions/EmptyTableRef',
                    'JOIN': '#/definitions/JoinRef',
                    'SUBQUERY': '#/definitions/SubqueryRef',
                    'TABLE_FUNCTION': '#/definitions/TableFunctionRef'
                },
                'propertyName': 'type'
            },
            'oneOf': [
                {
                    '$ref': '#/definitions/BaseTableRef'
                },
                {
                    '$ref': '#/definitions/EmptyTableRef'
                },
                {
                    '$ref': '#/definitions/TableFunctionRef'
                },
                {
                    '$ref': '#/definitions/SubqueryRef'
                },
                {
                    '$ref': '#/definitions/JoinRef'
                }
            ],
            'title': 'TableRefSubclasses'
        },
        'TypeCatalogEntry': {
            'additionalProperties': False,
            'description': '''A type catalog entry
src/include/duckdb/catalog/catalog_entry/type_catalog_entry.hpp#L20''',
            'properties': {
                'user_type': {
                    '$ref': '#/definitions/LogicalType'
                }
            },
            'required': [
                'user_type'
            ],
            'title': 'TypeCatalogEntry',
            'type': 'object'
        },
        'UserTypeInfo': {
            'additionalProperties': False,
            'description': '''User Type
src/common/types.cpp#L1263''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    '$ref': '#/definitions/TypeCatalogEntry'
                },
                'type': {
                    'enum': [
                        'USER_TYPE_INFO'
                    ],
                    'title': 'Type',
                    'type': 'string'
                },
                'user_type_name': {
                    'title': 'User Type Name',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'alias',
                'user_type_name'
            ],
            'title': 'UserTypeInfo',
            'type': 'object'
        },
        'Value': {
            'additionalProperties': False,
            'description': '''The Value object holds a single arbitrary value of any type that can be
stored in the database.
src/include/duckdb/common/types/value.hpp#L30''',
            'properties': {
                'is_null': {
                    'title': 'Is Null',
                    'type': 'boolean'
                },
                'type': {
                    '$ref': '#/definitions/LogicalType'
                },
                'value': {
                    'title': 'Value'
                }
            },
            'required': [
                'type',
                'is_null'
            ],
            'title': 'Value',
            'type': 'object'
        },
        'WindowBoundary': {
            'description': 'src/include/duckdb/parser/expression/window_expression.hpp#L16',
            'enum': [
                'INVALID',
                'UNBOUNDED_PRECEDING',
                'UNBOUNDED_FOLLOWING',
                'CURRENT_ROW_RANGE',
                'CURRENT_ROW_ROWS',
                'EXPR_PRECEDING_ROWS',
                'EXPR_FOLLOWING_ROWS',
                'EXPR_PRECEDING_RANGE',
                'EXPR_FOLLOWING_RANGE'
            ],
            'title': 'WindowBoundary'
        },
        'WindowExpression': {
            'additionalProperties': False,
            'description': '''The WindowExpression represents a window function in the query. They are a special case of aggregates which is why
they inherit from them.
src/include/duckdb/parser/expression/window_expression.hpp#L32''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog': {
                    'title': 'Catalog',
                    'type': 'string'
                },
                'children': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'enum': [
                        'WINDOW'
                    ],
                    'title': 'Class',
                    'type': 'string'
                },
                'default_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'end': {
                    'allOf': [
                        {
                            '$ref': '#/definitions/WindowBoundary'
                        }
                    ],
                    'default': 'INVALID'
                },
                'end_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'filter_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'function_name': {
                    'title': 'Function Name',
                    'type': 'string'
                },
                'ignore_nulls': {
                    'title': 'Ignore Nulls',
                    'type': 'boolean'
                },
                'offset_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'orders': {
                    'items': {
                        '$ref': '#/definitions/OrderByNode'
                    },
                    'title': 'Orders',
                    'type': 'array'
                },
                'partitions': {
                    'items': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Partitions',
                    'type': 'array'
                },
                'schema': {
                    'title': 'Schema',
                    'type': 'string'
                },
                'start': {
                    'allOf': [
                        {
                            '$ref': '#/definitions/WindowBoundary'
                        }
                    ],
                    'default': 'INVALID'
                },
                'start_expr': {
                    '$ref': '#/definitions/ParsedExpressionSubclasses'
                },
                'type': {
                    'enum': [
                        'WINDOW_AGGREGATE',
                        'WINDOW_ROW_NUMBER',
                        'WINDOW_FIRST_VALUE',
                        'WINDOW_LAST_VALUE',
                        'WINDOW_NTH_VALUE',
                        'WINDOW_RANK',
                        'WINDOW_RANK_DENSE',
                        'WINDOW_PERCENT_RANK',
                        'WINDOW_CUME_DIST',
                        'WINDOW_LEAD',
                        'WINDOW_LAG',
                        'WINDOW_NTILE'
                    ],
                    'title': 'Type',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'catalog',
                'schema',
                'function_name',
                'children',
                'partitions',
                'orders',
                'ignore_nulls'
            ],
            'title': 'WindowExpression',
            'type': 'object'
        }
    },
    'title': 'ParsingModel[Root]'
}
