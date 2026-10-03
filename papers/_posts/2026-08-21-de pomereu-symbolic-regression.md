---
layout: paper
title: "Symbolic regression enables coarse-grained model discovery of intracellular signalling dynamics"
authors: "de Pomereu T, Fröhlich F"
year: 2026
ref: "de Pomereu et al. 2026. bioRxiv"
journal: "bioRxiv"
pdflink: https://www.biorxiv.org/content/10.64898/2026.08.20.745973v1.full.pdf
pdf: 
doi: 10.64898/2026.08.20.745973
volume: 
issue: 
pages: ""
preprint: True
code: https://github.com/frohlich-lab/symbolic_regression_signalling
---

# Abstract

Cells respond to their environment through protein networks often dysregulated in cancer, making dynamical modelling crucial. Limitations in experimental data and computational resources motivate coarse-graining methods to build low-dimensional descriptions. Yet classical approaches to coarse-grained modelling rely on strong assumptions, leaving it unclear when partial experimental observations support reduced descriptions of system dynamics. Here we show that symbolic regression (SR) provides a data-driven way to test whether, and how compactly, the dynamics of a signalling system coarse-grain over the measured variables, and, when they do, infers mechanistically interpretable models. In synthetic enzyme systems, SR recovers Michaelis-Menten kinetics for the two-step mechanism and under three-step extensions. As data quality is degraded, SR simplifies toward effective kinetic laws while preserving correct theoretical limits. Applied to published time-resolved ERK phosphorylation data, SR identifies compact phospho-ERK rate laws in selected cancer-relevant gene overexpression contexts, yielding interpretable kinetic effects. A sparse neural ODE baseline requires few inputs where SR succeeds, but on average more where it fails, indicating that, where a reduced model is learnable at all, SR failure is associated with more complex dynamics that a simple mathematical model cannot describe. Together, these findings establish symbolic regression as a way to test when a compact coarse-grained description is warranted, generating hypotheses where one holds and motivating potential new measurements where it does not.
