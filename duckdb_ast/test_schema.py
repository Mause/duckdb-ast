from snapshottest.module import SnapshotTest

from .generate_schema import generate_schema


def test_schema_generation(snapshot: SnapshotTest):
    schema = generate_schema()
    schema.pop("version")
    snapshot.assert_match(schema)
