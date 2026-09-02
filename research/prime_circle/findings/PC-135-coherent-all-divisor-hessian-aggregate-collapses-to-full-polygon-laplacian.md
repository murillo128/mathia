# PC-135 — coherent all-divisor Hessian aggregate collapses to the full-polygon Laplacian

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the canonical equal-weight growing divisor-shell Hessian aggregate.

## Claim

Let

\[
\mu_N=\bigsqcup_{d\mid N}P_d^*
\]

be the exact-order decomposition of the regular `N`-gon. Form the collision energy obtained by including, with their intrinsic multiplicity one, every same-shell logarithmic Vandermonde interaction and every cross-shell logarithmic resultant interaction. Its angular Hessian at the roots of unity is **exactly** the universal inverse-square chord Laplacian of the complete regular `N`-gon:

\[
\boxed{
-D^2V_N=\mathcal L_N,
\qquad
\operatorname{Spec}(\mathcal L_N)
=\left\{\frac{k(N-k)}2:0\le k<N\right\}.
}
\]

Thus allowing the number of primitive-shell blocks to grow over the complete divisor lattice does not preserve the arithmetic birth labels in this coherent aggregate. The partition recombines to the ordinary full-polygon Vandermonde before spectralization.

This closes one natural growing-network escape left outside PC-134. It does **not** classify selectively weighted, cross-shell-only, non-polynomial, or genuinely non-Cauchy growing operators.

## 1. Exact-order shells partition every root once

Write

\[
z_a=e^{2\pi ia/N},\qquad 0\le a<N.
\]

Each `z_a` has a unique exact order `d|N`, hence

\[
\mu_N=\bigsqcup_{d\mid N}S_d,
\qquad S_d:=P_d^*.
\]

The common anchor is not discarded: `S_1={1}` is one of the exact-order strata.

For independent angular variables `theta_a`, define the full logarithmic collision energy

\[
V_N(\theta)
:=
\sum_{0\le a<b<N}
\log|e^{i\theta_a}-e^{i\theta_b}|.
\]

Partitioning the unordered vertex pairs by their exact-order labels gives the identity

\[
\boxed{
V_N
=
\sum_{d\mid N}V_{d,d}
+
\sum_{\substack{d<e\\d,e\mid N}}V_{d,e},
}
\]

where `V_{d,d}` is the within-`S_d` Vandermonde energy and `V_{d,e}` is the cross energy between `S_d` and `S_e`.

At the undeformed roots of unity,

\[
2V_{d,d}=\log|\operatorname{Disc}\Phi_d|,
\qquad
V_{d,e}=\log|\operatorname{Res}(\Phi_d,\Phi_e)|.
\]

Accordingly the scalar product identity is the standard discriminant factorization induced by

\[
x^N-1=\prod_{d\mid N}\Phi_d(x):
\]

\[
\boxed{
|\operatorname{Disc}(x^N-1)|
=
\prod_{d\mid N}|\operatorname{Disc}\Phi_d|
\prod_{d<e}|\operatorname{Res}(\Phi_d,\Phi_e)|^2
=N^N.
}
\]

The point here is not this classical scalar identity but what happens when the full vertexwise second variation is retained.

## 2. The Hessians recombine edge by edge

For one pair with angular difference `delta`,

\[
f(\delta)=\log\left|2\sin\frac\delta2\right|
\]

satisfies

\[
-f''(\delta)
=
\frac1{4\sin^2(\delta/2)}.
\]

Therefore, at the regular `N`-gon, every unordered pair `{a,b}` contributes the rank-one edge Laplacian

\[
\frac1{|z_a-z_b|^2}
(e_a-e_b)(e_a-e_b)^*.
\]

PC-128 identifies the cross-shell pieces `-D^2V_{d,e}` precisely with the corresponding bipartite inverse-square chord Laplacians. The same calculation for `V_{d,d}` gives the within-shell edge blocks. Since the exact-order partition assigns every unordered pair to exactly one of these terms,

\[
\boxed{
- D^2 V_N
=
\sum_{d\mid N}(-D^2V_{d,d})
+
\sum_{d<e}(-D^2V_{d,e})
=
\mathcal L_N,
}
\]

where

\[
(\mathcal L_N)_{ab}
=
-\frac1{|z_a-z_b|^2}
\quad(a\ne b),
\]

and the diagonal makes each row sum to zero.

This equality is stronger than a determinant or trace identity: the complete operator itself is independent of the divisor-shell bookkeeping once all canonically required collision terms are assembled.

## 3. The spectrum is the classical full-polygon spectrum

`\mathcal L_N` is circulant, so Fourier modes diagonalize it. As already used in PC-032 and in the classical Calogero--Perelomov `csc^2` matrix calculation,

\[
\boxed{
\lambda_k=\frac{k(N-k)}2,
\qquad 0\le k<N.
}
\]

Consequently every spectral invariant of the coherent aggregate is an elementary function of this list. For example,

\[
\operatorname{pdet}\mathcal L_N
=
\prod_{k=1}^{N-1}\frac{k(N-k)}2
=
\boxed{\frac{((N-1)!)^2}{2^{N-1}}}.
\]

The all-divisor construction has therefore returned exactly to the single regular-polygon inverse-square spectrum already classified in PC-032. Any spectral-zeta interpretation of the resulting single-polygon object is additionally inside the prior-art boundary recorded in PC-008; the divisor labels have disappeared before such a transform is taken.

## 4. Growing `N` does not restore the arithmetic labels

This collapse is not merely finite-window. Normalize the eigenvalues by `N^2` and form the empirical measure

\[
\nu_N
:=
\frac1N\sum_{k=0}^{N-1}
\delta_{\lambda_k/N^2}.
\]

Since

\[
\frac{\lambda_k}{N^2}
=
\frac12\frac{k}{N}\left(1-\frac{k}{N}\right),
\]

ordinary Riemann-sum convergence gives

\[
\boxed{
\nu_N\Longrightarrow
\left(x\mapsto\frac{x(1-x)}2\right)_*dx.
}
\]

The limiting density is explicitly

\[
\boxed{
\frac{4}{\sqrt{1-8y}}\,\mathbf 1_{(0,1/8)}(y)\,dy.
}
\]

Thus even though the number of divisor shells and pair-shell Hessian blocks can grow without bound with `N`, the canonically aggregated spectrum has a universal factorization-blind continuum limit. No prime-factor statistics survive in it.

## 5. Falsification control: the arithmetic partition is irrelevant

The strongest control is immediate. Replace the exact-order partition `\{S_d:d|N\}` by **any** partition of the same `N` roots, then sum the same within-block and between-block logarithmic collision energies with coefficient one. Every unordered pair still occurs exactly once, so the resulting Hessian is again `\mathcal L_N`.

Hence the collapse is not a subtle cyclotomic cancellation. It is a partition-forgetting identity. The arithmetic content of the exact-order labels matters only if a construction does something nontrivial with those labels before summing all edges equally.

This rules out interpreting the complete equal-weight divisor-shell resultant/discriminant Hessian as a new arithmetic spectral object. Its apparent cross-level complexity is bookkeeping for a universal regular-polygon operator.

## 6. Relation to the current frontier

PC-134 proves that every **fixed finite** polynomial tensor network of resultant Hessian edges lies in confluent Cauchy/cyclotomic algebra, but deliberately leaves growing-level organizations open. The present result treats one especially canonical growing organization: take the full divisor lattice of a conductor `N` and include every collision term dictated by the factorization of `x^N-1`. Despite the growing number of shell blocks, it collapses exactly to `\mathcal L_N` for every `N` and has a universal normalized limit.

PC-012 is complementary: it says finite unlabeled cross-level chord arrangements embed in one regular polygon. PC-135 is an operator-level version for the complete **vertexwise logarithmic collision Hessian**, including both same-shell discriminant and cross-shell resultant terms, and it remains exact along a growing sequence of conductors.

The surviving boundary is narrower but nonempty. This finding does not rule out:

- the cross-shell Hessian sum with the within-shell discriminant pieces deliberately omitted;
- arithmetic or scale-dependent weights on different divisor pairs;
- inverses, Schur complements, or other non-polynomial functional calculus applied before the partition is forgotten;
- growing networks that do not contain every edge with the same canonical coefficient;
- intrinsically non-Cauchy operators;
- nonlinear global uniformization/monodromy.

Any such escape must justify its weighting or omission intrinsically. The unweighted coherent product supplied directly by the cyclotomic factorization does not do the job.

## 7. Prior art and novelty audit

No theorem-level novelty is claimed for the ingredients:

- `Disc(fg)=Disc(f)Disc(g)Res(f,g)^2` (up to the conventional sign) is a standard discriminant/resultant identity;
- `x^N-1=prod_{d|N}Phi_d(x)` is the standard cyclotomic factorization;
- the `csc^2` regular-polygon spectrum is classical Calogero--Perelomov theory and is already anchored in `SOURCES.md` for PC-032;
- single-polygon Riesz/spectral-zeta RH reformulations are already prior art in PC-008.

A directed novelty check against discriminant product formulas, roots-of-unity logarithmic energies, Calogero/Sutherland `csc^2` Hessians, and regular-polygon spectral zeta did not expose a distinct arithmetic mechanism in this complete divisor-shell aggregation. The durable contribution is therefore a scope result specific to the current research program: **one natural way to cross PC-134's fixed-network boundary still loses all exact-order information because the growing divisor network recombines to the full Vandermonde Hessian before spectralization.**
