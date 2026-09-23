# VIS-414 — sign-definite Wang windows force balanced Bargmann cycle signs

## Claim

Let `F_1,...,F_K` be a finite labelled family of the real Wang shell functions from `VIS-413`, and let `w(T)>=0` be a nonzero integrable window with

`W = integral w(T) dT > 0`.

Define the finite-window Gram matrix

`G_(ij) = W^(-1) integral w(T) F_i(T) F_j(T) dT`.

Assume that every participating shell is sign-definite on `supp(w)`: for each `i` there is `s_i in {+1,-1}` such that

`s_i F_i(T) >= 0`

throughout the window support. With `D=diag(s_1,...,s_K)`, one then has

`(D G D)_(ij) = W^(-1) integral w(T) |F_i(T)| |F_j(T)| dT >= 0`.

Hence the signed graph of the nonzero Gram entries is switchable to an all-positive signing. Equivalently, every nonzero Bargmann cycle product

`Delta_C = G_(i_1 i_2) G_(i_2 i_3) ... G_(i_m i_1)`

is positive real, so its residual `Z_2` phase from `VIS-413` is `0`, never `pi`.

For a connected interval window this gives a concrete converse obstruction: if a nonzero cycle has negative sign, then at least one shell appearing in that cycle cannot be sign-definite on the interval. Since every fixed Wang shell is a continuous finite cosine polynomial, that shell must have a zero in the window.

In particular, fix a height `T_0` at which a finite selected family satisfies `F_i(T_0) != 0` for every `i`. Continuity gives a `delta>0` such that every nonnegative window supported inside `(T_0-delta,T_0+delta)` lies in the balanced regime above. Thus sufficiently local Wang Bargmann holonomy is trivial away from shell zeros.

The surviving `pi`-valued cycle phase is therefore not an infinitesimal local phase carrier. It can occur only on a window large enough, or positioned appropriately, to encounter nontrivial sign structure in the participating real shells.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-SIGNED-GRAPH-BALANCE SPECIALIZATION + NEGATIVE REPRESENTATION BOUNDARY + NO-NOVELTY-CLAIM`.

This does not show that negative cycle signs are source-free. The zero locations and relative sign patterns of the Wang shells may still depend on the arithmetic source. The result identifies the minimum mesoscopic structure that any nontrivial finite-window `Z_2` holonomy must use.

## 1. Switching by shell signs makes the Gram matrix entrywise nonnegative

The assumption says that each real shell has one fixed sign on the window support. Choose `s_i` so that

`H_i(T)=s_i F_i(T)>=0`.

Then

`(D G D)_(ij)`
` = s_i s_j G_(ij)`
` = W^(-1) integral w(T) H_i(T) H_j(T) dT`.

Because `w`, `H_i`, and `H_j` are nonnegative, every entry is nonnegative. Diagonal switching is exactly the residual real shell gauge from `VIS-413`: changing `F_i` to `-F_i` multiplies every incident Gram edge by `s_i` while leaving closed-cycle signs unchanged.

This is stronger than merely observing that `G` is a positive-semidefinite Gram matrix. Positive semidefiniteness alone does not forbid negative off-diagonal entries or negative products around cycles. The sign-definite realization supplies the extra entrywise-positive gauge.

## 2. Every closed cycle is positive

Consider a cycle using only nonzero Gram edges. Since `DGD` has nonnegative entries, all corresponding switched edges are strictly positive. Therefore their cyclic product is positive.

The same conclusion follows algebraically from the edge signs. Whenever `G_(ij) != 0`,

`sign G_(ij) = s_i s_j`.

Hence around

`C=(i_1,...,i_m,i_1)`,

`sign Delta_C`
` = product_(r=1)^m s_(i_r) s_(i_(r+1))`
` = product_(r=1)^m s_(i_r)^2`
` = +1`.

This is exactly the classical structural-balance condition for a signed graph: a signing is balanced when every cycle has positive sign, equivalently when a vertex switching makes all edges positive.

The cycle product itself remains gauge invariant exactly as in `VIS-411`; the new point is that the real finite-window Wang representation lands in the trivial balanced sector whenever all shells keep a fixed sign across the window.

## 3. Negative cycle phase requires a shell zero on a connected window

Suppose `supp(w)` lies in a connected interval `I` and a nonzero cycle product is negative. If every shell on that cycle were sign-definite on `I`, the preceding argument would force the cycle positive. Therefore at least one participating shell is not sign-definite on `I`.

Each fixed Wang shell from `VIS-413` is a finite real cosine polynomial and hence continuous. Failure of sign-definiteness on a connected interval means that the shell takes both positive and negative values there, so by the intermediate value theorem it has a zero in `I`.

Thus a negative Bargmann sign is a certificate that the selected window spans at least one shell sign transition. The converse is false: a shell zero or sign change does not by itself force a negative cycle. Multiple edges may change coherently and the cycle parity can remain positive.

For disconnected window support, retain only the weaker exact statement: a negative cycle implies that at least one participating shell is not sign-definite on the full support. Continuity may place the required zero between support components rather than inside them.

## 4. Sufficiently narrow windows away from zeros have trivial holonomy

Fix a finite shell set and a point `T_0` with

`F_i(T_0) != 0`

for every selected `i`. By continuity, for each shell there is a neighborhood on which its sign agrees with `sign F_i(T_0)`. Intersecting finitely many such neighborhoods gives one `delta>0` on which all shell signs are simultaneously fixed.

Every nonnegative window supported in that common neighborhood therefore has a balanced Gram signing and only zero cycle phase.

This finite-family qualification matters. If the shell family grows with scale, the nearest zero among all retained shells may approach `T_0`, so no scale-uniform `delta` follows from this argument. A growing-family statement would require a separate quantitative zero-spacing or sign-stability estimate.

If the normalized windows form an approximate identity around `T_0`, the stronger matrix limit is also immediate:

`G_(ij) -> F_i(T_0) F_j(T_0)`.

The limiting Gram matrix is rank one. After switching by the pointwise signs of the shells it becomes the positive outer product `|F(T_0)| |F(T_0)|^T`. This limit is useful as intuition, but the cycle-sign theorem above does not require any limiting argument.

## 5. Representation consequence

The representation ladder from `VIS-411`--`VIS-413` now sharpens one step further.

For general complex shell rays, gauge-invariant phase lives on `U(1)` Bargmann cycles (`VIS-411`). For the real Wang finite-window shells, that phase is quantized to `Z_2={0,pi}` (`VIS-413`). Under simultaneous sign-definiteness on the window, the `Z_2` quotient collapses again: every nonzero cycle belongs to the balanced `+1` sector.

Therefore an arbitrarily fine local visualization of these real shell cycles cannot reveal a nontrivial holonomy away from zeros. The full Gram matrix still retains amplitudes and local shell geometry, but its cycle-sign quotient has become information-free there.

Any meaningful negative-cycle statistic must consequently operate at a mesoscopic scale where the window resolves relative shell sign changes. Its admissibility then depends on whether that sign-transition geometry distinguishes the arithmetic Wang source from matched controls preserving the coarse shell frequencies, energies, or zero-crossing densities.

## 6. Prior art and novelty boundary

The signed-graph theorem used here is classical. Frank Harary, **On the notion of balance of a signed graph**, *Michigan Mathematical Journal* 2:2 (1953--1954), 143--146, DOI `10.1307/mmj/1028989917`, introduced structural balance for signed graphs and characterized balanced signings by vertex switching/bipartition; equivalently, every cycle has positive sign.

No novelty is claimed for structural balance, switching equivalence, Gram positive semidefiniteness, the intermediate value theorem, or the fact that products of vertex signs cancel on cycles. The Mathia-specific contribution is only the specialization of that classical balance mechanism to the real finite-window Wang Gram representation of `VIS-413`, which identifies a sharp local boundary for when its residual Bargmann `Z_2` phase can be nontrivial.

The Bargmann/frame-gauge background remains the prior art already recorded in `VIS-411`, and `VIS-412` supplies the complementary infinite-window obstruction: in intrinsic Bohr geometry the distinct Wang dyadic shells are orthogonal, so no cross-shell cycle exists at all.

## 7. Boundaries and falsification

The nonnegative-window hypothesis is essential to the proof. A signed or complex analysis kernel can produce an indefinite weighted pairing even when every shell keeps a fixed pointwise sign, so the entrywise-positive switching conclusion need not survive.

The real-shell hypothesis is equally essential. Complex shell representatives can carry genuine continuous Bargmann phases and are not reduced to this signed-graph problem.

Zero Gram edges are omitted from the signed frame graph. A cycle phase is defined only when every factor is nonzero. Sign-definite shells may themselves vanish at isolated points without changing sign; this does not hurt the integral argument, although an edge can disappear if the overlap integral is zero.

A negative cycle is only a **necessary sign-transition witness**, not sufficient evidence of arithmetic specificity. To falsify the core theorem, it would be enough to construct real shell functions that are simultaneously sign-definite on the support of a nonnegative window yet have a nonzero negative Gram cycle product. Such an example would contradict the displayed switching identity directly.

## Dependencies

- `VIS-411`: independent shell-phase gauge and Bargmann cycle invariants.
- `VIS-412`: intrinsic Wang Bohr-shell orthogonality and the finite-window escape route.
- `VIS-413`: Wang real shells and the reduction of finite-window Bargmann phase from `U(1)` to `Z_2`.

## Research consequence

The next useful question is no longer whether an infinitesimal Wang window can carry a nontrivial cycle phase: it cannot away from shell zeros. The live object is the **scale and organization of simultaneous shell sign transitions**.

A later invocation may ask when a growing family of Wang shells first loses simultaneous sign-definiteness, whether negative-cycle incidence has a stable scaling law, and whether matched arithmetic-independent controls reproduce that law. Those questions require a new representation/control campaign and are intentionally left beyond this finding.