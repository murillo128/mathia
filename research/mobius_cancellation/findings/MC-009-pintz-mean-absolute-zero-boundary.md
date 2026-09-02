# MC-009 — Pintz mean-absolute Möbius exponent recovers the rightmost zero boundary

**Status:** `LITERATURE+DERIVED`, `NEEDS-AUDIT`.

## Claim

Let

\[
\vartheta=\sup_{\rho:\zeta(\rho)=0}\operatorname{Re}\rho
\]

where the supremum runs over nontrivial zeros, and define the global mean-absolute and near-end maximal Mertens statistics

\[
D_M(x)=\frac1x\int_0^x |M(u)|\,du,
\qquad
S_{M,\delta}(x)=\max_{x^{1-\delta}\le u\le x}|M(u)|
\]

for fixed `delta>0`.

A very recent preprint of Pintz (`MC-S19`) proves, in Theorem 2.2, that

\[
\log D_M(x)\sim \log S_{M,\delta}(x)\sim \log Z(x),
\tag{1}
\]

where

\[
Z(x)=\max_{\rho:\gamma>0}\frac{x^{\beta}}{\gamma},
\qquad \rho=\beta+i\gamma.
\tag{2}
\]

Together with the zero-edge definition of `vartheta`, (1) yields the exact logarithmic exponents

\[
\boxed{
\lim_{x\to\infty}\frac{\log D_M(x)}{\log x}
=
\lim_{x\to\infty}\frac{\log S_{M,\delta}(x)}{\log x}
=\vartheta.}
\tag{3}
\]

Consequently, conditional only on the correctness of the cited fresh preprint theorem,

\[
\boxed{
RH
\iff
D_M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.}
\tag{4}
\]

Equivalently,

\[
RH
\iff
D_M(x)=x^{1/2+o(1)}
\quad\text{in logarithmic order}. 
\tag{5}
\]

The important line-specific message is that **global absolute averaging does not erase the exponent of the rightmost zeta-zero boundary**. A hypothetical zero with real part `beta>1/2` forces the mean absolute size of `M` to have logarithmic exponent at least `beta`; it cannot be hidden merely by sign oscillation or by averaging `|M|` over `[0,x]`.

This does not provide a new proof route by itself. Pintz's theorem is analytic zero-sensitive input, not an independently easier arithmetic estimate for `D_M`. But it changes the target hierarchy for this line: an RH-scale **mean-absolute** bound is already enough to recover RH, even though it is formally much weaker than a pointwise RH-scale bound for `M(x)`.

## 1. The zero-edge exponent of `Z(x)` is exactly `vartheta`

The deduction from Pintz's Theorem 2.2 to (3) is elementary and does not use an additional analytic theorem.

For every zero `rho=beta+i gamma` with `gamma>0`,

\[
\frac{x^\beta}{\gamma}\le C_\rho x^\vartheta,
\]

so

\[
\limsup_{x\to\infty}\frac{\log Z(x)}{\log x}\le\vartheta.
\tag{6}
\]

Conversely, for any `eta>0`, the definition of the supremum supplies a fixed zero `rho_eta=beta_eta+i gamma_eta` with

\[
\beta_\eta>\vartheta-\eta.
\]

Then

\[
Z(x)\ge\frac{x^{\beta_\eta}}{\gamma_\eta},
\]

hence

\[
\liminf_{x\to\infty}\frac{\log Z(x)}{\log x}
\ge \vartheta-\eta.
\]

Letting `eta` tend to zero gives

\[
\frac{\log Z(x)}{\log x}\longrightarrow\vartheta.
\tag{7}
\]

Combining (7) with (1) proves (3). Pintz records the analogous calculation for the prime-number-theorem error term earlier in the same paper; the present step simply applies his new Möbius theorem.

Equation (3) is equivalent to the two-sided exponent statement that for every fixed `epsilon>0`, eventually

\[
x^{\vartheta-\varepsilon}
\le D_M(x)
\le x^{\vartheta+\varepsilon},
\tag{8}
\]

up to changing the threshold in `x`. Thus the mean-absolute statistic determines `vartheta` exactly at the power-law level.

## 2. Why the mean-absolute criterion is genuinely weaker than the classical pointwise criterion

The classical Mertens RH criterion uses

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\tag{9}
\]

Pointwise control (9) trivially implies the corresponding bound for `D_M`, so RH gives the forward implication in (4) without needing Pintz's new theorem.

The reverse implication is where the new theorem matters. An estimate on

\[
\frac1x\int_0^x|M(u)|\,du
\]

places no generic pointwise bound of the same exponent on `M`; sparse spikes can be invisible to an average. Nevertheless (3) says that such spikes cannot carry an off-critical zero while leaving the **global mean exponent** below that zero's real part. If `D_M(x)=O_\varepsilon(x^{1/2+\varepsilon})` for all `epsilon`, then (3) forces `vartheta<=1/2`. Since functional-equation symmetry of the nontrivial zero set gives `vartheta>=1/2` and `vartheta=1/2` exactly when all nontrivial zeros lie on the critical line, RH follows.

This is an information-fidelity statement specific to the Möbius/zero interface: absolute averaging destroys sign and location information but, according to the theorem, preserves the extremal zero **exponent**.

## 3. Relation to the local-to-global obstruction chain

This finding does not contradict `MC-001` or `MC-006`.

`MC-001` proves that almost-all short-interval magnitude plus exceptional-set measure, used only through a triangle-inequality transfer, gives an error budget `eta X+B+H`; the currently proved logarithmic rates do not reach any fixed power saving. `MC-006` similarly shows that the current averaged two-point Chowla rate, fed through black-box van der Corput, gives only logarithmic global saving.

The new literature result changes **what would be sufficient at the end of a successful transfer**, not the strength of the existing local inputs. A local/multiscale argument no longer needs to reconstruct the pointwise Mertens bound if it can instead prove

\[
D_M(x)\ll_\varepsilon x^{1/2+\varepsilon}.
\tag{10}
\]

But present almost-all and averaged-correlation theorems still do not provide the polynomial information needed to establish (10) by the black-box routes already audited.

This suggests a narrower target for future local-to-global work: preserve enough **signed or multiscale organization** to control the first absolute moment of the global partial-sum process, rather than demanding uniform pointwise control. Whether this weaker target is materially more accessible is open; the Pintz theorem only certifies that it is sufficient.

## 4. Off-critical zeros have a rigid averaged signature

The README asks whether a hypothetical off-critical zero forces a detectable signature in Möbius observables beyond a tautological restatement of `1/zeta(s)`. Theorem 2.2 supplies such a signature at the level of a natural global statistic:

\[
\vartheta>\frac12
\quad\Longrightarrow\quad
D_M(x)=x^{\vartheta+o(1)}
\quad\text{in logarithmic order}.
\tag{11}
\]

It simultaneously gives

\[
S_{M,\delta}(x)=x^{\vartheta+o(1)},
\tag{12}
\]

for every fixed positive `delta`. Thus the rightmost zero boundary controls both the average absolute Mertens size and the maximum occurring in the terminal multiplicative window `[x^{1-delta},x]`, to the same logarithmic exponent.

This is stronger than merely saying that one off-critical zero gives an `Omega(x^{beta-epsilon})` sequence of exceptional values. It identifies the asymptotic power exponent of a global average and a broad near-end maximum with the extremal zero boundary.

However, the mechanism remains explicitly analytic. Pintz's proof works through `1/zeta(s)`, zero-free information and complex-analytic estimates. It therefore does not satisfy the line's stronger ambition of deriving RH-scale cancellation from independently controlled arithmetic structure; it supplies a precise target and a fidelity theorem for such a route.

## Prior art and novelty assessment

`MC-S19` is the primary source and is unusually fresh: arXiv `2608.24878`, submitted 25 August 2026 and revised 26 August 2026. Its abstract states that the mean absolute order of `M(x)` agrees to high accuracy with the largest zero-driven term, and Theorems 2.1–2.2 give the precise asymptotic comparison used above.

The paper itself traces the mean-absolute lower-bound program back to Pintz's 1982/83 work and presents the new theorem as the Möbius analogue of his earlier sharp results for the prime-number-theorem error term. No novelty is claimed here for Pintz's theorem, for the classical RH-equivalent pointwise Mertens bound, or for the definition of `vartheta`.

The Mathia-derived content is only the explicit research-facing extraction of (3)–(5) and its placement against the existing `MC-001`/`MC-006` information-budget obstructions. Because the source is a brand-new preprint and its long proof has not been independently reconstructed in this run, the finding is deliberately marked `NEEDS-AUDIT` rather than treating the theorem as independently verified mathematics.

## Boundaries and falsification tests

This finding does **not** improve the unconditional upper bound for `M(x)` or `D_M(x)`. It does not show that the mean-absolute target (10) is easy, or even easier in practice than the pointwise target.

It also does not provide an elementary implication from a mean bound to pointwise cancellation. The reverse implication in (4) depends essentially on Pintz's theorem identifying the mean exponent with the zero boundary.

Finite computations of `M(x)` cannot validate the asymptotic theorem. The decisive audit is theorem-level: independently reconstruct the hypotheses and proof of Pintz's Theorems 2.1–2.2, with particular attention to the `vartheta=1` case that the paper identifies as the difficult new regime, and confirm that no unstated simplicity, multiplicity, zero-density, or RH assumption enters the asymptotic comparison.

If that audit fails, (3)–(5) must be withdrawn or narrowed. If it succeeds, the durable conclusion is not a new RH proof but a sharper target hierarchy:

```text
pointwise RH-scale Mertens bound
        =>
mean-absolute RH-scale Mertens bound
        =>
rightmost-zero boundary theta = 1/2
        =>
RH,
```

where the second implication is nontrivial literature input and the first is elementary.

## Consequences for the line

The local-to-global frontier should distinguish two endpoints:

- the classical strong endpoint `M(x)=O_epsilon(x^(1/2+epsilon))`;
- the weaker but still RH-complete endpoint `D_M(x)=O_epsilon(x^(1/2+epsilon))` supplied by `MC-S19`.

A future short-interval, correlation, bilinear or multiscale mechanism should therefore be tested first against the mean-absolute endpoint. If it cannot deliver polynomial control even there, it cannot reach RH through this route. If it can, Pintz's theorem gives an exact analytic bridge from that weaker arithmetic target to the zero boundary.

This is potentially a useful reduction in required output strength, but not a reduction in the currently proved input strength.