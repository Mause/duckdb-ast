import json
from importlib.resources import open_text
from typing import Any, Union

import duckdb
from pydantic import parse_raw_as

from .models import ErrorResponse, Root, SuccessResponse

__all__ = [
    "parse_sql_to_json",
    "get_schema",
    "parse_sql",
]


def escape_sql(sql: str) -> str:
    "Escapes quotes in an SQL string"
    return sql.replace('"', '""').replace("'", "''")


def parse_sql_to_json(sql: str) -> str:
    "Returns raw (unparsed) DuckDB AST JSON"
    duckdb.install_extension("json")
    duckdb.load_extension("json")

    inner = f"select json_serialize_sql('{escape_sql(sql)}')"
    res = duckdb.execute(inner)
    assert res
    (ast,) = res.fetchone()

    return ast


def parse_sql(sql: str) -> Union[ErrorResponse, SuccessResponse]:
    "Parses DuckDB flavoured SQL"
    ast = parse_sql_to_json(sql)
    return parse_raw_as(Root, ast).__root__


def get_schema() -> dict[str, Any]:
    """
    Returns DuckDB AST jsonschema contained within package
    """
    with open_text(__package__, "schema.json") as fh:
        return json.load(fh)
