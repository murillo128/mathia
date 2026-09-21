# MI-054 — Finite cusp-jet subtraction moves the model obstruction to the true endpoint

**Evidence level:** exact/asymptotic synthesis from [PL-410](../../findings/PL-410-finite-cusp-jet-renormalization-endpoint.md), sharpening the first untreated cusp alias in [PL-409](../../findings/PL-409-cubic-cusp-eighth-order-boundary.md).

For the fixed cubic Abel kernel, the nonsmooth local jet is not a single `|x|^7` term. Its algebraic Fourier tail contains the ladder of orders

`k_j = 6j+2 = 8,14,20,26,...`,

and Poisson summation sends the `j`-th cusp coefficient to the explicit arithmetic alias

`beta_(j,eta) J_(k_j)(q) H^(-k_j)`.

If the first `M` aliases are subtracted using the exact finite sums

`S_k(Q)=sum_(q<=Q) mu(q)^2 J_k(q)/phi(q)^2`,

the remaining model contribution obeys

`R_(eta,M)(H,Q) <<_(eta,M) H^(-(6M+8)) Q^(6M+7) (log log(3Q))^2`.

For `Q=H^kappa`, this is `o(H^(-7/4))` whenever

`kappa < 1 - 3/(4(6M+7))`.

Hence every fixed fractional interior `kappa<1` can be pushed below the zero-sensitive scale by subtracting finitely many explicit cusp counterterms. The `25/28` crossover from PL-409 is only the first untreated member of this hierarchy, not a fundamental moving-boundary exponent. Generically one `J_8` subtraction moves the next crossover to `49/52`; special zeros of cusp coefficients can move it farther.

The model-side nonrenormalized region is therefore the genuine boundary `q/H = Theta(1)`. There successive cusp orders are no longer separated by a small factor `(Q/H)^6`, so fixed finite subtraction does not make the endpoint disappear. A source-faithful prime/model bridge should target that signed endpoint after removing the explicit finite cusp jet appropriate to the claimed interior accuracy, rather than repeatedly improving fixed-power denominator ranges.

**Boundary.** `M` is fixed before `H->infinity`; PL-410 supplies no uniform infinite renormalization as `kappa->1`. The exact finite `S_k(Q)` are load-bearing counterterms; replacing them only by leading asymptotics creates an unaudited remainder. The result remains model-side and proves neither actual-prime source replacement nor the required signed endpoint estimate.