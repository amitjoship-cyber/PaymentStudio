"""
Payment Studio
Dashboard
"""

import streamlit as st

from App.Core.Repository.repository_service import RepositoryService
from App.Core.Repository.business_area_service import BusinessAreaService
from App.Core.Repository.asset_service import AssetService


def render_dashboard():

    service = RepositoryService()
    business_service = BusinessAreaService()
    asset_service = AssetService()

    st.title("🏦 Payment Studio")

    st.write("Welcome to the ISO 20022 Engineering Workbench.")

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    stats = service.statistics()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Business Areas", stats["Business Areas"])
    col2.metric("Messages", stats["Messages"])
    col3.metric("Versions", stats["Versions"])
    col4.metric("Repository", "Connected")

    st.divider()

    # ----------------------------------------------------
    # Repository Explorer
    # ----------------------------------------------------

    st.subheader("Repository Explorer")

    business_areas = service.business_areas()

    area_lookup = {}

    for area in business_areas:

        display = f"{area.code} - " f"{business_service.get_name(area.code)}"

        area_lookup[display] = area

    selected_display = st.selectbox(
        "Business Area",
        list(area_lookup.keys()),
    )

    selected_business = area_lookup[selected_display]

    # ----------------------------------------------------
    # Messages
    # ----------------------------------------------------

    message_lookup = {}

    for message in selected_business.messages:

        display = f"{message.message_id}" f" ({len(message.versions)} Versions)"

        message_lookup[display] = message

    selected_message_display = st.selectbox(
        "Message",
        list(message_lookup.keys()),
    )

    selected_message = message_lookup[selected_message_display]

    # ----------------------------------------------------
    # Versions
    # ----------------------------------------------------

    version_lookup = {}

    for version in selected_message.versions:

        version_lookup[version.version] = version

    selected_version = st.selectbox(
        "Version",
        list(version_lookup.keys()),
    )

    message_version = version_lookup[selected_version]

    st.divider()

    # ----------------------------------------------------
    # Message Information
    # ----------------------------------------------------

    st.subheader("Message Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Business Area**")
        st.write(business_service.get_name(selected_business.code))

        st.write("**Message ID**")
        st.write(selected_message.message_id)

    with col2:

        st.write("**Version**")
        st.write(message_version.version)

        st.write("**Source**")
        st.write(message_version.xsd.source)

    st.divider()

    # ----------------------------------------------------
    # Message Assets
    # ----------------------------------------------------

    st.subheader("Message Assets")

    assets = asset_service.get_assets(message_version)

    for asset in assets:

        col1, col2, col3 = st.columns([2, 2, 2])

        with col1:
            st.write(asset["name"])

        with col2:
            st.write(asset["status"])

        with col3:
            st.write(asset["source"])
