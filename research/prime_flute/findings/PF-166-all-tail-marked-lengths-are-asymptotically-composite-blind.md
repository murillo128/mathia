# PF-166 — all tail marked lengths are asymptotically composite-blind

**Status:** `EXACT-DERIVED + LITERATURE-CLASSIFIED + DECISIVE-NEGATIVE/BOUNDARY` for mechanisms whose claimed arithmetic content lives only in the asymptotic marked translation-length function of the flute tail. PF-111 controls arbitrary closed words inside one pair of pants, while PF-105/PF-109 control the explicit canonical separator family. PF-125 is strong enough to remove both restrictions: its globally coherent prime/shift marking is asymptotically bilipschitz on the complete tail, so **every** hyperbolic conjugacy class supported sufficiently far out — simple or self-intersecting, primitive or imprimitive, traversing arbitrarily many pants — has the same marked length in the prime flute and the exact all-composite shift clone up to one uniform multiplicative error tending to `1`.

This does not give a full relative Selberg/Ruelle zeta function. The number of tail primitive classes is itself uncontrolled at the level needed for infinite orbit products, so infinitely many individually vanishing length defects may still accumulate. PF-158 already demonstrates this distinction in the canonical-separator sector. The finding rules out the **tail marked-length/right-limit datum itself** as a primality selector; it does not rule out a genuinely nonlocal summation or interference mechanism built from the complete primitive orbit family.

## Claim

Let `X` be the exact prime flute and `X_+` the exact all-composite shift clone `p_n -> p_n+1` of PF-106. Let

\[
F:X\longrightarrow X_+
\]

be the globally coherent marking constructed in PF-125. Write `P_n,P_n^+` for the matched one-cusp pants, and let

\[
\varepsilon_n:=\max(\delta_n,\delta_{n+1}),
\qquad
\delta_n=a_n^+-a_n,
\]

with the PF-125 tail estimate

\[
\operatorname{Bilip}(F|_{P_n})\le 1+C\varepsilon_n,
\qquad
\varepsilon_n\longrightarrow0.
\tag{1}
\]

After discarding a fixed finite head, let `T_N` be the closed tail component obtained by cutting `X` along the distinguished separating cuff before `P_N`, and let `T_N^+` be the matched tail in `X_+`. Put

\[
K_N:=\sup_{n\ge N}\operatorname{Bilip}(F|_{P_n}).
\tag{2}
\]

Then

\[
\boxed{K_N\longrightarrow1.}
\tag{3}
\]

Moreover the restriction

\[
F_N:=F|_{T_N}:T_N\longrightarrow T_N^+
\]

is globally `K_N`-bilipschitz. Consequently, for every hyperbolic free homotopy class `alpha` represented in `T_N`, if `ell_X(alpha)` and `ell_{X_+}(F_*alpha)` denote the lengths of the global geodesic representatives in the two complete flutes, then

\[
\boxed{
K_N^{-1}
\le
\frac{\ell_{X_+}(F_*\alpha)}{\ell_X(\alpha)}
\le
K_N.
}
\tag{4}
\]

Equivalently, if `H(T_N)` denotes all hyperbolic conjugacy classes carried by the tail,

\[
\boxed{
D_N^{\rm all}
:=
\sup_{\alpha\in H(T_N)}
\left|
\log\frac{\ell_{X_+}(F_*\alpha)}{\ell_X(\alpha)}
\right|
\le \log K_N
\longrightarrow0.
}
\tag{5}
\]

The same bound therefore holds after restricting the supremum to primitive classes, simple classes, any fixed topological word family, or any family whose word complexity and number of crossed pants are allowed to grow arbitrarily with `N`.

Thus the exact prime flute and the exact all-composite shift clone have asymptotically identical **complete marked tail translation-length functions**. In the standard terminology of infinite-type length-spectrum Teichmüller theory, the PF-125 marking is an asymptotic isometry in the length-spectrum sense; here that conclusion is obtained directly from the project-specific bilipschitz marking and does not require an upper-bounded pants decomposition.

## 1. The pantwise constants glue without accumulation

PF-125 does more than provide independent near-isometries of pants. Its finite-cuff traces commute exactly with the zero-twist gluing, the two Lambert halves agree on their split ray, and each cusp interpolation is incorporated into the same pantwise `1+O(epsilon_n)` estimate and becomes exactly isometric sufficiently deep. Therefore the maps on adjacent pants define one continuous map `F` on the complete surface.

Let a rectifiable curve `gamma` be contained in `T_N`. Decompose it at its intersections with the canonical cuffs. A compact curve meets only finitely many members of the locally finite pants decomposition. On every piece lying in `P_n`, equation (1) gives

\[
\operatorname{length}_{X_+}(F\gamma|_{P_n})
\le
K_N\operatorname{length}_{X}(\gamma|_{P_n}).
\]

Summing the finitely many pieces gives

\[
\operatorname{length}_{X_+}(F\gamma)
\le
K_N\operatorname{length}_{X}(\gamma).
\tag{6}
\]

The inverse pant maps obey the same bilipschitz constant, so the reverse inequality holds as well. There is no product of pantwise errors: a length is additive over the crossed pieces, hence only the **largest** tail bilipschitz constant enters. Since `epsilon_n -> 0`, the tail supremum in (2) tends to `1`, proving (3).

This is the point that PF-111 did not address. Arbitrarily complicated words crossing an arbitrarily long finite chain of pants do not accumulate a factor such as `prod_n(1+C epsilon_n)`; the global metric comparison gives the supremum bound instead.

## 2. Tail classes keep their geodesic representatives in the tail

It remains to check that taking geodesic representatives does not let a tail class escape through the cutting cuff and exploit the finite head.

Let `C_N` be the simple closed geodesic bounding `T_N`. A free homotopy class represented by a loop in `T_N` has geometric intersection number zero with `C_N`. The geodesic representative of a hyperbolic class and the geodesic `C_N` are in minimal position: two hyperbolic geodesics cannot bound a bigon. Hence the geodesic representative has no intersections with `C_N`. Unless the class is the boundary class itself, connectedness then places the entire geodesic in the interior of `T_N`; the boundary class is already contained in `T_N`.

The identical argument applies to `T_N^+`. Therefore one may apply (6) to the prime geodesic representative to obtain

\[
\ell_{X_+}(F_*\alpha)
\le
K_N\ell_X(\alpha),
\]

and apply the inverse estimate to the clone geodesic representative to obtain the reverse inequality. This proves (4)--(5).

No simplicity assumption on `alpha` is required. A closed geodesic may self-intersect arbitrarily often; only its zero geometric intersection with the separating tail boundary is used.

## 3. Relation to asymptotic length-spectrum Teichmüller theory

F. Yaşar, *Infinite-dimensional Teichmüller spaces*, arXiv:2104.00289, Definition 2.8, calls a length-spectrum bounded marking an **asymptotic isometry** when, for every `epsilon>0`, one can remove a finite-type subsurface so that the remaining length-spectrum constant is less than `1+epsilon`. The paper then studies the resulting little length-spectrum Teichmüller space `T^0_ls`.

Equation (5) supplies exactly this type of tail control, and in fact a stronger version because it bounds all hyperbolic conjugacy classes, not only the simple closed curves entering the usual length-spectrum constant. Given `epsilon>0`, choose `N` with `K_N<1+epsilon` and take the finite head before `C_N` as the removed finite-type subsurface.

Yaşar's Fenchel--Nielsen characterization later in that paper assumes an upper-bounded base pants decomposition. The distinguished prime-flute cuffs grow without bound, so that characterization is **not** being imported here. The asymptotic-isometry conclusion follows directly from PF-125's explicit global map; the literature is used only to classify the resulting tail relation as a standard notion rather than a new general theorem.

Likewise, the elementary fact that a `K`-bilipschitz marking distorts every marked closed length by at most `K` is classical. The project-specific content is that PF-125 supplies such markings with `K_N -> 1` for the exact prime flute and an exact all-composite control despite the unbounded cuffs, cusps, zero systole, and arbitrarily extreme neighboring gap ratios.

## 4. What this kills and what survives

PF-105 proved uniform tail equivalence for exact four-point cross-ratios and canonical multi-gap separators of a dilation clone. PF-109 sharpened the separator comparison for the shift clone, and PF-111 controlled every closed word **inside one pant**. Equation (5) upgrades the shift-clone control to every marked closed word carried by the complete escaping tail.

Therefore no proposed RH mechanism can obtain primality specificity merely from:

- a pointed/right limit of finitely many marked primitive lengths escaping to infinity;
- the tail length-spectrum constant or any continuous scalar extracted only from the uniform marked length-ratio function;
- choosing more complicated primitive words, or words crossing more pants, while still reading only their individual asymptotic marked lengths.

The all-composite shift clone has the same data in the limit.

The surviving loophole is genuinely collective. Equation (5) supplies **uniform vanishing**, not an `ell^1` estimate over the set of primitive conjugacy classes. On this flute there can be infinitely many relevant orbit classes in bounded length ranges, and an infinite product/sum can amplify small paired defects. PF-158 is a concrete warning: even for the explicitly controlled canonical separator family, the relative Selberg logarithmic derivative has a nontrivial convergence abscissa because orbit multiplicity competes with the individual length error.

Accordingly PF-166 does **not** imply convergence or zero-freeness of a full relative Selberg/Ruelle product, equality of unmarked primitive length multisets, equality of resonances or scattering matrices, equality of discrete Laplace spectra, trace-class relative resolvent, or any RH statement. It says that any such surviving mechanism must use the infinite assembly of orbit data, multiplicities, phases, or an operator-level effect; it cannot reside in the asymptotic marked length of any individual tail word, no matter how complicated that word is.

## 5. Audit / falsification core

A later adversary can check the finding through the following short chain.

1. Verify PF-125's exact global gluing and the uniform pant estimate `Bilip(F|P_n) <= 1+C epsilon_n` with `epsilon_n -> 0`, including its cusp interpolation.
2. Take the tail supremum to obtain `K_N -> 1`.
3. Check that exact trace matching across cuffs makes the restriction to `T_N` globally `K_N`-bilipschitz; because lengths add over pieces, no product of local constants appears.
4. For a tail-supported free homotopy class, use the geodesic bigon/minimal-intersection argument with the separating cuff `C_N` to show that its global geodesic representative remains in the tail, and repeat on the clone.
5. Apply the map and its inverse to the two geodesic representatives to prove (4), then take the supremum to prove (5).
6. Compare only with Yaşar's definition of asymptotic isometry; do not invoke the upper-bounded Fenchel--Nielsen characterization, whose hypothesis fails for the distinguished prime-flute pants decomposition.
7. Do not upgrade uniform tail length control to convergence of an infinite primitive-orbit sum/product without a separate multiplicity and summability estimate.

A refutation must therefore find a failure in PF-125's global tail bilipschitz estimate/gluing, show that a tail class can have a global geodesic representative crossing the separating geodesic despite zero geometric intersection, or identify a hidden dependence of the length comparison on word complexity after gluing. Merely showing that a full relative zeta can still accumulate infinitely many small errors does not refute PF-166; that collective amplification is explicitly outside the claim.

## Consequence for the research line

The natural marked-length escape route left open by pant-local and canonical-separator controls is closed. The exact prime surface and an exact all-composite surface are asymptotically indistinguishable at the level of the **entire marked tail length function**. A future prime-specific spectral/dynamical mechanism must therefore survive an asymptotic length-spectrum equivalence and extract information from a genuinely global infinite assembly — for example a summation threshold, operator ideal, scattering phase, resonance mechanism, or other nonlocal construction — rather than from individual primitive lengths or their finite right-limit configurations.
