# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_generation 1'] = {
    '$ref': '#/definitions/Root',
    'definitions': {
        'AggregrateHandling': {
            'description': 'An enumeration.',
            'enum': [
                'STANDARD_HANDLING'
            ],
            'title': 'AggregrateHandling'
        },
        'BaseTableRef': {
            'additionalProperties': False,
            'description': 'https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/tableref/basetableref.hpp',
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
        'CaseCheck': {
            'additionalProperties': False,
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
                        'CASE'
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
            'description': 'https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/cast_expression.hpp#L22-L26',
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
                        'CAST'
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
            'description': 'https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/columnref_expression.hpp#L28',
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
        'ComparisonExpression': {
            'additionalProperties': False,
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
                        'GREATERTHAN',
                        'EQUAL',
                        'GREATERTHANOREQUALTO'
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
                        'AND',
                        'OR'
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
                        'CONSTANT'
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
        'EmptyTableRef': {
            'additionalProperties': False,
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
        'ListTypeInfo': {
            'additionalProperties': False,
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
            'description': 'An enumeration.',
            'enum': [
                'BOOLEAN',
                'VARCHAR',
                'LIST',
                'STRUCT',
                'UNION',
                'DECIMAL',
                'USER',
                'DOUBLE',
                'BIT',
                'BLOB',
                'NULL',
                'TINYINT',
                'SMALLINT',
                'INTEGER',
                'BIGINT',
                'HUGEINT',
                'UTINYINT',
                'USMALLINT',
                'UINTEGER',
                'UBIGINT',
                'DATE',
                'TIMESTAMP',
                'TIMESTAMP WITH TIME ZONE'
            ],
            'title': 'LogicalTypeId'
        },
        'OperatorExpression': {
            'additionalProperties': False,
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
                        'IS_NULL'
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
        'OrderModifier': {
            'additionalProperties': False,
            'properties': {
                'orders': {
                    'items': {
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
        'ParsedExpressionSubclasses': {
            'additionalProperties': False,
            'discriminator': {
                'mapping': {
                    'AND': '#/definitions/ConjunctionExpression',
                    'CASE': '#/definitions/CaseExpression',
                    'CAST': '#/definitions/CastExpression',
                    'COLLATE': '#/definitions/CollateExpression',
                    'COLUMN_REF': '#/definitions/ColumnRefExpression',
                    'CONSTANT': '#/definitions/ConstantExpression',
                    'EQUAL': '#/definitions/ComparisonExpression',
                    'FUNCTION': '#/definitions/FunctionExpression',
                    'GREATERTHAN': '#/definitions/ComparisonExpression',
                    'GREATERTHANOREQUALTO': '#/definitions/ComparisonExpression',
                    'IS_NULL': '#/definitions/OperatorExpression',
                    'OR': '#/definitions/ConjunctionExpression',
                    'STAR': '#/definitions/StarExpression',
                    'SUBQUERY': '#/definitions/SubqueryExpression'
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
                }
            ],
            'title': 'ParsedExpressionSubclasses'
        },
        'Root': {
            'additionalProperties': False,
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
            'description': 'An enumeration.',
            'enum': [
                'System',
                'Bernoulli',
                'Reservoir'
            ],
            'title': 'SampleMethod'
        },
        'SampleOptions': {
            'additionalProperties': False,
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
            'properties': {
                'aggregate_handling': {
                    '$ref': '#/definitions/AggregrateHandling'
                },
                'cte_map': {
                    'title': 'Cte Map',
                    'type': 'object'
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
        'StarExpression': {
            'additionalProperties': False,
            'description': 'https://github.com/duckdb/duckdb/blob/88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1/src/include/duckdb/parser/expression/star_expression.hpp',
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
                    'additionalProperties': {
                        '$ref': '#/definitions/ParsedExpressionSubclasses'
                    },
                    'title': 'Replace List',
                    'type': 'object'
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
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'catalog_entry': {
                    '$ref': '#/definitions/TypeCatalogEntry'
                },
                'child_types': {
                    'items': {
                        'anyOf': [
                            {
                                'type': 'string'
                            },
                            {
                                '$ref': '#/definitions/LogicalType'
                            }
                        ]
                    },
                    'title': 'Child Types',
                    'type': 'array'
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
            'properties': {
                'alias': {
                    'title': 'Alias',
                    'type': 'string'
                },
                'child': {
                    'title': 'Child',
                    'type': 'boolean'
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
                        'INVALID'
                    ],
                    'title': 'Comparison Type',
                    'type': 'string'
                },
                'subquery': {
                    '$ref': '#/definitions/SelectNode'
                },
                'subquery_type': {
                    'enum': [
                        'SCALAR'
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
        'SuccessResponse': {
            'additionalProperties': False,
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
                        '$ref': '#/definitions/SelectNode'
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
            'discriminator': {
                'mapping': {
                    'BASE_TABLE': '#/definitions/BaseTableRef',
                    'EMPTY': '#/definitions/EmptyTableRef',
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
                }
            ],
            'title': 'TableRefSubclasses'
        },
        'TypeCatalogEntry': {
            'additionalProperties': False,
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
        }
    },
    'title': 'ParsingModel[Root]'
}
