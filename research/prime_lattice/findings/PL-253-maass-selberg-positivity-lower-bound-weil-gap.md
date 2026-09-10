# PL-253 — Maaß–Selberg positivity reaches the Weil zero distribution only through a signed remainder

## Claim

The live frontier after `PL-252` asks for a source-derived global Hermitian/test-function positivity that is already meaningful after analytic continuation and can constrain the principal Riemann-zeta divisor. Classical Arthur–Selberg theory gets substantially closer to this target than coefficient positivity does, but Tian An Wong's exact `SL(2)` analysis shows where the implication stops.

For positive-type automorphic test functions, Arthur truncation makes the relevant continuous spectral distribution `J^T_chi` positive-definite because it is an absolutely convergent integral of `L^2` inner products of truncated Eisenstein series. The same continuous spectral term contains the logarithmic derivative of the scattering/intertwining normalizing factor, whose completed Hecke `L`-quotient admits a Weil explicit-formula expansion over **all nontrivial zeros in the critical strip**. Thus this is a genuinely global, nonfactorizing Hilbert-space positivity source, not merely a positive Euler product in `Re(s)>1`.

However, after the Maaß–Selberg/explicit-formula decomposition, positivity gives only

`(1/2) sum_rho (g_hat(rho) + g_hat(-conj(rho))) >= -D_1(g) - D_2(g)`

for `g=g_0*g_0^*`, with `D_1` the remaining explicit-formula terms and `D_2` the normalized-intertwiner contribution. In the Riemann-zeta specialization Wong writes the corresponding lower bound explicitly. Weil's criterion instead requires the zero functional itself to be nonnegative for every admissible positive-type test function. The trace-formula positivity therefore does **not** transfer its sign directly to the zeta zero divisor: a residual geometric/scattering term must still be controlled with the correct sign (or removed by a stronger identity).

Moreover, the truncation height does not provide an asymptotic escape from this remainder. For fixed nonzero convolution-square `g`, the positive Maaß–Selberg expression has the exact shape

`Q_T(g) = g(1) log T + D(g) + B_T(g) >= 0`,

where `B_T(g)` is the oscillatory normalized-scattering boundary term. Wong records that `B_T(g)` has a finite limit up to `o(1)` as `T -> infinity`, whereas `g(1)>0` for a nonzero convolution square. Rearranging for the zero functional therefore produces a lower bound with a term `-g(1) log T+O(1)`, which tends to `-infinity`. Sending the truncation boundary outward cannot isolate Weil positivity; any useful optimization in `T` must occur at finite truncation and still requires a sign mechanism beyond the Maaß–Selberg norm itself.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT + NO-NOVELTY-CLAIM` for the route

`ordinary Arthur truncation + Maaß-Selberg positivity -> positive continuous spectral distribution -> Weil explicit zero sum -> RH sign automatically`.

The durable line-specific delta is that the strongest generic form of the "global Hermitian positivity after continuation" escape left open by `PL-252` is already classical in the continuous spectrum of `SL(2)`. It does couple the completed `L`-function to a positive global Hilbert-space object, but the desired Weil form is only one summand of that positive object. The remaining sign problem is not eliminated by the trace formula itself, and it is not removed by taking the truncation height to infinity.

## 1. The positive object is genuinely global and Hilbertian

Let `Lambda^T` denote Arthur's truncation. Wong recalls that truncated Eisenstein series are square-integrable and that `Lambda^T` is self-adjoint and idempotent. For the continuous spectral class indexed by `chi`, the coarse spectral distribution can be written, in the `SL(2)` case, as an absolutely convergent sum/integral of inner products of truncated Eisenstein series.

His Lemma 5.1 states that `J^T_chi(f)` is a positive-definite distribution. The proof is not coefficientwise: the relevant truncated intertwining kernel is represented by an `L^2` inner product, hence gives a positive self-adjoint operator, and a positive-definite automorphic test function `f*f^*` produces a nonnegative spectral integral.

For `F=Q`, Remark 5.2 makes the mechanism completely explicit with the Maaß–Selberg relation. Taking the boundary values on the unitary line and a convolution-square test function gives an integral of

`||Lambda^T E(.,1/2+ir)||_2^2 |g_hat_0(1/2+ir)|^2`,

which is nonnegative. This is exactly the sort of source-forced Hermitian positivity that cannot be dismissed by the primewise phase or scalar-factorization controls of the bare exponent lattice.

## 2. The same spectral term really sees the analytically continued zero divisor

The global intertwining operator factors into a normalizing scalar built from completed Hecke `L`-functions and normalized local intertwiners. Its logarithmic derivative enters the continuous spectral side through the Maaß–Selberg relation.

Wong's Theorem 1.1 identifies the contribution of that normalizing factor with a Weil explicit formula: a sum over the nontrivial zeros of the associated Hecke `L`-function plus prime-ideal and archimedean terms. His derivation keeps the analytic-continuation gate explicit. Euler-product expansions are used only after shifting to a half-plane of absolute convergence; the contour/functional-equation calculation and the meromorphic intertwining theory then supply the global identity. The zeros in the final formula range through the full critical strip, not only a zero-free or absolutely convergent region.

For the Riemann zeta function this is particularly well matched to the exponent-lattice mandate. The finite arithmetic contribution is supported on prime powers `p^k`, i.e. on the axis rays `k e_p`, and carries the usual energy `k log p = <k e_p,(log q)_q>`. But those prime-axis terms are now assembled together with the archimedean place, the scattering factor, and the zero divisor inside one global trace-formula distribution. The construction therefore supplies real local-to-global assembly beyond the standard Bohr torus.

## 3. Positivity yields a lower bound, not the Weil sign

Write Wong's explicit-formula distribution schematically as

`D(g) = (1/2) sum_rho (g_hat(rho)+g_hat(-conj(rho))) + D_1(g)`.

After separating the normalized-intertwiner term `D_2(g)`, Corollary 1.3 gives, for convolution-square tests,

`(1/2) sum_rho (g_hat(rho)+g_hat(-conj(rho))) >= -D_1(g)-D_2(g)`.

For zeta, functional-equation symmetry reduces this to the corresponding single zero sum, and Wong writes an explicit right-hand side involving the elementary/pole term, the von Mangoldt sum, the scattering term, and the archimedean integral. The truncation height `T` is an additional parameter; varying it may improve a particular finite-`T` numerical lower bound, but the theorem does not provide the sign needed by RH.

This distinction is exact. Wong's Theorem 2.3 states the Weil criterion in the same test-function language: RH for the relevant `L`-function is equivalent to positive-definiteness of the zero functional `W(g*g^*)=sum_rho (g*g^*)_hat(rho)`. Positivity of `J^T_chi` gives only `W >= -R_T`, where `R_T` is the residual trace-formula contribution. Without an independent theorem forcing `R_T<=0` (or an identity that cancels it while preserving the full admissible test class), the desired conclusion `W>=0` does not follow.

The obstruction is therefore **not** that the trace formula fails to see the critical strip or lacks a positive Hilbert-space source. It has both. The obstruction is the projection from positivity of the whole spectral expression to positivity of the particular zero-divisor summand selected by Weil's criterion.

## 4. The large-truncation limit makes the lower bound worse, not sharper

The truncation parameter itself admits a clean adversarial test. In the `SL(2,R)` specialization Wong writes the positive continuous contribution as

`Q_T(g) = g(1) log T - (1/(4 pi)) integral (m'/m)(it) g_hat(it) dt + (1/(4 pi i)) integral m(it) g_hat(it) T^(it) dt/t >= 0`.

The middle term is the same normalizing-factor distribution `D(g)` whose explicit-formula expansion contains the zero sum. Denote the last term by `B_T(g)`. Thus, in the zeta case and with Wong's decomposition `D=W+D_1`, positivity gives

`W(g) >= -D_1(g) - g(1) log T - B_T(g)`.

This is exactly the `T`-dependent version of the lower bound whose displayed Corollary 1.3 is evaluated at `T=1`. Wong explicitly notes that `T` may be varied and might optimize the bound for individual test functions.

That freedom cannot be exploited by sending `T` to infinity. Wong also records, citing Kubota's treatment of Eisenstein series, that the term containing `g_hat` satisfies

`B_T(g) = (1/4) m(0) g(0) + o(1)`

as `T -> infinity`. Hence `B_T(g)=O_g(1)`. On the other hand, for the admissible convolution square `g=g_0*g_0^*`, the value at the identity is a positive quadratic norm: directly from the multiplicative convolution convention, `g(1)>0` whenever `g_0` is nonzero. Equivalently, the transform on the unitary line is `|g_hat_0(1/2+ir)|^2`, and the corresponding Plancherel identity gives the same positivity.

Therefore, for every fixed nonzero admissible convolution square,

`-D_1(g) - g(1) log T - B_T(g) = -g(1) log T + O_g(1) -> -infinity`.

This does **not** say that every finite choice of `T` is useless: Wong's admissible range is `T>sqrt(3)/2`, and finite-`T` optimization can improve a numerical lower bound for a given `g`. It says something narrower and rigorous: **large truncation cannot asymptotically wash away the signed remainder or converge to the Weil-positive zero form**. The positive bulk norm grows like `g(1) log T`, while the oscillatory scattering boundary stays bounded, so solving the RH sign problem requires a finite-parameter sign/cancellation theorem or a different projection, not a `T -> infinity` limit.

This conclusion is an exact derived corollary of formulas already written by Wong, not a novelty claim. The literature search found no need for an additional theorem: the Maaß–Selberg formula, the `T`-dependent lower bound, the asymptotic of the boundary term, and the convolution-square positivity are all explicit in the same source.

## 5. This is strictly stronger as a control than `PL-252`

`PL-252` rules out a weaker inference: nonnegative Rankin–Selberg coefficients and a positive automorphic integral for real `s>1` do not constrain an inherited `zeta(s)` factor after continuation. One could still hope that a positive quadratic form **on the continued spectral object itself** would fix that defect.

The Maaß–Selberg construction is precisely that stronger matched control. The truncated Eisenstein norm is positive on the unitary spectral axis, while the logarithmic derivative of the meromorphic scattering factor is converted into a sum over all zeros by the explicit formula. Yet the sign remains attached to the whole continuous spectral distribution, not to its Riemann-zero component. Thus moving positivity from the physical Euler-product half-plane to a genuine global spectral trace is necessary but still not sufficient in the ordinary `SL(2)` trace formula.

This does not contradict Weil's criterion. Weil positivity is a specially isolated global quadratic functional of the zero divisor and is itself equivalent to RH. Wong's result instead demonstrates that an independently positive automorphic distribution can contain that functional together with additional terms of uncontrolled sign.

## 6. Prior art and novelty audit

The mechanism is established prior art; no new trace-formula theorem is claimed.

- **Tian An Wong**, “Explicit formulas for the spectral side of the trace formula of `SL(2)`,” *Acta Arithmetica* **195**(2) (2020), 149–175. DOI `10.4064/aa190115-9-10`; arXiv `1608.02296` (submitted 8 August 2016, revised 8 October 2019). Theorem 1.1 identifies the logarithmic derivative of the intertwining normalizing factor with a Weil explicit formula over Hecke-`L` zeros; Theorem 2.3 states the Weil positivity criterion; Lemma 5.1 proves positivity of the truncated continuous spectral distribution; Remark 5.2 gives the explicit Maaß–Selberg norm; Corollary 1.3 and its proof give the `T`-dependent lower bound for the zero sum, including the zeta specialization. Wong further states that the oscillatory `g_hat` term is `(1/4)m(0)g(0)+o(1)` as `T -> infinity`, citing Kubota, p. 107.
- Wong explicitly notes that the method is an average of the Maaß–Selberg relation in the spectral parameter and thereby sees all possible zeros in the critical strip. He also records that the support class for test functions relevant to known unconditional Weil-positivity checks remains restricted and presents the trace-formula lower bound as a possible route to larger support, not as a proof of the full criterion.
- The positivity input itself is standard Arthur truncation/Selberg–Maaß theory; Wong cites Arthur's trace-formula exposition for the general reductive-group statement. The present finding uses Wong because he places the positive spectral distribution, the explicit zero formula, the resulting lower bound, and the truncation-height dependence in one auditable theorem chain.
- A search for follow-up uses of the truncation parameter did not uncover a stronger theorem turning `T`-optimization into the full Weil sign. This is not evidence of nonexistence; the durable claim here needs only Wong's exact formulas to rule out the specific `T -> infinity` escape.

Internal duplication was checked against `PL-013`, `PL-033`, `PL-039`, and the current `PL-251`–`PL-252` frontier. `PL-013` stores the Weil form and modern zeta-spectral-triple context but not this automorphic positive-distribution decomposition. `PL-033` realizes zeros through automorphic scattering without forcing their location. `PL-039` shows that the unramified spherical scattering operator scalarizes the zeta channel after normalization. `PL-252` tests positivity before continuation. None records the stronger matched control here: **the standard automorphic trace formula already supplies a nonfactorizing positive Hilbert-space distribution whose continued spectral expansion contains the Weil zero functional, but positivity reaches that functional only modulo a residual term**.

## 7. Adversarial boundaries

1. **Not a no-go theorem for trace formulas.** A relative/stable trace formula, period identity, cohomological construction, or different truncation could isolate the zero functional more cleanly or give the residual term a sign. The obstruction concerns the ordinary Arthur–Selberg/Maaß–Selberg positivity chain audited here.
2. **No sign for the remainder is asserted.** The conclusion is logical: the published positivity theorem yields only a lower bound with `D_1+D_2`; it does not by itself imply the zero sum is nonnegative. Showing a suitable residual sign would be new mathematical input and could materially change the route.
3. **The test class matters.** Weil's criterion quantifies over the full admissible positive-type class. Positivity on a bounded-support subclass, or a lower bound optimized separately in `T`, cannot be promoted to RH without a theorem that preserves the required quantifiers and limiting topology.
4. **The large-`T` claim is fixed-test only.** The derivation holds for each fixed nonzero convolution square `g`: its `g(1) log T` term diverges while `B_T(g)=O_g(1)`. It does not rule out a coupled family `g_T` whose shape changes with `T`; such a route would need uniform control of support, normalization, Weil admissibility, and every remaining term before it could be relevant to RH.
5. **The zero sum is not obtained by termwise continuation of the Euler product.** The absolute-convergence manipulations and the meromorphic/global continuation steps are separated in Wong's derivation.
6. **Global does not automatically mean nonfactorizing at every representation-theoretic layer.** Local intertwiners and Euler factors still occur. The relevant nonfactorization here is the positive `L^2` norm/integrated trace distribution on the global automorphic quotient; the claim is not that all local tensor structure disappears.
7. **No novelty is inferred from prime-exponent coordinates.** Identifying the von Mangoldt support with exponent-lattice axis rays is only the line-specific dictionary. The mathematical content is the exact prior-art boundary between automorphic Hilbert positivity and Weil-divisor positivity.

## Research implication

The frontier should no longer be phrased merely as “find a global positive trace object whose continued spectral side contains zeta zeros.” Arthur–Selberg/Maaß–Selberg theory already provides such an object. Nor should the ordinary truncation parameter be treated as an asymptotic projection onto the zero functional: for every fixed nonzero admissible convolution square, the resulting lower bound deteriorates like `-g(1) log T` as `T -> infinity`.

The sharper obligation is to **isolate the principal zero-divisor quadratic form with no uncontrolled signed complement**, or to prove a canonical sign/coercivity theorem for that complement over the full Weil test class. A finite-`T` optimization would count only if it supplies such a theorem uniformly over the required test class; numerical improvement of individual lower bounds is not enough.

In prime-lattice terms, the local prime-power axis skeleton is already assembled with the archimedean and scattering data by a genuine global automorphic mechanism. What remains missing is not assembly but a sign-preserving projection from that assembly onto the zeta divisor. Any proposed relative trace, period, cohomological or operator construction should therefore be tested first for this exact failure mode: if its positive global form decomposes as `Weil-zero-form + remainder`, the route has advanced only if the remainder is canonically nonpositive, cancels, or is otherwise controlled strongly enough to recover the full Weil criterion.