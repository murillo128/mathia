# AF-312 — Five-prime exact hits have a low-harmonic exclusion window and finite integer recurrence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `POWER-SUM-RIGIDITY`, `UNIT-EQUATIONS`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-310 and AF-311 show that the first unresolved saturated prime-support exact-zero problem occurs at five terms and that neither integer character relations nor Baker's algebraic-linear relations separate the prime phase curve from generic equilateral-pentagon closure. A different nonlinear constraint appears when one asks what a hypothetical exact hit can do at its **integer harmonics**.

Let `p_1,...,p_5` be distinct rational primes and write

\[
F_P(t)=\sum_{j=1}^5 p_j^{-it}.
\tag{1}
\]

If `t\ne0` and

\[
F_P(t)=0,
\tag{2}
\]

then

\[
\boxed{
F_P(2t),\ F_P(3t),\ F_P(4t),\ F_P(5t)\ne0.
}
\tag{3}
\]

Thus any five-prime exact hit is isolated from exact cancellation at its first four positive integer multiples. The mechanism is genuinely nonlinear in the phase configuration: the unit-circle self-reciprocity of the root polynomial converts the first power-sum zero into exact identities among the next power sums, and a second zero at orders `2,3,4,5` forces cyclotomic subgeometry that rational-prime logarithms cannot realize at one common nonzero time.

There is also a global recurrence obstruction on every fixed integer time lattice. For every `t_0\ne0`,

\[
\boxed{
\#\{n\in\mathbb Z:F_P(nt_0)=0\}<\infty,
}
\tag{4}
\]

with a bound depending only on the four-variable dimension and rank one, not on the particular primes or on `t_0`. This is a direct specialization of the Evertse--Schlickewei--Schmidt theorem on nondegenerate linear equations in finite-rank multiplicative groups.

Neither statement settles whether a first five-prime hit (2) exists. Together they close two natural amplification routes beyond AF-311: a hypothetical first hit cannot immediately reproduce at the low harmonics `2t,...,5t`, and exact recurrence along the full integer orbit of any fixed base time is uniformly finite. The unresolved problem is therefore still a first-incidence problem for the specific prime-log direction, not a generic repeated-cancellation phenomenon.

## Power-sum identities for a centered five-point unit configuration

Assume (2) and set

\[
z_j=p_j^{-it}\in S^1,
\qquad
s_m=\sum_{j=1}^5 z_j^m=F_P(mt).
\tag{5}
\]

Let `e_k` be the elementary symmetric functions of `z_1,...,z_5`, and put

\[
E=e_5=\prod_{j=1}^5 z_j.
\tag{6}
\]

Since every root has modulus one, complementation of subsets gives the exact coefficient symmetry

\[
e_{5-k}=E\,\overline{e_k},
\qquad 0\le k\le5.
\tag{7}
\]

The hypothesis `s_1=0` is `e_1=0`, so (7) yields

\[
e_4=0,
\qquad
e_3=E\,\overline{e_2}.
\tag{8}
\]

Newton's identities now collapse the first few higher power sums to one complex parameter `e_2`:

\[
\boxed{s_2=-2e_2,}
\tag{9}
\]

\[
\boxed{
s_3=3e_3
=3E\overline{e_2}
=-\frac32E\,\overline{s_2},
}
\tag{10}
\]

\[
\boxed{
s_4=2e_2^2=\frac12s_2^2,
}
\tag{11}
\]

and

\[
\boxed{
s_5=5E(1-|e_2|^2)
=5E\left(1-\frac{|s_2|^2}{4}\right).
}
\tag{12}
\]

These identities are purely geometric: they hold for every multiset of five unit complex numbers whose first power sum vanishes. Their relevance here comes from combining the forced algebraic alternatives with the arithmetic restrictions on a common-time rational-prime phase orbit.

For reference, the monic root polynomial is

\[
Q(w)=\prod_{j=1}^5(w-z_j)
=w^5+e_2w^3-e_3w^2-E.
\tag{13}
\]

Equation (13) already shows why this is not another linear-forms-in-logarithms argument. The new constraint is a nonlinear relation between the whole zero polygon and its higher power images.

## Harmonics two, three, and four force a regular pentagon

If any one of `s_2,s_3,s_4` vanishes, equations (9)--(11) force

\[
e_2=0.
\tag{14}
\]

Then (8) gives `e_3=0`, so (13) reduces to

\[
Q(w)=w^5-E.
\tag{15}
\]

Hence the five phases are exactly a rotated regular pentagon: after dividing by any one phase, the other phase ratios are fifth roots of unity.

Such a configuration cannot arise from five distinct rational primes at one common nonzero time. Indeed, choose three indices whose normalized fifth-root ratios relative to one fixed phase are nontrivial and distinct. In particular two independent ratios satisfy

\[
(p_a/p_c)^{-5it}=1,
\qquad
(p_b/p_c)^{-5it}=1.
\tag{16}
\]

Thus for nonzero integers `m,n`,

\[
5t\log(p_a/p_c)=2\pi m,
\qquad
5t\log(p_b/p_c)=2\pi n.
\tag{17}
\]

Eliminating `t` gives

\[
n\log(p_a/p_c)-m\log(p_b/p_c)=0.
\tag{18}
\]

Exponentiation produces a nontrivial multiplicative relation among the distinct rational primes `p_a,p_b,p_c`, contradicting unique factorization. Therefore

\[
s_2,s_3,s_4\ne0.
\tag{19}
\]

This recovers the relevant arithmetic content of AF-310 in a different guise: the regular-pentagon branch contains too many simultaneous torsion relations for the prime-log orbit.

## A fifth-harmonic zero forces an antipodal pair plus an equilateral triple

The fifth harmonic has a different exact alternative. If `s_5=0`, equation (12) gives

\[
|e_2|=1.
\tag{20}
\]

Using `e_3=E\overline{e_2}`, condition (20) implies

\[
e_2e_3=E.
\tag{21}
\]

Consequently the root polynomial (13) factors exactly as

\[
\boxed{
Q(w)=(w^2+e_2)(w^3-e_3).
}
\tag{22}
\]

The quadratic factor contributes an antipodal pair of unit phases, while the cubic factor contributes a rotated equilateral triple. In particular three of the original five phase entries sum to zero.

That is impossible for three distinct rational primes at one common nonzero time. If `q_1,q_2,q_3` were distinct primes with

\[
q_1^{-it}+q_2^{-it}+q_3^{-it}=0,
\tag{23}
\]

then three unit vectors closing to zero would form a rotated equilateral triangle. After normalizing by the third phase, the two ratios would be nontrivial cube roots of unity, so

\[
(q_1/q_3)^{-3it}=1,
\qquad
(q_2/q_3)^{-3it}=1.
\tag{24}
\]

Eliminating `t` again gives a nontrivial rational linear relation between `\log(q_1/q_3)` and `\log(q_2/q_3)`, equivalently a nontrivial multiplicative relation among `q_1,q_2,q_3`, contradicting unique factorization.

Therefore `s_5\ne0`. Combining this with (19) proves the low-harmonic exclusion (3).

The factorization (22) is stronger than merely saying that a second zero is nongeneric. It identifies the exact geometry forced by simultaneous first- and fifth-power cancellation, and that geometry contains a three-prime exact-zero subsystem already excluded arithmetically.

## Integer-time recurrence is a rank-one unit-equation problem

Fix any `t_0\ne0` and normalize by the fifth prime:

\[
u_j=(p_j/p_5)^{-it_0},
\qquad 1\le j\le4.
\tag{25}
\]

Then

\[
F_P(nt_0)=0
\iff
1+u_1^n+u_2^n+u_3^n+u_4^n=0.
\tag{26}
\]

Let

\[
\Gamma_{t_0}
=
\{(u_1^n,u_2^n,u_3^n,u_4^n):n\in\mathbb Z\}
\le(\mathbb C^*)^4.
\tag{27}
\]

The generator `u=(u_1,...,u_4)` is not torsion. If `u^q=(1,1,1,1)` for some nonzero integer `q`, then two coordinates would give

\[
qt_0\log(p_1/p_5)=2\pi a,
\qquad
qt_0\log(p_2/p_5)=2\pi b
\tag{28}
\]

with nonzero integers `a,b`; eliminating `qt_0` contradicts unique factorization exactly as above. Hence `\Gamma_{t_0}` is infinite cyclic and has multiplicative rank one.

Equation (26) is therefore the four-variable unit equation

\[
-x_1-x_2-x_3-x_4=1,
\qquad x\in\Gamma_{t_0}.
\tag{29}
\]

Every solution arising from (26) is **nondegenerate** in the Evertse--Schlickewei--Schmidt sense: no nonempty proper subsum of the left side vanishes.

- A one-term subsum cannot vanish because every `x_j` is nonzero.
- A two-term zero, say `x_a+x_b=0`, leaves `1+x_c+x_d=0` by (26), which after undoing the normalization is a forbidden three-prime zero.
- A three-term zero is itself, after undoing the normalization, a forbidden three-prime zero.

Thus the 2002 Evertse--Schlickewei--Schmidt theorem applies with dimension `4` and group rank `1`. It gives an explicit universal bound, depending only on those two parameters, for the number of nondegenerate solutions of (29).

Finally, the map

\[
n\longmapsto(u_1^n,u_2^n,u_3^n,u_4^n)
\tag{30}
\]

is injective. Equality at distinct integers `m,n` would make `u^{m-n}` torsion-trivial, contradicting the preceding argument. Hence the number of integers `n` satisfying (26) is bounded by the same universal finite constant. This proves (4).

The result is stronger than a statement that zeros cannot be periodic: even sparse exact recurrence on one fixed integer time lattice is uniformly finite.

## Why finite-rank unit equations do not settle first continuous incidence

It is important not to overread (4). For one fixed `t_0`, the integer orbit (27) is a rank-one multiplicative group, so finite-rank Diophantine machinery applies. The full continuous prime phase curve

\[
t\longmapsto
\bigl((p_1/p_5)^{-it},\ldots,(p_4/p_5)^{-it}\bigr)
\tag{31}
\]

does not lie in any finite-rank multiplicative subgroup of `(\mathbb C^*)^4`.

Indeed, the map (31) is injective: equality at two distinct times would make all four normalized ratios roots of unity at one common nonzero time difference, already impossible by two-coordinate prime-log independence. Its image is therefore uncountable. By contrast, every finite-rank subgroup of `(\mathbb C^*)^4` is countable: its torsion subgroup lies in the countable group of tuples of roots of unity, and its torsion-free quotient of finite rank embeds in a finite-dimensional `\mathbb Q`-vector space.

So the unit-equation theorem controls exact recurrence **after a base time has been fixed**. It supplies no discretization theorem for the unknown first hit itself. Any attempt to use finite-rank multiplicative-group machinery to exclude (2) must first produce an additional source-specific arithmetic restriction that places the relevant continuous incidence into a finite-rank or otherwise height-controlled class.

## Prior art and novelty assessment

No novelty is claimed for Newton's identities, reciprocal/self-inversive coefficient symmetry of unit-circle root polynomials, unique factorization, unit equations, or finite-rank multiplicative-group finiteness.

- I. G. Macdonald, ***Symmetric Functions and Hall Polynomials***, 2nd ed., Oxford University Press (1995), is a standard reference for Newton identities relating elementary symmetric functions and power sums.
- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, London Mathematical Society Lecture Note Series 352, Cambridge University Press (2010), pp. 312--321, DOI `10.1017/CBO9780511721274.020`, is direct prior art for the conjugate-reciprocal/self-inversive structure forced by unit-circle roots.
- Jan-Hendrik Evertse, **“On sums of S-units and linear recurrences,”** *Compositio Mathematica* 53(2) (1984), 225--244, is classical prior art connecting unit equations with zero sets of linear recurrences.
- Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt, **“Linear equations in variables which lie in a multiplicative group,”** *Annals of Mathematics* 155(3) (2002), 807--836, DOI `10.2307/3062133`, proves the finite-rank nondegenerate-solution bound used in (4), uniformly in the coefficients once dimension and rank are fixed.

A targeted literature audit found extensive classical theory for each ingredient and for zeros of exponential polynomials / linear recurrences. Nothing here is presented as a new theorem in transcendence theory or unit-equation theory. The durable Arithmetic Fidelity content is the exact mechanism audit at the first unresolved prime support: combining centered unit-circle power-sum rigidity with prime-log independence closes the first four harmonic repetitions, while finite-rank unit-equation theory closes unlimited integer recurrence without resolving the initial continuous incidence.

## Boundaries and failure modes

- The theorem is conditional on a hypothetical five-prime exact hit. It neither proves nor disproves existence of `t\ne0` with `F_P(t)=0`.
- The exclusion window is proved only for positive harmonics `m=2,3,4,5`. No claim is made here for `m\ge6`.
- The power-sum identities (9)--(12) are universal geometry for five centered unit phases. The arithmetic content enters only when their forced regular-pentagon or `2+3` cyclotomic branches are compared with rational-prime common-time phases.
- Exact low-harmonic exclusion does not restore a positive stability margin. AF-306 already shows that fixed saturated prime supports can approach zero arbitrarily closely at large heights.
- The finite recurrence theorem concerns one integer lattice `{nt_0}`. It does not bound the number of arbitrary real zeros of `F_P(t)` on the whole real axis.
- Evertse--Schlickewei--Schmidt controls nondegenerate solutions. The nondegeneracy verification here is essential and uses the exact three-prime zero obstruction; omitting it would leave degenerate unit-equation families outside the theorem.
- The finite-rank theorem does not imply that one solution is impossible. In particular, it cannot by itself settle the first-incidence question left by AF-311.
- Nothing here supplies a zeta zero count, analytic continuation, a Riemann-zero divisor, or an RH implication.

## Consequence for the research line

AF-311 narrowed the five-prime frontier from generic “stronger transcendence” to a nonlinear source-specific incidence obstruction. AF-312 identifies one such nonlinear layer and determines exactly how far it reaches.

A first exact five-prime zero would force a centered self-inversive quintic whose low power sums obey (9)--(12). That configuration cannot cancel again at powers `2,3,4,5`; and on any fixed integer orbit, all exact repetitions are uniformly finite by a rank-one unit-equation theorem. Therefore neither low-harmonic propagation nor generic recurrence can amplify a hypothetical first hit into the sort of repeated structure that standard linear-recurrence or finite-rank arguments would automatically exclude.

The remaining theorem surface is sharper: one needs either a source-specific obstruction to the **first** intersection of the prime-log one-parameter subgroup with the pentagon zero manifold, or a stronger nonlinear invariant whose forced behavior at higher powers contradicts rational-prime phases. Any such invariant must go beyond the algebraic-linear relation rank of AF-311 and beyond the finite-recurrence control established here.