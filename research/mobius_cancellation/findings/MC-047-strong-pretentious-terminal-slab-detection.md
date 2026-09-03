# MC-047 — Strong power-aware pretentiousness detects the terminal-prime mass missed by the ordinary metric

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

The terminal-prime controls of `MC-045` and `MC-046` defeat the ordinary prime-harmonic pretentious distance because that distance weights a changed prime near scale `X` by only `1/X`. They do **not** defeat the stronger power-cancellation carrier of Jung--Lemke Oliver (`MC-S7`). For the exact-support multiplicative sign-twist class, the stronger carrier sees the endpoint discrepancy at exactly the target power normalization.

Let `F` be any set of primes. Define the completely multiplicative sign character

\[
\chi_F(p)=
\begin{cases}
-1,&p\in F,\\
+1,&p\notin F,
\end{cases}
\]

and put

\[
a_F(n)=\mu(n)\chi_F(n).
\tag{1}
\]

Then `a_F` is multiplicative and has exactly Möbius's square-free support. In `Re(s)>1`,

\[
A_F(s):=\sum_{n\ge1}\frac{a_F(n)}{n^s}
=\frac{R_F(s)}{\zeta(s)},
\tag{2}
\]

where

\[
R_F(s)
=\prod_{p\in F}\frac{1+p^{-s}}{1-p^{-s}}.
\tag{3}
\]

Writing

\[
a_F=\mu*h_F,
\]

the local convolution quotient is

\[
\sum_{k\ge0}h_F(p^k)z^k
=\frac{1+z}{1-z}
=1+2z+2z^2+\cdots
\qquad(p\in F),
\tag{4}
\]

and it is `1` for `p\notin F`. Thus

\[
h_F(p^k)=2
\qquad(p\in F,\ k\ge1).
\tag{5}
\]

In the reverse direction `\mu=a_F*\widetilde h_F`,

\[
\sum_{k\ge0}\widetilde h_F(p^k)z^k
=\frac{1-z}{1+z}
=1-2z+2z^2-2z^3+\cdots,
\tag{6}
\]

so `|\widetilde h_F(p^k)|=2` on the same prime powers.

Consequently the Jung--Lemke Oliver strong `beta`-pretentious convolution quantity is the same in both directions and is exactly

\[
\boxed{
H_\beta(\mu,a_F)
=H_\beta(a_F,\mu)
=2\sum_{p\in F}\frac{p^{-\beta}}{1-p^{-\beta}}.
}
\tag{7}
\]

In particular,

\[
H_\beta(\mu,a_F)<\infty
\quad\Longleftrightarrow\quad
\sum_{p\in F}p^{-\beta}<\infty.
\tag{8}
\]

This gives two useful consequences.

First, consider the scale-dependent terminal slab from `MC-045`--`MC-046`. To avoid collision with the pretentious exponent, write its slab exponent as `theta`:

\[
\frac{17}{30}<\theta<\frac34,
\qquad
H=\lfloor X^\theta\rfloor,
\qquad
F_X=\{p:X-H<p\le X\}.
\tag{9}
\]

Let `nu_X=a_{F_X}` and

\[
P_X=|F_X|\sim\frac{H}{\log X}
\]

by `MC-S32`, as already used in `MC-045`. For every fixed `beta>0`, all primes in `F_X` are `X(1+o(1))`, hence

\[
\boxed{
H_\beta(\mu,\nu_X)
=(2+o(1))\frac{P_X}{X^\beta}
=(2+o(1))\frac{X^{\theta-\beta}}{\log X}.
}
\tag{10}
\]

But `MC-045` gives the exact endpoint discrepancy

\[
\sum_{n\le X}\nu_X(n)-M(X)=2P_X.
\tag{11}
\]

Therefore

\[
\boxed{
H_\beta(\mu,\nu_X)
=(1+o(1))
\frac{\sum_{n\le X}\nu_X(n)-M(X)}{X^\beta}.
}
\tag{12}
\]

For this matched control, the strong power-aware carrier and the normalized endpoint defect have the **same asymptotic scale**. If `theta>beta`, the control creates a discrepancy polynomially larger than `X^beta`, but its strong `beta`-pretentious quantity also grows polynomially. If `theta<beta`, the strong quantity tends to zero, but the endpoint discrepancy is already `o(X^beta)`. At `theta=beta`, both are only logarithmic-border quantities of order `1/log X` after target normalization.

Thus the terminal prime slab is a decisive counterexample to ordinary one-scale pretentiousness, but **not** to power-cancellation-aware strong pretentiousness. The strengthened carrier retains precisely the prime-weight scale needed to notice this failure mode.

Second, for a **fixed** prime set `F`, suppose

\[
\sum_{p\in F}p^{-1/2-\varepsilon}<\infty
\qquad\text{for every }\varepsilon>0.
\tag{13}
\]

Then `a_F` and Möbius have equivalent RH-scale power cancellation:

\[
\boxed{
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\Longleftrightarrow\quad
\sum_{n\le x}a_F(n)=O_\varepsilon(x^{1/2+\varepsilon}).
}
\tag{14}
\]

The implication in either direction is elementary from `(4)`--`(8)`: for any fixed `delta>0`, condition `(13)` makes the absolute convolution kernel summable with weight `n^{-1/2-\delta}`, and convolution transfers a `1/2+delta` power bound in both directions. Equivalently, `MC-S7` identifies exactly this strong-pretentious regime as one in which power cancellation transfers.

Since the Möbius estimate in `(14)` is equivalent to RH, every fixed exact-support prime-sign twist satisfying `(13)` inherits the same RH barrier. A sufficiently sparse fixed prime perturbation is therefore **not** an independently easier comparator from which critical cancellation can be transferred back to Möbius; the sparse Euler correction preserves the obstruction rather than removing it.

## 1. Exact Euler and convolution structure

Because `mu(p)=-1` and `mu(p^k)=0` for `k>=2`, the local Dirichlet factor of Möbius is

\[
1-p^{-s}.
\]

For `p\notin F`, the twist does nothing. For `p\in F`, equation `(1)` changes `a_F(p)` from `-1` to `+1`, while all higher prime powers remain zero. Its local factor is therefore

\[
1+p^{-s}.
\]

Taking the ratio gives `(3)` and the formal power series `(4)`. The reverse quotient gives `(6)`. No analytic continuation or zero information is used in these coefficient identities.

For `beta>0`, absolute summability of either convolution kernel is governed by

\[
\sum_{n\ge1}\frac{|h_F(n)|}{n^\beta}
=
\prod_{p\in F}
\left(1+2\sum_{k\ge1}p^{-k\beta}\right)
=
\prod_{p\in F}\frac{1+p^{-\beta}}{1-p^{-\beta}}.
\tag{15}
\]

The logarithm of each local factor is

\[
2p^{-\beta}+O(p^{-2\beta}),
\]

with the evident finite-prime harmlessness. Hence `(15)` is finite exactly when `sum_(p in F) p^{-beta}` is finite. The reverse kernel has the same absolute Euler factors. This proves `(7)`--`(8)` and supplies the two-sided transfer used in `(14)`.

There is also an analytic interpretation, which should not be confused with an independent proof. Under `(13)`, the product `R_F(s)` converges locally uniformly and is holomorphic and nonzero throughout `Re(s)>1/2`: on every compact sub-half-plane `Re(s)>=1/2+delta`, the defining prime sum is absolutely convergent. Thus the meromorphic continuation represented by `R_F(s)/zeta(s)` has exactly the same possible poles in that half-plane as `1/zeta(s)`. The sparse twist changes a nonvanishing Euler multiplier, not the zeta zero divisor.

## 2. Exact finite-scale sensitivity of the terminal slab

For the slab `(9)`, formula `(7)` becomes

\[
H_\beta(\mu,\nu_X)
=2\sum_{X-H<p\le X}
\frac{p^{-\beta}}{1-p^{-\beta}}.
\tag{16}
\]

Uniformly across the slab,

\[
p^{-\beta}=X^{-\beta}(1+o(1)),
\qquad
(1-p^{-\beta})^{-1}=1+o(1).
\]

Together with `P_X~H/log X`, this yields `(10)`.

The scale matching `(12)` is then immediate from `(11)`. This is the key distinction from the ordinary metric audited in `MC-045` and `MC-046`. There,

\[
\mathbb D(\nu_X,\mu;X)^2
\sim 2\frac{P_X}{X}
\sim 2\frac{X^{\theta-1}}{\log X}=o(1)
\tag{17}
\]

for every admissible `theta<1`, even though the endpoint discrepancy can be much larger than `sqrt(X)`. The ordinary metric measures the slab with weight `1/p`; the strong power-aware quantity at target exponent `beta` measures it at weight `p^{-beta}`. At the square-root boundary this changes the information budget from roughly `P_X/X` to `P_X/sqrt(X)`, exactly the normalization of the endpoint perturbation itself.

For an RH-scale target `beta=1/2+epsilon`, a slab with

\[
\theta>\frac12+\varepsilon
\]

cannot remain uniformly strongly `beta`-pretentious while creating its super-target discrepancy: `(10)` diverges as a fixed positive power of `X` up to the logarithm. The `MC-045`--`MC-046` control therefore passes a genuine new falsification test against this strengthened carrier.

This does **not** prove a Möbius bound. It proves only that this particular information-loss witness no longer survives after upgrading from ordinary pretentious distance to the power-aware convolution datum.

## 3. Fixed sparse twists inherit the critical barrier

Let

\[
A_F(x)=\sum_{n\le x}a_F(n).
\]

Assume `(13)`. Fix `epsilon>0` and put

\[
\gamma=\frac12+\frac\varepsilon2.
\]

Then both absolute convolution norms

\[
\sum_n\frac{|h_F(n)|}{n^\gamma},
\qquad
\sum_n\frac{|\widetilde h_F(n)|}{n^\gamma}
\tag{18}
\]

are finite by `(13)` and `(15)`.

If

\[
M(y)=O_\varepsilon(y^\gamma),
\]

then

\[
|A_F(x)|
\le
\sum_{m\le x}|h_F(m)|\,|M(x/m)|
\ll
x^\gamma
\sum_m\frac{|h_F(m)|}{m^\gamma}
\ll_{F,\varepsilon}x^\gamma.
\tag{19}
\]

The same argument with the reverse kernel transfers the bound from `A_F` back to `M`. Since `gamma<1/2+epsilon`, this proves `(14)` after the usual epsilon relabeling.

The dependence of the constants on `F` is essential. Each terminal set `F_X` in `MC-045` is finite and therefore satisfies `(13)` when frozen, but the associated norm `(15)` varies with `X`. Equation `(10)` quantifies exactly how the relevant strong-pretentious budget deteriorates along the scale-dependent family. There is therefore no contradiction between the fixed-function equivalence `(14)` and the large finite-scale endpoint separation in `MC-045`--`MC-046`.

## 4. Prior art and novelty boundary

Jung and Lemke Oliver (`MC-S7`) explicitly introduced strengthened notions of pretentiousness because ordinary pretentiousness can fail to detect power cancellation. Their strong `beta`-pretentious convolution criterion and transfer theorem are established prior art, and their paper also contains sharp sparse-prime perturbation phenomena showing why the ordinary framework is insufficient. `MC-003` already specialized their theory to Möbius versus Liouville and found the square-layer threshold `beta=1/2`.

The Euler-factor identity `(2)`--`(6)`, absolute convolution argument, and the principle that multiplying `1/zeta(s)` by a nonvanishing Euler product preserves its zero obstruction are classical mechanisms. No novelty is claimed for them.

The durable line-specific result is the exact audit against the later `MC-045`--`MC-046` control. Those findings left "stronger prime-sensitive or prime-power-sensitive structure" as a surviving escape because ordinary pretentiousness remained asymptotically blind. Equations `(10)`--`(12)` show that the known strong power-aware carrier is **not** blind: on the exact same support-preserving multiplicative terminal perturbation, its size matches the normalized endpoint defect. Equation `(14)` then shows why a fixed sparse exact-support twist that is strongly close throughout the critical half-plane cannot serve as an easier RH-scale comparator.

A targeted literature check around power-cancellation pretentiousness, sparse prime perturbations, and modified multiplicative functions found the Jung--Lemke Oliver framework as the directly adjacent general theory. The present specialization is therefore stored as `CLASSICAL-MECHANISM` plus a Mathia-specific matched-control synthesis, not as a new theorem of analytic number theory.

## 5. Boundaries and surviving frontier

This finding closes only one branch of the post-`MC-046` escape space.

It does **not** show that strong power-aware pretentiousness yields any new unconditional estimate for actual Möbius. `MC-003` already shows that the most natural same-prime comparator, Liouville, has no independently known fixed power saving to transfer and reaches the same square-root threshold through its square convolution.

It also does not rule out:

- a comparator outside the exact-square-free-support sign-twist class with independently controlled power cancellation and a useful strong-pretentious relation to Möbius;
- signed cancellation inside a convolution kernel that is invisible to the absolute `H_beta` budget;
- a multiscale or bilinear theorem that uses the exact Möbius prime law without simply reconstructing Möbius by definition;
- a localized carrier whose success depends on arithmetic relations among neighboring prime scales rather than scalar closeness;
- a nonlinear mechanism combining the Huxley--Watt occupancy/phase structure of `MC-033`--`MC-034` with information not reducible to a strong-pretentious norm.

But the terminal-prime control can no longer be cited as evidence that **all** pretentious enrichments are too weak at square-root scale. It kills the ordinary `1/p` carrier precisely because that carrier underweights current endpoint primes. The established power-aware convolution carrier repairs that specific information loss by replacing the relevant prime cost with `p^{-beta}`, and at target exponent `beta` this is exactly the cost required to see a coherent endpoint slab.

The remaining problem is therefore not to invent a stronger distance merely to detect `MC-045`. That detection already exists in prior art. The hard question is to obtain a strong power-aware relation to some independently cancellative arithmetic object, or to exploit signed structure beyond the absolute convolution transfer, without moving the original Mertens/RH burden unchanged into the hypothesis.