# PC-076 — the first Hardy/Hilbert relative trace is parity-twisted von Mangoldt

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The Prime-Circle specialization and the exact trace reduction are derived here. The cyclotomic endpoint values are classical, and the general phenomenon that trace-class Hankel traces reduce to boundary/symbol endpoint data has established operator-theoretic prior art. No theorem-level novelty is claimed.

PC-075 shows that the canonical Hardy interior/exterior coupling of the cyclotomic logarithmic potential has a universal Hilbert-matrix absolutely-continuous core plus a trace-class arithmetic remainder. It explicitly leaves relative trace-class invariants open. The simplest such invariant can now be evaluated exactly, and it collapses all the way back to the scalar common-anchor data of PC-001 together with its antipodal analogue.

For every `n>1`, let

\[
W\Gamma_nW^*=-\frac1n C_n\otimes H+T_n,
\qquad T_n\in\mathcal S_1,
\]

be the exact PC-075 decomposition, where

\[
(C_n)_{rs}=c_n(r+s+1),
\qquad
(H_\alpha)_{ab}=\frac1{a+b+\alpha},
\]

and the `(r,s)` block of the remainder is

\[
(T_n)_{rs}
=-\frac{c_n(r+s+1)}{n}\left(H_{(r+s+1)/n}-H_1\right).
\]

Then

\[
\boxed{
\operatorname{Tr}T_n
=\frac12\Bigl(\Lambda(n)-\mathbf 1_{2\mid n}\Lambda(n/2)\Bigr),
\qquad n>1,
}
\]

with the convention `Lambda(1)=0`. Equivalently, for `n>2`,

\[
\boxed{
\operatorname{Tr}T_n
=\frac12\log\frac{\Phi_n(1)}{\Phi_n(-1)}.
}
\]

The exceptional level `n=2` has `Phi_2(-1)=0`, so the endpoint-ratio display is not meaningful there, but direct evaluation gives

\[
\operatorname{Tr}T_2=\frac12\log2,
\]

which is exactly the same von-Mangoldt formula above.

Thus the **first relative spectral trace of the genuinely nonlocal Hardy/Hankel lift contains no arithmetic beyond two scalar shell potentials at the antipodal anchors `+1` and `-1`**.

## 1. Trace of one generalized-Hilbert difference

Only the diagonal residue blocks contribute to the trace. For `alpha>0`, PC-075 already proves `H_alpha-H_1` is trace class. Its trace has the elementary moment representation

\[
\begin{aligned}
\operatorname{Tr}(H_\alpha-H_1)
&=\sum_{a\ge0}\left(\frac1{2a+\alpha}-\frac1{2a+1}\right)\\
&=\int_0^1\frac{x^{\alpha-1}-1}{1-x^2}\,dx.
\end{aligned}
\]

Therefore

\[
\operatorname{Tr}T_n
=-\frac1n\sum_{r=0}^{n-1}c_n(2r+1)
\int_0^1
\frac{x^{(2r+1)/n-1}-1}{1-x^2}\,dx.
\]

For `n>2`, the constant part disappears because

\[
\sum_{r=0}^{n-1}c_n(2r+1)=0.
\]

Indeed, writing `zeta=exp(2 pi i/n)`,

\[
\sum_{r=0}^{n-1}c_n(2r+1)
=\sum_{u\in U(n)}\zeta^u
\sum_{r=0}^{n-1}(\zeta^{2u})^r=0,
\]

since a unit `u` cannot satisfy `zeta^(2u)=1` when `n>2`.

## 2. The full residue sum telescopes to the two antipodal anchors

Substitute `x=y^n`. The remaining numerator is

\[
\sum_{r=0}^{n-1}c_n(2r+1)y^{2r}.
\]

Expanding the Ramanujan sum first gives the exact finite geometric identity

\[
\begin{aligned}
\sum_{r=0}^{n-1}c_n(2r+1)y^{2r}
&=\sum_{u\in U(n)}\zeta^u
\sum_{r=0}^{n-1}(\zeta^{2u}y^2)^r\\
&=(1-y^{2n})
\sum_{u\in U(n)}\frac{\zeta^u}{1-\zeta^{2u}y^2}.
\end{aligned}
\]

Hence

\[
\operatorname{Tr}T_n
=-\sum_{u\in U(n)}
\int_0^1\frac{\zeta^u}{1-\zeta^{2u}y^2}\,dy.
\]

Pair `u` with `-u`. This removes any logarithm-branch ambiguity and yields a real logarithm. Equivalently, taking the product over the full primitive shell gives

\[
\operatorname{Tr}T_n
=-\frac12\sum_{u\in U(n)}
\log\frac{1+\zeta^u}{1-\zeta^u}
=\frac12\log\frac{\prod_u(1-\zeta^u)}{\prod_u(1+\zeta^u)}.
\]

For `n>2`, `phi(n)` is even, so the defining cyclotomic products give

\[
\prod_{u\in U(n)}(1-\zeta^u)=\Phi_n(1),
\qquad
\prod_{u\in U(n)}(1+\zeta^u)=\Phi_n(-1).
\]

This proves

\[
\boxed{
\operatorname{Tr}T_n=\frac12\log\frac{\Phi_n(1)}{\Phi_n(-1)}.
}
\]

The apparently infinite-dimensional relative trace has therefore collapsed to two evaluations of the original finite cyclotomic shell polynomial.

## 3. Cyclotomic endpoint values give the parity-twisted von Mangoldt law

The `+1` endpoint is PC-001:

\[
\log\Phi_n(1)=\Lambda(n),
\qquad n>1.
\]

The classical `-1` endpoint classification gives, for `n>2`,

\[
\log\Phi_n(-1)
=
\begin{cases}
0,&n\text{ odd},\\
\Lambda(n/2),&n\text{ even}.
\end{cases}
\]

Consequently

\[
\boxed{
\operatorname{Tr}T_n
=\frac12\left(\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2)\right).
}
\]

The support is especially restrictive:

- an odd prime power `p^k` contributes `+(1/2) log p`;
- twice an odd prime power contributes `-(1/2) log p`;
- powers `2^k` with `k>=2` cancel exactly;
- all other composite levels contribute zero;
- `n=2` contributes `+(1/2) log 2`.

Thus even the sign pattern is just the elementary competition between the common anchor and its antipode.

As a further control, for `Re(s)>1`,

\[
\begin{aligned}
\sum_{n\ge2}\frac{\operatorname{Tr}T_n}{n^s}
&=\frac12(1-2^{-s})
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}\\
&=\boxed{-\frac12(1-2^{-s})\frac{\zeta'(s)}{\zeta(s)}}.
\end{aligned}
\]

So Dirichlet-aggregating this relative trace does not create a new zeta object either: it is the classical logarithmic derivative with the elementary Euler factor at `2` removed.

## 4. Prior-art and novelty audit

The exact Prime-Circle identity above was checked against two separate classical boundaries.

1. The endpoint evaluations `Phi_n(1)` and `Phi_n(-1)` are standard cyclotomic arithmetic. In particular, `Phi_n(1)=exp(Lambda(n))` is already the classical identity persisted as PC-001; the `-1` value follows from the equally standard parity identities for cyclotomic polynomials. Therefore the final arithmetic expression is not new arithmetic data.
2. Aurelian Gheondea and Raimund J. Ober, **A trace formula for Hankel operators**, *Proceedings of the American Mathematical Society* 127:7 (1999), 2007–2012, DOI `10.1090/S0002-9939-99-04669-9`, prove in a general trace-class Hankel setting that the operator trace is one half of a symbol endpoint difference. Their theorem is not being invoked as a black-box proof of the residue-block calculation above, but it is strong neighboring prior art for precisely the phenomenon encountered here: the first trace of a trace-class Hankel correction naturally collapses to endpoint data.

Directed searches for Ramanujan-sum Hankel traces, cyclotomic Hankel operators, and the exact coefficient pattern `c_n(j+k+1)/(j+k+1)` found the established surrounding Hankel and Ramanujan-matrix theories already recorded for PC-075, but not an authoritative source stating this exact Prime-Circle specialization. Absence of that wording is not treated as evidence of novelty.

The durable contribution is therefore an **internal classification/obstruction**: the first trace of the PC-075 arithmetic remainder cannot serve as the missing RH-sensitive invariant because it is exactly the old scalar cyclotomic source strength, with only an antipodal parity correction.

## 5. Why this closes the simplest relative-spectrum escape from PC-075

PC-075 deliberately did not infer that its trace-class remainder `T_n` was spectrally trivial. The present result closes only the first and most canonical relative invariant:

\[
\text{cyclotomic log field}
\to
\text{Hardy/Hankel operator}
\to
\text{universal Hilbert core}+T_n
\to
\operatorname{Tr}T_n
\to
\frac12(U_n(1)-U_n(-1)).
\]

The last quantity is scalar endpoint data. It has no intrinsic complex spectral parameter, no gamma factor, no `s <-> 1-s` symmetry, and no critical-line selector. Applying a Dirichlet transform merely recovers `-zeta'/zeta` with a trivial local factor.

This is a stronger negative statement than saying that the essential spectrum of `Gamma_n` is universal: **even the first trace-class correction, after the universal Hilbert channels are removed, still does not retain the multidimensional information that PC-001 warned scalar evaluation loses.**

## 6. Boundary of the obstruction

This finding does **not** show that the complete trace-class remainder is determined by its trace. In particular, the following remain outside the claim:

- higher Schatten moments such as `Tr(T_n^k)` for `k>=2`;
- Fredholm or perturbation determinants built from `T_n`;
- isolated eigenvalues or threshold resonances of `Gamma_n` relative to the Hilbert core;
- cross-level Hardy operators coupling different shells before residue decomposition;
- shell-dependent or refinement-forced weights;
- nonlinear operations on the Hardy/Hankel blocks;
- the old/new cotangent coupling of PC-047 and the global uniformization/monodromy branch of PC-017.

A viable continuation of the PC-075 branch must therefore show that **nonlinear or higher relative data do not themselves collapse to the same endpoint/divisor package**. The scalar first spectral shift is exhausted.

## 7. Falsification surface

The result has five direct failure points.

1. The PC-075 block formula for `T_n` must be used with exactly the stated normalization.
2. `Tr(H_alpha-H_1)` must equal the convergent diagonal sum and the moment integral above.
3. For `n>2`, the odd-index Ramanujan sum over a full residue system must vanish.
4. The finite geometric series must reduce the residue sum to the primitive-root logarithmic product without a missing branch/sign factor.
5. The standard values of `Phi_n(1)` and `Phi_n(-1)` must give the displayed parity-twisted von Mangoldt law.

Independent numerical evaluation of the convergent diagonal trace for `2<=n<=50` agrees with the closed formula, including the controls `n=6 -> -(1/2)log 3`, `n=9 -> +(1/2)log 3`, `n=12 -> 0`, and `n=18 -> -(1/2)log 3`. These checks are controls only; the claim rests on the exact derivation above.

## Research consequence

The first relative trace of the canonical nonlocal Hardy/Hankel remainder is not a new Prime-Circle bridge to RH:

\[
\boxed{
\operatorname{Tr}T_n
=\frac12\bigl(\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2)\bigr).
}
\]

The nonlocal operator survives PC-037 at the operator level, but its simplest trace-class spectral statistic falls back to the same classical cyclotomic endpoint information already present at the common vertex. Further work on this branch is justified only for genuinely higher/relative spectral data, not for the first trace or its Dirichlet transform.