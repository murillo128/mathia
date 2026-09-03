# PL-131 — Any accumulating critical-line reflection-phase data uniquely identifies a Grosswald–Schnitzer deformation

## Claim

`PL-130` proves a strong finite-data obstruction: in the original Grosswald–Schnitzer class with real generators `p_n <= q_n <= p_(n+1)`, every finite collection of natural critical-line phase jets and phase samples has exact local aliases. The complementary infinite-data boundary is unexpectedly rigid.

For an admissible real sequence `q=(q_n)`, let

`phi_q(s)=prod_n (1-p_n^(-s))/(1-q_n^(-s))`,

which Grosswald–Schnitzer prove is analytic and nonvanishing for `Re(s)>0`, and define its reflection cocycle in the critical strip by

`R_q(s)=phi_q(s)/phi_q(1-s)`.

Let `q` and `r` be two admissible real Grosswald–Schnitzer sequences. If

`R_q(1/2+i t)=R_r(1/2+i t)`

for `t` in **any set having a finite accumulation point**, then

`q_n=r_n` for every `n`.

Equivalently, the normalized critical-line reflection phase determines the whole Grosswald–Schnitzer generator sequence from any nontrivial phase arc, and even from a countable exact sample set accumulating at one finite height. In particular, equality of the complete Taylor jet at one critical-line point also suffices whenever it is interpreted as equality of the corresponding analytic germs.

**Evidence/status:** `EXACT-DERIVED + POSITIVE-DISCRIMINATOR + FINITE/INFINITE-BOUNDARY`.

The proof has three ingredients. Equality of the reflection cocycles forces the quotient `psi=phi_q/phi_r` to satisfy `psi(s)=psi(1-s)` in the strip. That relation glues the initially right-half-plane quotient to a zero-free entire function. The Grosswald–Schnitzer prime-gap restriction supplies a global exponential-type bound on this glued function, so classical Hadamard factorization reduces it to `exp(a s+b)`; reflection forces `a=0`, and Euler-product normalization at `+infinity` forces the constant to be one. Equality `phi_q=phi_r` then recovers the ordered generator sequence by the first differing frequency.

This does **not** resolve the accepted finite-integer phase-fingerprint clue. It instead gives a sharp information boundary around `PL-130`: finite phase data are non-identifying in the real deformation class, while any exact accumulating phase data are globally identifying. The unresolved corner is whether arithmetic discreteness makes some genuinely finite fingerprint injective for **integer** generators.

## Step 1: reflection equality makes the quotient symmetric in the strip

Put

`psi(s)=phi_q(s)/phi_r(s)`.

Both factors are analytic and nonzero in `Re(s)>0`, so the same is true of `psi`. On `0<Re(s)<1`,

`R_q(s)/R_r(s)=psi(s)/psi(1-s)`.

Suppose the two critical-line cocycles agree on a set `E` whose heights have a finite accumulation point. Then the analytic function

`F(s)=psi(s)-psi(1-s)`

vanishes at the points `s=1/2+i t`, `t in E`, with an accumulation point inside the open strip. The identity theorem therefore gives

`psi(s)=psi(1-s)`

throughout `0<Re(s)<1`.

No Euler product has been continued term by term into the strip here. The functions `phi_q` and `phi_r` are the nonvanishing analytic quotients supplied by the Grosswald–Schnitzer continuation theorem; the identity theorem is applied only after those quotients exist there.

On the critical line, real generators imply `phi_q(1/2-it)=conj(phi_q(1/2+it))`, so every `R_q` has unit modulus. Thus the statement can be phrased purely in terms of the continuous phase `R_q(1/2+it)=exp(i theta_q(t))`: equality of the normalized phases on an accumulating set gives equality of `R_q` there. As in `PL-127`, critical-line modulus alone remains completely blind because it is identically one.

## Step 2: the strip symmetry glues `psi` to an entire zero-free function

The symmetry relation is stronger than a boundary identity. Keep the original `psi(s)` on `Re(s)>0`, and on `Re(s)<1` define

`psi_ext(s)=psi(1-s)`,

where the right-hand side is evaluated in the original right half-plane because `Re(1-s)>0`. On the overlap `0<Re(s)<1`, Step 1 says that the two definitions agree. They therefore glue to one analytic function on

`{Re(s)>0} union {Re(s)<1}=C`.

The extension is zero-free because both local definitions are zero-free. Hence reflection-phase equality has automatically promoted the relative Grosswald–Schnitzer quotient from a half-plane function to a zero-free entire function.

This promotion alone is not enough for rigidity: there are many nonconstant zero-free entire functions satisfying `f(s)=f(1-s)`. The load-bearing extra input is the growth forced by the prime-gap deformation class.

## Step 3: the prime-gap condition gives exponential type

For fixed `s` with `Re(s)>0`, use the analytic branch

`h_s(x)=log(1-x^(-s))`,  `x>1`,

obtained from the absolutely convergent logarithmic series because `|x^(-s)|<1`. For `sigma=Re(s)>=1/2`, differentiation in the real variable `x` gives

`partial_x h_s(x)=s x^(-s-1)/(1-x^(-s))`.

Since `x>=2`,

`|partial_x h_s(x)|
 <= |s| x^(-sigma-1)/(1-x^(-sigma))
 <= C |s| x^(-3/2)`,

with the absolute constant `C=(1-2^(-1/2))^(-1)`.

Write `d_n=p_(n+1)-p_n`. The Grosswald–Schnitzer interval condition gives `0<=q_n-p_n<=d_n`, hence

`|h_s(p_n)-h_s(q_n)| <= C |s| d_n p_n^(-3/2)`.

The majorant is summable without any prime-number-theorem input. Bertrand's postulate gives `p_(n+1)<2p_n`; therefore

`d_n p_n^(-3/2)
 <= 2^(3/2) integral_(p_n)^(p_(n+1)) x^(-3/2) dx`.

Summing the adjacent intervals proves

`sum_n d_n p_n^(-3/2)<infinity`.

Consequently the canonical logarithm of every admissible quotient satisfies a global half-plane estimate

`|log phi_q(s)| <= C_0 |s|`,  `Re(s)>=1/2`,

with a constant independent of the particular admissible sequence. The same estimate holds for `phi_r`, so

`|psi(s)| <= exp(C_1 |s|)`,  `Re(s)>=1/2`.

For `Re(s)<=1/2`, the symmetry from Step 1 and the glued continuation give `psi(s)=psi(1-s)`, while `Re(1-s)>=1/2`. Hence

`|psi(s)| <= exp(C_2(1+|s|))`

on the whole plane. The entire zero-free function `psi` is therefore of exponential type, in particular of order at most one.

This estimate is where the standard Grosswald–Schnitzer prime-gap control is essential. Their theorem admits broader variants with weaker asymptotic restrictions on `q_n`; the argument above does not automatically extend to those variants unless a comparable summable displacement/growth bound is proved.

## Step 4: Hadamard rigidity collapses the relative quotient

A zero-free entire function of order at most one has, by the classical zero-free case of Hadamard factorization, the form

`psi(s)=exp(a s+b)`

for constants `a,b`.

The global reflection relation gives

`exp(a s+b)=exp(a(1-s)+b)`

for every `s`. Thus `exp(a(2s-1))=1` identically, which forces `a=0`. Hence `psi` is a nonzero constant.

The constant is fixed by the original Euler-product normalization. For positive real `sigma->infinity`, the estimate above can be sharpened using `d_n<p_n` from Bertrand:

`|log phi_q(sigma)|
 <= C sigma sum_n d_n p_n^(-sigma-1)
 <= C sigma sum_p p^(-sigma)
 <= C sigma (zeta(sigma)-1)
 ->0`.

Therefore `phi_q(sigma)->1` and likewise `phi_r(sigma)->1`, so

`psi(sigma)=phi_q(sigma)/phi_r(sigma)->1`.

The constant is one:

`phi_q(s)=phi_r(s)`  for all `Re(s)>0`.

The role of the normalization is real. Reflection cocycles are invariant under multiplying `phi` by a nonzero constant, so the phase data alone can determine the relative quotient only up to that scalar. The canonical Grosswald–Schnitzer normalization at `+infinity` removes exactly this gauge.

## Step 5: equality of the quotients recovers every generator

It remains to exclude the possibility that two different admissible generator sequences produce the same `phi`. Work on the positive real axis with `sigma>1`, where all Euler products converge absolutely. Since the prime numerators cancel,

`phi_q(sigma)/phi_r(sigma)
 = product_n (1-r_n^(-sigma))/(1-q_n^(-sigma))`.

Assume the sequences differ and let `j` be their first differing index. Without loss of generality let

`a=q_j<r_j=b`.

Because `b<=p_(j+1)`, strict inequality gives `a<p_(j+1)`. Expanding only in the safe half-plane `sigma>1`,

`log(1-b^(-sigma))-log(1-a^(-sigma))
 = a^(-sigma)(1+o(1))`.

Every later generator is at least `p_(j+1)`. The complete tail is bounded by

`O(sum_(m>=p_(j+1)) m^(-sigma))
 = O(p_(j+1)^(1-sigma)/(sigma-1))
 = o(a^(-sigma))`,

because `a/p_(j+1)<1`. Thus

`log(phi_q(sigma)/phi_r(sigma))=a^(-sigma)(1+o(1))`,

which cannot vanish identically. This contradicts `phi_q=phi_r`. The opposite ordering is identical with the sign reversed, so no first differing index exists and `q_n=r_n` for all `n`.

The last step is simply uniqueness of the first generalized-Dirichlet frequency, written explicitly so that duplicate endpoint generators or nonintegral `q_n` cause no hidden uniqueness assumption.

## Relation to PL-127, PL-129, and PL-130

The four findings now give a clean hierarchy of information in the Grosswald–Schnitzer matched-control class.

`PL-127` shows that one scalar derivative, the central phase slope, detects whether the entire deformation is zero and gives a scale-aware prefix certificate for integer generators. `PL-129` shows that this scalar has exact arbitrary-tail aliases even in the integer endpoint subclass. `PL-130` shows that **every finite** collection of natural phase jets/samples has exact local aliases for real generators. The present result shows that the obstruction does not persist to analytic-germ information: an accumulating exact set of phase values forces equality of the entire deformation.

Thus the real class exhibits a sharp qualitative transition:

`finite exact phase data -> non-identifying`,

whereas

`any exact accumulating phase data -> globally identifying`.

This is an injectivity statement, not a stability theorem. Analytic continuation from a short phase arc can be catastrophically ill-conditioned, and nothing here supplies a quantitative reconstruction bound from noisy or approximate data. The distinction is especially important for the active clue, whose target is a **finite, tail-uniform integer** fingerprint rather than an infinite exact analytic germ.

## Prior-art and novelty audit

No novelty is claimed for either external ingredient. Grosswald–Schnitzer's 1978 theorem supplies the nonvanishing quotient in `Re(s)>0` and the prime-gap deformation class; it was already audited in `PL-125`, `PL-127`, `PL-129`, and `PL-130`. Classical Hadamard factorization for zero-free entire functions of order at most one was already used as the rigidity engine in `PL-128`.

The additional content here is the exact bridge between those ingredients: equality of the **relative reflection phase only on an accumulating critical-line set** first forces a global symmetric entire continuation of `phi_q/phi_r`, while the prime-gap displacement estimate supplies the order-one growth needed to make that continuation rigid. Targeted searches around Grosswald–Schnitzer functional equations, critical-line phase/reflection data, boundary-phase uniqueness, and exponential-type quotients found the original deformation theorem and generic Hadamard/functional-equation rigidity, but no source stating this reflection-cocycle injectivity result. No broad novelty claim is attached to that absence; the result is classified as an exact derived boundary theorem for this research line.

Primary literature already audited by the preceding findings:

- Emil Grosswald, F. J. Schnitzer, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357.
- R. P. Boas, Jr., *Entire Functions*, Academic Press, 1954; classical Hadamard-factorization reference used in `PL-128`.

## Adversarial boundaries

Several stronger interpretations are false or unproved.

First, this does not say that finitely many phase samples identify an integer deformation. `PL-130` kills finite fingerprints for real generators, while the integer case remains genuinely discrete and open in the accepted clue.

Second, a discrete infinite sample set with no finite accumulation point is not covered. The identity theorem supplies the decisive bridge only when the equality set accumulates inside the strip. Additional growth/sampling theory would be needed for separated samples tending to infinity.

Third, exact equality is essential. No lower bound is proved for the distance between phase arcs generated by different sequences, and no noise-stable inverse theorem follows from analytic injectivity.

Fourth, the interval restriction `q_n<=p_(n+1)` is used quantitatively in the exponential-type estimate. A broader generalized-prime control may preserve the zero divisor while allowing a relative quotient of higher or uncontrolled order; Hadamard then leaves nontrivial symmetric zero-free gauges.

Fifth, this is not an RH mechanism. Every Grosswald–Schnitzer member already shares the zeta zero divisor in `Re(s)>0`. The reflection phase distinguishes the arithmetic generator system **despite** the common zeros; it does not constrain those zeros to `Re(s)=1/2`.

Finally, the theorem should not be read as evidence that an arbitrary spectral model has recovered the rational-prime lattice merely because it outputs some critical-line phase. The relevant discriminator is the exact Grosswald–Schnitzer reflection cocycle with its analytic continuation and normalization. A model that inserts this phase by definition has only re-encoded the arithmetic input.

## Consequence for the prime-lattice line

The Grosswald–Schnitzer control now has a precise information hierarchy. The zero divisor alone does not determine the prime lattice (`PL-125`). One scalar phase derivative does not locate individual defects against an arbitrary tail (`PL-129`). No finite natural phase fingerprint identifies real deformations (`PL-130`). But the analytic reflection phase is not intrinsically information-losing: any accumulating exact fragment of it determines the entire standard Grosswald–Schnitzer deformation (`PL-131`).

This narrows the active question rather than solving it. For the rational-prime lattice, the useful unresolved target is whether **integer discreteness collapses the required information from an analytic germ to a finite certificate**. A positive result would need a genuinely arithmetic separation argument; a negative result would need an exact integer vector collision. Smooth dimension counting is no longer relevant, while simply taking infinitely many samples is now known to be sufficient and therefore no longer a useful research target.

For RH, the larger target remains the one isolated by `PL-126` and `PL-128`: after arithmetic identity and global self-duality have been recovered, an independent positivity/unitarity/Hodge mechanism is still required to localize the already-distinguished zeta divisor on the self-dual axis.