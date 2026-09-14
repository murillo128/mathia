# RE-123 — regular CA phases resolve the full subedge packet superalgebraically

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + FULL-SUBEDGE-PACKET + CA-PHASE-COVERING + SUPERALGEBRAIC-SAMPLING + NEGATIVE/OBSTRUCTION + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch of `RE-121`--`RE-122`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and let `C` range over sufficiently large regular colossally abundant states. Write

\[
\nu_C:=\log\log C.
\]

For fixed `K>=0`, retain the complete signed subedge packet of `RE-121`,

\[
\mathcal S_K(u)
:=
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\beta:=\Re\rho<\Theta}}
 e^{-(\Theta-\beta)u}e^{i\gamma u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\qquad
\gamma:=\Im\rho .
\tag{1}
\]

The sum is real after conjugate pairing and absolutely convergent for every `u>=1`. `RE-121` gives, for the order-`K` regular-CA residual,

\[
R_K(\nu_C)
:=
B_\Theta(C)-\mathcal E_K(\nu_C)
=
\mathcal S_K(\nu_C)+O_K(\nu_C^{-K-1}).
\tag{2}
\]

`RE-122` left a two-stage finite-edge frontier: an algebraically visible residual first needs subedge zeros approaching `Theta` at polynomial ordinate height, and then their signed phases must combine without cancelling. The second requirement is genuine, but **arithmetic placement of the regular CA phases does not add another obstruction at any fixed algebraic scale**.

More precisely, fix `L>0`. For every real `A>0`, every sufficiently large `U`, and every

\[
u\in[U,U+L],
\]

there is a regular CA state `C=C(u,U)` with

\[
\boxed{
|\nu_C-u|
\ll_L
 e^{-U/2}U^{3/2}
}
\tag{3}
\]

and

\[
\boxed{
\mathcal S_K(\nu_C)-\mathcal S_K(u)
=o_{A,K,L}(U^{-A}).
}
\tag{4}
\]

Thus the actual regular-CA phase set samples the **entire infinite subedge packet**, not only a fixed finite collection of zero frequencies, with error smaller than every prescribed inverse power of the phase.

Combining (2) and (4), whenever

\[
0<A<K+1,
\tag{5}
\]

one has

\[
\boxed{
R_K(\nu_C)
=
\mathcal S_K(u)+o_{A,K,L}(U^{-A}).
}
\tag{6}
\]

Consequently, if along an unbounded sequence of windows there are continuum phases `u` for which

\[
\mathcal S_K(u)\ge cU^{-A}
\qquad\text{or}\qquad
\mathcal S_K(u)\le-cU^{-A}
\tag{7}
\]

with fixed `c>0` and `A<K+1`, then actual regular CA states realize the same signed excursion with asymptotically the same algebraic size.

This removes a live escape route after `RE-122`. A polynomial-height zero packet may still cancel because of its **internal signed spectral geometry**, but it cannot produce an algebraically visible continuum excursion that the regular CA staircase systematically misses. At every fixed algebraic order, the CA phase mesh is already too fine.

## 1. Polynomial spectral truncations have only polylogarithmic phase speed

For `T>=2`, define the ordinate-truncated packet

\[
\mathcal S_{K,T}(u)
:=
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\beta<\Theta\\
|\gamma|\le T}}
 e^{-(\Theta-\beta)u}e^{i\gamma u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{8}
\]

For `|gamma|` large and `u>=1`, the bracket in (8) is

\[
O_{K,\Theta,\sigma_0}(|\gamma|^{-2}).
\tag{9}
\]

Indeed, the leading coefficient contains two linear zero factors,

\[
\frac1{\rho(1-\rho)}=O(|\gamma|^{-2}),
\]

while every `k>=1` term is `O_K(|gamma|^{-k-1})`. Differentiating a summand with respect to `u` multiplies the exponential by

\[
-(\Theta-\beta)+i\gamma
\]

and differentiates the powers `u^{-k}`. Hence

\[
\left|
\frac{d}{du}
\left\{
 e^{-(\Theta-\beta)u}e^{i\gamma u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\right\}
\right|
\ll_K
\frac1{1+|\gamma|}.
\tag{10}
\]

The finitely many low zeros are absorbed into the implied constant.

Let `N(T)` count nontrivial zeta zeros with multiplicity. The ordinary Riemann--von Mangoldt estimate

\[
N(T)=O(T\log(eT))
\tag{11}
\]

gives by dyadic summation or partial summation

\[
\sum_{0<|\gamma|\le T}
\frac1{1+|\gamma|}
=O((\log(eT))^2).
\tag{12}
\]

Therefore

\[
\boxed{
\sup_{u\ge1}
|\mathcal S_{K,T}'(u)|
\ll_K
(\log(eT))^2.
}
\tag{13}
\]

The important feature is not merely that a finite packet is smooth. Even when the cutoff grows as an arbitrary fixed power of the CA phase, its worst possible phase speed grows only polylogarithmically. The reciprocal-square zero coefficient suppresses the increasing number and frequency of the modes strongly enough for this bound.

## 2. The omitted high-frequency packet is algebraically negligible

The same coefficient estimate gives uniformly for `u>=1`

\[
|\mathcal S_K(u)-\mathcal S_{K,T}(u)|
\ll_K
\sum_{|\gamma|>T}
\frac1{1+\gamma^2}.
\tag{14}
\]

Riemann--von Mangoldt again yields

\[
\sum_{|\gamma|>T}
\frac1{1+\gamma^2}
\ll
\frac{\log(eT)}{T},
\tag{15}
\]

so

\[
\boxed{
\sup_{u\ge1}
|\mathcal S_K(u)-\mathcal S_{K,T}(u)|
\ll_K
\frac{\log(eT)}{T}.
}
\tag{16}
\]

Fix the desired algebraic accuracy `A>0` and, for a phase window based at `U`, choose for example

\[
T_U:=U^{A+2}.
\tag{17}
\]

Then

\[
\sup_{u\ge1}
|\mathcal S_K(u)-\mathcal S_{K,T_U}(u)|
=o(U^{-A}).
\tag{18}
\]

Thus arbitrarily high zero frequencies do not create an algebraic sampling problem. To accuracy `U^{-A}`, the complete packet can always be replaced by a polynomial-height packet, and its derivative is only `O_A((log U)^2)`.

This matches the geometric conclusion of `RE-122` from the opposite direction. `RE-122` showed that a genuine order-`U^{-A}` anomaly forces access to a shrinking near-edge layer by polynomial ordinate height. Equations (16)--(18) show directly that the full higher-ordinate tail is too small to encode a separate algebraic phase-placement obstruction.

## 3. The regular CA mesh beats every polynomial zero frequency

`RE-119` proves that consecutive sufficiently large regular-CA phases have gap

\[
\delta_{\mathrm{CA}}(U)
\ll
 e^{-U/2}U^{3/2}
\tag{19}
\]

uniformly on every fixed-length phase window `[U,U+L]`. Hence every `u` in such a window has a regular-CA phase `nu_C` satisfying (3), allowing the adjacent state to lie an amount `O(delta_CA(U))` beyond an endpoint when `u` itself is at the endpoint.

Apply the mean-value theorem to the common truncation `T_U` from (17). Equations (3) and (13) give

\[
\begin{aligned}
|\mathcal S_{K,T_U}(\nu_C)-\mathcal S_{K,T_U}(u)|
&\ll
 e^{-U/2}U^{3/2}(\log U)^2\\
&=o_M(U^{-M})
\qquad\text{for every fixed }M>0.
\end{aligned}
\tag{20}
\]

Adding the two tails from (18) proves (4).

The same nearest CA state works independently of the chosen algebraic accuracy. The proof changes the auxiliary cutoff `T_U`, not the phase `nu_C`. Therefore the statement really is superalgebraic sampling of the complete packet by the fixed arithmetic phase set.

For the actual regular-CA residual, equation (2) and `nu_C=U+O_L(1)` yield

\[
R_K(\nu_C)
=
\mathcal S_K(u)
+o(U^{-A})
+O(U^{-K-1}).
\tag{21}
\]

When `A<K+1`, the last term is also `o(U^{-A})`, proving (6).

Since `K` is arbitrary but fixed, any prescribed finite algebraic order can be reached by taking the edge expansion deep enough first. What does **not** follow is a single convergent all-orders expansion with `K` growing with `U`; `RE-120`--`RE-121` only provide fixed-`K` Poincare asymptotics, and this result preserves that quantifier order.

## 4. Stress tests and exact limits of the obstruction

### A single polynomial-height near-edge zero

Suppose a relevant conjugate pair has

\[
|\gamma|\asymp U^B
\]

for fixed `B`. Its raw phase period is of order `U^{-B}`, while the CA mesh is exponentially smaller:

\[
|\gamma|\,\delta_{\mathrm{CA}}(U)
\ll
 e^{-U/2}U^{B+3/2}
=o_M(U^{-M})
\]

for every fixed `M`. Thus even a mode at the maximum polynomial height allowed by an algebraic anomaly is resolved far more finely than its oscillation scale.

### A maximally dense packet allowed by total zero counting

The conclusion is not an artifact of testing one zero at a time. With `O(T log T)` zeros up to ordinate `T`, summing their differentiated reciprocal-square coefficients gives only the `O((log T)^2)` bound in (13). Hence the entire worst-case packet allowed by ordinary zero counting still varies superalgebraically little across one CA phase gap when `T` is polynomial in `U`.

### Frequencies above every fixed polynomial

No pointwise derivative bound for the **untruncated** packet is asserted. Indeed the absolute derivative majorant would contain `sum 1/|gamma|`, which diverges. The argument instead uses the value tail (16): frequencies above `U^{A+2}` have total amplitude `o(U^{-A})`, so they are irrelevant at the requested algebraic resolution even if their individual phase velocities are enormous.

### Cancellation remains completely live

Nothing here proves that `mathcal S_K` has a positive or negative excursion of order `U^{-A}`. A polynomial-height near-edge packet may have too little weighted mass, as already emphasized by `RE-122`, or may undergo strong cancellation among its conjugate-pair phases. Equation (4) says only that **if the signed continuum packet has such an excursion, the regular CA arithmetic placement cannot hide it**.

Likewise, this result does not address the nonattained finite-edge branch of `RE-113`, the `Theta=1` branch, or any mechanism outside the `RE-121` zero-packet representation.

## 5. Representation and prior-art audit

The source data are unchanged: the actual subedge zeta zeros and the regular CA phase set. Truncating at `T_U` is only an auxiliary approximation used to compare phase scales; the final statement (4) concerns the full infinite packet. No new coordinate or independent arithmetic information is manufactured.

The zero-sum architecture itself is classical. Ramanujan's divisor-sum analysis, in the form developed effectively by Nicolas, already contains the familiar zero sum with coefficients `1/(rho(1-rho))`; the ordinary Riemann--von Mangoldt count and the reciprocal-square tail estimate are standard. Those ingredients are already bounded in `SOURCES.md`. Numerical work has also long explored zero-phase corrections along CA values. None of these observations is claimed as new.

The line-specific content is the splice of three facts that only became simultaneously available after `RE-119`--`RE-122`:

1. the actual regular CA phase mesh is `O(e^{-u/2}u^{3/2})`;
2. the complete nonisolated subedge correction is the signed packet (1) with reciprocal-square zero weights;
3. any fixed algebraic resolution can discard the high-frequency tail after a polynomial ordinate cutoff.

A targeted prior-art search across Robin/CA explicit formulas, Ramanujan--Nicolas zero sums, and CA numerical zero-phase corrections located no theorem asserting this superalgebraic sampling of the complete subedge packet by regular CA phases. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

## 6. Consequence for the finite-edge research frontier

`RE-122` separated polynomial-height **access** from useful signed phase. `RE-123` removes a possible third gate between them and the arithmetic destination: fixed-order signed spectral information is not lost when one restricts from continuum phase to actual regular CA states.

The surviving finite-edge problem is therefore sharper. If polynomial-height near-edge zeros occur, one must determine whether their weighted phases can create or suppress the required signed packet **internally**. A proof cannot rely on the idea that favorable spectral phases exist but the CA staircase is too sparse to hit them: at every fixed algebraic scale, it is not.

This is a negative result about selector placement, not a contradiction to the finite-edge hypothesis and not progress on the existence of polynomial-height edge approach itself. It narrows the remaining source question to the signed correlation/cancellation structure of the near-edge zero packet, or to genuinely new arithmetic information outside that packet.