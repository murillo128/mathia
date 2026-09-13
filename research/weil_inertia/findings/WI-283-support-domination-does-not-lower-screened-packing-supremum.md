# WI-283 — support domination does not lower the completely screened packing supremum

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed** first-crossing relaxation developed in `WI-267`, `WI-281`, and `WI-282`. This finding asks whether the source-specific support-cover constraint proved in `WI-267` supplies the missing strict decrement once it is added to complete active prime-power screening and full essential span.
- **Result:** it does not. For every aperture `a>(log 2)/2`, the exact relaxed supremum remains `K_pack` even after imposing simultaneously: nonnegativity, normalization, complete prime-power autocorrelation screening, full essential span, and the pointwise prime-translation support domination forced by every actual Suzuki null mode.
- **What it does not claim:** this does not construct a Suzuki null mode, does not show that `A_a f=0` can attain or approximate `K_pack`, does not address sign-changing first modes, and does not weaken `WI-267`. It shows only that the **support-topological content** of `WI-267`, when detached from the amplitudes in the null equation, is relaxation-sharp.
- **Novelty boundary:** the graph-theoretic principle “maximal independent implies dominating” is classical, and finite forbidden-distance sets are classical distance-avoidance objects. The new line-local deduction is their use to saturate the `WI-282` screened near-extremizers without paying a positive amount of `B_+`, proving that the exact `WI-267` support-cover constraint still leaves the `K_pack` ceiling sharp. No historical priority claim is made.

## Claim

Retain the notation of `WI-281` and `WI-282`. Put

\[
L:=\log 2,
\qquad
I_L:=(-L/2,L/2),
\tag{1}
\]

and

\[
K(t)=|t|w(|t|)\mathbf 1_{|t|<h_0},
\qquad
B_+(f):=\frac12\iint f(x)f(y)K(x-y)\,dx\,dy.
\tag{2}
\]

Let `T_L` be the integral operator on `L^2(I_L)` with kernel `K(x-y)` and

\[
K_{\rm pack}:=\frac12\lambda_{\max}(T_L).
\tag{3}
\]

Fix

\[
a>L/2
\tag{4}
\]

and define the finite active von-Mangoldt lag set exactly as in `WI-267`,

\[
\mathcal P_a
:=\{\log n:\Lambda(n)>0,\ \log n\le2a\}.
\tag{5}
\]

For `f\in L^2(-a,a)`, extend `f` by zero to `\mathbb R`, write

\[
C_f(d):=\int_{\mathbb R}f(x+d)f(x)\,dx,
\tag{6}
\]

and let `S_f` denote the closed essential support of that zero extension.

Consider normalized nonnegative profiles satisfying all three constraints

\[
C_f(d)=0\qquad(d\in\mathcal P_a),
\tag{7}
\]

\[
\operatorname*{ess\,inf}\{x:f(x)>0\}=-a,
\qquad
\operatorname*{ess\,sup}\{x:f(x)>0\}=a,
\tag{8}
\]

and the exact `WI-267` support domination

\[
(-a,a)
\subset
S_f\cup
\bigcup_{d\in\mathcal P_a}
\bigl((S_f-d)\cup(S_f+d)\bigr).
\tag{9}
\]

Then

\[
\boxed{
\sup B_+(f)=K_{\rm pack}.
}
\tag{10}
\]

Thus there is no constant `c(a)>0` such that

\[
B_+(f)\le K_{\rm pack}-c(a)
\tag{11}
\]

follows from (7)--(9) together with `f\ge0` and `\|f\|_2=1`.

The upper bound in (10) is already `WI-281`: the active lag `L=\log2` alone gives the exact selector-mod-`L` packing ceiling `K_pack`. The content here is the lower approximation under the additional support domination (9).

## 1. A finite forbidden-distance saturation lemma

The mechanism is independent of zeta and is useful to isolate exactly what (9) contributes.

Let `I=(-a,a)` and let `D\subset(0,2a]` be finite with

\[
d_0:=\min D>0.
\tag{12}
\]

Call an open set `E\subset I` **`D`-avoiding** if

\[
(E+d)\cap E=\varnothing
\qquad(d\in D).
\tag{13}
\]

Suppose `E_0\subset I` is open and `D`-avoiding. Then there exists an open `D`-avoiding set `E\supset E_0` such that, for

\[
S:=\overline E,
\tag{14}
\]

one has

\[
\boxed{
I\subset
S\cup\bigcup_{d\in D}\bigl((S-d)\cup(S+d)\bigr).
}
\tag{15}
\]

### Proof

Partially order the open `D`-avoiding supersets of `E_0` by inclusion. The union of a chain is open. It is also `D`-avoiding: if two points of the union differed by some `d\in D`, they lie in two members of the chain, and the larger of those two members would already contain a forbidden pair. Zorn's lemma therefore gives a maximal open `D`-avoiding set `E\supset E_0`.

Assume (15) fails at some

\[
x\in I\setminus S.
\tag{16}
\]

Then

\[
x+d\notin S,
\qquad
x-d\notin S
\qquad(d\in D).
\tag{17}
\]

Because `S` is closed and `D` is finite, a sufficiently small open interval `J\ni x` satisfies

\[
J\cap S=\varnothing,
\qquad
(J+d)\cap S=(J-d)\cap S=\varnothing
\quad(d\in D),
\tag{18}
\]

and also

\[
\operatorname{diam}J<d_0.
\tag{19}
\]

Condition (19) forbids a `D`-distance inside `J`, while (18) forbids one between `J` and `E`. Hence `E\cup J` is a strictly larger open `D`-avoiding set, contradicting maximality. This proves (15).

This is the continuous finite-distance analogue of the classical graph fact that a maximal independent set is dominating. The proof is included because the open-set version, rather than the abstract graph slogan, is what is needed for essential supports.

## 2. The `WI-282` near-extremizer can be seeded inside an open avoiding set

It remains to start the saturation lemma from profiles arbitrarily close to `K_pack` while preserving full span. The construction is a slightly hardened form of `WI-282`, chosen so that the ambient avoiding set is genuinely open rather than merely distance-avoiding up to null endpoints.

Let `\phi\ge0` be a normalized top eigenfunction of `T_L`, extended by zero outside `I_L`, so

\[
B_+(\phi)=K_{\rm pack}.
\tag{20}
\]

Fix `\eta>0` and truncate the core to

\[
J_\eta=(-L/2+\eta,L/2-\eta).
\tag{21}
\]

The width of `J_\eta` is strictly below `L=\min\mathcal P_a`, so no two core points are separated by an active prime-power lag.

The only lag equal to `2a`, if it occurs at all, is automatically screened by support in the open interval `(-a,a)`. Put

\[
d_*:=\max\bigl(\mathcal P_a\cap(0,2a)\bigr).
\tag{22}
\]

This set is nonempty because `L<2a`. Choose `\delta>0` so small that

\[
\delta<L,
\qquad
2a-2\delta>d_*,
\qquad
 a-\delta>L/2-\eta.
\tag{23}
\]

Define the endpoint satellites

\[
S_+=(a-\delta,a),
\qquad
S_-=(-a,-a+\delta).
\tag{24}
\]

and the finite forbidden core set

\[
H_{\eta,\delta}
:=J_\eta\cap
\bigcup_{d\in\mathcal P_a}
\bigl((S_++d)\cup(S_+-d)\cup(S_-+d)\cup(S_--d)\bigr).
\tag{25}
\]

Now remove the **closure** of these holes and set

\[
E_0
:=
\bigl(J_\eta\setminus\overline{H_{\eta,\delta}}\bigr)
\cup S_+\cup S_-.
\tag{26}
\]

Then `E_0` is open and is exactly `\mathcal P_a`-avoiding. Indeed:

1. two core points are at distance `<L`;
2. two points in one satellite are at distance `<\delta<L`;
3. two points in opposite satellites have distance in `(2a-2\delta,2a)`, hence exceed every active lag `<2a`, while the endpoint lag `2a` is never attained;
4. every core--satellite pair at a lag in `\mathcal P_a` has been removed by (25).

Because the closure of a finite union of intervals has the same measure as that union,

\[
|\overline{H_{\eta,\delta}}|
\le4|\mathcal P_a|\delta.
\tag{27}
\]

Define

\[
h_\delta
:=(2\delta)^{-1/2}
\bigl(\mathbf 1_{S_+}+\mathbf 1_{S_-}\bigr)
\tag{28}
\]

and, for `\varepsilon>0`,

\[
u_{\eta,\delta,\varepsilon}
:=
\phi\,\mathbf1_{J_\eta\setminus\overline{H_{\eta,\delta}}}
+\varepsilon h_\delta,
\qquad
f_0:=
\frac{u_{\eta,\delta,\varepsilon}}
{\|u_{\eta,\delta,\varepsilon}\|_2}.
\tag{29}
\]

Then `f_0\ge0`, `\|f_0\|_2=1`, its positive set is contained in `E_0`, it screens every active prime-power lag exactly, and the satellite intervals force full essential span `2a`.

First send `\eta\downarrow0`, then `\delta\downarrow0`, then `\varepsilon\downarrow0`. Equation (27), absolute continuity of the integral of `|\phi|^2`, and `\|\varepsilon h_\delta\|_2=\varepsilon` give a diagonal choice for which

\[
f_0\longrightarrow\phi
\quad\text{in }L^2(\mathbb R).
\tag{30}
\]

As in `WI-282`, the convolution kernel defining `B_+` is in `L^1`, so `B_+` is continuous on bounded `L^2` sets. Therefore, for every `\rho>0`, the parameters can be chosen so that

\[
B_+(f_0)>K_{\rm pack}-\rho.
\tag{31}
\]

## 3. Saturation adds the `WI-267` support cover at arbitrarily small analytic cost

Apply the lemma of §1 with

\[
D=\mathcal P_a
\tag{32}
\]

and the open seed `E_0` from (26). Let `E\supset E_0` be a maximal open `\mathcal P_a`-avoiding set and put `S=\overline E`. Then

\[
(-a,a)
\subset
S\cup
\bigcup_{d\in\mathcal P_a}
\bigl((S-d)\cup(S+d)\bigr),
\tag{33}
\]

which is exactly the `WI-267` support-cover geometry.

To make this geometric saturation into the actual essential support of a screened profile, define

\[
h_E(x):=\operatorname{dist}(x,E^c).
\tag{34}
\]

Since `E\subset(-a,a)`, the function `h_E` is bounded, belongs to `L^2`, is positive exactly on `E`, and has closed essential support

\[
\operatorname{supp}_{\rm ess}(h_E)=\overline E=S.
\tag{35}
\]

For `t>0`, set

\[
g_t:=f_0+t h_E,
\qquad
f_t:=\frac{g_t}{\|g_t\|_2}.
\tag{36}
\]

Every `f_t` is nonnegative and normalized. Because both summands are supported almost everywhere in the `\mathcal P_a`-avoiding set `E`,

\[
C_{f_t}(d)=0
\qquad(d\in\mathcal P_a).
\tag{37}
\]

Moreover `h_E>0` throughout `E`, so the closed essential support of `f_t` is exactly `S`; hence (33) becomes the required support domination (9). Since `E` contains the two endpoint satellites from `E_0`, `f_t` also has full essential span (8).

Finally,

\[
f_t\longrightarrow f_0
\quad\text{in }L^2
\qquad(t\downarrow0),
\tag{38}
\]

so

\[
B_+(f_t)\longrightarrow B_+(f_0).
\tag{39}
\]

Combining (31) and (39), for every `\rho>0` there exists an admissible `f_t` satisfying all of (7)--(9) with

\[
B_+(f_t)>K_{\rm pack}-\rho.
\tag{40}
\]

The `WI-281` upper bound gives the reverse inequality, proving (10).

## 4. Why this is a stronger barrier than `WI-282`

`WI-282` showed that complete prime-power screening plus qualitative full span does not lower `K_pack`. `WI-267`, however, had supplied an additional **source-specific necessary condition** for every actual Suzuki null mode: the closed essential support must dominate the whole aperture by active prime translations. It was therefore still possible that this pointwise support propagation, when added to the screened packing problem, would exclude the `WI-282` near-extremizers and force a strict gap.

Equation (10) closes that possibility. The distinction is subtle but important: exact screening forbids positive-measure overlap of `E` with `E\pm d`, whereas support domination can be satisfied by **boundary contact** after maximal saturation. The added mass used to populate the saturated open set can have arbitrarily small `L^2` norm, so the support topology can change drastically while `B_+` changes arbitrarily little.

Thus the support theorem of `WI-267` is genuine rigidity for solutions of the Suzuki equation, but its geometric shadow is too weak to improve the scalar packing budget. Any useful next constraint must control **how much amplitude** is transported to those prime-translated contacts, not merely assert that the closed support reaches them.

In particular, the following route is now closed as a standalone bootstrap:

\[
\text{complete screening}
+\text{full span}
+\text{prime-translation support domination}
\Longrightarrow
B_+\le K_{\rm pack}-c.
\tag{41}
\]

No positive `c` exists at this level of relaxation.

## 5. Surviving gates

The barrier leaves intact precisely the stronger information that the construction discards. A strict decrement can still come from, for example:

- the actual distributional null equation `A_a f=0`, not just its support consequence;
- a quantitative lower bound on mass in prime-translated regions, rather than closure contact;
- regularity, nodal, or boundary-flux information forcing non-negligible amplitude near the dominating contacts;
- source-weighted signed balance between the archimedean and von-Mangoldt terms;
- a positive first-crossing spectral-area margin or simultaneous-cut identity that couples amplitudes at several cuts.

The construction gives no evidence against any of these. It only says that replacing them by support topology loses too much information.

## Prior-art and novelty audit

The zeta-specific ingredients are inherited from earlier audited findings. `WI-267` derives (9) from Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (revised 17 Aug 2026), using the distributional localized null equation. `WI-281` proves the `K_pack` upper bound from powers-of-two screening, and `WI-282` proves that all active prime-power lags plus full span still leave that upper bound sharp.

The geometric principle in §1 is classical in graph theory: an independent set maximal under inclusion is dominating. The present proof uses its elementary open-set finite-distance analogue so no graph-theoretic theorem is imported as a black box. The distance-avoidance viewpoint itself is classical; `WI-282` already audited Fernando Mário de Oliveira Filho and Frank Vallentin, **Fourier analysis, linear programming, and densities of distance avoiding sets in R^n**, *JEMS* 12 (2010), 1417--1428, DOI `10.4171/JEMS/236`, and Evan DeCorte, Fernando Mário de Oliveira Filho and Frank Vallentin, **Complete positivity and distance-avoiding sets**, *Mathematical Programming* 191 (2022), 487--558, DOI `10.1007/s10107-020-01562-6`.

A focused line-local audit of `WI-267`, `WI-281`, `WI-282`, the current clue frontier, and recent `weil_inertia` history found no existing deduction that the **support-domination constraint itself** can be imposed while keeping the exact `K_pack` supremum. A targeted web search across Suzuki/Weil support domination, prime-power autocorrelation screening, and packing terminology likewise located no such statement. Search absence is audit context only and is not evidence of priority.

The substantive Mathia result is therefore not the classical maximal-independent-set lemma but the exact variational consequence (10): the source-specific support condition extracted in `WI-267` is still insufficient, even jointly with complete screening and full span, to produce a positive first-crossing packing gap.

## Falsification and audit test

The proof uses no floating-point or computer-assisted certificate. A falsification must break at least one of these load-bearing points:

1. the `WI-281` selector-mod-`log 2` argument does not actually give `B_+(f)\le K_pack` for every nonnegative profile screened at `log 2`;
2. the hardened seed set (26) is not open or fails to avoid some active lag, including a possible endpoint lag `2a`;
3. the deleted-hole estimate (27) is insufficient to recover the `WI-282` `L^2` approximation to `\phi`;
4. a chain union of open `D`-avoiding supersets can create a forbidden-distance pair, invalidating the Zorn saturation;
5. failure of the cover (15) does not permit insertion of a small open interval because one of the finitely many translated closures can approach the candidate point;
6. `h_E=dist(\cdot,E^c)` fails to have essential support `\overline E` or fails to lie in `L^2(-a,a)`;
7. exact `D`-avoidance of `E` does not imply the autocorrelation identities (37) for nonnegative functions supported there;
8. `B_+` is not continuous under the `L^2` perturbation (38).

Items 2 and 5 are the most useful review targets. Item 2 is why (26) removes the **closed** forbidden core holes rather than only the open holes used in the qualitative `WI-282` presentation.

## Research decision

Treat **support domination alone** as exhausted as a route below `K_pack`. The next one-signed first-crossing step should not spend effort strengthening the topology of the support unless that strengthening comes with a quantitative amplitude or operator estimate. The live gate is to turn the actual null equation, source balance, regularity, or simultaneous cuts into a positive amount of unavoidable screened-overlap defect.