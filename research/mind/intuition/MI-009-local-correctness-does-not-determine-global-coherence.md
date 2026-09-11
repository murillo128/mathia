# MI-009 — A product of centered coordinate functions hides from every proper marginal

**Evidence level:** supported; this is an explicit shared construction in the Boolean and prime-Cauchy models, not a statement about every restricted arithmetic source.

On `{-1,+1}^r`, all marginals of order at most `d` retain exactly the Walsh moments of degree at most `d`. Their missing linear space is `span{chi_S:|S|>d}`. The positive laws `2^-r(1 +/- theta chi_S)` with `0<theta<=1` collide under those marginals whenever `|S|>d` ([AF-032](../../arithmetic_fidelity/findings/AF-032-k-way-marginals-retain-exactly-low-degree-walsh-interactions.md)). This identifies the unobserved sector, not just an example of ambiguous data.

The same centered-product mechanism occurs in the prime Gram problem. For a finite set `P` of `r=d+1` primes, let `mu` be Cauchy of scale `1/2`, set `h_p(x)=cos((log p)x)-p^-1/2`, and take

\[
d\pi_\varepsilon=\left(1+\varepsilon\prod_{p\in P}h_p\right)\,d\mu^{\otimes P},
\quad
0<|\varepsilon|\le\prod_{p\in P}(1+p^{-1/2})^{-1}.
\]

Each `h_p` has zero mean, so integrating out any one coordinate removes the perturbation. The induced characteristic kernel stays normalized and positive and agrees with the Bost-Connes kernel on every valuation difference supported on at most `d` primes. Nevertheless, at `N_P=product_(p in P)p`,

\[
K_\varepsilon(N_P,1)-G_{\rm BC}(N_P,1)
=\varepsilon\,2^{-r}\prod_{p\in P}(1-p^{-1})\ne0.
\]

This extends consistently with independent coordinates on the other primes ([WP-236](../../weil_positivity/findings/WP-236-bounded-order-prime-marginals-do-not-determine-critical-cauchy-coupling.md)). Thus adding any fixed number of prime-marginal orders cannot identify the joint kernel in that ambient positive class.

The exact correspondence is `chi_S` versus `product h_p`: both vanish under every projection omitting one participating coordinate. To obtain lower-order identification in a smaller source class, one must exclude these collision directions by a source identity, not by positivity alone. Full independence does exclude them; whether the desired arithmetic pairing satisfies an appropriate source-forced identity is a separate question.
