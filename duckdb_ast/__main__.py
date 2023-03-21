"""
Call module directly to dump jsonschema

```sh
$ python3 -m duckdb_ast
```
"""

import json
from argparse import ArgumentParser

from duckdb_ast import get_schema


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", default="schema.json")
    args = parser.parse_args()
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(get_schema(), fh, indent=2)


if __name__ == "__main__":
    main()
