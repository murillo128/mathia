# WI-272 — positive archimedean tail gives a below-`h_0` prime-overlap criterion

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + CLASSICAL-YOUNG + PRIOR-ART-AUDITED`.
- **Scope:** a quantitative necessary condition on the **one-signed branch** of a hypothetical first unrestricted Suzuki null mode. It extends `WI-271` below the archimedean sign-change length by bounding the remaining positive continuous-source payment exactly by its `L^1` tail mass.
- **What it does not claim:** this is not RH, does not show that the actual first null mode is one-signed, does not force the existence of an internal support gap, and does not control arbitrarily narrow gaps. The sign-changing branch remains governed by the signed-source/nodal machinery of `WI-269`.

## Claim

Assume RH is false and let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be the first unrestricted crossing of Suzuki's localized Weil ground-state energy. Let `v` be a normalized real null mode

\[
\|v\|_2=1,
\qquad A_av=0,
\qquad q_a\ge0,
\tag{1}
\]

and assume the one-signed branch, so after changing sign if necessary

\[
v\ge0\quad\text{a.e.}
\tag{2}
\]

Use the exact continuous source weight from `WI-269`,

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{3}
\]

and let

\[
h_0=\log\rho,
\qquad \rho^3-\rho-1=0.
\tag{4}
\]

Then `w>0` on `(0,h_0)`, `w(h_0)=0`, and `w<0` on `(h_0,\infty)`. Define the positive tail budget

\[
\boxed{
B(L):=\int_L^{\infty}w(h)_+\,dh
=
\begin{cases}
\displaystyle\int_L^{h_0}w(h)\,dh,&0<L<h_0,\\[2mm]
0,&L\ge h_0.
\end{cases}}
\tag{5}
\]

Suppose there is an internal essential-support gap

\[
(\alpha,\beta)\subset(-a,a),
\qquad v=0\ \text{a.e. on }(\alpha,\beta),
\tag{6}
\]

with positive mass on both sides. Put

\[
L=\beta-\alpha>0,
\qquad
M_L=\int_{-a}^{\alpha}v(x)^2dx,
\qquad
M_R=\int_{\beta}^{a}v(x)^2dx,
\tag{7}
\]

and

\[
r_L=\frac{a+\alpha}{2},
\qquad
r_R=\frac{a-\beta}{2}.
\tag{8}
\]

Let `J_{\alpha,\beta}(h)` and the prime-power cross-gap mass `P_{\alpha,\beta}` be exactly as in `WI-271`:

\[
J_{\alpha,\beta}(h)
=\int_{\mathbb R}
\mathbf1_{\{x\le\alpha,\ x+h\ge\beta\}}
 v(x+h)v(x)\,dx,
\tag{9}
\]

\[
P_{\alpha,\beta}
=
\sum_{\substack{L\le\log n<2a\\\Lambda(n)>0}}
\frac{\Lambda(n)}{\sqrt n}
J_{\alpha,\beta}(\log n).
\tag{10}
\]

Then

\[
\boxed{
P_{\alpha,\beta}
\ge
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}
-B(L)\sqrt{M_LM_R}.
}
\tag{11}
\]

Consequently the mass-independent sufficient condition

\[
\boxed{B(L)<\sqrt{\lambda_{r_L}\lambda_{r_R}}}
\tag{12}
\]

forces

\[
P_{\alpha,\beta}>0,
\tag{13}
\]

and therefore at least one active prime power satisfies

\[
L\le\log n<2a,
\qquad
\boxed{C_v(\log n)>0.}
\tag{14}
\]

For `L\ge h_0`, `B(L)=0`, so (11) recovers `WI-271` exactly. For `L<h_0`, it gives a strict extension whenever the positive archimedean tail is too small to pay the proper-aperture firstness cost.

Under **complete prime screening**,

\[
C_v(\log n)=0
\qquad
(\Lambda(n)>0,\ \log n<2a),
\tag{15}
\]

one-signedness implies `P_{\alpha,\beta}=0`, and every internal gap must satisfy the stronger pair of exact constraints

\[
\boxed{
B(L)
\ge
\lambda_{r_L}\sqrt{\frac{M_L}{M_R}},
\qquad
B(L)
\ge
\lambda_{r_R}\sqrt{\frac{M_R}{M_L}}.
}
\tag{16}
\]

Equivalently,

\[
\boxed{
\frac{\lambda_{r_R}}{B(L)}
\le
\sqrt{\frac{M_L}{M_R}}
\le
\frac{B(L)}{\lambda_{r_L}},
}
\tag{17}
\]

which is possible only if

\[
\boxed{B(L)^2\ge\lambda_{r_L}\lambda_{r_R}.}
\tag{18}
\]

Thus complete screening constrains not only the width of every internal gap but also the allowable left/right mass imbalance.

## 1. The exact cross-gap identity from `WI-271`

Choose a bounded Lipschitz multiplier `chi` that is zero on the left of the gap, one on the right, and transitions only inside `(\alpha,\beta)`. Since `v=0` on the transition region,

\[
\chi v=v_R,
\qquad
(1-\chi)v=v_L,
\tag{19}
\]

where `v_L` and `v_R` are the exact left and right pieces. The `WI-269` ground-state transform then gives the common side energy

\[
q_a(v_L)=q_a(v_R)=:Q_{\alpha,\beta}
\tag{20}
\]

with

\[
Q_{\alpha,\beta}
=
P_{\alpha,\beta}
+
\int_L^{2a}w(h)J_{\alpha,\beta}(h)\,dh.
\tag{21}
\]

Firstness and translation invariance give

\[
\boxed{
Q_{\alpha,\beta}
\ge
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}
>0.
}
\tag{22}
\]

No new operator-domain step is needed here; (20)--(22) are the exact gap compression already established in `WI-271`.

## 2. Young's inequality measures exactly how much positive source remains below `h_0`

Because `v\ge0`,

\[
J_{\alpha,\beta}(h)\ge0.
\tag{23}
\]

The part of (21) with `h>h_0` is therefore nonpositive. Hence

\[
Q_{\alpha,\beta}
\le
P_{\alpha,\beta}
+
\int_L^{h_0}w(h)J_{\alpha,\beta}(h)\,dh,
\tag{24}
\]

with the last integral understood as zero if `L\ge h_0`.

Extend `v_L,v_R` by zero to the real line and define

\[
K_L(h)=w(h)\mathbf1_{[L,h_0]}(h)
\tag{25}
\]

when `L<h_0`, and `K_L=0` otherwise. The positive cross-gap term can be written as the bilinear convolution pairing

\[
\int_L^{h_0}w(h)J_{\alpha,\beta}(h)\,dh
=
\langle v_R,K_L*v_L\rangle.
\tag{26}
\]

Cauchy--Schwarz followed by the classical `L^1*L^2\to L^2` Young inequality gives

\[
\begin{aligned}
\langle v_R,K_L*v_L\rangle
&\le \|v_R\|_2\,\|K_L*v_L\|_2\\
&\le \|K_L\|_1\,\|v_L\|_2\,\|v_R\|_2\\
&=B(L)\sqrt{M_LM_R}.
\end{aligned}
\tag{27}
\]

This is the only new analytic estimate. In this endpoint case Young's inequality has constant one and follows directly from Minkowski's integral inequality, so no numerical or asymptotic input is hidden in (27).

Combining (22), (24), and (27) proves (11).

## 3. Screening forces a width--mass compatibility law

The elementary inequality

\[
\max\{x,y\}\ge\sqrt{xy}
\tag{28}
\]

applied to the two firstness terms in (11) yields

\[
P_{\alpha,\beta}
\ge
\left(
\sqrt{\lambda_{r_L}\lambda_{r_R}}-B(L)
\right)\sqrt{M_LM_R}.
\tag{29}
\]

Both masses are positive. Thus (12) forces (13). Since every term of `P_{\alpha,\beta}` is nonnegative, some active prime-power cross-gap term is positive, and because `v\ge0`,

\[
C_v(\log n)\ge J_{\alpha,\beta}(\log n)>0.
\]

This proves (14).

For a quantitative autocorrelation bound, define as in `WI-271`

\[
W_a(L)
:=
\sum_{\substack{L\le\log n<2a\\\Lambda(n)>0}}
\frac{\Lambda(n)}{\sqrt n}.
\tag{30}
\]

Whenever the right side of (11) is positive, `W_a(L)>0` automatically and

\[
\boxed{
\max_{\substack{L\le\log n<2a\\\Lambda(n)>0}}
C_v(\log n)
\ge
\frac{
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}
-B(L)\sqrt{M_LM_R}
}{W_a(L)}.
}
\tag{31}
\]

Under complete screening, `P_{\alpha,\beta}=0`; rearranging (11) separately against each firstness term gives (16)--(17), and multiplying the two inequalities in (16) gives (18).

The mass-ratio constraint is useful because a screened gap cannot evade the width tariff merely by putting almost all `L^2` mass on one side. Making `M_L/M_R` large relaxes the right-side inequality only while simultaneously tightening the left-side one.

## 4. The hard threshold `h_0` has a quadratic collar, not a jump

The positive-source budget tends to zero smoothly as `L` approaches `h_0` from below. Since

\[
\frac{d}{dh}\log\left(\frac{e^{-5h/2}}{1-e^{-2h}}\right)
=-\frac52-\frac{2e^{-2h}}{1-e^{-2h}}<0,
\]

one has `w'(h)<0` for every `h>0`. At `h_0=\log\rho`, the relation `\rho^3-\rho-1=0` gives

\[
\frac1{\rho^2-1}=\rho,
\qquad
w'(h_0)=-\sqrt\rho\,(3+2\rho).
\tag{32}
\]

Therefore

\[
\boxed{
B(L)
=
\frac{\sqrt\rho(3+2\rho)}{2}
(h_0-L)^2
+O\!\left((h_0-L)^3\right)
\qquad(L\uparrow h_0).
}
\tag{33}
\]

Numerically `h_0=0.2811995743...`, and the quadratic coefficient in (33) is `3.2511484678...`; the theorem itself does not use these decimals.

This shows that `WI-271`'s sign-change threshold is not a discontinuous barrier. For any fixed proper-aperture side energies `\lambda_{r_L},\lambda_{r_R}>0`, there is a strict interval below `h_0` in which a screened gap is impossible. More uniformly, if both side radii satisfy

\[
r_L,r_R\le a-\delta
\tag{34}
\]

for some `\delta>0`, monotonicity of the ground-state energy gives

\[
\sqrt{\lambda_{r_L}\lambda_{r_R}}
\ge\lambda_{a-\delta}>0.
\tag{35}
\]

Hence every completely screened gap with this endpoint margin must satisfy

\[
B(L)\ge\lambda_{a-\delta}.
\tag{36}
\]

Because `B(L)\to0` quadratically at `h_0`, (36) excludes a uniform collar immediately below `h_0` for every fixed `\delta`.

## 5. Barrier of the same argument at very small gaps

The present improvement deliberately does not claim that every positive-width gap forces arithmetic overlap. Near zero,

\[
w(h)=\frac1{2h}+O(1),
\qquad h\downarrow0,
\tag{37}
\]

so

\[
B(L)\sim\frac12\log\frac1L
\qquad(L\downarrow0).
\tag{38}
\]

Thus the generic `L^1` convolution budget becomes arbitrarily large for very narrow gaps. No refinement of (27) that only keeps `\|K_L\|_1` and the two total side masses can produce a uniform positive lower bound on the gap width. To attack the narrow-gap or gapless one-signed regime one must use more local information about `v`, a sharper source-conditioned operator norm, or the full family of cut/multiplier constraints rather than this scalar tail mass alone.

This is an exact limitation of the present route, not evidence that such screened narrow gaps actually exist.

## 6. Prior art and novelty boundary

Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), supplies the localized Weil operator and source decomposition used through the already-audited `WI-253`, `WI-269`, and `WI-271` interfaces. The present finding does not add a claim about Suzuki's operator itself.

The estimate (27) is the classical Young convolution inequality in its endpoint form `L^1*L^2\to L^2`; its constant one is elementary and is rederived above. General nonlocal ground-state representations and signed-kernel cut arguments are neighboring classical mechanisms already audited in `WI-269`/`WI-270`. The prior-art audit located Suzuki's operator framework and general Young/nonlocal-ground-state theory but no theorem identifying the zeta-specific positive source tail `B(L)` as the exact screening budget for an internal first-crossing gap. This absence is audit context only; no priority claim is made.

The Mathia deduction is the source-specific combination of four already-rigorous ingredients: the exact cross-gap multiplier identity, strict proper-aperture firstness, the unique sign change of `w`, and the sharp `L^1*L^2` convolution bound. Its new content is (11), the screening compatibility law (16)--(18), and the quadratic below-`h_0` collar (33).

## Falsification and audit test

The load-bearing steps are explicit:

1. the smooth transition inside a genuine zero gap gives the exact cross-gap identity (21), as in `WI-271`;
2. one-signedness gives `J_{\alpha,\beta}(h)\ge0`, so the `h>h_0` source contribution is nonpositive;
3. the positive remainder is exactly the bilinear convolution (26), with no factor of two;
4. Young's inequality gives (27) with `\|K_L\|_1=B(L)`;
5. firstness supplies (22) with strictly positive `\lambda_r` for every proper aperture;
6. complete prime screening plus `v\ge0` makes every prime cross-gap term vanish.

An error in any one of these implications invalidates the finding. A sharper bound on the positive convolution term would strengthen it; a construction that saturates the `B(L)` budget while satisfying Suzuki's null equation would identify the true remaining one-signed escape geometry.

## Consequence for the research line

The one-signed screening problem is no longer separated by a hard geometric dichotomy at `L=h_0`. Every internal gap carries a continuous source budget `B(L)`: prime screening is possible only when that budget is large enough to dominate the geometric mean of the two proper-aperture firstness energies, with the side masses constrained by (17).

The next one-signed gate is therefore sharper. Either derive from the full cut/null-equation family a gap or bottleneck for which `B(L)` is too small, or construct a genuine one-signed screened first mode whose support remains sufficiently connected and whose local mass profile pays the singular short-range source at every cut. The sign-changing branch remains separate and should continue through the PSD/nodal compensation interface of `WI-269`.