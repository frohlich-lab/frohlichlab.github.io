---
layout: paper
title: "Benchmarking optimization methods for parameter estimation in large kinetic models"
authors: "Villaverde AF, Fröhlich F, Weindl D, Hasenauer J, Banga JR"
year: 2018
ref: "Villaverde et al. 2018. Bioinformatics"
journal: "Bioinformatics"
pdflink: https://academic.oup.com/bioinformatics/article-pdf/35/5/830/27994799/bty736.pdf
pdf: 
doi: 10.1093/bioinformatics/bty736
volume: 35
issue: 5
pages: "830-838"
preprint: False
code: https://zenodo.org/record/1304034#.Y2k3Zi-B2-Z
---

# Abstract

Kinetic models contain unknown parameters that are estimated by optimizing the fit to experimental data. This task can be computationally challenging due to the presence of local optima and ill-conditioning. While a variety of optimization methods have been suggested to surmount these issues, it is difficult to choose the best one for a given problem a priori. A systematic comparison of parameter estimation methods for problems with tens to hundreds of optimization variables is currently missing, and smaller studies provided contradictory findings.We use a collection of benchmarks to evaluate the performance of two families of optimization methods: (i) multi-starts of deterministic local searches and (ii) stochastic global optimization metaheuristics; the latter may be combined with deterministic local searches, leading to hybrid methods. A fair comparison is ensured through a collaborative evaluation and a consideration of multiple performance metrics. We discuss possible evaluation criteria to assess the trade-off between computational efficiency and robustness. Our results show that, thanks to recent advances in the calculation of parametric sensitivities, a multi-start of gradient-based local methods is often a successful strategy, but a better performance can be obtained with a hybrid metaheuristic. The best performer combines a global scatter search metaheuristic with an interior point local method, provided with gradients estimated with adjoint-based sensitivities. We provide an implementation of this method to render it available to the scientific community.
