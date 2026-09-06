# ANF-073 — two doubled real sites puncture the minimum-slack central-notch ray

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY-OBSTRUCTION + NORMALIZATION-REDIRECT + SHAPE-RATIO-GATE`. `ANF-036` explicitly left real multiplicity tests open even though all conjugation-invariant configurations of cardinality at most four collapse to them, while `ANF-046` showed only that the central-notch profile survives the elementary one-/two-point, isolated-double, imaginary-pair, and high-multiplicity tests at the slack `delta_s=s b_eta eta`. The missing finite-multiplicity test is already decisive for that *minimum-slack* candidate: two distinct doubled real sites force a stronger exact inequality. Consequently every central-notch profile constructed by `ANF-034` fails the affine certificate with `A_s=2-2 delta_s` at cardinality four, before any five- or six-point complex geometry is relevant.

More generally, if

\[
s(Z)\ge A|Z|-E_F(Z),
\qquad
E_F(Z)=\sum_{z,w\in Z}F(z-w),
\tag{1}
\]

is to hold for every finite conjugation-invariant multiset and

\[
d:=F(0),
\qquad
\delta:=1+d-A,
\qquad
m_{\mathbb R}(F):=\inf_{t\in\mathbb R}F(t),
\tag{2}
\]

then the two-doubled-site family gives the necessary condition

\[
\boxed{
\delta\ge 1-d-2m_{\mathbb R}(F).
}
\tag{3}
\]

For the notch profile

\[
F_s=R_{\rm MT}-s\Phi_\eta,
\qquad
\Phi_\eta(t)=b_\eta\eta
\left(\frac{\sin(\pi\eta t)}{\pi\eta t}\right)^2,
\qquad
F_s(0)=1-\delta_s,
\quad
\delta_s=s b_\eta\eta,
\tag{4}
\]

every genuine Montgomery--Taylor zero `z in Z_MT` with `Phi_eta(z)>0` satisfies

\[
F_s(z)=-s\Phi_\eta(z)<0.
\tag{5}
\]

At the minimum elementary slack `delta=delta_s`, equation (3) would require `F_s(t)>=0` on the whole real axis. Hence the sign change that powers the finite-real separator is itself incompatible with the unadjusted affine intercept once this four-point multiplicity test is admitted.

## 1. Exact four-point multiplicity inequality

Fix a nonzero real number `t` and take the real multiset

\[
Z_t=\{0,0,t,t\}.
\tag{6}
\]

It has cardinality four and no simple elements. Its ordered pair energy is

\[
E_F(Z_t)=8d+8F(t):
\tag{7}
\]

there are eight same-site ordered pairs, contributing `d`, and eight cross-site ordered pairs, contributing `F(t)`. Applying (1) gives

\[
0\ge 4A-8d-8F(t),
\]

or

\[
A\le 2d+2F(t).
\tag{8}
\]

Substitute `A=1+d-delta` from (2). Then

\[
\boxed{
F(t)\ge\frac{1-d-\delta}{2}
\qquad(t\ne0).
}
\tag{9}
\]

Taking the infimum over `t` proves (3). This condition is independent of spectral positivity; it follows solely from the universal deterministic counting inequality. It is therefore a genuine finite-multiplicity constraint, not a Gram-positivity surrogate.

Equation (9) is strictly stronger than the distinct-simple two-point bound `F(t)>=-delta` from `ANF-005` whenever the diagonal has already consumed part of the slack. In particular, if the isolated double point saturates its necessary condition,

\[
\delta=1-d,
\tag{10}
\]

then (9) becomes

\[
\boxed{F(t)\ge0\quad\text{for every real }t.}
\tag{11}
\]

Thus a real-axis sign change and saturation of the isolated-double slack cannot coexist in a universal affine certificate.

This does not contradict `ANF-046`: that finding explicitly certifies the listed elementary tests from `ANF-005`, not all finite real multiplicity patterns, and `ANF-036` records that the latter remained open. The new point is that the first omitted pattern is only `{0,0,t,t}`.

## 2. The explicit `ANF-034` notch is falsified at its minimum slack

For the central-notch profile, `ANF-046` gives

\[
d_s=1-\delta_s,
\qquad
A_s=1+d_s-\delta_s=2-2\delta_s.
\tag{12}
\]

Let `z_1` be the first positive zero of the Montgomery--Taylor kernel. `ANF-031` gives

\[
z_1=1+\frac{\varepsilon_1}{\pi},
\qquad
0<\varepsilon_1<\frac\pi4,
\tag{13}
\]

and hence

\[
1<z_1<\frac54.
\tag{14}
\]

The finite-real separator construction of `ANF-034` chooses `eta` and an auxiliary cutoff `L_0` so that

\[
B_{\eta,L_0}
=\frac4{c_0}\left(\eta+\frac4{L_0}\right)
<a_{\rm MT},
\qquad
c_0=\int_{-1}^{1}
\left(\frac{\sin\pi u}{\pi u}\right)^2du,
\qquad
a_{\rm MT}=C_{\rm MT}^{-1}.
\tag{15}
\]

This condition itself forces the notch to be narrow. Indeed `c_0<1`, because the full-line integral of the squared normalized sinc equals one and the integrand is positive outside `[-1,1]`. Also

\[
C_{\rm MT}
=\frac12+\theta\cot\theta>\frac54,
\qquad
\theta=2^{-1/2},
\tag{16}
\]

since `sin theta<theta` and `cos theta>1-theta^2/2=3/4`. Therefore `a_MT<4/5`, and (15) implies

\[
\boxed{0<\eta<\frac15.}
\tag{17}
\]

Combining (14) and (17),

\[
0<\pi\eta z_1<\frac\pi4.
\tag{18}
\]

Hence `Phi_eta(z_1)>0`. In fact the normalized sinc is strictly decreasing on `(0,pi)`, so

\[
p_\eta(z_1)
:=\left(\frac{\sin(\pi\eta z_1)}{\pi\eta z_1}\right)^2
>
\left(\frac{\sin(\pi/4)}{\pi/4}\right)^2
=\frac8{\pi^2}.
\tag{19}
\]

Since `R_MT(z_1)=0`,

\[
F_s(z_1)
=-\delta_s p_\eta(z_1)<0.
\tag{20}
\]

Now evaluate the affine slack of

\[
Z_{z_1}=\{0,0,z_1,z_1\}
\tag{21}
\]

at the candidate intercept `A_s`:

\[
\begin{aligned}
\mathcal S_s(Z_{z_1})
&:=s(Z_{z_1})-A_s|Z_{z_1}|+E_{F_s}(Z_{z_1})\\
&=8F_s(0)+8F_s(z_1)-4A_s\\
&=-8\delta_s p_\eta(z_1).
\end{aligned}
\tag{22}
\]

Therefore

\[
\boxed{
\mathcal S_s(Z_{z_1})
< -\frac{64}{\pi^2}\,\delta_s<0.
}
\tag{23}
\]

This is a finite exact falsifier. No limiting configuration, interval computation, curvature expansion, or complex displacement is needed. It applies for every `s>0` on every width admitted by the explicit `ANF-034` separator construction.

Consequently the later five- and six-point analyses at the fixed intercept `A_s=2-2delta_s` remain valid as conditional geometry, but they cannot certify universality of that unadjusted candidate: the candidate has already failed on the real four-point multiset (21).

## 3. The correct normalization gate is a real-multiplicity ratio

The obstruction does not by itself kill the *shape* `F_s`, because the affine intercept and the overall spectral amplitude may be reoptimized. Equation (3) supplies the correct first scale-free gate.

Let a fixed real-even shape `F` have

\[
d=F(0),
\qquad
m=m_{\mathbb R}(F),
\qquad
M=M(F),
\tag{24}
\]

and scale it by `lambda>0`. The pair functional becomes `lambda M`, while (3) forces

\[
\delta_\lambda
\ge
1-\lambda(d+2m).
\tag{25}
\]

Together with the singleton condition `delta_lambda>=0`, every amplitude on the ray obeys

\[
\boxed{
\lambda M+\delta_\lambda
\ge
\lambda M+\max\{0,1-\lambda(d+2m)\}.
}
\tag{26}
\]

If

\[
D_2(F):=d+2m>0,
\qquad
0\le M<D_2(F),
\tag{27}
\]

then the right side of (26) is minimized exactly at

\[
\lambda=D_2(F)^{-1},
\]

and its minimum is

\[
\boxed{
\frac{M(F)}{D_2(F)}.
}
\tag{28}
\]

If `M>=D_2>0`, the infimum of the right side is at least one, so the ray is automatically useless for a sub-Montgomery--Taylor objective. Thus any amplitude-rescaled shape that could still beat Montgomery--Taylor after the doubled-site test must satisfy the necessary ratio condition

\[
\boxed{
\frac{M(F)}{F(0)+2\inf_{\mathbb R}F}<m_{\rm MT}.
}
\tag{29}
\]

The denominator is a finite-multiplicity analogue of the real-energy floors in `ANF-017`: it records the most dangerous pair of doubled real sites rather than a distinct real set and its global duplication.

For the central notch, the explicit zero `z_1` yields

\[
m_{\mathbb R}(F_s)\le -\delta_s p_\eta(z_1),
\]

so

\[
D_2(F_s)\le
1-\delta_s\bigl(1+2p_\eta(z_1)\bigr).
\tag{30}
\]

Equivalently, at fixed unscaled amplitude the doubled-site test forces

\[
\boxed{
\delta\ge
\delta_s\bigl(1+2p_\eta(z_1)\bigr)
>
\delta_s\left(1+\frac{16}{\pi^2}\right).
}
\tag{31}
\]

So the true deterministic slack is already more than a factor `1+16/pi^2` larger than the elementary minimum on the `ANF-034` widths. This is the normalization quantity that must be paid before further complex-configuration tests are meaningful.

## 4. What is closed and what remains open

The exact conclusion is deliberately narrower than a no-go for every central notch. What is closed is the **minimum-elementary-slack candidate** used in the post-`ANF-046` chain: `A_s=2-2delta_s` cannot be universal because (21) violates it. The finite-real separator over distinct sets does not protect against this failure; repeated real sites carry different simple-point bookkeeping and expose the negative spatial value directly.

A reoptimized central-notch shape may still survive. For very narrow `eta`, the pair-functional gain in `ANF-046` is order `s b_eta`, whereas the extra doubled-site slack in (31) is only order `s b_eta eta`. Therefore (31) alone does not justify claiming that the entire notch family is below the Montgomery--Taylor objective after amplitude optimization. That stronger statement would require solving the real-multiplicity envelope, not merely finding one additional constraint.

The research order should therefore change. Before extending the five-/six-point complex calculations, determine the sharp real-multiplicity normalization functional for `J_s`: begin with the exact denominator `D_2(F_s)` in (29), then test whether larger finite multiplicity patterns force a still smaller scale-free denominator. Only a shape that remains below `m_MT` after this multiplicity optimization warrants renewed complex-geometry analysis.

## 5. Prior art and evidence boundary

The load-bearing external inputs are unchanged: the Montgomery--Taylor / Carneiro--Chandee--Littmann--Milinovich extremizer and its explicit zero set are already anchored in `SOURCES.md`, while `ANF-031` independently derives the branchwise zero description and records the closely related public-artifact sum-free argument. The doubled-site inequality (8)--(9) is a direct finite-multiset calculation from the universal affine certificate and needs no external theorem.

A targeted check of current simple-zero work, multiplicity-aware formalizations, finite Montgomery--Taylor gap certificates, and the public `ainta/zeta-simple-zeros` artifact found the expected use of multiplicities and Montgomery--Taylor overlap zeros, but no separate result was located that supplies the specific two-doubled-site slack identity (3) or the central-notch consequence (22). No publication-level novelty claim is made, and no new `SOURCES.md` entry is load-bearing.

The finding does **not** refute `ANF-034` as a distinct-real separator, does not contradict the restricted elementary-test statement of `ANF-046`, and does not invalidate the algebraic energy comparisons in `ANF-062`--`ANF-072`. It changes their role in the universal-affine program: at the previously chosen intercept, a cheaper real-multiplicity falsifier must be repaired first.

## 6. Next decisive test

The cheapest decisive continuation is now one-dimensional in the kernel rather than higher-dimensional in point geometry. For each objective-compatible notch width, determine or rigorously bound

\[
m_{\mathbb R}(F_s)=\inf_{t\in\mathbb R}F_s(t)
\tag{32}
\]

and evaluate the amplitude-optimized ratio (29). If that ratio is already at least `m_MT`, the central-notch shape is dead by four-point real multiplicity alone. If it remains strictly below `m_MT`, the next task is to characterize whether any larger real multiplicity pattern strengthens `D_2` enough to erase the remaining gain. Complex five-/six-point tests should be revisited only after that real-multiplicity normalization gate is passed.