# ANF-050 — equal-height five-point danger has an exact height-dependent bandwidth radius

**Status:** `EXACT-DERIVED + EQUAL-HEIGHT-CORE + FREQUENCYWISE-POSITIVITY + HEIGHT-DEPENDENT-BANDWIDTH-RADIUS + SHARP-UNIVERSAL-THRESHOLD + STRUCTURAL-REDUCTION`. `ANF-049` confines the last irreducible cardinality-five obstruction to nearly height-balanced two-pair shapes, while `ANF-042` identifies the equal-height diagonal as the exceptional case where the amplitude-mismatch guard disappears. On that diagonal the pointwise phase problem is exactly solvable. If the positive spectrum is supported in `[-B,B]`, then two equal-height conjugate pairs at height `y>0` are frequencywise safe for every common horizontal translation whenever

\[
\boxed{
|x_1-x_2|
\le D_{\rm eq}(y;B)
:=
\frac1{\pi B}
\arccos\!\left(\frac1{4\cosh^2(\pi By)}\right).
}
\tag{1}
\]

The radius increases strictly with height from the phase-blind constant of `ANF-048`,

\[
D_{\rm eq}(0;B)
=
\frac{\arccos(1/4)}{\pi B}
=
\frac{\arccos(-7/8)}{2\pi B},
\tag{2}
\]

toward the first anti-phase distance `1/(2B)`. More precisely,

\[
\boxed{
D_{\rm eq}(y;B)
=
\frac1{2B}
-
\frac{e^{-2\pi By}}{\pi B}
+O\!\left(\frac{e^{-4\pi By}}B\right)
\qquad(y\to\infty).
}
\tag{3}
\]

Thus the nearly balanced core isolated by `ANF-049` has additional geometry on its exact diagonal: as the common height grows, a possible negative defect must move exponentially close to or beyond the first bandwidth anti-phase scale. The radius in (1) is sharp as a rule uniform over all continuous nonnegative spectra supported in `[-B,B]`; immediately beyond it one can concentrate spectral mass near a dangerous frequency and obtain a negative equal-height two-pair defect.

Retain the two-pair five-point configuration

\[
W=\{x_1\pm iy,x_2\pm iy,r\},
\qquad y>0,
\tag{4}
\]

its real-part collapse

\[
R(W)=\{x_1,x_1,x_2,x_2,r\},
\tag{5}
\]

and put

\[
t_j=x_j-r,
\qquad d=x_1-x_2=t_1-t_2.
\tag{6}
\]

Let

\[
F=\widehat J,
\qquad J\ge0,
\qquad \operatorname{supp}J\subset[-B,B],
\tag{7}
\]

with `J` continuous, even and nonzero. As in `ANF-040`--`ANF-049`,

\[
E_F(W)-E_F(R(W))
=4H_J
=4\int J(\alpha)h_\alpha\,d\alpha.
\tag{8}
\]

## 1. Equal heights give an exact one-frequency danger inequality

At a fixed frequency define

\[
p(\alpha)
:=2\bigl(\cosh(2\pi\alpha y)-1\bigr),
\qquad
C(\alpha):=\cos(\pi\alpha d).
\tag{9}
\]

For equal heights the mismatch variable `q` in `ANF-042` vanishes. Its exact phase-amplitude normal form therefore reduces, for every `alpha!=0`, to

\[
\boxed{
\min_m h_\alpha
=p(\alpha)|C(\alpha)|
\left((p(\alpha)+4)|C(\alpha)|-1\right),
}
\tag{10}
\]

where `m` is the mean horizontal phase. Since

\[
p(\alpha)+4
=4\cosh^2(\pi\alpha y),
\tag{11}
\]

a negative pointwise contribution is possible for some horizontal placement if and only if

\[
\boxed{
0<|\cos(\pi\alpha d)|
<
\frac1{4\cosh^2(\pi\alpha y)}.
}
\tag{12}
\]

At `alpha=0`, as already separated in `ANF-042`, the physical phases are forced to zero and `h_0=0` identically. Equation (12) is therefore asserted only for nonzero frequencies.

The pointwise criterion is stronger than the height-independent equal-height bound in `ANF-048`. There the factor `p(alpha)` was discarded in order to obtain a support-only phase-blind radius. Here it is retained exactly, and its hyperbolic growth makes the dangerous anti-phase tube shrink with height.

## 2. The full support interval collapses to one edge inequality

Suppose first

\[
B|d|<\frac12.
\tag{13}
\]

Then `cos(pi alpha d)>0` on `[0,B]`, so frequencywise safety is equivalent to

\[
4\cosh^2(\pi\alpha y)\cos(\pi\alpha|d|)\ge1
\qquad(0\le\alpha\le B).
\tag{14}
\]

The nontrivial point is that it is enough to check the spectral edge `alpha=B`. Put

\[
a:=\pi y,
\qquad b:=\pi|d|,
\qquad
G(\alpha):=\cosh^2(a\alpha)\cos(b\alpha).
\tag{15}
\]

On the interval under (13), `G>0`, and

\[
\frac{d}{d\alpha}\log G(\alpha)
=
R(\alpha)
:=2a\tanh(a\alpha)-b\tan(b\alpha).
\tag{16}
\]

Its derivative is

\[
R'(\alpha)
=2a^2\operatorname{sech}^2(a\alpha)
-b^2\sec^2(b\alpha),
\tag{17}
\]

and

\[
R''(\alpha)
=-4a^3\operatorname{sech}^2(a\alpha)\tanh(a\alpha)
-2b^3\sec^2(b\alpha)\tan(b\alpha)<0
\tag{18}
\]

for `0<alpha<=B`. Thus `R'` is strictly decreasing and `R`, with `R(0)=0`, is strictly concave. Consequently `R` is either nonpositive throughout, nonnegative throughout, or changes sign once from positive to negative. Hence `G` is either decreasing, increasing, or increases once and then decreases: **it has no strict interior minimum**. Therefore

\[
\boxed{
\min_{0\le\alpha\le B}G(\alpha)
=
\min\{G(0),G(B)\}
=
\min\left\{1,
\cosh^2(\pi By)\cos(\pi B|d|)
\right\}.
}
\tag{19}
\]

Since the safety threshold in (14) is `G>=1/4` and `G(0)=1`, the whole frequency band is safe if and only if

\[
\boxed{
4\cosh^2(\pi By)\cos(\pi B|d|)\ge1.
}
\tag{20}
\]

Solving (20) for `|d|` gives exactly (1). Notice that its right-hand side is always strictly smaller than `1/(2B)`, so the preliminary condition (13) is automatic inside the certified radius.

If instead `B|d|>=1/2`, the first anti-phase zero `alpha_0=1/(2|d|)` lies in the band. In every punctured neighborhood of `alpha_0`, `|cos(pi alpha d)|` is positive and arbitrarily small while the right side of (12) remains positive. Thus pointwise-danger frequencies necessarily occur. This confirms that no second safe interval is hidden beyond the first anti-phase scale.

Combining the two cases proves

\[
\boxed{
|d|\le D_{\rm eq}(y;B)
\quad\Longrightarrow\quad
h_\alpha\ge0
\quad\text{for every }|\alpha|\le B
}
\tag{21}
\]

for every common horizontal translation, and therefore

\[
\boxed{
|d|\le D_{\rm eq}(y;B)
\quad\Longrightarrow\quad
H_J\ge0.
}
\tag{22}
\]

For a nonzero continuous spectrum and a genuine configuration the inequality is strict unless the spectrum is supported only on the zero set of the pointwise lower bound, which cannot happen for a continuous nonzero density on an open interval. In particular the Montgomery--Taylor and central-notch spectra are strictly safe in this zone.

## 3. Height strictly enlarges the `ANF-048` equal-height zone

The map

\[
y\mapsto \frac1{4\cosh^2(\pi By)}
\tag{23}
\]

is strictly decreasing for `y>0`, while `arccos` is strictly decreasing. Hence

\[
\boxed{
D_{\rm eq}(y;B)>D_{\rm eq}(0;B)
\qquad(y>0).
}
\tag{24}
\]

Using `cos(2theta)=2cos^2(theta)-1`,

\[
\arccos(1/4)
=\frac12\arccos(-7/8),
\tag{25}
\]

so the zero-height limit is exactly the equal-height phase-blind radius of `ANF-048`, not a competing constant.

At large height,

\[
\frac1{4\cosh^2(\pi By)}
=e^{-2\pi By}+O(e^{-4\pi By}),
\tag{26}
\]

and `arccos z=pi/2-z+O(z^3)` at zero, which gives (3). Thus the gap between the safe radius and the first anti-phase distance decays exponentially:

\[
\boxed{
\frac1{2B}-D_{\rm eq}(y;B)
\sim
\frac{e^{-2\pi By}}{\pi B}.
}
\tag{27}
\]

For the support-one branch this gives, for example,

\[
D_{\rm eq}(0.5;1)=0.4873572595\ldots,
\qquad
D_{\rm eq}(1;1)=0.4994077881\ldots.
\tag{28}
\]

So already at unit vertical height an equal-height negative candidate must have pair-center separation beyond `0.4994...`, compared with the height-blind `0.41957...` exclusion from `ANF-048`.

## 4. The radius is sharp for bandwidth-only uniform control

The threshold (1) cannot be enlarged uniformly over continuous even nonnegative spectra supported in `[-B,B]`.

Fix `y>0` and

\[
d_0>D_{\rm eq}(y;B).
\tag{29}
\]

If `B d_0<1/2`, then by strict failure of (20),

\[
4\cosh^2(\pi By)\cos(\pi B d_0)<1.
\tag{30}
\]

By continuity there is some `alpha_0 in (0,B)` sufficiently close to `B` for which

\[
0<\cos(\pi\alpha_0d_0)
<\frac1{4\cosh^2(\pi\alpha_0y)}.
\tag{31}
\]

If `B d_0>=1/2`, choose instead `alpha_0` sufficiently close to, but not equal to, the first anti-phase zero `1/(2d_0)`. Equation (31), with an absolute value on the cosine if needed, again holds.

By the exact criterion (12), choose the common horizontal translation so that `h_{alpha_0}<0`. The same strict inequality persists on a small neighborhood of `alpha_0`; by evenness it persists on the reflected neighborhood. Choosing any nonzero continuous even `J>=0` supported inside those two neighborhoods gives

\[
\boxed{H_J<0.}
\tag{32}
\]

Thus `D_eq(y;B)` is the **largest radius that guarantees equal-height two-pair safety using only spectral nonnegativity, bandwidth `B`, and the common height `y`**. For a fixed spread-out spectrum such as `J_MT` or `J_s`, failure of (1) is not a counterexample: cross-frequency positive mass can still dominate. The sharpness statement concerns the universal bandwidth-only class.

## 5. Interaction with the central-notch frontier

`ANF-049` shows that any residual negative two-pair defect must be nearly height balanced; its exact equal-height diagonal is therefore not a negligible special case but the center of the remaining obstruction cone. The present result removes a height-dependent slab around `d=0` on that diagonal. For support one,

\[
\boxed{
H_J(y,y;t_1,t_2)<0
\quad\Longrightarrow\quad
|d|>
\frac1\pi
\arccos\!\left(\frac1{4\cosh^2(\pi y)}\right)
}
\tag{33}
\]

for every nonnegative support-one spectrum.

For the central-notch spectra of `ANF-034` and `ANF-046`, `J_s` is identical to `J_MT` away from a narrow central interval and remains positive on the interior of `[-1,1]`. Equation (33) is therefore a strict safety statement for the actual notch family, not merely for an auxiliary envelope. It does **not** settle separations beyond the radius, because there the same physical common translation must still align the negative phase tube coherently across the weighted spectrum.

Together with `ANF-043`--`ANF-044`, `ANF-048`, and `ANF-049`, a possible five-point notch falsifier is now confined not only to a compact, nonlocal, nearly balanced shape region, but on the balanced centerline it must also lie beyond a radius that rapidly approaches `1/2` as height grows. This suggests that the next phase-aware gate should be organized around the first anti-phase resonance rather than around arbitrary `(y_1,y_2,d)` boxes.

## 6. Falsification, prior art, and evidence boundary

The load-bearing identity (10) is exactly the equal-height specialization of the canonical `ANF-042` normal form; (19) is an elementary one-variable calculus lemma. The decisive falsification checks are finite: expanding (10) must reproduce `p|C|((p+4)|C|-1)`; a frequency with `0<|C|<1/(p+4)` must admit a negative mean phase; and on `B|d|<1/2` the function `cosh^2(pi alpha y)cos(pi alpha|d|)` must have no interior minimum. Equations (16)--(18) establish the last point without numerical sampling.

The source audit found no new external dependency. The positive Fourier--Laplace representation and Montgomery--Taylor support-one spectrum are already anchored in `SOURCES.md`; all new statements here are exact consequences of the previously derived five-point normal form plus elementary hyperbolic/trigonometric calculus. No publication-level novelty claim is made, and no `SOURCES.md` update is required.

The result is specific to the equal-height slice of the two-conjugate-pair plus one-real-point geometry. It does not prove positivity throughout the nearly equal-height cone of `ANF-049`, does not show that `J_MT` or the central notch is safe beyond (1), and does not address cardinalities greater than five. Its gain is a sharp, height-sensitive removal of the exact diagonal core that the preceding reductions identified as the most coherent remaining five-point regime.