# FD-101 — one-shell exactification makes tagged nonhead source descent impossible

**Status:** `EXACT-DERIVED + ONE-SHELL-SOURCE-RIGIDITY + ROUNDING-NONACCUMULATION + TAGGED-CARRIER-GENEALOGY + SOURCE-DESCENT-HEAD-ONLY + PACKET-SWITCHING-FRONTIER`.

`FD-100` proves that on an exact carrier `H=rX`, every currently available source-neutral nonhead repair spends at least one unit of the binary row potential `log_2(r/4)` while preserving the sampled source `X` exactly. Its explicit boundary is that the real predecessor argument does not generally start from exact divisibility: the canonical compression uses ceilings and floors, so it was still possible that repeated rounding could drift the sampled source through many adjacent quotient shells before the row potential was exhausted.

It cannot. For every tagged nonsquarefree coordinate, the first canonical prime compression changes the physical source quotient by either zero or **exactly one upward shell**. If the `+1` case occurs, the destination becomes an exact carrier automatically. From that point onward `FD-100` applies and the source quotient can never change again under nonhead repairs. Hence along an arbitrary tagged nonhead genealogy the sampled source is constant, except possibly for one single `+1` transition. Rounding errors do not accumulate with depth.

Combined with the strict row-potential drain of `FD-100`, every tagged nonhead genealogy reaches the four-adic head after finitely many repairs with head source equal to either the original source quotient or that quotient plus one. Thus **none of the currently proved nonhead predecessor mechanisms can create genuine source descent along a fixed carrier lineage**. The remaining packet-level escape is narrower than before: either a source-moving head step is taken, or the adaptive energy argument must retag onto a different coordinate genealogy. The live amortized theorem should therefore charge carrier retagging, not generic floor/ceiling drift.

## 1. A universal first-compression lemma

Let `H>=1`, let `r>=4` be a nonsquarefree row, and let `p` be the repeated-prime label used by the canonical predecessor construction, so

\[
p^2\mid r.
\]

Put

\[
A:=\left\lceil\frac Hp\right\rceil,
\qquad
s:=\frac rp,
\qquad
x:=\left\lfloor\frac Hr\right\rfloor,
\qquad
y:=\left\lfloor\frac As\right\rfloor.
\tag{1}
\]

Because `r=ps`, the inequalities defining `x` are

\[
psx\le H<ps(x+1).
\tag{2}
\]

Dividing by `p` and taking ceilings gives

\[
sx\le A\le s(x+1).
\tag{3}
\]

Therefore

\[
\boxed{y\in\{x,x+1\}.}
\tag{4}
\]

There is a stronger rigidity in the upper case. If `y=x+1`, then (3) and the definition of the floor force

\[
A=s(x+1).
\tag{5}
\]

So whenever the source quotient changes at all, the first-deflated coordinate becomes an **exact carrier**. Equivalently,

\[
\boxed{
y=x+1\quad\Longrightarrow\quad A=sy.}
\tag{6}
\]

This is an integer identity. It uses no asymptotics, no false-RH hypothesis, no Mertens estimate, and no energy inequality.

## 2. Every secondary repair preserves that quotient, including exactification

The nonhead mechanisms of `FD-091` and `FD-093` begin with the compression in (1) and then either stop or apply an exact reembedding. In all cases the final destination has physical source quotient exactly `y`.

For an odd repeated prime write

\[
r=p^2t,
\qquad s=pt.
\]

The repaired state is

\[
B:=\left\lfloor\frac Ap\right\rfloor,
\qquad
C:=4B,
\qquad
u:=4t.
\tag{7}
\]

Floor composition gives

\[
\left\lfloor\frac C\nu\right\rfloor
=
\left\lfloor\frac Bt\right\rfloor
=
\left\lfloor\frac A{pt}\right\rfloor
=y.
\tag{8}
\]

If the first compression jumped, (6) gives `A=pty`; hence `B=ty` and therefore

\[
\boxed{C=\nu y.}
\tag{9}
\]

Thus the full odd-prime repair is itself an exact carrier whenever the source shell increased.

For the already-eligible dyadic branch, the destination is simply `(A,s)`, so (4) applies directly and (6) already proves exactification in the `+1` case.

For the dyadic terminal nonhead branch, write

\[
r=4m,
\qquad s=2m,
\qquad m>1\text{ odd and squarefree},
\]

and let `q` be the deterministic odd prime used in the repair, `m=qt`. Put

\[
B:=\left\lfloor\frac A2\right\rfloor,
\qquad
C:=4\left\lfloor\frac Bq\right\rfloor,
\qquad
\nu:=4t.
\tag{10}
\]

The exact identities from `FD-093` give

\[
\left\lfloor\frac C\nu\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor
=
\left\lfloor\frac A{2m}\right\rfloor
=y.
\tag{11}
\]

If `y=x+1`, then `A=2my`, so `B=my`, `floor(B/q)=ty`, and again

\[
\boxed{C=\nu y.}
\tag{12}
\]

Hence all three currently available nonhead branches obey the same rule: the destination source is `x` or `x+1`; if it is `x+1`, the destination is exactly divisible by its repaired row.

## 3. The `+1` correction can happen at most once in an entire tagged genealogy

Consider a tagged genealogy of physical coordinates

\[
(H_0,r_0),(H_1,r_1),\ldots
\]

in which each transition follows the canonical nonhead repair associated with the tagged row. Define

\[
x_j:=\left\lfloor\frac{H_j}{r_j}\right\rfloor.
\tag{13}
\]

Sections 1--2 imply

\[
x_{j+1}\in\{x_j,x_j+1\}.
\tag{14}
\]

If the second alternative ever occurs, the child satisfies

\[
H_{j+1}=r_{j+1}x_{j+1}.
\tag{15}
\]

But an exact carrier is precisely the setting of `FD-100`: every subsequent nonhead repair preserves its source quotient exactly. Therefore no second jump is possible. We obtain the global one-shell law

\[
\boxed{
 x_j\in\{x_0,x_0+1\}\quad\text{for every }j,
\qquad
\#\{j:x_{j+1}\ne x_j\}\le1.
}
\tag{16}
\]

This is substantially stronger than the naive per-step estimate `x_{j+1}=x_j+O(1)`, which would permit an accumulated `O(depth)` source drift. The canonical ceiling error has a self-terminating structure: the first time it is large enough to cross a quotient shell, it lands exactly on that shell boundary and removes all future rounding ambiguity.

## 4. Row-potential exhaustion therefore reaches the head in the same source shell

The row maps are the same as in `FD-100`, independently of whether the horizon is an exact multiple of the row:

\[
r'=\frac{4r}{p^2}\le\frac49r
\quad(p\ge3),
\]

\[
r'=\frac r2
\quad\text{for the eligible dyadic branch},
\]

and

\[
r'=\frac rq\le\frac r3
\quad\text{for the dyadic terminal nonhead repair}.
\tag{17}
\]

Thus every nonhead step satisfies `4<=r'<=r/2`. The binary potential

\[
\mathfrak I(r):=\log_2(r/4)
\tag{18}
\]

still drops by at least one, so a tagged genealogy reaches row `4` after at most

\[
\boxed{
k\le\left\lceil\log_2(r_0/4)\right\rceil}
\tag{19}
\]

nonhead repairs.

Let `(H_*,4)` be that terminal state and put `x_*=floor(H_*/4)`. By (16),

\[
x_*\in\{x_0,x_0+1\}.
\tag{20}
\]

The subsequent dyadic head exposure uses

\[
A_*:=\left\lceil\frac{H_*}{2}\right\rceil,
\qquad
B_*:=\left\lfloor\frac{A_*}{2}\right\rfloor.
\tag{21}
\]

Applying the same first-compression lemma to row `4` shows that

\[
\boxed{B_*\in\{x_0,x_0+1\}.}
\tag{22}
\]

Indeed, if a `+1` jump had already occurred earlier then `(H_*,4)` is exact and `B_*=x_*`; if none occurred earlier, the final head exposure is the only remaining place where the one-shell correction can occur.

Consequently an arbitrary tagged carrier from the actual, non-divisible physical state reaches the source-head obstruction at essentially the **same discrete source argument**, with an absolute error at most one. The exact-carrier hypothesis of `FD-100` is not needed to prevent cumulative source drift.

## 5. On the frontier core the one-shell error is asymptotically invisible

In the `FD-088`--`FD-093` block construction the tagged parent rows lie in the core

\[
r_0\le R_H
=\left\lfloor\frac{H}{L_H+1}\right\rfloor,
\qquad
L_H=H^{\Theta-\delta+o(1)}.
\tag{23}
\]

Hence their initial physical source arguments satisfy

\[
x_0=\left\lfloor\frac H{r_0}\right\rfloor
\ge L_H.
\tag{24}
\]

The terminal head source therefore obeys

\[
\boxed{
B_*=x_0+O(1)
=x_0\bigl(1+O(L_H^{-1})\bigr).
}
\tag{25}
\]

So even on the real stitched packet, not merely on the matched exact carriers of `FD-099`--`FD-100`, a fixed tagged nonhead genealogy cannot use floor/ceiling effects to migrate to a genuinely smaller source scale. At frontier scales the only allowed rounding change is negligible even additively compared with the source magnitude.

This does **not** prove that a positive fraction of the packet energy follows one tagged genealogy. The adaptive predecessor theorem can reselect a different row after each step. Equation (25) instead removes one possible explanation for such reselection: accumulated quotient-shell rounding is not a source of fresh carrier inventory.

## 6. Sharpness controls

The `+1` alternative is real, so (16) cannot be strengthened to exact invariance for arbitrary starting horizons. The smallest dyadic example is

\[
(H,r)=(15,8).
\]

Here `x=floor(15/8)=1`, while

\[
A=\left\lceil\frac{15}{2}\right\rceil=8,
\qquad s=4,
\qquad
\left\lfloor\frac As\right\rfloor=2.
\]

The source jumps from `1` to `2`, but the destination is immediately exact: `8=4\cdot2`. No later nonhead repair can change source `2`.

An odd-prime example is `(H,r)=(17,9)`. With `p=3`,

\[
A=6,
\qquad s=3,
\qquad y=2=x+1,
\]

and the four-adic repair gives `(C,\nu)=(8,4)=4\cdot2`. Again the jump exactifies the carrier.

Conversely `(H,r)=(14,8)` has no nonhead jump: the half-scale destination is `(7,4)` with source `1`. Its final head exposure moves to source `2`. This shows why the head exposure must be included when stating the final one-shell bound (22), but it still produces only the same single upward correction rather than a cumulative drift.

A finite exhaustive check over thousands of integer horizons and nonsquarefree rows was also used as an adversarial sanity test of the branch formulas before canonicalization; no violation of (4), exactification after a jump, or the row contraction in (17) appeared. The proof above is exact and does not depend on that computation.

## 7. Prior-art boundary and research consequence

A targeted literature audit rechecked classical Farey--Mertens discrepancy formulas and recent recursive formulas for local Farey discrepancy, including the 2025 work of Rogelio Tomás García. Those sources organize Farey ranks and local discrepancy through Möbius/Mertens floor sums, but no located result states the Mathia-specific canonical repeated-prime compression together with the one-shell exactification property above. No external theorem is load-bearing: the result is elementary integer arithmetic applied to the already-canonical predecessor maps of `FD-091` and `FD-093`. `SOURCES.md` therefore requires no update.

The live frontier after `FD-100` is correspondingly narrower. **Tagged nonhead ancestry cannot cause source descent and cannot replenish its source-neutral inventory through accumulated rounding.** Each tagged lineage spends the finite row potential and arrives at the four-adic head in the same source shell, up to one exactifying `+1` correction.

Therefore a packet-level amortized theorem no longer needs to budget `O(depth)` quotient-shell uncertainty. Its unresolved escape is structural: the energy selection may abandon one tagged genealogy and retag onto another row whose source quotient is different. A useful next invariant should couple projective quality and row-potential inventory while charging such **carrier switches** explicitly. If enough energy must remain genealogically coherent, `FD-101` and `FD-100` force it to the head without source loss; if not, the failure itself must exhibit repeated source-scale retagging that can be quantified separately.