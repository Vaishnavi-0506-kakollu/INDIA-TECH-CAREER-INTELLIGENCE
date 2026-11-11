"""
EDA Visualizations Module - India Tech Career Intelligence 2026
Extracted directly from the Exploratory Data Analysis (EDA) Jupyter Notebook.
Features modern, dark-themed, colorful Seaborn and Matplotlib visualizations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Theme Color Constants
DARK_BG = '#111827'       # Slate 900
CARD_BG = '#161e2e'       # Slightly elevated dark
TEXT_TITLE = '#F8FAFC'    # Crisp white heading
TEXT_LABEL = '#CBD5E1'    # Slate 300
TEXT_MUTED = '#94A3B8'    # Slate 400
GRID_COLOR = '#1F2937'    # Subtle grid
BORDER_COLOR = '#334155'  # Border line

def apply_dark_ax_styling(ax, title=""):
    """Applies clean modern dark theme to an axis."""
    ax.figure.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    if title:
        ax.set_title(title, fontsize=12.5, weight='bold', pad=12, color=TEXT_TITLE)
    ax.tick_params(colors=TEXT_MUTED, labelsize=8.5)
    ax.xaxis.label.set_color(TEXT_LABEL)
    ax.yaxis.label.set_color(TEXT_LABEL)
    ax.xaxis.label.set_size(9.5)
    ax.yaxis.label.set_size(9.5)
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(0.8)
    ax.grid(True, color=GRID_COLOR, linestyle='--', alpha=0.5, zorder=0)


# ==============================================================================
# 1. JOB CATEGORIES & ROLES
# ==============================================================================

def plot_job_category_distribution(df: pd.DataFrame):
    """Distribution of Job Categories using Seaborn Set2 palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    counts = df["job_category"].value_counts()
    
    sns.barplot(
        x=counts.index,
        y=counts.values,
        hue=counts.index,
        palette="Set2",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Distribution of Job Categories")
    
    for p in ax.patches:
        h = p.get_height()
        ax.annotate(f"{int(h):,}\n({h/len(df)*100:.1f}%)",
                    (p.get_x() + p.get_width() / 2., h / 2),
                    ha='center', va='center', fontsize=9, color='#0F172A', weight='bold')
        
    ax.set_xlabel("Job Category", weight='bold')
    ax.set_ylabel("Number of Postings", weight='bold')
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels([c.replace(" ", "\n") for c in counts.index], fontsize=8.5, color=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_employment_type_pie(df: pd.DataFrame):
    """Employment Type Distribution Donut Chart."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=130)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    counts = df["employment_type"].value_counts()
    colors = sns.color_palette("Set2", len(counts))
    
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        pctdistance=0.75,
        wedgeprops=dict(width=0.45, edgecolor=DARK_BG, linewidth=2.5)
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_weight("bold")
        at.set_color("#0F172A")
    for t in texts:
        t.set_fontsize(9.5)
        t.set_weight("bold")
        t.set_color(TEXT_LABEL)
        
    ax.set_title("Employment Type Distribution (Permanent vs Intern)", fontsize=12.5, weight='bold', pad=12, color=TEXT_TITLE)
    ax.text(0, 0, f"{len(df):,}\nTotal", ha="center", va="center", fontsize=11, weight="bold", color=TEXT_TITLE)
    ax.axis("equal")
    plt.tight_layout()
    return fig


def plot_job_category_percentage_pie(df: pd.DataFrame):
    """Job Category Percentage Distribution with HUSL palette."""
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=130)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    counts = df["job_category"].value_counts()
    colors = sns.color_palette("husl", len(counts))
    
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=[c.replace(" Engineering", "").replace(" Architecture", "") for c in counts.index],
        autopct="%1.1f%%",
        startangle=120,
        colors=colors,
        pctdistance=0.72,
        wedgeprops=dict(edgecolor=DARK_BG, linewidth=2)
    )
    for at in autotexts:
        at.set_fontsize(8.5)
        at.set_weight("bold")
        at.set_color("#FFFFFF")
    for t in texts:
        t.set_fontsize(8.5)
        t.set_color(TEXT_LABEL)
        
    ax.set_title("Job Category Share of Total Market", fontsize=12.5, weight='bold', pad=12, color=TEXT_TITLE)
    ax.axis("equal")
    plt.tight_layout()
    return fig


def plot_category_vs_experience_heatmap(df: pd.DataFrame):
    """Job Categories vs Experience Levels Heatmap with YlGnBu colormap."""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=130)
    ct = pd.crosstab(df["job_category"], df["experience_level"])
    
    sns.heatmap(
        ct,
        annot=True,
        fmt="d",
        cmap="YlGnBu",
        linewidths=0.8,
        linecolor=DARK_BG,
        cbar_kws={'label': 'Requisition Count'},
        ax=ax
    )
    apply_dark_ax_styling(ax, "Job Categories vs Experience Levels")
    ax.set_xlabel("Experience Level", weight='bold')
    ax.set_ylabel("Job Category", weight='bold')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=8.5, color=TEXT_LABEL)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=9, color=TEXT_LABEL)
    
    # Adjust colorbar text color
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color=TEXT_MUTED)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=TEXT_MUTED)
    cbar.ax.yaxis.label.set_color(TEXT_LABEL)
    
    plt.tight_layout()
    return fig


# ==============================================================================
# 2. COMPANIES & INDUSTRIES
# ==============================================================================

def plot_top_10_companies(df: pd.DataFrame):
    """Top 10 Companies by Number of Job Records with HUSL palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    top_orgs = df["company_name"].value_counts().head(10).sort_values(ascending=True)
    
    sns.barplot(
        x=top_orgs.values,
        y=top_orgs.index,
        hue=top_orgs.index,
        palette="husl",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Top 10 Companies by Number of Job Postings")
    
    max_val = top_orgs.max()
    for p in ax.patches:
        w = p.get_width()
        ax.annotate(f" {int(w):,}",
                    (w, p.get_y() + p.get_height() / 2.),
                    va='center', ha='left', fontsize=8.5, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlim(0, max_val * 1.18)
    ax.set_xlabel("Number of Jobs", weight='bold')
    ax.set_ylabel("Company Name", weight='bold')
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_company_type_pie(df: pd.DataFrame):
    """Company Type Distribution with Set3 palette."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=130)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    counts = df["company_type"].value_counts()
    colors = sns.color_palette("Set3", len(counts))
    
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        pctdistance=0.75,
        wedgeprops=dict(width=0.48, edgecolor=DARK_BG, linewidth=2.5)
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_weight("bold")
        at.set_color("#0F172A")
    for t in texts:
        t.set_fontsize(9)
        t.set_weight("bold")
        t.set_color(TEXT_LABEL)
        
    ax.set_title("Company Type Distribution", fontsize=12.5, weight='bold', pad=12, color=TEXT_TITLE)
    ax.axis("equal")
    plt.tight_layout()
    return fig


def plot_top_10_industries(df: pd.DataFrame):
    """Top 10 Industries by Job Records with Set2 palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    top_ind = df["industry"].value_counts().head(10).sort_values(ascending=True)
    
    sns.barplot(
        x=top_ind.values,
        y=top_ind.index,
        hue=top_ind.index,
        palette="Set2",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Top 10 Industries by Job Records")
    
    max_val = top_ind.max()
    for p in ax.patches:
        w = p.get_width()
        ax.annotate(f" {int(w):,}",
                    (w, p.get_y() + p.get_height() / 2.),
                    va='center', ha='left', fontsize=8.5, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlim(0, max_val * 1.18)
    ax.set_xlabel("Number of Jobs", weight='bold')
    ax.set_ylabel("Industry Sector", weight='bold')
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_company_size_distribution(df: pd.DataFrame):
    """Company Size Distribution with HUSL palette."""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=130)
    counts = df["company_size"].value_counts()
    
    sns.barplot(
        x=counts.index,
        y=counts.values,
        hue=counts.index,
        palette="husl",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Company Size Distribution (Employee Count)")
    
    for p in ax.patches:
        h = p.get_height()
        ax.annotate(f"{int(h):,}\n({h/len(df)*100:.1f}%)",
                    (p.get_x() + p.get_width() / 2., h / 2),
                    ha='center', va='center', fontsize=9, color='#FFFFFF', weight='bold')
        
    ax.set_xlabel("Company Size Bracket", weight='bold')
    ax.set_ylabel("Number of Postings", weight='bold')
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels(counts.index, color=TEXT_LABEL)
    plt.tight_layout()
    return fig


# ==============================================================================
# 3. SKILL INTELLIGENCE
# ==============================================================================

def plot_top_10_skills(df: pd.DataFrame):
    """Top 10 Most Frequently Listed Skills with HUSL palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    
    all_skills = []
    for s_str in df["skills_extracted"].dropna():
        for s in s_str.split(","):
            s_clean = s.strip()
            if s_clean:
                all_skills.append(s_clean)
                
    skill_counts = pd.Series(all_skills).value_counts().head(10).sort_values(ascending=True)
    
    sns.barplot(
        x=skill_counts.values,
        y=skill_counts.index,
        hue=skill_counts.index,
        palette="husl",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Top 10 In-Demand Technical Skills Across Postings")
    
    max_val = skill_counts.max()
    for p in ax.patches:
        w = p.get_width()
        pct = (w / len(df)) * 100
        ax.annotate(f" {int(w):,} ({pct:.1f}%)",
                    (w, p.get_y() + p.get_height() / 2.),
                    va='center', ha='left', fontsize=8.5, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlim(0, max_val * 1.25)
    ax.set_xlabel("Listing Frequency in Job Specifications", weight='bold')
    ax.set_ylabel("Technical Skill / Tool", weight='bold')
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_skill_patterns_share(df: pd.DataFrame):
    """Share of Postings by Skill-List Pattern with Viridis palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    
    pattern_counts = df["skills_extracted"].value_counts()
    top_patterns = pattern_counts.head(6)
    share_pct = (top_patterns / len(df)) * 100
    
    labels = [
        "AI / ML Stack (Python, PyTorch, TF...)",
        "Web Dev Stack (HTML, CSS, React, Node...)",
        "Cloud Stack (AWS, Azure, CloudFormation...)",
        "DevOps Stack (Docker, K8s, Jenkins...)",
        "Cybersecurity Stack (Network Sec, Wireshark...)",
        "Data Science Stack (Python, SQL, Tableau...)"
    ][:len(top_patterns)]
    
    sns.barplot(
        x=share_pct.values,
        y=labels,
        hue=labels,
        palette="viridis",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Share of Postings by Skill-List Pattern (6 Standard Bundles)")
    
    for p in ax.patches:
        w = p.get_width()
        ax.annotate(f" {w:.2f}%",
                    (w, p.get_y() + p.get_height() / 2.),
                    va='center', ha='left', fontsize=9, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlim(0, 22)
    ax.set_xlabel("Share of Total Job Postings (%)", weight='bold')
    ax.set_ylabel("Canonical Skill Pattern", weight='bold')
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_skill_category_heatmap(df: pd.DataFrame):
    """Skill Frequency Across Job Categories Co-Occurrence Heatmap."""
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=130)
    
    all_skills = []
    for s_str in df["skills_extracted"].dropna():
        for s in s_str.split(","):
            s_clean = s.strip()
            if s_clean:
                all_skills.append(s_clean)
    top_12_skills = pd.Series(all_skills).value_counts().head(12).index.tolist()
    
    matrix_data = []
    for cat in df["job_category"].unique():
        sub = df[df["job_category"] == cat]
        for skill in top_12_skills:
            cnt = len(sub) if skill in sub["skills_extracted"].iloc[0] else 0
            matrix_data.append({"Category": cat, "Skill": skill, "Postings": cnt})
            
    df_matrix = pd.DataFrame(matrix_data).pivot(index="Skill", columns="Category", values="Postings").reindex(top_12_skills)
    
    sns.heatmap(
        df_matrix,
        annot=True,
        fmt=",d",
        cmap="YlGnBu",
        linewidths=0.8,
        linecolor=DARK_BG,
        cbar_kws={'label': 'Requisition Volume'},
        ax=ax
    )
    apply_dark_ax_styling(ax, "Skill vs Job Category Co-Occurrence Matrix")
    ax.set_xlabel("Job Category", weight='bold')
    ax.set_ylabel("Technical Skill", weight='bold')
    ax.set_xticklabels([c.replace(" ", "\n") for c in df_matrix.columns], fontsize=8, color=TEXT_LABEL)
    ax.set_yticklabels(df_matrix.index, fontsize=8.5, color=TEXT_LABEL)
    
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color=TEXT_MUTED)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=TEXT_MUTED)
    cbar.ax.yaxis.label.set_color(TEXT_LABEL)
    
    plt.tight_layout()
    return fig


def plot_skill_count_distribution(df: pd.DataFrame):
    """Skill-Count Distribution per Requisition with Set2 palette."""
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=130)
    counts = df["skill_count"].value_counts().sort_index()
    
    sns.barplot(
        x=[f"{int(k)} Skills" for k in counts.index],
        y=counts.values,
        hue=[f"{int(k)} Skills" for k in counts.index],
        palette="Set2",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Skill-Count Distribution (Stack Complexity)")
    
    for p in ax.patches:
        h = p.get_height()
        ax.annotate(f"{int(h):,}\n({h/len(df)*100:.1f}%)",
                    (p.get_x() + p.get_width() / 2., h / 2),
                    ha='center', va='center', fontsize=9.5, color='#0F172A', weight='bold')
        
    ax.set_xlabel("Number of Required Skills", weight='bold')
    ax.set_ylabel("Number of Postings", weight='bold')
    ax.tick_params(axis='x', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


# ==============================================================================
# 4. LOCATION & WORK MODE
# ==============================================================================

def plot_top_10_cities(df: pd.DataFrame):
    """Top 10 Cities by Job Opportunities with HUSL palette."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    top_cities = df["location_city"].value_counts().head(10).sort_values(ascending=True)
    
    sns.barplot(
        x=top_cities.values,
        y=top_cities.index,
        hue=top_cities.index,
        palette="husl",
        legend=False,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Top 10 Cities by Job Opportunities")
    
    max_val = top_cities.max()
    for p in ax.patches:
        w = p.get_width()
        pct = (w / len(df)) * 100
        ax.annotate(f" {int(w):,} ({pct:.1f}%)",
                    (w, p.get_y() + p.get_height() / 2.),
                    va='center', ha='left', fontsize=8.5, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlim(0, max_val * 1.25)
    ax.set_xlabel("Number of Jobs", weight='bold')
    ax.set_ylabel("City / Technology Hub", weight='bold')
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_work_mode_donut(df: pd.DataFrame):
    """Attractive Donut Chart for Work Mode with Vibrant Colors."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=130)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    counts = df["work_mode"].value_counts()
    
    vibrant_colors = ["#00D4FF", "#FF4F9A", "#FFD166"]
    
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=vibrant_colors[:len(counts)],
        pctdistance=0.75,
        wedgeprops=dict(width=0.45, edgecolor=DARK_BG, linewidth=2.5)
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_weight("bold")
        at.set_color("#0F172A")
    for t in texts:
        t.set_fontsize(9.5)
        t.set_weight("bold")
        t.set_color(TEXT_LABEL)
        
    ax.set_title("Work Mode Distribution", fontsize=12.5, weight='bold', pad=12, color=TEXT_TITLE)
    ax.text(0, 0, f"{len(df):,}\nRoles", ha="center", va="center", fontsize=11, weight="bold", color=TEXT_TITLE)
    ax.axis("equal")
    plt.tight_layout()
    return fig


def plot_work_mode_across_categories(df: pd.DataFrame):
    """Work Mode Across Job Categories (Fixed without height argument bug)."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    ct = pd.crosstab(df["job_category"], df["work_mode"], normalize="index") * 100
    ct = ct[["Remote", "Hybrid", "On-site"]]
    
    vibrant_colors = ["#00D4FF", "#FF4F9A", "#FFD166"]
    # In pandas DataFrame.plot(kind='barh'), bar thickness is width, NOT height!
    ct.plot(
        kind="barh",
        stacked=True,
        ax=ax,
        color=vibrant_colors,
        edgecolor=DARK_BG,
        linewidth=1.2,
        width=0.55
    )
    apply_dark_ax_styling(ax, "Work Mode Across Job Categories (%)")
    ax.set_xlabel("Percentage (%)", weight='bold')
    ax.set_ylabel("Job Category", weight='bold')
    ax.set_xlim(0, 100)
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    
    leg = ax.legend(title="Work Mode", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True, facecolor=CARD_BG, edgecolor=BORDER_COLOR)
    plt.setp(leg.get_texts(), color=TEXT_LABEL)
    plt.setp(leg.get_title(), color=TEXT_TITLE)
    
    plt.tight_layout()
    return fig


def plot_city_work_mode_distribution(df: pd.DataFrame):
    """Work Mode Distribution by City (Fixed without height argument bug)."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=130)
    ct = pd.crosstab(df["location_city"], df["work_mode"], normalize="index") * 100
    ct = ct[["Remote", "Hybrid", "On-site"]]
    
    vibrant_colors = ["#00D4FF", "#FF4F9A", "#FFD166"]
    # In pandas DataFrame.plot(kind='barh'), bar thickness is width, NOT height!
    ct.plot(
        kind="barh",
        stacked=True,
        ax=ax,
        color=vibrant_colors,
        edgecolor=DARK_BG,
        linewidth=1.2,
        width=0.55
    )
    apply_dark_ax_styling(ax, "Work Mode Distribution by City (%)")
    ax.set_xlabel("Percentage (%)", weight='bold')
    ax.set_ylabel("City", weight='bold')
    ax.set_xlim(0, 100)
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    
    leg = ax.legend(title="Work Mode", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True, facecolor=CARD_BG, edgecolor=BORDER_COLOR)
    plt.setp(leg.get_texts(), color=TEXT_LABEL)
    plt.setp(leg.get_title(), color=TEXT_TITLE)
    
    plt.tight_layout()
    return fig


# ==============================================================================
# 5. COMPENSATION & SALARIES
# ==============================================================================

def plot_full_time_salary_distribution(df: pd.DataFrame):
    """Full-Time Tech Salary Distribution (Min, Mid, Max) Histogram & KDE."""
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=130)
    
    df_ft = df[df["employment_type"] == "Full-time"].copy()
    if "salary_midpoint" not in df_ft.columns:
        df_ft["salary_midpoint"] = (df_ft["salary_minimum"] + df_ft["salary_maximum"]) / 2.0
        
    c_min = '#00d4aa'   # Vibrant Teal for Minimum
    c_mid = '#a855f7'   # Electric Purple for Midpoint
    c_max = '#ff6b6b'   # Vibrant Coral for Maximum
    
    sns.histplot(df_ft['salary_minimum'] / 1e5, kde=True, color=c_min, 
                 label='Minimum (Median: ₹4.5L)', stat='density', bins=30, alpha=0.35, ax=ax, zorder=3)
    sns.histplot(df_ft['salary_midpoint'] / 1e5, kde=True, color=c_mid, 
                 label='Midpoint (Median: ₹8.5L)', stat='density', bins=30, alpha=0.45, ax=ax, zorder=3)
    sns.histplot(df_ft['salary_maximum'] / 1e5, kde=True, color=c_max, 
                 label='Maximum (Median: ₹12.5L)', stat='density', bins=30, alpha=0.35, ax=ax, zorder=3)
    
    apply_dark_ax_styling(ax, "Full-Time Tech Salary Distribution: Min, Midpoint & Max (N = 59,871)")
    
    # Medians
    ax.axvline(df_ft['salary_minimum'].median() / 1e5, color=c_min, linestyle='--', linewidth=2, zorder=4)
    ax.axvline(df_ft['salary_midpoint'].median() / 1e5, color=c_mid, linestyle='--', linewidth=2.5, zorder=4)
    ax.axvline(df_ft['salary_maximum'].median() / 1e5, color=c_max, linestyle='--', linewidth=2, zorder=4)
    
    ax.set_xlabel("Annual Compensation (₹ Lakhs per Annum / LPA)", weight='bold')
    ax.set_ylabel("Probability Density", weight='bold')
    ax.set_xlim(2, 18)
    
    leg = ax.legend(frameon=True, facecolor=CARD_BG, edgecolor=BORDER_COLOR, fontsize=9, loc='upper right')
    plt.setp(leg.get_texts(), color=TEXT_LABEL)
    
    plt.tight_layout()
    return fig


def plot_salary_box_by_category(df: pd.DataFrame):
    """Tech Salary Midpoint Comparison Across Job Categories (Box Plot)."""
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=130)
    
    df_ft = df[df["employment_type"] == "Full-time"].copy()
    if "salary_midpoint" not in df_ft.columns:
        df_ft["salary_midpoint"] = (df_ft["salary_minimum"] + df_ft["salary_maximum"]) / 2.0
        
    order_cats = df_ft.groupby("job_category")["salary_midpoint"].median().sort_values(ascending=False).index.tolist()
    cat_palette = ['#38bdf8', '#818cf8', '#c084fc', '#f472b6', '#fb923c', '#34d399']
    
    sns.boxplot(
        data=df_ft,
        y='job_category',
        x=df_ft['salary_midpoint'] / 1e5,
        order=order_cats,
        hue='job_category',
        hue_order=order_cats,
        legend=False,
        palette=cat_palette[:len(order_cats)],
        width=0.55,
        linewidth=1.3,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Salary Midpoint Comparison Across Job Categories (₹ LPA)")
    
    for i, cat in enumerate(order_cats):
        med_val = df_ft[df_ft["job_category"] == cat]["salary_midpoint"].median() / 1e5
        cnt = (df_ft["job_category"] == cat).sum()
        ax.text(med_val + 0.15, i, f"₹{med_val:.2f}L (n={cnt:,})", 
                va='center', ha='left', fontsize=8.5, weight='bold', color=TEXT_TITLE)
        
    ax.set_xlabel("Derived Salary Midpoint (₹ Lakhs)", weight='bold')
    ax.set_ylabel("Job Category", weight='bold')
    ax.set_xlim(3.5, 15)
    ax.tick_params(axis='y', colors=TEXT_LABEL)
    plt.tight_layout()
    return fig


def plot_internship_stipend_histogram(df: pd.DataFrame):
    """Internship Stipend Distribution (Histogram & KDE) in Emerald Green."""
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=130)
    
    df_int = df[df["employment_type"] == "Internship"].copy()
    stip_color = '#10b981' # Vibrant Emerald Green
    
    sns.histplot(
        df_int['stipend_amount'] / 1e3,
        kde=True,
        color=stip_color,
        stat='density',
        bins=28,
        alpha=0.45,
        edgecolor='#34d399',
        linewidth=1.2,
        ax=ax,
        zorder=3
    )
    apply_dark_ax_styling(ax, "Internship Stipend Distribution (N = 40,129 Internship Postings)")
    
    q1 = df_int['stipend_amount'].quantile(0.25) / 1e3
    med = df_int['stipend_amount'].median() / 1e3
    q3 = df_int['stipend_amount'].quantile(0.75) / 1e3
    
    ax.axvline(q1, color='#34d399', linestyle=':', linewidth=2, label=f"Q1: ₹{q1:.1f}k", zorder=4)
    ax.axvline(med, color='#f43f5e', linestyle='--', linewidth=2.4, label=f"Median: ₹{med:.1f}k", zorder=4)
    ax.axvline(q3, color='#34d399', linestyle=':', linewidth=2, label=f"Q3: ₹{q3:.1f}k", zorder=4)
    ax.axvspan(q1, q3, color=stip_color, alpha=0.12, label='IQR (Middle 50% of Interns)', zorder=2)
    
    ax.set_xlabel("Monthly Stipend (₹ Thousands INR / Month)", weight='bold')
    ax.set_ylabel("Probability Density", weight='bold')
    ax.set_xlim(12, 48)
    
    leg = ax.legend(frameon=True, facecolor=CARD_BG, edgecolor=BORDER_COLOR, fontsize=9, loc='upper right')
    plt.setp(leg.get_texts(), color=TEXT_LABEL)
    
    plt.tight_layout()
    return fig


def plot_city_salary_midpoint_bars(df: pd.DataFrame):
    """Geographic Salary Midpoints & Range Spread with Mako palette."""
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=130)
    
    df_ft = df[df["employment_type"] == "Full-time"].copy()
    if "salary_midpoint" not in df_ft.columns:
        df_ft["salary_midpoint"] = (df_ft["salary_minimum"] + df_ft["salary_maximum"]) / 2.0
        
    city_stats = df_ft.groupby("location_city")["salary_midpoint"].agg(
        median=lambda x: x.median() / 1e5,
        q1=lambda x: x.quantile(0.25) / 1e5,
        q3=lambda x: x.quantile(0.75) / 1e5,
        count="count"
    ).sort_values(by="median", ascending=True)
    
    cities = city_stats.index.tolist()
    midpoints = city_stats["median"].tolist()
    q1_vals = city_stats["q1"].tolist()
    q3_vals = city_stats["q3"].tolist()
    counts = city_stats["count"].tolist()
    
    xerr_lower = [m - q1 for m, q1 in zip(midpoints, q1_vals)]
    xerr_upper = [q3 - m for m, q3 in zip(midpoints, q3_vals)]
    asymmetric_err = [xerr_lower, xerr_upper]
    
    city_palette = sns.color_palette("mako", n_colors=len(cities))
    y_positions = np.arange(len(cities))
    
    bars = ax.barh(y_positions, midpoints, xerr=asymmetric_err, color=city_palette,
                   edgecolor=BORDER_COLOR, height=0.55, capsize=4, 
                   error_kw={'elinewidth': 1.4, 'ecolor': '#94a3b8'}, zorder=3)
    apply_dark_ax_styling(ax, "Tech Salary Midpoint & Spread Across Indian Cities (₹ LPA)")
    
    for idx, (m_val, n_val) in enumerate(zip(midpoints, counts)):
        ax.text(m_val - 0.4, idx, f"₹{m_val:.2f}L", va='center', ha='right', fontsize=9, weight='bold', color='#FFFFFF')
        ax.text(q3_vals[idx] + 0.15, idx, f"(n={n_val:,})", va='center', ha='left', fontsize=8.5, color=TEXT_TITLE)
        
    ax.set_yticks(y_positions)
    ax.set_yticklabels(cities, fontsize=9.5, color=TEXT_LABEL, weight='bold')
    ax.set_xlabel("Median Salary Midpoint (₹ Lakhs) with Q1-Q3 Bounds", weight='bold')
    ax.set_ylabel("Technology Hub City", weight='bold')
    ax.set_xlim(0, 12.0)
    plt.tight_layout()
    return fig
