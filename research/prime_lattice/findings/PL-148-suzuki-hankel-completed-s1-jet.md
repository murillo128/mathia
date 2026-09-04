# PL-148 — Suzuki’s Hankel criterion is a completed `s=1` jet, not a raw prime-lattice moment measure

## Claim

Masatoshi Suzuki’s 2023 screw-function theory already contains the natural Hankel/Stieltjes-moment discretization of the scalar prime-power-axis positivity channel isolated in `PL-146` and `PL-147`. With

`mu_m = (1/4) integral_0^infinity exp(-t/2) Psi(t) t^m dt`,

Suzuki proves that RH is equivalent to nonnegativity of the determinants of both Hankel towers

`Delta_n = (mu_(i+j))_(0<=i,j<=n)`

and

`Delta_n^(1) = (mu_(i+j+1))_(0<=i,j<=n)`

for every positive integer `n`. He also proves the exact generating identity

`mu_m = [d^m/dX^m ((1-2X)^(-2) (xi'/xi)(1-X))]_(X=0)`.

Thus the entire RH-equivalent Hankel data is already encoded by the infinite Taylor jet at `s=1` of the **completed** logarithmic derivative, after the explicit rational prefactor. This is a prior-art redirect for the prime-lattice program: taking moments of the Suzuki/weighted-Chebyshev axis discrepancy and asking for Hankel positivity does not produce a new lattice mechanism; it lands in an existing RH-equivalent criterion closely related to the Keiper–Li coefficients.

There is also a sharper derived obstruction to reading those moments as a positive measure built term-by-term from prime-power lattice rays. For a single von-Mangoldt event `q=p^k`, write `lambda=log q`. Its contribution to Suzuki’s explicit formula for `Psi` is

`- Lambda(q)/sqrt(q) * (t-lambda) * 1_(t>=lambda)`.

If this one term is pushed through the moment transform, its formal contribution is

`- Lambda(q)/q * P_m(log q)`,

where

`P_m(x) = sum_(j=0)^m binom(m,j) 2^j (j+1)! x^(m-j)`.

However, the sum over prime powers of these contributions diverges already for `m=0`, because it contains `-sum_q Lambda(q)/q`. Simultaneously, the leading term `4 exp(t/2)` in `Psi` has a divergent moment after multiplication by `(1/4)exp(-t/2)`. The finite `mu_m` therefore exist only after the **global cancellation of these separately divergent pieces** (with the remaining completion terms contributing finite corrections). The canonical Suzuki moment sequence is not obtained by an absolutely convergent prime-ray moment measure at the critical boundary.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`. Suzuki’s RH-equivalent Hankel criterion, the moment definition, determinacy argument, the completed-jet identity, and the relation with Li coefficients are peer-reviewed literature. The polynomial `P_m` and the termwise-divergence audit are exact elementary consequences of Suzuki’s displayed explicit formula. No new RH criterion or proof is claimed.

## Exact relation to the exponent lattice

Suzuki’s arithmetic forcing is supported by `Lambda(q)`, hence only by prime powers `q=p^k`. In exponent coordinates,

`v(q)=k e_p`,

`E(v(q))=<v(q),(log r)_r>=k log p=log q`,

and the critical explicit-formula amplitude is

`Lambda(q)/sqrt(q) = log(p) exp(-E(v(q))/2)`.

The moment transform contributes another factor `exp(-t/2)`. At the event threshold `t=E(v(q))`, this changes the critical half-weight into the borderline arithmetic scale

`exp(-E(v(q))/2) exp(-E(v(q))/2) = exp(-E(v(q))) = 1/q`.

More precisely,

`I_m(lambda) = integral_lambda^infinity exp(-t/2)(t-lambda)t^m dt`.

Writing `t=lambda+u` gives

`I_m(lambda) = exp(-lambda/2) sum_(j=0)^m binom(m,j) lambda^(m-j) integral_0^infinity exp(-u/2)u^(j+1)du`

`= exp(-lambda/2) sum_(j=0)^m binom(m,j) lambda^(m-j)(j+1)! 2^(j+2)`.

Multiplication by the outer factor `1/4` and by `-Lambda(q)/sqrt(q)` yields exactly

`-Lambda(q)/q P_m(log q)`.

Every coefficient of `P_m` is positive. Hence this is not a conditionally convergent oscillatory prime sum whose ordering might rescue the interpretation: the separate arithmetic contribution has one sign and diverges in magnitude. Already

`P_0(x)=1`

produces `-sum_q Lambda(q)/q`, which diverges. For higher `m`, `P_m(x)>=x^m` for `x>=0`, so the obstruction persists.

This is a useful boundary fact. `PL-147` showed that an RH-equivalent scalar criterion can live entirely on the prime-power axis skeleton. The present finding shows that the most obvious attempt to turn that scalar criterion into a positive Hankel geometry cannot assign finite moments independently to those rays at the critical weight. The required finite moment data is a renormalized/completed scalar object.

## Suzuki’s existing Hankel/Stieltjes mechanism

Suzuki defines the real continuous function `Psi(t)` from the explicit formula and proves

`RH <=> Psi(t)>=0 for every real t`.

He then introduces

`mu_m=(1/4) integral_0^infinity exp(-t/2) Psi(t)t^m dt`.

The integral is absolutely convergent because his unconditional estimate gives sufficient decay after the `exp(-t/2)` weight. If RH holds, the density

`(1/4) exp(-t/2) Psi(t) dt`

is a positive measure on `[0,infinity)`, so `(mu_m)` is a Stieltjes moment sequence and both Hankel towers are positive semidefinite. Conversely, positivity of all the Hankel determinants gives some Stieltjes representing measure. Suzuki invokes determinacy of this moment problem, using the decay of the actual density, to identify that representing measure with `(1/4)exp(-t/2)Psi(t)dt`. Hence `Psi>=0`, and his pointwise criterion yields RH.

This distinction matters for the lattice interpretation. Under RH the positive Stieltjes measure is a **continuous measure in the scalar time/energy variable `t`**. It is not the counting measure of the prime-power sites `k e_p`, nor a sum of positive atoms at `log(p^k)`. The prime-power lattice enters through the piecewise-linear forcing inside `Psi`; positivity belongs only to the globally assembled scalar density.

Suzuki further proves

`mu_m = [d^m/dX^m ((1-2X)^(-2)(xi'/xi)(1-X))]_(X=0)`.

Therefore the Hankel matrices can be reconstructed without retaining the prime decomposition at all: they are determined by the infinite completed jet at the single regular point `s=1`. Section 8 of the same paper gives explicit invertible relations between `(mu_m)` and the Keiper–Li coefficients. The Hankel criterion is consequently not a new multidimensional Fourier dual of the exponent lattice; it is another exact scalar encoding of completed zeta data.

## Why the termwise prime decomposition is illegitimate at the boundary

Suzuki’s explicit formula contains, for `t>=0`, the arithmetic term

`- sum_(q<=exp(t)) Lambda(q)/sqrt(q) (t-log q)`

together with the elementary main term `4(exp(t/2)+exp(-t/2)-2)` and the archimedean gamma/Hurwitz–Lerch completion terms. For each fixed `t` the prime-power sum is finite, so this formula is perfectly legitimate.

The problem appears only if one tries to interchange the infinite prime-power decomposition with the moment integral over `0<t<infinity`. The separate prime-power moments are the divergent series derived above. The leading `4 exp(t/2)` term is equally nonintegrable after the moment weight, since

`(1/4)exp(-t/2) * 4 exp(t/2) * t^m = t^m`.

Thus neither piece has a finite moment by itself. The convergence of `mu_m` is a cancellation statement across the globally assembled explicit formula before the infinite integration is performed. The archimedean terms are part of the completed `xi'/xi` identity and contribute finite corrections here, but they are not what makes the two displayed divergent pieces individually integrable.

Equivalently, the derivative formula at `s=1` should be treated as the safe continuation-sensitive representation. It is a formula for the completed logarithmic derivative at a regular point, not the result of substituting `s=1` into the absolutely convergent Dirichlet series

`-zeta'(s)/zeta(s)=sum_n Lambda(n)n^(-s)`,

which is valid only for `Re(s)>1`. The pole at `s=1` is precisely the reason the raw `Lambda(n)/n` moments cannot be used termwise.

## Prior-art and novelty audit

Primary source:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`, first published 4 July 2023; arXiv `2206.03682`. Theorem 1.7 is the pointwise criterion `RH <=> Psi>=0`. Equation (1.13) defines the moments. Theorem 1.8 is the two-Hankel-tower criterion. Equation (1.15) identifies the moments with derivatives of the completed logarithmic derivative, and Theorem 8.1 gives their explicit invertible relation with Li coefficients. The proof of Theorem 1.8 supplies the Stieltjes-moment and determinacy argument.

The current literature check did not identify a later theorem that turns these Suzuki moments into an independent positive prime-power-atom measure or a multidimensional prime-exponent geometry. The relevant published mechanism is already Suzuki’s scalar Stieltjes problem, while the termwise axis formula above fails before one reaches such a measure because of the `Lambda(q)/q` divergence.

The polynomial expression `P_m` is not claimed as deep novelty. It is stored because it gives a falsifiable line-level obstruction: the exact prime-ray decomposition that one would naturally inherit from `PL-146`/`PL-147` cannot be inserted term-by-term into Suzuki’s Hankel moments. Any future “prime-lattice moment matrix” claim must specify a legitimate renormalization or a different summability mechanism rather than silently interchanging these divergent operations.

## Adversarial boundaries and falsification

1. **This is not an RH proof.** Suzuki’s Hankel positivity is an equivalent condition. Proving all determinants nonnegative remains exactly as difficult as proving RH.

2. **The critical exponent is not derived.** The amplitude `q^(-1/2)` and the moment weight `exp(-t/2)` are already built into Suzuki’s construction. Their product exposes the borderline `1/q` divergence; it does not explain from bare lattice geometry why `1/2` must be the critical line.

3. **Do not replace the completed jet by the Euler product at `s=1`.** The Dirichlet series for `-zeta'/zeta` is only absolutely convergent for `Re(s)>1`. The finite `mu_m` use the completed analytic object after the pole/main-term cancellation.

4. **Hankel positivity does not recover mixed-support exponent vectors.** All arithmetic input in `Psi` is on `k e_p`, then projected to `log(p^k)`, then integrated to a scalar sequence `(mu_m)`. The full lattice geometry has disappeared before the Hankel matrix is formed.

5. **The Stieltjes measure is not a prime counting measure.** Under RH it has density `(1/4)exp(-t/2)Psi(t)` with respect to `dt`. The prime powers determine kinks/slopes in `Psi`; they are not positive atoms of the representing measure.

6. **Finite Hankel truncations are not certificates of RH.** Any finite collection of determinants uses only finitely many moments/derivatives. Suzuki’s equivalence requires the entire infinite tower together with the determinate moment problem.

7. **The divergence only blocks the canonical termwise interpretation.** It does not rule out every possible regularized prime-lattice moment construction. A new proposal could survive if it states a mathematically controlled renormalization and proves that the resulting positivity is not merely another restatement of completed `xi` data.

A falsification of the stored exact obstruction would require either an error in the one-event integral producing `P_m`, or convergence of `sum_q Lambda(q)/q` despite the standard pole of `-zeta'/zeta` at `s=1`. Neither is compatible with the classical zeta theory used in Suzuki’s derivation.

## Consequence for the research line

Do not spend further passes trying to obtain RH by simply taking polynomial moments of Suzuki’s weighted prime-power-axis discrepancy and testing the resulting Hankel matrices for positivity. That construction is already present, in completed form, in Suzuki 2023.

More importantly, a future lattice interpretation must not pretend that Suzuki’s Hankel matrix is the Gram/moment matrix of independently positive prime-ray atoms. At the critical weight those raw moments diverge. The cancellation that makes the moments finite is global and continuation-sensitive, and the resulting data can be compressed to the completed `s=1` jet.

A genuinely new mechanism would therefore need at least one ingredient absent from this scalar reduction: a controlled renormalization whose positivity follows from arithmetic structure rather than from assuming the completed `Psi` positivity, an operator coupling that retains more than the energy projection `v -> <v,log p>`, or a rigidity principle that explains the critical half-weight instead of inserting it. Otherwise the proposed “Hankel geometry of the prime lattice” is prior-art repackaging of Suzuki’s criterion.