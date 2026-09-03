# WI-116 — the Tsang bad-pair tail needs microscopic density slope two

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It closes the most direct zero-density repair left by WI-115: the published Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB) mechanism for discarding pairs outside the Tsang positivity strip requires a microscopic horizontal zero-density decay with exponent slope `2` and a little-`o` saving. The strongest established near-critical-line density estimates located in the audit have strictly smaller microscopic slope and give only an `O(T log T)`-scale exceptional population at fixed normalized depth. They therefore cannot be inserted as a black-box replacement for the BGSTB strong-density hypothesis.

The same audit also materially narrows the fallback “use known higher vertical correlations to rule out lattice screening” route. Lagarias--Rodgers construct a half-lattice point process matching **all** presently proved band-limited `n`-point GUE correlation statistics. This does not model the off-line same-height multiplicities of WI-115 and hence is not itself a screened zeta counterexample, but it proves that the Montgomery--Hejhal--Rudnick--Sarnak higher-correlation theorems do not contain a generic anti-lattice principle. A successful horizontal-rigidity argument must therefore use more than the currently established band-limited vertical correlation identities.

## 1. The exact BGSTB tail that must be controlled

The primary source is S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376; arXiv:2306.04799, especially §6:

https://arxiv.org/html/2306.04799#S6

Write `L=log T`. Their equation (6.3) isolates the contribution

\[
\mathcal S(T)
=2\pi\operatorname{Re}
\sum_{\substack{\rho,\rho'\\0<\gamma,\gamma'\le T\\
|\beta-\beta'|\ge1/L}}
K\!\left(-i(\rho-\rho')L\right)w(\rho-\rho')
\tag{1}
\]

and needs

\[
\boxed{\mathcal S(T)=o(TL).}
\tag{2}
\]

Using

\[
K(-i(\rho-\rho')L)
\ll
\frac{T^{|\beta-\beta'|}}
{((\beta-\beta')L)^2+((\gamma-\gamma')L)^2}
\tag{3}
\]

plus symmetry about `Re s=1/2`, they reduce the tail to

\[
\boxed{
\mathcal S(T)
\ll
\sum_{\substack{\beta\ge1/2+1/(2L)\\0<\gamma\le T}}
T^{2\beta-1}.
}
\tag{4}
\]

Their hypothesis (6.2) is the uniform **strong density hypothesis**

\[
\boxed{
N(\sigma,T)=o\!\left(T^{2(1-\sigma)}\right)
}
\tag{5}
\]

for

\[
\frac12+\frac1{2L}\le\sigma\le\frac{25}{32}+\eta.
\]

Together with Bourgain's estimate farther right, partial summation converts (5) into (2). The current BGSTB follow-up, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545v3, revised 1 September 2026, retains exactly this logical gate: its narrow-box theorem obtains termwise Tsang positivity directly, while Remark 3 says the box can instead be replaced by a suitably strong Zero Density Hypothesis.

Thus the useful question is not merely whether some zero-density theorem exists. It is whether unconditional density information decays fast enough at horizontal distance `Theta(1/L)` to make the weighted reservoir (4) sublinear relative to `TL`.

## 2. Normalized horizontal depth exposes the required slope exactly

Parameterize the right half of the zero set by normalized depth

\[
a=(\beta-\tfrac12)L,
\qquad
\beta=\frac12+\frac{a}{L}.
\tag{6}
\]

Then the BGSTB weight in (4) is

\[
T^{2\beta-1}=e^{2a}.
\tag{7}
\]

The strong density hypothesis (5) becomes, at this scale,

\[
N\!\left(\frac12+\frac aL,T\right)
=o\!\left(Te^{-2a}\right).
\tag{8}
\]

The exponent `2` is therefore load-bearing: it exactly cancels the `e^{2a}` growth of the complex Tsang kernel after the symmetry reduction. The remaining little-`o` is what makes the integrated tail `o(TL)` rather than merely another main-term-sized contribution.

This gives a clean interface criterion. A black-box density theorem of the schematic form

\[
N\!\left(\frac12+\frac aL,T\right)
\lesssim TL^B e^{-\kappa a}
\tag{9}
\]

cannot reproduce the BGSTB argument when `kappa<2`; even before logarithmic losses, weighting by (7) leaves `e^{(2-kappa)a}` rather than decay. If `kappa=2` but only a big-`O` estimate is available, the exact cancellation still does not provide the little-`o` in (2) without an additional saving.

## 3. Published microscopic zero-density gives only fixed-factor suppression

A particularly clean unconditional near-line theorem is Kenneth Maples and Brad Rodgers, **Bootstrapped zero density estimates and a central limit theorem for the zeros of the zeta function**, *International Journal of Number Theory* 11 (2015), 2087--2107; arXiv:1404.3080v2:

https://arxiv.org/html/1404.3080

Their Theorem 2.4 states that for every fixed `c in (0,1)`,

\[
N(\sigma,T)
\ll_c
(T\log T)T^{-c(\sigma-1/2)}.
\tag{10}
\]

At the fixed microscopic box edge

\[
\sigma_b=\frac12+\frac{b}{2L},
\tag{11}
\]

this becomes **exactly**

\[
\boxed{
N(\sigma_b,T)
\ll_c
(TL)e^{-cb/2}.
}
\tag{12}
\]

For fixed `b`, the factor `e^{-cb/2}` is only a constant. It does not tend to zero with `T`. Their Proposition 2.5 bootstraps the same density input to all fixed local moments,

\[
\frac1T\int_0^T
\left|
N(\sigma,t+H/L)-N(\sigma,t)
\right|^kdt
\ll_{c,k}
H^kT^{-c(\sigma-1/2)},
\tag{13}
\]

but at (11) the right-hand decay is again only `e^{-cb/2}`. Thus even the local `L^k` refinement does not turn a fixed-width Tsang strip into a density-zero exceptional set.

The broader zero-density audit points in the same direction. Ingham's classical estimate

\[
N(\sigma,T)
\ll
T^{3(1-\sigma)/(2-\sigma)}L^5
\tag{14}
\]

has, at `sigma=1/2+a/L`,

\[
\frac{3(1-\sigma)}{2-\sigma}
=1-\frac{4a}{3L-2a},
\tag{15}
\]

and hence microscopic exponential slope `4/3+o(1)`, still strictly below the required `2`, with additional logarithmic loss. The 2025 systematic frontier audit of Tao--Trudgian--Yang, **New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach**, arXiv:2501.16779, records Ingham's exponent as the current best fixed-`sigma` `A(sigma)` bound from `1/2` through `0.7`. Their newer improvements farther right do not provide the uniform strong-density statement (5) at the `1/L` box edge.

Accordingly, no published theorem located in the audit supplies the particular interface

\[
N\!\left(\frac12+\frac aL,T\right)
=o(Te^{-2a})
\tag{16}
\]

uniformly over the range needed by (4). This is **not** a claim that every conceivable use of zero-density information is impossible. It is the narrower decisive statement that the direct BGSTB substitution “replace the box by currently established zero density and discard the bad Tsang pairs” does not close.

## 4. Known band-limited higher vertical correlations do not provide a generic anti-lattice theorem

A second natural response to WI-115 is to abandon pair-level control and invoke the established higher correlations of zeta ordinates. There is strong prior art showing that this cannot be treated as a generic vertical anti-lattice principle.

Jeffrey C. Lagarias and Brad Rodgers, **Higher Correlations and the Alternative Hypothesis**, *Quarterly Journal of Mathematics* 71 (2020), 257--280, DOI 10.1093/qmathj/haz043; arXiv:1905.12123:

https://academic.oup.com/qjmath/article/71/1/257/5714711

Their Theorem 2.4 recalls the proved higher-correlation information: assuming RH, the Montgomery (`n=2`), Hejhal (`n=3`) and Rudnick--Sarnak (`n>3`) correlations agree with the sine/GUE process for Schwartz test functions whose Fourier support lies in the standard band-limited region, in particular the nontrivial region

\[
|\xi_1|+\cdots+|\xi_n|<2.
\tag{17}
\]

Lagarias--Rodgers then construct the `1/2`-discrete sine process and prove in Theorem 4.7 that, after a random translation, it is a simple stationary point process supported on a translate of

\[
\frac12\mathbb Z
\tag{18}
\]

whose `n`-point correlations agree with the sine process for **every `n>=1` and every test function in exactly the known band-limited class**. All spacings in every realization are half-integers. Their construction is an explicit proof that all presently known band-limited higher vertical correlations remain compatible with a rigid lattice-supported Alternative Hypothesis.

The relevance to WI-007/WI-115 is a scope barrier, not an identification of the two models. The Lagarias--Rodgers process is simple and concerns ordinates only; it does **not** contain the same-height off-line mirror pairs or multiplicities used by the WI screening construction. Therefore it does not prove that the exact WI-005/WI-006 screened configuration satisfies every known higher-correlation theorem. What it does prove is enough to kill the weaker hoped-for inference

\[
\boxed{
\text{known band-limited higher vertical correlations}
\Longrightarrow
\text{generic nonlattice / anti-aliasing rigidity}.
}
\tag{19}
\]

Any higher-correlation repair must identify a more specific statistic that is incompatible with the **actual screened multiplicity geometry**; merely citing the existing Montgomery--Hejhal--Rudnick--Sarnak band-limited correlation package does not supply that conclusion.

## 5. Prior-art and novelty audit

No novelty is claimed for the strong density hypothesis, the Selberg--Jutila/Maples--Rodgers zero-density estimates, Ingham's exponent, the Tsang-kernel tail reduction, or the Lagarias--Rodgers Alternative-Hypothesis construction. All are literature results.

The durable Mathia contribution here is the interface audit against the live WI-115 clue:

- rewrite the BGSTB bad-pair tail at normalized horizontal depth and identify the exact density slope `2` forced by the `e^{2a}` kernel weight;
- compare that requirement with the fixed-factor microscopic suppression actually supplied by the established near-line density theorems;
- identify Lagarias--Rodgers as a direct prior-art warning that the already-proved higher **vertical** correlations do not themselves encode generic anti-lattice rigidity.

A bounded search found no unconditional theorem supplying the strong microscopic density interface (16). This absence is not used as a priority claim; it only records the state of the source audit needed for this research decision.

## 6. Consequence for the horizontal-rigidity program

The first two cheap repairs after WI-115 are now sharply constrained.

First, the published zero-density literature cannot simply be substituted into the BGSTB tail argument. A successful density-based repair needs genuinely stronger information: either the slope-two little-`o` behavior (16), or a **direct weighted estimate for (1)/(4)** that exploits cancellation and is materially stronger than what follows from zero counts alone.

Second, escalation to the currently established higher vertical correlations is not by itself an anti-screening mechanism. Lagarias--Rodgers show that those band-limited identities tolerate exact half-lattice support. A useful higher-order observable must therefore retain information that their Alternative-Hypothesis model does not fix, and in the unconditional Weil-inertia problem it must additionally be horizontally sensitive to the off-line/double ambiguity.

The live escape routes are consequently narrower:

1. prove a direct unconditional estimate for the **weighted** Tsang bad-pair reservoir, without routing through present zero-density counts;
2. find an arithmetically accessible pair kernel whose horizontal signal survives the WI screening quotient at density scale;
3. cross support one with enough new prime-pair information to activate the nonzero alias channel of WI-007; or
4. find a genuinely horizontal or mixed higher-order statistic, beyond the currently proved vertical band-limited package, and test it explicitly against the WI-005/WI-006 screening configuration.

This finding therefore narrows but does not resolve `CLUE-higher-zero-correlations-horizontal-rigidity`: the direct zero-density substitution is closed at current theorem strength, and generic appeal to known higher vertical correlations is classicalized as insufficient, while direct weighted-tail control and genuinely non-screened observables remain open.