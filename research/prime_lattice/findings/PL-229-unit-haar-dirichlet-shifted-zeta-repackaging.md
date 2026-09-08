# PL-229 — The unit-boundary Haar Dirichlet transform only repackages the shifted reciprocal zeta divisor

## Claim

`PL-228` identifies the canonical all-prime coprimality limit in the high-temperature Bost--Connes sector with normalized Haar measure on

\[
\widehat{\mathbb Z}^{\times}.
\]

For a reduced rational character of order `q`, and in particular for `e(1/q)`, its Fourier coefficient is

\[
\omega_{\mathrm{Haar}}(e(1/q))
=\frac{\mu(q)}{\varphi(q)}.
\]

A natural attempt to recover analytic continuation from this arithmetic boundary state is to collapse those Fourier coefficients by character order and form the Dirichlet transform

\[
D(s)
:=\sum_{q\ge1}\frac{\mu(q)}{\varphi(q)}q^{-s}.
\]

This transform is indeed zero-sensitive, but in an entirely explicit and non-rigid way. For `Re(s)>0`, where the series and Euler product converge absolutely,

\[
\boxed{
D(s)=\prod_p\left(1-\frac{p^{-s}}{p-1}\right)
=\frac{C(s)}{\zeta(s+1)},
}
\]

with

\[
C(s)
:=\prod_p
\frac{1-p^{-s}/(p-1)}{1-p^{-s-1}}.
\]

The correction product `C` converges normally and defines a holomorphic function on `Re(s)>-1`. In the half-plane `Re(s)>-1/2`, its only zeros are the elementary `p=2` zeros

\[
s=\frac{2\pi i k}{\log 2},\qquad k\in\mathbb Z,
\]

on `Re(s)=0`; in particular `C(rho-1) != 0` for every nontrivial zeta zero `rho` with `Re(rho)>1/2`. Therefore the factorization gives a meromorphic continuation of `D` to `Re(s)>-1` and

\[
\boxed{
\mathrm{RH}
\iff
D(s)\text{ is holomorphic on }\Re(s)>-\tfrac12.
}
\]

If RH holds, the nontrivial zeta zeros become boundary poles of this continuation at

\[
s=\rho-1,\qquad \Re(s)=-\frac12,
\]

with the same multiplicities because `C` is nonzero there.

This is **not a new RH mechanism**. The critical boundary appears only after applying an additional one-dimensional norm-weighted Dirichlet transform to the profinite-unit Fourier coefficients, and the exact factorization then restores the ordinary reciprocal zeta function with a harmless Euler correction. The Bost--Connes/Haar state itself still has its intrinsic thermodynamic boundary at `beta=1`; no KMS positivity, unit-boundary geometry, spectral theorem, or new continuation principle forces the zeta divisor onto `Re(s)=1/2`.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. The coefficients are the canonical unit-boundary Fourier data

Let

\[
W=\widehat{\mathbb Z}^{\times}
\]

with normalized Haar probability measure `m_W`. For a reduced character `e(a/q)`, `PL-228` derives

\[
\int_W e(a u/q)\,dm_W(u)
=\frac{c_q(a)}{\varphi(q)}.
\]

When `(a,q)=1`, the classical Ramanujan sum satisfies

\[
c_q(a)=\mu(q),
\]

so the value depends only on the order `q` of the character:

\[
\boxed{
a(q):=\omega_{\mathrm{Haar}}(e(1/q))
=\frac{\mu(q)}{\varphi(q)}.
}
\]

Thus the scalar sequence used below is not an arbitrary observable fitted to zeta. It is the exact Fourier profile of the canonical high-temperature unit-boundary state found in `PL-228`.

However, the passage

\[
a(q)\longmapsto \sum_q a(q)q^{-s}
\]

is already a substantial compression. It forgets the full torsion character and retains only its order together with the rational norm `q`. Any zero-sensitive structure found after this compression must therefore be checked against ordinary Euler-product arithmetic before being interpreted as boundary-state geometry.

## 2. Absolute convergence and the exact Euler product

The arithmetic function

\[
q\longmapsto\frac{\mu(q)}{\varphi(q)}
\]

is multiplicative and supported on square-free integers. Hence its local values are

\[
a(p)=-\frac1{p-1},
\qquad
a(p^k)=0\quad(k\ge2).
\]

For `sigma=Re(s)>0`,

\[
\sum_p \frac{p^{-\sigma}}{p-1}<\infty,
\]

because the summand is `O(p^{-1-sigma})`. Therefore the Dirichlet series is absolutely convergent and Euler multiplication is legitimate in this half-plane:

\[
\boxed{
D(s)=\prod_p\left(1-\frac{p^{-s}}{p-1}\right),
\qquad \Re(s)>0.
}
\]

This domain matters. Nothing below interprets this Euler product itself as convergent in the critical half-plane. Continuation will come from an independently normally convergent correction product together with the classical meromorphic continuation of `zeta`.

## 3. Extraction of the shifted reciprocal zeta factor

Factor each local term as

\[
1-\frac{p^{-s}}{p-1}
=
(1-p^{-s-1})
\frac{1-p^{-s}/(p-1)}{1-p^{-s-1}}.
\]

Thus in `Re(s)>0`,

\[
D(s)=\frac{C(s)}{\zeta(s+1)},
\]

where

\[
C(s)=\prod_p c_p(s),
\qquad
c_p(s)=
\frac{1-p^{-s}/(p-1)}{1-p^{-s-1}}.
\]

The correction from `1` is exact:

\[
c_p(s)-1
=
-\frac{p^{-s-1}}
{(p-1)(1-p^{-s-1})}.
\]

Fix a compact set `K` in `Re(s)>-1`. For all sufficiently large `p`, uniformly on `K`, the denominator is bounded away from zero and

\[
|c_p(s)-1|
\ll_K p^{-\Re(s)-2}.
\]

Since the exponent is strictly larger than `1` on `K`, the sum of these bounds over primes converges. The finitely many remaining local factors are holomorphic away from the lines where `1-p^{-s-1}=0`, all of which lie on `Re(s)=-1`. Consequently

\[
\boxed{
C(s)\text{ is holomorphic on }\Re(s)>-1,
}
\]

and the product is normally convergent there in the usual local-product sense.

Using the classical meromorphic continuation of `zeta`, the identity from `Re(s)>0` therefore supplies the meromorphic continuation

\[
\boxed{
D(s):=\frac{C(s)}{\zeta(s+1)},
\qquad \Re(s)>-1.
}
\]

This is a continuation of the Dirichlet series, not a claim that the original series or Euler product converges in the enlarged half-plane.

## 4. The correction factor cannot hide an off-line zeta zero

A zero of an individual numerator factor satisfies

\[
p^{-s}=p-1.
\]

Taking absolute values gives

\[
\Re(s)
=-\frac{\log(p-1)}{\log p}.
\]

For `p>=3`,

\[
-\frac{\log(p-1)}{\log p}
\le
-\frac{\log2}{\log3}
< -\frac12.
\]

For `p=2`, the zero set is

\[
2^{-s}=1
\iff
s=\frac{2\pi i k}{\log2},
\qquad k\in\mathbb Z.
\]

Normal convergence implies that away from these local zeros the product cannot acquire additional zeros. Hence in the open half-plane `Re(s)>-1/2`, `C` is nonzero except at the displayed `p=2` points on the imaginary axis.

Now let `rho` be a nontrivial zero of `zeta` with `Re(rho)>1/2`. Since zeta has no zero on `Re(rho)=1`,

\[
-\frac12<\Re(\rho-1)<0.
\]

Therefore `rho-1` cannot be a `p=2` zero of `C`, and the `p>=3` zero lines lie farther left. Thus

\[
\boxed{
C(\rho-1)\ne0.
}
\]

Every off-critical zero on the right of the critical line therefore produces a genuine pole of the continued `D` at `s=rho-1`, with no cancellation by the correction factor.

The exceptional point `s=0` causes no difficulty: `zeta(s+1)` has its pole there, so `1/zeta(s+1)` has a zero rather than a pole. The elementary `p=2` zero of `C` at the same point only increases vanishing.

## 5. Exact RH equivalence and why it is only a repackaging

Suppose RH holds. Every nontrivial zeta zero has real part `1/2`, so every pole contributed by `1/zeta(s+1)` lies on the boundary

\[
\Re(s)=-\frac12.
\]

There are no trivial zeta zeros in `Re(s)>-1`, after the shift by `1`, and the pole of zeta at `1` becomes a zero of the reciprocal factor. Since `C` is holomorphic, `D` is therefore holomorphic throughout `Re(s)>-1/2`.

Conversely, if RH fails, the functional equation symmetry of the nontrivial zeta divisor supplies a zero `rho` with

\[
\Re(rho)>\frac12.
\]

Section 4 shows that `C(rho-1)` is nonzero, so the continued `D` has a pole in `Re(s)>-1/2`. Hence

\[
\boxed{
\mathrm{RH}
\iff
D\text{ has no pole in }\Re(s)>-\frac12.
}
\]

Equivalently, because all other factors are holomorphic there,

\[
\boxed{
\mathrm{RH}
\iff
D\text{ is holomorphic in }\Re(s)>-\frac12.
}
\]

The equivalence is exact but does not add leverage. After the elementary factorization, the statement is simply the usual zero-free half-plane for `zeta(s+1)`. The `-1/2` boundary is the ordinary critical line translated by `-1`; it is not generated by a new self-duality of the unit boundary.

In particular, the positivity of Haar measure on `W` does not imply this holomorphy. Positivity only says that the full Fourier kernel on `Q/Z` is positive definite. The transform `D` first collapses that kernel to character order and then weights order `q` by `q^{-s}`. The location of its poles is controlled by the resulting scalar Euler product, not by positivity of the original state.

## 6. Prior-art and matched-control audit

The Fourier coefficient

\[
c_q(a)/\varphi(q)
\]

is classical Ramanujan-sum arithmetic; for `(a,q)=1`, `c_q(a)=mu(q)`. Ramanujan's 1918 work on trigonometric sums is the classical source of this Fourier arithmetic and already connects Ramanujan sums with zeta-valued Dirichlet series. The Bost--Connes interpretation of the profinite unit boundary and its phase transition is also classical, as audited in `PL-228` through Bost--Connes and Neshveyev.

A structural search for the specific `mu(q)/phi(q)` Dirichlet transform did not uncover a source that would justify a novelty claim, and none is made. The factorization above is an immediate multiplicative calculation once the coefficient sequence is written down. Its value for this line is as a **falsification control**: the most obvious attempt to turn the new-looking unit-boundary Möbius profile into a critical-strip analytic object collapses to shifted reciprocal zeta.

The control also survives abstraction of the probabilistic part. Haar measure on a compact unit group can generate positive-definite Fourier coefficients without any RH content. Rational-prime specificity enters only when the exact character order `q`, its totient, and the norm weight `q^{-s}` are imposed. At that point the leading local coefficient

\[
-\frac1{p-1}=-\frac1p+O(p^{-2})
\]

forces the reciprocal-zeta Euler factor, while the `O(p^{-2})` difference is precisely what the normally convergent correction `C` absorbs. Thus the zero-sensitive term is not an emergent spectral feature of the boundary state; it is the familiar prime-norm Euler factor exposed by the scalar transform.

## Boundaries and falsification tests

This finding does **not** claim that every observable of the Bost--Connes unit boundary is zero-blind. It classifies the canonical order-collapsed Dirichlet transform of its Haar Fourier coefficients. A genuinely different construction would evade this no-go only if it retained additional cyclotomic/multi-character information or coupled it to another source-forced arithmetic object in a way that cannot be reduced to a scalar Euler product times a normally convergent nonvanishing correction.

The decisive checks are:

- the original series/Euler product is used only in `Re(s)>0`, where absolute convergence is proved;
- the extension to `Re(s)>-1` comes from the normally convergent `C` product and classical zeta continuation, not from formal continuation of the original product;
- the zero set of `C` is explicitly separated from shifted nontrivial zeta zeros in `Re(s)>-1/2`;
- the RH equivalence is labeled as a repackaging, not as an independent criterion with new coercivity or positivity.

A counterexample to normal convergence of `C` on some compact subset of `Re(s)>-1`, or a zero of `C` at `rho-1` for a nontrivial zeta zero with `Re(rho)>1/2`, would invalidate the claimed clean divisor separation. The local-factor calculation above rules out both in the stated region.

## Consequence for the research line

`PL-228` showed that all-prime coprimality conditioning retains a canonical arithmetic unit boundary but introduces only the classical Bost--Connes threshold `beta=1`. The present result closes the most direct attempt to recover the missing critical line by taking a Mellin/Dirichlet transform of that boundary's Möbius Fourier profile:

\[
\boxed{
\text{unit-boundary Haar Fourier data}
\xrightarrow{\text{order }q\text{ + }q^{-s}}
\frac{\text{harmless }C(s)}{\zeta(s+1)}.
}
\]

The transform is mathematically exact and even yields an RH-equivalent holomorphy statement, but precisely for that reason it supplies no new rigidity: it has simply reintroduced the ordinary zeta divisor after a one-dimensional norm collapse.

A surviving Bost--Connes/prime-lattice route should therefore not treat the Ramanujan/Haar coefficient profile or its scalar Dirichlet transforms as an independent source of critical-line structure. It must exploit genuinely coupled cyclotomic, target-relative, infinite-prime, or noncommutative data and derive a sign/localization statement that does not factor back to zeta by an elementary Euler correction.