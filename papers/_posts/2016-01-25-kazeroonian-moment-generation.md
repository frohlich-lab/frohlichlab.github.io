---
layout: paper
title: "CERENA: ChEmical REaction Network Analyzer - A Toolbox for the Simulation and Analysis of Stochastic Chemical Kinetics"
authors: "Kazeroonian A, Fröhlich F, Raue A, Theis FJ, Hasenauer J"
year: 2016
ref: "Kazeroonian et al. 2016. PLoS One"
journal: "PLoS One"
pdflink: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0146732&type=printable
pdf: 
doi: 10.1371/journal.pone.0146732
volume: 11
issue: 1
pages: "1-15"
preprint: False
code: https://github.com/CERENADevelopers/CERENA
---

# Abstract

Gene expression, signal transduction and many other cellular processes are subject to stochastic fluctuations. The analysis of these stochastic chemical kinetics is important for understanding cell-to-cell variability and its functional implications, but it is also challenging. A multitude of exact and approximate descriptions of stochastic chemical kinetics have been developed, however, tools to automatically generate the descriptions and compare their accuracy and computational efficiency are missing. In this manuscript we introduced CERENA, a toolbox for the analysis of stochastic chemical kinetics using Approximations of the Chemical Master Equation solution statistics. CERENA implements stochastic simulation algorithms and the finite state projection for microscopic descriptions of processes, the system size expansion and moment equations for meso- and macroscopic descriptions, as well as the novel conditional moment equations for a hybrid description. This unique collection of descriptions in a single toolbox facilitates the selection of appropriate modeling approaches. Unlike other software packages, the implementation of CERENA is completely general and allows, e.g., for time-dependent propensities and non-mass action kinetics. By providing SBML import, symbolic model generation and simulation using MEX-files, CERENA is user-friendly and computationally efficient. The availability of forward and adjoint sensitivity analyses allows for further studies such as parameter estimation and uncertainty analysis.
