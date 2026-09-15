# PL-319 — A convergent logarithmic source trace forces the moving-tail law after leading boundary matching

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-TAIL-MECHANISM + SOURCE-TRACE-REDUCTION`

**Status:** `SOURCE-TRACE-TAUBERIAN-EQUIVALENCE + MOVING-DIAGONAL-GATE-REDUCED + RESIDUAL-DINI/INTEGRABILITY-OPEN`

## Precise claim

`PL-314` shows that the completed-Weil corner transfer is stable once a logarithmic endpoint mismatch `m(Q)` satisfies

\[
m\in L^1(0,\infty),\qquad Qm(Q)\to0,
\]

and `PL-315`--`PL-318` show that this pointwise tail law does not follow from weighted integrability, all finite logarithmic Fourier moments, `BV/W^{k,1}` regularity, critical zero-extension `H^{1/2}`, or even bounded logarithmic-Poisson forcing. The remaining question is whether the **actual source relation** can suppress the sparse moving-diagonal saturation.

For the one-dimensional Dirichlet logarithmic Laplacian, there is an exact endpoint-coordinate identity that does so once the residual has a mild vanishing local-Dini remainder.

Fix `Q_0>log 4`, put

\[
d_0=2e^{-Q_0}<\frac12,
\qquad
x_Q=1-2e^{-Q},
\]

and let `m\in W^{2,1}(Q_0,\infty)`. Define a right-endpoint tail profile by

\[
u(x)=
\begin{cases}
m\!\left(-\log\frac{1-x}{2}\right),&1-d_0<x<1,\\
0,&\text{otherwise},
\end{cases}
\tag{PL319-1}
\]

with an inessential smooth cutoff at `Q_0` if a globally regular representative is desired. Let

\[
F(Q)=(L_\Delta u)(x_Q).
\]

Then

\[
\boxed{
F(Q)=2Qm(Q)-\int_{Q_0}^{Q}m(P)\,dP+H_{Q_0}m(Q)+c_{Q_0}(Q)m(Q),
}
\tag{PL319-2}
\]

where

\[
\begin{aligned}
H_{Q_0}m(Q)
={}&\int_0^{Q-Q_0}
\frac{m(Q)-m(Q-h)}{e^h-1}\,dh\\
&+\int_0^\infty
\frac{m(Q)-m(Q+h)}{e^h-1}\,dh,
\end{aligned}
\tag{PL319-3}
\]

and

\[
c_{Q_0}(Q)=\rho_1-2\log2-\log\!\left(1-e^{-(Q-Q_0)}\right).
\tag{PL319-4}
\]

Here `rho_1` is the scalar constant in Chen--Weth's one-dimensional singular-integral realization of `L_Delta`.

The Sobolev hypothesis is only a convenient sufficient condition for the local singular remainder. It gives

\[
H_{Q_0}m(Q)\to0,
\qquad
m(Q)\to0,
\qquad
\int_{Q_0}^{Q}m(P)\,dP\to M:=\int_{Q_0}^\infty m(P)\,dP,
\]

and therefore the exact asymptotic

\[
\boxed{
F(Q)=2Qm(Q)-M+o(1).
}
\tag{PL319-5}
\]

Consequently

\[
\boxed{
\lim_{Q\to\infty}F(Q)\ \text{exists}
\quad\Longleftrightarrow\quad
Qm(Q)\to0,
}
\tag{PL319-6}
\]

and in that case

\[
\boxed{
\lim_{Q\to\infty}F(Q)=-\int_{Q_0}^\infty m(P)\,dP.
}
\tag{PL319-7}
\]

The reverse implication in (PL319-6) uses integrability in an essential Tauberian way: if `F(Q)` converges, (PL319-5) forces `Qm(Q)` to have a finite limit; any nonzero limit would imply `|m(Q)|\gtrsim1/Q` eventually and contradict `m\in L^1`.

Thus, after leading boundary matching has produced an integrable residual with enough local-Dini control to make `H_{Q_0}m(Q)->0`, **existence of the logarithmic-Poisson source trace is equivalent to the exact moving-tail condition required by `PL-314`**. For the completed-Weil eigenstate the source trace is structurally much easier than the tail itself, because the zero-order eigen-equation expresses `L_Delta u` through finitely many fixed translations, a continuous archimedean remainder, and scalar multiples of the state.

## 1. Exact derivation in logarithmic endpoint coordinates

Chen--Weth's one-dimensional formula, in the normalization already used in `PL-289` and `PL-318`, is

\[
L_\Delta u(x)
=
\int_{\mathbb R}
\frac{u(x)\mathbf1_{|x-y|<1}-u(y)}{|x-y|}\,dy
+\rho_1u(x).
\tag{PL319-8}
\]

Write

\[
\delta=1-x_Q=2e^{-Q},
\qquad
z=1-y=2e^{-P}.
\]

Because the tail is supported in `0<z<d_0<1/2`, every pair of points inside that tail lies inside the local unit ball. The right exterior interval `z<0` contributes

\[
m(Q)\log\frac1\delta,
\tag{PL319-9}
\]

while the local zero region `z>d_0` contributes

\[
-m(Q)\log(d_0-\delta).
\tag{PL319-10}
\]

For the internal tail, the Jacobian is `dz=-z\,dP`. When `P<Q`,

\[
\frac{z}{z-\delta}
=
\frac1{1-e^{-(Q-P)}}
=
1+\frac1{e^{Q-P}-1},
\tag{PL319-11}
\]

whereas for `P>Q`,

\[
\frac{z}{\delta-z}
=
\frac1{e^{P-Q}-1}.
\tag{PL319-12}
\]

Therefore the internal integral equals

\[
(Q-Q_0)m(Q)-\int_{Q_0}^{Q}m(P)\,dP+H_{Q_0}m(Q).
\tag{PL319-13}
\]

Finally,

\[
\log\frac1\delta-\log(d_0-\delta)+(Q-Q_0)
=
2Q-2\log2-\log\!\left(1-e^{-(Q-Q_0)}\right),
\]

which gives (PL319-2) exactly. The coefficient `2Q` is not an asymptotic guess: one factor of `Q` comes from the exterior Dirichlet interaction and the other from the one-sided internal kernel after the transformation to logarithmic distance.

## 2. The singular translation remainder vanishes under a simple tail condition

The kernel in (PL319-3) behaves like `1/h` at the origin and decays exponentially for large `h`. For `0<h<1`, the mean-value theorem gives, once `Q` is large,

\[
|m(Q)-m(Q\pm h)|
\le
h\sup_{P\ge Q-1}|m'(P)|.
\]

Since `m\in W^{2,1}(Q_0,\infty)`, both `m'\in L^1` and `m''\in L^1`; choosing the absolutely continuous representative gives

\[
\sup_{P\ge R}|m'(P)|
\le\int_R^\infty |m''(t)|\,dt\to0.
\tag{PL319-14}
\]

Thus the `h<1` part of `H_{Q_0}m(Q)` tends to zero. For `h\ge1`, use `(e^h-1)^{-1}\le Ce^{-h}`. Split the left integral at `h=(Q-Q_0)/2`: on the first part both arguments lie in the tail where `m->0`, while on the second part the exponential kernel contributes `O(e^{-(Q-Q_0)/2})||m||_\infty`. The right integral is analogous. Hence

\[
\boxed{H_{Q_0}m(Q)\to0.}
\tag{PL319-15}
\]

Nothing special about `W^{2,1}` is claimed. The exact load-bearing condition is simply the vanishing of (PL319-3); a Dini-type tail modulus, a suitable derivative estimate, or another source-specific regularity theorem could replace `W^{2,1}`.

## 3. Why the `Q^{-1/2}` boundary law is compatible with a finite source trace

The sharp logarithmic-Laplacian boundary theory in source 97 gives the canonical scale

\[
u(x)\asymp |\log\operatorname{dist}(x,\partial I)|^{-1/2}.
\]

In the coordinate `Q`, the corresponding model is

\[
b(Q)=CQ^{-1/2}.
\]

Although `b` is not integrable in `dQ`, the two large terms in (PL319-2) cancel at leading order:

\[
2Qb(Q)=2C\sqrt Q,
\qquad
\int^{Q}b(P)\,dP=2C\sqrt Q+O(1).
\tag{PL319-16}
\]

Moreover its local singular remainder tends to zero. After a smooth cutoff away from the endpoint, `L_Delta b(x_Q)` therefore has a finite one-sided limit. This is an exact structural reason that the `Q^{-1/2}` Hopf scale can coexist with a finite zero-order source: it is the borderline profile on which the exterior `Qm(Q)` growth cancels the accumulated internal mass.

This matters for `PL-313`--`PL-318`. The theorem above is not to be applied to the leading `Q^{-1/2}` profile itself. It applies to the **residual after that coefficient has been matched**. If

\[
u(x_Q)=CQ^{-1/2}+m(Q)
\tag{PL319-17}
\]

with `m\in W^{2,1}` in the tail, then both `L_Delta u` and the cutoff model `L_Delta(CQ^{-1/2})` have finite endpoint traces exactly when the residual satisfies the PL-314 moving-tail law.

## 4. The completed-Weil eigen-equation supplies the source trace, not yet the residual class

On a source-static aperture interval, `PL-291` writes Suzuki's fixed-domain operator as

\[
A_a=T+K_a,
\qquad
T=\frac12L_\Delta+\gamma I,
\tag{PL319-18}
\]

where `K_a` is a scalar term plus finitely many compressed prime-power translations and the continuous archimedean completion kernel. For an eigenstate,

\[
Tu=(\lambda-K_a)u.
\tag{PL319-19}
\]

The established logarithmic-Laplacian boundary theory gives a continuous zero boundary trace for the state, and interior continuity. Hence, at the right endpoint, every active fixed lag `h in (0,2)` has

\[
C_hu(x)\to0,
\qquad
C_{-h}u(x)\to u(1-h)
\qquad(x\uparrow1),
\tag{PL319-20}
\]

while the continuous completion term has a finite boundary limit by its integral-kernel regularity. Equation (PL319-19) therefore gives a finite one-sided endpoint limit for `L_Delta u`. The same holds at the left endpoint by reflection.

This is exactly the extra property absent from the counterexamples in `PL-315`--`PL-318`: their sparse `1/Q` saturation forces the logarithmic source to retain endpoint oscillations rather than converge. In particular, `PL-318` remains a valid sharp guardrail: **boundedness** of `L_Delta u` does not imply the tail law; the present mechanism needs convergence of its boundary trace together with enough residual regularity for the singular remainder to vanish.

The unresolved step is now narrower. Existing theory does not yet prove an expansion (PL319-17) for the actual completed-Weil branch with a residual in `W^{2,1}(dQ)`, nor even the minimal combination `m in L^1(dQ)` plus `H_{Q_0}m(Q)->0`. Establishing that residual class is still a real matched-asymptotic theorem, not a corollary of the source trace alone.

## 5. Consequence for the moving Green diagonal

Assume the actual right-endpoint mismatch has already been matched at leading `Q^{-1/2}` order and, after a harmless compact/tail split, its residual `m` obeys the hypotheses above. The actual eigen-equation supplies the finite source trace, so (PL319-6) forces

\[
Qm(Q)\to0.
\]

`PL-314` then applies automatically and gives, for every fixed outer `r>0`,

\[
\mathcal A_s[m](r)
\longrightarrow
 e^{-r}\int_0^\infty m(Q)\,dQ.
\tag{PL319-21}
\]

Thus the diagonal anti-concentration condition is **not an independent gate** once one has all three pieces:

\[
\boxed{
\text{leading }Q^{-1/2}\text{ coefficient matched}
\ +\ 
\text{integrable/Dini residual}
\ +\
\text{convergent source trace}.
}
\tag{PL319-22}
\]

For the actual completed-Weil branch, the third piece is supplied structurally by the zero-order eigen-equation. The remaining analytic frontier is therefore the first two pieces, especially a residual theorem strong enough to make the singular translation remainder (PL319-3) vanish. Once that is proved, the rank-one endpoint moment of `PL-313` is stable without a separate pointwise moving-tail assumption.

A compactly supported bulk component causes no difficulty: for a profile supported away from `x=1`, its logarithmic Laplacian at `x_Q` converges directly to the finite scalar `-\int u(y)/(1-y)\,dy`. It may therefore be split off before applying the tail identity, changing only the endpoint source constant and the already-known PL-313 moment.

## 6. Adversarial and novelty audit

**No RH or arithmetic sign mechanism is obtained.** The identity is universal one-dimensional logarithmic-Laplacian geometry. Rational-prime specificity enters only through the actual completed-Weil state and its finite translated source. Even a complete matching theorem would still leave the separate arithmetic first-crossing/sign gate identified elsewhere in the line.

**This does not contradict `PL-315`.** That finding constructs residuals in every `W^{k,1}(dQ)` with sparse `Qm(Q)=Theta(1)` saturation. For such a residual, (PL319-5) says exactly what must fail: its logarithmic source cannot have a single endpoint limit. The new input is source-trace convergence, not another generic Sobolev norm.

**This does not contradict `PL-318`.** The bounded-source construction there has `L_Delta u in L^infty` but does not assert convergence at the endpoint. The present result separates these hypotheses sharply: bounded forcing permits sparse saturation; a convergent trace, combined with a vanishing singular remainder, forbids it.

**`W^{2,1}` is only sufficient.** The theorem must not be read as saying that the actual residual needs two integrable derivatives. Formula (PL319-2) isolates the true remainder `H_{Q_0}`. Any weaker theorem proving `H_{Q_0}m(Q)->0` is enough.

**Leading-coefficient matching is still open.** The `Q^{-1/2}` cancellation in (PL319-16) shows consistency and identifies why that scale is special; it does not prove that an actual localized-Weil eigenstate has a boundary quotient limit `Q^{1/2}u(x_Q)->C`.

**No analytic-continuation shortcut is involved.** The argument uses Chen--Weth's established real-variable Dirichlet realization of the logarithmic Laplacian and Suzuki's already established localized operator decomposition. No Euler product is continued and no critical-strip identity is inferred from a convergence-region formula.

**Prior art remains the ingredients, not the line-specific Tauberian conclusion.** Source 96 supplies the singular-integral formula for `L_Delta`; source 97 supplies the sharp `Q^{-1/2}` boundary scale. A targeted audit of zero-order-kernel boundary regularity, logarithmic-Laplacian Dirichlet theory, and logarithmic-coordinate boundary asymptotics found the established regularity framework but no theorem packaging the exact endpoint identity (PL319-2) with the source-trace equivalence (PL319-6) or the moving-Green application. Search absence is not treated as broad novelty evidence. The durable delta is the exact derivation and its use to remove the independent `Qm(Q)->0` gate once source trace plus residual control are available.

## Consequence for the research line

`PL-314`--`PL-318` progressively showed that the moving Green atom defeats generic regularity and even bounded zero-order forcing. The missing mechanism can now be stated more precisely: **the actual eigen-equation supplies a convergent endpoint source trace, and the logarithmic Laplacian converts that trace into the desired moving-tail law as soon as the post-`Q^{-1/2}` residual has enough integrability/local-Dini control.**

The next theorem should therefore not attempt another ambient Sobolev upgrade. It should establish a genuine leading boundary coefficient for the completed-Weil state and a residual estimate sufficient for `m in L^1(dQ)` and `H_{Q_0}m(Q)->0` (with `W^{2,1}` only one convenient benchmark). If that succeeds, `PL-314` supplies the corner transfer automatically; the remaining non-universal question is then the rational-prime-specific scalar compatibility/sign mechanism rather than diagonal anti-concentration.

## Sources

- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*, *Communications in Partial Differential Equations* **44**(11) (2019), 1100–1139. Supplies the one-dimensional singular-integral realization used in (PL319-8).
- Source 97 in `research/prime_lattice/SOURCES.md`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, *DCDS* **45**(1) (2025), 1–36. Supplies the sharp `ell(delta)^{1/2}` boundary scale used as the leading-profile control.
- `PL-291`: exact localized-Weil decomposition into `T=(1/2)L_Delta+gamma`, finite prime-power translations, scalar terms, and the continuous completion kernel.
- `PL-313`--`PL-318`: rank-one corner transfer, moving-diagonal obstruction, critical/supercritical Sobolev threshold, and bounded-source negative controls.
