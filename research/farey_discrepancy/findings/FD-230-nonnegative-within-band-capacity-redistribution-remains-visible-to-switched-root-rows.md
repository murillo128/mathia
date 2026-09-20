# FD-230 — Nonnegative within-band capacity redistribution remains visible to switched root rows

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / nonnegative cellwise cushions / dyadic mass dominance / switched stability / within-band redistribution veto
- **Depends on:** FD-229, FD-226, FD-225, FD-212
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + NONNEGATIVE-CELLWISE-CUSHION + DYADIC-MASS-DOMINANCE + SWITCHED-NORMALIZED-STABILITY + WITHIN-BAND-REDISTRIBUTION-VETO`

## Claim

FD-229 rules out every bounded **scalar-per-dyadic-band** capacity cushion, including arbitrary aperiodic band amplitudes. Its stated boundary leaves open the possibility that a positive reservoir cushion could evade the switched rows by redistributing its occupancy nonuniformly **inside** each dyadic divisor band. Nonnegativity is enough to remove that escape at the level relevant to aggregate capacity.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m} b_d M\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{1}
\]

be the exact divisor-response operator from FD-225, and let

\[
b_d\ge0,
\qquad
b_d\le C d
\tag{2}
\]

for one fixed `C`. Put

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\qquad
s_k:=4^{-(k+1)}\sum_{d\in B_k}b_d,
\tag{3}
\]

and define the dyadic response

\[
y_j=(\mathscr A b)(2^j),
\qquad
r_j=q_j+1=(1,4,4,1,4,4,\ldots)
\tag{4}
\]

with the switched schedule of FD-212. If

\[
\boxed{
(E-I)^{r_j}y_j=o(4^j)
}
\tag{5}
\]

for all sufficiently large `j`, then

\[
\boxed{
s_k\longrightarrow0.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\frac{\sum_{d\in B_k}b_d}
     {\sum_{d\in B_k}d}
\longrightarrow0.
}
\tag{7}
\]

Thus a nonnegative switched-null cushion cannot retain a nonvanishing aggregate fraction of the natural linear reservoir capacity on late dyadic bands, no matter how irregularly that occupancy is distributed among the individual cells inside each band.

The mechanism is stronger than the scalar first-lag argument of FD-229. At the next dyadic sample, the whole immediately preceding band enters with the positive coefficient `M(1)=1`, except for one negligible power-of-two endpoint. Every older band is discounted by a summable Mertens tail. After normalizing by `4^j`, the immediate band mass dominates the entire older-band mass operator with the explicit elementary bound

\[
\boxed{
\sum_{\ell\ge2} c_\ell\le\frac78<1.
}
\tag{8}
\]

No within-band regularity, periodicity, limiting profile or Riemann-sum approximation is used.

## 1. Arbitrary positive profiles collapse to dyadic band masses

Write

\[
u_j:=4^{-j}y_j.
\tag{9}
\]

The linear envelope in (2) makes `(u_j)` bounded. Indeed, using only `|M(n)|\le n`,

\[
\begin{aligned}
|y_j|
&\le
\sum_{d\le2^j} C d
\left|M\!\left(\left\lfloor\frac{2^j}{d}\right\rfloor\right)\right|\\
&\le
\sum_{d\le2^j} C d\frac{2^j}{d}
\le C4^j.
\end{aligned}
\tag{10}
\]

Now split the sum in (1) into the dyadic bands below `2^j`. The immediately preceding band is special. For

\[
2^{j-1}<d<2^j
\]

one has

\[
\left\lfloor\frac{2^j}{d}\right\rfloor=1,
\qquad M(1)=1,
\]

whereas at its lower endpoint `d=2^(j-1)` the quotient is `2` and `M(2)=0`. Hence that complete band contributes

\[
4^{-j}
\sum_{d\in B_{j-1}}
 b_dM\!\left(\left\lfloor\frac{2^j}{d}\right\rfloor\right)
=
s_{j-1}-4^{-j}b_{2^{j-1}}.
\tag{11}
\]

The incomplete top band consists only of `d=2^j`, with normalized contribution `4^(-j)b_(2^j)`. Both endpoint terms are `O(2^(-j))` by (2).

For an older band `B_(j-ell)`, `ell>=2`, every quotient lies in

\[
2^{\ell-1}\le
\left\lfloor\frac{2^j}{d}\right\rfloor
\le2^\ell.
\]

Define

\[
m_\ell=
\max_{2^{\ell-1}\le n\le2^\ell}|M(n)|,
\qquad
c_\ell=4^{1-\ell}m_\ell.
\tag{12}
\]

Because the coefficients `b_d` are nonnegative,

\[
\begin{aligned}
4^{-j}
\left|
\sum_{d\in B_{j-\ell}}
 b_dM\!\left(\left\lfloor\frac{2^j}{d}\right\rfloor\right)
\right|
&\le
4^{-j}m_\ell
\sum_{d\in B_{j-\ell}}b_d\\
&=
c_\ell s_{j-\ell}.
\end{aligned}
\tag{13}
\]

Therefore the complete cellwise geometry has been compressed, without approximation, to the scalar inequality

\[
\boxed{
|u_j-s_{j-1}|
\le
\sum_{\ell=2}^{j}c_\ell s_{j-\ell}
+O(2^{-j}).
}
\tag{14}
\]

This is the key difference from FD-229. There the scalar band ansatz was needed to identify an asymptotic Toeplitz **equality**. Here positivity gives a one-sided **mass inequality** that is valid for every arrangement inside every band.

## 2. The older-band mass operator has norm at most `7/8`

Only two short Mertens ranges need to be evaluated beyond the trivial bound. Directly,

\[
M(2)=0,
\quad
M(3)=-1,
\quad
M(4)=-1,
\]

so

\[
m_2=1.
\tag{15}
\]

Also

\[
M(4),M(5),M(6),M(7),M(8)
=(-1,-2,-1,-2,-2),
\]

and therefore

\[
m_3=2.
\tag{16}
\]

For every `ell>=4`, the trivial estimate `|M(n)|<=n` gives

\[
m_\ell\le2^\ell,
\qquad
c_\ell\le2^{2-\ell}.
\tag{17}
\]

Consequently

\[
\begin{aligned}
\sum_{\ell\ge2}c_\ell
&\le
\frac14
+
\frac18
+
\sum_{\ell\ge4}2^{2-\ell}\\
&=
\frac14+
\frac18+
\frac12\\
&=
\boxed{\frac78}.
\end{aligned}
\tag{18}
\]

The margin `1/8` is deliberately crude but completely elementary. Sharper finite Mertens values improve it substantially, but no improvement is needed for coercivity.

Notice what (18) controls. It is not the signed average kernel coefficient `h_ell` of FD-229. It controls the **worst possible absolute response of an arbitrary nonnegative profile** in an older band, expressed in units of that band's total normalized mass. The immediate band has coefficient one in those units, while all older bands together have operator mass at most `7/8`.

## 3. Switched subquadratic response still forces `u_j -> 0`

Condition (5) is exactly the same switched condition used in FD-229. Since

\[
y_{j+t}=4^{j+t}u_{j+t},
\]

we have

\[
4^{-j}(E-I)^{r_j}y_j
=
(4E-I)^{r_j}u_j
=o(1).
\tag{19}
\]

FD-229 proves that the normalized `(1,4,4)` switched system is strictly stable. Over one scheduler period its state matrix is similar to `mathcal M/64`, where

\[
\mathcal M=
\begin{pmatrix}
-10&15&-4\\
-2&4&-1\\
1&0&0
\end{pmatrix},
\]

and

\[
\rho(\mathcal M/64)
=
\frac{7+3\sqrt5}{128}
<1.
\tag{20}
\]

Because `(u_j)` is bounded by (10), an `o(1)` forcing in this stable finite-dimensional recurrence gives

\[
\boxed{u_j\longrightarrow0.}
\tag{21}
\]

No property of the within-band distribution is used in this step.

## 4. A limsup argument kills every persistent positive band mass

The sequence `(s_k)` is nonnegative and bounded. Put

\[
L=\limsup_{k\to\infty}s_k.
\tag{22}
\]

Apply (14), use `u_j->0`, and take a subsequence `k_n` with `s_(k_n)->L`, setting `j=k_n+1`. For any fixed truncation depth `R`, every index `k_n+1-ell` with `2<=ell<=R` tends to infinity, so its limsup is at most `L`. The remaining coefficient tail is summable, while `(s_k)` is globally bounded. Thus first letting `n->infinity` and then `R->infinity` gives

\[
L
\le
\left(\sum_{\ell\ge2}c_\ell\right)L.
\tag{23}
\]

Equation (18) yields

\[
L\le\frac78L,
\]

hence

\[
\boxed{L=0.}
\tag{24}
\]

Since `s_k>=0`, this is exactly (6).

Finally,

\[
\sum_{d\in B_k}d
=\left(\frac32+o(1)\right)4^k,
\]

whereas (6) says `sum_(d in B_k)b_d=o(4^(k+1))=o(4^k)`. This proves the capacity-fraction formulation (7).

The argument is robust because it uses only three features: positivity of the occupancy, the linear capacity envelope, and the exact small Mertens values needed to make the old-band mass norm strictly less than one. It does not assume any smoothness or statistical regularity inside a band.

## 5. Consequence for scale-adapted prime reservoirs

FD-226 gives source-side prime reservoirs with capacity

\[
|I_d^*\cap\mathbb P|
\asymp
B_N d,
\qquad
B_N:=\frac{N}{D\log N},
\tag{25}
\]

up to fixed constants and the already recorded Vinogradov--Korobov resolution error. A candidate positive null cushion using these cells therefore has, after division by its common source scale `B_N lambda_N`, a coefficient vector satisfying precisely the envelope (2).

FD-229 showed that one cannot hide a nonvanishing scalar fraction of capacity by changing the amplitude from dyadic band to dyadic band. FD-230 removes the stronger remaining loophole: **one also cannot hide that fraction by redistributing it arbitrarily among the individual divisor cells inside a band**. If a growing interior block retained a fixed positive aggregate fraction of its available band capacity while every switched residual were `o(4^j)` in the corresponding quadratic cushion scale, the normalized band masses would stay bounded below, contradicting (6). The same conclusion follows for finite growing blocks by the standard interior compactness argument: the coefficient tail in (18) is summable and the normalized switched recurrence is uniformly contractive.

This does not require the occupancy to be approximately proportional to `d` cell by cell. It permits cells to be empty, saturated, highly irregular, or arranged adversarially. Only the aggregate mass in each late dyadic band matters.

The implication for the FD-226 bottleneck is therefore sharper. Any positive switched-null baseline that tries to exploit the larger `d`-dependent reservoir capacities must become **aggregate-capacity sparse** along late dyadic bands. The remaining escape is no longer ordinary within-band reshuffling. It must allow the relative cushion mass itself to collapse on a growing collection of bands, use signed rather than positive baseline degrees of freedom, or abandon the asymptotically subquadratic switched-null requirement.

The theorem does not by itself show that such a depleted cushion cannot absorb the physical signed Mertens correction. Establishing that would require a lower bound on how much positive slack the correction needs across the divisor cells, or a different source-side capacity argument. So the result narrows the remaining route without claiming that the Vinogradov--Korobov depth of FD-223--FD-226 is intrinsic.

## 6. Boundary, prior art and verdict

The nonnegativity hypothesis is load-bearing. For signed `b_d`, the immediately preceding band's total mass need not control its response, and arbitrary cellwise cancellation can occur before any Mertens tail is seen. FD-229 handles signed **scalar-per-band** amplitudes, but FD-230 makes no claim for arbitrary signed cellwise profiles.

The conclusion is aggregate rather than pointwise. Sparse capacity spikes can survive the statement. For example, values supported only on one cell per dyadic band can have `b_d` of linear size at those cells while their normalized band mass still tends to zero. Such profiles are exactly in the depleted regime left open here.

The switched hypothesis is also pointwise along all sufficiently large dyadic rows. Sparse-row, averaged-row or probabilistic observation bounds are not covered, and no Mertens estimate or RH consequence is improved.

The literature audit found the expected general frameworks of strict diagonal dominance, Neumann-series inversion and convolution stability, as well as current Farey-discrepancy work, but no source-side statement matching (14)--(24). No general novelty is claimed for diagonal-dominance reasoning. No external theorem is load-bearing: the proof uses the exact divisor/Mertens response already established in FD-225, the switched contraction already established in FD-229, the elementary values of `M(n)` through `8`, and `|M(n)|<=n`. Therefore no new source anchor is required in `SOURCES.md`.

**Verdict.** The final explicit escape left by FD-229 -- arbitrary positive structure *inside* each dyadic divisor band -- does not preserve a nonzero fraction of aggregate reservoir capacity. Under switched subquadratic visibility, every nonnegative linear-capacity cushion has vanishing dyadic mass fraction. A future capacity-based countermodel must therefore become genuinely band-depleted (or use signed degrees of freedom); merely moving the positive occupancy around inside a full-capacity band is insufficient.