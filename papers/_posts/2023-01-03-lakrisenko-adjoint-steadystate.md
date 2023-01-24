---
layout: paper
title: "Efficient computation of adjoint sensitivities at steady-state in ODE models of biochemical reaction networks"
authors: "Lakrisenko P, Stapor P, Grein S, Paszkowski Ł, Pathirana D, Fröhlich F, Lines GT, Weindl D, Hasenauer J"
year: 2023
ref: "Lakrisenko et al. 2023. PLoS Comput. Biol."
journal: "PLoS Computational Biology"
pdflink: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1010783&type=printable
pdf: 
doi: 10.1371/journal.pcbi.1010783
volume: 19
issue: 1
pages: "1-19"
preprint: False
code: 
---

# Abstract

Dynamical models in the form of systems of ordinary differential equations have become a standard tool in systems biology. Many parameters of such models are usually unknown and have to be inferred from experimental data. Gradient-based optimization has proven to be effective for parameter estimation. However, computing gradients becomes increasingly costly for larger models, which are required for capturing the complex interactions of multiple biochemical pathways. Adjoint sensitivity analysis has been pivotal for working with such large models, but methods tailored for steady-state data are currently not available. We propose a new adjoint method for computing gradients, which is applicable if the experimental data include steady-state measurements. The method is based on a reformulation of the backward integration problem to a system of linear algebraic equations. The evaluation of the proposed method using real-world problems shows a speedup of total simulation time by a factor of up to 4.4. Our results demonstrate that the proposed approach can achieve a substantial improvement in computation time, in particular for large-scale models, where computational efficiency is critical.
