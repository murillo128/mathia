# WI-201 — Bourgain--Watt does not supply the 1515/4816 exponent-pair input

**Status:** `LITERATURE-PRIMARY + EXACT-DERIVED + PRIOR-ART-REDIRECT + CORRECTION + DECISIVE-NEGATIVE`.

A primary-source audit invalidates the numerical specialization used in WI-200. Khayrulloev's 2024 every-interval odd-order-zero theorem and Rakhmonov's 2025 narrow-rectangle zero-density theorem are genuinely parameterized by an ordinary exponent pair `(kappa,lambda)` through

\[
\theta(\kappa,\lambda)=\frac{\kappa+\lambda}{2\kappa+2}.
\]

However, their subsequent numerical insertion

\[
\theta_*\le \frac{1515}{4816}=0.314576411960\ldots
\]

is attributed to Bourgain--Watt, **Decoupling for perturbed cones and mean square of |zeta(1/2+it)|**, *International Mathematics Research Notices* 2018, DOI `10.1093/imrn/rnx009`, and the cited paper does not prove that `1515/4816` is obtainable from an ordinary exponent pair. In Bourgain--Watt, `1515/4816` occurs in the short-interval/mean-square zeta-error analysis. The paper explicitly states that it does **not** improve Huxley's bounds for the error terms in the circle and divisor problems.

This distinction is load-bearing. For an ordinary exponent pair `(kappa,lambda)`, the classical exponent-pair reduction to the circle/divisor problem uses exactly

\[
\frac{\kappa+\lambda}{2\kappa+2}.
\]

Thus an ordinary exponent pair with value `1515/4816` would itself improve Huxley's `131/416` circle/divisor exponent, contrary to the cited Bourgain--Watt paper's explicit evidence boundary. The source therefore cannot support the numerical exponent-pair corollary as used by Khayrulloev, Rakhmonov, or WI-200.

The correction is narrow but consequential. The **generic** theorem surfaces remain usable: if a verified ordinary exponent pair `(kappa,lambda)` is supplied, then Khayrulloev gives the corresponding every-interval critical-line reservoir above `T^(theta(kappa,lambda)+epsilon)`, and Rakhmonov gives his corresponding every-center narrow-rectangle estimate above the same threshold. What is withdrawn is only the claim that Bourgain--Watt supplies the specific ordinary-exponent-pair threshold `1515/4816`.

## 1. Primary-source reconciliation

Khayrulloev's Theorem 1 states the generic exponent-pair result and then gives Corollary 1.1 with `1515/4816`, citing Bourgain--Watt. Rakhmonov's Theorem 1 has the same generic exponent-pair parameter and likewise records the `1515/4816` numerical specialization with the same attribution. These are valid evidence that the two later papers *state* the numerical corollary, but not independent evidence for the load-bearing exponent-pair input because both point to the same source.

The cited Bourgain--Watt paper is:

Jean Bourgain and Nigel Watt, **Decoupling for perturbed cones and mean square of |zeta(1/2+it)|**, *International Mathematics Research Notices* 2018:17, 5219--5296, DOI `10.1093/imrn/rnx009`, arXiv:1505.04161.

Its relevant numerical threshold `1515/4816` belongs to the zeta mean-square error analysis. In the same paper the authors explicitly say that they do not obtain an improvement of Huxley's circle/divisor error exponents. Therefore reading the zeta mean-square threshold as an ordinary exponent-pair value is not source-supported.

A later Bourgain--Watt manuscript, **Mean square of zeta function, circle problem and divisor problem revisited**, arXiv:1709.04340, cannot repair this step. The arXiv record states that the manuscript was withdrawn; the 16 July 2023 revision notes proof problems in key propositions and removes theorem status from its principal claims. It is therefore excluded from the established evidence base.

## 2. Consequence for the bow frontier

WI-200 used `1515/4816` twice: first to extend the every-interval odd-order critical-line reservoir down from the source-safe `27/82` range, and second to extend Rakhmonov's fixed-physical-depth exclusion for the explicit Maynard--Pratt deep plateau over the same exponent band. Both deductions are algebraically valid **conditional on** an ordinary exponent pair with the claimed `theta`; the failed step is the numerical input.

Accordingly the established statements

\[
\vartheta>1515/4816
\]

in WI-200 are withdrawn. Pending an independently verified compatible ordinary exponent pair below the already audited Karatsuba threshold, the line returns to the last source-safe numerical frontier already established in WI-198/WI-199:

\[
\boxed{\vartheta>27/82.}
\]

This does **not** claim that `27/82` is optimal among all ordinary exponent pairs. It is only the strongest numerical cutoff already established inside this research line with a source chain that survived the present audit. A future improvement must exhibit and primary-source-check the actual exponent pair, rather than importing a numerically similar circle/divisor or zeta mean-square exponent from another method.

The generic conditional deduction can be retained in the following form. If `(kappa,lambda)` is a verified exponent pair and

\[
\theta=\frac{\kappa+\lambda}{2\kappa+2},
\]

then the WI-200 packing argument excludes mirror-closed count-saturating bows for every fixed `vartheta>theta`, and Rakhmonov's theorem excludes the same fixed-depth deep plateau in the range in which its stated density estimate applies. No new simple-critical-zero proportion follows from this correction.

## 3. Research consequence and evidence boundary

This is a prior-art redirect rather than a new analytic estimate. It prevents the program from treating a citation-repeated numerical value as two independent theorem inputs and restores the stricter evidence boundary required by the research contract. The accepted distinguished-twist covariance clue remains live; its source-fixed arithmetic problem is unchanged in the source-safe surviving range.

The correction does not invalidate Khayrulloev's or Rakhmonov's generic exponent-pair theorems, does not assert that no stronger ordinary exponent pair exists, and does not infer anything about actual off-critical zeros from the bow complement. It only removes an unsupported numerical specialization from Mathia's established frontier.

A targeted prior-art search located repetitions of the `1515/4816` attribution but no published correction of this specific source mismatch. No priority claim is made from absence of a search hit.

## Primary sources

- Sh. A. Khayrulloev, **On the estimate of the number of odd-order zeros of the Riemann zeta function lying on the critical line**, *Izvestiya of the National Academy of Sciences of Tajikistan*, 2024, No. 4 (197), 51--64, https://journals.anrt.tj/files/News_m/news_m_2024_04.pdf.
- Z. Kh. Rakhmonov, **Density of zeros of the Riemann zeta function in narrow rectangles of the critical strip**, *Chebyshevskii Sbornik* 26:5 (2025), 158--183, DOI `10.22405/2226-8383-2025-26-5-158-183`, https://www.mathnet.ru/eng/cheb1627.
- Jean Bourgain and Nigel Watt, **Decoupling for perturbed cones and mean square of |zeta(1/2+it)|**, *International Mathematics Research Notices* 2018:17, 5219--5296, DOI `10.1093/imrn/rnx009`, arXiv:1505.04161.
- Jean Bourgain and Nigel Watt, **Mean square of zeta function, circle problem and divisor problem revisited**, arXiv:1709.04340. **Withdrawn; exclusion evidence only.**
