---
layout: post
title: Hiring scientists in the age of AI
description: "When papers and grants stop being currency: a proposal to the research community from the Fröhlich Lab."
# The blog page shows the text above this marker, with a link to the full post.
excerpt_separator: <!--more-->
---
*When papers and grants stop being currency: a proposal to the research community.*

AI can now write the paper, draft the grant and polish the CV. Papers and grants were imperfect proxies for good science long before AI, but AI accelerates their failure. Meanwhile the qualities that actually matter are becoming more valuable, not less. This piece sets out what those qualities are, why current evaluation struggles to see them, and how hiring and funding can adapt.

<!--more-->

*The boxes in this post hold background, evidence and detail. They are closed by default, and the argument reads without them.*

## What science needs from its people

In the age of AI, science should select for intellectual character, not for skills or output. AI increasingly supplies the skills and the output. Character decides how someone uses AI, and AI amplifies whatever it is given, so character is what hiring committees and funders are really choosing.

- **Curiosity.** Wanting to know, not wanting to have produced.
- **Honesty and humility.** Saying "I don't know" and "I was wrong", and resisting fluent, plausible answers, including from AI models.
- **Independence and courage.** Holding unfashionable views and following odd questions.
- **Judgement.** Knowing what matters and when evidence is enough.
- **Adaptability.** Learning and unlearning as tools and roles change every few years.
- **Generosity and trustworthiness.** Sharing, crediting fairly and keeping commitments.
- **Responsibility.** Remaining the author of what one, and any tools or agents acting on one's behalf, put into the world.

<details class="aside" markdown="1">
<summary markdown="span">Where this list comes from</summary>

Responsibilist virtue epistemology ([Zagzebski 1996](https://doi.org/10.1017/CBO9781139174763); Roberts & Wood 2007) gives the vocabulary: it treats good knowers as defined by traits of intellectual character, not only by reliable skills. Several of the traits have a literature of their own:

- **Honesty and humility.** Fluent, plausible answers from AI models can create [illusions of understanding](https://doi.org/10.1038/s41586-024-07146-0) (Messeri & Crockett 2024).
- **Independence and courage.** Diverse perspectives are an epistemic resource (Longino 1990).
- **Judgement.** Aristotle's *phronesis*, practical wisdom. Deciding when evidence suffices is value-laden, and scientists are responsible for it (Douglas 2009).
- **Generosity and trustworthiness.** Science runs on trust networks.

</details>

## The problem: AI makes these traits harder to see

Academic careers run on two currencies, papers and grants. The community has used them as proxies for these virtues. A paper suggested someone found a question worth asking, did the work, checked it and stood behind it. A grant suggested good ideas and peer endorsement. Both proxies were already weak; AI is breaking them faster.

AI is unbundling the paper. Writing, analysis and even hypothesis generation are becoming cheap, so a paper no longer proves the scarce parts happened. Publication counts were already gameable, and paper mills have industrialised the gaming.

Grants are failing in parallel. Persuasive writing is now cheap, so a polished proposal shows little about its author. And grant income was never a clean signal: it measures luck, network and timing as well as quality.

<details class="aside" markdown="1">
<summary markdown="span">Grant outcomes were noisy before AI</summary>

Reviewers agree poorly near the funding line ([Heyard et al. 2022](https://doi.org/10.1080/2330443X.2022.2086190)). Success also compounds. Near-identical applicants diverge sharply after one early win, partly because near-misses stop applying ([Bol et al. 2018](https://doi.org/10.1073/pnas.1719557115)).

</details>

Cover letters, research statements and proposals are now uniformly fluent. Bibliometrics and grant totals took over evaluation because they were cheap, not because they were valid ([DORA](https://sfdora.org/read/)). Meanwhile the virtues above matter more: when output is cheap, people driven by output drown in it, and those who think against the grain become harder to replace.

The obvious fix, reading everything carefully, runs into the real constraint: **human attention is the bottleneck**. A single postdoc call can draw hundreds of applications, and funders face the same problem at far larger scale as AI cuts the cost of writing proposals. No one can spend more attention, only spend it in different places. Verification is also easier in the computational world than the experimental one: code and commits leave machine-readable traces, while bench skill and care mostly do not.

## Principles for evaluation in the age of AI

1. **Machines verify; people judge.** Automation should check facts and flag problems. It should never rank quality or read character.
2. **Evidence should be costly to fake.** Trust what others have asserted, timestamped and reused, not what applicants say about themselves.
3. **Spend human attention late, and spend it well.** Cheap, robust stages should shrink the pool. Human time goes to a few, in structured formats, which are among the most valid selection methods in employment generally ([Sackett et al. 2022](https://doi.org/10.1037/apl0000994)).
4. **Model uncertainty honestly.** Above a competence floor, documents barely discriminate. Select in proportion to the probability of being among the best, rather than pretend to a precise ranking.
5. **Don't offload costs onto others.** Saving evaluators' attention must not mean spending referees' or applicants' time on things no one reads. Contact referees only for shortlisted candidates.
6. **Normalise for opportunity.** Read records per year of career and per unit of resources received, with person-time and facility use costed at standard rates, compared within fields, and adjusted for documented breaks and career path.
7. **Assume AI help, and design around it.** Do not use AI-text detection. Ask questions where judgement and specificity matter more than prose.
8. **Publish criteria, not weights.** Every published metric decays once targeted ([Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)). Rotate weights and audit outcomes. Applicants are still entitled to a meaningful explanation of how decisions are made, so this is a balance, not a secret.
9. **Let the strength of evidence set the method.** Where verifiable evidence is rich, use it. Where it is sparse, for early-career researchers, new fields and recent work, rely less on metrics and more on randomisation and structured human judgement, rather than penalising people for what cannot yet be measured.

## The new currency: evidence that is costly to fake

AI can generate any text. It is much harder to retroactively create a third-party record, a multi-year deposit history, or reuse by independent groups. Nothing is impossible to fake, so the design rule is simple: credit comes mainly from **reuse by others**. A fabricated artefact that nobody uses earns nothing.

A signal is costly to fake when it is:

- **Asserted by a third party.** A publisher, repository, funder or institution writes the record, not the researcher.
- **Timestamped by the platform or an archive.** Archive snapshots such as Software Heritage or Zenodo count, not dates the researcher can set, such as git commit dates.
- **Costly to produce.** Real data, reagents and working tools take real work.
- **Used by independent others.** Reuse by people with no stake in the researcher is the strongest signal.
- **Cross-checkable.** Several sources must agree, such as a DOI, an ORCID record and a repository.

Most of this already exists in public infrastructure and can be checked from a single ORCID iD.

<details class="aside" markdown="1">
<summary markdown="span">Eleven signals, who asserts them, and why they are costly to fake</summary>

| Signal | Asserted by | Why it is costly to fake |
| --- | --- | --- |
| Outputs exist, with matching authorship and CRediT roles | Publishers via Crossref/DataCite | Third-party record, cross-checked |
| Code and data behind published papers actually resolve | Repositories and archives (Zenodo, Software Heritage, institutional) | Public, archive-timestamped, inspectable |
| Maintainer roles on tools others depend on | Package registries (PyPI, CRAN, Bioconductor, conda-forge) | Self-asserted, so meaningful only where independent projects depend on the tool |
| Raw data deposited at publication | GEO/SRA, PRIDE, FlowRepository, BioImage Archive, PDB | Curated deposits, dated, tied to papers |
| Reagents and protocols shared | Addgene, protocols.io, animal and cell repositories | Physical material, requests by others |
| Negative and null results made available | Preprint servers, data repositories, registered reports | Timestamped, citable; credited only with controls showing the method worked |
| Rigour reporting | RRIDs, cell-line checks against Cellosaurus/ICLAC | Machine-checkable identifiers |
| Breadth of independent reuse | OpenAlex (papers), DataCite and Make Data Count (datasets), software dependents | Requires many independent groups to act |
| Delivery relative to resources | Institutions via ORCID and grant DOIs, reconciled with funders and audited accounts | Complete accounting: every resource attributed exactly once |
| Open practices | Preprint servers, registries, ORCID peer-review records | Timestamped third-party records |
| Integrity flags | Retraction Watch (via Crossref), PubPeer, image-integrity screening | Independent scrutiny; for human review only |

</details>

What does **not** belong on this list includes journal impact factor, h-index, raw paper counts, author position, lines of code, commit counts, downloads, stars, grant income, number of awards, self-reported skills, and AI-text detection.

Not all good work can be public. Industry projects, embargoed work and unpublished theses also count. Evaluators should accept such work when a named supervisor or collaborator verifies it, at the stage where referees are contacted.

This works only if the records exist. Today they are patchy, patchier for experimental than computational work, and uneven across fields. Fixing that is a collective task.

## From virtues to evidence

Verifiable evidence can show some virtues; others only show in structured human assessment. Being explicit about which is which keeps the system honest about what it measures.

<details class="aside" markdown="1">
<summary markdown="span">Virtue by virtue: what machines can verify and what people must assess</summary>

| Virtue | Verifiable evidence (machine) | Structured human assessment |
| --- | --- | --- |
| Curiosity | None reliable | Live follow-up questions on a topic of the candidate's choice; depth of the questions they ask |
| Honesty and humility | Corrections issued, negative results shared, open data | Critique of their own best work; response to challenge in conversation |
| Independence and courage | Weak: work outside supervisors' areas, unusual combinations of fields | A view they hold that their field rejects, and why |
| Judgement | None reliable | Work sample: when is this evidence enough, and what would change their mind |
| Adaptability | Weak: changes of method or field over a career | An approach they abandoned, and how |
| Generosity and trustworthiness | Breadth of reuse, maintenance, reviewing, contributor roles | References at the final stage, about specific behaviours |
| Responsibility | Integrity record, corrections | How they verified work their tools or agents produced, on a real example |

</details>

Two virtues, curiosity and judgement, have no machine signal at all, and independence has only a weak one. Verifiable evidence therefore sets a floor; it cannot select for the qualities that matter most. Systems built on reuse also tend to reward conscientious, conventional productivity over risky, unfashionable work. Stratified selection, randomisation and human judgement at the frontier exist partly to protect independence from that bias. Human assessments of these traits should use behavioural anchors, not impressions, because judgements of confidence and courage are prone to bias towards assertive and culturally dominant styles.

## The incentives this creates: public goods become career currency

How science evaluates people shapes what they do. Papers and grant income reward private credit: the more you hold back data, code and reagents, the longer you keep your advantage. Sharing has been something researchers do despite their incentives, not because of them. It is a classic public-goods problem: everyone benefits from shared resources, but each individual bears the cost of providing them.

Open science has tried to fix this with mandates. Data-management plans, availability statements and repository requirements ask researchers to make *everything* available. In practice this often produces a compliance burden. Data are dumped to tick a box, poorly documented and rarely reused, and the effort is resented rather than rewarded.

Evaluating people on verifiable, *reused* contributions changes the logic. The question is no longer "did you share everything?" but "did you make available the things that matter to others?" Researchers are rewarded for choosing what is worth sharing, and for sharing it well:

- **Data, code and protocols that others actually use** become evidence of contribution, not a compliance burden.
- **Reagents and tools** count when others request and use them, more than a paper describing them.
- **Reviewing, maintaining software and curating resources**, long invisible service work, leave records and earn credit.
- **Honest reporting and correction** stop being career risks, because integrity flags and candour are both on the record.

### Negative results can finally count

A paper-based system has no place for most negative results. A failed replication, a null effect or a model that did not work rarely makes a story a journal wants. So these results stay in drawers, other groups repeat the same dead ends, and the literature overstates what works.

When contribution is measured by what is verifiable and useful, the format no longer matters. A well-documented null dataset, a failed perturbation deposited with its protocol, or a preprint showing that a published effect does not replicate can all earn credit. Reuse alone will undervalue them, because a result that saves others from a dead end is rarely cited. So negative results need credit for being available and well documented. They also need evidence that the method worked, such as positive controls, so that a failed technique is not relabelled as a null finding.

The goal is a system where publishing what did not work is as natural, and as creditable, as publishing what did.

### Team science becomes creditable

Papers and grants compress collaboration into a single dimension. Author order turns twenty contributions into one ranking, and fights over first and last place follow. Grants credit one principal investigator for work done by many. People whose contributions don't fit the paper format are systematically undercredited. These include research software engineers, technicians, core facility staff, data curators and the people who keep shared tools alive.

Machine-readable contribution records let credit be shared without being diluted. Each person can then show exactly what they did in a large project, and no one has to win the author-order lottery to get credit. That makes it rational to join and build team efforts rather than guard small personal territories. For the same reason, reuse by collaborators must never count against anyone. It simply does not add to the *breadth* of independent reuse.

<details class="aside" markdown="1">
<summary markdown="span">Where contribution records already exist</summary>

- **CRediT roles** record who designed, investigated, analysed, wrote software or curated data.
- **Maintainer lists in package registries**, such as PyPI, CRAN, Bioconductor and conda-forge, record who is responsible for a tool.
- **Contributor fields in DataCite**, along with depositor records in repositories and Addgene, record who produced a dataset or reagent.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Why lines of code and commit counts don't count</summary>

Lines of code, commit counts and similar volume measures are bad metrics. They reward verbosity, are trivial to inflate, especially now that AI writes code, and say nothing about quality or responsibility. What counts is the role a project assigns to someone, such as maintainer, reviewer or core developer, and whether others depend on the result.

</details>

### Fewer, better grant applications

Normalising output by resources also changes how people apply for money. Today, winning grants is itself a career asset, so researchers apply for as many as they can, and reviewers drown. If evaluation divides output by resources received, extra grants only help if they produce proportionally more. Holding more money than you can use well lowers your record rather than raising it. The rational strategy becomes applying for what you need, not for everything available. That reduces the load on reviewers, frees money for others, and weakens the cumulative advantage that lets early winners keep winning.

### The bigger picture

This is Merton's norm of communalism made operational. It aligns individual incentives with the collective good, which is what the [FAIR principles](https://doi.org/10.1038/sdata.2016.18) and the open-science movement have asked for, without a reward structure to back them.

It also changes how AI is used. If prose and paper counts no longer pay, there is little reason to use AI to inflate them, and every reason to use it to produce better data, tools and checks that others can reuse.

Rewarding public goods also creates a duty to sustain them. Funders who credit shared software and data must also pay for its maintenance.

## What funders and institutions should do

Funders face the same problems from the other side. Proposals are becoming cheap to write, review capacity is not growing, and grant decisions feed straight back into hiring as a signal of quality. Fixing grant evaluation therefore also fixes a large part of hiring.

1. **Make the CV machine-readable, once.** Agree a shared structured backbone across funders and institutions, based on ORCID with trusted-source assertions: funders write awards, publishers write outputs, repositories write datasets and reagents, institutions write employment. Pair it with a short narrative for humans. One CV, maintained once, reused everywhere. Canada's move to [narrative CVs](https://casrai.org/guides/tri-agency-narrative-cv-2027-transition) is right about narrative, but it needs a verifiable machine-readable backbone beside it.
2. **Institutions should account for the resources behind research, completely.** Only host institutions see the full picture. Every resource should be attributed exactly once, with totals reconciled to audited institutional research expenditure, so nothing can be hidden (see the box below).
3. **Require persistent identifiers.** These include DOIs for outputs, RRIDs for reagents, accession numbers for data, ROR IDs for institutions, and grant DOIs. Treat experimental contributions as first-class outputs: protocols, deposits, reagents, CRediT roles.
4. **Fund the open infrastructure and its upkeep.** ORCID, Crossref, DataCite, OpenAlex, Software Heritage and the data repositories make evidence checkable. Shared software and resources need maintenance funding too, if they are to count as contributions.
5. **Fund people, not projects.** Give long, renewable, person-based awards, evaluated retrospectively. Investigators funded by HHMI's person-based model produced high-impact papers at a much higher rate than comparable NIH-funded scientists, and moved into more novel lines of inquiry ([Azoulay et al. 2011](https://doi.org/10.1111/j.1756-2171.2011.00140.x)). The evidence is observational and comes from an elite group, but it points the same way as the theory.
6. **Model uncertainty and randomise honestly.** Use Bayesian ranking, with a lottery where proposals are indistinguishable from the funding line ([Heyard et al. 2022](https://doi.org/10.1080/2330443X.2022.2086190)), or posterior sampling across the pool. Use wider randomisation bands where evidence is sparse, such as early-career schemes.
7. **Cut the cost of applying.** Use a light first stage (an ORCID iD plus two pages) and invite full proposals only from a shortlist. For high-volume schemes, consider distributed peer review ([Kerzendorf et al. 2020](https://doi.org/10.1038/s41550-020-1038-y)).
8. **Stop requiring letters up front.** Collect referee names and contact referees only for shortlisted applicants.
9. **Reward candour at renewal.** Credit honest reporting of what failed and why direction changed.
10. **Credit negative results explicitly.** Count well-documented null results, failed replications and deposited negative data as outputs. Fund venues and repositories that make them citable.
11. **Fund and credit teams.** Allow shared leadership and named contributor roles on awards. Recognise research software engineers, technicians and core staff as contributors in their own right.
12. **Experiment on yourselves.** Publish anonymised evaluation data, and run randomised trials of your own processes.

<details class="aside" markdown="1">
<summary markdown="span">Complete resource accounting, in detail</summary>

The full picture includes external grants, charity and industry funding, core and start-up funding, people funded from elsewhere, and use of shared facilities. Resources should be counted in standardised terms, person-time at a standard rate and facility use at standard internal rates, so that unpaid or cheaply paid labour never looks free.

Attribution should be made at the level of the group or unit, with credit then shared within it by contributor roles. Each researcher should be able to see and contest their own attribution. Funders should reconcile the figures against their own awards, and evaluators should see only normalised outputs, compared within fields, never raw amounts. Normalised figures are for comparing people within a field, never for deciding which fields deserve funding.

</details>

A first step any funder could take now is to pilot an ORCID-based first stage in one scheme, randomised against the current process, and publish the results.

## How this system can be gamed

Any evaluation that matters will be gamed. The question is whether gaming is costlier than doing the real thing. Fabricated artefacts earn little when credit comes mainly from reuse by others, so the pressure moves onto reuse, resources and roles.

The general defences: combine many weak signals rather than a few strong ones, weight by independence, prefer curated over self-deposited records, cap counts, rotate checks, and audit every stage, including the evaluators. The boxes below take the main routes one by one.

<details class="aside" markdown="1">
<summary markdown="span">Citation cartels and inflated reuse</summary>

Groups may cite or depend on each other reciprocally, inflate downloads with bots, or split one tool into many interdependent packages. Defences:

- Credit the **breadth** of reuse, meaning the number of distinct independent groups, not raw counts, and cap credit per citing group. A cartel then has to be large to matter, and large cartels are costly and conspicuous.
- Judge independence **at the time of reuse**, not over a whole career, so collaborating widely is never penalised.
- **Detect anomalies.** Reciprocal citation and citation stacking between small clusters are detectable; indexers already suppress journals for them.
- Prefer **costly reuse**, such as dependencies in established packages or reanalyses with their own data deposits, over passing citations. Ignore downloads and stars entirely.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Riding on consortia</summary>

A paper with a thousand authors is reused by thousands of groups, and breadth would flow to every author. Defence: allocate credit by contributor role, not by authorship.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Inflating roles</summary>

CRediT roles are self-reported, and anyone can list themselves as maintainer of their own package. Defence: treat roles as claims; count maintainer roles only on tools others depend on, consistent with real review and release activity.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Hiding resources</summary>

Researchers could look efficient by using separately funded students, unpaid labour or shared facilities without attribution, and institutions could shuffle attribution between people. Defence: complete accounting reconciled to audited totals, so resources cannot disappear; standardised costing of person-time and facility use, so cheap labour is not free; attribution at group level; and each researcher's right to see and contest their own figures, which turns strategic attribution into a visible, zero-sum game. Resources that cross institutions remain the hardest to track.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Relabelling failure</summary>

Experiments that failed through poor technique can be deposited as "null results" to earn credit. Defence: credit negative results only with evidence that the method worked, such as positive controls.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Flooding</summary>

Low-effort preprints, or applications to every scheme that uses a lottery. Defence: documentation-quality bars, caps on what counts per year, limits on applications per scheme, and effortful application prompts. Resource normalisation also removes the payoff from accumulating grants.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Optimising to the threshold</summary>

Once applicants infer the floor, they aim just above it. Coordinated subject access requests or contest requests can also help reverse-engineer private weights. Defence: rotate checks, audit a random sample below the threshold, and give explanations at the level of criteria rather than weights.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Gaming the human stages</summary>

AI-coached answers, leaked tasks, rehearsed interviews and, in remote settings, proxy candidates. Defence: live unscripted follow-ups, rotated tasks, and at least one identity-verified or in-person stage before an offer.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Weaponising the system against others</summary>

Hostile post-publication comments or integrity reports filed against rivals. Defence: flags never filter automatically, every flag gets human review, and candidates have a right of reply.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Evaluators gaming it</summary>

A committee can override or rerun a draw to remove someone and blame chance. Defence: pre-register the procedure, log random seeds, and publish audits comparing outcomes with draws.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Misusing efficiency scores</summary>

Funders could use resource-normalised output to argue that expensive fields deserve less money. Defence: state explicitly that normalisation compares people within fields and must not drive allocation between them.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Goodhart at the scale of the community</summary>

Researchers may drift toward producing countable, shareable artefacts over hard, slow questions. There is no complete defence. Verifiable evidence should set a floor, never become the target, and evaluators should say so openly.

</details>

## Legal implications

Automating parts of evaluation, and drawing lots, changes the legal footing of hiring and funding decisions. What follows is an overview, not legal advice. The details depend on jurisdiction, and anyone implementing these ideas should involve their data-protection officer and HR or legal teams early.

In short: keep meaningful human involvement in every rejection, keep machines to verification, assess the equality impact before rollout, and document any lottery in advance.

<details class="aside" markdown="1">
<summary markdown="span">Automated decisions</summary>

The UK has no AI-specific statute; AI in hiring is governed by data-protection and equality law. Since February 2026, the [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18) permits solely automated significant decisions based on ordinary personal data, but only with safeguards: applicants must be told in advance, can obtain human review, and can contest the outcome. Decisions involving special-category data, such as health or ethnicity, remain more tightly restricted.

Under the EU GDPR, Article 22 still largely prohibits solely automated significant decisions unless an exception applies. A score-weighted draw is clearly a decision based on evaluating personal data; a purely random draw among equally qualified candidates arguably is not, but the threshold that decides who enters it is.

In both regimes, meaningful human involvement in every rejection is the simplest compliant design, and it is what this proposal recommends anyway. Applicants are also entitled to meaningful information about how decisions are made, which limits how far weights can be kept private.

</details>

<details class="aside" markdown="1">
<summary markdown="span">AI in recruitment</summary>

The [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) does not ban AI in hiring, but classes systems that filter or evaluate job applicants as high-risk. Deployers must ensure trained human oversight, keep logs, inform applicants and workers' representatives, and explain decisions on request. Those obligations apply from December 2027, after the 2026 Digital Omnibus postponed them. Emotion recognition in the workplace is banned outright.

Systems that follow rules set solely by humans fall outside the Act's definition of AI. Fitted statistical models, such as a Bayesian ranking, are a grey zone, and using language models to score or rank applicants is squarely inside. That is one more reason to keep machines to verification.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Equality and indirect discrimination</summary>

Requirements that look neutral can disadvantage protected groups. Under the UK [Equality Act 2010](https://www.legislation.gov.uk/ukpga/2010/15), these include an ORCID record, public artefacts and reuse metrics, which may disadvantage people with career breaks for pregnancy, caring or disability. Such requirements must be a proportionate means to a legitimate aim. That calls for an equality impact assessment before rollout, normalising records for documented breaks, alternative routes for evidence that cannot be public, and reasonable adjustments. Public funders in the UK also carry the Public Sector Equality Duty.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Processing data about researchers</summary>

Data pulled from ORCID, OpenAlex or repositories is still personal data, and per-researcher and per-group resource records, including costed person-time, are more sensitive still. Evaluators and institutions need a lawful basis, typically legitimate interests, plus privacy notices, data minimisation, access controls and defined retention. Systematic evaluation of this kind will usually require a data-protection impact assessment.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Integrity flags</summary>

Post-publication comments and image-screening hits are allegations, not findings. They must never trigger automatic rejection. Each needs human review, and the person concerned needs a chance to respond.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Lotteries</summary>

Random selection among equally qualified candidates is lawful in principle and already used by several funders. It must be applied only above a defensible threshold and documented in advance. It must also be auditable, and institutional HR policy may need updating before it is used for employment.

</details>

## Limits

<details class="aside" markdown="1">
<summary markdown="span">Verifiable evidence may favour conformists</summary>

Reuse rewards conventional, conscientious productivity; risky and unfashionable work is reused less. This cuts against the independence the system is meant to value, and only stratification, randomisation and human judgement counteract it.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Early-career researchers have little reuse yet</summary>

Reuse takes years to accumulate. Early-career researchers need credit for well-documented availability and quality, statistical shrinkage toward a career-stage prior rather than penalties for sparse records, and wider randomisation bands (principle 9).

</details>

<details class="aside" markdown="1">
<summary markdown="span">Reuse favours big fields</summary>

Larger fields generate more reuse, which pushes people toward crowded areas. Field-normalised measures such as the [Relative Citation Ratio](https://doi.org/10.1371/journal.pbio.1002541) help, but are unstable for recent, rarely cited and interdisciplinary work ([Janssens et al. 2017](https://doi.org/10.1371/journal.pbio.2002536)), and cannot normalise work that founds a new field. Evaluators should combine field normalisation with shrinkage, stratify selection across field sizes, and rely on human judgement at the frontier.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Reuse has its own Matthew effect</summary>

Well-known groups' data and tools get reused partly because they are well known. Weighting by independence and breadth softens this, but does not remove it.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Resource normalisation has its own failure modes</summary>

- Costs differ hugely between fields and methods, so comparisons must be within fields.
- Expensive but valuable work, such as building shared instruments or large datasets, can look inefficient, which argues for crediting shared infrastructure separately.
- Output may also grow less than proportionally with resources, which would penalise ambitious large projects unless the normalisation is flattened.
- Resources shared across institutions, such as a collaborator's instrument elsewhere, need a cross-institution ledger that does not yet exist.
- Complete accounting is real administrative work, easier for large institutions than small ones.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Field norms differ</summary>

Some fields deposit everything, others rarely do. Comparisons should be within fields, not across them.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Some contributions remain invisible to machines</summary>

This is especially true at the bench. Better identifiers help, but skill still has to be seen in person.

</details>

<details class="aside" markdown="1">
<summary markdown="span">The virtues are hard to measure, and human judgements of them are biased</summary>

We argue they matter most, not that any process measures them reliably. Structured, behaviourally anchored human judgement remains essential at the end.

</details>

<details class="aside" markdown="1">
<summary markdown="span">Randomisation will occasionally drop a strong candidate</summary>

So does every current process; randomisation is just honest about it.

</details>

## Conclusion

AI does not make scientists less important. It makes the right ones harder to recognise with the tools we have. The answer is not more surveillance of text or cleverer metrics on old outputs. It is evaluation built on evidence that is costly to fake, credited through independent reuse, normalised for the resources people actually had, and completed by structured human judgement where evidence runs out, which is where the most important virtues live. Science has asked for open data, negative results and team credit for decades. Changing how we hire and fund is how we finally pay for them.

<details class="aside" markdown="1">
<summary markdown="span">References and data sources</summary>

**Evaluation, selection and funding**

- [San Francisco Declaration on Research Assessment (DORA)](https://sfdora.org/read/)
- [Sackett et al. 2022, *J. Appl. Psychol.*](https://doi.org/10.1037/apl0000994): validity of selection methods.
- [Heyard et al. 2022, *Statistics and Public Policy*](https://doi.org/10.1080/2330443X.2022.2086190): Bayesian ranking and lottery at the SNSF.
- [Bol, de Vaan & van de Rijt 2018, *PNAS*](https://doi.org/10.1073/pnas.1719557115): the Matthew effect in science funding.
- [Azoulay, Graff Zivin & Manso 2011, *RAND J. Econ.*](https://doi.org/10.1111/j.1756-2171.2011.00140.x): incentives and creativity, HHMI vs NIH.
- [Fang & Casadevall 2016, *mBio*](https://doi.org/10.1128/mBio.00422-16): the case for a modified funding lottery.
- [Kerzendorf et al. 2020, *Nature Astronomy*](https://doi.org/10.1038/s41550-020-1038-y): distributed peer review.
- [Hutchins et al. 2016, *PLoS Biology*](https://doi.org/10.1371/journal.pbio.1002541): the Relative Citation Ratio.
- [Janssens et al. 2017, *PLoS Biology*](https://doi.org/10.1371/journal.pbio.2002536): a critique of the RCR algorithm.
- [Canada's tri-agency narrative CV transition](https://casrai.org/guides/tri-agency-narrative-cv-2027-transition)
- [Messeri & Crockett 2024, *Nature*](https://doi.org/10.1038/s41586-024-07146-0): AI and illusions of understanding.
- [Wilkinson et al. 2016, *Scientific Data*](https://doi.org/10.1038/sdata.2016.18): the FAIR Guiding Principles.
- [CRediT – Contributor Roles Taxonomy](https://credit.niso.org)

**Law and regulation**

- [Data (Use and Access) Act 2025 (UK)](https://www.legislation.gov.uk/ukpga/2025/18)
- [Equality Act 2010 (UK)](https://www.legislation.gov.uk/ukpga/2010/15)
- [Regulation (EU) 2024/1689, the AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**Philosophy and sociology of science**

- [Zagzebski 1996, *Virtues of the Mind*](https://doi.org/10.1017/CBO9781139174763)
- Roberts & Wood 2007, *Intellectual Virtues*, Oxford University Press.
- Longino 1990, *Science as Social Knowledge*, Princeton University Press.
- Douglas 2009, *Science, Policy, and the Value-Free Ideal*, University of Pittsburgh Press.
- Merton 1942, "A note on science and democracy", *Journal of Legal and Political Sociology*; reprinted as "The normative structure of science" in *The Sociology of Science* (1973), University of Chicago Press.

**Data sources**

[ORCID](https://info.orcid.org/documentation/) · [Crossref](https://www.crossref.org) · [DataCite](https://datacite.org) · [Make Data Count](https://makedatacount.org) · [OpenAlex](https://openalex.org) · [Software Heritage](https://www.softwareheritage.org) · [Retraction Watch](https://retractionwatch.com) · [PubPeer](https://pubpeer.com) · [Cellosaurus](https://www.cellosaurus.org) · [ICLAC](https://iclac.org) · [Addgene](https://www.addgene.org) · [protocols.io](https://www.protocols.io)

</details>
