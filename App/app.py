import streamlit as st

from App.UI.theme import load_theme
from App.UI.sidebar import render_sidebar
from App.UI.dashboard import render_dashboard
from App.UI.generator import render_generator


def main():

    st.set_page_config(
        page_title="Payment Studio",
        page_icon="🏦",
        layout="wide",
    )

    load_theme()

    render_sidebar()

    page = st.session_state.get("page", "dashboard")

    if page == "generate":

        render_generator()

    else:

        render_dashboard()


if __name__ == "__main__":
    main()
