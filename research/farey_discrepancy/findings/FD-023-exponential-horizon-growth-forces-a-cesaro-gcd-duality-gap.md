# FD-023 — exponential horizon growth forces a Cesàro GCD-duality gap

**Status:** `EXACT-DERIVED + UNBOUNDED-RATIO-MULTIHORIZON + HORIZON-ENTROPY-OBSTRUCTION + POLYNOMIAL-SOURCE-CESARO-GAP + SUPEREXPONENTIAL-NECESSITY + NEGATIVE/OBSTRUCTION`.

`FD-022` proves a positive Cesàro gap for polynomial-growth sources on integer-ratio horizon chains with a fixed transition ceiling. Its stated boundary is unbounded transition breadth. The ceiling is stronger than necessary. A polynomial source can still sacrifice rare very large jumps, while the cumulative logarithmic growth of the horizon controls both how many such jumps can occur and how often a nonsquarefree near-extremizer can amplify its endpoint.

Let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad Z:=\zeta(2),
\]

and for a real source `A(1),A(2),...` define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H},
\tag{1}
\]

with `R_H:=0` when the horizon vector is zero. As in `FD-003`,

\[
0\le R_H\le C_H:=(K_H^{-1})_{11}\le Z.
\tag{2}
\]

Consider an arbitrary integer-ratio chain

\[
H_j=q_jH_{j-1},\qquad q_j\in\mathbb Z_{\ge2},
\tag{3}
\]

with no upper bound on `q_j`, and assume only the polynomial source envelope

\[
|A(n)|\le Cn^\alpha
\qquad(C>0,\ \alpha\ge0).
\tag{4}
\]

Define the logarithmic horizon growth

\[
\Lambda_n:=\frac1n\log\frac{H_n}{H_0}
=\frac1n\sum_{j=1}^n\log q_j.
\tag{5}
\]

Then the sharp one-horizon constant cannot be saturated in Cesàro mean at finite logarithmic horizon density:

\[
\boxed{
\frac1{n+1}\sum_{j=0}^nR_{H_j}\longrightarrow Z
\quad\Longrightarrow\quad
\Lambda_n\longrightarrow\infty.
}
\tag{6}
\]

Equivalently, **Cesàro saturation by any polynomial-growth source forces the sampled horizons to grow superexponentially in their index**:

\[
\boxed{
\forall L<\infty,\qquad
H_n>H_0e^{Ln}
\quad\text{eventually}.
}
\tag{7}
\]

For the physical source `A=M`, the trivial bound `|M(n)|\le n` gives `alpha=1`, so (6)--(7) apply with no cancellation estimate. Thus the bounded-ratio restriction of `FD-022` can be replaced, at the qualitative saturation boundary, by the much weaker requirement that the horizon chain have at most exponential growth.

## 1. A finite-entropy subsequence already has a positive average gap

The contrapositive is quantitative. Fix `L<infinity` and suppose an infinite subsequence `n_k` satisfies

\[
\Lambda_{n_k}\le L.
\tag{8}
\]

Choose any finite integer `B>=2` and any `0<theta<1`. Set

\[
r_\theta:=
\left(\frac1Z+\frac{\theta^2}{Z^2}\right)^{-1},
\qquad
a_\theta:=Z-r_\theta>0.
\tag{9}
\]

For squarefree `q<=B`, let `p_-(q)` be its least prime factor and retain the `FD-015` gap

\[
\kappa_q^\sharp
:=
\left(
\frac1Z+
\frac{4}{25p_-(q)^2q^2Z^2}
\right)^{-1}.
\tag{10}
\]

Put

\[
\kappa_B^{\rm sf}:=
\max_{\substack{2\le q\le B\\q\ \mathrm{squarefree}}}
\kappa_q^\sharp,
\qquad
b_B:=\frac{Z-\kappa_B^{\rm sf}}2>0.
\tag{11}
\]

If

\[
c_{\alpha,L}(B,\theta)
:=1-\frac{L}{\log B}
-\frac{\alpha L}{\log(1/\theta)}>0,
\tag{12}
\]

then along every subsequence satisfying (8),

\[
\boxed{
\liminf_{k\to\infty}
\frac1{n_k+1}\sum_{j=0}^{n_k}(Z-R_{H_j})
\ge
\Delta_{\alpha,L}(B,\theta)
:=
\frac{a_\theta b_B}{a_\theta+b_B}
\,c_{\alpha,L}(B,\theta)
>0.
}
\tag{13}
\]

Such parameters always exist for finite `L`: take `B` sufficiently large and then `theta` sufficiently small. For example, `B>e^{4L}` and, when `alpha L>0`, `theta<e^{-4alpha L}` make the two losses in (12) each less than `1/4`; when `alpha=0`, the second loss vanishes.

Thus (6) is not merely a failure of pointwise convergence. Any return of the horizon-growth entropy to a bounded value forces a fixed positive Cesàro deficit along that same subsequence.

## 2. Rare large transitions cost at most logarithmic horizon entropy

For fixed `B`, let

\[
L_B(n):=\#\{1\le j\le n:q_j>B\}.
\tag{14}
\]

Every counted transition contributes at least `log B` to the sum in (5), hence

\[
L_B(n)\log B
\le
\sum_{j=1}^n\log q_j
=n\Lambda_n.
\tag{15}
\]

Along (8), therefore,

\[
\limsup_{k\to\infty}
\frac{L_B(n_k)}{n_k}
\le\frac{L}{\log B}.
\tag{16}
\]

This is the first place where the fixed transition ceiling of `FD-022` can be removed. Very large jumps may be discarded entirely; finite average logarithmic growth forces their density to be small once `B` is chosen large.

## 3. Near-saturated nonsquarefree stages also consume logarithmic entropy

`FD-022` derives the long-range coordinate identity behind its bounded-chain theorem. If `i<j`, then

\[
d_{i,j}:=\frac{H_j}{H_i}\in\mathbb Z
\]

is a coordinate at horizon `H_j` and samples the earlier endpoint exactly:

\[
m_{d_{i,j}}^{(H_j)}=A(H_i).
\tag{17}
\]

If the current transition `q_j` is nonsquarefree, then `d_(i,j)` is nonsquarefree. The GCD equality ray vanishes at every nonsquarefree coordinate, and the `FD-014` stability estimate therefore gives

\[
\boxed{
\left|\frac{A(H_i)}{A(H_j)}\right|
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1Z}
}
\tag{18}
\]

whenever `R_(H_j)>0`.

Let

\[
G_\theta(n)
:=
\#\{1\le j\le n:
q_j\ \text{nonsquarefree and }R_{H_j}\ge r_\theta\}.
\tag{19}
\]

Enumerate these indices as `g_1<...<g_m`. Equation (18) and the definition of `r_theta` imply

\[
|A(H_{g_\ell})|
\ge\theta^{-1}|A(H_{g_{\ell-1}})|
\qquad(2\le\ell\le m).
\tag{20}
\]

Since every counted ratio is positive, the counted endpoints are nonzero. Iteration and the polynomial envelope give

\[
\theta^{-(m-1)}|A(H_{g_1})|
\le C H_n^\alpha.
\tag{21}
\]

Consequently

\[
G_\theta(n)\log(1/\theta)
\le
\alpha\log H_n+O(1),
\tag{22}
\]

and along (8)

\[
\boxed{
\limsup_{k\to\infty}
\frac{G_\theta(n_k)}{n_k}
\le
\frac{\alpha L}{\log(1/\theta)}.
}
\tag{23}
\]

No bound on the individual `q_j` enters this argument. The resource limiting repeated nonsquarefree near-saturation is the total logarithmic horizon growth itself.

## 4. The remaining density must pay a duality deficit

Let

\[
S_B(n):=
\#\{1\le j\le n:q_j\le B\text{ and }q_j\text{ squarefree}\},
\qquad
d_j:=Z-R_{H_j}.
\tag{24}
\]

For fixed `B`, all sufficiently late transitions counted by `S_B` satisfy the finite threshold in `FD-015`. Summing its adjacent-edge gap exactly as in `FD-020` gives

\[
\frac1{n+1}\sum_{j=0}^nd_j
\ge
b_B\frac{S_B(n)}n-o(1).
\tag{25}
\]

Every transition index not belonging to the union of

- `q_j>B`,
- `q_j<=B` squarefree,
- nonsquarefree stages with `R_(H_j)>=r_theta`,

is a bounded nonsquarefree stage with

\[
d_j>a_\theta.
\tag{26}
\]

The first and third sets may overlap, so subtracting their cardinalities separately is conservative. Along (8), if `s_k:=S_B(n_k)/n_k`, equations (16), (23), and (26) imply

\[
\liminf_k
\frac1{n_k+1}\sum_{j=0}^{n_k}d_j
\ge
\liminf_k
\max\left\{
 b_Bs_k,
 a_\theta\bigl(c_{\alpha,L}(B,\theta)-s_k\bigr)
\right\}.
\tag{27}
\]

For `a,b>0` and `0<c<=1`,

\[
\min_{s\in[0,1]}\max\{bs,a(c-s)\}
=\frac{ab}{a+b}c.
\tag{28}
\]

Equations (27)--(28) prove (13).

Now suppose Cesàro saturation held but `Lambda_n` did not tend to infinity. Then some finite `L` and infinite subsequence would satisfy (8). Choosing `B,theta` with (12) positive, (13) would give a fixed positive deficit along that subsequence, contradicting saturation. This proves (6)--(7).

## 5. Relation to the existing multihorizon boundary

The conclusion fits tightly between the two previous sides of the relaxation. `FD-017` shows that if successive horizon ratios tend to infinity, then an unrestricted real source can be constructed that saturates the full one-horizon constant. Such a chain automatically has `Lambda_n->infinity`. `FD-023` proves the converse growth requirement for **every polynomial-growth source**, even for the weaker demand of Cesàro saturation rather than pointwise saturation.

This does not identify the exact threshold for arbitrary real sources or for the physical Mertens staircase. In particular, `Lambda_n->infinity` is necessary here but not sufficient for a polynomial-growth source, and the theorem still concerns the normalized dual ratio rather than a direct upper bound for `M(H)` or the Franel energy. It therefore does not improve the RH-critical exponent.

What it does close is the stated unbounded-ratio loophole of `FD-022` at the qualitative growth level: **rare large transition ratios do not rescue any hierarchy whose sampled horizons remain at most exponential in the number of retained scales**. Any compressed-horizon strategy hoping to evade the accumulated GCD-duality gap must become superexponentially sparse before source-specific Möbius cancellation even enters.

## 6. Stress tests and prior-art boundary

The proof uses only canonical local ingredients: the universal one-horizon GCD duality of `FD-003`, the equality-ray stability identity of `FD-014`, the squarefree two-horizon gap of `FD-015`, and the long-range nonsquarefree zero-coordinate mechanism already derived in `FD-022`. The new step is the entropy split (15): an unbounded transition schedule is partitioned into a finite bounded part and a rare large-jump part, with both the sacrificed-jump density and the endpoint-amplification density charged to `log H_n`.

Zero endpoints do not weaken the count: every stage in `G_theta` has `R_H>=r_theta>0`, hence a nonzero endpoint. The squarefree edge threshold is uniform after a finite prefix because `B` is fixed. No estimate for primes, Möbius cancellation, or Farey gaps is used. The overlap between large nonsquarefree transitions and `G_theta` is harmless because (27) uses a union bound in the weakening direction.

A targeted prior-art search covered Franel--Landau/Farey discrepancy, GCD-matrix extremality and GCD sums, floor-quotient Möbius formulations, and Cesàro averaging. The neighboring literature concerns static GCD matrices, Farey discrepancy or floor-quotient inversion; no directly matching theorem about source-coherent horizon saturation versus logarithmic horizon growth was located. No literature novelty claim is made from absence of a search hit. The mathematical dependencies remain the Smith/Jordan GCD-matrix anchors already recorded in `SOURCES.md`, so no new durable bibliographic source is required.

The decisive falsification test is elementary: find an integer-ratio chain with `liminf Lambda_n<infinity` and a polynomial-growth source whose Cesàro mean of `R_(H_j)` tends to `Z`. Such an example would have to violate at least one of the exact counting inequalities (15), (18), (23), or the accumulated squarefree edge gap (25).