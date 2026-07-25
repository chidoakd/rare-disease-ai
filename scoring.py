from retriever import get_variant_data

def phenotype_score(patient_phenotypes, gene_phenotypes):
    matched_phenotypes = (
        set(patient_phenotypes)
        & set(gene_phenotypes)
    )

    if len(patient_phenotypes) == 0:
        return 0

    match_ratio = (
        len(matched_phenotypes)
        / len(patient_phenotypes)
    )

    score = match_ratio * 40

    return score


patient_phenotypes = [
    "seizure",
    "hypotonia",
    "developmental delay",
]

gene_phenotypes = [
    "seizure",
    "hypotonia",
]

result = phenotype_score(
    patient_phenotypes,
    gene_phenotypes,
)

print(result)


def rarity_score(allele_frequency):

    if allele_frequency <= 0.00001:
        return 20

    elif allele_frequency <= 0.0001:
        return 16

    elif allele_frequency <= 0.001:
        return 12

    elif allele_frequency <= 0.01:
        return 6

    else:
        return 0
    
print(rarity_score(0.000001))
print(rarity_score(0.0005))
print(rarity_score(0.02))

def total_score(patient_phenotypes, gene_phenotypes, allele_frequency):

    phenotype = phenotype_score(patient_phenotypes, gene_phenotypes)

    rarity = rarity_score(allele_frequency)

    total = phenotype + rarity

    return total

patient = [
    "seizure",
    "hypotonia",
    "developmental delay"
]

gene = [
    "seizure",
    "hypotonia"
]

print(total_score(patient, gene, 0.000001))


def clinvar_score(clinical_significance):

    if clinical_significance == "Pathogenic":
        return 25

    elif clinical_significance == "Likely Pathogenic":
        return 20

    elif clinical_significance == "VUS":
        return 10

    elif clinical_significance == "Likely Benign":
        return 5

    else:
        return 0
    
def total_score(
    patient_phenotypes,
    gene_phenotypes,
    allele_frequency,
    clinical_significance,
):

    phenotype = phenotype_score(
        patient_phenotypes,
        gene_phenotypes
    )

    rarity = rarity_score(
        allele_frequency
    )

    clinvar = clinvar_score(
        clinical_significance
    )

    total = phenotype + rarity + clinvar

    return total

#print(
#    total_score(
#       patient,
#       gene,
#       0.000001,
#       "Pathogenic",
#    )
#)


variant = get_variant_data()

score = total_score(
    patient,
    variant["gene_phenotypes"],
    variant["allele_frequency"],
    variant["clinical_significance"],
)

print(score) 

