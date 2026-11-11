"""
India Tech Career Intelligence 2026 - Modern EDA Dashboard
==========================================================
Ultra-clean, modern, visual-first workforce intelligence dashboard.
Developed by Team ELECTRIC EPOCHS.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import cached data loader
from data_loader import load_dataset

# Import all 20 verified EDA visualizations
from eda_charts import (
    plot_job_category_distribution,
    plot_employment_type_pie,
    plot_job_category_percentage_pie,
    plot_category_vs_experience_heatmap,
    plot_top_10_companies,
    plot_company_type_pie,
    plot_top_10_industries,
    plot_company_size_distribution,
    plot_top_10_skills,
    plot_skill_patterns_share,
    plot_skill_category_heatmap,
    plot_skill_count_distribution,
    plot_top_10_cities,
    plot_work_mode_donut,
    plot_work_mode_across_categories,
    plot_city_work_mode_distribution,
    plot_full_time_salary_distribution,
    plot_salary_box_by_category,
    plot_internship_stipend_histogram,
    plot_city_salary_midpoint_bars
)

# -----------------------------------------------------------------------------
# 1. STREAMLIT PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="India Tech Career Intelligence 2026 | EDA Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. MODERN DARK-THEME & GLASSMORPHIC STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Dark Theme Canvas */
    .stApp {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
        max-width: 1420px;
    }
    
    /* Top Header & Gradient Title */
    .dashboard-title {
        font-size: 2.25rem;
        font-weight: 900;
        letter-spacing: -0.025em;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
        display: inline-block;
    }
    .dashboard-subtitle {
        font-size: 0.95rem;
        color: #94a3b8;
        margin-bottom: 1.35rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Modern Glassmorphic KPI Cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 14px;
        margin-bottom: 1.6rem;
    }
    .metric-chip {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 0.9rem 0.75rem;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-chip:hover {
        transform: translateY(-2px);
        border-color: #38bdf8;
    }
    .metric-value {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .metric-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #94a3b8;
        font-weight: 600;
        margin-top: 0.3rem;
    }
    
    /* Modern Pill Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #111827;
        padding: 8px;
        border-radius: 14px;
        border: 1px solid #1f2937;
        margin-bottom: 1.4rem;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #94a3b8 !important;
        font-weight: 600;
        font-size: 0.92rem;
        padding: 8px 18px;
        transition: all 0.2s ease;
        border: none !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #f8fafc !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e293b, #0f172a) !important;
        color: #38bdf8 !important;
        border-bottom: 2px solid #38bdf8 !important;
        box-shadow: 0 2px 10px rgba(56, 189, 248, 0.25);
    }
    
    /* Section Headings */
    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    /* Plot Wrapper Card */
    .plot-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 0.75rem;
        margin-bottom: 1.35rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
    }
    
    /* Clean Footer */
    .footer-bar {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #64748b;
        font-size: 0.85rem;
        border-top: 1px solid #1e293b;
        margin-top: 2.5rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. LOAD DATASET
# -----------------------------------------------------------------------------
df = load_dataset()

# -----------------------------------------------------------------------------
# 4. TOP TITLE & METRIC STRIP
# -----------------------------------------------------------------------------
st.markdown('<div class="dashboard-title">📊 India Tech Career Intelligence 2026</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="dashboard-subtitle">'
    '<span>Exploratory Data Analysis (EDA) Dashboard</span> · '
    '<span style="color: #38bdf8;">100,000 Verified Postings</span> · '
    '<span>Team ELECTRIC EPOCHS</span>'
    '</div>',
    unsafe_allow_html=True
)

# Modern 6-Metric Bar
kpi_html = f"""
<div class="metric-grid">
    <div class="metric-chip">
        <div class="metric-value" style="color: #38bdf8;">100,000</div>
        <div class="metric-label">Total Postings</div>
    </div>
    <div class="metric-chip">
        <div class="metric-value" style="color: #34d399;">59,871</div>
        <div class="metric-label">Full-Time (59.9%)</div>
    </div>
    <div class="metric-chip">
        <div class="metric-value" style="color: #e879f9;">40,129</div>
        <div class="metric-label">Internships (40.1%)</div>
    </div>
    <div class="metric-chip">
        <div class="metric-value" style="color: #fbbf24;">6</div>
        <div class="metric-label">Tech Domains</div>
    </div>
    <div class="metric-chip">
        <div class="metric-value" style="color: #fb7185;">₹8.50 LPA</div>
        <div class="metric-label">Median Salary</div>
    </div>
    <div class="metric-chip">
        <div class="metric-value" style="color: #2dd4bf;">₹30,000</div>
        <div class="metric-label">Median Stipend/mo</div>
    </div>
</div>
"""
st.markdown(kpi_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. MODERN TOP TABS NAVIGATION
# -----------------------------------------------------------------------------
tab_cats, tab_comps, tab_skills, tab_locs, tab_sal, tab_all = st.tabs([
    "📊 Job Categories & Roles",
    "🏢 Companies & Industries",
    "💡 Skill Intelligence",
    "📍 Location & Work Mode",
    "💰 Compensation & Salaries",
    "🖼️ All Visualizations (Gallery)"
])

# =============================================================================
# TAB 1: JOB CATEGORIES & ROLES
# =============================================================================
with tab_cats:
    st.markdown('<div class="section-title">📊 Job Category & Employment Distributions</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig1 = plot_job_category_distribution(df)
        st.pyplot(fig1, use_container_width=True)
        plt.close(fig1)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig2 = plot_employment_type_pie(df)
        st.pyplot(fig2, use_container_width=True)
        plt.close(fig2)
        st.markdown('</div>', unsafe_allow_html=True)
        
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig3 = plot_job_category_percentage_pie(df)
        st.pyplot(fig3, use_container_width=True)
        plt.close(fig3)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig4 = plot_category_vs_experience_heatmap(df)
        st.pyplot(fig4, use_container_width=True)
        plt.close(fig4)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 2: COMPANIES & INDUSTRIES
# =============================================================================
with tab_comps:
    st.markdown('<div class="section-title">🏢 Hiring Organizations & Industry Sectors</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig5 = plot_top_10_companies(df)
        st.pyplot(fig5, use_container_width=True)
        plt.close(fig5)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig6 = plot_company_type_pie(df)
        st.pyplot(fig6, use_container_width=True)
        plt.close(fig6)
        st.markdown('</div>', unsafe_allow_html=True)
        
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig7 = plot_top_10_industries(df)
        st.pyplot(fig7, use_container_width=True)
        plt.close(fig7)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig8 = plot_company_size_distribution(df)
        st.pyplot(fig8, use_container_width=True)
        plt.close(fig8)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 3: SKILL INTELLIGENCE
# =============================================================================
with tab_skills:
    st.markdown('<div class="section-title">💡 Technical Skills Demand & Co-Occurrence Matrix</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig9 = plot_top_10_skills(df)
        st.pyplot(fig9, use_container_width=True)
        plt.close(fig9)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig10 = plot_skill_patterns_share(df)
        st.pyplot(fig10, use_container_width=True)
        plt.close(fig10)
        st.markdown('</div>', unsafe_allow_html=True)
        
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig11 = plot_skill_category_heatmap(df)
        st.pyplot(fig11, use_container_width=True)
        plt.close(fig11)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig12 = plot_skill_count_distribution(df)
        st.pyplot(fig12, use_container_width=True)
        plt.close(fig12)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 4: LOCATION & WORK MODE
# =============================================================================
with tab_locs:
    st.markdown('<div class="section-title">📍 Geographic Tech Hubs & Work Mode Policy</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig13 = plot_top_10_cities(df)
        st.pyplot(fig13, use_container_width=True)
        plt.close(fig13)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig14 = plot_work_mode_donut(df)
        st.pyplot(fig14, use_container_width=True)
        plt.close(fig14)
        st.markdown('</div>', unsafe_allow_html=True)
        
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig15 = plot_work_mode_across_categories(df)
        st.pyplot(fig15, use_container_width=True)
        plt.close(fig15)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig16 = plot_city_work_mode_distribution(df)
        st.pyplot(fig16, use_container_width=True)
        plt.close(fig16)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 5: COMPENSATION & SALARIES
# =============================================================================
with tab_sal:
    st.markdown('<div class="section-title">💰 Compensation Economics & Salary Spread</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig17 = plot_full_time_salary_distribution(df)
        st.pyplot(fig17, use_container_width=True)
        plt.close(fig17)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig18 = plot_salary_box_by_category(df)
        st.pyplot(fig18, use_container_width=True)
        plt.close(fig18)
        st.markdown('</div>', unsafe_allow_html=True)
        
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig19 = plot_internship_stipend_histogram(df)
        st.pyplot(fig19, use_container_width=True)
        plt.close(fig19)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig20 = plot_city_salary_midpoint_bars(df)
        st.pyplot(fig20, use_container_width=True)
        plt.close(fig20)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 6: FULL EDA GALLERY (ALL CHARTS IN ONE SEAMLESS VIEW)
# =============================================================================
with tab_all:
    st.markdown('<div class="section-title">🖼️ Complete EDA Visual Gallery (All 20 Charts)</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="color: #38bdf8; font-weight: 700; margin-bottom: 0.5rem;">SECTION 1: JOB CATEGORIES & ROLES</div>', unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g1 = plot_job_category_distribution(df)
        st.pyplot(fig_g1, use_container_width=True)
        plt.close(fig_g1)
        st.markdown('</div>', unsafe_allow_html=True)
    with g2:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g2 = plot_employment_type_pie(df)
        st.pyplot(fig_g2, use_container_width=True)
        plt.close(fig_g2)
        st.markdown('</div>', unsafe_allow_html=True)
        
    g3, g4 = st.columns(2)
    with g3:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g3 = plot_job_category_percentage_pie(df)
        st.pyplot(fig_g3, use_container_width=True)
        plt.close(fig_g3)
        st.markdown('</div>', unsafe_allow_html=True)
    with g4:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g4 = plot_category_vs_experience_heatmap(df)
        st.pyplot(fig_g4, use_container_width=True)
        plt.close(fig_g4)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div style="color: #38bdf8; font-weight: 700; margin: 1.5rem 0 0.5rem 0;">SECTION 2: COMPANIES & INDUSTRIES</div>', unsafe_allow_html=True)
    g5, g6 = st.columns(2)
    with g5:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g5 = plot_top_10_companies(df)
        st.pyplot(fig_g5, use_container_width=True)
        plt.close(fig_g5)
        st.markdown('</div>', unsafe_allow_html=True)
    with g6:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g6 = plot_company_type_pie(df)
        st.pyplot(fig_g6, use_container_width=True)
        plt.close(fig_g6)
        st.markdown('</div>', unsafe_allow_html=True)
        
    g7, g8 = st.columns(2)
    with g7:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g7 = plot_top_10_industries(df)
        st.pyplot(fig_g7, use_container_width=True)
        plt.close(fig_g7)
        st.markdown('</div>', unsafe_allow_html=True)
    with g8:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g8 = plot_company_size_distribution(df)
        st.pyplot(fig_g8, use_container_width=True)
        plt.close(fig_g8)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div style="color: #38bdf8; font-weight: 700; margin: 1.5rem 0 0.5rem 0;">SECTION 3: SKILL INTELLIGENCE</div>', unsafe_allow_html=True)
    g9, g10 = st.columns(2)
    with g9:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g9 = plot_top_10_skills(df)
        st.pyplot(fig_g9, use_container_width=True)
        plt.close(fig_g9)
        st.markdown('</div>', unsafe_allow_html=True)
    with g10:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g10 = plot_skill_patterns_share(df)
        st.pyplot(fig_g10, use_container_width=True)
        plt.close(fig_g10)
        st.markdown('</div>', unsafe_allow_html=True)
        
    g11, g12 = st.columns(2)
    with g11:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g11 = plot_skill_category_heatmap(df)
        st.pyplot(fig_g11, use_container_width=True)
        plt.close(fig_g11)
        st.markdown('</div>', unsafe_allow_html=True)
    with g12:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g12 = plot_skill_count_distribution(df)
        st.pyplot(fig_g12, use_container_width=True)
        plt.close(fig_g12)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div style="color: #38bdf8; font-weight: 700; margin: 1.5rem 0 0.5rem 0;">SECTION 4: LOCATION & WORK MODE</div>', unsafe_allow_html=True)
    g13, g14 = st.columns(2)
    with g13:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g13 = plot_top_10_cities(df)
        st.pyplot(fig_g13, use_container_width=True)
        plt.close(fig_g13)
        st.markdown('</div>', unsafe_allow_html=True)
    with g14:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g14 = plot_work_mode_donut(df)
        st.pyplot(fig_g14, use_container_width=True)
        plt.close(fig_g14)
        st.markdown('</div>', unsafe_allow_html=True)
        
    g15, g16 = st.columns(2)
    with g15:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g15 = plot_work_mode_across_categories(df)
        st.pyplot(fig_g15, use_container_width=True)
        plt.close(fig_g15)
        st.markdown('</div>', unsafe_allow_html=True)
    with g16:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g16 = plot_city_work_mode_distribution(df)
        st.pyplot(fig_g16, use_container_width=True)
        plt.close(fig_g16)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div style="color: #38bdf8; font-weight: 700; margin: 1.5rem 0 0.5rem 0;">SECTION 5: COMPENSATION & SALARIES</div>', unsafe_allow_html=True)
    g17, g18 = st.columns(2)
    with g17:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g17 = plot_full_time_salary_distribution(df)
        st.pyplot(fig_g17, use_container_width=True)
        plt.close(fig_g17)
        st.markdown('</div>', unsafe_allow_html=True)
    with g18:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g18 = plot_salary_box_by_category(df)
        st.pyplot(fig_g18, use_container_width=True)
        plt.close(fig_g18)
        st.markdown('</div>', unsafe_allow_html=True)
        
    g19, g20 = st.columns(2)
    with g19:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g19 = plot_internship_stipend_histogram(df)
        st.pyplot(fig_g19, use_container_width=True)
        plt.close(fig_g19)
        st.markdown('</div>', unsafe_allow_html=True)
    with g20:
        st.markdown('<div class="plot-card">', unsafe_allow_html=True)
        fig_g20 = plot_city_salary_midpoint_bars(df)
        st.pyplot(fig_g20, use_container_width=True)
        plt.close(fig_g20)
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. MINIMAL CLEAN FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="footer-bar">
    <span style="color: #38bdf8; font-weight: 700;">CareerScope</span> · India Tech Career Intelligence 2026 · Developed by <b style="color: #f8fafc;">Team ELECTRIC EPOCHS</b>
</div>
""", unsafe_allow_html=True)
