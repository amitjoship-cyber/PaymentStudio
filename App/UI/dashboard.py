"""
Payment Studio
Dashboard
"""

import streamlit as st

from App.Core.Repository.repository_service import RepositoryService
from App.Core.Repository.business_area_service import BusinessAreaService
from App.Core.Repository.asset_service import AssetService


def render_dashboard():

    st.markdown("### 🏠 Dashboard")

    st.caption("ISO 20022 Engineering Workbench — repository overview.")

    st.write("")

    try:

        service = RepositoryService()
        business_service = BusinessAreaService()
        asset_service = AssetService()

        stats = service.statistics()

    except Exception as error:

        st.error(
            "Could not load the repository. This usually means "
            "PAYMENT_STUDIO_ASSETS isn't pointing at a valid "
            "location, or the asset folder is missing."
        )

        st.caption(f"Details: {error}")

        return

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Business Areas", stats["Business Areas"])
    col2.metric("Messages", stats["Messages"])
    col3.metric("Versions", stats["Versions"])
    col4.metric("Repository", "Connected")

    st.write("")

    # ----------------------------------------------------
    # Repository Explorer
    # ----------------------------------------------------

    with st.container(border=True):

        st.markdown("##### Repository Explorer")

        st.write("")

        business_areas = service.business_areas()

        if not business_areas:

            st.info(
                "No business areas found yet. Add ISO 20022 XSDs "
                "to the Repository to populate this."
            )

            return

        area_lookup = {}

        for area in business_areas:

            display = f"{area.code} - {business_service.get_name(area.code)}"

            area_lookup[display] = area

        col1, col2, col3 = st.columns(3)

        with col1:

            selected_display = st.selectbox(
                "Business Area",
                list(area_lookup.keys()),
            )

        selected_business = area_lookup[selected_display]

        message_lookup = {}

        for message in selected_business.messages:

            display = f"{message.message_id} ({len(message.versions)} versions)"

            message_lookup[display] = message

        with col2:

            selected_message_display = st.selectbox(
                "Message",
                list(message_lookup.keys()),
            )

        selected_message = message_lookup[selected_message_display]

        version_lookup = {}

        for version in selected_message.versions:

            version_lookup[version.version] = version

        with col3:

            selected_version = st.selectbox(
                "Version",
                list(version_lookup.keys()),
            )

        message_version = version_lookup[selected_version]

    st.write("")

    # ----------------------------------------------------
    # Message Information
    # ----------------------------------------------------

    with st.container(border=True):

        st.markdown("##### Message Information")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            st.caption("Business Area")
            st.write(business_service.get_name(selected_business.code))

            st.caption("Message ID")
            st.write(selected_message.message_id)

        with col2:

            st.caption("Version")
            st.write(message_version.version)

            st.caption("Source")
            st.write(message_version.xsd.source)

    st.write("")

    # ----------------------------------------------------
    # Message Assets
    # ----------------------------------------------------

    with st.container(border=True):

        st.markdown("##### Message Assets")

        st.write("")

        assets = asset_service.get_assets(message_version)

        if not assets:

            st.caption("No assets recorded for this version.")

        else:

            for asset in assets:

                col1, col2, col3 = st.columns([2, 2, 2])

                with col1:
                    st.write(asset["name"])

                with col2:
                    st.write(asset["status"])

                with col3:
                    st.write(asset["source"])
