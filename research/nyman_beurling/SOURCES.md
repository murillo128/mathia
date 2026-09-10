# Nyman–Beurling source anchors

This file records durable literature dependencies for `research/nyman_beurling/`. It is an anchor list, not a search history.

## Core criterion

- [`research/prior_art/nyman-beurling-criterion.md`](../prior_art/nyman-beurling-criterion.md). Role: Mathia prior-art anchor for the Hilbert-space closure formulation equivalent to RH.
- [`research/prior_art/baez-duarte-strengthening-of-nyman-beurling.md`](../prior_art/baez-duarte-strengthening-of-nyman-beurling.md). Role: retained anchor for the discrete Báez-Duarte strengthening and its relation to the original criterion.
- [`research/prior_art/baez-duarte-criterion.md`](../prior_art/baez-duarte-criterion.md). Role: neighboring discrete RH criterion and boundary against merely restating a known equivalent sequence condition.
- Luis Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis*, Rend. Lincei Mat. Appl. 14 (2003), 5–11, [arXiv:math/0202141](https://arxiv.org/abs/math/0202141). Role: primary source for the integer-dilation strengthening used by the canonical discrete family.
- Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137–146, DOI `10.1007/BF02829783`, [arXiv:math/0607733](https://arxiv.org/abs/math/0607733). Role: authoritative Hardy-space/Mellin formulation used in `NB-001`, including the target, discrete generators, boundary norm, and inner-multiplier isometries.

## Quantitative approximation boundary

- Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Adv. Math. 170 (2002), 56–70, DOI `10.1006/aima.2001.2066`, [arXiv:math/0103058](https://arxiv.org/abs/math/0103058). Role: zero-sensitive lower-bound boundary for claims about asymptotic Nyman approximation rates.
- Sandro Bettin, J. Brian Conrey, David W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman-Beurling criterion*, [arXiv:1211.5191](https://arxiv.org/abs/1211.5191). Role: conditional optimal-constant boundary; the matching asymptotic requires RH plus an additional reciprocal-`ζ'` moment hypothesis, so finite target-aware identities do not by themselves supply the known deep rate.

## Harmonic arithmetic and separated-frequency tools

- Srinivasa Ramanujan, *On certain trigonometrical sums and their applications in the theory of numbers*, Trans. Cambridge Philos. Soc. 22 (1918), no. 13, 259–276, [original paper](https://ramanujan.sirinudi.org/Volumes/published/ram21.pdf). Role: classical prior-art boundary for the Ramanujan sums used to diagonalize finite divisibility contrasts in `NB-012`; the specific finite Nyman normal-equation transform is derived in the finding.
- H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`. Role: generalized Hilbert inequality for separated frequencies; `NB-012` uses its standard two-sided lower-frame corollary for reduced rational frequencies with denominator at most `L`.

## Multiplication-table geometry

- Kevin Ford, *The distribution of integers with a divisor in a given interval*, Ann. of Math. (2) 168 (2008), 367–433, DOI `10.4007/annals.2008.168.367`, [journal version](https://annals.math.princeton.edu/2008/168-2/p01), [arXiv:math/0401223](https://arxiv.org/abs/math/0401223). Role: Corollary 3 gives the order of magnitude of the number of distinct entries in an `N x N` multiplication table; `NB-016` uses it after an exact quotient-frame identification to quantify the rank sparsity of the compressed Nyman enrichment operator.

## Möbius local-pattern input

- Kaisa Matomäki, Maksym Radziwiłł, Terence Tao, *Sign patterns of the Liouville and Möbius functions*, Forum Math. Sigma 4 (2016), e14, DOI `10.1017/fms.2016.6`, [arXiv:1509.01545](https://arxiv.org/abs/1509.01545). Role: proves positive lower natural density for every two-term value pattern `(mu(n),mu(n+1))`; `NB-027` uses the resulting positive-density same-sign nonzero pairs to turn Möbius coefficient locking into logarithmic coefficient mass transverse to an adjacent-difference matching.

## Classical Möbius summatory cancellation

- Harold Davenport, *Multiplicative Number Theory*, 3rd ed., revised by Hugh L. Montgomery, Graduate Texts in Mathematics 74, Springer, 2000, ISBN `978-0-387-95097-6`. Role: standard classical source for prime-number-theorem consequences for Möbius sums; `NB-028` uses only the unconditional consequence `M(x)=o(x)`, while `NB-035` uses the standard PNT consequence `sum_{n<=x} mu(n)/n -> 0` for its growing-cutoff corollary.

## Expansion rule

Add a primary source when a canonical finding depends on an exact quantitative approximation theorem, Gram asymptotic, dual formulation, best-approximation bound, or other specialized external estimate. Do not turn `SOURCES.md` into a bibliography of every Nyman–Beurling paper.