# FD-165 — Polylogarithmically many Farey horizons still leave dense orientations undetermined

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact matched-control obstruction / growing cross-horizon information boundary / source-bridge test
- **Depends on:** FD-009, FD-117, FD-163, FD-164
- **Classification:** `LITERATURE+EXACT-DERIVED + MATCHED-SQUAREFREE-UNIT-CONTROL + NEGATIVE/INFORMATION-BRIDGE`

## Claim

`FD-164` proves that one complete Farey discrepancy field does not determine the Möbius orientations on any positive-density squarefree family. The construction there uses finitely many macroscopic quotient shells and explicitly leaves open a growing bundle of horizons.

The same ambiguity survives **any polylogarithmically large family of arbitrary horizons**. The relevant resource is not the number of Farey samples inside each field — `FD-117` already compresses one full field to its floor-quotient staircase — but the total number of distinct high source breakpoints contributed by the horizon family.

Let

\[
\mathcal H_T\subseteq\{1,\ldots,T\},
\qquad
J_T:=|\mathcal H_T|,
\tag{1}
\]

be any horizon family, allowed to depend arbitrarily on `T`, and for `H in mathcal H_T` put

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\}.
\tag{2}
\]

Fix `0<beta<1`, define

\[
r_0:=\lfloor\beta T\rfloor,
\qquad
\mathcal R_T:=\bigcup_{H\in\mathcal H_T}\mathcal Q_H,
\tag{3}
\]

and let

\[
\mathfrak M_\beta(T)
:=
\max_{r_0\le x\le T}|M(x)|.
\tag{4}
\]

There is a coefficient source

\[
a_T:\{1,\ldots,T\}\to\{-1,0,+1\}
\tag{5}
\]

with

\[
a_T(1)=1,
\qquad
a_T(n)=0\iff\mu(n)=0,
\qquad |a_T(n)|=1\quad(\mu^2(n)=1),
\tag{6}
\]

such that, with

\[
A_T(x):=\sum_{n\le x}a_T(n),
\tag{7}
\]

one has the simultaneous exact match

\[
\boxed{
A_T(r)=M(r)
\qquad
\text{for every }r\in\mathcal R_T.
}
\tag{8}
\]

Moreover the source can be chosen so that

\[
\boxed{
\frac{
\#\{n\le T:\mu^2(n)=1,\ a_T(n)\ne\mu(n)\}
}{Q_{\rm sf}(T)}
\ge
1-\beta
-O_\beta\!\left(
\frac{J_T\mathfrak M_\beta(T)}{T}
\right)
-o_\beta(1).
}
\tag{9}
\]

Here `Q_sf(x)=#\{n<=x:mu^2(n)=1\}`. Therefore the unconditional Davenport estimate already recorded in `SOURCES.md`,

\[
M(x)\ll_A \frac{x}{(\log x)^A}
\qquad\text{for every fixed }A>0,
\tag{10}
\]

implies the following growing-horizon corollary. For every fixed `B>=0` and every family satisfying

\[
J_T\ll (\log T)^B,
\tag{11}
\]

there is one squarefree-unit source `a_T`, common to **all** horizons in `mathcal H_T`, for which

\[
\boxed{
A_T(r)=M(r)
\quad(r\in\mathcal R_T),
\qquad
\frac{\#\{n\in V_T:a_T(n)\ne\mu(n)\}}{|V_T|}
\ge1-\beta-o_{\beta,B}(1).
}
\tag{12}
\]

Since `beta` may be chosen as any fixed positive constant before `T->infinity`, a polylogarithmic bundle of complete Farey fields can be matched exactly while changing an arbitrarily large asymptotic fraction of the squarefree orientations.

The localization from `FD-164` also survives. If `D_T subseteq V_T` satisfies

\[
\liminf_{T\to\infty}
\frac{|D_T|}{|V_T|}
\ge\delta>0,
\tag{13}
\]

then the flips may be selected so that

\[
\boxed{
\frac{\#\{n\in D_T:a_T(n)\ne\mu(n)\}}{|D_T|}
\ge
1-
\frac{\beta}{\delta}
-O_{\beta,\delta}\!\left(
\frac{J_T\mathfrak M_\beta(T)}{T}
\right)
-o_{\beta,\delta}(1).
}
\tag{14}
\]

Thus under (11), for every fixed `epsilon>0` one may choose `beta<delta epsilon/2` and alter at least a `1-epsilon` fraction of `D_T` for all sufficiently large `T`, while every complete Farey field in the prescribed polylogarithmic horizon family remains exactly unchanged through the `FD-117` source map.

In particular, the positive-density prime-avoidance anchor face forced by the bounded-resource hypotheses of `FD-163` is **not oriented by adding only polylogarithmically many arbitrary Farey horizons**. The live source bridge is narrower than `FD-164` left it: it must use a denser cross-horizon hierarchy, multiplicative/divisor coherence not reducible to these sampled fields, or another specifically Möbius law.

## 1. One horizon contributes only boundedly many breakpoints above a fixed fraction of `T`

For a horizon `H<=T`, suppose

\[
r=\left\lfloor\frac Hm\right\rfloor>\beta T.
\tag{15}
\]

Then

\[
\frac Hm>\beta T,
\qquad
m<\frac{H}{\beta T}\le\frac1\beta.
\tag{16}
\]

Hence the number of floor quotients of `H` lying above `beta T` is at most a constant depending only on `beta`. In particular,

\[
\#\bigl(\mathcal R_T\cap(r_0,T]\bigr)
\le
\left\lceil\frac1\beta\right\rceil J_T.
\tag{17}
\]

Adjoin `T` if it is not already present, order the resulting breakpoints as

\[
r_0<r_1<\cdots<r_L=T,
\tag{18}
\]

and set

\[
I_\ell:=(r_{\ell-1},r_\ell]\cap\mathbb Z.
\tag{19}
\]

Then

\[
L\le 1+\left\lceil\frac1\beta\right\rceil J_T.
\tag{20}
\]

This is the entire cross-horizon combinatorial input. A complete field at one horizon contains many point values and Fourier coordinates, but after `FD-117` they constrain the source only at `mathcal Q_H`; above a fixed macroscopic cutoff, that set has bounded cardinality.

## 2. Balanced squarefree-unit flips kill every sampled breakpoint simultaneously

Set

\[
a_T(n)=\mu(n)
\qquad(n\le r_0).
\tag{21}
\]

For each block `I_l`, split its squarefree integers by physical Möbius sign,

\[
P_\ell:=\{n\in I_\ell:\mu(n)=+1\},
\qquad
N_\ell:=\{n\in I_\ell:\mu(n)=-1\},
\tag{22}
\]

and put

\[
m_\ell:=\min(|P_\ell|,|N_\ell|).
\tag{23}
\]

Choose subsets

\[
P'_\ell\subseteq P_\ell,
\qquad
N'_\ell\subseteq N_\ell,
\qquad
|P'_\ell|=|N'_\ell|=m_\ell,
\tag{24}
\]

and flip the Möbius sign on their union. Nonsquarefree coefficients remain zero. Therefore the total source change over each complete block is exactly

\[
\sum_{n\in I_\ell}(a_T(n)-\mu(n))
=-2|P'_\ell|+2|N'_\ell|=0.
\tag{25}
\]

Starting from the exact match at `r_0`, equation (25) gives

\[
A_T(r_\ell)=M(r_\ell)
\qquad(1\le\ell\le L).
\tag{26}
\]

Every element of `mathcal R_T` is either at most `r_0`, where the source was not changed, or is one of the breakpoints in (18). This proves (8).

The same finite source works for the whole horizon family. To make the Farey implication explicit, for any cumulative source `A` define, as in `FD-164`,

\[
\mathcal D_{H,A}(x)
:=
x-\lfloor x\rfloor
+
\sum_{m\le H}
(\lfloor mx\rfloor-mx)
A\!\left(\left\lfloor\frac Hm\right\rfloor\right).
\tag{27}
\]

For the physical source `A=M`, `FD-117` identifies (27) with the actual Farey discrepancy field `D_H`. Since every argument in (27) belongs to `mathcal Q_H subseteq mathcal R_T`, equation (8) gives the simultaneous pointwise identities

\[
\boxed{
\mathcal D_{H,A_T}(x)=D_H(x)
\qquad
(H\in\mathcal H_T,\ 0\le x\le1).
}
\tag{28}
\]

Thus the matched control is invisible to **every complete discrepancy field in the chosen horizon bundle**, not merely to one scalar statistic per horizon.

## 3. A quantitative horizon-budget law

The number of flipped coefficients in one block is

\[
2m_\ell
=
|P_\ell|+|N_\ell|
-
\bigl||P_\ell|-|N_\ell|\bigr|.
\tag{29}
\]

The first two terms count its squarefree integers, while

\[
|P_\ell|-|N_\ell|
=
M(r_\ell)-M(r_{\ell-1}).
\tag{30}
\]

Hence the total number `C_T` of changed squarefree coefficients has the exact finite formula

\[
\boxed{
C_T
=
Q_{\rm sf}(T)-Q_{\rm sf}(r_0)
-
\sum_{\ell=1}^{L}
|M(r_\ell)-M(r_{\ell-1})|.
}
\tag{31}
\]

Using (4) and (20),

\[
\sum_{\ell=1}^{L}
|M(r_\ell)-M(r_{\ell-1})|
\le
2L\mathfrak M_\beta(T)
\ll_\beta
(1+J_T)\mathfrak M_\beta(T).
\tag{32}
\]

The elementary squarefree asymptotic

\[
Q_{\rm sf}(x)=\frac{x}{\zeta(2)}+O(\sqrt x)
\tag{33}
\]

then turns (31) into (9). In particular, the general sufficient condition for dense ambiguity is

\[
\boxed{
J_T\mathfrak M_\beta(T)=o(T).
}
\tag{34}
\]

This isolates the actual resource threshold supplied by the proof. No specific growth law for `J_T` is needed until one inserts arithmetic information about `M`.

For the physical Möbius source, Davenport's unconditional log-power cancellation gives, uniformly for `x in [beta T,T]`,

\[
\mathfrak M_\beta(T)
\ll_{A,\beta}
\frac{T}{(\log T)^A}
\tag{35}
\]

for every fixed `A`. If `J_T<<log^B T`, choose any `A>B`; then (34) follows. This proves (12).

The role of Davenport is limited and transparent. Exact cross-horizon invisibility, equations (8), (28), and (31), are finite combinatorics. The analytic input is used only to show that the sign imbalance left unflipped across a growing number of macroscopic blocks is still negligible compared with the squarefree population.

## 4. Every positive-density exposed family remains ambiguous

The subsets in (24) can be chosen to maximize flips inside any prescribed `D_T subseteq V_T` without changing their cardinalities. In each block, flip all coefficients from the minority Möbius sign and choose the required equal number from the majority sign so as to include as many elements of `D_T` as possible.

If `|P_l|>=|N_l|`, all of `N_l` is flipped and at most

\[
|P_\ell|-|N_\ell|
\tag{36}
\]

members of `D_T cap P_l` can remain unflipped; the opposite case is identical. Consequently

\[
|D_T\setminus\{n:a_T(n)\ne\mu(n)\}|
\le
Q_{\rm sf}(r_0)
+
\sum_{\ell=1}^{L}
|M(r_\ell)-M(r_{\ell-1})|.
\tag{37}
\]

Combining (32), (33), and the positive-density hypothesis (13) proves (14).

Now impose the bounded-resource ancestry hypotheses of `FD-163`. That finding gives a constant `delta_0>0`, depending only on the architecture resource bounds, such that its prime-avoidance anchor face `D_(S,T)` satisfies

\[
|D_{S,T}|\ge(\delta_0-o(1))|V_T|.
\tag{38}
\]

Taking any fixed `0<delta<delta_0` in (14), and then choosing `beta` sufficiently small, shows that the orientation ambiguity persists on an arbitrarily large fraction of the geometrically exposed anchor even after adding any prescribed polylogarithmic family of complete Farey horizons.

This sharpens the ordering of obligations in the current ancestry route. Positive anchored expansion forces exposure; `FD-164` shows that one horizon does not orient it; the present result shows that **polylogarithmically many arbitrary horizons still do not orient it**. The source bridge must carry genuinely more coherence than a small bundle of exact Farey observations.

## 5. Adversarial boundaries and relation to exact recovery

The control `a_T` depends on `T` and on the chosen horizon family. The theorem produces one source common to all horizons in that finite bundle, but it does **not** construct a single infinite non-Möbius source that matches an unbounded nested sequence of such bundles. A proof may therefore still exploit consistency of one permanent source across arbitrarily many scales. `FD-126`, for example, studies a different common-source question on sparse repeated-square horizons; its conclusion concerns asymptotic Fourier-skeleton saturation rather than exact equality of complete Farey fields.

The result also does not conflict with `FD-009`. If one imposes the physical divisor identity at every consecutive horizon through a cutoff, the first discrete difference exposes the divisor sums and Möbius inversion recovers every source coefficient exactly. The two findings delimit opposite regimes:

\[
\text{polylogarithmically many arbitrary complete fields}
\quad\text{still have a dense orientation kernel,}
\tag{39}
\]

whereas

\[
\text{the full consecutive divisor-horizon hierarchy}
\quad\text{is lossless source recovery.}
\tag{40}
\]

Nothing here identifies a sharp threshold between those regimes. In particular, (34) is a sufficient ambiguity criterion coming from this block construction, not a necessary information lower bound.

Nor does the theorem impose multiplicativity on the control. It preserves exactly the Möbius zero set and the unit magnitude on every squarefree coefficient, but not the sign law `mu(mn)=mu(m)mu(n)` on coprime arguments. A multiplicative or divisor-coherent observation that is not already a function of the sampled Farey fields can therefore distinguish the control. This is precisely the type of source-specific information the current research line now needs.

Finally, the matched source is a control for the exact `FD-117` coefficient-to-Farey observation map, not the inclusion-exclusion law of a second realizable Farey point set. The conclusion is an information-boundary theorem: the observed complete fields do not by themselves certify the physical signs on the exposed coefficient surface. It is not a counterexample to the arithmetic Farey sequence and does not supply an RH estimate.

## 6. Prior art and representation audit

The external ingredients are classical and already anchored in `SOURCES.md`. Davenport supplies arbitrary fixed log-power cancellation for the Möbius summatory function; the squarefree counting asymptotic is elementary; and the Farey/Mertens transform is the exact local `FD-117` representation. Targeted searches also recover the expected neighboring floor-quotient literature, including the floor-quotient partial order of Lagarias--Richman and Mertens-matrix work, as well as classical Farey/Möbius formulas. Those objects study the quotient structure and its arithmetic transforms. No source located in the audit states the matched-control conclusion above: exact simultaneous preservation of a growing arbitrary family of complete Farey fields while changing asymptotically almost every squarefree orientation.

No novelty is claimed for floor-quotient counting, balanced sign swaps, Davenport cancellation, or squarefree density separately. The new line-local contribution is their combination into the quantitative horizon-budget law (34) and its consequence for the positive-density anchor forced by `FD-163`.

The representation split is explicit. The generic part is a cumulative-sampling kernel: zero-sum modifications inside intervals between observed cumulative breakpoints are invisible. The arithmetic part is the uniform Möbius cancellation that bounds the unflipped sign imbalance while the number of blocks grows. The Farey-specific part is `FD-117`, which says that an entire horizon field contributes no source coordinates beyond its floor-quotient breakpoints. The ancestry-specific consequence is inherited from `FD-163` through the positive-density localization (14).

No new external theorem is load-bearing beyond the current source anchors, so `SOURCES.md` remains unchanged. No local clue changes disposition: the result narrows the cross-horizon/source-law gate but does not resolve the accepted spectral-allocation or nonsquarefree-occupation questions.

### Retrieval notes

- Internal inputs: the current line mandate and synthesis, `FD-009`, `FD-117`, `FD-126`, `FD-163`, `FD-164`, current local clue dispositions, and existing Farey/floor-quotient/Davenport source anchors.
- No local adversarial-review sidecar had owner precedence when this investigation began.
- The finite multi-horizon block construction and quantitative budget (34) were derived before the external prior-art audit; the search was used to delimit novelty against classical Farey/Mertens and floor-quotient work.
- `SOURCES.md`, clues, `mind/**`, graph artifacts, code, and experiments are unchanged.
- No computation or formalization handoff is warranted: the decisive statement is an exact finite balance construction plus an already-anchored uniform asymptotic, while the surviving problem is the mathematical source-coherence bridge.
