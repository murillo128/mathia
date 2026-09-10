# PC-241 — original-coordinate/refinement noncommutativity is the classical Cuntz ax+b system

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the noncommuting original-coordinate / all-scale refinement escape left open by PC-239 and PC-240. The canonical unit-circle coordinate together with the canonical power-map pullbacks satisfies exactly the addition-dilation relations of Cuntz's `ax+b` C*-algebra over the natural numbers. At finite polygon level, adjoining any finite family of old-space projections to the original coordinate produces an explicit matrix algebra over only the common residual cyclic factor. Thus making the refinement system genuinely noncommutative does not by itself create a new Prime-Circle RH mechanism: the resulting abstract operator algebra is established arithmetic operator-algebraic structure, and its finite shadows depend only on elementary gcd/congruence data. Any surviving mechanism must use embedded geometric information not determined by these addition/dilation/refinement relations.

## 1. The source-forced circle operators

Prime Circle has two operations before any hyperbolic model is imposed:

1. the original circle coordinate `z`, and
2. the power/refinement maps `z -> z^n`.

On the canonical Hilbert space

\[
H=L^2(S^1,m),
\]

with normalized Haar measure, let

\[
(Uf)(z)=z f(z),
\qquad
(V_n f)(z)=f(z^n),
\qquad n\ge1.
\tag{1}
\]

No spectral wrapper or external arithmetic weight has been introduced here. `U` is multiplication by the original embedded coordinate, while `V_n` is the pullback by the same power map that organizes polygon refinement.

For the Fourier basis `e_k(z)=z^k`, `k in Z`,

\[
Ue_k=e_{k+1},
\qquad
V_n e_k=e_{nk}.
\tag{2}
\]

Each `V_n` is an isometry because `z -> z^n` preserves Haar measure. Its range projection

\[
E_n:=V_nV_n^*
\tag{3}
\]

is therefore exactly the congruence projection

\[
E_n e_k=\mathbf 1_{n\mid k}e_k.
\tag{4}
\]

This is the infinite-circle counterpart of the old/pullback projections that appear at finite refinement levels in PC-224--PC-240.

## 2. Exact ax+b relations

Equations (1)--(4) immediately give

\[
V_mV_n=V_{mn},
\qquad
V_nU=U^nV_n.
\tag{5}
\]

Moreover, conjugating `E_n` by powers of `U` selects the residue classes modulo `n`:

\[
U^rE_nU^{-r}e_k
=
\mathbf 1_{k\equiv r\pmod n}e_k.
\tag{6}
\]

The residue classes partition `Z`, hence

\[
\boxed{
\sum_{r=0}^{n-1}U^rV_nV_n^*U^{-r}=I.
}
\tag{7}
\]

Together with unitarity of `U` and isometricity of the `V_n`, (5) and (7) are precisely the canonical addition-dilation relations for the C*-algebra associated with the semigroup `N \rtimes N^x` studied by Cuntz. In particular, the apparent new noncommutativity

\[
V_nU\ne UV_n
\]

is not a new Prime-Circle operator phenomenon: it is the standard affine relation `x -> nx+r` in Fourier index.

The matched-control point is exact. Nothing in (5)--(7) asks whether `n` is prime. Every positive integer dilation satisfies the same relations. Restricting attention to prime refinement generators does not create a different multiplicative closure, because products of the prime `V_p` generate `V_n` for every `n`.

## 3. Finite polygon shadow: all old projections reduce to one gcd

The same mechanism can be classified exactly before taking any infinite limit. Fix a polygon level `L` and use the Fourier basis

\[
e_k(z)=z^k,
\qquad k\in\mathbb Z/L\mathbb Z.
\]

Let `Z_L=M_z`, so `Z_Le_k=e_{k+1}`. For a divisor `d|L`, let `E_d` be the projection onto the pullback of the `d`-level along `z -> z^{L/d}`. Writing

\[
r_d=\frac Ld,
\]

we have exactly

\[
E_de_k=\mathbf 1_{r_d\mid k}e_k.
\tag{8}
\]

Now choose any finite family `D={d_1,...,d_t}` of divisors of `L` and define

\[
g=\gcd(d_1,\ldots,d_t),
\qquad
R=\operatorname{lcm}(L/d_1,\ldots,L/d_t)=\frac Lg.
\tag{9}
\]

Then

\[
\boxed{
C^*(Z_L,\{E_d:d\in D\})
\cong
M_R(\mathbb C)\otimes C(\mu_g)
\cong
\bigoplus_{\mu_g}M_R(\mathbb C).
}
\tag{10}
\]

This is an exact finite-dimensional statement. To prove it, conjugate every `E_d` by powers of `Z_L`. The resulting projections are indicators of residue classes modulo `r_d`. Their Boolean algebra therefore contains the atom projections `P_a` onto

\[
k\equiv a\pmod R,
\qquad 0\le a<R,
\tag{11}
\]

because the intersection of the compatible class `a mod r_d` over all `d in D` is exactly `a mod R`.

Set

\[
F_{ab}=P_aZ_L^{a-b}P_b.
\tag{12}
\]

Since `0<=a,b<R`, these maps preserve the residual index inside each class and satisfy the matrix-unit relations

\[
F_{ab}F_{cd}=\delta_{bc}F_{ad},
\qquad
F_{ab}^*=F_{ba}.
\tag{13}
\]

Finally `W=Z_L^R` commutes with all `F_{ab}` and has order `g`. Conversely,

\[
Z_L
=
\sum_{a=0}^{R-2}F_{a+1,a}
+WF_{0,R-1},
\tag{14}
\]

while every original `E_d` is a sum of the `P_a`. Hence the two sides of (10) generate one another.

PC-240 is the one-projection specialization of (10): if `L=Nq` and `D={N}`, then `g=N`, `R=q`, and one obtains `C(mu_N) tensor M_q`. The finite theorem shows exactly what happens when more canonical old projections are added in an attempt to mix those blocks. They only replace the center `mu_N` by `mu_g`, where `g` is the gcd of the retained levels. If `g=1`, the algebra becomes the full matrix algebra `M_L(C)`; maximal noncommutative freedom is therefore possible, but its occurrence is controlled by the elementary gcd condition rather than by a prime-specific spectral selector.

As a numerical stress check, direct matrix-algebra generation gives dimensions `36`, `16`, `32`, and `100` respectively for `(L,D)=(6,{2,3}), (8,{4}), (8,{2,4}), (10,{2,5})`, agreeing with the exact dimension `g(L/g)^2` from (10). The proof above, not these finite checks, is the evidence for the formula.

## 4. Relation to PC-010 and the current frontier

PC-010 already established that if one forgets the embedding and keeps only roots of unity, birth levels, divisibility, and power maps, the refinement dynamics is the classical Bost--Connes cyclotomic tower. PC-239 and PC-240 deliberately left open a stronger possibility: perhaps retaining the original coordinate *together with* refinement and old-space projections, before commutative functional calculus, creates a genuinely new noncommutative carrier.

Equations (5)--(7) identify that carrier. Cuntz's 2008 construction is explicitly the `ax+b` C*-algebra obtained from the Bost--Connes algebra by adjoining a unitary generator corresponding to addition. In the Prime-Circle Fourier representation, that extra generator is exactly `U=M_z`, and the Bost--Connes/refinement isometries are exactly the `V_n`. Cuntz further identifies the stabilization with an affine crossed product over the finite adeles. Thus the natural abstract passage

\[
\text{cyclotomic refinement}
+\text{original coordinate}
\longrightarrow
\text{noncommutative all-scale C* algebra}
\]

lands directly in established arithmetic noncommutative geometry.

This is stronger than saying that some chosen determinant or trace happens to reproduce zeta data. It identifies the source-generated operator algebra itself before a Hamiltonian is chosen. Consequently, the mere facts that the algebra is noncommutative, has full matrix finite shadows, admits adelic crossed-product descriptions, or supports generic spectral triples cannot be counted as a new RH mechanism.

## 5. What this does and does not rule out

The result is a **prior-art classicalization and boundary theorem**, not a no-go for every operator that could act on the same Hilbert space. It rules out novelty from the abstract algebra generated solely by:

- the original circle coordinate;
- power-map/refinement pullbacks;
- their range/old-space projections; and
- finite algebraic/C*-closure of those operations.

A surviving Prime-Circle mechanism must use source data not determined by the affine relations themselves. Examples still outside this theorem are chord-dependent weights attached to primitive/new vertices, harmonic or off-circle fields, primitive-shell masks used as distinguished geometric operators rather than generic congruence projections, source-forced unbounded/domain-sensitive operators carrying more than the abstract `ax+b` action, or the global uniformization/accessory branch already isolated elsewhere in this line.

The theorem also does not say that Cuntz/Bost--Connes systems are mathematically irrelevant to zeta. It says the opposite novelty-wise: they are already mature arithmetic operator-algebraic structures. Recovering them from Prime Circle is therefore a classification of the noncommutative refinement architecture, not progress toward RH by itself.

## Literature / novelty check

- Joachim Cuntz, **C*-algebras associated with the `ax+b`-semigroup over N**, in *K-Theory and Noncommutative Geometry*, EMS Series of Congress Reports (2008), 201--215. DOI: `10.4171/060-1/8`; arXiv: `math/0611541`. The published abstract states that the algebra is naturally associated with the `ax+b` semigroup over the natural numbers, is obtained from the Bost--Connes algebra by adding one unitary generator corresponding to addition, and has a stabilization described by the affine action over the finite adeles. This is the direct prior-art match to (5)--(7).
- Nathan Brownlowe, Astrid an Huef, Marcelo Laca and Iain Raeburn, **Boundary quotients of the Toeplitz algebra of the affine semigroup over the natural numbers**, *Ergodic Theory and Dynamical Systems* 32 (2012), 35--62. DOI: `10.1017/S0143385710000830`. This places Cuntz's `Q_N` inside the broader semigroup/Toeplitz boundary-quotient framework and confirms that the addition-dilation C*-algebra is established operator-algebraic territory.

No novelty is claimed for the Cuntz relations or the resulting infinite C*-algebra. The project-specific exact contribution is the identification of the current Prime-Circle noncommuting coordinate/refinement escape with that classical system, together with the finite multi-old-projection classification (10) showing how its polygon shadows collapse to gcd-controlled matrix blocks.