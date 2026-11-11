# CareerScope — Design System & Brand Identity Specification

## 1. Brand Identity
- **Brand Name:** `CareerScope`
- **Tagline:** *"Understand the Market. Discover Your Direction."*
- **Design Direction:** *Premium enterprise analytics with a modern editorial feel.*
- **Core Philosophy:** Calm, trustworthy, evidence-based data journalism reflecting precision workforce intelligence rather than flashy or cluttered generic dashboard templates.

---

## 2. Signature Color Palette

| Token Name | Hex Code | Role | UI Application & Rules |
| :--- | :--- | :--- | :--- |
| **Forest Teal** | `#183A37` | **Primary Brand** | Navigation headers, primary action buttons, key metrics, dominant chart series. |
| **Muted Brass** | `#D6A85F` | **Highlights** | Used sparingly for high-value signals (e.g. top salary percentiles, key milestones, featured badges). |
| **Warm Ivory** | `#F5F3ED` | **Main Canvas** | The foundational page background. Eliminates harsh cold white glare and delivers an organic, editorial canvas. |
| **Slate Ink** | `#263746` | **Text & Headings** | High-contrast typography, structural headings, axis labels, tick text, and crisp data values. |
| **Sage** | `#A9BDB5` | **Secondary Charts** | Baseline distributions, secondary comparative categories, soft area fills. |
| **Dusty Coral** | `#D9A69B` | **Secondary Highlights** | Contrasting metrics, comparative benchmarks, high-density delta indicators. |

### Derived & Surface Tokens
- **Card Background:** `#FFFFFF` (Crisp contrast against `#F5F3ED`)
- **Card Border:** `#E4E0D7` (Subtle 1px border; avoids heavy, noisy drop-shadows)
- **Subtle Divider:** `#ECE8DF`
- **Muted Text:** `#5E707E` (Descriptive captions, metadata, units)
- **Teal Light Tint:** `#E8F0EE`
- **Brass Light Tint:** `#FDF8EE`
- **Coral Light Tint:** `#FBF1EE`

---

## 3. Typography Hierarchy
- **Primary Font Family:** `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Heading Font Family:** `'Manrope', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
- **Letter Spacing:** `-0.02em` on primary headings for a sharp, editorial, and trustworthy presence.
- **Hierarchy:**
  - `H1` (Page Title): `2.15rem`, Bold (700/800)
  - `H2` (Section Headers): `1.50rem`, Bold (700) with subtle bottom accent border
  - `H3` (Component Headers): `1.20rem`, Semi-Bold (600)
  - `Body / Paragraphs`: `0.95rem`, Regular (400), line-height `1.5`
  - `Metric Values`: `1.85rem` - `2.25rem`, Extra Bold (800)
  - `Metric Labels`: `0.78rem`, Uppercase, letter-spacing `0.08em`

---

## 4. UI Architecture & Design Rules
1. **Canvas Consistency:** Every page and module renders over Warm Ivory (`#F5F3ED`).
2. **Subtle Elevation:** Drop-shadows are eliminated or kept ultra-soft (`box-shadow: 0 1px 3px rgba(38, 55, 70, 0.04)`); structure is defined by 1px borders in `#E4E0D7`.
3. **Restraint in Highlights:** Muted Brass (`#D6A85F`) is never used for backgrounds of large components; it is reserved for accentuating high-value data points.
4. **Clean Chart Sizing & Spacing:** All charts adhere to standard aspect ratios, uncluttered margins, Slate Ink labels, and Forest Teal / Sage / Dusty Coral categorical encoding.
5. **Calm & Trustworthy Tone:** The interface avoids noisy gamification, loud gradients, or distracting animations, presenting insights with clarity and professional dignity.
