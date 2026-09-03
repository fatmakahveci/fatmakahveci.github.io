import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.has_title = False
        self.has_viewport = False
        self.local_stylesheets = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "html":
            self.lang = attributes.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta" and attributes.get("name") == "viewport":
            self.has_viewport = True
        elif tag == "link" and attributes.get("rel") == "stylesheet":
            href = attributes.get("href", "")
            if href.startswith("/"):
                self.local_stylesheets.append(href)

    def handle_data(self, data):
        if self._in_title and data.strip():
            self.has_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False


class SiteSmokeTests(unittest.TestCase):
    def test_home_page_has_accessible_document_metadata(self):
        parser = DocumentParser()
        parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

        self.assertEqual(parser.lang, "en")
        self.assertTrue(parser.has_title)
        self.assertTrue(parser.has_viewport)

    def test_home_page_local_stylesheets_exist(self):
        parser = DocumentParser()
        parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

        self.assertTrue(parser.local_stylesheets)
        for href in parser.local_stylesheets:
            with self.subTest(href=href):
                self.assertTrue((ROOT / href.lstrip("/")).is_file())


if __name__ == "__main__":
    unittest.main()
