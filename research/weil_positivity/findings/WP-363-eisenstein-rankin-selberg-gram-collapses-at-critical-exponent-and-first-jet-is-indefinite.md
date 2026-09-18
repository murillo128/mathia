---
id: WP-363
title: Eisenstein Rankin--Selberg Gram positivity collapses at the critical exponent, and its first nonzero jet is indefinite
branch: weil_positivity
status: supported
kind: rankin-selberg-critical-gram-obstruction
claim_strength: exact two-parameter Hecke Gram factorization, critical collapse, and first-jet non-positivity
created: 2026-09-18
related: [WP-237, WP-345, WP-357, WP-361, WP-362]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - B. M. Wilson, Proofs of Some Formulae Enunciated by Ramanujan, Proceedings of the London Mathematical Society (2) 21 (1923), 235-255, DOI 10.1112/plms/s2-21.1.235
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - E. C. Titchmarsh, The Theory of the Riemann Zeta-function, 2nd ed. revised by D. R. Heath-Brown, Oxford University Press, 1986
---

# WP-363 — Eisenstein Rankin--Selberg Gram positivity collapses at the critical exponent, and its first nonzero jet is indefinite

## Claim

`WP-361` and `WP-362` classify the scalar level-one Hecke--Eisenstein route: at fixed spectral parameter the finite Hecke Gram is rank one, the critical all-prime multiplier does not converge ordinarily, and the canonical Hecke Euler completion is a conjugate-product scalar whose logarithmic derivative imports the zeta divisor. A natural remaining escape is to **not fix the Eisenstein spectral parameter before taking positivity**. One can instead correlate the full family of Hecke eigenvalue vectors across two parameters. This produces a canonical, genuinely non-scalar positive kernel in the half-plane of absolute convergence.

That stronger object still fails exactly at the Weil exponent.

For real `r`, let

\[
\lambda_r(n)=n^{ir}\sigma_{-2ir}(n)
\tag{1}
\]

be the normalized level-one Eisenstein Hecke eigenvalue from `WP-361`. For real `s>1`, define the two-parameter coefficient Gram

\[
K_s(r,u)
:=\sum_{n\ge1}\frac{\lambda_r(n)\lambda_u(n)}{n^s}.
\tag{2}
\]

Since `lambda_r(n)` is real on the unitary axis, for every finite family `r_1,...,r_m` and coefficients `c_j`,

\[
\sum_{i,j}\overline{c_i}c_jK_s(r_i,r_j)
=\sum_{n\ge1}\frac{1}{n^s}
\left|\sum_jc_j\lambda_{r_j}(n)\right|^2
\ge0.
\tag{3}
\]

Thus `K_s` is a positive-semidefinite kernel for every real `s>1`. Unlike the fixed-`r` Gram of `WP-361`, this kernel has genuine spectral-parameter rank.

The classical Ramanujan--Wilson divisor-product identity, equivalently a direct Euler-factor calculation, gives the exact meromorphic continuation

\[
\boxed{
K_s(r,u)
=
\frac{
\zeta(s+i(r+u))
\zeta(s+i(r-u))
\zeta(s-i(r-u))
\zeta(s-i(r+u))
}{\zeta(2s)}.
}
\tag{4}
\]

The denominator is decisive. Because `zeta(2s)` has its simple pole at `s=1/2` while all four numerator arguments then have real part `1/2`,

\[
\boxed{K_{1/2}(r,u)=0\qquad\text{for every real }r,u.}
\tag{5}
\]

So the canonical analytic continuation of the positive Rankin--Selberg coefficient Gram does not produce a nontrivial positive critical kernel: **the entire Gram collapses to zero at exactly the Weil half-density exponent**.

The minimal scalar renormalization does not rescue positivity. Since

\[
\frac1{\zeta(2s)}
=2\left(s-\frac12\right)
+O\!\left(\left(s-\frac12\right)^2\right),
\tag{6}
\]

the first nonzero transverse jet is

\[
\boxed{
J(r,u)
:=\frac12\left.\partial_sK_s(r,u)\right|_{s=1/2}
=
F(r+u)F(r-u),
}
\tag{7}
\]

where

\[
F(t):=\left|\zeta\!\left(\frac12+it\right)\right|^2.
\tag{8}
\]

This kernel is entrywise nonnegative but **not positive semidefinite**. Let `gamma!=0` be the ordinate of any known critical-line zero `zeta(1/2+i gamma)=0` (Hardy's theorem gives infinitely many), and put `r=gamma/2`. Then

\[
J(r,r)=F(\gamma)F(0)=0.
\tag{9}
\]

For a positive-semidefinite kernel, a zero diagonal entry forces the whole corresponding row to vanish by Cauchy--Schwarz. But the critical zeros are discrete, so one may choose a real `u` for which neither `r+u` nor `r-u` is a zero ordinate. Then

\[
J(r,u)=F(r+u)F(r-u)>0.
\tag{10}
\]

The `2 x 2` principal minor on `{r,u}` therefore has determinant

\[
J(r,r)J(u,u)-J(r,u)^2=-J(r,u)^2<0.
\tag{11}
\]

Hence the first nonzero critical jet, equivalently the bare renormalization obtained by cancelling the universal `1/zeta(2s)` zero, has lost the Gram sign.

Finally, the logarithmic readout exposes the same carrier/sign bifurcation as `WP-362`, now for the non-scalar kernel. In `Re s>1`,

\[
\boxed{
-\partial_s\log K_s(r,u)
=
4\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
\cos(r\log n)\cos(u\log n)
-2\sum_{n\ge2}\frac{\Lambda(n)}{n^{2s}}.
}
\tag{12}
\]

At the formal critical value the first term has the desired linear Mangoldt half-density `Lambda(n)/sqrt(n)`, while the second is the universal diagonal correction forced by the Rankin--Selberg square. Meromorphically, the same readout has the universal pole coming from `2 zeta'(2s)/zeta(2s)` at `s=1/2` and the zero-divisor poles of the four shifted zeta factors. Thus the operation that reveals the linear Weil carrier again acts only **after** inherited positivity has disappeared.

The conclusion is an exact obstruction to the most canonical two-parameter Rankin--Selberg escape from scalarization:

\[
\boxed{
\text{positive non-scalar Hecke Gram for }s>1
\;\xrightarrow{\text{canonical continuation}}\;
0\text{ at }s=\frac12,
\qquad
\text{first nonzero jet is indefinite.}
}
\tag{13}
\]

A surviving automorphic route must therefore obtain its sign from a different source-defined operation that couples finite and archimedean/scattering data **before** this Rankin--Selberg diagonal factor kills the critical Gram. Merely taking the natural coefficient Gram, cancelling its universal diagonal factor, or applying a logarithmic derivative does not supply Weil positivity.

**Classification:** `CLASSICAL-RAMANUJAN-WILSON + RANKIN-SELBERG-GRAM + EXACT-DERIVED + NONSCALAR-POSITIVE-HALFPLANE + CRITICAL-COLLAPSE + FIRST-JET-INDEFINITE + LOG-DERIVATIVE-DIVISOR-OBSTRUCTION + NEGATIVE/NARROWING + NO-NOVELTY-CLAIM-FOR-CLASSICAL-IDENTITIES`.

## 1. The two-parameter kernel is an intrinsic positive Gram before continuation

For a prime `p`, write `theta_r=r log p`. The normalized Eisenstein eigenvalues satisfy

\[
\lambda_r(p^k)
=\sum_{j=0}^k e^{i(k-2j)\theta_r}.
\tag{14}
\]

A direct geometric-series computation gives the local correlation identity

\[
\sum_{k\ge0}
\lambda_r(p^k)\lambda_u(p^k)x^k
=
\frac{1-x^2}{
(1-e^{i(\theta_r+\theta_u)}x)
(1-e^{i(\theta_r-\theta_u)}x)
(1-e^{-i(\theta_r-\theta_u)}x)
(1-e^{-i(\theta_r+\theta_u)}x)
}.
\tag{15}
\]

With `x=p^{-s}`, multiplying (15) over primes yields (4). The global denominator

\[
\prod_p(1-p^{-2s})=\frac1{\zeta(2s)}
\tag{16}
\]

is therefore not an arbitrary regularizer: it is forced locally by the Hecke recurrence in the **coefficient square itself**. This is precisely why the obstruction is stronger than saying that some chosen analytic completion happens to vanish at the critical point.

For real `s>1`, the vectors

\[
v_r^{(s)}
:=\left(\lambda_r(n)n^{-s/2}\right)_{n\ge1}
\in\ell^2(\mathbb N)
\tag{17}
\]

are well defined and

\[
K_s(r,u)=\langle v_r^{(s)},v_u^{(s)}\rangle.
\tag{18}
\]

Thus the positivity in (3) is an ordinary Hilbert-space theorem, not a sign inferred from zeta zeros or from the desired Weil criterion. It is exactly the kind of independent positivity the branch is seeking, but only in the absolutely convergent region.

This also distinguishes the construction from `WP-361`. At a fixed `r`, all vectors `T_pE_r` are collinear on the Eisenstein eigenline, so the finite-prime Hecke Gram has rank one. Here the index set is the continuum of spectral parameters, and `K_s(r,u)` measures correlations of their full Hecke coefficient vectors. The candidate is therefore genuinely non-scalar before analytic continuation.

## 2. The critical exponent is a forced zero of the whole Gram

At `s=1/2`, none of the four numerator factors in (4) has a pole, because their real parts are all `1/2`. The denominator `zeta(2s)` has the classical simple pole at `1`. Hence `1/zeta(2s)` has a simple zero and equation (5) follows uniformly pointwise in real `r,u`.

This collapse is independent of RH. It does not matter whether additional zeta zeros lie off the critical line; they can only create more zeros in the numerator. The positive Gram that exists for `s>1` therefore reaches the Weil exponent only as the zero form.

One might try to interpret this as a harmless normalization artifact and divide out the vanishing scalar. Equation (15) shows why that move is not innocent: the factor `1-p^{-2s}` occurs at every prime in the exact local correlation identity. Removing the global product changes the coefficient-square object from which positivity came. The next section shows that this loss is visible immediately at the first nonzero critical jet.

## 3. The first nonzero critical jet fails the PSD test exactly

Equation (6) follows from the Laurent expansion `zeta(1+epsilon)=epsilon^{-1}+O(1)`. Differentiating (4) at `s=1/2` then gives (7) without differentiating any numerator factor, because the reciprocal-zeta factor itself vanishes there.

For real `r,u`, the four numerator factors pair by complex conjugation:

\[
\begin{aligned}
J(r,u)
&=
\left|\zeta\!\left(\frac12+i(r+u)\right)\right|^2
\left|\zeta\!\left(\frac12+i(r-u)\right)\right|^2\\
&=F(r+u)F(r-u).
\end{aligned}
\tag{19}
\]

Every entry is nonnegative. That is much weaker than positive-semidefinite kernel positivity. The critical-line zeros provide an exact separator.

Hardy's theorem that infinitely many nontrivial zeros lie on `Re s=1/2` is unconditional. Fix one such ordinate `gamma`. Because zeta is meromorphic and not identically zero, its zeros on the line are discrete. Therefore one can choose `u` outside the discrete union of translates that would make either `r+u` or `r-u` a zero ordinate. Equations (9)--(11) then give a negative principal determinant.

This falsification uses known zero existence only as a **control on the candidate kernel**. The construction of `K_s`, its positivity for `s>1`, its continuation, and its critical renormalization are all defined independently of the zero set. No zero data are inserted into the proposed geometry.

The result also rules out every scalar first-order renormalization with the same critical zero. If `a(s)` is scalar in `r,u` and `a(s)K_s` has a finite nonzero limit proportional to `J` at `s=1/2`, then a positive scalar multiple has the same negative `2 x 2` minor, while a negative scalar multiple already has nonpositive diagonal. Thus the bare scalar cancellation of the universal critical zero cannot preserve a nontrivial PSD limit.

## 4. The logarithmic derivative recovers the right scale only after the sign is gone

Taking the logarithmic derivative of (4) gives

\[
\begin{aligned}
-\partial_s\log K_s(r,u)
={}&-\frac{\zeta'}{\zeta}(s+i(r+u))
-\frac{\zeta'}{\zeta}(s+i(r-u))\\
&-\frac{\zeta'}{\zeta}(s-i(r-u))
-\frac{\zeta'}{\zeta}(s-i(r+u))
+2\frac{\zeta'}{\zeta}(2s).
\end{aligned}
\tag{20}
\]

Expanding each logarithmic derivative in its common half-plane of absolute convergence yields (12), using

\[
\cos((r+u)L)+\cos((r-u)L)
=2\cos(rL)\cos(uL).
\tag{21}
\]

The first term of (12) is exactly at the critical half-density when `s=1/2`; it is linear in `Lambda(n)`, not squared. This is the attractive part of the route. But the same operation also exposes two unavoidable features.

First, `2 zeta'(2s)/zeta(2s)` has a simple pole at `s=1/2`, reflecting the zero of the original Gram. Removing that pole means choosing a finite-part normalization after positivity has already degenerated.

Second, each shifted `zeta'/zeta` has poles on the shifted zeta divisor. Thus the meromorphic continuation that gives meaning to the critical Mangoldt readout already contains the zero data whose sign is supposed to be constrained. Taking an absolute square afterward recreates tautological positivity while changing the linear Weil object, exactly as in the scalar control `WP-362`.

So the two-parameter Gram does improve the geometry—there is genuine non-scalar correlation before continuation—but it does not improve the logical order of the sign theorem.

## 5. Matched controls and attempted escapes

**Keep `s>1` and approach the critical value through positivity.** The Hilbert Gram theorem is valid in the absolute-convergence region. The meromorphic path to `s=1/2` crosses the Rankin--Selberg singular structure around `s=1`; there is no continuous PSD extension whose nonzero limit is forced by (3). The exact continuation at the target is the zero kernel, and its first nonzero jet is already indefinite.

**Multiply by `zeta(2s)` before taking the limit.** This is the minimal cancellation of the universal local factor and produces exactly `J`. Equations (9)--(11) show that `J` is not PSD. The factor cannot be dismissed as a harmless common normalization if the inherited Gram sign is the intended theorem.

**Use the diagonal only.** On the diagonal,

\[
J(r,r)=|\zeta(1/2+2ir)|^2|\zeta(1/2)|^2\ge0.
\tag{22}
\]

This returns to conjugate-product positivity of the type already classified in `WP-362`: it is true regardless of off-critical zeros and discards the non-scalar cross-parameter information that motivated the route.

**Take absolute values or squares of the off-diagonal kernel.** Entrywise positivity is already present in `J`; the failure is matrix positivity. Squaring entries does not supply a source theorem that all principal minors are nonnegative, and it further moves away from the linear Weil carrier.

**Choose spectral parameters avoiding critical zeros.** Positive-semidefinite kernel positivity is a statement for the whole source-defined parameter domain, not a test-dependent subset selected after inspecting zeta values. More importantly, deleting zero ordinates would explicitly use the target divisor to define the geometric domain, which is excluded by the research mandate.

**Add Gamma factors.** A regular nonzero scalar completion in the continuation variable cannot change the zero-kernel conclusion or the sign of a first nonzero jet up to scalar. A genuinely nonseparable archimedean kernel could change the matrix structure, but that would be a new construction requiring its own independent positivity theorem; it is not inherited from the coefficient Gram proved here.

## 6. Prior-art and novelty boundary

No novelty is claimed for the divisor-product identity, its Euler product, Rankin--Selberg convolution, the pole of `zeta(s)` at `s=1`, or the existence of infinitely many critical-line zeros.

The exact generalized divisor identity underlying (4) is classical Ramanujan--Wilson:

\[
\sum_{n\ge1}\frac{\sigma_a(n)\sigma_b(n)}{n^w}
=
\frac{\zeta(w)\zeta(w-a)\zeta(w-b)\zeta(w-a-b)}{\zeta(2w-a-b)},
\tag{23}
\]

in its domain of absolute convergence, with meromorphic continuation supplied by the right-hand side. Wilson's 1923 paper is a primary historical anchor; standard Rankin--Selberg treatments place such coefficient correlations in the automorphic convolution framework. Hardy's 1914 theorem supplies the unconditional critical-line zero used in the PSD falsification; Titchmarsh is the standard reference.

A bounded literature audit around Ramanujan--Wilson divisor products, Eisenstein Rankin--Selberg convolution, and critical-line zeros did not surface a theorem presented as the specific Mathia no-go above. That is not a historical novelty proof. The Mathia-specific contribution is the **exact use of the classical two-parameter coefficient Gram as a candidate sign mechanism and the identification of its critical failure mode**: the locally forced `1/zeta(2s)` factor annihilates the entire positive kernel at `s=1/2`, while the first source-defined nonzero jet fails a `2 x 2` PSD test because of unconditional critical-line zeros.

This is materially stronger than observing that a scalar completed `L`-value is a modulus square. It tests a genuine non-scalar positive kernel before scalarization and shows precisely where its sign is lost.

## 7. Consequence for the Maaß--Selberg / Hecke frontier

The accepted Maaß--Selberg clue remains open only in a narrower category. `WP-361` showed that fixed-parameter Hecke amplification is rank-one and ordinary critical all-prime packets do not complete. `WP-362` showed that the canonical scalar Euler completion is positive only as a conjugate product, while its Mangoldt logarithmic derivative imports the divisor. The present result closes the next canonical repair: **retain the entire Eisenstein spectral family and use its Rankin--Selberg coefficient Gram before taking positivity**.

That object really is non-scalar and independently positive where it is defined as a Hilbert Gram, but its exact local Hecke normalization forces the global critical zero (5). Cancelling that zero yields an indefinite kernel, and differentiating logarithmically recovers the desired prime scale only together with the zeta divisor and a universal singular counterterm.

A surviving route must therefore introduce structure not present in the bare Eisenstein coefficient correlation: for example a source-forced finite--archimedean coupling whose archimedean part changes the critical matrix inertia before scalar cancellation, a nonlocal Arthur/Maaß--Selberg operator acting on spectral parameters rather than the coefficient Gram alone, or a genuinely cohomological/intersection sign theorem. Such a construction remains open; it must derive its orientation independently rather than inherit it from (2).