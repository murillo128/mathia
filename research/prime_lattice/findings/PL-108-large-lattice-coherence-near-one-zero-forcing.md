# PL-108 — Large energy-ball coherence along the log-prime flow forces local zeta-zero clusters near `Re(s)=1`

## Claim

A very recent inverse theorem gives a rigorous, nontrivial bridge from a finite prime-exponent-lattice Fourier amplitude to the zero set of the ordinary Riemann zeta function.

For `x>=1`, let

```text
B_x = { alpha in N_0^(P), finite support :
        E(alpha)=sum_p alpha_p log p <= log x }.
```

Unique factorization identifies `B_x` with the integers `n<=x`. Along the distinguished Kronecker orbit

```text
z_p(t)=p^(it)=exp(i t log p),
```

the finite Bohr polynomial

```text
P_x(z)=sum_(alpha in B_x) z^alpha
```

satisfies the exact identity

```text
P_x(z(t))
 = sum_(alpha in B_x) exp(i t E(alpha))
 = sum_(n<=x) n^(it)
 =: S(x,t).
```

Dong, Wang, Wang, and Zhang (arXiv:2608.31060, submitted 31 August 2026 and revised 1 September 2026) prove an unconditional **inverse zero-forcing theorem** for large values of `S(x,t)`. In their stated range

```text
T <= |t| <= 2T,
exp(sqrt(log T)) <= x <= sqrt(T),
|S(x,t)| = x/N,
N <= (log x)^(1/100),
```

there is a real `phi` close to `t` such that, for every admissible

```text
c N^6 <= L <= (log x)/2,
```

the disk centered at `1+i phi` with radius

```text
R = L log T / (log x)^2
```

contains at least `L/360` nontrivial zeta zeros, counted with multiplicity.

Thus an abnormally coherent value of the **uniform energy-sublevel lattice amplitude** is not merely correlated with zeta: it quantitatively forces a local zero cluster near the same spectral height.

However, the theorem does **not** supply the critical-line geometry sought by this research line. The Fourier observable depends on `alpha` only through the scalar energy `E(alpha)=log n`, and its analytic bridge is the shifted Dirichlet series `zeta(s-it)`. The mechanism naturally works near the Euler-product/pole edge `Re(s)=1`; `Re(s)=1/2` enters only when one asks whether the forced disk lies wholly to the right of the critical line. It is therefore a genuine harmonic/arithmetic mechanism and useful RH diagnostic, but not a full-lattice localization mechanism selecting the critical line.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT`.

No novelty is claimed for the inverse theorem, the Bohr rewrite, or the character-sum method behind it. The durable contribution here is to identify exactly what this new theorem means in the canonical `prime_lattice` coordinates and to separate its real zero-forcing content from a stronger claim that the exponent-lattice geometry itself explains `Re(s)=1/2`.

## 1. Exact exponent-lattice / Bohr formulation

Write

```text
n = product_p p^(alpha_p),
alpha=v(n),
E(alpha)=<alpha,(log p)_p>=log n.
```

Then `n<=x` is exactly the weighted lattice simplex/energy ball

```text
E(alpha)<=log x.
```

Define the counting measure on that finite set,

```text
mu_x = sum_(alpha in B_x) delta_alpha.
```

Its character evaluation along the one-parameter prime-frequency flow is

```text
A_x(t)
 = integral exp(i t E(alpha)) d mu_x(alpha)
 = S(x,t).
```

Equivalently, on the infinite torus,

```text
P_x(z)=sum_(alpha in B_x) z^alpha,
z(t)=(p^(it))_p,
A_x(t)=P_x(z(t)).
```

This is a literal finite Bohr polynomial with coefficient `1` on every exponent vector below the arithmetic-energy cutoff. The sign convention is immaterial: the more usual vertical zeta orbit uses `p^(-it)`, which complex-conjugates this polynomial for real `t`.

The normalized quantity

```text
C_x(t)=S(x,t)/x
```

can therefore be read as a mesoscopic coherence amplitude of all exponent-lattice points in the energy ball when sampled by the `log p` Kronecker flow. Large `|C_x(t)|` means that the phases

```text
exp(i t <alpha,log p>)
```

fail to cancel strongly over the energy sublevel set.

This interpretation is exact; no Euler product or analytic continuation is used in obtaining it.

## 2. The new inverse theorem is genuinely zero-forcing

Theorem 1.1 of Dong--Wang--Wang--Zhang starts with one large value of

```text
S(x,t)=sum_(n<=x)n^(it)
```

and forces many zeros of `zeta` near height `t`. In the notation above, the hypothesis is exactly a lower bound on one value of the finite lattice Fourier transform:

```text
|P_x(z(t))|=x/N.
```

Under the quantitative range stated in the claim, there exists `phi` with `phi` close to `t` for which every permitted `L` produces at least `L/360` zeros in

```text
D(1+i phi, R),
R=L log T/(log x)^2.
```

This direction is mathematically stronger than merely saying that the same frequencies occur in both objects. The input polynomial contains no zeta zeros and no zero-dependent coefficients. A sufficiently coherent arithmetic phase sum forces the zero set of a separately defined analytic function to have local mass.

The paper's proof is not a spectral/operator construction. It adapts the Granville--Soundararajan inverse method for large character sums, using mean-value estimates for multiplicative functions, a Gaussian transform, and the Hadamard-product/zero information of `zeta`. The associated Dirichlet series is shifted in height:

```text
sum_(n>=1) n^(it) n^(-s) = zeta(s-it)
```

in its half-plane of absolute convergence. This is why a large sum at frequency `t` produces zero information near height `t`. The pole of zeta at `1` also contributes a residue when the Gaussian contour is shifted; the authors show that this residue is exponentially small in their working range rather than silently discarding it.

## 3. A large enough coherence event can be an unconditional RH-falsification certificate

The forced disks are centered on the vertical line `Re(s)=1`. Therefore, whenever one can choose an admissible `L` for which

```text
R=L log T/(log x)^2 < 1/2,
```

the entire forced disk lies in

```text
Re(s)>1/2.
```

Since the theorem guarantees at least one nontrivial zero there (indeed at least `L/360` counted with multiplicity once the numerical lower bound is nonzero), such a coherence event would contradict RH.

Taking the smallest permitted scale `L` of order `N^6`, the relevant geometric condition is of the form

```text
N^6 log T / (log x)^2 < constant.
```

The exact absolute constant is inherited from the theorem and is not normalized away here.

Conversely, the paper proves a local zero-density implication: if thin fixed windows immediately to the left of `Re(s)=1` contain sufficiently few zeros, then in polynomial ranges of `x` one has

```text
|S(x,t)| << x/(log x)^(1/100).
```

For any fixed window width `delta<1/2`, RH makes that near-`1` zero hypothesis automatic because all nontrivial zeros would lie on `Re(s)=1/2`. Thus RH excludes the extreme coherence regime addressed by the theorem.

This is a real RH-sensitive harmonic statement, but it is not an equivalence in the form recorded here and must not be promoted to one.

## 4. Why this still does not identify a critical-line mechanism

The exponent-vector notation makes an important information-loss point explicit. The observable is

```text
alpha -> exp(i t E(alpha)),
E(alpha)=<alpha,log p>.
```

Hence it factors completely through the scalar map

```text
alpha -> E(alpha)=log n.
```

It does not inspect coordinate support, Hamming weight, square-free faces, divisibility joins, prime-axis incidence, or any other multidimensional relation between exponent vectors. Two constructions with the same multiset of scalar energies would give the same Fourier amplitude.

The mechanism therefore belongs to the strongest **energy-projection** part of the prime-lattice program, not to a genuinely multidimensional prime-coordinate geometry.

There is a second boundary. The proof's analytic object is `zeta(s-it)` and its zero-forcing argument operates in neighborhoods of the pole/Euler-product boundary at `Re(s)=1`. The line `Re(s)=1/2` is not selected by a symmetry, positivity law, self-duality, or self-adjoint spectrum in the theorem. It appears only as the RH boundary against which a disk centered at `Re(s)=1` can be tested.

So the exact logical picture is

```text
large lattice energy coherence
        |
        v
multiplicative mean-value / Gaussian inverse theorem
        |
        v
many zeta zeros near 1+i t
        |
        +-- if the forced neighborhood stays right of 1/2 -> RH is false
```

not

```text
prime-lattice geometry -> zeros are forced onto Re(s)=1/2.
```

## 5. Prior art and novelty audit

The main source is:

- **Zikang Dong, Ruihua Wang, Weijia Wang, Hao Zhang**, “Large zeta sums and zeros of the Riemann zeta function,” arXiv:2608.31060 [math.NT], submitted 31 August 2026, revised 1 September 2026. Theorem 1.1 is the pointwise inverse zero-forcing result used above; Theorem 1.2 gives the local zero-density-to-small-sum consequence.

The paper explicitly places itself in two established lines of prior art.

First, Gonek, Graham, and Lee recast Lindelof-type/RH questions in terms of exponential sums of the form `sum_(n<=x)n^(-it)` and generalized sequences:

- **Steven M. Gonek, Sidney W. Graham, Yoonbok Lee**, “The Lindelöf hypothesis for primes is equivalent to the Riemann hypothesis,” *Proceedings of the American Mathematical Society* **148** (2020), 2863–2875. DOI `10.1090/proc/14974`.

Second, the inverse mechanism is modeled on the theorem that large character sums force zeros of the associated Dirichlet `L`-function:

- **Andrew Granville, Kannan Soundararajan**, “Large character sums: Burgess's theorem and zeros of L-functions,” *Journal of the European Mathematical Society* **20** (2018), 1–14. DOI `10.4171/JEMS/757`.

The new 2026 theorem is therefore not evidence that Mathia independently discovered a new prime-lattice principle. Its value for this line is that a very natural finite Fourier observable of the weighted exponent lattice now has a rigorous inverse theorem to ordinary zeta zeros, and the theorem sharply reveals where that mechanism lives: scalar energy projection and the near-`1` analytic edge.

A targeted search on 2 September 2026 for the exact theorem together with exponent-lattice, Bohr/Kronecker, and Hilbert--Polya language found no source claiming that this inverse theorem supplies a multidimensional or spectral localization explanation of the critical line. Absence of such wording is not used as a novelty claim.

## 6. Adversarial boundaries

### This is not just `zeta` inserted into the observable

Correct. `P_x(z)` has coefficient `1` on the finite energy ball and is defined without zeta zeros. The nontrivial content is the analytic-number-theory theorem that a large value forces a zero cluster. That is why this result is stronger than the programmable-readout obstruction of `PL-106`.

### The proof nevertheless uses zeta analytically

Also correct. The inverse theorem is not an operator generating zeta from the bare lattice. Its proof uses the associated Dirichlet series `zeta(s-it)`, Hadamard/zero information, and a contour/Gaussian argument. The correct status is a rigorous **arithmetic inverse theorem**, not an independent Hilbert--Polya construction.

### Does a large sum force zeros on the critical line?

No. It forces zeros in disks centered near `Re(s)=1`. In a sufficiently small disk those zeros would actually be **to the right** of the critical line and hence disprove RH. The result is therefore naturally a zero-free-region/coherence constraint, not a localization theorem placing zeros on `1/2`.

### Could the full exponent geometry be hidden in the cutoff `n<=x`?

The cutoff is indeed the weighted simplex `E(alpha)<=log x`, so the exponent lattice gives a useful exact geometric description of the summation set. But the phase and cutoff both factor through the same scalar energy `E(alpha)`. No theorem step in the present result distinguishes coordinate directions once their sum `E(alpha)` is known. Claiming genuinely multidimensional lattice dependence would therefore overstate the evidence.

### Does the result cross the analytic-continuation boundary legitimately?

Yes, but through the paper's analytic argument, not through termwise continuation of the finite polynomial or Euler product. The finite `S(x,t)` is entire in `t`; the zero conclusion is obtained through estimates and contour/Hadamard machinery for zeta. Nothing here asserts an Euler-product identity in the critical strip.

## Consequence for the research line

This finding adds a useful positive mechanism to the otherwise obstruction-heavy harmonic audit:

```text
energy-ball lattice Fourier coherence
    -> can force ordinary zeta zeros quantitatively.
```

But it also gives a clean design boundary. Coherence of the single projected frequency

```text
log n=<v(n),log p>
```

already has powerful zero-detection content, yet its natural inverse theorem points to `Re(s)=1`, not to a geometry that forces `Re(s)=1/2`.

Future work should therefore not treat the mere existence of large/small Kronecker-flow sums as the missing critical-line mechanism. A genuinely new contribution would need either:

1. an additional invariant using relations among exponent coordinates that does not factor through `log n`; or
2. a global positivity/self-duality/operator principle coupling such coherence to the completed functional equation in a way that **localizes** zeros rather than merely detecting or excluding them near `Re(s)=1`.

This leaves the new inverse theorem as a strong benchmark: any proposed prime-lattice harmonic mechanism should explain what information it contains beyond `S(x,t)` and why that extra information changes zero **location**, not only zero detection.