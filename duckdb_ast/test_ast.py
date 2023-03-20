from pytest import mark
from snapshottest.snapshot import Snapshot
from rich.console import Console
from rich import print
import duckdb_ast.parse
from io import StringIO

@mark.parametrize(
    'sql',
    [
        "select 1",
        "select * from range(0, 10)",
        "select * from duckdb_tables",
        "select frog from frogs",
        "select frog from frogs where height > 5 and leader = true",
        "create table dummy as select 1",
        "select 1 * 1",
        "select frog.age from frogs",
    ],
)
def test_sql(sql, snapshot: Snapshot):
    parsed = duckdb_ast.parse.parse_sql(sql)
    file = StringIO()
    Console(width=120, file=file).print(parsed)
    snapshot.assert_match(file.getvalue())
