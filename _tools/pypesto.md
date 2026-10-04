---
layout: project
title: pyPESTO
tagline: python Parameter EStimation TOolbox
github: ICB-DCM/pyPESTO
image: /assets/images/projects/pypesto.png
description: Widely applicable and highly customizable toolbox for parameter estimation.
order: 1
---

pyPESTO is a software tool to solve parameter estimation problems. It supports
optimization based and sampling based parameter estimation and uncertainty analysis.
It provides interfaces to state of the art optimization and sampling libraries
such as [pymc] and [fides], including both gradient-based and derivative-free
methods.

Users can import problems specified in [PEtab] or define their own objective
functions.

pyPESTO is jointly developed with the [Hasenauer Lab] and supersedes the MATLAB
toolbox described

- [Stapor et al. 2017]({% post_url papers/2017-10-23-stapor-pesto-estimation%})

[pymc]: https://www.pymc.io
[fides]: {% link _tools/fides.md %}
[PETab]: {% link _tools/PEtab.md %}
[Hasenauer Lab]: https://www.mathematics-and-life-sciences.uni-bonn.de/en/research/hasenauer-group
