# ANF-071 — central-notch-induced six-point reversal is confined to a thin curvature-height layer

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH-PERTURBATION + SIX-POINT-COMPACTIFICATION + STRUCTURAL-REDUCTION`. `ANF-070` closes the complete one-pair/four-real-anchor branch whose **base Montgomery--Taylor** profile already reverses real collapse. The unresolved six-point possibility is therefore a reversal created by the notch itself from a horizontal configuration for which the base curvature coefficient is nonnegative. That residual mechanism is much thinner than an arbitrary finite-height perturbation.

Let
\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\phi_\eta(\alpha)=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad
0<\eta<1,\quad 0<s<1,
\]
with `0<b_eta<=1` and `0<=phi_eta<=J_MT` as in `ANF-034` and `ANF-046`. For four distinct nonzero real anchors `T={t_1,t_2,t_3,t_4}`, put
\[
W_{y,T}=\{iy,-iy,t_1,t_2,t_3,t_4\},
\qquad
R_T=\{0,0,t_1,t_2,t_3,t_4\}.
\]
Write
\[
K(t)=\int\alpha^2J_{\rm MT}(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad
D(T)=2K(0)+\sum_{j=1}^4K(t_j),
\]
and let `K_s,D_s` denote the same quantities for `J_s`.

If the base profile is nonreversing,
\[
D(T)\ge0,
\]
but the notched profile reverses real collapse at some positive height,
\[
E_{\widehat J_s}(W_{y,T})<E_{\widehat J_s}(R_T),
\]
then necessarily
\[
\boxed{
0\le D(T)<s b_\eta\eta^3,
}
\tag{1}
\]
and
\[
\boxed{
0<-D_s(T)\le s b_\eta\eta^3.
}
\tag{2}
\]
Moreover every such reversing height satisfies
\[
\boxed{
y^2<
\frac{3s b_\eta\eta^3}
{4\pi^2\left(M_2(0)-s b_\eta\eta^5/15\right)},
}
\tag{3}
\]
where
\[
M_2(0)=\int\alpha^4J_{\rm MT}(\alpha)\,d\alpha
>0.05854458579969
\]
is the canonical Montgomery--Taylor fourth spectral moment from `ANF-038`/`ANF-069`.

Thus a notch cannot create a new one-pair six-point collapse reversal deep inside the base-nonreversing region. The only new branch is squeezed against the base curvature boundary `D=0` at width `O(s b_eta eta^3)`, and its vertical height tends to zero at rate
\[
y=O\!\left(\sqrt{s b_\eta\eta^3}\right)
\qquad(s\downarrow0,\ \eta\text{ fixed}).
\]
For the objective-compatible widths of `ANF-046`, `eta<3-sqrt(6)`, the canonical moment bound also gives the convenient uniform consequence
\[
\boxed{y<0.481\sqrt{s}.}
\tag{4}
\]
Equation (4) is only a coarse width-uniform corollary; the load-bearing estimate is the sharper profile-dependent bound (3).

## 1. The notch changes six-point curvature by at most `s b_eta eta^3`

Let
\[
K_\phi(t)
:=\int_{-\eta}^{\eta}\alpha^2\phi_\eta(\alpha)
\cos(2\pi\alpha t)\,d\alpha.
\tag{5}
\]
Since `phi_eta>=0`,
\[
|K_\phi(t)|\le K_\phi(0).
\tag{6}
\]
The triangular profile has the exact second moment
\[
\begin{aligned}
K_\phi(0)
&=2b_\eta\int_0^\eta
\alpha^2\left(1-\frac\alpha\eta\right)d\alpha\\
&=2b_\eta\left(\frac{\eta^3}{3}-\frac{\eta^3}{4}\right)
=\boxed{\frac{b_\eta\eta^3}{6}}.
\end{aligned}
\tag{7}
\]
Because `K_s=K-sK_phi`,
\[
D_s(T)
=D(T)-sP_\eta(T),
\tag{8}
\]
where
\[
P_\eta(T)
:=2K_\phi(0)+\sum_{j=1}^4K_\phi(t_j).
\tag{9}
\]
Using (6)--(7),
\[
P_\eta(T)
\le6K_\phi(0)
=\boxed{b_\eta\eta^3}.
\tag{10}
\]
No sign assumption on the individual `K_phi(t_j)` is needed.

Now `J_s>=0`, is continuous, even, nonzero, and compactly supported. Therefore the all-order one-pair theorem `ANF-069` applies to the **notched profile itself**. With four real anchors, a real-collapse reversal at any positive height exists if and only if
\[
D_s(T)<0.
\tag{11}
\]
If simultaneously `D(T)>=0`, equations (8), (10), and (11) give
\[
0\le D(T)<sP_\eta(T)\le s b_\eta\eta^3,
\]
which is (1). The same identities give
\[
0<-D_s(T)=sP_\eta(T)-D(T)
\le sP_\eta(T)
\le s b_\eta\eta^3,
\]
proving (2).

A useful contrapositive is exact:
\[
\boxed{
D(T)\ge s b_\eta\eta^3
\quad\Longrightarrow\quad
D_s(T)\ge0
\quad\Longrightarrow\quad
E_{\widehat J_s}(W_{y,T})>E_{\widehat J_s}(R_T)
\ \text{for every }y>0.
}
\tag{12}
\]
So the complement of the thin curvature strip is eliminated globally in height, not just perturbatively near `y=0`.

## 2. Spectral positivity also squeezes every new reversing height to zero

For a nonnegative spectrum with four real anchors, the quartic floor in `ANF-069` gives, whenever `D_s(T)<0`,
\[
y^2<
-\frac{3D_s(T)}{4\pi^2M_{2,s}(0)},
\tag{13}
\]
where
\[
M_{2,s}(0)
=\int\alpha^4J_s(\alpha)\,d\alpha.
\tag{14}
\]
The triangular fourth moment is also exact:
\[
\begin{aligned}
\int\alpha^4\phi_\eta(\alpha)d\alpha
&=2b_\eta\int_0^\eta
\alpha^4\left(1-\frac\alpha\eta\right)d\alpha\\
&=2b_\eta\left(\frac{\eta^5}{5}-\frac{\eta^5}{6}\right)
=\boxed{\frac{b_\eta\eta^5}{15}}.
\end{aligned}
\tag{15}
\]
Hence
\[
\boxed{
M_{2,s}(0)
=M_2(0)-\frac{s b_\eta\eta^5}{15}>0.
}
\tag{16}
\]
Strict positivity also follows directly from `J_s>=0` and `s<1`; (16) records the exact quantitative loss.

Substituting (2) and (16) into (13) proves (3). In particular, at fixed notch width the residual notch-created branch approaches the real axis as `sqrt(s)`. This removes the possibility of a finite positive-height branch surviving as `s->0` while its base Montgomery--Taylor curvature stays nonnegative.

For the widths that can beat the elementary Montgomery--Taylor objective, `ANF-046` requires
\[
0<\eta<3-\sqrt6<0.551.
\tag{17}
\]
Using `b_eta<=1`, `s<1`, the canonical lower bound on `M_2(0)`, and the elementary `pi>3.14`, equations (3) and (17) imply
\[
y^2
<
\frac{3s(0.551)^3}
{4(3.14)^2\left(0.05854458579969-(0.551)^5/15\right)}
<0.231s,
\]
which gives (4).

## 3. Relation to the branch already screened by `ANF-070`

There are now two logically distinct one-pair/four-anchor curvature regimes.

If
\[
D(T)<0,
\]
the base Montgomery--Taylor profile already lies in the curvature-seeded class. `ANF-070` supplies a fixed positive affine margin for that entire base class, including its finite-height continuation, and gives an explicit small-central-notch margin on the actual base-reversing branch.

If instead
\[
D(T)\ge0,
\]
then the base profile never reverses collapse at any height by `ANF-069`. The present finding shows that subtracting the central tent can create a reversal only when `D(T)` is within `s b_eta eta^3` of zero, and then only at height bounded by (3). Thus the residual notch-specific mechanism is not another global six-point search. It is a singular perturbation problem around the codimension-one boundary
\[
D(T)=0,\qquad y=0.
\tag{18}
\]

This is the useful reduction for the next affine step. To close the complete one-pair six-point central-notch inequality, it is enough on the base-nonreversing side to control affine slack in the shrinking region (1)--(3), rather than over arbitrary horizontal curvature and arbitrary height. The finding itself does **not** assert that the affine slack stays positive there: real multiplicity slack and the signed spatial response of the notch must still be compared with the possible negative collapse defect.

## 4. Stress tests and evidence boundary

The crucial use of `ANF-069` is profile-generic: its coefficientwise proof requires only a nonzero continuous even compactly supported spectrum `J>=0`, not the exact Montgomery--Taylor formula. Since `0<=phi_eta<=J_MT` and `0<s<1`, the notched profile satisfies those hypotheses. Reusing the theorem for `J_s` is therefore legitimate and is the reason a finite-height search collapses back to the perturbed quadratic coefficient.

The sign of `P_eta(T)` is deliberately not assumed. A central notch may either increase or decrease the curvature coefficient for a given horizontal configuration. The argument needs only the one-sided bound `P_eta(T)<=b_eta eta^3`; if a reversal is newly created from `D>=0`, equation (11) automatically forces `P_eta(T)>0` for that configuration.

The scale `eta^3` is also load-bearing, not notation. It is the exact second moment of the removed triangular spectrum multiplied by the six curvature slots `2+4`. Replacing it by the removed mass `b_eta eta` would lose two powers of the narrow width and obscure the perturbative separation already visible in `ANF-046`.

A fresh prior-art check revisited the current unconditional pair-correlation/Hilbert-space work around the Montgomery--Taylor profile, including the recent Alpöge--Furman and Lamzouri formulations and the BGSST pair-correlation framework already represented in `SOURCES.md`. Those works supply the ambient pair-correlation and extremal-function machinery, but no searched source formulates the finite one-pair central-notch curvature strip (1) or the induced height compactification (3). No publication-level novelty claim is made, and no new external theorem is load-bearing, so `SOURCES.md` is unchanged.

The result does not prove a universal affine counting inequality, does not close the remaining real-multiplicity slack in the thin strip, does not cover two or more nonreal pairs, and does not address the distinct one-pair higher-order frontier beginning at total cardinality eleven. Its exact contribution is the elimination of every base-nonreversing six-point notch-induced collapse reversal outside the shrinking region (1)--(3).

## 5. Decisive next gate

The next one-pair six-point calculation should therefore be local in both variables. On the region
\[
0\le D(T)<s b_\eta\eta^3,
\qquad
y^2<
\frac{3s b_\eta\eta^3}
{4\pi^2\left(M_2(0)-s b_\eta\eta^5/15\right)},
\]
compare the exact candidate-intercept slack of the collapsed real multiset `R_T` with the negative part of the notched collapse defect. If that comparison has a uniform positive first-order term in `s`, then the possible vertical loss is at most second order after optimizing `y^2=O(s)`, and the complete one-pair six-point central-notch layer closes. If the first-order real-multiplicity slack can vanish on the `D=0` boundary, that boundary instead identifies the first genuinely new six-point notch obstruction to analyze.