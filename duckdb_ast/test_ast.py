from pytest import mark
from snapshottest.snapshot import Snapshot

import duckdb_ast.parse


@mark.parametrize(
    'sql',
    [
        "select 1",
        "select * from range(0, 10)",
        "select * from duckdb_tables",
        "select frog from frogs",
        "select frog from frogs where height > 5 and leader = true",
        "create table dummy as select 1",
    ])

def test_sql(sql, snapshot: Snapshot):
    snapshot.assert_match(duckdb_ast.parse.parse_sql(sql))
