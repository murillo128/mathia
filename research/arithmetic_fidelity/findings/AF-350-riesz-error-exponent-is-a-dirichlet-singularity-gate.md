# AF-350 — Riesz error exponents preserve Dirichlet singularity data above the error line

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-349 shows that a complete fixed-order Riesz cutoff profile is exactly recoverable, while AF-348 shows that a coarse `C^0` readout can nevertheless identify radically different sources modulo bounded error. The missing question is what the **coarse error class itself still preserves**.

It preserves the singularity data of the associated Dirichlet transform above the declared error exponent.

Fix an integer `r>=0`. For a coefficient sequence `c=(c_n)_{n>=1}` define

\[
\mathcal R_r[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^r,
\qquad X>0,
\tag{1}
\]

and suppose its Dirichlet series

\[
C(s):=\sum_{n\ge1}c_n n^{-s}
\tag{2}
\]

converges absolutely in some right half-plane. Let `theta>=0`. If

\[
\boxed{
\mathcal R_r[c](X)=O(X^\theta)
\qquad (X\to\infty),
}
\tag{3}
\]

then `C(s)` admits a holomorphic continuation to

\[
\boxed{\Re s>\theta.}
\tag{4}
\]

Indeed, in that half-plane the continuation is given by

\[
\boxed{
C(s)
=
\frac{s(s+1)\cdots(s+r)}{r!}
\int_0^\infty
\mathcal R_r[c](X)X^{-s-1}\,dX.
}
\tag{5}
\]

Consequently, if `a` and `b` have Dirichlet transforms `A` and `B` that are meromorphic on `Re s>theta`, then

\[
\mathcal R_r[a](X)-\mathcal R_r[b](X)=O(X^\theta)
\tag{6}
\]

forces

\[
\boxed{
A-B\in\operatorname{Hol}(\Re s>\theta).
}
\tag{7}
\]

So `A` and `B` have the same principal parts at every point of `Re s>theta`. The quotient that identifies Riesz profiles modulo `O(X^theta)` may erase coefficient identity, support geometry, signs, and local provenance, but it **cannot erase a Dirichlet singularity lying strictly to the right of the error line**.

Equivalently, let

\[
Q_\theta(f)=f\bmod O(X^\theta)
\tag{8}
\]

and let

\[
\Sigma_\theta(A)=A\bmod\operatorname{Hol}(\Re s>\theta)
\tag{9}
\]

record only the meromorphic singularity class in that half-plane. Then on sources for which the meromorphic continuation exists,

\[
\boxed{
Q_\theta(\mathcal R_r[a])=Q_\theta(\mathcal R_r[b])
\Longrightarrow
\Sigma_\theta(A)=\Sigma_\theta(B).
}
\tag{10}
\]

This gives the first exact calibration of the weak terminal metric exposed by AF-348--AF-349: **an `O(X^theta)` Riesz observer forgets much of the source but still retains every Dirichlet pole above `Re s=theta`.**

For the von Mangoldt discriminator this immediately becomes zero-sensitive. Put

\[
c_n:=\Lambda(n)-1.
\tag{11}
\]

For `Re s>1`,

\[
C(s)
=
-\frac{\zeta'(s)}{\zeta(s)}-\zeta(s).
\tag{12}
\]

The two poles at `s=1` cancel, while every nontrivial zero `rho` of zeta of multiplicity `m_rho` gives a pole of `(12)` with residue `-m_rho`. Therefore, for `0<=theta<1`,

\[
\boxed{
\mathcal R_r[\Lambda-1](X)=O(X^\theta)
\Longrightarrow
\zeta(s)\ne0\quad(\Re s>\theta).
}
\tag{13}
\]

If

\[
\beta:=\sup_{\zeta(\rho)=0,\ 0<\Re\rho<1}\Re\rho,
\tag{14}
\]

then every admissible Riesz error exponent satisfies

\[
\boxed{\theta\ge\beta.}
\tag{15}
\]

In particular, either of the bounds

\[
\mathcal R_r[\Lambda-1](X)=O(X^{1/2})
\tag{16}
\]

or, more weakly,

\[
\mathcal R_r[\Lambda-1](X)=O_\varepsilon(X^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0
\tag{17}
\]

implies the Riemann hypothesis, by the functional-equation symmetry of the nontrivial zeros.

No converse is claimed here. The point is not a new RH criterion; it is a fidelity theorem identifying exactly what a coarse Riesz error exponent is still capable of transmitting.

## Derivation

### 1. An `O(X^theta)` terminal bound enlarges the Mellin half-plane

AF-349 proves, initially in a half-plane of absolute convergence,

\[
\int_0^\infty
\mathcal R_r[c](X)X^{-s-1}\,dX
=
B(s,r+1)C(s),
\tag{18}
\]

where

\[
B(s,r+1)
=
\frac{r!}{s(s+1)\cdots(s+r)}.
\tag{19}
\]

Because no source term appears before `X=1`, there is no small-`X` convergence issue. Under `(3)`, the integral

\[
I(s):=
\int_1^\infty
\mathcal R_r[c](X)X^{-s-1}\,dX
\tag{20}
\]

converges absolutely and locally uniformly whenever `Re s>theta`. Hence `I` is holomorphic on that half-plane.

On the nonempty right half-plane where the original Dirichlet series is absolutely convergent, `(18)` gives

\[
C(s)=B(s,r+1)^{-1}I(s).
\tag{21}
\]

For integer `r`,

\[
B(s,r+1)^{-1}
=
\frac{s(s+1)\cdots(s+r)}{r!}
\tag{22}
\]

is a polynomial, so the right-hand side of `(21)` is holomorphic throughout `Re s>theta`. By uniqueness of analytic continuation it is the continuation of `C`, proving `(4)`--`(5)`.

This is an important directionality point. AF-349 used Mellin integration to recover a Dirichlet series where it already converged absolutely. AF-350 uses a quantitative bound on the **destination profile** to extend that recovery into a larger half-plane. The target error exponent therefore becomes an analytic-fidelity threshold.

### 2. Pairwise error equivalence preserves principal parts

Apply the previous argument to `c=a-b`. If `(6)` holds, the difference Dirichlet series `C=A-B`, initially defined in a common absolute-convergence half-plane, extends holomorphically to `Re s>theta`.

If `A` and `B` themselves have meromorphic continuations there, uniqueness identifies their meromorphic difference with this holomorphic continuation. Thus every pole and every principal-part coefficient cancels between them in that half-plane. This proves `(7)` and `(10)`.

The statement is deliberately one-way. Two Dirichlet transforms may differ by a holomorphic function on `Re s>theta` without their Riesz profiles differing by `O(X^theta)` unless additional vertical-growth or inversion hypotheses are imposed. Arithmetic Fidelity therefore gets a safe implication without smuggling in a Tauberian converse.

### 3. The von Mangoldt-minus-unit source converts the error line into a zero-free line

For `Re s>1`, the Euler product gives the classical identity

\[
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=
-\frac{\zeta'(s)}{\zeta(s)},
\tag{23}
\]

while unit mass has transform `zeta(s)`. Hence `(12)` holds.

Near `s=1`, zeta has a simple pole with residue one, and `-zeta'/zeta` also has a simple pole with residue one. Their difference in `(12)` is therefore regular at `s=1`.

At a nontrivial zero `rho` of multiplicity `m_rho`,

\[
\frac{\zeta'(s)}{\zeta(s)}
=
\frac{m_\rho}{s-\rho}+O(1),
\tag{24}
\]

so `(12)` has principal part

\[
-\frac{m_\rho}{s-\rho}.
\tag{25}
\]

Thus the only singularities of `(12)` in the open positive half-plane are exactly the nontrivial zeta zeros. If `(3)` holds for `c=Lambda-1`, theorem `(4)` says `(12)` must be holomorphic on `Re s>theta`; no such zero can lie there. This proves `(13)`--`(15)`.

For `(17)`, if a zero had real part `beta_0>1/2`, choose `epsilon` with

\[
0<\varepsilon<\beta_0-\frac12.
\tag{26}
\]

Then `(13)` applied at `theta=1/2+epsilon` would exclude that zero. Hence no zero lies to the right of the critical line. The functional equation sends every nontrivial zero `rho` to `1-rho`, so a zero to the left of the critical line would create one to the right. Therefore all nontrivial zeros lie on `Re s=1/2`.

### 4. The AF-348 perfect-power controls pass exactly because their singularity class already agrees

For the weighted perfect-`k`-power background

\[
b_k(n)=
\begin{cases}
km^{k-1},&n=m^k,\ m\ge2,\\
0,&\text{otherwise},
\end{cases}
\tag{27}
\]

AF-344 gives

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr).
\tag{28}
\]

Dense unit mass has transform `zeta(s)`, so their difference is

\[
D_k(s)
=
k\bigl(\zeta(ks-k+1)-1\bigr)-\zeta(s).
\tag{29}
\]

Each zeta factor has only one pole, and both occur at `s=1` with residue one; the pole cancels in `(29)`. Hence `D_k` is in fact entire.

AF-348 proves that for `r>=k-1`,

\[
\mathcal R_r[b_k](X)-\mathcal R_r[1](X)=O_{k,r}(1).
\tag{30}
\]

AF-350 now explains why this strong `C^0` collapse does not conflict with analytic fidelity. Bound `(30)` forces only equality of singularity classes in `Re s>0`, and `(29)` shows that those classes already agree exactly. The quotient is blind to sparse-versus-dense provenance because that provenance lives in the holomorphic remainder, not in a right-half-plane singularity.

This control is decisive for interpreting `(13)`: a bounded or small Riesz residual is not generically arithmetic-faithful. It is faithful only to the **singularity discriminator** represented at the destination.

## Relation to AF-348--AF-349

AF-348 establishes a severe loss in raw amplitude resolution: after enough fixed-order smoothing, a sparse perfect-power source and dense unit mass are only `O(1)` apart. AF-349 then proves that the full profile remains injective and exactly conditioned in a source-matched derivative-variation norm, locating the loss in the later observation metric rather than in the Riesz transform itself.

AF-350 calibrates that weak metric instead of merely declaring it lossy. Quotienting by `O(X^theta)` removes all distinctions carried only by a Dirichlet function holomorphic on `Re s>theta`, but it necessarily preserves meromorphic principal parts to the right of that line. The terminal metric therefore has a precise surviving resource:

\[
\boxed{
\text{Riesz error exponent }	heta
\quad\Longrightarrow\quad
\text{Dirichlet singularity fidelity on }\Re s>\theta.
}
\tag{31}
\]

This is exactly the kind of source-to-destination transport demanded by the current line mandate. A strong source norm need not survive. The much weaker amplitude exponent is already sufficient when the target discriminator is represented by a pole whose real part crosses the same threshold.

## Prior art and novelty assessment

No novelty claim is made for the constituent analytic-number-theory statements.

- G. H. Hardy and Marcel Riesz, *The General Theory of Dirichlet's Series*, Cambridge Tracts in Mathematics and Mathematical Physics 18, Cambridge University Press (1915), develops typical Riesz means for Dirichlet series. Hardy and Littlewood explicitly state that the Riesz contour formula they use is a special case of Hardy--Riesz Theorem 40.
- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119--196 (1916), DOI `10.1007/BF02422942`, equations (2.251)--(2.252), write the Riesz mean of the von Mangoldt coefficients as a Mellin contour integral of `-zeta'/zeta` and then as a main term plus contributions `X^rho` from the zeta zeros. This is direct classical prior art for the zero-sensitive Riesz error mechanism used in `(13)`.
- The Mellin principle used in `(20)`--`(22)` is standard: a growth bound at infinity enlarges the half-plane in which the Mellin integral converges holomorphically. AF-349 already records the exact beta-kernel identity for this Riesz profile.

The potentially useful content here is therefore not a new RH criterion. It is the **Arithmetic Fidelity organization** of the classical mechanism: the coarse target quotient from AF-348 is neither wholly faithful nor wholly destructive. It retains exactly enough information to obstruct removal of singularities above its error exponent, while the perfect-power controls demonstrate that large coefficient-level differences lying in the holomorphic remainder can still disappear at bounded-error resolution.

## Boundaries and failure modes

### The theorem is one-way

`A-B` holomorphic on `Re s>theta` does not by itself imply an `O(X^theta)` Riesz residual. Such a converse requires quantitative vertical growth, contour-shift, or Tauberian hypotheses. AF-350 does not identify holomorphic equivalence with Riesz error equivalence.

### The error metric is global asymptotic `C^0`

The hypothesis is a uniform eventual bound on the scalar cutoff profile. Sparse samples, average bounds, bounds only on a subsequence, or distributional control are different destination metrics and do not automatically provide the Mellin convergence used above.

### Singularities on the boundary are not detected

An `O(X^theta)` bound gives holomorphy only for `Re s>theta`. It says nothing by itself about singularities on `Re s=theta`. In particular, `(16)` is stronger than what RH alone is asserted to provide here; no converse or optimal boundary estimate is claimed.

### Integer Riesz order is used

The polynomial inverse beta factor `(22)` is stated for fixed integer `r>=0`, matching AF-347--AF-349. Analogous statements for noninteger order can be formulated with gamma factors but require a separate pole/zero audit.

### Principal-part fidelity is not source fidelity

Two sources with the same singularity class may remain radically different in coefficients, support, sign pattern, local concentration, or any source-matched norm. AF-348's perfect-power family is the explicit matched control. The result licenses only the discriminator actually represented by the retained singularity data.

## Consequence for Arithmetic Fidelity

AF-350 turns the AF-348--AF-349 warning into a positive transport theorem. The raw amplitude metric is too weak to recover the source, but it is **not too weak to carry every Dirichlet singularity whose real part exceeds its error exponent**.

For the prime discriminator `Lambda-1`, those surviving singularities are exactly the nontrivial zeta zeros. For the perfect-power matched controls, the corresponding difference transform is entire, so bounded-error collapse is allowed. The same terminal metric therefore separates the two cases for an exact structural reason rather than by provenance labels.

The next live question becomes sharper: seek a source/control pair and an actual RH-facing destination for which the desired arithmetic distinction appears as a singularity, boundary defect, or comparable invariant that the destination metric is forced to preserve. Source complexity is useful only when it can be priced in the final observer's own topology; AF-350 provides one exact model of that pricing.