"""
CareerScope - Data Loader & Query Engine
========================================
Efficient cached loader for the India Tech Career Intelligence 2026 dataset.
"""

import os
from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
import numpy as np
import streamlit as st

# Locate data paths: Parquet (2.4MB lightweight deploy-ready) or Raw CSV (local 61MB)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARQUET_PATH = os.path.join(CURRENT_DIR, "data", "career_intelligence_data.parquet")

DATASET_RELATIVE_PATH = os.path.join(
    os.path.dirname(CURRENT_DIR),
    "CODE_RESOURCE",
    "cleaned_india_tech_career_intelligence_2026.csv"
)

DATASET_NAME = "India Tech Career Intelligence 2026"
TOTAL_RECORDS = 100_000

@st.cache_data(show_spinner="Loading Career Intelligence Dataset...")
def load_dataset() -> pd.DataFrame:
    """Loads and standardizes the cleaned 100k India Tech Career dataset."""
    # Priority 1: High-performance, deploy-ready Parquet (2.4MB)
    if os.path.exists(PARQUET_PATH):
        df = pd.read_parquet(PARQUET_PATH)
        if "posted_date" in df.columns:
            df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")
        if "application_deadline" in df.columns:
            df["application_deadline"] = pd.to_datetime(df["application_deadline"], errors="coerce")
    # Priority 2: Local Raw CSV (61MB) if available
    elif os.path.exists(DATASET_RELATIVE_PATH):
        df = pd.read_csv(
            DATASET_RELATIVE_PATH,
            parse_dates=["posted_date", "application_deadline"],
            dtype={
                "work_mode": "category",
                "experience_level": "category",
                "employment_type": "category",
                "company_type": "category",
                "source_platform": "category",
                "location_city": "category"
            }
        )
    else:
        raise FileNotFoundError(
            f"Dataset not found. Checked Parquet: {PARQUET_PATH} and CSV: {DATASET_RELATIVE_PATH}"
        )
    
    # Precompute average salary for fast aggregation
    if "salary_minimum" in df.columns and "salary_maximum" in df.columns:
        if "salary_avg" not in df.columns:
            df["salary_avg"] = (df["salary_minimum"] + df["salary_maximum"]) / 2.0
        if "salary_avg_lpa" not in df.columns:
            df["salary_avg_lpa"] = df["salary_avg"] / 100_000.0
        if "salary_min_lpa" not in df.columns:
            df["salary_min_lpa"] = df["salary_minimum"] / 100_000.0
        if "salary_max_lpa" not in df.columns:
            df["salary_max_lpa"] = df["salary_maximum"] / 100_000.0

    return df


@st.cache_data
def get_dataset_metadata(df: pd.DataFrame) -> Dict[str, Any]:
    """Computes high-level metadata from actual data."""
    min_date = df["posted_date"].min()
    max_date = df["posted_date"].max()
    
    return {
        "dataset_name": DATASET_NAME,
        "total_records": len(df),
        "total_columns": len(df.columns),
        "min_date": min_date.strftime("%b %d, %Y") if pd.notnull(min_date) else "Jan 01, 2026",
        "max_date": max_date.strftime("%b %d, %Y") if pd.notnull(max_date) else "May 30, 2026",
        "last_updated": max_date.strftime("%B %d, %Y") if pd.notnull(max_date) else "May 30, 2026",
        "data_cycle": "Q1-Q2 2026 (Live Recruitment Audit)",
        "source_count": df["source_platform"].nunique() if "source_platform" in df.columns else 0,
        "categories_count": df["job_category"].nunique() if "job_category" in df.columns else 0,
        "cities_count": df["location_city"].nunique() if "location_city" in df.columns else 0,
        "companies_count": df["company_name"].nunique() if "company_name" in df.columns else 0
    }


def filter_dataset(
    df: pd.DataFrame,
    selected_categories: Optional[List[str]] = None,
    selected_employment_types: Optional[List[str]] = None,
    selected_work_modes: Optional[List[str]] = None,
    selected_exp_levels: Optional[List[str]] = None,
    selected_cities: Optional[List[str]] = None,
    search_query: Optional[str] = None
) -> pd.DataFrame:
    """Applies multi-dimensional global filters and search queries efficiently."""
    filtered_df = df
    
    if selected_categories:
        filtered_df = filtered_df[filtered_df["job_category"].isin(selected_categories)]
        
    if selected_employment_types:
        filtered_df = filtered_df[filtered_df["employment_type"].isin(selected_employment_types)]
        
    if selected_work_modes:
        filtered_df = filtered_df[filtered_df["work_mode"].isin(selected_work_modes)]
        
    if selected_exp_levels:
        filtered_df = filtered_df[filtered_df["experience_level"].isin(selected_exp_levels)]
        
    if selected_cities:
        filtered_df = filtered_df[filtered_df["location_city"].isin(selected_cities)]
        
    if search_query and search_query.strip():
        q = search_query.strip().lower()
        title_match = filtered_df["job_title"].str.lower().str.contains(q, na=False)
        comp_match = filtered_df["company_name"].str.lower().str.contains(q, na=False)
        skills_match = filtered_df["skills_extracted"].str.lower().str.contains(q, na=False) if "skills_extracted" in filtered_df.columns else False
        filtered_df = filtered_df[title_match | comp_match | skills_match]
        
    return filtered_df
