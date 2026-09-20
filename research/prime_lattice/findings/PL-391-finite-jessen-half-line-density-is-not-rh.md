# PL-391 — Finite Bohr–Jessen zero-density singles out `1/2`, but only through coefficient energy and a sparse-zero-blind limit

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

**Parent finding:** `PL-390`.

**Related findings:** `PL-001`, `PL-003`, `PL-005`, `PL-389`, `PL-390`.

**Status:** `A-SEPTEMBER-2026-PREPRINT-PROVES-THAT-THE-JESSEN-ZERO-DENSITY-MEASURES-OF-THE-FINITE-RIEMANN-ZETA-DIRICHLET-POLYNOMIALS-CONCENTRATE-AT-Re(s)=1/2. THIS-IS-A-GENUINE-PRIME-EXPONENT/FINITE-BOHR-TORUS-MECHANISM-THAT-NATURALLY-SINGLES-OUT-THE-HALF-LINE, BUT-IT-DOES-NOT-LOCALIZE-THE-ZEROS-OF-THE-ANALYTICALLY-CONTINUED-RIEMANN-ZETA-FUNCTION. THE-LINE-IS-SELECTED-BY-THE-L2-COEFFICIENT-ENERGY-THRESHOLD, THE-THEOREM-TAKES-HEIGHT-TO-INFINITY-FIRST-AT-EACH-FIXED-TRUNCATION-AND-ONLY-THEN-LETS-THE-TRUNCATION-GROW, AND-WEAK-CONVERGENCE-OF-NORMALIZED-ZERO-DENSITY-CANNOT-EXCLUDE-FINITE-OR-ZERO-DENSITY-OFF-LINE-EXCEPTIONS. THUS-THE-OBVIOUS-JESSEN-REPAIR-LEFT-OPEN-BY-PL-390-IS-PRIOR-ART-AND-IS-NOT-RH-SENSITIVE-WITHOUT-AN-ADDITIONAL-SINGLE-ZERO-SENSITIVE-BRIDGE-TO-THE-ACTUAL-ZETA-DIVISOR`.

## Claim

For the finite zeta Dirichlet polynomial

\[
P_N(s)=\sum_{n\le N}n^{-s},
\tag{PL391-1}
\]

write its finite Bohr lift as

\[
F_N(\sigma,z)
=\sum_{n\le N} n^{-\sigma}z^{v(n)},
\qquad
z\in\mathbb T^{\pi(N)}.
\tag{PL391-2}
\]

The vertical Kronecker orbit is

\[
z_p(t)=e^{-it\log p},
\qquad
F_N(\sigma,z(t))=P_N(\sigma+it).
\tag{PL391-3}
\]

Thus the Jessen function

\[
J_N(\sigma)
=
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}\log|P_N(\sigma+it)|\,dt
\tag{PL391-4}
\]

is an intrinsic finite-prime-torus potential. Jessen--Tornehave theory identifies its distributional second derivative with vertical zero density.

Eric Dubon, *Zero-Density Concentration for Dirichlet Polynomials*, arXiv:2609.17875 (submitted 15 September 2026; revised 17 September 2026), proves for (PL391-1) that

\[
\boxed{
\frac{J_N(\sigma)}{\log N}
\longrightarrow
\left(\frac12-\sigma\right)_+
}
\tag{PL391-5}
\]

locally uniformly on `R`, and hence

\[
\boxed{
\frac1{\log N}J_N''
\xrightarrow{\mathrm w}
\delta_{1/2}.
}
\tag{PL391-6}
\]

This is a real geometric/harmonic mechanism in exponent coordinates that singles out `1/2`. It is nevertheless **not an RH-localization mechanism**. Three independent controls show why:

1. the location `1/2` is already encoded in the quadratic coefficient-energy threshold;
2. the limiting measure records normalized vertical density, so a finite or zero-density population away from `1/2` is invisible;
3. the theorem takes `T -> infinity` first for each finite Dirichlet polynomial and only afterwards `N -> infinity`; it does not identify the zeros of those polynomials with the zeros of the analytic continuation of `zeta` in the critical strip.

The direct Jensen/Jessen escape from the `B^2` pointwise blindness of `PL-390` is therefore substantially prior art, but its first natural zero-density invariant remains too coarse for RH.

## 1. The prime-exponent geometry is exact, not metaphorical

For fixed `N`, only the primes `p<=N` occur. Unique factorization gives the finite exponent vectors

\[
v(n)=(v_p(n))_{p\le N}\in\mathbb N_0^{\pi(N)},
\tag{PL391-7}
\]

and the frequencies satisfy

\[
\log n=\langle v(n),(\log p)_{p\le N}\rangle.
\tag{PL391-8}
\]

The logarithms of distinct primes are rationally independent: an integral relation among them exponentiates to a multiplicative relation among primes and is therefore trivial. Kronecker--Weyl then makes the vertical orbit (PL391-3) equidistributed on the full finite torus.

Dubon's paper makes this representation explicit before introducing the Jessen potential. The singular function `log|F_N|` is handled through the classical logarithmic-integrability/Jessen framework rather than by pretending that ordinary uniform equidistribution applies at its zero set. This distinction matters: the zero-density measure is genuinely attached to the finite Bohr lift, not obtained by formally continuing an Euler product.

The classical theorem behind this step is Børge Jessen and Hans Tornehave, “Mean motions and zeros of almost periodic functions,” *Acta Mathematica* **77** (1945), 137--279, DOI `10.1007/BF02392225`. For ordinary Dirichlet polynomials their Jensen/Jessen formula identifies

\[
\frac{J_N''((a,b))}{2\pi}
=
\lim_{T\to\infty}\frac1{2T}
\#\{\rho=\beta+i\gamma:P_N(\rho)=0,\ a<\beta<b,\ |\gamma|<T\},
\tag{PL391-9}
\]

with multiplicity. Thus (PL391-6) is a spectral/zero-density statement in exactly the harmonic language requested by this research line.

## 2. Why `1/2` appears: the quadratic energy has its kink there

Dubon's abstract criterion uses the quadratic coefficient energy

\[
E_N(\sigma)
=\sum_{n\le N}|a_n|^2n^{-2\sigma}.
\tag{PL391-10}
\]

For zeta partial sums `a_n=1`, so elementary summation gives

\[
E_N(\sigma)
\asymp
\begin{cases}
N^{1-2\sigma}/(1-2\sigma),&\sigma<1/2,\\
\log N,&\sigma=1/2,\\
1,&\sigma>1/2
\end{cases}
\tag{PL391-11}
\]

where in the last line the sequence converges to `zeta(2sigma)`. Consequently

\[
\boxed{
\frac{1}{2\log N}\log E_N(\sigma)
\longrightarrow
\left(\frac12-\sigma\right)_+.
}
\tag{PL391-12}
\]

This is exactly the kink that appears in (PL391-5). The paper's second load-bearing input is a translation-uniform anti-concentration estimate obtained from a large family of isolated prime coordinates; it supplies the lower control needed to promote the energy asymptotic to the Jessen-potential limit. But the **location** of the corner is already selected by (PL391-12).

This is the same square-summability boundary seen in `PL-001`, `PL-021`, and `PL-390`, now upgraded to a nontrivial statement about the normalized zero-density measure of finite Dirichlet polynomials. The upgrade is mathematically real. The interpretation must nevertheless remain narrow: a half-line selected by coefficient energy is not yet a theorem that the Riemann zero divisor is forced onto that line.

A matched-family control in the same preprint makes this explicit. The same concentration line `Re(s)=1/2` is proved for partial sums of every fixed Dirichlet `L`-function and for normalized Hecke eigenvalues; with classical weight-`k` Fourier coefficients the line moves to `Re(s)=k/2` under the corresponding normalization. Thus the corner tracks the natural coefficient-energy normalization across families rather than isolating a zeta-specific off-line-zero rigidity.

## 3. Concentration of mass is compatible with a large off-line support

The most important adversarial control is already emphasized in the preprint itself: **support and normalized mass are different questions**. For a fixed truncation, earlier work on zeta partial sums shows that real parts of zeros can be dense throughout a broad critical interval. Dubon's theorem says that, after taking vertical density and normalizing by the total mass `log N`, asymptotically almost all of that mass lies in every fixed neighborhood of `1/2`.

There is no contradiction. Weak convergence

\[
\nu_N:=\frac{J_N''}{\log N}
\xrightarrow{\mathrm w}\delta_{1/2}
\tag{PL391-13}
\]

allows exceptional zero sets away from `1/2` whose vertical density is `o(log N)`. Their support may remain wide. In particular, a finite number of exceptional zeros contributes zero normalized mass.

That distinction is fatal to a direct RH inference. RH is falsified by **one** persistent zero `rho` with `Re(rho)>1/2`. Any invariant that retains only a normalized limiting zero-density measure can equal `delta_{1/2}` while such a sparse exceptional set survives. The general Research Watch warning that “density one is not all zeros” is therefore instantiated here inside the exact prime-lattice/Jessen geometry.

This does not make (PL391-6) vacuous. It says precisely that it is a bulk localization theorem rather than an all-zero localization theorem.

## 4. The order of limits does not approximate analytic continuation in the strip

The paper states its order of limits explicitly:

\[
\boxed{
\text{for each fixed }N:\ T\to\infty,
\qquad\text{then }N\to\infty.
}
\tag{PL391-14}
\]

No coupled `(N,T)` limit is claimed. This matters for the Riemann problem because the raw Dirichlet partial sums (PL391-1) are not the analytic continuation of `zeta(s)` for `Re(s)<=1`; the ordinary Dirichlet series has abscissa of convergence `1`.

Therefore (PL391-6) does **not** say that the zero divisor of analytic `zeta(s)` is a limit of the zero-density measures of the `P_N` in a topology preserving individual zeros. Hurwitz-type transfer would require locally uniform convergence on an analytic domain, exactly what the raw partial sums do not provide in the critical strip.

This is the key representation audit. The finite Bohr torus is exact for each `P_N`; the Jessen zero measure is exact for each `P_N`; and the normalized `N->infinity` concentration is exact under the preprint's theorem. The missing arrow is from that finite-truncation limit to the pointwise divisor of the analytically continued Riemann zeta function. Inserting that arrow without a new theorem would simply reintroduce the original analytic-continuation problem.

## 5. Prior-art and novelty audit

The finite Bohr lift, Kronecker--Weyl passage, Jessen function, and zero-density interpretation are classical almost-periodic function theory, with Jessen--Tornehave (1945) as the main historical anchor.

The new September 2026 literature input is:

- Eric Dubon, “Zero-Density Concentration for Dirichlet Polynomials,” arXiv:2609.17875, submitted 15 September 2026 and revised 17 September 2026: https://arxiv.org/abs/2609.17875 . Theorem 2.4 gives (PL391-5)--(PL391-6); Theorem 2.2 gives the general isolated-prime criterion; Section 3 develops the finite Bohr/Jessen framework. The source is a current preprint and is therefore treated as non-peer-reviewed literature, not as independently certified new mathematics.
- Børge Jessen, Hans Tornehave, “Mean motions and zeros of almost periodic functions,” *Acta Mathematica* **77** (1945), 137--279, DOI: https://doi.org/10.1007/BF02392225 . This is the classical source for the Jessen convex potential and its vertical zero-frequency measure.

A targeted audit against the current `prime_lattice` corpus found no stored finding containing Dubon's September 2026 theorem. `PL-390` explicitly left a distinguished analytic representative/Jensen object as one possible repair of native `B^2` zero-blindness while warning that Borchsenius--Jessen theory is prior art. The present finding sharpens that boundary with a theorem published after that classical theory: **even an exact finite-prime Bohr/Jessen construction can force normalized zero density onto `1/2` without supplying the single-zero-sensitive passage required by RH.**

No novelty is claimed for Dubon's theorem or for the classical Jessen machinery. The durable Mathia delta is the route classification: the most direct finite-truncation Jensen repair does naturally recover the critical line, but its invariant is a bulk density limit whose half-line is selected by coefficient energy and whose order of limits is not analytic continuation.

## Boundary and falsification tests

This finding does not rule out all Jensen/subharmonic approaches. It rules out treating (PL391-6), or any invariant with the same information content, as an RH localization mechanism by itself.

A proposed repair must pass two tests. First, **single-zero sensitivity**: adding or retaining one persistent off-line zero must change the decisive invariant even after normalization. Second, **analytic-continuation compatibility**: the bridge from finite prime-lattice objects to the actual zeta divisor must use a topology or operator limit that preserves the relevant analytic zeros in `1/2<Re(s)<1`, rather than the order (PL391-14) alone.

A third matched-control test is useful: if the mechanism still works solely from the asymptotic quadratic energy (PL391-12) plus generic prime-coordinate anti-concentration, then it is a bulk central-line phenomenon. Additional arithmetic structure is required before interpreting it as rigidity of the Riemann zero divisor.

## Consequence for the research line

`PL-390` showed that native `B^2` remembers the prime-lattice frequencies through `Re(s)>1/2` but erases isolated pointwise zeros. The obvious analytic repair was to retain a distinguished analytic representative and its Jensen/Jessen zero measure. `PL-391` shows that this repair is both classical and, in a very strong finite-Bohr form, now active current prior art.

The important lesson is not that Jensen geometry is useless. It is that **bulk zero-density is still too coarse**. A future prime-lattice mechanism must retain an analytic object whose divisor is sensitive to every off-line zero, or prove a rigidity theorem turning a bulk Jessen concentration statement into exclusion of all exceptional zeros. Merely obtaining a corner at `1/2` or weak convergence to `delta_{1/2}` is no longer a meaningful RH target.