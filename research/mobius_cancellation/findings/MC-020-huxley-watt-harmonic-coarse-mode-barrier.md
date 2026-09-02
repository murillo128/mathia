# MC-020 — Huxley–Watt scale doubling exposes an RH-equivalent harmonic coarse mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

A classical scale-doubling identity of Huxley and Watt gives a genuinely nonlinear way to reconstruct `M(N^2)` using only Möbius values up to `N`, so it escapes the finite local-linear obstruction of `MC-018` at the algebraic level. However, its most natural matrix decomposition exposes a new coarse scalar whose RH-scale control is itself equivalent to RH.

Let

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

and define

\[
\mathbf m=(\mu(1),\ldots,\mu(N))^{\rm T},
\quad
\mathbf f=(1,1/2,\ldots,1/N)^{\rm T},
\quad
\mathbf u=(1,\ldots,1)^{\rm T}.
\]

For the `N x N` matrix

\[
A_{mn}=\left\lfloor\frac{N^2}{mn}\right\rfloor,
\]

Huxley and Watt record the exact identity

\[
M(N^2)=2M(N)-\mathbf m^{\rm T}A\mathbf m
\tag{1}
\]

and the exact decomposition

\[
A=N^2\mathbf f\mathbf f^{\rm T}
-\frac12\mathbf u\mathbf u^{\rm T}+Z,
\qquad
Z_{mn}=-\psi\!\left(\frac{N^2}{mn}\right),
\tag{2}
\]

where

\[
\psi(x)=x-\lfloor x\rfloor-\frac12.
\]

Since

\[
\mathbf m^{\rm T}\mathbf f=H(N),
\qquad
\mathbf m^{\rm T}\mathbf u=M(N),
\]

(1)–(2) give the exact scale-doubling formula

\[
\boxed{
M(N^2)
=2M(N)-N^2H(N)^2+\frac12M(N)^2-\mathbf m^{\rm T}Z\mathbf m .
}
\tag{3}
\]

The harmonic coefficient `H(N)` is not a harmless lower-order statistic. One has the classical-equivalent boundary

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
H(x)=O_\varepsilon\!\left(x^{-1/2+\varepsilon}\right)
\text{ for every }\varepsilon>0 .
}
\tag{4}
\]

Consequently, controlling the rank-one term in (3) separately at the scale needed for RH,

\[
N^2H(N)^2=O_\varepsilon(N^{1+\varepsilon}),
\tag{5}
\]

is already RH-equivalent after relabelling `epsilon`. A spectral or low-rank treatment that simply isolates the `\mathbf f` mode and assumes (5) has therefore relocated the full zero-free burden rather than reduced it.

At the same time, the residual matrix is only pointwise bounded:

\[
|Z_{mn}|\le\frac12.
\tag{6}
\]

The direct absolute estimate therefore gives

\[
|\mathbf m^{\rm T}Z\mathbf m|
\le\frac12\left(\sum_{n\le N}|\mu(n)|\right)^2
=O(N^2),
\tag{7}
\]

whereas RH-scale control of `M(N^2)` is `O_\varepsilon(N^{1+\varepsilon})`. Thus the obvious absolute treatment of the fractional-part kernel loses essentially a full factor `N`. The remaining potentially useful information in (3) is **signed coupling**: cancellation inside `\mathbf m^{\rm T}Z\mathbf m`, or cancellation between that term and the harmonic/coarse pieces, must be derived from arithmetic structure rather than destroyed by termwise absolute bounds.

This produces a concrete answer to the coarse-mode question left by `MC-018` and `MC-019`. Nonlinear multiplicative scale coupling is mathematically real, but the Huxley–Watt representation does not by itself make the critical coarse mode cheaper: in its first natural decomposition, the missing global information reappears as the reciprocal-weighted Möbius sum `H(N)`.

## 1. Exact specialization of the Huxley–Watt identity

Huxley and Watt prove more generally that for a totally multiplicative function `g`,

\[
M(g,N^2)=2M(g,N)-\mathbf m_g^{\rm T}A_g\mathbf m_g,
\tag{8}
\]

where

\[
M(g,X)=\sum_{n\le X}\mu(n)g(n),
\qquad
(\mathbf m_g)_n=\mu(n)g(n),
\]

and

\[
(A_g)_{mn}=\sum_{k\le N^2/(mn)}g(k).
\]

For `g=1`, this gives (1). Their decomposition (2) follows entrywise from

\[
\left\lfloor\frac{N^2}{mn}\right\rfloor
=\frac{N^2}{mn}-\frac12
-\psi\!\left(\frac{N^2}{mn}\right).
\tag{9}
\]

Taking the quadratic form of (2) against `\mathbf m` yields

\[
\mathbf m^{\rm T}A\mathbf m
=N^2H(N)^2-\frac12M(N)^2+\mathbf m^{\rm T}Z\mathbf m,
\tag{10}
\]

and substitution in (1) proves (3).

The important distinction from the local filters of `MC-018` is structural. Formula (1) reconstructs a quantity at horizon `N^2` from the complete arithmetic data up to horizon `N`; it is neither a fixed-radius filter nor an anchor-free linear statistic of the partial-sum process. It therefore passes the algebraic escape test that `MC-018` left open. The obstruction found here appears only after asking whether the exact nonlinear identity supplies a **strictly weaker quantitative input** than the target.

## 2. The harmonic Möbius coefficient has the RH boundary

We prove (4) directly to make the circularity audit explicit.

Assume RH. The classical Mertens criterion gives, for every positive `epsilon`,

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{11}
\]

RH also implies the prime number theorem, hence the classical convergence

\[
\sum_{n\ge1}\frac{\mu(n)}n=0.
\tag{12}
\]

Partial summation therefore gives

\[
H(x)
=\frac{M(x)}x-\int_x^\infty\frac{M(t)}{t^2}\,dt
=O_\varepsilon(x^{-1/2+\varepsilon}),
\tag{13}
\]

which is the forward implication.

Conversely, suppose the bound in (4) holds for every positive `epsilon`. Put

\[
a_n=\frac{\mu(n)}n,
\qquad
A(x)=\sum_{n\le x}a_n=H(x).
\]

Abel summation implies that

\[
F(s)=\sum_{n\ge1}\frac{\mu(n)}{n^s}
\tag{14}
\]

converges locally uniformly and is holomorphic throughout `Re(s)>1/2`: on any compact set at positive distance from that line, choose `epsilon` smaller than the distance and apply the assumed decay of `A(x)` to the series `sum a_n n^{-(s-1)}`.

For `Re(s)>1`, absolute convergence gives

\[
F(s)=\frac1{\zeta(s)}.
\tag{15}
\]

To pass the pole at `s=1` without hiding a meromorphic step, let

\[
Z_0(s)=(s-1)\zeta(s),
\]

which is holomorphic on `Re(s)>1/2`. On `Re(s)>1`,

\[
Z_0(s)F(s)=s-1.
\tag{16}
\]

The identity theorem extends (16) to the connected half-plane `Re(s)>1/2`. If `rho` were a nontrivial zeta zero there, then the left side of (16) would vanish at `rho` while the right side would equal `rho-1`, a contradiction. Hence zeta has no nontrivial zero with real part greater than `1/2`; the functional equation then gives RH. This proves (4).

Thus the harmonic mode is analytically different from the Riesz constant mode in `MC-019`, but it carries the same critical zero-free boundary.

## 3. What the square-scale identity does and does not buy

Equation (3) is not vacuous. It expresses the much longer-scale value `M(N^2)` using only Möbius data through `N`, and it packages that data into a structured quadratic form. In a hypothetical scale-doubling induction, a previously established RH-scale estimate for `M(N)` would make the explicit terms `2M(N)` and `M(N)^2/2` compatible with the target at `N^2`. The genuinely additional coarse obligation exposed by (3) is `H(N)`.

But treating the displayed pieces independently fails in two complementary ways. First, (5) is already equivalent to the desired zero-free boundary through (4). Second, the only estimate on `Z` available from its definition without arithmetic cancellation is (7), which is polynomially too large. The decomposition is therefore cancellation-sensitive in exactly the sense highlighted by `MC-014`: separating an internally coupled identity into positive budgets can erase the mechanism one hopes to exploit.

The Huxley–Watt paper also studies the spectrum of `A`: its Perron–Frobenius eigenvalue is approximately `(pi^2/6)N^2` and the corresponding eigenvector is approximately `\mathbf f`. That spectral fact reinforces, rather than removes, the information audit above. The dominant direction is precisely the reciprocal-weight direction whose Möbius coefficient is `H(N)`. No conclusion about the entire residual operator norm is needed here; the exact decomposition (2) is enough to locate the obstruction.

A non-circular continuation must therefore avoid demanding separate RH-scale control of `H(N)`. Two concrete possibilities remain open:

- prove a signed arithmetic relation forcing cancellation between `N^2H(N)^2` and `\mathbf m^{\rm T}Z\mathbf m` (and the smaller-scale `M(N)` terms) at the target scale;
- exploit the full totally-multiplicative `g` identity as a coupled hierarchy rather than one isolated scalar. In particular `g(n)=1/n` gives an exact scale-doubling identity for `H(N^2)` itself, with matrix entries `sum_{k\le N^2/(mn)}1/k`; whether the resulting coupled system has a contraction or merely relocates the same zero-free information is a separate falsifiable question.

Neither possibility is established by this finding.

## 4. Prior art and novelty boundary

The source is M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, arXiv `1807.05890` (2018), published in *Chebyshevskii Sbornik* 19(3), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`.

The paper itself states that the underlying family of Mertens identities is not new apart from the arbitrary-range generalization; its proof is inspired by Meissel and it discusses Linnik/Vaughan-type antecedents. Equation (1), the general form (8), the matrix `A`, the Perron–Frobenius analysis, and the decomposition (2) are therefore **prior art**, not Mathia discoveries.

No novelty is claimed for the reciprocal-zeta Dirichlet series, partial summation, the RH/Mertens criterion, or the weighted equivalence (4), which is an elementary classical consequence once the objects are aligned. The durable line-specific result is the information audit: the first natural low-rank/spectral decomposition of a bona fide nonlinear scale-doubling Mertens identity exposes an RH-equivalent harmonic mode, while the residual fractional-part quadratic form is too large under absolute control.

This is materially different from merely observing that the identity contains Möbius data. It identifies exactly what a successful use of that prior-art mechanism must prove and what does **not** count as a weaker bootstrap.

## 5. Boundaries and decisive continuation

This finding does not prove that Huxley–Watt scale doubling cannot contribute to RH. It kills only the naive route that separately bounds its coarse rank-one and residual terms at the target scale and treats the matrix decomposition itself as a gain.

It also does not claim that `H(N)` and `M(N)` are independent pieces of information, that the fractional-part kernel is random, or that a particular spectral truncation cannot exploit cancellations. The exact identity may contain arithmetic cancellation invisible to the entrywise estimate (7).

A decisive positive continuation must produce a theorem of one of the following forms without importing a zero-free region equivalent to the conclusion:

\[
N^2H(N)^2+\mathbf m^{\rm T}Z\mathbf m
\quad\text{has target-scale cancellation from independently controlled arithmetic input},
\]

with the signs adjusted according to (3), or an exact coupled recursion (for example using `g(n)=1/n`) whose hypotheses close under scale doubling with a strict quantitative gain. A decisive negative continuation would construct a matched multiplicative model satisfying the proposed smaller-scale inputs while the same coarse/residual decomposition still produces super-square-root growth at the doubled scale.

The main frontier after `MC-019` is therefore sharpened: **changing from additive multiscale coordinates to a classical multiplicative quadratic scale-doubling identity does not by itself eliminate the coarse-mode problem; it changes the coarse mode from a Riesz average to a harmonic Möbius coefficient.**