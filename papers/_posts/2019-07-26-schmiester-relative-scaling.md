---
layout: paper
title: "Efficient parameterization of large-scale dynamic models based on relative measurements"
authors: "Schmiester L, Schälte Y, Fröhlich F, Hasenauer J, Weindl D"
year: 2019
ref: "Schmiester et al. 2019. Bioinformatics"
journal: "Bioinformatics"
pdflink: https://academic.oup.com/bioinformatics/article-pdf/36/2/594/31962762/btz581.pdf
pdf: 
doi: 10.1093/bioinformatics/btz581
volume: 36
issue: 2
pages: "594-602"
preprint: False
code: https://github.com/ICB-DCM/CS_Signalling_ERBB_RAS_AKT
---

# Abstract

Mechanistic models of biochemical reaction networks facilitate the quantitative understanding of biological processes and the integration of heterogeneous datasets. However, some biological processes require the consideration of comprehensive reaction networks and therefore large-scale models. Parameter estimation for such models poses great challenges, in particular when the data are on a relative scale.Here, we propose a novel hierarchical approach combining (i) the efficient analytic evaluation of optimal scaling, offset and error model parameters with (ii) the scalable evaluation of objective function gradients using adjoint sensitivity analysis. We evaluate the properties of the methods by parameterizing a pan-cancer ordinary differential equation model (>1000 state variables, >4000 parameters) using relative protein, phosphoprotein and viability measurements. The hierarchical formulation improves optimizer performance considerably. Furthermore, we show that this approach allows estimating error model parameters with negligible computational overhead when no experimental estimates are available, providing an unbiased way to weight heterogeneous data. Overall, our hierarchical formulation is applicable to a wide range of models, and allows for the efficient parameterization of large-scale models based on heterogeneous relative measurements.
