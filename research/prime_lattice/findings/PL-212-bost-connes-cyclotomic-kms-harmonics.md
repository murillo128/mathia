# PL-212 — Bost–Connes cyclotomic KMS harmonics split into a zeta-free invariant channel and `L/zeta` broken-symmetry channels

## Claim

The canonical Bost–Connes arithmetic subalgebra provides a source-forced way to leave the independent divisibility diagonal tested in `PL-211`: its cyclotomic generators `e(r)` retain residue-class/Galois phase data that is not a product statistic of the prime valuations. At a prime cyclotomic level, however, the KMS symmetry structure separates this arithmetic information in a way that blocks the most direct RH mechanism.

Fix a rational prime `ell`, let `zeta_ell=exp(2 pi i/ell)`, and write `U=(Z/ell Z)^*`. In the low-temperature Gibbs phase `beta>1`, the extremal Bost–Connes KMS states are indexed by `rho in \hat Z^*` and, on `e(1/ell)`, have the classical value

\[
\phi_{\beta,\rho}(e(1/\ell))
=\frac{\operatorname{Li}_{\beta}(\rho(\zeta_\ell))}{\zeta(\beta)}.
\]

Restricting `rho` modulo `ell` gives the `U`-orbit

\[
F_u(s)=\frac{\operatorname{Li}_s(\zeta_\ell^u)}{\zeta(s)},
\qquad u\in U,
\qquad \Re s>1.
\]

Take its finite Galois Fourier transform

\[
A_\chi(s)
=\frac1{\ell-1}\sum_{u\in U}\overline{\chi(u)}F_u(s)
\]

for Dirichlet characters `chi mod ell`. Absolute convergence in `Re(s)>1` gives the exact decomposition

\[
\boxed{
A_{\mathbf 1}(s)
=\frac{\ell^{1-s}-1}{\ell-1}
}
\]

for the invariant character, while every nontrivial character satisfies

\[
\boxed{
A_\chi(s)
=\frac{\tau(\overline\chi)}{\ell-1}\,
\frac{L(s,\chi)}{\zeta(s)}.
}
\]

The first channel is not merely an average chosen for the calculation. Bost–Connes symmetry restoration makes it the actual high-temperature equilibrium value. For `0<beta<=1` there is a unique KMS state and the standard KMS classification gives

\[
\boxed{
\phi_\beta(e(1/\ell))
=\frac{\ell^{1-\beta}-1}{\ell-1}.
}
\]

It is independent of the numerator of `e(a/ell)` when `a` is a unit modulo `ell`, hence every nontrivial finite Galois Fourier coefficient vanishes exactly in the unique KMS state. The invariant channel passes through the phase transition at `beta=1` as an elementary entire exponential polynomial, with the Riemann zeta factor cancelled identically. The channels that retain `1/zeta(s)` exist as broken-symmetry Fourier components only in the low-temperature KMS family; after meromorphic continuation they are not positive KMS states in the critical strip.

Thus the canonical cyclotomic escape from the Bost–Connes divisibility diagonal has an exact information split:

\[
\text{KMS-invariant equilibrium channel}
\longrightarrow
\text{zeta cancels},
\]

whereas

\[
\text{nontrivial Galois channels}
\longrightarrow
L(s,\chi)/\zeta(s)
\]

retain zero-divisor sensitivity but lose their interpretation as equilibrium-state degrees of freedom once the arithmetic symmetry is restored. This is a **negative/obstruction for the canonical prime-level cyclotomic KMS-harmonic route**, not a no-go theorem for the full Bost–Connes algebra, endomotives, adele-class trace formulas, or other completed arithmetic constructions.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. Why this tests a genuinely source-forced escape from `PL-211`

`PL-211` studied the commuting divisibility projections

\[
E_n=S_nS_n^*
\]

and showed that their canonical Möbius orientation separates a phase-blind `beta=1/2` support threshold from phase coherence at `beta=1`. The matched-control analysis in the Möbius line subsequently sharpened the diagonal obstruction: under every Bost–Connes KMS state, disjoint prime valuation coordinates are independent on the divisibility diagonal, so connected diagonal prime covariances cannot restore the missing Möbius orientation at the half boundary.

The arithmetic generator `e(r)` is different. In the standard representation it records an additive cyclotomic phase depending on the integer residue, and the Bost–Connes symmetry group `\hat Z^*` acts on these roots of unity. This data is part of the original arithmetic algebra; it is not a freely programmed finite-rank label of the sort ruled out by `PL-208`--`PL-210`. Consequently the `e(1/ell)` channel is a canonical test of whether genuine Bost–Connes residue/Galois structure supplies the cross-prime arithmetic rigidity left open by the previous negative results.

The test is deliberately kept at prime conductor. That makes every nontrivial character primitive and keeps the Gauss-sum decomposition exact without imprimitive local correction factors. The obstruction already appears there, so no composite-conductor generalization is needed for the claim.

## 2. Low-temperature KMS values and the finite Galois orbit

Bost and Connes prove that the partition function of the positive-energy representation is `zeta(beta)` and that the system has a phase transition at `beta=1`. In the low-temperature region `beta>1`, the extremal KMS states form a free transitive orbit under `\hat Z^*`. Connes and Marcolli record the arithmetic-subalgebra evaluation in the form

\[
\phi_{\beta,\rho}(e(r))
=\frac{\operatorname{Li}_\beta(\rho(\zeta_r))}{\zeta(\beta)}.
\]

For `r=1/ell`, the reduction of `rho` modulo `ell` lies in `U=(Z/ell Z)^*`, so the distinct cyclotomic values are

\[
F_u(\beta)
=\frac{\operatorname{Li}_\beta(\zeta_\ell^u)}{\zeta(\beta)}.
\]

For the harmonic calculation, replace the real Gibbs parameter by a complex variable `s` but **only initially in `Re(s)>1`**. There both series

\[
\operatorname{Li}_s(\zeta_\ell^u)
=\sum_{n\ge1}\frac{\zeta_\ell^{un}}{n^s},
\qquad
\zeta(s)=\sum_{n\ge1}\frac1{n^s}
\]

are absolutely convergent, so finite Fourier transformation and interchange with the Dirichlet sum are justified without analytic continuation.

## 3. Exact Galois Fourier decomposition

For a nontrivial Dirichlet character `chi mod ell`, define

\[
A_\chi(s)
=\frac1{\ell-1}\sum_{u\in U}
\overline{\chi(u)}
\frac{\operatorname{Li}_s(\zeta_\ell^u)}{\zeta(s)}.
\]

Using the standard Gauss-sum identity

\[
\sum_{u\in U}\overline{\chi(u)}\zeta_\ell^{un}
=\tau(\overline\chi)\chi(n),
\]

where `chi(n)=0` if `ell|n`, absolute convergence gives

\[
\begin{aligned}
A_\chi(s)
&=\frac1{(\ell-1)\zeta(s)}
\sum_{n\ge1}\frac1{n^s}
\sum_{u\in U}\overline{\chi(u)}\zeta_\ell^{un}\\
&=\frac{\tau(\overline\chi)}{\ell-1}
\frac{L(s,\chi)}{\zeta(s)}.
\end{aligned}
\]

For the trivial character, the inner sum is the prime Ramanujan sum

\[
c_\ell(n)=
\sum_{u\in U}\zeta_\ell^{un}
=\begin{cases}
\ell-1,&\ell\mid n,\\
-1,&\ell\nmid n.
\end{cases}
\]

Hence

\[
\sum_{n\ge1}\frac{c_\ell(n)}{n^s}
=(\ell-1)\ell^{-s}\zeta(s)
-\bigl(1-\ell^{-s}\bigr)\zeta(s)
=\bigl(\ell^{1-s}-1\bigr)\zeta(s),
\]

and therefore

\[
A_{\mathbf1}(s)
=\frac{\ell^{1-s}-1}{\ell-1}.
\]

The cancellation of `zeta(s)` in the invariant character is exact before any continuation. Conversely, every nontrivial Galois harmonic carries the quotient `L(s,chi)/zeta(s)`.

The smallest matched control is `ell=2`, where `U` is trivial and there is no nontrivial harmonic at all. The familiar identity

\[
\frac{\operatorname{Li}_s(-1)}{\zeta(s)}
=2^{1-s}-1
\]

shows directly that the only cyclotomic phase available at conductor `2` cancels the zeta divisor completely.

## 4. Symmetry restoration projects the equilibrium state onto the zeta-free channel

The high-temperature KMS theorem gives a unique KMS state for every `0<beta<=1`. Connes--Marcolli record, for `e(a/b)` with `(a,b)=1`,

\[
\phi_\beta(e(a/b))
=b^{-\beta}
\prod_{p\mid b}
\frac{1-p^{\beta-1}}{1-p^{-1}}.
\]

For `b=ell` this reduces to

\[
\phi_\beta(e(a/\ell))
=\frac{\ell^{1-\beta}-1}{\ell-1},
\qquad a\in U.
\]

Thus the unique state is constant across the entire finite Galois orbit. Its finite Fourier transform is consequently

\[
\frac1{\ell-1}\sum_{a\in U}
\overline{\chi(a)}\phi_\beta(e(a/\ell))
=0
\]

for every nontrivial character `chi`, while the trivial component is exactly

\[
\frac{\ell^{1-\beta}-1}{\ell-1}.
\]

This is the same function obtained by averaging the low-temperature extremal formula over the Galois orbit. Therefore the canonical invariant channel crosses the thermodynamic boundary continuously at the level of this observable and is already entire as a function of the complexified parameter. What disappears at `beta=1` is not a scalar singularity in this channel but the symmetry-broken family whose nontrivial Fourier coefficients retained the arithmetic phase distinctions.

This strengthens the diagnosis of `PL-024`. That finding showed that the elementary Bost–Connes log-prime covariance has its intrinsic phase boundary at `beta=1`, not `1/2`. Here the richer cyclotomic algebra is allowed to participate, and the result is more specific: **the part selected by the restored KMS equilibrium symmetry is precisely the part in which the Riemann zeta denominator cancels**.

## 5. Analytic continuation does not turn the broken harmonics into a Hilbert–Pólya mechanism

The identities above are proved in `Re(s)>1`. Once established there, the classical analytic continuations of the polylogarithm/periodic zeta functions, Dirichlet `L`-functions, and Riemann zeta function give meromorphic continuations of the scalar formulas. In particular,

\[
A_\chi(s)
=\frac{\tau(\overline\chi)}{\ell-1}
\frac{L(s,\chi)}{\zeta(s)}
\]

continues meromorphically for nontrivial `chi`.

That continuation must not be confused with the KMS classification. Below `beta=1` the positive equilibrium state is the unique invariant KMS state just computed. A nontrivial character projection of the low-temperature family is a signed/complex linear combination of states, not itself a positive state; after continuation into the critical strip it is merely a meromorphic scalar function. A zero of `zeta` may therefore appear as a pole of `L/zeta` unless cancelled by the numerator, but no self-adjoint spectrum, positivity theorem, trace identity, or KMS principle here forces the location of that pole onto `Re(s)=1/2`.

This distinction prevents a false continuation argument of exactly the kind excluded by the line mandate. The Bost–Connes system does not analytically continue its Gibbs trace or its broken-symmetry extremal state manifold into the critical strip. It supplies a different, unique KMS state there as a real-temperature equilibrium construction.

## 6. Prior art and novelty audit

The system, KMS phase diagram, arithmetic subalgebra, Galois symmetry, and polylogarithmic state formulas are classical. The principal sources are:

- Jean-Benoît Bost and Alain Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” *Selecta Mathematica, New Series* **1** (1995), 411–457, DOI `10.1007/BF01589495`.
- Alain Connes and Matilde Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, AMS Colloquium Publications **55** (2008), especially the Bost–Connes KMS classification around Theorem 3.32 and formulas `(3.133)`--`(3.142)`.

The finite Fourier/Gauss-sum decomposition is an elementary consequence of those classical formulas together with standard Dirichlet-character orthogonality. The periodic-zeta/polylogarithm relation and its analytic continuation are classical as well. A targeted novelty search found the ingredients and many uses of Bost–Connes arithmetic observables, but no reason to treat this particular organization as a new theorem. Accordingly **no novelty claim is made**.

There is also established literature embedding RH-equivalent arithmetic inequalities in Bost–Connes observables, for example Planat, Solé and Omar, “Riemann hypothesis and quantum mechanics,” *Journal of Physics A* **44** (2011), 145203, arXiv `1012.4665`. That is an important boundary on the negative claim: the Bost–Connes algebra can host RH-equivalent statements. The present result says only that the canonical prime-level cyclotomic KMS harmonic decomposition does not itself produce zero localization; its invariant equilibrium channel removes `zeta`, while the zero-sensitive broken channels lose KMS-state status across the phase boundary.

## Boundaries, counterarguments, and falsification tests

The negative is intentionally narrow.

- It treats the canonical arithmetic generators `e(a/ell)` at prime conductor and their finite Galois harmonics. It does not classify arbitrary noncommuting products involving the semigroup isometries, cyclic-homology classes, endomotive realizations, or adelic/scaling trace-formula observables.
- The statement that nontrivial harmonics “disappear” below `beta=1` means that the unique positive KMS state is Galois invariant and has zero nontrivial Fourier coefficient. It does **not** mean that the meromorphic scalar functions `L(s,chi)/zeta(s)` cease to exist.
- The result does not assert that every Riemann zero is a pole of every nontrivial channel; cancellation by `L(s,chi)` is possible.
- Composite conductors introduce imprimitive-character and local-factor bookkeeping. They may enrich the harmonic decomposition but cannot falsify the exact prime-conductor calculation.
- The established adele-class/Weil/trace-formula programs add global structures not present in this KMS-harmonic test and remain outside the negative.

The finding would be materially falsified or narrowed if any of the following occurred:

1. the standard Bost–Connes extremal KMS formula on `e(1/ell)` were not `Li_beta(zeta_ell^u)/zeta(beta)` for `beta>1`;
2. the unique KMS formula for `0<beta<=1` failed to be constant on `e(a/ell)` for units `a`;
3. the finite Gauss/Ramanujan transform above failed, so that the invariant channel did not cancel `zeta` or a nontrivial prime character did not give `L(s,chi)/zeta(s)`;
4. a nontrivial Galois harmonic could be realized as an additional positive KMS state for some `0<beta<=1`, contradicting uniqueness/symmetry restoration;
5. an additional canonical structure, absent from this calculation, converted the meromorphic `L/zeta` divisor into a positive/self-adjoint spectral constraint that forces the Riemann zeros onto `Re(s)=1/2`.

The first four are excluded by the classical KMS theorem and elementary finite harmonic analysis. The fifth is precisely the kind of additional global mechanism the research line would need.

## Consequence for `prime_lattice`

After `PL-211`, it remained plausible that the failure of the divisibility diagonal was merely an artifact of throwing away the Bost–Connes arithmetic phase algebra. `PL-212` tests that escape at its simplest canonical cyclotomic level and finds a sharper obstruction.

The source-forced arithmetic phases are real and nontrivial, but their KMS harmonic decomposition separates them from the equilibrium continuation in the wrong way for RH: symmetry restoration keeps the Galois-invariant component, and that component has already cancelled the Riemann zeta denominator. The nontrivial character channels remember `1/zeta`, but only as broken-symmetry Fourier data whose meromorphic continuation has no positivity or spectral-localization force.

Accordingly a live Bost–Connes/prime-lattice route must now do more than “use the arithmetic subalgebra” or “retain cyclotomic phases.” It must identify a **canonical non-invariant or global coupling that survives the restored phase without averaging away the zeta-sensitive information**, and it must connect that coupling to a positivity, self-adjointness, trace, or explicit-formula constraint that genuinely distinguishes `Re(s)=1/2`. Otherwise the construction either returns to the zeta-free invariant KMS channel isolated here or to the already classical adelic/Weil completion tracked elsewhere in the line.