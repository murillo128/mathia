# PL-152 — Smooth second-scale Weil coefficients are eventually bounded for all probes iff RH

## Claim

The fixed-depth second-amplitude family isolated in `PL-151` admits an exact converse that was left open there. Fix `R>0`, let `D_(L,R)` be the centered cross-end block from `PL-063`, and for `f,g in C_c^infinity(0,R)` define

`F_(f,g)(L)=exp(L) <g,D_(L,R)f>`.

Then

`boxed: RH <=> F_(f,g)(L) is bounded for all sufficiently large L, for every f,g in C_c^infinity(0,R).`

Under RH this is the uniformly almost-periodic boundedness already proved in `PL-151`. Conversely, if any nontrivial zero lies off the critical line, functional-equation symmetry gives a zero `rho_0=beta_0+i gamma_0` with `beta_0>1/2`. One can choose smooth probes with nonzero coefficient at `rho_0`; the one-sided Laplace transform in the boundary-location variable then has a genuine pole at

`z=2 rho_0-1`,

which lies in `Re(z)>0`. Eventual boundedness would make that Laplace transform holomorphic throughout `Re(z)>0`, a contradiction.

Thus the second-scale boundary dynamics does contain an exact RH-equivalent stability statement: the critical line is precisely the neutral-growth line for every smooth matrix coefficient. But this is a **readout criterion, not an independent rigidity mechanism**. The pole locations come from the already-continued completed explicit formula before the boundedness test is applied. The same argument works for any comparable explicit-formula system after centering at its symmetry line, and same-zero Grosswald--Schnitzer deformations inherit the same zero-side pole test while changing the prime generators.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + RH-EQUIVALENT-READOUT + NEGATIVE/OBSTRUCTION`. The exact boundary expansion is inherited from `PL-063`; `PL-151` supplies the RH almost-periodic direction. The converse below is an elementary Laplace-transform pole argument. No novelty is claimed for the general principle that square-root-normalized explicit-formula errors detect off-line zeros.

## Exact second-scale expansion

`PL-063` gives, with `X=exp(2L)`,

`<g,D_(L,R)f>`

` = - sum_rho X^(rho-1) A_f(rho-1/2) conjugate(A_g(conjugate(rho)-1/2))`

`   + O_R(X^(-3)) ||f||_2 ||g||_2`,

where

`A_f(w)=integral_0^R f(a) exp(-w a) da`

and the sum runs over nontrivial zeta zeros with multiplicity. Multiplying by `exp(L)=X^(1/2)` gives

`F_(f,g)(L)`

` = - sum_rho c_rho(f,g) exp((2 rho-1)L) + r_(f,g)(L)`,

with

`c_rho(f,g)=A_f(rho-1/2) conjugate(A_g(conjugate(rho)-1/2))`

and

`r_(f,g)(L)=O_R(exp(-5L)) ||f||_2 ||g||_2`.

For compactly supported smooth probes, repeated integration by parts gives, uniformly for `-1/2<=Re(w)<=1/2`,

`|A_f(w)| <= C_(f,m) (1+|Im(w)|)^(-m)`

for every `m`. Together with the Riemann--von Mangoldt local zero count, this makes the coefficient sequence rapidly summable in the zero ordinate. In particular, the zero series converges normally on every bounded `L`-interval, and after an additional Laplace weight it may be integrated termwise in any half-plane `Re(z)>1`.

This identity is not obtained by continuing an Euler product. It is the completed von-Mangoldt/Weil explicit formula already established in `PL-063`, tested against compact boundary correlations.

## RH gives bounded uniformly almost-periodic coefficients

If RH holds, every zero is `rho=1/2+i gamma`, so

`exp((2 rho-1)L)=exp(2 i gamma L)`.

The rapid summability above therefore gives an absolutely and uniformly convergent Fourier series

`F_(f,g)(L) = - sum_gamma c_gamma(f,g) exp(2 i gamma L) + O_R(exp(-5L))`.

The leading term is uniformly Bohr almost periodic and hence bounded. The exponentially decaying remainder is bounded as well. This proves the forward implication and recovers the boundedness part of `PL-151`.

The ordinary Bohr autocorrelation also exists. After grouping equal ordinates and writing the grouped Fourier coefficient as `b_gamma(f,g)`,

`M_L [ Z_(f,g)(L+h) conjugate(Z_(f,g)(L)) ]`

` = sum_gamma |b_gamma(f,g)|^2 exp(2 i gamma h)`,

where `Z_(f,g)` denotes the almost-periodic leading term and `M_L` its Bohr mean. Thus the correlation/diffraction spectrum is pure point and supported on the zero ordinates. This is standard almost-periodic harmonic analysis, not a new spectral localization mechanism.

## An off-line zero forces an unbounded smooth coefficient

Assume RH is false. The functional equation and conjugation symmetry of the completed zeta divisor then give at least one zero

`rho_0=beta_0+i gamma_0`,  `beta_0>1/2`.

The evaluation functional

`f -> A_f(rho_0-1/2)`

is not identically zero on `C_c^infinity(0,R)`: for example, a nonnegative bump concentrated sufficiently close to any interior point has nonzero transform at that fixed complex argument after a sufficiently small localization. Choose `f` and `g` so that

`c_(rho_0)(f,g) != 0`.

Suppose, toward a contradiction, that this `F_(f,g)` is bounded on `[L_0,infinity)` for some `L_0`. Its tail Laplace transform

`H(z)=integral_(L_0)^infinity exp(-zL) F_(f,g)(L) dL`

is then holomorphic on `Re(z)>0`.

For `Re(z)>1`, termwise integration of the exact zero expansion is justified by the rapid coefficient decay and `0<Re(rho)<1`. It gives

`H(z)`

` = - sum_rho c_rho(f,g) exp(-(z-(2rho-1))L_0)/(z-(2rho-1)) + R(z)`,

where

`R(z)=integral_(L_0)^infinity exp(-zL) r_(f,g)(L) dL`

extends holomorphically at least to `Re(z)>-5`.

The zero sum on the right defines a meromorphic function of `z`, locally normally convergent away from the discrete set

`{2rho-1}`.

At `z_0=2rho_0-1`, its residue is the nonzero grouped coefficient contributed by `rho_0` and its multiplicity. There is no cancellation with a distinct zero because the map `rho -> 2rho-1` is injective; multiplicity only repeats the same coefficient with the same sign. Hence the right-hand side has a genuine pole at `z_0`, and

`Re(z_0)=2beta_0-1>0`.

But on `Re(z)>1` this meromorphic function equals the holomorphic transform `H(z)-R(z)`. By analytic continuation they must agree throughout the connected half-plane `Re(z)>0` away from their poles. The pole at `z_0` would therefore have to be removable, contradicting its nonzero residue. Thus the chosen smooth matrix coefficient cannot be eventually bounded.

We have proved

`[all smooth second-scale coefficients eventually bounded] => [no zero with Re(rho)>1/2]`.

Functional-equation symmetry then excludes zeros with `Re(rho)<1/2` as well, yielding RH.

## What the criterion does and does not add

The implication is mathematically exact, but it does not evade the main obstruction identified throughout the Weil-boundary branch. The zero divisor is already present in the starting identity. The boundary variable `L` simply converts each shifted zero

`rho-1/2`

into the exponential mode

`exp(2(rho-1/2)L)`.

The critical line is therefore the neutral-stability axis because `Re(2rho-1)=0` exactly there. Proving boundedness from the zero expansion is equivalent to proving the desired zero location; no independent positivity, self-adjointness, or prime-lattice rigidity has appeared.

The autocorrelation/hull escape left explicit in `PL-151` is correspondingly classicalized. Under RH the translation hull is compact because the smooth coefficients are uniformly almost periodic, and its pure-point spectrum reads the ordinates. If RH fails, some smooth coefficient cannot even remain bounded, so that compact-hull property fails. This gives a clean dynamical reformulation but not a mechanism that forces compactness from the rational-prime geometry.

## Prior-art and novelty audit

The underlying harmonic picture is classical. A. P. Guinand's explicit-formula harmonic analysis treats the prime-power and zero sides as Fourier-dual weighted sequences, and the later limiting-distribution literature of Akbary--Ng--Shahabi places square-root-normalized prime-number-theorem errors in almost-periodic frameworks under RH. `PL-151` records those sources and the precise bibliography.

A targeted search for the exact statement above in the specific `PL-063` fixed-depth boundary-Hankel realization did not locate it. That search absence is not novelty evidence. The safe interpretation is `EXACT-DERIVED`: once the exact zero expansion is available, the converse is a standard Laplace-transform pole argument.

More broadly, classical explicit-formula bounds already give many RH-equivalent growth criteria. The present result should therefore not be advertised as a new RH criterion. Its value to this line is narrower: it closes the logical gap in `PL-151` and identifies exactly what the surviving second-scale dynamical boundedness would mean.

## Matched controls and falsification

The result fails the rational-prime-specificity test in the expected way.

First, the proof only needs an explicit formula whose completed divisor is symmetric about a line `Re(s)=sigma_0`, together with smooth test transforms. After normalization by that line, zeros become modes `exp((rho-sigma_0)t)`, and the same Laplace-pole argument turns boundedness of all smoothed coefficients into a zero-on-the-symmetry-line condition. This is generic explicit-formula technology rather than a property of the free exponent cone.

Second, the Grosswald--Schnitzer controls already audited in `PL-125` preserve the nontrivial zeta zero divisor while deforming the prime generators. Any zero-side second-scale criterion depending only on the exponents `2rho-1` therefore gives the same verdict for those deformed systems. It cannot identify the exact rational primes or recover mixed-support exponent geometry.

Third, the prime-lattice contribution to `D_(L,R)` remains supported on prime-power axis points `k e_p`. Mixed-support exponent vectors still play no role in the proof. The identity `log(p^k)=<k e_p,(log q)_q>` explains the event locations, but the RH equivalence is supplied by completion and the zero divisor, not by a new interaction among lattice directions.

A falsification of the exact criterion would require failure of the `PL-063` zero expansion, failure of rapid decay of compact smooth Laplace transforms, cancellation of a genuine pole with nonzero residue at an identical shifted zero, or failure of the completed zeta functional-equation symmetry. None is compatible with the inherited exact formula and classical complex analysis.

## Consequence for the research line

Do not pursue the fixed-depth `exp(L)` second-amplitude family merely by replacing pointwise convergence with **boundedness, compact translation hulls, or ordinary Bohr spectral analysis**. Those properties can encode RH exactly, but only because the explicit formula has already supplied the zeros as exponential modes. Under RH the hull is a classical almost-periodic zero readout; off RH a right-half-plane Laplace pole destroys boundedness.

A genuinely new mesoscopic mechanism must therefore prove a stability/positivity property from prime-side or geometric structure *before* the zero divisor is inserted, or must use a moving geometry/coupling whose invariant distinguishes rational primes from same-zero or generalized-prime controls. The exact boundedness equivalence is useful as a diagnostic target, not as an explanation of why the critical line should hold.