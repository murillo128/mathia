# VIS-012 — Higher log-residual jets are reciprocal-power moments of the zero set

## Claim

Let `xi` be Riemann's entire xi function and let `rho` be a zero of exact multiplicity `m>=1`. Write

`xi(rho+w)=a_m w^m+a_(m+1)w^(m+1)+...`, with `a_m != 0`,

and remove the complete local zero monomial,

`H_rho(w)=xi(rho+w)/(a_m w^m)`, with the removable value `H_rho(0)=1`.

Choose the local logarithm with `log H_rho(0)=0`. Then for every integer `r>=2`,

`(log H_rho)^(r)(0)=(-1)^(r-1)(r-1)! sum_(rho' != rho) (rho-rho')^(-r)`,

where the nontrivial zeros `rho'` are counted with multiplicity and all copies of the local zero `rho` are omitted.

Thus every finite log-residual jet of order at least two is exactly a reciprocal-power moment of the remaining zero configuration. It is not an independent local geometric invariant created by the visualization.

For a critical-line zero `rho=1/2+i gamma`, the second normal derivative of the normalized modulus is

`kappa_rho := d^2/dx^2 log|H_rho(x)| |_(x=0) = - sum_(rho' != rho) (rho-rho')^(-2)`.

By `VIS-011`, this quantity is real. Under RH, writing every other zero as `rho'=1/2+i gamma'`, it becomes the positive inverse-square crowding field

`kappa_rho = sum_(gamma' != gamma) 1/(gamma-gamma')^2`.

**Evidence/status:** `CLASSICAL-HADAMARD + EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/BASELINE`.

No novelty is claimed for the Hadamard logarithmic-derivative identity or for inverse-square zero crowding. The durable research consequence is that a tempting family of reflection-even local visual statistics — finite Taylor/log jets after the zero monomial and reflection parity have been removed — collapses to classical functions of the zero set.

## Exact derivation

Use a genus-one Hadamard factorization

`xi(s)=exp(A+Bs) product_(rho') E_1(s/rho')`,

with `E_1(z)=(1-z)e^z` and zeros counted with multiplicity. For a zero `rho' != rho`,

`log E_1(s/rho') = log(1-s/rho') + s/rho'`.

The linear canonical correction disappears after the first derivative, and for every `r>=2`,

`d^r/ds^r log E_1(s/rho') |_(s=rho)
 = (-1)^(r-1)(r-1)! (rho-rho')^(-r)`.

The global exponential `A+Bs` also contributes nothing for `r>=2`.

For the `m` local factors at `rho`,

`E_1((rho+w)/rho)^m = (-w/rho)^m exp(m+mw/rho)`.

After division by `a_m w^m`, their contribution to `log H_rho` is constant plus linear in `w`, so it too vanishes after two derivatives. Summing the remaining factors gives the stated identity. For `r>=2` the reciprocal-power sum is absolutely convergent in the relevant canonical-product sense; in particular the reciprocal-square zero sum converges for the order-one xi zero set.

For `r=2`,

`(log H_rho)''(0) = - sum_(rho' != rho) (rho-rho')^(-2)`.

Along real normal displacement `w=x`, the real part is exactly the second derivative of `log|H_rho(x)|`. At a reflection-fixed critical-line zero, `VIS-011` already proves that `log|H_rho(x+iy)|` is even in `x`, so the second normal jet is the first nontrivial modulus jet but is completely determined by this reciprocal-square moment.

## Exact relation to the classical Lehmer-pair field

The second-order quantity is especially revealing because it lands directly on established Lehmer-pair machinery.

In the real entire-function normalization used by Csordas, Smith, and Varga for the de Bruijn-Newman family, let `x_k` and `x_(k+1)` be consecutive simple real zeros, let

`Delta_k = x_(k+1)-x_k`,

and define the normalized local residual at a zero by

`R_k(u)=H_0(x_k+u)/(H_0'(x_k)u)`.

Set

`C_k := -(log R_k)''(0) = sum_(j != k) 1/(x_k-x_j)^2`,

with zeros counted as in the canonical product. Their equation (1.12) defines

`g_k(0) = sum'_(j != k,k+1) [1/(x_k-x_j)^2 + 1/(x_(k+1)-x_j)^2]`.

Separating the mutual contribution of the pair gives the exact identity

`C_k + C_(k+1) = 2/Delta_k^2 + g_k(0)`.

Therefore the Csordas-Smith-Varga Lehmer-pair inequality, equation (1.11),

`Delta_k^2 g_k(0) < 4/5`,

is equivalently

`(Delta_k^2/2)(C_k+C_(k+1)) < 7/5`.

So even the gap-normalized average second log-residual curvature of a neighboring pair is not a new visual discriminator: it is an affine re-expression of the classical inverse-square crowding quantity used to define Lehmer pairs.

## Relevance to visual exploration

The accepted critical-strip multiscale clue has already removed three strong local confounds. `VIS-008` shows that the leading normalized portrait of any isolated analytic zero is the universal multiplicity monomial. `VIS-011` shows that after removing that monomial, the whole modulus residual at a critical-line zero is exactly reflection-even. The natural next temptation is to inspect the remaining curvature or a finite vector of higher Taylor coefficients and search for a critical-line signature.

The present result closes that route as an independent mechanism. For every fixed `r>=2`, the corresponding log-residual jet is just a reciprocal-power statistic of the rest of the zeros. A finite collection of jets therefore repackages finite-order zero-configuration moments. Any apparent discrimination must be compared first with classical gap statistics, pair correlation, inverse-power crowding, and related zero-set statistics rather than interpreted as new mesoscopic geometry.

This does not make such plots useless. They can be excellent visual instruments for seeing zero crowding or exceptional configurations. The epistemic point is narrower: the local jet itself carries no extra arithmetic information beyond the zero positions already entering its reciprocal-power sum.

## Prior art and novelty assessment

The canonical-product step is classical Hadamard factorization for an entire function of order one. No novelty is claimed for differentiating that product.

George Csordas, Wayne Smith, and Richard S. Varga, *Lehmer pairs of zeros, the de Bruijn-Newman constant Lambda, and the Riemann Hypothesis*, Constructive Approximation 10 (1994), 107–129, DOI `10.1007/BF01205170`, is the decisive prior-art boundary for the second-order interpretation. Their equation (1.7) records the relevant even canonical product, equation (1.12) defines the inverse-square interaction `g_k(0)`, and equation (1.11) gives the Lehmer-pair threshold.

The only Mathia-specific contribution persisted here is the exact bridge from the visual line's Taylor-normalized residual language to that classical zero-moment language, and the resulting negative control on what can count as a new mesoscopic visual mechanism.

## Boundary conditions and counterarguments

The formula deliberately starts at `r=2`. The first logarithmic derivative depends on the linear exponential/gauge term in a genus-one canonical product, so it is not represented by the same absolutely convergent raw reciprocal sum without a normalization convention.

For a multiple zero, all local copies of `rho` must be removed with the full monomial before the formula is applied. The statement then remains valid for the residual.

Without RH, the second moment at a critical-line zero is still constrained to be real by reflection symmetry, but it need not be expressible as a positive sum over real ordinates alone: off-line zeros contribute through their complex reflected configurations.

Most importantly, this result does **not** say that the complete finite-radius residual is determined by a small finite vector of moments, nor that all mesoscopic structure is classical. The full analytic germ contains the entire infinite sequence of moments, while a finite-radius view may encode nonlinear relations among many neighboring zeros and scale changes. The result closes only the route that treats one or finitely many local log jets as a new invariant.

## Consequence for the research line

The accepted clue [[research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md]] should now begin beyond finite-order local residual jets. A useful candidate must involve finite-radius or cross-scale organization that is not reducible to a small vector of reciprocal-power moments, ordinary local gaps, pair correlation, the Csordas-Smith-Varga Lehmer field, or another already classical zero-set statistic.

This raises the bar in a useful way: future visual structure has to survive not only the universal zero monomial and exact reflection parity, but also the classical zero-moment content of its local Taylor geometry.