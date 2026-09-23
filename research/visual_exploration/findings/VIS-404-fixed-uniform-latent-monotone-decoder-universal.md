# VIS-404 — fixing the latent law only moves arbitrary residual freedom into the quantile decoder

## Claim

Continue in the fixed-`m_1` rank-one qutrit setting of `VIS-388`--`VIS-403`, where the admissible normalized spectrum is parameterized by one residual coordinate

`u in I=[u_-,u_+]`

through the affine weight map

`w=w(u)=(w_1(u),w_2(u),w_3(u))`.

`VIS-403` showed that an unrestricted scalar latent can reproduce any Borel probability law `nu` on `I` by taking the latent itself to have law `nu`. Fixing the latent law does **not** repair that non-identifiability if the decoder remains unrestricted, even if the residual decoder is required to be monotone.

Let

`U ~ Uniform(0,1)`

be fixed independently of `nu`. Write

`F_nu(x)=nu((-∞,x])`

and define the generalized quantile

`Q_nu(p)=inf{x in I : F_nu(x)>=p}`.

Then `Q_nu` is nondecreasing and Borel measurable, and the classical quantile-transform identity gives

`Q_nu(U) ~ nu`.

Therefore, with any fixed `T>0`, the deterministic sector decoder

`S_i(U)=sqrt(T w_i(Q_nu(U)))`

has normalized squared energies

`W_i=S_i(U)^2 / sum_j S_j(U)^2 = w_i(Q_nu(U))`,

so the qutrit residual has exactly the arbitrary target law `nu`. Conditional on the fixed latent `U`, the sector amplitudes are again deterministic and hence conditionally independent.

Thus **a fixed scalar latent law plus an unrestricted monotone residual decoder still spans every Borel residual law on the qutrit interval**. Requiring a standard latent distribution, monotonicity, or an order-preserving one-dimensional transport does not create a falsifiable nuisance family by itself; it merely relocates the target-dependent freedom from the latent law into the decoder.

For smooth target laws the same obstruction survives qualitative smoothness. If `nu` has a strictly positive continuous density `f` on `I`, then `F_nu` is strictly increasing and the ordinary quantile `Q_nu=F_nu^{-1}` is continuously differentiable on `(0,1)`, with

`Q_nu'(p)=1/f(Q_nu(p))`.

If moreover `0<m<=f<=M<infinity`, then

`1/M <= Q_nu'(p) <= 1/m`.

So continuity, differentiability, invertibility and finite derivative bounds that are allowed to depend on the target law are likewise not sufficient restrictions. A useful control needs **pre-specified quantitative or structural decoder constraints whose admissible class is fixed independently of the residual being tested**.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL QUANTILE-TRANSFORM REPRESENTATION + NEGATIVE IDENTIFIABILITY/CONTROL RESULT + NO-NOVELTY-CLAIM`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. The generalized quantile gives a universal monotone decoder

For any probability law `nu` on the compact interval `I`, its distribution function `F_nu` is nondecreasing and right-continuous. The generalized inverse

`Q_nu(p)=inf{x in I:F_nu(x)>=p}`

is nondecreasing. For every real `x`, the generalized-inverse relation gives, up to the irrelevant endpoint convention at a null set of `p`,

`{p in (0,1): Q_nu(p)<=x} = (0,F_nu(x)]`.

Hence for `U~Uniform(0,1)`,

`P(Q_nu(U)<=x)=P(U<=F_nu(x))=F_nu(x)`.

Therefore `Q_nu(U)` has law `nu`.

This is the standard inversion/quantile-transform construction. The point here is not a new probability theorem but the control consequence for the current Wang residual: **fixing the base latent distribution to a canonical uniform law does not reduce model capacity while the monotone decoder may depend arbitrarily on the target law**.

## 2. Composition with the qutrit spectral slice

`VIS-389` supplies an affine parameterization `u -> w(u)` of the fixed-`m_1` qutrit simplex slice. Composing that map with `Q_nu` produces a deterministic decoder from the fixed latent `U` to the full normalized spectrum.

Choose a fixed total energy `T>0` and set

`S_i(U)=sqrt(T w_i(Q_nu(U)))`.

Because the weights sum to one,

`sum_i S_i(U)^2=T`,

and radial normalization returns exactly `w(Q_nu(U))`. Thus the residual coordinate is `Q_nu(U)` and has the prescribed law `nu`.

Each affine coordinate `w_i(u)` is monotone or constant on the one-dimensional admissible slice, so after composition with nondecreasing `Q_nu` and the increasing square root, each sector amplitude is itself monotone in one direction or constant wherever the coordinate remains positive. The construction therefore does not rely on an oscillatory or high-dimensional latent map.

The decoder is nevertheless target-dependent: all of `nu` has been encoded into `Q_nu`. That is exactly why monotonicity alone is not a complexity restriction.

## 3. Qualitative smoothness does not repair the control

Suppose `nu` has density `f` continuous and strictly positive on `I`. Then

`F_nu'(x)=f(x)>0`,

so `F_nu` is a `C^1` bijection from `I` to `[0,1]`, and the inverse-function theorem gives

`Q_nu'(p)=1/f(Q_nu(p))`.

If `f` is bounded above and away from zero, `Q_nu` is bi-Lipschitz with finite derivative bounds. More target regularity transfers to `Q_nu` in the usual way when the corresponding derivatives and nondegeneracy assumptions hold.

This does **not** mean one fixed derivative bound can represent every distribution. The bounds above depend on `nu`. It shows the precise control boundary: saying only “the decoder is monotone”, “continuous”, “smooth”, or “has some finite Lipschitz constant” remains non-diagnostic when the function itself and its quantitative constants are selected after seeing the residual.

A genuine restriction must predeclare something the target cannot freely tune away: for example a fixed finite-dimensional decoder basis, degree/order bound, variation or Lipschitz budget with a numerical constant frozen in advance, source-packet incidence rule, coefficient constraints, prescribed kernel family, or another Wang-derived admissibility condition.

## 4. Consequence for the source-packet localization frontier

The accepted Wang packet-localization clue currently asks for a constrained latent nuisance family derived independently from the source/packet mathematics. `VIS-403` ruled out latent dimension and conditional independence as restrictions when both latent law and decoder are free. The present result closes the next superficial repair: **fixing the scalar latent law, even to the canonical uniform distribution, does not help if arbitrary monotone transport remains available**.

The next useful null must therefore constrain the *joint latent-to-residual mechanism*, not one coordinate description of it. In particular, a proposed control should not be credited merely because it uses a standard latent prior or an order-preserving decoder. Its admissible decoder class, numerical capacity, or packet-derived structure must be frozen independently and have at least one testable consequence that excludes some residual laws.

This is a representation-level no-go result. It deliberately prevents a standard probability reparameterization from being mistaken for a narrower physical or arithmetic model.

## Prior-art and novelty audit

The generalized-quantile construction is classical inverse-transform sampling. A standard reference is Luc Devroye, *Non-Uniform Random Variate Generation*, Springer, 1986, Chapter II “General Principles in Random Variate Generation”, especially the inversion principle; DOI `10.1007/978-1-4613-8643-8_2`. Berkeley probability notes also state the generalized quantile `q_X(u)=inf{x:F_X(x)>=u}` and the standard proposition that `q_X(U)` has the law of `X` for `U~Uniform(0,1)`.

No novelty is claimed for inverse-transform sampling, generalized quantiles, the inverse-function theorem, monotone transport on the line, or their regularity properties. The Mathia-specific contribution is the negative control boundary obtained by composing this classical transport with the already-derived one-dimensional qutrit Wang residual: **a fixed standard latent and qualitative monotonicity/regularity still do not make the nuisance family falsifiable unless decoder capacity is independently bounded**.

## Boundaries

- The universal Borel-law statement requires only a nondecreasing Borel generalized-quantile decoder; atomic target laws may produce jumps or flat regions.
- The `C^1`/bi-Lipschitz refinement applies only to target laws with the stated positive continuous density and quantitative bounds. It is not a universality theorem for all Borel laws under one fixed smoothness budget.
- A genuinely fixed decoder, a fixed finite-parametric decoder family, or a predeclared numerical regularity/complexity budget can be restrictive. This finding does not rule those out.
- The result does not show that an actual Wang/source-packet decoder family contains arbitrary quantile maps. It says such maps must be excluded by an independently derived restriction before a fixed-latent null becomes informative.
- `VIS-394`--`VIS-402` remain substantive controls because their packet architectures and nuisance choices are independently specified; the present result concerns the unrestricted representation escape identified after `VIS-403`.
- No retained visualization is required because the result is an exact one-dimensional representation/identifiability statement.