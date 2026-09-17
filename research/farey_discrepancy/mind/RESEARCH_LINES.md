# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Bridge exact permanent-source rigidity to restricted space-time observation and destination coupling

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-026-consecutive-midpoint-horizons-are-a-dirichlet-invertible-temporal-sensor`.

FD-145--FD-163 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure and show that bounded-resource anchor geometry cannot make the exposed squarefree mass disappear merely by sparse holes, terminal-core migration or one omitted small prime. Under the stated expansion/distortion/leakage hypotheses a positive-density source surface remains visible.

FD-164 then separates visibility from orientation. At one horizon the complete Farey discrepancy field is exactly equivalent to the floor-quotient Mertens staircase, yet finitely many macroscopic quotient-shell sign flips can preserve that entire field while changing a dense fraction of squarefree orientations. FD-165 extends the finite-cutoff ambiguity to arbitrary horizon bundles of size `J_T` whenever `J_T M_beta(T)=o(T)`.

FD-166 closes the exact **permanent-source** version. Every quotient set `Q_H` contains the consecutive prefix `1,...,floor(sqrt(H))`. If one fixed source matches complete fields on any unbounded horizon set, those prefixes exhaust the source and force `a=mu` identically. A first source defect at `n_0` is exposed by every `H>=n_0^2`.

FD-167 gives the corresponding complete-field conditioning theorem in unnormalized `L^2`, and FD-168 solves the raw Fourier-coordinate partial-observation problem. For a target prefix `r<=R`, the union of the nonzero Möbius inverse-row supports is the coordinate-minimal raw sampler over the full formal source space and retains the same localized inverse modulus. FD-169 closes unrestricted mixed-linear acquisition: target-aware arbitrary mixing reduces the minimum count to target rank by moving the inverse into the sensor.

FD-170 adds a different observation axis. Fix only the Farey discrepancy at the midpoint but observe it over consecutive horizons. If `P_a(H)=D_{H,a}(1/2)` and `g_a(H)=P_a(H)-P_a(H-1)`, then

`g_a(H)=-(1/2)(u*a)(H)`,

where `u` is the odd-indicator and `u^{-1}(n)=mu(n)` on odd integers and zero on even integers. Hence

`a(n)=-2 sum_(d|n, d odd) mu(d) g_a(n/d)`.

One fixed spatial sensor across all consecutive horizons therefore recovers the whole source prefix exactly. Uniform midpoint-path error `epsilon` propagates only by the divisor factor `4 epsilon 2^(omega(n_odd))=epsilon n^(o(1))`. The physical Möbius midpoint value itself becomes stationary, so the information is carried by the **horizon increments**, not by spatial richness at any one horizon.

FD-171 closes the exact sparse/nonconsecutive version over the unrestricted normalized source space. In the invertible coordinate `b=u*(a-mu)`, a midpoint observation at `H` is just a cumulative prefix sum of `b`. If any horizon `k>=2` is omitted, `b=e_k-e_(k+1)` and `a-mu=mu_odd*b` give a fixed integer-valued permanent perturbation that matches the Möbius midpoint at every `H!=k`. Thus midpoint-only temporal sensing is injective iff every horizon is observed. On a finite prefix `2,...,K`, any selected horizon set `S` has exact rank `|S|` and kernel dimension `K-1-|S|`.

FD-172 shows that this zero-redundancy theorem is not stable under genuinely arithmetic source restrictions. For multiplicative squarefree-supported sources with prime amplitudes `-1<=a(p)<=1`, the same midpoint transform `F=u*a` has nonnegative odd coefficients `F(m)=prod_(p|m)(1+a(p))`. The midpoint error satisfies

`-2 E_H = (A(H)-A(H/2)) + (1+a(2))A(H/2)`,

with `A` the odd `F`-prefix, so every term is nonnegative. Any odd prime defect `1+a(p)>0` is therefore exposed by the first dyadic annulus `(2^(m-1),2^m]` containing `p`. Exact agreement with Möbius at `H=2,4,8,...` forces `a=mu`; agreement through `2^M` forces the whole source prefix through `2^M`. Moreover dyadic error at most `epsilon` forces `0<=1+a(p)<=2epsilon` for every prime. This is Möbius **target-rigidity**, not pairwise injectivity between arbitrary admissible sources.

The live observation problem has consequently split cleanly. Over unrestricted formal sources, sparse midpoint sensing has an exact kernel and no temporal redundancy. Over a strong squarefree-multiplicative Möbius-scale class, exponentially sparse dyadic horizons already certify the Möbius target because source structure converts signed pulse freedom into positive annular mass. The next question is how much of that architecture is truly needed: remove multiplicativity while retaining squarefree/ternary coefficients, characterize horizon sets by multiplicative-gap coverage, or ask for genuine pairwise injectivity rather than one-target rigidity. Mixed sparse-time/local-space sensing remains the parallel route. Separately, coefficient coercivity still needs a destination coupling to the nonlocal Franel--Landau norm.

## Apply the information-budget gate only after the observation-family kernel and normalization are fixed

FD-144 remains a later lower bound: even after geometric exposure and orientation are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can be fooled along a subsequence. FD-168--FD-172 sharpen the order of obligations. First declare the observation family, including whether changing horizon counts as a new measurement, identify its kernel relative to both the target and the admissible source class, and fix the norm/noise normalization; only then count measurements or price inverse stability.

For raw Fourier selectors, FD-168 gives a nontrivial coordinate-minimal support because the basis is fixed. For unrestricted linear acquisition, FD-169 shows that the target row space itself is the minimal measurement space, so count alone is tautological. For midpoint temporal acquisition, FD-170 shows that one spatial coordinate is not one scalar degree of information when the operator changes with every horizon, while FD-171 shows that every horizon row is essential over the unrestricted formal source class. FD-172 then gives the complementary warning: nonlinear source restrictions can collapse that apparent row-count requirement for a fixed target, because positivity can make `O(log X)` dyadic tests certify the entire Möbius prefix through `X`. Any information-budget claim must therefore specify whether it concerns unrestricted recovery, target testing, or recovery within a restricted arithmetic model.

## Keep coefficient coercivity and destination coercivity separate

Exact or uniformly subcritical complete-field errors on an unbounded hierarchy identify an integer-valued permanent source. FD-168 preserves coefficient coercivity under a sharply reduced raw Fourier skeleton, and FD-170 gives a stable triangular temporal inverse from consecutive midpoint horizons. FD-171 proves that this temporal inverse has an exact nullspace as soon as any horizon is removed over unrestricted sources; FD-172 shows that squarefree multiplicativity plus primewise positivity can nevertheless restore sparse **target** coercivity at dyadic horizons. None proves the RH-critical discrepancy estimate. A useful continuation must determine how far the FD-172 restrictions can be weakened, develop mixed observation coercivity under a precisely declared source class, or connect source-native structure directly to the nonlocal Franel--Landau norm.
