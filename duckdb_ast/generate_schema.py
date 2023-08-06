import json
from pathlib import Path
from typing import Any

import duckdb
from docutils import nodes
from docutils.core import Publisher
from docutils.io import StringInput
from pydantic import TypeAdapter
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util.docutils import sphinx_domains

from .models import Root

__all__ = ["generate_schema"]


def render_node(node: nodes.Node) -> str:
    if isinstance(node, nodes.Text):
        return str(node)
    else:
        sep = (
            " "
            if any(isinstance(child, addnodes.pending_xref) for child in node.children)
            else "\n"
        )

        return sep.join(render_node(child).strip() for child in node.children)


def render_field(has_description: dict[str, str], publisher: Publisher) -> None:
    publisher.set_source(has_description["description"])
    publisher.publish()

    has_description["description"] = render_node(publisher.document).strip()


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

    docs = Path(__file__).parent.parent / "docs"

    srcdir = docs / "source"
    build = docs / "build"
    buildername = "html"
    app = Sphinx(
        srcdir=srcdir,
        confdir=srcdir,
        outdir=build / buildername,
        doctreedir=build / "doctrees",
        buildername=buildername,
        confoverrides={"extensions": ["gh_link"]},
    )

    env = app.env
    env.prepare_settings("docname")
    env.srcdir = "<string>"
    publisher = app.registry.get_publisher(app, "restructuredtext")
    publisher.source_class = StringInput

    schema = {"version": duckdb.__version__}
    schema.update(TypeAdapter(Root).json_schema())

    with sphinx_domains(app.env):
        update_docs(schema, publisher)

    return schema


if __name__ == "__main__":
    schema = generate_schema()

    with open(Path(__file__).parent / "schema.json", "w") as fh:
        json.dump(schema, fh, indent=2)
