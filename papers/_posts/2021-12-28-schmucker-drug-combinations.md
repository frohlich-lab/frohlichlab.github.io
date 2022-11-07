---
layout: paper
title: "Combination treatment optimization using a pan-cancer pathway model"
authors: "Schmucker R, Farina G, Faeder J, Fröhlich F, Saglam AS, Sandholm T"
year: 2021
ref: "Schmucker et al. 2021. PLoS Comput. Biol."
journal: "PLoS Computational Biology"
pdflink: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1009689&type=printable
pdf: 
doi: 10.1371/journal.pcbi.1009689
volume: 17
issue: 12
pages: "1-22"
preprint: False
code: https://github.com/Sandholm-Lab/treatment-opt-pancancer
---

# Abstract

The design of efficient combination therapies is a difficult key challenge in the treatment of complex diseases such as cancers. The large heterogeneity of cancers and the large number of available drugs renders exhaustive in vivo or even in vitro investigation of possible treatments impractical. In recent years, sophisticated mechanistic, ordinary differential equation-based pathways models that can predict treatment responses at a molecular level have been developed. However, surprisingly little effort has been put into leveraging these models to find novel therapies. In this paper we use for the first time, to our knowledge, a large-scale state-of-the-art pan-cancer signaling pathway model to identify candidates for novel combination therapies to treat individual cancer cell lines from various tissues (e.g., minimizing proliferation while keeping dosage low to avoid adverse side effects) and populations of heterogeneous cancer cell lines (e.g., minimizing the maximum or average proliferation across the cell lines while keeping dosage low). We also show how our method can be used to optimize the drug combinations used in sequential treatment plans that is, optimized sequences of potentially different drug combinations providing additional benefits. In order to solve the treatment optimization problems, we combine the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) algorithm with a significantly more scalable sampling scheme for truncated Gaussian distributions, based on a Hamiltonian Monte-Carlo method. These optimization techniques are independent of the signaling pathway model, and can thus be adapted to find treatment candidates for other complex diseases than cancers as well, as long as a suitable predictive model is available.
