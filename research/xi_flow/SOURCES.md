# Xi-flow source anchors

This file records durable literature dependencies for `research/xi_flow/`. It is an anchor list, not a search history.

## De Bruijn–Newman deformation

- [`research/prior_art/de-bruijn-newman-deformation.md`](../prior_art/de-bruijn-newman-deformation.md). Role: Mathia prior-art anchor for the heat-flow formulation, the threshold `Lambda`, the equivalence `RH <=> Lambda <= 0`, and the Rodgers–Tao lower bound.
- Brad Rodgers and Terence Tao, **The de Bruijn–Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6. Role: primary anchor for `Lambda >= 0`, the zero-dynamics contradiction mechanism, and its use of local zero statistics.
- Charles M. Newman and Wei Wu, **Constants of de Bruijn–Newman type in analytic number theory and statistical physics**, *Bulletin of the American Mathematical Society* 57:4 (2020), 595–614. Role: authoritative historical/structural survey of the de Bruijn and Newman deformation framework and neighboring de Bruijn–Newman constants.

## Zero dynamics and Lehmer pairs

- George Csordas, Wayne Smith and Richard S. Varga, **Lehmer Pairs of Zeros, the de Bruijn–Newman Constant Lambda, and the Riemann Hypothesis**, *Constructive Approximation* 10 (1994), 107–129, DOI `10.1007/BF01205170`. Role: primary anchor for the classical real-zero dynamics/Lehmer-pair mechanism, the exact `Delta^2 G < 4/5` Lehmer criterion used in XF-005, and the associated lower bounds on `Lambda`.
- Jeffrey Stopple, **Lehmer Pairs Revisited**, *Experimental Mathematics* 26:1 (2017), 130–138; arXiv:1508.05870. Role: accessible restatement of the Csordas–Smith–Varga criterion and its reformulation through pre-Schwarzian data and nearby zeros of `zeta'`; used only for prior-art calibration in XF-005.

## Upper-bound and high-zero asymptotic machinery

- D. H. J. Polymath, **Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn–Newman constant**, *Research in the Mathematical Sciences* 6 (2019), article 31; arXiv:1904.12438. Role: primary anchor for effective `H_t` asymptotics, the fixed-`t` zero-counting law used in XF-004, and the published `Lambda <= 0.22` upper-bound framework.
- Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to `3·10^12`**, *Bulletin of the London Mathematical Society* 53:3 (2021), 792–797, DOI `10.1112/blms.12460`. Role: rigorous interval-arithmetic verification that all zeta zeros through height `3·10^12` are simple and on the critical line; combined with the Polymath15 criterion this supplies the established `Lambda <= 0.2` benchmark referenced in XF-004.
- `teorth/optimizationproblems`, constant 21 and PR `#126`, **Improve upper bound for the de Bruijn–Newman constant to 0.1875 (certified record package)**, merged 17 July 2026; associated bundle DOI `10.5281/zenodo.21175533`. Role: current crowdsourced/certificate-backed candidate `Lambda <= 3/16`. The optimization repository marks this value with an asterisk for minimal external verification, so Mathia treats it as a current audit/benchmark signal rather than established peer-reviewed evidence.

## Laguerre–Pólya approximation and polynomial heat-flow controls

- Alexandru Aleman, Dmitry Beliaev and Håkan Hedenmalm, **Real zero polynomials and Pólya–Schur type theorems**, *Journal d'Analyse Mathématique* 94 (2004), 49–60, DOI `10.1007/BF02789041`. Role: primary real-zero-preserver anchor for the Pólya–Benz/Pólya–Schur machinery underlying the matched polynomial backward-heat controls in XF-006.
- Theodoros Assiotis, **Random Entire Functions from Random Polynomials with Real Zeros**, *Advances in Mathematics* 410 Part A (2022), article 108701, DOI `10.1016/j.aim.2022.108701`. Role: modern peer-reviewed Laguerre–Pólya convergence framework and explicit anchor for the locally uniform closure of real-rooted polynomials used in XF-006.
- Brian C. Hall and Ching-Wei Ho, **The heat flow conjecture for polynomials and random matrices**, *Letters in Mathematical Physics* 115 (2025), article 60, DOI `10.1007/s11005-025-01946-9`. Role: explicit contemporary statement that backward polynomial heat flow preserves the class of all-real-rooted polynomials by the Pólya–Benz theorem; direct prior-art boundary for XF-006.
- Zakhar Kabluchko, **Lee–Yang zeroes of the Curie–Weiss ferromagnet, unitary Hermite polynomials, and the backward heat flow**, *Annales Henri Lebesgue* 8 (2025), 1–34, DOI `10.5802/ahl.227`. Role: modern finite/high-degree real-rooted polynomial backward-heat context; supports the matched-control interpretation in XF-006 without being used as evidence for any Xi-specific claim.

## Zero statistics used by the flow

- [`research/prior_art/montgomery-pair-correlation.md`](../prior_art/montgomery-pair-correlation.md). Role: retained anchor for the zero-statistical input used to falsify overly rigid local-equilibrium behavior, with RH-conditional and conjectural regimes kept distinct.

## Audited contemporary claims

- Kevin Schatz, **Riemann Hypothesis: Backward Parabolic Positivity Barriers for the Xi Flow**, preprint dated 20 November 2025, DOI `10.5281/zenodo.17636625`. Role: source audited in XF-001. The manuscript claims a backward positivity barrier proving `Lambda=0`; XF-001 gives an exact backward-heat double-collision calculation showing that its Lemma C.1 holomorphic root-labelling step is false and that the speed-dependent endpoint Gronwall bridge is not justified as written. This source is retained as an audit target, not as established RH evidence.

## Expansion rule

Add primary sources for zero-motion, Lehmer-pair, collision, or real-entire-function mechanisms only when a canonical finding depends on their exact theorem. A numerical trajectory or secondary exposition is not a source anchor for a mathematical claim.
