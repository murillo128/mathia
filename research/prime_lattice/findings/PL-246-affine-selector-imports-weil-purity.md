# PL-246 — The affine null-root selector becomes canonical only after scalar Pochhammer normalization; its global extra symmetry imports Weil purity rather than deriving zero localization

## Claim

`PL-245` left one precise affine escape open: Weyl symmetry leaves one-variable freedom along the minimal imaginary root `delta`, but an additional arithmetic/local-global selector might canonically determine that factor and perhaps create an RH-relevant constraint. Popa–Walsh's 2026 treatment of quadratic `\widetilde A_1` supplies the cleanest available test of exactly that escape.

In this model the extra, non-Weyl functional equation does canonically determine the untwisted null-root factor, but the factor is the one-variable Pochhammer product

`N_0(x;u)=(u^2 x;x^2)_infty`.

It is then divided out in the normalized local factor used for the global local-to-global identity. For the twisted global multiple Dirichlet series, the same extra symmetry does see the nontrivial quadratic `L`-data, but only after the coefficients have been assigned their `q`-Weil weights. That weight assignment uses the Riemann hypothesis for the underlying function-field curves: after the standard `1/2` centering, the geometric `L`-factor has weight zero and is therefore fixed by the extra action. Consequently the proof of the extra functional equation computes its nontrivial multiplier entirely from explicit Pochhammer factors while the zero-bearing geometric factor cancels from the transformation.

Thus the known affine selector does **not** provide a mechanism that derives critical-line localization from imaginary-root/Weyl geometry. In the explicit `\widetilde A_1` case, the new affine symmetry has two parts: a scalar null-root normalization whose divisor is an explicit `q`-product, and a geometric `L`-factor whose critical normalization is already supplied by Weil purity. The latter is invariant under the extra action once that purity is input.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. The formulas, the extra functional equations, and the use of `q`-Weil weights are theorem-level prior art in Popa–Walsh. The RH-facing conclusion is an exact structural audit of their proof. It is decisive only against using this known `\widetilde A_1` selector or its bare weight symmetry as an independent localization mechanism. It does not rule out higher affine types with genuinely nonseparable selector data, number-field constructions carrying an independent positivity/self-adjointness principle, or an arithmetic mechanism that proves the analogue of purity rather than assuming it.

## The one-variable freedom of `PL-245` is explicitly selected in `\widetilde A_1`

For `\widetilde A_1`, let `delta=alpha_0+alpha_1`, write `x=x^delta=x_0x_1`, and let `u` be the parameter with `u^2=q` in the Chinta–Gunnells average. Popa–Walsh exhibit the Weyl-invariant comparison function

`F_0(x_0,x_1;u)=1/[(u x_0;x)_infty (u x_1;x)_infty]`.

Their affine decomposition gives

`Z_0(x_0,x_1;u)=N_0(x;u) F_0(x_0,x_1;u)`,

where the entire residual freedom is the one-variable null-root factor `N_0`. This is exactly the affine one-dimensional freedom isolated abstractly in `PL-245`.

The extra transformation `tau` sends `u -> u x`. Popa–Walsh prove that it commutes with the Chinta–Gunnells Weyl action after multiplication by an explicit rational cocycle, and derive the scalar recurrence

`N_0(x;u)=(1-u^2 x)N_0(x;ux)`.

Combining this with the `u=-1` specialization supplied by the affine Macdonald identity fixes the factor uniquely in the relevant power-series class:

`N_0(x;u)=(u^2 x;x^2)_infty = product_(k>=0) (1-u^2 x^(2k+1))`.

Hence

`Z_0(x_0,x_1;u)=(u^2 x;x^2)_infty / [(u x_0;x)_infty (u x_1;x)_infty]`.

This is a genuine selector beyond the affine Weyl group, but its output is still a scalar function of the single null-root coordinate. Its zeros and poles are the explicit `q`-geometric divisor of a Pochhammer product; no Riemann-zero divisor has emerged from the selection step.

The fundamental-weight twist gives an even sharper control. For `Z_{omega_1}`, the analogous recurrence is

`N_{omega_1}(x;u)=N_{omega_1}(x;u x^2)`,

and the `u=0` specialization forces

`N_{omega_1}(x;u)=1`.

Thus adding a nontrivial affine twist does not by itself make the imaginary-root selector spectrally richer in this rank-one affine model.

## The canonical normalization removes the selected null-root factor

The global function-field construction makes the role of the Pochhammer selector especially transparent. For the untwisted local factor Popa–Walsh define

`\widetilde Z_0 = Z_0/(u^2 x^delta;x^(2delta))_infty`

and therefore obtain simply

`\widetilde Z_0(x_0,x_1;u)=1/[(u x_0;x^delta)_infty (u x_1;x^delta)_infty]`.

They choose this normalization precisely so that the global untwisted multiple Dirichlet series satisfies the local-to-global identity. In other words, the extra functional equation succeeds in fixing the affine imaginary-root ambiguity, but the fixed factor is then recognized as the correction that must be normalized away to recover the canonical global object.

This is consistent with the broader affine/Kac–Moody literature: imaginary-root correction factors are established features of affine denominator, spherical, and Whittaker formulas, and in affine type their explicit determination is tied to Macdonald-type constant-term/product identities. The existence of such a correction factor is therefore not evidence of a new zeta-zero mechanism.

## The twisted global series contains genuine `L`-zeros, but the extra symmetry treats them as already pure

The more serious test is the twisted global `\widetilde A_1` multiple Dirichlet series over `F_q[t]`, because it contains actual quadratic `L`-functions rather than only the local Pochhammer correction. For coprime square-free twisting polynomials `c_0,c_1`, Popa–Walsh prove the explicit factorization

`Z(s;c_0,c_1)`

`= product_(n>=0, n even) L(1/2+s_0+n delta(s),chi_{c_0}) L(1/2+s_1+n delta(s),chi_{c_1})`

`  * product_(n>=0, n odd) L(1/2+s_0+n delta(s),chi_{c_1}) L(1/2+s_1+n delta(s),chi_{c_0}),`

where `delta(s)=s_0+s_1`. This formula is valid on the full interior `Re delta(s)>0` of the affine complexified Tits cone in this case, apart from the stated elementary poles when a twisting character is trivial. Thus the continuation being used here is theorem-level continuation of the multiple Dirichlet series, not a formal continuation of an Euler product.

For nontrivial square-free `d`, the relevant quadratic function-field `L`-function is

`L(s,chi_d)=(1-q^(-s))^(epsilon_d) P_{C_d}(q^(-s))`,

where `C_d: y^2=d(t)` is the associated hyperelliptic curve. Write

`P_{C_d}(T)=product_j (1-alpha_j T)`.

At this point Popa–Walsh explicitly invoke the Riemann hypothesis for curves over finite fields, proved by Weil, to assert that every `alpha_j` is a `q`-Weil number of weight one:

`|sigma(alpha_j)|=q^(1/2)`

for every complex embedding/Galois conjugate `sigma`. This is exactly the purity statement that places the zeros of the curve numerator on their critical circle.

Their extra global action `tau` is then defined coefficientwise by weight: a `q`-Weil number `alpha` of weight `m` is replaced by `alpha x^(m delta)`. After the `1/2` shift in the displayed `L`-factors, the geometric polynomial part has weight-zero coefficients. Popa–Walsh therefore obtain

`W_geom^tau = W_geom`.

They explicitly use this identity in the proof of their global extra functional equation (Theorem 6.9): the ratios `W/W^tau` and `W/W^(tau^2)` are computed from the remaining Pochhammer factors. The part containing the nontrivial curve `L`-zero data does not contribute to the multiplier.

## Exact matched control: the extra action is blind to the zero phases once purity is supplied

The previous step is more than a historical observation about what theorem was cited. It gives a direct matched-control obstruction.

Suppose a geometric numerator has roots `alpha_j=q^(1/2) e^(i theta_j)` (or the corresponding algebraic/Galois package) with arbitrary phases `theta_j` compatible with its other algebraic constraints. After centering by `1/2`, each normalized root `q^(-1/2) alpha_j` has weight zero. The `tau` action used in Theorem 6.9 therefore fixes its contribution regardless of the angular positions `theta_j`.

Those phases determine the heights of the function-field zeros along the critical line. The extra affine symmetry is insensitive to them once their common modulus `q^(1/2)` has been supplied. Conversely, the common modulus is exactly the function-field RH/purity input used to define the weight-zero geometric block in the proof. Thus the new symmetry cannot be read backwards as an independent derivation of that modulus without circularity.

This also separates two notions that can otherwise look deceptively similar:

- the affine transformation `u -> u x^delta` and its Pochhammer cocycle determine the imaginary-root normalization;
- the `1/2` centering of the zero-bearing geometric factor is justified by Weil purity, after which that factor is fixed by the extra action.

The first does not imply the second.

## Why this does not transfer an RH mechanism to the rational-prime lattice

The `prime_lattice` target asks for a structure that could explain why the ordinary zeta divisor is localized at `Re(s)=1/2`, rather than merely packaging that divisor after its critical normalization is known. The explicit affine function-field model fails this test in a particularly informative way.

For a curve over `F_q`, Frobenius gives a finite-dimensional cohomological object whose eigenvalues carry integer weights, and Weil's theorem supplies the absolute-value rule `q^(m/2)`. Popa–Walsh can therefore build their extra action directly on the resulting `q`-Weil grading. In the ordinary Riemann-zeta problem there is no already-proved analogue assigning the hypothetical zero-bearing spectral data a purity weight that forces real part `1/2`. Declaring such a weight from the desired modulus would simply insert RH into the construction.

Accordingly, the transferable lesson is not that affine null roots single out the critical line. It is that **a source of purity external to the affine Weyl symmetry can make an extra affine functional equation compatible with a critical normalization**. For the rational primes, finding the analogue of that source of purity is the hard problem; the free exponent lattice and the affine correction factor do not supply it.

## Adversarial controls and boundaries

**The result does not say that the full twisted MDS is zero-blind.** The explicit product in Theorem 6.5 certainly contains the full quadratic `L`-polynomials, hence their zeros. The narrower statement is that the *extra affine `tau` symmetry and its selector* do not derive their critical modulus: the geometric factor is invariant in the proof only after Weil weights are known.

**Ordinary Weyl functional equations remain present.** This finding does not claim that every symmetry of the MDS cancels the geometric data. It isolates the additional non-Weyl symmetry left open by `PL-245`, because that was the candidate mechanism under test.

**`\widetilde A_1` is degenerate.** Popa–Walsh explicitly caution that its unusually explicit formulas should not be expected verbatim for other affine root systems. A higher-rank affine selector could retain genuinely mixed variables or interact nonseparably with arithmetic data. Such a construction would evade this finding only if the interaction itself supplies a localization principle rather than merely accepting a pre-existing purity grading.

**Pochhammer divisors can still matter analytically.** The fact that the null-root correction is scalar does not make it irrelevant to continuation, poles, moment asymptotics, or Kac–Moody representation theory. The negative conclusion is only RH-facing: its explicit divisor is not an independently localized Riemann-zeta divisor.

**Function-field RH is legitimate input in the cited theorem.** There is no criticism of Popa–Walsh's argument. Their use of Weil purity is a strength of the function-field theory. It becomes an obstruction only if this theorem is proposed as a noncircular model for proving ordinary RH.

## Prior-art and novelty audit

The decisive source is Alexandru A. Popa and Jack Walsh, “A decomposition of Weyl group multiple Dirichlet series for symmetrizable Kac-Moody root systems,” arXiv:2607.11834v1 (13 July 2026). Their Theorem 6.1 gives the explicit untwisted `\widetilde A_1` Pochhammer factor; Theorem 6.3 gives the fundamental-weight case; Theorem 6.5 gives the global product of shifted quadratic function-field `L`-functions; Definition 6.8 and Theorem 6.9 define and prove the extra weight action, with the proof explicitly invoking the Weil-number structure of the hyperelliptic numerator and using `W_geom^tau=W_geom`.

The imaginary-root correction-factor phenomenon itself is much older. I. G. Macdonald, “Affine root systems and Dedekind's eta-function,” *Inventiones Mathematicae* **15** (1972), 91–143, supplies the affine denominator/product identity used in the `\widetilde A_1` specialization. In the Kac–Moody spherical/Whittaker setting, Dinakar Muthiah, Anna Puskás, and Ian Whitehead, “Correction factors for Kac-Moody groups and t-deformed root multiplicities,” arXiv:1806.05209, treats these correction factors as established imaginary-root data and notes that the affine factor is classically known through Macdonald's constant-term theory.

No novelty is claimed for the formulas or for the fact that Popa–Walsh use Weil numbers. The useful line-level contribution is the **routing conclusion**: the most explicit known arithmetic selector for the affine one-variable freedom of `PL-245` separates into a scalar Macdonald/Pochhammer correction and a zero-bearing geometric block whose critical purity is an input to the extra symmetry, not its output.

## Research implication

The surviving affine search should no longer ask merely for an extra functional equation that selects the null-root factor. That phenomenon already exists and, in the cleanest solvable case, does not generate zero localization.

A viable next affine mechanism must pass a stronger test: after isolating the same divisor intended to model the ordinary Riemann zeros, its source-forced arithmetic/representation-theoretic structure must **prove** the analogue of purity or positivity that fixes the critical real part. A transformation that becomes well-defined or trivial on the zero-bearing component only after assigning it the desired weight is a control, not a solution.
