# PL-322 — Vanishing integrated endpoint flux makes the residual moment automatic

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-GATE-REDUCTION + CONSERVATIVE-ENDPOINT-FLUX`

**Status:** `H-TRACE-NOT-NEEDED-FOR-MOMENT + CESARO-COEFFICIENT-FORCED + POINTWISE-QM-GATE-REMAINS`

## Precise claim

`PL-319` gives the exact endpoint identity

\[
F(Q)=2Qg(Q)-U(Q)+H_{Q_0}g(Q)+c_{Q_0}(Q)g(Q),
\qquad
U(Q)=\int_{Q_0}^{Q}g(P)\,dP,
\tag{PL322-1}
\]

where `Q_0>log 4`, `c_{Q_0}(Q)` is bounded and has a finite limit, and

\[
\begin{aligned}
H_{Q_0}g(Q)
={}&\int_0^{Q-Q_0}\frac{g(Q)-g(Q-h)}{e^h-1}\,dh\\
&+\int_0^\infty\frac{g(Q)-g(Q+h)}{e^h-1}\,dh.
\end{aligned}
\tag{PL322-2}
\]

`PL-320` extracted the critical coefficient and a conditionally convergent residual moment by additionally assuming that `H_{Q_0}g(Q)` has a finite pointwise limit. That assumption is not needed for those two conclusions.

Assume only

\[
g(Q)=O(Q^{-1/2}),
\qquad
F(Q)\longrightarrow F_\infty,
\tag{PL322-3}
\]

in the exact `PL-319` setting, with the singular remainder realized locally integrably as in (PL322-1). Then there is a unique `C in C` such that

\[
\boxed{
U(X)=2C\sqrt X-F_\infty+o(1),
}
\tag{PL322-4}
\]

and therefore

\[
\boxed{
C=\lim_{X\to\infty}\frac{1}{2\sqrt X}
\int_{Q_0}^{X}g(Q)\,dQ.
}
\tag{PL322-5}
\]

For

\[
m(Q):=g(Q)-CQ^{-1/2},
\tag{PL322-6}
\]

the improper residual moment converges automatically:

\[
\boxed{
\int_{Q_0}^{X}m(Q)\,dQ
\longrightarrow
2C\sqrt{Q_0}-F_\infty.
}
\tag{PL322-7}
\]

Thus source convergence plus the sharp critical envelope already force the coefficient in a primitive/Cesaro sense and supply exactly the conditional moment required by `PL-321`. The remaining pointwise gate is not the existence of the moment but

\[
\boxed{Qm(Q)\to0.}
\tag{PL322-8}
\]

Moreover, after (PL322-4)--(PL322-7), this gate is equivalent to vanishing of the singular endpoint flux:

\[
Qm(Q)\to0
\quad\Longleftrightarrow\quad
H_{Q_0}m(Q)\to0
\quad\Longleftrightarrow\quad
H_{Q_0}g(Q)\to0.
\tag{PL322-9}
\]

In particular, if `H_{Q_0}g(Q)` has any finite limit at all, that limit is necessarily zero. The `PL-320` pointwise trace hypothesis can therefore be narrowed from an unknown finite asymptotic datum to the single vanishing-flux gate (PL322-9).

For the actual completed-Weil endpoint state, the envelope in (PL322-3) is supplied by the sharp `ell(delta)^(1/2)` logarithmic-Laplacian boundary law of source 97 after `Q=-log delta`; `PL-319` supplies convergence of the completed-Weil source trace. No continuation of an Euler product or RH assumption enters this reduction.

## 1. The singular remainder is a conservative half-line flux

Put

\[
k(h)=\frac1{e^h-1}.
\tag{PL322-10}
\]

Then (PL322-2) is equivalently

\[
H_{Q_0}g(Q)
=
\int_{Q_0}^{\infty}
\bigl(g(Q)-g(P)\bigr)k(|Q-P|)\,dP,
\tag{PL322-11}
\]

with the same singular-integral interpretation as in `PL-319`. The kernel is symmetric. Hence, when this flux is integrated over a finite interval, all interactions internal to that interval cancel pairwise.

Let

\[
J(X):=\int_{Q_0}^{X}H_{Q_0}g(Q)\,dQ.
\tag{PL322-12}
\]

To make the cancellation literal, first truncate `k(h)` at `h=epsilon>0`, perform Fubini on the nonsingular kernel, and then pass to the locally integrable realization of (PL322-11). The square `[Q_0,X]^2` cancels by antisymmetry and only interactions crossing the endpoint `X` remain:

\[
\boxed{
J(X)
=
\int_0^\infty k(h)
\int_{\max(Q_0,X-h)}^{X}
\bigl(g(q)-g(q+h)\bigr)\,dq\,dh.
}
\tag{PL322-13}
\]

This identity is the key extra structure missing from the purely pointwise treatment in `PL-320`: `H` is not an arbitrary singular remainder. Its primitive is only a boundary flux through the moving cut `X`.

## 2. The integrated flux actually vanishes

Assume `X` is large compared with `Q_0`. For `0<h<=X/2`, every `q` in the inner interval of (PL322-13) satisfies `q>=X-h>=X/2`. The critical envelope gives

\[
\left|
\int_{X-h}^{X}
(g(q)-g(q+h))\,dq
\right|
\ll \frac{h}{\sqrt X}.
\tag{PL322-14}
\]

Since

\[
\int_0^\infty\frac{h}{e^h-1}\,dh<\infty,
\tag{PL322-15}
\]

the contribution of `h<=X/2` is `O(X^{-1/2})`.

For `h>X/2`, the inner integral is `O(sqrt X)` from `g(Q)=O(Q^{-1/2})`, while

\[
k(h)\ll e^{-h}.
\tag{PL322-16}
\]

That tail is `O(sqrt X e^{-X/2})`. Consequently

\[
\boxed{
J(X)=O(X^{-1/2})\longrightarrow0.
}
\tag{PL322-17}
\]

No pointwise limit of `H_{Q_0}g` has been used. The cancellation is purely the conservative symmetry of the exact half-line kernel plus the sharp endpoint envelope. In particular, (PL322-17) must not be confused with `H_{Q_0}g(Q)->0`; a function can have a vanishing primitive without having a pointwise limit.

## 3. Source convergence forces a primitive critical coefficient

Absorb the bounded lower-order coefficient into

\[
R(Q):=F(Q)-c_{Q_0}(Q)g(Q).
\tag{PL322-18}
\]

Because `g(Q)->0` and `c_{Q_0}` is bounded,

\[
R(Q)\longrightarrow F_\infty.
\tag{PL322-19}
\]

Define

\[
V(X):=\int_{Q_0}^{X}U(Q)\,dQ,
\qquad
A(X):=\int_{Q_0}^{X}R(Q)\,dQ.
\tag{PL322-20}
\]

Integrating (PL322-1) and using `U(Q_0)=0` gives the exact relation

\[
2XU(X)-3V(X)+J(X)=A(X).
\tag{PL322-21}
\]

Indeed, integration by parts gives

\[
\int_{Q_0}^{X}2Qg(Q)\,dQ
=2XU(X)-2V(X),
\tag{PL322-22}
\]

and the additional `-U` contributes the third copy of `-V`.

Set

\[
B(X):=A(X)-J(X).
\tag{PL322-23}
\]

By (PL322-17) and (PL322-19),

\[
B(X)=F_\infty X+o(X).
\tag{PL322-24}
\]

Since `U=V'`, equation (PL322-21) becomes

\[
2XV'(X)-3V(X)=B(X),
\tag{PL322-25}
\]

or

\[
\left(X^{-3/2}V(X)\right)'
=\frac{B(X)}{2X^{5/2}}.
\tag{PL322-26}
\]

The right side is `O(X^{-3/2})`, hence integrable at infinity. Therefore

\[
L:=\lim_{X\to\infty}X^{-3/2}V(X)
\tag{PL322-27}
\]

exists. Integrating (PL322-26) backward from infinity and using (PL322-24) yields

\[
V(X)=LX^{3/2}-F_\infty X+o(X).
\tag{PL322-28}
\]

Substituting in (PL322-25),

\[
U(X)=\frac{3V(X)+B(X)}{2X}
=\frac{3L}{2}\sqrt X-F_\infty+o(1).
\tag{PL322-29}
\]

With

\[
C:=\frac{3L}{4},
\tag{PL322-30}
\]

this is precisely (PL322-4). The coefficient is therefore not assumed and is not obtained from a pointwise quotient `sqrt(Q)g(Q)`; it is selected by the primitive of the actual source-coupled endpoint state.

Subtracting

\[
\int_{Q_0}^{X}CQ^{-1/2}\,dQ
=2C(\sqrt X-\sqrt{Q_0})
\tag{PL322-31}
\]

from (PL322-4) gives (PL322-7). This is exactly the conditional moment datum used by `PL-321`.

## 4. The only remaining endpoint gate is pointwise flux matching

Let

\[
b(Q)=CQ^{-1/2},
\qquad
g=b+m.
\tag{PL322-32}
\]

The model profile itself has vanishing singular flux:

\[
H_{Q_0}b(Q)\longrightarrow0.
\tag{PL322-33}
\]

For example, on `0<h<=Q/2`, the mean-value theorem gives

\[
|b(Q)-b(Q\pm h)|\ll |C|hQ^{-3/2},
\tag{PL322-34}
\]

which is integrable against `k(h)` by (PL322-15); the complementary `h`-range is exponentially suppressed by (PL322-16), including the fixed lower endpoint `Q_0`.

Write

\[
M(Q):=\int_{Q_0}^{Q}m(P)\,dP.
\tag{PL322-35}
\]

By (PL322-7),

\[
M(Q)\longrightarrow M_\infty
:=2C\sqrt{Q_0}-F_\infty.
\tag{PL322-36}
\]

Substituting `g=b+m` into (PL322-1), using

\[
2Qb(Q)-\int_{Q_0}^{Q}b(P)\,dP
=2C\sqrt{Q_0},
\tag{PL322-37}
\]

and then taking the convergent terms to infinity gives

\[
\boxed{
2Qm(Q)+H_{Q_0}m(Q)\longrightarrow0.
}
\tag{PL322-38}
\]

Because (PL322-33) also implies

\[
H_{Q_0}g(Q)-H_{Q_0}m(Q)\to0,
\tag{PL322-39}
\]

(PL322-38) proves all equivalences in (PL322-9).

There is also a useful rigidity check on any hypothesized finite trace limit. If `H_{Q_0}g(Q)->L_H`, then Cesaro averaging and (PL322-17) give

\[
L_H
=
\lim_{X\to\infty}
\frac{J(X)}{X-Q_0}
=0.
\tag{PL322-40}
\]

Thus the finite limit assumed in `PL-320`, if it exists, cannot be a new endpoint constant: it is forced to vanish.

## 5. What this does and does not close

The analytic chain is now sharper. In the exact completed-Weil endpoint problem,

\[
F(Q)\to F_\infty
\quad+\quad
g(Q)=O(Q^{-1/2})
\tag{PL322-41}
\]

already imply a canonical primitive coefficient `C` and the conditional residual moment (PL322-7). If one can additionally prove the single pointwise statement `Qm(Q)->0` -- equivalently `H_{Q_0}g(Q)->0` -- then `PL-321` transfers that residual moment through the moving Green kernel. The separate hypothesis that the singular remainder merely has some finite limit is no longer structurally informative.

This finding **does not prove** the remaining pointwise gate. In particular:

- (PL322-17) is an integrated cancellation and cannot be upgraded to pointwise flux decay without further input;
- `PL-318` remains the matched obstruction showing that bounded logarithmic forcing, smoothness, and even absolute residual integrability do not force `Qm(Q)->0`;
- no absolute `L^1` bound for `m` is obtained or needed;
- no monotonicity, sign, or positivity of the endpoint state is assumed;
- the conservative-kernel argument is universal real-variable structure, so it is not an arithmetic sign mechanism and does not by itself advance the first-crossing/RH gate.

The substantive progress is instead a gate reduction: the source-coupled endpoint identity contains enough conservation to make the residual moment automatic. What remains is genuinely pointwise matching of the endpoint state to its forced critical profile.

## Novelty and prior-art audit

The symmetric cancellation behind (PL322-13) is classical jump-kernel/conservative-flux geometry in spirit; it is not claimed as a new theorem about nonlocal operators. Sources 96 and 97 already supply the logarithmic-Laplacian realization and the sharp boundary scale used here. A targeted audit around logarithmic-Laplacian endpoint regularity, Volterra asymptotics, nonlocal flux identities, and critical boundary traces did not locate the specific implication (PL322-3) -> (PL322-4)--(PL322-7) for the exact transformed `PL-319` source identity.

Accordingly the line-specific claim is narrow: combining the exact completed-Weil endpoint balance from `PL-319` with its conservative singular remainder removes the `H(Q)->H_infinity` hypothesis from the coefficient/moment extraction in `PL-320`. This is a derived internal gate reduction, not a claim of a new general PDE principle.

The adversarial controls are `PL-318` (regularity/forcing without source convergence does not close the pointwise gate), `PL-320` (previous stronger trace hypothesis), and `PL-321` (conditional moment is already enough once `Qm->0`). The prime-specific arithmetic sign/first-crossing problem remains downstream and untouched.

## Sources

- `PL-318`, bounded logarithmic forcing and endpoint regularity do not force the moving-diagonal condition.
- `PL-319`, exact endpoint source/trace identity and bounded coefficient `c_{Q_0}`.
- `PL-320`, source-trace plus pointwise singular-remainder convergence previously used to extract the critical tail and conditional residual moment.
- `PL-321`, conditional residual moments suffice for the moving Green transfer once `Qm(Q)->0`.
- Source 96: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian* (2019), for the exact logarithmic-Laplacian singular-integral framework.
- Source 97: Víctor Hernández-Santamaría, Luis Fernando López Ríos, and Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian* (2025), for the sharp `ell(delta)^(1/2)` boundary envelope.