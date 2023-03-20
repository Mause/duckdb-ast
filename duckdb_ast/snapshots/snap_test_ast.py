# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sql[create table dummy as select 1] 1'] = '''ErrorResponse(
    error=True,
    error_message='Only SELECT statements can be serialized to json!',
    error_type='not implemented'
)
'''

snapshots['test_sql[select * from duckdb_tables] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[
                StarExpression(
                    type='STAR',
                    clazz='STAR',
                    alias='',
                    columns=False,
                    replace_list=[],
                    relation_name='',
                    exclude_list=[]
                )
            ],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=BaseTable(
                type='BASE_TABLE',
                alias='',
                sample=None,
                schema_name='',
                table_name='duckdb_tables',
                catalog_name='',
                column_name_alias=[]
            )
        )
    ]
)
'''

snapshots['test_sql[select * from range(0, 10)] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[
                StarExpression(
                    type='STAR',
                    clazz='STAR',
                    alias='',
                    columns=False,
                    replace_list=[],
                    relation_name='',
                    exclude_list=[]
                )
            ],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=TableFunction(
                type='TABLE_FUNCTION',
                alias='',
                function=Function(
                    clazz='FUNCTION',
                    type='FUNCTION',
                    schema_name='',
                    function_name='range',
                    catalog='',
                    alias='',
                    is_operator=False,
                    children=[
                        Constant(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=0,
                                is_null=False
                            )
                        ),
                        Constant(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=10,
                                is_null=False
                            )
                        )
                    ],
                    distinct=False,
                    order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                    export_state=False,
                    filter=None
                ),
                sample=None,
                column_name_alias=[]
            )
        )
    ]
)
'''

snapshots['test_sql[select 1 * 1] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[
                Function(
                    clazz='FUNCTION',
                    type='FUNCTION',
                    schema_name='',
                    function_name='*',
                    catalog='',
                    alias='',
                    is_operator=True,
                    children=[
                        Constant(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=1,
                                is_null=False
                            )
                        ),
                        Constant(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=1,
                                is_null=False
                            )
                        )
                    ],
                    distinct=False,
                    order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                    export_state=False,
                    filter=None
                )
            ],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=EmptyTable(type='EMPTY', alias='', sample=None)
        )
    ]
)
'''

snapshots['test_sql[select 1] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[
                Constant(
                    type='CONSTANT',
                    clazz='CONSTANT',
                    alias='',
                    value=Value(
                        type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                        value=1,
                        is_null=False
                    )
                )
            ],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=EmptyTable(type='EMPTY', alias='', sample=None)
        )
    ]
)
'''

snapshots['test_sql[select frog from frogs where height > 5 and leader = true] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['frog'])],
            where_clause=Conjunction(
                clazz='CONJUNCTION',
                type='AND',
                alias='',
                children=[
                    Comparison(
                        clazz='COMPARISON',
                        type='GREATERTHAN',
                        alias='',
                        left=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['height']
                        ),
                        right=Constant(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=ValueType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=5,
                                is_null=False
                            )
                        )
                    ),
                    Comparison(
                        clazz='COMPARISON',
                        type='EQUAL',
                        alias='',
                        left=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['leader']
                        ),
                        right=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=Constant(
                                type='CONSTANT',
                                clazz='CONSTANT',
                                alias='',
                                value=Value(
                                    type=ValueType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                    value='t',
                                    is_null=False
                                )
                            ),
                            cast_type=ValueType(id=<LogicalTypeId.BOOLEAN: 'BOOLEAN'>, type_info=None),
                            try_cast=False
                        )
                    )
                ]
            ),
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=BaseTable(
                type='BASE_TABLE',
                alias='',
                sample=None,
                schema_name='',
                table_name='frogs',
                catalog_name='',
                column_name_alias=[]
            )
        )
    ]
)
'''

snapshots['test_sql[select frog from frogs] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['frog'])],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=BaseTable(
                type='BASE_TABLE',
                alias='',
                sample=None,
                schema_name='',
                table_name='frogs',
                catalog_name='',
                column_name_alias=[]
            )
        )
    ]
)
'''

snapshots['test_sql[select frog.age from frogs] 1'] = '''SuccessResponse(
    error=False,
    statements=[
        Statement(
            type=<StatementType.SELECT_NODE: 'SELECT_NODE'>,
            modifiers=[],
            cte_map={'map': []},
            select_list=[
                ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['frog', 'age'])
            ],
            where_clause=None,
            sample=None,
            qualify=None,
            having=None,
            group_sets=[],
            group_expressions=[],
            aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=BaseTable(
                type='BASE_TABLE',
                alias='',
                sample=None,
                schema_name='',
                table_name='frogs',
                catalog_name='',
                column_name_alias=[]
            )
        )
    ]
)
'''
