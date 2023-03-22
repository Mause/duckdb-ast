from io import StringIO
from typing import cast

from pytest import mark
from rich.console import Console
from snapshottest.module import SnapshotTest

from . import SuccessResponse, parse_sql


@mark.parametrize(
    "sql",
    [
        "select 1",
        "select * from range(0, 10)",
        "select * from duckdb_tables",
        "select frog from frogs",
        "select frog from frogs where height > 5 and leader = true",
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
        "SELECT 1 < 1, 1 <= 2",
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
        "SELECT 'Math' IN ('CS', 'Math'), X NOT IN ('CS', 'Math')",
        "SELECT a BETWEEN x AND y",
        "SELECT a NOT BETWEEN x AND y",
        "SELECT expression IS NOT NULL",
        "SELECT 2 IS DISTINCT FROM NULL, NULL IS NOT DISTINCT FROM NULL",
        "SELECT 2 < 3, 2 > 3, 2 <= 3, 4 >= NULL, NULL = NULL, 2 <> 2",
        "SELECT EXISTS(SELECT * FROM grades WHERE course='Math');",
        "SELECT 'Math' IN (SELECT course FROM grades);",
        """
        SELECT *
        FROM grades grades_parent
        WHERE grade=
            (SELECT MIN(grade)
             FROM grades
             WHERE grades.course=grades_parent.course);
        """,
        "SELECT MIN(COLUMNS(*)), COUNT(COLUMNS(*)) from numbers;",
        "SELECT a.* FROM (SELECT {'x':1, 'y':2, 'z':3} as a);",
        """
        WITH ranked_functions as (
            SELECT
                schema_name,
                function_name,
                row_number() over (partition by schema_name order by function_name) as function_rank
            FROM duckdb_functions()
        )
        SELECT
            *
        FROM ranked_functions
        WHERE
            function_rank < 3;
        """,
        """
        WITH RECURSIVE tag_hierarchy(id, source, path) AS (
  SELECT id, name, [name] AS path
  FROM tag
  WHERE subclassof IS NULL
UNION ALL
  SELECT tag.id, tag.name, list_prepend(tag.name, tag_hierarchy.path)
  FROM tag, tag_hierarchy
  WHERE tag.subclassof = tag_hierarchy.id
)
SELECT path
FROM tag_hierarchy
WHERE source = 'Oasis';
        """,
    ],
)
def test_sql(sql, snapshot: SnapshotTest):
    root = parse_sql(sql)
    assert not root.error, root.error_message
    fh = StringIO()

    root = cast(SuccessResponse, root)

    statements = root.statements
    assert len(statements) == 1

    Console(width=120, file=fh).print(statements[0])
    snapshot.assert_match(fh.getvalue())
