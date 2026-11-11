"""
CareerScope - Design System & Brand Identity
===========================================
Brand Name: CareerScope
Tagline: Understand the Market. Discover Your Direction.
Developed by: Team ELECTRIC EPOCHS for Manthan Mini Hackathon 2026
"""

from typing import Dict, List, Any
import matplotlib.pyplot as plt
import matplotlib as mpl

# -----------------------------------------------------------------------------
# BRAND IDENTITY & PALETTE TOKENS
# -----------------------------------------------------------------------------
BRAND_NAME = "CareerScope"
TAGLINE = "Understand the Market. Discover Your Direction."
TEAM_NAME = "Team ELECTRIC EPOCHS"
HACKATHON_EVENT = "Manthan Mini Hackathon 2026"
DESIGN_DIRECTION = "Premium enterprise analytics with a modern editorial feel"

# Signature Color Palette (Strictly Enforced)
COLOR_FOREST_TEAL   = "#183A37"  # Primary brand: sidebar, key actions, primary series
COLOR_MUTED_BRASS   = "#D6A85F"  # Highlights: KPIs, milestones, high-value signals
COLOR_WARM_IVORY    = "#F5F3ED"  # Main canvas: page background
COLOR_SLATE_INK     = "#263746"  # Headings, labels, body text
COLOR_SAGE          = "#A9BDB5"  # Secondary charts: baseline comparisons, categories
COLOR_DUSTY_CORAL   = "#D9A69B"  # Secondary highlights: callouts, comparative series

# Derived & Semantic Tokens (Calm, Trustworthy, Subtle)
COLOR_CARD_BG       = "#FFFFFF"  # Crisp card background against Warm Ivory canvas
COLOR_CARD_BORDER   = "#E4E0D7"  # Subtle neutral 1px border (no heavy shadows)
COLOR_BORDER_SUBTLE = "#ECE8DF"  # Divider line
COLOR_TEXT_MUTED    = "#5E707E"  # Secondary labels & captions
COLOR_TEAL_LIGHT    = "#E8F0EE"  # Light tint for badges
COLOR_BRASS_LIGHT   = "#FDF8EE"  # Light tint for callouts
COLOR_CORAL_LIGHT   = "#FBF1EE"  # Light tint for alerts/highlights

# Chart Categorical Color Sequences
CHART_PALETTE = [
    COLOR_FOREST_TEAL,
    COLOR_MUTED_BRASS,
    COLOR_SAGE,
    COLOR_DUSTY_CORAL,
    COLOR_SLATE_INK,
    "#436B67",  # Medium Teal
    "#C49246",  # Deep Brass
    "#7D968C",  # Deep Sage
    "#C88478",  # Rose Coral
    "#3E5365"   # Medium Slate
]

# Typography Specifications
FONT_FAMILY_PRIMARY = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_FAMILY_HEADING = "'Manrope', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif"

# -----------------------------------------------------------------------------
# GLOBAL STREAMLIT CSS STYLING
# -----------------------------------------------------------------------------
CUSTOM_CSS = f"""
<style>
/* Import Inter & Manrope Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

/* Main App Canvas: Warm Ivory Background */
html, body, [class*="css"] {{
    font-family: {FONT_FAMILY_PRIMARY};
    color: {COLOR_SLATE_INK};
}}

.stApp {{
    background-color: {COLOR_WARM_IVORY};
}}

header[data-testid="stHeader"] {{
    background-color: {COLOR_WARM_IVORY};
}}

/* Typography: Headings */
h1, h2, h3, h4, h5, h6 {{
    font-family: {FONT_FAMILY_HEADING};
    color: {COLOR_SLATE_INK} !important;
    font-weight: 700;
    letter-spacing: -0.02em;
}}

h1 {{
    font-size: 2.05rem;
    line-height: 1.25;
    margin-bottom: 0.25rem;
}}

h2 {{
    font-size: 1.45rem;
    margin-top: 1.25rem;
    margin-bottom: 0.5rem;
    border-bottom: 1px solid {COLOR_CARD_BORDER};
    padding-bottom: 0.35rem;
}}

h3 {{
    font-size: 1.15rem;
    margin-top: 0.9rem;
    margin-bottom: 0.35rem;
}}

p, span, label, div {{
    color: {COLOR_SLATE_INK};
    font-size: 0.92rem;
    line-height: 1.5;
}}

/* Sidebar: Forest Teal Background */
section[data-testid="stSidebar"] {{
    background-color: {COLOR_FOREST_TEAL} !important;
    border-right: 1px solid #0F2523;
}}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4 {{
    color: #FFFFFF !important;
}}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {{
    color: #E2DDD5 !important;
}}

/* Sidebar Radio Buttons */
section[data-testid="stSidebar"] div[role="radiogroup"] label {{
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 6px;
    padding: 6px 12px;
    margin-bottom: 4px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.2s ease;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
    background-color: rgba(214, 168, 95, 0.18);
    border-color: {COLOR_MUTED_BRASS};
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
    background-color: rgba(214, 168, 95, 0.25) !important;
    border-color: {COLOR_MUTED_BRASS} !important;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] span,
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) span {{
    color: {COLOR_MUTED_BRASS} !important;
    font-weight: 700;
}}

/* Clean White Analytical Cards */
.cs-card {{
    background-color: {COLOR_CARD_BG};
    border: 1px solid {COLOR_CARD_BORDER};
    border-radius: 8px;
    padding: 1.25rem 1.45rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(38, 55, 70, 0.04);
}}

/* Primary Buttons */
.stButton > button {{
    background-color: {COLOR_FOREST_TEAL};
    color: #FFFFFF !important;
    border: 1px solid {COLOR_FOREST_TEAL};
    border-radius: 6px;
    padding: 0.5rem 1.25rem;
    font-weight: 600;
    font-size: 0.88rem;
    transition: all 0.2s ease;
}}

.stButton > button:hover {{
    background-color: #204B47;
    border-color: #204B47;
    color: {COLOR_MUTED_BRASS} !important;
}}

/* Sidebar Inputs & Controls */
section[data-testid="stSidebar"] .stTextInput input {{
    background-color: #0E2422 !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
}}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
    background-color: #0E2422 !important;
    color: #FFFFFF !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
}}

/* Main Canvas Selectboxes */
div[data-baseweb="select"] > div {{
    background-color: {COLOR_CARD_BG};
    border-color: {COLOR_CARD_BORDER};
    border-radius: 6px;
}}

/* Tabs Styling */
button[data-baseweb="tab"] {{
    font-family: {FONT_FAMILY_HEADING};
    font-weight: 700;
    color: {COLOR_SLATE_INK};
    padding: 0.6rem 1.2rem;
    font-size: 0.95rem;
}}

button[data-baseweb="tab"][aria-selected="true"] {{
    color: {COLOR_FOREST_TEAL} !important;
    border-bottom: 3px solid {COLOR_MUTED_BRASS} !important;
}}

/* DataFrames */
[data-testid="stDataFrame"] {{
    background-color: {COLOR_CARD_BG};
    border: 1px solid {COLOR_CARD_BORDER};
    border-radius: 6px;
}}
</style>
"""

# -----------------------------------------------------------------------------
# MATPLOTLIB / SEABORN THEME CONFIGURATION
# -----------------------------------------------------------------------------
def apply_matplotlib_theme():
    """Applies CareerScope editorial styling rules to matplotlib & seaborn."""
    mpl.rcParams.update({
        # Figure & Axes Canvas
        "figure.facecolor": COLOR_CARD_BG,
        "axes.facecolor": COLOR_CARD_BG,
        "axes.edgecolor": COLOR_CARD_BORDER,
        "axes.linewidth": 1.0,
        "axes.grid": True,
        "grid.color": COLOR_BORDER_SUBTLE,
        "grid.linestyle": "--",
        "grid.linewidth": 0.6,
        "grid.alpha": 0.8,
        
        # Typography
        "font.family": "sans-serif",
        "font.sans-serif": ["Inter", "Manrope", "DejaVu Sans", "Arial"],
        "text.color": COLOR_SLATE_INK,
        "axes.labelcolor": COLOR_SLATE_INK,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlecolor": COLOR_SLATE_INK,
        "axes.labelsize": 9.5,
        "axes.labelweight": "medium",
        "xtick.color": COLOR_TEXT_MUTED,
        "ytick.color": COLOR_TEXT_MUTED,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        
        # Colors & Lines
        "axes.prop_cycle": mpl.cycler(color=CHART_PALETTE),
        "lines.linewidth": 2.0,
        "patch.edgecolor": "none",
        
        # Legend
        "legend.facecolor": COLOR_CARD_BG,
        "legend.edgecolor": COLOR_CARD_BORDER,
        "legend.fontsize": 8.5,
        "legend.title_fontsize": 9,
        "legend.framealpha": 0.95,
        
        # Spines
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": True,
        "axes.spines.bottom": True,
    })


def get_palette_dict() -> Dict[str, str]:
    """Returns signature palette dictionary."""
    return {
        "Forest Teal": COLOR_FOREST_TEAL,
        "Muted Brass": COLOR_MUTED_BRASS,
        "Warm Ivory": COLOR_WARM_IVORY,
        "Slate Ink": COLOR_SLATE_INK,
        "Sage": COLOR_SAGE,
        "Dusty Coral": COLOR_DUSTY_CORAL,
        "Card Background": COLOR_CARD_BG,
        "Subtle Border": COLOR_CARD_BORDER,
        "Muted Text": COLOR_TEXT_MUTED,
    }
