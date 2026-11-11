# 📊 India Tech Career Intelligence 2026

> **Understand the Market. Discover Your Direction.**  
> *Enterprise workforce career intelligence suite and interactive EDA dashboard.*  
> **Developed by: Team ELECTRIC EPOCHS** · *Manthan Mini Hackathon 2026*

---

## 🌟 Executive Summary

**India Tech Career Intelligence 2026** is a comprehensive workforce analytics platform and interactive exploratory data analysis (EDA) dashboard. The project investigates **100,000 verified Indian technology job requisitions** spanning January 1, 2026 to May 30, 2026 across 36 audited attributes.

The platform transforms raw job board data into actionable, evidence-backed career guidance for engineering students, fresh graduates, academic placement cells, and talent acquisition leaders.

---

## 🧭 Key Market Insights at a Glance

| Metric | Dataset Value | Analytical Significance |
| :--- | :--- | :--- |
| **Total Postings Analyzed** | **100,000** | Statistically representative nationwide tech hiring sample |
| **Permanent Roles** | **59,871 (59.9%)** | Robust permanent hiring baseline across enterprise tiers |
| **Early-Career Internships** | **40,129 (40.1%)** | Highly active early-talent recruitment pipeline |
| **Core Technical Domains** | **6 Categories** | AI/ML, Cloud, DevOps, Cybersecurity, Data Science, Web Dev |
| **Geographic Metros** | **8 Technology Hubs** | Multi-polar distribution (NCR, Southern Hubs, Western Hubs) |
| **Median Full-Time Salary** | **₹8.50 LPA** | Consistent baseline midpoint across all 6 technical domains |
| **Median Internship Stipend** | **₹30,000 / month** | 100% paid internships; Bangalore leads at ₹30,403/mo |
| **Work Mode Flexibility** | **79.7% Flexible** | 40% Remote, 40% Hybrid, 20% On-site across all domains |

---

## 📁 Repository Structure

```plaintext
INDIA TECH CAREER INTELLIGENCE - DASHBOARD/
│
├── DASHBOARD/                                   # Streamlit Interactive Dashboard
│   ├── app.py                                   # Main dashboard application entrypoint
│   ├── eda_charts.py                            # 20 colorful, dark-themed Seaborn & Matplotlib visualizations
│   ├── data_loader.py                           # Dual-engine data loader (Parquet / CSV)
│   ├── components.py                            # Reusable UI cards, headers, and footer components
│   ├── views.py                                 # Deep-dive analytical views
│   ├── theme.py                                 # Design system tokens and styling rules
│   ├── style.css                                # Standalone CSS styles
│   ├── DESIGN_SYSTEM.md                         # Visual design documentation
│   ├── requirements.txt                         # Dashboard runtime dependencies
│   └── data/
│       └── career_intelligence_data.parquet     # Compressed (2.4 MB) complete 100k-row production data
│
├── CODE_RESOURCE/                               # Data Engineering & Jupyter Notebooks
│   └── BATCH2_DIET_PATH2.ipynb                  # Complete step-by-step EDA Jupyter Notebook
│
├── Documents/                                   # Research & Strategy Reports
│   ├── Batch1_DIET_PATH2_Business Report.pptx   # Executive business presentation
│   └── TEAM2_DIET_PATH2_DocumentWorkFlow.pdf    # Comprehensive methodology & workflow documentation
│
├── requirements.txt                             # Root dependency specification
├── .gitignore                                   # Git ignore rules (excludes large >50MB CSV files)
└── README.md                                    # Project documentation and deployment guide
```

---

## 🎨 Interactive Dashboard Features

The dashboard is built using a modern dark tech aesthetic with glassmorphic cards, luminous metric chips, and colorful Seaborn/Matplotlib charts:

1. **📊 Job Categories & Roles:**
   - *Distribution of Job Categories* (`sns.barplot` with `Set2` palette & annotated counts)
   - *Employment Type Distribution* (Donut chart with `Set2` palette: 59.9% Full-time vs 40.1% Internships)
   - *Job Category Percentage Share* (Pie chart with `husl` palette)
   - *Job Categories vs Experience Levels* (Heatmap with `YlGnBu` colormap)

2. **🏢 Companies & Industries:**
   - *Top 10 Hiring Organizations* (HCLTech, Tech Mahindra, Cognizant, Swiggy, Cred, etc.)
   - *Company Type Distribution* (Top MNCs ~50.1%, Tech Startups ~33.3%, Fintech Unicorns ~16.6%)
   - *Top 10 Industries by Requisition Volume*
   - *Company Size Distribution* (10k+ employees, 1k-5k, 500-1000)

3. **💡 Skill Intelligence:**
   - *Top 10 Technical Skills* (Led by cross-domain anchors: **Python** [33,212] and **Linux** [33,134])
   - *Share of Postings by Skill-List Pattern* (Analysis of 6 canonical standardized bundles)
   - *Skill vs Job Category Co-Occurrence Matrix* (Heatmap with `YlGnBu` colormap)
   - *Skill-Count Distribution* (49.9% require 7 skills, 33.2% require 6 skills, 16.9% require 8 skills)

4. **📍 Location & Work Mode:**
   - *Top 10 Cities by Job Opportunities* (Chennai, Noida, Gurgaon, Delhi NCR, Pune, Mumbai, Hyderabad, Bangalore)
   - *Work Mode Distribution* (40% Remote, 40% Hybrid, 20% On-site)
   - *Work Mode Across Job Categories* (Stacked horizontal bar chart)
   - *City-Wise Work Mode Breakdown* (Proof of nationwide work-from-home adoption)

5. **💰 Compensation & Salaries:**
   - *Full-Time Tech Salary Distribution* (Tri-modal Histplot & KDE: Min ₹4.5L, Midpoint ₹8.5L, Max ₹12.5L)
   - *Salary Midpoint Box Plot Across Categories* (Tight interquartile range across all domains)
   - *Internship Monthly Stipend Distribution* (Emerald Green histogram & KDE; Q1 ₹22.5k, Median ₹30.0k, Q3 ₹37.5k)
   - *City Salary Midpoints & Q1-Q3 Spread* (Horizontal bar chart with error bounds, `mako` palette)

6. **🖼️ Complete Visual EDA Gallery:**
   - Continuous visual gallery showing all 20 charts for rapid review and presentation.

---

## ⚡ Data Engineering & Deploy-Ready Architecture

- **Large CSV Management:** The original raw CSV file is ~61 MB. To comply with GitHub repository best practices (<50 MB) and enable instant deployment, the cleaned dataset is serialized into a high-performance Apache Parquet format (`career_intelligence_data.parquet`, only **2.4 MB**).
- **Dual-Engine Data Loader:** `DASHBOARD/data_loader.py` dynamically auto-detects the data source:
  - In cloud deployment: Instantly loads the 2.4 MB Parquet file in < 0.2 seconds.
  - In local development: Seamlessly falls back to the raw CSV if present in `CODE_RESOURCE/`.

---

## 🚀 Local Installation & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/mounikarayapalli/INDIA-TECH-CAREER-INTELLIGENCE.git
cd INDIA-TECH-CAREER-INTELLIGENCE
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Dashboard
```bash
python -m streamlit run DASHBOARD/app.py
```
Open **`http://localhost:8501`** in your browser.

---

## ☁️ How to Deploy on Streamlit Community Cloud (Free & Instant)

You can deploy this dashboard online in less than 2 minutes using **Streamlit Community Cloud**:

1. Go to **[share.streamlit.io](https://share.streamlit.io/)** and sign in with your GitHub account.
2. Click **"New app"** (or **"Create app"**).
3. Fill in the deployment details:
   - **Repository:** `mounikarayapalli/INDIA-TECH-CAREER-INTELLIGENCE`
   - **Branch:** `main`
   - **Main file path:** `DASHBOARD/app.py`
4. Click **"Deploy!"**.
5. Streamlit will automatically read `requirements.txt`, launch the container, and provide a permanent public URL (e.g. `https://india-tech-career-intelligence.streamlit.app`).

---

## 👥 Project Team Attribution

* **Event:** Manthan Mini Hackathon 2026
* **Project Name:** CareerScope – India Tech Career Intelligence 2026
* **Engineering Team:** **Team ELECTRIC EPOCHS**
* **Repository:** [mounikarayapalli/INDIA-TECH-CAREER-INTELLIGENCE](https://github.com/mounikarayapalli/INDIA-TECH-CAREER-INTELLIGENCE)

---
*CareerScope | India Tech Career Intelligence 2026 | Developed by Team ELECTRIC EPOCHS.*
