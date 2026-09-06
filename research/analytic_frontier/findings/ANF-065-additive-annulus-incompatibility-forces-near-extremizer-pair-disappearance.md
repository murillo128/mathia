# ANF-065 — additive annulus incompatibility forces pair disappearance in Montgomery--Taylor near-extremizers

**Status:** `EXACT-DERIVED + PROFILE-SPECIFIC + GLOBAL-EXCESS-LOWER-BOUND + NEAR-EXTREMIZER-REDUCTION`. `ANF-064` proves the sharp Montgomery--Taylor five-point floor and a uniform positive quartic remainder, but its independent moment bounds discard the additive linkage among the three horizontal arguments `t_1`, `t_2`, and `t_1-t_2`. Restoring only that linkage and combining it with the curvature annulus of `ANF-059` yields a new global lower bound.

Let

\[
K(t):=K_{\rm MT}(t),\qquad K_0:=K(0),\qquad k_*:=\inf_{t\in\mathbb R}K(t),
\tag{1}
\]

and put

\[
\theta:=-\frac{K_0}{3},\qquad
\Delta:=\max\{0,\theta-k_*\}.
\tag{2}
\]

For a genuine two-pair geometry relabel the pairs so that `y_h>=y_l>0`, and define

\[
S:=y_h^2+y_l^2,\qquad
r:=\frac{y_l^2}{S}\in(0,1/2],\qquad
d:=t_h-t_l,
\tag{3}
\]

as well as

\[
c_*:=2\pi^2\bigl(2K_0+3k_*\bigr),\qquad
E:=\frac{H_{\rm MT}}{S}-c_*.
\tag{4}
\]

Then, with the certified constant `epsilon=0.00082277` from `ANF-064`, one has the exact-profile inequality

\[
\boxed{
E\ge 2\pi^2\Delta r+2\pi^4\varepsilon S.
}
\tag{5}
\]

Thus the already-known radial collapse `S=O(E)` has a horizontal-compatibility companion. Whenever the scalar curvature minimum crosses the `ANF-059` threshold, equivalently `Delta>0`, every sequence approaching the sharp five-point floor must also satisfy `r=O(E)`: the smaller conjugate pair disappears. The remaining horizontal classification is reduced to the geometry of the global minimizer set of the single explicit curvature function `K`.

## 1. The normalized excess retains one exact linked quadratic form

Write

\[
g(t):=K(t)-k_*\ge0.
\tag{6}
\]

The `n=1` term of the exact height expansion in `ANF-064`, after division by `S`, differs from the sharp floor `c_*` by

\[
\boxed{
2\pi^2Q,
\qquad
Q:=(1-r)g(t_h)+r g(t_l)+2g(d).
}
\tag{7}
\]

This is an identity at quadratic order, not an independent lower bound on the three curvature values. It is precisely where the relation

\[
d=t_h-t_l
\tag{8}
\]

survives.

All coefficients of height order at least four are positive by `ANF-063`--`ANF-064`. More specifically, the certified order-two moment margin in `ANF-064` gives

\[
H_{\rm MT}
\ge
S\bigl(c_*+2\pi^2Q\bigr)
+2\pi^4\varepsilon S^2.
\tag{9}
\]

Dividing by `S` therefore yields

\[
\boxed{
E\ge2\pi^2Q+2\pi^4\varepsilon S.
}
\tag{10}
\]

The problem is now to lower-bound `Q` without separately forcing each of its three arguments to minimize `K`.

## 2. The low-curvature set is trapped in a sum-free signed annulus

`ANF-059` proves the strict profile-specific exclusion

\[
|t|\le0.545\quad\text{or}\quad |t|\ge1.01
\qquad\Longrightarrow\qquad
K(t)>-\frac{K_0}{3}=\theta.
\tag{11}
\]

Hence, if `Delta>0`, then

\[
g(t)<\Delta
\quad\Longrightarrow\quad
K(t)<k_*+\Delta=\theta
\quad\Longrightarrow\quad
t\in W,
\tag{12}
\]

where

\[
W:=(-1.01,-0.545)\cup(0.545,1.01).
\tag{13}
\]

The key elementary fact is that `W` contains no additive triple `u,v,u-v`. Indeed, if `u,v` have the same sign, then

\[
|u-v|<1.01-0.545=0.465<0.545,
\tag{14}
\]

while if they have opposite signs, then

\[
|u-v|>0.545+0.545=1.09>1.01.
\tag{15}
\]

Thus it is impossible for all three linked arguments `t_h`, `t_l`, and `d=t_h-t_l` to satisfy `g<Delta`. At least one obeys

\[
g(t_h)\ge\Delta,
\qquad\text{or}\qquad
g(t_l)\ge\Delta,
\qquad\text{or}\qquad
g(d)\ge\Delta.
\tag{16}
\]

If `Delta=0`, the lower bound derived below is automatic, so no crossing hypothesis is being smuggled into the unconditional statement.

## 3. Additive incompatibility gives a weighted curvature gap

The three weights in `Q` are `1-r`, `r`, and `2`. Because `0<r<=1/2`, each weight is at least `r`. Combining this with (16) gives, for `Delta>0`,

\[
Q\ge r\Delta.
\tag{17}
\]

The same inequality is trivially true when `Delta=0`. Therefore

\[
\boxed{Q\ge r\Delta}
\tag{18}
\]

for every genuine geometry, and substitution into (10) proves (5).

This is stronger than the separate scalar moment bounds in exactly one direction: it uses no more spectral information, but it prevents all three horizontal curvature arguments from simultaneously occupying the only region where they could lie below the `ANF-059` threshold.

## 4. Consequences for near-extremizers

Assume now that

\[
\Delta>0,
\tag{19}
\]

which is equivalent to the one-dimensional statement `k_*<-K_0/3`. Then (5) immediately yields

\[
\boxed{
S\le\frac{E}{2\pi^4\varepsilon},
\qquad
r\le\frac{E}{2\pi^2\Delta}.
}
\tag{20}
\]

Thus any sequence with `E->0` has both total height scale and smaller-pair squared-height share tending to zero linearly in `E`. Since

\[
\frac{y_l}{y_h}=\sqrt{\frac{r}{1-r}},
\tag{21}
\]

the actual height ratio is `O(sqrt(E))`, not `O(E)`.

The same exact form (7) also controls the two high-weight horizontal arguments independently:

\[
g(t_h)
\le\frac{Q}{1-r}
\le\frac{E}{2\pi^2(1-r)}
\le\frac{E}{\pi^2},
\tag{22}
\]

and

\[
g(d)\le\frac{Q}{2}\le\frac{E}{4\pi^2}.
\tag{23}
\]

Under (19), `k_*<0`, while `K(t)->0` as `|t|->infinity`; hence the global minimizer set

\[
\mathcal M:=\{t:K(t)=k_*\}
\tag{24}
\]

is nonempty and compact. Equations (22)--(23) imply that every near-extremizing sequence satisfies

\[
\operatorname{dist}(t_h,\mathcal M)\to0,
\qquad
\operatorname{dist}(d,\mathcal M)\to0.
\tag{25}
\]

Consequently, if the remaining one-dimensional curvature problem establishes

\[
\mathcal M=\{-\tau,+\tau\}
\tag{26}
\]

for some `tau>0`, then every near-extremizer has, after subsequence extraction,

\[
t_h\to\sigma\tau,
\qquad
d\to\eta\tau,
\qquad
\sigma,\eta\in\{-1,+1\},
\tag{27}
\]

and therefore

\[
\boxed{
t_l=t_h-d\to0\quad\text{or}\quad t_l\to\pm2\tau.}
\tag{28}
\]

This proves the two proposed boundary families once uniqueness of the signed minimizers is known. A nondegenerate minimum `K''(tau)>0` would strengthen the qualitative convergence in (25) to the expected `O(sqrt(E))` horizontal deviations and is exactly the residual input needed for a full two-sided quadratic stability law.

## 5. Stress tests, prior art and evidence boundary

The argument is exact conditional only where it says it is conditional. Inequality (5) uses `Delta` with a positive part and therefore remains true even if the curvature minimum does not cross `-K_0/3`; in that case its pair-disappearance term becomes vacuous. The stronger consequences (20), (25), and (28) require `Delta>0`, while the two-branch classification additionally requires the minimizer-set statement (26). No numerical optimizer, sampled minimum, or unvalidated curvature picture is used as evidence for either missing fact.

The strict endpoints in `ANF-059` make the additive argument robust: values with `K<=theta` lie strictly inside `W`, and the numerical gaps `0.465<0.545` and `1.09>1.01` leave no boundary ambiguity. Relabelling by height is also essential for the uniform weight bound, because it gives `r<=1/2`. The conclusion concerns a squared-height share; translating it to the actual height ratio requires the square root in (21).

A targeted check of the closest Montgomery--Taylor extremal and recent pair-correlation literature finds the underlying extremal profile, pair-correlation inequalities, and critical-line proportion machinery, but no near-extremizer classification for this exact five-point curvature defect or an additive-annulus pair-disappearance estimate of the form (5). No external theorem is load-bearing here, so `SOURCES.md` requires no new anchor.

This finding does not prove uniqueness or nondegeneracy of the global curvature minimizer, does not extend the five-point theorem to larger conjugation-invariant multisets, and does not imply RH. Its durable contribution is to remove two parts of the accepted near-extremizer problem analytically: the total height scale and the smaller-pair mass are already forced to vanish at explicit rates once the single scalar crossing `k_*<-K_0/3` is certified. The remaining five-point rigidity question is genuinely one-dimensional: identify the global minimizer set of `K` and its local curvature.