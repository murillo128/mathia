# PL-325 — First-prime shift algebra is already public prior art; the live RH mechanism must lie beyond the single overlap operator

**Evidence:** `LITERATURE+INDEPENDENT-RECONSTRUCTION + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`

**Status:** `FIRST-PRIME-SHIFT-ALGEBRA-CLASSICALIZED + OPERATOR-NORM-SHORTCUT-CLOSED + FINITE-SCALE-CERTIFICATE-NOT-INDEPENDENTLY-ADOPTED`

## Precise claim

The most immediate next step after `PL-324` is not a new prime-lattice mechanism. In the first-prime window

\[
\frac12\log 2<a<\frac12\log 3,
\]

only the prime-power lag `b=log 2` is active in Suzuki's localized Weil form. The corresponding truncated translation operator on `L^2(-a,a)` has an exact two-edge flip decomposition

\[
C_{b,a}\cong
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\otimes I
\oplus 0,
\]

and hence

\[
\boxed{\sigma(C_{b,a})=\{-1,0,1\},\qquad \|C_{b,a}\|=1.}
\]

Both nonzero eigenspaces are infinite-dimensional. Consequently the first-prime layer is intrinsically indefinite, and its operator norm jumps from `0` to `1` as soon as `2a` crosses `log 2`; shrinking overlap does **not** make it a small bounded perturbation in operator norm.

This algebra is already stated and proved explicitly in the public `telleroutlook/weil-first-prime` project (Theorem 1 and Corollaries 1--2), together with the first-prime Legendre matrix algebra, endpoint-potential absorption, and a finite-dimensional Schur-complement certification framework. The exact flip decomposition is also independently reconstructed below directly from the same localized translation appearing in `PL-324`, so this finding does not rely on the project's computer-assisted certificate claims.

The redirect is therefore sharp: neither the `±1` reflection decomposition, its Legendre compression, nor operator-norm perturbation at the first-prime threshold is a new route. Any new RH-facing structure must use information beyond this single-step overlap algebra: for example the **signed state selected by the full Weil operator**, an aperture-uniform arithmetic sign law, or the source/endpoint-flux bridge isolated in `PL-319`--`PL-324`.

## 1. Exact reconstruction of the first-prime overlap operator

Let

\[
I_a=(-a,a),\qquad b=\log2,
\]

and assume

\[
\frac b2<a<b.
\]

(The entire first-prime window satisfies this because `(1/2)log 3 < log 2`.) Define the truncated forward shift

\[
(S_{b,a}f)(x)=\mathbf 1_{I_a}(x)\mathbf 1_{I_a}(x+b)f(x+b)
\]

and its self-adjoint symmetrization

\[
C_{b,a}=S_{b,a}+S_{b,a}^*.
\]

Split the interval into

\[
I_-=(-a,a-b),\qquad
I_0=(a-b,-a+b),\qquad
I_+=(-a+b,a).
\]

Because `b/2<a<b`, these are disjoint up to endpoints and `I_-`, `I_+` have the same positive length `2a-b`. Translation by `b` identifies `L^2(I_-)` unitarily with `L^2(I_+)`. Under

\[
L^2(I_a)=L^2(I_-)\oplus L^2(I_0)\oplus L^2(I_+),
\]

`C_{b,a}` swaps the two edge components and kills the middle component. Thus

\[
C_{b,a}\simeq
\begin{pmatrix}0&I\\ I&0\end{pmatrix}
\oplus0.
\]

For every nonzero `h in L^2(I_-)`, the symmetric and antisymmetric edge combinations are eigenvectors with eigenvalues `+1` and `-1`. The center gives the `0` eigenspace. Since each strip has positive measure, all three eigenspaces are infinite-dimensional. In particular,

\[
\|C_{b,a}\|=1
\]

for every `a>b/2`, however close `a` is to `b/2`.

Before the threshold, `2a<=b`, the two translated copies have no positive-measure overlap and `C_{b,a}=0`. Hence the operator norm has the exact discontinuity

\[
0\longrightarrow1
\]

at the first-prime event.

This is an elementary exact consequence of interval geometry. It agrees term-for-term with Theorem 1 and Corollary 2 of the audited external project.

## 2. Odd-sector specialization: the active prime channel is a reflection with both signs

`PL-324` shows that the odd Weil sector removes the archimedean Beurling--Deny obstruction and that the first arithmetic lag is exactly what destroys the modulus inequality. The flip above makes the signed structure more explicit.

Write an odd state as

\[
u(x)=f(x),\qquad u(-x)=-f(x),\qquad 0<x<a.
\]

Since `b>a` throughout the first-prime window, the `b`-correlation couples only opposite halves. With

\[
J_b f(y)=f(b-y),
\qquad b-a<y<a,
\]

one obtains directly

\[
\int_{-a}^{a-b}u(x+b)u(x)\,dx
=-\int_{b-a}^{a} f(b-y)f(y)\,dy.
\]

The map `J_b` is a self-adjoint involution on `L^2(b-a,a)`. Therefore

\[
L^2(b-a,a)=\ker(J_b-I)\oplus\ker(J_b+I),
\]

and both subspaces are infinite-dimensional. The first-prime contribution can consequently take either sign even after restricting to the RH-complete odd class.

This does **not** contradict `PL-324`. Beurling--Deny failure there concerns the nonlinear odd-modulus map `f -> |f|`; the present decomposition concerns the signed quadratic channel itself. Together they show that the first rational-prime event simultaneously introduces an indefinite reflection channel and destroys the standard order-preserving semigroup mechanism.

## 3. Why the norm jump is not itself a spectral crossing mechanism

A tempting inference would be that the norm jump forces a comparably abrupt change in the bottom Weil eigenvalue. That inference is false. Near the first-prime threshold the same overlap is small in a much stronger **form-localization** sense even though its bounded-operator norm is one.

After scaling `(-a,a)` to `(-1,1)`, let

\[
\tau=\frac{b}{a},\qquad
\varepsilon=2-\tau.
\]

The first-prime coupling lives only on the edge strips

\[
E_-=(-1,-1+\varepsilon),\qquad E_+=(1-\varepsilon,1).
\]

For the standard endpoint potential

\[
V(x)=-\frac12\log(1-x^2),
\]

one has on those strips

\[
V(x)\ge \kappa_{\rm edge}(a)
:=\frac12\log\frac1{2\varepsilon}.
\]

This lower bound is useful as a positive coercive weight only when

\[
\varepsilon<\frac12
\quad\Longleftrightarrow\quad
\tau>\frac32
\quad\Longleftrightarrow\quad
\frac b2<a<\frac{2b}{3}.
\]

In that near-threshold range,

\[
|\langle C_{\tau,1}w,w\rangle|
\le \|w\|_{L^2(E_-\cup E_+)}^2
\le \kappa_{\rm edge}(a)^{-1}\langle Vw,w\rangle.
\]

As `a downarrow b/2`, `epsilon -> 0` and `kappa_edge(a) -> infinity`. Thus the prime perturbation is **not** small in bounded-operator norm, but it becomes small relative to the endpoint coercive form. This is exactly the topology in which a continuous bottom eigenvalue can survive the first-prime event.

There is a small but important audit correction here. `docs/THEOREMS.md` states `kappa_edge(L)>0` while presenting Theorem 2 over the broader interval `b/2<L<b`. Algebraically, `kappa_edge>0` requires `epsilon<1/2`, hence `L<2b/3`. The support inequality `V>=kappa_edge` remains formally true when the right side is nonpositive, but division by `kappa_edge` then cannot give the claimed positive absorption estimate. The finite target `a=7/20` lies safely in the corrected near-threshold range, so this does not affect the project's Theorem 3 calculation; it only narrows the general range in which Theorem 2 yields coercive absorption.

Accordingly, neither side of the naive perturbative dichotomy is useful for RH:

- bounded-operator norm sees an artificial jump of size one;
- the natural closed-form topology can absorb the first-prime layer sufficiently close to threshold.

A genuine first-crossing argument must use the selected eigenstate or a source-specific signed identity, not merely the size of the overlap operator.

## 4. Prior-art audit and evidence boundary

The closest source located is the public repository

`https://github.com/telleroutlook/weil-first-prime`

at audited `main` commit

`e66f467bc4447c5b2491577cbb6c3ae0e721fb43` (12 August 2026).

Its `docs/THEOREMS.md` contains written proofs of:

- Theorem 1: the single-step flip decomposition and spectrum `{-1,0,1}`;
- Corollaries 1--2: the first-prime `log 2` sign structure and operator-norm jump;
- Theorems 2--3: endpoint-potential absorption and a rational bound at `a=7/20`, with the general positivity range correction above;
- Theorem 4: exact Legendre matrix algebra `J_ij(tau), E_ij(tau) in Q[tau]`;
- Theorem 5: a split-residual Schur criterion;
- Theorem 6: explicit negative witnesses for one weakened proof path.

A targeted search for the same first-prime overlap theorem did not locate a peer-reviewed or arXiv paper containing this exact package. The repository is therefore treated as **public contemporaneous prior art**, not as peer-reviewed authority. No broad originality claim is made for the elementary flip decomposition regardless: it follows immediately from the truncated shift geometry and has been independently checked above.

The project's stronger computer-assisted status is deliberately **not imported as Mathia evidence**. Its current README reports `FP-0.35 HOLDS` and gives a reproducible Arb/Schur script, while `docs/THEOREMS.md` still says that `FP-0.35` remains a conjecture. More importantly, the current head commit itself fixes an earlier misuse of python-flint interval construction and regenerates the certificate. This history is evidence that the certification layer must be independently replayed and audited before Mathia can use its numerical positivity margin. `PL-325` therefore relies only on the exact analytic overlap/algebra statements that can be reconstructed directly, plus the elementary corrected support estimate above.

The distinction is essential: finite-scale positivity at `a=7/20`, even if fully certified, does not imply RH, and the external project explicitly states that limitation.

## 5. Consequence for the prime-lattice line

`PL-324` remains intact: its exact odd-sector Beurling--Deny threshold and two-bump post-threshold obstruction are not supplied by the external flip theorem. What changes is the next research allocation.

The following are now low-value duplication unless they add a genuinely new theorem:

1. diagonalizing the single `log 2` overlap operator;
2. deriving its `±1` reflection sectors;
3. compressing that reflection into Legendre matrices;
4. arguing perturbatively from overlap width in bounded-operator norm;
5. proving one more isolated finite-scale positivity point without a bridge to the all-aperture RH criterion.

The live burden identified by `PL-319`--`PL-324` is more specific. One needs a mechanism that couples the **actual signed endpoint/source-selected Weil state** to the arithmetic prime-power channels strongly enough to control the first negative crossing, or an aperture-uniform theorem whose content survives beyond the finite first-prime block. The bare one-prime overlap algebra does not supply that mechanism.

## Sources

- Public research repository `telleroutlook/weil-first-prime`, audited at commit `e66f467bc4447c5b2491577cbb6c3ae0e721fb43`, especially `docs/THEOREMS.md` and `README.md`. The analytic overlap statements are independently reconstructed here; the computer-assisted `FP-0.35` certificate is not independently adopted.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2`; source 56 in `research/prime_lattice/SOURCES.md` and the localized Weil-form authority used by `PL-265` and `PL-324`.
- `PL-324`: exact odd-sector Beurling--Deny threshold at `(1/2)log2` and first-prime order obstruction.
- `PL-319`--`PL-323`: current endpoint/source-flux chain, whose analytic boundary-transfer gates are closed while the arithmetic sign/first-crossing problem remains live.
