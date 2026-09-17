# MI-028 — Sparse midpoint rigidity comes from quantitative cross-coordinate multiplicativity, not near-maximal coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-181](../../findings/FD-181-sparse-signed-perturbations-cannot-hide-from-prime-extension-multiplicativity.md). The quantitative rigidity statement is proved for squarefree-supported perturbations of Möbius with support `o(x/log x)`; it remains a source-identifiability theorem, not a Franel--Landau estimate.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-180 first showed that such a repair cannot also make prime-extension multiplicativity too accurate: on the fixed-prime deletion fibre the normalized finite-`L^q` defect sits at the natural scale `(log x loglog x)^(-1/q)`.

FD-181 removes the fragile source assumptions behind the coercive direction. Let `delta=a-mu`, let `S` be its support, and suppose only `S(x)=o(x/log x)`, with arbitrary real signed amplitudes and with prime coordinates themselves allowed to move. For the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`,

one has

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Since `|E_x|~x loglog x/zeta(2)`, any normalized defect `o((log x loglog x)^(-1/q))` forces `a=mu`. Signed compensations and sparse movement of prime coordinates therefore do not evade the relation boundary.

The mechanism is a clean prime fan. One erroneous parent `n` emits about `x/(n log x)` extension edges on which the defect is exactly `delta(n)`. Hiding a positive fraction of that fan requires spending a comparable number of changed prime labels or changed children. A global support budget `o(x/log x)` is too small to screen even one fixed erroneous parent. This is why the relevant resource is relational boundary size, not the depth or rank of individually correct coefficients.

The next cardinal frontier is now explicit. At support size comparable to `x/log x`, the perturbation budget is large enough in principle to cover one full prime fan, so the present proof stops for a structural reason rather than because signed cancellation was overlooked. Dense tiny-amplitude perturbations form a separate frontier because support counting is then the wrong currency.

**Boundary.** Prime-extension energy is an additional source-faithfulness observable. FD-181 does not show that sparse Farey midpoint observations control this energy, does not prove the Franel--Landau critical discrepancy estimate, and does not establish optimality of the `x/log x` support threshold. A useful continuation must either connect a natural Farey observation to this relation energy at the required rate or find a destination-relevant relation whose coercivity is already intrinsic to the observed Farey data.