# PL-142 — The zeta Hardy kernel fails complete Pick positivity on the first two-prime face

## Claim

The canonical Hedenmalm–Lindqvist–Seip coefficient Hilbert space has reproducing kernel

`K(s,u)=zeta(s+conj(u))`

on `Re(s),Re(u)>1/2`. This kernel is **not** a complete Nevanlinna–Pick kernel. The obstruction is already visible on the first genuinely two-prime square-free face of the exponent lattice and requires no analytic continuation:

`1/zeta(w)=sum_(n>=1) mu(n)n^(-w)`

for `Re(w)>1`, so the reciprocal-kernel Dirichlet coefficient at `n=pq` for distinct primes `p,q` is

`mu(pq)=+1`.

McCarthy–Shalit's complete-Pick criterion for Dirichlet-series kernels requires every reciprocal coefficient after the constant term to be nonpositive. Hence the standard zeta kernel fails the criterion as soon as two independent prime directions are present.

The failure does not undergo a special transition at `Re(s)=1/2`: every ordinary coefficient damping/translation of this kernel has the same sign obstruction. Conversely, the canonical complete-Pick Dirichlet kernels constructed by pulling back Drury–Arveson geometry replace zeta's coefficient `1` at each lattice point by multinomial path-counting weights. For prime generators their multiplier geometry is universal for any sequence with Q-linearly independent logarithms, rather than specific to the rational-prime norm map.

Therefore the route

`native Bohr-Hardy zeta kernel -> complete-Pick interpolation positivity -> RH localization`

is decisively blocked. Complete-Pick geometry remains available only after changing the coefficient geometry or adding external structure; it is not an intrinsic positivity mechanism of the standard zeta/prime-exponent Hardy kernel.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT` for the specifically stated native complete-Pick/interpolation route. McCarthy–Shalit's characterization and Drury–Arveson realization are literature. The specialization to the HLS zeta kernel and the two-prime Möbius sign obstruction are immediate exact consequences. No novelty is claimed for complete Pick theory, the zeta kernel, Möbius inversion, or the Drury–Arveson construction.

## Exact reciprocal-coefficient obstruction

McCarthy and Shalit consider kernels of the form

`k(s,u)=sum_(n>=1) a_n n^(-s-conj(u))`,

with `a_1=1`, on a half-plane where the series converges. Write the reciprocal Dirichlet series at infinity as

`1/(sum_(n>=1) a_n n^(-w)) = sum_(n>=1) c_n n^(-w)`.

Their Theorem 26 states that the corresponding Hilbert function space has the complete Pick property if and only if

`c_n <= 0` for every `n>=2`.

For the standard HLS space,

`a_n=1`

and therefore, in the honest absolute-convergence half-plane `Re(w)>1`,

`sum_(n>=1) a_n n^(-w)=zeta(w)`,

`1/zeta(w)=sum_(n>=1) mu(n)n^(-w)`.

Thus `c_n=mu(n)`. At a prime `p`, `c_p=-1`, which has the allowed sign. At the first product of two distinct prime directions,

`c_(pq)=mu(pq)=+1`,

which violates the necessary and sufficient condition. In particular `c_6=+1` is already a complete obstruction.

Nothing here uses the meromorphic continuation of `zeta`. Since `s,u` are in the HLS evaluation half-plane, `Re(s+conj(u))>1`, and the reciprocal Dirichlet series is being used exactly where its Euler/Dirichlet expansion converges absolutely.

## Prime-lattice meaning of the sign failure

Under the Bohr lift, the same kernel is

`K(z,w)=product_p (1-z_p conj(w_p))^(-1)`

on its natural Hilbert-domain slice. A single prime coordinate gives the one-variable Szego kernel and has complete Pick geometry. The obstruction appears when two independent coordinates are multiplied together.

Indeed,

`1 - 1/K(z,w)`

has square-free coefficients `-mu(n)`. It is positive on a one-prime monomial but changes sign on the two-prime monomial `z_p z_q conj(w_p w_q)`. The complete Pick condition therefore detects a concrete difference between one-axis Hardy geometry and the multiplicative product of two or more prime axes: the product kernel is not itself complete Pick.

This is an algebraic Boolean-face obstruction, not a subtle critical-strip phenomenon. It is also not specific to the sizes of `p` and `q`; only the existence of two multiplicatively independent supported directions is needed. Hence it cannot encode the placement of the Riemann zero divisor.

## No critical transition from coefficient damping

A natural attempt after `PL-001` is to ask whether the complete-Pick property might appear or disappear at the same half-boundary as bounded point evaluation. It does not.

For a coefficient-damped translate

`K_eta(s,u)=sum_(n>=1) n^(-2 eta) n^(-s-conj(u))`

in any half-plane where the defining Dirichlet series converges, the scalar Dirichlet generating function is

`zeta(2 eta+w)`.

Its reciprocal coefficients are

`c_n=mu(n)n^(-2 eta)`.

For every distinct pair of primes,

`c_(pq)=(pq)^(-2 eta)>0`.

Thus ordinary radial damping can move the convergence/evaluation boundary but never repairs complete-Pick positivity. There is no `eta=1/2` transition hidden in this property.

This separates the present obstruction from `PL-001`: `Re(s)=1/2` is genuinely the natural evaluation boundary of the standard infinite-polydisk Hardy geometry, but complete-Pick positivity does not sharpen that boundary into an RH-sensitive condition.

## What a canonical complete-Pick repair changes

McCarthy–Shalit also construct Dirichlet-series complete Pick spaces by choosing positive weights `b_k` with `sum_k b_k^2=1`, a sequence of integers `n_k`, and the map

`f(s)=(b_k n_k^(-s))_k`.

Pulling back the Drury–Arveson kernel gives

`K_b(s,u)=1/(1-<f(s),f(u)>)`

`          =1/(1-sum_k b_k^2 n_k^(-s-conj(u)))`.

If the generators are the primes, expansion of the geometric series shows that the coefficient at

`n=product_p p^(v_p(n))`

is

`a_n = Omega(n)!/product_p(v_p(n)!) * product_p b_p^(2 v_p(n)).`

The factor

`Omega(n)!/product_p(v_p(n)!)`

counts ordered prime-step paths to the lattice point `v(n)`. This is fundamentally different from the zeta kernel, whose coefficient is exactly `1` for every integer lattice point. Enforcing complete Pick geometry has therefore changed the arithmetic Hilbert metric rather than discovered a hidden positivity of the native zeta metric.

The same paper's Theorem 41 makes the loss of prime specificity sharper. For these Drury–Arveson pullbacks, the multiplier closure is the full ball, and the space is weakly isomorphic to the corresponding Drury–Arveson space, exactly when

`log n_1, log n_2, ...`

are linearly independent over `Q`. The rational primes satisfy that condition by unique factorization, but so do many other multiplicatively independent integer sequences. Consequently the resulting complete-Pick multiplier geometry does not distinguish the exact rational-prime norm map, which is a required falsification control of this research line.

## Prior art and novelty audit

The principal source is:

- John E. McCarthy, Orr Moshe Shalit, “Spaces of Dirichlet series with the complete Pick property,” *Israel Journal of Mathematics* **220**(2) (2017), 509–530. DOI: https://doi.org/10.1007/s11856-017-1527-6. arXiv: https://arxiv.org/abs/1507.04162.

Theorem 26 supplies the exact reciprocal-coefficient characterization used above. Their Drury–Arveson pullback construction and Theorem 41 supply the universality comparison for Q-linearly independent logarithms. Modern work continues to study multiplier varieties and classification for complete-Pick Dirichlet kernels, so complete-Pick geometry is an established Dirichlet-series research program rather than a new prime-lattice construction.

The specialization `c_n=mu(n)` for the standard zeta kernel is immediate from the classical reciprocal identity and should not be treated as a novelty claim. The durable value for `prime_lattice` is the line-specific negative conclusion: the most canonical RKHS positivity/interpolation upgrade of `PL-001` already fails at the finite two-prime Boolean face, while the canonical repair changes the lattice weights and becomes universal under mere logarithmic independence.

Targeted searches for combinations of Riemann zeta, complete Pick kernels, Dirichlet-series Hardy spaces, and the Möbius reciprocal criterion found the general classification and later complete-Pick multiplier literature, but no theorem in which the standard HLS zeta kernel acquires an RH-sensitive complete-Pick transition. Absence of such a theorem is not used as evidence; the negative conclusion follows from the exact coefficient sign calculation.

## Boundary conditions and adversarial controls

This result does **not** say that complete-Pick spaces of Dirichlet series are impossible or irrelevant. McCarthy–Shalit explicitly construct large families of them, including universal Drury–Arveson pullbacks. It also does not rule out an equivalent renorming, a target-relative kernel, a de Branges/canonical-system construction, or another RKHS in which complete-Pick structure is introduced together with genuinely global arithmetic data.

What is ruled out is narrower and exact: the standard HLS/zeta reproducing kernel, and its simple coefficient-damped translates, do not possess complete-Pick positivity. Any proposed repair must say what new weights or global structure were introduced and then show independently why those data retain the Riemann zero divisor rather than merely produce a convenient interpolation space.

The Beurling/Helson controls are especially important. The two-prime sign obstruction is local and generic; it does not know whether the coordinate frequencies are the rational prime logarithms or another multiplicatively independent system. On the repair side, Theorem 41 likewise identifies Q-linear independence of the logarithms as sufficient for the full Drury–Arveson multiplier geometry. Neither side supplies the rational-prime-specific global coupling required by the line mandate.

Nor does failure of complete Pick imply failure of ordinary Hardy-space methods. `PL-017`--`PL-020` use a different Mellin/Nyman Hilbert geometry whose RH content comes through analytic continuation and a distinguished target/closed-span problem. `PL-021` separately shows that native Bohr cyclicity of the Möbius vector is unconditional wherever that vector lies in `H^2`. The present result closes a different escape: replacing cyclicity by the stronger interpolation positivity of the **native reproducing kernel** still does not produce zero localization.

## Decisive audit test

Any future proposal that uses complete-Pick or Nevanlinna–Pick positivity on the prime-exponent Hardy space as the missing RH mechanism should first answer both of the following exact tests.

First, compute the reciprocal Dirichlet coefficients of its kernel. If the kernel still has zeta coefficients `a_n=1`, then the coefficient at every square-free two-prime point is `+1` in `1/zeta`, and complete Pick fails immediately.

Second, if the kernel is modified so those coefficients become nonpositive, compute the new lattice weights and compare the resulting multiplier geometry with McCarthy–Shalit's Drury–Arveson models. If the construction depends only on Q-linear independence of the logarithmic generators, it has not passed the rational-prime matched control and cannot by itself be an RH-localization mechanism.

## Consequence for `prime_lattice`

Do not pursue native complete-Pick interpolation positivity as an upgrade of the `Re(s)=1/2` Bohr-Hardy boundary. Its obstruction is finite, algebraic, and independent of the critical line.

A viable RKHS route must instead add a structure that is simultaneously sensitive to analytic continuation and to the exact rational-prime global norm map: for example a target-relative Mellin/Nyman geometry, an adelic/Fourier duality, a Weil-type positivity form, or another mechanism whose arithmetic content survives the Helson/Beurling matched controls. Merely replacing the standard product Hardy kernel by a complete-Pick kernel trades the zeta coefficient geometry for universal interpolation geometry and does not address RH.