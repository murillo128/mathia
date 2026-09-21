---
finding_id: NB-273
prefix: NB
title: Target-anchor floor forces coefficient mass to escape every fixed shell prefix
status: proposed
verdict: pending
reviewed: false
created: 2026-09-21
updated: 2026-09-21
authors:
  - OpenAI
origin:
  kind: research-watch
  ref: nyman_beurling
depends_on:
  - NB-269
  - NB-272
supersedes: []
superseded_by: []
related_findings:
  - NB-270
  - NB-271
---

# Target-anchor floor forces coefficient mass to escape every fixed shell prefix

## Claim

The `sqrt(K)` target-anchor mismatch left open by `NB-272` has a sharp geometric consequence in the resolved shell coordinates of `NB-269`.

Let

\[
S_K:\mathbb C^K\to\mathcal H,
\qquad
R_K=S_K^*S_K,
\qquad
b_K=S_K^*g,
\]

and assume the resolved Gram metric is uniformly nondegenerate,

\[
r_- I\preceq R_K\preceq r_+ I
\tag{1}
\]

for fixed `0<r_-<=r_+<infinity`. Write

\[
a_K:=R_K^{-1}b_K
\tag{2}
\]

for the unconstrained least-squares coefficient vector, and impose the Euler anchor

\[
e_K^*c=1,
\qquad
e_K=(1,\ldots,1)^T.
\tag{3}
\]

Embed each `a_K=(a_{K,0},...,a_{K,K-1})` in the common coefficient space `ell^2(N_0)` by zero-padding beyond `K-1`. If this coefficient family is uniformly tail-tight,

\[
\lim_{L\to\infty}
\sup_K
\sum_{j=L}^{K-1}|a_{K,j}|^2
=0,
\tag{4}
\]

then

\[
\boxed{
\frac{e_K^*a_K}{\sqrt K}\longrightarrow0.
}
\tag{5}
\]

Consequently the anchor mismatch

\[
\mu_K:=1-e_K^*a_K
\tag{6}
\]

satisfies `mu_K=o(sqrt(K))`, so the anchor penalty in the exact `NB-272` residual is `o(1)`.

Conversely, suppose along a subsequence the unanchored section defect tends to zero,

\[
\delta_K:=\operatorname{dist}(g,\operatorname{ran}S_K)\to0,
\tag{7}
\]

while the anchored residual stays above a fixed `eta>0`. Then for every fixed shell prefix length `L`, a nonzero amount of coefficient `ell^2` mass must remain beyond that prefix:

\[
\boxed{
\liminf_{K\to\infty}
\sum_{j=L}^{K-1}|a_{K,j}|^2
\ge
\frac{\eta}{2r_+}
}
\tag{8}
\]

along that subsequence. Thus, once the target itself is asymptotically captured by the resolved section, a surviving target-anchor obstruction is possible only through **coefficient mass escaping to increasing shell index**. It is incompatible with relative compactness, or equivalently uniform tail-tightness, of the unconstrained target coefficients in the declared shell coordinates.

This does not prove that the canonical Nyman target coefficients are tail-tight. It converts the remaining `NB-272` alternative into a concrete asymptotic target: either prove tail-tightness and eliminate the target-anchor floor, or exhibit genuine coefficient escape and identify the arithmetic mechanism that drives it.

## 1. Why this is the next discriminating question

`NB-269` showed that the resolved projected Hardy channel has a uniformly conditioned coefficient metric. `NB-271` then showed that any additional positive quadratic repair must be macroscopically strong: a bounded perturbation of that metric cannot produce an order-one anchored floor. `NB-272` separated the exact fixed-target problem into

\[
\inf_{e_K^*c=1}\|g-S_Kc\|_{\mathcal H}^2
=
\delta_K^2
+
\frac{|1-e_K^*R_K^{-1}b_K|^2}
{e_K^*R_K^{-1}e_K}.
\tag{9}
\]

Under (1),

\[
\frac{K}{r_+}
\le
e_K^*R_K^{-1}e_K
\le
\frac{K}{r_-}.
\tag{10}
\]

Therefore, if `delta_K=o(1)`, an order-one residual can survive only if

\[
|1-e_K^*a_K|\asymp\sqrt K
\tag{11}
\]

on some subsequence. The open issue was whether this `sqrt(K)` alternative was merely algebraically possible or whether it forced recognizable structure in the target coefficients.

The answer is rigid: bounded coefficient norm plus a `sqrt(K)` coherent sum cannot be carried by any fixed prefix, and it cannot occur in a uniformly tight family. The mass has to keep moving into newly opened coefficient coordinates.

## 2. The target minimizers have uniformly bounded coefficient norm

The first ingredient is automatic from the resolved Gram bounds. Since `a_K=R_K^{-1}b_K`, the synthesized vector `S_Ka_K` is the orthogonal projection of `g` onto `ran(S_K)`. Hence

\[
a_K^*R_Ka_K
=
\|S_Ka_K\|_{\mathcal H}^2
=
\|P_{\operatorname{ran}S_K}g\|_{\mathcal H}^2
\le
\|g\|_{\mathcal H}^2.
\tag{12}
\]

Using the lower spectral bound in (1),

\[
r_-\|a_K\|_2^2
\le
a_K^*R_Ka_K,
\]

so

\[
\boxed{
\sup_K\|a_K\|_2
\le
C_g:=\frac{\|g\|_{\mathcal H}}{\sqrt{r_-}}.
}
\tag{13}
\]

This is important because `sqrt(K)` growth of the unnormalized anchor pairing cannot come from growth of the total coefficient energy. It can only come from coherent participation of an increasing number of coordinates.

Equivalently, define the normalized anchor direction

\[
u_K:=\frac{1}{\sqrt K}(1,\ldots,1,0,0,\ldots)
\in\ell^2(\mathbb N_0).
\tag{14}
\]

Then `||u_K||_2=1` and `u_K` converges weakly to zero. The normalized mismatch-driving quantity is exactly

\[
\frac{e_K^*a_K}{\sqrt K}
=
\langle u_K,a_K\rangle.
\tag{15}
\]

A weakly null sequence pairs uniformly to zero against a relatively compact set. The next section gives the elementary tail proof specialized to the present coordinates, so no external compactness theorem is needed.

## 3. Uniform tail-tightness kills the sqrt(K) mismatch

Fix a prefix length `L<K`. Split the anchor sum into the first `L` coordinates and the tail:

\[
\frac1{\sqrt K}
\left|\sum_{j=0}^{K-1}a_{K,j}\right|
\le
\frac1{\sqrt K}
\left|\sum_{j=0}^{L-1}a_{K,j}\right|
+
\frac1{\sqrt K}
\left|\sum_{j=L}^{K-1}a_{K,j}\right|.
\tag{16}
\]

Cauchy-Schwarz and (13) give

\[
\frac1{\sqrt K}
\left|\sum_{j=0}^{L-1}a_{K,j}\right|
\le
C_g\sqrt{\frac LK},
\tag{17}
\]

while

\[
\frac1{\sqrt K}
\left|\sum_{j=L}^{K-1}a_{K,j}\right|
\le
\sqrt{\frac{K-L}{K}}
\left(
\sum_{j=L}^{K-1}|a_{K,j}|^2
\right)^{1/2}.
\tag{18}
\]

For fixed `L`, the prefix term in (17) tends to zero as `K` grows. Under the tail-tightness assumption (4), the second term can then be made uniformly arbitrarily small by taking `L` large. Therefore

\[
\frac{|e_K^*a_K|}{\sqrt K}\to0,
\tag{19}
\]

which proves (5).

Since

\[
|\mu_K|
=|1-e_K^*a_K|
=o(\sqrt K),
\tag{20}
\]

and the denominator in (9) is at least `K/r_+`, the anchor contribution obeys

\[
0\le
\frac{|\mu_K|^2}{e_K^*R_K^{-1}e_K}
\le
r_+\frac{|\mu_K|^2}{K}
=o(1).
\tag{21}
\]

Thus tail-tightness eliminates the only target-anchor mechanism left by `NB-272`. If additionally `delta_K=o(1)`, the full anchored residual tends to zero inside this resolved model.

The same conclusion follows if `{a_K}` is relatively compact in the zero-padded `ell^2` coefficient space. For uniformly bounded families, relative compactness is equivalent to uniform control of the coordinate tails used in (4), so (4) is the more concrete form for the present shell ordering.

## 4. Quantitative converse: a surviving floor forces tail escape

Assume now that along a subsequence

\[
\delta_K\to0
\tag{22}
\]

but

\[
\inf_{e_K^*c=1}\|g-S_Kc\|_{\mathcal H}^2
\ge\eta>0.
\tag{23}
\]

For all sufficiently large `K`, (9) and (22) imply

\[
\frac{|\mu_K|^2}{e_K^*R_K^{-1}e_K}
\ge\frac\eta2.
\tag{24}
\]

Using the lower denominator bound from (10),

\[
|\mu_K|^2
\ge
\frac\eta2\frac K{r_+}.
\tag{25}
\]

Set

\[
c_\eta:=\sqrt{\frac{\eta}{2r_+}}.
\tag{26}
\]

Then

\[
|e_K^*a_K|
\ge
|\mu_K|-1
\ge
c_\eta\sqrt K-1.
\tag{27}
\]

Fix any `L`. The prefix contribution is bounded uniformly in `K`:

\[
\left|\sum_{j=0}^{L-1}a_{K,j}\right|
\le
\sqrt L\,\|a_K\|_2
\le
C_g\sqrt L.
\tag{28}
\]

Therefore the tail must carry an anchor sum of size

\[
\left|\sum_{j=L}^{K-1}a_{K,j}\right|
\ge
c_\eta\sqrt K-1-C_g\sqrt L.
\tag{29}
\]

A final Cauchy-Schwarz estimate gives

\[
\left(
\sum_{j=L}^{K-1}|a_{K,j}|^2
\right)^{1/2}
\ge
\frac{c_\eta\sqrt K-1-C_g\sqrt L}
{\sqrt{K-L}}.
\tag{30}
\]

Taking `K->infinity` with `L` fixed yields

\[
\liminf_{K\to\infty}
\sum_{j=L}^{K-1}|a_{K,j}|^2
\ge
c_\eta^2
=
\frac\eta{2r_+},
\tag{31}
\]

which is (8).

This is stronger than merely saying that `{a_K}` is not compact. A fixed positive amount of coefficient energy must stay outside **every** fixed shell prefix. The lower bound is independent of `L`.

## 5. What the result does and does not identify

The result turns the target-side branch of the `NB-271`/`NB-272` fork into a concrete geometric dichotomy. Once the resolved section itself approximates the target (`delta_K->0`), either the unconstrained coefficient vectors remain tail-tight, in which case the Euler anchor costs `o(1)`, or an order-one anchored floor forces persistent coefficient energy into newly opened shell indices.

This statement is deliberately made in the **declared resolved shell coordinates**. It is not invariant under arbitrary `K`-dependent unitary changes of coefficient basis. That is not a defect hidden by the proof: the Euler anchor `e_K^*c=1` and the shell ordering are themselves coordinate data in this model. Any future claim of tail-tightness must therefore be proved for the actual Nyman/Ford shell parameterization, not manufactured by orthogonalizing the Gram matrix or choosing a favorable basis.

There is a second important qualification. In the rank-coupled families used in the recent Ford findings, the physical atoms can depend on `K`; zero-padding the coefficient vectors does **not** assert that shell `j` at rank `K` is literally the same Hilbert vector as shell `j` at another rank. Equation (31) is a coefficient-index escape statement, not physical strong convergence of generators. A useful next theorem must connect this index escape to the actual target pairings `b_K` and shell geometry.

Finally, the result says nothing if the section defect `delta_K` itself stays bounded away from zero. In that case the obstruction already lives in target-span geometry and no anchor analysis is needed. `NB-273` isolates only the harder regime in which the target is asymptotically captured before the Euler normalization is imposed.

## 6. Adversarial checks

### Check A: bounded norm alone is not enough

The extreme vector

\[
a_K=K^{-1/2}e_K
\tag{32}
\]

has `||a_K||_2=1` but

\[
e_K^*a_K=\sqrt K.
\tag{33}
\]

It realizes the dangerous scale from `NB-272`. It also violates tail-tightness maximally: for every fixed `L`,

\[
\sum_{j=L}^{K-1}|a_{K,j}|^2
=1-\frac LK\to1.
\tag{34}
\]

So the added hypothesis is genuinely stronger than the already-known coefficient norm bound and is exactly targeted at the remaining failure mode.

### Check B: pointwise coefficient convergence is not enough

The same example has `a_{K,j}=K^{-1/2}->0` for each fixed `j`, yet the normalized anchor pairing stays equal to one. Thus coordinatewise convergence, or control of every fixed prefix separately, does not suffice. Uniform tail control is the relevant topology.

### Check C: a moving packet gives the same obstruction

Take a normalized block of width `M_K->infinity` supported on indices that move to infinity. Its `ell^2` norm can remain bounded while every fixed prefix eventually vanishes. If the block has coherent phase, its anchor sum can scale like `sqrt(M_K)`. Reaching the full `sqrt(K)` scale requires a macroscopically large coherent block, but the theorem does not assume any particular packet shape; it only records the necessary tail energy.

### Check D: no zeta-zero statement is being made

The proof uses only the exact finite-dimensional residual identity of `NB-272`, the resolved Gram bounds of `NB-269`, and elementary Hilbert-space estimates. It does not place synthetic zeros, infer a property of actual zeta zeros, or import a zero-density hypothesis.

### Check E: no revival of the refuted cross-cutoff clue

`CLUE-cross-cutoff-coherence-breaks-inverse-section-repair` was resolved as refuted. The present statement does not use its inverse-section coherence claim. `NB-273` concerns the coefficient geometry of the **target minimizer** `a_K=R_K^{-1}b_K` and follows directly from (9). The two statements should not be conflated.

## 7. Prior-art audit

A fresh search covered Nyman-Beurling Gram/finite-section coefficient behavior, finite-section stability, and standard `ell^2` compactness/tail criteria. The generic fact that bounded uniformly tail-tight subsets of `ell^2` are relatively compact is standard Hilbert-space analysis, and the weak-null pairing observation in (15) is likewise standard. Recent Nyman-Beurling Gram work studies decay and compressibility of generator Gram matrices, while general finite-section literature studies stability and convergence of truncations.

No external theorem is load-bearing here: (13), (16)-(21), and (24)-(31) provide the complete argument needed for the research-line claim. The new content for this line is the coupling of the exact `NB-272` anchored residual with the `NB-269` uniform Gram bounds to classify the only remaining `sqrt(K)` target mismatch as coefficient-tail escape. No new source dependency is therefore added to `SOURCES.md`.

## 8. Research consequence and next discriminating test

`NB-272` left two target-side mechanisms for a persistent floor: a nonvanishing section defect `delta_K`, or a `sqrt(K)` anchor mismatch. `NB-273` makes the second mechanism testable without guessing another Gram correction.

The next high-value calculation is to estimate the actual unconstrained target coefficients

\[
a_K=R_K^{-1}b_K
\tag{35}
\]

in the resolved Nyman shell family and ask whether their tails are uniformly tight in the physical shell ordering. There are two sharply different outcomes:

1. If one can prove a uniform tail estimate of the form

\[
\sup_K\sum_{j\ge L}|a_{K,j}|^2\le\varepsilon_L,
\qquad
\varepsilon_L\to0,
\tag{36}
\]

then the target-anchor branch is closed: any remaining order-one obstruction must be `delta_K` or a genuinely new source-source component outside the resolved channel.

2. If (36) fails, the escaping tail is itself new structure. One should then locate its shell scale, phase coherence, and dependence on the exact target pairings `b_K`. A `sqrt(K)` mismatch requires not merely energy at high index but enough coherent aggregate pairing with the anchor to survive normalization.

This is a better discriminator than another abstract off-diagonal Gram ansatz. It asks directly whether the canonical target solution exhibits the only coefficient geometry capable of sustaining the `NB-272` anchor obstruction.

## Conclusion

For uniformly conditioned resolved Nyman sections, a target-anchor floor cannot remain mysterious once the unanchored target defect vanishes. If the unconstrained target coefficients are compact/tail-tight in the declared shell coordinates, the normalized Euler-anchor pairing vanishes and the anchor penalty is `o(1)`. If an order-one anchored floor nevertheless survives, a fixed positive amount of coefficient `ell^2` mass must escape beyond every fixed shell prefix.

The unresolved question is therefore no longer whether a `sqrt(K)` mismatch is algebraically possible; `NB-272` already showed that it is. The discriminating question is whether the **actual Nyman target** drives this required coefficient escape. That can now be attacked directly through `R_K^{-1}b_K` rather than by introducing another speculative Gram repair.
