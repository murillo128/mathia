# MC-117 — Fractional Mertens moments have a sharp sub-L1 transfer ceiling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

For `0<p<1`, define the time-domain fractional partial-sum quasi-mean of a path
\[
S(k)=\sum_{n\le k}a(n),\qquad a(n)\in\{-1,0,1\},
\]
by
\[
P_p(N):=
\left(\frac1N\sum_{k=0}^{N-1}|S(k)|^p\right)^{1/p},
\qquad
D_1(N):=\frac1N\sum_{k=0}^{N-1}|S(k)|.
\tag{1}
\]

Every such bounded-increment path satisfies the deterministic interpolation inequality
\[
\boxed{
D_1(N)
\ll_p
N^{(1-p)/(p+1)}
P_p(N)^{2p/(p+1)}.
}
\tag{2}
\]

Consequently, if
\[
P_p(N)\ll_\varepsilon N^{\alpha+\varepsilon},
\tag{3}
\]
then
\[
D_1(N)
\ll_\varepsilon
N^{\beta_p(\alpha)+\varepsilon},
\qquad
\boxed{
\beta_p(\alpha)=\frac{1-p+2p\alpha}{p+1}.
}
\tag{4}
\]

For the square-root fractional-moment scale `alpha=1/2`,
\[
\boxed{
\beta_p(1/2)=\frac1{p+1}>\frac12
\qquad(0<p<1).
}
\tag{5}
\]

Thus a square-root bound for a **sub-L1 time moment** does not generically transfer to the RH-complete first absolute moment from bounded increments alone. For the actual Mertens path, combining `(4)` with `MC-115` gives only the corresponding zero-free half-plane
\[
\zeta(s)\ne0
\qquad
\left(\operatorname{Re}s>\beta_p(\alpha)\right),
\tag{6}
\]
unless additional Möbius arithmetic improves the transfer.

The exponent in `(5)` is sharp even after retaining two major Möbius-facing controls from earlier findings. Fix `0<p<1` and the deterministic subpower-dense checkpoints
\[
X_j=\lfloor e^{j^2}\rfloor,
\qquad
\frac{\log X_{j+1}}{\log X_j}\longrightarrow1.
\tag{7}
\]
There exists a single deterministic sequence `a:N->{-1,0,1}` such that

\[
|a(n)|=\mu(n)^2
\quad\text{for every }n,
\tag{8}
\]

`a` has the full qualitative Chowla property, and for every `epsilon>0`,
\[
\boxed{
P_{p,a}(X_j)
\ll_{\varepsilon,p}
X_j^{1/2+\varepsilon}
}
\tag{9}
\]
for all sufficiently large `j`, while simultaneously
\[
\boxed{
D_{1,a}(X_j)
\gg_p
X_j^{1/(p+1)}.
}
\tag{10}
\]

Therefore exact square-free support, all qualitative fixed-shift Chowla limits, and RH-scale fractional `p`-moment control on a checkpoint mesh already sufficient for `MC-116` **do not** imply RH-scale mean-absolute cancellation when `p<1`. The missing structure is not scale coverage. It must control rare coherent amplitude in a way absent from those inputs; multiplicative consistency is the most important structure deliberately omitted by the matched control.

For `p>=1`, the situation changes at once: ordinary power-mean monotonicity gives `D_1(N)<=P_p(N)`. Hence an RH-scale `P_p` bound is RH-complete through `MC-115`. The time-moment order `p=1` is therefore an exact generic transfer threshold for this route.

## 1. Bounded increments give the interpolation law

Write
\[
A_p(N):=\sum_{k=0}^{N-1}|S(k)|^p,
\qquad
H:=\max_{0\le k<N}|S(k)|.
\tag{11}
\]

Since `S(0)=0` and every increment has absolute value at most one, a point at height `H` must be preceded by order `H` consecutive indices whose absolute value is still a fixed fraction of `H`. More explicitly, if `H>=2` and `|S(k_0)|=H`, then for
\[
0\le r\le\lfloor H/2\rfloor
\]
we have `k_0-r>=0` and
\[
|S(k_0-r)|\ge H-r\ge H/2.
\tag{12}
\]
Thus, with an absolute constant depending harmlessly on `p`,
\[
A_p(N)\gg_p H^{p+1},
\qquad
H\ll_p A_p(N)^{1/(p+1)}.
\tag{13}
\]

For `0<p<1`,
\[
A_1(N)
=
\sum |S(k)|^p|S(k)|^{1-p}
\le
H^{1-p}A_p(N).
\tag{14}
\]
Combining `(13)` and `(14)` gives
\[
A_1(N)\ll_p A_p(N)^{2/(p+1)}.
\tag{15}
\]
Since `A_p(N)=N P_p(N)^p`, division by `N` proves `(2)`.

Substituting `(3)` into `(2)` gives `(4)`. In particular, the interpolation route can reach the RH exponent `1/2` from a sub-L1 moment only if
\[
\alpha\le\frac{3p-1}{4p}.
\tag{16}
\]
For `p<1`, this is strictly stronger than square-root scaling `alpha=1/2`; for `p<=1/3`, even the formal non-growing exponent `alpha=0` does not reach `1/2` through this generic interpolation. This is an information-budget statement only, not a claim that the actual Möbius fractional moments cannot carry additional arithmetic information.

Equation `(15)` is a one-dimensional bounded-slope interpolation mechanism closely adjacent in spirit to classical Gagliardo-Nirenberg inequalities. Here no functional-analytic theorem is needed: the discrete proof above is elementary and remains valid in the quasi-norm regime `0<p<1`.

## 2. The exponent is pathwise sharp

The exponent in `(15)` cannot be improved for the bounded-increment class. A triangular excursion of height `H`, with `H` successive `+1` increments followed by `H` successive `-1` increments, has
\[
A_p\asymp_p H^{p+1},
\qquad
A_1\asymp H^2.
\tag{17}
\]
Hence
\[
A_1\asymp_p A_p^{2/(p+1)}.
\tag{18}
\]

If this excursion is placed in a horizon of length `N` and
\[
H=N^{a_p},
\qquad
a_p:=\frac{p+2}{2(p+1)},
\tag{19}
\]
then
\[
H^{p+1}=N^{1+p/2},
\qquad
\frac{H^2}{N}=N^{1/(p+1)}.
\tag{20}
\]
So the excursion has exactly the total `p`-mass compatible with `P_p(N)\asymp N^{1/2}`, while its first absolute mean has the exponent in `(5)`.

This abstract sharpness by itself would be too weak for the line because it ignores Möbius support and pseudorandomness. The next section keeps both.

## 3. Exact-support Chowla control saturates the same ceiling on a subpower-dense mesh

Let
\[
q(n)=\mu(n)^2
\tag{21}
\]
and start from the support-matched independent-sign process
\[
a_0(n)=q(n)\varepsilon_n,
\tag{22}
\]
where the signs on square-free positions are independent Rademacher variables. By `MC-S10`, almost every realization has the full qualitative Chowla property.

Let
\[
S_0(k)=\sum_{n\le k}a_0(n).
\]
For `0<p<1`,
\[
\mathbb E|S_0(k)|^p
\le
\bigl(\mathbb E S_0(k)^2\bigr)^{p/2}
=
Q(k)^{p/2}
\le k^{p/2},
\tag{23}
\]
where `Q(k)=sum_{n<=k}mu(n)^2`. Therefore
\[
\mathbb E\sum_{k<X_j}|S_0(k)|^p
\ll_p X_j^{1+p/2}.
\tag{24}
\]

Set
\[
L_j=\lfloor X_j^{a_p}\rfloor.
\tag{25}
\]
Because `a_p>1/2`, the square-free estimate
\[
Q(x)=\frac6{\pi^2}x+O(\sqrt x)
\tag{26}
\]
from `MC-S12` implies that, for one fixed sufficiently large constant `C_p`, the terminal interval
\[
(X_j-C_pL_j,\;X_j]
\tag{27}
\]
contains at least `3L_j` square-free integers for all large `j`. Let `I_j` be the block formed by the last `3L_j` square-free positions up to `X_j`. The blocks are disjoint for large `j`, because `L_j=o(X_j)` and `X_{j-1}/X_j=e^{-2j+1}`.

Choose one realization of `(22)` satisfying, eventually for every `j`,

\[
\sum_{k<X_j}|S_0(k)|^p
\ll_p
j^2X_j^{1+p/2},
\tag{28}
\]
\[
|S_0(\text{start}(I_j)-1)|
\le j\sqrt{X_j},
\tag{29}
\]
and
\[
\left|\sum_{n\in I_j}a_0(n)\right|
\le j\sqrt{3L_j}.
\tag{30}
\]

Such a realization exists: `(28)` follows from Markov and `(24)`, `(29)` from the second moment of the partial sum, `(30)` from the variance of a `3L_j`-term Rademacher block, and the three failure probabilities can be made summable in `j`; intersect this Borel-Cantelli event with the probability-one Chowla event.

Now alter only the signs on `I_j`. Let
\[
B_j=S_0(\text{start}(I_j)-1)
\]
and choose `sigma_j=sgn(B_j)`, taking `sigma_j=1` when `B_j=0`. Set the first `L_j` square-free signs of `I_j` equal to `sigma_j`. Choose the remaining `2L_j` signs so that the **total signed sum over `I_j` is exactly the same as for `a_0`**.

For large `j` this is always possible. By `(30)`, the required sum on the final `2L_j` signs differs from `-sigma_j L_j` by `o(L_j)`, hence lies strictly inside `[-2L_j,2L_j]`; the parity is automatically correct because both the original `3L_j`-term sum and `sigma_jL_j` have the parity of `L_j`.

Call the modified sequence `a`. The endpoint matching has an important consequence: after every block `I_j`, the modified partial sum rejoins the original path `S_0` exactly. Thus `S=S_0` outside the union of the terminal blocks.

During the first `L_j` square-free steps of `I_j`,
\[
|S|=|B_j|+1,\ |B_j|+2,\ldots,\ |B_j|+L_j,
\tag{31}
\]
so
\[
\sum_{k<X_j}|S(k)|
\ge
\frac{L_j(L_j+1)}2.
\tag{32}
\]
This gives `(10)` by `(19)`--`(20)`.

For the fractional moment, `(29)` and `a_p>1/2` give `|B_j|=o(L_j)`. The calendar length of `I_j` is `O_p(L_j)` by `(26)`, and the modified height inside it is `O(L_j)`. Hence its total `p`-mass is
\[
O_p(L_j^{p+1})
=
O_p(X_j^{1+p/2}).
\tag{33}
\]
Because `X_j=e^{j^2+o(1)}`, the sum of the corresponding contributions from all earlier blocks is dominated by the last one. Combining `(28)` and `(33)`,
\[
\sum_{k<X_j}|S(k)|^p
\ll_p
j^2X_j^{1+p/2}.
\tag{34}
\]
Taking the `p`-th root after dividing by `X_j`, and using `j^{2/p}=X_j^{o(1)}`, proves `(9)`.

Finally, the union of the modified blocks has natural density zero:
up to `X_j` its size is
\[
O\!\left(\sum_{i\le j}L_i\right)
=
O(X_j^{a_p})
=
o(X_j).
\tag{35}
\]
A density-zero sign perturbation changes any fixed finite Chowla correlation on only a density-zero set of starting indices, exactly as audited in `MC-004`. Therefore the full qualitative Chowla property of the base realization survives. Equation `(8)` is preserved pointwise because only signs on square-free positions were changed.

This proves the matched-control claim `(8)`--`(10)` with one sequence and the same subpower-dense checkpoint geometry used by `MC-116`.

## 4. What this says about the mean-absolute route

`MC-115` makes the first absolute mean RH-complete and `MC-116` shows that subpower-dense checkpoints are already enough. The present control therefore removes two possible escape explanations for a failed fractional-moment transfer:

- the obstruction is **not** caused by using power-lacunary scales; the checkpoints `(7)` satisfy the lossless logarithmic-density condition of `MC-116`;
- the obstruction is **not** removed by exact Möbius square-free support or by all qualitative fixed-shift Chowla limits.

What survives is the same structural theme already visible in `MC-001`, `MC-006`, and `MC-015`: a sparse coherent block can be invisible to qualitative finite-pattern statistics while carrying a polynomial amount of accumulated amplitude. For `p<1`, the concavity of `x^p` discounts precisely those rare large excursions, and the interpolation exponent `(5)` quantifies the resulting loss sharply.

The construction deliberately breaks multiplicativity. It therefore does **not** prove that a fractional moment theorem for the actual Möbius function cannot imply RH by a specifically arithmetic argument. Instead it gives a strict admission test: any proposed `p<1` route must identify the multiplicative, growing-scale, or otherwise source-specific mechanism that rules out the endpoint-matched coherent blocks above. Merely invoking bounded increments, exact support, qualitative Chowla, or subpower-dense scale coverage cannot close the gap.

## Prior art and novelty assessment

The bounded-increment interpolation `(12)`--`(15)` is an elementary one-dimensional concentration/interpolation argument, closely related in spirit to classical Gagliardo-Nirenberg estimates. No novelty is claimed for that analytic mechanism.

The support-matched random base and preservation of qualitative Chowla under sparse perturbation are already established within this line from Ruxi Shi, *Construction of some Chowla sequences*, Monatsh. Math. 194 (2021), 193--224, DOI `10.1007/s00605-020-01448-x` (`MC-S10`). The square-free counting input is the classical estimate recorded as `MC-S12`.

Two adjacent literature checks are important for scope:

- Nathan Ng, *The Distribution of the Summatory Function of the Möbius Function*, Proc. London Math. Soc. 89 (2004), 361--389, DOI `10.1112/S0024611504014741`, studies conditional limiting-distribution and weak-Mertens consequences under RH plus negative-moment hypotheses for zeta. It does not provide the unconditional sub-L1 time-moment transfer used here.
- Alberto Verjovsky, *How Random Is the Möbius Function? Smoothing, Probability, and the Riemann Hypothesis*, arXiv `2607.25002v2` (14 August 2026), gives RH criteria from `L^p` control of a **Laplace transform** for `1<=p<2` and from local moments of Möbius Fourier polynomials on arcs of scale `1/N`. Those moments live in transform/evaluation space and recover reciprocal-zeta or the point value `M(N)` by additional analytic structure; they are not the time-domain fractional quasi-means `(1)`.

A targeted search for Mertens `L^p`/fractional time moments did not locate an authoritative theorem identifying the `0<p<1` statistic `(1)` with RH or with the exact transfer law `(4)`. Absence from that search is not evidence of novelty. The durable contribution is the line-specific sharp information-budget calculation and matched control.

## Boundaries and falsification tests

This finding establishes no new unconditional estimate for the actual Mertens function and no new zero-free region.

- The matched control is not multiplicative. A theorem exploiting the exact multiplicative identities of `mu` may beat `(2)` and is not ruled out.
- The square-root fractional bound `(9)` is proved on the checkpoints `(7)`, not at every integer cutoff. That is intentional: those checkpoints are already dense enough for lossless first-moment interpolation under `MC-116`, so scale sparsity cannot explain the failure.
- Qualitative Chowla is preserved, but no polynomially uniform growing-shift Chowla estimate is asserted for the control.
- Equation `(6)` is only the zero-free region obtained by passing through the generic interpolation `(2)` and then `MC-115`. A different arithmetic transform could in principle extract more from the same actual-Möbius fractional moment.
- For `p>=1`, the matched obstruction disappears at the level relevant here because `P_p` directly dominates the first absolute mean.

A decisive continuation would therefore require a genuinely Möbius-specific inequality that beats `(2)` for some `p<1`, or a source-natural theorem that directly controls `P_1` rather than first compressing the path through a concave fractional moment.

## Consequences for the line

The accepted mean-absolute transfer direction is narrowed again.

A tempting weakening is now ruled out as a black-box route:
\[
\text{RH-scale sub-L1 time moment}
+
\text{exact square-free support}
+
\text{qualitative Chowla}
+
\text{subpower-dense checkpoints}
\not\Longrightarrow
\text{RH-scale first absolute mean}.
\]

The sharp generic loss is the exponent map `(4)`, and at square-root fractional scale it lands at `1/(p+1)`, not `1/2`.

This leaves a cleaner target for future work: preserve at least first-moment sensitivity to rare coherent amplitude, or prove a specifically multiplicative mechanism that prevents the endpoint-matched sparse excursions which saturate the sub-L1 ceiling. In particular, replacing `D_M` by a seemingly easier concave moment does not reduce the arithmetic burden for free.
