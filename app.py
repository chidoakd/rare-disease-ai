import streamlit as st

from retriever import get_variant_data
from scoring import total_score

st.set_page_config(page_title="Rare Disease Prediction", layout="wide")
st.title("🧬 Rare Disease AI")
st.write("Welcome to our genomic variant prioritization system.")


patient = [
    "seizure",
    "hypotonia",
    "developmental delay",
]

if st.button("Analyze Variant"):

    variant = get_variant_data()

    score = total_score(
        patient,
        variant["gene_phenotypes"],
        variant["allele_frequency"],
        variant["clinical_significance"],
    )

    st.subheader("Priority Score")
    st.metric("Variant Score", score)

