# FD-158 — Finite auxiliary prime boxes replicate the cross-core leakage obstruction

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / finite prime box / recursive cross-core leakage law
- **Depends on:** FD-155, FD-156, FD-157

## Claim

FD-157 shows that bounded-distortion multi-parent escape from the pure `S`-Boolean packet must export mass to nontrivial `S`-free cores. A natural repair is therefore to add a finite auxiliary prime vocabulary `U`, allow arbitrary mixing among all `S`-states over those auxiliary cores, and hope that this absorbs the cross-core flux. It does not: once the complete `S union U` Boolean box is present below the truncation, the same prime-face obstruction is replicated over every `U`-core state, and bounded parent load forces fresh leakage to a prime outside `S union U`.

Fix disjoint finite prime sets `S,U`, write

\[
P_S:=\prod_{p\in S}p,
\qquad
P_U:=\prod_{q\in U}q,
\qquad
s:=|S|,
\qquad
u:=|U|,
\tag{1}
\]

and assume

\[
T\ge P_SP_U.
\tag{2}
\]

Retain the squarefree vertex set, uniform law, prime-avoidance anchor, directed divisibility relation, edge probability measure, anchored Cheeger constant, and parent distortion of FD-157:

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
R_{S,T}:=V_T\setminus D_{S,T},
\tag{3}
\]

\[
h_{S,T}
:=
\inf_{\varnothing\ne A\subseteq R_{S,T}}
\frac{\eta_T(\partial A)}{\nu_T(A)},
\qquad
P_{S,T}
:=
\max_{d\in D_{S,T}}
\frac{\eta_T^-(d)}{\nu_T(d)}.
\tag{4}
\]

Define the completed auxiliary prime box

\[
B_{S\mid U}
:=
\{n:n\mid P_SP_U,\ (n,P_S)>1\}.
\tag{5}
\]

It consists of every nonempty `S`-face state over every `U`-core state, so

\[
|B_{S\mid U}|
=(2^s-1)2^\nu.
\tag{6}
\]

Let the fresh-prime leakage be

\[
E_{\rm out}(S,U,T)
:=
\{(n,m)\in E_T^*:n\in B_{S\mid U},\ m\notin B_{S\mid U}\},
\tag{7}
\]

\[
L_{S,U,T}
:=
|V_T|\,\eta_T(E_{\rm out}(S,U,T)).
\tag{8}
\]

Then every multi-parent architecture satisfies

\[
\boxed{
P_{S,T}+2^{-\nu}L_{S,U,T}
\ge
h_{S,T}(2^s-1).
}
\tag{9}
\]

Equivalently,

\[
\boxed{
L_{S,U,T}
\ge
2^\nu\bigl(h_{S,T}(2^s-1)-P_{S,T}\bigr).
}
\tag{10}
\]

Every child occurring in `E_out(S,U,T)` contains at least one prime outside `S union U`. Thus enlarging the pure packet by any finite collection of auxiliary prime coordinates does not dilute the FD-157 parent-load obstruction as long as the complete Boolean box fits below `T`: it only creates `2^nu` copies of the same cut, and the number of possible incoming anchor states grows by the identical factor.

If in addition the child distortion is bounded as in FD-157,

\[
\eta_T^+(m)\le K_{S,T}\nu_T(m),
\qquad m\in R_{S,T},
\tag{11}
\]

and `C_(S,U,T)` denotes the distinct children hit by `E_out(S,U,T)`, then

\[
\boxed{
|C_{S,U,T}|
\ge
\frac{2^\nu\bigl(h_{S,T}(2^s-1)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{12}
\]

Consequently, under fixed positive expansion and bounded parent/child distortion, a completed `S union U` box forces `Omega(2^{s+nu})` distinct recipients carrying at least one fresh prime outside the declared box. A bounded-load escape from FD-157 therefore cannot terminate inside any such finite completed auxiliary prime box.

## 1. The completed box has only `U`-anchor divisors entering it

Take an edge `(d,m)` with

\[
m\in B_{S\mid U},
\qquad
d\notin B_{S\mid U}.
\tag{13}
\]

Because every edge respects divisibility, `d|m`; because `m|P_SP_U`, also `d|P_SP_U`. If `d` contained any prime from `S`, then `(d,P_S)>1` and (5) would put `d` back in `B_(S|U)`, contradicting (13). Hence `d` avoids `S`, and therefore

\[
d\mid P_U.
\tag{14}
\]

Conversely every divisor of `P_U` is an anchor vertex because `S` and `U` are disjoint. Thus the entire incoming boundary of `B_(S|U)` is supported on the finite anchor set

\[
A_U:=\{d:d\mid P_U\},
\qquad
|A_U|=2^\nu.
\tag{15}
\]

This is the exact enlargement of the single incoming anchor `1` from FD-157. Adding one auxiliary prime doubles both the number of packet copies and the number of possible anchor parents; adding `nu` of them multiplies both by `2^nu`.

Now take an outgoing edge `(n,m)` with `n in B_(S|U)` and `m notin B_(S|U)`. Since `n|m`, the child still contains an `S`-prime and hence lies in `R_(S,T)`. If every prime factor of `m` belonged to `S union U`, squarefreeness would imply

\[
m\mid P_SP_U,
\tag{16}
\]

and the surviving `S`-prime would imply `(m,P_S)>1`; (5) would again force `m in B_(S|U)`. Therefore every outgoing boundary child has a genuinely new prime coordinate:

\[
\exists r\mid m
\quad\text{with}\quad
r\notin S\cup U.
\tag{17}
\]

The boundary consequently decomposes exactly as

\[
\boxed{
\eta_T(\partial B_{S\mid U})
=
\eta_T\!\left(
\{(d,m)\in E_T^*:d\mid P_U,\ m\in B_{S\mid U}\}
\right)
+
\frac{L_{S,U,T}}{|V_T|}.
}
\tag{18}
\]

No structural approximation enters (18).

## 2. The auxiliary multiplicity cancels from the Cheeger test

For every `d|P_U`, the parent marginal is bounded by the same anchor distortion:

\[
\eta_T^-(d)
\le
\frac{P_{S,T}}{|V_T|}.
\tag{19}
\]

Summing over the `2^nu` possible incoming anchors gives

\[
\eta_T\!\left(
\{(d,m):d\mid P_U,\ m\in B_{S\mid U}\}
\right)
\le
\frac{2^\nu P_{S,T}}{|V_T|}.
\tag{20}
\]

On the other hand, `B_(S|U)` is a nonempty subset of the nonanchor region, so the definition of `h_(S,T)` gives

\[
\eta_T(\partial B_{S\mid U})
\ge
h_{S,T}\nu_T(B_{S\mid U})
=
\frac{h_{S,T}(2^s-1)2^\nu}{|V_T|}.
\tag{21}
\]

Insert (18) and (20) into (21), multiply by `|V_T|`, and divide by `2^nu`. This yields exactly (9).

The cancellation of `2^nu` is the point. If no edge from the completed box introduces a prime outside `S union U`, then `L_(S,U,T)=0`, and (9) collapses to

\[
\boxed{
\frac{P_{S,T}}{h_{S,T}}
\ge
2^s-1,
}
\tag{22}
\]

with **no dependence on the size of the auxiliary prime set**. Arbitrary multi-parent mixing among the `2^nu` auxiliary core states does not buy any improvement in the prime-face load ratio when the full finite box is closed under the dynamics.

More generally, if `h_(S,T)>=c>0` and `P_(S,T)<=P`, then

\[
2^{-\nu}L_{S,U,T}
\ge
c(2^s-1)-P.
\tag{23}
\]

Thus the fresh-prime flux per auxiliary Boolean state remains on the original `2^s` scale. FD-157's cross-core leakage has not been absorbed; it has merely been replicated across the auxiliary box.

## 3. Bounded child distortion forces fresh-prime recipient proliferation

Let

\[
C_{S,U,T}
:=
\{m\in R_{S,T}\setminus B_{S\mid U}:
\exists n\in B_{S\mid U}\text{ with }(n,m)\in E_T^*\}.
\tag{24}
\]

By (17), every member of `C_(S,U,T)` contains a prime outside `S union U`. Under (11), all outgoing leakage into this recipient set is bounded by

\[
\eta_T(E_{\rm out}(S,U,T))
\le
\sum_{m\in C_{S,U,T}}\eta_T^+(m)
\le
\frac{K_{S,T}|C_{S,U,T}|}{|V_T|}.
\tag{25}
\]

Since the left side is `L_(S,U,T)/|V_T|`, equations (10) and (25) give (12).

In particular, if

\[
h_{S,T}\ge c>0,
\qquad
P_{S,T}=O(1),
\qquad
K_{S,T}\le K<\infty,
\tag{26}
\]

then as `s -> infinity`, for every auxiliary set whose complete box obeys (2),

\[
\boxed{
|C_{S,U,T}|
\ge
\left(\frac cK-o(1)\right)2^{s+\nu}.
}
\tag{27}
\]

So bounded child load rules out a second naive repair: the architecture cannot add a finite collection of auxiliary primes and then funnel all newly forced boundary through a bounded family of vertices just outside that enlarged box.

## 4. What this adds to FD-157

FD-157 deliberately stopped at a real gap: `Omega(2^s)` distinct cross-core recipients do not imply `Omega(2^s)` independent source information, because many recipient vertices can share the same `S`-free prime vocabulary. Equation (9) does not erase that warning. Instead it tests the most immediate way of exploiting it.

Suppose one tries to choose a finite set `U` of outside primes, build all available core states from `U`, and use those extra coordinates as a mixing reservoir for the pure `S`-face. Once that reservoir is completed to the divisor box (5), it becomes another exact order ideal for divisibility except at its anchor face and at edges introducing a new prime. The Cheeger test then reproduces the original obstruction with no loss. **Finite completed auxiliary prime support is therefore not a terminal resource.** Positive expansion plus bounded parent load must keep exporting flux to fresh prime coordinates.

This turns the live escape from FD-157 into a more specific one. A viable bounded-distortion architecture must now exploit at least one of the following phenomena: an auxiliary prime vocabulary that keeps migrating/growing so that no relevant completed box closes below `T`; strongly nonuniform use of only a sparse subset of auxiliary Boolean states, so that the completed-box test is not the right cut; loss of parent or child conditioning; or a further invariant/source identity that makes the fresh-prime migration Farey-native rather than a disguised reconstruction of Möbius signs.

The result is therefore a **prime-support migration obstruction**, not yet an information lower bound.

## 5. Scope and limitations

The completeness hypothesis (2) is essential to the clean cardinality law. It guarantees that every divisor of `P_SP_U`, hence every one of the `(2^s-1)2^nu` nonanchor Boolean states, is present in `V_T`. If `P_SP_U>T`, only a truncated down-set remains; its boundary-to-volume ratio depends on the geometry of that truncation, and (9) cannot be quoted unchanged.

Likewise, (9) does not imply that one can iterate fresh-prime leakage indefinitely at fixed `T`. New recipient primes may be large, and after adjoining them to `U` the enlarged full product can exceed `T`, destroying the completed-box hypothesis. Nor does (12) prove that the recipient set carries independent Möbius information: distinct recipients may still be generated by a deterministic rule whose parity/source provenance is already available elsewhere.

Those limitations are exactly where the remaining problem lives. FD-158 excludes a finite completed-prime-box gadget as the missing multi-parent mechanism; it does not yet exclude scale-dependent sparse or ever-migrating prime support.

## 6. Stress tests

For `S={2}` and `U={3}`, the completed box is

\[
B_{S\mid U}=\{2,6\}.
\tag{28}
\]

Its only possible incoming anchor parents are `1` and `3`. Any outgoing child divisible by `2` but outside `{2,6}` must contain a prime other than `2,3`. Thus the factor `2^nu=2` in both the volume and incoming-load budget is exact.

For `S={2,3}` and `U={5}`,

\[
B_{S\mid U}=\{2,3,6,10,15,30\},
\tag{29}
\]

of size `(2^2-1)2=6`. Again the only outside divisors that can enter the box are the anchors `1,5`; every outgoing boundary child contains a prime outside `{2,3,5}`. These examples also show why merely saying "cross-core" is weaker than (17): FD-158 identifies the boundary as **fresh-prime leakage relative to the entire declared auxiliary vocabulary**.

## 7. Prior-art audit and next pressure point

A post-candidate search checked generic edge-isoperimetry on Boolean lattices/hypercubes, Cheeger inequalities on discrete graphs, and divisor-poset formulations. That literature supplies broad neighboring language but no result found in this pass states the anchored divisor resource law (9), its cancellation of the auxiliary factor, or the Farey/Möbius interpretation above. The proof here is the direct divisor-order-ideal cut identity (18) plus the already internal FD-157 distortion framework; no new external theorem is load-bearing, so no source anchor is added.

The next pressure point is the regime deliberately left open by the theorem: **sparse or scale-dependent auxiliary prime support that never fills a completed box before the truncation ceiling**. A useful next invariant would need to charge such migrating support without replacing the exact Boolean count by a bound too weak to survive the first-`s`-prime thinning scale from FD-155. Equivalently, one wants a truncated-down-set analogue of (9) whose cost depends on occupied prime-coordinate entropy or divisor shadows rather than on possession of the entire `S union U` cube.

### Retrieval notes

- Internal inputs: FD-155, FD-156, FD-157 and the current `farey_discrepancy` mind synthesis.
- Prior-art search executed only after the finite-box candidate was formed; no external result was used in the proof.
- Formalization gate: not opened. The contribution is a stable exact cut identity, but its proof is elementary and its present value is architectural rather than a mature standalone formal theorem surface.

### Confidence

High for (9)--(12): they are exact consequences of divisibility, squarefreeness, and the FD-157 definitions. Medium-high for the architectural interpretation: the completed-box escape is genuinely closed, but sparse/truncated/growing prime vocabularies remain open and are explicitly outside the claim.