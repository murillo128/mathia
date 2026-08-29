# PF-012 — zero-twist prime-flute parabolicity is forced by universal telescoping

**Status:** `DECISIVE-NEGATIVE / EXACT-DERIVED + LITERATURE-VERIFIED` for any proposed RH mechanism whose arithmetic content is only the global parabolic/conformal type, Brownian recurrence, geodesic-flow ergodicity, or divergence of the Poincaré series at exponent `1`. Patterson–Sullivan consequences are recorded separately in PF-023.

## Claim

Let

\[
u_n=\cot\frac{\pi}{p_n},
\qquad
h_n=\log\frac{u_n}{u_{n-1}}>0,
\]

for the exact zero-twist prime-flute. PF-001 gives the exact distinguished-cuff identity

\[
\boxed{
e^{-\ell_n/2}=\tanh\frac{h_n}{4}.
}
\tag{1}
\]

Because `u_n` is increasing and `u_n -> infinity`,

\[
\sum_{n=2}^{N} h_n
=
\log\frac{u_N}{u_1}
\longrightarrow\infty.
\tag{2}
\]

For every positive sequence `(h_n)`, divergence of `sum h_n` forces divergence of `sum tanh(h_n/4)`: if infinitely many `h_n>=1`, the terms are bounded below by `tanh(1/4)>0`; otherwise eventually `0<h_n<1`, and concavity of `tanh` on `[0,1/4]` gives

\[
\tanh\frac{h_n}{4}
\ge
h_n\tanh\frac14.
\tag{3}
\]

Therefore

\[
\boxed{
\sum_n e^{-\ell_n/2}=\infty.
}
\tag{4}
\]

Basmajian–Hakobyan–Šarić, Theorem 1.5 / Theorem 9.4 in *The type problem for Riemann surfaces via Fenchel–Nielsen parameters* (Proc. London Math. Soc. 125 (2022), 568–625), proves for a **zero-twist tight flute** that

\[
X\text{ is parabolic}
\iff
X\text{ is complete}
\iff
\sum_n e^{-\ell_n/2}=\infty.
\tag{5}
\]

Hence the exact prime-flute is parabolic and complete.

The important point is that (2)--(4) use **no prime-gap theorem, no PNT asymptotic, and no exceptional prime pattern**. The same argument applies to every member of this orthogonal-circle zero-twist endpoint family whose positive endpoint coordinate `u_n` increases without bound. Thus parabolicity here is a telescoping background effect of escape to infinity, not a prime-gap invariant.

## 1. Exact derivation from the prime-flute cuffs

The proof is internal to the exact geometry up to the one imported tight-flute theorem.

PF-001 established

\[
\ell_n
=
2\log\frac{\sqrt{u_n}+\sqrt{u_{n-1}}}
             {\sqrt{u_n}-\sqrt{u_{n-1}}},
\]

which is equivalent to (1). Since `p_n -> infinity` and

\[
\cot\frac{\pi}{p_n}\to\infty,
\]

(2) is an exact telescoping identity.

No estimate on the size or regularity of `p_n-p_{n-1}` is needed. In particular, replacing the primes by any strictly increasing labels that drive the same endpoint coordinate to infinity leaves the proof unchanged.

## 2. Dynamical and probabilistic consequences are equally universal

Gordillo Herrerías–Le Quellec, *Ergodic Geodesic Flows and First Kind Flute Surfaces* (arXiv:2510.24576v2, revised 29 January 2026), summarizes the standard equivalences for a parabolic Riemann surface `X=H/Gamma`. In particular parabolicity is equivalent to:

- absence of a positive Green function;
- zero harmonic measure of the boundary at infinity;
- recurrence of Brownian motion;
- ergodicity of the geodesic flow on `T^1 X`;
- divergence of
  \[
  \sum_{\gamma\in\Gamma} e^{-d(z,\gamma z)}.
  \]

Consequently every one of these scalar/global classifications is fixed before any fine prime-gap fluctuation enters the geometry.

Since a Fuchsian critical exponent satisfies `delta(Gamma)<=1`, divergence of the Poincaré series at `s=1` also forces

\[
\delta(\Gamma)=1
\]

and divergence type at the critical exponent. PF-023 records the corresponding Patterson–Sullivan consequences and should be used for that stronger boundary-measure statement.

## 3. Why this closes a natural prime-flute branch

A tempting route was

\[
\text{prime gaps}
\longrightarrow
\{\ell_n\}
\longrightarrow
\text{parabolic/first-kind or recurrence data}
\longrightarrow
\text{spectral/dynamical arithmetic signal}.
\]

Equations (1)--(4) show that the middle global classification has already forgotten the prime gaps. Its decisive input is only

\[
u_n\uparrow\infty.
\]

Thus none of the following can by itself be a prime-sensitive RH mechanism for this construction:

```text
parabolic versus non-parabolic type,
completeness of the zero-twist flute,
Brownian recurrence,
geodesic-flow ergodicity,
divergence of the Poincare series at s=1,
the associated critical exponent delta=1.
```

This does **not** rule out finer return-time statistics, non-leading transfer-operator spectrum, correlations, relative scattering, or other observables that retain multi-gap cross-ratio data. It only removes the global type/recurrence branch.

## 4. Relation to PF-023

The previous version of PF-012 recorded this conclusion as an audit-sensitive working statement. The primary-source audit is now closed for the parabolicity input:

```text
PF-001 exact cuff identity
    -> telescoping sum h_n = infinity
    -> sum exp(-ell_n/2) = infinity
    -> BHS zero-twist criterion
    -> parabolic + complete
    -> standard recurrence/ergodicity/Poincare-divergence equivalences.
```

PF-023 independently reaches `delta=1` from the bottom of the Laplacian and records the Patterson–Sullivan/Lebesgue conclusion. Keeping the two findings separate avoids using boundary-measure uniqueness as part of the proof of parabolicity.

## 5. Novelty audit

The imported theorems are established literature, not project novelty:

- A. Basmajian, H. Hakobyan, D. Šarić, *The type problem for Riemann surfaces via Fenchel–Nielsen parameters*, Proc. London Math. Soc. 125 (2022), 568–625, DOI `10.1112/plms.12465`, arXiv:2011.03166. Theorem 1.5 states the zero-twist equivalence used in (5).
- E. Gordillo Herrerías, N. Le Quellec, *Ergodic Geodesic Flows and First Kind Flute Surfaces*, arXiv:2510.24576v2 (29 January 2026), Theorem 1.1 summarizes the parabolicity/Green-function/harmonic-measure/Poincaré-series/Brownian-recurrence/geodesic-flow equivalences and places them in the current flute-surface literature.

No novelty is claimed for those equivalences. The durable project-specific contribution is the exact one-line reduction (1)--(4), which shows that the prime-flute satisfies the zero-twist criterion for a reason that is completely independent of prime-gap fluctuations. That makes the negative conclusion stronger than a numerical or asymptotic observation: the global parabolic/dynamical type is structurally universal across the whole escaping-endpoint subfamily.

## 6. Audit / falsification core

To falsify the project-specific deduction one would have to break one of the following explicit steps:

1. PF-001's identity `e^{-ell_n/2}=tanh(h_n/4)`;
2. monotone escape `u_n=cot(pi/p_n) -> infinity`;
3. the elementary implication `sum h_n=infinity => sum tanh(h_n/4)=infinity`;
4. applicability of the BHS zero-twist tight-flute theorem to the prime-flute construction.

The literature audit confirms item 4. No prime-number-theoretic estimate is an input to the argument.