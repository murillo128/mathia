---
id: WP-295
title: Three-prime support rigidity collapses fixed positive multi-channel relocalization to Möbius
branch: weil_positivity
status: supported
kind: multichannel-positive-relocalization-no-go
claim_strength: exact Hilbert-valued classification theorem for source-native arithmetic convolution with prime-power-supported output, plus fixed-PSD selector corollary
created: 2026-09-14
related: [WP-030, WP-292, WP-293, WP-294]
prior_art:
  - classical identities 1 * Lambda = log and mu * log = Lambda
  - E. D. Cashwell and C. J. Everett, The ring of number-theoretic functions, Pacific J. Math. 9 (1959), 975-985
---

# WP-295 — Three-prime support rigidity collapses fixed positive multi-channel relocalization to Möbius

## Claim

`WP-293` proves that exact **scalar** source-native convolutional recovery of the Mangoldt carrier from the all-integer logarithmic carrier is uniquely Möbius. `WP-294` then shows that exact agreement on the full Weil autocorrelation cone does not weaken that scalar conclusion. Both findings leave an explicit escape: perhaps several arithmetic channels, coupled by a positive form before scalarization, can recover the prime-power support without any individual channel carrying Möbius inversion.

For the most direct fixed positive multi-channel construction, that escape also collapses.

Let `H` be a complex Hilbert space, let

\[
A:\mathbb N\to H
\]

be any Hilbert-valued arithmetic function, and put

\[
L(n)=\log n,
\qquad
F:=A*L,
\qquad
F(N)=\sum_{d\mid N}A(d)\log(N/d).
\tag{1}
\]

Assume only the **support condition**

\[
F(N)=0
\quad\text{whenever }N\text{ is not a prime power}.
\tag{2}
\]

Then there is a single vector `u in H` such that

\[
\boxed{
F(N)=u\,\Lambda(N)
\quad\text{for every }N,
\qquad
A(N)=u\,\mu_{\rm Mob}(N)
\quad\text{for every }N.
}
\tag{3}
\]

Thus vector-valued channels do not buy freedom once a source-native divisor convolution with `log` is required to erase **all mixed-prime support**. The prime-power amplitudes and their directions are forced as well: every surviving prime-power coefficient is the same fixed Hilbert direction times `log p`.

Consequently, if the positive selector is the fixed Hilbert norm

\[
s_A(N):=\frac{\|F(N)\|}{\sqrt N}
\tag{4}
\]

and one asks for the exact finite Weil weight

\[
s_A(N)=\frac{\Lambda(N)}{\sqrt N}
\qquad(N\ge2),
\tag{5}
\]

then (3) gives

\[
A=\mu_{\rm Mob}\,u,
\qquad
\|u\|=1.
\tag{6}
\]

More generally, any finite collection of scalar source-native channels followed by a **fixed positive-semidefinite quadratic coupling** factors through this theorem. After quotienting the nullspace of the coupling, all visible channels collapse to one Möbius direction. Extra positive channels therefore do not avoid the signed inverse found in `WP-293`; they only embed it in a larger Hilbert space.

The rigidity is genuinely a **three-prime consistency effect**. It is false on a free multiplicative monoid with only two prime generators: there are nonlinear prime-power-supported outputs not proportional to `Lambda`. The third independent generator kills those solutions exactly. The same proof therefore works for any free generalized-prime monoid with at least three generators and nonzero logarithmic weights, so this is an arithmetic-generic route closure rather than a `Q`-specific positivity theorem.

**Classification:** `EXACT-DERIVED + HILBERT-VALUED-DIRICHLET-CONVOLUTION + PRIME-POWER-SUPPORT-RIGIDITY + THREE-PRIME-CONSISTENCY + FIXED-PSD-COUPLING + UNIQUE-VISIBLE-MOBIUS-KERNEL + TWO-GENERATOR-MATCHED-CONTROL + GENERALIZED-PRIME-GENERIC + ROUTE-CLOSURE + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. Half-density multi-channel recovery reduces to (1)

The source-native half-density objects used in `WP-292` are

\[
\omega
=
\sum_{m\ge2}\frac{L(m)}{\sqrt m}\,\delta_{\log m},
\qquad
\eta_A
=
\sum_{d\ge1}\frac{A(d)}{\sqrt d}\,\delta_{\log d}.
\tag{7}
\]

Their convolution is Hilbert-valued and locally finite on the logarithmic integer lattice. At `log N`,

\[
(\eta_A*\omega)(\{\log N\})
=
\frac1{\sqrt N}
\sum_{d\mid N}A(d)L(N/d)
=
\frac{F(N)}{\sqrt N}.
\tag{8}
\]

Thus the half-density normalization introduces no hidden channel dependence: exact positive recovery of `Lambda(N)/sqrt(N)` by a pointwise Hilbert norm is precisely (5).

The key question is therefore stronger and simpler than exact-value recovery: **can `A*L` merely have prime-power support without `A` being Möbius?** For scalar exact recovery `WP-293` did not need to answer this. In several channels it is the decisive issue because `||F(N)||=0` outside the prime powers forces vector vanishing, but on a prime power the norm initially fixes only a magnitude, not a direction.

## 2. Formal Dirichlet coordinates expose the support constraint

Use the standard formal-power-series realization of Dirichlet convolution. For every prime `p`, let `x_p` record its exponent, so the arithmetic function `B` corresponds formally to

\[
\mathscr B(x)
=
\sum_{n\ge1}B(n)\prod_p x_p^{v_p(n)}.
\tag{9}
\]

Scalar Dirichlet convolution becomes multiplication of these formal series; Hilbert-valued arithmetic functions form a module over the scalar ring. The classical identity

\[
L=\mathbf 1*\Lambda
\tag{10}
\]

lets us write

\[
F=A*L=(A*\mathbf 1)*\Lambda=:B*\Lambda.
\tag{11}
\]

The formal series of `Lambda` is

\[
\mathscr L_\Lambda(x)
=
\sum_p (\log p)\frac{x_p}{1-x_p}.
\tag{12}
\]

Introduce a separate invertible formal coordinate on every prime axis,

\[
y_p
:=
(\log p)\frac{x_p}{1-x_p},
\qquad
x_p=\frac{y_p}{\log p+y_p}.
\tag{13}
\]

Because `log p != 0`, this is a formal change of variables with invertible linear term. In the `y` coordinates,

\[
\mathscr L_\Lambda(y)=\sum_p y_p.
\tag{14}
\]

Condition (2) says that the formal series of `F` contains no mixed-prime monomial. The coordinate change (13) acts separately on each prime axis, so that property is preserved. Hence there are one-variable Hilbert-valued formal series `psi_p`, each with zero constant term, such that

\[
\boxed{
\mathscr B(y)\left(\sum_p y_p\right)
=
\sum_p\psi_p(y_p).
}
\tag{15}
\]

The entire theorem is now a divisibility statement: a sum of one-variable series is divisible by the linear form `sum y_p` in the full prime-variable ring.

## 3. Three primes force every one-variable term to be linear with the same slope

Choose any three distinct primes `p,q,r` and set all other variables to zero in (15). Writing `x,y,z` for the three surviving `y` variables gives

\[
B_{pqr}(x,y,z)(x+y+z)
=
\psi_p(x)+\psi_q(y)+\psi_r(z).
\tag{16}
\]

The right side is therefore divisible by `x+y+z`. Passing to the quotient by that linear form, equivalently substituting `z=-x-y`, yields the exact identity

\[
\psi_p(x)+\psi_q(y)+\psi_r(-x-y)=0.
\tag{17}
\]

Set `y=0` and then `x=0`:

\[
\psi_p(x)=-\psi_r(-x),
\qquad
\psi_q(y)=-\psi_r(-y).
\tag{18}
\]

Thus `psi_p=psi_q`; because any two primes admit a third distinct prime, all prime-axis series are one common series `psi`. Substituting (18) back into (17) gives the formal Cauchy equation

\[
\psi(x+y)=\psi(x)+\psi(y).
\tag{19}
\]

Write

\[
\psi(t)=\sum_{k\ge1}u_k t^k,
\qquad u_k\in H.
\tag{20}
\]

For every `k>=2`, the coefficient of `x^{k-1}y` in (19) is `k u_k`, hence `u_k=0` over characteristic zero. Therefore

\[
\boxed{\psi(t)=u t}
\tag{21}
\]

for one fixed `u in H`, and (15) becomes

\[
\mathscr F(y)=u\sum_p y_p=u\,\mathscr L_\Lambda(y).
\tag{22}
\]

Returning to arithmetic coefficients,

\[
\boxed{F=u\Lambda.}
\tag{23}
\]

This is the nontrivial strengthening over `WP-293`: **prime-power support alone has already forced the exact Mangoldt amplitude law and a common channel direction.** No norm values at prime powers were used.

## 4. Injectivity then forces the kernel itself to be Möbius

From (1), (23), and the classical identity `mu_Mob * L = Lambda`,

\[
(A-u\mu_{\rm Mob})*L=0.
\tag{24}
\]

Convolution by the nonzero scalar arithmetic function `L` is injective even on Hilbert-valued arithmetic functions. Indeed, if a Hilbert-valued `C` were nonzero with `C*L=0`, choose an index `n_0` with `C(n_0) != 0` and apply the scalar functional

\[
v\mapsto\langle v,C(n_0)\rangle.
\tag{25}
\]

The resulting nonzero scalar arithmetic function would annihilate `L` under Dirichlet convolution, contradicting the no-zero-divisor property proved directly in `WP-293`. Hence (24) implies

\[
\boxed{A=u\mu_{\rm Mob}.}
\tag{26}
\]

Equations (23) and (26) prove (3). If the stronger norm condition (5) holds, then on any prime power `p^k`,

\[
\|u\|\log p
=
\|F(p^k)\|
=
\Lambda(p^k)
=
\log p,
\tag{27}
\]

so `||u||=1`, proving (6).

## 5. Fixed positive-semidefinite channel coupling gives no extra active freedom

Let `a(n) in C^m` collect `m` scalar arithmetic kernels and define the recovered channel vector

\[
c(N):=(a*L)(N)\in\mathbb C^m.
\tag{28}
\]

Let `M >= 0` be a fixed Hermitian positive-semidefinite matrix and use the positive selector

\[
s_M(N)
:=
\frac{\sqrt{c(N)^*Mc(N)}}{\sqrt N}.
\tag{29}
\]

Factor `M=R^*R` and set

\[
A(d):=R\,a(d),
\qquad
F(N)=R\,c(N)=(A*L)(N).
\tag{30}
\]

If `s_M(N)=Lambda(N)/sqrt(N)` for every `N`, the theorem gives a unit vector `u` in the range of `R` such that

\[
R\,a(d)=\mu_{\rm Mob}(d)u
\qquad(d\ge1).
\tag{31}
\]

Therefore every component seen by the positive form is the same Möbius selector embedded in one fixed direction. Components in `ker R=ker M` may be arbitrary, but they are invisible to the positive readout and cannot supply arithmetic information to it. If `M` is positive definite, even this null freedom disappears and the raw channel vector itself is proportional to `mu_Mob` at every integer.

Thus a larger fixed positive channel space does not weaken `WP-293`. It makes the sign of the **readout** automatic, but the exact finite arithmetic selector hidden underneath remains the same signed Möbius inverse.

Combining this with the cone-separation step of `WP-294` gives the corresponding exact-Weil consequence. If the scalarized atomic carrier produced by (29) enters linearly in the finite explicit-formula term and agrees with the canonical finite term on the full Weil autocorrelation cone, with any global remainder finite-place-clean near the nonzero log-integer atoms, distributional separation forces (5) coefficientwise. The multi-channel selector then collapses by (31).

## 6. Matched control: two generators really do admit nonlinear escapes

The third independent prime is load-bearing. On a free multiplicative monoid with only two generators, use the transformed variables `x,y` of (13) and take

\[
B(x,y)=x^2-xy+y^2.
\tag{32}
\]

Then

\[
B(x,y)(x+y)=x^3+y^3.
\tag{33}
\]

The output has support on the two pure generator axes and is not proportional to `x+y`. Since the constant-one arithmetic function is convolution-invertible, this `B` corresponds to a genuine kernel `A=B*mu` in the two-generator Dirichlet ring. Hence support-only uniqueness is false in that matched toy model.

With three generators the same cubic attempt fails exactly:

\[
x^3+y^3+z^3\big|_{z=-x-y}
=-3xy(x+y)
=3xyz,
\tag{34}
\]

which is not identically zero. More generally, the three-variable divisibility argument in Section 3 forces every admissible axis series to satisfy the additive equation (19), leaving only the linear solution.

This control rules out an accidental proof by notation: the rigidity is not a generic property of one- or two-axis convolution. It appears precisely when compatibility across three independent multiplicative generators is imposed.

## 7. Generalized-prime and twisted-weight controls

Nothing in Sections 2--4 uses unique features of the ordinary numerical values of the rational primes beyond having at least three free generators and nonzero axis weights. Replacing `log p` by arbitrary nonzero weights `lambda_p` merely changes (13) to

\[
y_p=\lambda_p\frac{x_p}{1-x_p},
\tag{35}
\]

with the same invertible coordinate change and the same three-variable argument.

Therefore the support-rigidity theorem persists on free Beurling/generalized-prime monoids with at least three generators, as well as under nonzero independent axis reweightings. This is important for interpretation: the theorem closes a **representation class**, but it does not distinguish the arithmetic of `Q` from natural Euler-product clones and cannot itself be the missing global Weil sign mechanism.

## 8. Exact boundary of the no-go

The theorem is intentionally narrower than arbitrary positive geometry.

**Nonlocal coupling across different integers.** Equation (29) couples channels at a fixed `N`. A positive operator that mixes different log-integer sites before scalarization is not reduced to the pointwise Hilbert norm above. Such nonlocality is one of the genuine remaining possibilities.

**Boundary- or site-dependent positive forms.** If `M` depends on `N`, on a boundary state, or on global arithmetic data, the factorization no longer produces one fixed Hilbert-valued convolution kernel. Such dependence must be source-forced rather than chosen to encode prime powers, but it lies outside the theorem.

**Nonlinear upstream selectors.** The Gram-volume mechanism of `WP-030` is not contradicted. Its top exterior degree changes with the number of distinct prime directions, and `sqrt(det G)` is not a fixed Hilbert norm of a vector-valued divisor convolution. The present result explains why replacing that support-sensitive nonlinear rank test by a fixed quadratic channel norm cannot retain an escape from Möbius.

**Indefinite channel forms.** If `M` is indefinite, zero scalar output does not force the channel vector to vanish because isotropic vectors can occur. That evades the proof but also forfeits the independent positivity that motivated the construction.

**Approximate or restricted targets.** The theorem is exact. Approximate suppression of mixed-prime coefficients, finite windows, or restricted test spaces remain separate questions and do not establish the global Weil criterion without an independent extension theorem.

**Archimedean/global completion.** No Gamma term, polar counterterm, or global sign theorem is produced here. The result concerns the finite arithmetic selector only. It therefore cannot be promoted to a global positivity statement.

## 9. Prior-art and novelty audit

The algebraic setting is classical. Dirichlet convolution, `1*Lambda=log`, Möbius inversion, and the formal realization of arithmetic functions by prime-indexed power series are standard; Cashwell--Everett is a classical reference for the ring of number-theoretic functions. `WP-293` already used the integral-domain consequence to prove scalar exact-value uniqueness.

The present mathematical delta is different: the target values at prime powers are **not assumed at all**. Vanishing on mixed-prime integers, together with three-generator consistency, forces every prime-axis output to be one common linear function and therefore forces the full vector-valued output to be `u Lambda`. A bounded literature search over Dirichlet-convolution support, formal Dirichlet series, and prime-power support did not expose a standard named theorem matching this exact support-rigidity statement. No claim of new number theory is needed: for this line it is an exact derived classification of the fixed positive multi-channel escape left open explicitly by `WP-294`.

The result also survives the line's principal matched clone: any free generalized-prime system with at least three generators has the same rigidity. That survival is a warning, not positive evidence for RH. It shows that merely adding fixed positive channel dimension to the source-native logarithmic carrier does not create the missing arithmetic/global structure.

## Consequence for the search

The remaining multi-channel frontier must leave at least one hypothesis used above. In particular, a viable positive mechanism cannot be just

\[
\text{all-integer log carrier}
\xrightarrow{\text{fixed source-native divisor convolutions}}
\text{several channels}
\xrightarrow{\text{fixed PSD norm}}
\text{prime-power weights}.
\tag{36}
\]

That architecture is exactly Möbius inversion in disguise on its visible subspace.

A genuinely different candidate must instead obtain its arithmetic specificity from source-forced nonlocal coupling across log sites, boundary-conditioned/site-dependent geometry, a nonlinear support-sensitive construction such as an exterior/rank mechanism, or another structure that assembles finite and archimedean data before the final positive scalarization. It must then still pass the independent-sign and generalized-prime controls of the line mandate.