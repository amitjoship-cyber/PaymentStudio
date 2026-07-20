import streamlit as st

# --------------------------------------------------
# Payment Studio
# Version: 0.1.0-alpha
# --------------------------------------------------

st.set_page_config(page_title="Payment Studio", page_icon="💳", layout="wide")

st.title("💳 Payment Studio")
st.caption("Enterprise Payment Message Explorer & Generator")

st.divider()

st.success("✅ Payment Studio is running successfully!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Repository")
    st.info("Repository module coming soon.")

with col2:
    st.subheader("ISO 20022")
    st.info("ISO Explorer coming soon.")

st.divider()

st.subheader("Sprint Status")

st.write("Version : **0.1.0-alpha**")
st.write("Bootstrap : ✅ Complete")
st.write("GitHub : ✅ Connected")
st.write("Streamlit : ✅ Installed")
st.write("Application : ✅ Running")

st.divider()

st.caption("Built with ❤️ for Payments Professionals")
