(() => {
  "use strict";

  const REPO = "kayoderaheem/research-portfolio";
  const DATA_URL = "data/portfolio.json";

  const byId = (id) => document.getElementById(id);
  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  };

  const navToggle = document.querySelector(".nav-toggle");
  const nav = byId("site-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", () => {
      nav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  }

  const outcomeCopy = {
    positive: {
      kicker: "Selected branch · Continue",
      title: "Earn the right to scale.",
      body: "The initial signal is promising, but the claim should now survive stronger baselines, leakage-resistant validation, calibration checks, and an independent cohort.",
      steps: ["Freeze the primary endpoint before expansion.", "Compare against simple and established methods.", "Quantify uncertainty and subgroup stability.", "Seek orthogonal biological evidence."]
    },
    mixed: {
      kicker: "Selected branch · Refine",
      title: "Let one parameter float.",
      body: "A context-specific result often means the question is useful but the cohort, endpoint, modality, or scale is poorly matched. Change one constraint and preserve what the evidence supports.",
      steps: ["Identify the boundary condition behind the signal.", "Separate biological heterogeneity from measurement bias.", "Choose one parameter to change at a time.", "Write a narrower, falsifiable claim."]
    },
    negative: {
      kicker: "Selected branch · Pivot",
      title: "Use the failure as data.",
      body: "A failed primary signal should not trigger endless tuning. Ask what the failure rules out, turn the question around, and choose the branch with the greatest remaining information value.",
      steps: ["Stop optimization against the failed endpoint.", "Record which assumption was falsified.", "Test the strongest competing explanation.", "Park the project if no branch remains consequential."]
    }
  };

  const detail = byId("outcome-detail");
  document.querySelectorAll(".outcome").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".outcome").forEach((item) => item.classList.remove("is-active"));
      button.classList.add("is-active");
      const copy = outcomeCopy[button.dataset.outcome];
      if (!copy || !detail) return;
      detail.replaceChildren();
      detail.append(el("span", "detail-kicker", copy.kicker), el("h3", "", copy.title), el("p", "", copy.body));
      const list = el("ul");
      copy.steps.forEach((step) => list.append(el("li", "", step)));
      detail.append(list);
    });
  });

  function ideaCard(idea) {
    const card = el("article", "idea-card");
    const top = el("div", "idea-card-top");
    top.append(el("span", "idea-number", `Idea #${idea.number}`));
    const ratingText = idea.games > 0 ? `Elo ${Math.round(idea.rating)}` : "Awaiting comparison";
    top.append(el("span", "rating-pill", ratingText));
    card.append(top, el("h3", "", idea.title.replace(/^\[Idea\]\s*/i, "")));
    const record = idea.games > 0 ? `${idea.games} comparisons · ${idea.wins}W / ${idea.draws}D / ${idea.losses}L` : "Ready for assumption analysis and a second candidate idea.";
    card.append(el("p", "", record));
    const link = el("a", "", "Review the decision record →");
    link.href = idea.url || `https://github.com/${REPO}/issues/${idea.number}`;
    card.append(link);
    return card;
  }

  function renderPortfolio(data) {
    const ideas = Array.isArray(data.ideas) ? data.ideas : [];
    const evaluated = ideas.filter((idea) => Number(idea.games) > 0).length;
    const decisions = ideas.reduce((total, idea) => total + Number(idea.games || 0), 0);
    byId("idea-count").textContent = String(ideas.length);
    byId("evaluated-count").textContent = String(evaluated);
    byId("decision-count").textContent = String(decisions);

    const grid = byId("idea-grid");
    grid.replaceChildren();
    if (!ideas.length) {
      const empty = el("div", "empty-card");
      const copy = el("div");
      copy.append(el("span", "empty-kicker", "Portfolio ready · no ideas captured yet"));
      copy.append(el("h3", "", "Start with two competing questions, not one favorite solution."));
      copy.append(el("p", "", "Open two [Idea] issues. The workflow will compare their scientific value, expose the main risk, and recommend the earliest decision-changing test."));
      empty.append(copy, el("div", "empty-count", "0"));
      grid.append(empty);
    } else {
      ideas.slice(0, 6).forEach((idea) => grid.append(ideaCard(idea)));
    }

    const status = byId("portfolio-status");
    if (data.updated_at) {
      const updated = new Date(data.updated_at);
      status.textContent = `Synchronized from GitHub · ${updated.toLocaleDateString(undefined, {year: "numeric", month: "short", day: "numeric"})}`;
    } else {
      status.textContent = ideas.length ? "Portfolio synchronized from GitHub." : "The system is ready for its first two candidate ideas.";
    }
  }

  async function loadPortfolio() {
    try {
      const response = await fetch(`${DATA_URL}?v=${Date.now()}`, { cache: "no-store" });
      if (!response.ok) throw new Error(`Portfolio data returned ${response.status}`);
      renderPortfolio(await response.json());
    } catch (error) {
      renderPortfolio({ ideas: [] });
      byId("portfolio-status").textContent = "Live portfolio data is temporarily unavailable. Ideas remain accessible on GitHub.";
    }
  }

  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .08 });
    reveals.forEach((node) => observer.observe(node));
  } else {
    reveals.forEach((node) => node.classList.add("is-visible"));
  }

  byId("current-year").textContent = String(new Date().getFullYear());
  loadPortfolio();
})();
