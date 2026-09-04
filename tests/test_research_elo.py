import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


elo = load_module("research_elo", ROOT / "scripts" / "research_elo.py")
renderer = load_module("render_research_elo", ROOT / "scripts" / "render_research_elo.py")


def idea(number, title="Candidate", body="A testable research question"):
    return {
        "number": number,
        "title": f"[Idea] {title} {number}",
        "body": body,
        "user": {"login": "kayoderaheem"},
        "updated_at": "2026-09-04T00:00:00Z",
    }


class PrepareTests(unittest.TestCase):
    def run_prepare(self, ideas):
        with tempfile.TemporaryDirectory() as directory:
            old = os.getcwd()
            os.chdir(directory)
            try:
                args = SimpleNamespace(
                    issue=1,
                    prompt_file="prompt.txt",
                    context_file="context.json",
                    status_file="status.json",
                )
                with patch.object(elo, "fetch_ideas", return_value=ideas):
                    elo.prepare(args)
                return (
                    json.loads(Path("context.json").read_text()),
                    json.loads(Path("status.json").read_text()),
                    Path("prompt.txt").read_text(),
                )
            finally:
                os.chdir(old)

    def test_first_idea_is_published_without_failed_comparison(self):
        context, status, prompt_text = self.run_prepare([idea(1)])
        self.assertFalse(context["ready"])
        self.assertFalse(status["ready"])
        self.assertEqual(prompt_text, "")

    def test_two_ideas_create_risk_aware_prompt(self):
        context, status, prompt_text = self.run_prepare([idea(1), idea(2)])
        self.assertTrue(context["ready"])
        self.assertTrue(status["ready"])
        self.assertEqual(len(context["pairs"]), 1)
        self.assertIn("EARLIEST DECISION", prompt_text)
        self.assertIn("patient- or donor-level separation", prompt_text)
        self.assertIn("main_risk", prompt_text)

    def test_missing_target_fails_clearly(self):
        with tempfile.TemporaryDirectory() as directory:
            args = SimpleNamespace(
                issue=9,
                prompt_file=f"{directory}/prompt.txt",
                context_file=f"{directory}/context.json",
                status_file=f"{directory}/status.json",
            )
            with patch.object(elo, "fetch_ideas", return_value=[idea(1)]):
                with self.assertRaisesRegex(RuntimeError, "open owner-authored"):
                    elo.prepare(args)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.context = {
            "pairs": [
                {"pair_id": "p1", "A": 1, "B": 2},
                {"pair_id": "p2", "A": 1, "B": 3},
            ]
        }

    def result(self):
        return {
            "comparisons": [
                {
                    "pair_id": "p1",
                    "winner": "A",
                    "reason": "More informative",
                    "main_risk": "External validity",
                    "next_test": "Independent cohort",
                },
                {
                    "pair_id": "p2",
                    "winner": "draw",
                    "reason": "Insufficient evidence",
                    "main_risk": "No matched data",
                    "next_test": "Small feasibility audit",
                },
            ]
        }

    def test_valid_result_is_accepted_and_mentions_are_neutralized(self):
        result = self.result()
        result["comparisons"][0]["reason"] = "Ask @reviewers"
        validated = elo.validate_result(self.context, result)
        self.assertIn("@\u200breviewers", validated["p1"]["reason"])

    def test_duplicate_pair_is_rejected(self):
        result = self.result()
        result["comparisons"][1]["pair_id"] = "p1"
        with self.assertRaisesRegex(RuntimeError, "unknown or duplicate"):
            elo.validate_result(self.context, result)

    def test_extra_fields_are_rejected(self):
        result = self.result()
        result["comparisons"][0]["confidence"] = 0.8
        with self.assertRaisesRegex(RuntimeError, "exactly the required"):
            elo.validate_result(self.context, result)

    def test_elo_update_is_zero_sum(self):
        a, b = 1500.0, 1610.0
        expected_a = elo.expected(a, b)
        new_a = a + 24 * (1 - expected_a)
        new_b = b + 24 * (0 - (1 - expected_a))
        self.assertAlmostEqual((new_a - a) + (new_b - b), 0.0)


class RendererTests(unittest.TestCase):
    def test_compared_ideas_sort_before_uncompared_ideas(self):
        state = {
            "ratings": {
                "1": {"rating": 1512, "games": 1, "wins": 1, "draws": 0, "losses": 0}
            }
        }
        rows = renderer.build_rows(
            state,
            {1: idea(1), 2: idea(2)},
            "kayoderaheem/research-portfolio",
        )
        self.assertEqual([row["number"] for row in rows], [1, 2])
        self.assertEqual(rows[1]["games"], 0)

    def test_readme_renderer_preserves_surrounding_content(self):
        original = "before\n<!-- RESEARCH_ELO_START -->old<!-- RESEARCH_ELO_END -->\nafter\n"
        rendered = renderer.render_readme(original, [], "2026-09-04 12:00 UTC")
        self.assertTrue(rendered.startswith("before"))
        self.assertTrue(rendered.endswith("after\n"))
        self.assertIn("two open `[Idea]` issues", rendered)


if __name__ == "__main__":
    unittest.main()
