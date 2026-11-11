# CareerScope — India Tech Career Intelligence Dashboard (2026)

> **Understand the Market. Discover Your Direction.**  
> *Enterprise workforce intelligence suite developed by **Team ELECTRIC EPOCHS**.*

---

## 1. Executive Summary

**CareerScope** is a high-density, evidence-based workforce analytics product built for engineering students, academic placement cells, and tech recruiters across India. It processes **100,000 verified tech vacancy records** across 36 audited attributes spanning **January 1, 2026 to May 30, 2026**.

The dashboard adheres strictly to an editorial enterprise design standard, utilizing custom color palettes, subtle 1px borders, and clear typographic hierarchy rather than generic corporate templates.

---

## 2. Design System Tokens & Brand Identity

* **Brand Name:** CareerScope
* **Tagline:** *Understand the Market. Discover Your Direction.*
* **Design Tone:** Premium enterprise analytics with a modern editorial feel (Calm, trustworthy, evidence-backed).
* **Typography:** `Manrope` (Headings, -0.02em tracking) paired with `Inter` (Body, KPIs, Data tables).

### Signature Color Palette
* **Forest Teal (`#183A37`):** Primary brand, navigation shell, primary actions, and anchor charts.
* **Muted Brass (`#D6A85F`):** Highlights, milestones, key KPIs, top salary deciles.
* **Warm Ivory (`#F5F3ED`):** Foundational canvas background replacing harsh glare.
* **Slate Ink (`#263746`):** Typography, structural headings, axis labels, and high-contrast metrics.
* **Sage (`#A9BDB5`):** Secondary charts, baseline distributions, and comparative categories.
* **Dusty Coral (`#D9A69B`):** Secondary highlights, alerts, and benchmark deltas.

---

## 3. Product Features & Analytical Modules

1. **Market Overview:**
   * Instant macro perspective across 100k verified postings.
   * Dynamic 6-KPI grid: Total Postings, Full-Time (59,871), Internships (40,129), Categories (6), Original Columns (33), Original Missing (33,499).
   * **Market Snapshot:** Live natural-language synthesis panel explaining active dataset splits.
   * Donut distributions for Full-time vs Internship and Work Modes; horizontal bar charts for domains and top cities.
2. **Job & Company Intelligence:**
   * Role hierarchy, employer classification (Top MNC 50.1%, Startup 33.3%, Fintech Unicorn 16.6%), and company size distributions.
   * Top 10 recruiting organizations led by HCLTech, Tech Mahindra, Cognizant, Swiggy, Cred.
   * **Job Explorer:** Interactive category selector displaying related titles, sample counts, and granular salary spans.
   * Real-world impact playbook for placement cells and students.
3. **Skill Intelligence (Key Differentiating Section):**
   * Top 10 technical skills led by cross-domain anchors: **Python** (33,212) and **Linux** (33,134).
   * Skill-count distribution (49.9% 7 skills, 33.2% 6 skills, 16.9% 8 skills).
   * **Skill vs. Category Heatmap:** Custom color-scaled co-occurrence matrix.
   * **Skill Explorer:** Inspect canonical technology bundles, occurrence rates, and associated titles.
   * **Methodology Alert:** Preserves and documents the 6 canonical template bundles limitation.
4. **Location Intelligence:**
   * Regional distribution across India's 8 primary tech corridors.
   * State-wise rankings led by Maharashtra (24,895 / 24.9%) and Tamil Nadu / UP (~12.6k).
   * City-wise salary midpoints (~₹8.50 LPA) and internship stipends (led by Bangalore at ₹30,403/mo).
   * **Location Explorer:** Detailed metro inspection including leading employers and work-mode splits.
   * Spatial tech map with accurate geographic coordinates.
5. **Work Mode & Experience Intelligence:**
   * Universal 40% Remote / 40% Hybrid / 20% On-site allocation across all engineering categories.
   * Seniority criteria: 59.9% Mid-Senior (2-4y) vs 40.1% Freshers (0-1y).
   * Education criteria: Evenly balanced between Bachelor's Degrees, MCA/MSc, and B.E./B.Tech.
   * Inbound applicant distribution (median 247 apps/post).
   * **Opportunity Comparison:** Side-by-side empirical benchmark of any two engineering domains.
   * **Methodological Caution:** Clarifies that applicant volume reflects platform visibility, not selection odds.
6. **Compensation Intelligence:**
   * **Strict Stream Isolation (Problem Statement 6):** Full-time annual salary (₹ LPA) isolated from monthly internship stipends (INR/mo).
   * Tab A (Full-Time): Salary midpoints, percentiles (Q1: ₹7.12L, Median: ₹8.50L, Q3: ₹9.87L), box plots, range spreads.
   * Tab B (Internships): Monthly stipend distributions (Q1: ₹22,464, Median: ₹29,959, Q3: ₹37,392), city comparisons, quartile tables.
   * **Compensation Comparator:** Interactive comparator benchmarking two domains across Median, Q1, Q3, and record counts.
7. **Data Quality Audit & Integrity Report:**
   * Missing-value analysis (33,499 nulls in raw `probation_period` -> 0 in cleaned production dataset).
   * Duplicate audit: 0 exact full-row duplicates; 13,448 legitimate multi-slot requisitions investigated.
   * Validation suite: Chronological dates (`deadline >= posted`), non-negative salaries, INR currency integrity.
   * Cleaning log and audit comparison table.
8. **Executive Career Insights & Strategic Playbook:**
   * 5 evidence-backed career pillars synthesized across all modules.
   * Finding, supporting chart, practical student interpretation, and explicit analytical limitation for every insight.

---

## 4. How to Launch the Dashboard

### Prerequisites
* Python 3.10+
* Required packages: `streamlit`, `pandas`, `numpy`, `matplotlib`, `altair`

### Startup Command
From the project root directory, run:
```bash
python -m streamlit run DASHBOARD/app.py
```
Or navigate into the `DASHBOARD` directory:
```bash
cd DASHBOARD
python -m streamlit run app.py
```

The application will launch on `http://localhost:8501`.

---

## 5. Project Team Attribution
* **Project Name:** CareerScope – India Tech Career Intelligence 2026
* **Event:** Manthan Mini Hackathon 2026
* **Engineering Team:** **Team ELECTRIC EPOCHS**
* **Tagline:** *Understand the Market. Discover Your Direction.*
* **Footer:** `CareerScope | India Tech Career Intelligence 2026 | Developed by Team ELECTRIC EPOCHS.`
