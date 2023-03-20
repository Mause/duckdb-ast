from io import StringIO

from pytest import mark
from rich.console import Console
from snapshottest.snapshot import Snapshot

import duckdb_ast.parse


@mark.parametrize(
    "sql",
    [
        "select 1",
        "select * from range(0, 10)",
        "select * from duckdb_tables",
        "select frog from frogs",
        "select frog from frogs where height > 5 and leader = true",
        "create table dummy as select 1",
        "select 1 * 1",
        "select frog.age from frogs",
        "select []::boolean[]",
        "select frog.* EXCLUDE age from frogs",
        """
SELECT *
EXCLUDE (timestamp_tz)
REPLACE (varchar.replace(chr(0), chr(10)) AS whatever)
FROM test_all_types()
        """,
    ],
)
def test_sql(sql, snapshot: Snapshot):
    parsed = duckdb_ast.parse.parse_sql(sql)
    file = StringIO()
    Console(width=120, file=file).print(parsed)
    snapshot.assert_match(file.getvalue())
