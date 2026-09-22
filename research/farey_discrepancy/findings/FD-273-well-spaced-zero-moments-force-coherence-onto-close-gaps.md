# FD-273 — Well-spaced zero moments force threshold coherence onto close gaps

- **Date:** 2026-09-22
- **Status:** proved literature-transfer restriction, conditional on RH
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** negative zeta-derivative moments / zero spacing / discrete logarithmic sampling / divisor-replicated packet / source-phase localization
- **Depends on:** FD-261, FD-270, FD-271, FD-272
- **Classification:** `LITERATURE+DERIVED + RH-CONDITIONAL + CLOSE-ZERO-LOCALIZATION + DISCRETE-PACKET-TRANSFER`

## Claim

FD-272 left the finite critical-zero route conditional on an upper exponent for the full reciprocal-square derivative moment

\[
J_{-1}(T)
=
\sum_{0<\gamma\le T}
|\zeta'(\tfrac12+i\gamma)|^{-2}.
\]

A published theorem of Bui, Florea and Milinovich gives enough unconditional-in-the-moment control to remove that hypothesis from the **well-spaced part** of the packet. The price is an RH assumption and a structural conclusion rather than a full packet bound: any surviving threshold-sized coherence must be supplied by zeros lying in the complementary close-gap family.

Let

\[
\beta_*:=\log_2\frac32
=0.5849625007\ldots
\]

and, on each dyadic zero-height block `(U,2U]`, let `\mathcal F(U)` be the Bui--Florea--Milinovich family of zeros satisfying their isolation condition

\[
|\gamma-\gamma'|\gg \frac1{\log U}
\]

from every other zero ordinate `\gamma'`. Assume RH. Their Theorem 1.1 with `k=1` gives, for every fixed `delta>0`,

\[
\boxed{
\sum_{\gamma\in\mathcal F(U)}
|\zeta'(\tfrac12+i\gamma)|^{-2}
\ll_\delta U^{3/2+\delta}.
}
\tag{1}
\]

Form the dyadic union `\mathcal G(T)` of these isolated zeros up to height `T`, and let `S^{\mathcal G}_{T,x}(N)` denote the FD-271 replicated depth-band mass with the zero packet restricted to `\mathcal G(T)`. Then

\[
\boxed{
\left(
\frac1X
\sum_{X<N\le2X}
S^{\mathcal G}_{x,x}(N)^2
\right)^{1/2}
\le
x^{5/4+o(1)}
}
\qquad (2\le x\le X).
\tag{2}
\]

Consequently, at the FD-261 threshold `x^(2-beta_*)`,

\[
\boxed{
\frac1X
\#\left\{
X<N\le2X:
S^{\mathcal G}_{x,x}(N)
\ge \frac12 x^{2-\beta_*}
\right\}
\le
x^{-\kappa_*+o(1)},
}
\tag{3}
\]

where

\[
\boxed{
\kappa_*
:=
\frac32-2\beta_*
=
0.3300749985\ldots>0.
}
\tag{4}
\]

Thus the well-spaced zero packet cannot be threshold-coherent on more than a polynomially sparse set of integer horizons. No conjectural full `J_{-1}` upper bound is needed for this conclusion.

Let `\mathcal C(T)` be the complementary simple critical zeros in the finite packet, and define `S^{\mathcal C}_{T,x}` analogously. Pointwise,

\[
S^{\mathrm{full}}_{T,x}(N)
\le
S^{\mathcal G}_{T,x}(N)
+
S^{\mathcal C}_{T,x}(N).
\tag{5}
\]

Therefore, outside the exceptional set in (3),

\[
S^{\mathrm{full}}_{x,x}(N)
\ge x^{2-\beta_*}
\quad\Longrightarrow\quad
\boxed{
S^{\mathcal C}_{x,x}(N)
\ge \frac12 x^{2-\beta_*}.
}
\tag{6}
\]

In words: **under RH, any threshold-sized coherence of the finite simple critical-zero packet that survives on a nonexceptional integer horizon must be carried at threshold scale by the close-zero complement.** The generic isolated zeros cannot do it.

At the RH first-row depth `x=X^(1/2+o(1))`, the well-spaced coherent exceptional set has size at most

\[
\boxed{
X^{1-\kappa_*/2+o(1)}
=
X^{\beta_*+1/4+o(1)}
=
X^{0.8349625007\ldots+o(1)}.
}
\tag{7}
\]

Combining (7) with the Pintz abundance transfer in FD-272 shows that, on arbitrarily large dyadic horizon blocks, a full-counting-exponent family of near-frontier Mertens-large horizons lies outside the well-spaced coherent exceptional set. Hence if the finite critical packet is threshold-coherent on those source-large horizons, equation (6) forces that coherence into the close-gap zero family rather than merely into an unspecified exceptional phase set.

## Evidence

The load-bearing literature input is:

Hung M. Bui, Alexandra Florea and Micah B. Milinovich, *Negative discrete moments of the derivative of the Riemann zeta-function*, Bulletin of the London Mathematical Society **56**(8) (2024), 2680--2703, DOI `10.1112/blms.13092`, especially Theorem 1.1.

Their theorem assumes RH and bounds negative derivative moments over a family of zeros whose ordinates are separated from every other zero ordinate by a fixed constant multiple of the local mean-spacing scale `1/log U`. For their notation

\[
J_{-k}(U;\mathcal F)
:=
\sum_{\gamma\in\mathcal F(U)}
|\zeta'(\rho)|^{-2k},
\]

Theorem 1.1 states, for every fixed `delta>0`,

\[
J_{-k}(U;\mathcal F)
\ll_{k,\delta}
\begin{cases}
U^{1+\delta}, & k<1/2,\\
U^{k+1/2+\delta}, & k\ge1/2.
\end{cases}
\tag{8}
\]

Taking `k=1` gives exactly (1). This is weaker than the conjectural full-packet scale `U^(1+o(1))`, but it is still comfortably below the exponent `1.830074...` that FD-272 identified as sufficient for the discrete coherence barrier.

The rest of the finding is an exact transfer of (1) through the already proved FD-271 discrete packet estimate. No zero-spacing conjecture, pair-correlation conjecture, or conjectural full `J_{-1}` upper bound enters equations (2)--(7).

## Derivation or experiment

For a simple critical zero `rho=1/2+i gamma`, retain the FD-270/FD-271 divisor-replication kernel

\[
K_\rho(d)
=
\sum_{q\mid d}
\left(q^\rho-(q-1)^\rho\right).
\]

For any selected subfamily `\mathcal A(T)` of simple critical zeros up to height `T`, define

\[
P^{\mathcal A}_{T,d}(N)
=
\sum_{\substack{0<\gamma\le T\\ \gamma\in\mathcal A(T)}}
\frac{K_\rho(d)}{\rho\zeta'(\rho)}N^{i\gamma},
\]

and let `S^{\mathcal A}_{T,x}(N)` be the corresponding sum of absolute replicated coefficients over `x<d<=2x`, with the common `N^(1/2)` amplitude normalized away exactly as in FD-271.

The proof of FD-271 is subset-stable. Its integer logarithm kernel satisfies

\[
\frac1X
\left|
\sum_{X<N\le2X}N^{i(\gamma-\gamma')}
\right|
\ll
\frac1{1+|\gamma-\gamma'|}
\qquad (T\le X),
\]

and the Schur row sum used there is bounded by the local count of **all** zeta zeros. Deleting frequencies can only decrease that row-sum majorant. Therefore, for every subfamily `\mathcal A(T)`, FD-271 gives

\[
\left(
\frac1X
\sum_{X<N\le2X}
S^{\mathcal A}_{T,x}(N)^2
\right)^{1/2}
\ll_\varepsilon
x^{1+\varepsilon}
\log(2+T)
\left(\mathcal L_{-1}^{\mathcal A}(T)\right)^{1/2},
\tag{9}
\]

where

\[
\mathcal L_{-1}^{\mathcal A}(T)
:=
\sum_{\substack{0<\gamma\le T\\ \gamma\in\mathcal A(T)}}
\frac1{(1+\gamma)|\zeta'(\rho)|^2}.
\tag{10}
\]

Now take `\mathcal A=\mathcal G`, the dyadic union of Bui--Florea--Milinovich isolated families. On a dyadic block `(U,2U]`, equation (1) and `1/(1+gamma)\asymp1/U` give

\[
\sum_{\gamma\in\mathcal F(U)}
\frac1{(1+\gamma)|\zeta'(\rho)|^2}
\ll_\delta
U^{1/2+\delta}.
\tag{11}
\]

Summing geometrically over dyadic `U<=T` yields

\[
\boxed{
\mathcal L_{-1}^{\mathcal G}(T)
\ll_\delta
T^{1/2+\delta}.
}
\tag{12}
\]

Put `T=x` in (9). Since `delta>0` and `epsilon>0` may be arbitrarily small fixed constants and logarithms are absorbed at power scale,

\[
\left(
\frac1X
\sum_{X<N\le2X}
S^{\mathcal G}_{x,x}(N)^2
\right)^{1/2}
\le
x^{1+1/4+o(1)},
\]

which is (2).

Markov at half the FD-261 threshold gives

\[
\frac1X
\#\left\{
S^{\mathcal G}_{x,x}(N)
\ge\frac12x^{2-\beta_*}
\right\}
\ll
\frac{x^{5/2+o(1)}}{x^{4-2\beta_*}}
=
x^{-(3/2-2\beta_*)+o(1)},
\]

proving (3)--(4). Numerically,

\[
2-\beta_*=1.4150374992\ldots,
\qquad
\frac54=1.25,
\]

so the RMS packet exponent remains below threshold by

\[
\frac34-\beta_*
=0.1650374992\ldots,
\]

and squaring that separation gives `kappa_*`.

For (6), decompose the finite simple critical packet into `\mathcal G` and its complement `\mathcal C`. The replicated fields add linearly before absolute values, hence triangle inequality in every depth coordinate and then over the band gives (5). If the full packet has mass at least `x^(2-beta_*)` while the good packet has mass below half of that, the close packet must supply at least the other half.

Finally impose RH, so the zero-frontier exponent in FD-272 is `Theta=1/2`, and choose the first-row depth `x=Y^(1/2+o(1))`. Equation (3) gives the count exponent in (7). FD-272, using Pintz's average-order theorem, gives arbitrarily large dyadic `Y` carrying `Y^(1-epsilon)` horizons with

\[
|M(N)|\ge Y^{1/2-\epsilon}
\]

for every fixed sufficiently small `epsilon>0`. Since

\[
\beta_*+\frac14
=0.8349625007\ldots<1,
\]

the well-spaced coherent exceptional set is polynomially too small to contain that whole source-large family. The surviving overlap must therefore satisfy the close-zero necessity (6).

## Prior art check

Bui--Florea--Milinovich explicitly study negative moments of `zeta'(rho)` on well-spaced zero subfamilies and prove the moment bound used in (1). They do **not** study the Farey/Mertens repair transform, consecutive differences, divisor replication, the integer-horizon packet `S_(T,x)(N)`, or the FD-261 positive-capacity threshold. No novelty is claimed for their negative-moment theorem or for the general observation that very small derivatives are associated with problematic zero spacing.

The derived content here is the quantitative transfer of their `k=1` exponent through the exact FD-271 discrete-horizon kernel, producing the explicit coherence exponent

\[
\kappa_*=\frac32-2\log_2(3/2),
\]

and the resulting decomposition statement that threshold coherence must be supplied by the close-gap complement.

A targeted search around negative derivative moments, well-spaced zeta zeros, Mertens large values, discrete logarithmic sampling, and divisor-replicated zero packets found the Bui--Florea--Milinovich theorem and neighboring work on zeta-derivative moments, but no prior theorem making this replicated-packet/source-phase transfer.

The literature source is load-bearing and has been added to `SOURCES.md`.

There is also a stronger conditional refinement already contained in Bui--Florea--Milinovich Theorem 1.2. Under RH plus the Farmer--Gonek--Hughes conjectural bound

\[
|S(t)|\ll\sqrt{\log t\log\log t},
\]

the same negative-moment bound holds over an enlarged family whose required zero separation is only

\[
\gg
\exp\left(
-\frac{\sqrt{\log U}}{f(U)\sqrt{\log\log U}}
\right)
\]

for a slowly growing `f`. Repeating the derivation leaves (2)--(7) unchanged but shrinks the complementary family from ordinary mean-spacing collisions to exceptionally tiny gaps. This refinement is recorded as a calibration, not used in the main claim.

## Implications

FD-272's full-packet statement required a conjectural reciprocal-square moment exponent `sigma<1.8300749985...`. FD-273 shows that **one large structural part of the packet already satisfies a sufficient exponent by published mathematics**: the well-spaced family has `sigma=3/2+o(1)` under RH. The remaining moment problem is therefore not evenly distributed over the zeros.

This materially narrows the live phase-selective route. If finite low-critical-zero coherence is to challenge the FD-260/FD-261 positive-cushion barrier at source-large integer horizons, it cannot be generated predominantly by ordinary isolated zeros. It must exploit the complementary zeros where local spacing degenerates, or leave the finite low-critical packet entirely and use the explicit-formula remainder, higher zeros, multiple zeros, or another source of one-sided repair mass.

The exponent loss is still polynomially favorable. At RH first-row depth, isolated-zero coherence can occupy at most `X^(0.8349625...+o(1))` horizons, whereas Pintz abundance supplies source-large horizons with full polynomial counting exponent one. Thus the prior vague phrase "rarer coherent subsequence" becomes a more specific structural requirement: **a successful low-zero subsequence must also be close-gap dominated.**

The Theorem 1.2 calibration sharpens that diagnosis further if one is willing to add the Farmer--Gonek--Hughes `S(t)` conjecture: then the required coherence must be carried by an extremely close-gap family rather than merely by zeros failing a fixed mean-spacing isolation test.

## Limitations

The principal limitation is that (1) assumes RH. Therefore FD-273 is a conditional localization theorem, not an RH proof ingredient that can simply be inserted into a contradiction argument without accounting for that assumption. Its value is to identify where the finite spectral mechanism would have to live if RH is true and to separate generic isolated-zero mass from the exceptional-spacing component.

The result does not bound `S^{\mathcal C}`. The close-zero complement may have very large reciprocal derivatives, and the entire purpose of the negative-moment problem is that rare small values of `|zeta'(rho)|` can dominate inverse moments. Equation (6) says that this complement is necessary for threshold coherence outside the good exceptional set; it does not say such coherence is impossible.

The Bui--Florea--Milinovich family is expected to be large, but FD-273 does not use or prove a density-one statement for it. The conclusion is driven by the moment bound on the selected family, not by a count of how many zeros are selected.

As in FD-270--FD-272, the packet is finite and contains simple critical zeros only. No control is obtained for an explicit-formula remainder, zeros above truncation height, or multiple-zero residue structure. The estimate is two-sided in absolute depth mass and creates no one-sided lower bound for the true nonnegative repair demand.

Finally, source abundance plus (3) does not rule out an infinite arithmetic subsequence on which Mertens largeness and close-zero packet coherence coincide. It only shows that ordinary well-spaced zeros cannot supply the threshold on the full-counting-exponent source-large family.

## What would change my mind

The claim would fail if Theorem 1.1 of Bui--Florea--Milinovich did not in fact give the `k=1` exponent `U^(3/2+delta)` on the stated isolated-zero family under RH, or if its family could not be assembled dyadically while preserving the reciprocal-square estimate. The published theorem states precisely that bound, and dyadic damping gives (12) directly.

The transfer would also fail if the FD-271 discrete mean-square proof relied on summing over the complete zero set in a way that is not stable under deleting frequencies. Re-expanding that proof shows the opposite: the integer phase kernel is unchanged, the local zero-count Schur majorant only decreases for a subset, and the divisor-replication estimate is pointwise in each zero. Equation (9) is therefore subset-stable.

A counterexample to (3) would require a sequence of dyadic horizon blocks on which the isolated packet exceeds half the FD-261 threshold on more than `X x^(-kappa_*+o(1))` points while (1) and the FD-271 kernel bounds remain valid. That would contradict the displayed second-moment calculation.

What would materially supersede rather than refute this finding is a theorem controlling the complementary close-zero packet strongly enough to place the **full** `J_{-1}` ledger below exponent `1.830074...`, or a direct source-phase estimate showing that close-zero residues still cannot align on the Mertens-large horizons. Either result would turn the present localization into a fuller closure of the finite spectral route.