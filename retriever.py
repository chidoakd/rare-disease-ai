def get_variant_data():

    variant = {
        "gene": "KCNQ2",
        "allele_frequency": 0.000001,
        "clinical_significance": "Pathogenic",
        "gene_phenotypes": [
            "seizure",
            "hypotonia",
            "developmental delay"
        ]
    }

    return variant

variant = get_variant_data()

print(variant["gene"])
print(variant["allele_frequency"])
print(variant["clinical_significance"])

