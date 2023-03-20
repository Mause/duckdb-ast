from snapshottest.snapshot import Snapshot

import duckdb_ast.parse


def test_schema_generation(snapshot: Snapshot):
    snapshot.assert_match(duckdb_ast.parse.get_schema())
