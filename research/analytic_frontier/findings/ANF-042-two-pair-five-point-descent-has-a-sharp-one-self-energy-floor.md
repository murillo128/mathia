# ANF-042 — two-pair five-point descent has a sharp one-self-energy floor

**Status:** `EXACT-DERIVED + GLOBAL-FIVE-POINT-ENERGY-FLOOR + POINTWISE-DANGER-BAND + STRUCTURAL-BOUNDARY`. `ANF-040` reduces the last genuinely coupled cardinality-five geometry to two conjugate pairs plus one real point, while `ANF-041` closes its entire small-height boundary whenever the curvature gate `m_5(J)` is nonnegative. The remaining question is genuinely finite height. The exact integrand admits a further global reduction: its negative part is uniformly bounded by one quarter per frequency, and negative contribution is possible only in an explicitly characterized phase-amplitude danger region.

Let `J` be a nonzero continuous even nonnegative compactly supported spectrum, let `F=widehat J`, and retain the `ANF-040` configuration

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
R(W)=\{x_1,x_1,x_2,x_2,r\},
\qquad y_1,y_2>0.
\]

With `t_j=x_j-r`, `d=t_1-t_2`, `c_j(\alpha)=\cosh(2\pi\alpha y_j)`, `ANF-040` gives

\[
E_F(W)-E_F(R(W))=4\int J(\alpha)h_\alpha\,d\alpha,
\tag{1}
\]

where

\[
\begin{aligned}
h_\alpha={}&(c_1^2-1)+(c_2^2-1)
+2(c_1c_2-1)\cos(2\pi\alpha d)\\
&+(c_1-1)\cos(2\pi\alpha t_1)
+(c_2-1)\cos(2\pi\alpha t_2).
\end{aligned}
\tag{2}
\]

Then, for every frequency, every two heights, and every horizontal geometry,

\[
\boxed{h_\alpha\ge-\frac14.}
\tag{3}
\]

The constant is sharp at the pointwise level. Consequently,

\[
\boxed{
E_F(W)-E_F(R(W))\ge-F(0).
}
\tag{4}
\]

For nonzero continuous `J`, equality in (4) is impossible, so in fact the inequality is strict for every fixed genuine configuration. Thus **a finite-height two-pair deformation can lower the pair energy relative to its real collapse by less than one self-energy unit, uniformly over all heights and horizontal placements**.

More importantly, (3) comes with an exact danger criterion. Put

\[
a:=c_1-1,\qquad b:=c_2-1,
\qquad p:=a+b,\qquad q:=a-b.
\tag{5}
\]

A negative value of `h_alpha` is possible for some horizontal phases at that frequency **if and only if**

\[
\boxed{|q|<1,}
\tag{6}
\]

that is,

\[
\boxed{
|\cosh(2\pi\alpha y_1)-\cosh(2\pi\alpha y_2)|<1.
}
\tag{7}
\]

Hence unequal heights automatically make all sufficiently high frequencies pointwise safe. The unresolved global obstruction is therefore not unbounded vertical amplification; it is cross-frequency phase coherence inside a quantitatively localized danger band.

## 1. Exact phase-amplitude normal form

Write

\[
\theta_j:=2\pi\alpha t_j,
\qquad
m:=\frac{\theta_1+\theta_2}{2},
\qquad
u:=\frac{\theta_1-\theta_2}{2}=\pi\alpha d,
\]

and abbreviate

\[
C:=\cos\nu,
\qquad S:=\sin\nu.
\tag{8}
\]

Substituting `c_1=1+a`, `c_2=1+b` into (2), and using the half-sum/half-difference identities, gives the exact expression

\[
\boxed{
h_\alpha
=p^2C^2+q^2S^2+4pC^2+pC\cos m-qS\sin m.
}
\tag{9}
\]

Define

\[
R:=\sqrt{p^2C^2+q^2S^2}.
\tag{10}
\]

The last two terms in (9) are the scalar product of `(pC,-qS)` with the unit vector `(cos m,sin m)`. Therefore their exact minimum over the mean phase is `-R`, and

\[
\boxed{
\min_m h_\alpha
=R^2-R+4pC^2.
}
\tag{11}
\]

Equivalently,

\[
\boxed{
h_\alpha
\ge
\left(R-\frac12\right)^2-rac14+4pC^2.
}
\tag{12}
\]

Since `p>=0`, (3) follows immediately. No positivity theorem or asymptotic approximation enters this bound; it is a finite trigonometric identity followed by one Euclidean norm inequality.

The lower constant is sharp. Equality in (12) and then in (3) requires `C=0`, `R=1/2`, and alignment of the mean phase with the negative direction in (9). Because `C=0` gives `R=|q|`, the sharp configurations satisfy

\[
\theta_1-\theta_2\equiv\pi\pmod{2\pi},
\qquad |a-b|=\frac12,
\tag{13}
\]

with the remaining phase chosen to attain the linear minimum. Hyperbolic amplitudes can realize such a mismatch, so `-1/4` cannot be improved as a universal pointwise constant.

## 2. The integrated descent is at most one self-energy unit

Integrating (3) against `J>=0` and using

\[
F(0)=\int J(\alpha)\,d\alpha
\tag{14}
\]

in (1) yields (4). This is global in both heights; it does not use the small-height gate `m_5` from `ANF-037`--`ANF-041`.

For the stated nonzero continuous spectrum the bound is strict. If equality held in (4), then `h_alpha=-1/4` for `J(alpha)dalpha`-almost every frequency. Continuity and nontriviality give an open interval on which `J>0`. The equality conditions above would force

\[
\cos(\pi\alpha d)=0
\tag{15}
\]

throughout that interval, impossible for a cosine of a linear phase. Thus no fixed genuine configuration saturates the integrated floor. No uniform positive gap above `-F(0)` is asserted.

A more localized version is immediate. At every frequency outside the danger set where `h_alpha` can be negative, the integrand is nonnegative, while inside it (3) applies. Hence if `D(W)` denotes any measurable superset of the actual negative-frequency set,

\[
\boxed{
E_F(W)-E_F(R(W))
\ge-\int_{D(W)}J(\alpha)\,d\alpha.
}
\tag{16}
\]

This converts any geometric localization of dangerous phases into a spectral-mass budget.

## 3. Exact amplitude-mismatch barrier

Equation (11) also gives a complete pointwise existence test. Since

\[
R^2=q^2+(p^2-q^2)C^2,
\tag{17}
\]

we have `R>=|q|`. If `|q|>=1`, then `R>=1`, so `R^2-R>=0` and (11) is nonnegative for every `C`. Thus no horizontal phases can make the frequency harmful.

Conversely, if `0<|q|<1`, choose `C=0`. Then `R=|q|`, the positive `4pC^2` term vanishes, and an appropriate mean phase gives

\[
\min_m h_\alpha=q^2-|q|<0.
\tag{18}
\]

If `q=0`, choose any sufficiently small nonzero `|C|`. Then `R=p|C|` and

\[
\min_m h_\alpha
=p|C|\bigl((p+4)|C|-1\bigr)<0
\tag{19}
\]

whenever `0<|C|<1/(p+4)`. This proves the equivalence (6)--(7).

For unequal heights, assume without loss of generality `y_1>y_2`. The mismatch

\[
q(\alpha)
=2\sinh\!\bigl(\pi|\alpha|(y_1+y_2)\bigr)
\sinh\!\bigl(\pi|\alpha|(y_1-y_2)\bigr)
\tag{20}
\]

is strictly increasing for `|alpha|>0`, starts at zero, and tends to infinity. Therefore there is a unique `alpha_*(y_1,y_2)>0` satisfying `q(alpha_*)=1`, and every frequency with

\[
|\alpha|\ge\alpha_*(y_1,y_2)
\tag{21}
\]

is pointwise safe independently of `t_1,t_2`. In particular, using `sinh x>=x`, every potentially negative frequency obeys the simpler necessary bound

\[
\boxed{
|\alpha|<
\frac{1}{\pi\sqrt{2|y_1^2-y_2^2|}}.
}
\tag{22}
\]

Thus increasing the disparity between the two squared heights squeezes all possible negative spectral contribution toward the central band.

## 4. Equal heights localize danger to anti-phase tubes

When `y_1=y_2=y`, the amplitude mismatch vanishes identically, so (22) gives no information. But (19) becomes an exact phase criterion. Here

\[
p=2\bigl(\cosh(2\pi\alpha y)-1\bigr),
\]

and a negative pointwise contribution is possible precisely when

\[
0<|\cos(\pi\alpha d)|
<\frac{1}{p+4}
=\frac{1}{4\cosh^2(\pi\alpha y)}.
\tag{23}
\]

Therefore at large equal height the dangerous frequencies are forced into narrow neighborhoods of the anti-phase loci

\[
\pi\alpha d\equiv\frac\pi2\pmod\pi.
\tag{24}
\]

The two regimes are complementary. Unequal heights localize danger by **amplitude mismatch**, while equal heights localize it by **phase anti-alignment**. Neither mechanism alone proves the integrated defect nonnegative, because the phases at different frequencies are linked by the same physical separation `d`.

## 5. What this changes in the five-point frontier

`ANF-041` left two possibilities for the finite-height two-pair gate: lift the positive-definite coupling to the full hyperbolic transforms, or exhibit a genuine finite-height reversal. The present reduction rules out a third, simpler possibility: there is no frequencywise positivity proof to be had in general. Whenever (7) holds, a single frequency admits horizontal phases with negative defect. In particular, every genuine two-pair configuration has small frequencies where the amplitude condition alone permits negativity.

At the same time, vertical amplification cannot create an arbitrarily deep local well. The total descent is bounded by one self-energy unit, and for unequal heights only the central spectral mass below `alpha_*` can participate at all. This makes the remaining problem a **coherence problem across frequencies**: can one pair of physical horizontal separations align enough of the danger region to make the `J`-weighted integral negative, or does positive-definite/Fourier coherence force compensating positive mass elsewhere?

This is especially relevant to the central-notch separator ray of `ANF-034`. A notch near zero removes spectral weight precisely from the amplitude-danger region for strongly unequal heights, but this observation by itself does not prove that notching is monotone for the full two-pair defect. Equal-height anti-phase tubes remain possible away from zero, and the sign of the removed integrand can depend on geometry. The correct next gate is therefore a coherent integral estimate, not another pointwise sign check.

## 6. Prior art, falsification, and evidence boundary

The only generic ingredient in (9)--(12) is the classical harmonic-amplitude identity that the minimum of `A cos m+B sin m` is `-sqrt(A^2+B^2)`. A targeted check of trigonometric-polynomial and Fourier--Laplace positive-definite literature found the standard harmonic reduction and the already relevant Bochner/Fourier--Laplace framework, but no external theorem is needed for the present claim. No publication-level novelty claim is made, and no new `SOURCES.md` entry is required because every load-bearing step is derived explicitly here.

The result is exact but deliberately limited. It does **not** prove `G_{2,2,1;J}(y_1,y_2)>=0`, does not close the central-notch program, and does not extend the all-height one-pair theorem of `ANF-039` to two pairs. The lower bound (4) is a universal floor, not a sign theorem.

The decisive audit is finite. Expanding (9) must reproduce the `ANF-040` integrand (2); minimizing its last two terms must give (11); completing the square must give (12). The sharpness test is the anti-phase configuration (13). The amplitude criterion is falsified by any example with `|a-b|>=1` and negative `h_alpha`, or by failure to construct negative phases when `|a-b|<1`; equations (18)--(19) settle both directions exactly.

## 7. Consequence for the next gate

Further cardinality-five work should target a cross-frequency inequality for the exact normal form (9), preferably one that combines the positive spectrum with the fact that `m`, `nu`, `a`, and `b` all arise from the same frequency variable rather than being independently selectable. For unequal heights, (20)--(22) reduce the potentially harmful spectrum to a bounded central window whose mass can be estimated directly. For equal or nearly equal heights, the corresponding target is control of the narrow anti-phase tubes (23) under a single linear phase `pi alpha d`.

A successful all-height closure must exploit that coherence. A counterexample, conversely, must place enough `J`-mass in those coherent danger regions to overcome the nonnegative complement while still satisfying the finite-real and curvature gates already imposed by `ANF-034` and `ANF-038`--`ANF-041`.