# PC-238 — joint coarse-fresh quotient calculus is a commutative CRT cylinder

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the bounded regular **coupled coarse/fresh operator** escape left explicitly open by PC-236 and PC-237. At a fixed coarse conductor `N`, adjoining one fresh prime `q` supplies two canonical quotient coordinates on the same refined polygon: `z^q in mu_N` and `z^N in mu_q`. Keeping them jointly before packet separation does mix coarse packet centers and fresh packet indices, but the exact CRT decomposition shows that their operator algebra is already the tensor product of one finite cyclic shift with one fresh cyclic shift. Along `q -> infinity` in a fixed residue class, the latter becomes the bilateral shift of PC-235 while the former remains finite. Every uniformly bounded family of joint observables that is equicontinuous at the fresh-fiber scale therefore has accumulation operators in

\[
\boxed{
C^*(R_N,S)\cong C(\mu_N\times\mathbb T)
\cong\bigoplus_{a=0}^{N-1}C(\mathbb T),
}
\]

which is commutative and independent of primality. Thus coupling the **two intrinsic quotient coordinates** before packet separation does not by itself create the noncommuting or growing carrier sought by the Prime-Circle mandate.

A particularly geometric control is the coupled quotient chord

\[
|z^q-z^N|^2.
\]

Its operator is exactly `2I-U^*V-V^*U`, with `U=M_{z^q}` and `V=M_{z^N}`. Since `gcd(N-q,Nq)=1`, `U^*V=M_{z^{N-q}}` is merely a generator of the full regular `Nq`-gon. Consequently the apparently two-scale coupled chord has exactly the ordinary regular-polygon spectrum

\[
\boxed{
\left\{4\sin^2\!\frac{\pi k}{Nq}:0\le k<Nq\right\},
}
\]

and its limiting spectrum is `[0,4]`. The same statement holds with `q` replaced by any integer coprime to `N`, so even this most direct joint geometric observable is prime-blind.

This does **not** classify `q`-mesh-resolving/non-equicontinuous joint profiles, original-coordinate observables whose CRT exponents grow with `q`, simultaneous `N,q -> infinity`, old/new operators that are not multiplication-functional calculus of the quotient coordinates, genuinely noncommuting operators added before the diagonal coordinate algebra, or global uniformization/accessory data.

## 1. The two source-forced quotient coordinates have an exact CRT tensor form

Fix `N>1`, let `q` be prime with `q \nmid N`, and put

\[
M=Nq.
\tag{1}
\]

On the full refined polygon `mu_M`, define the two canonical coordinate multipliers

\[
(U_{N,q}F)(z)=z^qF(z),
\qquad
(V_{N,q}F)(z)=z^NF(z).
\tag{2}
\]

The first remembers the coarse `N`-th-root quotient and the second the fresh `q`-th-root quotient. They are forced by the two power maps in the refinement square; no coefficient choice is involved. They satisfy

\[
U_{N,q}^N=I,
\qquad
V_{N,q}^q=I,
\qquad
U_{N,q}V_{N,q}=V_{N,q}U_{N,q}.
\tag{3}
\]

In the normalized Fourier basis `e_k`, multiplication by a monomial shifts the Fourier label, hence

\[
\boxed{
U_{N,q}e_k=e_{k+q},
\qquad
V_{N,q}e_k=e_{k+N}.
}
\tag{4}
\]

Write

\[
r=q\bmod N
\tag{5}
\]

and let `Nbar` be the inverse of `N modulo q`. The CRT label

\[
\boxed{
k\longmapsto
(b,n)=\bigl(k\bmod N,\;\overline N k\bmod q\bigr)
}
\tag{6}
\]

is a bijection from `Z/(Nq)Z` to `Z/NZ x Z/qZ`. In these coordinates, (4) becomes exactly

\[
\boxed{
U_{N,q}:(b,n)\mapsto(b+r,n),
\qquad
V_{N,q}:(b,n)\mapsto(b,n+1).
}
\tag{7}
\]

Therefore, after the CRT Fourier identification,

\[
\boxed{
U_{N,q}=R_r\otimes I,
\qquad
V_{N,q}=I\otimes S_q,
}
\tag{8}
\]

where `R_r` is translation by `r` on `ell^2(Z/NZ)` and `S_q` is the cyclic unit shift on `ell^2(Z/qZ)`. Since `r` is a unit modulo `N`, `R_r` is conjugate to the standard `N`-cycle. There is no carry cocycle, projective phase, or hidden associator in the joint quotient action.

The same conclusion is visible in the vertex basis. The map

\[
\boxed{
\mu_{Nq}\longrightarrow\mu_N\times\mu_q,
\qquad
z\longmapsto(z^q,z^N)
}
\tag{9}
\]

is a group isomorphism: its kernel consists of roots satisfying both `z^q=1` and `z^N=1`, hence is trivial because `(N,q)=1`, and both sides have `Nq` elements. Thus the two quotient coordinates together generate the full diagonal algebra of the refined polygon, but they generate it as an **abelian CRT product**, not as a new relational noncommutative algebra.

## 2. Fixed-base packet limit is a finite cyclic factor times the bilateral shift

PC-227 proves that the mode-resolved one-mask transfer at fixed `N` concentrates near finitely many coarse cyclotomic poles and, after canonical local identification, each nonzero component converges in `ell^2` to a shifted Cauchy packet. PC-235 identifies the fresh coordinate `V_{N,q}` on those packets with the bilateral shift

\[
(Sf)(j)=f(j+1).
\tag{10}
\]

Equation (8) gives the missing joint-coordinate statement without any additional asymptotic calculation. The coarse quotient operator does not acquire a new infinite coordinate: it remains the fixed finite translation `R_r`, while the fresh quotient gives `S_q -> S` on the packet windows. Enlarging the packet model by the finitely many coarse translates needed for `R_r` therefore yields

\[
\boxed{
(U_{N,q},V_{N,q})
\longrightarrow
(R_r,S)
}
\tag{11}
\]

on the source-forced packet sector along every fixed residue class `q = r (mod N)`.

The finite and infinite translations in (11) commute. Consequently the C*-algebra generated by the joint limit is the reduced/full group C*-algebra of the discrete abelian group `Z/NZ x Z`, hence by Pontryagin/Gelfand-Fourier duality

\[
\boxed{
C^*(R_r,S)
\simeq C^*(\mathbb Z/N\mathbb Z\times\mathbb Z)
\simeq C(\mu_N\times\mathbb T).
}
\tag{12}
\]

The dependence on `r` only permutes the finite cyclic factor. It does not change the isomorphism class or introduce a prime-specific phase.

## 3. Arbitrary regular coarse-fresh coupling still closes in the same commutative algebra

The previous section is not restricted to separable observables `A(z^q)B(z^N)`. Let

\[
F_q:\mu_N\times\mathbb T\to\mathbb C
\tag{13}
\]

be a family uniformly bounded in sup norm and uniformly equicontinuous in the circle variable, with no restriction on its dependence on the finite coarse coordinate. Define the exact refined-level observable by joint functional calculus,

\[
B_{N,q}=F_q(U_{N,q},V_{N,q}).
\tag{14}
\]

At finite `q`, only the values on `mu_N x mu_q` matter, so (14) includes every bounded scalar interaction of the two quotient coordinates whose sampled profile comes from such a regular family.

Because `mu_N` is finite, Arzela--Ascoli applies componentwise. Every sequence contains a subsequence for which

\[
\|F_q-F\|_\infty\longrightarrow0
\tag{15}
\]

for some `F in C(mu_N x T)`. Uniform trigonometric approximation on each of the finitely many circle components gives a fixed finite polynomial

\[
P(c,w)=
\sum_{a\bmod N}\sum_{|h|\le H}p_{a,h}c^aw^h
\tag{16}
\]

approximating `F` arbitrarily well. Functional calculus gives the corresponding uniform operator-norm bound at every finite `q`. For the fixed polynomial (16), PC-235 supplies convergence of the fresh shifts while (8) handles the coarse shifts exactly. Hence on every PC-227 packet state,

\[
\boxed{
F_q(U_{N,q},V_{N,q})
\longrightarrow
F(R_r,S)
}
\tag{17}
\]

along that subsequence, in the same packet sense used by PC-236.

Therefore every accumulation operator of a bounded equicontinuous **joint** quotient observable lies in (12). Several such observables retained simultaneously still commute before any compression, and after diagonalizing the finite cyclic factor they are simply `N` scalar continuous functions of one bilateral-shift spectral variable. Joint dependence can mix the coarse packet labels in the Fourier representation, but it does not create a growing matrix size, a second continuous spectral dimension, or a noncommutative fiber algebra.

This strictly strengthens PC-236 in one direction: equicontinuity need not hold for one fresh-coordinate profile independent of the coarse sector. The profile may depend arbitrarily and nonseparably on the coarse quotient `z^q`; the exact CRT action still leaves only a finite direct sum of the same bilateral-shift calculus.

## 4. The coupled quotient chord is exactly an ordinary polygon chord

A direct geometric stress test is to compare the two quotient images of the same refined vertex. Their squared Euclidean chord is

\[
\begin{aligned}
|z^q-z^N|^2
&=(z^q-z^N)(z^{-q}-z^{-N})\\
&=2-z^{N-q}-z^{q-N}.
\end{aligned}
\tag{18}
\]

Accordingly its multiplication operator is

\[
\boxed{
L_{N,q}^{\rm cross}
=2I-U_{N,q}^*V_{N,q}-V_{N,q}^*U_{N,q}.
}
\tag{19}
\]

Now

\[
\gcd(N-q,Nq)=1,
\tag{20}
\]

because any common divisor of `N-q` with `N` divides `q`, and any common divisor with `q` divides `N`; `(N,q)=1`. Thus the power map

\[
z\mapsto z^{N-q}
\tag{21}
\]

permutes all `Nq` roots of unity. Hence `U^*V=M_{z^{N-q}}` is unitarily just the standard full-cycle coordinate multiplier. It follows immediately that

\[
\boxed{
\operatorname{Spec}(L_{N,q}^{\rm cross})
=
\left\{
4\sin^2\left(\frac{\pi k}{Nq}\right):
0\le k<Nq
\right\}.
}
\tag{22}
\]

No arithmetic of the fresh prime remains. The same proof works for every integer `m` coprime to `N`, replacing `q` by `m`. Thus this source-native observable passes an especially strong matched-composite control: the nominally coupled two-scale chord is exactly a relabelled one-scale regular-polygon chord before any limit is taken.

As `q -> infinity`, (22) fills `[0,4]`, agreeing with the spectrum of the cylinder-limit operator

\[
2I-R_r^*S-S^*R_r.
\tag{23}
\]

Since `R_r` has finite root-of-unity spectrum and `S` has spectrum `T`, the product `R_r^*S` again has the full circle as spectrum. The limiting cross-chord therefore supplies no discrete divisor or special half-line condition.

## 5. Stress tests and exact boundary

The result is prime-blind at its algebraic core. Equations (6)--(9) need only `(N,m)=1`, not primality of the new factor. A matched coprime composite refinement has the same tensor decomposition, the same commutative quotient algebra, and the same coupled-chord relabelling. Any claimed prime discriminator inside this regular joint-coordinate class therefore fails before one asks about RH.

The theorem also does not hide a noncommutative effect behind a change of basis. `U` and `V` commute exactly at every finite level, not merely asymptotically. A Fourier/packet representation may make either operator look like a translation between sectors, but their commutator is identically zero. Any noncommutativity obtained by compressing them to a chosen non-invariant subspace is therefore a compression effect; at fixed `N` its source dimension is bounded and it is not a new growing coordinate algebra by itself.

The equicontinuity condition in Section 3 is essential. Since (9) is a bijection, **arbitrary** functions on the finite CRT grid can encode arbitrary `q`-dependent information. In particular the original refined coordinate `z` can be reconstructed from `(z^q,z^N)` using Bezout exponents, but those exponents vary with `q`; when expressed as a profile on `mu_N x T` this can have fresh-frequency winding that grows with `q`. Such `q`-mesh-resolving profiles are deliberately outside (17). Treating their arbitrary finite-grid freedom as a spectral discovery would merely choose information by hand; a surviving Prime-Circle route must show that a specific non-equicontinuous dependence is **forced by the embedded old/new or chord geometry** and retains arithmetic information under matched controls.

Also outside the theorem are simultaneous `N,q -> infinity`, operators coupling different old/new subspaces that are not scalar functions of `(z^q,z^N)`, singular renormalizations whose fresh modulus degenerates with `q`, genuinely noncommuting differential/transfer operators applied before the coordinate functional calculus, and global uniformization/accessory data.

## 6. Prior art and novelty audit

The abstract mathematics of the collapse is classical. The Chinese remainder theorem gives the finite product in (6)--(9); Fourier analysis of finite cyclic products gives (7)--(8). Pontryagin duality identifies the duals of finite cyclic groups and `Z`, and the standard Gelfand-Fourier theorem for a discrete abelian group `G` identifies its group C*-algebra with continuous functions on the compact dual. In the present case this is exactly

\[
C^*(\mathbb Z/N\mathbb Z\times\mathbb Z)
\cong C(\mu_N\times\mathbb T).
\]

Standard references include the classical Pontryagin-duality literature summarized by the *Encyclopedia of Mathematics*, **Pontryagin duality**, https://encyclopediaofmath.org/wiki/Pontryagin_duality, and the general commutative group-C*-algebra framework; Y. Kuznetsova, **A duality of locally compact groups which does not involve the Haar measure**, arXiv:1201.5023, explicitly places `C_0(G)` and `C^*(G)` in the locally compact group duality setting. The finite-cyclic Fourier/circulant and uniform trigonometric-approximation ingredients are the same classical machinery already audited in PC-236 through Davis and Katznelson.

No historical novelty is claimed for CRT, cyclic shifts, Pontryagin duality, abelian group C*-algebras, or Arzela--Ascoli/Stone--Weierstrass approximation. A directed prior-art search found no reason to interpret their combination as a new spectral mechanism. The project-specific durable content is narrower: the **two quotient coordinates forced by one Prime-Circle refinement step are exactly the two CRT regular translations**, so the explicit coupled-coarse/fresh escape left by PC-236/237 classicalizes to a finite cyclic factor times the already-known bilateral packet shift.

The result also supplies no zeta factor, gamma factor, functional equation, zero divisor, or distinguished real part `1/2`. Adding such data through `F_q` would be external unless an independently derived Prime-Circle construction forces it.

## 7. Consequence for the live Prime-Circle frontier

The route

\[
\boxed{
\text{PC-227 fixed-base packets}
\longrightarrow
\text{bounded regular joint function of }(z^q,z^N)
\longrightarrow
\text{coarse/fresh sector coupling before separation}
\longrightarrow
\text{new RH-facing operator carrier}
}
\]

is closed. The finite coarse coordinate does not turn the fresh bilateral shift into a new noncommutative object; it only forms the classical CRT cylinder `mu_N x T`. Even the most direct quotient-to-quotient chord is exactly a relabelled ordinary polygon chord and survives a matched composite control unchanged.

The surviving fixed-base frontier is therefore narrower: a candidate must use a **source-forced `q`-scale/non-equicontinuous dependence**, an old/new or transfer operator not contained in scalar joint quotient functional calculus, or a genuinely noncommuting operator inserted before that scalarization. Beyond fixed base, simultaneous conductor growth and global uniformization/accessory data remain outside this no-go theorem.