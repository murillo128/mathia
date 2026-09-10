# PC-240 — old projection and original coordinate generate only fresh matrix defects

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most direct genuinely noncommuting fixed-base escape left open by PC-225, PC-238 and PC-239. At a coprime refinement `N -> Nq`, keep the canonical old-space projection `E_{N,q}` and the intrinsic original-coordinate multiplier `Z=M_z` simultaneously, before any singular-value or multiplication-functional-calculus compression. They do not commute, and the noncommutativity is not asymptotically small in operator norm. Nevertheless their complete finite-level C*-algebra is exactly

\[
\boxed{
C^*(Z,E_{N,q})\cong C(\mu_N)\otimes M_q(\mathbb C)
\cong\bigoplus_{x\in\mu_N}M_q(\mathbb C).
}
\]

Thus the pair is maximally noncommutative **inside each fresh fiber** but remains completely decomposed over the coarse coordinate. No cross-coarse arithmetic coupling is created. The statement uses only `gcd(N,q)=1`; replacing the prime `q` by any coprime refinement degree gives the identical matrix-fiber architecture.

Along a fixed residue class with the fresh degree tending to infinity, the local Fourier limit is the bilateral shift `S` together with one rank-one projection `P_0`. Their algebra is exactly the split Laurent-plus-compact algebra

\[
\boxed{
C^*(S,P_0)=C^*(S)+\mathcal K(\ell^2(\mathbb Z)),
\qquad C^*(S)\simeq C(\mathbb T).
}
\]

The compact extension splits through the actual bilateral unitary `S`, so every Fredholm element in this algebra has index zero. This is materially different from obtaining a new Toeplitz/index mechanism: the source-forced noncommutativity survives only as a compact fiber defect over the already-classified bilateral-shift symbol. Arbitrary spectra can of course be encoded by choosing arbitrary elements of the full finite matrix fibers or compact ideal, but that freedom is not supplied by Prime-Circle arithmetic and is exactly the arbitrary-spectral-wrapper failure mode excluded by the research mandate.

This finding does **not** classify simultaneous `N,q -> infinity`, source-forced operators that genuinely mix different coarse fibers, exact-order projectors for a growing composite fresh conductor, unbounded/domain-sensitive limits, or global uniformization/accessory data.

## 1. The exact source-forced noncommuting pair

Let

\[
H_m=L^2(\mu_m)
\]

with normalized counting measure. Fix `N>1` and an integer `q>1` with `(N,q)=1`; primality will not be used in the derivation. The refinement map is the power map

\[
\mu_{Nq}\longrightarrow\mu_N,
\qquad z\longmapsto z^q,
\]

and the canonical old-state pullback is

\[
J_{N,q}:H_N\longrightarrow H_{Nq},
\qquad
(J_{N,q}f)(z)=f(z^q).
\tag{1}
\]

Put

\[
E_{N,q}=J_{N,q}J_{N,q}^*.
\tag{2}
\]

This is the orthogonal projection/conditional expectation onto the old subspace. The second operator is not chosen spectrally: it is the original refined-polygon coordinate itself,

\[
Z_{N,q}=M_z.
\tag{3}
\]

It retains precisely the coordinate whose common-anchor chord is `|1-z|`, and PC-239 left noncommuting old/new operators applied before coordinate functional calculus outside its classification.

Use the canonical CRT isomorphism

\[
\mu_{Nq}\stackrel{\sim}{\longrightarrow}\mu_N\times\mu_q,
\qquad
z\longmapsto(x,y)=(z^q,z^N).
\tag{4}
\]

Choose integers `a,b` satisfying

\[
aq+bN=1.
\tag{5}
\]

Then

\[
z=x^a y^b,
\tag{6}
\]

so under `H_{Nq}\simeq H_N\otimes H_q`,

\[
\boxed{
Z_{N,q}=A\otimes B,
\qquad
A=M_{x^a},
\qquad
B=M_{y^b},
}
\tag{7}
\]

while

\[
\boxed{
E_{N,q}=I\otimes P,
\qquad
Ph=\langle \mathbf1,h\rangle\mathbf1.
}
\tag{8}
\]

Because `aq == 1 (mod N)` and `bN == 1 (mod q)`, `A` and `B` are full cyclic coordinate generators on their respective factors.

In the fresh Fourier basis `e_j(y)=y^j`, reindexing by the unit `b` makes

\[
B=S_q,
\qquad
S_q e_j=e_{j+1},
\qquad
P=|e_0\rangle\langle e_0|.
\tag{9}
\]

Thus the noncommutativity is completely explicit rather than an artifact of a later compression.

## 2. The commutator survives in norm but has fixed fresh rank

From (7)--(9),

\[
[E_{N,q},Z_{N,q}]
=A\otimes[P,S_q].
\tag{10}
\]

On the fresh factor,

\[
[P,S_q]
=|e_0\rangle\langle e_{-1}|
-|e_1\rangle\langle e_0|.
\tag{11}
\]

The two displayed partial matrix units have orthogonal initial and final spaces. Hence, for every `q>1`,

\[
\boxed{
\operatorname{rank}[E_{N,q},Z_{N,q}]=2N,
\qquad
\|[E_{N,q},Z_{N,q}]\|=1,
}
\tag{12}
\]

and its nonzero singular values are exactly `1`, with multiplicity `2N`. In particular,

\[
\boxed{
\|[E_{N,q},Z_{N,q}]\|_{HS}^2=2N,
\qquad
\frac1{Nq}\operatorname{Tr}
([E,Z]^*[E,Z])=\frac2q.
}
\tag{13}
\]

This gives the correct asymptotic interpretation. The pair does **not** become commutative in operator norm, so dismissing it by a norm-small argument would be wrong. Instead, at fixed coarse conductor the failure of commutativity occupies only two fresh Fourier links per coarse block; its normalized Hilbert-space density tends to zero.

## 3. Exact finite-level algebra: full matrix fiber, no coarse mixing

The complete algebra generated by the pair can be calculated without approximation. From (7),

\[
Z_{N,q}^q=A^q\otimes I.
\tag{14}
\]

Since `q` is a unit modulo `N`, choose `c` with `cq == 1 (mod N)`. Because `A^N=I`,

\[
\boxed{
A\otimes I=(Z_{N,q}^q)^c.
}
\tag{15}
\]

Consequently

\[
\boxed{
I\otimes B=(A^*\otimes I)Z_{N,q}
\in C^*(Z_{N,q},E_{N,q}).
}
\tag{16}
\]

Now (9) gives every fresh matrix unit:

\[
\boxed{
S_q^i P S_q^{-j}=|e_i\rangle\langle e_j|,
\qquad i,j\in\mathbb Z/q\mathbb Z.
}
\tag{17}
\]

Therefore

\[
C^*(B,P)=M_q(\mathbb C).
\tag{18}
\]

Since `A` has all `N` distinct `N`-th roots as its spectrum,

\[
C^*(A)\simeq C(\mu_N)\simeq\mathbb C^N.
\tag{19}
\]

Equations (15)--(19) prove both inclusions in

\[
\boxed{
C^*(Z_{N,q},E_{N,q})
=C^*(A)\otimes M_q(\mathbb C)
\simeq C(\mu_N)\otimes M_q(\mathbb C).
}
\tag{20}
\]

The center is exactly `C(mu_N) tensor I`. Hence the noncommuting pair can reconstruct **every** linear operator within each fresh `q`-fiber, but it cannot create any operator taking one coarse CRT point to another. This sharpens the module boundary of PC-225: retaining the internal terminal fiber before the left-unitary quotient really does recover a large noncommutative algebra, but the recovered algebra is the universal full matrix algebra of the fresh coordinate, not an arithmetic coupling between coarse fibers.

The conclusion is also a warning about spectral interpretation. Because (20) contains arbitrary matrices on each fresh fiber, an arbitrary `q`-dependent polynomial in the generators can manufacture essentially arbitrary finite spectra. Such freedom cannot count as a Prime-Circle spectral mechanism unless a specific element and its coefficients are forced independently by the source geometry.

## 4. Coprime composite control

Nothing in (4)--(20) uses that the fresh degree is prime. Let `m>1` be any integer coprime to `N`. Replacing `q` by `m` gives exactly

\[
\boxed{
C^*(Z_{N,m},E_{N,m})
\simeq C(\mu_N)\otimes M_m(\mathbb C),
}
\tag{21}
\]

with

\[
\operatorname{rank}[E_{N,m},Z_{N,m}]=2N,
\qquad
\|[E_{N,m},Z_{N,m}]\|=1,
\qquad
\frac1{Nm}\|[E,Z]\|_{HS}^2=\frac2m.
\tag{22}
\]

Thus the algebraic mechanism sees the fresh degree as the size of a cyclic fiber and nothing more. At a prime `q`, the nonconstant fresh Fourier modes coincide with all nontrivial characters of the fresh factor; for composite `m` they split further by exact conductor, but the pair `(E,Z)` does not distinguish that internal divisor decomposition. Reading primality from the externally visible matrix size would merely read the refinement label already supplied as input, not extract a new geometric invariant.

Accordingly (21) is a matched architecture control rather than a claim that prime and composite levels of different cardinalities are unitarily identical. Any mechanism that genuinely uses the exact-order decomposition of a composite fresh factor is outside this statement and must demonstrate that the additional projector is itself source-forced and survives its own controls.

## 5. Growing fresh fiber: bilateral shift plus compacts

The finite matrix algebra is large, so the relevant question is whether its canonical large-fiber limit supplies a nonclassical operator carrier. Let the coprime degree `m -> infinity` in a fixed residue class `r (mod N)`. Then the Bezout exponent `a` in (5) may be chosen fixed modulo `N`, so the coarse generator `A` is fixed up to a harmless cyclic relabelling.

Use the standard local Fourier identification of bounded cyclic indices with `ell^2(Z)`. On finitely supported vectors,

\[
S_m\longrightarrow S,
\qquad
Se_j=e_{j+1},
\tag{23}
\]

and the old projection remains

\[
P_m\longrightarrow P_0=|e_0\rangle\langle e_0|.
\tag{24}
\]

The limiting fresh algebra is therefore

\[
\mathcal B=C^*(S,P_0).
\tag{25}
\]

It has an elementary exact classification. First,

\[
S^iP_0S^{-j}=|e_i\rangle\langle e_j|,
\tag{26}
\]

so all finite-rank operators, hence all compact operators `K=K(ell^2(Z))`, lie in `B`. Conversely, every algebraic word containing at least one `P_0` is finite rank after using

\[
P_0S^kP_0=\delta_{k0}P_0,
\tag{27}
\]

while words without `P_0` are Laurent polynomials in the bilateral shift. Taking norm closures gives

\[
\boxed{
\mathcal B=C^*(S)+\mathcal K.
}
\tag{28}
\]

The bilateral shift is unitary and has spectrum `T`, so continuous functional calculus identifies

\[
C^*(S)\simeq C(\mathbb T).
\tag{29}
\]

Moreover `C^*(S) cap K={0}`. For if a nonzero `f(S)` were compact, the basis vectors `e_j` converge weakly to zero while

\[
\|f(S)e_j\|=\|f(S)e_0\|
\tag{30}
\]

by translation invariance, contradicting compactness unless `f(S)=0`.

Therefore the local fixed-base limit is

\[
\boxed{
C(\mu_N)\otimes\bigl(C^*(S)+\mathcal K\bigr),
}
\tag{31}
\]

and the fresh factor fits into the split exact sequence

\[
\boxed{
0\longrightarrow\mathcal K
\longrightarrow\mathcal B
\longrightarrow C(\mathbb T)
\longrightarrow0.
}
\tag{32}
\]

The splitting is the actual *-homomorphism

\[
f\longmapsto f(S).
\tag{33}
\]

Thus the noncommutativity that remained norm-visible in (12) becomes a compact defect over the ordinary bilateral Laurent symbol; it does not create a new bulk spectral coordinate.

## 6. No Toeplitz/Fredholm index is forced

Equation (32) is close enough in appearance to the classical Toeplitz extension that an index interpretation must be checked explicitly rather than assumed. The difference is decisive. The unilateral Toeplitz algebra is generated by a proper isometry and has the familiar compact extension whose Fredholm index records symbol winding. Here the source coordinate tends to the **bilateral unitary** `S`, and (32) splits by that unitary itself.

Indeed, let

\[
T=f(S)+K\in\mathcal B,
\qquad f\in C(\mathbb T),
\qquad K\in\mathcal K.
\tag{34}
\]

By Atkinson's theorem, `T` is Fredholm exactly when its image in the Calkin algebra is invertible, equivalently when `f` is nowhere zero on `T`. But then `f(S)` is already invertible, and `T` is only a compact perturbation of an invertible operator. Hence

\[
\boxed{
T\text{ Fredholm}\quad\Longrightarrow\quad\operatorname{ind}T=0.
}
\tag{35}
\]

So the most direct noncommuting refinement pair does **not** secretly manufacture the standard Toeplitz winding index. Any nonzero index would require an additional one-sided boundary/compression or another non-split structure; inserting such a boundary solely to obtain the index would not be forced by the present Prime-Circle geometry.

For prior-art orientation, the unilateral comparison belongs to classical Toeplitz/C*-algebra theory; see L. A. Coburn, **The C*-algebra generated by an isometry**, *Bulletin of the American Mathematical Society* 73 (1967), 722--726, DOI `10.1090/S0002-9904-1967-11845-7`. The bilateral-shift, matrix-unit and compact-ideal facts used above are standard operator theory. No novelty is claimed for those abstract ingredients. The project-specific content is their exact realization by the two source-forced Prime-Circle operators `(Z_{N,q},E_{N,q})` and the resulting closure of this explicit post-PC-239 escape.

## 7. Relation to the existing Prime-Circle boundary

PC-224 and PC-225 showed that one or many refinement/mask networks built from pullbacks, diagonal masks and conditional expectations remain module maps over the coarse diagonal algebra, so their final `T^*T` data scalarize fiberwise. They deliberately left open retaining a distinguished operation on the terminal fiber before quotienting by left unitaries. Equation (20) answers the simplest canonical version of that objection: the internal fiber can indeed become fully noncommutative, but only as `M_q` independently over each coarse point.

PC-238 then showed that the two quotient coordinates themselves generate a commutative CRT cylinder, while PC-239 showed that the original coordinate carries a ballistic Bezout winding which returns to the bilateral-shift calculus after the appropriate channel completion. The present calculation adds the old/new projector **before** that multiplication functional calculus. The commutator is genuinely nonzero, so this is not a restatement of PC-238; yet its growing-fiber closure is only the split compact extension (31), so the new noncommutativity is not a new arithmetic bulk carrier.

This closes the fixed-base route

\[
\text{canonical old/new projection}
+\text{ original Prime-Circle coordinate}
\longrightarrow
\text{noncommuting operator algebra}
\longrightarrow
\text{new RH spectral/index mechanism}
\tag{36}
\]

when the claimed novelty comes solely from the algebra generated by those two operators. The result supplies no zeta divisor, gamma factor, functional-equation involution, or distinguished real part `1/2`.

## Research consequence

Noncommutativity by itself is no longer a sufficient frontier criterion at fixed coarse conductor. The pair `(E_{N,q},M_z)` is already strongly noncommuting and even generates every fresh matrix fiber, yet its arithmetic content is exhausted by a central coarse coordinate plus a universal cyclic matrix factor; locally at growing fresh degree that factor becomes a **split** Laurent-plus-compact extension with zero Fredholm index.

A viable next operator test must therefore add structure not generated by this pair: a source-forced operator that mixes distinct coarse CRT fibers, a simultaneous `N,q -> infinity` regime where the coarse center itself grows and a nonclassical coupling survives quantitative controls, an exact-order operation whose composite-conductor behavior is essential rather than merely the old/new complement, or a genuinely unbounded/domain-sensitive/global construction. Any proposed spectral invariant should also be tested against the full-matrix freedom in (20): if the desired spectrum appears only after choosing `q`-dependent coefficients inside `M_q`, it is engineered rather than extracted from Prime-Circle geometry.