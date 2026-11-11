"""
CareerScope - Core UI Components
================================
Modular components ensuring design consistency across all analytical views.
"""

from typing import Optional, List, Dict, Any
import pandas as pd
import numpy as np
import streamlit as st
from theme import (
    BRAND_NAME,
    COLOR_FOREST_TEAL,
    COLOR_MUTED_BRASS,
    COLOR_WARM_IVORY,
    COLOR_SLATE_INK,
    COLOR_SAGE,
    COLOR_DUSTY_CORAL,
    COLOR_CARD_BG,
    COLOR_CARD_BORDER,
    COLOR_BORDER_SUBTLE,
    COLOR_TEXT_MUTED,
    COLOR_TEAL_LIGHT,
    COLOR_BRASS_LIGHT,
    COLOR_CORAL_LIGHT
)

# Standard Product Footer Specification
FOOTER_TEXT = "CareerScope | India Tech Career Intelligence 2026 | Developed by Team ELECTRIC EPOCHS."

def render_top_header(
    page_title: str,
    page_subtitle: str,
    metadata: Dict[str, Any],
    filtered_count: int,
    total_count: int = 100_000,
    active_filters_summary: Optional[str] = None
) -> None:
    """
    Renders the compact top header containing:
    - Current page title & description
    - Dataset name & verified record count
    - Last updated information based on actual data
    - Live sample-size indicator
    """
    pct_retained = (filtered_count / total_count) * 100 if total_count > 0 else 100.0
    
    st.markdown(f"""
    <div style="background-color: {COLOR_CARD_BG}; border: 1px solid {COLOR_CARD_BORDER}; border-radius: 8px; padding: 1.1rem 1.4rem; margin-bottom: 1.25rem;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
            <div>
                <div style="font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; color: {COLOR_FOREST_TEAL};">
                    CareerScope Analytics Engine · Team ELECTRIC EPOCHS
                </div>
                <h1 style="margin: 0.2rem 0 0.25rem 0; font-size: 1.65rem; color: {COLOR_SLATE_INK};">
                    {page_title}
                </h1>
                <p style="margin: 0; color: {COLOR_TEXT_MUTED}; font-size: 0.88rem; max-width: 720px; line-height: 1.4;">
                    {page_subtitle}
                </p>
            </div>
            <div style="text-align: right; min-width: 260px;">
                <div style="display: inline-flex; align-items: center; gap: 6px; background: {COLOR_TEAL_LIGHT}; border: 1px solid #C8DBD7; padding: 3px 10px; border-radius: 20px; margin-bottom: 4px;">
                    <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background-color: {COLOR_FOREST_TEAL};"></span>
                    <span style="font-size: 0.74rem; font-weight: 700; color: {COLOR_FOREST_TEAL};">{metadata.get('dataset_name', 'India Tech Career Intelligence 2026')}</span>
                </div>
                <div style="font-size: 0.85rem; font-weight: 700; color: {COLOR_SLATE_INK}; margin-top: 2px;">
                    {filtered_count:,} <span style="font-weight: 400; color: {COLOR_TEXT_MUTED};">of {total_count:,} records</span> 
                    <span style="color: {COLOR_FOREST_TEAL}; font-size: 0.78rem; font-weight: 600;">({pct_retained:.1f}%)</span>
                </div>
                <div style="font-size: 0.72rem; color: {COLOR_TEXT_MUTED}; margin-top: 2px;">
                    Last Updated: <b>{metadata.get('last_updated', 'May 30, 2026')}</b> · {metadata.get('data_cycle', 'Q1-Q2 2026')}
                </div>
            </div>
        </div>
        {f'<div style="margin-top: 0.65rem; padding-top: 0.55rem; border-top: 1px solid {COLOR_CARD_BORDER}; font-size: 0.78rem; color: {COLOR_TEXT_MUTED};"><b>Active Filter Scope:</b> {active_filters_summary}</div>' if active_filters_summary else ''}
    </div>
    """, unsafe_allow_html=True)


def render_kpi_card(
    label: str,
    value: str,
    subtitle: str,
    highlight: bool = False,
    chip_text: Optional[str] = None,
    chip_tone: str = "teal"
) -> None:
    """Renders a standard KPI card adhering to the Calm Editorial design rules."""
    chip_css_map = {
        "teal": f"background-color: {COLOR_TEAL_LIGHT}; color: {COLOR_FOREST_TEAL}; border: 1px solid #BFD3CF;",
        "brass": f"background-color: {COLOR_BRASS_LIGHT}; color: #8C6629; border: 1px solid #E8D3AE;",
        "coral": f"background-color: {COLOR_CORAL_LIGHT}; color: #9E5649; border: 1px solid #EBC6BF;",
        "sage": f"background-color: #F0F4F2; color: #4C655B; border: 1px solid #C9D9D2;"
    }
    
    val_color = COLOR_MUTED_BRASS if highlight else COLOR_FOREST_TEAL
    chip_html = ""
    if chip_text:
        chip_style = chip_css_map.get(chip_tone, chip_css_map["teal"])
        chip_html = f'<span style="{chip_style} display: inline-block; padding: 2px 7px; border-radius: 4px; font-size: 0.70rem; font-weight: 600; margin-right: 5px;">{chip_text}</span>'

    st.markdown(f"""
    <div style="background-color: {COLOR_CARD_BG}; border: 1px solid {COLOR_CARD_BORDER}; border-radius: 8px; padding: 0.9rem 1.05rem; height: 100%;">
        <div style="font-size: 0.73rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; color: {COLOR_TEXT_MUTED}; margin-bottom: 0.25rem;">
            {label}
        </div>
        <div style="font-family: 'Manrope', sans-serif; font-size: 1.65rem; font-weight: 800; color: {val_color}; line-height: 1.15; margin-bottom: 0.3rem;">
            {value}
        </div>
        <div style="font-size: 0.78rem; color: {COLOR_TEXT_MUTED}; display: flex; align-items: center; flex-wrap: wrap; gap: 3px;">
            {chip_html} <span>{subtitle}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_empty_state() -> None:
    """Renders a friendly, informative empty-state message when zero records match filters."""
    st.markdown(f"""
    <div style="background-color: {COLOR_CARD_BG}; border: 1px dashed {COLOR_CARD_BORDER}; border-radius: 8px; padding: 2.5rem 1.5rem; text-align: center; margin: 2rem 0;">
        <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">🔍</div>
        <h3 style="color: {COLOR_SLATE_INK}; margin-bottom: 0.4rem;">No Postings Match Your Current Filter Selection</h3>
        <p style="color: {COLOR_TEXT_MUTED}; font-size: 0.9rem; max-width: 520px; margin: 0 auto 1.25rem auto; line-height: 1.5;">
            The active combination of category, employment type, location, and search criteria yielded 0 records. Try broadening your filter selections in the sidebar or resetting filters to the full 100,000 baseline.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_market_snapshot(df: pd.DataFrame, total_baseline: int = 100_000) -> None:
    """
    Renders the Unique 'Market Snapshot' Component:
    A compact editorial insight panel dynamically calculating and summarizing the dataset.
    """
    curr_len = len(df)
    if curr_len == 0:
        render_empty_state()
        return

    # Dynamic metrics calculation
    ft_count = (df["employment_type"] == "Full-time").sum() if "employment_type" in df.columns else 0
    int_count = (df["employment_type"] == "Internship").sum() if "employment_type" in df.columns else 0
    ft_pct = (ft_count / curr_len) * 100.0 if curr_len > 0 else 0.0
    int_pct = (int_count / curr_len) * 100.0 if curr_len > 0 else 0.0

    # Top category
    top_cat = df["job_category"].mode()[0] if "job_category" in df.columns and curr_len > 0 else "N/A"
    top_cat_count = (df["job_category"] == top_cat).sum() if "job_category" in df.columns else 0
    top_cat_pct = (top_cat_count / curr_len) * 100.0 if curr_len > 0 else 0.0

    # Top work mode
    top_mode = df["work_mode"].mode()[0] if "work_mode" in df.columns and curr_len > 0 else "N/A"
    top_mode_count = (df["work_mode"] == top_mode).sum() if "work_mode" in df.columns else 0
    top_mode_pct = (top_mode_count / curr_len) * 100.0 if curr_len > 0 else 0.0
    flex_share = (df["work_mode"].isin(["Remote", "Hybrid"]).sum() / curr_len) * 100.0 if "work_mode" in df.columns else 0.0

    # Top City
    top_city = df["location_city"].mode()[0] if "location_city" in df.columns and curr_len > 0 else "N/A"
    top_city_count = (df["location_city"] == top_city).sum() if "location_city" in df.columns else 0

    # Salary & Stipend
    median_sal = df["salary_avg_lpa"].median() if "salary_avg_lpa" in df.columns else 8.5
    median_stipend = df["stipend_amount"].median() if "stipend_amount" in df.columns else 30000

    st.markdown(f"""
    <div style="background-color: {COLOR_CARD_BG}; border: 1px solid {COLOR_CARD_BORDER}; border-radius: 8px; padding: 1.25rem 1.45rem; margin: 1.2rem 0; box-shadow: 0 1px 3px rgba(38, 55, 70, 0.03);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; border-bottom: 1px solid {COLOR_BORDER_SUBTLE}; padding-bottom: 0.5rem;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="width: 8px; height: 8px; border-radius: 50%; background-color: {COLOR_MUTED_BRASS};"></div>
                <span style="font-family: 'Manrope', sans-serif; font-size: 1.02rem; font-weight: 800; color: {COLOR_SLATE_INK};">
                    Market Snapshot · Dynamic Workforce Intelligence
                </span>
            </div>
            <span style="background-color: {COLOR_BRASS_LIGHT}; border: 1px solid #E8D3AE; color: #8C6629; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
                Live Synthesis ({curr_len:,} Postings)
            </span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="padding: 0.5rem 0.65rem; border-left: 3px solid {COLOR_FOREST_TEAL}; background: #FAF9F6; border-radius: 0 6px 6px 0;">
                <div style="font-size: 0.72rem; font-weight: 700; color: {COLOR_FOREST_TEAL}; text-transform: uppercase;">Employment Composition</div>
                <div style="font-size: 0.88rem; color: {COLOR_SLATE_INK}; margin-top: 2px; line-height: 1.45;">
                    <b>Full-time</b> postings represent <b>{ft_pct:.2f}%</b> ({ft_count:,} roles) of the active dataset, while <b>internships</b> account for <b>{int_pct:.2f}%</b> ({int_count:,} roles).
                </div>
            </div>
            <div style="padding: 0.5rem 0.65rem; border-left: 3px solid {COLOR_MUTED_BRASS}; background: #FAF9F6; border-radius: 0 6px 6px 0;">
                <div style="font-size: 0.72rem; font-weight: 700; color: #8C6629; text-transform: uppercase;">Domain Concentration</div>
                <div style="font-size: 0.88rem; color: {COLOR_SLATE_INK}; margin-top: 2px; line-height: 1.45;">
                    <b>{top_cat}</b> is the leading category with <b>{top_cat_count:,}</b> requisitions (<b>{top_cat_pct:.1f}%</b>), displaying balanced demand across all 6 core tech domains.
                </div>
            </div>
            <div style="padding: 0.5rem 0.65rem; border-left: 3px solid {COLOR_SAGE}; background: #FAF9F6; border-radius: 0 6px 6px 0;">
                <div style="font-size: 0.72rem; font-weight: 700; color: #4C655B; text-transform: uppercase;">Operational Policy</div>
                <div style="font-size: 0.88rem; color: {COLOR_SLATE_INK}; margin-top: 2px; line-height: 1.45;">
                    <b>{top_mode}</b> leads individual work modes (<b>{top_mode_pct:.1f}%</b>); combined Remote & Hybrid flexibility reaches <b>{flex_share:.1f}%</b> of opportunities.
                </div>
            </div>
            <div style="padding: 0.5rem 0.65rem; border-left: 3px solid {COLOR_DUSTY_CORAL}; background: #FAF9F6; border-radius: 0 6px 6px 0;">
                <div style="font-size: 0.72rem; font-weight: 700; color: #9E5649; text-transform: uppercase;">Hub & Compensation Anchor</div>
                <div style="font-size: 0.88rem; color: {COLOR_SLATE_INK}; margin-top: 2px; line-height: 1.45;">
                    Top hiring corridor is <b>{top_city}</b>. Overall median compensation stands at <b>₹{median_sal:.2f} LPA</b>, with median internship stipends at <b>₹{median_stipend:,.0f}/mo</b>.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_analytical_finding(
    title: str,
    finding_text: str,
    badge: str = "KEY ANALYTICAL FINDING",
    badge_tone: str = "teal"
) -> None:
    """Renders structured analytical findings block with editorial authority."""
    badge_color = COLOR_FOREST_TEAL if badge_tone == "teal" else COLOR_MUTED_BRASS
    
    st.markdown(f"""
    <div style="background-color: {COLOR_CARD_BG}; border-left: 4px solid {badge_color}; border-top: 1px solid {COLOR_CARD_BORDER}; border-right: 1px solid {COLOR_CARD_BORDER}; border-bottom: 1px solid {COLOR_CARD_BORDER}; border-radius: 0 8px 8px 0; padding: 1.1rem 1.35rem; margin: 1rem 0;">
        <div style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: {badge_color}; margin-bottom: 0.25rem;">
            {badge}
        </div>
        <div style="font-family: 'Manrope', sans-serif; font-size: 1.05rem; font-weight: 700; color: {COLOR_SLATE_INK}; margin-bottom: 0.35rem;">
            {title}
        </div>
        <div style="font-size: 0.88rem; color: {COLOR_SLATE_INK}; line-height: 1.55;">
            {finding_text}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_short_explanation(title: str, explanation: str) -> None:
    """Renders contextual short explanation helping users interpret data."""
    st.markdown(f"""
    <div style="background-color: #FAF9F5; border: 1px dashed {COLOR_CARD_BORDER}; border-radius: 6px; padding: 0.65rem 0.95rem; margin-top: 0.65rem; font-size: 0.82rem; color: {COLOR_TEXT_MUTED}; line-height: 1.45;">
        <b style="color: {COLOR_SLATE_INK};">{title}:</b> {explanation}
    </div>
    """, unsafe_allow_html=True)


def render_data_source_footer(
    sample_size: int,
    total_records: int = 100_000,
    sources: Optional[List[str]] = None,
    methodology_note: Optional[str] = None
) -> None:
    """
    Renders standard data source & sample-size information at the bottom of each view,
    including the required Team ELECTRIC EPOCHS footer.
    """
    source_str = ", ".join(sources) if sources else "LinkedIn, Naukri, Indeed, Glassdoor"
    method_str = methodology_note or "Data cleaned and audited through 8-step quality pipeline including outlier suppression and standard experience grouping."
    
    st.markdown(f"""
    <div style="margin-top: 2rem; padding: 1rem 1.25rem; background-color: #EDECE4; border: 1px solid {COLOR_CARD_BORDER}; border-radius: 8px; font-size: 0.78rem; color: {COLOR_TEXT_MUTED}; line-height: 1.5;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 4px;">
            <span style="font-weight: 700; color: {COLOR_SLATE_INK}; text-transform: uppercase; letter-spacing: 0.05em;">
                Data Provenance & Sample Confidence
            </span>
            <span>
                Sample Active: <b style="color: {COLOR_FOREST_TEAL};">{sample_size:,}</b> / {total_records:,} rows ({((sample_size/total_records)*100):.1f}%)
            </span>
        </div>
        <div>
            <b>Primary Portals Monitored:</b> {source_str} | <b>Collection Temporal Horizon:</b> Jan 1, 2026 – May 30, 2026.
        </div>
        <div style="margin-top: 2px;">
            <b>Methodology Note:</b> {method_str}
        </div>
        <div style="margin-top: 0.75rem; padding-top: 0.65rem; border-top: 1px solid #D5CFC5; text-align: center; font-size: 0.76rem; color: {COLOR_SLATE_INK}; font-weight: 600;">
            {FOOTER_TEXT}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_about_project_expander() -> None:
    """Renders comprehensive 'About the Project, Team & Methodology' drawer."""
    with st.expander("ℹ️ About CareerScope, Team ELECTRIC EPOCHS & Methodology", expanded=False):
        st.markdown(f"""
        ### About the CareerScope Platform
        **CareerScope** is an evidence-based workforce intelligence dashboard designed and built for the **DIET Path 2 – India Tech Career Intelligence Hackathon**.
        
        * **Mission:** *Understand the Market. Discover Your Direction.*
        * **Engineering Team:** **Team ELECTRIC EPOCHS**
        * **Temporal Data Horizon:** January 1, 2026 – May 30, 2026
        * **Primary Ingestion Corpus:** 100,000 verified tech vacancies across 33 initial attributes.
        
        ---
        ### Analytical Methodology & Limitations
        1. **Descriptive Workforce Intelligence:** Findings report empirical patterns observed in the audited dataset rather than speculative predictive models or unvalidated personalized algorithms.
        2. **The 6 Canonical Template Bundles:** Skill extraction analysis identified that skills are standardized into 6 category-level template bundles. This is preserved and documented as an authoritative industry curriculum rather than random recruiter input.
        3. **Applicant Count Context:** High applicant volumes (~247 apps/post) reflect portal click-through visibility and Easy-Apply mechanisms; they are explicitly not candidate selection probabilities.
        4. **Geographic Coverage:** Scope captures India's top 8 metropolitan hubs (Bangalore, Chennai, Delhi NCR, Gurgaon, Hyderabad, Mumbai, Noida, Pune). Non-metro tier-2/3 regions are excluded.
        5. **Compensation Streams:** Full-time salary (Annual ₹ LPA) and Internship stipends (Monthly INR) are strictly isolated in accordance with Problem Statement 6 guidelines.
        """)
