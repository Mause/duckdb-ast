# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sql[ SELECT * EXCLUDE (timestamp_tz) REPLACE (varchar.replace(chr(0), chr(10)) AS whatever) FROM test_all_types() ] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=False,
                            replace_list={},
                            relation_name='',
                            exclude_list=['timestamp_tz'],
                            expr=None
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
                from_table=TableRefSubclasses(
                    __root__=TableFunctionRef(
                        alias='',
                        sample=None,
                        type='TABLE_FUNCTION',
                        function=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='test_all_types',
                            catalog='',
                            is_operator=False,
                            children=[],
                            distinct=False,
                            order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                            export_state=False,
                            filter=None
                        ),
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[ SELECT city, COUNT(*) FROM addresses GROUP BY city HAVING COUNT(*) >= 50; ] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['city']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='count_star',
                            catalog='',
                            is_operator=False,
                            children=[],
                            distinct=False,
                            order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                            export_state=False,
                            filter=None
                        )
                    )
                ],
                where_clause=None,
                sample=None,
                qualify=None,
                having=ParsedExpressionSubclasses(
                    __root__=ComparisonExpression(
                        type='GREATERTHANOREQUALTO',
                        clazz='COMPARISON',
                        alias='',
                        left=ParsedExpressionSubclasses(
                            __root__=FunctionExpression(
                                type='FUNCTION',
                                clazz='FUNCTION',
                                alias='',
                                schema_name='',
                                function_name='count_star',
                                catalog='',
                                is_operator=False,
                                children=[],
                                distinct=False,
                                order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                                export_state=False,
                                filter=None
                            )
                        ),
                        right=ParsedExpressionSubclasses(
                            __root__=ConstantExpression(
                                type='CONSTANT',
                                clazz='CONSTANT',
                                alias='',
                                value=Value(
                                    type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                    value=50,
                                    is_null=False
                                )
                            )
                        )
                    )
                ),
                group_sets=[{0}],
                group_expressions=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['city']
                        )
                    )
                ],
                aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='addresses',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[ select (select 1) as one ] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=SubqueryExpression(
                            type='SUBQUERY',
                            clazz='SUBQUERY',
                            alias='one',
                            child=None,
                            comparison_type='INVALID',
                            subquery=SelectNode(
                                type='SELECT_NODE',
                                modifiers=[],
                                cte_map={'map': []},
                                select_list=[
                                    ParsedExpressionSubclasses(
                                        __root__=ConstantExpression(
                                            type='CONSTANT',
                                            clazz='CONSTANT',
                                            alias='',
                                            value=Value(
                                                type=LogicalType(
                                                    id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                    type_info=None
                                                ),
                                                value=1,
                                                is_null=False
                                            )
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
                                from_table=TableRefSubclasses(
                                    __root__=EmptyTableRef(alias='', sample=None, type='EMPTY')
                                )
                            ),
                            subquery_type='SCALAR'
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots["test_sql[SELECT '101010'::BIT] 1"] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=ParsedExpressionSubclasses(
                                __root__=ConstantExpression(
                                    type='CONSTANT',
                                    clazz='CONSTANT',
                                    alias='',
                                    value=Value(
                                        type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                        value='101010',
                                        is_null=False
                                    )
                                )
                            ),
                            cast_type=LogicalType(id=<LogicalTypeId.BIT: 'BIT'>, type_info=None),
                            try_cast=False
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[SELECT * FROM frogs USING SAMPLE 1% (BERNOULLI);] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=False,
                            replace_list={},
                            relation_name='',
                            exclude_list=[],
                            expr=None
                        )
                    )
                ],
                where_clause=None,
                sample=SampleOptions(
                    sample_size=Value(
                        type=LogicalType(id=<LogicalTypeId.DOUBLE: 'DOUBLE'>, type_info=None),
                        value=1.0,
                        is_null=False
                    ),
                    is_percentage=True,
                    method=<SampleMethod.BERNOULLI_SAMPLE: 'Bernoulli'>,
                    seed=-1
                ),
                qualify=None,
                having=None,
                group_sets=[],
                group_expressions=[],
                aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[create table dummy as select 1] 1'] = '''Root(
    __root__=ErrorResponse(
        error=True,
        error_message='Only SELECT statements can be serialized to json!',
        error_type='not implemented'
    )
)
'''

snapshots['test_sql[select * from duckdb_tables] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=False,
                            replace_list={},
                            relation_name='',
                            exclude_list=[],
                            expr=None
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
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='duckdb_tables',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select * from range(0, 10)] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=False,
                            replace_list={},
                            relation_name='',
                            exclude_list=[],
                            expr=None
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
                from_table=TableRefSubclasses(
                    __root__=TableFunctionRef(
                        alias='',
                        sample=None,
                        type='TABLE_FUNCTION',
                        function=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='range',
                            catalog='',
                            is_operator=False,
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                            value=0,
                                            is_null=False
                                        )
                                    )
                                ),
                                ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                            value=10,
                                            is_null=False
                                        )
                                    )
                                )
                            ],
                            distinct=False,
                            order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                            export_state=False,
                            filter=None
                        ),
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select 0::DECIMAL(15, 6)] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=ParsedExpressionSubclasses(
                                __root__=ConstantExpression(
                                    type='CONSTANT',
                                    clazz='CONSTANT',
                                    alias='',
                                    value=Value(
                                        type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                        value=0,
                                        is_null=False
                                    )
                                )
                            ),
                            cast_type=LogicalType(
                                id=<LogicalTypeId.DECIMAL: 'DECIMAL'>,
                                type_info=DecimalTypeInfo(
                                    type='DECIMAL_TYPE_INFO',
                                    alias='',
                                    catalog_entry=None,
                                    width=15,
                                    scale=6
                                )
                            ),
                            try_cast=False
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select 0::STRUCT(a INT)] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=ParsedExpressionSubclasses(
                                __root__=ConstantExpression(
                                    type='CONSTANT',
                                    clazz='CONSTANT',
                                    alias='',
                                    value=Value(
                                        type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                        value=0,
                                        is_null=False
                                    )
                                )
                            ),
                            cast_type=LogicalType(
                                id=<LogicalTypeId.STRUCT: 'STRUCT'>,
                                type_info=StructTypeInfo(
                                    type='STRUCT_TYPE_INFO',
                                    alias='',
                                    catalog_entry=None,
                                    child_types=[
                                        'a',
                                        LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None)
                                    ]
                                )
                            ),
                            try_cast=False
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select 0::USER_TYPE] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=ParsedExpressionSubclasses(
                                __root__=ConstantExpression(
                                    type='CONSTANT',
                                    clazz='CONSTANT',
                                    alias='',
                                    value=Value(
                                        type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                        value=0,
                                        is_null=False
                                    )
                                )
                            ),
                            cast_type=LogicalType(
                                id=<LogicalTypeId.USER: 'USER'>,
                                type_info=UserTypeInfo(
                                    type='USER_TYPE_INFO',
                                    alias='',
                                    catalog_entry=None,
                                    user_type_name='USER_TYPE'
                                )
                            ),
                            try_cast=False
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select 1 * 1] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='*',
                            catalog='',
                            is_operator=True,
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                            value=1,
                                            is_null=False
                                        )
                                    )
                                ),
                                ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                            value=1,
                                            is_null=False
                                        )
                                    )
                                )
                            ],
                            distinct=False,
                            order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                            export_state=False,
                            filter=None
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select 1] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=1,
                                is_null=False
                            )
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select []::boolean[]] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=CastExpression(
                            type='CAST',
                            clazz='CAST',
                            alias='',
                            child=ParsedExpressionSubclasses(
                                __root__=FunctionExpression(
                                    type='FUNCTION',
                                    clazz='FUNCTION',
                                    alias='',
                                    schema_name='main',
                                    function_name='list_value',
                                    catalog='',
                                    is_operator=False,
                                    children=[],
                                    distinct=False,
                                    order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                                    export_state=False,
                                    filter=None
                                )
                            ),
                            cast_type=LogicalType(
                                id=<LogicalTypeId.LIST: 'LIST'>,
                                type_info=ListTypeInfo(
                                    type='LIST_TYPE_INFO',
                                    alias='',
                                    catalog_entry=None,
                                    child_type=LogicalType(id=<LogicalTypeId.BOOLEAN: 'BOOLEAN'>, type_info=None)
                                )
                            ),
                            try_cast=False
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select frog from frogs where height > 5 and leader = true] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['frog']
                        )
                    )
                ],
                where_clause=ParsedExpressionSubclasses(
                    __root__=ConjunctionExpression(
                        type='AND',
                        clazz='CONJUNCTION',
                        alias='',
                        children=[
                            ParsedExpressionSubclasses(
                                __root__=ComparisonExpression(
                                    type='GREATERTHAN',
                                    clazz='COMPARISON',
                                    alias='',
                                    left=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['height']
                                        )
                                    ),
                                    right=ParsedExpressionSubclasses(
                                        __root__=ConstantExpression(
                                            type='CONSTANT',
                                            clazz='CONSTANT',
                                            alias='',
                                            value=Value(
                                                type=LogicalType(
                                                    id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                    type_info=None
                                                ),
                                                value=5,
                                                is_null=False
                                            )
                                        )
                                    )
                                )
                            ),
                            ParsedExpressionSubclasses(
                                __root__=ComparisonExpression(
                                    type='EQUAL',
                                    clazz='COMPARISON',
                                    alias='',
                                    left=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['leader']
                                        )
                                    ),
                                    right=ParsedExpressionSubclasses(
                                        __root__=CastExpression(
                                            type='CAST',
                                            clazz='CAST',
                                            alias='',
                                            child=ParsedExpressionSubclasses(
                                                __root__=ConstantExpression(
                                                    type='CONSTANT',
                                                    clazz='CONSTANT',
                                                    alias='',
                                                    value=Value(
                                                        type=LogicalType(
                                                            id=<LogicalTypeId.VARCHAR: 'VARCHAR'>,
                                                            type_info=None
                                                        ),
                                                        value='t',
                                                        is_null=False
                                                    )
                                                )
                                            ),
                                            cast_type=LogicalType(
                                                id=<LogicalTypeId.BOOLEAN: 'BOOLEAN'>,
                                                type_info=None
                                            ),
                                            try_cast=False
                                        )
                                    )
                                )
                            )
                        ]
                    )
                ),
                sample=None,
                qualify=None,
                having=None,
                group_sets=[],
                group_expressions=[],
                aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select frog from frogs] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['frog']
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
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select frog.* EXCLUDE age from frogs] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=False,
                            replace_list={},
                            relation_name='frog',
                            exclude_list=['age'],
                            expr=None
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
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select frog.age from frogs] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['frog', 'age']
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
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''

snapshots['test_sql[select list_apply([1, 2, 3], x => x * 2)] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='list_apply',
                            catalog='',
                            is_operator=False,
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=FunctionExpression(
                                        type='FUNCTION',
                                        clazz='FUNCTION',
                                        alias='',
                                        schema_name='main',
                                        function_name='list_value',
                                        catalog='',
                                        is_operator=False,
                                        children=[
                                            ParsedExpressionSubclasses(
                                                __root__=ConstantExpression(
                                                    type='CONSTANT',
                                                    clazz='CONSTANT',
                                                    alias='',
                                                    value=Value(
                                                        type=LogicalType(
                                                            id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                            type_info=None
                                                        ),
                                                        value=1,
                                                        is_null=False
                                                    )
                                                )
                                            ),
                                            ParsedExpressionSubclasses(
                                                __root__=ConstantExpression(
                                                    type='CONSTANT',
                                                    clazz='CONSTANT',
                                                    alias='',
                                                    value=Value(
                                                        type=LogicalType(
                                                            id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                            type_info=None
                                                        ),
                                                        value=2,
                                                        is_null=False
                                                    )
                                                )
                                            ),
                                            ParsedExpressionSubclasses(
                                                __root__=ConstantExpression(
                                                    type='CONSTANT',
                                                    clazz='CONSTANT',
                                                    alias='',
                                                    value=Value(
                                                        type=LogicalType(
                                                            id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                            type_info=None
                                                        ),
                                                        value=3,
                                                        is_null=False
                                                    )
                                                )
                                            )
                                        ],
                                        distinct=False,
                                        order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                                        export_state=False,
                                        filter=None
                                    )
                                ),
                                ParsedExpressionSubclasses(
                                    __root__=FunctionExpression(
                                        type='FUNCTION',
                                        clazz='FUNCTION',
                                        alias='x',
                                        schema_name='',
                                        function_name='*',
                                        catalog='',
                                        is_operator=True,
                                        children=[
                                            ParsedExpressionSubclasses(
                                                __root__=ColumnRefExpression(
                                                    type='COLUMN_REF',
                                                    clazz='COLUMN_REF',
                                                    alias='',
                                                    column_names=['x']
                                                )
                                            ),
                                            ParsedExpressionSubclasses(
                                                __root__=ConstantExpression(
                                                    type='CONSTANT',
                                                    clazz='CONSTANT',
                                                    alias='',
                                                    value=Value(
                                                        type=LogicalType(
                                                            id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                            type_info=None
                                                        ),
                                                        value=2,
                                                        is_null=False
                                                    )
                                                )
                                            )
                                        ],
                                        distinct=False,
                                        order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                                        export_state=False,
                                        filter=None
                                    )
                                )
                            ],
                            distinct=False,
                            order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                            export_state=False,
                            filter=None
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
                from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
            )
        ]
    )
)
'''

snapshots['test_sql[select name from frogs GROUP BY age] 1'] = '''Root(
    __root__=SuccessResponse(
        error=False,
        statements=[
            SelectNode(
                type='SELECT_NODE',
                modifiers=[],
                cte_map={'map': []},
                select_list=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['name']
                        )
                    )
                ],
                where_clause=None,
                sample=None,
                qualify=None,
                having=None,
                group_sets=[{0}],
                group_expressions=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['age']
                        )
                    )
                ],
                aggregate_handling=<AggregrateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                from_table=TableRefSubclasses(
                    __root__=BaseTableRef(
                        alias='',
                        sample=None,
                        type='BASE_TABLE',
                        schema_name='',
                        table_name='frogs',
                        catalog_name='',
                        column_name_alias=[]
                    )
                )
            )
        ]
    )
)
'''
