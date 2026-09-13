# RE-102 — two-sided first-layer contact closes the local support-boundary frontier

**Status:** `EXACT-DERIVED + FRONTIER-SYNTHESIS + TWO-SIDED-FIRST-LAYER-CONTACT + FULL-PRIME-GAP-PULLBACK + LOCAL-BOUNDARY-CLOSURE + GLOBAL-FRONTIER-RECLASSIFICATION + SOURCE-ASSEMBLY-OBSTRUCTION + PRIOR-ART-BOUNDED`.

`RE-101` lowers the last unresolved mixed first/depth-two support-boundary estimate below `173/200`, but by itself it does not say what geometry remains after that channel is removed. Recomputing the full local boundary decomposition gives a stronger structural conclusion. Above the new threshold

\[
\boxed{
\Theta_*:=\frac{265657}{307200}
=0.8647688802\ldots,
}
\tag{1}
\]

every sufficiently late false-RH compact threshold fan is, outside vanishing threshold measure, supported only on chambers whose **two adjacent physical support boundaries both contain a first-layer CA event**. Equivalently, the surviving open chamber pulls back under the first-layer event map to one entire gap between consecutive ordinary primes.

This closes the current hierarchy of **local support-boundary depth channels**. The deeper-boundary channel had already fallen to `469/600` in `RE-091`; same-depth higher-layer chambers were cheaper still by `RE-090`; `RE-095`--`RE-101` now remove the only remaining one-sided depth-two escape. No larger numerical boundary-depth frontier remains in the present decomposition.

The conclusion is deliberately not a global RH frontier. Two-sided first-layer contact does not make the selected fan first-layer-only: depth-two events may tie either endpoint, and higher-layer events may still alter selected states elsewhere in the fan or be crossed in selected-state switches. Moreover `RE-083`--`RE-084` show that first-layer endpoint support and timing geometry by themselves are already reconstructed from ordinary primes, while `RE-079`--`RE-082` show that the corresponding smooth transport geometry is noncoercive. The obstruction left after (1) is therefore **nonlocal/source-conditioned assembly**, not another unaccounted local boundary depth.

Assume RH is false and write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\tag{2}
\]

Suppose

\[
\Theta>\Theta_*.
\tag{3}
\]

Choose a compact threshold interval

\[
J=[b_0,b_1]
\Subset
\left(1-\Theta,\,1-\Theta_*\right),
\qquad
1-\Theta_*
=\frac{41543}{307200}.
\tag{4}
\]

Work on the sufficiently late common positive CA blocks supplied by `RE-040`. For a selected state `C`, let

\[
\xi_-(C)<\xi_+(C)
\tag{5}
\]

be its adjacent physical support coordinates and let `I_C\subset J` be its selected threshold cell. Call a boundary **first-layer-contacting** if its physical coordinate contains an event `(p,1)` for some ordinary prime `p`; ties with higher-layer events are allowed.

Then there are exceptional unions `\mathcal E_{\mathcal B}\subset J`, one on each sufficiently late block `\mathcal B`, with

\[
\boxed{
|\mathcal E_{\mathcal B}|\longrightarrow0
}
\tag{6}
\]

along the late blocks, such that every selected cell meeting `J\setminus\mathcal E_{\mathcal B}` has **both** `\xi_-(C)` and `\xi_+(C)` first-layer-contacting.

If

\[
\xi_-(C)=\eta_1(p_-),
\qquad
\xi_+(C)=\eta_1(p_+),
\qquad p_-<p_+,
\tag{7}
\]

then `p_-` and `p_+` are consecutive ordinary primes and

\[
\boxed{
\eta_1^{-1}\!\left((\xi_-(C),\xi_+(C))\right)
=(p_-,p_+).
}
\tag{8}
\]

Consequently

\[
\boxed{
\xi_+(C)-\xi_-(C)
=(p_+-p_-)+O\!\left(\frac1{\log p_-}\right),
}
\tag{9}
\]

uniformly on late surviving cells. Thus, at the local support-boundary level, the residual chamber metric is exactly ordinary-prime-gap geometry passed through the deterministic first-layer CA map.

## 1. Deep boundaries are already below the new threshold

`RE-091` combines the depth-at-least-three host count with Stadlmann's ordinary-prime-gap second moment. Its conclusion is stronger than merely excluding higher-layer-only chambers: whenever

\[
\Theta>\frac{469}{600},
\tag{10}
\]

the total selected threshold measure of cells touching a depth `j\ge3` boundary tends to zero, and after splicing with `RE-090`, every remaining selected cell has a first-layer atom on at least one adjacent support boundary.

The present threshold satisfies

\[
\Theta_* - \frac{469}{600}
=\frac{25529}{307200}>0.
\tag{11}
\]

Moreover the band in (4) lies far inside the capacity range required by that argument because

\[
b_1<1-\Theta_*
=0.135231\ldots
<\frac{131}{600}.
\tag{12}
\]

Hence, on the present false-RH band, let `\mathcal E_{\ge3}` be the union of selected cells having at least one adjacent depth-at-least-three event. Then

\[
|\mathcal E_{\ge3}|=o_J(1),
\tag{13}
\]

and outside a further `o_J(1)` exceptional union every selected cell has first-layer contact on at least one side.

This step is where the older depth hierarchy is exhausted. A surviving boundary that has no first-layer atom cannot be depth `3` or deeper outside (13). Since every physical support boundary is a CA event coordinate, its only remaining higher-layer possibility is depth `2`.

## 2. RE-101 removes exactly the remaining one-sided depth-two escape

Consider now a surviving selected cell `C` with first-layer contact on one boundary but not on the other. By Section 1, after discarding `\mathcal E_{\ge3}`, the non-first-layer boundary contains a depth-two event and no first-layer event. This is precisely the residual mixed class isolated in `RE-095`:

\[
\mathcal M_{1/2}(X)
=
\{\text{one first-layer-contacting boundary and one depth-two-only boundary}\}
\tag{14}
\]

on a bounded-ratio physical shell `X\le Y_C<2X`. Ties on the first-layer side do not change this classification; a tie involving depth `3` or deeper is already in `\mathcal E_{\ge3}`.

`RE-095` proves that a polynomial saving in the number of deformed-quadratic bad hosts lowers the old `173/200` moment frontier by exactly half that host-count saving. `RE-096`--`RE-100` reduce and then progressively sharpen the required sparse-host theorem, and `RE-101` closes its complete zero-density tail. Optimizing the resulting two terms gives exactly (1): for every false-RH exponent satisfying (3), one may choose the auxiliary short-interval exponent strictly inside the admissible window so that

\[
\sum_{C\in\mathcal M_{1/2}(X)}|I_C|
\ll_J X^{-\delta_J+o(1)}
\tag{15}
\]

for some `\delta_J>0`. Summing late dyadic shells yields

\[
\left|
\bigcup_{C\in\mathcal M_{1/2}}I_C
\right|
=o_J(1).
\tag{16}
\]

Let `\mathcal E_{1/2}` denote this union. Combining (13), (16), and the one-sided first-layer-contact conclusion of `RE-091` proves (6): if a selected cell outside

\[
\mathcal E_{\mathcal B}
:=
\mathcal E_{\ge3}
\cup
\mathcal E_{1/2}
\cup
\mathcal E_{\mathrm{one\text{-}side}},
\tag{17}
\]

failed first-layer contact on either boundary, the other boundary would have first-layer contact and the missing side would be depth-two-only, putting the cell back in `\mathcal E_{1/2}`. Here `\mathcal E_{\mathrm{one\text{-}side}}` denotes the vanishing exceptional union already present in the final splice of `RE-091`.

Thus the decomposition is exhaustive at the level claimed:

\[
\boxed{
\Theta>\Theta_*
\Longrightarrow
\text{two-sided first-layer contact for almost every selected threshold cell.}
}
\tag{18}
\]

No purity statement is used or obtained.

## 3. Every surviving chamber pulls back to one whole ordinary prime gap

Take a surviving cell and write its first-layer endpoint labels as in (7). The first-layer event map is strictly increasing in the ordinary prime label by `RE-004`. Because `(\xi_-(C),\xi_+(C))` is an open physical support chamber, it contains no CA event of any layer.

If there were an ordinary prime `r` with

\[
p_-<r<p_+,
\tag{19}
\]

then monotonicity would give

\[
\xi_-(C)=\eta_1(p_-)
<\eta_1(r)
<\eta_1(p_+)=\xi_+(C),
\tag{20}
\]

contradicting the defining emptiness of the chamber. Hence `p_-` and `p_+` are consecutive primes. Since `\eta_1` is invertible and increasing on the first-layer coordinate,

\[
\eta_1^{-1}((\eta_1(p_-),\eta_1(p_+)))
=(p_-,p_+),
\tag{21}
\]

which proves (8). This is stronger than the generic pullback used in `RE-091`: there the chamber only supplied a prime-free subinterval contained in an ambient ordinary-prime gap; after two-sided first-layer contact, the pullback is the **entire** gap.

The asymptotic first-layer translation from `RE-042`, `RE-069`, and `RE-084`,

\[
\eta_1(p)
=p+\frac12
-\frac{1}{2(\log p+1)}
+O(p^{-1}),
\tag{22}
\]

then gives (9). In particular, the universal half-unit shift cancels from the chamber width. Any further local metric gain on this surviving class must therefore be a theorem about the ordinary prime gap itself or about how another CA layer is tied to its endpoints; there is no residual first-layer timing scale to exploit.

## 4. Two-sided first-layer contact is not a first-layer-only fan

A stronger interpretation would be false. Equation (18) says only that both adjacent support coordinates contain first-layer atoms. Either endpoint may simultaneously contain a depth-two event. Higher-layer thresholds outside the open chamber can change the exponent vector, alter which CA states are exposed, or occur inside a selected-state switch spanning several physical events. The sparse higher-layer source can therefore remain dynamically important even when it no longer supplies a naked adjacent boundary.

This matters because several earlier negative results apply with full force to the new normal form. `RE-083` proves that on arbitrary mixed fan segments the selector prime set and physical first-layer support births agree exactly up to the two fringe bits, regardless of intervening higher-layer events. `RE-084` then reconstructs the entire labeled first-layer event timeline from those endpoint data and shows that all fixed one-prime delay statistics collapse to the universal half-translation. Thus two-sided first-layer contact does not create a new endpoint mismatch that could contradict the fan.

Likewise `RE-079` shows that the corrected Chebyshev and reciprocal-Mertens Lyapunov coordinates are two kernel moments of one positive transport measure, and `RE-081`--`RE-082` show that the long-fan complementary transport front survives after deleting discrete higher-layer atoms and can already be realized by smooth selector dilation. The surviving problem is therefore not to find a third local boundary depth estimate. It is to explain why the **actual ordinary-prime/CA source cannot assemble the selected sequence of states** required by the false-RH fan while satisfying the height condition.

## 5. The numerical frontier and the global obstruction must now be kept separate

The present support-boundary hierarchy has three numerical scales. Same-depth higher-layer chambers are eliminated above the `0.57` aggregate-gap threshold of `RE-090`; any chamber touching depth `3` or deeper is eliminated above `469/600` by `RE-091`; and the mixed first/depth-two residue is eliminated above `Theta_*` by `RE-101` through `RE-095`. Since

\[
0.57
<\frac{469}{600}
<\Theta_*,
\tag{23}
\]

the maximum current **local support-boundary** threshold is exactly `Theta_*`.

But none of these statements excludes a false-RH fan whose local cells all have the two-sided first-layer form (18). In particular, the universal height localization of `RE-021`--`RE-022` survives every CA boundary chamber: a hypothetical self-tangent counterexample still requires the selected finite-annulus mixed Mertens--Chebyshev excursion there. Global one-sided control of that mixed race is already RH-strength by `RE-009`, so simply replacing the local boundary argument by a global prime-race bound would only restate the original difficulty.

The destination after `RE-101` is therefore qualitatively different from the one before it. The line no longer needs another unconditional estimate whose sole purpose is to make an exposed support boundary touch the first layer. The next useful theorem must exploit information that survives the reductions above, for example a source-selected restriction coupling the full prime gap `(p_-,p_+)` to tied depth-two endpoints, a non-endpoint statistic of the ordering of mixed-layer events across selected-state switches, or a direct bound on the finite-annulus mixed race along the CA-selected host sequence. Any candidate functional depending only on the reconstructed first-layer endpoint set or its deterministic timing should first be reduced through `RE-083`--`RE-084`; those channels are already information-theoretically exhausted.

## 6. Stress tests and prior-art boundary

The theorem is intentionally an almost-everywhere threshold statement. It does not say that every late selected cell has two first-layer boundaries, and it does not turn the `o_J(1)` exceptional union into a count estimate. A sparse exceptional sequence can still be arithmetically significant and must not be silently discarded in a pointwise Robin argument.

The result also does not improve (1) numerically. It consumes the `RE-101` bound and recomputes its destination. If a future theorem lowers the mixed first/depth-two exponent again, the same synthesis will lower the two-sided-contact threshold automatically until another channel overtakes it.

Tied endpoints are harmless for (8). Strict monotonicity of `p\mapsto\eta_1(p)` means a physical coordinate contains at most one first-layer label, even if one or more higher-layer events share that coordinate. Hence the labels `p_-` and `p_+` in (7) are unambiguous.

Finally, no new external theorem is load-bearing in this synthesis. The prime-gap inputs and sparse-sample zero-density inputs used by `RE-090`, `RE-091`, and `RE-101` are already anchored in `SOURCES.md`. A directed current prior-art audit found neighboring work on CA/Robin extremal windows and divisor-sum exchange arguments, but no source giving this threshold-measure two-sided first-layer-contact normal form or the consequent separation between the local numerical frontier and the nonlocal source-assembly obstruction. `SOURCES.md` therefore requires no new entry.

The durable conclusion is:

\[
\boxed{
\text{above }\Theta_*,
\quad
\text{local support-boundary depth is no longer the obstruction;}
\quad
\text{selected source assembly is.}
}
\tag{24}
