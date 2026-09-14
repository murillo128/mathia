# FD-116 — fixed rational anchor horizon dynamics is a periodic Möbius transform

**Status:** `LITERATURE+EXACT-DERIVED + REPRESENTATION-CLASSIFICATION + FIXED-ENDPOINT-HORIZON-COLLAPSE + NEGATIVE/ROUTE-RESTRICTION`.

`FD-115` leaves the absolute discrepancy anchor `D_Q(A)` as the only discrepancy coordinate inside one Farey parent cone that is not reconstructed from the local refinement movie. Its cross-horizon evolution is therefore a natural surviving candidate for `CLUE-ordered-plucker-refinement-transfer.md`.

For a **fixed reduced rational endpoint**

\[
A=\frac ab,
\qquad 0<a<b,
\qquad (a,b)=1,
\tag{1}
\]

that escape is already completely classified by the denominator-shell/Möbius source of `FD-001`. With

\[
D_Q(x)=I_Q(x)-C_Qx,
\qquad
C_Q=\sum_{q=2}^Q\varphi(q),
\tag{2}
\]

and exact-denominator shell discrepancy `e_q` as in `FD-001`, one has

\[
\boxed{D_Q(A)-D_{Q-1}(A)=e_Q(A).}
\tag{3}
\]

Define the elementary rational sawtooth

\[
f_A(m):=\left\lfloor\frac{am}{b}\right\rfloor-\frac{am}{b}
=-\left\{\frac{am}{b}\right\}.
\tag{4}
\]

Then the exact shell identity of `FD-001` gives, for every `q>=2`,

\[
\boxed{
e_q(A)
=\sum_{m\mid q}\mu(q/m)f_A(m).
}
\tag{5}
\]

The crucial representation point is that `f_A` is `b`-periodic. Moreover

\[
\frac1b\sum_{m=1}^b f_A(m)
=-\frac{b-1}{2b},
\tag{6}
\]

because multiplication by `a` permutes the residue classes modulo `b`. Hence, after centering

\[
g_A(m):=f_A(m)+\frac{b-1}{2b},
\tag{7}
\]

`g_A` is a zero-mean `b`-periodic sequence, and for every `q>1`

\[
\boxed{
e_q(A)
=\sum_{m\mid q}\mu(q/m)g_A(m),
}
\tag{8}
\]

since `sum_(m|q) mu(q/m)=0`. Thus **the entire cross-horizon increment path of a fixed rational discrepancy anchor is the Möbius convolution of one finite periodic table**. No additional Farey-refinement state is created by retaining that anchor through time.

Summing (5) also gives the exact cumulative form

\[
\boxed{
D_Q(A)
=A+
\sum_{m\le Q}
 f_A(m)
 M\!\left(\left\lfloor\frac Qm\right\rfloor\right),
}
\tag{9}
\]

where `M` is the Mertens function. The additive `A` is only the `q=1` correction induced by the interior-Farey convention. Equation (9) makes the boundary explicit: a fixed rational anchor can still carry difficult Möbius cancellation, but it does not provide an arithmetic source independent of the existing denominator-shell/Mertens frame.

The same conclusion survives any **fixed finite family** of rational anchors. If `A_j=a_j/b_j`, `1<=j<=k`, and `B=lcm(b_1,...,b_k)`, then the vector

\[
\mathbf g(m)
=
\bigl(g_{A_1}(m),\ldots,g_{A_k}(m)\bigr)
\tag{10}
\]

is `B`-periodic and

\[
\boxed{
\bigl(
D_q(A_j)-D_{q-1}(A_j)
\bigr)_{j=1}^k
=
\sum_{m\mid q}\mu(q/m)\mathbf g(m).
}
\tag{11}
\]

Therefore adding finitely many fixed absolute anchors, or exteriorizing them into a larger Plücker vector, can increase ambient dimension without supplying a new source channel. A nonlinear or antisymmetric statistic of those anchor paths may still be useful if it proves a stronger estimate for this Möbius-filtered object, but its information is not independent Farey geometry.

## 1. Exact derivation

Partitioning the interior Farey sequence by exact denominator gives

\[
D_Q(x)=\sum_{q=2}^Qe_q(x).
\tag{12}
\]

Taking the difference between consecutive horizons immediately proves (3). The exact sawtooth identity from `FD-001` is

\[
e_q(x)
=\sum_{m\mid q}\mu(q/m)
\bigl(\lfloor mx\rfloor-mx\bigr),
\tag{13}
\]

so substituting `x=a/b` proves (5).

Periodicity is exact:

\[
\begin{aligned}
f_A(m+b)
&=\left\lfloor\frac{a(m+b)}b\right\rfloor
  -\frac{a(m+b)}b\\
&=\left\lfloor\frac{am}b\right\rfloor+a
  -\frac{am}b-a\\
&=f_A(m).
\end{aligned}
\tag{14}
\]

For `m=1,...,b`, the residues `am mod b` are a permutation of `0,...,b-1`; therefore

\[
\sum_{m=1}^b f_A(m)
=-\frac1b\sum_{r=0}^{b-1}r
=-\frac{b-1}{2},
\tag{15}
\]

which proves (6)--(8).

For the cumulative identity, include temporarily the formal `q=1` shell from (13). Since `0<A<1`,

\[
e_1(A)=f_A(1)=-A.
\tag{16}
\]

Interchanging the finite divisor sums gives

\[
\begin{aligned}
\sum_{q\le Q}e_q(A)
&=
\sum_{q\le Q}
\sum_{m\mid q}\mu(q/m)f_A(m)\\
&=
\sum_{m\le Q}f_A(m)
\sum_{r\le Q/m}\mu(r)\\
&=
\sum_{m\le Q}f_A(m)
M\!\left(\left\lfloor\frac Qm\right\rfloor\right).
\end{aligned}
\tag{17}
\]

Removing `e_1(A)=-A` recovers (9). Applying (8) coordinatewise proves the finite-family statement (11).

## 2. Representation preflight and what is actually killed

The source object in this test is the exact-denominator shell family `{e_q}` already classified in `FD-001`. The candidate new observable is the absolute common-mode anchor left open by `FD-115`, sampled over varying Farey horizon while the rational endpoint is held fixed. Endpoint jump convention and the deterministic `q=1` term are nuisance bookkeeping; neither affects horizon increments for `q>=2`.

Under those controls the reconstruction test is decisive. Equation (3) reconstructs the anchor path from shell evaluations, (5) reconstructs each evaluation from the same Möbius/sawtooth source, and rationality reduces the sawtooth input to one finite periodic table. Thus fixed-endpoint cross-horizon anchoring does not pass the information-independence gate.

This is a representation classification, not a smallness theorem. The sequence in (9) can remain arithmetically difficult because it contains Mertens cancellation. Nor does the classification show that every functional of a fixed anchor path is useless: a genuinely stronger estimate for the same Möbius-filtered quantity would still be progress. What is ruled out is the claim that simply retaining one or finitely many **fixed rational** absolute anchors introduces a new Farey-specific source coordinate beyond the denominator-shell/Möbius channel.

## 3. Stress tests and boundaries

The symmetric point `A=1/2` is an exact degenerate control. In that case the convolution in (8) gives

\[
e_2(1/2)=\frac12,
\qquad
e_q(1/2)=0\quad(q\ge3),
\tag{18}
\]

so

\[
D_Q(1/2)=\frac12\qquad(Q\ge2).
\tag{19}
\]

This confirms that an apparently global absolute anchor can in fact become completely stationary after one shell.

The opposite control is also important. For endpoints such as `A=1/3`, the shell increments remain nontrivial at arbitrarily many horizons; the theorem does **not** claim eventual constancy or bounded support in general. It classifies their source as periodic-kernel Möbius convolution.

A direct exact rational-arithmetic check over every reduced `a/b` with `2<=b<=12` and every `b<=Q<=50` verified (3), (5), (6), and (9) in 1,921 endpoint/horizon instances. The computation is only a regression check; the proof is the finite algebra above.

The main boundary is that `b` is fixed. If the selected anchor moves with the horizon, `A=A_Q`, or its denominator grows with `Q`, then the periodic kernel itself changes and its state dimension need not remain bounded. Likewise a number of anchors growing with `Q`, or a selection rule that chooses anchors from global discrepancy information, is not reduced by the fixed-family statement (11). Those are genuine surviving versions of the cross-horizon/common-mode route.

## 4. Prior-art boundary and consequence for the live clue

The underlying formulas are not new. García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, DOI `10.3390/math13010140`, derives exact Möbius- and Mertens-based formulas for the local discrepancy at a Farey fraction `h/k`, explicitly including periodic residue-class structure. `FD-001` already derives the denominator-shell sawtooth identity (13) and its cumulative Mertens collapse. No novelty is claimed for Möbius inversion, the periodicity of a rational sawtooth, or rational-point Farey rank formulas.

The Mathia-specific durable delta is the splice with the live representation frontier after `FD-115`: **the simplest surviving common-mode escape, namely following a fixed absolute rational anchor through many horizons, is already inside the known shell/Mertens source.** The same is true for any fixed finite collection of such anchors.

Consequently `CLUE-ordered-plucker-refinement-transfer.md` remains only `proposed`. A viable discrepancy/common-mode coordinate must now use a moving or growing-denominator anchor, a family whose size grows with the horizon, a genuinely global cross-cone/cross-horizon selection law, or another source-conditioned quantity not reconstructible from fixed periodic Möbius filters. Re-embedding finitely many fixed anchor paths into a higher-dimensional exterior representation does not by itself clear the algebraic gate.

No stronger Franel--Landau estimate, Mertens bound, or RH consequence is obtained here. All load-bearing mathematics is derived from the canonical shell identity already stored in `FD-001`; García (2025), already anchored in `SOURCES.md`, is the prior-art boundary rather than a new dependency.