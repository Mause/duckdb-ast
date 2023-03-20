from pytest import fixture
from snapshottest.pytest import PyTestSnapshotTest


class Snap(PyTestSnapshotTest):
    @property
    def test_name(self):
        original = super().test_name

        return original.replace("'", "\\'")


@fixture()
def snapshot(request):
    with Snap(request) as snap:
        yield snap
