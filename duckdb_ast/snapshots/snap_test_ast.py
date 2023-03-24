# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sql[ SELECT * EXCLUDE (timestamp_tz) REPLACE (varchar.replace(chr(0), chr(10)) AS whatever) FROM test_all_types() ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[ SELECT * FROM grades grades_parent WHERE grade= (SELECT MIN(grade) FROM grades WHERE grades.course=grades_parent.course); ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    where_clause=ParsedExpressionSubclasses(
        __root__=ComparisonExpression(
            type='EQUAL',
            clazz='COMPARISON',
            alias='',
            left=ParsedExpressionSubclasses(
                __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['grade'])
            ),
            right=ParsedExpressionSubclasses(
                __root__=SubqueryExpression(
                    type='SUBQUERY',
                    clazz='SUBQUERY',
                    alias='',
                    child=None,
                    comparison_type='INVALID',
                    subquery=QueryNodeSubclasses(
                        __root__=SelectNode(
                            type='SELECT_NODE',
                            modifiers=[],
                            cte_map=CommonTableExpressionMap(map={}),
                            select_list=[
                                ParsedExpressionSubclasses(
                                    __root__=FunctionExpression(
                                        type='FUNCTION',
                                        clazz='FUNCTION',
                                        alias='',
                                        schema_name='',
                                        function_name='min',
                                        catalog='',
                                        is_operator=False,
                                        children=[
                                            ParsedExpressionSubclasses(
                                                __root__=ColumnRefExpression(
                                                    type='COLUMN_REF',
                                                    clazz='COLUMN_REF',
                                                    alias='',
                                                    column_names=['grade']
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
                            where_clause=ParsedExpressionSubclasses(
                                __root__=ComparisonExpression(
                                    type='EQUAL',
                                    clazz='COMPARISON',
                                    alias='',
                                    left=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['grades', 'course']
                                        )
                                    ),
                                    right=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['grades_parent', 'course']
                                        )
                                    )
                                )
                            ),
                            sample=None,
                            qualify=None,
                            having=None,
                            group_sets=[],
                            group_expressions=[],
                            aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                            from_table=TableRefSubclasses(
                                __root__=BaseTableRef(
                                    alias='',
                                    sample=None,
                                    type='BASE_TABLE',
                                    schema_name='',
                                    table_name='grades',
                                    catalog_name='',
                                    column_name_alias=[]
                                )
                            )
                        )
                    ),
                    subquery_type='SCALAR'
                )
            )
        )
    ),
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='grades_parent',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='grades',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ SELECT * FROM range(10) t1 UNION ALL SELECT * FROM range(5) t2; ] 1'] = '''SetOperationNode(
    type='SET_OPERATION_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    set_op_type='UNION',
    left=QueryNodeSubclasses(
        __root__=SelectNode(
            type='SELECT_NODE',
            modifiers=[],
            cte_map=CommonTableExpressionMap(map={}),
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
            aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=TableRefSubclasses(
                __root__=TableFunctionRef(
                    alias='t1',
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
    ),
    right=QueryNodeSubclasses(
        __root__=SelectNode(
            type='SELECT_NODE',
            modifiers=[],
            cte_map=CommonTableExpressionMap(map={}),
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
            aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
            from_table=TableRefSubclasses(
                __root__=TableFunctionRef(
                    alias='t2',
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
                                        value=5,
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
    )
)
'''

snapshots['test_sql[ SELECT Plant, Date, AVG(MWh) OVER ( PARTITION BY Plant ORDER BY Date ASC RANGE BETWEEN INTERVAL 3 DAYS PRECEDING AND INTERVAL 3 DAYS FOLLOWING) AS \'MWh 7-day Moving Average\' FROM \'Generation History\' ORDER BY 1, 2 ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[
        ResultModifierSubclasses(
            __root__=OrderModifier(
                type='ORDER_MODIFIER',
                orders=[
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
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
                    ),
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ConstantExpression(
                                type='CONSTANT',
                                clazz='CONSTANT',
                                alias='',
                                value=Value(
                                    type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                    value=2,
                                    is_null=False
                                )
                            )
                        )
                    )
                ]
            )
        )
    ],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['Plant'])
        ),
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['Date'])
        ),
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='WINDOW_AGGREGATE',
                clazz='WINDOW',
                alias='MWh 7-day Moving Average',
                catalog='',
                schema_name='',
                function_name='avg',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['MWh']
                        )
                    )
                ],
                partitions=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['Plant']
                        )
                    )
                ],
                orders=[
                    OrderByNode(
                        type=<OrderType.ASCENDING: 'ASCENDING'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['Date']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.EXPR_PRECEDING_RANGE: 'EXPR_PRECEDING_RANGE'>,
                end=<WindowBoundary.EXPR_FOLLOWING_RANGE: 'EXPR_FOLLOWING_RANGE'>,
                start_expr=ParsedExpressionSubclasses(
                    __root__=FunctionExpression(
                        type='FUNCTION',
                        clazz='FUNCTION',
                        alias='',
                        schema_name='',
                        function_name='to_days',
                        catalog='',
                        is_operator=False,
                        children=[
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
                                                type=LogicalType(
                                                    id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                    type_info=None
                                                ),
                                                value=3,
                                                is_null=False
                                            )
                                        )
                                    ),
                                    cast_type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                    try_cast=False
                                )
                            )
                        ],
                        distinct=False,
                        order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                        export_state=False,
                        filter=None
                    )
                ),
                end_expr=ParsedExpressionSubclasses(
                    __root__=FunctionExpression(
                        type='FUNCTION',
                        clazz='FUNCTION',
                        alias='',
                        schema_name='',
                        function_name='to_days',
                        catalog='',
                        is_operator=False,
                        children=[
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
                                                type=LogicalType(
                                                    id=<LogicalTypeId.INTEGER: 'INTEGER'>,
                                                    type_info=None
                                                ),
                                                value=3,
                                                is_null=False
                                            )
                                        )
                                    ),
                                    cast_type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                    try_cast=False
                                )
                            )
                        ],
                        distinct=False,
                        order_bys=OrderModifier(type='ORDER_MODIFIER', orders=[]),
                        export_state=False,
                        filter=None
                    )
                ),
                offset_expr=None,
                default_expr=None
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='Generation History',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ SELECT amount - lead(amount) OVER (ORDER BY time), amount - lag(amount) OVER (ORDER BY time), amount / SUM(amount) OVER (PARTITION BY region), FIRST(employee_name) OVER (ORDER BY salary DESC), LAST(employee_name) OVER (ORDER BY salary DESC), NTH_VALUE(employee_name, 2) OVER (ORDER BY salary DESC) FROM basic_pays ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=FunctionExpression(
                type='FUNCTION',
                clazz='FUNCTION',
                alias='',
                schema_name='',
                function_name='-',
                catalog='',
                is_operator=True,
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['amount']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=WindowExpression(
                            type='LEAD',
                            clazz='WINDOW',
                            alias='',
                            catalog='',
                            schema_name='',
                            function_name='lead',
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['amount']
                                    )
                                )
                            ],
                            partitions=[],
                            orders=[
                                OrderByNode(
                                    type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                                    null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                                    expression=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['time']
                                        )
                                    )
                                )
                            ],
                            filter_expr=None,
                            ignore_nulls=False,
                            start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                            end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                            start_expr=None,
                            end_expr=None,
                            offset_expr=None,
                            default_expr=None
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
                alias='',
                schema_name='',
                function_name='-',
                catalog='',
                is_operator=True,
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['amount']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=WindowExpression(
                            type='LAG',
                            clazz='WINDOW',
                            alias='',
                            catalog='',
                            schema_name='',
                            function_name='lag',
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['amount']
                                    )
                                )
                            ],
                            partitions=[],
                            orders=[
                                OrderByNode(
                                    type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                                    null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                                    expression=ParsedExpressionSubclasses(
                                        __root__=ColumnRefExpression(
                                            type='COLUMN_REF',
                                            clazz='COLUMN_REF',
                                            alias='',
                                            column_names=['time']
                                        )
                                    )
                                )
                            ],
                            filter_expr=None,
                            ignore_nulls=False,
                            start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                            end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                            start_expr=None,
                            end_expr=None,
                            offset_expr=None,
                            default_expr=None
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
                alias='',
                schema_name='',
                function_name='/',
                catalog='',
                is_operator=True,
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['amount']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=WindowExpression(
                            type='WINDOW_AGGREGATE',
                            clazz='WINDOW',
                            alias='',
                            catalog='',
                            schema_name='',
                            function_name='sum',
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['amount']
                                    )
                                )
                            ],
                            partitions=[
                                ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['region']
                                    )
                                )
                            ],
                            orders=[],
                            filter_expr=None,
                            ignore_nulls=False,
                            start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                            end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                            start_expr=None,
                            end_expr=None,
                            offset_expr=None,
                            default_expr=None
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
            __root__=WindowExpression(
                type='FIRST_VALUE',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='first',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['employee_name']
                        )
                    )
                ],
                partitions=[],
                orders=[
                    OrderByNode(
                        type=<OrderType.DESCENDING: 'DESCENDING'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['salary']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        ),
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='LAST_VALUE',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='last',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['employee_name']
                        )
                    )
                ],
                partitions=[],
                orders=[
                    OrderByNode(
                        type=<OrderType.DESCENDING: 'DESCENDING'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['salary']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        ),
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='NTH_VALUE',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='nth_value',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['employee_name']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=2,
                                is_null=False
                            )
                        )
                    )
                ],
                partitions=[],
                orders=[
                    OrderByNode(
                        type=<OrderType.DESCENDING: 'DESCENDING'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['salary']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='basic_pays',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ SELECT city, COUNT(*) FROM addresses GROUP BY city HAVING COUNT(*) >= 50; ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['city'])
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
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['city'])
        )
    ],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[ WITH RECURSIVE per_investor_amount AS ( SELECT 0 AS investors_number, 0.00 AS investment_amount, 0.00 AS individual_amount UNION SELECT investors_number + 1, i.investment_amount, i.investment_amount / (investors_number + 1) FROM investment i, per_investor_amount pia WHERE investors_number << 3 ) SELECT * FROM per_investor_amount ORDER BY investment_amount, investors_number; ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[
        ResultModifierSubclasses(
            __root__=OrderModifier(
                type='ORDER_MODIFIER',
                orders=[
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['investment_amount']
                            )
                        )
                    ),
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['investors_number']
                            )
                        )
                    )
                ]
            )
        )
    ],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='per_investor_amount',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ WITH RECURSIVE tag_hierarchy(id, source, path) AS ( SELECT id, name, [name] AS path FROM tag WHERE subclassof IS NULL UNION ALL SELECT tag.id, tag.name, list_prepend(tag.name, tag_hierarchy.path) FROM tag, tag_hierarchy WHERE tag.subclassof = tag_hierarchy.id ) SELECT path FROM tag_hierarchy WHERE source = \'Oasis\'; ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['path'])
        )
    ],
    where_clause=ParsedExpressionSubclasses(
        __root__=ComparisonExpression(
            type='EQUAL',
            clazz='COMPARISON',
            alias='',
            left=ParsedExpressionSubclasses(
                __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['source'])
            ),
            right=ParsedExpressionSubclasses(
                __root__=ConstantExpression(
                    type='CONSTANT',
                    clazz='CONSTANT',
                    alias='',
                    value=Value(
                        type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                        value='Oasis',
                        is_null=False
                    )
                )
            )
        )
    ),
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='tag_hierarchy',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ WITH ranked_functions as ( SELECT schema_name, function_name, row_number() over (partition by schema_name order by function_name) as function_rank FROM duckdb_functions() ) SELECT * FROM ranked_functions WHERE function_rank < 3; ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    where_clause=ParsedExpressionSubclasses(
        __root__=ComparisonExpression(
            type='LESSTHAN',
            clazz='COMPARISON',
            alias='',
            left=ParsedExpressionSubclasses(
                __root__=ColumnRefExpression(
                    type='COLUMN_REF',
                    clazz='COLUMN_REF',
                    alias='',
                    column_names=['function_rank']
                )
            ),
            right=ParsedExpressionSubclasses(
                __root__=ConstantExpression(
                    type='CONSTANT',
                    clazz='CONSTANT',
                    alias='',
                    value=Value(
                        type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                        value=3,
                        is_null=False
                    )
                )
            )
        )
    ),
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='ranked_functions',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[ select (select 1) as one ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=SubqueryExpression(
                type='SUBQUERY',
                clazz='SUBQUERY',
                alias='one',
                child=None,
                comparison_type='INVALID',
                subquery=QueryNodeSubclasses(
                    __root__=SelectNode(
                        type='SELECT_NODE',
                        modifiers=[],
                        cte_map=CommonTableExpressionMap(map={}),
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
                        aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                        from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[ select thing[0], thing[\'hello\'], thing[1:3], struct_pack(hello := \'world\').hello, ] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='ARRAY_EXTRACT',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['thing']
                        )
                    ),
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
                    )
                ]
            )
        ),
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='ARRAY_EXTRACT',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['thing']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='hello',
                                is_null=False
                            )
                        )
                    )
                ]
            )
        ),
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='ARRAY_SLICE',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['thing']
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
                    ),
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                value=3,
                                is_null=False
                            )
                        )
                    )
                ]
            )
        ),
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='STRUCT_EXTRACT',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=FunctionExpression(
                            type='FUNCTION',
                            clazz='FUNCTION',
                            alias='',
                            schema_name='',
                            function_name='struct_pack',
                            catalog='',
                            is_operator=False,
                            children=[
                                ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='hello',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                            value='world',
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
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='hello',
                                is_null=False
                            )
                        )
                    )
                ]
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT \'101010\'::BIT] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT \'Math\' IN (\'CS\', \'Math\'), X NOT IN (\'CS\', \'Math\')] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='IN',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='Math',
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
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='CS',
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
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='Math',
                                is_null=False
                            )
                        )
                    )
                ]
            )
        ),
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='COMPARE_NOT_IN',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['X']
                        )
                    ),
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='CS',
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
                                type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                value='Math',
                                is_null=False
                            )
                        )
                    )
                ]
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT \'Math\' IN (SELECT course FROM grades);] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=SubqueryExpression(
                type='SUBQUERY',
                clazz='SUBQUERY',
                alias='',
                child=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                            value='Math',
                            is_null=False
                        )
                    )
                ),
                comparison_type='EQUAL',
                subquery=QueryNodeSubclasses(
                    __root__=SelectNode(
                        type='SELECT_NODE',
                        modifiers=[],
                        cte_map=CommonTableExpressionMap(map={}),
                        select_list=[
                            ParsedExpressionSubclasses(
                                __root__=ColumnRefExpression(
                                    type='COLUMN_REF',
                                    clazz='COLUMN_REF',
                                    alias='',
                                    column_names=['course']
                                )
                            )
                        ],
                        where_clause=None,
                        sample=None,
                        qualify=None,
                        having=None,
                        group_sets=[],
                        group_expressions=[],
                        aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                        from_table=TableRefSubclasses(
                            __root__=BaseTableRef(
                                alias='',
                                sample=None,
                                type='BASE_TABLE',
                                schema_name='',
                                table_name='grades',
                                catalog_name='',
                                column_name_alias=[]
                            )
                        )
                    )
                ),
                subquery_type='ANY'
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT \'hello\' COLLATE NOCASE] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=CollateExpression(
                type='COLLATE',
                clazz='COLLATE',
                alias='',
                child=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                            value='hello',
                            is_null=False
                        )
                    )
                ),
                collation='NOCASE'
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT * FROM frogs USING SAMPLE 1% (BERNOULLI);] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[SELECT 0::HUGEINT] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                cast_type=LogicalType(id=<LogicalTypeId.HUGEINT: 'HUGEINT'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT 0::UNION(num INT, str VARCHAR)] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                    id=<LogicalTypeId.UNION: 'UNION'>,
                    type_info=StructTypeInfo(
                        type='STRUCT_TYPE_INFO',
                        alias='',
                        catalog_entry=None,
                        child_types=[
                            '',
                            LogicalType(id=<LogicalTypeId.TINYINT: 'TINYINT'>, type_info=None),
                            'num',
                            LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            'str',
                            LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None)
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT 1 < 1, 1 <= 2] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='LESSTHAN',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
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
                right=ParsedExpressionSubclasses(
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
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='LESSTHANOREQUALTO',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
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
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT 2 < 3, 2 > 3, 2 <= 3, 4 >= NULL, NULL = NULL, 2 <> 2] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='LESSTHAN',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=3,
                            is_null=False
                        )
                    )
                )
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='GREATERTHAN',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=3,
                            is_null=False
                        )
                    )
                )
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='LESSTHANOREQUALTO',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=3,
                            is_null=False
                        )
                    )
                )
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='GREATERTHANOREQUALTO',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=4,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
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
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
                        )
                    )
                )
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='NOTEQUAL',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT 2 IS DISTINCT FROM NULL, NULL IS NOT DISTINCT FROM NULL] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='DISTINCT_FROM',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            value=2,
                            is_null=False
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
                        )
                    )
                )
            )
        ),
        ParsedExpressionSubclasses(
            __root__=ComparisonExpression(
                type='NOT_DISTINCT_FROM',
                clazz='COMPARISON',
                alias='',
                left=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
                        )
                    )
                ),
                right=ParsedExpressionSubclasses(
                    __root__=ConstantExpression(
                        type='CONSTANT',
                        clazz='CONSTANT',
                        alias='',
                        value=Value(
                            type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                            value=None,
                            is_null=True
                        )
                    )
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT DATE \'1992-09-20\'] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                            value='1992-09-20',
                            is_null=False
                        )
                    )
                ),
                cast_type=LogicalType(id=<LogicalTypeId.DATE: 'DATE'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT EXISTS(SELECT * FROM grades WHERE course=\'Math\');] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=SubqueryExpression(
                type='SUBQUERY',
                clazz='SUBQUERY',
                alias='',
                child=None,
                comparison_type='INVALID',
                subquery=QueryNodeSubclasses(
                    __root__=SelectNode(
                        type='SELECT_NODE',
                        modifiers=[],
                        cte_map=CommonTableExpressionMap(map={}),
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
                        where_clause=ParsedExpressionSubclasses(
                            __root__=ComparisonExpression(
                                type='EQUAL',
                                clazz='COMPARISON',
                                alias='',
                                left=ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['course']
                                    )
                                ),
                                right=ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                            value='Math',
                                            is_null=False
                                        )
                                    )
                                )
                            )
                        ),
                        sample=None,
                        qualify=None,
                        having=None,
                        group_sets=[],
                        group_expressions=[],
                        aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                        from_table=TableRefSubclasses(
                            __root__=BaseTableRef(
                                alias='',
                                sample=None,
                                type='BASE_TABLE',
                                schema_name='',
                                table_name='grades',
                                catalog_name='',
                                column_name_alias=[]
                            )
                        )
                    )
                ),
                subquery_type='EXISTS'
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT INTERVAL 1 YEAR] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=FunctionExpression(
                type='FUNCTION',
                clazz='FUNCTION',
                alias='',
                schema_name='',
                function_name='to_years',
                catalog='',
                is_operator=False,
                children=[
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
                                        value=1,
                                        is_null=False
                                    )
                                )
                            ),
                            cast_type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                            try_cast=False
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT MIN(COLUMNS(*)), COUNT(COLUMNS(*)) from numbers;] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=FunctionExpression(
                type='FUNCTION',
                clazz='FUNCTION',
                alias='',
                schema_name='',
                function_name='min',
                catalog='',
                is_operator=False,
                children=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=True,
                            replace_list={},
                            relation_name='',
                            exclude_list=[],
                            expr=None
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
                alias='',
                schema_name='',
                function_name='count',
                catalog='',
                is_operator=False,
                children=[
                    ParsedExpressionSubclasses(
                        __root__=StarExpression(
                            type='STAR',
                            clazz='STAR',
                            alias='',
                            columns=True,
                            replace_list={},
                            relation_name='',
                            exclude_list=[],
                            expr=None
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='numbers',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[SELECT NULL IS NULL] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='IS_NULL',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ConstantExpression(
                            type='CONSTANT',
                            clazz='CONSTANT',
                            alias='',
                            value=Value(
                                type=LogicalType(id=<LogicalTypeId.NULL: 'NULL'>, type_info=None),
                                value=None,
                                is_null=True
                            )
                        )
                    )
                ]
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT TIMESTAMP \'1992-09-20 11:30:00\'] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                            value='1992-09-20 11:30:00',
                            is_null=False
                        )
                    )
                ),
                cast_type=LogicalType(id=<LogicalTypeId.TIMESTAMP: 'TIMESTAMP'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT TIMESTAMPTZ \'1992-09-20 11:30:00\'] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                            value='1992-09-20 11:30:00',
                            is_null=False
                        )
                    )
                ),
                cast_type=LogicalType(id=<LogicalTypeId.TIMESTAMP_TZ: 'TIMESTAMP WITH TIME ZONE'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT a BETWEEN x AND y] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=BetweenExpression(
                type='COMPARE_BETWEEN',
                clazz='BETWEEN',
                alias='',
                input=ParsedExpressionSubclasses(
                    __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['a'])
                ),
                lower=ParsedExpressionSubclasses(
                    __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['x'])
                ),
                upper=ParsedExpressionSubclasses(
                    __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['y'])
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT a NOT BETWEEN x AND y] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='NOT',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=BetweenExpression(
                            type='COMPARE_BETWEEN',
                            clazz='BETWEEN',
                            alias='',
                            input=ParsedExpressionSubclasses(
                                __root__=ColumnRefExpression(
                                    type='COLUMN_REF',
                                    clazz='COLUMN_REF',
                                    alias='',
                                    column_names=['a']
                                )
                            ),
                            lower=ParsedExpressionSubclasses(
                                __root__=ColumnRefExpression(
                                    type='COLUMN_REF',
                                    clazz='COLUMN_REF',
                                    alias='',
                                    column_names=['x']
                                )
                            ),
                            upper=ParsedExpressionSubclasses(
                                __root__=ColumnRefExpression(
                                    type='COLUMN_REF',
                                    clazz='COLUMN_REF',
                                    alias='',
                                    column_names=['y']
                                )
                            )
                        )
                    )
                ]
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT a.* FROM (SELECT {\'x\':1, \'y\':2, \'z\':3} as a);] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=StarExpression(
                type='STAR',
                clazz='STAR',
                alias='',
                columns=False,
                replace_list={},
                relation_name='a',
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=SubqueryRef(
            alias='',
            sample=None,
            type='SUBQUERY',
            subquery=SelectStatement(
                __root__=QueryNodeSubclasses(
                    __root__=SelectNode(
                        type='SELECT_NODE',
                        modifiers=[],
                        cte_map=CommonTableExpressionMap(map={}),
                        select_list=[
                            ParsedExpressionSubclasses(
                                __root__=FunctionExpression(
                                    type='FUNCTION',
                                    clazz='FUNCTION',
                                    alias='a',
                                    schema_name='main',
                                    function_name='struct_pack',
                                    catalog='',
                                    is_operator=False,
                                    children=[
                                        ParsedExpressionSubclasses(
                                            __root__=ConstantExpression(
                                                type='CONSTANT',
                                                clazz='CONSTANT',
                                                alias='x',
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
                                                alias='y',
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
                                                alias='z',
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
                            )
                        ],
                        where_clause=None,
                        sample=None,
                        qualify=None,
                        having=None,
                        group_sets=[],
                        group_expressions=[],
                        aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
                        from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
                    )
                )
            ),
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[SELECT expression IS NOT NULL] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=OperatorExpression(
                type='IS_NOT_NULL',
                clazz='OPERATOR',
                alias='',
                children=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['expression']
                        )
                    )
                ]
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[SELECT i, CASE WHEN i>2 THEN 1 ELSE 0 END AS test FROM integers] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['i'])
        ),
        ParsedExpressionSubclasses(
            __root__=CaseExpression(
                type='CASE',
                clazz='CASE',
                alias='test',
                case_checks=[
                    CaseCheck(
                        when_expr=ParsedExpressionSubclasses(
                            __root__=ComparisonExpression(
                                type='GREATERTHAN',
                                clazz='COMPARISON',
                                alias='',
                                left=ParsedExpressionSubclasses(
                                    __root__=ColumnRefExpression(
                                        type='COLUMN_REF',
                                        clazz='COLUMN_REF',
                                        alias='',
                                        column_names=['i']
                                    )
                                ),
                                right=ParsedExpressionSubclasses(
                                    __root__=ConstantExpression(
                                        type='CONSTANT',
                                        clazz='CONSTANT',
                                        alias='',
                                        value=Value(
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
                                            value=2,
                                            is_null=False
                                        )
                                    )
                                )
                            )
                        ),
                        then_expr=ParsedExpressionSubclasses(
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
                    )
                ],
                else_expr=ParsedExpressionSubclasses(
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='integers',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[SELECT row_number() OVER () FROM sales;] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='ROW_NUMBER',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='row_number',
                children=[],
                partitions=[],
                orders=[],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='sales',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[SELECT row_number() OVER (ORDER BY time) FROM sales;] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='ROW_NUMBER',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='row_number',
                children=[],
                partitions=[],
                orders=[
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['time']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='sales',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[SELECT row_number() OVER (PARTITION BY region ORDER BY time) FROM sales;] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=WindowExpression(
                type='ROW_NUMBER',
                clazz='WINDOW',
                alias='',
                catalog='',
                schema_name='',
                function_name='row_number',
                children=[],
                partitions=[
                    ParsedExpressionSubclasses(
                        __root__=ColumnRefExpression(
                            type='COLUMN_REF',
                            clazz='COLUMN_REF',
                            alias='',
                            column_names=['region']
                        )
                    )
                ],
                orders=[
                    OrderByNode(
                        type=<OrderType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        null_order=<OrderByNullType.ORDER_DEFAULT: 'ORDER_DEFAULT'>,
                        expression=ParsedExpressionSubclasses(
                            __root__=ColumnRefExpression(
                                type='COLUMN_REF',
                                clazz='COLUMN_REF',
                                alias='',
                                column_names=['time']
                            )
                        )
                    )
                ],
                filter_expr=None,
                ignore_nulls=False,
                start=<WindowBoundary.UNBOUNDED_PRECEDING: 'UNBOUNDED_PRECEDING'>,
                end=<WindowBoundary.CURRENT_ROW_RANGE: 'CURRENT_ROW_RANGE'>,
                start_expr=None,
                end_expr=None,
                offset_expr=None,
                default_expr=None
            )
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(
        __root__=BaseTableRef(
            alias='',
            sample=None,
            type='BASE_TABLE',
            schema_name='',
            table_name='sales',
            catalog_name='',
            column_name_alias=[]
        )
    )
)
'''

snapshots['test_sql[select * from duckdb_tables] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select * from range(0, 10)] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select 0::DECIMAL(15, 6)] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select 0::STRUCT(a INT)] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                        child_types=['a', LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None)]
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select 0::USER_TYPE] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select 1 * 1] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select 1] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select []::boolean[]] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select frog from frogs where height > 5 and leader = true] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['frog'])
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
                                    type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
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
                                            type=LogicalType(id=<LogicalTypeId.VARCHAR: 'VARCHAR'>, type_info=None),
                                            value='t',
                                            is_null=False
                                        )
                                    )
                                ),
                                cast_type=LogicalType(id=<LogicalTypeId.BOOLEAN: 'BOOLEAN'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select frog from frogs] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['frog'])
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[],
    group_expressions=[],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select frog.* EXCLUDE age from frogs] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select frog.age from frogs] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql[select list_apply([1, 2, 3], x => x * 2)] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
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
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
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
                                            type=LogicalType(id=<LogicalTypeId.INTEGER: 'INTEGER'>, type_info=None),
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
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
    from_table=TableRefSubclasses(__root__=EmptyTableRef(alias='', sample=None, type='EMPTY'))
)
'''

snapshots['test_sql[select name from frogs GROUP BY age] 1'] = '''SelectNode(
    type='SELECT_NODE',
    modifiers=[],
    cte_map=CommonTableExpressionMap(map={}),
    select_list=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['name'])
        )
    ],
    where_clause=None,
    sample=None,
    qualify=None,
    having=None,
    group_sets=[{0}],
    group_expressions=[
        ParsedExpressionSubclasses(
            __root__=ColumnRefExpression(type='COLUMN_REF', clazz='COLUMN_REF', alias='', column_names=['age'])
        )
    ],
    aggregate_handling=<AggregateHandling.STANDARD_HANDLING: 'STANDARD_HANDLING'>,
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
'''

snapshots['test_sql_errors[select] 1'] = '''ErrorResponse(error=True, error_message='SELECT clause without selection list', error_type='parser')
'''

snapshots['test_sql_errors[set threads = 5] 1'] = '''ErrorResponse(
    error=True,
    error_message='Only SELECT statements can be serialized to json!',
    error_type='not implemented'
)
'''
