# PL-045 — Prime Kronecker recurrence defeats uniform pointwise cancellation in localized Weil positivity

## Claim

A new compact-window Weil-positivity result makes a precise connection between the prime-exponent Kronecker flow and a concrete obstruction in the explicit-formula program. For each fixed window `L>0`, the non-archimedean part of the completed Weil symbol is the finite prime-power trigonometric polynomial

```text
P_L(t)
  = sum_(log n < 2L) 2 Lambda(n)/sqrt(n) cos(t log n)
  = sum_(k log p < 2L) 2 log(p)/p^(k/2) cos(k t log p).
```

In exponent coordinates the frequencies are exactly the active axis-ray lattice points

```text
k e_p,
E(k e_p)=<k e_p,(log q)_q>=k log p.
```

Let

```text
A_L = sum_(log n < 2L) 2 Lambda(n)/sqrt(n) = P_L(0).
```

Because the finitely many frequencies `{log p : p < exp(2L)}` are linearly independent over `Q`, Kronecker/Weyl recurrence implies that for every `epsilon>0` and every `T>0` there is a `t>T` for which all active prime phases `exp(i t log p)` are simultaneously as close to `1` as required. Their powers are then simultaneously close to `1` as well, so

```text
P_L(t) > A_L - epsilon.
```

Consequently

```text
limsup_(t -> infinity) P_L(t) = A_L.
```

This is stronger than the trivial observation `P_L(0)=A_L`: the full worst-case alignment recurs at arbitrarily large height. Therefore **no uniform pointwise tail estimate can gain cancellation from the prime phases**. Any method that tries to lower-bound the completed Weil symbol for every sufficiently large `t` by replacing the prime comb with a smaller universal constant is blocked by the prime Kronecker flow itself.

Marcus Chuk's August 2026 preprint proves this point explicitly and quantifies its cost for a particular certified positivity method. In his normalization,

```text
Psi_L(t)
  = Re psi(1/4+i t/2) - log pi - P_L(t),
```

and his one-stroke pointwise-envelope certificate requires a tail threshold

```text
T_sharp > T_1(L) = 2 pi exp(A_L).
```

The prime number theorem gives

```text
A_L = (4+o(1)) exp(L),
```

hence

```text
log T_1(L) = (4+o(1)) exp(L)
```

and the required tail scale is doubly exponential in the window radius. The finite matrix used by that certificate correspondingly has dimension of order `L T_1`.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
prime-torus phase cancellation
    -> improved uniform pointwise bound on the prime comb
    -> scalable localized Weil positivity
    -> RH.
```

The finding is deliberately narrow. It does not obstruct non-pointwise estimates that couple the prime comb to the Paley--Wiener constraints on the test function, nor does it obstruct global Weil positivity, sampling, de Branges/canonical-system, trace-formula, or other approaches that exploit more structure than a pointwise envelope.

## Exact exponent-lattice derivation

Fix `L`. Only finitely many rational primes occur because `k log p < 2L` implies `p < exp(2L)`. Let these primes be `p_1,...,p_r`. Unique factorization proves rational linear independence:

```text
sum_(j=1)^r q_j log p_j = 0,
q_j in Q
```

implies, after clearing denominators,

```text
product_j p_j^(m_j) = 1,
m_j in Z,
```

and hence every `m_j=0` and every `q_j=0`.

The continuous orbit

```text
t |-> (exp(-i t log p_1),...,exp(-i t log p_r))
```

is therefore dense in the finite torus `T^r`. Equivalently, it returns arbitrarily close to the identity after arbitrarily large times. If the basis phase for `p` is within `delta` of `1`, then for each of the finitely many active powers `p^k` its phase

```text
exp(-i t k log p)
```

is also close to `1`, uniformly once `delta` is chosen for the finite set of exponents.

Every coefficient in `P_L` is positive. Thus the torus identity is the simultaneous maximizer of every active axis-ray cosine, and recurrence gives values arbitrarily close to the same maximum at arbitrarily large `t`:

```text
sup_(t>T) P_L(t) = A_L
```

for every finite `T` (with `sup`, not necessarily `max`). This is the exact prime-lattice statement underlying Chuk's Weyl-equidistribution lemma.

The role of the full exponent lattice is sharply limited here. Because the Weil explicit formula is weighted by `Lambda`, the active Fourier support is only

```text
R_L = {k e_p : k log p < 2L};
```

mixed-prime vectors never occur directly. Nevertheless the primitive coordinate frequencies `log p` control all active rays at once. In this particular explicit-formula channel, the free prime-coordinate geometry therefore creates **coherent recurrence**, not generic cancellation.

## Why this is a genuine obstruction rather than a numerical inconvenience

The archimedean part of `Psi_L(t)` grows only logarithmically with `|t|`, while a uniform pointwise treatment of the prime comb must allow the full amplitude `A_L` at arbitrarily large heights. Thus one has to move far enough into the tail that the archimedean logarithm dominates a quantity of size `A_L`.

By partial summation and the prime number theorem,

```text
sum_(n <= x) Lambda(n)/sqrt(n) = (2+o(1)) sqrt(x).
```

Taking `x=exp(2L)` and multiplying by the factor `2` in the symbol gives

```text
A_L=(4+o(1))exp(L).
```

Since `Re psi(1/4+i t/2)-log pi = log(t/(2 pi))+o(1)` as `t->infinity`, a worst-case pointwise tail has to reach roughly

```text
t > 2 pi exp(A_L),
```

which is `exp((4+o(1))exp(L))`. Chuk makes this heuristic exact for his one-stroke certificate and shows that the constant `A_L` itself cannot be lowered within the class of pointwise prime-comb envelopes.

The obstruction is therefore structural: **the same rational independence of `log p` that gives equidistribution of the prime flow guarantees arbitrarily late near-perfect constructive interference.** Treating the torus phases as if they supplied a uniform random-like cancellation is mathematically false.

## Matched controls and arithmetic specificity

This obstruction is not itself special enough to distinguish the ordinary rational primes from all generalized systems. If a finite collection of positive generalized-prime energies `{omega_j}` is rationally independent, the same Kronecker argument makes

```text
sum_j,k a_(j,k) cos(k t omega_j)
```

with positive coefficients recurrent arbitrarily close to its all-aligned maximum. Thus the no-go survives Beurling-style replacement whenever the relevant finite energy set remains rationally independent.

The rational primes do supply a canonical and globally consistent infinite set of weights `log p`, and the PNT supplies the specific growth `A_L~4e^L`. But **recurrence itself is generic free-frequency geometry, not RH rigidity**. A successful use of the prime lattice must therefore exploit information that is lost by taking a pointwise supremum over its torus orbit.

## Relation to `PL-011` and `PL-044`

`PL-011` found that the canonical Kronecker flow has pure-point spectrum and by itself supplies no Hilbert--Polya zero spectrum. `PL-044` found that localized Weil self-adjointness and real-zero finite characteristic functions already exist in the prime-free window, so those properties are not the missing arithmetic mechanism.

The present result identifies what happens once the prime-power thresholds do activate. The finite prime flow does not automatically help positivity through phase cancellation. On the contrary,

```text
prime powers activate
    -> finite positive trigonometric prime comb
    -> Kronecker recurrence to the torus identity
    -> arbitrarily late near-maximal constructive interference
    -> no uniform pointwise cancellation gain.
```

This closes a natural but misleading bridge between `prime-torus equidistribution` and `Weil positivity`: equidistribution provides good average statistics but simultaneously guarantees the worst configurations needed to defeat a uniform pointwise argument.

## What remains live

Chuk's paper also demonstrates why the negative is method-specific. His certified positivity at `L=0.8` is obtained by combining an exact low-frequency finite-matrix estimate with a sign-definite high-frequency tail, not by claiming generic prime cancellation. At this scale the active exponent rays are already nonempty (`2`, `3`, and `4` satisfy `log n<1.6`), so unconditional positivity extends beyond the prime-free window of `PL-044`.

The durable target is therefore **non-pointwise cross-scale arithmetic control**. Examples that are not excluded include:

```text
- estimates coupling P_L(t) to where a Paley--Wiener transform |F(t)|^2 can concentrate;
- quantitative control of the measure/spacing of near-alignment times rather than their existence;
- an arithmetic uncertainty or large-sieve inequality for the log-prime frequency set;
- a trace/positivity identity that compares successive prime-power activation thresholds without taking a pointwise supremum;
- a genuinely zeta-specific global mechanism connecting those finite-window forms as L -> infinity.
```

Any such proposal must be tested against rationally independent Beurling energy sets: a statement depending only on torus density/recurrence remains too generic.

## Analytic-continuation boundary

No Euler product is continued into the critical strip in this argument. The symbol `Psi_L` is the geometric side of the **completed Weil explicit formula**, so the zeta continuation and archimedean terms are already part of the established formula. The prime sum is finite for each fixed `L`.

Kronecker recurrence is applied only to that finite trigonometric polynomial. The PNT is used only to estimate its total coefficient mass as `L->infinity`. Thus the obstruction survives the analytic-continuation audit cleanly.

## Prior-art and novelty audit

The principal source is:

- **Marcus Chuk**, “Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law,” arXiv:`2608.24827` (submitted 25 August 2026; manuscript dated 27 August 2026), preprint. Its Lemma 6 proves optimality of the pointwise prime-comb constant using Weyl equidistribution of the prime-log phases; Theorem 3 derives the threshold `T_1(L)=2 pi exp(A_L)` and the doubly exponential matrix-size barrier for the one-stroke pointwise-envelope certificate. The paper also proves unconditional positivity at `L=0.8` and clearly separates the certified theorem from the fitted Landau--Widom law.

The underlying rational independence of `{log p}` and finite-dimensional Kronecker/Weyl theorem are classical and were already part of the corpus around `PL-011`. The exponent-coordinate rewrite `k e_p -> k log p` is immediate. **No novelty is claimed for the theorem or the recurrence argument.** The durable contribution is the research-line redirect: a newly explicit Weil-positivity theorem shows that the prime Kronecker flow is an adversarial obstruction to uniform pointwise cancellation, rather than a source of the cancellation needed for RH.

A targeted literature search around prime-log Kronecker flow, Weil's explicit formula, and pointwise prime-comb cancellation found the exact modern result above; older sources in the corpus provide the ingredients but not a stronger theorem needed here. Since the key no-go is already explicit in Chuk, this finding is stored as prior-art/derived evidence rather than as an original claim.

## Falsification and escape tests

The core claim would fail if any of the following were established:

1. a nontrivial rational relation among finitely many distinct `log p`;
2. a fixed tail `t>T` on which `P_L(t) <= A_L-delta` for some `delta>0`;
3. a pointwise-envelope certificate whose proof genuinely uses a universal constant below `A_L` while remaining valid for all sufficiently large `t`;
4. an error in the stated finite Weil symbol or in the positive von-Mangoldt weights.

Items 1--2 are excluded by unique factorization and Kronecker recurrence; item 3 would contradict the same recurrence unless it uses additional `t`-dependent/test-function information and therefore is no longer a pure pointwise envelope; item 4 is fixed by the standard completed explicit formula and Chuk's explicit normalization.

The finding does **not** claim that the doubly exponential threshold is an intrinsic complexity lower bound for all proofs of localized Weil positivity. It is a sharp obstruction only for the pointwise-envelope class audited above.

## Consequence for the research line

The prime torus now has a more precise role in the completed explicit-formula channel:

```text
Bohr/Kronecker coordinates
    -> exact phases exp(-it log p)
    -> dense finite torus orbits
    -> arbitrarily late coherent prime-power alignment
    -> optimal worst-case prime-comb amplitude A_L
    -> pointwise Weil-positivity barrier.
```

Accordingly, further `prime_lattice` work should not seek an RH mechanism in uniform pointwise cancellation of the finite prime phases. The live question is whether the **distribution and cross-scale organization** of those recurrences, when coupled to the Paley--Wiener/Nyman/Weil target rather than viewed pointwise, carries arithmetic rigidity that fails generic rationally independent frequency systems.