# AF-251 — Exponential cancellation exception sets have codimension at least one

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `OUTPUT-SAMPLING`, `GENERIC-PHASE-BOUNDARY`, `DIOPHANTINE-FIDELITY`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-250 proves that destructive exponential cancellation in a fixed finite trigonometric mode is Haar exceptional. The exceptional set is substantially thinner than a measure-zero statement alone shows.

Let

\[
P(x)=\sum_{\ell=1}^{M}c_\ell e^{2\pi i\langle k_\ell,x\rangle},
\qquad x\in\mathbb T^d,
\tag{1}
\]

be a nonzero trigonometric polynomial, and write

\[
Z_P=\{x\in\mathbb T^d:P(x)=0\}.
\tag{2}
\]

If `Z_P` is nonempty, let `k=\dim_{\mathbb R}Z_P`; then `k\le d-1`. Define the exponential-cancellation exceptional set

\[
\mathcal E(P)
=
\left\{\alpha\in\mathbb T^d:
\limsup_{n\to\infty}
\frac{-\log |P(n\alpha)|}{n}>0
\right\},
\tag{3}
\]

with `-\log 0=+\infty`. Then

\[
\boxed{\dim_H\mathcal E(P)\le k\le d-1.}
\tag{4}
\]

If `Z_P=\varnothing`, then `\mathcal E(P)=\varnothing`.

Equivalently, outside a set of Hausdorff codimension at least one, the **entire** amplitude sequence satisfies

\[
\lim_{n\to\infty}|P(n\alpha)|^{1/n}=1,
\tag{5}
\]

and hence every unbounded output sampling `S\subset\mathbb N` is root-faithful. Conversely, every `\alpha\in\mathcal E(P)` admits some unbounded retained set on which the root rate is strictly below one. Thus `(3)` is exactly the phase set for which an adversarial infinite output sparsification can hide part of the finite-mode exponential scale.

The statement remains intrinsic on homogeneous lower-dimensional phase constraints. Let `H\le\mathbb T^d` be a connected subtorus of dimension `r\ge1`, let Haar/Hausdorff geometry be taken intrinsically on `H`, and suppose `P|_H` is not identically zero. Then

\[
\boxed{
\dim_H\bigl(\mathcal E(P)\cap H\bigr)
\le \dim_{\mathbb R}Z(P|_H)
\le r-1.
}
\tag{6}
\]

For the Li-shaped dominant modes

\[
P_m(x)=-2\sum_{j=1}^d m_j\cos(2\pi x_j),
\qquad m\in\mathbb N^d,
\tag{7}
\]

`P_m|_H` can never vanish identically on a connected subgroup because `0\in H` and

\[
P_m(0)=-2\sum_jm_j<0.
\tag{8}
\]

Consequently, for every connected `r`-dimensional subtorus `H`, the union of the bad sets for **all** positive-integer Li multiplicity patterns is still of Hausdorff dimension at most `r-1`:

\[
\boxed{
\dim_H\!\left(
\bigcup_{m\in\mathbb N^d}
\bigl(\mathcal E(P_m)\cap H\bigr)
\right)
\le r-1.
}
\tag{9}
\]

So exact homogeneous integer-linear relations among a finite collection of Keiper phases do not by themselves make exponential cancellation generic on the constrained locus. They can reduce the ambient dimension, but inside any connected subtorus the destructive generators remain confined to a codimension-at-least-one exceptional set.

## Why it matters

AF-250 changed the multimode obstruction from a generic phenomenon into a source-specific one: almost every phase vector is safe, but the actual zero-derived vector could still be exceptional. A natural concern remained that genuine arithmetic identities might force the phases onto a Haar-null subtorus, making full-torus genericity irrelevant.

Equation `(6)` closes that concern for **homogeneous toral constraints**. The same exceptional-set mechanism reruns intrinsically on every connected subtorus, and `(8)` removes the only catastrophic possibility for the Li multiplicity family, namely that the whole constrained subgroup lies in the cancellation locus. Therefore ordinary exact integer relations among phases cannot, by themselves, turn the AF-248 pathology into typical behavior. A source-specific obstruction would have to do something finer: place the actual phase vector in a thin shrinking-target subset of the allowed locus, impose an affine/non-homogeneous resonance, or supply another constraint not captured by membership in a connected subgroup.

The Hausdorff-dimension bound also calibrates how exceptional the missing arithmetic theorem is. In one phase dimension the bad set has Hausdorff dimension zero, strengthening AF-249's distinction between ordinary irrational phases and exponentially approximable exceptional phases. In several dimensions the universal upper bound is the dimension of the analytic cancellation locus itself, rather than the full phase-space dimension.

This still does **not** prove anything about the actual Riemann-zero phase vector. A fixed arithmetic point can lie in a set of Hausdorff dimension zero. The result instead removes a broad class of explanations for why genericity might fail after exact phase relations are imposed.

## Derivation / evidence

### 1. Exponentially small values lie exponentially close to the analytic zero set

The squared modulus

\[
f(x)=|P(x)|^2
\tag{10}
\]

is a nonnegative real-analytic function on the compact torus and has zero set exactly `Z_P`. The compact Łojasiewicz distance inequality gives constants `A>0` and `C>0` such that

\[
\operatorname{dist}(x,Z_P)^A\le C|P(x)|^2
\tag{11}
\]

for all `x\in\mathbb T^d` when `Z_P\ne\varnothing`.

Fix `c>0` and define

\[
E_n(c)=\{\alpha\in\mathbb T^d:|P(n\alpha)|<e^{-cn}\}.
\tag{12}
\]

By `(11)`, if `\alpha\in E_n(c)` then

\[
\operatorname{dist}(n\alpha,Z_P)
\le C_1e^{-\sigma n}
=:\delta_n,
\qquad \sigma=\frac{2c}{A}>0,
\tag{13}
\]

for a fixed `C_1`. Thus the amplitude shrinking target is contained in an exponentially shrinking tubular neighborhood of the fixed analytic zero set.

If `Z_P=\varnothing`, compactness gives `\min|P|>0`, so `(12)` is empty for all sufficiently large `n`; this proves the empty-set branch of the claim.

### 2. The zero set has polynomial covering complexity

A trigonometric polynomial is a Laurent polynomial in the torus characters. After multiplying by a nonvanishing monomial and using the standard embedding

\[
\mathbb T^d\hookrightarrow (S^1)^d\subset\mathbb R^{2d},
\tag{14}
\]

its real and imaginary zero conditions are polynomial. Hence `Z_P` is a compact real-algebraic/semialgebraic set in this embedding.

Classical stratification or tubular-neighborhood bounds for fixed real algebraic sets imply that, if `k=\dim_{\mathbb R}Z_P`, then for every `\eta>0` there are constants `C_{P,\eta}` and `\delta_0>0` such that `Z_P` can be covered, for `0<\delta<\delta_0`, by at most

\[
C_{P,\eta}\,\delta^{-(k+\eta)}
\tag{15}
\]

balls of radius comparable to `\delta`. The harmless `\eta` avoids needing a sharp Minkowski-content normalization; the fixed-set real-algebraic tube estimates are stronger than `(15)`.

Apply `(15)` at `\delta=\delta_n`. The multiplication map

\[
M_n:\mathbb T^d\to\mathbb T^d,
\qquad M_n(\alpha)=n\alpha,
\tag{16}
\]

has `n^d` local inverse sheets, each scaling distances by `1/n`. Therefore the preimage of the `\delta_n`-tube around `Z_P`, and hence `E_n(c)`, is coverable by at most

\[
C_{P,\eta}\,n^d\delta_n^{-(k+\eta)}
\tag{17}
\]

balls of radius at most `C_2\delta_n/n`.

### 3. Hausdorff--Borel--Cantelli removes one full dimension

Let `s>k`. Choose `\eta>0` with `k+\eta<s`. The total `s`-cost of the cover in `(17)` is bounded by

\[
C\,n^d\delta_n^{-(k+\eta)}
\left(\frac{\delta_n}{n}\right)^s
=
C\,n^{d-s}\delta_n^{s-k-\eta}.
\tag{18}
\]

Because `\delta_n=C_1e^{-\sigma n}` and `s-k-\eta>0`, the series

\[
\sum_{n=1}^{\infty}
 n^{d-s}\delta_n^{s-k-\eta}
\tag{19}
\]

converges exponentially. The Hausdorff--Borel--Cantelli covering lemma therefore gives

\[
\mathcal H^s\!\left(\limsup_{n\to\infty}E_n(c)\right)=0.
\tag{20}
\]

Since this holds for every `s>k`,

\[
\dim_H\left(\limsup_nE_n(c)\right)\le k.
\tag{21}
\]

Now `(3)` is the countable union over positive rational `c` of these limsup sets:

\[
\mathcal E(P)
=
\bigcup_{c\in\mathbb Q_{>0}}
\limsup_{n\to\infty}E_n(c).
\tag{22}
\]

Hausdorff dimension is countably stable under unions, so `(4)` follows.

This proof is different from AF-250's Haar-measure argument. AF-250 only needs a small-value **measure** estimate. AF-251 resolves the geometry of the exceptional generators themselves: exponential amplitude loss forces exponentially accurate recurrence to a fixed lower-dimensional algebraic target, while the polynomial `n^d` proliferation of inverse sheets is too slow to compensate for exponential target shrinkage.

### 4. The exceptional set is exactly the all-sampling failure set

If `\alpha\notin\mathcal E(P)`, then

\[
\limsup_n\frac{-\log|P(n\alpha)|}{n}=0.
\tag{23}
\]

The quantity in `(23)` is eventually finite and nonnegative up to an `O(1/n)` adjustment when `|P|>1`; boundedness of `P` supplies the complementary upper root bound. Hence

\[
|P(n\alpha)|^{1/n}\longrightarrow1.
\tag{24}
\]

Every unbounded subsequence inherits `(24)`.

Conversely, if `\alpha\in\mathcal E(P)`, choose `c>0` below the positive limsup in `(3)`. There are infinitely many indices with

\[
|P(n\alpha)|^{1/n}<e^{-c}.
\tag{25}
\]

Taking those indices as an unbounded set `S` gives

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|P(n\alpha)|^{1/n}
\le e^{-c}<1.
\tag{26}
\]

Thus `(3)` is not merely a convenient exceptional set: it exactly parameterizes phase generators for which **some** infinite output sampling loses root fidelity.

### 5. The argument localizes to connected subtori

Let `H\le\mathbb T^d` be a connected subtorus of dimension `r`. Then `H\cong\mathbb T^r`, multiplication by `n` restricts to a degree-`n^r` local similarity on `H`, and `P|_H` is again a trigonometric polynomial in intrinsic torus coordinates.

If `P|_H` is nonzero, its zero set has real dimension at most `r-1`. Repeating `(10)`--`(22)` with `d` replaced by `r` proves `(6)`.

For `(7)`, equation `(8)` shows nonvanishing of the restricted polynomial for every connected subgroup. Since `\mathbb N^d` is countable, taking the union over all multiplicity vectors preserves the Hausdorff-dimension upper bound and proves `(9)`.

The connected/homogeneous hypothesis matters. An affine torsion coset need not contain the origin, and a Li-shaped polynomial can in principle vanish identically on a specially arranged affine component. Non-homogeneous phase constraints therefore require a separate residue/coset analysis rather than being silently absorbed into `(6)`.

## Prior-art audit

The distance-to-zero estimate `(11)` is the classical Łojasiewicz inequality for real-analytic functions on compact sets. An authoritative summary states the form `dist(x,Z_f)^A <= C|f(x)|` on compact subsets of the analytic domain: Encyclopedia of Mathematics, **“Lojasiewicz inequality,”** https://encyclopediaofmath.org/wiki/Lojasiewicz_inequality .

Polynomial tubular-neighborhood control is classical. Richard Wongkew, **“Volumes of tubular neighbourhoods of real algebraic varieties,”** *Pacific Journal of Mathematics* 159(1) (1993), 177--184, DOI `10.2140/pjm.1993.159.177`, gives degree-controlled tube-volume bounds for real algebraic varieties; these imply the fixed-set polynomial covering estimate needed in `(15)`. Martin Lotz, **“On the volume of tubular neighborhoods of real algebraic varieties,”** *Proceedings of the American Mathematical Society* 143(5) (2015), 1875--1889, DOI `10.1090/S0002-9939-2014-12397-5`, gives a modern self-contained treatment of such bounds.

The convergence implication from `(19)` to `(20)` is the standard Hausdorff analogue of Borel--Cantelli, often called the Hausdorff--Cantelli or Hausdorff--Borel--Cantelli lemma. Victor Beresnevich's 2026 exposition **“The dimension of well approximable numbers,”** *Journal of the London Mathematical Society* (2026), explicitly states this general limsup covering lemma and notes its long-standing use in metric Diophantine approximation. The general shrinking-target dimension literature includes Richard Hill and Sanju Velani, **“The Shrinking Target Problem for Matrix Transformations of Tori,”** *Journal of the London Mathematical Society* 60 (1999), 381--398, DOI `10.1112/S0024610799007681`. Their problem concerns iterates of a fixed toral endomorphism hitting shrinking balls; `(12)` instead uses the varying multiplication maps `M_n` and a fixed analytic zero variety, so their dimension formula is not being invoked here.

AF-250 already uses Wayne Lawton's polynomial small-value estimate to prove Haar-nullity. That estimate is not needed for the dimension proof above: Łojasiewicz localization plus algebraic target geometry is enough. A targeted literature search did not locate the exact synthesis `(3)`--`(9)` for finite Keiper--Li phase modes or arbitrary output sparsification. No broad novelty is claimed; the ingredients are classical, while the derived contribution is the codimension bound and its interpretation as the exact all-sampling failure locus in the current Arithmetic Fidelity framework.

## Boundaries

**Hausdorff-small does not exclude an arithmetic point.** Equation `(4)` is a stronger genericity calibration than Haar-nullity, but even a zero-dimensional set may contain the phase vector determined by actual zeta zeros. This finding supplies no source-specific Diophantine theorem for that vector.

**No lower bound or sharp dimension is claimed.** The cancellation zero set may have dimension `k`, but the limsup set of generators that hit it exponentially accurately can be much smaller. `(4)` is an upper bound obtained from a convergence cover.

**Fixed finite mode.** The constants and algebraic target are fixed with `P`. No uniform statement is proved when the number of co-dominant modes or the polynomial itself varies with `n`.

**Connected homogeneous constraints only in `(6)`--`(9)`.** Affine cosets, disconnected subgroups, nonlinear arithmetic subvarieties, or singular measures may change the target geometry or introduce exact residue-class aliases. They require their own intrinsic analysis.

**Output sampling is still downstream of source access.** Even perfect root fidelity for every retained output does not reduce the cancellation-coherent arithmetic depth required to form a large Li coefficient.

## Research consequence

The generic multimode story now has two layers. AF-250 shows that bad phase generators have Haar measure zero; AF-251 shows that they occupy at most the dimension of the finite-mode cancellation locus and therefore lose at least one Hausdorff dimension, even after imposing any connected homogeneous toral constraint on Li phases.

This rules out a simple escape from the source-specific frontier: discovering exact integer-linear relations among the dominant Keiper phases would not, by itself, explain why exponential cancellation should be typical. The remaining useful targets are more rigid and arithmetic. One needs either a direct lower bound excluding exponential approach of the **actual** zero-derived orbit to the Li cancellation variety, or a genuinely non-homogeneous constraint whose induced locus can be proved to avoid—or force—the exceptional set.

For one dominant conjugate pair, AF-249 already identifies the needed scalar invariant as a parity-restricted exponential approximation exponent. For several pairs, AF-251 suggests the corresponding source object should be treated as a Diophantine-approximation problem to a fixed algebraic/analytic cancellation variety, with the decisive question no longer its generic size but whether zeta supplies enough arithmetic structure to certify that its specific phase vector lies outside the exponentially approximable locus.