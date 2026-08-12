import streamlit as st

from App.UI.theme import load_theme
from App.UI.sidebar import render_sidebar
from App.UI.dashboard import render_dashboard


def main():

    st.set_page_config(
        page_title="Payment Studio",
        page_icon="🏦",
        layout="wide",
    )

    load_theme()

    render_sidebar()

    render_dashboard()


if __name__ == "__main__":
    main()
