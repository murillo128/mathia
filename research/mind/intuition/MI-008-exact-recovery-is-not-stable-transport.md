# MI-008 — Exact recovery and accurate approximation are not stable transport without conditioning

**Evidence level:** supported by exact divisor-moment stability and Xi Vieta-normalization counterexamples through AF-168 and XF-080

## Core intuition

Two independent lines now separate **information-theoretic sufficiency** from **quantitatively usable transport**. Arithmetic Fidelity gives an exactly sufficient finite witness whose inverse becomes Hölder-singular at multiple-root collisions. Xi Flow gives an exponentially accurate local finite-band approximation with the correct mode count whose normalization into Vieta coordinates amplifies hidden outer-coefficient smallness into a macroscopic low mode.

The common principle is that an injective representation or tiny forward error is not enough. A source-to-destination bridge needs a recovery/normalization map whose condition number is controlled on the actual asymptotic family.

## Strongest justified principle

AF-167 shows that degree plus the first `n` phase-gradient moments exactly recover a degree-`n` finite Blaschke divisor, with `n-1` moments sharply insufficient. AF-168 then proves that the inverse of this exact moment map is globally only `1/n`-Hölder and locally only `1/m`-Hölder at multiplicity `m`; local Lipschitz behavior returns only at simple separated divisors, with Vandermonde conditioning deteriorating as collisions approach.

XF-078--XF-079 solve two apparently different interface costs: a Gaussian quotient is locally approximable with the ordinary Vieta-sized frequency budget, and the weighted selector resource needs only one safe center. XF-080 nevertheless shows that the explicit accurate surrogate has exponentially small outer Laurent coefficients. Vieta normalization divides by those coefficients and produces `P_1=Theta(N)`, outside the bounded source regime despite exponentially small local function error.

The exact mechanisms differ, but the structural failure is the same: **the forward representation can look lossless while the inverse map to the theorem's actual coordinates is singular or badly conditioned.**

## Program consequence

Whenever a bridge claims that source information has survived because a representation is injective, exactly reconstructible, or approximated to `o(1)`, identify the inverse operation consumed next. Control its degree dependence, multiplicities, separations, outer coefficients, normalization denominators, or other singular loci in the same asymptotic regime.

If the destination only needs a quotient, first remove destination-null distinctions rather than overconditioning a stronger inverse. If the full inverse is genuinely required, its recovery modulus is a separate theorem, not a corollary of exact sufficiency.

## Counterevidence and boundary

Poor conditioning is not universal. AF-168 gives locally analytic inversion for simple separated divisors, and Xi Flow may admit a different surrogate or direct selector dictionary that avoids the tiny outer coefficient. The synthesis therefore does not say that exact recovery is useless; it says that **stability must be established in the admissible family rather than assumed from exactness.**

## Status / novelty

Root-conditioning, Vandermonde singularity, and Fourier-extension/Vieta conditioning are classical phenomena in their native settings. The Mathia synthesis is cross-line: inverse conditioning is a distinct research gate between retention and downstream coercivity. It is a supported heuristic, not a theorem about RH.

## Falsification criterion

Produce an asymptotic Mathia bridge whose forward representation has vanishing error while its inverse condition number diverges, yet the final destination resource remains uniformly controlled without another compensating quotient or theorem; or prove uniform stable inversion across one of the exact collision/outer-normalization controls above. Either result would sharpen the scope of this principle.