import json
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "img":
            self.images.append(values)
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_required_sections_exist(self):
        self.assertTrue({"main", "portfolio", "framework", "decision-tree", "workflow"}.issubset(self.parser.ids))
        self.assertIn("Research Portfolio", self.parser.title)

    def test_internal_assets_exist(self):
        for relative in ["assets/styles.css", "assets/app.js", "assets/mark.svg", "data/portfolio.json"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_images_have_alt_text(self):
        self.assertTrue(self.parser.images)
        self.assertTrue(all("alt" in image for image in self.parser.images))

    def test_issue_and_source_links_exist(self):
        joined = "\n".join(self.parser.links)
        self.assertIn("deep-evaluation.yml", joined)
        self.assertIn("quick-research-idea.yml", joined)
        self.assertIn("10.1016/j.cell.2024.03.012", joined)

    def test_public_data_is_valid_and_contains_no_sensitive_fields(self):
        data = json.loads((ROOT / "data" / "portfolio.json").read_text())
        self.assertEqual(data["version"], 1)
        self.assertIsInstance(data["ideas"], list)
        self.assertNotIn("body", json.dumps(data).lower())

    def test_javascript_does_not_inject_remote_html(self):
        script = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
        self.assertNotIn("innerHTML", script)
        self.assertIn("textContent", script)


if __name__ == "__main__":
    unittest.main()
