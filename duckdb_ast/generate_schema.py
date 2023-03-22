import json
from pathlib import Path
from typing import Any

import duckdb
from docutils import nodes
from docutils.core import publish_doctree
from pydantic import schema_of
from sphinx.application import Sphinx

from .models import Root

__all__ = ["generate_schema"]


def render_node(node):
    if isinstance(node, nodes.Text):
        return str(node)
    elif hasattr(node, "children"):
        return "\n".join(render_node(child) for child in node.children)


def render_field(has_description):
    res = publish_doctree(has_description["description"])

    has_description["description"] = render_node(res).strip()


def update_docs(root):
    if isinstance(root, dict):
        if "description" in root:
            render_field(root)
        for item in root.values():
            update_docs(item)
    elif isinstance(root, list):
        for item in root:
            update_docs(item)


def generate_schema() -> dict[str, Any]:
    "Returns jsonschema of DuckDB AST"

    docs = Path(__file__).parent.parent / "docs"

    srcdir = docs / "source"
    build = docs / "build"
    buildername = "html"
    Sphinx(
        srcdir=srcdir,
        confdir=srcdir,
        outdir=build / buildername,
        doctreedir=build / "doctrees",
        buildername=buildername,
    )

    schema = {"version": duckdb.__version__}
    schema.update(schema_of(Root))
    update_docs(schema)

    return schema


if __name__ == "__main__":
    schema = generate_schema()

    with open(Path(__file__).parent / "schema.json", "w") as fh:
        json.dump(schema, fh, indent=2)
