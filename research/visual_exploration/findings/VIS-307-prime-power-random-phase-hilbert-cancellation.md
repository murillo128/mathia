# VIS-307 — exact prime-power support still cancels under independent coefficient phases

## Claim

Keep Wang's exact Dirichlet-polynomial coefficients from `VIS-302`--`VIS-304`,

`a_q = (Lambda(q)/sqrt(q)) min(q/x,x/q)`,

supported on the exact prime powers `q=p^k`. Let `(epsilon_q)` be independent Steinhaus variables, uniform on the unit circle, one for each prime-power support point, and define the support- and magnitude-preserving phase control

`D_x^epsilon(t)=sum_(q prime power) epsilon_q a_q q^(-it)`.

For an interval `I=(T,T+H]`, put

`R_I^epsilon = integral_I |D_x^epsilon(t)|^2 dt - H sum_q a_q^2`.

Then, uniformly in real `T` and `H>0`,

`E R_I^epsilon = 0`

and

`E |R_I^epsilon|^2 << x log^3(3x)`.

Consequently

`R_I^epsilon = O_p(sqrt(x) log^(3/2)(3x))`.

In particular, at the unresolved Wang boundary of `VIS-304`,

`H asymp x log log(3x)`,

one has

`R_I^epsilon/H -> 0`

in probability.

This control retains the **entire actual prime-power support, all prime-power spacings, and all Wang coefficient magnitudes**. It deliberately destroys only the deterministic relative coefficient phases, including the harmonic relation between powers of the same base prime. Therefore prime-power spacing geometry and coefficient size, by themselves, cannot sustain an `H`-scale signed endpoint remainder at `H asymp x log log x`. Any such obstruction for the true polynomial must use phase coherence that the control removes.

**Evidence/status:** `EXACT-DERIVED + EXACT-SUPPORT RANDOM-PHASE CONTROL + SIGNED-CANCELLATION NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No estimate for Wang's actual deterministic remainder, no random-multiplicative-function theorem, no prime-gap theorem, and no RH consequence is claimed.

## 1. Phase randomization diagonalizes the quadratic remainder exactly

For `q!=r`, write

`K_I(q,r)=integral_T^(T+H) exp(-it log(q/r)) dt`.

Expanding the squared modulus and removing the diagonal gives

`R_I^epsilon`
` = sum_(q!=r) epsilon_q conjugate(epsilon_r) a_q a_r K_I(q,r)`.

Every off-diagonal phase has zero expectation, so

`E R_I^epsilon=0`.

For the second moment, independence and unit-circle orthogonality imply

`E[epsilon_q conjugate(epsilon_r) conjugate(epsilon_s) epsilon_u]=0`

unless the oriented pair `(s,u)` equals `(q,r)` after the balance of phase exponents. Since `q!=r` and `s!=u`, the only surviving contribution to `E|R_I^epsilon|^2` is the identical oriented edge. Hence

`E |R_I^epsilon|^2`
` = sum_(q!=r) a_q^2 a_r^2 |K_I(q,r)|^2`.

Also

`|K_I(q,r)| <= 2/|log(q/r)|`.

Therefore

`E |R_I^epsilon|^2`
` <= 4 sum_(q!=r) a_q^2 a_r^2 / log^2(q/r)`.

This is the exact-support analogue of the product-torus orthogonality already used in `VIS-067` and of the torus `L^2` viewpoint in `VIS-213`. The new task is only to evaluate the resulting Wang-weighted prime-power spacing energy.

## 2. Comparable prime powers contribute at most `x log^3 x`

Put

`v_x(q)=min(q/x,x/q)`,

so

`a_q^2 = [Lambda(q)^2/q] v_x(q)^2`.

Partition the first variable into dyadic shells `Y<q<=2Y`. For the comparable region `q/2<r<2q`, both variables lie in an enlarged shell of scale `Y`, and

`|log(q/r)| asymp |q-r|/Y`.

On that enlarged shell,

`a_r^2 << [log^2(4Y)/Y] v_x(Y)^2`,

where replacing `v_x(r)` by `v_x(Y)` costs only an absolute constant. Thus for each fixed `q`,

`sum_(r!=q; q/2<r<2q) a_r^2/log^2(q/r)`
` << Y v_x(Y)^2 log^2(4Y) sum_(h!=0) 1/h^2`
` << Y v_x(Y)^2 log^2(4Y)`.

The classical summatory square-von-Mangoldt estimate used in `VIS-291`--`VIS-302` gives

`sum_(Y<q<=2Y) Lambda(q)^2 << Y log(3Y)`.

Hence

`sum_(Y<q<=2Y) a_q^2 << v_x(Y)^2 log(3Y)`.

Multiplying the two bounds, the comparable ordered-pair contribution with first variable on scale `Y` is

`<< Y v_x(Y)^4 log^3(4Y)`.

For `Y<=x`, this is

`<< (Y^5/x^4) log^3(4Y)`,

while for `Y>=x` it is

`<< (x^4/Y^3) log^3(4Y)`.

Both dyadic sums are dominated by `Y asymp x`, so the total comparable contribution is

`<< x log^3(3x)`.

This estimate uses no prime-gap asymptotic. Once the exact support has been retained, the square kernel is summable strongly enough that the crude integer separation `|q-r|>=1` and the established `Lambda^2` mass already suffice.

## 3. Noncomparable pairs are negligible on this scale

If `r<=q/2` or `r>=2q`, then

`|log(q/r)| >= log 2`.

Therefore the noncomparable contribution is at most a constant multiple of

`(sum_q a_q^2)^2`.

`VIS-291` and `VIS-302` give

`sum_q a_q^2 = log x + O(exp(-c V(log x)))`,

so this part is `O(log^2(3x))`, negligible compared with the comparable-pair bound.

Combining Sections 2 and 3 proves

`E |R_I^epsilon|^2 << x log^3(3x)`

uniformly in `T,H`.

Chebyshev gives, for every fixed `A>0`,

`P(|R_I^epsilon| > A sqrt(x) log^(3/2)(3x)) << A^(-2)`.

More importantly, for any fixed `eta>0`,

`P(|R_I^epsilon| > eta H)`
` << x log^3(3x)/H^2`.

At `H asymp x log log(3x)`, the right-hand side is

`<< log^3(3x)/[x (log log(3x))^2] -> 0`.

Thus the exact-support random-phase remainder is `o_p(H)` at the current pointwise boundary.

## 4. What information the control preserves and destroys

This is a stricter support control than `VIS-305`--`VIS-306`. The support is no longer Bernoulli: every actual prime power is retained. Therefore the control preserves exactly:

- all prime and prime-power locations;
- every small-gap and higher-order spacing relation among those locations;
- Wang's taper and coefficient magnitudes;
- the complete reciprocal-log spacing geometry that enters the absolute Hilbert majorant of `VIS-304`.

It does **not** preserve the deterministic phase relation among coefficients. In particular, assigning an independent `epsilon_(p^k)` to each prime power deliberately destroys the harmonic relation that would arise from one shared base-prime phase `epsilon_p^k`.

That loss is the point of the control rather than a hidden approximation. The question being falsified is whether the exact support geometry and coefficient magnitudes alone are enough to force an `H`-scale signed remainder. They are not: after only the phase organization is randomized, the signed quadratic form falls to root-mean-square scale `O(sqrt(x) log^(3/2)x)`.

This does not show that a stronger phase-preserving random multiplicative control would also cancel, and it does not estimate the true deterministic endpoint phases. Those are the next discriminating levels.

## 5. Prior art and novelty boundary

The phase-orthogonality calculation is classical. `VIS-067` already records product-torus orthogonality for independent prime phases, while `VIS-213` identifies related deterministic prime-phase quadratic forms with unit-modulus torus optimization. The present finding does not claim a new random-phase or quadratic-form theorem; it specializes the same elementary orthogonality to Wang's exact prime-power support and evaluates the resulting spacing energy at the active `x log log x` boundary.

General moment bounds for quadratic forms in independent variables go back at least to P. Whittle, **Bounds for the Moments of Linear and Quadratic Forms in Independent Variables**, *Theory of Probability and Its Applications* 5:3 (1960), 302--305, DOI `10.1137/1105028`. Phillip Ainsleigh, **A Method for Computing Moments of Quadratic Forms Involving Wrapped Random Variables**, *SIAM Journal on Matrix Analysis and Applications* 38:3 (2017), 887--909, DOI `10.1137/16M1082019`, treats moments of quadratic forms involving independent wrapped phases. Random Dirichlet polynomials with Steinhaus or other independent coefficients are also classical objects; none of that literature is being claimed as new here.

The targeted novelty audit found no reason to promote the exact second-moment identity itself. The durable Mathia content is the **matched-control conclusion**: even the true prime-power spacing pattern cannot explain the current Wang boundary without retaining additional deterministic phase coherence.

## Boundaries and falsification

The control randomizes one phase per prime-power support point, not one phase per base prime. It therefore does not preserve multiplicative phase coherence between `p,p^2,p^3,...`. A future obstruction surviving only under that coherence would be fully compatible with this finding.

The result is probabilistic over the artificial phase ensemble. It gives no pointwise estimate for the actual coefficient phases and no uniform statement over all possible phase assignments. Indeed `VIS-213`--`VIS-226` show in related prime-phase models that worst torus phases can behave very differently from Haar-typical phases.

The `x log^3 x` second-moment bound is deliberately coarse in logarithms. Improving that bound would sharpen the null but is unnecessary for separating it from `H asymp x log log x`.

Falsify the finding by finding an extra nonzero phase pairing in the exact second-moment expansion, a failure of the comparable-pair logarithmic-spacing bound, an error in the dyadic Wang-weight summation, or a contribution from noncomparable pairs exceeding the stated coefficient-mass bound.

## Dependencies

- `VIS-291` and `VIS-302`: asymptotics for `sum Lambda(n)^2` and `sum a_n^2`.
- `VIS-304`: actual prime-power support and the `x log log x` weighted-Hilbert boundary.
- `VIS-305`--`VIS-306`: density/parity Bernoulli spacing and signed-remainder controls.
- `VIS-067`: exact product-torus covariance under independent phase randomization.
- `VIS-213`: torus `L^2` versus worst-phase distinction for related prime-phase quadratic forms.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue.

## Research consequence

The moving upper-source frontier narrows again. `VIS-306` showed that density/parity sparsity does not sustain an `H`-scale signed remainder. The present exact-support control removes the next candidate explanation: **prime-power spacing correlations and Wang coefficient magnitudes still do not suffice when deterministic coefficient phases are randomized**.

Therefore a genuine obstruction near `H asymp x log log x` must use information carried by deterministic phase organization, such as coherent relations among base-prime harmonics or alignment of the actual endpoint phases with the weighted prime-power interaction matrix. Conversely, a cancellation theorem for the true phases would move Wang's pointwise boundary further. The next matched control should preserve a concrete phase-coherence mechanism rather than merely refine support geometry again.