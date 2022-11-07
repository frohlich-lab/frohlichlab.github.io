---
layout: paper
title: "Efficient computation of adjoint sensitivities at steady-state in ODE models of biochemical reaction networks"
authors: "Lakrisenko P, Stapor P, Grein S, Paszkowski {, Pathirana D, Fröhlich F, Lines GT, Weindl D, Hasenauer J"
year: 2022
ref: "Lakrisenko et al. 2022. bioRxiv"
journal: "bioRxiv"
pdflink: https://www.biorxiv.org/content/early/2022/08/11/2022.08.08.503176.full.pdf
pdf: 
doi: 10.1101/2022.08.08.503176
volume: 
issue: 
pages: ""
preprint: True
code: 
---

# Abstract

Dynamical models in the form of systems of ordinary differential equations have become a standard tool in systems biology. Many parameters of such models are usually unknown and have to be inferred from experimental data. Gradient-based optimization has proven to be effective for parameter estimation. However, computing gradients becomes increasingly costly for larger models, which are required for capturing the complex interactions of multiple biochemical pathways. Adjoint sensitivity analysis has been pivotal for working with such large models, but methods tailored for steady-state data are currently not available. We propose a new adjoint method for computing gradients, which is applicable if the experimental data include steady-state measurements. The method is based on a reformulation of the backward integration problem to a system of linear algebraic equations. The evaluation of the proposed method using real-world problems shows a speedup of total simulation time by a factor of up to 4.4. Our results demonstrate that the proposed approach can achieve a substantial improvement in computation time, in particular for large-scale models, where computational efficiency is critical.Author summary Large-scale dynamical models are nowadays widely used for the analysis of complex processes and the integration of large-scale data sets. However, computational cost is often a bottleneck. Here, we propose a new gradient computation method that facilitates the parameterization of large-scale models based on steady-state measurements. The method can be combined with existing gradient computation methods for time-course measurements. Accordingly, it is an essential contribution to the environment of computationally efficient approaches for the study of large-scale screening and omics data, but not tailored to biological applications, and, therefore, also useful beyond the field of computational biology.
