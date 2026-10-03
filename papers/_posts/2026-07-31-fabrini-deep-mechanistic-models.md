---
layout: paper
title: "Deep Mechanistic Models reveal pathway-extrinsic drivers of mammary MAPK signalling heterogeneity"
authors: "Fabrini G, Fröhlich F"
year: 2026
ref: "Fabrini et al. 2026. bioRxiv"
journal: "bioRxiv"
pdflink: https://www.biorxiv.org/content/10.64898/2026.07.30.741759v1.full.pdf
pdf: 
doi: 10.64898/2026.07.30.741759
volume: 
issue: 
pages: ""
preprint: True
code: https://github.com/frohlich-lab/DeepMechanisticModels
---

# Abstract

Cells sense and respond to their environment through signalling pathways, and the dynamics of these pathways shape cell fate even within genetically identical populations. Two largely separate computational traditions describe this behaviour: mechanistic differential-equation models and representation-learning methods. Mechanistic models encode pathway topology and kinetics but cannot easily represent variation arising outside the modelled pathway. Representation learning, instead, maps genome-wide measurements onto low-dimensional manifolds but offers no mechanistic account of how the resulting cell states execute their functions. Reconciling these views, explaining signalling heterogeneity in a manner that is at once data-driven and mechanistically interpretable, has remained difficult. Here we introduce deep mechanistic models (DMMs), which couple semi-supervised representation learning to an ordinary-differential-equation model of EGFR/MAPK signalling, trained end-to-end so that the learnt representation and mechanistic parametrisation inform each other. Applying DMMs to multiplexed signalling data from 63 breast cancer cell lines, we show that the models generalise to held-out cell lines and attribute most heterogeneity to pathway-extrinsic factors, namely baseline ERBB2 activation and a Ca²⁺/p38 signalling axis, rather than to variation in core MAPK components. Where the models fail, the discrepancies pinpoint rare signalling-altering mutations and recurrent programmes, including a putative AMPK–BRAF MEK-inhibitor-resistance axis and a cytoskeletal programme. We further find that mechanistic integration of EGFR receptor levels reshapes the learnt representation, rendering a molecular and a systems-level account of the same data equivalent in predictive power. DMMs thus offer a general framework for fusing mechanism with learning, naturally extendable to further modalities such as imaging, and simultaneously turn model failure into a systematic route to discover and evaluate candidate biology.
