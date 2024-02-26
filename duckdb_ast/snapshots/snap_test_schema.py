# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_generation 1'] = {
    '$defs': {
        'AggregateHandling': {
            'description': 'src/include/duckdb/common/enums/aggregate_handling.hpp#L16',
            'enum': [
                'STANDARD_HANDLING',
                'NO_AGGREGATES_ALLOWED',
                'FORCE_AGGREGATES'
            ],
            'title': 'AggregateHandling',
            'type': 'string'
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
                    'anyOf': [
                        {
                            'items': {
                                'type': 'string'
                            },
                            'type': 'array'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Column Name Alias'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
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
                    'const': 'BASE_TABLE',
                    'title': 'Type'
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
                    'const': 'BETWEEN',
                    'title': 'Class'
                },
                'input': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'lower': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'COMPARE_BETWEEN',
                    'title': 'Type'
                },
                'upper': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
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
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'then_expr': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'when_expr': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
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
                        '$ref': '#/$defs/CaseCheck'
                    },
                    'title': 'Case Checks',
                    'type': 'array'
                },
                'class': {
                    'const': 'CASE',
                    'title': 'Class'
                },
                'else_expr': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'CASE_EXPR',
                    'title': 'Type'
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
                    '$ref': '#/$defs/LogicalType'
                },
                'child': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'class': {
                    'const': 'CAST',
                    'title': 'Class'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'try_cast': {
                    'title': 'Try Cast',
                    'type': 'boolean'
                },
                'type': {
                    'const': 'OPERATOR_CAST',
                    'title': 'Type'
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
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'class': {
                    'const': 'COLLATE',
                    'title': 'Class'
                },
                'collation': {
                    'title': 'Collation',
                    'type': 'string'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'COLLATE',
                    'title': 'Type'
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
                    'const': 'COLUMN_REF',
                    'title': 'Class'
                },
                'column_names': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Column Names',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'COLUMN_REF',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/parser/common_table_expression_info.hpp#L18',
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
                    '$ref': '#/$defs/SelectStatement'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
                    '$ref': '#/$defs/OrderedDict_str_CommonTableExpressionInfo_'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
                    'const': 'COMPARISON',
                    'title': 'Class'
                },
                'left': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'right': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
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
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'const': 'CONJUNCTION',
                    'title': 'Class'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
                    'const': 'CONSTANT',
                    'title': 'Class'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'VALUE_CONSTANT',
                    'title': 'Type'
                },
                'value': {
                    '$ref': '#/$defs/Value'
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
            'description': 'src/include/duckdb/common/extra_type_info.hpp#L66',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/TypeCatalogEntry'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'scale': {
                    'title': 'Scale',
                    'type': 'integer'
                },
                'type': {
                    'const': 'DECIMAL_TYPE_INFO',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L144',
            'properties': {
                'distinct_on_targets': {
                    'items': {
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Distinct On Targets',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'DISTINCT_MODIFIER',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/parser/tableref/emptytableref.hpp#L15',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'type': {
                    'const': 'EMPTY',
                    'title': 'Type'
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
                    'const': True,
                    'title': 'Error'
                },
                'error_message': {
                    'title': 'Error Message',
                    'type': 'string'
                },
                'error_type': {
                    'title': 'Error Type',
                    'type': 'string'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
        'FirstSecond_str_LogicalType_': {
            'properties': {
                'first': {
                    'title': 'First',
                    'type': 'string'
                },
                'second': {
                    '$ref': '#/$defs/LogicalType'
                }
            },
            'required': [
                'first',
                'second'
            ],
            'title': 'FirstSecond[str, LogicalType]',
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
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'const': 'FUNCTION',
                    'title': 'Class'
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
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
                    '$ref': '#/$defs/OrderModifier'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'schema': {
                    'title': 'Schema',
                    'type': 'string'
                },
                'type': {
                    'const': 'FUNCTION',
                    'title': 'Type'
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'join_type': {
                    'enum': [
                        'INVALID',
                        'LEFT',
                        'RIGHT',
                        'INNER',
                        'OUTER',
                        'SEMI',
                        'ANTI',
                        'MARK',
                        'SINGLE'
                    ],
                    'title': 'Join Type',
                    'type': 'string'
                },
                'left': {
                    '$ref': '#/$defs/TableRefSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'ref_type': {
                    'enum': [
                        'CROSS',
                        'ASOF',
                        'NATURAL',
                        'REGULAR',
                        'DEPENDENT',
                        'POSITIONAL'
                    ],
                    'title': 'Ref Type',
                    'type': 'string'
                },
                'right': {
                    '$ref': '#/$defs/TableRefSubclasses'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'type': {
                    'const': 'JOIN',
                    'title': 'Type'
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
        'LambdaExpression': {
            'additionalProperties': False,
            'description': '''LambdaExpression represents either:
1. A lambda operator that can be used for e.g. mapping an expression to a list
2. An OperatorExpression with the "->" operator
Lambda expressions are written in the form of "params -> expr", e.g. "x -> x + 1"
src/include/duckdb/parser/expression/lambda_expression.hpp#L20''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'const': 'LAMBDA',
                    'title': 'Class'
                },
                'expr': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'lhs': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'LAMBDA',
                    'title': 'Type'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'lhs',
                'expr'
            ],
            'title': 'LambdaExpression',
            'type': 'object'
        },
        'LimitModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L98',
            'properties': {
                'limit': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'offset': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'LIMIT_MODIFIER',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L165',
            'properties': {
                'limit': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'offset': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'LIMIT_PERCENT_MODIFIER',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/common/extra_type_info.hpp#L105',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/TypeCatalogEntry'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'child_type': {
                    '$ref': '#/$defs/LogicalType'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'LIST_TYPE_INFO',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/common/types.hpp#L238',
            'properties': {
                'id': {
                    '$ref': '#/$defs/LogicalTypeId'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type_info': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ListTypeInfo'
                        },
                        {
                            '$ref': '#/$defs/DecimalTypeInfo'
                        },
                        {
                            '$ref': '#/$defs/UserTypeInfo'
                        },
                        {
                            '$ref': '#/$defs/StructTypeInfo'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'title': 'Type Info'
                }
            },
            'required': [
                'id',
                'type_info'
            ],
            'title': 'LogicalType',
            'type': 'object'
        },
        'LogicalTypeId': {
            'description': '''SQL Types
src/include/duckdb/common/types.hpp#L186''',
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
            'title': 'LogicalTypeId',
            'type': 'string'
        },
        'OperatorExpression': {
            'additionalProperties': False,
            'description': '''Represents a built-in operator expression
src/include/duckdb/parser/expression/operator_expression.hpp#L19''',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'children': {
                    'items': {
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'const': 'OPERATOR',
                    'title': 'Class'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
src/include/duckdb/parser/result_modifier.hpp#L77''',
            'properties': {
                'expression': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                },
                'null_order': {
                    '$ref': '#/$defs/OrderByNullType'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    '$ref': '#/$defs/OrderType'
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
            'title': 'OrderByNullType',
            'type': 'string'
        },
        'OrderModifier': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/result_modifier.hpp#L121',
            'properties': {
                'orders': {
                    'items': {
                        '$ref': '#/$defs/OrderByNode'
                    },
                    'title': 'Orders',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'ORDER_MODIFIER',
                    'title': 'Type'
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
            'title': 'OrderType',
            'type': 'string'
        },
        'OrderedDict_str_CommonTableExpressionInfo_': {
            'items': {
                '$ref': '#/$defs/Pair_str_CommonTableExpressionInfo_'
            },
            'title': 'OrderedDict[str, CommonTableExpressionInfo]',
            'type': 'array'
        },
        'OrderedDict_str_ParsedExpressionSubclasses_': {
            'items': {
                '$ref': '#/$defs/Pair_str_ParsedExpressionSubclasses_'
            },
            'title': 'OrderedDict[str, ParsedExpressionSubclasses]',
            'type': 'array'
        },
        'Pair_str_CommonTableExpressionInfo_': {
            'properties': {
                'key': {
                    'title': 'Key',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/$defs/CommonTableExpressionInfo'
                }
            },
            'required': [
                'key',
                'value'
            ],
            'title': 'Pair[str, CommonTableExpressionInfo]',
            'type': 'object'
        },
        'Pair_str_ParsedExpressionSubclasses_': {
            'properties': {
                'key': {
                    'title': 'Key',
                    'type': 'string'
                },
                'value': {
                    '$ref': '#/$defs/ParsedExpressionSubclasses'
                }
            },
            'required': [
                'key',
                'value'
            ],
            'title': 'Pair[str, ParsedExpressionSubclasses]',
            'type': 'object'
        },
        'ParameterExpression': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/expression/parameter_expression.hpp#L30',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'const': 'PARAMETER',
                    'title': 'Class'
                },
                'identifier': {
                    'title': 'Identifier',
                    'type': 'string'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'VALUE_PARAMETER',
                    'title': 'Type'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'identifier'
            ],
            'title': 'ParameterExpression',
            'type': 'object'
        },
        'ParsedExpressionSubclasses': {
            'anyOf': [
                {
                    '$ref': '#/$defs/FunctionExpression'
                },
                {
                    '$ref': '#/$defs/ColumnRefExpression'
                },
                {
                    '$ref': '#/$defs/StarExpression'
                },
                {
                    '$ref': '#/$defs/ConstantExpression'
                },
                {
                    '$ref': '#/$defs/CastExpression'
                },
                {
                    '$ref': '#/$defs/ComparisonExpression'
                },
                {
                    '$ref': '#/$defs/ConjunctionExpression'
                },
                {
                    '$ref': '#/$defs/LambdaExpression'
                },
                {
                    '$ref': '#/$defs/ParameterExpression'
                },
                {
                    '$ref': '#/$defs/PositionalReferenceExpression'
                },
                {
                    '$ref': '#/$defs/SubqueryExpression'
                },
                {
                    '$ref': '#/$defs/OperatorExpression'
                },
                {
                    '$ref': '#/$defs/CaseExpression'
                },
                {
                    '$ref': '#/$defs/CollateExpression'
                },
                {
                    '$ref': '#/$defs/BetweenExpression'
                },
                {
                    '$ref': '#/$defs/WindowExpression'
                }
            ],
            'description': 'Union of ParsedExpression subclasses',
            'title': 'ParsedExpressionSubclasses'
        },
        'PositionalReferenceExpression': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/expression/positional_reference_expression.hpp#L14',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'class': {
                    'const': 'POSITIONAL_REFERENCE',
                    'title': 'Class'
                },
                'index': {
                    'title': 'Index',
                    'type': 'integer'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'POSITIONAL_REFERENCE',
                    'title': 'Type'
                }
            },
            'required': [
                'type',
                'class',
                'alias',
                'index'
            ],
            'title': 'PositionalReferenceExpression',
            'type': 'object'
        },
        'QueryNodeSubclasses': {
            'anyOf': [
                {
                    '$ref': '#/$defs/SelectNode'
                },
                {
                    '$ref': '#/$defs/SetOperationNode'
                },
                {
                    '$ref': '#/$defs/RecursiveCTENode'
                }
            ],
            'description': 'Union of QueryNode subclasses',
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
                    '$ref': '#/$defs/CommonTableExpressionMap'
                },
                'cte_name': {
                    'title': 'Cte Name',
                    'type': 'string'
                },
                'left': {
                    '$ref': '#/$defs/QueryNodeSubclasses'
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/$defs/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'right': {
                    '$ref': '#/$defs/QueryNodeSubclasses'
                },
                'type': {
                    'const': 'RECURSIVE_CTE_NODE',
                    'title': 'Type'
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
            'anyOf': [
                {
                    '$ref': '#/$defs/LimitPercentModifier'
                },
                {
                    '$ref': '#/$defs/DistinctModifier'
                },
                {
                    '$ref': '#/$defs/LimitModifier'
                },
                {
                    '$ref': '#/$defs/OrderModifier'
                }
            ],
            'description': 'Union of ResultModifier subclasses',
            'title': 'ResultModifierSubclasses'
        },
        'SampleMethod': {
            'description': 'src/include/duckdb/parser/parsed_data/sample_options.hpp#L18',
            'enum': [
                'System',
                'Bernoulli',
                'Reservoir'
            ],
            'title': 'SampleMethod',
            'type': 'string'
        },
        'SampleOptions': {
            'additionalProperties': False,
            'description': 'src/include/duckdb/parser/parsed_data/sample_options.hpp#L23',
            'properties': {
                'is_percentage': {
                    'title': 'Is Percentage',
                    'type': 'boolean'
                },
                'method': {
                    '$ref': '#/$defs/SampleMethod'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample_size': {
                    '$ref': '#/$defs/Value'
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/AggregateHandling'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'cte_map': {
                    '$ref': '#/$defs/CommonTableExpressionMap'
                },
                'from_table': {
                    '$ref': '#/$defs/TableRefSubclasses'
                },
                'group_expressions': {
                    'anyOf': [
                        {
                            'items': {
                                '$ref': '#/$defs/ParsedExpressionSubclasses'
                            },
                            'type': 'array'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Group Expressions'
                },
                'group_sets': {
                    'anyOf': [
                        {
                            'items': {
                                'items': {
                                    'type': 'integer'
                                },
                                'type': 'array',
                                'uniqueItems': True
                            },
                            'type': 'array'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Group Sets'
                },
                'having': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/$defs/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'qualify': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'select_list': {
                    'items': {
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Select List',
                    'type': 'array'
                },
                'type': {
                    'const': 'SELECT_NODE',
                    'title': 'Type'
                },
                'where_clause': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
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
                    '$ref': '#/$defs/QueryNodeSubclasses'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
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
                    '$ref': '#/$defs/CommonTableExpressionMap'
                },
                'left': {
                    '$ref': '#/$defs/QueryNodeSubclasses'
                },
                'modifiers': {
                    'items': {
                        '$ref': '#/$defs/ResultModifierSubclasses'
                    },
                    'title': 'Modifiers',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'right': {
                    '$ref': '#/$defs/QueryNodeSubclasses'
                },
                'setop_all': {
                    'default': True,
                    'title': 'Setop All',
                    'type': 'boolean'
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
                    'const': 'SET_OPERATION_NODE',
                    'title': 'Type'
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
                    'const': 'STAR',
                    'title': 'Class'
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'relation_name': {
                    'title': 'Relation Name',
                    'type': 'string'
                },
                'replace_list': {
                    '$ref': '#/$defs/OrderedDict_str_ParsedExpressionSubclasses_'
                },
                'type': {
                    'const': 'STAR',
                    'title': 'Type'
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
            'description': 'src/include/duckdb/common/extra_type_info.hpp#L124',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/TypeCatalogEntry'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'child_types': {
                    'items': {
                        '$ref': '#/$defs/FirstSecond_str_LogicalType_'
                    },
                    'title': 'Child Types',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    'const': 'STRUCT_TYPE_INFO',
                    'title': 'Type'
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'class': {
                    'const': 'SUBQUERY',
                    'title': 'Class'
                },
                'comparison_type': {
                    'enum': [
                        'INVALID',
                        'COMPARE_EQUAL'
                    ],
                    'title': 'Comparison Type',
                    'type': 'string'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'subquery': {
                    '$ref': '#/$defs/SelectStatement'
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
                    'const': 'SUBQUERY',
                    'title': 'Type'
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
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'subquery': {
                    '$ref': '#/$defs/SelectStatement'
                },
                'type': {
                    'const': 'SUBQUERY',
                    'title': 'Type'
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
                    'const': False,
                    'title': 'Error'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'statements': {
                    'items': {
                        '$ref': '#/$defs/SelectStatement'
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
                    'anyOf': [
                        {
                            'items': {
                                'type': 'string'
                            },
                            'type': 'array'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Column Name Alias'
                },
                'function': {
                    '$ref': '#/$defs/FunctionExpression'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'sample': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/SampleOptions'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'type': {
                    'const': 'TABLE_FUNCTION',
                    'title': 'Type'
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
            'anyOf': [
                {
                    '$ref': '#/$defs/BaseTableRef'
                },
                {
                    '$ref': '#/$defs/EmptyTableRef'
                },
                {
                    '$ref': '#/$defs/TableFunctionRef'
                },
                {
                    '$ref': '#/$defs/SubqueryRef'
                },
                {
                    '$ref': '#/$defs/JoinRef'
                }
            ],
            'description': 'Union of TableRef subclasses',
            'title': 'TableRefSubclasses'
        },
        'TypeCatalogEntry': {
            'additionalProperties': False,
            'description': '''A type catalog entry
src/include/duckdb/catalog/catalog_entry/type_catalog_entry.hpp#L20''',
            'properties': {
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'user_type': {
                    '$ref': '#/$defs/LogicalType'
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
            'description': 'src/include/duckdb/common/extra_type_info.hpp#L163',
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog': {
                    'title': 'Catalog',
                    'type': 'string'
                },
                'catalog_entry': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/TypeCatalogEntry'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'schema': {
                    'title': 'Schema',
                    'type': 'string'
                },
                'type': {
                    'const': 'USER_TYPE_INFO',
                    'title': 'Type'
                },
                'user_type_name': {
                    'title': 'User Type Name',
                    'type': 'string'
                }
            },
            'required': [
                'type',
                'alias',
                'user_type_name',
                'schema',
                'catalog'
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
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'type': {
                    '$ref': '#/$defs/LogicalType'
                },
                'value': {
                    'anyOf': [
                        {
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
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
            'title': 'WindowBoundary',
            'type': 'string'
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
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Children',
                    'type': 'array'
                },
                'class': {
                    'const': 'WINDOW',
                    'title': 'Class'
                },
                'default_expr': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'end': {
                    'allOf': [
                        {
                            '$ref': '#/$defs/WindowBoundary'
                        }
                    ],
                    'default': 'INVALID'
                },
                'end_expr': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'filter_expr': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
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
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
                },
                'orders': {
                    'items': {
                        '$ref': '#/$defs/OrderByNode'
                    },
                    'title': 'Orders',
                    'type': 'array'
                },
                'partitions': {
                    'items': {
                        '$ref': '#/$defs/ParsedExpressionSubclasses'
                    },
                    'title': 'Partitions',
                    'type': 'array'
                },
                'query_location': {
                    'anyOf': [
                        {
                            'type': 'integer'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None,
                    'title': 'Query Location'
                },
                'schema': {
                    'title': 'Schema',
                    'type': 'string'
                },
                'start': {
                    'allOf': [
                        {
                            '$ref': '#/$defs/WindowBoundary'
                        }
                    ],
                    'default': 'INVALID'
                },
                'start_expr': {
                    'anyOf': [
                        {
                            '$ref': '#/$defs/ParsedExpressionSubclasses'
                        },
                        {
                            'type': 'null'
                        }
                    ],
                    'default': None
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
    'description': 'Union of possible responses',
    'discriminator': {
        'mapping': {
            'False': '#/$defs/SuccessResponse',
            'True': '#/$defs/ErrorResponse'
        },
        'propertyName': 'error'
    },
    'oneOf': [
        {
            '$ref': '#/$defs/ErrorResponse'
        },
        {
            '$ref': '#/$defs/SuccessResponse'
        }
    ],
    'title': 'Root'
}
