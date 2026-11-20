#!/usr/bin/env python3
"""Check links in the production Hugo output without making network requests."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path: Path):
        super().__init__()
        self.links: list[str] = []
        self.anchors: set[str] = set()
        self.language = ""
        self.canonical = ""
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if anchor := attributes.get("id"):
            self.anchors.add(anchor)
        if tag == "a":
            if anchor := attributes.get("name"):
                self.anchors.add(anchor)
            if href := attributes.get("href"):
                self.links.append(href)
        if tag == "html":
            self.language = attributes.get("lang", "")
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href", "")


def check_site(public: Path) -> int:
    root = public.resolve()
    pages = {path: Page(path) for path in root.rglob("*.html")}

    errors = []
    for name, lang in (("index.html", "de"), ("en/index.html", "en")):
        page = pages.get(root / name)
        if page is None or page.language != lang:
            errors.append(f"{name}: expected a rendered page with lang={lang!r}")

    home = pages.get(root / "index.html")
    base_url = home.canonical if home else ""
    base = urlsplit(base_url)
    if base.scheme not in {"http", "https"} or not base.netloc:
        errors.append("index.html: expected an absolute canonical URL")
        return report(errors, len(pages), 0)

    checked = 0
    for source, page in sorted(pages.items()):
        relative = source.relative_to(root).as_posix()
        route = relative.removesuffix("index.html") if source.name == "index.html" else relative
        source_url = urljoin(base_url, route)
        for href in page.links:
            target_url = urlsplit(urljoin(source_url, href))
            if target_url.scheme not in {"http", "https"} or target_url.netloc != base.netloc:
                continue

            checked += 1
            path = unquote(target_url.path)
            if not path.startswith(base.path):
                errors.append(f"{relative}: {href!r} points outside the built site")
                continue
            target = (root / path.removeprefix(base.path).lstrip("/")).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"{relative}: {href!r} has no generated target")
                continue

            fragment = unquote(target_url.fragment)
            if fragment and target in pages and fragment not in pages[target].anchors:
                errors.append(f"{relative}: {href!r} refers to a missing anchor")

    return report(errors, len(pages), checked)


def report(errors: list[str], pages: int, checked: int) -> int:
    for error in errors:
        print(error)
    print(f"Checked {checked} internal links across {pages} HTML files. Errors: {len(errors)}.")
    return int(bool(errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public", type=Path, help="Hugo output directory")
    raise SystemExit(check_site(parser.parse_args().public))
