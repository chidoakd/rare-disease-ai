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

    return match_ratio * 40


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

    return phenotype + rarity + clinvar


def score_breakdown(
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

    return {
        "phenotype": phenotype,
        "rarity": rarity,
        "clinvar": clinvar,
        "total": phenotype + rarity + clinvar,
    }


