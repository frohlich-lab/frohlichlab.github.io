---
layout: paper
title: "Parameter estimation for dynamical systems with discrete events and logical operations"
authors: "Fröhlich F, Theis FJ, Rädler JO, Hasenauer J"
year: 2016
ref: "Fröhlich et al. 2016. Bioinformatics"
journal: "Bioinformatics"
pdflink: https://academic.oup.com/bioinformatics/article-pdf/33/7/1049/25149840/btw764.pdf
pdf: 
doi: 10.1093/bioinformatics/btw764
volume: 33
issue: 7
pages: "1049-1056"
preprint: False
code: 
---

# Abstract

Ordinary differential equation (ODE) models are frequently used to describe the dynamic behaviour of biochemical processes. Such ODE models are often extended by events to describe the effect of fast latent processes on the process dynamics. To exploit the predictive power of ODE models, their parameters have to be inferred from experimental data. For models without events, gradient based optimization schemes perform well for parameter estimation, when sensitivity equations are used for gradient computation. Yet, sensitivity equations for models with parameter- and state-dependent events and event-triggered observations are not supported by existing toolboxes.In this manuscript, we describe the sensitivity equations for differential equation models with events and demonstrate how to estimate parameters from event-resolved data using event-triggered observations in parameter estimation. We consider a model for GFP expression after transfection and a model for spiking neurons and demonstrate that we can improve computational efficiency and robustness of parameter estimation by using sensitivity equations for systems with events. Moreover, we demonstrate that, by using event-outputs, it is possible to consider event-resolved data, such as time-to-event data, for parameter estimation with ODE models. By providing a user-friendly, modular implementation in the toolbox AMICI, the developed methods are made publicly available and can be integrated in other systems biology toolboxes.
