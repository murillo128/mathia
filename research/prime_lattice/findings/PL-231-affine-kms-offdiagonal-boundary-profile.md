# PL-231 — Low-temperature affine KMS off-diagonal data are one replicated boundary Fourier profile, not cross-prime arithmetic coupling

## Claim

The off-diagonal low-temperature sector left open by `PL-230` can be classified exactly for the canonical affine-semigroup KMS system. In the Toeplitz algebra

\[
\mathcal T(\mathbb N\rtimes\mathbb N^\times)=C^*(s,v_a:a\ge1)
\]

with Laca--Raeburn dynamics

\[
\sigma_t(s)=s,\qquad \sigma_t(v_a)=a^{it}v_a,
\]

every finite-temperature `KMS_beta` state has one of two behaviours.

For `1 <= beta <= 2`, the KMS state is unique and every off-diagonal spanning monomial vanishes:

\[
\psi_\beta(s^m v_a v_b^*s^{*n})=0
\]

unless `a=b` and `m=n`. Thus the shifted Riemann critical temperature `beta=3/2` lies in a regime where the canonical off-diagonal KMS readout is identically zero.

For `beta>2`, KMS states are parametrized by probability measures `nu` on the circle. Define the Fourier moments with the convention

\[
\widehat\nu(r):=\int_{\mathbb T}z^r\,d\nu(z).
\]

Then for every `a>=1`, `n>=0`, and positive integer `r`,

\[
\boxed{
\psi_{\beta,\nu}
\!\left(s^{n+ar}v_a v_a^*s^{*n}\right)
=a^{-\beta} C_{\beta,\nu}(r),
}
\]

where

\[
\boxed{
C_{\beta,\nu}(r)
=\frac{1}{\zeta(\beta-1)}
\sum_{d\mid r}d^{1-\beta}\widehat\nu(r/d).
}
\]

The normalized profile is independent of both the multiplicative channel `a` and the base point `n`. Moreover,

\[
\psi_{\beta,\nu}(s^m v_a v_b^*s^{*n})=0\qquad(a\ne b).
\]

Hence there is no nonzero KMS matrix coefficient directly coupling distinct multiplicative channels. All surviving additive off-diagonal information is a **single scalar boundary Fourier profile replicated identically in every channel**, with the only `a`-dependence being the Boltzmann factor `a^{-beta}`.

The divisor smoothing above is invertible. If `mu_ar` denotes the ordinary arithmetic Möbius function, then

\[
\boxed{
\widehat\nu(r)
=\zeta(\beta-1)
\sum_{d\mid r}\mu_{\rm ar}(d)d^{1-\beta}
C_{\beta,\nu}(r/d).
}
\]

Thus the full normalized off-diagonal profile contains exactly the same information as the boundary measure's Fourier moments; it is not an additional source-forced arithmetic invariant hidden in the KMS correlations.

In particular,

\[
C_{\beta,\nu}(1)
=\frac{\widehat\nu(1)}{\zeta(\beta-1)}.
\]

As `nu` ranges over probability measures on `T`, `\widehat\nu(1)` ranges over the closed unit disk. Even the first normalized off-diagonal coefficient can therefore have arbitrary phase and any modulus from `0` to `1/zeta(beta-1)`. For extremal KMS states it has arbitrary phase on the boundary circle.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The negative is deliberately restricted to the canonical affine-semigroup dynamics and its ordinary KMS state simplex/spanning-monomial correlations. It does not exclude an additional target-relative observable, completed trace formula, non-KMS state selection principle, unbounded affiliated construction, or independently justified arithmetic condition that selects a special boundary state and then proves a new coercive property.

## 1. The published KMS formula already isolates the off-diagonal freedom

Laca and Raeburn compute all KMS states of the natural dynamics on `T(N rt N^x)`. Their Theorem 7.1 gives:

- no KMS states for `beta<1`;
- one unique KMS state for `1<=beta<=2`, with only the diagonal coefficients `a^{-beta}` surviving;
- for `beta>2`, a simplex affinely isomorphic to the probability measures on the unit circle.

For the extremal state indexed by `z in T`, their exact formula is

\[
\psi_{\beta,z}(s^m v_a v_b^*s^{*n})
=
\begin{cases}
0,&a\ne b\text{ or }m\not\equiv n\pmod a,\\[4pt]
\displaystyle
\frac{1}{a\zeta(\beta-1)}
\sum_{\{x:\,a\mid x\mid(m-n)\}}
 x^{1-\beta}z^{(m-n)/x},
& a=b,\ m\equiv n\pmod a.
\end{cases}
\]

The theorem is stronger than merely saying that low-temperature equilibrium states are nonunique: it supplies every matrix coefficient on a spanning set. Since the KMS simplex is the probability-measure simplex, the formula for a general `nu` is obtained by integrating the extremal formula against `nu`.

This is exactly the sector that `PL-230` left open after proving that residue projections are KMS-rigid and purely positive. The low-temperature freedom is real, but the published formula lets us determine whether it carries a new relation among prime channels rather than only state-boundary data.

## 2. Reduction to one universal normalized profile

Take `m=n+ar` with `r>=1`. The divisibility condition is automatic. In the Laca--Raeburn sum put `x=ad`. Then `x` runs over the positive divisors of `ar` that are multiples of `a` precisely when `d|r`, and

\[
\begin{aligned}
\psi_{\beta,z}(s^{n+ar}v_av_a^*s^{*n})
&=\frac{1}{a\zeta(\beta-1)}
  \sum_{d\mid r}(ad)^{1-\beta}z^{r/d}\\
&=a^{-\beta}
  \frac{1}{\zeta(\beta-1)}
  \sum_{d\mid r}d^{1-\beta}z^{r/d}.
\end{aligned}
\]

Integrating over `z` replaces `z^k` by `\widehat\nu(k)` and gives the claimed `C_(beta,nu)(r)`. No prime-specific datum remains in the normalized expression. For primes `p,q`, for example,

\[
\boxed{
p^\beta\psi_{\beta,\nu}(s^{n+pr}v_pv_p^*s^{*n})
=q^\beta\psi_{\beta,\nu}(s^{n+qr}v_qv_q^*s^{*n})
=C_{\beta,\nu}(r).
}
\]

So the KMS relation does impose a joint relation across all multiplicative channels, but it is the opposite of the hoped-for arithmetic coupling: after the forced energy normalization, all channels are copies of the same one-dimensional additive profile.

The separate published condition `a != b => 0` makes the collapse sharper. There is no surviving coefficient of the basic form `v_a v_b^*` with distinct multiplicative energies from which a relative prime phase or signed `p-q` interaction could be extracted. Energy invariance kills those cross-channel matrix coefficients before any zero-sensitive interpretation is possible.

## 3. Möbius inversion shows that the profile is exactly boundary-state data

Let

\[
h_\beta(d):=d^{1-\beta}.
\]

For positive integers `r`, the normalized profile is the Dirichlet convolution

\[
\zeta(\beta-1)C_{\beta,\nu}=h_\beta*\widehat\nu.
\]

Because `h_beta` is completely multiplicative, its Dirichlet inverse is

\[
h_\beta^{-1}(d)=\mu_{\rm ar}(d)d^{1-\beta}.
\]

Convolving once more therefore gives

\[
\widehat\nu(r)
=\zeta(\beta-1)
\sum_{d\mid r}\mu_{\rm ar}(d)d^{1-\beta}C_{\beta,\nu}(r/d).
\]

This is an exact information-equivalence, not merely a heuristic similarity. The divisor weights supplied by the affine semigroup apply a fixed invertible triangular transform to the Fourier moments of the boundary measure. Consequently a proposed low-temperature invariant obtained solely from this normalized off-diagonal sequence has not generated new arithmetic information: one can recover the arbitrary circle-state moments from it and vice versa.

The first coefficient makes the flexibility especially transparent. Since

\[
C_{\beta,\nu}(1)=\widehat\nu(1)/\zeta(\beta-1),
\]

and the first moment of a probability measure on the circle can be any point of the closed unit disk, its phase is not source-selected. Point masses `delta_z` give every phase with maximal modulus; mixtures with Haar measure fill the interior. Positivity of `nu` constrains the whole moment sequence by positive definiteness, so the higher moments are not independently programmable, but that constraint is generic circle harmonic analysis rather than a rational-prime relation.

## 4. The critical-temperature regime is even more rigidly negative

`PL-199` already observed that the ordinary partition function is `zeta(beta-1)`, with trace-class boundary and phase transition at `beta=2`, while the shifted Riemann critical line corresponds to `Re(beta)=3/2`.

The present calculation closes a possible objection to that pole-based negative. One might hope that although the scalar partition function is blind to the critical line, **off-diagonal equilibrium correlations** inside the unique-KMS phase retain a more subtle arithmetic signature. Laca--Raeburn's theorem rules this out for the canonical spanning coefficients:

\[
1\le\beta\le2
\quad\Longrightarrow\quad
\psi_\beta(s^m v_a v_b^*s^{*n})=0
\]

whenever `(a,m)!=(b,n)`. In particular, at the real shifted-critical value `beta=3/2`, the entire ordinary off-diagonal monomial sector vanishes. There is no hidden circle boundary phase there to analyze.

The symmetry-breaking freedom appears only after crossing the pole-driven transition `beta=2`. Once it appears, Section 2 shows that it is replicated boundary Fourier data, not a prime-specific interaction. Thus neither side of the phase transition supplies the missing RH sign mechanism: below and at `2` the off-diagonal profile is zero; above `2` it is nonzero but boundary-state dependent and prime-blind after energy normalization.

## 5. Prior-art and novelty audit

The main primary source is:

**Marcelo Laca, Iain Raeburn**, “Phase transition on the Toeplitz algebra of the affine semigroup over the natural numbers,” *Advances in Mathematics* **225**(2) (2010), 643--688. DOI `10.1016/j.aim.2010.03.007`, arXiv `0907.3760`.

Their Theorem 7.1 is the direct literature basis for the complete KMS phase diagram and the matrix-coefficient formula used above. The paper also states that a KMS state is determined by its behaviour on the `C*`-subalgebra generated by the additive isometry and constructs the low-temperature states from probability measures on the circle. No novelty is claimed for that classification, the phase transition, or the circle parametrization.

A complementary structural explanation is provided by:

**Sergey Neshveyev**, “KMS states on the `C*`-algebras of non-principal groupoids,” *Journal of Operator Theory* **70**(2) (2013), 513--530. DOI `10.7900/jot.2011sep20.1915`, arXiv `1106.5912`.

Neshveyev's general groupoid theorem describes KMS states through traces on isotropy-group `C*`-algebras; in the relevant affine-semigroup phenomenon the isotropy is `Z`, explaining why probability measures on its dual circle occur as the state parameter. This supports the interpretation that the low-temperature phase freedom is boundary/isotropy data rather than an unrecognized prime-exponent invariant.

The only derived content being stored here is the research-line audit: substitute `m-n=ar`, factor out `a^{-beta}`, identify the resulting universal divisor-smoothed Fourier profile, invert that smoothing by ordinary Möbius convolution, and compare this exact structure with the post-`PL-230` requirement for a source-forced cross-prime relation. These deductions are elementary consequences of the published formula. A targeted search around affine-semigroup KMS off-diagonal coefficients, circle moments, isotropy, and prime-channel correlations found the classification itself and its groupoid explanation, not an RH localization theorem arising from these coefficients. No novelty inference is drawn from the absence of such a theorem.

## 6. Boundary conditions and decisive tests

This finding does **not** say that every non-diagonal observable in every completion of the affine algebra is arithmetically trivial. It classifies the ordinary KMS state values on the standard spanning monomials, and hence all bounded expectations determined from them by linearity and norm continuity, but an additional construction can still introduce a genuinely new ingredient.

In particular, the negative does not cover:

- a canonical theorem that selects one boundary measure `nu` for an arithmetic reason external to the KMS simplex and proves a non-generic property of it;
- a target-relative compression such as a Nyman/model-space coupling whose sign is not a function only of the KMS boundary moments;
- an unbounded affiliated observable, renormalized determinant, or completed trace formula requiring data outside ordinary bounded KMS expectations;
- a different dynamics whose energy balance permits nonzero `a!=b` coefficients and whose choice is independently forced by the prime-lattice object rather than tuned to a desired answer.

The finding should be withdrawn or narrowed if any of the following occurs:

1. Theorem 7.1 of Laca--Raeburn does not give the stated coefficient formula for `beta>2` or the stated diagonal-only formula for `1<=beta<=2`;
2. the substitution `m-n=ar`, `x=ad` does not reduce the coefficient to `a^{-beta}C_(beta,nu)(r)`;
3. the Dirichlet inverse of `d^(1-beta)` is not `mu_ar(d)d^(1-beta)`;
4. the circle-measure parametrization contains an additional source constraint that prevents the first Fourier moment from ranging over the closed unit disk;
5. an independently established arithmetic selection principle inside this same canonical KMS system forces a distinguished `nu` and derives a zero-sensitive coercive/sign relation not equivalent to specifying its Fourier moments.

The first four tests are exact or directly published. The fifth marks the remaining mechanism boundary rather than a claim of impossibility.

## Consequence for the research line

`PL-230` showed that the affine KMS **residue diagonal** is too rigid in the wrong direction: it is positive, local, multiplicative, and fixed by elementary KMS scaling. The natural next move was to leave that diagonal and use the low-temperature off-diagonal state freedom.

`PL-231` shows that the canonical version of this move does not create the missing relational arithmetic either. Cross-multiplicative channels vanish, and each surviving same-channel additive correlation is merely a Boltzmann-scaled copy of one boundary Fourier profile. That profile is itself an invertible repackaging of the freely chosen circle measure.

Thus the surviving affine route must add a load-bearing relation **before** ordinary KMS evaluation scalarizes it to circle moments. A useful next candidate must couple distinct prime/multiplicative channels in a way not killed by the log-energy balance, or tie the affine algebra to an independently fixed target/completed positivity structure. Merely choosing a non-Haar low-temperature KMS state, inspecting more of its additive Fourier moments, or interpreting the divisor smoothing of those moments as a new prime-lattice spectrum does not pass the source-forcing or matched-control gate.