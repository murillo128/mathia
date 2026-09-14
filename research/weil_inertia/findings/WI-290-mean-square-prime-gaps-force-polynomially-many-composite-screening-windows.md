# WI-290 — Mean-square prime gaps force polynomially many composite-screening windows

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`; the `77/200` exponent uses a recent unrefereed preprint theorem and is recorded separately from the published `3/8` baseline.
- **Scope:** the composite-prime-power residual set isolated in `WI-289` for the one-signed, completely screened, symmetric two-island branch. The question is whether the positive residual measure left after all `k>=2` prime-power Lambert exclusions could nevertheless be concentrated into only a few surviving windows, leaving the unresolved `k=1` prime-gap coupling essentially pointlike.
- **Result:** it cannot. A general prime-gap second-moment bound

  \[
  \sum_{p_n\le y}(p_{n+1}-p_n)^2
  \ll_\varepsilon y^{1+\theta+\varepsilon}
  \]

  forces at least

  \[
  \boxed{
  M_c(X)\gg_{c,\varepsilon}
  X^{(1-\theta)/2-\varepsilon}
  \left(\frac{\log\log X}{\log X}\right)^2
  }
  \]

  positive-length connected components of the composite-safe residual in `[X,2X]`. The published Peck--Maynard exponent `theta=1/4` therefore gives

  \[
  \boxed{
  M_c(X)\gg_{c,\varepsilon}
  X^{3/8-\varepsilon}
  \left(\frac{\log\log X}{\log X}\right)^2.
  }
  \]

  Julia Stadlmann's unrefereed Theorem 1, `theta=0.23`, would sharpen the exponent to `77/200=0.385`.
- **What it does not claim:** this does not construct a center satisfying the full `WI-288` screening condition, prove that a giant ordinary-prime gap near `x` intersects one of these windows, prove statistical independence between the prime processes at `x` and `sqrt(x)`, improve the simple-critical-zero proportion, or exclude the two-island branch. It rigidifies only the topology of the already-established composite-safe reservoir.
- **Novelty boundary:** mean-square prime-gap estimates are literature results, and the `WI-289` residual-measure estimate is already canonical Mathia evidence. The line-local deduction here is the prime-square separator argument converting those two inputs into a polynomial lower bound for the number of composite-safe windows. Targeted searches around prime-gap moments, consecutive-prime squares, prime-power exclusions, and connected-component counts found no direct formulation of this Lambert-screening consequence; search absence is audit context only, not a priority claim.

## Claim

Keep the notation of `WI-289`. For fixed `c>0`, let

\[
D_c(x)=\frac{W(c\sqrt{x})}{\sqrt{x}}
\]

and let

\[
\mathcal C_{\ge2}(X)
:=\left\{x\in[X,2X]:
\exists\ p\ \mathrm{prime},\ k\ge2,
\ |k\log p-\log x|<D_c(x)
\right\}.
\]

Write

\[
R_c(X):=[X,2X]\setminus\mathcal C_{\ge2}(X).
\]

Let `M_c(X)` denote the number of positive-length connected components of `R_c(X)`; if this number is infinite, all lower bounds below are automatic. Suppose that for some `theta>=0`, for every `epsilon>0`,

\[
S_2(y):=\sum_{p_n\le y}(p_{n+1}-p_n)^2
\ll_\varepsilon y^{1+\theta+\varepsilon}.
\tag{1}
\]

Then

\[
\boxed{
M_c(X)\gg_{c,\varepsilon}
X^{(1-\theta)/2-\varepsilon}
\left(\frac{\log\log X}{\log X}\right)^2.
}
\tag{2}
\]

In particular, the established `theta=1/4` mean-square bound identified by Peck and independently reproduced by Maynard yields

\[
\boxed{
M_c(X)\gg_{c,\varepsilon}
X^{3/8-\varepsilon}
\left(\frac{\log\log X}{\log X}\right)^2.
}
\tag{3}
\]

Stadlmann's Theorem 1 states

\[
S_2(y)\ll_\varepsilon y^{1.23+\varepsilon},
\tag{4}
\]

which, if that recent preprint theorem is admitted, gives

\[
\boxed{
M_c(X)\gg_{c,\varepsilon}
X^{77/200-\varepsilon}
\left(\frac{\log\log X}{\log X}\right)^2.
}
\tag{5}
\]

The exponent conversion is exact: `(1-23/100)/2=77/200`.

## 1. Prime squares are separators of the residual

Every prime square is itself forbidden by the `k=2` condition. Indeed, at `x=p^2`,

\[
|2\log p-\log x|=0<D_c(x).
\tag{6}
\]

Hence no connected component of `R_c(X)` can cross a prime square. If

\[
I_n=(p_n^2,p_{n+1}^2)
\tag{7}
\]

is a gap between consecutive prime squares, every positive-length component `J` of `R_c(X)` is contained in one such `I_n`, apart from harmless truncation at the endpoints `X,2X`.

For the components `J_{n,j}` lying in a fixed parent interval `I_n`, put `ell_{n,j}=|J_{n,j}|`. Since they are disjoint subintervals,

\[
\sum_j\ell_{n,j}\le |I_n|,
\]

and therefore

\[
\sum_j\ell_{n,j}^2
\le
\left(\sum_j\ell_{n,j}\right)^2
\le |I_n|^2.
\tag{8}
\]

This step is insensitive to the additional `k>=3` exclusions. They may split one square-gap survivor into more pieces, but splitting only decreases the sum of squared component lengths.

## 2. Prime-gap second moments bound the component energy

Write

\[
g_n:=p_{n+1}-p_n.
\]

Then exactly

\[
|I_n|
=p_{n+1}^2-p_n^2
=(p_{n+1}+p_n)g_n.
\tag{9}
\]

For every parent square gap intersecting `[X,2X]`, both bounding primes are `asymp sqrt(X)`. A fixed absolute multiplicative enlargement handles the two endpoint parent gaps; for example Bertrand's postulate is already enough. Thus for one absolute `C>0`,

\[
\sum_n |I_n|^2
\ll
X\sum_{p_n\le C\sqrt X}g_n^2.
\tag{10}
\]

Summing (8) and applying (1) at `y=C sqrt(X)` gives

\[
\boxed{
\sum_{J\subset R_c(X)} |J|^2
\ll_\varepsilon
X^{(3+\theta)/2+\varepsilon}.
}
\tag{11}
\]

No distributional independence is used here. This is only the exact square-map identity (9) plus the prime-gap second moment.

## 3. Residual mass plus (11) forces many windows

`WI-289` proves

\[
|R_c(X)|
\ge
\left(2+o(1)\right)
\frac{X\log\log X}{\log X}.
\tag{12}
\]

There are only finitely many relevant prime-power centers on a fixed dyadic shell, so up to measure-zero singleton components the measure in (12) is the sum of the lengths of the positive-length components. If these lengths are `ell_1,...,ell_M`, Cauchy--Schwarz gives

\[
|R_c(X)|^2
=\left(\sum_{j=1}^{M}\ell_j\right)^2
\le
M\sum_{j=1}^{M}\ell_j^2.
\tag{13}
\]

Combining (11)--(13) yields

\[
M
\gg_{c,\varepsilon}
\frac{X^2(\log\log X/\log X)^2}
{X^{(3+\theta)/2+\varepsilon}},
\]

which is (2). The argument also shows the more reusable inequality

\[
M_c(X)
\gg
\frac{|R_c(X)|^2}
{X\,S_2(C\sqrt X)}.
\tag{14}
\]

Thus any future improvement in the prime-gap second moment translates automatically into a stronger topological lower bound for the composite-screening reservoir.

## 4. Literature bridge and evidence split

A. S. Peck's published paper *Differences Between Consecutive Primes*, *Proceedings of the London Mathematical Society* 76 (1998), 33--69, DOI `10.1112/S0024611598000021`, is the published source behind the `theta=1/4` endpoint. James Maynard's later note *On the difference between consecutive primes*, arXiv:1201.1787, explicitly says it reproduces Peck's earlier result and states the bound in the exact form needed here:

\[
\sum_{p_n\le x}(p_{n+1}-p_n)^2
\ll_\varepsilon x^{5/4+\varepsilon}.
\tag{15}
\]

Julia Stadlmann, *On the mean square gap between primes*, arXiv:2212.10867, improves the exponent. Her introduction explicitly records Peck and Maynard as giving (1) with `nu=1/4`, and Theorem 1 states

\[
\sum_{p_n\le x}(p_{n+1}-p_n)^2
\ll_\varepsilon x^{1.23+\varepsilon}.
\tag{16}
\]

The arXiv version inspected for this finding is a preprint rather than a peer-reviewed publication. Accordingly, (3) is the literature-established specialization retained as the baseline, while (5) is a stronger `RECENT-PREPRINT` specialization. The exact reduction (14) does not depend on which exponent is used.

## 5. Stress tests and boundary conditions

The argument does **not** infer a lower bound on the length of any individual residual component. Cauchy uses only total residual mass and the quadratic component-energy ceiling. A polynomial component count is compatible with most surviving intervals being very short.

The use of prime squares is one-sided and robust. It does not assume that the `k=2` forbidden neighborhood fills a fixed fraction of every prime-square gap; it uses only the exact separator fact (6). Deeper powers can only refine the partition, and therefore cannot invalidate (8).

The endpoint parent intervals do not affect the exponent. The prime immediately below `sqrt(X)` and the prime immediately above `sqrt(2X)` remain within a fixed multiplicative range of `sqrt(X)` by elementary prime-existence bounds, so they are absorbed in the constant `C` in (10).

Most importantly, (2) is not a coupling theorem. A `k=1` giant-prime-gap core near `x` could in principle avoid all of these composite-safe components. Ruling that out still requires arithmetic information correlating a rare large gap near `x` with the prime-square-scale geometry near `sqrt(x)` (and the thin `k>=3` resonances).

## 6. Prior-art audit

The closest classical objects are moment bounds for consecutive prime gaps, prime distribution between consecutive prime squares, and work on placing perfect powers inside large prime gaps. The first supplies (1); the latter two study different incidence questions. Targeted searches by the structural formulation -- prime-gap second moments plus prime-square separators plus component counts of a prime-power exclusion set -- found no source stating (14) or its Lambert-screening specialization.

This search result is not used as evidence of priority. The durable mathematical content is the transparent implication (14), whose inputs and provenance are explicit.

## Consequence for the research line

`WI-289` showed that composite prime powers leave a residual set of order `X loglog(X)/log(X)` but did not control how fragmented that set might be. The present finding rules out concentration into a bounded, logarithmic, or otherwise subpolynomial collection of windows using only established prime-gap information: already the published `theta=1/4` theorem forces `X^{3/8-o(1)}` surviving components.

Therefore the unresolved `WI-288` two-island obstruction is not accurately modeled as “find one exceptional composite-safe interval.” The hard step is genuinely a **cross-scale incidence problem**: prove that a sufficiently large ordinary-prime desert at scale `x` cannot systematically avoid a polynomial family of composite-safe windows whose dominant geometry is generated by prime gaps at scale `sqrt(x)`. This narrows where new arithmetic information must enter without assuming any independence that current theorems do not provide.
