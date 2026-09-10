# FD-016 — multiplicatively sparse horizons can jointly near-saturate GCD duality

**Status:** `EXACT-DERIVED + SPARSE-HORIZON-INTERPOLATION + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`. `FD-014` and `FD-015` show that coherence of one source sequence across nearby multiplicative horizons genuinely obstructs simultaneous saturation of the sharp square-GCD coordinate inequality. The remaining cumulative question is whether a growing but compressed set of coherent horizons can amplify that obstruction without reconstructing the source. There is a complementary limitation: if the sampled horizons are multiplicatively sparse enough, then the first finitely many equality-ray coordinates at each new horizon can be planted independently above all earlier horizons, while the already-fixed source values are pushed into a lower tail whose effect can be overwhelmed by scaling.

Consequently, **arbitrarily many coherent horizons do not by themselves force a nonvanishing saturation deficit.** More precisely, let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
C_R=(K_R^{-1})_{11}
=\sum_{r\le R}\frac{\mu(r)^2}{J_2(r)},
\qquad
Z=\zeta(2).
\]

Fix `R>=2`. Let

\[
H_0<H_1<H_2<\cdots
\]

be integer horizons such that

\[
H_j\ge R^2
\quad\text{and}\quad
\left\lfloor\frac{H_j}{R}\right\rfloor>H_{j-1}
\qquad(j\ge1).
\tag{1}
\]

For every `delta>0` there exists a **single real sequence** `A(1),A(2),...` such that, with

\[
m_d^{(H)}=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H=\frac{A(H)^2}{E_H},
\tag{2}
\]

one has

\[
\boxed{
R_{H_j}>C_R-\delta
\qquad\text{for every }j\ge0.
}
\tag{3}
\]

This is an interpolation theorem for the unrestricted real source class used in the `FD-014`/`FD-015` coherence tests. It does not assert that the constructed sequence is a Mertens function or even a partial-sum sequence with bounded increments.

A useful geometric corollary follows by taking an integer `Q>=3`, `R=Q-1`, and

\[
H_j=Q^jH_0,
\qquad H_0\ge(Q-1)^2.
\tag{4}
\]

Then for every `delta>0` one source sequence satisfies

\[
\boxed{
R_{Q^jH_0}>C_{Q-1}-\delta
\qquad(j\ge0).
}
\tag{5}
\]

Since `FD-003` gives

\[
0\le Z-C_{Q-1}\le\frac{Z}{Q-1},
\tag{6}
\]

any universal theorem based **only** on coherence of the unrestricted source along this `Q`-geometric chain that guarantees a deficit

\[
\inf_jR_{Q^jH_0}\le Z-g_Q
\tag{7}
\]

must satisfy

\[
\boxed{
g_Q\le Z-C_{Q-1}\le\frac{Z}{Q-1}.}
\tag{8}
\]

The same upper bound applies to any universal deficit asserted for every finite or asymptotic average of these chain ratios. Thus a compressed hierarchy whose multiplicative spacing itself grows cannot obtain a scale-independent gain merely by accumulating more horizons. A successful coherence mechanism must keep enough overlap between scales, or exploit arithmetic restrictions absent from the arbitrary-real-source relaxation.

## 1. The principal equality ray can be planted at a fresh horizon

Fix `R>=2` and write

\[
u:=K_R^{-1}e_1.
\tag{9}
\]

Then

\[
u_1=C_R,
\qquad
u^TK_Ru=C_R.
\tag{10}
\]

At any horizon `H>=R^2`, the integers

\[
x_d(H):=\left\lfloor\frac Hd\right\rfloor,
\qquad1\le d\le R,
\tag{11}
\]

are pairwise distinct. Indeed for `1<=d<R`,

\[
\frac Hd-\frac H{d+1}
=\frac{H}{d(d+1)}
\ge\frac{R^2}{R(R-1)}>1,
\]

so consecutive floors in (11) strictly decrease.

The top-left `R x R` principal block of `K_H` is exactly `K_R`, because the kernel `gcd(d,e)^2/(de)` does not depend on the ambient horizon. Hence if the first `R` staircase coordinates at `H` are set equal to `t u` and all remaining coordinates vanish, then

\[
E_H=t^2C_R,
\qquad
A(H)=tu_1=tC_R,
\]

and therefore

\[
R_H=C_R.
\tag{12}
\]

The point of the sparse-horizon condition (1) is that these `R` source locations can be made fresh at every stage.

## 2. Earlier horizons occupy only the lower tail of every later staircase

Construct `A` inductively. At `H_0`, assign

\[
A(x_d(H_0))=t_0u_d
\qquad(1\le d\le R)
\tag{13}
\]

for any nonzero `t_0`, and set every other `A(n)` with `n<=H_0` to zero. Since every tail sample with `d>R` is strictly below `x_R(H_0)`, equation (12) gives

\[
R_{H_0}=C_R.
\tag{14}
\]

Suppose now that all values `A(n)` through `H_{j-1}` have been fixed. By (1),

\[
x_R(H_j)>H_{j-1},
\]

so all `x_d(H_j)` for `1<=d<=R` are new source locations. Set all other still-unassigned values in `(H_{j-1},H_j]` to zero and prescribe

\[
A(x_d(H_j))=t_ju_d.
\tag{15}
\]

At horizon `H_j`, every staircase coordinate with `d>R` samples an integer below `x_R(H_j)`. Therefore the full horizon vector has the form

\[
\boxed{
m^{(H_j)}=t_j\widetilde u+b_j,}
\tag{16}
\]

where `widetilde u=(u_1,...,u_R,0,...,0)` and `b_j` has its first `R` coordinates exactly zero. Crucially, `b_j` is already fixed before `t_j` is chosen: it contains only values inherited from earlier stages or the zeros just assigned in the current lower tail.

Because the principal block is `K_R`,

\[
\widetilde u^TK_{H_j}\widetilde u=C_R.
\tag{17}
\]

Consequently

\[
E_{H_j}
=t_j^2C_R
+2t_j\,\widetilde u^TK_{H_j}b_j
+b_j^TK_{H_j}b_j,
\tag{18}
\]

while

\[
A(H_j)=t_ju_1=t_jC_R.
\tag{19}
\]

For each fixed stage `j`, the two coefficients involving `b_j` in (18) are finite and independent of `t_j`. Positive definiteness of `K_{H_j}` ensures the denominator is positive for nonzero vectors. Letting `|t_j|` tend to infinity therefore gives

\[
\boxed{
R_{H_j}
=\frac{t_j^2C_R^2}{E_{H_j}}
\longrightarrow C_R.
}
\tag{20}
\]

Choose a finite nonzero `t_j` large enough that `R_{H_j}>C_R-delta`. Later stages alter only values above `H_j`, so they cannot change any staircase at an earlier horizon. Induction proves (3) for one globally defined source sequence; all integers never selected by the construction may be assigned value zero.

This is why merely requiring all horizon vectors to come from one sequence is insufficient once the horizons are sparse: fresh source coordinates let each stage reproduce an arbitrarily dominant copy of the same finite equality-ray prefix while relegating all prior commitments to the tail.

## 3. Quantitative consequence for geometric chains

For (4), put `R=Q-1`. Since `H_{j-1}>=Q-1`,

\[
\frac{H_j}{R}
=\frac{QH_{j-1}}{Q-1}
=H_{j-1}+\frac{H_{j-1}}{Q-1}
\ge H_{j-1}+1,
\]

and hence

\[
\left\lfloor\frac{H_j}{R}\right\rfloor>H_{j-1}.
\tag{21}
\]

The condition `H_0>=(Q-1)^2` also gives `H_j>=R^2`. Thus the interpolation theorem applies and proves (5).

Now suppose a source-independent chain theorem of the form (7) held with `g_Q>0`. For every `delta>0`, (5) supplies a sequence with

\[
\inf_jR_{Q^jH_0}\ge C_{Q-1}-\delta.
\]

Combining with (7) gives

\[
C_{Q-1}-\delta\le Z-g_Q.
\]

Letting `delta` tend to zero yields the first inequality in (8); the second is exactly the tail estimate for `C_R` proved in `FD-003`.

For squarefree `Q`, this complements rather than contradicts `FD-015`. That finding supplies a positive two-horizon deficit at each adjacent pair. In its sharpened repeated-prime form, the explicit conservative deficit is of order

\[
\frac{1}{p_-(Q)^2Q^2},
\]

where `p_-(Q)` is the least prime factor; for prime `Q` this specializes to order `Q^{-4}`, while for composite squarefree dilations with a fixed small prime factor it is of order `Q^{-2}`. The present result says that the **best possible universal deficit based only on unrestricted source coherence along a `Q`-geometric chain cannot exceed `Z-C_{Q-1}=O(1/Q)`**. There remains a wide quantitative interval between these statements. What is ruled out here is the idea that simply having infinitely many sparse coherent horizons can amplify a local incompatibility into a fixed large gap independently of the source.

## 4. Relation to the Farey/Mertens problem

For the physical choice `A=M`, `FD-003` identifies

\[
E_H=12\left(M_H\mathfrak F_H+\frac1{12}\right),
\]

so a genuine RH-facing improvement would need information that excludes the interpolation construction. The arbitrary sequence above deliberately violates most arithmetic structure available to the true Mertens source: its increments are unrestricted, its values can be scaled independently on fresh blocks, and it need not satisfy the Möbius divisor identities beyond those forced by the definition of the sampled staircase.

Accordingly, (3)--(8) are **not** counterexamples to a stronger theorem for the actual Mertens function. They locate the missing hypothesis. A sparse-horizon argument must use something beyond common-source consistency: bounded/squarefree Möbius increments, linked divisor identities, quantitative overlap between successive floor-quotient sets, or another Farey-specific relation that prevents independent planting of equality-ray prefixes.

The theorem also does not reopen the full-hierarchy route closed by `FD-009`. Consecutive divisor-horizon data can reconstruct the Möbius prefix precisely because the scales overlap densely enough to make source values triangularly recoverable. Here the opposite extreme is isolated: when the first `R` samples at every new horizon all lie above the previous horizon, those load-bearing coordinates are freely reset. The live region is therefore between **dense reconstructive coherence** and **sparse interpolable coherence**.

## 5. Prior art, falsification controls, and boundary

The square-GCD matrix, its inverse coordinate norm `C_R`, and the estimate `0<=Z-C_R<=Z/R` are already established and sourced in `FD-003` through classical Smith/Jordan GCD-matrix factorization. The floor-quotient sets `floor(H/d)` themselves belong to a well-developed arithmetic literature; targeted prior-art searches included J.-P. Cardinal, *Symmetric matrices related to the Mertens function* (arXiv:0811.3701), and J. C. Lagarias--D. H. Richman, *The floor quotient partial order*, Advances in Applied Mathematics **153** (2024), 102615. No theorem from those papers is required for the interpolation argument, and no broad novelty claim is made for floor-quotient structure.

The durable Mathia-specific content is the exact obstruction (3)--(8) at the current multihorizon frontier. Its falsification points are explicit: the first `R` floor samples must be distinct; condition (1) must make every one of them new; the tail vector `b_j` must be independent of the newly chosen scale `t_j`; and the principal `R x R` block of `K_{H_j}` must equal `K_R`. If any of these fails, the induction need not work. Under the stated hypotheses all four are exact.

No improved estimate for the true Mertens function, Franel discrepancy, or RH is obtained. The result narrows the cumulative strategy: **source coherence is useful only when successive horizon constraints overlap enough, and strongly enough, that the dangerous equality-ray coordinates cannot be re-planted independently; counting more widely separated horizons is not itself an amplification mechanism.**