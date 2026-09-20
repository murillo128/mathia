# PC-376 — finite coprime Chebyshev transfer families are universal polydisk shifts

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the finite multi-refinement escape left open by PC-375. After the shell-2 order coordinate of PC-372 and the canonical arcsine half-density normalization of PC-374, any finite family of pairwise-coprime refinement degrees is jointly a countable-multiplicity copy of the standard coordinate shifts on a finite polydisk, plus the constant mode. The joint operator class depends only on the number of directions, not on whether the degrees are prime. In particular, every fixed finite prime family is exactly matched by a family of composite prime-power degrees, and every fixed scalar linear combination of the normalized inverse-branch transfers has a universal disk spectrum.

PC-375 showed that a single Chebyshev refinement remains a universal backward shift even after arbitrary unimodular branch twisting, but deliberately left simultaneous sums of distinct refinement directions outside its one-isometry argument. The present result tests that opening without inserting any new shell-independent weight: keep several source-forced Chebyshev refinements at once and retain their relative ranges before taking a spectral combination. The relative ranges are real, but for pairwise-coprime degrees they form the standard doubly-commuting multishift geometry, so finite multi-direction coupling still does not distinguish prime degrees.

## 1. The simultaneous Chebyshev tuple

Use the canonical arcsine completion from PC-374,

\[
\mathcal H=L^2([0,1],\mu),
\qquad
 d\mu(\lambda)=\frac{d\lambda}{\pi\sqrt{\lambda(1-\lambda)}}.
\]

With

\[
e_0=1,
\qquad
e_k(\lambda)=\sqrt2\,T_k(2\lambda-1),\quad k\ge1,
\]

we have an orthonormal basis. For the Chebyshev refinement

\[
C_m(\lambda)=\frac{1+T_m(2\lambda-1)}2,
\]

define the Koopman isometry

\[
(V_m f)(\lambda)=f(C_m(\lambda)).
\]

The composition identity for Chebyshev polynomials gives exactly

\[
\boxed{V_m e_k=e_{mk}}
\tag{1}
\]

for every `k>=0`. Hence its adjoint `P_m=V_m^*` satisfies

\[
\boxed{
P_m e_k=
\begin{cases}
e_{k/m},&m\mid k,\\
0,&m\nmid k,
\end{cases}
\qquad k\ge1,
}
\tag{2}
\]

and `P_m e_0=e_0`.

For coprime `m,n`, the refinement isometries not only commute but **doubly commute**:

\[
V_mV_n=V_nV_m=V_{mn},
\tag{3}
\]

and

\[
\boxed{V_m^*V_n=V_nV_m^*.}
\tag{4}
\]

Indeed, on `e_k`, the left side is nonzero exactly when `m|nk`. Since `(m,n)=1`, this is equivalent to `m|k`, and in that case both sides equal `e_{nk/m}`. Thus retaining several coprime refinement directions does preserve their relative ranges, but those ranges already obey the canonical relations of a doubly-commuting shift tuple.

## 2. Exact orbit decomposition into a standard polydisk shift

Fix pairwise-coprime degrees

\[
\mathbf m=(m_1,\ldots,m_d),
\qquad d<\infty.
\]

For every positive integer `k`, define

\[
a_j(k)=\max\{a\ge0:m_j^a\mid k\}.
\]

Pairwise coprimality gives the unique decomposition

\[
\boxed{
k=r\prod_{j=1}^d m_j^{a_j},
\qquad
m_j\nmid r\ \text{for every }j.
}
\tag{5}
\]

Let `R_m` be the set of such cores `r`, and set

\[
\mathcal H_r=
\overline{\operatorname{span}}
\left\{
e_{r\prod_jm_j^{a_j}}:a_1,\ldots,a_d\ge0
\right\}.
\tag{6}
\]

Every `H_r` reduces all `V_{m_j}` and all `P_{m_j}`, and

\[
\mathcal H
=
\mathbb C e_0
\oplus
\bigoplus_{r\in R_{\mathbf m}}\mathcal H_r.
\tag{7}
\]

On each `H_r`, the unitary map

\[
e_{r\prod_jm_j^{a_j}}
\longmapsto
z_1^{a_1}\cdots z_d^{a_d}
\tag{8}
\]

identifies the tuple with the coordinate shifts on `H^2(D^d)`:

\[
\boxed{
(V_{m_1},\ldots,V_{m_d})|_{\mathcal H_r}
\simeq
(M_{z_1},\ldots,M_{z_d}),
}
\tag{9}
\]

and therefore

\[
\boxed{
(P_{m_1},\ldots,P_{m_d})|_{\mathcal H_r}
\simeq
(M_{z_1}^*,\ldots,M_{z_d}^*).
}
\tag{10}
\]

For finite `d`, `R_m` is countably infinite. Consequently the entire nonconstant tuple is a countably-infinite multiplicity copy of the standard `d`-variable shift tuple. The constant mode contributes only the one-dimensional fixed representation `(1,...,1)`.

This has an immediate matched-control consequence. If `p_1,...,p_d` are distinct primes, then

\[
(P_{p_1},\ldots,P_{p_d})
\quad\text{and}\quad
(P_{p_1^2},\ldots,P_{p_d^2})
\tag{11}
\]

are jointly unitarily equivalent: both have the same fixed constant mode and countably many copies of the same `d`-variable backward shift. Thus **every finite prime refinement tuple is exactly matched by a tuple of composite refinement degrees** once the operator data are only the canonical Chebyshev refinements and their adjoints.

More generally, every fixed `*`-polynomial or finite matrix amplification with coefficients that do not themselves encode the numerical degrees has the same unitary-equivalence class for all pairwise-coprime `d`-tuples. Prime labels cannot re-enter through a finite operator word after this quotient.

## 3. Finite sums have an exact universal disk spectrum

The explicit model gives a stronger statement for the most natural multi-direction repair of PC-375. Let

\[
A_{\mathbf a}
=
\sum_{j=1}^d a_jP_{m_j},
\qquad a_j\in\mathbb C,
\tag{12}
\]

and write

\[
R=\sum_{j=1}^d|a_j|.
\]

On one copy of `H^2(D^d)`, the reproducing kernel `k_w`, `w in D^d`, satisfies

\[
M_{z_j}^*k_w=\overline{w_j}k_w.
\]

Hence

\[
\left(\sum_j a_jM_{z_j}^*\right)k_w
=
\left(\sum_ja_j\overline{w_j}\right)k_w.
\tag{13}
\]

As `w` ranges over the open polydisk, the scalar on the right ranges over the open disk of radius `R`. Therefore the spectrum contains that open disk and, being closed, its closure. Conversely,

\[
\|A_{\mathbf a}\|
\le\sum_j|a_j|=R,
\]

so no spectral point can lie outside it. The fixed constant mode contributes the eigenvalue `sum_j a_j`, already inside the same disk. Thus

\[
\boxed{
\sigma(A_{\mathbf a})
=
\{z\in\mathbb C:|z|\le\sum_j|a_j|\}.
}
\tag{14}
\]

In particular,

\[
\boxed{
\sigma\left(\frac1d\sum_{j=1}^dP_{m_j}\right)
=\overline{\mathbb D}
}
\tag{15}
\]

for every finite pairwise-coprime family. The relative positions of the ranges do not create a prime-sensitive spectral boundary: their scalar sum is exactly the same disk for prime and composite controls.

## 4. The half-density transfer family inherits the same collapse

PC-374 proved that on the canonical half-density line `Re(s)=1/2` the Chebyshev inverse-branch transfer satisfies

\[
\mathcal L_{m,s}
=
m^{1-s}J_s^{-1}P_mJ_s,
\tag{16}
\]

where the **same** `J_s` is unitary for every degree `m`. Therefore the normalized operator

\[
\widehat{\mathcal L}_{m,s}
:=m^{s-1}\mathcal L_{m,s}
=J_s^{-1}P_mJ_s
\tag{17}
\]

inherits the entire simultaneous tuple model, not merely the one-map spectrum. For any pairwise-coprime finite family,

\[
\boxed{
\sigma\left(
\sum_j a_j\widehat{\mathcal L}_{m_j,s}
\right)
=
\left\{z:|z|\le\sum_j|a_j|\right\},
\qquad \Re s=\frac12.
}
\tag{18}
\]

Even the unnormalized canonical sum has no hidden cancellation in the imaginary direction. At `s=1/2+it`, equation (16) and (14) give

\[
\boxed{
\sigma\left(
\sum_j a_j\mathcal L_{m_j,1/2+it}
\right)
=
\left\{z:|z|\le
\sum_j|a_j|\sqrt{m_j}
\right\}.
}
\tag{19}
\]

The phases `m_j^{-it}` disappear completely from the spectral set. Numerical degree survives only through the positive scalar radii `sqrt(m_j)`, exactly the degree factor already isolated in PC-373; no ordinate-dependent cancellation, zeta-zero condition, or additional critical-line selector remains in the finite scalar spectrum.

Thus the obvious repair

\[
\text{several Chebyshev refinement directions}
\longrightarrow
\text{sum their inverse-branch transfers}
\longrightarrow
\text{look for a new spectrum}
\]

is now closed at the canonical half-density completion.

## 5. The full prime family is the classical Bohr/infinite-polydisk representation

The finite matched-control statement should not be overextended to an infinite tuple: the family of all prime shifts has additional global cyclic structure. But that structure is already classical rather than a new Prime-Circle object.

On the nonconstant sector, unique prime factorization gives

\[
k=\prod_p p^{\nu_p(k)}.
\]

The unitary Bohr map

\[
e_k
\longmapsto
\prod_p z_p^{\nu_p(k)}
\tag{20}
\]

identifies `l^2(N)` with the Hardy space on the infinite polytorus/infinite polydisk and sends

\[
\boxed{V_p\longmapsto M_{z_p},\qquad P_p\longmapsto M_{z_p}^*.}
\tag{21}
\]

This is precisely the Hardy/Dirichlet-series model already anchored in `SOURCES.md` by Hedenmalm--Lindqvist--Seip and used in PC-174's multiplicative-Toeplitz classification. It is also the same multiplication-semigroup representation that PC-242 identifies with the canonical Bost--Connes representation once the rational rotations and logarithmic number Hamiltonian are added.

Accordingly, passing from one Chebyshev direction to all prime directions does recover the free prime-coordinate factorization of the integer index, but not a new geometric coupling among those directions. A zeta-bearing scalar can be produced by adding degree/energy weights such as `p^{-s}` or `log p`; those are precisely the classical Dirichlet/Bost--Connes ingredients already separated from embedded shell geometry in earlier Prime-Circle findings.

## 6. Prior art and novelty audit

No novelty is claimed for coordinate shifts on a polydisk, doubly-commuting multishifts, the Bohr lift, or Hardy spaces of Dirichlet series. The line already records Håkan Hedenmalm, Peter Lindqvist and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)**, *Duke Mathematical Journal* 86:1 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, as the primary infinite-polydisk/Dirichlet-series anchor. PC-174 further identifies Prime-Circle weak refinement with classical multiplicative Toeplitz structure, and PC-242 identifies the canonical positive-frequency multiplication semigroup with Bost--Connes dynamics.

The durable project-local contribution here is narrower: equations (5)--(10) explicitly classify the **simultaneous shell-2 Chebyshev refinements produced by PC-372**, equation (11) supplies a matched composite control for every finite prime family, and equations (14)--(19) show that the finite multi-direction spectral sum left open by PC-375 is a universal disk even after the canonical half-density transfer normalization. This is a new restriction on the Prime-Circle search, not a claim that the underlying operator theory is new.

A targeted literature check also finds the expected classical several-variable Wold theory for doubly-commuting isometries; that agreement strengthens the classicalization rather than supplying a new arithmetic mechanism. The exact decomposition needed here is elementary and is given explicitly above, so no additional literature theorem is load-bearing for the claim.

## 7. Boundary of the obstruction

Pairwise coprimality is load-bearing. It gives the double-commutation relation (4) and the independent exponent decomposition (5). This covers distinct prime directions and the composite prime-power controls used in (11), but it does not classify arbitrary overlapping composite degrees.

The result also assumes the canonical unweighted Chebyshev refinement tuple, or the PC-374 half-density transfers after their forced scalar degree factor is separated. A coefficient chosen explicitly as a function of the numerical degree can of course distinguish `p` from `p^2`, but that information is then inserted through the coefficient rather than generated by the relative range geometry. Such degree-weighted Dirichlet constructions require their own source-forcing argument and remain subject to the classical Dirichlet/Bost--Connes prior-art boundary.

Most importantly, PC-376 does **not** classify source-forced non-unimodular branch amplitudes, branch cocycles whose compatibility couples different refinements, genuinely infinite global operations that use the cyclic structure of the complete prime family, cross-shell matrix couplings before the shell-2 Chebyshev quotient, nonlinear interactions, or noncanonical domains/boundary conditions. Those are outside the unitary model proved here.

The exact result has direct audit tests. A failure would require one of the following: a coprime pair for which (4) fails; a positive mode with two distinct decompositions of the form (5); a finite prime tuple not jointly unitarily equivalent to its prime-square control; or a coefficient-independent finite operator word in the tuple whose unitary invariant differs between those controls. Equations (1)--(10) exclude all four within the stated hypotheses.

## 8. Consequence for the Prime-Circle/RH search

The finite multi-direction loophole left by PC-375 is substantially narrower than it appeared. Keeping several refinement ranges simultaneously does not by itself supply a new prime-sensitive interaction. For every finite set of prime directions, the entire canonical operator tuple is the same standard polydisk shift tuple obtained from composite prime-power controls, and its scalar transfer sums have a disk spectrum that discards even the `m^{-it}` phases on the half-density line.

Therefore a surviving order/refinement mechanism must use structure not contained in a fixed finite tuple of canonical Chebyshev pullbacks/adjoints with source-independent coefficients. The live boundary is pushed toward genuinely source-forced non-unimodular amplitudes or cocycles, infinite global coupling with an independently forced topology/domain, or cross-shell/nonlinear operators formed before the Chebyshev quotient. Merely adding more finite refinement directions does not escape the classical shift model.