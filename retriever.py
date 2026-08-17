##################################################
# retriever.py
#
# Retrieves candidate genetic variants.
# In a production system this module would query
# ClinVar, gnomAD, or another genomic database.
##################################################

def get_variant_data():

    variants = [
        {
            "gene": "KCNQ2",
            "allele_frequency": 0.000001,
            "clinical_significance": "Pathogenic",
            "gene_phenotypes": [
                "seizure",
                "hypotonia",
                "developmental delay"
            ]
        },

        {
            "gene": "SCN2A",
            "allele_frequency": 0.0005,
            "clinical_significance": "VUS",
            "gene_phenotypes": [
                "seizure",
                "developmental delay"
            ]
        },

        {
            "gene": "STXBP1",
            "allele_frequency": 0.00001,
            "clinical_significance": "Likely Pathogenic",
            "gene_phenotypes": [
                "seizure",
                "hypotonia",
                "developmental delay"
            ]
        }
    ]

    return variants
