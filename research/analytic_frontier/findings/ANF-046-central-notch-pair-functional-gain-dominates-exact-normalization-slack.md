# ANF-046 — central-notch pair-functional gain dominates exact normalization slack

**Status:** `EXACT-DERIVED + AFFINE-SLACK-SURVIVOR + CENTRAL-NOTCH + NECESSARY-CONSTRAINT-CLOSURE + STRUCTURAL-BOUNDARY`. `ANF-005` shows that every universal signed affine support-one certificate must pay a deterministic normalization slack `delta`, and that beating Montgomery--Taylor requires

\[
M(F)+\delta<m_{\rm MT},
\qquad m_{\rm MT}=C_{\rm MT}-1.
\tag{1}
\]

`ANF-034` later constructs an explicit positive-spectrum finite-real separator by removing a narrow central tent from the exact Montgomery--Taylor spectrum,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\phi_\eta(\alpha)=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\tag{2}
\]

with `0<eta<1`, `0<b_eta<=1`, `0<=phi_eta<=J_MT`, and arbitrarily small admissible `s>0`. That finding proves that the spatial kernel `F_s=widehat J_s` must change sign, but leaves open whether the compulsory affine slack already erases the pair-functional gain before any genuinely complex configuration is tested.

It does not. The tent has an exact nonnegative sinc-square transform, and this makes the normalization tradeoff completely explicit. For every sufficiently small width

\[
\boxed{0<\eta<3-\sqrt6=0.5505102572\ldots,}
\tag{3}
\]

the central-notch ray satisfies all one-point, two-point, imaginary-pair, double-point, and real high-multiplicity necessary conditions from `ANF-005` at its **smallest possible deterministic slack**, while still obeying the strict objective inequality (1). Thus the cheapest affine-normalization obstruction does not kill the notch. Any failure of this ray must come from stronger conjugation-invariant complex configurations or from failure of a full universal counting inequality, exactly the layer isolated in `ANF-036`--`ANF-045`.

## 1. The central tent has a positive sinc-square spatial kernel

Use the Fourier convention of the line,

\[
\widehat f(x)=\int_{\mathbb R}f(\alpha)e^{-2\pi i\alpha x}\,d\alpha.
\]

The triangular profile in (2) is a normalized convolution of two interval indicators, so its Fourier transform is exactly

\[
\boxed{
\Phi_\eta(x):=\widehat{\phi_\eta}(x)
=b_\eta\eta
\left(\frac{\sin(\pi\eta x)}{\pi\eta x}\right)^2
\ge0,
}
\tag{4}
\]

with the continuous value `Phi_eta(0)=b_eta eta`. In particular,

\[
0\le\Phi_\eta(x)\le b_\eta\eta
\qquad(x\in\mathbb R).
\tag{5}
\]

`ANF-030` gives the exact Montgomery--Taylor spatial kernel

\[
R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
R_{\rm MT}(0)=1.
\tag{6}
\]

Therefore

\[
F_s(x)=R_{\rm MT}(x)-s\Phi_\eta(x)
\tag{7}
\]

satisfies the global real-axis bound

\[
\boxed{F_s(x)\ge-sb_\eta\eta.}
\tag{8}
\]

At the origin the value is exact:

\[
\boxed{d_s:=F_s(0)=1-sb_\eta\eta.}
\tag{9}
\]

Put

\[
\boxed{\delta_s:=sb_\eta\eta.}
\tag{10}
\]

Then `d_s=1-delta_s`.

## 2. `delta_s` is the exact minimum slack allowed by the elementary universal tests

For a universal affine certificate

\[
s(Z)\ge A|Z|-E_{F_s}(Z),
\]

`ANF-005` defines

\[
\delta=1+F_s(0)-A
\]

and derives necessary conditions from finite conjugation-invariant multisets. The double real point already forces

\[
F_s(0)\ge1-\delta.
\tag{11}
\]

Using (9), every such certificate with the unscaled notch kernel therefore satisfies

\[
\boxed{\delta\ge\delta_s.}
\tag{12}
\]

This lower bound is simultaneously sufficient for **all of the elementary necessary tests in `ANF-005`**. At `delta=delta_s`, equation (8) gives the distinct-real two-point constraint

\[
F_s(t)\ge-\delta_s.
\tag{13}
\]

Because `J_s>=0` is even,

\[
F_s(iy)
=\int J_s(\alpha)\cosh(2\pi\alpha y)\,d\alpha
\ge\int J_s(\alpha)\,d\alpha
=F_s(0)
=1-\delta_s,
\tag{14}
\]

so the nonreal conjugate-pair constraint also holds. The singleton condition is simply `delta_s>=0`, and the double-real-point inequality (11) is saturated.

Finally, the high-multiplicity real constraint of `ANF-005` asks only for copositivity of every real translation Gram. Here one has the stronger positive-semidefinite identity

\[
\boxed{
\sum_{i,j}c_ic_jF_s(x_i-x_j)
=
\int J_s(\alpha)
\left|\sum_i c_i e^{-2\pi i\alpha x_i}\right|^2d\alpha
\ge0
}
\tag{15}
\]

for arbitrary real coefficients `c_i`, because `J_s>=0`. Hence all real translation Grams are PSD, not merely copositive.

Thus

\[
\boxed{
\delta_{\min}^{\rm elementary}(F_s)=\delta_s=sb_\eta\eta.
}
\tag{16}
\]

The minimum is forced by the lost diagonal mass `F_s(0)`, not by an uncontrolled negative real excursion. In particular, the sign change proved in `ANF-034` introduces no larger cost at this level.

## 3. The exact pair-functional gain is larger than that slack for a narrow notch

For a support-one spectrum `J`, `ANF-005` gives

\[
M(\widehat J)=C(J)-\widehat J(0),
\qquad
C(J)=J(0)+\int_{-1}^{1}|\alpha|J(\alpha)\,d\alpha.
\tag{17}
\]

The tent has the exact moments

\[
\phi_\eta(0)=b_\eta,
\qquad
\int_{-1}^{1}|\alpha|\phi_\eta(\alpha)\,d\alpha
=\frac{b_\eta\eta^2}{3},
\tag{18}
\]

and therefore

\[
C(\phi_\eta)
=b_\eta\left(1+\frac{\eta^2}{3}\right).
\tag{19}
\]

Since `C(J_MT)=C_MT`, equations (2) and (19) give

\[
C(J_s)
=C_{\rm MT}
-sb_\eta\left(1+\frac{\eta^2}{3}\right).
\tag{20}
\]

Combining (9), (17), and (20),

\[
\boxed{
M(F_s)
=m_{\rm MT}
-sb_\eta\left(1-\eta+\frac{\eta^2}{3}\right).
}
\tag{21}
\]

Now add the **minimum possible** elementary normalization slack (10):

\[
\boxed{
M(F_s)+\delta_s
=m_{\rm MT}
-sb_\eta\left(1-2\eta+\frac{\eta^2}{3}\right).
}
\tag{22}
\]

The coefficient is positive precisely when

\[
\eta^2-6\eta+3>0.
\]

Inside the relevant interval `0<eta<1`, this is equivalent to (3). Hence every positive `s` gives

\[
\boxed{
M(F_s)+\delta_s<m_{\rm MT}
\qquad
(0<\eta<3-\sqrt6).
}
\tag{23}
\]

The scale separation is structural. Removing a very narrow central tent lowers the pair-correlation functional by order `s b_eta`, because `C(J)` contains the point value `J(0)`. The compulsory affine slack is only order `s b_eta eta`, because it is controlled by the **integral mass** removed from the spectrum. Thus

\[
\frac{\delta_s}{m_{\rm MT}-M(F_s)}
=
\frac{\eta}{1-\eta+\eta^2/3}
\longrightarrow0
\qquad(\eta\downarrow0).
\tag{24}
\]

No optimization of the cheap normalization test can reverse this asymptotic advantage.

## 4. The finite-real separator and the complex curvature gates can be satisfied simultaneously

`ANF-034` allows the central width `eta` to be chosen arbitrarily small before choosing `L`, `delta`, and finally an arbitrarily small positive `s` on the separator ray. Therefore condition (3) can be imposed without changing that construction. For such a width, choose `s` small enough to satisfy the finite-real separation conditions of `ANF-034`. Then the same profile simultaneously has

\[
\frac{C(J_s)}{q_{\rm real}(J_s)}<C_{\rm MT}
\tag{25}
\]

and the strict affine necessary objective (23).

One can impose the five-point curvature margin at the same time. `ANF-038` shows that after fixing the notch width, taking `s` still smaller so that, for example,

\[
s\eta^3<0.009
\tag{26}
\]

keeps `m_5(J_s)>0`. Consequently there are central-notch profiles which simultaneously

- beat the Montgomery--Taylor ratio on every finite real configuration;
- beat the `ANF-005` objective after paying the exact minimum elementary deterministic slack;
- have positive spectrum and therefore PSD real translation Grams;
- pass the global one-conjugate-pair five-point gate of `ANF-039` and the local two-pair gate of `ANF-040`--`ANF-041`.

The remaining cardinality-five issue is therefore genuinely the finite-height, two-conjugate-pair coherence problem compactified and scalarized in `ANF-043`--`ANF-045`. It is not an artifact of having postponed an obvious normalization penalty.

## 5. Prior art, falsification, and evidence boundary

No new external theorem is load-bearing. The Montgomery--Taylor extremizer and pair-functional identity are already anchored in `SOURCES.md` through Carneiro--Chandee--Littmann--Milinovich, while the positivity/Gram representation is the same elementary Fourier-positive structure used throughout `ANF-012` and `ANF-041`. A targeted check of the neighboring bandlimited extremal, positive-definite, and semidefinite pair-correlation literature found the expected general frameworks but no external result is needed for (4), (16), or (22). No publication-level novelty claim is made, and no new `SOURCES.md` entry is required.

The proof has three direct audit points. First, (4) follows from writing the triangle as a normalized convolution of two interval indicators; a Fourier-normalization error would immediately change both `Phi_eta(0)` and the slack. Second, the exactness in (16) depends on both directions: the double real point forces `delta>=1-F_s(0)`, while (8), (14), and (15) verify every elementary `ANF-005` constraint at equality. Third, the objective calculation is only the linear identity (17) plus the tent moment (18); the threshold in (3) is the smaller root of `eta^2-6eta+3=0`.

This finding is **not** a universal affine counting theorem. Conditions (3)--(7) of `ANF-005` are necessary, not sufficient, and (23) proves only that the central notch survives them with room to spare. It does not prove nonnegativity of the finite-height two-pair defect from `ANF-045`, does not control larger conjugation-invariant multisets, and does not by itself improve the unconditional zeta-zero proportion. A stronger complex configuration may still force additional slack or directly violate the desired affine inequality.

## 6. Decisive next gate

The normalization-slack branch is now quantitatively settled for the central-notch candidate: the unavoidable elementary cost is exactly `s b_eta eta`, and for a narrow notch it is parametrically smaller than the pair-functional gain. Further work should therefore not spend effort trying to kill this ray with the one-/two-point or real-copositivity tests of `ANF-005`.

The next decisive scalar test remains the compact coherence inequality isolated in `ANF-045`,

\[
\kappa_*(y_1,y_2,d)
\le
x(y_1,y_2,d)+\frac{p(y_1,y_2,d)}{x(y_1,y_2,d)},
\tag{27}
\]

for a Montgomery--Taylor-compatible narrow notch on the obstruction box supplied by `ANF-044`. A proof would remove every new cardinality-five complex restriction beyond the real-collapse tests; a violating interior shape would give the first genuinely finite-height complex obstruction. Either outcome would now address the actual surviving mechanism rather than a normalization effect already shown to be too small.