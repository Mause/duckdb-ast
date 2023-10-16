import shelve
from pathlib import Path
from typing import Callable, TypeVar
from urllib.request import urlopen

from docutils import nodes
from docutils.utils import Reporter
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

gh_ref = "88b1bfa74d2b79a51ffc4bab18ddeb6a034652f1"
template = "https://github.com/duckdb/duckdb/blob/{}/{}".format

T = TypeVar("T")
cache = shelve.open(str(Path(__file__).parent / "disk_cache.db"))


def cached(func: Callable[[str], T]) -> Callable[[str], T]:
    def wrapper(key: str) -> T:
        if key not in cache:
            cache[key] = func(key)
        return cache[key]

    return wrapper


@cached
def get_file(filename: str) -> list[str]:
    return (
        urlopen(f"https://raw.githubusercontent.com/duckdb/duckdb/{gh_ref}/{filename}")
        .read()
        .decode()
        .splitlines()
    )


BOUNDARY = "//==="
PREFIX = "//! "


def get_doc(reporter: Reporter, filename: str) -> str:
    sep = "#L"

    assert sep in filename, filename
    filename, lineno = filename.split(sep)
    lines = get_file(filename)

    start = int(lineno) - 1 - 1

    first = lines[start]

    try:
        if first.startswith(PREFIX):
            return prefixed(lines, start)
        if first.startswith(BOUNDARY):
            return bounded(lines, start)
    except IndexError:
        reporter.warning(f"failed to extract docs for {filename} on lineno {lineno}")

    return ""


def bounded(lines: list[str], start: int) -> str:
    start -= 1
    extracted: list[str] = []

    while not lines[start].startswith(BOUNDARY):
        extracted.insert(0, lines[start].split(" ", 1)[1].strip())
        start -= 1

    return "\n".join(extracted)


def prefixed(lines: list[str], start: int) -> str:
    extracted: list[str] = []

    while lines[start].startswith(PREFIX):
        extracted.insert(0, lines[start][len(PREFIX) :].strip())
        start -= 1

    return "\n".join(extracted)


class GitHubLinkDirective(SphinxDirective):
    """A custom directive that describes a recipe."""

    has_content = True
    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        sig = self.arguments[0]

        doc = get_doc(self.reporter, sig)
        ref = nodes.reference("", sig, refuri=template(gh_ref, sig))

        return [nodes.Text(doc), nodes.paragraph("", "", ref)]


def setup(app: Sphinx) -> dict:
    app.add_directive("gh_link", GitHubLinkDirective)

    app.connect("build-finished", lambda app: cache.close())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
