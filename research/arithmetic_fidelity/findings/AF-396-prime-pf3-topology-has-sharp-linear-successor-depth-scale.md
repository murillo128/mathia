# AF-396 — Prime PF3 topology has a sharp linear successor-depth scale

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `PRIME-LOGS` · `LOCAL-TO-GLOBAL` · `BOUNDARY-TOPOLOGY` · `QUANTITATIVE-SAMPLING` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

AF-395 proves that, for one explicit smooth positive profile `f`, bounded successor-prime depth cannot detect the disconnected-curvature obstruction to translation `TN_3`. Its optional Baker--Harman--Pintz estimate gives a polynomial lower bound on the index span of a negative witness, but that estimate is not the intrinsic scale on the ordered prime sequence.

For the same profile, the prime number theorem gives the sharp scale: **linear successor depth in the prime index is necessary and sufficient, up to the boundary constant**.

Let

\[
e_n=\log p_n,
\]

and let `f` be the AF-395 profile with logarithmic curvature

\[
q(t)=\beta(t+2)+\beta(t-2),
\]

whose two positive components are separated by the zero interval `[-1,1]`.

For an index radius `R_N`, consider all sampled order-three minors whose row and column indices lie in the tail and satisfy

\[
N\le i_1<i_2<i_3,\qquad i_3-i_1\le R_N,
\]

\[
N\le j_1<j_2<j_3,\qquad j_3-j_1\le R_N.
\]

Then:

1. if
   \[
   \limsup_{N\to\infty}\frac{R_N}{N}<e-1,
   \tag{1}
   \]
   every such tail minor is nonnegative for all sufficiently large `N`;
2. if
   \[
   \liminf_{N\to\infty}\frac{R_N}{N}>e-1,
   \tag{2}
   \]
   then for every sufficiently large `N` there is a strictly negative sampled minor with all six indices in `[N,N+R_N]`.

In particular every sublinear successor depth

\[
R_N=o(N)
\tag{3}
\]

is eventually blind, whereas any linear depth with asymptotic coefficient strictly larger than `e-1` eventually detects the defect in every tail block. Thus the combinatorial reach needed to preserve this PF3 curvature-topology discriminator is

\[
\boxed{R_N=\Theta(N)}
\]

and the critical constant away from the unresolved equality boundary is `e-1`.

The determinant order remains three. What scales linearly is the number of prime labels the retained relation must be allowed to bridge.

## Step 1: the PNT converts successor depth into physical log-prime reach

The prime number theorem in nth-prime form gives

\[
p_n\sim n\log n.
\tag{4}
\]

Hence for every fixed `c>-1`,

\[
\frac{p_{\lfloor(1+c)n\rfloor}}{p_n}\longrightarrow1+c,
\qquad
\log\frac{p_{\lfloor(1+c)n\rfloor}}{p_n}\longrightarrow\log(1+c).
\tag{5}
\]

The same asymptotic is uniform enough on a tail for the upper bound needed below. Write

\[
\varepsilon_N=
\sup_{m\ge N}
\left|\frac{p_m}{m\log m}-1\right|,
\qquad
\varepsilon_N\to0.
\tag{6}
\]

If `m\ge N` and `0\le r\le R_N`, then

\[
\frac{p_{m+r}}{p_m}
\le
\frac{1+\varepsilon_N}{1-\varepsilon_N}
\left(1+\frac r m\right)
\frac{\log(m+r)}{\log m}.
\tag{7}
\]

Therefore, whenever `R_N/N\le c+o(1)`,

\[
\sup_{m\ge N,\,0\le r\le R_N}
\log\frac{p_{m+r}}{p_m}
\le
\log(1+c)+o(1).
\tag{8}
\]

In particular `(3)` implies that every `R_N`-successor block has physical log-prime diameter `o(1)`. More generally, a radius asymptotic to `cN` has physical reach `\log(1+c)` at the earliest possible tail base, with smaller reach farther out.

This replaces the single-gap viewpoint of AF-395 by the cumulative geometry that actually controls nonlocal stencil reach.

## Step 2: radii below `(e-1)N` are eventually blind

AF-395 proves the exact locality lemma

\[
(u_3-u_1)+(x_3-x_1)\le2
\quad\Longrightarrow\quad
\det(f(u_a-x_b))_{a,b=1}^3\ge0.
\tag{9}
\]

Assume `(1)`. Choose `c<e-1` and `N_0` such that `R_N/N\le c` for `N\ge N_0`. By `(8)`, uniformly over every admissible tail row triple,

\[
e_{i_3}-e_{i_1}\le\log(1+c)+o(1),
\tag{10}
\]

and the same bound holds for the column triple. Since

\[
2\log(1+c)<2,
\tag{11}
\]

the sum of the two physical spans is eventually strictly below two. Equation `(9)` then forces every retained minor to be nonnegative.

Thus not only fixed radius but **every radius growing more slowly than `(e-1)N` by a fixed relative margin** loses the curvature-component discriminator.

The sublinear case `(3)` is immediate: each row and column span tends uniformly to zero, so increasing resolution while allowing `o(N)` successor reach still collapses the global topology.

## Step 3: negative continuum witnesses exist with both axis spans arbitrarily close to one

AF-395 used one convenient negative minor with row and column spans `3/2`. The locality threshold `(9)` suggests that this geometry can be tightened, and for the same profile it can.

Fix any

\[
L>1.
\tag{12}
\]

Choose `\epsilon>0` and `\delta>0` so small that

\[
1+2\epsilon<L,
\qquad
1+\delta<L,
\qquad
0<\epsilon<\frac12.
\tag{13}
\]

Use rows

\[
t_1=0,
\qquad
t_2=\epsilon,
\qquad
t_3=1+\delta,
\tag{14}
\]

and column gaps

\[
a=2\epsilon,
\qquad
b=1,
\tag{15}
\]

so the columns are

\[
x_1=0,
\qquad
x_2=2\epsilon,
\qquad
x_3=1+2\epsilon.
\tag{16}
\]

As in AF-395 define

\[
U(t)=\frac{f(t-a)}{f(t)},
\qquad
V(t)=\frac{f(t-a-b)}{f(t)},
\tag{17}
\]

and

\[
A(t)=\int_{t-a}^{t}q(s)\,ds,
\qquad
B(t)=\int_{t-a-b}^{t-a}q(s)\,ds.
\tag{18}
\]

For `0\le t\le\epsilon`, the `A` interval lies entirely inside the zero gap `[-1,1]`, hence

\[
A(t)=0.
\tag{19}
\]

The `B` interval is

\[
[t-1-2\epsilon,\,t-2\epsilon].
\tag{20}
\]

Its left endpoint lies strictly below `-1` and its right endpoint lies strictly above `-1`, so it overlaps the left positive-curvature component. Therefore

\[
B(t)>0
\qquad(0\le t\le\epsilon).
\tag{21}
\]

It follows that

\[
U(t_1)=U(t_2),
\qquad
V(t_2)>V(t_1).
\tag{22}
\]

For `t>1`, the `A` interval enters the right curvature component. Hence

\[
U(t_3)>U(t_2).
\tag{23}
\]

The same normalized determinant identity used in AF-395 gives

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}
=-(U(t_3)-U(t_1))(V(t_2)-V(t_1))<0.
\tag{24}
\]

Positive row normalization preserves the sign of the original translation minor. By `(13)`--`(16)`, both its row span and its column span are strictly smaller than `L`.

Therefore

\[
\boxed{
\text{for every }L>1,
\text{ the AF-395 profile has a negative }3\times3
\text{ minor with each axis span }<L.
}
\tag{25}
\]

Combined with `(9)`, the infimum possible maximum axis span of a negative minor is exactly one. It is not attained by this argument; the relevant point is the sharp approach to the component-gap threshold.

## Step 4: radii above `(e-1)N` detect negativity in every large tail block

Assume `(2)`. Choose `c>e-1` and `N_0` such that

\[
R_N\ge cN
\tag{26}
\]

for `N\ge N_0`. Since `\log(1+c)>1`, choose `L` with

\[
1<L<\log(1+c).
\tag{27}
\]

Take the strict negative continuum configuration from `(25)`, with row offsets

\[
0=t_1<t_2<t_3<L
\]

and column offsets

\[
0=x_1<x_2<x_3<L.
\]

For each large `N`, define sampled indices

\[
i_a(N)=\lfloor e^{t_a}N\rfloor,
\qquad
j_b(N)=\lfloor e^{x_b}N\rfloor.
\tag{28}
\]

By `(5)`,

\[
\log\frac{p_{i_a(N)}}{p_N}\longrightarrow t_a,
\qquad
\log\frac{p_{j_b(N)}}{p_N}\longrightarrow x_b.
\tag{29}
\]

Hence

\[
\log\frac{p_{i_a(N)}}{p_{j_b(N)}}
\longrightarrow t_a-x_b
\tag{30}
\]

entrywise. Continuity of `f` and of the determinant implies that the sampled determinant converges to the strict negative continuum determinant `(24)`, so it is negative for all sufficiently large `N`.

Moreover

\[
i_3(N)-N
=(e^{t_3}-1+o(1))N
<(e^L-1+o(1))N
<cN,
\tag{31}
\]

and likewise for the columns. Thus all six indices lie in `[N,N+R_N]` for sufficiently large `N`.

This proves the second half of the claim. The full prime-ratio family does not merely contain negative witnesses arbitrarily far out: once a relative index window exceeds the critical physical reach, **every sufficiently large multiplicative-scale block contains one**.

## Sharp scale and the equality boundary

The two implications show that the successor-depth scale itself is sharp:

\[
R_N=o(N)
\quad\Longrightarrow\quad
\text{eventual blindness},
\tag{32}
\]

while any fixed relative radius strictly above `e-1` yields eventual detection.

The constant `e-1` comes from a clean coordinate conversion rather than from prime-gap technology. A physical log-prime span of one corresponds under the PNT to multiplying the prime index by `e`, hence to a successor radius `(e-1)N`.

This finding does **not** settle the exact boundary regime

\[
\frac{R_N}{N}\to e-1.
\tag{33}
\]

At that scale the available physical overhang beyond one is lower order, while the negative determinant margin in `(24)` also tends to zero if the continuum spans are driven down to one. Resolving `(33)` requires comparing those two rates and the prime-log approximation error; it is a conditioning problem, not a change in the linear information scale.

## Prior-art and novelty audit

The only new external ingredient beyond AF-395 is the classical prime number theorem in its equivalent nth-prime form `p_n\sim n\log n`. Equation `(5)` is an immediate regular-variation consequence of that asymptotic. The total-positivity input, the two-component profile, and the locality lemma are already canonical in AF-394/AF-395.

A focused search for nth-prime regular variation, prime-log total-positivity sampling, successor-prime stencil depth, and sampled Pólya-frequency determination found the PNT asymptotic and the previously audited sampled-Pólya-frequency literature, but no standard theorem packaging this particular successor-depth threshold. **No novelty is claimed.** The mathematical content here is the exact synthesis of two existing ingredients plus the tightened continuum witness `(25)`.

The result should not be read as a new theorem on prime gaps. In fact it removes prime-gap estimates from the governing scale. Baker--Harman--Pintz remains useful for pointwise covering and finite-witness conditioning as in AF-380, but cumulative successor reach is controlled at first order by `p_n\sim n\log n`.

## Fidelity interpretation

AF-395 separated sampling resolution from relational reach. AF-396 quantifies that separation on the actual ordered prime source.

A local observer retaining `R_N` successor labels around the `N`th prime has physical reach approximately

\[
\log\left(1+\frac{R_N}{N}\right).
\tag{34}
\]

The disconnected-curvature discriminator lives across a physical gap of one per row/column axis. Therefore a fixed or sublinear combinatorial neighborhood shrinks to zero in the intrinsic log-prime geometry and necessarily loses the global component relation. To preserve it, the retained relation must connect a **positive fraction of all earlier-scale prime labels**.

This is stronger than saying that the mesh must become fine or that a large finite stencil may eventually suffice. It identifies the resource class:

\[
\text{local prime resolution}
\not\Rightarrow
\text{global PF3 topology},
\]

whereas

\[
\text{linear successor reach}
\Rightarrow
\text{eventual access to the missing topology}
\]

for the explicit obstruction profile.

The conclusion is target-relative. It does not say that every RH-relevant prime observable requires linear index reach, nor that this AF-395 profile is itself an arithmetic object. It says that **if** an RH route compresses its relevant order-three relation into bounded or sublinear successor-prime neighborhoods, then this natural smooth PF3 control class contains a global topology discriminator that the compression provably cannot retain.

## Boundaries and failure modes

The theorem concerns the explicit AF-395 two-component profile. Other curvature-component geometries have different physical gap lengths and therefore rescale the numerical constant, though the PNT conversion from fixed positive log-prime reach to linear index reach is unchanged.

The threshold is about index radius, not determinant order, bit complexity, or numerical conditioning. A three-by-three determinant is enough throughout.

Condition `(2)` is sufficient because the explicit negative continuum witness can be made to fit any physical span strictly larger than one. The equality case `(33)` is deliberately left open.

The tail-blindness implication uses a uniform bound over all starting indices at least `N`. It is therefore stronger than a statement only about the block beginning exactly at `N`.

The detection implication is constructive only asymptotically: the chosen indices are `\lfloor e^{t_a}N\rfloor` and `\lfloor e^{x_b}N\rfloor`, and no explicit finite onset is extracted from the PNT error term or the determinant margin.

Finally, source identification and target fidelity remain separate. The prime labels enter here only through their asymptotic index geometry. Any nonprime sampling sequence with the same regular variation would exhibit the same scale conversion. This result therefore sharpens the **compression-resource audit** but does not by itself preserve rational-prime specificity or imply RH.

## Decisive audit rule

For a prime-index compression that claims to retain a fixed positive physical relation scale in `\log p`, compute

\[
\rho_N=\frac{R_N}{N}.
\]

If `\rho_N\to0`, the retained physical reach collapses to zero. More generally, a target relation requiring log-prime span `L>0` needs successor depth of order

\[
(e^L-1)N.
\]

Do not substitute a single-gap bound for this cumulative reach calculation. Prime-gap estimates control local covering; the PNT controls how many ordered prime labels must be traversed to retain a fixed macroscopic relation.

## Consequences

AF-395's qualitative local-to-global obstruction now has its intrinsic prime-index scale. Fixed-depth and polynomial lower bounds derived from one-step gap control are not the final resource statement: the actual transition is linear in the prime index.

For the current PF3 frontier this makes the missing resource precise. If arithmetic is ever to force the connected-curvature condition of AF-394 through sampled prime relations alone, those relations cannot remain confined to `o(N)` successor neighborhoods. Either the arithmetic source must supply connectedness by a separate theorem, or the retained observation must allow genuinely macroscopic prime-index reach.

This is a reusable Arithmetic Fidelity pattern: **vanishing local mesh can coexist with diverging combinatorial cost for preserving a fixed global relation scale**. The correct cost is determined by the cumulative geometry of the source sequence, not by its worst one-step gap.