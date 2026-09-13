# NB-101 — Local circumradius is the asymmetric three-state shear scale

**Status:** EXACT-DERIVED + CANONICAL-BLASCHKE-GEOMETRY + ASYMMETRIC-THREE-STATE-LOCAL-LAW + CIRCUMRADIUS-SHEAR-INVARIANT + FIRST-ORDER-COLLINEARITY-THRESHOLD + SOURCE-LOCAL-BOUNDARY.

## Claim

The quadratic-horizontal-tangency threshold isolated by `NB-100` is the symmetric coordinate expression of a more intrinsic three-state law.

Fix `a>0`. Let three distinct right-half-plane parameters form a regular common-scale collision

\[
\lambda_j(\varepsilon)
 = \lambda_*+\varepsilon w_j+O(\varepsilon^2),
\qquad
\lambda_*=a+i\Gamma,
\qquad j=1,2,3,
\]

as `epsilon -> 0+`, where the fixed first-order offsets `w_1,w_2,w_3` are pairwise distinct and the `O(epsilon^2)` remainders are bounded. Form the normalized Cauchy state Gram, apply the canonical sequential Blaschke deflation of `NB-095`--`NB-098`, and let `C_epsilon` be the resulting three-state Gram. After the harmless row-phase normalization of `NB-098`, write

\[
C_\varepsilon=R_\varepsilon^*R_\varepsilon,
\qquad
R_\varepsilon=
\begin{pmatrix}
1&r_{12}&r_{13}\\
0&1&r_{23}\\
0&0&1
\end{pmatrix}.
\]

Define

\[
\Delta(w)
:=w_1\overline{w_2}-w_1\overline{w_3}
-w_2\overline{w_1}+w_2\overline{w_3}
+w_3\overline{w_1}-w_3\overline{w_2},
\]

and

\[
\Pi(w):=(w_1-w_2)(w_1-w_3)(w_2-w_3).
\]

Then

\[
r_{12}=O(1),
\]

while, up to unimodular row phases,

\[
\varepsilon r_{13}
 = 2a\,\frac{\Delta(w)}{\Pi(w)}+O(\varepsilon),
\qquad
\varepsilon r_{23}
 =-2a\,\frac{\Delta(w)}{\Pi(w)}+O(\varepsilon).
\tag{1}
\]

For `w_j=x_j+i y_j`, one has

\[
|\Delta(w)|=4\,\operatorname{Area}(w_1,w_2,w_3).
\tag{2}
\]

If the normalized first-order triangle is noncollinear and `R(w)` denotes its Euclidean circumradius, the elementary identity

\[
R(w)
 =\frac{|w_1-w_2|\,|w_1-w_3|\,|w_2-w_3|}
 {4\,\operatorname{Area}(w_1,w_2,w_3)}
 =\frac{|\Pi(w)|}{|\Delta(w)|}
\]

turns (1) into

\[
|r_{13}|=|r_{23}|
 =\frac{2a}{\varepsilon R(w)}+O(1).
\tag{3}
\]

Equivalently, if `R_epsilon` is the circumradius of the actual triangle with vertices `lambda_1(epsilon),lambda_2(epsilon),lambda_3(epsilon)`, then in the noncollinear first-order regime

\[
R_\varepsilon=\varepsilon R(w)+O(\varepsilon^2)
\]

and

\[
|r_{13}|=|r_{23}|=\frac{2a}{R_\varepsilon}+O(1).
\tag{4}
\]

Hence a regular noncollinear first-order collision satisfies

\[
\boxed{
\kappa_2(C_\varepsilon)=\Theta(\varepsilon^{-4}).
}
\tag{5}
\]

If instead `w_1,w_2,w_3` are collinear, the `epsilon^{-1}` coefficients in (1) vanish. Under the same pairwise-distinct first-order hypothesis, all three off-diagonal Cholesky entries remain `O(1)`, and therefore

\[
\boxed{
\kappa_2(C_\varepsilon)=O(1).
}
\tag{6}
\]

Thus, for regular three-state collisions with distinct first-order offsets, **bounded canonical conditioning is equivalent to first-order affine collinearity**. The singular scale is inverse local circumradius. The special `NB-100` phrase “quadratic horizontal tangency” is not the invariant itself; it is what first-order collinearity becomes on that symmetric vertical slice.

The leading invariant is order-independent in magnitude. Both `Delta` and the Vandermonde factor `Pi` are alternating under a relabeling of the three states, so their ratio, and hence `|Delta/Pi|=1/R(w)`, is permutation-invariant. Individual triangular coefficients acquire order-dependent phases/signs, but the divergent scale and the conditioning conclusion do not.

## Derivation

### 1. Start from the exact canonical factorization

`NB-098` gives the exact factorization needed here. For ordered distinct right-half-plane parameters `lambda_1,lambda_2,lambda_3`, set

\[
a_j=\Re \lambda_j,
\qquad
G_{rs}=\frac{2\sqrt{a_ra_s}}
 {\lambda_r+\overline{\lambda_s}}.
\]

The normalized Cauchy Gram factors as `G=Q^*Q`, with

\[
Q_{jk}
=
\frac{2\sqrt{a_ja_k}}
 {\lambda_j+\overline{\lambda_k}}
\prod_{\ell<j}
\frac{\overline{\lambda_k}-\overline{\lambda_\ell}}
 {\overline{\lambda_k}+\lambda_\ell},
\qquad j\le k.
\]

For the canonical sequential deflation matrix `T`,

\[
T_{kk}
=
\prod_{\ell<k}
\frac{\lambda_k+\overline{\lambda_\ell}}
 {\lambda_k-\lambda_\ell},
\]

and for `r<k`,

\[
T_{rk}
=-\frac{2\sqrt{a_ra_k}}
 {\lambda_k-\lambda_r}
\prod_{\substack{\ell<k\\ \ell\ne r}}
\frac{\lambda_r+\overline{\lambda_\ell}}
 {\lambda_r-\lambda_\ell}.
\]

Putting `M=QT` gives `C=M^*M`. Every diagonal entry of `M` has modulus one. Multiplying rows by phases therefore produces the positive-diagonal Cholesky factor `R` without changing the magnitudes of the off-diagonal entries or the singular values.

A common imaginary translation `lambda_j -> lambda_j+i Gamma` is an exact gauge for these formulas: pairwise differences are unchanged, while every `lambda_r+bar(lambda_s)` is unchanged. We may therefore set `Gamma=0` during the local expansion and restore it afterward.

### 2. Expand a general regular triple, not a symmetric slice

Write

\[
\lambda_j=a+\varepsilon w_j+O(\varepsilon^2),
\qquad
\overline{\lambda_j}
 =a+\varepsilon\overline{w_j}+O(\varepsilon^2).
\]

Because the first-order offsets are pairwise distinct,

\[
\lambda_j-\lambda_k
 =\varepsilon(w_j-w_k)+O(\varepsilon^2),
\]

with denominators uniformly comparable to `epsilon` for small `epsilon`. Consequently the exact rational formulas above admit ordinary Laurent expansion with bounded remainder after the displayed singular term is removed.

Direct substitution and cancellation give

\[
\varepsilon M_{13}
\longrightarrow
2a\,
\frac{
 w_1\overline{w_2}-w_1\overline{w_3}
-w_2\overline{w_1}+w_2\overline{w_3}
+w_3\overline{w_1}-w_3\overline{w_2}
}
{(w_1-w_2)(w_1-w_3)(w_2-w_3)},
\tag{7}
\]

and

\[
\varepsilon M_{23}
\longrightarrow
-2a\,
\frac{
 w_1\overline{w_2}-w_1\overline{w_3}
-w_2\overline{w_1}+w_2\overline{w_3}
+w_3\overline{w_1}-w_3\overline{w_2}
}
{(w_1-w_2)(w_1-w_3)(w_2-w_3)}.
\tag{8}
\]

The same substitution gives `M_12=O(1)`. Equations (7)--(8) are exactly (1) before row-phase normalization.

The numerator is translation-invariant in the `w_j`; so is the denominator. Thus the singular invariant depends only on the first-order triangle, not on its location.

### 3. The numerator is oriented area

Let `w_j=x_j+i y_j`. Rearranging the numerator gives

\[
\Delta(w)
=2i\,\Im\!\left(
 (w_2-w_1)\overline{(w_3-w_1)}
\right)
\]

up to the orientation sign determined by the chosen ordering. Therefore

\[
|\Delta(w)|
=2\left|
\Im\!\left(
 (w_2-w_1)\overline{(w_3-w_1)}
\right)
\right|
=4\,\operatorname{Area}(w_1,w_2,w_3).
\]

The denominator magnitude is exactly the product of the three side lengths. Hence

\[
\left|\frac{\Delta(w)}{\Pi(w)}\right|
=\frac{4\operatorname{Area}}
 {|w_1-w_2|\,|w_1-w_3|\,|w_2-w_3|}
=\frac1{R(w)}.
\]

This is the promised coordinate-free local form of the collective shear.

### 4. Convert Cholesky shear into Gram conditioning

After phase normalization,

\[
R_\varepsilon=
\begin{pmatrix}
1&x_\varepsilon&y_\varepsilon\\
0&1&z_\varepsilon\\
0&0&1
\end{pmatrix},
\]

where `x_epsilon=O(1)` and, if `Delta(w) != 0`, both `|y_epsilon|` and `|z_epsilon|` are `Theta(epsilon^{-1})`. Therefore

\[
\|R_\varepsilon\|_2=\Theta(\varepsilon^{-1}).
\]

Its inverse is

\[
R_\varepsilon^{-1}
=
\begin{pmatrix}
1&-x_\varepsilon&x_\varepsilon z_\varepsilon-y_\varepsilon\\
0&1&-z_\varepsilon\\
0&0&1
\end{pmatrix}.
\]

The explicit `-z_epsilon` entry gives the lower bound

\[
\|R_\varepsilon^{-1}\|_2
\gg \varepsilon^{-1},
\]

while the displayed formula and `x_epsilon=O(1)` give the matching upper bound. Hence

\[
\kappa_2(R_\varepsilon)=\Theta(\varepsilon^{-2}).
\]

Since `C_epsilon=R_epsilon^* R_epsilon`,

\[
\kappa_2(C_\varepsilon)
=\kappa_2(R_\varepsilon)^2
=\Theta(\varepsilon^{-4}).
\]

If `Delta(w)=0`, the singular coefficients in both `M_13` and `M_23` vanish. Pairwise distinctness of the `w_j` keeps every difference denominator on the same `Theta(epsilon)` scale, so the next Laurent coefficient is finite. Thus all entries of `R_epsilon` and `R_epsilon^{-1}` remain bounded and (6) follows.

## Recovery of NB-098 and NB-100

The transverse synthetic packet of `NB-098` is

\[
w_1=i,
\qquad
w_2=c,
\qquad
w_3=-i.
\]

Its normalized triangle has circumradius

\[
R(w)=\frac{1+c^2}{2|c|}.
\]

Equation (3) therefore gives

\[
|r_{13}|,|r_{23}|
=\frac{4a|c|}{1+c^2}\frac1\varepsilon+O(1),
\]

which is exactly the singular coefficient found in `NB-098`.

For the symmetric two-parameter slice of `NB-100`,

\[
\lambda_1=a+i\varepsilon,
\qquad
\lambda_2=a+\delta,
\qquad
\lambda_3=a-i\varepsilon,
\]

a path with `delta=c epsilon+o(epsilon)` has the noncollinear first-order triangle above and therefore quartic blow-up. A path with

\[
\delta=O(\varepsilon^2)
\]

has first-order offsets `i,0,-i`, which are collinear, so the `epsilon^{-1}` shear disappears and conditioning stays bounded. Thus the sharp quadratic tangency threshold of `NB-100` is recovered immediately from first-order collinearity.

The exact `NB-100` scalar

\[
L_a(\delta,\varepsilon)
=\frac{|a\delta-\varepsilon^2|}
 {\delta^2+\varepsilon^2}
\]

contains more finite information inside the bounded regime. For the physical symmetric triangle,

\[
R_{\rm phys}
=\frac{\delta^2+\varepsilon^2}{2|\delta|}.
\]

Hence the divergent part of `L_a` is the same inverse-circumradius scale `a/R_phys`; the `-epsilon^2` term controls the bounded correction when the first-order triangle has already collapsed to a line. `NB-101` therefore generalizes the singular geometry without replacing the sharper exact symmetric formula.

## Source interpretation

For a hypothetical off-critical zeta zero `rho=beta+i gamma`, the Blaschke state parameter is `lambda=rho-1/2`. Consequently a regular shrinking triple of off-critical states may be viewed in the ordinary `(beta-1/2,gamma)` plane.

`NB-101` says that the canonical state system does **not** require the three points to approach on a vertical line in order to remain well conditioned. At first order it only requires their normalized displacement triangle to flatten onto *some* affine line. A genuinely two-dimensional first-order packet has nonzero normalized area, finite normalized circumradius, and necessarily produces the `epsilon^{-4}` Gram-conditioning blow-up.

This sharpens the source theorem requested after `NB-099`--`NB-100`. A rescue based on the actual zeros of zeta would need, for every relevant regular near-confluent off-critical triple, a source-specific mechanism forcing asymptotic first-order collinearity, or at least forcing the physical inverse circumradius to stay bounded. Absolute height, quartet completion, simplicity, and sparse global zero counts were already shown insufficient by `NB-099`; `NB-101` now identifies the local geometric quantity they fail to control.

Nothing here proves that actual zeta-zero triples realize a bad packet. Equally, nothing known in this line supplies the required collinearity law. The result converts the previous coordinate question “why should horizontal bending be quadratic?” into the invariant question “why should regular local off-critical zero packets have vanishing normalized area?”

## Prior-art boundary

A targeted audit was made against the closest model-space and Nyman/Blaschke literature rather than treating the Cauchy/Takenaka--Malmquist algebra as novel.

- Fricain, *Bases of reproducing kernels in model spaces* (J. Operator Theory 46, 2001), studies Riesz-basis criteria and stability of reproducing-kernel systems under perturbation.
- Baranov, *Stability of the bases and frames reproducing kernels in model spaces* (Ann. Inst. Fourier 55, 2005), studies perturbative stability for kernel bases and frames in half-plane model spaces.
- Baranov--Hartmann--Kellay, *Geometry of reproducing kernels in model spaces near the boundary* (JMAA 447, 2017), studies Riesz/minimal/overcomplete kernel geometry near model-space boundaries.
- Ziad, *A Gram-Spectral Autopsy of the BNBD Inversion Problem* (2026), is the closest current BNBD comparison located in this line and explicitly separates a Blaschke skeleton from the arithmetic Gram defect.

Those sources cover the broad kernel/model-space geometry in which this calculation lives. The targeted search did **not** locate the specific canonical-deflation three-state asymptotic (7)--(8), its circumradius reduction, or the first-order-collinearity dichotomy stated here. This is a boundary statement, not a priority claim. No external theorem is load-bearing in the derivation, so `SOURCES.md` requires no new dependency entry for this finding.

## Failure modes and scope

1. **Regular collision only.** The theorem assumes the three first-order offsets are pairwise distinct. If two offsets coincide, one pair collides on a finer scale than the others. Then `Pi(w)=0`, the common-scale Laurent expansion is not the correct normal form, and the packet must be rescaled hierarchically or treated by a confluent/Jordan analysis.

2. **Fixed positive horizontal base.** The constants are local for fixed `a>0`. A simultaneous `a -> 0` limit, relevant to states themselves approaching the critical boundary, is not covered by the stated asymptotics.

3. **Distinct zeros, not multiplicity.** A genuine multiple zero is not obtained by silently identifying distinct simple-state formulas. It requires derivative/Jordan states, as already noted in `NB-098`--`NB-100`.

4. **State conditioning, not target error.** The conclusion concerns the canonical Blaschke/Cauchy state Gram. It does not by itself give a Nyman target-distance lower or upper bound, a normalized correlation-entropy theorem, or an RH implication.

5. **Collinearity is first-order only.** When the first-order triangle is collinear, second-order geometry controls the finite bounded Cholesky coefficients. `NB-100` is an example: its exact `a delta-epsilon^2` numerator resolves that next order on one symmetric slice.

## Falsification tests

The claim has several cheap exact checks.

- Substitute `w_1=i`, `w_2=c`, `w_3=-i` into (7)--(8). The coefficient magnitude must reduce to `4a|c|/(1+c^2)`, matching `NB-098`.
- Take `w_1=i`, `w_2=0`, `w_3=-i`. The numerator `Delta(w)` must vanish, matching the bounded parabolic regime of `NB-100`.
- Choose a generic noncollinear triple, for example `w_1=0`, `w_2=1`, `w_3=i`. Expanding the exact `Q,T` formulas numerically or symbolically must give `epsilon M_13 -> 2a Delta/Pi` and `epsilon M_23 -> -2a Delta/Pi`.
- Relabel the three offsets. The magnitude `|Delta/Pi|` must remain unchanged, because it equals inverse circumradius.
- For any fixed collinear pairwise-distinct triple, direct evaluation of the exact matrices for decreasing `epsilon` must show bounded `kappa_2(C_epsilon)` rather than an `epsilon^{-4}` law.

A failure of any of these tests invalidates the claimed invariant reduction. A nested collision with coincident first-order offsets is outside the theorem rather than a counterexample.

## Consequence for the research line

`NB-098` showed that collective three-state shear is real and order-independent. `NB-099` showed that generic zeta symmetries and global sparsity do not remove it. `NB-100` found the exact quadratic tangency threshold on one symmetric slice. `NB-101` now identifies the coordinate-free regular-triple invariant:

\[
\boxed{
\text{singular collective shear}
\quad\Longleftrightarrow\quad
\text{nonzero first-order triangle area}
\quad\Longleftrightarrow\quad
R(w)<\infty.
}
\]

The next source-specific question is therefore substantially narrower. For actual hypothetical off-critical zeta zeros, can one prove a local law that forces regular shrinking triples to become first-order collinear, equivalently that their physical inverse circumradius remains bounded? If no such law is plausible or accessible, the canonical three-state representation has reached a genuine source-geometry boundary and the line should shift toward a representation or target conversion that does not require uniform local conditioning.
