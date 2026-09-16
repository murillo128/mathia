# FD-159 — Truncated auxiliary down-sets pay average-fiber leakage

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / truncated divisor down-set / average-fiber leakage law
- **Depends on:** FD-157, FD-158

## Claim

FD-158 proves the cross-core leakage obstruction when every `S`-face over a finite auxiliary Boolean cube is present below the ceiling `T`. Its explicit gap is truncation: if the full product no longer fits, different auxiliary cores support different numbers of primary `S`-states, and the factor `(2^s-1)2^nu` disappears.

The complete cube is not needed. The exact invariant is the **average occupied primary-fiber multiplicity over a divisor-downward auxiliary core set**.

Retain the squarefree vertex set, uniform law, directed divisibility relation, edge probability measure, anchored Cheeger constant, parent distortion, and (when invoked) child distortion from FD-157/FD-158:

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
R_{S,T}:=V_T\setminus D_{S,T},
\tag{1}
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
\frac{\eta_T^-(d)}{\nu_T(d)},
\tag{2}
\]

where `S` is a finite nonempty prime set and

\[
P_S:=\prod_{p\in S}p,
\qquad
p_*:=\min S.
\tag{3}
\]

Let `C` be a finite nonempty subset of `D_(S,T)` satisfying

\[
c\in C,\ d\mid c
\quad\Longrightarrow\quad
d\in C,
\tag{4}
\]

and assume every core is active,

\[
cp_*\le T,
\qquad c\in C.
\tag{5}
\]

For each `c in C`, define its occupied primary fiber

\[
F_{S,T}(c)
:=
\{q:q\mid P_S,\ q>1,\ qc\le T\},
\qquad
f_{S,T}(c):=|F_{S,T}(c)|,
\tag{6}
\]

and the truncated packet

\[
B_{S\mid C}(T)
:=
\{qc:c\in C,\ q\in F_{S,T}(c)\}.
\tag{7}
\]

Because `(c,P_S)=1`, the decomposition `qc` is unique. Hence

\[
M_{S,C}(T)
:=|B_{S\mid C}(T)|
=
\sum_{c\in C}f_{S,T}(c),
\qquad
\bar f_{S,C}(T)
:=
\frac{M_{S,C}(T)}{|C|}.
\tag{8}
\]

Define the outgoing leakage

\[
E_{\rm out}(S,C,T)
:=
\{(n,m)\in E_T^*:n\in B_{S\mid C}(T),\ m\notin B_{S\mid C}(T)\},
\tag{9}
\]

\[
L_{S,C,T}
:=
|V_T|\,\eta_T(E_{\rm out}(S,C,T)).
\tag{10}
\]

Then every multi-parent architecture satisfies the exact average-fiber obstruction

\[
\boxed{
P_{S,T}
+
\frac{L_{S,C,T}}{|C|}
\ge
h_{S,T}\,\bar f_{S,C}(T).
}
\tag{11}
\]

Equivalently,

\[
\boxed{
L_{S,C,T}
\ge
h_{S,T}M_{S,C}(T)-P_{S,T}|C|.
}
\tag{12}
\]

Every child in `E_out(S,C,T)` still contains an `S`-prime, but its `S`-free core lies outside `C`. Thus (11) is a genuine **outer-core-shadow leakage law**: truncating the auxiliary support replaces the full-cube multiplicity `2^nu` by the actual occupied core count and replaces the constant fiber size `2^s-1` by the average number of primary states that survive the ceiling.

If in addition

\[
\eta_T^+(m)\le K_{S,T}\nu_T(m),
\qquad m\in R_{S,T},
\tag{13}
\]

and `C_out(S,C,T)` is the set of distinct children hit by (9), then

\[
\boxed{
|C_{\rm out}(S,C,T)|
\ge
\frac{|C|\bigl(h_{S,T}\bar f_{S,C}(T)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{14}
\]

Consequently, sparse truncation by the ceiling does not by itself absorb the FD-158 obstruction. With positive anchored expansion and bounded parent/child distortion, insulation is possible only if the surviving auxiliary cores have bounded average primary-fiber multiplicity.

## 1. Divisor-downward support removes all internal parent holes

Take an incoming boundary edge `(d,m)` with

\[
m\in B_{S\mid C}(T),
\qquad
d\notin B_{S\mid C}(T).
\tag{15}
\]

Write the unique packet representation

\[
m=qc,
\qquad
c\in C,
\qquad
q\mid P_S,
\qquad
q>1.
\tag{16}
\]

Because every edge respects divisibility, `d|m`. Suppose first that `d` contains a prime from `S`. Squarefreeness gives a unique decomposition

\[
d=q'c',
\qquad
q'\mid P_S,
\qquad
q'>1,
\qquad
c'\mid c.
\tag{17}
\]

The down-set property (4) gives `c' in C`; also `d<=m<=T`. Hence `q' in F_(S,T)(c')`, so (7) puts `d` back in the packet, contradicting (15). Therefore every outside divisor parent entering the packet is `S`-free. Since it then divides `c`, (4) gives

\[
\boxed{
d\in C.
}
\tag{18}
\]

This is the truncated replacement for the `2^nu` incoming anchors of FD-158: **the entire incoming boundary is supported on at most the actual `|C|` occupied auxiliary core states**, independently of how unequal their primary fibers are.

Now take an outgoing edge `(n,m)` with `n in B_(S|C)(T)` and `m` outside. Since `n|m`, the child still contains an `S`-prime. Define its `S`-free core

\[
\kappa_S(m):=\frac{m}{\gcd(m,P_S)}.
\tag{19}
\]

If `kappa_S(m) in C`, then `gcd(m,P_S)>1`, `gcd(m,P_S)|P_S`, and `m<=T`; by (6)-(7) this would imply `m in B_(S|C)(T)`, again a contradiction. Hence

\[
\boxed{
\kappa_S(m)\notin C
\quad\text{for every }(n,m)\in E_{\rm out}(S,C,T).
}
\tag{20}
\]

Thus the boundary decomposes without approximation into incoming traffic from the occupied core down-set and outgoing traffic to its outer divisor shadow:

\[
\eta_T(\partial B_{S\mid C}(T))
=
\eta_T\!\left(
\{(d,m)\in E_T^*:d\in C,\ m\in B_{S\mid C}(T)\}
\right)
+
\frac{L_{S,C,T}}{|V_T|}.
\tag{21}
\]

## 2. Cheeger pressure is exactly the average primary-fiber size

Every `d in C` belongs to the anchor set `D_(S,T)`, so by definition of the parent distortion

\[
\eta_T^-(d)
\le
\frac{P_{S,T}}{|V_T|}.
\tag{22}
\]

Summing over the at most `|C|` incoming anchors from (18),

\[
\eta_T\!\left(
\{(d,m):d\in C,\ m\in B_{S\mid C}(T)\}
\right)
\le
\frac{|C|P_{S,T}}{|V_T|}.
\tag{23}
\]

The packet is a nonempty subset of `R_(S,T)`, so anchored Cheeger pressure gives

\[
\eta_T(\partial B_{S\mid C}(T))
\ge
h_{S,T}\nu_T(B_{S\mid C}(T))
=
\frac{h_{S,T}M_{S,C}(T)}{|V_T|}.
\tag{24}
\]

Combining (21), (23), and (24), and multiplying by `|V_T|`, yields

\[
L_{S,C,T}
\ge
h_{S,T}M_{S,C}(T)-P_{S,T}|C|,
\tag{25}
\]

which is (12). Division by `|C|` gives (11).

The cancellation mechanism from FD-158 is therefore more general than the complete Boolean count suggested. What cancels is not specifically `2^nu`; it is the **number of available incoming anchor cores**. The pressure left after that cancellation is exactly the mean number of nonanchor `S`-states carried by one such core.

In particular, if there is no outgoing outer-core leakage, then

\[
\boxed{
\frac{P_{S,T}}{h_{S,T}}
\ge
\bar f_{S,C}(T).
}
\tag{26}
\]

Thus a bounded parent-load ratio can close only packets whose average surviving primary fiber remains bounded.

## 3. FD-158 extends to an arbitrarily truncated finite auxiliary cube

Let `U` be any finite prime set disjoint from `S`; **do not assume** `P_SP_U<=T`. Define the active auxiliary cores

\[
C_U(T)
:=
\{c:c\mid P_U,\ cp_*\le T\}.
\tag{27}
\]

This is a divisor down-set. Moreover

\[
B_{S\mid C_U(T)}(T)
=
\{n\le T:n\mid P_SP_U,\ (n,P_S)>1\},
\tag{28}
\]

because every represented state `n=qc<=T` automatically has `p_*c<=qc<=T`, while every active core contributes precisely the `S`-divisors that fit.

Therefore (11) applies to the **actual ceiling-truncated `S union U` Boolean box** for every `T`. The completeness hypothesis `T>=P_SP_U` from FD-158 is needed only to make all fibers equal, not for the leakage mechanism itself.

When the full box does fit, `C_U(T)={c:c|P_U}`, every fiber has size `2^s-1`, and

\[
|C_U(T)|=2^{|U|},
\qquad
\bar f_{S,C_U(T)}(T)=2^s-1.
\tag{29}
\]

Equation (11) then reduces exactly to FD-158:

\[
P_{S,T}+2^{-|U|}L_{S,U,T}
\ge
h_{S,T}(2^s-1).
\tag{30}
\]

So FD-159 is not a different obstruction layered on top of FD-158; it identifies the quantity that FD-158's Boolean symmetry was hiding.

There is also a deterministic way to read the ceiling loss. Order the primary primes as

\[
p_1<p_2<\cdots<p_s
\tag{31}
\]

and define the available primary depth of a core by

\[
r_T(c)
:=
\max\left\{
0\le r\le s:
 c\prod_{j=1}^{r}p_j\le T
\right\}.
\tag{32}
\]

Every nonempty subset of the first `r_T(c)` primes has product at most their full product, hence

\[
f_{S,T}(c)
\ge
2^{r_T(c)}-1.
\tag{33}
\]

If

\[
\bar r_{S,C}(T)
:=
\frac1{|C|}\sum_{c\in C}r_T(c),
\tag{34}
\]

then convexity of `2^x` gives

\[
\boxed{
\bar f_{S,C}(T)
\ge
2^{\bar r_{S,C}(T)}-1.
}
\tag{35}
\]

Combining (11) and (35),

\[
\boxed{
P_{S,T}
+
\frac{L_{S,C,T}}{|C|}
\ge
h_{S,T}\bigl(2^{\bar r_{S,C}(T)}-1\bigr).
}
\tag{36}
\]

Thus under fixed positive expansion and bounded normalized leakage and parent load, the **average number of smallest primary coordinates that fit above an occupied auxiliary core must itself stay bounded**. Merely deleting high auxiliary states because of the ceiling is not enough if the surviving cores still have growing primary depth.

## 4. Bounded child distortion turns outer-core flux into recipient proliferation

Let

\[
C_{\rm out}(S,C,T)
:=
\{m\in R_{S,T}\setminus B_{S\mid C}(T):
\exists n\in B_{S\mid C}(T)
\text{ with }(n,m)\in E_T^*\}.
\tag{37}
\]

By (20), every recipient has an `S`-free core outside `C`. Under the child-distortion bound (13),

\[
\eta_T(E_{\rm out}(S,C,T))
\le
\sum_{m\in C_{\rm out}(S,C,T)}\eta_T^+(m)
\le
\frac{K_{S,T}|C_{\rm out}(S,C,T)|}{|V_T|}.
\tag{38}
\]

Since the left side is `L_(S,C,T)/|V_T|`, (12) gives (14). In particular, if

\[
h_{S,T}\ge h_0>0,
\qquad
P_{S,T}\le P_0,
\qquad
K_{S,T}\le K_0<\infty,
\tag{39}
\]

then any family for which `bar f_(S,C)(T)->infinity` forces

\[
\frac{|C_{\rm out}(S,C,T)|}{|C|}
\longrightarrow\infty.
\tag{40}
\]

The truncated packet cannot send its required boundary through only `O(1)` recipient vertices per occupied auxiliary core.

This still does **not** prove independent source-information growth. Many recipient vertices may share a structured outside core vocabulary, exactly as warned in FD-157/FD-158. What is new is that the ceiling itself no longer provides a generic way around the cut obstruction: it can help only by making the average primary fiber genuinely thin.

## 5. What sparse-support escape remains

FD-158 left two closely related possibilities open: ceiling-truncated support and deliberately sparse support. Equation (11) closes the first for every divisor-downward truncation and separates it cleanly from the second.

A genuinely sparse support can evade the proof only by having **holes below occupied auxiliary cores**. If `C` is not divisor-downward, then an incoming parent may carry an `S`-prime while landing in a missing lower core state; the contradiction in (17)-(18) disappears. Such holes create additional incoming boundary channels and can pay part of the Cheeger pressure without being charged to the anchor budget `P_(S,T)`.

This identifies a sharper next invariant: for arbitrary auxiliary support `A`, charge its failure of divisor closure by a **downward-hole boundary or shadow deficit**, and ask whether

\[
\text{parent budget}
+
\text{hole budget}
+
\text{outer-core leakage}
\tag{41}
\]

must still dominate the occupied primary-fiber mass. If so, the remaining sparse-support escape would have to pay explicitly for every missing lower core rather than hiding behind the truncation ceiling.

The result is therefore a truncated-support obstruction, not yet a complete arbitrary-sparse-support theorem and not an information lower bound.

## 6. Stress tests

Take `S={2,3}`, `U={5,7}`, and `T=30`. The full product `2*3*5*7=210` is far above the ceiling, so FD-158 cannot be applied. Here

\[
C_U(30)=\{1,5,7\},
\tag{42}
\]

while the core `35` is inactive. The occupied fibers have sizes

\[
f(1)=3,
\qquad
f(5)=3,
\qquad
f(7)=2,
\tag{43}
\]

corresponding to

\[
B_{S\mid C_U(30)}(30)
=
\{2,3,6,10,15,30,14,21\}.
\tag{44}
\]

Thus `M=8`, `|C|=3`, and (11) gives

\[
\boxed{
P_{S,30}+\frac13L_{S,C,30}
\ge
\frac83h_{S,30}.
}
\tag{45}
\]

The factor `8/3` is exactly the average number of surviving primary states per active core. The absent high core `35` simply disappears from both the packet mass and the incoming-anchor budget; it does not create a free dilution factor.

At the opposite extreme, if a core `c` lies so close to the ceiling that only `p_*c<=T` fits, then `f(c)=1`. Such a core really does contribute only one unit of Cheeger pressure per available anchor. This confirms that (11) responds to truncation in the correct direction: it does not pretend that the missing Boolean states still exist.

## 7. Prior-art audit and next pressure point

A post-candidate search checked classical Boolean-lattice shadow and down-set literature, including Kruskal-Katona-type shadow minimization and work on downsets. Those results are natural neighboring language for (20) and for the proposed hole-deficit continuation, but no external theorem is used in (11): the proof is the direct divisor-down-set boundary decomposition (21) plus the anchored Cheeger and distortion framework already internal to FD-157/FD-158. No new source is load-bearing, so no source anchor is added.

The next pressure point is now narrower than FD-158's: **non-downward sparse auxiliary support**. A useful continuation would replace the exact closure (4) by a quantitative defect and determine whether incoming traffic through missing lower cores can ever be large enough, under bounded distortion, to neutralize the average-fiber pressure without recreating an equally expensive shadow elsewhere.

### Retrieval notes

- Internal inputs: FD-157, FD-158, the current `farey_discrepancy` line synthesis, and the live clues for this line.
- Unresolved adversarial-review sidecars were checked before starting new research; none had precedence in this pass.
- Prior-art search was performed only after the truncated-down-set candidate was derived; no external result is used in the proof.
- `SOURCES.md`, clues, and `mind/**` are unchanged because this pass introduces no new load-bearing external source and causes no genuine clue-state transition.
