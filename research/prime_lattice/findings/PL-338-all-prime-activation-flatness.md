# PL-338 — Every finite odd prime-power activation is first-order flat; a nonzero boundary trace gives the favorable birth sign

**Evidence:** `EXACT-DERIVED + POSITIVE-LOCAL-MECHANISM + ROUTE-NARROWING`

**Status:** `ALL-FINITE-ACTIVATIONS-NORM-RESOLVENT-CONTINUOUS + NEW-CHANNEL-O-DELTA + NONZERO-ODD-TRACE-GIVES-FAVORABLE-BIRTH-SIGN + LATER-TRACE-NONCOLLAPSE-OPEN`

## Precise claim

Fix a prime power

\[
q=p^k,
\qquad
\ell=\log q,
\qquad
w_q=\frac{\Lambda(q)}{\sqrt q}>0,
\]

and its source threshold

\[
a_0=\frac{\ell}{2}.
\]

Let `A_a` be Suzuki's fixed-domain localized completed-Weil operator on `I=(-1,1)` used in `PL-291`, `PL-330`, and `PL-337`. Then the first-prime continuity mechanism of `PL-330` is not special to `q=2`:

\[
\boxed{
A_a\longrightarrow A_{a_0}
\quad\text{in norm resolvent as }a\to a_0
}
\tag{PL338-1}
\]

at **every finite prime-power activation**. More generally, `a -> A_a` is norm-resolvent continuous on every compact aperture interval.

Now approach the threshold from above,

\[
a_\delta=a_0+\delta,
\qquad
\delta\downarrow0.
\]

Let `u_delta` be any real odd normalized completed-Weil eigenstate with eigenvalues in a fixed bounded window. Write its right-endpoint profile in the physical interval `(-a_delta,a_delta)` as

\[
g_\delta(t)=u_\delta(a_\delta-t),
\qquad 0<t<2\delta,
\]

and put

\[
Q_\delta(t)=\log\frac{2a_\delta}{t},
\qquad
L_\delta=\log\frac{a_\delta}{\delta}.
\]

The compact-aperture `L^infinity` estimate of `PL-337`, inserted into the exact endpoint source equation of `PL-319`--`PL-329`, gives a source-selected coefficient `C_delta`, uniformly bounded on such a family, and the uniform tail expansion

\[
g_\delta(t)
=
C_\delta Q_\delta(t)^{-1/2}+r_\delta(t),
\tag{PL338-2}
\]

with

\[
\boxed{
\|r_\delta\|_{L^2(0,2\delta)}
=O\!\left(\frac{\sqrt\delta}{L_\delta}\right).
}
\tag{PL338-3}
\]

No first-prime property enters this estimate: on a compact aperture interval there are only finitely many active prime-power shifts, and `PL-337` bounds the state and hence every translated term in the endpoint forcing uniformly.

The newly active `q`-correlation has the exact odd-reflection identity

\[
C_\ell(u_\delta)
:=
\int_{-a_\delta}^{a_\delta-\ell}
 u_\delta(x+\ell)u_\delta(x)\,dx
=
-
\int_0^{2\delta}
 g_\delta(t)g_\delta(2\delta-t)\,dt.
\tag{PL338-4}
\]

Consequently its contribution to the localized Weil form is

\[
P_q(u_\delta)
=-2w_q C_\ell(u_\delta)
=
2w_q H_\delta(g_\delta),
\qquad
H_\delta(g)
:=
\int_0^{2\delta}g(t)g(2\delta-t)\,dt.
\tag{PL338-5}
\]

The canonical half-log profile gives

\[
\boxed{
H_\delta(g_\delta)
=
2C_\delta^2\frac{\delta}{L_\delta}
+o\!\left(\frac{\delta}{L_\delta}\right)
}
\tag{PL338-6}
\]

whenever `C_delta` has a nonzero limit; without any noncollapse assumption one still has

\[
\boxed{
H_\delta(g_\delta)=O\!\left(\frac{\delta}{L_\delta}\right),
\qquad
P_q(u_\delta)=o(\delta).
}
\tag{PL338-7}
\]

For a simple isolated odd eigenvalue at `a_0`, norm-resolvent continuity supplies an `L^2`-continuous phase-aligned branch. The fixed-block argument of `PL-332` then applies verbatim to the uniform expansion (PL338-2), so

\[
C_\delta\to C_0.
\tag{PL338-8}
\]

Hence, if the threshold state has nonzero source-selected boundary coefficient,

\[
C_0\ne0,
\tag{PL338-9}
\]

then the newly born prime-power channel has the universal asymptotic

\[
\boxed{
P_q(u_\delta)
=
4\frac{\Lambda(q)}{\sqrt q}
C_0^2
\frac{\delta}{L_\delta}
\bigl(1+o(1)\bigr)>0.
}
\tag{PL338-10}
\]

Thus **every finite prime-power source is born on the favorable side of the odd Weil form whenever the threshold branch has nonzero canonical boundary trace**. The source activation is also first-order flat: despite the unit operator-norm jump of the compressed translation, its value on an actual bounded-eigenvalue odd state is `o(delta)`.

For `q=2`, `PL-335` proves `C_0>0` on the lowest odd threshold state, so (PL338-10) recovers the unconditional first-prime sign closed by `PL-337`. At later thresholds, the new local gate is no longer concentration, topology, or the reflection asymptotic itself. It is the scalar question whether the selected odd branch has `C_0 != 0` at that threshold, together with branch-ordering and already-active multi-channel effects away from birth.

## 1. All finite prime activations are norm-resolvent continuous

On a compact aperture interval

\[
J=[a_-,a_+]\subset(0,\infty),
\]

`PL-337` writes the arithmetic part using the fixed finite source set `log n<=2a_+` as

\[
P_a
=
\sum_{\log n\le2a_+}w_nD_{h_n(a)}
-2\Bigl(\sum_{\log n\le2a_+}w_n\Bigr)I,
\qquad
h_n(a)=\frac{\log n}{a}.
\tag{PL338-11}
\]

For zero extension outside `I`, each compressed translation `S_h` is a contraction and is strongly continuous in `h`. At `h=2`, it converges strongly to zero from below because its support is confined to two edge strips whose measure tends to zero; this is exactly the edge-strip argument of `PL-330`. For `h>2`, it is identically zero. Hence

\[
a\mapsto D_{h_n(a)}
\]

is strongly continuous and uniformly bounded through both active motion and activation.

Together with the norm-continuous scalar and continuous-completion pieces, Suzuki's fixed-domain family has the form

\[
A_a=T+K_a,
\tag{PL338-12}
\]

where `T` is the common logarithmic principal operator, `K_a` is bounded self-adjoint,

\[
\sup_{a\in J}\|K_a\|<\infty,
\qquad
K_a\to K_{a_0}\quad\text{strongly},
\tag{PL338-13}
\]

and `T+K_{a_0}` has compact resolvent. For nonreal `z`, set

\[
R_0(z)=(A_{a_0}-z)^{-1}.
\]

Because `R_0(z)` is compact, uniform boundedness plus strong convergence gives

\[
\|(K_a-K_{a_0})R_0(z)\|\to0.
\tag{PL338-14}
\]

The resolvent identity then yields

\[
\|(A_a-z)^{-1}-(A_{a_0}-z)^{-1}\|
\le
\frac1{|\operatorname{Im}z|}
\|(K_a-K_{a_0})R_0(z)\|
\to0,
\]

proving (PL338-1). This is the `PL-330` compact-resolvent mechanism with the unnecessary `q=2` restriction removed.

## 2. Compact-aperture boundedness makes the endpoint source estimate uniform

The endpoint source identity used in `PL-319` and `PL-329` is local to the logarithmic principal operator. Its right-hand side contains the eigenvalue/scalar terms, the bounded continuous completion, and finitely many compressed source translations.

For normalized eigenstates with `|lambda|<=M`, `PL-337` gives

\[
\sup\|u_\delta\|_\infty<\infty
\tag{PL338-15}
\]

uniformly through every activation in `J`. Every compressed translation has `L^infinity` norm at most one, and only finitely many source terms occur on `J`. Therefore the endpoint forcing amplitude `S_delta` of `PL-329` satisfies

\[
\boxed{S_\delta=O(1)}
\tag{PL338-16}
\]

at an arbitrary finite threshold, not only at `q=2`.

The endpoint comparison and integrated source argument of `PL-329` therefore give (PL338-2) with constants independent of small `delta`. Restricting that pointwise estimate to `0<t<2delta` gives precisely the `L^2` remainder estimate (PL338-3). The proof uses no positivity of the odd cone and is unaffected by the already-active lower prime-power channels; they enter only through the uniformly bounded forcing.

This step is important because the raw compressed shift has norm one immediately after activation. The smallness in (PL338-7) is not operator-norm smallness. It is a **state-selected boundary regularity effect**.

## 3. Exact odd reflection reduces every source birth to the same endpoint autocorrelation

Since `ell=2a_0` and `a_delta=a_0+delta`,

\[
a_\delta-\ell=-a_\delta+2\delta.
\]

In the correlation integral set

\[
x=-a_\delta+t,
\qquad 0<t<2\delta.
\]

Then

\[
x+\ell
=a_\delta-(2\delta-t).
\]

Oddness gives

\[
u_\delta(-a_\delta+t)
=-u_\delta(a_\delta-t)
=-g_\delta(t),
\]

so (PL338-4) follows exactly. The same algebra works for every prime power because the only arithmetic datum used is the equality `ell=log q=2a_0`.

This is why the birth geometry is universal. The prime label survives only in the positive scalar weight `w_q` and in the location of the threshold.

## 4. The half-log endpoint law makes the birth contribution `delta/log(1/delta)`

Write

\[
b_\delta(t)=C_\delta Q_\delta(t)^{-1/2},
\qquad
g_\delta=b_\delta+r_\delta.
\]

The main reflected overlap is

\[
J_\delta
:=
\int_0^{2\delta}
\frac{dt}{\sqrt{Q_\delta(t)Q_\delta(2\delta-t)}}.
\tag{PL338-17}
\]

With `t=delta x`,

\[
Q_\delta(\delta x)
=L_\delta+\log\frac2x,
\qquad
Q_\delta(\delta(2-x))
=L_\delta+\log\frac2{2-x},
\]

and therefore

\[
J_\delta
=
\frac{\delta}{L_\delta}
\int_0^2
\frac{dx}{
\sqrt{
\left(1+\frac{\log(2/x)}{L_\delta}\right)
\left(1+\frac{\log(2/(2-x))}{L_\delta}\right)
}}.
\tag{PL338-18}
\]

Both logarithms are nonnegative on `(0,2)`. The integrand is bounded by one and converges pointwise to one, so dominated convergence gives

\[
\boxed{
J_\delta
=2\frac{\delta}{L_\delta}(1+o(1)).
}
\tag{PL338-19}
\]

Moreover,

\[
\|b_\delta\|_2
=O\!\left(|C_\delta|\sqrt{\frac\delta{L_\delta}}\right),
\]

while (PL338-3) gives

\[
\|r_\delta\|_2
=O\!\left(\frac{\sqrt\delta}{L_\delta}\right).
\]

Cauchy--Schwarz therefore yields

\[
\left|
H_\delta(g_\delta)-C_\delta^2J_\delta
\right|
\le
2\|b_\delta\|_2\|r_\delta\|_2
+\|r_\delta\|_2^2
=
O\!\left(
|C_\delta|\frac\delta{L_\delta^{3/2}}
+
\frac\delta{L_\delta^2}
\right).
\tag{PL338-20}
\]

The endpoint construction bounds `C_delta` uniformly. Equations (PL338-19)--(PL338-20) prove the `O(delta/L_delta)` part of (PL338-7). If `C_delta -> C_0 != 0`, the error is `o(delta/L_delta)` and (PL338-6), hence (PL338-10), follows.

Because

\[
\frac{\delta/L_\delta}{\delta}
=\frac1{L_\delta}\to0,
\]

the newly active arithmetic channel is first-order flat on these state-selected families even though its bounded-operator norm jumps at activation.

## 5. Simple branches transport the boundary coefficient at every threshold

Norm-resolvent continuity (PL338-1) gives norm-continuous Riesz projections for isolated spectral clusters. At a simple eigenvalue, choose the normalized real odd eigenvector continuously in `L^2`.

The coefficient-continuity lemma of `PL-332` is not intrinsically tied to `q=2`: it uses only `L^2` convergence on the fixed interval and a uniform expansion

\[
|g_\delta(Q)-C_\delta Q^{-1/2}|\le K/Q
\]

on one fixed remote logarithmic block. Equations (PL338-15)--(PL338-16) provide exactly that uniform expansion here. Thus (PL338-8) follows for every simple isolated odd branch crossing a finite prime-power threshold.

The only source-specific local hypothesis left for a strict birth sign is therefore (PL338-9). For the first threshold, `PL-335` proves it through the antisymmetric logarithmic-Laplacian Hopf mechanism. No analogous noncollapse theorem is claimed here for later thresholds, where lower prime channels are already active and the odd-sector positivity-preserving mechanism of `PL-324` has failed.

## 6. Adversarial and novelty audit

**This is not operator-norm continuity.** The compressed source channel still has norm one for every `delta>0` and is zero at the threshold. Equations (PL338-7) and (PL338-10) concern its value on completed-Weil eigenstates selected by the logarithmic endpoint equation.

**Norm-resolvent continuity does not orient the sign by itself.** `PL-330` and the counterlayers of `PL-327` remain valid controls. The sign comes only after the uniform source-selected remainder is combined with a nonvanishing critical coefficient.

**The later noncollapse problem is real.** `PL-335` relies on the special first-threshold odd Hopf sign. Once lower arithmetic channels are active, the odd-cone Beurling--Deny property is already false by `PL-324`. This finding does not silently propagate that maximum principle to later thresholds.

**No eigenvalue-derivative theorem is claimed.** The new `q`-channel contributes `o(delta)` along the selected state family, but other already-active translations and the continuous aperture dependence can contribute at larger order. Therefore (PL338-7) does not imply differentiability of `lambda(a)` or continuity of its derivative.

**No multi-channel positivity follows.** A newly born channel is favorable under (PL338-9), but correlations at previously active lags need not have a fixed sign and can evolve with the branch. The result is local in the activation parameter and does not sum to global Weil positivity.

**No broad novelty claim.** Strong continuity of translations, compact-resolvent upgrading, dominated convergence in (PL338-19), and the logarithmic-Laplacian boundary scale are standard or already anchored in the cited local findings. A targeted literature audit found Suzuki's 2026 localized-Weil framework and the existing logarithmic-Laplacian boundary/Hopf literature, but no theorem stating this all-prime activation law. Search absence is not evidence of general novelty. The durable contribution is the line-specific synthesis: the first-prime source-selected reflection argument extends to every finite prime-power birth once `PL-337` removes the uniform-source gate.

**No analytic-continuation shortcut is used.** Everything is derived from the localized completed-Weil operator and its exact real-space von-Mangoldt source terms. No Euler product is evaluated outside its convergence domain and no zero data are inserted.

## Consequence for `prime_lattice`

`PL-337` left later prime-power activations as possible fresh correlation-sign gates. The present calculation separates the genuinely new part from the universal one.

At every finite source threshold, topology, concentration, endpoint asymptotics, and the newly born reflected channel behave exactly as at the first threshold: the operator is norm-resolvent continuous; normalized bounded-eigenvalue states have uniform endpoint forcing; the new source contributes only `O(delta/log(1/delta))`; and on a simple odd branch with nonzero threshold boundary coefficient it is born with the favorable sign.

The later-activation frontier is therefore narrower:

\[
\boxed{
\text{later local gate}
=
\text{boundary-coefficient noncollapse / branch selection},
}
\]

while the genuinely global difficulty is the evolution and interaction of **already active** signed prime-power correlations away from their birth layers. A future mechanism should attack that multi-channel geometry or prove a later-threshold trace-noncollapse theorem; another generic regularity or source-activation continuity estimate would duplicate a gate already closed here.

## Dependencies and literature anchors

- `PL-291`: fixed-domain logarithmic principal operator, common graph domain, compact resolvent, and bounded continuous completion.
- `PL-319`--`PL-323`: exact endpoint source equation, canonical half-log boundary scale, and source-selected tail control.
- `PL-324`: odd-sector positivity-preserving threshold and its failure once cross-half prime lags are active.
- `PL-327`: hostile critical endpoint layer showing why topology alone cannot orient reflection.
- `PL-329`: sharp source-amplitude reflection estimate and the `delta/L_delta` sign scale.
- `PL-330`: first-threshold strong-shift / compact-resolvent mechanism generalized in Section 1.
- `PL-332`: fixed-block continuity of the source-selected boundary coefficient.
- `PL-335`: first-threshold antisymmetric Hopf theorem proving the needed noncollapse for `q=2`.
- `PL-337`: compact-aperture `L^infinity` estimate through every finite prime-power activation.
- Source 56 in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v2, 17 August 2026).
- Sources 96--97 and 103 in `research/prime_lattice/SOURCES.md`: logarithmic-Laplacian Dirichlet regularity and (antisymmetric) Hopf/maximum-principle anchors already used by the endpoint analysis.