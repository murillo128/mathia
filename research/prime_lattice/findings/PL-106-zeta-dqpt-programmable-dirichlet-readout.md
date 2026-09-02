# PL-106 — Engineered zeta DQPTs are programmable Dirichlet-series readouts, not a prime-lattice zero-localization mechanism

## Claim

The 2026 Nature Communications construction of Wei et al. gives a genuine engineered quantum realization in which dynamical observables reproduce Riemann-zeta zero information, but its first mechanism is exactly a **programmable Dirichlet-series readout** over the logarithmic spectrum and therefore does not add an independent prime-lattice mechanism that could force the zeros onto `Re(s)=1/2`.

For a finite cutoff `N`, put

```text
H_N = sum_(n<=N) log(n) |n><n|,
Z_N(beta) = sum_(n<=N) n^(-beta),
rho_(beta,N) = Z_N(beta)^(-1) exp(-beta H_N).
```

For any diagonal phase observable

```text
A_a = sum_(n<=N) a_n |n><n|,
|a_n|=1,
```

one has the exact identity

```text
Tr(rho_(beta,N) exp(-it H_N) A_a)
 = Z_N(beta)^(-1)
   sum_(n<=N) a_n n^(-(beta+it)).
```

Thus the architecture `log n spectrum + thermal weights + diagonal phase` can encode **any chosen unimodular Dirichlet polynomial**. The Wei et al. first system chooses

```text
a_n=(-1)^(n+1),
```

so the numerator is the partial Dirichlet eta series. For `Re(s)>0`,

```text
eta(s)=sum_(n>=1) (-1)^(n+1)n^(-s)
      =(1-2^(1-s)) zeta(s).
```

The continuation into the critical strip is therefore supplied by the classical alternating-series regularization encoded in the observable. It is not generated dynamically from the bare exponent lattice, and it is not a continuation of the Euler product.

In exponent-vector coordinates, the chosen phase is especially sparse:

```text
a(v(n)) = +1  if v_2(n)=0,
          -1  if v_2(n)>=1.
```

It only asks whether the `2`-coordinate is occupied. The full mixed-prime geometry of `v(n)` does not enter the continuation mechanism.

The paper's thermodynamic dynamical-free-energy statement is an exact RH-equivalent **readout** of the already encoded zeta divisor. For `0<beta<1`, the normalization itself diverges as

```text
Z_N(beta) ~ N^(1-beta)/(1-beta).
```

At a point where `eta(beta+it) != 0`, the numerator converges to a nonzero constant and hence the raw phase amplitude already tends to zero like `N^(-(1-beta))`. At a zeta zero, the eta partial sum has the additional alternating-series tail decay used by Wei et al.; their normalized free-energy density jumps from

```text
(1-beta) log 2
```

to

```text
log 2.
```

Therefore the mathematically stable thermodynamic diagnostic is the **change of decay exponent**, not literal pointwise vanishing of the raw normalized amplitude, which occurs generically throughout `0<beta<1`. If a hypothetical nontrivial zero existed at `beta != 1/2`, the same construction would produce the same DQPT singularity there. The quantum system consequently reformulates

```text
all nontrivial zeta zeros have beta=1/2
```

as

```text
all corresponding engineered DQPT singularities occur at beta=1/2,
```

but supplies no independent principle that enforces the latter.

The paper's second construction is even more explicitly zeta-specific: its time-dependent coupling contains the derivative of the **Riemann–Siegel theta function**, and its Loschmidt amplitude is built from the Riemann–Siegel/Hardy-`Z` approximation. This is a useful physical realization and computational observable, but not an independently derived spectral localization law.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
logarithmic integer/exponent-lattice Hamiltonian
+ engineered thermal state
+ engineered phase/Loschmidt observable reproducing zeta
+ DQPT singularities at encoded zeros
    -> new arithmetic mechanism forcing Re(s)=1/2.
```

The negative conclusion is deliberately scoped. It does **not** dispute the experiment, the exact correspondence, the DQPT interpretation, or the proposed quantum algorithms. It says only that the correspondence is not an independent zero-localization mechanism for the Prime-Lattice objective because the relevant Dirichlet coefficients and, in the second model, Riemann–Siegel completion data are explicitly programmed into the dynamics.

## 1. Exact universal Dirichlet-polynomial encoder

The exact finite-dimensional calculation is independent of zeta. Since

```text
exp(-beta H_N)
 = sum_(n<=N) n^(-beta)|n><n|
```

and

```text
exp(-it H_N)
 = sum_(n<=N) n^(-it)|n><n|,
```

any diagonal `A_a` gives

```text
rho_(beta,N) exp(-itH_N) A_a
 = Z_N(beta)^(-1)
   sum_(n<=N) a_n n^(-(beta+it)) |n><n|.
```

Taking the trace proves

```text
boxed:
L_(a,N)(beta,t)
 = Z_N(beta)^(-1)
   sum_(n<=N) a_n n^(-s),
 s=beta+it.
```

No arithmetic theorem has been used. The Hamiltonian supplies the universal frequency map

```text
n -> log n = <v(n),(log p)_p>,
```

while the observable supplies the coefficient sequence `a_n`.

This distinction is essential for the Prime-Lattice mandate. The same logarithmic Hamiltonian can read out very different Dirichlet series simply by changing the diagonal phase. Hence a zero set observed in `L_(a,N)` is not determined by the spectrum `log n` or by the exponent lattice unless one first proves that the coefficient observable `A_a` itself is canonically forced by additional arithmetic structure.

## 2. The Wei phase is exactly the eta regularization

Wei et al. choose a probe phase which acts on the `n`th thermal population as

```text
(-1)^(n+1)n^(-it).
```

Therefore

```text
L_N(beta,t)
 = Z_N(beta)^(-1)
   sum_(n<=N)(-1)^(n+1)n^(-s).
```

For `Re(s)>0`, the alternating Dirichlet series converges by the Dirichlet test. The identity

```text
eta(s)=(1-2^(1-s))zeta(s)
```

is first elementary in `Re(s)>1` and then continues analytically; equivalently the eta series itself supplies the classical continuation of the product on that half-plane. This is a legitimate continuation bridge, unlike transporting the Euler product term-by-term into the critical strip.

In prime-exponent coordinates,

```text
n odd  <=> v_2(n)=0,
n even <=> v_2(n)>=1.
```

Hence the coefficient is the one-coordinate threshold

```text
(-1)^(n+1)
 = 1 - 2 * 1_(v_2(n)>=1).
```

The corresponding Dirichlet identity can be seen directly as

```text
sum_n n^(-s)
 -2 sum_(2|n)n^(-s)
 = zeta(s)-2^(1-s)zeta(s)
```

in `Re(s)>1`, followed by the eta continuation to `Re(s)>0`.

There is no interaction here among different prime coordinates. In particular the continuation mechanism does not use square-free cube geometry, mixed-prime faces, Kronecker correlations among `{log p}`, or a new global operator coupling all places.

A simple analytic control shows that even the `2`-choice is not the structural source of continuation. For every integer `q>=2`, the bounded periodic coefficient

```text
b_q(n)=1-q*1_(q|n)
```

has mean zero over one period and hence its Dirichlet series converges for `Re(s)>0`. In `Re(s)>1`,

```text
sum_n b_q(n)n^(-s)
 =(1-q^(1-s))zeta(s),
```

and analytic continuation extends the identity. The case `q=2` is special physically because `b_2(n)` is already phase-valued `+/-1`; mathematically the continuation principle is ordinary periodic cancellation rather than a rigidity of the rational-prime lattice.

## 3. The thermodynamic limit detects a decay exponent, not exclusive raw zeros

A normalization subtlety matters for interpreting the zero statement. For fixed `0<beta<1`,

```text
Z_N(beta)
 = sum_(n<=N)n^(-beta)
 ~ N^(1-beta)/(1-beta).
```

If `eta(s) != 0`, then

```text
sum_(n<=N)(-1)^(n+1)n^(-s)
 -> eta(s) != 0,
```

so

```text
L_N(beta,t)
 ~ (1-beta) eta(s) N^(-(1-beta))
 ->0.
```

Thus the raw normalized phase amplitude tends to zero at every such fixed point in the open critical strip, not only at zeta zeros.

At a zero of `zeta(s)` with `0<beta<1`, the prefactor `1-2^(1-s)` is nonzero, so `eta(s)=0`. The remaining partial sum is the negative tail of the convergent eta series and decays on the additional `N^(-beta)` scale used in the paper. With `d=log_2 N`, Wei et al. obtain

```text
F_1(beta,t)
 = -lim_(N->infinity) d^(-1) log|L_N(beta,t)|
 = log 2                      if zeta(s)=0,
   (1-beta)log 2              if zeta(s)!=0, 0<beta<1,
   0                           if beta>1.
```

This is a real nonanalytic rate-function distinction. But it is logically downstream of the exact eta/zeta identity. If an off-line zero `rho=beta+it` existed, the numerator would have the same extra decay at that `beta`, and the same free-energy jump would occur there. Nothing in the logarithmic Hamiltonian or thermodynamic normalization prevents that outcome.

Therefore

```text
RH
<=>
all zeta-induced singularities of this engineered rate function
occur at beta=1/2
```

is an exact reformulation, not a proof-producing selection principle for the half-axis.

## 4. The second system inserts the Riemann–Siegel completion explicitly

The complementary Loschmidt construction does not repair this logical direction. Wei et al. use the time-dependent Hamiltonian

```text
H_c(t')
 = sigma_x tensor (H_0 - theta_dot(t') I),
```

where `theta(t)` is the Riemann–Siegel theta function associated with `zeta(1/2+it)`. Their generalized Loschmidt amplitude at `beta=1/2` is then expressed through

```text
exp(i theta(t)) sum_(n<=N)n^(-1/2-it)
+ exp(-i theta(t)) sum_(n<=N)n^(-1/2+it),
```

with `N~sqrt(t/(2 pi))`, i.e. the classical Riemann–Siegel approximation to Hardy's `Z(t)`.

This construction can be valuable as a quantum realization or zero-finding algorithm. For the mathematical Prime-Lattice question, however, the archimedean completion phase that makes the Hardy function real on the critical line is already an explicit input to the Hamiltonian. The model therefore cannot be used to infer that the prime-exponent geometry itself derived that completion or selected the critical line.

This is exactly the continuation/completion distinction enforced by `PL-013` and `PL-014`: a legitimate critical-strip mechanism needs archimedean/global data, but importing those data into an engineered observable is not the same as deriving a new localization theorem from the lattice.

## 5. Matched-control: the same Hamiltonian can encode flexible Helson divisors

The programmability obstruction is stronger than a purely formal objection. Choose any completely multiplicative unimodular function `chi`, so

```text
|chi(n)|=1,
chi(mn)=chi(m)chi(n).
```

Using the same logarithmic Hamiltonian and the diagonal phase

```text
A_chi |n> = chi(n)|n>
```

gives exactly

```text
Tr(rho_(beta,N)e^(-itH_N)A_chi)
 = Z_N(beta)^(-1)
   sum_(n<=N) chi(n)n^(-s).
```

These are finite sections of Helson zeta functions. `PL-003` records the decisive literature control: while preserving the same ambient prime-character torus and the same frequency list `{log p}`, suitable choices of `chi(p)` can produce radically different continuation domains and essentially arbitrary meromorphic zero/pole divisors.

This does **not** claim that the precise Wei free-energy tail asymptotic or DQPT theorem automatically transfers to every Helson function; that would require separate partial-sum estimates. The control is used only at the correct logical level: the quantum trace architecture itself does not determine the analytic divisor. The divisor depends on the programmed coefficient phase.

Consequently a successful dynamical Prime-Lattice mechanism would need an independent theorem showing why the untwisted/eta observable is canonically selected and why the resulting dynamics has a positivity or spectral constraint that fails for these flexible phase controls.

## 6. Prior art and novelty audit

The 2026 DQPT paper is recent, peer-reviewed work and should be credited for the physical construction, experimental implementation, DQPT correspondence, and quantum-algorithm analysis:

- **Shijie Wei, Yue Zhai, Quanfeng Lu, Wentao Yang, Pan Gao, Chao Wei, Junda Song, Franco Nori, Tao Xin, Guilu Long**, “The Riemann Hypothesis manifested in dynamical quantum phase transitions,” *Nature Communications* **17** (2026), Article 8163, DOI `10.1038/s41467-026-74935-8`; published 1 July 2026, version of record 11 August 2026.

The mathematical ingredients that make the Prime-Lattice collision decisive are older:

- `PL-004` already records Julia's classical Riemann/primon gas: levels `log p`, occupation numbers `v_p(n)`, total energy `log n`, and zeta as partition function are prior art.
- R. Mack et al., “Riemann zeta function from wave-packet dynamics,” *Physical Review A* **82** (2010), 032119, DOI `10.1103/PhysRevA.82.032119`, is earlier engineered-quantum prior art connecting wave-packet dynamics with zeta.
- C. Feiler and W. P. Schleich, “Entanglement and analytical continuation: an intimate relation told by the Riemann zeta function,” *New Journal of Physics* **15** (2013), 063009, DOI `10.1088/1367-2630/15/6/063009`, explicitly uses quantum measurements to realize Dirichlet representations and analytic continuation into the critical strip.
- `PL-003` supplies the stronger line-specific matched control through Helson-zeta divisor flexibility.

No novelty is claimed here for the eta identity, the logarithmic Hamiltonian, DQPT theory, or the physical realization. The durable Mathia contribution is the **exact architecture audit** against the canonical `prime_lattice` mandate: the new DQPT correspondence is a programmable coefficient readout of a known continued Dirichlet function, and therefore does not close the missing arrow from exponent-lattice geometry to an independent zero-localization law.

## 7. Adversarial boundaries

1. **The physical result is not dismissed as tautological in every sense.** Realizing the encoded correspondence in a controllable many-body platform, identifying its DQPT rate structure, and studying quantum resources are substantive physics/computation results. The negative conclusion concerns only its use as a new mathematical RH mechanism for this line.

2. **The eta continuation is legitimate.** The series converges for `Re(s)>0`; the finding does not accuse the construction of using the divergent Euler product in the critical strip. The point is precisely that a known continuation device is built into the phase observable.

3. **The raw thermodynamic amplitude and the rate function must not be conflated.** In `0<beta<1`, the partition normalization makes the raw amplitude tend to zero generically. The zeta zeros are distinguished by the extra numerator decay and hence by the free-energy exponent/nonanalyticity.

4. **The finite system is an approximation.** At finite `N`, zeros of the truncated Dirichlet polynomial need not equal the exact zeta zeros. The paper's statements concern controlled thermodynamic and, for the second model, joint large-`N`/large-`t` limits.

5. **Helson flexibility is a matched-control for the encoder, not a transferred DQPT theorem.** No claim is made that arbitrary Helson phases have the same thermodynamic critical exponents.

6. **The coefficient `(-1)^(n+1)` is not the Möbius function and does not use the square-free cube.** It depends only on occupation/nonoccupation of the prime `2` coordinate. Any inference from the DQPT construction to full square-free or mixed-prime lattice geometry would require an additional argument.

7. **The location `beta=1/2` is not a thermodynamic equilibrium critical point of `Z_N`.** The free Riemann-gas partition function has its classical singularity at `beta=1`; the DQPT half-axis is inherited from the location of the encoded nontrivial zeta zeros. Therefore it cannot independently explain why those zeros should be there.

## Consequence for the research line

This current-literature audit closes a tempting dynamical shortcut:

```text
prime/exponent energies log n
    -> engineered quantum dynamics
    -> observable equal to a continued zeta representation
    -> DQPTs at zeta zeros
    -> explanation of RH.
```

The first three arrows are valid and physically realizable, but the fourth only reads out the zero divisor already carried by the chosen Dirichlet coefficients/completion data. The architecture remains compatible with arbitrary programmed unimodular coefficient phases and therefore does not by itself constrain that divisor.

A surviving quantum/dynamical route must instead derive a **non-programmable arithmetic constraint**: a canonical state/observable/operator forced by the rational-prime structure, together with an independent positivity, self-adjointness, trace, or localization theorem that excludes off-line zeros and fails for Helson/Beurling controls. Merely constructing a Hamiltonian or observable whose expectation value is a known representation of `zeta(s)` is now a decisive prior-art/programmability no-go for this line.
