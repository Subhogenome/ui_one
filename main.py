import streamlit as st
import pandas as pd
from datetime import datetime

# --------------------------
# Mock Data
# --------------------------
data = pd.DataFrame({
    "Agency": ["FDA", "EMA", "MHRA", "CDSCO"],
    "Title": [
        "New Guidance on Oncology Drug Safety",
        "Manufacturing GMP Update",
        "Medical Device Alert Notice",
        "Clinical Trial Registry Revision"
    ],
    "Region": ["US", "EU", "UK", "India"],
    "Impact Score": [92, 75, 63, 45],
    "Date": ["2025-11-21", "2025-11-22", "2025-11-19", "2025-11-20"],
    "Summary": [
        "This update impacts oncology drug post-market surveillance...",
        "GMP clause update related to sterility and batch validation...",
        "Medical device reporting rules updated for recall notifications...",
        "Rules updated for site registration, sponsor transparency..."
    ]
})

# --------------------------
# UI Layout
# --------------------------
st.set_page_config(page_title="Regulatory Intelligence Platform", layout="wide")

# Header
st.title("📊 Regulatory Intelligence Command Center")
st.write("Prototype UI for Regulatory Monitoring, Ranking & Summarization")

# Search + Filters Row
with st.container():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    search = col1.text_input("🔍 Search Regulation", placeholder="Search by keyword, topic or agency...")
    region_filter = col2.multiselect("🌍 Region Filter", ["US", "EU", "UK", "India"], default=[])
    agency_filter = col3.multiselect("🏛 Agency Filter", ["FDA", "EMA", "MHRA", "CDSCO"], default=[])
    sort_option = col4.selectbox("Sort by", ["Newest", "Oldest", "Highest Impact", "Lowest Impact"])

# Mock filtered table logic
filtered_data = data.copy()

if search:
    filtered_data = filtered_data[filtered_data["Title"].str.contains(search, case=False)]

if region_filter:
    filtered_data = filtered_data[filtered_data["Region"].isin(region_filter)]

if agency_filter:
    filtered_data = filtered_data[filtered_data["Agency"].isin(agency_filter)]

if sort_option == "Highest Impact":
    filtered_data = filtered_data.sort_values(by="Impact Score", ascending=False)
elif sort_option == "Lowest Impact":
    filtered_data = filtered_data.sort_values(by="Impact Score", ascending=True)
elif sort_option == "Newest":
    filtered_data = filtered_data.sort_values(by="Date", ascending=False)
elif sort_option == "Oldest":
    filtered_data = filtered_data.sort_values(by="Date", ascending=True)

# Table Display Block
st.subheader("📁 Regulatory Updates")
st.dataframe(filtered_data, use_container_width=True)

# Sidebar: AI Summary Panel
st.sidebar.title("🧠 AI Analyst")
st.sidebar.write("Interactive assistant for deeper insights")

selected_topic = st.sidebar.selectbox(
    "Ask insights:",
    [
        "What changed this week?",
        "High impact alerts",
        "Compare FDA vs EMA guidance",
        "Summarize all oncology related updates",
        "Show clinical trial policy shifts"
    ]
)

if st.sidebar.button("Generate Summary"):
    st.sidebar.write("✨ AI Summary:")
    st.sidebar.success("Here is a generated summary (placeholder):\n\n- 2 major guidance changes\n- 1 high-risk alert affecting oncology\n- EMA introduced updated GMP norms\n- FDA aligns post-market safety reporting")

# Footer
st.markdown("---")
st.caption("Prototype UI — Regulatory Intelligence PoC • Streamlit Mock • © 2025")

