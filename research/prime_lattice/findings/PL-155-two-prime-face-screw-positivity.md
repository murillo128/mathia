# PL-155 — Any two-prime exponent face already tests Suzuki screw positivity

## Claim

Let `Psi` be Masatoshi Suzuki's completed real even function associated with the Riemann zeta function, normalized by `Psi(0)=0`, and put `g=-Psi`. Its anchored screw/Schoenberg kernel is

`K(t,u)=Psi(t)+Psi(u)-Psi(t-u)`.

Suzuki proves that the Riemann hypothesis is equivalent to positive semidefiniteness of this kernel on the whole real line. In prime-exponent coordinates that global test can be reduced much further than the full lattice suggests.

Fix **any two distinct rational primes** `p!=q` and define

`S_(p,q)={m log p+n log q : m,n in N_0}`.

This is exactly the energy image of the two-dimensional exponent face

`{m e_p+n e_q : m,n in N_0}`.

Then

`RH <=> K is positive semidefinite on S_(p,q) x S_(p,q)`.

Equivalently, for one fixed pair such as `p=2`, `q=3`, it is enough that every finite matrix

`K_(i,j)=Psi((m_i log 2+n_i log 3))
          +Psi((m_j log 2+n_j log 3))
          -Psi(((m_i-m_j)log 2+(n_i-n_j)log 3))`

be positive semidefinite for nonnegative integer pairs `(m_i,n_i)`.

The proof is exact and short. Positivity on the positive two-generator semigroup implies conditional negative definiteness of `Psi` on its difference group. That difference group is `Z log p+Z log q`, which is dense in `R` because `log p/log q` is irrational. Continuity then upgrades the negative-type inequality to all real points, recovering Suzuki's full screw condition and hence RH.

The result is therefore primarily a **structural reduction and negative diagnostic** for the prime-lattice program. In this completed screw channel, infinite-dimensional prime-exponent geometry is not needed even as a sampling set: a fixed two-prime face already detects the full RH-equivalent positivity. The reduction is not an arithmetic explanation of RH, because the completed function `Psi` already contains the entire rational-prime and archimedean data. The two-prime face supplies only a dense difference set on which to test a translation-invariant positivity property.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + STRUCTURAL-REDUCTION + NEGATIVE/OBSTRUCTION`. Suzuki's screw criterion is peer-reviewed literature. The Schoenberg conditional-negative-definite reformulation is classical. The two-prime reduction is an elementary exact consequence of translation invariance, group completion, unique factorization, and continuity. A targeted literature search did not locate this exact zeta-specific two-prime restriction, but no novelty claim is made: the mechanism is a generic dense-subgroup principle once Suzuki's completed function is supplied.

## From Suzuki's screw criterion to an exponent-face kernel

Suzuki defines the screw kernel of `g` by

`G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)`.

For the completed zeta function used here, `g=-Psi`, `Psi` is real and even, and `Psi(0)=0`. Hence

`G_g(t,u)=Psi(t)+Psi(u)-Psi(t-u)=K(t,u)`.

Suzuki's Theorem 1.2 gives

`RH <=> g is a screw function on R`

and therefore

`RH <=> K is positive semidefinite on R x R`.

This is the same completed positivity structure already identified in `PL-144` as the Schoenberg image of conditional negative definiteness of `Psi`. The present result does not introduce another positivity avatar. It asks how small a prime-exponent sampling set still determines that already-established global condition.

For integers of the form

`N=p^m q^n`,

the exponent vector is

`v(N)=m e_p+n e_q`

and its canonical lattice energy is

`E(v(N))=m log p+n log q`.

Thus `S_(p,q)` is not an externally chosen set of real sampling times: it is exactly the energy projection of a fixed two-coordinate face of the positive exponent cone.

## Positive-semigroup kernel positivity gives negative type on the difference group

Assume `K` is positive semidefinite on `S=S_(p,q)`. Take finitely many `x_1,...,x_N` in `S` and complex coefficients `c_1,...,c_N` satisfying

`sum_i c_i=0`.

Since the kernel matrix is positive semidefinite,

`0 <= sum_(i,j) c_i conjugate(c_j) K(x_i,x_j)`.

Substitute

`K(x_i,x_j)=Psi(x_i)+Psi(x_j)-Psi(x_i-x_j)`.

The first two contributions vanish because the coefficients have zero sum, leaving

`sum_(i,j) c_i conjugate(c_j) Psi(x_i-x_j) <= 0`.

Hence `Psi` is conditionally negative definite for all finite configurations whose points lie in the positive semigroup `S`.

Now form the additive group completion

`H=S-S=Z log p+Z log q`.

Let `y_1,...,y_N` be arbitrary points of `H`. Choose integer representations

`y_i=a_i log p+b_i log q`,  `a_i,b_i in Z`.

There are common integers `A,B>=0` large enough that

`x_i=y_i+A log p+B log q`

belongs to `S` for every `i`. Translation does not alter pairwise differences:

`x_i-x_j=y_i-y_j`.

Applying the preceding inequality to the translated points therefore gives

`sum_(i,j) c_i conjugate(c_j) Psi(y_i-y_j) <= 0`

for every zero-sum coefficient family. Thus positivity of the anchored kernel on the **one-sided** exponent face already makes `Psi` conditionally negative definite on its entire group completion `H`.

This step is the load-bearing reason that the nonnegative semigroup is enough even though it is not itself dense in `R`. Conditional negative definiteness depends only on differences, so the positive cone automatically exposes its signed group completion after a common translation.

## Two prime logarithms make the group completion dense

For distinct primes `p` and `q`, the ratio

`log p/log q`

is irrational. If it were `r/s` with positive integers `r,s`, then

`p^s=q^r`,

contradicting unique factorization. Therefore the additive subgroup

`H=Z log p+Z log q`

is dense in `R`, by the standard irrational-rotation/Kronecker argument.

Let now `t_1,...,t_N` be arbitrary real numbers and let `c_i` be any complex coefficients with `sum_i c_i=0`. Choose sequences `y_i^(k) in H` with

`y_i^(k) -> t_i`.

Suzuki's `Psi` is continuous, so

`Psi(y_i^(k)-y_j^(k)) -> Psi(t_i-t_j)`

for every pair. Passing to the limit in the finite conditional-negative-definite quadratic form yields

`sum_(i,j) c_i conjugate(c_j) Psi(t_i-t_j) <= 0`.

Thus `Psi` is conditionally negative definite on all of `R`.

For completeness, the anchored Schoenberg implication can be recovered directly without invoking an abstract theorem. Given arbitrary coefficients `d_1,...,d_N` at points `t_1,...,t_N`, add the base point `t_0=0` with coefficient

`d_0=-sum_(i=1)^N d_i`.

The conditional-negative-type inequality for this zero-sum family rearranges exactly to

`sum_(i,j=1)^N d_i conjugate(d_j)
 [Psi(t_i)+Psi(t_j)-Psi(t_i-t_j)] >= 0`.

Hence `K` is positive semidefinite on `R`, and Suzuki's theorem gives RH. This proves the nontrivial implication. The converse is immediate by restriction of a globally positive semidefinite kernel to `S_(p,q)`.

## Prime-exponent meaning and the information actually being used

The criterion may be written entirely on the face

`{m e_p+n e_q : m,n>=0}`

of the exponent lattice. For the concrete pair `(2,3)`, the sampled integers are the `3`-smooth numbers

`2^m 3^n`,

but the kernel differences probe the dense signed energy module

`Z log 2+Z log 3`.

This is a striking dimensional collapse of the **sampling geometry**, not of the arithmetic content of `Psi`. Evaluating `Psi(m log 2+n log 3)` does not mean that only the primes `2` and `3` enter the completed zeta function. Suzuki's explicit formula for `Psi(t)` contains all prime-power events with `log(r^k)<=t`, together with the pole and archimedean completion terms. The full rational-prime system is already encoded in the scalar function being sampled.

Accordingly, this result cannot be used to argue that two primes somehow generate the zeta function or its zero divisor. What two multiplicatively independent lattice directions generate densely is only the **additive time group after taking differences**. Continuity and translation invariance then make that dense group a uniqueness set for the negative-type inequality.

The same observation explains why square-free geometry is not responsible for the reduction. The semigroup needs unbounded powers `p^m q^n`; restricting to the four square-free face points `{1,p,q,pq}` would give only a finite sampling set and no dense group completion.

## Generic matched control

The two-prime reduction is not specific to rational primes after the completed zeta function has been fixed. Let `psi:R->R` be any continuous even function with `psi(0)=0`, and let `a,b>0` satisfy `a/b` irrational. Set

`S={m a+n b:m,n in N_0}`

and

`K_psi(t,u)=psi(t)+psi(u)-psi(t-u)`.

Exactly the same proof gives

`K_psi PSD on S x S`

if and only if

`psi is conditionally negative definite on R`,

if and only if

`K_psi PSD on R x R`.

Thus the decisive sampling property is just rank-two irrational additive generation. Replacing `log p,log q` by generic incommensurable energies gives the same theorem. Rational-prime unique factorization supplies a canonical guarantee that every pair of distinct prime logarithms is incommensurable, but it does not supply the missing sign or positivity.

This generic control is the reason to classify the result partly as a negative obstruction. Any proposed interpretation of the restricted two-prime test as evidence that a low-dimensional prime-lattice geometry forces RH would fail immediately on arbitrary continuous negative-type candidates sampled on an irrational two-generator semigroup.

## Analytic-continuation boundary

No Euler product is used or continued in this argument. The object being sampled is Suzuki's already completed function `Psi`, constructed from the analytically continued `xi`/explicit-formula machinery. The equivalence with RH is Suzuki's global screw theorem, not a statement obtained by evaluating an Euler product on the critical line.

The only continuation-like step in the present derivation is **topological continuity on the real time variable**: a conditional-negative-type inequality known on the dense additive subgroup `Z log p+Z log q` passes to `R`. This has nothing to do with analytic continuation in `s` and cannot manufacture zeta information that was not already present in `Psi`.

This distinction is important for the line mandate. The theorem genuinely survives the critical-strip issue because it begins with a globally defined completed object, but that is also why the low-dimensional sampling reduction does not explain how the completion or the critical normalization arose.

## Prior-art and novelty audit

Primary zeta source:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487. DOI `10.1112/jlms.12785`; arXiv `2206.03682`. Theorem 1.2 proves `RH` if and only if `g=-Psi` is a screw function on `R`; equation (1.4) is the corresponding anchored kernel. The same paper supplies the global completed construction and continuity used above.

Classical structural inputs:

- **I. J. Schoenberg**, “Metric spaces and positive definite functions,” *Transactions of the American Mathematical Society* **44** (1938), 522–536. This is classical background for the equivalence between negative-type functions and positive-definite exponential/anchored-kernel constructions. The precise screw-to-Schoenberg identification for Suzuki's `Psi` is already recorded in `PL-144`.
- Density of `Z a+Z b` for irrational `a/b` is the elementary rank-two Kronecker/irrational-rotation theorem. Here irrationality of `log p/log q` follows immediately from unique factorization.

A targeted search around Suzuki's screw function, dense subgroups, pairs of prime logarithms, and restrictions to `{2^m3^n}` did not locate a published statement of this exact zeta-specific reduction. Generic harmonic-analysis literature contains the expected dense-subgroup principle for continuous positive/negative-definite functions. That is enough to prevent a novelty claim based on the reduction's wording. The durable value here is its consequence for the research line: **the RH-equivalent completed screw positivity does not intrinsically require an infinite-dimensional prime-lattice test domain.**

This finding sharpens `PL-144` rather than duplicating it. `PL-144` proves that the completed screw, Schoenberg, and Lévy positivity avatars collapse to the same RH-equivalent scalar structure. The present result identifies a further collapse of the domain on which that structure must be tested: one fixed two-prime exponent face is already determining.

## Adversarial boundaries

1. **The result does not prove RH.** It replaces one global positivity test by an equivalent discrete positivity test. Establishing the restricted kernel matrices are positive semidefinite remains RH-equivalent.

2. **The positive semigroup is not dense.** The proof does not claim that `{m log p+n log q:m,n>=0}` is dense in `R` or in `R_+`. Density appears only after passing to the difference group `Z log p+Z log q`; translation invariance of the conditional-negative-type inequality is what makes that passage legitimate.

3. **Two primes are sufficient for this generic density argument, not proved necessary for every zeta-specific criterion.** A single generator gives only the discrete group `Z log p`, so this proof cannot reduce further to one prime. That does not exclude some different analytic theorem making a one-prime sampling sequence RH-equivalent for special reasons.

4. **The arithmetic content of `Psi` is still global.** Sampling on the `(p,q)` face does not truncate Suzuki's prime-power sum to those two axes. Any claim that the result makes all other primes irrelevant would confuse the test set with the data encoded in the tested function.

5. **Unbounded exponents are essential to the argument.** A finite or square-free two-coordinate face has no dense difference completion and does not support the proof.

6. **Continuity is load-bearing.** Without continuity, negative type on a dense subgroup need not determine the function on all real points. Suzuki's completed function has the required continuity.

7. **The reduction is generic after completion.** Any continuous even candidate on `R` is subject to the same two-incommensurable-generator sampling principle. The theorem therefore does not discriminate rational primes from matched irrational-frequency controls except for the canonical source of incommensurability.

A falsification would require an error in Suzuki's RH/screw equivalence, failure of the algebra converting anchored kernel positivity to conditional negative type, failure to translate arbitrary finite configurations in `H` into the positive semigroup, rational dependence of two distinct prime logarithms, or discontinuity of `Psi`. None is compatible with the stated inputs.

## Consequence for the research line

Do not treat the infinite-dimensionality of the exponent lattice, or the need to test all prime coordinates simultaneously, as an essential ingredient of Suzuki's completed screw/negative-type criterion. **For that channel, any fixed pair of prime axes is already a complete test set once the full completed zeta function has been constructed.**

This makes the remaining burden more precise. A genuinely new full-lattice mechanism must inject information *before* the completed scalar function has collapsed the arithmetic to a translation-invariant one-variable kernel, or must constrain `Psi` in a way not obtainable from generic dense-subgroup sampling. Mixed-prime geometry remains potentially useful only if it proves the missing positivity/sign from arithmetic structure; it cannot be justified merely by claiming that the completed screw condition itself needs the whole exponent lattice as its test domain.