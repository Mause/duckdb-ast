import importlib
from pathlib import Path
from textwrap import dedent
from unittest.mock import MagicMock

from docutils.utils import Reporter
from pytest import MonkeyPatch, mark
from snapshottest.module import SnapshotTest

from .generate_schema import generate_schema


def test_schema_generation(snapshot: SnapshotTest):
    schema = generate_schema()
    schema.pop("version")
    snapshot.assert_match(schema)


@mark.parametrize(
    "comments,expected",
    [
        (
            dedent(
                """\
//===--------------------------------------------------------------------===//
// Struct Type
//===--------------------------------------------------------------------===//
struct StructTypeInfo : public ExtraTypeInfo {
    """
            ),
            "Struct Type",
        ),
        (
            dedent(
                """

//! Extra Type Info Type
enum class ExtraTypeInfoType : uint8_t {
        """
            ),
            "Extra Type Info Type",
        ),
        (
            dedent(
                """

//===
struct StructTypeInfo : public ExtraTypeInfo {
    """
            ),
            "",
        ),
    ],
)
def test_comment_extraction(comments: str, expected: str, monkeypatch: MonkeyPatch):
    monkeypatch.syspath_prepend(str(Path(__file__).parent.parent / "docs"))
    gh_link = importlib.import_module("gh_link")

    monkeypatch.setattr(gh_link, "get_file", lambda filename: comments.splitlines())

    assert (
        gh_link.get_doc(MagicMock(spec=Reporter), "src/include/duckdb/types.cpp#L4")
        == expected
    )
