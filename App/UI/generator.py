"""
Payment Studio
Generate & Validate
"""

import streamlit as st

from App.Core.Engine.payment_studio import PaymentStudio
from App.Core.Country.country_repository import CountryRepository


#
# MVP scope: only messages already proven to generate cleanly
# (or near-cleanly) end-to-end against real ISO 20022 schemas are
# offered here. Expanding this list is a deliberate decision, not
# an automatic side effect of adding XSDs to the Repository - see
# Docs/VISION_AND_ROADMAP.md, Milestone C.
#

SUPPORTED_MESSAGES = {
    "pacs.008 - FI to FI Customer Credit Transfer": "pacs.008",
    "pain.001 - Customer Credit Transfer Initiation": "pain.001",
    "camt.053 - Bank to Customer Statement": "camt.053",
}


@st.cache_resource
def get_studio():

    #
    # Cached across reruns: parsing XSDs is not free, and
    # Streamlit reruns this module on every interaction.
    #

    return PaymentStudio()


@st.cache_resource
def get_countries():

    return CountryRepository()


def render_generator():

    st.markdown("### ⚡ Generate & Validate")

    st.caption(
        "Generate a sample ISO 20022 message from a real schema, "
        "and validate it against that same schema."
    )

    st.write("")

    with st.container(border=True):

        st.markdown("##### Message Parameters")

        st.write("")

        col1, col2, col3 = st.columns([2, 1.4, 1.4])

        with col1:

            message_display = st.selectbox(
                "Message Type",
                list(SUPPORTED_MESSAGES.keys()),
            )

            message = SUPPORTED_MESSAGES[message_display]

        with col2:

            countries = get_countries()

            country_codes = countries.all_codes()

            country_labels = {
                code: f"{countries.get(code).name} ({code})"
                for code in country_codes
            }

            default_code = "IN" if "IN" in country_codes else country_codes[0]

            selected_label = st.selectbox(
                "Country",
                list(country_labels.values()),
                index=list(country_labels.keys()).index(default_code),
            )

            country = next(
                code
                for code, label in country_labels.items()
                if label == selected_label
            )

        with col3:

            sample_display = st.radio(
                "Sample Mode",
                ["Minimal", "Complete"],
                horizontal=True,
            )

            sample = "minimal" if sample_display == "Minimal" else "complete"

        st.write("")

        generate_clicked = st.button(
            "⚡  Generate Message",
            type="primary",
            use_container_width=True,
        )

    if not generate_clicked:

        st.write("")

        st.info(
            "Choose a message type, country, and sample mode above, "
            "then click **Generate Message**."
        )

        return

    studio = get_studio()

    with st.spinner(f"Generating {message}..."):

        result = studio.generate(
            message,
            country=country,
            sample=sample,
            output="XML",
        )

    st.write("")

    #
    # Validation result
    #

    if not result.errors:

        st.success(
            f"✅  **Valid** — {message} generated and validated "
            f"successfully against the real ISO 20022 schema."
        )

    else:

        st.error(
            f"❌  **Invalid** — {len(result.errors)} schema "
            f"validation error(s) found."
        )

        with st.expander("Show validation errors", expanded=True):

            for index, error in enumerate(result.errors, start=1):

                st.write(f"**{index}.** {error}")

    if result.warnings:

        with st.expander(f"Warnings ({len(result.warnings)})"):

            for warning in result.warnings:

                st.write(warning)

    st.write("")

    #
    # Generated XML
    #

    with st.container(border=True):

        st.markdown("##### Generated Message (XML)")

        st.code(
            result.xml or "(no output generated)",
            language="xml",
            line_numbers=True,
        )

        if result.xml:

            st.download_button(
                "⬇  Download XML",
                data=result.xml,
                file_name=f"{message}_{country}_{sample}.xml",
                mime="application/xml",
                use_container_width=True,
            )
