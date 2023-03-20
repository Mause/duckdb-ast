from io import StringIO

from pytest import mark
from rich.console import Console
from snapshottest.module import SnapshotTest

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
        "select list_apply([1, 2, 3], x => x * 2)",
        "select 0::DECIMAL(15, 6)",
        "select 0::USER_TYPE",
        "select 0::STRUCT(a INT)",
        "select name from frogs GROUP BY age",
        "SELECT * FROM frogs USING SAMPLE 1% (BERNOULLI);",
        """
        select (select 1) as one
        """,
        """
        SELECT city, COUNT(*)
        FROM addresses
        GROUP BY city
        HAVING COUNT(*) >= 50;
        """,
        "SELECT '101010'::BIT",
        "SELECT 0::HUGEINT",
        "SELECT 0::UNION(num INT, str VARCHAR)",
        # r"SELECT '\xAA'::BLOB",
        "SELECT INTERVAL 1 YEAR",
        "SELECT NULL IS NULL",
        "SELECT DATE '1992-09-20'",
        "SELECT TIMESTAMP '1992-09-20 11:30:00'",
        "SELECT TIMESTAMPTZ '1992-09-20 11:30:00'",
        "SELECT i, CASE WHEN i>2 THEN 1 ELSE 0 END AS test FROM integers",
        "SELECT 'hello' COLLATE NOCASE",
        "SELECT 'Math' IN ('CS', 'Math');",
        "SELECT a BETWEEN x AND y",
        "SELECT a NOT BETWEEN x AND y",
        "SELECT expression IS NOT NULL",
    ],
)
def test_sql(sql, snapshot: SnapshotTest):
    parsed = duckdb_ast.parse.parse_sql(sql)
    fh = StringIO()
    Console(width=120, file=fh).print(parsed)
    snapshot.assert_match(fh.getvalue())
