---
layout: paper
title: "PEtab.jl: advancing the efficiency and utility of dynamic modelling"
authors: "Persson S, Fröhlich F, Grein S, Loman T, Ognissanti D, Hasselgren V, Hasenauer J, Cvijovic M"
year: 2025
ref: "Persson et al. 2025. Bioinformatics"
journal: "Bioinformatics"
pdflink: https://academic.oup.com/bioinformatics/article-pdf/41/9/btaf497/64232071/btaf497.pdf
pdf: 
doi: 10.1093/bioinformatics/btaf497
volume: 41
issue: 9
pages: "btaf497"
preprint: False
code: https://github.com/sebapersson/PEtab.jl
---

# Abstract

Dynamic models represent a powerful tool for studying complex biological processes, ranging from cell signalling to cell differentiation. Building such models often requires computationally demanding modelling workflows, such as model exploration and parameter estimation. We developed two Julia-based tools: SBMLImporter.jl, an SBML importer, and PEtab.jl, an importer for parameter estimation problems in the PEtab format, designed to streamline modelling processes. These tools leverage Julia's high-performance computing capabilities, including symbolic pre-processing and advanced ODE solvers. PEtab.jl aims to be a Julia-accessible toolbox that supports the entire modelling pipeline from parameter estimation to identifiability analysis. SBMLImporter.jl and PEtab.jl are implemented in the Julia programming language. Both packages are available on GitHub (github.com/sebapersson/SBMLImporter.jl and github.com/sebapersson/PEtab.jl) as officially registered Julia packages, installable via the Julia package manager. Each package is continuously tested and supported on Linux, macOS, and Windows.
