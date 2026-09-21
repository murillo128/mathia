# MI-053 — The Abel cusp creates a deterministic 25/28 Ramanujan background

**Evidence level:** exact/asymptotic synthesis from [PL-409](../../findings/PL-409-cubic-cusp-eighth-order-boundary.md), sharpening the safe model-side localization in PL-408.

For fixed `eta>0`, the cubic Abel kernel

`K_eta(x)=|x| exp(-eta|x|^3) sin(pi|x|^3/6)`

has first nonsmooth local term `-(pi eta/6)|x|^7`. Its Fourier transform therefore has the sharp tail

`Khat_eta(xi)=-(105 eta)/(16 pi^7)|xi|^(-8)+O_eta(|xi|^(-14))`.

After Poisson summation, the first nonzero alias at Ramanujan denominator `q` is

`-(pi eta/720) J_8(q) H^(-8)`

up to the controlled higher-order remainder. Because `J_8(q)>0`, all denominators have the same leading sign; no cancellation between denominators can improve this term.

Moreover

`sum_(q<=Q) mu(q)^2 J_8(q)/phi(q)^2 ~ (C_8/7) Q^7`,

so truncation at `Q=H^kappa` creates the deterministic background

`-(pi eta C_8/10080) H^(-8+7kappa)(1+o(1))`.

It reaches the previously isolated zero-sensitive scale `H^(-7/4)` exactly at `kappa=25/28`. Hence every fixed fractional interior below `25/28` is invisible at that scale, the `25/28` interior contributes a nonzero regulator term at exactly that scale, and larger fixed interiors produce a regulator background that dominates the zero layer while remaining below the deterministic `H^(-1)` correction.

The moving-boundary audit must therefore subtract or otherwise control this cusp-generated term before interpreting an `H^(-7/4)` contribution as zero-sensitive arithmetic information. The earlier `7/8` threshold was only a safe consequence of a nonsharp seventh-order Fourier bound; `25/28` is the sharp crossover for this fixed kernel and truncation.

**Boundary.** `25/28` is not an RH-critical exponent. The statement assumes fixed `eta>0` and the declared Abel kernel; joint `eta->0` limits can change the balance. PL-409 remains model-side and does not prove that the actual prime spectral measure matches the critical Ramanujan endpoint.