from snapshottest.module import SnapshotTest

from duckdb_ast import get_schema


def test_schema_generation(snapshot: SnapshotTest):
    snapshot.assert_match(get_schema())
