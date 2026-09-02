# MC-008 — Analytic nonmasking is weaker than absolute inversion for a 2-adic Möbius comparator

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`.

## Claim

There is an explicit `1`-bounded multiplicative function `g_2` which agrees with Möbius at every prime and for which the absolute reverse-transfer threshold from `MC-007` is as bad as possible, yet whose RH-scale summatory bound is still equivalent to RH.

Define `g_2` prime-power-wise by

\[
g_2(p)=-1\qquad\text{for every prime }p,
\]

\[
g_2(p^k)=0\quad(p\text{ odd},\ k\ge2),
\qquad
g_2(2^k)=-1\quad(k\ge2).
\tag{1}
\]

Thus `g_2` differs from `mu` only on powers of `2` of exponent at least two. Put

\[
S_2(x)=\sum_{n\le x}g_2(n).
\]

Then

\[
\boxed{
RH
\iff
S_2(x)=O_\varepsilon(x^{1/2+\varepsilon})
\text{ for every }\varepsilon>0.
}
\tag{2}
\]

At the same time, if `h=1*g_2` is the transfer kernel in `g_2=mu*h`, its local generating series is

\[
H_2(z)=\sum_{k\ge0}h(2^k)z^k
      =\frac{1-2z}{(1-z)^2},
\tag{3}
\]

so `H_2` has a zero at `z=1/2`. The Dirichlet inverse therefore has coefficients growing like `2^k`, and its absolute Dirichlet series converges only for `Re(s)>1`. In the notation of `MC-007`,

\[
\vartheta(g_2)=1.
\tag{4}
\]

Hence the black-box absolute-value inversion of `MC-007` cannot recover any fixed exponent below `1` from a bound on `S_2`. Equation (2) nevertheless shows that this failure of absolute inversion is **not** a failure of RH sensitivity.

The distinction is exact: for RH inference it is enough that the transfer factor not **mask** hypothetical zeta zeros in the open right critical half-strip; coefficientwise absolute invertibility is a strictly stronger requirement.

## 1. Exact dyadic convolution

At every odd prime, `g_2` has the same local factor as Möbius. At `p=2`, writing `z=2^{-s}` formally,

\[
G_{2,2}(z)
=1-z-z^2-z^3-\cdots
=\frac{1-2z}{1-z}.
\tag{5}
\]

The Möbius local factor is `1-z`, so the quotient is exactly (3):

\[
H_2(z)=\frac{G_{2,2}(z)}{1-z}
      =\frac{1-2z}{(1-z)^2}.
\]

Expanding gives

\[
h(1)=1,\qquad h(2)=0,\qquad h(2^k)=1-k\quad(k\ge2),
\tag{6}
\]

and `h(n)=0` for integers having an odd prime factor. Thus

\[
S_2(x)
=M(x)-\sum_{k\ge2}(k-1)M(x/2^k),
\tag{7}
\]

with the sum finite for each `x`. This is a genuinely signed dyadic filter of the Mertens function.

Its inverse is very different. From

\[
\frac1{H_2(z)}
=\frac{(1-z)^2}{1-2z}
=1+\sum_{k\ge2}2^{k-2}z^k,
\tag{8}
\]

the inverse kernel `k=h^{-1}` satisfies

\[
k(1)=1,\qquad k(2)=0,\qquad k(2^j)=2^{j-2}\quad(j\ge2).
\tag{9}
\]

Therefore

\[
\sum_n\frac{|k(n)|}{n^\sigma}
=1+\sum_{j\ge2}\frac{2^{j-2}}{2^{j\sigma}}
\]

converges if and only if `sigma>1`. This proves (4) directly and makes the loss in absolute reverse transfer concrete rather than merely locating a local zero.

## 2. The Dirichlet-series transfer factor does not mask nontrivial zeros

For `Re(s)>1`, Euler products give

\[
F_2(s)
:=\sum_{n\ge1}\frac{g_2(n)}{n^s}
=\frac{A_2(s)}{\zeta(s)},
\tag{10}
\]

where

\[
A_2(s)
=H_2(2^{-s})
=\frac{1-2^{1-s}}{(1-2^{-s})^2}.
\tag{11}
\]

The numerator in (11) is the classical alternating-zeta prefactor recorded in `MC-S18`. Its zeros satisfy

\[
2^{1-s}=1,
\]

hence

\[
s=1-\frac{2\pi i m}{\log2},\qquad m\in\mathbb Z,
\tag{12}
\]

and all lie on `Re(s)=1`. The denominator vanishes only when

\[
s=-\frac{2\pi i m}{\log2},
\]

on `Re(s)=0`. Consequently `A_2` is holomorphic and zero-free throughout

\[
\frac12<\operatorname{Re}s<1.
\tag{13}
\]

This is the key difference between **analytic nonmasking** and the absolute inverse criterion. The same zero `z=1/2` that makes the inverse coefficients grow exponentially becomes, after the substitution `z=2^{-s}`, a vertical family on the boundary `Re(s)=1`; it does not coincide with any point of the open critical strip.

## 3. RH implies the comparator bound

Assume RH. The classical Mertens criterion gives, for every `epsilon>0`,

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{14}
\]

Using (7), for any fixed `alpha>1/2`,

\[
|S_2(x)|
\le Cx^\alpha
\left(1+\sum_{k\ge2}(k-1)2^{-k\alpha}\right)
\ll_\alpha x^\alpha,
\tag{15}
\]

because the forward kernel has absolutely summable dyadic mass for every positive exponent. Taking `alpha=1/2+epsilon` proves the forward direction of (2).

No reverse kernel is needed in this direction.

## 4. The comparator bound implies RH without absolute inversion

Assume now that for every `epsilon>0`,

\[
S_2(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{16}
\]

By partial summation, (16) implies that the Dirichlet series `F_2(s)` converges locally uniformly and defines a holomorphic function in every half-plane `Re(s)>1/2+epsilon`; taking the union over `epsilon` gives holomorphy on

\[
\operatorname{Re}s>\frac12.
\tag{17}
\]

On `Re(s)>1`, (10) holds by absolute convergence. The right-hand side `A_2(s)/zeta(s)` is meromorphic on `Re(s)>1/2` and agrees there with the holomorphic `F_2` by uniqueness of meromorphic continuation.

If `rho` were a zero of `zeta` with

\[
\frac12<\operatorname{Re}\rho<1,
\]

then (13) gives `A_2(rho) != 0`, so `A_2(s)/zeta(s)` would have a pole at `rho`. That contradicts (17). Hence zeta has no zero in the open right half of the critical strip. Together with the classical location of nontrivial zeros in `0<Re(s)<1` and the functional-equation symmetry `rho -> 1-rho`, all nontrivial zeros must lie on `Re(s)=1/2`. This proves RH and completes (2).

More generally, the same argument yields a useful **masking lemma**. Suppose `g=mu*h`, the Dirichlet series

\[
H(s)=\sum_n h(n)n^{-s}
\]

is holomorphic on `Re(s)>1/2`, and `S_g(x)=O_\varepsilon(x^{1/2+\varepsilon})`. Then every zeta zero `rho` with `Re(rho)>1/2` must also be a zero of `H`, with at least the multiplicity needed to remove the pole of `H/zeta`. Therefore a zero-free transfer factor on the open right critical strip is sufficient for the comparator bound to imply RH. Absolute convergence of the Dirichlet inverse of `h` is not required.

## 5. Why this materially refines MC-007

`MC-007` proved that all large-prime local factors are automatically harmless for absolute reverse transfer above `1/2`, while `p=2,3` can produce genuine local zeros and raise the absolute inverse threshold. Its explicit `p=2` example is exactly the local rule used in (1), and it correctly gives threshold `1`.

The present result does not contradict that finding. It separates two questions that the absolute-value transfer cannot distinguish:

1. **Pointwise recoverability:** can a bound on `S_g` be pushed back to a bound on `M` by convolving with an absolutely summable inverse kernel?
2. **Zero-divisor fidelity:** does the auxiliary Dirichlet series remain sensitive to every hypothetical off-critical zeta zero, or can the transfer factor cancel one?

For `g_2`, the first answer is negative throughout exponents below `1`, while the second answer is positive throughout the nontrivial right critical half-strip. Thus `vartheta(g)` is a sufficient threshold for direct coefficientwise recovery, but it is not the correct threshold for preserving RH information.

This is a concrete signed/multiscale escape from the absolute-inversion obstruction left open at the end of `MC-007`. It does **not** provide an easier proof of the required comparator bound; it identifies a weaker structural condition that an independently tractable comparator would need to satisfy.

## Prior art and novelty assessment

The convolution algebra and the factor `1-2^{1-s}` are classical. `MC-S18` records the standard Dirichlet-eta relation, so no novelty is claimed for the location of the zeros in (12). Jung and Lemke Oliver (`MC-S7`) explicitly show that small-prime convolution convergence is essential for their power-cancellation transfer theorems and give a prime-`2` example where changing one local factor radically changes summatory cancellation. Their result is the closest direct prior-art warning against ignoring the local inverse kernel.

There is also a broader adjacent nonvanishing program. Venturini (`MC-S17`) proves, in a different setting of bounded **completely** multiplicative coefficients, that holomorphic continuation of an auxiliary Dirichlet series can force a zero-free half-plane for zeta. That theorem does not apply directly to `g_2`, which is not completely multiplicative, and it does not supply the local factor (11); it does show that the general strategy “auxiliary multiplicative Dirichlet-series analyticity constrains zeta zeros” is established prior art.

Accordingly, no claim is made that (2) is a new RH criterion in analytic number theory. A targeted search found the classical eta prefactor, Jung–Lemke Oliver's small-prime transfer obstruction, and Venturini's adjacent nonvanishing principle. The durable Mathia contribution is the **line-specific separation of absolute recoverability from zero-divisor fidelity inside the exact same-prime comparator family of MC-007**, together with an explicit witness where the two thresholds differ maximally (`1` versus `1/2`). This changes the structural interpretation of the remaining small-prime escape without claiming a standalone new theorem.

## Boundaries and falsification tests

This result does not improve the best known unconditional bound for `M(x)` or for `S_2(x)`. Since (2) is an equivalence, proving the RH-scale estimate for `g_2` may be exactly as difficult as proving RH by any other route.

It also does not say that every singular small-prime comparator is harmless. If a transfer factor `H(s)` has zeros inside `1/2<Re(s)<1`, those zeros can in principle mask zeta poles in `H/zeta`, and an RH-scale bound for the comparator alone would not exclude coincident zeta zeros. The zero set of the transfer factor must therefore be audited as part of the information budget.

Nor does analytic nonmasking produce a pointwise formula recovering `M(x)` with the same exponent. Equation (8) shows precisely why direct absolute inversion fails here.

The main claim can be falsified by any one of three exact checks:

- a failure of the local Euler-factor calculation (5)–(11);
- a zero of `A_2(s)` in the open strip `1/2<Re(s)<1`;
- a counterexample to the standard partial-summation implication from (16) to holomorphy of `F_2` on `Re(s)>1/2`.

All three reduce to elementary or classical analytic facts, so the result is exact rather than heuristic.

## Consequences for the research line

The comparator frontier after `MC-007` should not require absolute inverse convergence as a universal gate. For RH-sensitive auxiliary functions, the weaker invariant is the **zero mask of the transfer factor** in the critical strip.

A genuinely productive next comparator would need two properties simultaneously:

- its summatory cancellation is independently more tractable than Möbius cancellation; and
- its transfer factor is nonmasking in `1/2<Re(s)<1`, or a finite family of comparators has complementary masks with empty common intersection there.

The first condition is the hard arithmetic content; the second is now an exact, cheaply auditable fidelity condition. `g_2` supplies the minimal test case showing that signed local filtering can preserve all RH-relevant zero information even when coefficientwise reverse recovery is catastrophically ill-conditioned.