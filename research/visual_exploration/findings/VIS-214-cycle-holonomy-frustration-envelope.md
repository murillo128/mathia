# VIS-214 — cycle holonomy exactly controls coefficient-envelope attainability in the prime-phase torus

## Claim

Keep the Hermitian prime-phase torus objective from `VIS-213`, but state the result for any finite Hermitian zero-diagonal matrix `A` on a vertex set `V`. Let the support graph contain the unordered edges `{u,v}` for which `A_(u,v) != 0`. Choose one orientation of each support edge and write

`A_(u,v)=w_(u,v) exp(i theta_(u,v))`, with `w_(u,v)>0`,

and `theta_(v,u)=-theta_(u,v)` modulo `2 pi`. For `z_u=exp(i phi_u)`,

`G(z)=z^* A z = 2 sum_(u->v) w_(u,v) cos(theta_(u,v)+phi_v-phi_u)`.

Define the absolute coefficient envelope

`B(A)=2 sum_(u->v) w_(u,v)`.

Then the apparent phase-frustration language in `VIS-213` has an exact gauge-invariant form.

1. `max_z G(z)=B(A)` if and only if the unit gains `g_(u,v)=exp(i theta_(u,v))` are balanced: equivalently, the product of the gains around every oriented cycle is `1`, or the edge phases are a vertex coboundary.
2. `min_z G(z)=-B(A)` if and only if the shifted gains `-g_(u,v)` are balanced: equivalently, for every oriented cycle `C`,

   `sum_(e in C) theta_e = |C| pi  (mod 2 pi)`.
3. Consequently,

   `max_z |G(z)|=B(A)`

   if and only if the gain graph is either balanced or switching-equivalent to the all-negative gain graph. Otherwise the coefficient envelope is strictly unattainable.

There is also an elementary quantitative certificate. For an oriented support cycle `C` of length `k`, let

`Theta_C = sum_(e in C) theta_e  (mod 2 pi)`,

`h_+(C)=dist(Theta_C, 2 pi Z)`,

`h_-(C)=dist(Theta_C-k pi, 2 pi Z)`,

and `m(C)=min_(e in C) w_e`. Then every torus point satisfies

`B(A)-G(z) >= 2 m(C) [1-cos(h_+(C)/k)]`,

`B(A)+G(z) >= 2 m(C) [1-cos(h_-(C)/k)]`.

Thus a cycle with nonzero `h_+` certifies a positive-envelope deficit, while a cycle with nonzero `h_-` certifies a negative-envelope deficit. If both signs are obstructed — possibly by different cycles — one gets a strict explicit upper bound below `B(A)` for `max |G|`.

For an even cycle, `h_+=h_-`, so any nontrivial holonomy obstructs both signs. For an odd cycle, the two exceptional holonomies are `0` and `pi`; an odd cycle whose holonomy is neither value obstructs both coefficient-envelope signs by itself.

Applied to `A_(y,H)` from `VIS-213`, cycle holonomy is therefore an exact first obstruction to coherent amplification. Raw edge phases are gauge-dependent; cycle gains are the invariant object.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GAIN-GRAPH BALANCE SPECIALIZATION + QUANTITATIVE CYCLE OBSTRUCTION + NO-NOVELTY-CLAIM`.

## 1. Switching is exactly the torus phase action

For an oriented support edge `u->v`, define

`delta_(u,v)=theta_(u,v)+phi_v-phi_u` modulo `2 pi`.

Changing the torus point `z` therefore switches the edge gain by the vertex phases. The objective is

`G(z)=2 sum_e w_e cos(delta_e)`.

Because every `w_e` is positive,

`G(z) <= B(A)`

with equality if and only if every `delta_e=0` modulo `2 pi`. This means

`g_(u,v) exp(i(phi_v-phi_u))=1`

on every support edge, i.e. the gain function can be switched to the trivial all-positive gain function.

Around any oriented cycle the vertex phases telescope, so switching leaves

`prod_(e in C) g_e = exp(i Theta_C)`

unchanged. A gain assignment can be switched to all-positive exactly when every cycle product is `1`: choose a root in each connected component, define vertex phases along a spanning tree, and cycle consistency makes the definition path-independent. This proves the first equivalence without any optimization approximation.

## 2. The negative envelope is the same balance test after a pi shift

Similarly,

`G(z) >= -B(A)`

with equality if and only if every `delta_e=pi` modulo `2 pi`. Equivalently the shifted gain `-g_e` can be switched to `+1` on every edge.

On a cycle of length `k`,

`prod_(e in C) (-g_e)=(-1)^k exp(i Theta_C)`.

Hence the all-negative edge preference is globally compatible exactly when

`Theta_C = k pi  (mod 2 pi)`

for every cycle. This is the gain-graph analogue of antibalance in signed graphs. Combining the positive and negative cases gives the exact criterion for attaining the absolute coefficient envelope.

A useful corollary for dense support graphs is that triangle holonomies already expose the local obstruction: a triangle with holonomy neither `0` nor `pi` rules out both signs of the envelope. One must still respect the actual support graph of `A_(y,H)`; a coefficient zero removes that edge and any cycle using it.

## 3. One frustrated cycle gives a quantitative deficit

Fix an oriented cycle `C` of length `k`. Take principal representatives of the switched edge phases `delta_e` in `[-pi,pi]`. Their sum modulo `2 pi` is `Theta_C`, so

`h_+(C) <= sum_(e in C) |delta_e|`.

At least one edge therefore has

`|delta_e| >= h_+(C)/k`.

Since `1-cos x` is increasing on `[0,pi]`,

`B(A)-G(z)`
` = 2 sum_e w_e [1-cos(delta_e)]`
` >= 2 m(C) [1-cos(h_+(C)/k)]`.

For the negative envelope, take principal representatives of `delta_e-pi`. Their cycle sum modulo `2 pi` is `Theta_C-k pi`, and the same argument gives

`B(A)+G(z) >= 2 m(C) [1-cos(h_-(C)/k)]`.

Define

`D_+ = max_C 2 m(C) [1-cos(h_+(C)/|C|)]`,

`D_- = max_C 2 m(C) [1-cos(h_-(C)/|C|)]`,

with the maximum understood as `0` when the support graph has no cycles. Then

`max_z |G(z)| <= B(A)-min(D_+,D_-)`.

This bound is deliberately crude: it uses only one cycle at a time and only its smallest weight. Its value is that it converts a visual or numerical impression of phase frustration into an exact certificate. A useful asymptotic bound for the prime matrix will require proving that sufficiently frustrated cycles carry non-negligible coefficient mass as `y,H` grow.

## 4. Prior art and novelty boundary

Cycle balance and switching are classical gain-graph notions. Matteo Cavaleri and Alfredo Donno, **On cospectrality of gain graphs**, *Special Matrices* 10:1 (2022), DOI `10.1515/spma-2022-0169`, records the general switching formalism and the standard equivalence between balance and switching to the trivial gain function. Francesco Belardo, Maurizio Brunetti, and Nathan Reff, **Balancedness and the Least Laplacian Eigenvalue of Some Complex Unit Gain Graphs**, *Discussiones Mathematicae Graph Theory* 40:2 (2020), 417–433, DOI `10.7151/dmgt.2281`, is a direct complex-unit-gain reference for cycle balance and algebraic frustration.

No novelty is claimed for balance, switching, cycle holonomy, antibalance, or phase synchronization as general theories. The Mathia-specific contribution is to identify the exact invariant controlling the coefficient-envelope question left open by `VIS-213`, and to record the elementary weighted cycle deficit in the normalization of that prime-phase torus objective.

The quantitative inequality above is derived directly here; it is not attributed to either reference as a new theorem of theirs, nor is it claimed as a new general graph-theoretic result.

## 5. Boundary and research consequence

This finding does **not** estimate the actual torus optimum sharply. Failure of exact balance only proves a strict deficit, and the displayed deficit may be tiny if every obstructing cycle contains a very small coefficient. Conversely, exact or near balance says nothing about how quickly the one-parameter prime-log orbit reaches the corresponding torus region; the access-time problem from `VIS-213` remains separate.

The useful representation is now gauge-invariant. Instead of plotting raw preferred edge phases of `A_(y,H)`, a future visual experiment should organize weighted cycle holonomies — especially short cycles carrying substantial coefficient mass — and compare their positive/negative envelope deficits with the Haar RMS scale `sqrt(R_v(y,H))`. That is a new quantitative question, not established by this finding, so it is left for a later invocation rather than expanded here.
