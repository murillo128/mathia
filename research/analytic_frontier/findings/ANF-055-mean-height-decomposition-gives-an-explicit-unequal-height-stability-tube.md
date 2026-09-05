# ANF-055 — mean-height decomposition gives an explicit unequal-height stability tube

**Status:** `EXACT-DERIVED + QUANTITATIVE-DIAGONAL-TUBE + HEIGHT-MISMATCH-DECOMPOSITION + GLOBAL-HORIZONTAL-CLOSURE + STRUCTURAL-REDUCTION`. `ANF-054` proves that the two-pair five-point defect is strictly positive on the exact equal-height diagonal whenever the curvature gate `m_5(J)>=0`, but it leaves the neighboring unequal-height tube only qualitatively open by compactness. The present finding makes that tube explicit. Around the mean height, the unequal-height defect is the equal-height defect plus a positive quadratic mismatch block and exactly two mismatch correlation channels. Elementary hyperbolic bounds then give a global, all-horizontal lower bound depending only on the support radius, the second spectral moment and the relative height mismatch.

Let `J` be nonzero, continuous, even and nonnegative, supported in `[-B,B]` with `B>0`, and put

\[
K_J(t)=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad
K_0=K_J(0)>0,
\]

\[
m_5(J)=2K_0+3\inf_tK_J(t).
\tag{1}
\]

Assume

\[
\boxed{m_5(J)\ge0.}
\tag{2}
\]

For arbitrary genuine heights `y_1,y_2>0`, define their mean and half-mismatch by

\[
y:=\frac{y_1+y_2}{2}>0,
\qquad
\delta:=\frac{|y_1-y_2|}{2},
\qquad
q:=\frac{\delta}{y}\in[0,1).
\tag{3}
\]

Define also

\[
\boxed{
c_J:=\frac{8\pi^2}{3}
\left(1+\frac{m_5(J)}{K_0}\right)
\left(
1-\sqrt{\frac{3}{8\left(1+m_5(J)/K_0\right)}}
\right).
}
\tag{4}
\]

Then for every horizontal placement `t_1,t_2 in R`, the exact two-pair defect satisfies

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge
K_0y^2\left[
c_J
-4\pi^2q(2+q)
\cosh(2\pi By)\cosh(2\pi Bqy)
\right].
}
\tag{5}
\]

Consequently the whole common-translation variable and the whole relative-horizontal variable are safe whenever

\[
\boxed{
4\pi^2q(2+q)
\cosh(2\pi By)\cosh(2\pi Bqy)
<c_J.
}
\tag{6}
\]

Thus `ANF-054` does not merely remove the codimension-one set `y_1=y_2`: it extends to an explicit open unequal-height tube at every finite mean height. Since `m_5>=0`, one may drop the profile-specific excess and use the universal constant

\[
\boxed{
c_*:=\frac{8\pi^2}{3}\left(1-\sqrt{\frac38}\right)
=10.2019485\ldots,}
\tag{7}
\]

so condition (6) remains valid with `c_J` replaced by `c_*` for every spectrum passing the curvature gate.

## 1. Mean height diagonalizes the symmetric and antisymmetric mismatch channels

Retain the notation of `ANF-042`. Put

\[
d=t_1-t_2,
\qquad
m=\pi\alpha(t_1+t_2),
\qquad
C=\cos(\pi\alpha d),
\qquad
S=\sin(\pi\alpha d).
\tag{8}
\]

Choose a signed half-mismatch `Delta=(y_1-y_2)/2`, so `|Delta|=delta`, and set

\[
u=2\pi\alpha y,
\qquad
v=2\pi\alpha\Delta.
\tag{9}
\]

For

\[
a=\cosh(2\pi\alpha y_1)-1,
\qquad
b=\cosh(2\pi\alpha y_2)-1,
\]

the sum and difference amplitudes in `ANF-042` become

\[
\boxed{
\frac{a+b}{2}=\cosh u\cosh v-1,
\qquad
\frac{a-b}{2}=\sinh u\sinh v.
}
\tag{10}
\]

The `ANF-042` frequency integrand is

\[
h_\alpha
=p^2C^2+q_h^2S^2+4pC^2+pC\cos m-q_hS\sin m,
\tag{11}
\]

where here `p=a+b` and `q_h=a-b` (the subscript avoids confusion with the relative mismatch `q` in (3)). Let `h_\alpha^{\rm diag}` denote the same expression after replacing both heights by their mean `y`, while keeping exactly the same `t_1,t_2`. Direct substitution of (10) gives the exact identity

\[
\boxed{
\begin{aligned}
h_\alpha-h_\alpha^{\rm diag}
={}&4\sinh^2v\bigl(\sinh^2u+C^2\bigr)\\
&+2\cosh u\,(\cosh v-1)C\cos m\\
&-2\sinh u\sinh v\,S\sin m.
\end{aligned}
}
\tag{12}
\]

The first line is nonnegative and quadratic in the height mismatch. The second line is also even in the mismatch and begins at order `v^2`. **The only first-order mismatch channel is the final antisymmetric term**

\[
-2\sinh u\sinh v\,S\sin m,
\tag{13}
\]

which couples height imbalance to relative anti-phase through `S` and to common translation through `sin m`. This identifies precisely how a putative unequal-height zero can leave the globally positive diagonal of `ANF-054`.

Equation (12) is also a useful audit of the symmetry. At `Delta=0`, every mismatch term vanishes. Swapping the two conjugate pairs reverses both the signed mismatch and the relative horizontal orientation, leaving the physical defect unchanged.

## 2. The mismatch loss is controlled by the second spectral moment

Discard the positive first line of (12) and bound the two correlation lines in absolute value. For real `x`,

\[
|\sinh x|\le |x|\cosh x,
\tag{14}
\]

and

\[
\cosh x-1
\le\frac{x^2}{2}\cosh x.
\tag{15}
\]

The second inequality follows, for `x>=0`, from

\[
\cosh x-1=\int_0^x\sinh s\,ds
\le\int_0^x s\cosh x\,ds,
\]

and evenness handles negative `x`.

Using `|C|,|S|,|cos m|,|sin m|<=1`, equations (12)--(15) give the pointwise bound

\[
\begin{aligned}
h_\alpha-h_\alpha^{\rm diag}
&\ge
-2\cosh|u|(\cosh|v|-1)
-2\sinh|u|\sinh|v|\\
&\ge
-\cosh|u|\cosh|v|\bigl(v^2+2|uv|\bigr)\\
&=
\boxed{
-4\pi^2\alpha^2\delta(2y+\delta)
\cosh(2\pi|\alpha|y)
\cosh(2\pi|\alpha|\delta).
}
\end{aligned}
\tag{16}
\]

Integrating against `J>=0` and using `|alpha|<=B` on its support yields

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge
H_J(y,y;t_1,t_2)
-4\pi^2K_0\delta(2y+\delta)
\cosh(2\pi By)\cosh(2\pi B\delta).
}
\tag{17}
\]

The important feature is that the perturbation cost is paid by the **same second spectral moment `K_0`** that controls the diagonal curvature margin. No zeroth-moment `F(0)` loss is needed. This is much stronger near the diagonal than a black-box uniform-continuity estimate or a direct `L^1` bound on the Fourier--Laplace kernel.

## 3. The curvature margin pays for the entire explicit tube

`ANF-054` proves for every mean height `y>0` and every horizontal placement

\[
H_J(y,y;t_1,t_2)
\ge
\frac{8\pi^2y^2}{3}(K_0+m_5)
\left(
1-\sqrt{\frac{3K_0}{8(K_0+m_5)}}
\right).
\tag{18}
\]

Factoring out `K_0y^2` gives precisely `c_J` from (4). Substituting (18) into (17), then writing `delta=qy`, proves (5). Condition (6) follows immediately.

The left side of (6) is strictly increasing in `q>=0` for fixed `y,B`. Therefore each finite mean height has a unique positive threshold `q_*(y)` determined by

\[
4\pi^2q_*(2+q_*)
\cosh(2\pi By)\cosh(2\pi Bq_*y)
=c_J,
\tag{19}
\]

and every physical shape with `q<min(1,q_*(y))` is strictly safe. A zero must satisfy `q>=q_*(y)` whenever `q_*(y)<1`, and a negative defect must satisfy the strict inequality `q>q_*(y)`.

For calibration, as `By->0`, the universal curvature-gate threshold tends to

\[
\boxed{
q_*(0^+)
=
\sqrt{1+\frac{c_*}{4\pi^2}}-1
=0.12179248\ldots.
}
\tag{20}
\]

This limiting number is not needed for the proof and does not replace the stronger all-shape small-height closure of `ANF-039`--`ANF-041`. Its role is to show that the new estimate has a nondegenerate relative-width limit rather than collapsing immediately away from `y_1=y_2`.

For the Montgomery--Taylor spectrum, `B=1` and `ANF-038` gives the stronger strict margin `m_5(J_MT)>0.0078`, so (4) can be used directly instead of the universal `c_*`. Thus the accepted base-zero problem has a fully explicit horizontal-uniform diagonal exclusion tube without any interval search in `t_1,t_2`.

## 4. Combining with the scale-free balance cone hollows out the residual zero region

`ANF-049` gives an independent necessary condition for a negative defect. In the present variables,

\[
|y_1^2-y_2^2|=4y\delta=4qy^2,
\]

so its algebraic balance cone says

\[
H_J<0
\quad\Longrightarrow\quad
4qy^2<\frac{9}{2\pi^2}d^2.
\tag{21}
\]

Any negative configuration must therefore satisfy both the failure of the new tube and the old balance cone:

\[
\boxed{
q>q_*(y),
\qquad
\frac{|d|}{y}>\sqrt{\frac{8\pi^2q_*(y)}9}.
}
\tag{22}
\]

For a zero, the corresponding first inequality is non-strict. The exact hyperbolic balance condition of `ANF-049` can of course replace (21) and yields a sharper intersection.

This changes the geometry of the accepted `CLUE-central-notch-base-margin-certificate`. `ANF-054` removed the exact diagonal; the present result removes a computable open tube around it, uniformly in both horizontal variables. `ANF-049` then shows that any residual negative point must also move far enough horizontally relative to its mean height to accommodate a mismatch outside that tube. Together with `ANF-043`--`ANF-044`, `ANF-048` and `ANF-051`, the unresolved Montgomery--Taylor zero search is no longer merely “unequal but balanced heights”: it is confined outside an explicit near-diagonal stability region while remaining inside the pre-existing compact and anti-phase restrictions.

## 5. Stress tests and evidence boundary

Several failure modes are explicit. First, (5) is a sufficient lower bound, not an equivalence. Failing (6) gives no counterexample and does not imply that the exact Fourier-character coherence of `ANF-045` is large enough to create a zero. Second, the exponential `cosh` factors come from replacing the actual spectral average in (17) by its support-edge maximum. The tube is therefore deliberately conservative at larger heights; it is not claimed to be optimal.

Third, the positive quadratic mismatch block in (12) is discarded when deriving (16). Keeping it, or retaining the exact `C,S` weights in the two correlation channels, can only improve the certificate and is a natural next refinement if the remaining Montgomery--Taylor region is still too large. Fourth, the proof requires a nonnegative spectral density and the curvature gate `m_5>=0`; without them `ANF-054` supplies no diagonal margin to pay for the mismatch.

The decisive algebraic audit is short. Starting from the exact `ANF-042` normal form, substitution of (10) must reproduce (12). The positive term must reduce to

\[
4\sinh^2v(\sinh^2u+C^2),
\]

using `cosh^2u=1+sinh^2u`. Applying (14)--(15) must give exactly the coefficient `4pi^2 alpha^2 delta(2y+delta)` in (16). Finally, setting `delta=0` must recover the `ANF-054` diagonal bound with no loss.

The load-bearing external framework is unchanged. Buescu--Paixão--Symeonides supplies the classical Fourier--Laplace representation for positive-definite strip kernels, while the Montgomery--Taylor and semidefinite pair-correlation literature supplies the surrounding extremal context already anchored in `SOURCES.md`. A targeted search of those strip-positive-definite and pair-correlation literatures found the general representation and established semidefinite methods but no theorem matching the mean-height decomposition (12) or the explicit five-point mismatch tube (5)--(6). No publication-level novelty claim is made, and no new `SOURCES.md` entry is required because every new load-bearing step is derived from the canonical `ANF-042` and `ANF-054` identities by elementary inequalities.

The finding remains a cardinality-five result. It does not settle the accepted Montgomery--Taylor zero-freeness clue, does not prove the narrow central notch satisfies the full universal affine counting inequality, does not address larger conjugation-invariant multisets, and does not by itself resolve RH. Its durable contribution is an explicit, auditable stability neighborhood around the newly closed equal-height diagonal and an exact identification of the antisymmetric height-mismatch channel that must drive any remaining five-point obstruction.