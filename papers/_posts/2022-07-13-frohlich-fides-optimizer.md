---
layout: paper
title: "Fides: Reliable trust-region optimization for parameter estimation of ordinary differential equation models"
authors: "Fröhlich F, Sorger PK"
year: 2022
ref: "Fröhlich et al. 2022. PLoS Comput. Biol."
journal: "PLoS Computational Biology"
pdflink: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1010322&type=printable
pdf: 
doi: 10.1371/journal.pcbi.1010322
volume: 18
issue: 7
pages: "1-28"
preprint: False
code: https://github.com/fides-dev/fides-benchmark
---

# Abstract

Ordinary differential equation (ODE) models are widely used to study biochemical reactions in cellular networks since they effectively describe the temporal evolution of these networks using mass action kinetics. The parameters of these models are rarely known a priori and must instead be estimated by calibration using experimental data. Optimization-based calibration of ODE models on is often challenging, even for low-dimensional problems. Multiple hypotheses have been advanced to explain why biochemical model calibration is challenging, including non-identifiability of model parameters, but there are few comprehensive studies that test these hypotheses, likely because tools for performing such studies are also lacking. Nonetheless, reliable model calibration is essential for uncertainty analysis, model comparison, and biological interpretation. We implemented an established trust-region method as a modular Python framework (fides) to enable systematic comparison of different approaches to ODE model calibration involving a variety of Hessian approximation schemes. We evaluated fides on a recently developed corpus of biologically realistic benchmark problems for which real experimental data are available. Unexpectedly, we observed high variability in optimizer performance among different implementations of the same mathematical instructions (algorithms). Analysis of possible sources of poor optimizer performance identified limitations in the widely used Gauss-Newton, BFGS and SR1 Hessian approximation schemes. We addressed these drawbacks with a novel hybrid Hessian approximation scheme that enhances optimizer performance and outperforms existing hybrid approaches. When applied to the corpus of test models, we found that fides was on average more reliable and efficient than existing methods using a variety of criteria. We expect fides to be broadly useful for ODE constrained optimization problems in biochemical models and to be a foundation for future methods development.
