---
layout: paper
title: "Inference for Stochastic Chemical Kinetics Using Moment Equations and System Size Expansion"
authors: "Fröhlich F, Thomas P, Kazeroonian A, Theis FJ, Grima R, Hasenauer J"
year: 2016
ref: "Fröhlich et al. 2016. PLoS Comput. Biol."
journal: "PLoS Computational Biology"
pdflink: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005030&type=printable
pdf: 
doi: 10.1371/journal.pcbi.1005030
volume: 12
issue: 7
pages: "1-28"
preprint: False
code: https://doi.org/10.1371/journal.pcbi.1005030.s002
---

# Abstract

Quantitative mechanistic models are valuable tools for disentangling biochemical pathways and for achieving a comprehensive understanding of biological systems. However, to be quantitative the parameters of these models have to be estimated from experimental data. In the presence of significant stochastic fluctuations this is a challenging task as stochastic simulations are usually too time-consuming and a macroscopic description using reaction rate equations (RREs) is no longer accurate. In this manuscript, we therefore consider moment-closure approximation (MA) and the system size expansion (SSE), which approximate the statistical moments of stochastic processes and tend to be more precise than macroscopic descriptions. We introduce gradient-based parameter optimization methods and uncertainty analysis methods for MA and SSE. Efficiency and reliability of the methods are assessed using simulation examples as well as by an application to data for Epo-induced JAK/STAT signaling. The application revealed that even if merely population-average data are available, MA and SSE improve parameter identifiability in comparison to RRE. Furthermore, the simulation examples revealed that the resulting estimates are more reliable for an intermediate volume regime. In this regime the estimation error is reduced and we propose methods to determine the regime boundaries. These results illustrate that inference using MA and SSE is feasible and possesses a high sensitivity.
