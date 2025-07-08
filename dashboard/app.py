import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from analysis.bottleneck_detector import detect_bottlenecks
from recommendations.suggestor import suggest_improvements

st.set_page_config(page_title="DevOps Bottleneck Analyzer", layout="wide")

st.title("🚀 DevOps Productivity and Bottleneck Analyzer")
st.markdown("Upload your team's PR data to analyze bottlenecks and get recommendations.")

uploaded_file = st.file_uploader("📤 Upload CSV File", type="csv")

if uploaded_file:
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    data_path = "data/sample_data.csv"

    # Save uploaded file
    with open(data_path, "wb") as f:
        f.write(uploaded_file.read())

    # Load data
    try:
        df = pd.read_csv(data_path)

        st.subheader("📄 Uploaded Data")
        st.dataframe(df)

        # Pass DataFrame (not file path) to the model
        bottlenecks_df = detect_bottlenecks(df)

        if bottlenecks_df.empty:
            st.success("✅ No bottlenecks detected!")
        else:
            st.subheader("🛑 Detected Bottlenecks")
            st.dataframe(bottlenecks_df)

            suggestions = suggest_improvements(bottlenecks_df)
            st.subheader("💡 Suggested Improvements")
            for i, suggestion in enumerate(suggestions, 1):
                st.markdown(f"{i}. {suggestion}")

    except Exception as e:
        st.error(f"❌ Error: {e}")
