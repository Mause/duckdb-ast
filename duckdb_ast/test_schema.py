from snapshottest.module import SnapshotTest

import duckdb_ast.parse


def test_schema_generation(snapshot: SnapshotTest):
    snapshot.assert_match(duckdb_ast.parse.get_schema())
