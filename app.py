##################################################
# app.py
#
# Streamlit interface for the Rare Disease AI project.
# Users can analyze candidate variants and view
# prioritization scores.
##################################################

import streamlit as st

from retriever import get_variant_data
from scoring import total_score, score_breakdown


st.set_page_config(
    page_title="Rare Disease Prediction",
    layout="wide"
)

st.title("🧬 Rare Disease AI")
st.write("Welcome to our genomic variant prioritization system.")


patient = st.multiselect(
    "Patient Phenotypes",
    [
        "seizure",
        "hypotonia",
        "developmental delay",
        "ataxia",
        "microcephaly",
        "epilepsy",
    ],
    default=[
        "seizure",
        "hypotonia",
        "developmental delay",
    ]
)


if st.button("Analyze Variant"):

    variants = get_variant_data()
    results = []

    for variant in variants:

        score = total_score(
            patient,
            variant["gene_phenotypes"],
            variant["allele_frequency"],
            variant["clinical_significance"],
        )

        breakdown = score_breakdown(
            patient,
            variant["gene_phenotypes"],
            variant["allele_frequency"],
            variant["clinical_significance"],
        )

        results.append({
            "Gene": variant["gene"],
            "Score": score,
            "Phenotype Score": breakdown["phenotype"],
            "Rarity Score": breakdown["rarity"],
            "ClinVar Score": breakdown["clinvar"],
            "Classification": variant["clinical_significance"],
        })

    results = sorted(
        results,
        key=lambda x: x["Score"],
        reverse=True
    )

    st.subheader("Candidate Variants")
    st.table(results)