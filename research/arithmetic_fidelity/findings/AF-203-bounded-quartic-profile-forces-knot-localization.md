# AF-203 — Bounded quartic profile forces knot localization

**Status:** `EXACT-DERIVED`, `SOURCE-COERCIVITY`, `QUANTITATIVE-RECOVERY`, `ARITHMETIC-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-202 identifies anchored knot-diameter collapse as the exact source-side localization topology for the five-node quartic minimal-support class once the homogeneous profile stays bounded. The profile bound itself already supplies that localization coercivity.

Let

\[
x=u_0<u_1<u_2<u_3<u_4,
\qquad
D:=u_4-u_0,
\]

and let `nu=mu_+-mu_-` be the normalized five-node minimal-support control from AF-195/AF-199: `mu_+` and `mu_-` are mutually singular probabilities and `nu` annihilates powers through degree three. Write

\[
\delta:=W_1(\mu_+,\mu_-)>0,
\qquad
M_4:=\int u^4\,d\nu(u)>0,
\qquad
Q:=\frac{M_4}{\delta^4}.
\]

Then every such source satisfies the universal quantitative properness estimate

\[
\boxed{
D\,\delta^3\le 3M_4,
\qquad\text{equivalently}\qquad
D\le 3Q\delta.
}
\tag{1}
\]

The constant `3` is only a convenient exact certificate and is not claimed sharp.

Consequently, for any sequence in this class,

\[
\boxed{
\sup_n Q_n<\infty,
\qquad
\delta_n\to0
\quad\Longrightarrow\quad
D_n\to0.
}
\tag{2}
\]

Thus **bounded homogeneous quartic profile is already a projective coercivity condition**: no separate compact gap-ratio assumption, bounded `D/delta`, Peano first-moment bound, or source tightness hypothesis is required to obtain the AF-202 localization gate.

Combining `(1)` with AF-201/AF-202 gives a useful varying-profile sufficient condition as well. Since the normalized Peano carrier is supported in `[x,x+D]`, the AF-201 finite-band derivative estimate gives

\[
\sup_{|\tau|\le T}
\left|
\frac1{\delta^4}\int F_{\sigma+i\tau}\,d\nu
-
\frac{Q}{24}F_{\sigma+i\tau}^{(4)}(x)
\right|
\le
\frac{L_5}{24}QD.
\tag{3}
\]

Therefore `(1)` implies

\[
\boxed{
\text{transfer error}
\le
\frac{L_5}{8}Q^2\delta.
}
\tag{4}
\]

In particular, the weaker profile-scale gate

\[
Q_n^2\delta_n\to0
\tag{5}
\]

already forces uniform fixed-band transfer, even when `Q_n` is not bounded. Bounded `Q_n` is a simple special case of `(5)`.

This does **not** make full-Euler sublevels coercive. AF-200's symmetric escape family has `delta->0`, normalized full Euler discrepancy tending to zero, but `Q->infinity` and physical diameter escaping. Hence an unrestricted full-Euler sublevel does not by itself imply the profile bound needed in `(2)`. What `(1)` closes is the source-geometry question: once `Q` is controlled, diameter localization follows automatically.

## Derivation

### 1. Exact gap formulas

Translation does not affect the quantities above, so set `u_0=0` and write the four positive gaps as

\[
a=u_1-u_0,
\quad b=u_2-u_1,
\quad c=u_3-u_2,
\quad d=u_4-u_3,
\quad D=a+b+c+d.
\tag{6}
\]

For the divided-difference weights

\[
\lambda_j=\frac1{\prod_{\ell\ne j}(u_j-u_\ell)},
\]

the signs alternate `+,-,+,-,+`. AF-195/AF-199 normalize by

\[
A=\lambda_0+\lambda_2+\lambda_4
=-\lambda_1-\lambda_3.
\]

Direct simplification gives

\[
\boxed{
A=
\frac{ab+ad+cd}
{abcd\,(a+b+c)(b+c+d)}
}
\tag{7}
\]

and therefore

\[
\boxed{
M_4=\frac1A
=
\frac{abcd\,(a+b+c)(b+c+d)}
{ab+ad+cd}.
}
\tag{8}
\]

For the signed cumulative distribution `F_nu`, the signs on the four gap intervals alternate. The one-dimensional transport identity used in AF-199 gives

\[
\delta=\int |F_\nu(t)|\,dt.
\]

Summing the four constant gap contributions and simplifying yields

\[
\boxed{
\delta=
\frac{2abcd\,P(a,b,c,d)}
{(a+b)(b+c)(c+d)(ab+ad+cd)D},
}
\tag{9}
\]

where

\[
\begin{aligned}
P={}&a^2b+2a^2c+a^2d+2ab^2+6abc+3abd
+3ac^2+3acd+ad^2\\
&+b^3+5b^2c+3b^2d+5bc^2+6bcd+2bd^2
+c^3+2c^2d+cd^2.
\end{aligned}
\tag{10}
\]

Equations `(8)` and `(9)` are exact rational identities; no asymptotic regime or shape restriction has entered.

### 2. A positive-coefficient projective certificate

Substituting `(8)` and `(9)` into `3M_4-D delta^3` and clearing the positive denominator reduces `(1)` to

\[
H(a,b,c,d)\ge0,
\tag{11}
\]

with the compact exact definition

\[
\begin{aligned}
H:={}&3(a+b)^3(b+c)^3(c+d)^3(ab+ad+cd)^2D^2
(a+b+c)(b+c+d)\\
&-8a^2b^2c^2d^2P(a,b,c,d)^3.
\end{aligned}
\tag{12}
\]

Expanding `(12)` over `Z[a,b,c,d]` gives a homogeneous degree-17 polynomial with `598` nonzero monomials; every coefficient is a positive integer, with minimum coefficient `3`. Since `a,b,c,d>0`, this is a finite exact positivity certificate for `(11)` and hence `(1)`.

The coefficient certificate is deliberately used only for a nonsharp coercive constant. The sharp constant in

\[
D\delta^3\le C_*M_4
\]

is a separate optimization problem and is unnecessary for localization.

### 3. Coercivity and Euler transfer

Equation `(1)` immediately gives `(2)`. AF-202 then turns `D_n->0` into weak concentration of the normalized Peano carrier at the anchored endpoint, and AF-201 turns that concentration into uniform finite-band Euler transfer when `Q_n` stays bounded.

There is also a direct estimate that avoids invoking weak convergence. AF-199 writes the normalized Euler observation exactly as the Peano average of `F_s^(4)`. Because the carrier support lies inside `[x,x+D]`, the uniform finite-band Lipschitz constant

\[
L_5=
\sup_{u\ge x,\ |\tau|\le T}
|F_{\sigma+i\tau}^{(5)}(u)|
\]

gives `(3)`. Substituting `D<=3Q delta` proves `(4)` and `(5)`.

Thus the quartic profile has two roles that had previously been treated separately: it is the homogeneous response coefficient, and its boundedness prevents projective knot escape quickly enough to force physical localization as `W_1->0`.

## Consequence for the accepted localization clue

AF-200 showed that `W_1` alone is noncoercive. AF-201 identified the exact bounded-profile observation topology, and AF-202 translated that topology to knot diameter. Equation `(1)` now closes the specific projective-properness test left open there:

\[
Q=O(1),\quad W_1\to0
\quad\Longrightarrow\quad
D\to0.
\]

The residual is no longer whether bounded `Q` needs an extra source-localization hypothesis. It does not. The remaining issue is whether one can weaken the profile-scale condition beyond `(5)`, and, separately, whether any natural constrained full-Euler problem supplies such profile control. Unrestricted normalized full-Euler sublevels cannot do so because AF-200 already supplies an escaping sublevel sequence.

## Prior art and novelty assessment

The ingredients preceding the final projective inequality are classical or already audited in AF-195/AF-199: barycentric divided-difference weights, Peano/B-spline representation, and the one-dimensional cumulative-distribution formula for `W_1`. Carl de Boor's survey *Divided Differences* (Surveys in Approximation Theory 1, 2005; arXiv:math/0502036) is a primary reference for the divided-difference/Peano side. General Kolmogorov-type derivative inequalities and moment-space principal representations are adjacent literatures, but a targeted search did not identify the specific five-knot bound `(1)` as a named theorem.

No novelty claim is made for the underlying divided-difference or transport identities, nor for the broad fact that spline shape can be controlled by derivative inequalities. The durable result here is their exact quartic specialization `(1)` and its consequence for the AF-200--AF-202 localization frontier. The nonsharp coefficient `3` is chosen because it admits the direct positive-coefficient certificate `(12)` rather than because it is believed optimal.

## Boundaries

- The proof is for the **five-node minimal-support quartic** control class. It is not yet a theorem for arbitrary non-minimal-support moment-flat measures or other cancellation orders.
- The constant `3` is nonsharp. No sharp projective constant or equality case is claimed.
- Bounded `Q` is sufficient for diameter localization, not claimed to be the weakest possible varying-profile transfer condition. Equation `(5)` already allows some growth of `Q`.
- The result does not show that unrestricted full-Euler sublevels bound `Q`; AF-200 shows the opposite for the normalized fixed-band objective.
- Uniformity is for a fixed finite vertical band and fixed `sigma>0`. Growing-band behavior remains separate.
- No prime-specificity, zero-selection, RH implication, or arithmetic uniqueness is established.