"""
Payment Studio
Theme
"""

import streamlit as st


def load_theme():

    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

        <style>
        :root {
            --ps-bg: #0B0E14;
            --ps-surface: #12151C;
            --ps-surface-raised: #171B24;
            --ps-border: #232834;
            --ps-border-soft: #1A1E28;
            --ps-text: #E7E9EE;
            --ps-text-muted: #8B93A3;
            --ps-accent: #3B82F6;
            --ps-accent-soft: rgba(59, 130, 246, 0.12);
            --ps-success: #22C55E;
            --ps-success-soft: rgba(34, 197, 94, 0.10);
            --ps-danger: #EF4444;
            --ps-danger-soft: rgba(239, 68, 68, 0.10);
            --ps-warning: #F59E0B;
            --ps-warning-soft: rgba(245, 158, 11, 0.10);
            --ps-radius: 10px;
            --ps-space-1: 8px;
            --ps-space-2: 12px;
            --ps-space-3: 16px;
            --ps-space-4: 24px;
            --ps-space-5: 32px;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            font-size: 16px;
            color: var(--ps-text);
        }

        /* Tighten default Streamlit top padding */
        .block-container {
            padding-top: 2.5rem !important;
            padding-bottom: 3rem !important;
            max-width: 1200px;
        }

        /* Typographic scale */
        h1 {
            font-size: 1.85rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em;
            margin-bottom: 0.25rem !important;
        }
        h2 {
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.01em;
        }
        h3 {
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            color: var(--ps-text);
        }
        p, label, .stMarkdown {
            font-size: 0.95rem;
            color: var(--ps-text-muted);
        }

        /* Field labels */
        [data-testid="stWidgetLabel"] label p {
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--ps-text-muted) !important;
        }

        /* Bordered containers -> cards */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--ps-surface);
            border: 1px solid var(--ps-border);
            border-radius: var(--ps-radius);
            padding: var(--ps-space-1);
        }

        /* Buttons */
        .stButton button {
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.92rem !important;
            padding: 0.55rem 1rem !important;
            border: 1px solid var(--ps-border) !important;
            transition: all 0.15s ease;
        }
        .stButton button[kind="primary"] {
            background: var(--ps-accent) !important;
            border: 1px solid var(--ps-accent) !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.3);
        }
        .stButton button[kind="primary"]:hover {
            background: #2563EB !important;
            border-color: #2563EB !important;
        }
        .stButton button[kind="secondary"] {
            background: transparent !important;
            color: var(--ps-text-muted) !important;
        }
        .stButton button[kind="secondary"]:hover {
            border-color: var(--ps-accent) !important;
            color: var(--ps-text) !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: var(--ps-surface);
            border-right: 1px solid var(--ps-border);
        }
        [data-testid="stSidebar"] button {
            font-size: 0.92rem !important;
            justify-content: flex-start !important;
            text-align: left !important;
        }

        /* Alerts -> refined badges */
        .stAlert {
            border-radius: var(--ps-radius) !important;
            border: 1px solid var(--ps-border) !important;
            font-size: 0.92rem !important;
        }
        [data-testid="stAlertContentSuccess"] {
            color: var(--ps-success) !important;
        }
        div[data-baseweb="notification"]:has([data-testid="stAlertContentSuccess"]) {
            background: var(--ps-success-soft) !important;
            border-color: rgba(34, 197, 94, 0.35) !important;
        }
        div[data-baseweb="notification"]:has([data-testid="stAlertContentError"]) {
            background: var(--ps-danger-soft) !important;
            border-color: rgba(239, 68, 68, 0.35) !important;
        }
        div[data-baseweb="notification"]:has([data-testid="stAlertContentInfo"]) {
            background: var(--ps-accent-soft) !important;
            border-color: rgba(59, 130, 246, 0.35) !important;
        }
        div[data-baseweb="notification"]:has([data-testid="stAlertContentWarning"]) {
            background: var(--ps-warning-soft) !important;
            border-color: rgba(245, 158, 11, 0.35) !important;
        }

        /* Code blocks (generated XML) */
        .stCodeBlock, .stCodeBlock code, pre, pre code {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 14px !important;
            line-height: 1.6 !important;
        }
        .stCodeBlock {
            border: 1px solid var(--ps-border) !important;
            border-radius: var(--ps-radius) !important;
        }

        /* Metrics (dashboard stat cards) */
        [data-testid="stMetric"] {
            background: var(--ps-surface);
            border: 1px solid var(--ps-border);
            border-radius: var(--ps-radius);
            padding: var(--ps-space-3) var(--ps-space-3) var(--ps-space-2);
        }
        [data-testid="stMetricValue"] {
            font-size: 1.7rem !important;
            font-weight: 800 !important;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.78rem !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--ps-text-muted) !important;
        }

        /* Select / radio inputs */
        [data-baseweb="select"] > div {
            border-radius: 8px !important;
            border-color: var(--ps-border) !important;
        }

        /* Radio buttons - ensure visible against dark background */
        [data-baseweb="radio"] div:first-child {
            border-color: var(--ps-text-muted) !important;
            background: transparent !important;
        }
        [data-baseweb="radio"] input:checked + div {
            border-color: var(--ps-accent) !important;
        }
        [data-baseweb="radio"] input:checked + div > div {
            background: var(--ps-accent) !important;
        }
        .stRadio label p {
            color: var(--ps-text) !important;
            font-size: 0.92rem !important;
            font-weight: 400 !important;
            text-transform: none !important;
            letter-spacing: normal !important;
        }

        /* Dividers */
        hr {
            border-color: var(--ps-border-soft) !important;
            margin: var(--ps-space-4) 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
