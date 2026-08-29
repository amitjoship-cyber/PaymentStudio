"""
Payment Studio
Sidebar
"""

import streamlit as st


PAGES = {
    "dashboard": "🏠 Dashboard",
    "generate": "⚡ Generate & Validate",
}


def render_sidebar():

    if "page" not in st.session_state:

        st.session_state.page = "dashboard"

    with st.sidebar:

        st.title("🏦 Payment Studio")

        st.divider()

        for key, label in PAGES.items():

            is_current = st.session_state.page == key

            if st.button(
                label,
                use_container_width=True,
                type="primary" if is_current else "secondary",
            ):

                st.session_state.page = key

                st.rerun()

        st.divider()

        st.caption(
            "Repository Explorer, Import Wizard, and Settings "
            "are planned - see Docs/VISION_AND_ROADMAP.md."
        )

        st.divider()

        st.success("Repository Ready")
