# NB-100 — quadratic horizontal tangency is the local three-state shear threshold

**Status:** `EXACT-DERIVED + CANONICAL-BLASCHKE-GEOMETRY + THREE-STATE-LOCAL-LAW + QUADRATIC-TANGENCY-THRESHOLD + CONDITIONING-CLASSIFICATION + SOURCE-LOCAL-BOUNDARY`.

`NB-098` exhibits a transverse three-state collision with canonical Cholesky shear of size `epsilon^(-1)` and Gram condition number of size `epsilon^(-4)`. `NB-099` then shows that height, quartet symmetry, simplicity, and arbitrarily strong global sparsity do not exclude that geometry. The remaining source-specific question is local: **how much horizontal bending can a near-colliding three-zero packet tolerate before the canonical state system becomes singular?**

On the symmetric three-state slice used by `NB-098`, that threshold is exact. Fix `a>0` and let

\[
\lambda_1=a+i\varepsilon,
\qquad
\lambda_2=a+\delta,
\qquad
\lambda_3=a-i\varepsilon,
\tag{1}
\]

with `epsilon>0`, `delta in R`, `a+delta>0`, and `(delta,epsilon)->(0,0)`. Let `C_(epsilon,delta)` be the canonically deflated normalized half-line state Gram of `NB-095`--`NB-098`. Define the local bending parameter

\[
L_a(\delta,\varepsilon)
:=
\frac{|a\delta-\varepsilon^2|}
     {\delta^2+\varepsilon^2}.
\tag{2}
\]

Then, uniformly in a sufficiently small fixed neighborhood of the collision,

\[
\boxed{
\kappa_2(C_{\varepsilon,\delta})
\asymp_a
\bigl(1+L_a(\delta,\varepsilon)\bigr)^4.
}
\tag{3}
\]

Consequently, along any true collision `delta(epsilon)->0`,

\[
\boxed{
\sup \kappa_2(C_{\varepsilon,\delta(\varepsilon)})<\infty
\quad\Longleftrightarrow\quad
\delta(\varepsilon)=O(\varepsilon^2).
}
\tag{4}
\]

Thus the linear transverse path of `NB-098` is not merely one bad example. In this canonical slice, **bounded collective conditioning requires quadratic horizontal tangency to the common vertical line**. A local zeta theorem capable of rescuing this representation would therefore need genuinely second-order control, or else a different representation/target argument.

## 1. Exact substitution in the three-state triangular factor

Use the order displayed in `(1)`. `NB-098` factors the raw normalized Cauchy Gram as `G=Q^*Q`, writes the canonical deflation matrix as `T`, and sets

\[
M=QT,
\qquad
C_{\varepsilon,\delta}=M^*M.
\tag{5}
\]

Every diagonal entry of `M` has modulus one, so row-phase normalization turns `M` into the positive-diagonal Cholesky factor `R` of `C` without changing any entry magnitude.

The formulas of `NB-098` were written with `delta=c epsilon`. Substituting instead

\[
c=\frac{\delta}{\varepsilon}
\tag{6}
\]

without assuming that the ratio stays bounded gives the exact expressions

\[
M_{12}
=
-\frac{4i\varepsilon\sqrt{a(a+\delta)}}
{(\delta-i\varepsilon)(2a+\delta+i\varepsilon)},
\tag{7}
\]

and

\[
M_{23}
=
\frac{
4\sqrt{a(a+\delta)}(a\delta-\varepsilon^2)
(2a+\delta-i\varepsilon)
}
{
(\delta^2+\varepsilon^2)(a+i\varepsilon)
(2a+\delta+i\varepsilon)
}.
\tag{8}
\]

Taking absolute values cancels the final reflected factor exactly:

\[
\boxed{
|M_{23}|
=
\frac{4\sqrt{a(a+\delta)}}{\sqrt{a^2+\varepsilon^2}}
L_a(\delta,\varepsilon).
}
\tag{9}
\]

Hence `|M_(23)| asy_a L_a` throughout a sufficiently small collision neighborhood. Meanwhile `(7)` gives the uniform bound

\[
|M_{12}|\ll_a 1.
\tag{10}
\]

The remaining third-column entry is

\[
M_{13}
=
-\frac{2a\,P_a(\delta,\varepsilon)}
{(\delta^2+\varepsilon^2)(a+i\varepsilon)
(2a+\delta+i\varepsilon)},
\tag{11}
\]

where

\[
\begin{aligned}
P_a(\delta,\varepsilon)
={}&4a^2\delta+4a\delta^2+\delta^3-4a\varepsilon^2\\
&-i\delta^2\varepsilon-3\delta\varepsilon^2-i\varepsilon^3.
\end{aligned}
\tag{12}
\]

Separate the same local bending numerator:

\[
P_a(\delta,\varepsilon)
=
4a(a\delta-\varepsilon^2)+E_a(\delta,\varepsilon),
\tag{13}
\]

with

\[
E_a
=4a\delta^2+\delta^3-i\delta^2\varepsilon
-3\delta\varepsilon^2-i\varepsilon^3.
\tag{14}
\]

For `|delta|+epsilon` small,

\[
|E_a(\delta,\varepsilon)|
\ll_a \delta^2+\varepsilon^2,
\tag{15}
\]

while the two nonquadratic denominator factors in `(11)` stay bounded above and away from zero. Therefore

\[
\boxed{
|M_{13}|\ll_a 1+L_a(\delta,\varepsilon).
}
\tag{16}
\]

No asymptotic assumption on `delta/epsilon` is used in `(7)`--`(16)`.

## 2. The local bending parameter completely controls conditioning

After row-phase normalization write

\[
R=
\begin{pmatrix}
1&x&y\\
0&1&z\\
0&0&1
\end{pmatrix}.
\tag{17}
\]

Equations `(9)`, `(10)`, and `(16)` give

\[
|x|\ll_a1,
\qquad
|z|\asymp_a L_a,
\qquad
|y|\ll_a1+L_a.
\tag{18}
\]

Thus

\[
\|R\|_2\asymp_a1+L_a.
\tag{19}
\]

The inverse is explicit,

\[
R^{-1}
=
\begin{pmatrix}
1&-x&xz-y\\
0&1&-z\\
0&0&1
\end{pmatrix}.
\tag{20}
\]

Since `x=O_a(1)` and `y,z=O_a(1+L_a)`, its entries are all `O_a(1+L_a)`. Conversely `(R^(-1))_(23)=-z`, so

\[
\|R^{-1}\|_2\asymp_a1+L_a.
\tag{21}
\]

Because `C=R^*R`,

\[
\kappa_2(C)
=\kappa_2(R)^2
=
\bigl(\|R\|_2\|R^{-1}\|_2\bigr)^2,
\tag{22}
\]

and `(19)`--`(21)` prove `(3)`.

This also isolates where the singularity sits. Pairwise canonical interaction stays bounded, as in `NB-097`; the entire divergent scale is carried by the third-column collective coefficient `(9)`, measured by one scalar `L_a`.

## 3. Quadratic tangency is necessary and sufficient

Assume now `delta->0` and `epsilon->0`. If

\[
\delta=O(\varepsilon^2),
\tag{23}
\]

then the numerator of `(2)` is `O_a(epsilon^2)` and the denominator is at least `epsilon^2`, so `L_a=O_a(1)`. Equation `(3)` gives bounded conditioning.

Conversely, suppose `L_a<=K`. Then

\[
|a\delta-\varepsilon^2|
\le K(\delta^2+\varepsilon^2),
\tag{24}
\]

so

\[
a|\delta|
\le (K+1)\varepsilon^2+K\delta^2.
\tag{25}
\]

Once `|delta|` is small enough that `K|delta|<=a/2`, the quadratic term can be absorbed into the left side and

\[
|\delta|
\le \frac{2(K+1)}a\,\varepsilon^2.
\tag{26}
\]

This proves `(4)`.

Two matched controls make the threshold concrete. The transverse path of `NB-098`, `delta=c epsilon` with fixed `c!=0`, has

\[
L_a
=
\frac{a|c|}{1+c^2}\,\varepsilon^{-1}+O(1),
\tag{27}
\]

and hence recovers

\[
\kappa_2(C)=\Theta_{a,c}(\varepsilon^{-4}).
\tag{28}
\]

By contrast, every parabolic path

\[
\delta=k\varepsilon^2
\tag{29}
\]

with fixed real `k` has

\[
L_a\longrightarrow |ak-1|,
\tag{30}
\]

so the full three-state condition number remains bounded. At the distinguished curvature `k=1/a`, the exact coefficient `(9)` even vanishes to leading order, although the other bounded pairwise coefficients need not vanish.

Thus the transition is not between vertical collision and nonvertical collision. It is between **first-order transverse bending** and **second-order horizontal tangency**.

## 4. Consequence for the actual-zeta route

`NB-099` left a qualitative requirement: any source-specific rescue of the canonical state representation must constrain local tuples `(beta_r-1/2,gamma_r)` rather than only their global count. The present calculation makes one slice of that requirement quantitative.

If actual right-half zeros could contain arbitrarily small three-point packets whose outer members have essentially the same horizontal displacement and whose middle horizontal displacement from that outer value is larger than the square of the local ordinate half-gap, the canonical three-state conditioning would become unbounded along such packets. On the exact symmetric slice `(1)`, the required source law is precisely

\[
|\Delta\beta_{\rm middle}|
=O((\Delta\gamma)^2).
\tag{31}
\]

This is far stronger than simplicity and is not implied by any global zero-density estimate. Conversely, on this slice quadratic tangency is enough to neutralize the collective shear even though all three states genuinely coalesce.

The finding does **not** assert that zeta zeros admit the symmetric geometry `(1)`, nor that `(31)` is the correct invariant for a fully asymmetric triple. Its value is that the previously vague phrase "local zero geometry" now has an exact falsifiable threshold in the minimal bad family. The next geometric extension is to derive the corresponding invariant for a general near-confluent triple; the alternative remains to bypass this conditioning problem through a target-aware conversion.

## 5. Prior-art and novelty boundary

The Cauchy/Takenaka--Malmquist factorization underlying `M=QT` is classical, and no novelty is claimed for that machinery. Classical Hardy-space interpolation theory also makes separation of normalized kernels central to unconditional/Riesz behavior, so the general fact that crowded kernel systems can be badly conditioned is not new. The closest Nyman-specific contemporary source remains T. A. Ziad, *A Gram-Spectral Autopsy of the BNBD Inversion Problem* (2026), already anchored in `SOURCES.md`; it separates a finite Blaschke skeleton from the arithmetic projection defect but does not provide the canonical three-state threshold `(2)`--`(4)`.

A targeted literature audit also checked work on Takenaka--Malmquist systems, confluent/multiple-point Hardy-space constructions, and local spacing of zeta zeros. No located source states the scale law `(3)` or an unconditional zeta theorem coupling horizontal displacement to the square of a neighboring ordinate gap in the off-critical geometry needed here. This is only a bounded novelty audit, not a priority claim. No external theorem is load-bearing in the derivation, so `SOURCES.md` does not need a new anchor.

## 6. Boundary conditions and falsification tests

The classification `(3)` is for the exact symmetric slice `(1)` with fixed `a>0`. It is not yet a coordinate-free law for arbitrary triples whose three real parts and two adjacent ordinate gaps all vary independently. A generalization that produces a different invariant would refine, not contradict, the present result.

The constants implicit in `asymp_a` are local in `a`: the analysis assumes the collision remains inside a fixed compact subset of the open right half-plane. It does not describe a simultaneous limit `a->0`, where the zero approaches the critical line and the state normalization changes scale.

The simplest falsification test is algebraic: substitute `c=delta/epsilon` into the exact entries `(13)`--`(16)` of `NB-098`. Equation `(8)` must follow exactly, and `(12)`--`(14)` must reproduce the exact `M_(13)` numerator. Any sign or scaling failure there invalidates the threshold. A second matched test is to compare the two regimes `delta=c epsilon` and `delta=k epsilon^2`; they must respectively recover quartic blow-up and bounded conditioning.

## Consequence

The canonical three-state obstruction is now sharper than "crowded off-critical zeros may be bad." On its minimal symmetric slice, its condition number is controlled by the explicit second-order bending ratio `(2)`, and boundedness is equivalent to quadratic horizontal tangency. Therefore a source-specific continuation of the current canonical representation needs a genuinely local second-order law for off-critical zero geometry, or must change the representation/target conversion rather than trying to extract such a law from global zero counts.