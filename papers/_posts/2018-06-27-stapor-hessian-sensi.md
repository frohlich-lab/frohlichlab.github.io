---
layout: paper
title: "Optimization and profile calculation of ODE models using second order adjoint sensitivity analysis"
authors: "Stapor P, Fröhlich F, Hasenauer J"
year: 2018
ref: "Stapor et al. 2018. Bioinformatics"
journal: "Bioinformatics"
pdflink: https://academic.oup.com/bioinformatics/article-pdf/34/13/i151/25098355/bty230.pdf
pdf: 
doi: 10.1093/bioinformatics/bty230
volume: 34
issue: 13
pages: "i151-i159"
preprint: False
code: https://github.com/AMICI-dev/AMICI
---

# Abstract

Parameter estimation methods for ordinary differential equation (ODE) models of biological processes can exploit gradients and Hessians of objective functions to achieve convergence and computational efficiency. However, the computational complexity of established methods to evaluate the Hessian scales linearly with the number of state variables and quadratically with the number of parameters. This limits their application to low-dimensional problems.We introduce second order adjoint sensitivity analysis for the computation of Hessians and a hybrid optimization-integration-based approach for profile likelihood computation. Second order adjoint sensitivity analysis scales linearly with the number of parameters and state variables. The Hessians are effectively exploited by the proposed profile likelihood computation approach. We evaluate our approaches on published biological models with real measurement data. Our study reveals an improved computational efficiency and robustness of optimization compared to established approaches, when using Hessians computed with adjoint sensitivity analysis. The hybrid computation method was more than 2-fold faster than the best competitor. Thus, the proposed methods and implemented algorithms allow for the improvement of parameter estimation for medium and large scale ODE models.
