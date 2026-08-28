# WP-002 — Prime-Circle uniformization-defect energies have the wrong support for the Weil finite-prime distribution

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the natural route that turns the PC-017 projective/uniformization defect itself into a positive scalar energy at each integer level and then identifies those energies with the finite-prime part of a Weil explicit-formula pairing. This does **not** rule out a signed derivative, divisor transform, global quotient/compression, or other construction that couples several levels and the archimedean sector before positivity appears.

## 1. Exact support obstruction

PC-017 defines the canonical birth-versus-full Fuchsian projective-connection defect

\[
A_n(z)\,dz^2
=
\bigl(Q_n^{\rm birth}(z)-Q_n^{\rm full}(z)\bigr)\,dz^2
\]

and proves the exact primality criterion

\[
\boxed{A_n\equiv0\iff n\text{ is prime}.}
\]

Consider the most direct geometric-positivity proposal suggested by this structure: choose an intrinsic positive Hermitian form on the relevant defect space and set

\[
E_n=\langle A_n,A_n\rangle_n\ge0.
\]

If the form is positive definite on nonzero defects, then

\[
E_p=0\quad(p\text{ prime}),
\qquad
E_n>0\quad(n\text{ composite}).
\]

Even for a merely positive-semidefinite form, the first statement is unavoidable:

\[
\boxed{E_p=0\quad\text{for every prime }p.}
\]

By contrast, in the finite-prime part of the Weil explicit formula the atomic arithmetic coefficient on the logarithmic scale is, up to the global sign convention,

\[
\frac{\Lambda(n)}{\sqrt n},
\]

where

\[
\Lambda(p^k)=\log p,
\qquad
\Lambda(n)=0\quad\text{if }n\text{ is not a prime power}.
\]

Thus the target support contains **every prime** and every higher prime power, while excluding composites having at least two distinct prime factors.

The mismatch is already decisive on two elementary tests:

\[
\begin{array}{c|c|c}
 n & E_n\text{ for a genuine defect norm} & \Lambda(n)/\sqrt n \\
\hline
 p & 0 & (\log p)/\sqrt p>0 \\
 pq,\ p\ne q & >0 & 0
\end{array}
\]

Therefore no positive-definite scalar energy of the raw PC-017 defect can be the finite-prime Weil weight coefficient-for-coefficient. No asymptotic normalization can repair a support contradiction.

Equivalently, writing the finite arithmetic term as a distribution in a logarithmic test variable gives atoms at

\[
\pm\log(p^k),\qquad k\ge1,
\]

with nonzero first-prime atoms at \(\pm\log p\). Any distribution built by placing weights \(E_n\) at \(\pm\log n\) has zero mass at all those \(k=1\) prime atoms. A test function supported in a sufficiently small neighbourhood of one \(\log p\) therefore separates the two distributions exactly.

## 2. Why Liouville / Weil–Petersson positivity does not rescue the route

PC-017 is geometrically close to a classical positive structure: for punctured genus-zero surfaces, Takhtajan–Zograf identify the classical Liouville action as a generating function for accessory parameters and as a Kähler potential for the Weil–Petersson metric. Hence a Liouville Hessian, Weil–Petersson norm, or comparable positive quadratic form on the projective/accessory defect is a mathematically natural candidate rather than an arbitrary inserted kernel.

But this classical positivity changes only the sign property of the quadratic form; it cannot change the exact zero set of its argument. Since the Mathia defect itself vanishes at every prime level, every honest norm-square built from it also vanishes there. The Weil finite-place distribution requires precisely the opposite first-order behaviour: the prime levels carry its basic nonzero atoms.

This distinguishes the obstruction from WP-001. WP-001 showed that the Prime-Circle **prime-ray** kernel has the right prime-power coefficient magnitudes but the wrong local positivity structure after removing the diagonal. WP-002 shows that the separate PC-017 **uniformization-defect energy** has a more basic problem: its arithmetic support is wrong before one even asks about the sign of the Weil block.

## 3. Adversarial escape tests

### Positive-semidefinite instead of positive-definite

Allowing a kernel in the geometric form could force additional composite levels to have zero energy, so the unwanted \(pq\) atoms might in principle be removed. It cannot create the missing prime atoms, because \(A_p=0\) identically. Hence semidefinite weakening does not close the bridge.

### Positive reweighting

Replacing \(E_n\) by \(w_nE_n\) with any finite positive intrinsic weight leaves every prime coefficient equal to zero. The obstruction survives arbitrary rescaling.

### Adding a baseline at zero defect

A nonlinear scalar functional \(F(A_n)\) with the energy normalization \(F(0)=0\) has the same prime obstruction. Taking \(F(0)>0\) abandons the interpretation as a defect energy. Moreover, if the value at the zero defect is geometric and independent of the arithmetic label, all primes receive the same baseline; obtaining the required \((\log p)/\sqrt p\) amplitudes then needs an explicit prime-dependent weight supplied from outside the defect.

### Restricting to prime powers

Filtering the integer levels to \(p^k\) uses the desired arithmetic support as an external selector, and the \(k=1\) level still has zero defect. It therefore does not make the raw defect energy an intrinsic source of the finite Weil term.

### Möbius/divisor transforms or finite differences

Signed inclusion-exclusion across divisor levels can alter support and remains a legitimate direction to investigate because the full/birth construction already contains divisor data. But such a transform is no longer an independently nonnegative scalar norm of \(A_n\): the required cancellations introduce signs before any global positivity theorem has been supplied. This route survives only if the signed transformed object is shown to arise canonically as a boundary, quotient, intersection pairing, Schur complement, or comparable global geometric construction whose positivity follows independently.

### Letting the archimedean term cancel the mismatch

The present result rules out a **place-matched decomposition** in which the defect energy is claimed to supply the finite-prime arithmetic summand. A construction may instead abandon termwise locality and couple the finite and archimedean sectors before comparison. That is exactly the kind of global mechanism left open by WP-001; it is not a rescue of the raw defect-energy identification.

## 4. Prior-art / novelty audit

The ingredients on both sides are classical:

- Weil's explicit formula and its von-Mangoldt prime-power support are standard.
- Takhtajan–Zograf established the Liouville-action/accessory-parameter/Weil–Petersson relation for punctured genus-zero surfaces; the positive Kähler metric is not a Mathia novelty.
- Positive norms of quadratic differentials or tangent/cotangent vectors in Weil–Petersson geometry are standard geometric objects.

Directed searches combining Liouville/Weil–Petersson geometry, prime powers, explicit formulas, and Weil positivity did not locate a prior construction matching the specific PC-017 birth-shell defect to the Riemann finite-prime distribution. No historical-priority claim is made. The durable Mathia content is the negative synthesis: **the exact prime-zero/composite-nonzero support of the intrinsic uniformization defect is incompatible with the prime-power support required by the Weil arithmetic distribution.**

## 5. Consequence for the research line

The canonical projective/uniformization defect remains a genuine Mathia-native geometric discriminator, and its relation to Liouville/Weil–Petersson geometry supplies authentic independent positivity. But the most direct hoped-for bridge is closed:

```text
PC-017 defect A_n
    -> intrinsic positive norm / Liouville-WP energy E_n
    -> finite-prime Weil weights
```

fails already at the support level.

A surviving Prime-Circle route must therefore use more than the scalar energy of \(A_n\). It would have to derive a canonical **signed inter-level operation** and then recover positivity only after a global geometric operation, while also generating the archimedean/pole counterterms intrinsically. In particular, any future claim based on PC-017 should first explain where the missing \(k=1\) prime atoms come from without inserting von Mangoldt weights by hand.

## Internal dependencies

- `research/prime_circle/findings/PC-017-cyclotomic-uniformization-defect.md`
- `research/weil_positivity/findings/WP-001-prime-local-positive-rays-cannot-be-weil-summands.md`
- `research/weil_positivity/SOURCES.md`
