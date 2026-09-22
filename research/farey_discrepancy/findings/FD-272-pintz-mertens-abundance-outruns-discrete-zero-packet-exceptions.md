# FD-272 — Pintz Mertens abundance outruns the discrete zero-packet exceptional set

- **Date:** 2026-09-22
- **Status:** proved source-abundance bridge + conditional zero-moment comparison
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** Mertens large-value abundance / dyadic localization / critical-zero packet / exceptional-set avoidance / source-phase coupling
- **Depends on:** FD-046, FD-070, FD-077, FD-258, FD-261, FD-270, FD-271
- **Classification:** `EXACT-DERIVED + LITERATURE-TRANSFER + FULL-COUNTING-EXPONENT + DYADIC-SOURCE-ABUNDANCE + EXCEPTIONAL-SET-AVOIDANCE + SOURCE-PHASE-COUPLING`

## Claim

FD-271 reduced threshold-sized coherence of the finite critical-zero packet to a polynomially sparse exceptional set of integer horizons. Its explicit remaining counting question was whether Mertens-large horizons could themselves be sparse enough to hide inside that set. Pintz's 2026 average-order theorem rules out that possibility at the polynomial-counting level.

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\]

and let

\[
\mathbf M(n)=\sum_{m\le n}\mu(m).
\]

For every fixed `kappa>0`, define

\[
A_\kappa(X)
:=
\#\left\{
n\le X:
|\mathbf M(n)|\ge X^{\Theta-\kappa}
\right\}.
\tag{1}
\]

Then Pintz's average-order theorem, together with the classical Mertens power frontier already used in FD-046 and FD-258, gives

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+A_\kappa(X))}{\log X}=1.
}
\tag{2}
\]

Thus near-frontier Mertens values have **full polynomial counting exponent one**. This is the direct-Mertens analogue of the physical-source abundance transfer in FD-077.

That global abundance can be localized to dyadic blocks. For every fixed `kappa,delta>0`, there are arbitrarily large `Y` for which

\[
\boxed{
\#\left\{
Y<N\le2Y:
|\mathbf M(N)|\ge Y^{\Theta-\kappa}
\right\}
\ge Y^{1-\delta}.
}
\tag{3}
\]

Now retain the FD-271 packet notation

\[
S_{T,x}(N)
=
\sum_{x<d\le2x}
\left|
N^{-1/2}G_{T,N}(d)
\right|,
\]

and write

\[
\beta_*:=\log_2\frac32.
\]

Suppose the reciprocal-square derivative moment of the simple critical-line zeros obeys

\[
J_{-1}^{\le}(T)
:=
\sum_{0<\gamma\le T}
|\zeta'(\tfrac12+i\gamma)|^{-2}
\le T^{\sigma+o(1)}
\tag{4}
\]

for some

\[
\sigma<3-2\beta_*
=1.8300749985\ldots .
\tag{5}
\]

Set

\[
c_\sigma
:=
2(1-\beta_*)-
\max(\sigma-1,0)>0.
\tag{6}
\]

For any fixed depth exponent `lambda in (0,1]`, put

\[
x=\lfloor Y^\lambda\rfloor.
\]

FD-271 then gives

\[
\#\left\{
Y<N\le2Y:
S_{x,x}(N)\ge x^{2-\beta_*}
\right\}
\le
Y^{1-c_\sigma\lambda+o(1)}.
\tag{7}
\]

Comparing (3) and (7) yields the new source--phase avoidance statement: for every fixed `epsilon>0` there are arbitrarily large dyadic scales `Y` such that

\[
\boxed{
\#\left\{
\begin{array}{c}
Y<N\le2Y:\\[2mm]
|\mathbf M(N)|\ge Y^{\Theta-\epsilon},\\[1mm]
S_{x,x}(N)<x^{2-\beta_*}
\end{array}
\right\}
\ge Y^{1-\epsilon}.
}
\tag{8}
\]

In words: under any reciprocal-square moment exponent `sigma<1.83007...`, **near-frontier Mertens-large horizons cannot be swallowed by the threshold-coherent critical-zero exceptional set**. Along suitable dyadic blocks, a full-counting-exponent family of source-large horizons lies outside it.

Under the natural calibration `sigma=1`,

\[
c_1=2(1-\beta_*)
=0.8300749985\ldots .
\tag{9}
\]

Hence the counting separation holds at every fixed polynomial divisor depth `lambda>0`. At the FD-258 first-row ceiling `lambda=1-Theta` (when `Theta<1`), the coherent packet can occupy at most

\[
Y^{1-0.8300749985\ldots(1-\Theta)+o(1)}
\tag{10}
\]

horizons, whereas the Mertens-large family has counting exponent one. In the RH-frontier calibration `Theta=1/2`, `lambda=1/2`, the exceptional exponent in (10) is exactly

\[
1-(1-\beta_*)=\beta_*
=0.5849625007\ldots,
\]

far below the source count exponent one.

This closes the **cardinality-only** source-correlation loophole left by FD-271. It does not close the full spectral route: the finite critical packet may still be threshold-coherent on a rarer source-selected subsequence, and the explicit-formula remainder, critical zeros above the truncation height, or off-critical zeros when `Theta>1/2` are not controlled by (8).

## 1. Pintz average order forces full-counting Mertens abundance

Pintz's Theorems 2.1--2.2 for the Mertens function state, with

\[
D_{\mathbf M}(X)
:=
\frac1X\int_0^X|\mathbf M(u)|\,du,
\]

that

\[
\log D_{\mathbf M}(X)
\sim
\log Z(X),
\qquad
\frac{\log Z(X)}{\log X}\to\Theta.
\tag{11}
\]

Equivalently, at power scale,

\[
D_{\mathbf M}(X)=X^{\Theta+o(1)}.
\tag{12}
\]

Because `M(u)` is constant on each unit interval away from integer endpoints, (12) has the discrete consequence

\[
\sum_{n\le X}|\mathbf M(n)|
=X^{1+\Theta+o(1)}
\tag{13}
\]

at logarithmic-exponent level.

Fix `kappa>0`. The classical power frontier used in FD-046 and proved for the dyadic increment in FD-258 implies that for every fixed `eta>0`,

\[
|\mathbf M(n)|\ll_\eta n^{\Theta+\eta}.
\tag{14}
\]

Split the sum in (13) according to the threshold in (1). For every sufficiently small fixed `eta<kappa`,

\[
\sum_{n\le X}|\mathbf M(n)|
\le
X^{1+\Theta-\kappa}
+
A_\kappa(X)\,O_\eta(X^{\Theta+\eta}).
\tag{15}
\]

On the other hand, (13) gives, for arbitrarily small fixed `eta>0` and all sufficiently large `X`,

\[
\sum_{n\le X}|\mathbf M(n)|
\ge X^{1+\Theta-\eta}.
\tag{16}
\]

Choose `eta<kappa/2`. The first term on the right of (15) is polynomially smaller than (16), so

\[
A_\kappa(X)
\gg_\eta
X^{1-2\eta}.
\tag{17}
\]

Since `eta` may be arbitrarily small and trivially `A_kappa(X)<=X`, equation (2) follows.

No distribution theorem for individual Mertens values is being imported here. The counting statement is the elementary consequence of two already anchored inputs: Pintz's absolute first moment has the full zero-frontier exponent, while no single value can exceed the same frontier by a fixed positive power.

## 2. Full global counting exponent produces dense dyadic source blocks

Fix `kappa,delta>0`. By (2), for all sufficiently large `X`,

\[
A_\kappa(X)
\ge X^{1-\delta/4}.
\tag{18}
\]

Partition `[1,X]` into `O(log X)` dyadic intervals of the form

\[
(Y,2Y].
\]

One such interval contains at least

\[
\frac{X^{1-\delta/4}}{O(\log X)}
\ge X^{1-\delta/2}
\tag{19}
\]

of the points counted by `A_kappa(X)`, for all sufficiently large `X`. Since `Y<=X`, (19) is at least `Y^(1-delta/2)`, and hence certainly at least `Y^(1-delta)`.

Every point counted in that block satisfies

\[
|\mathbf M(N)|
\ge X^{\Theta-\kappa}
\ge Y^{\Theta-\kappa},
\tag{20}
\]

provided `kappa<Theta`; if `kappa>=Theta`, the stated abundance is weaker and the conclusion is trivial. The number of points in (19) itself forces `Y\to\infty` as `X\to\infty`. This proves (3).

The dyadic localization is deliberately existential rather than uniform in every block. Pintz's current average theorem does not say that every interval `(Y,2Y]` carries frontier-near Mertens mass. For the comparison with FD-271, however, an unbounded sequence of dyadic blocks is enough to test whether the packet exceptional set can contain all source-large horizons.

## 3. The zero-packet exceptional exponent loses to source abundance

FD-271 gives, for `2<=T<=x<=Y`,

\[
\left(
\frac1Y
\sum_{Y<N\le2Y}
S_{T,x}(N)^2
\right)^{1/2}
\le
x^{1+\frac12\max(\sigma-1,0)+o(1)}
\tag{21}
\]

when (4) holds. Set `T=x`. Markov at the FD-261 threshold `x^(2-beta_*)` gives

\[
\frac1Y
\#\{Y<N\le2Y:S_{x,x}(N)\ge x^{2-\beta_*}\}
\le
x^{-c_\sigma+o(1)},
\tag{22}
\]

where `c_sigma` is exactly (6). The condition (5) is equivalent to `c_sigma>0`.

At polynomial depth `x=Y^(lambda+o(1))`, (22) becomes (7). Choose `delta` in (3) so that

\[
0<\delta<c_\sigma\lambda.
\tag{23}
\]

Then the source-large count `Y^(1-delta)` is polynomially larger than the entire packet-coherent exceptional set `Y^(1-c_sigma lambda+o(1))`. Subtracting the two sets leaves

\[
Y^{1-\delta}(1-o(1))
\]

source-large horizons with subthreshold packet mass. Taking `kappa` and `delta` smaller than an arbitrary prescribed `epsilon` proves (8).

This is exactly the counting comparison that FD-271 left open. The conclusion is stronger than merely finding one Mertens-large horizon outside the packet exception: on the selected dyadic blocks, the complement still has full polynomial counting exponent.

## 4. Why local spike persistence was not enough

FD-070 already showed that the one-Lipschitz law

\[
|\mathbf M(n+h)-\mathbf M(n)|\le|h|
\]

(or its physical-source analogue) expands a spike of height `A` into a local interval of length `asymp A`. At a zero-frontier spike `A=X^(Theta+o(1))`, that mechanism alone guarantees only about

\[
X^{\Theta+o(1)}
\]

nearby large values.

That local count does **not** beat FD-271 at the first-row depth ceiling. Under the natural `sigma=1` calibration and `lambda=1-Theta`, the coherent exceptional exponent is

\[
1-c_1(1-\Theta),
\]

and

\[
\bigl[1-c_1(1-\Theta)\bigr]-\Theta
=(1-c_1)(1-\Theta)>0
\qquad(\Theta<1).
\tag{24}
\]

So a single Lipschitz-expanded spike could still fit entirely inside the packet exceptional budget. The new ingredient is genuinely Pintz's **global average abundance**, which raises the source count exponent from `Theta` to `1` while preserving near-frontier amplitude up to an arbitrarily small fixed power loss.

This matched comparison is also a guard against a circular interpretation of (8): the result does not follow merely from the elementary bounded increment of `M`. It uses the external average-order theorem at the precise point where local persistence is quantitatively insufficient.

## 5. Prior-art boundary, limitations, and verdict

The load-bearing external input is János Pintz, *Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*, arXiv `2608.24878v2` (2026), Theorems 2.1--2.2. The paper proves that the average absolute order `D_M(X)` and the fixed-power-window maximum have the same logarithmic order as the largest zeta-zero term. That source is already anchored in `SOURCES.md` and was already used in FD-076--FD-077. The full-counting corollary (2) is elementary from Pintz plus the classical power upper frontier; no novelty is claimed for average-to-counting conversion in isolation.

The research-specific content is the composition with FD-271: the direct Mertens count is localized to dyadic horizon blocks and compared with the exact discrete zero-packet exceptional exponent. A targeted prior-art search found Pintz's average/maximal-order theorem and classical/conditional work on the distribution of `M(x)`, but no theorem coupling those large-value sets to the consecutive-difference/divisor-replicated finite zero packet used here.

There are several important boundaries.

First, (8) is **conditional on the reciprocal-square moment upper exponent** in (4). Under the natural `sigma=1` calibration the separation is large, but FD-272 does not prove that moment conjecture.

Second, `S_(x,x)` controls only the finite simple critical-line packet through height `x`. It does not control the explicit-formula remainder, zeros above `x`, or off-critical zeros when RH is false. Equation (8) therefore does not say that the full Mertens repair is subthreshold on those source-large horizons.

Third, the statement is two-sided in packet absolute mass. This is sufficient for route pruning—if the absolute packet mass is below `x^(2-beta_*)`, its negative one-sided contribution is also below threshold—but it does not create a positive lower bound for the true repair demand.

Fourth, a sparse coherent set can still be infinite. The result rules out the possibility that **all** near-frontier Mertens-large horizons are forced into that set by cardinality alone; it does not rule out a rarer arithmetic subsequence on which both source largeness and packet coherence occur.

**Verdict.** FD-271's counting loophole can be closed for the bulk of near-frontier Mertens-large horizons. Pintz's absolute-average theorem forces those horizons to have full polynomial counting exponent, while threshold-sized critical-zero coherence has strictly smaller exponent at every fixed polynomial depth whenever `sigma<1.8300749985...`. The surviving spectral route can no longer appeal merely to the scarcity of source-large horizons. It must identify a genuinely rarer source property correlated with the coherent packet, or obtain the missing one-sided depth amplification from the explicit-formula remainder/high-zero/off-critical part rather than from generic low critical-zero coherence.
