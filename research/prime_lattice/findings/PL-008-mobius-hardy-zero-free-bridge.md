# PL-008 — Möbius hypercube cancellation already feeds a Hardy zero-free criterion, but the proved bridge stops at `Re(s)>1`

## Claim

A precise functional-analytic route from Möbius cancellation to zero-free half-planes is already present in the Nyman–Beurling/Báez-Duarte/Bagchi literature and has recently been connected explicitly to the Hardy–Hilbert space of Dirichlet series.

Let

```text
E(s)=1/s,
G_k(s)=(k^{-s}-k^{-1}) zeta(s)/s.
```

Bagchi's Hardy-space reformulation states that RH is equivalent to

```text
E in closure(span{G_k : k>=2}) in H^2(C_{1/2}),
```

where `C_alpha={Re(s)>alpha}`.

Manzur–Noor–Quintero (2026) prove the more general implication

```text
E in closure(span{G_k}) in H^2(C_alpha)
    => zeta has no zero in C_alpha
```

for every `alpha>=1/2`. They then construct a bounded bridge from the square-summable Dirichlet-series space `mathcal H^2` and prove, using the explicit Möbius coefficients,

```text
sum_{k=2}^infinity mu(k) G_k -> E
    in H^2(C_alpha) for every alpha>1.
```

In prime-exponent coordinates, `mu(k)` is exactly the signed square-free sector

```text
mu(k)=(-1)^(sum_p v_p(k))    if every v_p(k) is 0 or 1,
mu(k)=0                      otherwise,
```

and the key cancellation

```text
sum_{d|n} mu(d)=delta_{n,1}
```

is Möbius inversion on the divisibility lattice / Boolean face of the exponent lattice.

Therefore a natural version of the sought **Möbius + prime-lattice + Hilbert-space cancellation mechanism is already classical/current prior art**. Its proved analytic consequence reaches only the known zero-free half-plane `Re(s)>1`. Extending this particular closure mechanism into `1/2<Re(s)<=1` is not supplied by the lattice identity itself and would amount to obtaining genuinely new zero-free information in the critical strip.

**Evidence/status:** `LITERATURE+DERIVED` — material prior-art redirect with a boundary obstruction.

The closure criteria and convergence theorem are literature results. The prime-lattice identification of the Möbius coefficients with the oriented square-free hypercube is exact but standard. No novelty is claimed for either ingredient.

## Literature theorem bridge

Bagchi (2006), reformulating the Nyman–Beurling/Báez-Duarte criterion, gives

```text
RH <=> E belongs to the closed span of {G_k} in H^2(C_{1/2}).
```

The reason such closure controls zeros is transparent in the reproducing-kernel Hardy space. If `rho` is a zero of zeta in `C_alpha`, then

```text
G_k(rho)=0 for every k>=2,
```

whereas

```text
E(rho)=1/rho != 0.
```

Norm convergence in `H^2(C_alpha)` implies pointwise convergence, so `E` cannot lie in the closure if such a zero exists. Manzur–Noor–Quintero record this for every `alpha>=1/2` as their Proposition 3.1.

Their bridge starts from

```text
mathcal H^2={sum_n a_n n^{-s}: sum_n |a_n|^2<infinity}
```

and uses a bounded operator `M^tau` into `H^2(C_{1/2+tau})`. For `tau>1/2`, they construct functions `g_{k,tau}` whose Möbius-weighted sum converges in the source Hilbert space. After applying the bounded operator, this yields

```text
sum_{k=2}^infinity mu(k) G_k -> E
    in H^2(C_{1/2+tau}),   tau>1/2,
```

that is, in every `H^2(C_alpha)` with `alpha>1`.

## Where the exponent lattice enters exactly

The coefficient `mu(k)` has a direct exponent-vector meaning. For

```text
k <-> v(k)=(v_p(k))_p,
```

`mu(k)` vanishes outside the finite-support `{0,1}` hypercube and alternates sign by Hamming weight on that hypercube. Thus the divisor identity

```text
sum_{d|n} mu(d)=delta_{n,1}
```

is exactly the Möbius function of the coordinatewise divisibility poset. In the square-free sector it is the alternating Boolean-lattice cancellation over subsets of the prime support.

This is the concrete link between the prime-lattice picture and the Hardy approximation. It is not merely metaphorical: the proof rearranges a double series and invokes precisely this divisor cancellation to collapse the low-index coefficients.

## The analytic bottleneck in the proved argument

After the exact Möbius cancellation, the remaining tail in Manzur–Noor–Quintero has coefficients bounded using the divisor function. In their notation,

```text
||phi_n||^2
    <= sum_{j>n} d(j)^2 / j^(2 tau).
```

Using `d(j)=o(j^epsilon)` gives convergence when

```text
tau > 1/2,
```

which translates to

```text
alpha=1/2+tau > 1.
```

So the exact Boolean/divisor cancellation removes the main coefficients, but the available norm control still stops precisely on the far side of the Euler-product boundary. The paper explicitly states that its analytical method does not settle `1/2<=alpha<=1`.

At `alpha=1/2`, the specific full sequence of Möbius partial sums is known not to converge in the required norm; this does not rule out suitable subsequences or other approximants. The 2026 paper presents numerical behavior inside the critical strip, but explicitly labels it suggestive rather than proof. This branch must not treat those computations as evidence of a zero-free region.

## Relevance to the Mathia construction

This result materially redirects one tempting use of the square-free hypercube. A naive plan might be:

```text
oriented square-free hypercube
    -> exact Möbius cancellation
    -> Hilbert-space approximation
    -> critical-strip zero exclusion.
```

The first two arrows are classical and the third already has a rigorous realization. What remains hard is exactly the final analytic step: obtaining norm closure in a half-plane that penetrates the critical strip.

Thus the prime-lattice representation does identify the correct combinatorial cancellation, but **the combinatorics is not the missing RH ingredient**. The unresolved content lies in analytic control strong enough to transport that cancellation through the relevant Hardy norm near the critical boundary.

## Prior art and novelty assessment

- Nyman, Beurling, Báez-Duarte, and Bagchi already turn RH into a Hilbert-space closure/completeness problem.
- Bagchi (2006) gives the `H^2(C_{1/2})` formulation used here.
- Ghosh–Kremnitzer–Noor–Santos (2024) develop a broader analytic-function-space framework for deriving zero-free half-planes from completeness/closure properties.
- Manzur–Noor–Quintero (2026) explicitly connect `mathcal H^2` of Dirichlet series to the half-plane Hardy spaces and use Möbius coefficients to prove the approximation for `alpha>1`.
- The identification of `mu` with the signed square-free exponent hypercube is classical Möbius inversion, not new structure.

Accordingly, any Mathia claim that the signed `{0,1}` prime hypercube itself supplies a new Hardy-space RH mechanism fails the novelty audit. The residual research question must add genuinely new analytic structure or estimates beyond this established closure framework.

## Boundary conditions and counterarguments

- The convergence theorem is proved only for `alpha>1`; it gives a new proof of a classical zero-free region, not new critical-strip zero exclusion.
- Proposition 3.1 is an implication: closure in `H^2(C_alpha)` forces zero-freeness. It does not prove that closure holds in the critical strip.
- Numerical smallness of finite approximation errors for some `alpha<1` is not mathematical evidence of convergence and is not promoted here.
- Divergence of one canonical sequence at `alpha=1/2` does not refute the Bagchi criterion, because the criterion concerns the closed span and may use other linear combinations/subsequences.
- The exact Möbius divisor identity alone cannot be analytically continued; its usefulness depends on norm estimates for the residual tail.

## Audit / falsification criterion

The stored claim can be audited by checking three independent items in the cited sources:

1. Bagchi's equivalence at `alpha=1/2`.
2. The zero-free implication from closure in `H^2(C_alpha)`.
3. The `mathcal H^2 -> H^2(C_{1/2+tau})` bounded map and Möbius-series convergence for `tau>1/2`.

Any future claim that this route has entered the critical strip must provide a rigorous proof of closure/convergence for some `alpha<=1` (or a different approximating family with an equally rigorous zero-free implication). Numerical evidence, formal rearrangement of Möbius sums, or the identity `sum_{d|n}mu(d)=delta_{n,1}` is insufficient.

## Consequence for the research line

The square-free hypercube does carry an exact orientation — Möbius sign — whose cancellation survives into a serious RH-equivalent Hardy-space framework. But the known bridge already demonstrates where the difficulty moves: from combinatorial inversion to analytic norm control. This rules out treating Möbius cancellation on the exponent lattice, by itself, as the missing mechanism and gives a precise literature-backed boundary any stronger prime-lattice proposal must cross.
