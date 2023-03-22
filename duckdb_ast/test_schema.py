from snapshottest.module import SnapshotTest

from .generate_schema import get_schema


def test_schema_generation(snapshot: SnapshotTest):
    schema = get_schema()
    schema.pop("version")
    snapshot.assert_match(schema)
