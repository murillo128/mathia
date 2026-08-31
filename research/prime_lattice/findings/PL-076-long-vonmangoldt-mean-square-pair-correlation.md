# PL-076 — Smoothed long von Mangoldt mean squares already route the global lag channel to zero pair correlation

## Claim

The global/growing-lag escape left open by `PL-075` is already present, in a closely matched and rigorously analyzed form, in classical long-Dirichlet-polynomial theory. For the half-weight logarithmic-derivative polynomial

```text
P_X(t)
 = sum_(n<=X) Lambda(n) n^(-1/2-it)
   (1-log n/log X),
```

Winston Heap proves, conditional on RH and for `X<=T^4`, an asymptotic mean-square formula whose non-diagonal term is an integral of Montgomery's zero pair-correlation function `F(u,T)`. In particular, for `T<=X<=T^4`,

```text
integral_T^(2T) |P_X(t)|^2 dt
  asymp T (log T)^2.
```

Thus, once the fixed-lag `Lambda` channel of `PL-075` is promoted to a completed/smoothed long aggregate, the first established zero-sensitive global statistic is not a new spectral invariant of the exponent lattice: it is the classical prime/zero pair-correlation channel.

There is a useful coefficient-level contrast in the same theorem package. For the long prime polynomial associated to `log zeta`,

```text
L_X(t)
 = sum_(n<=X)
   Lambda(n)V_X(log n)
   / (n^(1/2+it) log n),
```

with Heap's admissible Fourier-concentrated weights, RH gives even very long moments whose leading terms are purely diagonal. Heap explicitly notes that, if these moments are instead expanded through shifted `Lambda` correlations, the off-diagonal errors must cancel after averaging over the shift. The appearance or disappearance of a global zero-correlation term therefore depends on the distinguished arithmetic observable and its smoothing/completion, not on the bare `{log n}` character geometry or the exponent `1/2` alone.

**Evidence/status:** `LITERATURE+DERIVED + PRIOR-ART/REDIRECT` for the route

```text
PL-075 half-weight von Mangoldt channel
+ aggregate growing additive lags / long positive-cone polynomial
    -> new prime-lattice spectral statistic relevant to RH.
```

The redirect is deliberately not a no-go for every sharp-band or target-relative observable. Heap's theorem uses a triangular logarithmic cutoff and assumes RH; it does not prove that the exact macroscopic sharp band of `PL-075` has the same formula, and it cannot be used circularly as an unconditional proof of RH. It does show that the most natural completion-sensitive global version of the surviving `Lambda` branch is already a mature zero-pair-correlation construction.

## Exact classical bridge

Heap studies the triangularly smoothed logarithmic-derivative polynomial

```text
P_X(t)
 = sum_(n<=X)
   Lambda(n) n^(-1/2-it)
   (1-log n/log X).
```

Let Montgomery's pair-correlation statistic be

```text
F(u,T)
 = (2 pi)/(T log T)
   sum_(0<gamma_1,gamma_2<=T)
     T^(-iu(gamma_1-gamma_2))
     4/(4+(gamma_1-gamma_2)^2),
```

where, under RH, the nontrivial zeros are written `1/2+i gamma`. Heap's Theorem 2 states, for `X<=T^4`,

```text
integral_T^(2T) |P_X(t)|^2 dt
 = T sum_(p<=min(T,X))
       (log p)^2/p
       (1-log p/log X)^2

   + [ 1_(X>=t) t(log t)^2
       integral_1^(log X/log t)
         F(u,t)
         (1-u log t/log X)^2 du
     ]_(t=T)^(2T)

   + o(T(log T)^2).
```

The first term is the diagonal prime contribution. The second is a genuinely global off-diagonal term, but it is already expressed through the standard pair correlation of Riemann zeros. Heap then uses known RH bounds on unit-interval averages of `F` to obtain

```text
integral_T^(2T) |P_X(t)|^2 dt
  asymp T(log T)^2
```

uniformly for `T<=X<=T^4`.

This is exactly the kind of collective-lag phenomenon that `PL-075` intentionally did not classify. `PL-075` identifies, for every fixed additive shift `h`, the critical-band `Lambda` contribution with the Hardy--Littlewood correlation

```text
sum_(n<=x) Lambda(n)Lambda(n+h).
```

Heap's formula shows what happens in a canonical smoothed global aggregate: the collective off-diagonal contribution can instead be expressed, under RH, on the **zero side** through `F(u,T)`. The two descriptions belong to the classical prime/zero-correlation dictionary rather than to a new exponent-lattice spectral mechanism.

## Why this is not merely another fixed-lag restatement

For the finite-time character Gram kernel used in `PL-072`--`PL-075`, expanding a quadratic mean gives additive shifts because nearby multiplicative characters satisfy

```text
log((n+h)/n)
```

as their frequency gap. At the `N~T` resolution scale, fixed `h` survives and `PL-075` routes its arithmetic coefficient to Hardy--Littlewood.

The unresolved possibility was that **many growing lags taken together** might form a new lattice invariant even though each fixed lag is classical. Heap's theorem is relevant precisely at that level: the long polynomial is not analyzed shift by shift. Under RH, contour/explicit-formula methods reorganize the entire smoothed mean square so that its non-diagonal content is the zero-pair statistic `F`.

Hence the global aggregation does add information compared with any one fixed lag, but the information carrier is known:

```text
fixed Lambda lag
    -> Hardy--Littlewood prime-pair correlation;

smoothed long Lambda aggregate under RH
    -> Montgomery zero pair correlation.
```

This is a material prior-art redirect. A proposed `prime_lattice` construction that merely rediscovers this aggregate under a different Gram/operator notation has not produced a new mechanism.

## The `Lambda/log n` control shows that half weight and long length are insufficient

Heap's Theorem 1 gives a particularly strong falsification control. For admissible weights `V_X`, he considers

```text
L_X(t)
 = sum_(n<=X)
   Lambda(n)V_X(log n)
   / (n^(1/2+it) log n),
```

which is the prime polynomial associated to `log zeta` rather than `zeta'/zeta`.

Conditional on RH, for `X<=T^(2m)` and integral moments in the theorem's range, the leading terms are purely diagonal. For example the `2k`-th moment has leading term

```text
k! T
  ( sum_(p<=T^(theta/k)) V_X(log p)^2/p )^k,
```

with a controlled lower-order error. Heap emphasizes that, if one tried to obtain the same result through Hardy--Littlewood-type shifted correlations, the off-diagonal errors would have to cancel after averaging over the shifts.

This gives a matched control against overinterpreting the `PL-075` half-weight balance:

```text
same critical radial factor n^(-1/2)
+ same multiplicative frequencies log n
+ very long prime-supported polynomial

but

Lambda/log n observable
    -> diagonal leading law;

Lambda observable with logarithmic-derivative smoothing
    -> zero-pair-correlation term.
```

The difference is not supplied by the exponent lattice itself. It is supplied by the arithmetic observable and by the analytic machinery that connects that observable to `log zeta` or `zeta'/zeta`.

## Analytic-continuation boundary

The exact finite Dirichlet polynomials make sense without RH. The zero-side formula used here does not arise by formally continuing the Euler product.

Heap's argument assumes RH and passes through contour representations of `log zeta` / `zeta'/zeta`, shifted moments, and correlations of

```text
S(t)=(1/pi) Im log zeta(1/2+it).
```

For the logarithmic-derivative polynomial he obtains, under RH, an integral representation against `S(t+y)` and then applies Goldston-type formulas for shifted second moments of `S`. The pair-correlation term therefore enters through established analytic continuation / explicit-formula machinery.

This distinction is essential for the line mandate. The finding does **not** say that the finite prime-lattice Gram geometry itself derives the zeros, and it does not transport the Dirichlet series

```text
-zeta'(s)/zeta(s)
 = sum Lambda(n)n^(-s)
```

from `Re(s)>1` to the critical line by coefficient algebra. The zero-sensitive bridge is precisely the extra global analytic structure that the bare Bohr lattice lacks.

## Relation to classical prime/zero pair-correlation theory

Heap's result is part of a well-established chain. Strong Hardy--Littlewood information on shifted `Lambda` correlations is classically tied to Montgomery's strong pair-correlation conjecture. Conversely, explicit-formula methods connect zero pair statistics to prime variance in short intervals; Goldston--Montgomery and subsequent refinements are standard anchors for this dictionary.

`PL-075` already recorded this neighboring theory but correctly stopped short of identifying its exact fixed-lag Gram term with Montgomery's `F`. The present finding sharpens the boundary using Heap's theorem:

- the exact **fixed-lag** `PL-075` statement remains an elementary sinc-kernel reduction to `Lambda(n)Lambda(n+h)`;
- a specific **global smoothed long polynomial** built from the same half-weight `Lambda` coefficients has a rigorous RH-conditional formula whose off-diagonal term is `F`;
- no equivalence is asserted for the sharp macroscopic band, and no unconditional implication toward RH is obtained.

The correct interpretation is therefore a routing statement, not an identification of all long-lag geometries.

## Prior-art and novelty audit

The principal source is:

- **Winston Heap**, “Conditional mean values of long Dirichlet polynomials,” *Forum Mathematicum* (ahead-of-print publication 29 July 2026), DOI `10.1515/forum-2024-0193`; preprint arXiv:2201.02108. Theorem 1 gives RH-conditional diagonal leading moments for suitably weighted long `Lambda/log n` polynomials. Theorem 2 gives the displayed RH-conditional mean-square formula for the triangularly smoothed `Lambda` polynomial, with Montgomery's `F` as the global off-diagonal term; Corollary 1 gives order `T(log T)^2` for `T<=X<=T^4`.

The surrounding pair-correlation dictionary is classical: Montgomery's 1973 pair-correlation work, Goldston's work on `S(t)`, and the Goldston--Montgomery/Chan prime-short-interval equivalences already explain why sufficiently aggregated prime correlations and zero correlations meet through explicit-formula machinery. Modern long-Dirichlet-polynomial work treats exactly the difficulty that the polynomial length reaches or exceeds the observation horizon.

No novelty is claimed for Heap's theorem, Montgomery pair correlation, Hardy--Littlewood correlations, or the explicit formula. The durable line-specific content is the **collision audit** with `PL-075`: the most immediate global completion of its surviving `Lambda` fixed-lag channel lands in this established theory, and the same long half-weight geometry can have diagonal or zero-correlated leading behavior depending on which arithmetic observable is inserted.

## Adversarial controls and limitations

1. **RH is an input, not an output.** Heap's zero-side asymptotic cannot be cited as evidence for RH or as an unconditional localization mechanism.
2. **The weight matters.** The theorem uses the triangular logarithmic factor `1-log n/log X`; Heap explicitly notes that his method requires special Fourier concentration and does not automatically cover ordinary sharp interval cutoffs.
3. **The `PL-075` sharp band is not identified with `F`.** The current result redirects the canonical smoothed global branch only. A sharp-band theorem would need its own proof and novelty audit.
4. **Pair correlation is not RH.** Even under RH, Montgomery's pair-correlation conjecture concerns spacing statistics of zeros, not the assertion that all nontrivial zeros lie on the line. Recovering `F` from an operator does not independently explain critical-line localization.
5. **The half exponent is still non-discriminating.** `PL-075` already gives the same fixed-lag power balance for the square-free control `mu^2`. Heap's theorem adds zeta sensitivity through the chosen `Lambda` observable and analytic continuation, not by making `1/2` intrinsically spectral.
6. **Helson/Beurling controls remain mandatory.** A new claim must identify which completion/target singles out the ordinary rational-prime object; generic `{log p}` character geometry alone remains too flexible.
7. **No new operator spectrum is produced.** `F(u,T)` is a zero-pair statistic in a mean-square identity. Calling it a spectral determinant, Hilbert--Polya operator, or new lattice spectrum would add unsupported interpretation.

## Consequence for the research line

The finite-horizon coefficient branch now has a clearer map:

```text
unweighted positive characters
    -> universal N~T sinc resolution (`PL-072`);

Möbius sign orientation, unpointed
    -> torus/diagonal gauge (`PL-073`);

pointed Möbius / square-free fixed lags
    -> Chowla / Mirsky (`PL-074`);

half-weight Lambda fixed lags
    -> Hardy--Littlewood prime pairs (`PL-075`);

smoothed long half-weight Lambda aggregate, under RH
    -> Montgomery zero pair correlation (this finding).
```

Accordingly, simply summing more lags or replacing the fixed-lag calculation by a smoothed long `Lambda` mean square is not a new route. The live target, if this finite-horizon branch is pursued further, must exhibit a statistic that is **not already exhausted by the classical prime/zero pair-correlation dictionary** and whose dependence on the rational-prime system survives the line's Helson/Beurling controls.

A potentially meaningful escape would have to use a target/completion or higher-order/global invariant for which the zero-sensitive content is not inserted through an RH-conditional explicit-formula reduction and is not reproduced by the usual long-Dirichlet-polynomial correlation theory. No such invariant is established here.
