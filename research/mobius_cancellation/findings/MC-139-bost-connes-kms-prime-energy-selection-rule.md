# MC-139 — Bost–Connes KMS grading blocks cross-prime off-diagonal energy compensation

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

In the standard Bost–Connes system, the KMS condition itself imposes an exact selection rule on every homogeneous time-evolution mode. This rules out a natural residual escape from `MC-138`: one cannot restore the missing cross-prime Möbius orientation by balancing an off-diagonal semigroup-energy mode at one prime against a different prime inside an equilibrium KMS expectation.

Write the Bost–Connes dynamics on the standard algebraic generators as

\[
\sigma_t(\mu_n)=n^{it}\mu_n,
\qquad
\sigma_t(e(r))=e(r).
\tag{1}
\]

For `d>0`, call an analytic element `x` homogeneous of degree `d` when

\[
\sigma_t(x)=d^{it}x.
\tag{2}
\]

Let `phi_beta` be any `KMS_beta` state with `beta>0`. Then every homogeneous element satisfies

\[
\boxed{
 d\ne1\quad\Longrightarrow\quad \phi_\beta(x)=0.
}
\tag{3}
\]

Consequently, if `x` and `y` have degrees `d` and `e`, respectively,

\[
\boxed{
 d\ne e\quad\Longrightarrow\quad
 \phi_\beta(x^*y)=0.
}
\tag{4}
\]

The arithmetic specialization is sharper. Suppose `p_1,...,p_m` are distinct rational primes and `x_j` is homogeneous of degree `p_j^{k_j}` with `k_j in Z`. Since

\[
\sigma_t\!\left(\prod_{j=1}^m x_j\right)
=
\left(\prod_{j=1}^m p_j^{k_j}\right)^{it}
\prod_{j=1}^m x_j,
\]

we have

\[
\boxed{
\phi_\beta\!\left(\prod_{j=1}^m x_j\right)\ne0
\quad\Longrightarrow\quad
k_1=\cdots=k_m=0.
}
\tag{5}
\]

The last implication is just unique factorization in the positive rationals: distinct-prime energy degrees cannot compensate one another. A nonzero KMS moment may contain off-diagonal factors, but their total semigroup degree must cancel **prime by prime**, not merely after mixing different primes.

In particular, if `p!=q`, `k,l!=0`, `x_p` has degree `p^k`, and `y_q` has degree `q^l`, then both one-point expectations vanish and

\[
\boxed{
\operatorname{Cov}_{\phi_\beta}(x_p,y_q)
=
\phi_\beta(x_p^*y_q)=0.
}
\tag{6}
\]

Thus leaving the commutative divisibility diagonal does not by itself create a cross-prime equilibrium covariance channel. The raw semigroup off-diagonal modes are filtered by the KMS grading before any critical-half phenomenon can appear. A surviving Bost–Connes route must use degree-zero information after primewise energy cancellation — for example genuinely arithmetic coefficient/cyclotomic data or more global constructions — or leave the equilibrium-KMS setting altogether. It must still supply an independently cheaper transfer to anchored Mertens excursion.

## 1. The KMS condition gives the selection rule directly

For analytic elements, use the standard KMS identity

\[
\phi_\beta(ab)
=
\phi_\beta\!\left(b\,\sigma_{i\beta}(a)\right).
\tag{7}
\]

Taking `b=1` gives

\[
\phi_\beta(a)=\phi_\beta(\sigma_{i\beta}(a)).
\tag{8}
\]

If `a=x` is homogeneous of degree `d`, its entire analytic continuation along the dynamics is

\[
\sigma_z(x)=d^{iz}x,
\]

so

\[
\sigma_{i\beta}(x)=d^{-\beta}x.
\tag{9}
\]

Equations `(8)` and `(9)` yield

\[
(1-d^{-\beta})\phi_\beta(x)=0.
\]

For `beta>0`, the factor is nonzero exactly when `d!=1`, proving `(3)`. No uniqueness of the KMS state, Gibbs representation, trace formula, or low-/high-temperature classification is needed.

If `x` and `y` have degrees `d` and `e`, then `x^*y` has degree `e/d`. Applying `(3)` gives `(4)`. More generally, the product of homogeneous elements has degree equal to the product of their degrees even when the factors themselves do not commute, because the time evolution is an automorphism and the spectral factors are scalars.

## 2. Bost–Connes semigroup monomials carry rational energy degree

The original Bost–Connes time evolution `(1)` makes every standard algebraic monomial

\[
\mu_m\,a\,\mu_n^*,
\qquad
\sigma_t(a)=a,
\]

homogeneous of degree

\[
d=\frac{m}{n}.
\tag{10}
\]

Therefore every KMS state satisfies

\[
\boxed{
 m\ne n
\quad\Longrightarrow\quad
\phi_\beta(\mu_m a\mu_n^*)=0.
}
\tag{11}
\]

This is not a diagonal-factorization statement. The element can be genuinely off-diagonal in the semigroup crossed product; its expectation vanishes because its time-evolution degree is nonzero.

For degree one, the selection rule stops being informative. In the basic balanced monomial with the same semigroup index on both sides,

\[
\mu_n a\mu_n^*,
\]

the Bost–Connes relations identify the result with the corresponding endomorphism of the coefficient algebra. More complicated words can likewise have zero total degree after internal cancellation. Such degree-zero information is precisely outside the obstruction proved here.

## 3. Unique factorization makes neutrality primewise

The feature specific to the rational Bost–Connes energy grading is that its degrees lie in the multiplicative group generated freely by the rational primes. If a homogeneous word has degree

\[
d=\prod_p p^{k_p}
\]

with finite support, then `d=1` if and only if every `k_p=0`.

Hence an energy surplus `p^k` cannot be neutralized by a `q^{-l}` mode for `q!=p`. The KMS expectation sees the rational degree before any arithmetic interpretation of the coefficient part. This gives the exact primewise neutrality rule `(5)`.

The rule is stronger than merely observing that two chosen modes happen to be orthogonal in a particular Hilbert-space representation. It holds for **every** `KMS_beta` state with `beta>0`, including the symmetry-broken family above the Bost–Connes phase transition, because the derivation uses only the KMS identity and the source-defined time evolution.

It is also weaker than prime independence. Products such as a positive and negative degree at the same prime may be neutral and need not factor, and a word that is neutral separately at several primes can have a nonzero expectation. The theorem therefore says **no cross-prime energy compensation**, not that all non-diagonal prime data are independent.

## 4. Relation to the current Bost–Connes frontier

`MC-138` proved that the commutative divisibility diagonal is an exact product system across prime valuations under every Bost–Connes KMS state. Its conclusion deliberately left genuinely non-diagonal crossed-product observables as a possible escape.

The present finding removes the simplest such escape. Replacing diagonal observables by raw semigroup raising/lowering modes does not create a phase-sensitive covariance between distinct primes: if their energy degrees differ, `(4)` kills the covariance exactly; if several distinct-prime degrees occur in a moment, `(5)` requires separate cancellation of every prime exponent.

This does **not** close the full Bost–Connes route. The coefficient/cyclotomic algebra is fixed by the time evolution and can retain arithmetic residue/Galois information. Current Prime Lattice work (`PL-212`) independently shows that prime-level cyclotomic KMS harmonics have their own information split: the symmetry-invariant equilibrium channel cancels the zeta denominator, while nontrivial broken-symmetry harmonics carry `L(s,chi)/zeta(s)`. That result is complementary rather than a premise of `(3)`–`(5)`.

Together these boundaries mean that a future Bost–Connes-to-Mertens mechanism cannot obtain its decisive cross-prime information merely from diagonal valuation covariance or from cancellation of different-prime semigroup energies. It needs a degree-zero arithmetic carrier whose information survives the relevant KMS/symmetry projection and then a non-tautological bridge from that carrier to the additive prefix order defining `M(x)`.

## 5. Prior art and novelty audit

The underlying ingredients are classical.

Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica, New Series **1** (1995), no. 3, 411–457, DOI `10.1007/BF01589495`, define the arithmetic `C^*`-dynamical system and its norm-driven time evolution. Standard presentations record the generator form `(1)`.

The annihilation of nonzero time-evolution spectral subspaces by a KMS state is a standard consequence of the KMS condition/invariance of equilibrium states; it is not a new operator-algebra theorem. For adjacent modern crossed-product context, Johannes Christensen and Klaus Thomsen, *KMS states on crossed products by abelian groups*, Mathematica Scandinavica **128** (2022), 1–35, DOI `10.7146/math.scand.a-128965`, develops KMS states for flows on crossed products using fixed-point and spectral analysis.

A targeted search found the standard Bost–Connes dynamics, KMS classification, fixed-point/spectral-subspace language, and general crossed-product KMS theory. The primewise unique-factorization consequence above is an immediate specialization of those established ingredients. Accordingly this finding makes **no novelty claim**. Its value for Mathia is the exact elimination of a residual mechanism class left open by `MC-138`.

## Boundaries and falsification tests

- The result concerns expectations under genuine positive-temperature `KMS_beta` states. A meromorphically continued scalar formula, a non-KMS functional, a trace-formula distribution, or a zero-temperature limiting object is not covered merely because it comes from the same algebra.
- The selection rule uses time-evolution degree, not support in the coefficient algebra. An element with coefficient data involving many primes may still be homogeneous of degree `p^k`; `(3)` applies to its degree regardless of that coefficient support.
- Equation `(5)` does not say that every surviving moment factors across primes. It says only that its total energy exponent at each prime must vanish.
- Same-prime opposite degrees can cancel and may produce nontrivial degree-zero observables. These are not ruled out.
- Degree-zero cyclotomic/Galois information is not ruled out. `PL-212` shows that such information can indeed be nontrivial, while also identifying a separate symmetry/analytic-continuation obstruction for one canonical harmonic family.
- The theorem does not produce a Mertens estimate and does not constrain zeta zeros by itself. It is a representation-level obstruction.
- The conclusion would fail only if the proposed observable were not a KMS expectation for the Bost–Connes time evolution, were not homogeneous with the claimed rational degree, or used a construction in which the relevant information is carried entirely inside the zero-energy sector.

## Consequence for the line

The residual instruction after `MC-138` to explore “genuinely non-diagonal crossed-product data” needs a sharper qualification. **Non-diagonal semigroup energy is not itself the missing cross-prime carrier.** KMS equilibrium annihilates every nonzero energy mode, and rational unique factorization prevents different prime energies from neutralizing one another.

Future Bost–Connes work in Möbius Cancellation should therefore require an explicit degree-zero arithmetic carrier — not merely off-diagonality — and should test whether that carrier preserves Möbius orientation and anchored integer order cheaply enough to say anything new about `M(x)`.