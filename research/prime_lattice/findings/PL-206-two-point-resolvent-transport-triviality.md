# PL-206 — Two spectral parameters trivialize any fixed left resolvent transport

**Status:** negative result / structural collapse  
**Evidence class:** `EXACT-DERIVED + CLASSICAL-RESOLVENT-IDENTITY + DECISIVE-NEGATIVE` for spectral-parameter-independent exact left transport  
**Research line:** `prime_lattice`

## Claim

Let \(H_0,H_1\) be closed densely defined operators on one Hilbert space, and write

\[
R_j(z)=(H_j-z)^{-1}.
\]

Assume two distinct points \(z\neq w\) lie in \(\rho(H_0)\cap\rho(H_1)\). If one bounded operator \(A\) satisfies the same-parameter exact transport equations

\[
R_1(z)=A R_0(z),
\qquad
R_1(w)=A R_0(w),
\]

then necessarily

\[
\boxed{A=I}
\qquad\text{and}\qquad
\boxed{H_1=H_0}.
\]

Thus the fixed-parameter factorizations used in `PL-202`--`PL-205` cannot be promoted to a genuine resolvent-family covariance with one nontrivial spectral-parameter-independent prime edge, not even at two spectral points. In particular, the kernel-bearing/coisometric edge escape left open by `PL-205` disappears completely if the edge is required to represent the same prime operation at two points of the resolvent set.

More generally, suppose a bounded family \(A(z)\) satisfies

\[
R_1(z)=A(z)R_0(z)
\]

on a common resolvent domain. Then the first resolvent identity forces the transfer law

\[
\boxed{
A(z)-A(w)
=(z-w)R_1(z)\bigl(A(w)-I\bigr).
}
\]

Writing \(B(z)=A(z)-I\), this becomes

\[
\boxed{
B(z)=\bigl[I+(z-w)R_1(z)\bigr]B(w).
}
\]

The left factor is boundedly invertible, with inverse \(I+(w-z)R_1(w)\). Consequently kernel dimension, rank-type information, and membership of \(B(z)\) in any two-sided operator ideal such as \(S_q\) propagate across the resolvent parameter. A nontrivial exact resolvent transport therefore has to be an actual **operator-valued function of the spectral parameter**, or act by moving the spectral parameter itself; a fixed edge multiplier is impossible.

## 1. Two-point rigidity from Hilbert's resolvent identity

For either operator, the first resolvent identity is

\[
R_j(z)-R_j(w)
=(z-w)R_j(z)R_j(w).
\]

Using the assumed fixed transport at both points gives, on one hand,

\[
R_1(z)-R_1(w)
=A\bigl(R_0(z)-R_0(w)\bigr)
=(z-w)A R_0(z)R_0(w).
\]

On the other hand,

\[
R_1(z)-R_1(w)
=(z-w)R_1(z)R_1(w)
=(z-w)A R_0(z)A R_0(w).
\]

Since \(z\neq w\), subtraction yields

\[
A R_0(z)(I-A)R_0(w)=0.
\]

But \(A R_0(z)=R_1(z)\), and every resolvent is injective. Therefore

\[
(I-A)R_0(w)=0.
\]

The range of \(R_0(w)\) is \(\operatorname{Dom}H_0\), which is dense. Because \(A\) is bounded,

\[
A=I.
\]

Hence \(R_1(w)=R_0(w)\). Equality of one resolvent determines the underlying closed operator: both resolvents have the same range/domain, and inversion gives \(H_1-w=H_0-w\). Thus \(H_1=H_0\).

No self-adjointness, normality, compactness, Schatten hypothesis, prime commutation relation, or special spectral density is used. The only structural inputs are a genuine resolvent identity, dense domains, boundedness of the common left transport, and two distinct spectral parameters.

## 2. A parameter-dependent transfer obeys a forced propagation law

Now allow \(A\) to depend on the spectral parameter. Starting from

\[
R_1(z)=A(z)R_0(z),
\qquad
R_1(w)=A(w)R_0(w),
\]

expand the difference in two ways:

\[
\begin{aligned}
R_1(z)-R_1(w)
&=A(z)\bigl(R_0(z)-R_0(w)\bigr)
  +\bigl(A(z)-A(w)\bigr)R_0(w)\\
&=(z-w)R_1(z)R_0(w)
  +\bigl(A(z)-A(w)\bigr)R_0(w),
\end{aligned}
\]

while

\[
R_1(z)-R_1(w)
=(z-w)R_1(z)A(w)R_0(w).
\]

Therefore

\[
\Bigl(A(z)-A(w)
 -(z-w)R_1(z)(A(w)-I)\Bigr)R_0(w)=0.
\]

Since \(\operatorname{Ran}R_0(w)=\operatorname{Dom}H_0\) is dense and the operator in parentheses is bounded, it vanishes. This proves

\[
A(z)-A(w)
=(z-w)R_1(z)(A(w)-I).
\]

Equivalently,

\[
B(z)=L_1(z,w)B(w),
\qquad
L_1(z,w)=I+(z-w)R_1(z).
\]

The resolvent identity gives

\[
L_1(z,w)^{-1}=I+(w-z)R_1(w).
\]

Hence the defect \(B=A-I\) cannot change its basic ideal/range type arbitrarily with \(z\). For example,

\[
B(w)\in S_q\iff B(z)\in S_q
\]

for every Schatten class \(S_q\), including trace class. Likewise \(\ker B(z)=\ker B(w)\), and finite rank is preserved. These are ordinary consequences of the resolvent family, not arithmetic rigidity.

## 3. Why this matters for the prime-lattice resolvent branch

`PL-202` shows that at one fixed point, say \(z=i\), arbitrary bounded self-adjoint fiber data can be programmed by setting

\[
A_p(\alpha;i)
=R_{\alpha+e_p}(i)R_\alpha(i)^{-1}
\]

on the appropriate dense range, with a bounded extension in the exhibited construction. `PL-203` shows that even injective dense-range noninvertibility can be appended without restoring rigidity. `PL-205` then proves that exact bounded fiberwise covariance forces every edge range to be dense, eliminating cokernel and proper closed-range defects but leaving a kernel-bearing edge as a formal single-point possibility.

The present result separates **single-point factorization** from **resolvent-family transport**. If one insists that the same bounded prime edge \(A_p(\alpha)\) transport the resolvent at two distinct spectral parameters,

\[
R_{\alpha+e_p}(z)=A_p(\alpha)R_\alpha(z),
\qquad
R_{\alpha+e_p}(w)=A_p(\alpha)R_\alpha(w),
\]

then

\[
A_p(\alpha)=I,
\qquad
H_{\alpha+e_p}=H_\alpha.
\]

So a nontrivial kernel, coisometric defect, domain defect encoded only in a fixed bounded left edge, or any other nonidentity fixed edge is ruled out before one reaches trace ideals or spectral-shift theory.

This also clarifies the canonical logarithmic translation. If

\[
H_1=H_0+cI,
\]

then the natural relation is a **parameter shift**

\[
R_1(z)=R_0(z-c),
\]

not a nontrivial fixed left multiplier at the same \(z\). If one insists on same-parameter factorization, the transfer is necessarily \(z\)-dependent:

\[
R_1(z)=A_c(z)R_0(z),
\qquad
A_c(z)=I-cR_1(z).
\]

For the prime-energy shift \(c=\log p\), this is exactly the structural form expected from the logarithmic Hamiltonian: the prime acts on the spectral parameter or through a resolvent-dependent transfer function. The `log p` datum is therefore incompatible with a nontrivial parameter-independent left edge across the full resolvent family.

## 4. Prior-art and novelty audit

Hilbert's first resolvent identity is classical, as is the fact that one resolvent value determines a closed operator. Pseudo-resolvent theory treats the resolvent identity itself as the defining compatibility law for operator-valued families. No novelty is claimed for those abstract facts, nor for standard resolvent-comparable perturbation theory.

A targeted literature search around resolvent intertwining, pseudo-resolvents, quasi-affine transforms, and self-adjoint resolvent factorizations found the classical surrounding machinery but no reason to regard the two-line rigidity argument as a new general theorem. It should be read as an elementary corollary of the resolvent identity.

The durable line-specific delta is narrower: the recent `prime_lattice` branch deliberately analyzed exact covariance at one spectral point and left kernel/domain singularities as possible escapes. The two-point calculation shows that **none of those fixed-edge escapes can represent a genuine same-parameter resolvent family**. Any surviving relative-resolvent mechanism must introduce spectral-parameter dependence, parameter translation, ideal-valued error, an unbounded/domain-sensitive relation not expressible by one bounded left multiplier, or a different target architecture.

Because the proof is self-contained and the literature only delimits novelty through standard resolvent theory, no `SOURCES.md` update is required.

## 5. Adversarial boundaries

**Two distinct parameters are load-bearing.** At one point \(z_0\), the factorization

\[
R_1(z_0)=A R_0(z_0)
\]

is highly non-rigid; `PL-202` and `PL-203` exploit exactly this freedom. The theorem does not retroactively invalidate those single-point counterexamples.

**The same bounded edge is load-bearing.** A family \(A(z)\) is not forced to be trivial. It is instead constrained by the transfer law above. This is the natural regime for relative resolvents, perturbation determinants, scattering matrices, boundary triples, and spectral-shift functions.

**Same-parameter covariance is load-bearing.** A prime may act by a spectral translation such as \(z\mapsto z-\log p\). The theorem does not forbid such an action; indeed it identifies parameter motion as one of the canonical ways to escape fixed-edge triviality.

**Exact equality is load-bearing.** If the two covariance equations hold only modulo compact, Schatten, trace-class, or asymptotically small errors, the subtraction leaves an error term and the cancellation argument no longer forces \(A=I\).

**Boundedness/density are used.** The proof extends vanishing from \(\operatorname{Dom}H_0\) to the Hilbert space through boundedness of \(A\). Unbounded or partially defined edge transports require separate domain analysis.

**Nothing zeta-specific enters the theorem.** The result survives arbitrary relabeling of the prime axes and Beurling replacement. It is therefore a negative universality control, not positive evidence for RH.

## Falsification / audit test

The main claim is falsified by a closed densely defined pair \(H_0\ne H_1\), distinct common resolvent points \(z,w\), and one bounded \(A\ne I\) satisfying

\[
(H_1-z)^{-1}=A(H_0-z)^{-1},
\qquad
(H_1-w)^{-1}=A(H_0-w)^{-1}.
\]

Such an example would contradict the first-resolvent-identity calculation above. Apparent counterexamples should be checked for one of the actual escapes: a parameter-dependent \(A(z)\), a shifted spectral parameter, approximate/ideal-valued equality, an unbounded transport, or failure of dense-domain hypotheses.

## Consequence for the research line

The exact resolvent-covariance branch now has a sharper architecture boundary. Fixed-edge factorization at one spectral point is too programmable to be arithmetic (`PL-202`--`PL-203`), while a fixed bounded edge at two spectral points is too rigid to be nontrivial (this finding). Thus there is no intermediate RH-sensitive regime obtained merely by making a one-point edge singular and then pretending it transports the whole resolvent family.

A viable prime-resolvent construction must instead make the spectral parameter part of the geometry. The natural surviving targets are a source-forced parameter action such as the \(\log p\) translation, a genuinely parameter-dependent relative transfer with nontrivial arithmetic normalization, or an ideal-valued/scattering relation whose determinant or positivity is not programmable by generic operator data. Those mechanisms still need the line's usual Beurling/Helson and arbitrary-inner controls before they can carry RH evidence.