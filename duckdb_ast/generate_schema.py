import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, cast

import duckdb
from docutils.core import Publisher
from docutils.io import StringInput, StringOutput
from pydantic import TypeAdapter
from sphinx.application import Sphinx
from sphinx.builders.text import TextBuilder
from sphinx.util.docutils import sphinx_domains

from duckdb_ast.models import Root

__all__ = ["generate_schema"]


def render_field(has_description: dict[str, str], publisher: Publisher) -> None:
    publisher.set_source(has_description["description"])
    publisher.publish()

    has_description["description"] = write_to_string(
        publisher.app.builder, publisher
    ).strip()


def update_docs(root: object, publisher: Publisher) -> None:
    if isinstance(root, dict):
        if "description" in root:
            render_field(root, publisher)
        for item in root.values():
            update_docs(item, publisher)
    elif isinstance(root, list):
        for item in root:
            update_docs(item, publisher)


def generate_schema() -> dict[str, Any]:
    """
    Generate jsonschema for DuckDB AST

    Fetches docstrings from github, and inserts current DuckDB version
    """

    schema = {"version": duckdb.__version__}
    schema.update(TypeAdapter(Root).json_schema())

    with sphinx() as (app, publisher):
        update_docs(schema, publisher)

    return schema


@contextmanager
def sphinx():
    docs = Path(__file__).parent.parent / "docs"
    srcdir = docs / "source"
    build = docs / "build"
    buildername = "text"
    app = Sphinx(
        srcdir=str(srcdir),
        confdir=str(srcdir),
        outdir=str(build / buildername),
        doctreedir=str(build / "doctrees"),
        buildername=buildername,
        confoverrides={"extensions": ["gh_link"]},
    )
    env = app.env
    env.prepare_settings("docname")
    env.srcdir = "<string>"
    publisher = app.registry.get_publisher(app, "restructuredtext")
    publisher.source_class = StringInput
    publisher.app = app

    schema = {"version": duckdb.__version__}
    schema.update(TypeAdapter(Root).json_schema())

    with sphinx_domains(app.env):
        yield app, publisher
    app.events.emit("build-finished")


def write_to_string(builder: TextBuilder, publisher: Publisher) -> str:
    document = publisher.document
    builder.prepare_writing(set())
    destination = StringOutput(encoding="utf-8")
    builder.writer.write(document, destination)
    return cast(bytes, destination.destination).decode()


if __name__ == "__main__":
    schema = generate_schema()

    with open(Path(__file__).parent / "schema.json", "w") as fh:
        json.dump(schema, fh, indent=2)
