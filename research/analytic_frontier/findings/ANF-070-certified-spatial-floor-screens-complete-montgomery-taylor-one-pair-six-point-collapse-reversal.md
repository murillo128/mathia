# ANF-070 — certified spatial floor screens the complete Montgomery--Taylor one-pair six-point collapse-reversal branch

**Status:** `EXACT-DERIVED + COMPUTER-ASSISTED-ONE-DIMENSIONAL-CERTIFICATE + COMPLETE-BASE-REVERSAL-SCREENING + CENTRAL-NOTCH-BRANCH-MARGIN`. `ANF-069` reduces every one-pair/four-real-anchor Montgomery--Taylor collapse reversal to a negative curvature coefficient and confines the reversing height to `y<0.267431`. Its remaining scalar gate was the one-dimensional comparison between the spatial kernel and the curvature deficit. That gate is now certified.

Let
\[
F(t)=F_{\rm MT}(t)=G(t)^2,\qquad
K(t)=K_{\rm MT}(t)=-\frac{F''(t)}{4\pi^2},\qquad
K_0=K(0),
\]
with the exact Montgomery--Taylor factor `G` from `ANF-059`, and define
\[
r(t):=\left(-\frac{K_0}{3}-K(t)\right)_+.
\]
Then
\[
\boxed{
F(t)\ge \frac18 r(t)\qquad(t\in\mathbb R).
}
\tag{1}
\]
More strongly, with
\[
\varepsilon:=\frac{5246646}{10^9}=0.005246646,
\]
every point with `r(t)>0` satisfies
\[
\boxed{
F(t)>\frac18\bigl(r(t)+\varepsilon\bigr).
}
\tag{2}
\]

For four distinct nonzero real anchors `T={t_1,t_2,t_3,t_4}`, put
\[
D(T)=2K_0+\sum_{j=1}^4K(t_j),
\qquad
W_{y,T}=\{iy,-iy,t_1,t_2,t_3,t_4\}.
\]
If `D(T)<0`, then for every `y>0` the Montgomery--Taylor six-point affine slack at intercept `A=2` obeys
\[
\boxed{
\mathcal S_{\rm MT}(W_{y,T})>\frac{93}{10000}.
}
\tag{3}
\]
In particular this covers the entire base-profile collapse-reversing branch, not only its infinitesimal germ.

For the admissible central tent of `ANF-068`,
\[
J_s=J_{\rm MT}-s\phi_\eta,\qquad
0<\eta<1,\quad 0<s\le1,
\]
with candidate intercept `A_s=2-2s b_\eta\eta`, every configuration whose **base Montgomery--Taylor profile actually reverses real collapse** satisfies
\[
\boxed{
s b_\eta\eta\le\frac{93}{1600000}
\quad\Longrightarrow\quad
\mathcal S_s(W_{y,T})>\frac{93}{20000}.
}
\tag{4}
\]
Thus the complete curvature-seeded one-pair six-point reversal branch cannot obstruct a sufficiently small admissible central notch. This does not prove the full six-point notched inequality: a notch-dependent failure outside the base reversing branch, geometries with multiple nonreal pairs, and larger configurations remain open.

## 1. The remaining profile gate is a single explicit function

`ANF-059` gives
\[
G(t)=
\frac{\cos(\pi t)-\sqrt2\,\pi\cot(1/\sqrt2)\,t\sin(\pi t)}
{1-2\pi^2t^2},
\tag{5}
\]
and
\[
F(t)=G(t)^2,\qquad
K(t)=-\frac{G'(t)^2+G(t)G''(t)}{2\pi^2}.
\tag{6}
\]
The apparent poles of (5) are removable and lie outside the interval used below.

Introduce
\[
Q(t):=8F(t)+K(t)+\frac{K_0}{3}.
\tag{7}
\]
Whenever `r(t)>0`, equation (7) is exactly
\[
Q(t)=8F(t)-r(t).
\tag{8}
\]
Therefore (2), and hence (1), follows from the strict lower bound
\[
Q(t)>\varepsilon
\tag{9}
\]
on the whole region where the curvature deficit can be active.

`ANF-059` already certifies
\[
|t|\le0.545\ \text{or}\ |t|\ge1.01
\quad\Longrightarrow\quad
K(t)>-\frac{K_0}{3}.
\tag{10}
\]
Thus `r(t)=0` outside the compact annulus `0.545<|t|<1.01`; there (1) is immediate from `F=G^2>=0`. It remains only to prove (9) on `[0.545,1.01]`, with the negative half supplied by evenness.

## 2. Independent interval mesh plus an analytic Lipschitz bound certifies the compact gate

The finite certificate was reconstructed independently from the exact formulas (5)--(7), rather than trusting the adaptive cover that motivated the accepted clue. Using Python 3.13.5, SymPy 1.14.0 and `mpmath.iv` 1.3.0 at 60 decimal digits, evaluate the exact expression (7) by interval arithmetic at the rational grid
\[
t_j=\frac{109}{200}+\frac{j}{5000},
\qquad
0\le j\le2325.
\tag{11}
\]
All 2326 singleton interval enclosures have lower endpoint strictly greater than
\[
0.0156055.
\tag{12}
\]
The smallest lower endpoint occurs at the final node `t=1.01`; its enclosure begins
\[
0.0156055615421229457489069733\ldots.
\tag{13}
\]

A global derivative bound turns this finite node check into a continuous certificate. Since
\[
Q(t)-\frac{K_0}{3}
=
\int_{-1}^{1}(8+\alpha^2)J_{\rm MT}(\alpha)
\cos(2\pi\alpha t)\,d\alpha,
\tag{14}
\]
and `J_MT>=0`, `supp J_MT subset [-1,1]`, and
\[
\int_{-1}^{1}J_{\rm MT}(\alpha)\,d\alpha=F(0)=1,
\]
we have
\[
|Q'(t)|
\le
2\pi\int_{-1}^{1}|\alpha|(8+\alpha^2)J_{\rm MT}(\alpha)\,d\alpha
\le18\pi.
\tag{15}
\]
Every point of `[0.545,1.01]` is within `1/10000` of a grid node. Using the elementary `pi<22/7`, equations (12) and (15) give
\[
Q(t)>
0.0156055-\frac{396}{70000}
=
\frac{139277}{14000000}
=
0.009948357142857\ldots.
\tag{16}
\]
In particular
\[
\frac{139277}{14000000}
-\frac{5246646}{10^9}
=
\frac{16455989}{3500000000}>0,
\tag{17}
\]
which proves (9) with a substantial independent margin. The original adaptive Arb certificate is therefore not needed as an unverified black box for the canonical implication.

## 3. Negative curvature forces three active deficits and their spatial surplus survives vertical descent

For each anchor write
\[
r_j=r(t_j),\qquad
e_j=\left(K(t_j)+\frac{K_0}{3}\right)_+.
\]
Then
\[
K(t_j)=-\frac{K_0}{3}-r_j+e_j,
\]
and hence
\[
\sum_{j=1}^4r_j
=
\frac{2K_0}{3}+\sum_{j=1}^4e_j-D(T)
\ge
\frac{2K_0}{3}-D(T).
\tag{18}
\]

Moreover `D(T)<0` forces at least three indices with `r_j>0`. Indeed, if at most two deficits were active, the two active curvature values are bounded below by the global minimum `k_*`, while each inactive value is at least `-K_0/3`. Therefore
\[
D(T)
\ge
2K_0+2k_*-\frac{2K_0}{3}
=
\frac23(2K_0+3k_*)>0,
\tag{19}
\]
contradicting `D(T)<0`; the final strict inequality is canonical from `ANF-038`/`ANF-066`.

For an active anchor, (2) says
\[
F(t_j)>\frac{r_j+\varepsilon}{8}.
\]
The exact collapsed slack identity from `ANF-068` is
\[
\mathcal S_{\rm MT}(R_T)
=
4\sum_{j=1}^4F(t_j)
+
2\sum_{1\le j<k\le4}F(t_j-t_k),
\tag{20}
\]
where every term is nonnegative because `F=G^2`. Dropping the anchor--anchor terms and using at least three active deficits gives
\[
\boxed{
\mathcal S_{\rm MT}(R_T)
>
\frac{K_0}{3}
-\frac{D(T)}{2}
+\frac{3\varepsilon}{2}.
}
\tag{21}
\]

The all-order height expansion of `ANF-069` supplies, for four anchors,
\[
4Q_4(y;T)\ge-\frac{3D(T)^2}{2M_2(0)}
\qquad(y>0),
\tag{22}
\]
where `E_F(W_{y,T})-E_F(R_T)=4Q_4(y;T)`. Hence
\[
\mathcal S_{\rm MT}(W_{y,T})
>
\frac{K_0}{3}
-\frac{D(T)}{2}
-\frac{3D(T)^2}{2M_2(0)}
+\frac{3\varepsilon}{2}.
\tag{23}
\]

Use the already certified rational bounds
\[
K_0>k:=0.1549985926411760,
\quad
-D(T)<d:=0.055099459323598,
\quad
M_2(0)>m:=0.05854458579969.
\tag{24}
\]
Writing `x=-D(T)` reduces (23) to
\[
\mathcal S_{\rm MT}(W_{y,T})
>
\frac{k}{3}
+\frac{x}{2}
-\frac{3x^2}{2m}
+\frac{3\varepsilon}{2},
\qquad 0<x<d.
\tag{25}
\]
The right side is concave in `x`, so its minimum on `[0,d]` is at an endpoint. Direct rational evaluation gives
\[
x=0:\quad 0.0595361665470586\ldots,
\]
and
\[
x=d:\quad
0.0093002980288572302649\ldots
>
\frac{93}{10000}.
\tag{26}
\]
This proves (3). Notice that the bound holds for the whole negative-curvature class at every height, even after the base collapse defect has crossed back to positive.

## 4. The actual reversing branch leaves a uniform central-notch margin

For the central tent, `ANF-068` proves the exact slack identity
\[
\mathcal S_s(W_{y,T})
=
\mathcal S_{\rm MT}(W_{y,T})
+s\left(12b_\eta\eta-E_{\Phi_\eta}(W_{y,T})\right)
\tag{27}
\]
and the spectral estimate
\[
E_{\Phi_\eta}(W_{y,T})
\le
b_\eta\eta
\left(2\cosh(2\pi\eta y)+4\right)^2.
\tag{28}
\]
Therefore the notch can reduce the base slack by at most
\[
s b_\eta\eta
\left[
\left(2\cosh(2\pi\eta y)+4\right)^2-12
\right].
\tag{29}
\]

If the **base profile actually reverses real collapse**, `ANF-069` gives `y<0.267431`. Since `0<eta<1`, monotonicity of `cosh` and an independent 60-digit interval evaluation at the endpoint give
\[
\left(2\cosh(2\pi\cdot0.267431)+4\right)^2-12
<
79.270889919972
<
80.
\tag{30}
\]
Combining (3), (29), and (30), the condition
\[
s b_\eta\eta\le\frac{93}{1600000}
\]
gives
\[
\mathcal S_s(W_{y,T})
>
\frac{93}{10000}
-
80\frac{93}{1600000}
=
\frac{93}{20000},
\]
which is (4).

The distinction between `D(T)<0` and actual base reversal is load-bearing here. The base margin (3) is global in height, but the simple uniform notch-loss constant `80` uses the reversal-height compactification from `ANF-069`.

## 5. Prior art, audit boundary, and consequence for the line

A fresh structure-level check revisited the Carneiro--Chandee--Littmann--Milinovich extremal Hilbert-space treatment of pair correlation, the unconditional complex-zero pair-correlation theorem of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, and Lamzouri's September 2026 Hilbert-space proof. Those sources supply the Montgomery--Taylor extremal profile and the zeta-side pair-correlation framework already anchored in `SOURCES.md`; no searched source supplied the finite six-point curvature-deficit/spatial-slack comparison (1)--(4). No publication-level novelty claim is made, and no new literature dependency is load-bearing, so `SOURCES.md` is unchanged.

The computer-assisted component is only the finite one-dimensional interval evaluation (11)--(13) and the endpoint interval check in (30). The passage from that finite data to the global spatial floor uses the analytic derivative bound (15), while the six-point and notch consequences are exact algebra from canonical `ANF-068`--`ANF-069`. A reproducer must enclose the exact formula (7) at all 2326 rational nodes; ordinary floating-point sampling without interval enclosures is not evidence for (12).

This closes the accepted `CLUE-montgomery-taylor-six-point-curvature-deficit-screening` question for the base one-pair reversal branch. It does **not** prove the complete central-notch affine inequality at cardinality six, because configurations whose Montgomery--Taylor base profile does not reverse collapse can still respond differently to the notch. It also says nothing about two or more nonreal pairs, the first one-pair higher-order frontier at total cardinality eleven, another spectrum, or RH. The useful structural conclusion is narrower: the first scalar real-collapse failure at six points is completely screened by spatial affine slack, including its full finite-height continuation, so progress must leave that already classified base-reversal mechanism.
