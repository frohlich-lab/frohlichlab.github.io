---
title: SciML Software
icon: /assets/images/research/sciml.png
order: 3
---
SciML methods are often developed within individual projects and demand substantial numerical expertise, which limits their reuse and adoption. We turn them into reusable community software, from data processing and problem specification to model training. PEtab SciML extends the [PEtab] standard to hybrid mechanistic and machine learning models, with software support in Python (JAX) and Julia \[[Persson *et al.* 2026a]\], and builds on the second version of PEtab \[[Pathirana *et al.* 2026]\]. Curriculum multiple shooting makes training neural and universal differential equations robust \[[Persson *et al.* 2026b]\]. We also maintain established tools for simulation and calibration, including [AMICI] \[[Fröhlich *et al.* 2021]\] and [pyPESTO] \[[Schälte *et al.* 2023]\]. More recently, we have started to integrate these tools into agentic workflows for mechanistic world modelling \[[de Pomereu *et al.* 2026]\].

[PEtab]: {% link _tools/PEtab.md %}
[AMICI]: {% link _tools/amici.md %}
[pyPESTO]: {% link _tools/pypesto.md %}
[Persson *et al.* 2026a]: {% post_url papers/2026-08-20-persson-petab-sciml %}
[Pathirana *et al.* 2026]: {% post_url papers/2026-08-13-pathirana-petab-v2 %}
[Persson *et al.* 2026b]: {% post_url papers/2026-08-06-persson-curriculum-shooting %}
[Fröhlich *et al.* 2021]: {% post_url papers/2021-04-02-frohlich-amici-simulation %}
[Schälte *et al.* 2023]: {% post_url papers/2023-11-23-schalte-pypesto %}
[de Pomereu *et al.* 2026]: {% post_url papers/2026-09-28-de pomereu-gemot %}
