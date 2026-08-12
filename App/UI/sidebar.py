"""
Payment Studio
Sidebar
"""

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🏦 Payment Studio")

        st.divider()

        st.button("🏠 Dashboard", use_container_width=True)

        st.button("📚 Repository Explorer", use_container_width=True)

        st.button("📥 Import Wizard", use_container_width=True)

        st.button("⚙ Repository Settings", use_container_width=True)

        st.button("ℹ About", use_container_width=True)

        st.divider()

        st.success("Repository Ready")
