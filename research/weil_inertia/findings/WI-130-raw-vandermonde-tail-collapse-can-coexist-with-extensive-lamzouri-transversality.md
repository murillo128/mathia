# WI-130 — raw Vandermonde tail collapse can coexist with extensive Lamzouri transversality

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`. WI-128 gives a necessary spectral consequence of periodic Lamzouri screening: if a positive-density bounded-depth off-line sector makes the horizontal remainder subextensive, then a positive-density bottom singular-value tail of the normalized reciprocal-node Vandermonde must collapse. WI-129 then redirects scalar Riesz-basis arguments toward grouped/divided-difference exponential theory. The exact construction below shows why that redirection is load-bearing rather than cosmetic: a macroscopic raw Vandermonde tail can collapse to zero for a completely different reason — **nearby off-line pair centers** — while Lamzouri's actual anti-invariant quotient remains uniformly transverse and therefore pays extensive horizontal slack.

Consequently the raw bottom singular-value tail in WI-128 is a useful necessary condition, but it is not an orientation-sensitive proxy for the horizontal Schur complement

\[
H^*(I-P_V)H.
\]

A proof that targets only the unordered singular spectrum of the raw `f`-Vandermonde can therefore spend its effort excluding harmless confluent collapse. The correct next invariant is the grouped/confluent `g/h` quotient itself, or a theorem that uses genuinely zeta-specific information to rule out the close-center mechanism below before invoking raw spectral stability.

No unconditional zeta-zero percentage changes.

## 1. A density-one fixed-depth family with a collapsing raw spectral half

Fix a horizontal depth

\[
b>0.
\]

For an integer `M>=1`, put

\[
P=4M
\]

and choose `0<epsilon<1`. In one period of length `P`, take the `P` simple non-real labels

\[
\mathcal C_{M,\varepsilon}
=
\{\,4q\pm ib,\ 4q+\varepsilon\pm ib:
0\le q<M\,\}.
\tag{1}
\]

There are

\[
k=2M=P/2
\]

non-real conjugate pairs. All normalized horizontal depths are exactly `b`, so there is no approach to the critical line. The reciprocal nodes

\[
\omega_z=e^{-2\pi i z/P}
\]

are pairwise distinct for every `epsilon in (0,1)`.

Let

\[
\widetilde{\mathcal V}_P
=P^{-1/2}(\omega_z^r)_{0\le r<P,\ z\in\mathcal C_{M,\varepsilon}}
\tag{2}
\]

be the normalized raw reciprocal-node Vandermonde from WI-128, and write its singular values as

\[
\sigma_1\ge\cdots\ge\sigma_P\ge0.
\]

For each `q` and each sign, pair the two same-sign columns at real centers `4q` and `4q+epsilon`. If `v_P(z)` denotes the corresponding normalized column, then

\[
\begin{aligned}
\|v_P(z+\varepsilon)-v_P(z)\|^2
&=\frac1P\sum_{r=0}^{P-1}
|e^{-2\pi i r z/P}|^2
|e^{-2\pi i r\varepsilon/P}-1|^2\\
&\le
\frac{4\pi^2\varepsilon^2e^{4\pi b}}{P^3}
\sum_{r=0}^{P-1}r^2\\
&<\frac{4\pi^2}{3}e^{4\pi b}\varepsilon^2.
\end{aligned}
\tag{3}
\]

Here `|e^{-2 pi i r z/P}|^2<=e^{4 pi b}` for both signs and `|e^{i theta}-1|<=|theta|`.

The `P/2` coefficient vectors

\[
w_{q,\pm}
=\frac{e_{4q,\pm}-e_{4q+\varepsilon,\pm}}{\sqrt2}
\tag{4}
\]

have disjoint supports and are therefore orthonormal. Their images obey

\[
\|\widetilde{\mathcal V}_P w_{q,\pm}\|^2
<\frac{2\pi^2}{3}e^{4\pi b}\varepsilon^2.
\tag{5}
\]

By the Ky Fan minimum principle for the bottom `P/2` eigenvalues of `\widetilde{\mathcal V}_P^*\widetilde{\mathcal V}_P`, the span of these `w_{q,\pm}` is an admissible `P/2`-dimensional test space. Hence

\[
\boxed{
\frac1P\sum_{\ell=P/2+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2
<
\frac{\pi^2}{3}e^{4\pi b}\varepsilon^2.
}
\tag{6}
\]

Thus for any sequence `epsilon_M -> 0`, **the entire bottom half in the WI-128 sense collapses in mean square**:

\[
\frac2P\sum_{\ell=P/2+1}^{P}\sigma_\ell^2
\longrightarrow0.
\tag{7}
\]

This is already stronger than the necessary spectral collapse demanded in WI-128 for an off-line density `k/P=1/2`.

## 2. The collapse does not come from a long density island or from vanishing depth

The infinite periodic continuation of (1) is

\[
\mathcal Z_\varepsilon
=
\{\,4q\pm ib,\ 4q+\varepsilon\pm ib:q\in\mathbb Z\,\}.
\tag{8}
\]

It has exactly four labels in every period of length four, hence density one. For every real interval `I`, decomposing `I` into full four-periods plus at most two partial periods gives the uniform count-discrepancy bound

\[
\boxed{
\bigl|\#(\mathcal Z_\varepsilon\cap I)-|I|\bigr|\le8.
}
\tag{9}
\]

The exact constant is unimportant; the point is that it is independent of interval length and of `epsilon`. The WI-121 type obstruction to dense *long* count islands therefore does not see this family. The bad raw singular directions are produced by microscopic same-sign center collisions, not by macroscopic overpacking.

Nor does the family leave the classical grouped-exponential regime. It is the union of four subsequences

\[
4\mathbb Z+ib,
\quad4\mathbb Z-ib,
\quad4\mathbb Z+\varepsilon+ib,
\quad4\mathbb Z+\varepsilon-ib,
\tag{10}
\]

each uniformly separated by four. Hence it is relatively uniformly discrete in the sense used by Avdonin--Ivanov. Their exponential divided-difference theory is designed precisely for this situation: raw scalar exponentials can become ill-conditioned when points from different separated subsequences approach, while grouped/divided-difference coordinates remain the natural stable objects. This classical theory does not by itself prove the Lamzouri estimate below; it identifies the correct theorem surface and explains why raw singular collapse should not automatically be interpreted as horizontal screening.

## 3. Lamzouri's `g/h` quotient stays transverse in the confluent limit

Use Lamzouri's optimizing smoothing family from WI-126--WI-128,

\[
\eta_\delta(u)
=\frac{\psi_\delta(u)\sqrt{f_0(u)}}{\sqrt{A_\delta}},
\qquad
f_0(u)=
\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)},
\qquad |u|<\frac12,
\tag{11}
\]

with `A_delta<=1` and `psi_delta=1` on the flat core. It is enough to analyze the fundamental period-four motif

\[
\{\,\pm ib,\ \varepsilon\pm ib\,\},
\tag{12}
\]

because the period-`P=4M` continuation of (1) is exactly the same infinite set as the period-four continuation of (12).

Fiberize `L^2(-1/2,1/2)` over

\[
J=(-1/2,-1/4)
\]

with four rows

\[
u_r=t+r/4,
\qquad r=0,1,2,3.
\tag{13}
\]

Write

\[
a=2\pi b,
\qquad
c_r(t)=\cosh(au_r),
\qquad
s_r(t)=\sinh(au_r).
\]

After ignoring harmless nonzero scalar factors, the two retained even columns and the first omitted odd column are

\[
\begin{aligned}
g_0(t)&=D_\delta(t)c(t),\\
g_\varepsilon(t)&=D_\delta(t)
\bigl(e^{-2\pi i\varepsilon u_r}c_r(t)\bigr)_{r=0}^3,\\
h_0(t)&=-iD_\delta(t)s(t),
\end{aligned}
\tag{14}
\]

where

\[
D_\delta(t)=
\operatorname{diag}(\eta_\delta(u_0),\ldots,\eta_\delta(u_3)).
\]

For `epsilon != 0`, replacing `g_epsilon` by the difference quotient does not change its span with `g_0`:

\[
q_\varepsilon(t)
=\frac{g_\varepsilon(t)-g_0(t)}{\varepsilon}
\longrightarrow
-2\pi iD_\delta(t)(u_rc_r(t))_{r=0}^3
\tag{15}
\]

uniformly on compact subintervals of the flat core. Thus the confluent retained space is

\[
L_0(t)=D_\delta(t)
\operatorname{span}\{c(t),u\,c(t)\}.
\tag{16}
\]

The crucial point is that the omitted odd direction is not in this confluent even space. Dividing rowwise by the positive `c_r`, membership would require

\[
\tanh(au_r)=A+Bu_r
\tag{17}
\]

at all four fiber points for some constants `A,B`.

At the boundary value `t=-1/2`, consider only rows `r=0,2,3`, with

\[
u_0=-1/2,
\qquad u_2=0,
\qquad u_3=1/4.
\]

The determinant of the three columns `1,u,tanh(au)` on these rows is

\[
\frac14\left(2\tanh(a/4)-\tanh(a/2)\right).
\tag{18}
\]

If `tau=tanh(a/4)>0`, the double-angle identity gives

\[
2\tanh(a/4)-\tanh(a/2)
=2\tau-\frac{2\tau}{1+\tau^2}
=\frac{2\tau^3}{1+\tau^2}>0.
\tag{19}
\]

Therefore (17) fails. Since the corresponding minor is continuous in `t`, there is an interior compact interval

\[
E\Subset(-1/2,-1/4)
\tag{20}
\]

close enough to `-1/2` on which the distance from `s(t)` to `span{c(t),u c(t)}` is bounded below by a positive constant.

Choose `delta_0>0` smaller than the distance of all fiber points `u_r(t)`, `t in E`, from the endpoints `+/-1/2`. For every `0<delta<=delta_0`, the cutoff equals one on all these rows, so

\[
D_\delta(t)=A_\delta^{-1/2}D_0(t),
\qquad
D_0(t)=\operatorname{diag}(\sqrt{f_0(u_r)}).
\tag{21}
\]

The scalar `A_delta^{-1/2}` cannot reduce distances, and `D_0(t)` has a uniformly positive smallest diagonal entry on the compact set `E`. Hence there exists

\[
d_b>0
\tag{22}
\]

depending on `b` and the chosen `E`, but **not** on sufficiently small `delta`, such that

\[
\operatorname{dist}(h_0(t),L_0(t))\ge d_b
\qquad(t\in E).
\tag{23}
\]

The pair `g_0,q_0` is uniformly linearly independent on `E`. Uniform convergence in (15) therefore implies uniform convergence of the corresponding two-dimensional orthogonal projectors. Also `h_epsilon(t)->h_0(t)` uniformly. Consequently there is `epsilon_0(b)>0` such that for every

\[
0<\varepsilon\le\varepsilon_0(b),
\qquad0<\delta\le\delta_0,
\]

one has, after possibly decreasing `d_b`,

\[
\boxed{
\operatorname{dist}(h_0(t),\operatorname{span}\{g_0(t),g_\varepsilon(t)\})^2
+
\operatorname{dist}(h_\varepsilon(t),\operatorname{span}\{g_0(t),g_\varepsilon(t)\})^2
\ge d_b^2
}
\tag{24}
\]

for every `t in E`.

This is the orientation-sensitive fact that the raw singular values miss. As the two pair centers collide, the raw same-sign differences collapse, but the anti-invariant `sinh` direction does **not** collapse into the span of the two even `cosh` directions; the latter converge instead to an even direction plus its translation derivative.

## 4. The actual horizontal remainder stays extensive

Let `V_infty,epsilon` be Lamzouri's global retained space generated by the even `g` directions of the infinite period-four family (8). The standard fiber inclusion used already in WI-127 gives

\[
\operatorname{dist}(h,V_{\infty,\varepsilon})^2
\ge
\int_J
\operatorname{dist}(Uh(t),\mathcal V_\varepsilon(t))^2\,dt,
\tag{25}
\]

where `mathcal V_epsilon(t)=span{g_0(t),g_epsilon(t)}`. Integrating (24) only over `E` yields a constant

\[
c_b:=|E|d_b^2>0
\tag{26}
\]

such that one microscopic motif satisfies

\[
\boxed{
\operatorname{dist}(h_0,V_{\infty,\varepsilon})^2
+
\operatorname{dist}(h_\varepsilon,V_{\infty,\varepsilon})^2
\ge c_b
}
\tag{27}
\]

uniformly for all sufficiently small `epsilon` and along the same sufficiently small Lamzouri smoothing parameters `delta`.

Translation by four in the label is multiplication by a unitary modulation that leaves `V_infty,epsilon` invariant. Every one of the `M` microscopic motifs in (1) therefore pays the same lower bound. If `V_M` is Lamzouri's finite retained space for those `4M` labels, then

\[
V_M\subset V_{\infty,\varepsilon},
\]

so distance to `V_M` is no smaller. WI-126's exact horizontal slack consequently gives

\[
\begin{aligned}
R_H
&\ge4\sum_{z\in Z_+}
\operatorname{dist}(h_z,V_M)^2\\
&\ge4Mc_b.
\end{aligned}
\tag{28}
\]

Since the cell has `N=P=4M` labels,

\[
\boxed{
\frac{R_H}{N}\ge c_b>0.
}
\tag{29}
\]

Now choose any sequence `epsilon_M -> 0` with `epsilon_M<=epsilon_0(b)`. Equations (6) and (29) hold simultaneously:

\[
\boxed{
\frac1P\sum_{\ell=P/2+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2
\longrightarrow0,
\qquad
\frac{R_H}{N}\ge c_b>0.
}
\tag{30}
\]

Thus a macroscopic raw Vandermonde near-null sector can coexist with **extensive**, not screened, Lamzouri horizontal transversality.

## 5. Why this does not contradict WI-128

WI-128 proves the one-way inequality

\[
\frac{R_H}{PM}
\ge
f_{\min}e^{-2\pi B}
\frac1P\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2.
\tag{31}
\]

The present family makes the right-hand side small while leaving the left-hand side bounded below. There is no contradiction: Eckart--Young sees the best *arbitrary* rank-`P-k` approximation to the full raw matrix, whereas Lamzouri's screening asks whether one **specified block**, the anti-invariant `H`, is approximable by the specified retained block `V`.

The difference is orientation. The cheap raw near-null vectors in (4) are same-sign translation differences. In `g/h` coordinates they mix derivatives of both the retained even and omitted odd sectors. They do not force the odd sector itself into the even sector. Singular values forget this block orientation; the Schur complement

\[
S=H^*(I-P_V)H
\tag{32}
\]

retains it.

This also explains the connection to WI-129. Raw exponentials become ill-conditioned as nearby centers coalesce, while divided-difference coordinates renormalize the collapsing translation differences. Avdonin--Ivanov prove that generalized divided differences depend continuously on colliding parameters and provide the natural uniform local bases for relatively uniformly discrete clustered exponential systems; their global Riesz-basis theorem still requires the appropriate generating-function/Helson--Szego condition. The present argument does not import that global theorem. It uses only the same confluent geometry directly in Lamzouri's four-row fiber.

## 6. Consequence for the bootstrap program

The following route is now closed as a generic strategy:

\[
\text{bounded off-line depth + no long density islands}
\Longrightarrow
\text{uniform lower bound on the raw WI-128 bottom spectral tail}
\Longrightarrow
\text{Lamzouri defect-to-zero gain}.
\tag{33}
\]

The first implication fails even for a density-one periodic family with bounded interval-count discrepancy, fixed depth bounded away from zero, and a finite-union-of-separated-subsequences structure. A raw spectral lower-tail theorem would need additional zeta-specific hypotheses strong enough to forbid the microscopic same-sign clustering in (1), and then one would still need to check that those hypotheses are actually available unconditionally.

More efficiently, the next target should remain orientation-sensitive from the start. Natural candidates are:

- a lower bound for the horizontal Schur-complement trace `tr H^*(I-P_V)H` itself;
- grouped/confluent finite-section principal-angle bounds for the `g/h` system;
- or a zeta-specific statistic that separates translation-confluent raw nullity from genuine anti-invariant screening.

This narrows WI-128's spectral-tail target: **macroscopic raw collapse is necessary for screening but can be harmless.** What must be ruled out is macroscopic collapse aligned with the anti-invariant quotient.

## 7. Prior art and novelty audit

The nearest line-local results are WI-128 and WI-129. WI-128 derives the bottom-singular-tail condition by Eckart--Young but does not claim the converse and gives only a well-spaced all-off-line lattice as a non-screening example. WI-129 identifies grouped/divided-difference theory as the correct neighboring surface after scalar bounded-strip Riesz theory fails, but it does not construct a positive-density raw spectral collapse with a simultaneously extensive Lamzouri horizontal remainder. A focused repository audit found no earlier finding with the combination (6)+(29).

The relevant classical prior art is already anchored in `research/weil_inertia/SOURCES.md`: S. A. Avdonin and S. A. Ivanov, *Exponential Riesz bases of subspaces and divided differences* (2001/2002, arXiv:math/0103160), and S. Avdonin and W. Moran, *Ingham-type inequalities and Riesz bases of divided differences* (2001). Avdonin--Ivanov explicitly treat finite unions of separated sequences, show generalized divided differences depend continuously on clustered parameters, and use them as uniform local bases when raw exponentials lose uniform minimality. Those are classical statements; no novelty is claimed for confluent exponential coordinates, Ky Fan, or fiberization.

A targeted literature search around clustered exponentials, divided differences, Riesz bases, and finite-section stability located this classical grouped theory but no statement combining it with Lamzouri's September 2026 `g/h` horizontal remainder or with the WI-128 raw reciprocal-node spectral tail. Absence from that search is not evidence of priority and no priority claim is made.

The durable line-specific deduction is the explicit separation between two notions that WI-128 left logically distinct: raw positive-density Vandermonde near-nullity and actual Lamzouri anti-invariant screening. The family (1) proves that the former can occur at full macroscopic scale while the latter remains uniformly expensive.

## 8. Falsification controls

The raw-tail statement would fail if the difference vectors (4) were not orthonormal or if their image energies were not `O_b(epsilon^2)` uniformly in `P`; both are immediate from disjoint supports and (3). The horizontal statement would fail if `sinh(au)` belonged to the confluent retained span generated by `cosh(au)` and `u cosh(au)` on the period-four fibers; equations (18)--(19) give an explicit nonzero three-row minor. Compactness then supplies the uniform interior interval needed to survive Lamzouri's cutoff and the `epsilon -> 0` projector limit.

The finding does **not** assert that actual zeta zeros realize the clustered motif (1), that pair correlation permits it with positive density, or that all raw-tail approaches are useless. A source-compatible theorem that unconditionally forbids such microscopic clustering could restore a raw spectral route. Nor does this finding address critical-line doubles, which remain a separate zero-cost population in WI-126. Its claim is exactly the structural barrier (30): the unordered raw Vandermonde spectrum alone is insufficient to diagnose the horizontal screening quantity that would drive a Lamzouri defect bootstrap.

**Research implication.** After WI-128--WI-129, the next meaningful spectral object is not a better condition number for the raw reciprocal-node Vandermonde. It is the principal-angle / Schur-complement geometry of the conjugation-adapted `g/h` decomposition, preferably in confluent coordinates that quotient out translation collisions before measuring anti-invariant defect.