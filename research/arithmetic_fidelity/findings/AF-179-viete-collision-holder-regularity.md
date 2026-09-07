# AF-179 — Viète recovery has exact multiplicity-controlled Hölder exponent

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONING-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

The Viète map gives a clean Arithmetic Fidelity example in which **no set-theoretic information is lost after quotienting by the intended permutation gauge, yet inverse recovery becomes intrinsically non-Lipschitz at collision strata**.

Let

\[
\mathcal P_n
=\left\{p(z)=z^n+c_1z^{n-1}+\cdots+c_n:c_j\in\mathbb C\right\}
\cong\mathbb C^n
\tag{1}
\]

be the monic degree-`n` polynomials, equipped with any fixed norm on the coefficient vector. Let

\[
\operatorname{Sym}^n(\mathbb C)=\mathbb C^n/S_n
\tag{2}
\]

be unordered root multisets, equipped with the bottleneck matching metric

\[
d_{\rm root}([\lambda],[\mu])
:=\min_{\sigma\in S_n}\max_{1\le i\le n}
|\lambda_i-\mu_{\sigma(i)}|.
\tag{3}
\]

The Viète map

\[
V:\operatorname{Sym}^n(\mathbb C)\to\mathcal P_n,
\qquad
[\lambda_1,\dots,\lambda_n]
\mapsto
\prod_{i=1}^n(z-\lambda_i),
\tag{4}
\]

is bijective; its inverse `R=V^{-1}` recovers the unordered root multiset exactly.

Fix

\[
p_0(z)=\prod_{j=1}^r(z-\alpha_j)^{\mu_j},
\qquad
\alpha_i\ne\alpha_j\ (i\ne j),
\tag{5}
\]

and put

\[
m(p_0):=\max_j\mu_j.
\tag{6}
\]

Define the pointwise Hölder recovery exponent of `R` at `p_0` by

\[
h_R(p_0)
:=\sup\left\{\gamma>0:
\begin{array}{l}
\text{there exist }C>0\text{ and a neighborhood }U\ni p_0\\
\text{such that }d_{\rm root}(R(p),R(p_0))
\le C\|p-p_0\|^\gamma\quad(p\in U)
\end{array}
\right\}.
\tag{7}
\]

Then

\[
\boxed{
 h_R(p_0)=\frac1{m(p_0)}.
}
\tag{8}
\]

In particular:

- on the simple-root stratum, `m(p_0)=1`, so unordered-root recovery is locally Lipschitz;
- at a polynomial with an `m`-fold root, no local inverse estimate with exponent `\gamma>1/m` is possible;
- the loss of regularity is therefore controlled exactly by the largest collision multiplicity, even though the coefficient vector still determines the complete unordered root multiset.

This separates two notions that must not be conflated in Arithmetic Fidelity:

\[
\text{exact quotient fidelity}
\not\Rightarrow
\text{stable/Lipschitz recoverability}.
\tag{9}
\]

The discriminant/collision locus is not a set-theoretic failure of the Viète quotient. It is a **regularity boundary for its inverse in the natural coefficient and matching metrics**.

## Derivation

### Local root clusters persist

Choose pairwise disjoint closed disks

\[
D_j=\{z:|z-\alpha_j|\le r_j\}
\tag{10}
\]

small enough that `D_j` contains no root of `p_0` other than `\alpha_j`. On `\partial D_j`, `p_0` has a positive minimum modulus. Hence, for every polynomial `p` sufficiently close to `p_0` in coefficient norm, Rouché's theorem gives exactly `\mu_j` roots of `p` in `D_j`, counted with multiplicity.

Write

\[
p_0(z)=(z-\alpha_j)^{\mu_j}g_j(z),
\qquad
g_j(\alpha_j)\ne0.
\tag{11}
\]

After shrinking `D_j` if necessary, there is `a_j>0` such that

\[
|g_j(z)|\ge a_j
\qquad(z\in D_j).
\tag{12}
\]

Because all the disks lie in one fixed bounded set, evaluation of a coefficient perturbation is uniformly bounded there: there is `K>0` such that

\[
|p(z)-p_0(z)|\le K\|p-p_0\|
\qquad
\left(z\in\bigcup_jD_j\right)
\tag{13}
\]

for every nearby monic degree-`n` polynomial `p`. This uses only finite-dimensional norm equivalence and the elementary estimate of polynomial evaluation on a bounded set.

Now let `\beta` be a root of `p` lying in `D_j`. Since `p(\beta)=0`,

\[
|p_0(\beta)|
=|p_0(\beta)-p(\beta)|
\le K\|p-p_0\|.
\tag{14}
\]

Equations `(11)`--`(12)` therefore give

\[
a_j|\beta-\alpha_j|^{\mu_j}
\le K\|p-p_0\|,
\tag{15}
\]

hence

\[
|\beta-\alpha_j|
\le
\left(\frac K{a_j}\right)^{1/\mu_j}
\|p-p_0\|^{1/\mu_j}.
\tag{16}
\]

For sufficiently small `\|p-p_0\|<1`, and because `\mu_j\le m(p_0)`,

\[
\|p-p_0\|^{1/\mu_j}
\le
\|p-p_0\|^{1/m(p_0)}.
\tag{17}
\]

There are exactly `\mu_j` perturbed roots in each `D_j` and exactly `\mu_j` copies of `\alpha_j` in `R(p_0)`, so roots can be matched cluster by cluster. Taking the maximum of `(16)` over the finitely many clusters yields

\[
\boxed{
 d_{\rm root}(R(p),R(p_0))
\le C\|p-p_0\|^{1/m(p_0)}
}
\tag{18}
\]

for all sufficiently nearby `p`. Therefore

\[
h_R(p_0)\ge\frac1{m(p_0)}.
\tag{19}
\]

### The multiplicity exponent is sharp at every polynomial

Choose a root `\alpha` of maximal multiplicity

\[
m:=m(p_0)
\tag{20}
\]

and factor

\[
p_0(z)=(z-\alpha)^m g(z),
\qquad g(\alpha)\ne0.
\tag{21}
\]

For small nonzero `t\in\mathbb C`, define

\[
p_t(z)=\big((z-\alpha)^m-t\big)g(z).
\tag{22}
\]

This remains monic of degree `n`, and

\[
p_t-p_0=-t g.
\tag{23}
\]

If `A>0` denotes the norm of the padded coefficient vector of `g`, then exactly

\[
\|p_t-p_0\|=A|t|.
\tag{24}
\]

The roots of `g` are unchanged. The `m` copies of `\alpha` split into

\[
\alpha+t^{1/m}\omega_k,
\qquad
\omega_k^m=1,
\tag{25}
\]

all at Euclidean distance `|t|^{1/m}` from `\alpha`.

Let

\[
d_0:=\min\{|\alpha-\zeta|:g(\zeta)=0\}>0.
\tag{26}
\]

For `|t|^{1/m}<d_0/3`, matching each unchanged root of `g` to itself and each split root to one copy of `\alpha` gives

\[
d_{\rm root}(R(p_t),R(p_0))\le |t|^{1/m}.
\tag{27}
\]

No matching can do better. Any matching of a copy of `\alpha` to a root of `g` has cost at least `d_0`, while a matching with cost below `d_0` must pair all `m` copies of `\alpha` with the `m` split roots, each at distance exactly `|t|^{1/m}`. Thus

\[
\boxed{
 d_{\rm root}(R(p_t),R(p_0))=|t|^{1/m}.
}
\tag{28}
\]

Suppose a Hölder estimate with exponent `\gamma>1/m` held near `p_0`. Along `(22)`, equations `(24)` and `(28)` would imply

\[
|t|^{1/m}
\le C(A|t|)^\gamma,
\tag{29}
\]

or

\[
|t|^{1/m-\gamma}\le CA^\gamma.
\tag{30}
\]

The left-hand side tends to infinity as `t\to0`, a contradiction. Hence

\[
h_R(p_0)\le\frac1m.
\tag{31}
\]

Together with `(19)`, this proves `(8)`.

## Exact controls

### Simple-root control

If every root is simple, `m(p_0)=1`, and `(18)` is locally Lipschitz. This also follows root by root from the implicit-function theorem because

\[
\partial_z p_0(\alpha_j)=p_0'(\alpha_j)\ne0.
\tag{32}
\]

The sharpness family `(22)` with `m=1` shows that exponents strictly larger than `1` are impossible in general. Thus the simple stratum has pointwise exponent exactly `1`, not merely at least `1`.

### Full collision control

At

\[
p_0(z)=z^n,
\qquad
p_t(z)=z^n-t,
\tag{33}
\]

the coefficient perturbation is exactly `|t|` in the constant coefficient while every root moves a distance `|t|^{1/n}`. This is the classical model behind the global degree-`n` root-perturbation exponent.

### Intended gauge versus genuine instability

Before quotienting, ordered root vectors have an `S_n` labeling ambiguity. Viète coefficients deliberately forget that labeling. After passing to `\operatorname{Sym}^n(\mathbb C)`, however, the map `(4)` is one-to-one: there is no residual finite fiber to repair.

The failure at `(8)` is therefore not hidden permutation information. It is a failure of **metric regularity of exact recovery**. Collision multiplicity makes the same exact inverse increasingly sensitive to coefficient perturbation.

## Prior art and novelty assessment

No theorem-level novelty claim is made. The underlying root-perturbation phenomenon is classical, and the multiplicity-dependent exponent is explicitly present in the literature.

- David Brink, **“Hölder Continuity of Roots of Complex and p-adic Polynomials,”** *Communications in Algebra* 38(5) (2010), 1658--1662, DOI `10.1080/00927870902971320`, proves a multiplicity-sensitive continuity theorem: a root of multiplicity `\mu` has local Hölder order `1/\mu` as the coefficients vary, deriving it from local Lipschitz continuity of coprime factors.
- Bernard Beauzamy, **“How the Roots of a Polynomial Vary with its Coefficients: A Local Quantitative Result,”** *Canadian Mathematical Bulletin* 42(1) (1999), 3--12, DOI `10.4153/CMB-1999-001-6`, places the result against Ostrowski's classical global degree-`n` `\varepsilon^{1/n}` estimate and gives sharper local bounds that account for root multiplicity, including linear behavior at simple roots.
- The identification of monic coefficients with elementary symmetric functions of the unordered roots is the classical Viète correspondence. The discriminant detects the collision locus where roots cease to be simple.

AF-179's contribution is organizational rather than a claim of new polynomial perturbation theory: it packages the classical multiplicity law as an exact **Arithmetic Fidelity recovery exponent** for the natural quotient metric, with an elementary matching proof of both the local upper modulus and sharpness at every multiplicity profile.

The important distinction for this line is that classical continuity of roots is not merely a numerical-analysis caution. It gives a theorem-level counterexample to the inference

\[
\text{injective/correct quotient}
\Longrightarrow
\text{well-conditioned recovery}.
\tag{34}
\]

A compression can preserve the target exactly and still move from Lipschitz recovery to fractional-power recovery solely because the source approaches a collision stratum.

## Boundaries and failure modes

1. **Metric dependence matters.** Equation `(8)` is for a fixed finite-dimensional coefficient norm and the bottleneck matching metric `(3)`. All coefficient norms on `\mathbb C^n` are equivalent, so the exponent is norm-independent within that class, but a deliberately reweighted or snowflaked output metric can change Hölder exponents by definition.

2. **This is quotient-level recovery, not labeled-root recovery.** Global continuous labeling of individual roots is obstructed by monodromy even away from collisions. The theorem avoids that separate issue by working on the unordered symmetric product.

3. **The discriminant locus is a regularity boundary, not necessarily a singularity of the abstract quotient variety.** For one complex coordinate the symmetric product itself is identifiable with coefficient space. The branching occurs in the ordered-root map and manifests here as poor regularity when the quotient is measured by the natural matching metric.

4. **Largest multiplicity controls the pointwise exponent.** The proof does not say that every perturbation realizes the worst exponent. Many directions can be much better conditioned; `(8)` classifies the best uniform local exponent over all nearby coefficient perturbations.

5. **No arithmetic conclusion follows.** This result does not distinguish rational primes, does not invoke zeta zeros, and is not evidence for RH. It is a general compression theorem intended to sharpen which kind of stability must be checked before applying a formally faithful representation to arithmetic data.

## Consequences for Arithmetic Fidelity

AF-179 adds a third axis to the line's quotient audit. Fiber tests answer whether a target survives set-theoretically; minimal lifts answer what extra information is needed when it does not; the present theorem shows that, even after the fiber is reduced exactly to the intended gauge, one must still ask for the **inverse recovery modulus**.

For a transformation `T` and target quotient metric, a useful audit should therefore distinguish at least:

\[
\begin{array}{c}
\text{fiber fidelity: is the target determined?}\\[2mm]
\text{regularity fidelity: how does reconstruction error scale?}
\end{array}
\tag{35}
\]

The Viète map supplies a particularly clean calibration because the first answer is globally perfect while the second has an exact stratified law `1/m`.

This also sharpens the current collision/condition-number frontier. A diverging local Lipschitz condition number need not mean that exact recovery has disappeared. At a collision it can instead signal a **change of regularity class**: the correct replacement for a failed Lipschitz estimate may be a sharp Hölder modulus whose exponent is forced by the local branching multiplicity. Future compression audits near singular or collision strata should test for that possibility before declaring either complete instability or genuine information loss.