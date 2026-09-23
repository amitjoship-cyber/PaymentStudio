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
            --ps-surface-raised: #181D27;
            --ps-border: #303746;
            --ps-border-strong: #4B5567;

            --ps-text: #F3F4F6;
            --ps-text-muted: #A8B0BF;

            --ps-accent: #3B82F6;
            --ps-accent-hover: #60A5FA;

            --ps-success: #22C55E;
            --ps-danger: #EF4444;
            --ps-warning: #F59E0B;

            --ps-radius: 10px;
        }


        /* =========================================================
        GLOBAL
        ========================================================= */

        html,
        body,
        [class*="css"] {
            font-family: 'Inter',
                -apple-system,
                BlinkMacSystemFont,
                sans-serif !important;

            color: var(--ps-text);
        }


        .block-container {
            padding-top: 2.5rem !important;
            padding-bottom: 3rem !important;
            max-width: 1200px;
        }


        /* =========================================================
        TEXT
        ========================================================= */

        h1 {
            font-size: 1.85rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em;
        }

        h2 {
            font-size: 1.3rem !important;
            font-weight: 700 !important;
        }

        h3 {
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            color: var(--ps-text) !important;
        }

        p {
            color: var(--ps-text-muted);
        }


        /* =========================================================
        FIELD LABELS
        ========================================================= */

        [data-testid="stWidgetLabel"] label p {
            color: var(--ps-text-muted) !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }


        /* =========================================================
        CARDS
        ========================================================= */

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--ps-surface) !important;
            border: 1px solid var(--ps-border) !important;
            border-radius: var(--ps-radius) !important;
        }


        /* =========================================================
        BUTTONS
        
        IMPORTANT:
        Do NOT use bright blue as the button background.
        ========================================================= */

        .stButton > button,
        .stDownloadButton > button {

            background: #181D27 !important;

            color: #FFFFFF !important;

            border: 1px solid #4B5567 !important;

            border-radius: 8px !important;

            font-size: 0.92rem !important;
            font-weight: 600 !important;

            padding: 0.55rem 1rem !important;

            box-shadow: none !important;

            transition:
                background 0.15s ease,
                border-color 0.15s ease,
                color 0.15s ease;
        }


        /* Force ALL text inside buttons to white */

        .stButton > button *,
        .stDownloadButton > button * {
            color: #FFFFFF !important;
        }


        /* Hover */

        .stButton > button:hover,
        .stDownloadButton > button:hover {

            background: #222936 !important;

            color: #FFFFFF !important;

            border-color: #60A5FA !important;

            box-shadow: none !important;
        }


        .stButton > button:hover *,
        .stDownloadButton > button:hover * {
            color: #FFFFFF !important;
        }


        /* Primary buttons remain DARK.
        This overrides Streamlit's default blue primary style. */

        .stButton > button[kind="primary"],
        .stDownloadButton > button[kind="primary"] {

            background: #181D27 !important;

            color: #FFFFFF !important;

            border: 1px solid #4B5567 !important;
        }


        .stButton > button[kind="primary"]:hover,
        .stDownloadButton > button[kind="primary"]:hover {

            background: #222936 !important;

            color: #FFFFFF !important;

            border-color: #60A5FA !important;
        }


        /* =========================================================
        RADIO BUTTONS
        ========================================================= */

        div[data-testid="stRadio"] {

            color: #FFFFFF !important;
        }


        /* Radio option text */

        div[data-testid="stRadio"] label {

            color: #F3F4F6 !important;

            font-size: 0.92rem !important;

            font-weight: 500 !important;

            cursor: pointer;
        }


        div[data-testid="stRadio"] label p {

            color: #F3F4F6 !important;

            font-size: 0.92rem !important;

            font-weight: 500 !important;

            text-transform: none !important;

            letter-spacing: normal !important;
        }


        /*
        * Streamlit/BaseWeb radio circle.
        *
        * The first child of each radio label is the visible
        * circular control in current Streamlit versions.
        */

        div[data-testid="stRadio"] label > div:first-child {

            width: 20px !important;

            height: 20px !important;

            min-width: 20px !important;

            min-height: 20px !important;

            border-radius: 50% !important;

            border: 2px solid #8B95A7 !important;

            background: #0B0E14 !important;

            box-sizing: border-box !important;

            box-shadow: none !important;
        }


        /* Hover */

        div[data-testid="stRadio"] label:hover > div:first-child {

            border-color: #60A5FA !important;

            background: #12151C !important;
        }


        /*
        * Selected radio.
        *
        * :has() works in the Chromium browser used by Streamlit.
        */

        div[data-testid="stRadio"]
        label:has(input:checked)
        > div:first-child {

            border: 2px solid #60A5FA !important;

            background: #3B82F6 !important;

            box-shadow:
                inset 0 0 0 4px #12151C !important;
        }


        /* Selected label */

        div[data-testid="stRadio"]
        label:has(input:checked) p {

            color: #FFFFFF !important;

            font-weight: 600 !important;
        }


        /* =========================================================
        SELECT BOX
        ========================================================= */

        [data-baseweb="select"] > div {

            background: #181D27 !important;

            color: #F3F4F6 !important;

            border: 1px solid #4B5567 !important;

            border-radius: 8px !important;
        }


        [data-baseweb="select"] span {

            color: #F3F4F6 !important;
        }


        /* =========================================================
        ALERTS
        ========================================================= */

        .stAlert {

            border-radius: var(--ps-radius) !important;

            border: 1px solid var(--ps-border) !important;

            font-size: 0.92rem !important;
        }


        /* =========================================================
        CODE
        ========================================================= */

        .stCodeBlock,
        .stCodeBlock code,
        pre,
        pre code {

            font-family:
                'JetBrains Mono',
                monospace !important;

            font-size: 14px !important;

            line-height: 1.6 !important;
        }


        .stCodeBlock {

            border: 1px solid var(--ps-border) !important;

            border-radius: var(--ps-radius) !important;
        }


        /* =========================================================
        METRICS
        ========================================================= */

        [data-testid="stMetric"] {

            background: var(--ps-surface) !important;

            border: 1px solid var(--ps-border) !important;

            border-radius: var(--ps-radius) !important;

            padding: 16px !important;
        }


        [data-testid="stMetricValue"] {

            color: #FFFFFF !important;

            font-size: 1.7rem !important;

            font-weight: 800 !important;
        }


        [data-testid="stMetricLabel"] {

            color: var(--ps-text-muted) !important;

            font-size: 0.78rem !important;

            text-transform: uppercase;

            letter-spacing: 0.04em;
        }


        /* =========================================================
        SIDEBAR
        ========================================================= */

        [data-testid="stSidebar"] {

            background: var(--ps-surface) !important;

            border-right: 1px solid var(--ps-border) !important;
        }


        [data-testid="stSidebar"] button {

            color: #F3F4F6 !important;

            font-size: 0.92rem !important;

            text-align: left !important;
        }


        /* =========================================================
        DIVIDERS
        ========================================================= */

        hr {

            border-color: #1F2530 !important;

            margin: 24px 0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
