import copy
import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    spec = importlib.util.spec_from_file_location(
        "discover_research_ideas", ROOT / "scripts" / "discover_research_ideas.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


engine = load_module()
CONFIG = json.loads((ROOT / "config" / "research-focus.json").read_text())


def sources():
    return {
        "doi:10.1/alpha": {
            "source_id": "doi:10.1/alpha",
            "database": "Europe PMC",
            "title": "Drug resistance states across patient tumors",
            "abstract": "A" * 100,
            "authors": "Author A",
            "published": "2026-09-01",
            "venue": "Journal",
            "url": "https://doi.org/10.1/alpha",
        },
        "arxiv:2609.12345": {
            "source_id": "arxiv:2609.12345",
            "database": "arXiv",
            "title": "Leakage-resistant treatment response models",
            "abstract": "B" * 100,
            "authors": "Author B",
            "published": "2026-09-02",
            "venue": "arXiv preprint",
            "url": "https://arxiv.org/abs/2609.12345v2",
        },
    }


def valid_idea():
    return {
        "title": "Test transportable resistance-state signals across hospitals",
        "observation": "Recent studies report resistance-associated cell states in multiple tumor settings.",
        "scientific_problem": "It is unclear whether these states are transportable patient-level signals or study-specific artifacts.",
        "research_question": "Do pretreatment resistance-state scores predict response in an independent hospital cohort?",
        "hypothesis": "A compact resistance-state score will retain predictive value after clinical covariate adjustment.",
        "competing_explanation": "Apparent performance is caused by site, assay, or tumor-composition differences.",
        "impact_function": {
            "type": "precision-medicine",
            "primary": "Identify a reproducible signal that improves treatment-response stratification.",
            "secondary": "Clarify when cell-state measurements add value beyond routine covariates.",
        },
        "fixed_anchor": "Patient-level transportability of the resistance-state signal.",
        "floating_parameters": ["Expression platform", "Model family", "Tumor indication"],
        "assumptions": [
            {
                "text": "The cell state reflects biology shared across patients.",
                "type": "scientific",
                "risk": "high",
                "readout_weeks": 4,
                "test": "Check direction and effect stability by patient and site.",
            },
            {
                "text": "Available cohorts contain comparable outcomes and covariates.",
                "type": "technical",
                "risk": "medium",
                "readout_weeks": 2,
                "test": "Audit endpoints, missingness, and assay compatibility.",
            },
            {
                "text": "The score adds information beyond composition and clinical factors.",
                "type": "scientific",
                "risk": "high",
                "readout_weeks": 6,
                "test": "Compare nested patient-level models with prespecified covariates.",
            },
        ],
        "data_plan": {
            "required_data": "Pretreatment tumor profiles, outcomes, sites, and clinical covariates.",
            "independence_unit": "Patient or donor, never cells from the same patient.",
            "leakage_controls": "Fit normalization, feature selection, and tuning within training folds only.",
        },
        "strong_baselines": ["Clinical covariates only", "Regularized linear model"],
        "validation_plan": [
            "Lock the score and test it in an external independent cohort.",
            "Use orthogonal protein or imaging measurements where available.",
        ],
        "earliest_test": {
            "experiment": "Audit two cohorts and run a locked patient-level baseline comparison.",
            "estimated_weeks": 6,
            "success_threshold": "Positive adjusted effect with stable direction across sites.",
            "ambiguous_threshold": "Stable direction but wide uncertainty or modest added value.",
            "failure_threshold": "No transportable effect or performance below clinical baselines.",
        },
        "decision_tree": {
            "positive": "Validate prospectively designed endpoints in a third cohort.",
            "ambiguous": "Narrow the indication or improve measurement harmonization.",
            "negative": "Stop prediction work and publish the transportability boundary.",
        },
        "residual_value": "A negative result defines where resistance-state measurements fail to transport.",
        "why_now": "New patient-level datasets make a multi-site transportability test feasible.",
        "evidence": [
            {"source_id": "doi:10.1/alpha", "relevance": "Supports the resistance-state observation."},
            {"source_id": "arxiv:2609.12345", "relevance": "Motivates leakage-resistant model evaluation."},
        ],
        "scores": {
            "impact": 5,
            "tractability": 4,
            "novelty_potential": 3,
            "evidence_readiness": 4,
            "leverage": 4,
        },
    }


class SourceCollectionTests(unittest.TestCase):
    def test_arxiv_versions_are_deduplicated_and_old_entries_are_filtered(self):
        xml = """<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry><id>https://arxiv.org/abs/2609.12345v2</id><title>Recent response model</title>
          <summary>{recent}</summary><published>2026-09-02T00:00:00Z</published>
          <author><name>Researcher One</name></author></entry>
          <entry><id>https://arxiv.org/abs/2501.99999v1</id><title>Old response model</title>
          <summary>{old}</summary><published>2025-01-02T00:00:00Z</published>
          <author><name>Researcher Two</name></author></entry>
        </feed>""".format(recent="R" * 100, old="O" * 100)
        focus = {"query_terms": ["treatment response"]}
        with patch.object(engine, "http_get", return_value=xml):
            found, _ = engine.fetch_arxiv(focus, date(2026, 8, 21), 10)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["source_id"], "arxiv:2609.12345")

    def test_europe_pmc_handles_missing_book_details(self):
        payload = {
            "resultList": {
                "result": [{
                    "id": "1", "pmid": "123", "title": "A useful study",
                    "abstractText": "A" * 100, "bookOrReportDetails": None,
                    "firstPublicationDate": "2026-09-01",
                }]
            }
        }
        with patch.object(engine, "http_get", return_value=json.dumps(payload)):
            found, _ = engine.fetch_europe_pmc(
                {"query_terms": ["precision medicine"]}, "2026-08-21", "2026-09-04", 10
            )
        self.assertEqual(found[0]["source_id"], "pmid:123")
        self.assertEqual(found[0]["venue"], "")

    def test_similar_titles_ignore_formatting_and_stop_words(self):
        self.assertTrue(
            engine.similar_title(
                "A model for drug response in cancer",
                "Drug-response model for the cancer",
            )
        )

    def test_issue_prefix_does_not_hide_a_duplicate(self):
        self.assertTrue(
            engine.similar_title(
                "Test treatment response across hospitals",
                "[Idea] Test treatment response across hospitals",
            )
        )

    def test_openalex_reconstructs_abstracts(self):
        payload = {
            "results": [{
                "id": "https://openalex.org/W123",
                "doi": "https://doi.org/10.2/openalex",
                "title": "OpenAlex precision medicine study",
                "abstract_inverted_index": {
                    "Patient": [0], "level": [1], "treatment": [2], "response": [3],
                    "evidence": list(range(4, 84)),
                },
                "publication_date": "2026-09-02",
                "authorships": [{"author": {"display_name": "Researcher A"}}],
                "primary_location": {
                    "landing_page_url": "https://example.test/openalex",
                    "source": {"display_name": "Journal A"},
                },
            }]
        }
        with patch.object(engine, "http_get", return_value=json.dumps(payload)):
            found, _ = engine.fetch_openalex(
                {"query_terms": ["precision medicine"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertEqual(found[0]["source_id"], "doi:10.2/openalex")
        self.assertIn("Patient level treatment response", found[0]["abstract"])

    def test_crossref_removes_jats_markup(self):
        payload = {"message": {"items": [{
            "DOI": "10.2/crossref", "title": ["Crossref response study"],
            "abstract": "<jats:p>" + "Evidence " * 20 + "</jats:p>",
            "published-online": {"date-parts": [[2026, 9, 1]]},
            "author": [{"given": "Ada", "family": "Scientist"}],
            "container-title": ["Journal B"],
        }]}}
        with patch.object(engine, "http_get", return_value=json.dumps(payload)):
            found, _ = engine.fetch_crossref(
                {"query_terms": ["treatment response"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertNotIn("jats", found[0]["abstract"])
        self.assertEqual(found[0]["published"], "2026-09-01")

    def test_semantic_scholar_prefers_doi_identity(self):
        payload = {"data": [{
            "paperId": "paper-1", "title": "Semantic treatment response study",
            "abstract": "Evidence " * 20, "publicationDate": "2026-09-03",
            "venue": "Journal C", "url": "https://semanticscholar.org/paper-1",
            "externalIds": {"DOI": "10.2/semantic"},
            "authors": [{"name": "Researcher C"}],
        }]}
        with patch.object(engine, "http_get", return_value=json.dumps(payload)):
            found, _ = engine.fetch_semantic_scholar(
                {"query_terms": ["treatment response"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertEqual(found[0]["source_id"], "doi:10.2/semantic")

    def test_biorxiv_and_medrxiv_are_both_collected(self):
        def response(url, *args, **kwargs):
            server = "medrxiv" if "/medrxiv/" in url else "biorxiv"
            return json.dumps({
                "messages": [{"total": 1}],
                "collection": [{
                    "doi": f"10.1101/{server}", "title": f"{server} treatment response",
                    "abstract": "Treatment response evidence " * 10,
                    "authors": "Researcher D", "date": "2026-09-03",
                    "version": "1", "category": "bioinformatics",
                }],
            })
        with patch.object(engine, "http_get", side_effect=response):
            found, _ = engine.fetch_preprints(
                {"query_terms": ["treatment response"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertEqual({item["database"] for item in found}, {"bioRxiv", "medRxiv"})

    def test_clinical_trials_extracts_registered_studies(self):
        payload = {"studies": [{"protocolSection": {
            "identificationModule": {"nctId": "NCT123", "briefTitle": "Treatment response trial"},
            "descriptionModule": {"briefSummary": "Prospective treatment response evidence " * 8},
            "statusModule": {
                "studyFirstPostDateStruct": {"date": "2026-09-02"},
                "overallStatus": "RECRUITING",
            },
            "sponsorCollaboratorsModule": {"leadSponsor": {"name": "Research Institute"}},
            "conditionsModule": {"conditions": ["Cancer"]},
            "armsInterventionsModule": {"interventions": [{"name": "Therapy A"}]},
        }}]}
        with patch.object(engine, "http_get", return_value=json.dumps(payload)):
            found, _ = engine.fetch_clinical_trials(
                {"query_terms": ["treatment response"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertEqual(found[0]["source_id"], "nct:nct123")
        self.assertIn("RECRUITING", found[0]["venue"])

    def test_geo_search_and_summary_extract_dataset_accessions(self):
        search = {"esearchresult": {"idlist": ["9001"]}}
        summary = {"result": {
            "uids": ["9001"],
            "9001": {
                "accession": "GSE9001", "title": "Treatment response dataset",
                "summary": "Patient-level treatment response expression data " * 8,
                "pdat": "2026/09/01", "gdsType": "Expression profiling",
            },
        }}
        with patch.object(engine, "http_get", side_effect=[json.dumps(search), json.dumps(summary)]):
            found, _ = engine.fetch_geo(
                {"query_terms": ["treatment response"]}, date(2026, 8, 21), date(2026, 9, 4), 10
            )
        self.assertEqual(found[0]["source_id"], "geo:gse9001")
        self.assertEqual(found[0]["published"], "2026-09-01")

    def test_source_balancing_preserves_specialist_databases(self):
        records = []
        for index in range(5):
            record = copy.deepcopy(next(iter(sources().values())))
            record.update({"source_id": f"general:{index}", "database": "General", "published": f"2026-09-0{index + 1}"})
            records.append(record)
        specialist = copy.deepcopy(records[0])
        specialist.update({"source_id": "trial:1", "database": "ClinicalTrials.gov"})
        selected = engine.balance_sources(records + [specialist], 4)
        self.assertIn("ClinicalTrials.gov", {item["database"] for item in selected})

    def test_one_database_failure_does_not_discard_other_results(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = copy.deepcopy(CONFIG)
            for settings in config["source_databases"].values():
                settings["enabled"] = False
            config["source_databases"]["europe_pmc"]["enabled"] = True
            config["source_databases"]["openalex"]["enabled"] = True
            (root / "config.json").write_text(json.dumps(config))
            (root / "ledger.json").write_text(json.dumps({
                "version": 1, "seen_sources": [], "generated_ideas": [], "runs": []
            }))
            records = []
            titles = [
                "Transportable cell states across hospitals",
                "Perturbation response in patient organoids",
                "Spatial niches driving acquired resistance",
                "Calibrated multimodal treatment biomarkers",
            ]
            for index, title in enumerate(titles):
                record = copy.deepcopy(next(iter(sources().values())))
                record.update({
                    "source_id": f"openalex:{index}", "database": "OpenAlex",
                    "title": title,
                })
                records.append(record)
            args = SimpleNamespace(
                config=str(root / "config.json"), ledger=str(root / "ledger.json"),
                output=str(root / "sources.json"), status_file=str(root / "status.json"),
                prompt_file=str(root / "prompt.txt"), focus=None, lookback_days=14,
                max_sources=40, max_ideas=3,
            )
            with patch.object(engine, "fetch_europe_pmc", side_effect=RuntimeError("temporary outage")), \
                 patch.object(engine, "fetch_openalex", return_value=(records, "query")), \
                 patch.object(engine, "existing_idea_titles", return_value=[]), \
                 patch.dict("os.environ", {"GITHUB_REPOSITORY": "owner/repo"}):
                engine.fetch_command(args)
            status = json.loads((root / "status.json").read_text())
            self.assertTrue(status["ready"])
            self.assertEqual(status["source_count"], 4)
            self.assertIn("Europe PMC: temporary outage", status["errors"])


class ValidationTests(unittest.TestCase):
    def test_complete_idea_passes_and_is_scored(self):
        cleaned = engine.validate_idea(valid_idea(), sources(), CONFIG)
        self.assertEqual(cleaned["priority_score"], 4.15)
        self.assertEqual(len(cleaned["evidence"]), 2)

    def test_unknown_citation_is_rejected(self):
        proposal = valid_idea()
        proposal["evidence"][0]["source_id"] = "doi:invented"
        with self.assertRaisesRegex(RuntimeError, "unknown or duplicate"):
            engine.validate_idea(proposal, sources(), CONFIG)

    def test_generated_markdown_links_are_neutralized(self):
        proposal = valid_idea()
        proposal["why_now"] = "See [untrusted link](https://malicious.example) before proceeding."
        cleaned = engine.validate_idea(proposal, sources(), CONFIG)
        self.assertIn(r"\[untrusted link\]", cleaned["why_now"])

    def test_scientific_and_technical_assumptions_are_required(self):
        proposal = valid_idea()
        for assumption in proposal["assumptions"]:
            assumption["type"] = "scientific"
        with self.assertRaisesRegex(RuntimeError, "both scientific and technical"):
            engine.validate_idea(proposal, sources(), CONFIG)

    def test_external_validation_is_required(self):
        proposal = valid_idea()
        proposal["validation_plan"] = ["Use internal cross-validation.", "Inspect subgroup stability."]
        with self.assertRaisesRegex(RuntimeError, "external or independent"):
            engine.validate_idea(proposal, sources(), CONFIG)

    def test_issue_body_uses_validated_source_links(self):
        cleaned = engine.validate_idea(valid_idea(), sources(), CONFIG)
        body = engine.render_issue(cleaned, sources(), "Cancer drug response")
        self.assertIn(engine.MARKER, body)
        self.assertIn("https://doi.org/10.1/alpha", body)
        self.assertIn("Patient or donor", body)
        self.assertIn("Positive → Continue", body)


class PublishingTests(unittest.TestCase):
    def test_publish_is_bounded_and_updates_the_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_file, ideas_file = root / "sources.json", root / "ideas.json"
            ledger_file, summary_file = root / "ledger.json", root / "summary.json"
            source_file.write_text(json.dumps({"sources": list(sources().values())}))
            cleaned = engine.validate_idea(valid_idea(), sources(), CONFIG)
            ideas_file.write_text(json.dumps({"focus": {"name": "Test focus"}, "ideas": [cleaned]}))
            ledger_file.write_text(json.dumps({"version": 1, "seen_sources": [], "generated_ideas": [], "runs": []}))
            args = SimpleNamespace(
                sources=str(source_file), ideas=str(ideas_file), ledger=str(ledger_file),
                summary=str(summary_file), max_ideas=1,
            )
            created = {"number": 12, "title": f"[Idea] {cleaned['title']}", "html_url": "https://example.test/issues/12"}
            with patch.dict("os.environ", {"GITHUB_REPOSITORY": "owner/repo"}), \
                 patch.object(engine, "existing_idea_titles", return_value=[]), \
                 patch.object(engine, "ensure_labels", return_value=["research-idea"]), \
                 patch.object(engine, "github_api", return_value=created) as api:
                engine.publish_command(args)
            self.assertEqual(api.call_count, 1)
            ledger = json.loads(ledger_file.read_text())
            self.assertEqual(ledger["generated_ideas"][0]["issue_number"], 12)
            self.assertEqual(len(ledger["seen_sources"]), 2)
            summary = json.loads(summary_file.read_text())
            self.assertEqual(summary["created"][0]["number"], 12)


if __name__ == "__main__":
    unittest.main()
