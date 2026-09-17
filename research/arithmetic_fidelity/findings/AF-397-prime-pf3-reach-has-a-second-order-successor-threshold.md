# AF-397 — Prime PF3 reach has a second-order successor threshold

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `PRIME-LOGS` · `LOCAL-TO-GLOBAL` · `BOUNDARY-TOPOLOGY` · `QUANTITATIVE-SAMPLING` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

AF-396 located the first-order successor-depth transition for the explicit AF-395 two-component curvature profile at

\[
R_N\asymp(e-1)N,
\]

but left the boundary regime `R_N/N\to e-1` unresolved because the available physical log-prime overhang and the negative-minor margin both shrink there.

For this profile the determinant margin is not the right quantity to compare. The sign mechanism can be written so that **one prime-log mesh width of physical overhang beyond one already forces a strict negative minor**. Combined with the classical second-order asymptotic for the `n`th prime, this resolves the next scale.

Let

\[
e_n=\log p_n,
\]

let `f` be the AF-395 profile with

\[
q(t)=-(\log f)''(t)=\beta(t+2)+\beta(t-2),
\]

and, for an integer radius `R\ge1`, define the anchored block reach and mesh

\[
H_N(R)=e_{N+R}-e_N
      =\log\frac{p_{N+R}}{p_N},
\tag{1}
\]

\[
\Delta_N(R)
=\max_{N\le n<N+R}(e_{n+1}-e_n).
\tag{2}
\]

Then the following exact block criteria hold for all sufficiently large blocks:

1. if
   \[
   H_N(R)\le1,
   \tag{3}
   \]
   every sampled `3\times3` minor whose six indices lie in `[N,N+R]` is nonnegative;
2. if
   \[
   H_N(R)>1+\Delta_N(R)
   \tag{4}
   \]
   and `\Delta_N(R)<1/4`, then `[N,N+R]` contains a strictly negative sampled `3\times3` minor.

Thus the uncertainty between guaranteed blindness and guaranteed detection is only one local prime-log mesh width in the intrinsic coordinate.

Now fix `\alpha\in\mathbb R` and put

\[
R_N
=\left\lfloor
(e-1)N-\alpha\frac{N}{\log N}
\right\rfloor.
\tag{5}
\]

The classical expansion of the `n`th prime gives

\[
H_N(R_N)
=
1+
\frac{1-\alpha/e}{\log N}
+O\!\left(\frac{\log\log N}{\log^2N}\right).
\tag{6}
\]

The Baker--Harman--Pintz prime-gap input already audited in AF-380/AF-395 gives

\[
\Delta_N(R_N)
=O\!\left(p_N^{-19/40}\right)
=o\!\left(\frac1{\log N}\right).
\tag{7}
\]

Consequently:

- if `\alpha>e`, every order-three minor inside `[N,N+R_N]` is nonnegative for all sufficiently large `N`;
- if `\alpha<e`, every sufficiently large block `[N,N+R_N]` contains a strictly negative order-three minor.

Therefore the first-order boundary from AF-396 splits at the next scale:

\[
\boxed{
R_N^{\mathrm{crit}}
=
(e-1)N
-e\frac{N}{\log N}
+O\!\left(\frac{N\log\log N}{\log^2N}\right)
}
\tag{8}
\]

in the sense of the two one-sided implications above.

In particular the literal AF-396 equality-radius choice

\[
R_N=\lfloor(e-1)N\rfloor
\tag{9}
\]

is **eventually detecting**, not marginal: it lies above the second-order transition by asymptotically `eN/\log N` successor labels.

The remaining boundary is no longer the whole regime `R_N/N\to e-1`; it is the thinner scale around `\alpha=e`, where terms of order `N\log\log N/\log^2N` and smaller matter.

## Exact one-mesh overhang criterion

The blindness half is immediate from the AF-395 locality lemma. Any row triple and column triple inside `[N,N+R]` have physical spans at most `H_N(R)`. Hence `(3)` implies

\[
(e_{i_3}-e_{i_1})+(e_{j_3}-e_{j_1})
\le2H_N(R)\le2.
\tag{10}
\]

AF-395 proves that every order-three minor of the explicit profile whose complete argument hull has length at most two is nonnegative. This gives the first criterion.

For the converse assume `(4)` and write

\[
H=H_N(R),
\qquad
\Delta=\Delta_N(R).
\]

Use the first and last block points as both row and column endpoints. In physical coordinates relative to `e_N`, set

\[
t_1=0,
\qquad
t_2=e_{N+1}-e_N,
\qquad
t_3=H.
\tag{11}
\]

Then

\[
0<t_2\le\Delta<H-1.
\tag{12}
\]

For the middle column, let `j_2` be the first index in the block for which

\[
x_2=e_{j_2}-e_N\ge\frac12.
\tag{13}
\]

Such an index exists because `H>1`. Minimality and the mesh bound give

\[
\frac12\le x_2\le\frac12+\Delta<\frac34.
\tag{14}
\]

Take

\[
x_1=0,
\qquad x_3=H.
\tag{15}
\]

All six points are sampled prime logs from `[N,N+R]`.

Normalize the translation matrix rowwise by the positive factors `f(t_i)`, and define

\[
U(t)=\frac{f(t-x_2)}{f(t)},
\qquad
V(t)=\frac{f(t-H)}{f(t)}.
\tag{16}
\]

As in AF-394/AF-395,

\[
(\log U)'(t)=A(t)
=\int_{t-x_2}^{t}q(s)\,ds,
\tag{17}
\]

\[
(\log V)'(t)=A(t)+B(t),
\qquad
B(t)=\int_{t-H}^{t-x_2}q(s)\,ds.
\tag{18}
\]

For `0\le t\le t_2`, equations `(12)` and `(14)` put the full `A` interval inside the curvature-free gap `(-1,1)`, so

\[
A(t)=0.
\tag{19}
\]

On the same interval,

\[
t-H\le t_2-H<-1,
\qquad
t-x_2>-1,
\tag{20}
\]

so the `B` interval crosses the boundary point `-1` and contains a nonempty interval in the left positive-curvature component `(-3,-1)`. Therefore

\[
B(t)>0
\qquad(0\le t\le t_2).
\tag{21}
\]

It follows that

\[
U(t_1)=U(t_2),
\qquad
V(t_2)>V(t_1).
\tag{22}
\]

Finally, `q\ge0` makes `U` nondecreasing everywhere, and because `H>1`, the interval from `t_2` to `H` contains points immediately to the right of `1` where `[t-x_2,t]` overlaps the right curvature component `(1,3)`. Thus

\[
U(t_3)>U(t_2)=U(t_1).
\tag{23}
\]

The normalized determinant therefore satisfies the exact identity

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}
=
-(U(t_3)-U(t_1))(V(t_2)-V(t_1))<0.
\tag{24}
\]

Positive row normalization preserves the sign of the raw translation minor. This proves `(4)` without a determinant-continuity estimate and without needing a quantitative lower bound for the negative margin.

The important resource is therefore not a stable margin bounded away from zero. It is **enough physical overhang to insert one sampled point before the topology boundary and another beyond it**.

## Second-order conversion from prime index to physical reach

Write

\[
L=\log N,
\qquad
\ell=\log L,
\qquad
k_N=N+R_N.
\]

From `(5)`,

\[
\frac{k_N}{N}
=
e-\frac{\alpha}{L}+O\!\left(\frac1N\right),
\tag{25}
\]

and hence

\[
\log\frac{k_N}{N}
=
1-\frac{\alpha}{eL}
+O\!\left(\frac1{L^2}\right).
\tag{26}
\]

The classical Cipolla expansion, in the form

\[
p_n
=n\left(
\log n+\log\log n-1
+O\!\left(\frac{\log\log n}{\log n}\right)
\right),
\tag{27}
\]

is sufficient here. Define the exact slowly varying factor

\[
A(n)=\frac{p_n}{n}.
\tag{28}
\]

Equation `(27)` gives

\[
A(n)
=\log n+\log\log n-1
+O\!\left(\frac{\log\log n}{\log n}\right).
\tag{29}
\]

Because `\log k_N=L+1+O(1/L)`, subtraction of the two asymptotic formulas yields

\[
A(k_N)-A(N)
=1+O\!\left(\frac{\ell}{L}\right).
\tag{30}
\]

Since `A(N)=L+O(\ell)`, equations `(29)`--`(30)` and the logarithm expansion imply

\[
\log\frac{A(k_N)}{A(N)}
=
\frac1L
+O\!\left(\frac{\ell}{L^2}\right).
\tag{31}
\]

Combining `(26)` and `(31)` gives

\[
\begin{aligned}
H_N(R_N)
&=\log\frac{p_{k_N}}{p_N}\\
&=\log\frac{k_N}{N}
 +\log\frac{A(k_N)}{A(N)}\\
&=1+
\frac{1-\alpha/e}{L}
+O\!\left(\frac{\ell}{L^2}\right),
\end{aligned}
\tag{32}
\]

which is `(6)`.

This identifies a second-order effect hidden by the first-order regular-variation calculation in AF-396. Multiplying the prime index by exactly `e` increases the prime itself by slightly **more** than `e`, because the slowly varying `\log n` factor also grows. Therefore one needs slightly fewer than `(e-1)N` successors to obtain physical log-prime reach one.

Equivalently, define the exact locality-wall count

\[
B_N=\pi(e p_N)-N.
\tag{33}
\]

For `R\le B_N`, one has `p_{N+R}<e p_N` and hence `H_N(R)<1`, so the block is certified nonnegative by `(3)`. The standard asymptotic expansion of `\pi(x)` (equivalently `(27)`) gives

\[
B_N
=(e-1)N
-e\frac{N}{\log N}
+O\!\left(\frac{N\log\log N}{\log^2N}\right).
\tag{34}
\]

Thus `(8)` is not an arbitrary reparametrization: it is the second-order location of the exact physical topology boundary `p_{N+R}=e p_N`.

## Prime-log mesh is negligible at the second-order scale

AF-380/AF-395 already audit the Baker--Harman--Pintz consequence

\[
\log\frac{p_{n+1}}{p_n}
=O\!\left(p_n^{-19/40}\right).
\tag{35}
\]

Uniformly over `N\le n<N+R_N`, monotonicity of `p_n` gives

\[
\Delta_N(R_N)
=O\!\left(p_N^{-19/40}\right).
\tag{36}
\]

Since `p_N\sim N\log N`,

\[
p_N^{-19/40}
=o\!\left(\frac1{\log N}\right).
\tag{37}
\]

For `\alpha<e`, equation `(32)` therefore gives a constant `c_\alpha>0` such that

\[
H_N(R_N)-1
\ge\frac{c_\alpha}{\log N}
>\Delta_N(R_N)
\tag{38}
\]

for all sufficiently large `N`. The exact one-mesh criterion `(4)` then supplies a negative minor in every such block.

For `\alpha>e`, equation `(32)` gives `H_N(R_N)<1`, so `(3)` makes the entire block nonnegative. No prime-gap input is needed on the blind side.

At `\alpha=e`, the `1/\log N` term cancels. Equation `(32)` leaves an `O(\log\log N/\log^2N)` physical correction, still much larger than the BHP mesh bound in scale but not determined in sign by the truncated expansion used here. A further asymptotic term can sharpen that thinner boundary, but it does not alter the second-order conclusion.

## Prior-art and novelty audit

Juan Arias de Reyna and Jérémy Toulisse, **“The n-th prime asymptotically,”** *Journal de Théorie des Nombres de Bordeaux* **25**(3) (2013), 521--555, DOI `10.5802/jtnb.847`, give a modern derivation of the classical full asymptotic expansion of the `n`th prime, tracing it to Cipolla. Equation `(27)` is a low-order specialization of that classical expansion.

The Baker--Harman--Pintz short-interval/gap input and its prime-log consequence are already audited in AF-380 and reused in AF-395. The total-positivity criterion, the explicit two-component curvature profile, and the length-two locality lemma are already canonical in AF-394/AF-395.

A focused search for prime-log Pólya-frequency sampling, total positivity on successor-prime stencils, and second-order successor-depth thresholds did not identify a standard theorem packaging `(3)`--`(8)`. The external ingredients themselves are classical, and **no novelty is claimed**. The durable Arithmetic Fidelity content is the resource accounting: a global component discriminator has an exact physical reach wall, the sampled detector needs only one local mesh width beyond that wall, and classical prime asymptotics convert the wall into a two-term combinatorial-depth threshold.

## Fidelity interpretation

AF-396 showed that preserving this PF3 topology requires linear relational reach in the ordered prime labels. AF-397 shows that this statement has a meaningful lower-order structure.

The first-order approximation

\[
R_N\approx(e-1)N
\]

treats `p_n` as if it were exactly proportional to `n`. The second-order correction records the slowly varying prime-density factor. In fidelity language, **the cost of preserving a fixed physical relation depends not only on the coarse source geometry but on the source's local density law**.

The exact criteria `(3)` and `(4)` also separate two notions that were conflated in the AF-396 boundary discussion:

- the physical reach needed for the discriminator itself is exactly one per axis for the AF-395 topology obstruction;
- the additional sampled overhead needed to realize a strict witness is only one local mesh width.

Because the prime-log mesh is polynomially smaller than `1/\log N`, sampling/conditioning does not control the second-order threshold. The source-density correction does.

This remains a control theorem, not an RH mechanism. The profile is deliberately non-arithmetic and is used to measure what a successor-local compression can forget. The result says that retaining only approximately `(e-1)N` neighboring prime labels is too coarse a statement: at the next scale, a deficit of `\alpha N/\log N` is tolerated precisely on opposite sides of `\alpha=e`.

## Boundaries and failure modes

The two-sided theorem is stated for anchored blocks `[N,N+R_N]`. AF-396's stronger blind-side statement quantified over every triple starting anywhere in the tail with a common index-radius bound. The anchored formulation is intentional here because it gives an exact physical diameter `H_N(R)` and is sufficient to resolve the boundary behavior of the blocks used by the detection construction. No stronger uniform-tail second-order monotonicity claim is made.

The theorem is specific to the AF-395 profile, whose two curvature components are separated by a zero interval of length two and whose order-three locality wall is one per row/column axis. Rescaling that geometry rescales the corresponding prime-index threshold.

Equation `(4)` is sufficient, not asserted necessary. There may be negative sampled minors when `1<H_N(R)\le1+\Delta_N(R)`. The theorem deliberately isolates a transition strip no wider than one mesh in physical coordinates rather than claiming an exact first detecting index.

The BHP exponent is not believed to be optimal and is not structurally important. Any unconditional mesh estimate `\Delta_N=o(1/\log N)` would suffice for `(38)`.

The expansion `(8)` is a two-term threshold statement. The case `\alpha=e` requires the next term of the classical prime asymptotic together with the same exact detector criterion; it is not settled here.

Finally, a large successor radius is not by itself arithmetic fidelity. It merely prevents this particular topology discriminator from being lost. A successful RH-facing construction must still show that the retained relation is generated intrinsically by the rational primes and remains selective against matched non-prime controls.

## Decisive audit rule

When an arithmetic sampling proposal claims that a relational discriminator survives a growing successor window, compare three scales separately:

1. the **intrinsic physical wall** at which the target relation first can connect the required components;
2. the **source-density conversion** from physical reach to index reach, including lower-order terms when the first-order coefficient is critical;
3. the **sampling mesh overhead** needed to realize a strict discrete witness beyond the physical wall.

For the AF-395 PF3 control on prime logs, these scales are respectively `1`, `(e-1)N-eN/\log N+\cdots`, and `O(p_N^{-19/40})` in physical log-prime units. Confusing them hides which information resource is actually limiting fidelity.

## Consequences

The broad AF-396 boundary `R_N/N\to e-1` is no longer undifferentiated. At successor depths

\[
(e-1)N-\alpha N/\log N,
\]

the profile is eventually block-blind for `\alpha>e` and block-detecting for `\alpha<e`. In particular `\lfloor(e-1)N\rfloor` detects eventually.

This strengthens the line's current local-to-global lesson: **global relational reach has a source-dependent acquisition cost even when determinant order and local resolution are fixed**. For prime logs the first correction to that cost comes from the classical density law of the source, not from total-positivity conditioning.

The next mathematically distinct question is not whether the first-order constant is exactly attained; it is whether genuine arithmetic structure can supply the required nonlocal relation or connectedness without explicitly retaining a linear-sized successor neighborhood. That is the source-fidelity gate identified in the current Arithmetic Fidelity synthesis.