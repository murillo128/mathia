# ANF-058 — curvature-correlation retention confines Montgomery--Taylor five-point zeros to a compact separation annulus

**Status:** `EXACT-DERIVED + PHASE-AWARE-MISMATCH-TRANSFER + ALL-HEIGHT-SEPARATION-GATE + EXPLICIT-MONTGOMERY-TAYLOR-ANNULUS + STRUCTURAL-REDUCTION`. `ANF-057` shows that a horizontal-free comparison cannot enlarge the support-free relative-height tube much further: its small-frequency mismatch loss has the sharp coefficient `2q`. The exact mismatch identity still contains a positive term that `ANF-057` discards, namely `4 sinh^2(V) cos^2(pi alpha d)`. Retaining that term couples the unequal-height loss to the same curvature correlation `K_J(d)` that controls the equal-height margin. This produces an all-height separation gate. For the fixed Montgomery--Taylor profile, elementary moment and Fourier-tail bounds then confine every possible genuine five-point base zero to the explicit horizontal annulus

\[
\boxed{0.42<|d|<\frac74.}
\]

No height bound or numerical four-variable search is used.

Let `J` be nonzero, continuous, even, nonnegative and compactly supported, and put

\[
K_J(t)=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad K_0=K_J(0)>0,
\]

\[
m_5(J)=2K_0+3\inf_tK_J(t).
\tag{1}
\]

Assume explicitly throughout the general theorem that

\[
\boxed{m_5(J)\ge0.}
\tag{2}
\]

For genuine heights `y_1,y_2>0`, write

\[
y=\frac{y_1+y_2}{2},
\qquad
\delta=\frac{|y_1-y_2|}{2},
\qquad
q=\frac{\delta}{y}\in[0,1),
\tag{3}
\]

and for the pair-center separation put

\[
d=t_1-t_2.
\tag{4}
\]

Define the normalized curvature correlation

\[
\boxed{
a_J(d):=\frac{K_0+K_J(d)}{K_0}
=1+\frac{K_J(d)}{K_0}.}
\tag{5}
\]

The curvature gate implies `a_J(d)>=1/3` for every `d`.

## 1. The diagonal margin can retain the actual separation

On equal heights, `ANF-054` writes the positive block and the potentially negative character term as

\[
B=4\int J(\alpha)\sinh^2(2\pi\alpha y)
\cos^2(\pi\alpha d)\,d\alpha,
\tag{6}
\]

\[
L=2\int J(\alpha)(\cosh(2\pi\alpha y)-1)
|\cos(\pi\alpha d)|\,d\alpha,
\tag{7}
\]

with `H_J(y,y;t_1,t_2)>=B-L`. The same weighted Cauchy argument gives

\[
L^2\le B R_y,
\qquad
R_y\le\pi^2y^2K_0.
\tag{8}
\]

Instead of replacing `K_J(d)` by its global infimum, retain it in the lower bound

\[
B\ge8\pi^2y^2\bigl(K_0+K_J(d)\bigr)
=8\pi^2K_0y^2a_J(d).
\tag{9}
\]

Since `a_J(d)>=1/3`, the right side of (9) is larger than `R_y/4`, so `B-sqrt(BR_y)` is increasing in `B` throughout the relevant range. Therefore

\[
\boxed{
H_J(y,y;t_1,t_2)
\ge8\pi^2K_0y^2
\left(a_J(d)-\sqrt{\frac{a_J(d)}8}\right).
}
\tag{10}
\]

Taking the worst allowed `a_J(d)>=(1+m_5/K_0)/3` recovers exactly the diagonal coefficient used in `ANF-057`; equation (10) is its separation-aware version.

## 2. The discarded quadratic mismatch term produces a second copy of `K_0+K_J(d)`

Use the exact mean-height identity of `ANF-055`--`ANF-056`. For a fixed frequency set

\[
U=2\pi|\alpha|y,
\qquad
V=qU,
\qquad
C=\cos(\pi\alpha d),
\]

\[
x=\sinh U\,\sinh V.
\tag{11}
\]

Joint minimization of the two mismatch-correlation channels gives

\[
\boxed{
h_\alpha-h_\alpha^{\rm diag}
\ge4x^2-2x+4\sinh^2(V)C^2.}
\tag{12}
\]

The first two terms can only be negative when `x<1/2`. Let

\[
\ell_q(U)=2x(1-2x)_+.
\tag{13}
\]

For

\[
q\ge q_0:=6-\sqrt{35}=0.0839202\ldots,
\tag{14}
\]

the reciprocal-sinh estimate used in `ANF-057` gives, globally in `U`,

\[
\boxed{\ell_q(U)\le2qU^2.}
\tag{15}
\]

For completeness, the load-bearing scalar step is

\[
\frac{t}{\sinh t}\ge1-\frac{t^2}{6},
\]

which implies for `R=x/(qU^2)>=1` that

\[
1-R^{-1}\le\frac{(1+q^2)U^2}{6}\le2qU^2
\]

when `q>=q_0`; substituting `x=qU^2R` into (13) yields (15). Thus the current result does not depend on interpreting `m_5>=0` as anything other than the explicit hypothesis (2).

Now retain the last positive term of (12). Since `sinh V>=V`,

\[
\begin{aligned}
h_\alpha-h_\alpha^{\rm diag}
&\ge-2qU^2+4V^2C^2\\
&=4\pi^2\alpha^2y^2\bigl(-2q+4q^2C^2\bigr).
\end{aligned}
\tag{16}
\]

Integrating against `J>=0` and using

\[
\int \alpha^2J(\alpha)\cos^2(\pi\alpha d)\,d\alpha
=\frac{K_0+K_J(d)}2
\tag{17}
\]

gives the separation-aware mismatch transfer

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge H_J(y,y;t_1,t_2)
-8\pi^2qK_0y^2
+8\pi^2q^2\bigl(K_0+K_J(d)\bigr)y^2
}
\tag{18}
\]

for every `q>=q_0` and every horizontal placement.

Combining (10) and (18) gives the central inequality of this finding:

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge8\pi^2K_0y^2\,
\Phi_{a_J(d)}(q),
}
\tag{19}
\]

where

\[
\boxed{
\Phi_a(q)=a q^2-q+a-\sqrt{\frac a8}.}
\tag{20}
\]

The new `a q^2` term is exactly the horizontal information discarded by the previous support-free comparison.

## 3. A simple curvature-correlation threshold closes every height ratio

If

\[
\boxed{K_J(d)\ge-\frac13K_0,}
\tag{21}
\]

then `a_J(d)>=2/3`. For `a>=2/3`, the quadratic (20) is strictly positive for every real `q`. One quick audit is its discriminant

\[
\Delta(a)=1-4a\left(a-\sqrt{\frac a8}\right).
\tag{22}
\]

At `a=2/3`,

\[
\Delta(2/3)
=-\frac79+\frac{4}{3\sqrt3}<0,
\tag{23}
\]

because `4sqrt(3)<7`, and `Delta'(a)<0` for `a>=2/3`. Hence `Phi_a(q)>0` for all real `q` whenever `a>=2/3`.

For `q>=q_0`, (19) therefore proves strict positivity. For `0<=q<q_0`, the support-free theorem `ANF-056` already gives strict positivity because `q_0<q_c=0.10616522...`. Consequently

\[
\boxed{
K_J(d)\ge-\frac13K_0
\quad\Longrightarrow\quad
H_J(y_1,y_2;t_1,t_2)>0
}
\tag{24}
\]

for **all** genuine positive heights and every common translation, under the explicit curvature-gate hypothesis (2).

Equivalently, every genuine zero or negative two-pair five-point defect must satisfy the necessary separation condition

\[
\boxed{K_J(d)<-\frac13K_0.}
\tag{25}
\]

This is qualitatively different from the earlier origin-centered bandwidth radii. It does not merely say that `|d|` must be large enough. A possible obstruction must place its actual pair-center separation inside a significantly negative lobe of the second-moment cosine transform. In particular, every region where `K_J(d)` is nonnegative is automatically safe for all height ratios.

A more graded version is also immediate. For `a=a_J(d)>=1/3`, equation (19) certifies every `q>=q_0` for which `Phi_a(q)>0`; when its discriminant is nonnegative, the first possible crossing is

\[
q=\frac{1-\sqrt{1-4a(a-\sqrt{a/8})}}{2a}.
\tag{26}
\]

Thus the separation dependence can be retained quantitatively rather than reduced to the clean threshold (21).

## 4. Montgomery--Taylor zeros are confined to `0.42<|d|<7/4`

For the fixed Montgomery--Taylor spectrum, `ANF-038` writes

\[
w(\alpha)=\alpha^2J_{\rm MT}(\alpha),
\qquad
K_{\rm MT}(d)=\int_{-1}^{1}w(\alpha)\cos(2\pi\alpha d)\,d\alpha,
\]

and proves

\[
0.1549985926411760<K_0<0.1549985926411777.
\tag{27}
\]

It also gives the exact moment formula

\[
W_2:=\int\alpha^2w(\alpha)\,d\alpha
=\frac{31-19\cos\sqrt2-20\sqrt2\sin\sqrt2}
{2(1-\cos\sqrt2)}.
\tag{28}
\]

Substitution into the same outward enclosures persisted in `ANF-038` gives the deliberately coarse certified interval

\[
\boxed{0.05854<W_2<0.05855.}
\tag{29}
\]

For every real `x`, `cos x>=1-x^2/2`. Hence

\[
K_{\rm MT}(d)
\ge K_0-2\pi^2d^2W_2.
\tag{30}
\]

At `|d|<=21/50=0.42`, the outward bounds

\[
2(3.14159265360)^2(21/50)^2(0.05855)
<0.203871
<\frac43(0.1549985926411760)
\tag{31}
\]

show that the loss in (30) is strictly smaller than `4K_0/3`. Therefore

\[
\boxed{|d|\le0.42
\quad\Longrightarrow\quad
K_{\rm MT}(d)>-\frac13K_0.}
\tag{32}
\]

The opposite tail is controlled by the unimodality/variation certificate already proved in `ANF-038`. It gives

\[
\operatorname{TV}(w)<0.56,
\qquad
|K_{\rm MT}(d)|<\frac{0.56}{2\pi|d|}
\quad(d\ne0).
\tag{33}
\]

For `|d|>=7/4`, using `pi>3.14159265358`,

\[
\frac{0.56}{2(3.14159265358)(7/4)}
<0.050930
<\frac13(0.1549985926411760).
\tag{34}
\]

Thus

\[
\boxed{|d|\ge\frac74
\quad\Longrightarrow\quad
K_{\rm MT}(d)>-\frac13K_0.}
\tag{35}
\]

Applying the all-height gate (24) to (32) and (35) yields the explicit residual annulus

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)=0,\ y_1,y_2>0
\quad\Longrightarrow\quad
0.42<|t_1-t_2|<\frac74.}
\tag{36}
\]

The same conclusion holds a fortiori for a negative defect. Combining (36) with the independently certified Montgomery--Taylor relative-height exclusion gives the current residual geometry

\[
0.42<|d|<1.75,
\qquad
\frac{|y_1-y_2|}{y_1+y_2}>0.1409.
\tag{37}
\]

The first inequality is new here; the second remains the profile-specific curvature-margin consequence of the preceding unequal-height work.

## 5. Why this materially changes the accepted base-margin problem

`CLUE-central-notch-base-margin-certificate` asks for a sign decision for one fixed profile, not another optimization over notches. The current finding replaces the previous non-explicit horizontal compactification by a small explicit interval in the only relative-horizontal variable that remains after common-translation scalarization. More importantly, the mechanism explains *which* separations deserve attention: only negative lobes of `K_MT(d)` below `-K_0/3` can host a zero.

This gives a natural next certification route. On `0.42<|d|<7/4`, evaluate or bound the explicit curvature transform first. Wherever `K_MT(d)>=-K_0/3`, the entire height plane is removed analytically. Only the subintervals where the curvature transform is sufficiently negative require the full two-variable `(y,q)` defect or Hilbert-coherence analysis. Because `K_MT` is an explicit cosine transform of the closed-form density from `ANF-038`, those subintervals can be isolated with one-dimensional interval arithmetic before any higher-dimensional enclosure is attempted.

The result also explains why merely improving the horizontal-free coefficient in `ANF-057` was the wrong next move. The first information that survives its small-frequency sharpness barrier is precisely the `cos^2(pi alpha d)` term in (12), and after integration that term becomes the already canonical curvature correlation `K_J(d)`. No new analytic object is required.

## 6. Stress tests, prior art, and evidence boundary

The decisive algebraic checks are finite. Expanding the retained positive term in (12), applying `sinh(V)>=V`, and using the identity (17) must reproduce exactly the `+8pi^2 q^2(K_0+K_J(d))y^2` term in (18). Setting `q=0` must reduce (19) to the separation-aware diagonal margin (10). Replacing `K_J(d)` by the curvature-gate worst case `K_0+K_J(d)>=(K_0+m_5)/3` and then discarding the `a q^2` term recovers the previous horizontal-free comparison, so the new inequality is a genuine refinement rather than a competing normalization.

The threshold `-K_0/3` is deliberately simple, not optimal. The exact discriminant in (22) becomes negative slightly before `a=2/3`, and equation (26) gives a stronger graded certificate when `a<2/3`. Likewise, the numerical endpoints `0.42` and `7/4` are conservative rational choices chosen to leave visible outward-rounded margin. They are not claimed to be the exact components of the set `K_MT(d)<-K_0/3`.

A targeted prior-art audit of Montgomery--Taylor/pair-correlation extremal work and the classical positive-definite Fourier--Laplace strip literature recovers the established extremal framework and the Buescu--Paixão--Symeonides representation already anchored in `SOURCES.md`, but no theorem matching the two-pair curvature-correlation transfer (18)--(24) or the resulting Montgomery--Taylor separation annulus. No publication-level novelty claim is made. No new external theorem is load-bearing: after the canonical five-point normal form, all new steps are elementary hyperbolic, Cauchy, cosine-moment and bounded-variation estimates, so `SOURCES.md` requires no change.

The finding remains a cardinality-five statement. It does not prove that `H_MT` is zero-free inside the annulus (36), does not establish the full universal affine certificate for a central notch, and does not address larger conjugation-invariant multisets. Its durable contribution is to turn horizontal separation from a generic compactness variable into a signed curvature-correlation gate and to reduce the fixed Montgomery--Taylor zero problem to an explicit bounded separation interval before any interval search begins.