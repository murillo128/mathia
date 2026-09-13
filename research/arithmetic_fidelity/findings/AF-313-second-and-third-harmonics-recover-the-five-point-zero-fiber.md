# AF-313 — Second and third harmonics recover the five-point zero fiber

**Status:** `EXACT-DERIVED`, `STRUCTURAL-RECOVERY`, `ARITHMETIC-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-312 shows that a hypothetical exact five-prime phase cancellation cannot repeat at the first few integer harmonics. The stronger structural fact is that the second and third harmonics do not merely survive: away from one explicit torsion degeneration, they already recover the entire unordered five-phase configuration.

Let

\[
Z=\{z_1,\ldots,z_5\}\subset \mathbb S^1
\]

be an unordered multiset, allowing multiplicity, and write its power sums

\[
s_m(Z):=\sum_{j=1}^5 z_j^m.
\]

Restrict to the first-harmonic zero fiber

\[
s_1(Z)=0.
\tag{1}
\]

Then exactly one of the following occurs.

1. **Regular-pentagon fiber.** If `s_2(Z)=0`, then also `s_3(Z)=0` and

\[
\boxed{Z=\rho\,\mu_5}
\tag{2}
\]

for some `rho in S^1`, where `mu_5` is the full set of fifth roots of unity. Every rotated regular pentagon has the same observation

\[
(s_1,s_2,s_3)=(0,0,0).
\tag{3}
\]

2. **Faithful fiber.** If `s_2(Z) ne 0`, then the pair

\[
\boxed{(s_2(Z),s_3(Z))}
\tag{4}
\]

uniquely determines the unordered multiset `Z`, including multiplicities.

More explicitly, put

\[
E:=\prod_{j=1}^5 z_j.
\]

On the nondegenerate fiber,

\[
\boxed{
E=-\frac{2s_3}{3\overline{s_2}},
}
\tag{5}
\]

and `Z` is exactly the root multiset of

\[
\boxed{
P_{s_2,s_3}(w)
=
w^5-
\frac{s_2}{2}w^3-
\frac{s_3}{3}w^2+
\frac{2s_3}{3\overline{s_2}}.
}
\tag{6}
\]

Thus, on the five-point unit-circle zero fiber, the harmonic lift

\[
Z\longmapsto (s_2(Z),s_3(Z))
\tag{7}
\]

has one exceptional collision fiber, consisting precisely of the rotated regular pentagons, and is otherwise injective.

For distinct rational primes `p_1,...,p_5`, define

\[
F_P(t):=\sum_{j=1}^5 p_j^{-it}.
\tag{8}
\]

If `t ne 0` and `F_P(t)=0`, the exceptional fiber `(2)` is impossible. Consequently

\[
\boxed{
\bigl(F_P(2t),F_P(3t)\bigr)
}
\tag{9}
\]

recovers the complete unordered phase multiset

\[
\boxed{
\{p_1^{-it},\ldots,p_5^{-it}\}.
}
\tag{10}
\]

In this precise sense, the information destroyed by the scalar first-harmonic cancellation `F_P(t)=0` is restored by only two additional low-harmonic observations.

## Derivation

### 1. Newton identities plus unit-circle reciprocity

Let

\[
P(w)=\prod_{j=1}^5(w-z_j)
=w^5-e_1w^4+e_2w^3-e_3w^2+e_4w-e_5
\tag{11}
\]

with elementary symmetric functions `e_r=e_r(z_1,...,z_5)`, and set

\[
E:=e_5=\prod_{j=1}^5z_j.
\tag{12}
\]

Since every `|z_j|=1`, complementing an elementary-symmetric subset gives the standard self-inversive relations

\[
\boxed{
e_{5-r}=E\,\overline{e_r}
\qquad(0\le r\le5).
}
\tag{13}
\]

In particular,

\[
e_4=E\overline{e_1},
\qquad
e_3=E\overline{e_2}.
\tag{14}
\]

The zero-fiber condition `(1)` gives `e_1=s_1=0`, hence `e_4=0`. Newton's identities then give

\[
s_2+2e_2=0,
\qquad
s_3-3e_3=0,
\tag{15}
\]

so

\[
\boxed{
e_2=-\frac{s_2}{2},
\qquad
e_3=\frac{s_3}{3}.
}
\tag{16}
\]

Combining `(14)` and `(16)`,

\[
\frac{s_3}{3}
=E\,\overline{\left(-\frac{s_2}{2}\right)}
=-\frac{E\overline{s_2}}2.
\tag{17}
\]

If `s_2 ne0`, equation `(17)` immediately yields `(5)`. Equations `(11)` and `(16)`, together with `e_1=e_4=0` and `(5)`, then give exactly `(6)`. A monic polynomial determines its root multiset uniquely, so `(s_2,s_3)` is faithful on this nondegenerate fiber.

The same identity also gives the exact consistency law already implicit in AF-312,

\[
\boxed{|s_3|=\frac32|s_2|.}
\tag{18}
\]

Thus `s_2` and `s_3` vanish together on the zero fiber.

### 2. The complete exceptional fiber is the regular-pentagon orbit

Suppose `s_2=0`. Then `(16)` gives `e_2=0`, `(14)` gives `e_3=0`, and `s_1=0` gives `e_1=e_4=0`. Therefore

\[
P(w)=w^5-E.
\tag{19}
\]

Because `|E|=1`, choose `rho in S^1` with `rho^5=E`. The roots of `(19)` are precisely

\[
\rho,\rho\zeta_5,\rho\zeta_5^2,\rho\zeta_5^3,\rho\zeta_5^4,
\tag{20}
\]

which proves `(2)`. Conversely, every rotated regular pentagon has `s_m=0` for `m=1,2,3,4`, so all such rotations collapse to `(3)`.

This classifies the whole failure set of the two-harmonic lift, rather than merely showing generic injectivity.

### 3. Rational-prime phases exclude the exceptional fiber

Now let

\[
z_j=p_j^{-it}
\tag{21}
\]

for five distinct rational primes and `t ne0`, and suppose `F_P(t)=s_1=0`.

If `Z` were a rotated regular pentagon, every phase ratio would be a fifth root of unity. Choose three distinct primes, say `p_1,p_2,p_3`. Then

\[
\left(\frac{p_1}{p_2}\right)^{-5it}=1,
\qquad
\left(\frac{p_1}{p_3}\right)^{-5it}=1.
\tag{22}
\]

Hence there are nonzero integers `a,b` with

\[
5t\log(p_1/p_2)=2\pi a,
\qquad
5t\log(p_1/p_3)=2\pi b.
\tag{23}
\]

Therefore

\[
\frac{\log(p_1/p_2)}{\log(p_1/p_3)}=\frac ab\in\mathbb Q,
\tag{24}
\]

which implies a nontrivial multiplicative relation

\[
(p_1/p_2)^b=(p_1/p_3)^a.
\tag{25}
\]

Unique factorization makes `(25)` impossible for three distinct rational primes. Thus the regular-pentagon fiber cannot occur. This recovers, in a form adapted to the fidelity statement, the `s_2 ne0` part of AF-312's torsion exclusion.

Substituting

\[
s_2=F_P(2t),
\qquad
s_3=F_P(3t)
\tag{26}
\]

into `(5)`--`(6)` proves the prime specialization `(9)`--`(10)`.

## Fidelity interpretation

The scalar compression

\[
T(Z)=s_1(Z)
\tag{27}
\]

collapses the entire zero fiber to one value. The two-harmonic mark

\[
M(Z)=(s_2(Z),s_3(Z))
\tag{28}
\]

is an exact recovery lift on that fiber except for one completely classified torsion orbit. Rational-prime arithmetic removes precisely that bad orbit, so the same lift is faithful on every hypothetical nonzero five-prime exact hit.

This separates two questions that had been entangled in the current pentagon frontier:

- **incidence:** whether the prime logarithmic flow ever reaches the five-point zero cone at all remains open here;
- **post-incidence information loss:** conditional on such a hit, the first-harmonic collapse is not irreversible; the next two harmonics retain enough relational information to reconstruct the full phase multiset.

The result therefore does not solve the first-incidence problem from AF-308--AF-312, but it removes a possible secondary obstruction. If a five-prime exact hit exists, low-harmonic scalarization has not yet destroyed its phase geometry.

There is also an exact conditioning warning. Formula `(5)` divides by `s_2`, so recovery becomes ill-conditioned as the configuration approaches the regular-pentagon orbit. On any region `|s_2|>=eta>0`, coefficient recovery from `(s_2,s_3)` is locally Lipschitz with constants of order `eta^{-1}`. No uniform positive lower bound for `|s_2|` is proved for hypothetical prime hits, so exact identifiability must not be upgraded to uniform stable recovery.

## Prior art and novelty assessment

The algebraic ingredients are classical. Newton identities reconstruct elementary symmetric coefficients from power sums, while roots on the unit circle force the coefficient symmetry of a self-inversive polynomial. Standard references for the latter include Andrzej Schinzel, **“Self-Inversive Polynomials with All Zeros on the Unit Circle,”** *The Ramanujan Journal* 9 (2005), 19--23, DOI `10.1007/s11139-005-0821-9`, and Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials* (Cambridge University Press, 2010), 312--321, DOI `10.1017/CBO9780511721274.020`.

Finite recovery of atomic measures from moments is also classical Prony/trigonometric-moment territory. For a modern reconstruction reference, see Stefan Kunis, Thomas Peter, Tim Roemer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.023`.

A targeted search did not identify this exact five-point `s_1=0` two-harmonic specialization as a named theorem, but it is an elementary consequence of those classical structures. **No novelty claim is made.** Its durable value for Arithmetic Fidelity is the complete fiber classification: two low harmonics restore exact phase information everywhere except a single torsion family, and rational-prime arithmetic excludes exactly that family.

## Boundaries and falsification checks

- Recovery is of the **unordered phase multiset**, not a labeling that assigns each recovered phase to a particular prime.
- The theorem assumes exactly five unit-modulus points and the exact constraint `s_1=0`. It is not asserted for larger supports, unequal weights, approximate cancellation, or off-circle data.
- The pair `(s_2,s_3)` is proved sufficient, not minimal among all possible complex or nonlinear marks.
- Exact recovery is not uniformly conditioned. The singular set `s_2=0` is precisely the rotated regular-pentagon orbit, and arbitrarily close configurations can make the coefficient formula poorly conditioned.
- Repeated phase values, if they occur, are recovered with multiplicity by the polynomial, but individual root tracking can be unstable near collisions.
- The prime specialization excludes the torsion degeneration but does **not** prove that a nonzero five-prime hit exists or does not exist.
- No zero-selection theorem, critical-line statement, or RH implication follows.

## Dependency audit

- **AF-312:** supplies the current five-prime harmonic setting and independently establishes that a hypothetical nonzero prime hit cannot have `F_P(2t)=0` or `F_P(3t)=0`; the present finding strengthens that survival statement to exact recovery.
- **This finding:** classifies the `(s_2,s_3)` fibers of the full five-point unit-circle zero set and then specializes the exceptional fiber away using rational-prime unique factorization.
