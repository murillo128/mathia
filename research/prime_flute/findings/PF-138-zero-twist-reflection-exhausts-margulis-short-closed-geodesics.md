# PF-138 — zero-twist reflection exhausts the Margulis-short closed geodesics

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + POSITIVE/BOUNDARY`. PF-137 localized the unresolved Güneysu--Thalmaier wave weight to the true ambient thin set and left one geometric gap: a short simple closed geodesic outside the PF-004 canonical consecutive-block family might create an uncontrolled collar. The zero-twist reflection closes that gap at the level of the source prime metric. Every simple closed geodesic of length at most
\[
\mu_*:=2\operatorname{arsinh}1
\]
is either one of the distinguished tight-flute cuffs or the PF-004/PF-034 separator of a consecutive finite cusp block. Since the distinguished cuffs tend to infinity, every sufficiently far closed Margulis-thin core is canonical. Combining this classification with the exact PF-004 cross-ratio, the Baker--Harman--Pintz gap envelope, PF-109, and PF-128 gives a finite **sum of local model scattering costs over all closed thin collars**. This does not yet prove complete wave operators: the PF-128 collar maps still have to be reconciled with one globally smooth boundary-coherent comparison.

## Claim

Let `X` be the exact complete zero-twist prime flute and let `tau` be its intrinsic zero-twist reflection. Put
\[
\mu_*=2\operatorname{arsinh}1.
\tag{1}
\]

Then every essential simple closed geodesic `eta` on `X` satisfying
\[
\ell(\eta)\le \mu_*
\tag{2}
\]
belongs to one of the following two classes:

1. a distinguished tight-flute cuff `alpha_n`;
2. the simple primitive boundary of a finite **consecutive cusp block**, hence the PF-004/PF-034 canonical separator associated with a word `g_i g_j^{-1}`.

Moreover,
\[
\ell(\alpha_n)\longrightarrow\infty,
\tag{3}
\]
so only finitely many curves of type 1 can satisfy (2).

For a type-2 separator let `a<b<c<d` be its four ordered prime labels as in PF-034, with `[a,b]` and `[c,d]` the exterior side intervals of the block. Write
\[
X_0=V(b)-V(a),\qquad
Y_0=V(c)-V(b),\qquad
Z_0=V(d)-V(c),
\qquad
V(x)=\pi\cot\frac{\pi}{x}.
\tag{4}
\]
PF-004 gives
\[
\chi=\frac{Y_0(X_0+Y_0+Z_0)}{X_0Z_0},
\qquad
\ell=4\operatorname{arsinh}\sqrt{\chi}.
\tag{5}
\]

If `ell<=mu_*`, then
\[
\boxed{
\chi\le \chi_*:=\sinh^2\!\left(\frac{\mu_*}{4}\right)
=\frac{\sqrt2-1}{2},
}
\tag{6}
\]
and hence
\[
Y_0\le \chi_* X_0,
\qquad
Y_0\le \chi_* Z_0.
\tag{7}
\]

Using the unconditional prime-gap envelope `g(p)=O(p^theta)` with `theta=0.525`, the number `N(P)` of canonical separators satisfying (2) whose left exterior prime label is `P` obeys
\[
\boxed{N(P)=O(P^\theta).}
\tag{8}
\]

For the matched all-composite shift clone, PF-109 gives uniformly for every such separator
\[
t_\eta
:=
\log\frac{\ell_+(\eta)}{\ell(\eta)}
=
O(P^{-3}),
\tag{9}
\]
including the pinching regime. PF-128 gives a full-collar Güneysu--Thalmaier model cost `O(|t_eta|)`. Therefore the sum over **all** closed thin cores of the prime metric is finite:
\[
\boxed{
\sum_{\substack{\eta\ {\rm simple}\\ \ell(\eta)\le\mu_*}}
\operatorname{Cost}_{\rm collar}(\eta)
<\infty.
}
\tag{10}
\]

The finitely many short distinguished cuffs contribute only a finite head term; the infinite tail is bounded by
\[
\sum_{P\ {\rm prime}} O(P^\theta)O(P^{-3})
\le
C\sum_{m\ge3}m^{\theta-3}
<\infty.
\tag{11}
\]

Equation (10) is a **model-budget statement**: it does not assert that the local PF-128 collar maps already coincide with the PF-125/PF-136 global comparison on their interfaces.

## 1. The primary zero-twist model has the required reflection

Source S1 (Arredondo--Morales--Ramírez Maluendas, Section 2 / Figure 7) constructs the zero-twist tight flute by cutting along geodesic arcs
\[
\gamma_0,\gamma_1,\ldots
\]
joining consecutive cusp ends and along a geodesic ray `beta` running through the zero-twist chain. The source states explicitly that the surface admits a reflection `tau` whose connected fixed-point components are precisely the arcs `gamma_n` and `beta`. Cutting along the `gamma_n` produces the symmetric infinite ideal polygon used for the Fuchsian uniformization.

In particular `tau` fixes every isolated cusp end individually and preserves the unique accumulation end. This is the only external geometric input about the reflection used below.

## 2. Every `mu_*`-short geodesic is reflection invariant

Let `eta` satisfy (2). Its image `tau(eta)` is another simple closed geodesic with exactly the same length. Because `tau` fixes every end individually, `eta` and `tau(eta)` determine the same partition of the end space.

The collar theorem has the local consequence that two distinct simple closed geodesics of lengths at most `2 arsinh 1` are disjoint. Equivalently, if two simple geodesics intersect then
\[
\sinh\frac{\ell_1}{2}\,
\sinh\frac{\ell_2}{2}>1.
\tag{12}
\]
This statement is local and does not require finite topological type.

Assume `tau(eta)` were distinct from `eta`. By (2) and the collar theorem the two curves would be disjoint. On a genus-zero flute, two disjoint essential simple curves inducing the same end partition cobound an annulus containing no ends; hence they are isotopic. A free homotopy class on a complete hyperbolic surface has at most one closed geodesic representative. Therefore
\[
\tau(\eta)=\eta,
\tag{13}
\]
a contradiction to distinctness. Thus every `mu_*`-short simple closed geodesic is setwise fixed by the zero-twist reflection.

This step is what excludes highly wound or nonconsecutive short curve classes. Such classes may have the same end partition as a simpler curve, but reflection generally sends them to a different intersecting representative; the collar threshold prevents that from happening at short length.

## 3. Reflection invariance forces a consecutive-block or cuff class

Compactify the ends of the tight-flute chain and take the quotient by `tau`. Pant by pant, zero twist cuts each pair of pants into two mirror disks; the quotient pieces glue along a ray. The quotient end-compactification is therefore a disk whose ideal boundary carries the cusp ends in their natural linear order
\[
0,s_0,s_1,s_2,\ldots,\infty.
\tag{14}
\]

An essential invariant geodesic `eta` separates the planar flute into two components, each containing ends. Since `tau` fixes those ends individually, it preserves both complementary components. Because `tau` reverses the orientation of the surface, its restriction to `eta` is a reflection of the geodesic circle and has exactly two fixed points. Hence
\[
\eta/\tau
\]
is a properly embedded arc in the quotient disk.

A proper embedded arc in a disk cuts off a consecutive interval of the ordered boundary ends. Doubling that arc gives only two nonperipheral possibilities:

- the interval begins at the initial two-puncture head, in which case the doubled class is a distinguished cuff `alpha_n`;
- the interval is a finite consecutive block of later cusp ends, in which case the doubled class is the simple boundary of exactly that consecutive block.

PF-034 already proves that the latter boundary class is the primitive simple geodesic represented by the telescoping word `g_i g_j^{-1}`, and PF-004 gives its exact cross-ratio/length formula. Thus no third family of reflection-invariant short closed curves exists.

## 4. Distinguished cuffs disappear from the thin tail

PF-001 gives
\[
e^{-\ell_n/2}=\tanh\frac{h_n}{4},
\qquad
h_n=\log\frac{u_n}{u_{n-1}}.
\tag{15}
\]
The Baker--Harman--Pintz bound implies `p_{n+1}-p_n=o(p_n)`, while `u_p=cot(pi/p)~p/pi`. Hence
\[
h_n\longrightarrow0,
\]
and (15) yields
\[
\ell_n\longrightarrow\infty.
\tag{16}
\]

Therefore only finitely many distinguished cuffs lie below `mu_*`. Every sufficiently far closed component of the `mu_*`-thin part has a PF-004 canonical block separator as its core.

This is stronger than PF-137's previous localization statement: the “noncanonical short-geodesic collar” sector is empty in the tail of the exact zero-twist prime flute.

## 5. Shortness itself bounds how many canonical blocks can occur

For a canonical block, (5) can be written
\[
\chi
=
\frac{Y_0}{X_0}
+
\frac{Y_0}{Z_0}
+
\frac{Y_0^2}{X_0Z_0}.
\tag{17}
\]
All three terms are nonnegative, so (6) immediately gives (7).

Let `P=a` be the left exterior prime label. On `x>=3`, `V'(x)` is bounded above by an absolute constant and is greater than `1`. Since `[a,b]` is one consecutive-prime interval, BHP gives
\[
X_0=V(b)-V(a)=O(P^\theta),
\qquad \theta=0.525.
\tag{18}
\]
Equation (7) then gives
\[
Y_0=O(P^\theta).
\tag{19}
\]
Since `V'>1`,
\[
c-b\le V(c)-V(b)=Y_0,
\tag{20}
\]
so, after fixing the left exterior side, the right edge of any `mu_*`-short block can occur at only `O(P^theta)` integer labels, hence at only `O(P^theta)` prime labels. Its following exterior endpoint `d` is then fixed as the next prime. This proves (8).

The count is intentionally crude. No statistics of actual short blocks are needed. Any prime-gap bound with exponent below `2` would suffice for the final summation; the already-audited BHP exponent gives a comfortable margin.

## 6. The complete closed-thin model collar budget is summable

PF-109 proves for every PF-004 separator with four labels in a tail beginning at `P`
\[
\left|
\log\frac{\ell_+}{\ell}
\right|
\le CP^{-3},
\tag{21}
\]
uniformly over arbitrary block span and uniformly as `ell->0`.

PF-128 treats the entire standard collar of a matched core pair with `ell_+=e^t ell` and proves that the inverse-unit-ball-volume weighted metric-deviation cost is
\[
\operatorname{Cost}_{\rm collar}
\le C|t|,
\tag{22}
\]
with no blow-up as the core pinches.

Combining (8), (21), and (22),
\[
\sum_{\text{tail closed thin cores}}
\operatorname{Cost}_{\rm collar}
\le
C\sum_{P\ {\rm prime}}P^{\theta-3}<\infty,
\tag{23}
\]
and the finite head adds only a finite amount.

The Güneysu--Thalmaier criterion may use the unit-ball weight from one of the two metrics. PF-137 formulated the remaining gate using the **prime metric**, so (23) is exactly the thin-core family that had to be exhausted; no separate classification of clone-only thin components is required for this source-weighted localization.

## 7. What PF-138 closes and what it does not

PF-137 left two possible sources of failure:

1. genuinely noncanonical short closed geodesics whose collars were not covered by PF-109/PF-128;
2. incompatibility between the local thin/thick/cusp comparisons when one tries to produce a single smooth global marking.

PF-138 removes the first source at both the topological and summability levels:
\[
\boxed{
\text{all sufficiently far closed thin cores}
=
\text{PF-004 canonical block separators},
}
\tag{24}
\]
and their **entire local PF-128 weighted budget is summable**.

The second source remains. PF-128 constructs a boundary-to-boundary collar comparison optimized for the local core-length change, whereas PF-130--PF-136 construct a different boundary-coherent body/split correction and PF-129 fixes the cusp normalization. A wave-operator theorem still needs one smooth complete quasi-isometric common-manifold map for which these pieces have compatible traces and whose total Güneysu--Thalmaier weighted deviation is finite.

Accordingly PF-138 does **not** prove:

- existence or completeness of wave operators;
- equality of absolutely continuous spectra;
- equality of scattering matrices or resonances;
- a Schatten or trace-class relative resolvent;
- a determinant identity;
- any RH implication.

It converts the accepted wave clue from a thin-geometry **classification** problem into an **assembly/interface** problem.

## 8. Prior art and novelty audit

No novelty is claimed for:

- the zero-twist reflection and symmetric ideal-polygon model of Arredondo--Morales--Ramírez Maluendas (S1);
- the collar theorem and the `2 arsinh 1` short-curve threshold;
- uniqueness of geodesic representatives;
- planar-surface topology or the quotient-disk description of a reflection;
- the BHP prime-gap exponent (S6);
- the Güneysu--Thalmaier scattering criterion (S16).

Directed searches for combinations of `zero-twist flute`, `reflection`, `short geodesic`, `Margulis thin`, `consecutive cusp block`, and `tight flute` found the established flute-uniformization/parabolicity and coarse-hyperbolicity literature, but no theorem asserting that all sufficiently short closed geodesics of a zero-twist tight flute are the consecutive-block separators relevant here.

The durable Mathia content is the project-specific composition
\[
\boxed{
\text{zero-twist reflection}
\to
\text{short-curve invariance}
\to
\text{consecutive-block exhaustion}
\to
\text{PF-109 }O(P^{-3})
\to
\text{summable PF-128 thin-collar budget}.
}
\tag{25}
\]
This is a boundary result for the prime/shift wave-comparison program, not a new general collar or scattering theorem.

## 9. Audit / falsification core

A later adversary can check PF-138 through the following finite chain:

1. verify from S1 that the zero-twist tight flute has a reflection fixing the arcs `gamma_n` and `beta`, hence preserving every cusp and the infinite end;
2. use the collar theorem to show distinct simple geodesics of lengths at most `mu_*` are disjoint;
3. verify that two disjoint simple curves with the same end partition on a genus-zero flute are isotopic, then use uniqueness of geodesic representatives to obtain (13);
4. quotient an invariant essential geodesic by the reflection and check that the resulting proper arc in the quotient disk cuts off a consecutive interval of cusp ends;
5. identify the head intervals with distinguished cuffs and the other nonperipheral intervals with PF-034 consecutive-block separators;
6. use PF-001 plus the audited prime-gap envelope to verify `ell_n->infinity`;
7. insert `ell<=mu_*` into PF-004 to obtain the exact constant (6), then derive the counting bound (8);
8. combine PF-109's all-span `O(P^-3)` log-length defect with PF-128's `O(|t|)` full-collar weight and sum (23);
9. do not infer wave completeness until the local collar maps, PF-129 cusp maps, and PF-130--PF-136 body corrections are assembled into one smooth global comparison.

A counterexample to steps 2--5 would reopen the noncanonical thin-collar sector. A failure of step 8 would reopen the summability claim. A failure to perform the final global assembly would **not** refute PF-138; it is exactly the remaining gate stated here.
