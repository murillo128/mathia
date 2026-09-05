# ANF-049 — two-pair five-point descent is confined to a scale-free height-balance cone

**Status:** `EXACT-DERIVED + FREQUENCYWISE-POSITIVITY + HEIGHT-MISMATCH-EXCLUSION + SCALE-FREE-SAFETY-CONE + STRUCTURAL-REDUCTION`. `ANF-042` localizes pointwise danger by hyperbolic amplitude mismatch, while `ANF-048` localizes it by relative horizontal phase. Those two guards can be spliced at a single frequency without using the detailed spectrum. The result is a new global exclusion principle for the last irreducible five-point geometry: a negative two-pair defect is possible only when the two conjugate heights are quantitatively balanced relative to the separation of their real centers.

Retain

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad y_1,y_2>0,
\]

and its real-part collapse

\[
R(W)=\{x_1,x_1,x_2,x_2,r\}.
\]

Put

\[
t_j=x_j-r,
\qquad
d=x_1-x_2=t_1-t_2,
\]

and let

\[
F(z)=\widehat J(z),
\qquad J\ge0
\]

with `J` continuous, even, nonzero and compactly supported. As in `ANF-040`--`ANF-042`, write

\[
E_F(W)-E_F(R(W))
=4H_J(y_1,y_2;t_1,t_2)
=4\int J(\alpha)h_\alpha\,d\alpha.
\tag{1}
\]

For `d\ne0`, define the splice frequency

\[
\boxed{
\alpha_d:=\frac1{3|d|}.
}
\tag{2}
\]

Then the complete two-pair defect is nonnegative for every common horizontal translation whenever

\[
\boxed{
2\sinh\!\left(\frac{\pi(y_1+y_2)}{3|d|}\right)
\sinh\!\left(\frac{\pi|y_1-y_2|}{3|d|}\right)
\ge1.
}
\tag{3}
\]

Equivalently, every negative two-pair defect with `d\ne0` must lie in the exact dimensionless height-balance region

\[
\boxed{
2\sinh\!\left(\frac{\pi(y_1+y_2)}{3|d|}\right)
\sinh\!\left(\frac{\pi|y_1-y_2|}{3|d|}\right)
<1.
}
\tag{4}
\]

A simpler algebraic consequence is

\[
\boxed{
H_J<0
\quad\Longrightarrow\quad
|y_1^2-y_2^2|
<\frac{9}{2\pi^2}d^2
=0.4559453263\ldots\,d^2.
}
\tag{5}
\]

Thus a finite-height obstruction cannot have arbitrarily unequal conjugate heights at a fixed pair-center separation. This safety cone is **scale free** and does not use the support radius of `J`: it follows only from nonnegative spectral weighting and the exact five-point geometry.

## 1. The low-frequency phase guard

At a fixed frequency let

\[
a=\cosh(2\pi\alpha y_1)-1,
\qquad
b=\cosh(2\pi\alpha y_2)-1,
\qquad
s=a+b,
\]

and

\[
c=\cos(2\pi\alpha d).
\]

The exact normal form used in `ANF-048` is

\[
h_\alpha
=|V_\alpha|^2+\operatorname{Re}V_\alpha
+2s(1+c),
\tag{6}
\]

where

\[
V_\alpha
=a e^{2\pi i\alpha t_1}
+b e^{2\pi i\alpha t_2}.
\]

Writing `R=|V_alpha|`, one has `R<=s` and therefore

\[
h_\alpha
\ge R^2-R+2s(1+c).
\tag{7}
\]

If

\[
c\ge-\frac12,
\]

then `2s(1+c)>=s>=R`, so

\[
\boxed{h_\alpha\ge R^2\ge0.}
\tag{8}
\]

For every frequency satisfying

\[
|\alpha|\le\alpha_d=\frac1{3|d|},
\]

we have

\[
|2\pi\alpha d|\le\frac{2\pi}{3},
\]

and hence `c>=-1/2`. Thus the entire low-frequency interval

\[
\boxed{|\alpha|\le\alpha_d}
\tag{9}
\]

is pointwise safe independently of the two heights and independently of the common translation.

This is the local form of the bandwidth exclusion in `ANF-048`, but here the cutoff is chosen from the actual physical separation `d` rather than from a support edge.

## 2. The high-frequency amplitude guard

Assume first `y_1\ne y_2`. `ANF-042` shows that a nonzero frequency can be harmful for some horizontal phases only if the hyperbolic amplitude mismatch is smaller than one. In the present notation,

\[
q(\alpha)
:=
\left|
\cosh(2\pi\alpha y_1)
-
\cosh(2\pi\alpha y_2)
\right|
\tag{10}
\]

has the exact factorization

\[
\boxed{
q(\alpha)
=2\sinh\!\bigl(\pi|\alpha|(y_1+y_2)\bigr)
\sinh\!\bigl(\pi|\alpha||y_1-y_2|\bigr).
}
\tag{11}
\]

For unequal heights, `q(alpha)` is strictly increasing in `|alpha|>0`. Moreover, `ANF-042` proves

\[
q(\alpha)\ge1
\quad\Longrightarrow\quad
h_\alpha\ge0
\tag{12}
\]

for every choice of horizontal phases.

Evaluating (11) at the splice frequency (2) gives

\[
q(\alpha_d)
=
2\sinh\!\left(\frac{\pi(y_1+y_2)}{3|d|}\right)
\sinh\!\left(\frac{\pi|y_1-y_2|}{3|d|}\right).
\tag{13}
\]

Hence condition (3) implies `q(alpha_d)>=1`, and monotonicity gives

\[
q(\alpha)\ge1
\qquad(|\alpha|\ge\alpha_d).
\tag{14}
\]

So the entire complementary high-frequency region is pointwise safe as well.

Combining (9) and (14) covers the full frequency axis. Therefore

\[
\boxed{h_\alpha\ge0\quad\text{for every }\alpha,}
\tag{15}
\]

and, since `J>=0`,

\[
\boxed{H_J\ge0.}
\tag{16}
\]

No cancellation between frequencies, curvature estimate, compactness argument, or detailed information about the spectral mass is used.

The equal-height case `y_1=y_2` correctly falls outside condition (3): then `q` vanishes identically and the amplitude guard contributes nothing. Equal heights are precisely the regime where `ANF-042` leaves anti-phase tubes as the possible danger mechanism.

If `d=0`, division by `d` is unnecessary: `ANF-048` already gives frequencywise nonnegativity directly because `cos(2pi alpha d)=1`. Thus the only genuinely open case has `d\ne0`.

## 3. A universal algebraic cone

Condition (3) has an immediate, less sharp but very simple sufficient form. Since `sinh u>=u` for `u>=0`, equation (13) gives

\[
\begin{aligned}
q(\alpha_d)
&\ge
2\left(\frac{\pi(y_1+y_2)}{3|d|}\right)
\left(\frac{\pi|y_1-y_2|}{3|d|}\right)\\
&=
\frac{2\pi^2}{9d^2}|y_1^2-y_2^2|.
\end{aligned}
\tag{17}
\]

Consequently

\[
\boxed{
|y_1^2-y_2^2|
\ge\frac{9}{2\pi^2}d^2
\quad\Longrightarrow\quad
H_J\ge0.
}
\tag{18}
\]

Taking the contrapositive proves (5).

The geometry is best seen in dimensionless variables

\[
S:=\frac{y_1+y_2}{|d|},
\qquad
D:=\frac{|y_1-y_2|}{|d|}.
\tag{19}
\]

Every negative configuration must satisfy

\[
\boxed{
2\sinh\!\left(\frac{\pi S}{3}\right)
\sinh\!\left(\frac{\pi D}{3}\right)<1,
}
\tag{20}
\]

and therefore

\[
\boxed{SD<\frac{9}{2\pi^2}.}
\tag{21}
\]

This makes the scale invariance explicit. Rescaling all horizontal and vertical distances by the same factor does not move a shape into or out of the exclusion region.

## 4. Large mean height forces exponentially precise balance

The exact hyperbolic condition is substantially stronger than the quadratic cone when the pair heights are large relative to `|d|`. From the necessary condition (4) and

\[
\sinh u\ge u,
\]

applied only to the height-difference factor, any negative defect must obey

\[
2\sinh\!\left(\frac{\pi(y_1+y_2)}{3|d|}\right)
\frac{\pi|y_1-y_2|}{3|d|}
<1.
\]

Therefore

\[
\boxed{
|y_1-y_2|
<
\frac{3|d|}
{2\pi\sinh\!\left(\frac{\pi(y_1+y_2)}{3|d|}\right)}.
}
\tag{22}
\]

Once `(y_1+y_2)/|d|` is moderately large, the allowed height mismatch is exponentially small. Thus the residual finite-height problem is not merely "two heights in a compact interval": tall candidate pairs must approach the equal-height diagonal very rapidly relative to their horizontal separation.

This complements the height coercivity of `ANF-043`. There, sufficiently large absolute height is eventually safe after integration. Here, before invoking that asymptotic theorem, the frequencywise splice shows that **any finite-height candidate with appreciable height asymmetry is already safe**.

## 5. Interaction with the bandwidth and compactness reductions

Suppose now that `J` is supported in `[-B,B]`. `ANF-048` gives the independent support-only exclusion

\[
|d|\le\frac1{3B}
\quad\Longrightarrow\quad
H_J>0
\tag{23}
\]

for genuine two-pair heights. Hence any negative configuration must satisfy both

\[
\boxed{|d|>\frac1{3B}}
\tag{24}
\]

and the height-balance condition (4), in particular the algebraic restriction (5).

When `m_5(J)>=0`, `ANF-043`--`ANF-044` already confine every negative defect to a compact box in `(y_1,y_2,t_1,t_2)`. `ANF-048` punches a slab out of that box around `d=0`. The present finding removes the complementary strongly unbalanced-height region. What remains is therefore a compact annular shape domain concentrated around

\[
y_1\approx y_2,
\qquad
|d|>\frac1{3B}.
\tag{25}
\]

For the support-one Montgomery--Taylor and central-notch branch this means that every still-possible cardinality-five falsifier must have `|d|>1/3` and satisfy

\[
|y_1^2-y_2^2|<0.4559453263\ldots\,d^2,
\tag{26}
\]

with the stronger exact hyperbolic restriction (4). This removes another large part of the interval-certification domain without using any special formula for `J_MT` or the notch.

## 6. Falsification, prior art, and evidence boundary

The argument has two independent audit gates. First, a negative pointwise defect must evade the `ANF-048` phase guard, so it must occur at a frequency with `|alpha|>1/(3|d|)`. Second, it must evade the `ANF-042` amplitude-mismatch guard, so at that same frequency `q(alpha)<1`. Since `q` is increasing for unequal heights, those two facts force `q(1/(3|d|))<1`, which is exactly (4). Any explicit configuration with `H_J<0` violating (4) or (5) would therefore falsify the result.

The exact condition (3) is a sufficient safety criterion obtained by splicing two previously sharp pointwise guards at one cutoff. **No optimality is claimed for the resulting cone.** The phase function can return to safe and dangerous intervals as frequency increases, and a fixed spectrum can gain additional positivity from its mass distribution. Thus failure of (3) does not produce a counterexample; it only identifies the residual region in which cross-frequency coherence still has to be analyzed.

A targeted prior-art search in the neighboring complex-positive-definite/Fourier--Laplace and zeta pair-correlation literature found the standard strip Fourier--Laplace representation and the established semidefinite pair-correlation framework, already anchored in `SOURCES.md`, but no external theorem supplying this two-pair hyperbolic phase/amplitude splice or the dimensionless cone (20). No publication-level novelty claim is made. No new `SOURCES.md` entry is needed because the proof is an exact consequence of the canonical `ANF-042` and `ANF-048` identities.

The result is specific to the two-conjugate-pair plus one-real-point geometry and does not close the universal affine counting problem or configurations of larger cardinality. It also does not settle the equal-height residual core, where the amplitude mismatch vanishes and genuine cross-frequency phase coherence remains possible.

## 7. Consequence for the central-notch frontier

The last five-point obstruction has now been squeezed from four directions: small heights by `ANF-039`--`ANF-041`, large heights by `ANF-043`, horizontal escape by `ANF-044`, small relative separation by `ANF-048`, and now strong height imbalance by (4)--(5). The residual central-notch certification problem is therefore concentrated on finite, nonlocal, **nearly height-balanced** two-pair shapes.

The next useful certificate should exploit this concentration rather than treating the two heights independently over the whole compact box. In particular, an interval or analytic treatment can parameterize the residual domain by mean height and a small imbalance variable, with the exact restriction (22) shrinking the imbalance window exponentially as the mean-height-to-separation ratio grows. A counterexample, if one exists, must live inside that narrow coherent core.