# ANF-051 — two-pair five-point danger has an exact anti-phase tube and fixed-height bandwidth radius

**Status:** `EXACT-DERIVED + EXACT-POINTWISE-DANGER-TUBE + FIXED-HEIGHT-BANDWIDTH-RADIUS + SHARP-UNIVERSAL-RADIUS + STRUCTURAL-REDUCTION`. `ANF-042` gives the exact mean-phase minimum for the last irreducible cardinality-five geometry, `ANF-049` splices separate phase and amplitude guards to obtain a scale-free height-balance cone, and `ANF-050` solves the equal-height diagonal. The remaining pointwise problem with unequal heights can also be solved exactly. For every fixed nonzero frequency, the dangerous relative phases form one explicit tube around the anti-phase lattice; its width is determined by the unique positive root of a quadratic in the hyperbolic amplitude. Optimizing those exact tubes over the spectral band gives the largest origin-centered separation radius that is uniformly safe for fixed heights and every nonnegative spectrum of that bandwidth.

Retain

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad y_1,y_2>0,
\]

put

\[
t_j=x_j-r,
\qquad d=x_1-x_2=t_1-t_2,
\]

and let

\[
F=\widehat J,
\qquad J\ge0,
\qquad \operatorname{supp}J\subset[-B,B],
\]

with `J` continuous, even and nonzero. As in `ANF-040`--`ANF-050`,

\[
E_F(W)-E_F(R(W))
=4H_J
=4\int J(\alpha)h_\alpha\,d\alpha.
\tag{1}
\]

## 1. The exact pointwise minimum reduces to one quadratic root

Fix `alpha!=0` and write

\[
a=\cosh(2\pi\alpha y_1)-1,
\qquad
b=\cosh(2\pi\alpha y_2)-1,
\]

\[
p=a+b>0,
\qquad q=a-b,
\qquad \delta=|q|,
\qquad \Delta=p^2-q^2=4ab>0,
\]

and

\[
\nu=\pi\alpha d,
\qquad C=\cos\nu.
\tag{2}
\]

The exact normal form of `ANF-042`, after minimizing over the common horizontal mean phase `m`, is

\[
\boxed{
\min_m h_\alpha
=R^2-R+4pC^2,
\qquad
R^2=q^2+\Delta C^2.
}
\tag{3}
\]

If `delta>=1`, (3) is nonnegative for every `C`, recovering the amplitude-mismatch barrier of `ANF-042`. Assume therefore

\[
0\le\delta<1.
\tag{4}
\]

Eliminating `C^2=(R^2-\delta^2)/\Delta` from (3) gives

\[
\boxed{
\Delta\min_m h_\alpha
=(\Delta+4p)R^2-\Delta R-4p\delta^2.
}
\tag{5}
\]

Define `r_*` to be the positive root of the quadratic on the right:

\[
\boxed{
r_*
=
\frac{
\Delta+
\sqrt{\Delta^2+16p\delta^2(\Delta+4p)}
}
{2(\Delta+4p)}.
}
\tag{6}
\]

For `0<delta<1`, the polynomial in (5) is negative at `R=delta` and positive at `R=1`:

\[
P(\delta)=\Delta\delta(\delta-1)<0,
\qquad
P(1)=4p(1-\delta^2)>0.
\tag{7}
\]

Its constant term is negative, so it has exactly one positive root. Hence

\[
\delta<r_*<1.
\tag{8}
\]

For `delta=0`, the same formula gives the nonzero root

\[
r_*=rac{p}{p+4}.
\tag{9}
\]

At the root, equation (3) also gives

\[
4pC^2=r_*(1-r_*).
\]

Thus define the exact phase threshold

\[
\boxed{
C_*(p,\delta)
:=
\sqrt{\frac{r_*^2-\delta^2}{\Delta}}
=
\sqrt{\frac{r_*(1-r_*)}{4p}}
>0.
}
\tag{10}
\]

## 2. Every dangerous frequency is an exact anti-phase tube

Since `R` is strictly increasing in `C^2`, the sign change in (5) gives a complete fixed-frequency classification.

If

\[
0<\delta<1,
\]
then

\[
\boxed{
\min_m h_\alpha<0
\quad\Longleftrightarrow\quad
|\cos(\pi\alpha d)|<C_*(p,\delta).
}
\tag{11}
\]

If `delta=0`, the exact anti-phase center itself is neutral and

\[
\boxed{
\min_m h_\alpha<0
\quad\Longleftrightarrow\quad
0<|\cos(\pi\alpha d)|<C_*(p,0).
}
\tag{12}
\]

Together with the `delta>=1` safety barrier, (11)--(12) are the full pointwise danger criterion at every nonzero frequency. In phase language, when `0<delta<1` the dangerous set is

\[
\boxed{
\operatorname{dist}
\left(
\pi\alpha d,
\frac\pi2+\pi\mathbb Z
\right)
<\arcsin C_*(p,\delta).
}
\tag{13}
\]

The tube closes continuously as the hyperbolic mismatch reaches the `ANF-042` barrier:

\[
\delta\uparrow1
\quad\Longrightarrow\quad
r_*\uparrow1,
\qquad
C_*\downarrow0.
\tag{14}
\]

For equal heights, `delta=0`, and (9)--(10) reduce exactly to

\[
C_*=rac1{p+4}
=rac1{4\cosh^2(\pi\alpha y)},
\tag{15}
\]

which is the pointwise criterion used in `ANF-050`. Thus the equal-height anti-phase tube is not a separate mechanism; it is the zero-mismatch endpoint of the general formula.

## 3. Fixed heights have an exact largest bandwidth-only separation radius

For fixed `y_1,y_2`, let

\[
\delta(\alpha)
=
\left|
\cosh(2\pi\alpha y_1)
-
\cosh(2\pi\alpha y_2)
\right|.
\tag{16}
\]

If `y_1!=y_2`, `ANF-042` shows that `delta(alpha)` is strictly increasing for `alpha>0`; let `alpha_*` be the unique solution

\[
\delta(\alpha_*)=1.
\tag{17}
\]

If `y_1=y_2`, set `alpha_*=+infinity`. For `0<alpha<alpha_*`, let `C_*(alpha)` be (10), and define

\[
\theta_*(\alpha)
:=\arccos C_*(\alpha).
\tag{18}
\]

When `y_1!=y_2`, extend continuously to the amplitude boundary by

\[
\theta_*(\alpha_*)=\frac\pi2.
\tag{19}
\]

Put

\[
A_B:=\min\{B,\alpha_*\}
\]

with the evident convention when `alpha_*=+infinity`, and define

\[
\boxed{
D_{\rm fix}(y_1,y_2;B)
:=
\inf_{0<\alpha\le A_B}
\frac{\theta_*(\alpha)}{\pi\alpha},
}
\tag{20}
\]

using the continuous extension (19) when `A_B=alpha_*`.

Then

\[
\boxed{
|d|\le D_{\rm fix}(y_1,y_2;B)
\quad\Longrightarrow\quad
h_\alpha\ge0
\text{ for every }|\alpha|\le B
}
\tag{21}
\]

for every common horizontal translation. Indeed, frequencies with `delta(alpha)>=1` are automatically safe. At every remaining positive frequency, (20) gives

\[
\pi\alpha|d|\le\theta_*(\alpha)<\frac\pi2,
\]

so

\[
|\cos(\pi\alpha d)|
=\cos(\pi\alpha|d|)
\ge C_*(\alpha),
\]

which lies outside the exact danger tube (11)--(12). Evenness handles negative frequencies. Therefore every continuous even nonnegative spectrum supported in `[-B,B]` satisfies

\[
\boxed{
|d|\le D_{\rm fix}(y_1,y_2;B)
\quad\Longrightarrow\quad
H_J\ge0.
}
\tag{22}
\]

The infimum in (20) is attained after the endpoint extension. Near the central frequency the threshold angle has a finite positive limit while the factor `1/alpha` diverges, so the quotient in (20) tends to `+infinity` as `alpha->0`. Thus the first dangerous separation is generated by a genuinely nonzero frequency.

More strongly, (20) is the **largest origin-centered separation radius having this uniform property for the fixed heights and bandwidth**. Let `R>D_fix`. Choose an active frequency `alpha_0` with

\[
\frac{\theta_*(\alpha_0)}{\pi\alpha_0}<R.
\]

If the infimum occurs at `alpha_*`, take `alpha_0<alpha_*` sufficiently close to it. Since `theta_*(alpha_0)<pi/2`, one may choose

\[
\frac{\theta_*(\alpha_0)}{\pi\alpha_0}
<d_0<
\min\left\{R,\frac1{2\alpha_0}\right\}.
\tag{23}
\]

Then

\[
0<\cos(\pi\alpha_0d_0)<C_*(\alpha_0),
\]

so an appropriate mean phase makes `h_{alpha_0}<0`. The strict inequality persists on a neighborhood of `alpha_0`. Concentrating any continuous even nonnegative spectrum in that neighborhood and its reflection gives `H_J<0`, with `|d_0|<R`. Hence no larger origin-centered radius can be guaranteed from the fixed heights, spectral positivity and bandwidth alone.

## 4. The new radius strictly refines the one-third guard and recovers the equal-height theorem

The universal `ANF-048` phase guard implies that the exact threshold always obeys

\[
C_*(\alpha)<\frac12
\tag{24}
\]

for genuine fixed heights and every active nonzero frequency: at `|C|=1/2` one has `cos(2nu)=-1/2`, where the `ANF-048` lower bound is already strictly positive. Therefore

\[
\theta_*(\alpha)>\frac\pi3.
\tag{25}
\]

It follows from (20) that

\[
\boxed{
D_{\rm fix}(y_1,y_2;B)>rac1{3B}
}
\tag{26}
\]

for every fixed genuine pair of positive heights. Thus the sharp universal `1/(3B)` radius of `ANF-048` is attained only through a degenerating height-balance limit; once the two positive heights are fixed, the exact phase-amplitude geometry always opens a strictly larger safe interval.

For equal heights, (15) inserted in (20) gives

\[
D_{\rm fix}(y,y;B)
=
\inf_{0<\alpha\le B}
\frac1{\pi\alpha}
\arccos\!\left(
\frac1{4\cosh^2(\pi\alpha y)}
\right).
\tag{27}
\]

The calculus lemma proved in `ANF-050` says that this infimum occurs at the spectral edge `alpha=B`. Hence

\[
\boxed{
D_{\rm fix}(y,y;B)
=
\frac1{\pi B}
\arccos\!\left(
\frac1{4\cosh^2(\pi By)}
\right)
=D_{\rm eq}(y;B),
}
\tag{28}
\]

so (20) genuinely extends rather than competes with the equal-height result.

For unequal heights there is a second exact simplification. Once

\[
B\ge\alpha_*,
\]

all frequencies beyond `alpha_*` are pointwise safe by amplitude mismatch. Consequently

\[
\boxed{
D_{\rm fix}(y_1,y_2;B)
=D_{\rm fix}(y_1,y_2;\alpha_*)
\qquad(B\ge\alpha_*,\ y_1\ne y_2).
}
\tag{29}
\]

Thus fixed unequal heights exhibit **bandwidth saturation**: enlarging the spectral support past the amplitude-closure frequency cannot shrink their first-danger radius. Equal heights are exactly the exceptional case in which no such finite closure frequency exists.

## 5. The low-frequency endpoint recovers the balance geometry but never controls the radius

The exact tube also clarifies how `ANF-048` and `ANF-049` appear at very low frequency. Put

\[
\chi_0
:=
\frac{4y_1^2y_2^2}{(y_1^2+y_2^2)^2}
\in(0,1].
\tag{30}
\]

As `alpha->0`,

\[
p
=2\pi^2\alpha^2(y_1^2+y_2^2)+O(\alpha^4),
\qquad
\frac{|q|}{p}
\longrightarrow
\frac{|y_1^2-y_2^2|}{y_1^2+y_2^2}.
\tag{31}
\]

Substitution into (6)--(10) gives the finite limit

\[
\boxed{
C_*(\alpha)^2
\longrightarrow
\frac{
\chi_0+\sqrt{\chi_0^2+64(1-\chi_0)}
}{32}.
}
\tag{32}
\]

This is exactly the small-frequency balance threshold encoded by the `ANF-048` coefficient `chi=4ab/(a+b)^2`. At equal heights `chi_0=1` and the limit is `C_*=1/4`; as the height ratio degenerates, `chi_0->0` and the threshold approaches `1/2`, recovering the one-third universal phase guard.

But the corresponding angle remains a positive constant while (20) divides by `alpha`. Hence

\[
\frac{\theta_*(\alpha)}{\pi\alpha}
\longrightarrow+\infty
\qquad(\alpha\downarrow0).
\tag{33}
\]

So no fixed pair of positive heights can first become dangerous at infinitesimal frequency. The scale-free cone of `ANF-049` is a useful global sufficient splice, but the actual fixed-height first-danger geometry is always set at a finite nonzero frequency and is exactly the one-dimensional minimization (20).

## 6. Prior art, falsification, and evidence boundary

The external prior-art audit again finds the classical Fourier--Laplace representation for positive-definite strip functions (Buescu--Paixão--Symeonides, already anchored in `SOURCES.md`) and the established literature on positive-definite bandlimited extremal functions. None supplies the present five-point phase-amplitude classification. No external theorem is load-bearing after the canonical `ANF-042` normal form: the new step is the elementary elimination (5), its unique positive quadratic root, and optimization of the resulting anti-phase tube. No publication-level novelty claim is made, and no `SOURCES.md` update is required.

The decisive algebraic audit is direct. Expanding (5) using `Delta=p^2-q^2` must recover `Delta(R^2-R+4pC^2)`. For `0<delta<1`, the signs in (7) force a unique positive root and therefore (11). At `delta=0`, `C=0` must remain neutral while every sufficiently small nonzero `|C|` is dangerous, reproducing `ANF-050`. At `delta>=1`, no tube exists, reproducing `ANF-042`. Finally, any claimed bandwidth radius larger than (20) is falsified by the concentrated-spectrum construction following (23).

The theorem is deliberately pointwise/universal. It does not say that a spread-out fixed spectrum fails as soon as `|d|>D_fix`; beyond the radius, common-phase coherence across frequencies can still make the integrated defect positive. It also does not address cardinalities greater than five or prove the full universal affine counting certificate of `ANF-005`.

## 7. Consequence for the central-notch frontier

For support one, every residual central-notch five-point falsifier must now satisfy the exact height-dependent geometric condition

\[
\boxed{
|x_1-x_2|
>D_{\rm fix}(y_1,y_2;1),
}
\tag{34}
\]

in addition to the compactness of `ANF-043`--`ANF-044` and the height-balance restriction of `ANF-049`. On the equal-height diagonal this is precisely the `ANF-050` radius; off the diagonal, the amplitude mismatch narrows and eventually closes the anti-phase tube, and if its closure occurs below the support edge then the relevant bandwidth truncates automatically at `alpha_*`.

This reduces the next rigorous certification problem again. Instead of treating the entire compact `(y_1,y_2,d)` box, one can first compute or bound the exact one-dimensional threshold (20) for each height pair and discard every smaller separation. Only shapes beyond that first-danger surface need the phase-aware cross-frequency coherence test of `ANF-045` or the amplitude certificate of `ANF-047`. A genuine counterexample must therefore live not merely near equal height and finite separation, but beyond the exact anti-phase surface generated by a finite nonzero resonant frequency.