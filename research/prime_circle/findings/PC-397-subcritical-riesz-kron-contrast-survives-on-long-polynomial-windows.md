# PC-397 — subcritical Riesz Kron contrast survives on sufficiently long polynomial windows

**Status:** `ASYMPTOTIC-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` + `MATCHED-CONTROL-CLASSICALIZATION` for the genuinely nonsummable positive inverse-distance branch `0<alpha<1/2` left open by PC-396.

PC-395 and PC-396 show that the irreducible simultaneous-deletion Kron correction `Delta_T` vanishes on every fixed polynomial primorial window throughout `alpha>=1/2`. The remaining question is whether the slower positive tail `alpha<1/2` merely defeats those upper bounds or can actually carry an unscaled interaction of macroscopic size.

It can. Put `beta=2 alpha in (0,1)`, let `H=p^u`, let `q` be the next prime after `p`, and use the normalized regularized chord kernel of PC-390--PC-396. If

\[
\boxed{
 u>\frac{2}{1-\beta}=\frac{2}{1-2\alpha},
}
\tag{1}
\]

then the exact simultaneous-deletion correction satisfies the lower bound

\[
\boxed{
 \|\Delta_T\|_{\rm op}
 \gg_{\alpha,\tau,u}
 \frac{H^{1-2\alpha}}{q^2\log p}
 \asymp
 \frac{p^{u(1-2\alpha)-2}}{\log p}
 \longrightarrow\infty.
}
\tag{2}
\]

Thus the positive nonsummable phase is qualitatively different from the critical endpoint: for every fixed `0<alpha<1/2`, sufficiently long but still fixed polynomial windows preserve a genuine unscaled simultaneous-deletion contrast. The effect is not, however, evidence for a new zeta mechanism. Its leading lower-bound mechanism uses only the macroscopic Buchstab densities of the two rough-number clouds and the Euclidean Riesz tail; matched equidistributed point clouds with the same density scales reproduce it.

## 1. The exact Schur correction is asymptotic to the deleted-layer Laplacian on its active sector

Keep the successive-primorial notation of PC-391--PC-396,

\[
S=R_q(H),
\qquad
T=qR_p(H/q),
\tag{3}
\]

with survivor-to-deleted conductance matrix `B`, deleted survivor degrees `D=diag(d_i)`, and deleted-layer weighted Laplacian `K`. The exact factorization is

\[
\Delta_T=PQP^\top,
\qquad
P=BD^{-1},
\qquad
Q=D-D(D+K)^{-1}D.
\tag{4}
\]

At `beta=2 alpha in (0,1)`, the local-arc chord asymptotics give

\[
\kappa_M(d)\asymp_{\alpha,\tau}d^{-\beta}
\qquad(1\le d\le H=o(M)).
\tag{5}
\]

The prime reservoir used in PC-396 works throughout the subcritical phase. Every prime in `[H/2,H]` is a survivor once `p` is large, and the prime number theorem therefore gives, uniformly in `t_i in T`,

\[
d_i
=\sum_{a\in S}\kappa_M(|a-t_i|)
\gg_{\alpha,\tau,u}
\frac{H^{1-\beta}}{\log H}.
\tag{6}
\]

On the other hand the deleted points are `q`-separated. Hence their internal weighted degree obeys

\[
\max_i\sum_{j\ne i}\kappa_M(|t_i-t_j|)
\ll_{\alpha,\tau}
q^{-\beta}\sum_{1\le h\le H/q}h^{-\beta}
\ll_{\alpha,\tau}
\frac{H^{1-\beta}}q,
\tag{7}
\]

and consequently

\[
\|K\|_{\rm op}
\ll_{\alpha,\tau}
\frac{H^{1-\beta}}q.
\tag{8}
\]

Define the positive semidefinite matrix

\[
A=D^{-1/2}KD^{-1/2}.
\tag{9}
\]

Equations (6)--(8) imply

\[
\|A\|_{\rm op}
\ll_{\alpha,\tau,u}
\frac{\log H}{q}
=o(1).
\tag{10}
\]

The exact parallel-sum form of `Q` is

\[
Q
=D^{1/2}A(I+A)^{-1}D^{1/2}.
\tag{11}
\]

Since the scalar function `lambda/(1+lambda)` lies between `lambda/(1+epsilon)` and `lambda` on `[0,epsilon]`, (10) gives the two-sided Loewner estimate

\[
\boxed{
(1+o(1))K\preceq Q\preceq K.
}
\tag{12}
\]

This is the useful reversal of the upper-bound viewpoint in PC-394--PC-396: in the nonsummable polynomial-window regime, the deleted-to-survivor coupling is so much stronger than deleted-to-deleted coupling that the exact irreducible Schur response retains the deleted-layer Laplacian to leading order rather than suppressing it.

## 2. Buchstab asymptotics make both boundary clouds macroscopically equidistributed

PC-388 identifies `R_x(X)` exactly with the classical `x`-rough numbers and records the fixed-parameter Buchstab asymptotic

\[
|R_x(x^v)|\sim \omega(v)\frac{x^v}{\log x}
\qquad(v>1\text{ fixed}).
\tag{13}
\]

The same formula applied to fixed macroscopic subintervals gives weak equidistribution after scaling. Indeed, for every fixed `0<a<b<=1`, subtraction of the cumulative asymptotics at `aH` and `bH` yields

\[
\#\{s\in S:aH\le s\le bH\}
\sim
\omega(u)(b-a)\frac H{\log p},
\tag{14}
\]

because `log q/log p ->1` and the corresponding Buchstab parameter differs from `u` by `o(1)`. Likewise, since

\[
\frac Hq=p^{u-1+o(1)},
\tag{15}
\]

for `u>2`,

\[
\#\{t\in T:aH\le t\le bH\}
\sim
\omega(u-1)(b-a)\frac H{q\log p}.
\tag{16}
\]

Thus the survivor and deleted empirical measures are asymptotically Lebesgue at macroscopic scale, with density ratio of order `1/q`. Their fine support remains the exact rough-number wheel, but the bulk distribution needed below is classical Buchstab density only.

## 3. A macroscopic test vector sees different normalized Riesz profiles at opposite ends

Let

\[
g(x)=x,
\qquad
f_a=\frac{g(a/H)}{\left(\sum_{s\in S}g(s/H)^2\right)^{1/2}},
\qquad a\in S.
\tag{17}
\]

Then `||f||_2=1`, and (14) implies

\[
\sum_{s\in S}g(s/H)^2
\asymp_u \frac H{\log p}.
\tag{18}
\]

For a deleted point `t` with `y=t/H` in a compact subinterval of `(0,1)`, the `t`-th coordinate of `P^T f` is the normalized star average

\[
(P^Tf)_t
=
\frac{1}{\|g\|_{\ell^2(S)}}
\frac{\sum_{s\in S}\kappa_M(|s-t|)g(s/H)}
{\sum_{s\in S}\kappa_M(|s-t|)}.
\tag{19}
\]

Because `beta<1`, the limiting Riesz singularity is integrable. Equations (5) and (14), followed by ordinary partial summation and truncation around `x=y`, therefore give

\[
\frac{\sum_{s\in S}\kappa_M(|s-t|)g(s/H)}
{\sum_{s\in S}\kappa_M(|s-t|)}
\longrightarrow
F_\beta(y)
:=
\frac{\int_0^1x|x-y|^{-\beta}\,dx}
{\int_0^1|x-y|^{-\beta}\,dx}.
\tag{20}
\]

The limit is not constant for any `beta>0`. At the endpoints,

\[
F_\beta(0)=\frac{1-\beta}{2-\beta},
\qquad
F_\beta(1)=\frac1{2-\beta},
\tag{21}
\]

so their difference is `beta/(2-beta)>0`. By continuity, choose a fixed small `delta>0` and the two intervals

\[
I_-=[\delta,2\delta],
\qquad
I_+=[1-2\delta,1-\delta]
\tag{22}
\]

so that `F_beta` differs by at least a fixed `c_beta>0` between them. Combining (18)--(20), for all sufficiently large `p`,

\[
\boxed{
|(P^Tf)_t-(P^Tf)_{t'}|
\gg_{\alpha,u}
\left(\frac{\log p}{H}\right)^{1/2}
}
\tag{23}
\]

whenever `t/H in I_-` and `t'/H in I_+`.

The key point is geometric rather than number-theoretic: a genuinely nonsummable positive Riesz star remembers where its center lies on the macroscopic interval after normalization. At `beta=0` the limiting profile becomes constant and this contrast disappears exactly, while for every fixed `beta>0` it is nonzero.

## 4. Cross-window deleted pairs force a macroscopic Kron lower bound

Let

\[
T_-:=\{t\in T:t/H\in I_-\},
\qquad
T_+:=\{t\in T:t/H\in I_+\}.
\tag{24}
\]

By (16),

\[
|T_-|,|T_+|
\asymp_u
\frac H{q\log p}.
\tag{25}
\]

Every cross pair `(t,t') in T_- x T_+` has distance comparable with `H`; hence (5) supplies

\[
\kappa_M(|t-t'|)\gg_{\alpha,\tau,u}H^{-\beta}.
\tag{26}
\]

Put `x=P^Tf`. The quadratic form of the deleted-layer Laplacian satisfies

\[
\begin{aligned}
x^TKx
&=\sum_{i<j}\kappa_M(|t_i-t_j|)(x_i-x_j)^2\\
&\ge
\sum_{t\in T_-}\sum_{t'\in T_+}
\kappa_M(|t-t'|)(x_t-x_{t'})^2.
\end{aligned}
\tag{27}
\]

Using (23), (25), and (26),

\[
\boxed{
x^TKx
\gg_{\alpha,\tau,u}
H^{-\beta}
\left(\frac H{q\log p}\right)^2
\frac{\log p}{H}
=
\frac{H^{1-\beta}}{q^2\log p}.}
\tag{28}
\]

Finally (12) gives

\[
\|\Delta_T\|_{\rm op}
\ge f^T\Delta_Tf
=x^TQx
\ge(1-o(1))x^TKx,
\tag{29}
\]

which proves (2). Since `q\asymp p`, the lower bound diverges exactly under condition (1).

This does not claim a sharp transition at equality. The proof establishes a one-sided survival region. At `u=2/(1-beta)` the displayed lower scale is `1/log p`, and the present argument does not decide whether a different mode remains order one there. Likewise, for `2<u<2/(1-beta)` it does not improve PC-396 into a vanishing theorem; it only shows that sufficiently long windows genuinely escape the critical/summable no-go.

## 5. Prior-art, matched controls, and novelty boundary

The ingredients are classical separately. Dörfler--Bullo supplies the general Kron/Schur framework already anchored in `SOURCES.md`. The rough-number input is precisely the Buchstab/de Bruijn theory used in PC-388; a modern explicit source is Kai Fan, *Numerically explicit estimates for the distribution of rough numbers*, Journal of Number Theory 260 (2024), 120--150, DOI `10.1016/j.jnt.2024.01.008`, arXiv:2306.03347. The circle Riesz kernel and its scalar energies lie in the classical literature represented by Brauchart--Hardin--Saff, *The Riesz energy of the Nth roots of unity: an asymptotic expansion for large N*, Bulletin of the London Mathematical Society 41 (2009), 621--633, DOI `10.1112/blms/bdp034`, arXiv:0808.1291, already used as a novelty boundary in PC-396.

Targeted searches for combinations of Kron reduction, Riesz/power-law conductances, and rough-number or sifted supports did not locate a theorem matching (12)--(29). Absence from search is not a novelty proof. More importantly, the mechanism itself fails a strong arithmetic-specificity test: equations (23)--(28) need only two macroscopically equidistributed point clouds with survivor cardinality `asymp H/log p`, deleted cardinality `asymp H/(q log p)`, and the positive tail `d^{-beta}`. Replacing the rough-number supports by matched near-uniform deterministic clouds at those densities reproduces the same lower-bound scaling.

Therefore the surviving unscaled contrast in (2) is **not by itself an RH-facing arithmetic signal**. It is a generic macroscopic long-range Riesz/Kron mode whose density constants happen to be supplied here by Buchstab's rough-number sieve. Prime-specific information, if any survives in this regime, must live beyond this leading density mode—for example in centered fluctuations around the Buchstab continuum profile, cross-level orientation of the contrast spaces, or another source-forced observable that a matched equidistributed control does not reproduce.

## 6. Falsification boundary

The result uses four load-bearing facts: the exact factorization (4), the prime-reservoir lower bound (6), `q`-spacing of the deleted layer, and fixed-parameter Buchstab asymptotics on macroscopic subintervals. The lower bound can fail only if one of those ingredients is misapplied, or if the normalized Riesz star averages in (20) do not converge to their integrable continuum profile.

The latter is directly testable without any RH-scale computation: for fixed `alpha<1/2` and `u>2`, form the finite survivor/deleted sets, evaluate the star means in (19) for deleted points near `delta H` and `(1-delta)H`, and compare their separation with `F_beta`. Independently, the exact matrix inequality in (12) can be checked through the largest eigenvalue of `D^{-1/2}KD^{-1/2}`; the proof predicts `O(log p/p)`.

## Consequence for the research line

PC-396 marks `alpha=1/2` as a genuine endpoint rather than an artifact of the summability proof. For every fixed `alpha<1/2`, there are fixed polynomial windows on which the positive simultaneous-deletion correction survives and even diverges unscaled. The remaining research question is therefore no longer whether nonsummability can preserve a contrast at all; it can. The RH-relevant question is whether **after removing this generic Buchstab-density/Riesz continuum mode**, any centered or cross-level residue retains arithmetic information that is not already present in the rough-number support or a matched control.