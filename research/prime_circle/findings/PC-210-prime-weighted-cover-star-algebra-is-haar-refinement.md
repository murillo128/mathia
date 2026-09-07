# PC-210 — prime weighted-cover star algebra is Haar refinement

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the cross-level refinement branch left open by PC-209: compose the intrinsic cyclotomic-weighted power covers across several levels, allow adjoints/transfer back from refined fibers, and ask whether the resulting prime-generated operator algebra retains geometric information that is absent from the abstract multiplicative refinement tower.

PC-209 classifies one same-level operator

\[
W_n:=M_{\Phi_n}C_n,
\qquad
(C_nf)(z)=f(z^n),
\]

up to unitary equivalence, but deliberately leaves genuinely cross-level products, adjoints, and infinite-depth organization outside its theorem. The prime generators admit a stronger exact reduction: after the normalization already forced by PC-209, they are precisely the ordinary integer Haar-refinement isometries. Their finite products telescope by multiplication of the refinement scale, their adjoint overlaps are rational-dilation block averages, and their canonical infinite-depth prefixes have only the weak zero limit. No primitive-root placement survives in this prime-generated star algebra.

## 1. Prime shell weights are exactly Haar refinement masks

Put

\[
S_n(z):=1+z+\cdots+z^{n-1}=\frac{z^n-1}{z-1}
\]

and define

\[
H_n:=\frac1{\sqrt n}M_{S_n}C_n.
\tag{1}
\]

For every prime `p`,

\[
\Phi_p(z)=S_p(z),
\qquad
\|\Phi_p\|_{H^2}^2=p.
\]

Therefore the normalized PC-209 operator at a prime level is not merely unitarily equivalent to a standard isometry: it is exactly

\[
\boxed{
V_p:=p^{-1/2}W_p=H_p.
}
\tag{2}
\]

On the Hardy basis `e_k(z)=z^k`,

\[
\boxed{
H_ne_k=\frac1{\sqrt n}\sum_{j=0}^{n-1}e_{nk+j}.
}
\tag{3}
\]

Thus a coefficient is simply copied uniformly into the `n` consecutive children of its refinement block. This description uses no roots of unity, primitive residues, chord data, or cyclotomic coefficients.

## 2. Prime refinement paths telescope exactly

The geometric-series masks satisfy the elementary refinement identity

\[
S_m(z)S_n(z^m)
=\frac{z^m-1}{z-1}\frac{z^{mn}-1}{z^m-1}
=S_{mn}(z).
\tag{4}
\]

Using `C_mM_g=M_{g(z^m)}C_m`, equation (4) gives

\[
\boxed{
H_mH_n=H_{mn}=H_nH_m.
}
\tag{5}
\]

Consequently, for any finite list of primes `p_1,...,p_r`, with repetitions allowed and

\[
N=\prod_{j=1}^r p_j,
\]

we have the exact, order-independent identity

\[
\boxed{
V_{p_1}\cdots V_{p_r}=H_N.
}
\tag{6}
\]

Before normalization this says

\[
\boxed{
W_{p_1}\cdots W_{p_r}
=M_{S_N}C_N.
}
\tag{7}
\]

So an ordered prime refinement path carries no commutator, cocycle, or holonomy at this scalar weighted-cover level: every factorization path with the same product ends at the same operator.

The cyclotomic meaning of the telescoping is also exact. Since

\[
S_N(z)=\prod_{\substack{d\mid N\\d>1}}\Phi_d(z),
\tag{8}
\]

a prime-by-prime path does not preserve only the primitive shell at the final level; it accumulates **all** nontrivial divisor shells. Comparing it with the direct composite primitive operator gives

\[
\boxed{
M_{S_N}C_N
=M_{R_N}W_N,
\qquad
R_N(z):=\frac{S_N(z)}{\Phi_N(z)}
=\prod_{\substack{d\mid N\\1<d<N}}\Phi_d(z).
}
\tag{9}
\]

For composite `N`, `R_N` is exactly the polynomial of the old nontrivial `N`-th roots. Thus the discrepancy between the direct primitive shell and the composed prime path is the classical old-layer divisor factor, not a new refinement phase.

## 3. Every finite weighted-cover word still collapses abstractly

The previous telescoping is special to prime generators, but the finite-word obstruction is more general. For arbitrary conductors `n_1,...,n_r>=2`, let

\[
A_{\mathbf n}:=W_{n_1}\cdots W_{n_r},
\qquad
N_j:=\prod_{i=1}^j n_i,
\qquad
N_0:=1.
\]

Repeated covariance gives

\[
A_{\mathbf n}=M_{G_{\mathbf n}}C_{N_r},
\qquad
G_{\mathbf n}(z)
=\prod_{j=1}^r\Phi_{n_j}\!\left(z^{N_{j-1}}\right).
\tag{10}
\]

Its degree obeys

\[
\deg G_{\mathbf n}
=\sum_{j=1}^r N_{j-1}\varphi(n_j)
\le\sum_{j=1}^rN_{j-1}(n_j-1)
=N_r-1.
\tag{11}
\]

Hence the complete product still fits inside one covering block. If

\[
h_n:=\|\Phi_n\|_{H^2}^2,
\]

then PC-209 gives `W_n^*W_n=h_nI`, and therefore

\[
\boxed{
A_{\mathbf n}^*A_{\mathbf n}
=\left(\prod_{j=1}^r h_{n_j}\right)I.
}
\tag{12}
\]

Equivalently, equation (10) yields the exact coefficient-energy identity

\[
\boxed{
\|G_{\mathbf n}\|_{H^2}^2
=\prod_{j=1}^r h_{n_j}.
}
\tag{13}
\]

The multiplier `G_{\mathbf n}` has constant term `1`, positive degree, and degree `<N_r`. The same block/Wold argument as PC-209 therefore applies to the whole word and gives

\[
\boxed{
A_{\mathbf n}
\simeq
\left(\prod_{j=1}^r h_{n_j}\right)^{1/2}
S^{(\aleph_0)}.
}
\tag{14}
\]

Thus even when composite labels make concrete products order-dependent, **every finite product spectrum and abstract unitary class forgets that order** and retains only the product of the already-classical coefficient energies. For example `W_2W_4` and `W_4W_2` have different multipliers, so there is genuine concrete noncommutativity, but equation (14) assigns them the same complete abstract operator class. A finite cross-level product cannot evade PC-209 merely by being longer.

## 4. Adjoint transfer between prime refinements is rational dilation geometry

The next possible escape is to keep the prime refinement isometries and their adjoints jointly rather than compressing a word to one forward weighted composition operator. Equations (2)--(5) still remove the cyclotomic geometry before this star algebra is formed.

Let

\[
J:\ell^2(\mathbb N_0)\longrightarrow L^2(\mathbb R_+)
\]

be the isometric embedding

\[
Je_k=\mathbf 1_{[k,k+1)}.
\]

For `a>0`, define the ordinary unitary dilation

\[
(D_af)(x)=a^{-1/2}f(x/a).
\tag{15}
\]

Equation (3) is exactly

\[
\boxed{
JH_n=D_nJ.
}
\tag{16}
\]

Hence for any positive integers `m,n`,

\[
\boxed{
H_m^*H_n=J^*D_{n/m}J.
}
\tag{17}
\]

The matrix entries have the completely elementary interval-overlap form

\[
\boxed{
\langle e_a,H_m^*H_ne_b\rangle
=\frac{L_{m,n}(a,b)}{\sqrt{mn}},
}
\tag{18}
\]

where

\[
L_{m,n}(a,b)
=\max\!\left(
0,
\min(m(a+1),n(b+1))-\max(ma,nb)
\right).
\tag{19}
\]

Thus the first nontrivial transfer packet produced by interleaving an adjoint is merely the compression of the rational dilation `n/m` to unit-step functions. It depends on integer block overlaps and the rational ratio `n/m`, not on primitive residues or root positions.

Since every `H_N` is a product of the prime `H_p`, equation (5) also gives

\[
\boxed{
C^*(V_p:p\text{ prime})=C^*(H_n:n\ge2).
}
\tag{20}
\]

The right-hand side can be defined entirely from the subdivision rule (3), without mentioning the prime-circle. Its more elaborate star words may of course have nontrivial operator algebra, but any such structure is inherited from universal integer Haar refinement/rational dilation geometry. It cannot be credited as a geometric prime-circle mechanism merely because the semigroup was generated by prime birth levels.

## 5. The canonical infinite-depth prime path has no nonzero operator limit

Let `N_1|N_2|...` be any divisibility chain with `N_r -> infinity`; in particular, `N_r` may be the running product of an arbitrary infinite prime sequence. Equation (5) implies

\[
H_{N_{r+1}}H^2\subset H_{N_r}H^2.
\]

From (3), the range of `H_N` consists of coefficient sequences that are constant on every consecutive block of length `N`. Therefore

\[
\boxed{
\bigcap_{r\ge1}H_{N_r}H^2=\{0\}.
}
\tag{21}
\]

Indeed, a vector in the intersection is constant on the initial block of length `N_r` for every `r`; square summability forces that common value to be zero, and every fixed coordinate eventually lies in such an initial block.

Consequently the range projections satisfy

\[
H_{N_r}H_{N_r}^*\longrightarrow0
\qquad\text{strongly}.
\tag{22}
\]

Also

\[
\boxed{
H_{N_r}\longrightarrow0
\qquad\text{in the weak operator topology},
}
\tag{23}
\]

while no `H_{N_r}` can converge strongly to zero because each is an isometry. Thus the canonical normalized infinite prime-refinement prefix does not produce a new nonzero limiting operator. A nontrivial infinite-depth object must retain additional state/algebra, change the normalization, or add a genuinely different fiber coupling; those are extra structures that require their own geometric justification and novelty audit.

## 6. Prior-art and novelty audit

Nothing in the abstract refinement mechanism is new. The factorization of `z^N-1` into cyclotomic polynomials and the identities for `S_n` are classical. PC-010 already records that the roots-of-unity tower with the positive-integer power action is the Bost--Connes cyclotomic refinement system, so a multiplicative-semigroup effect by itself is explicitly excluded from Prime-Circle novelty.

The operator realization above is equally classical in character. Integer-scale refinement equations, characteristic-function scaling functions, and Haar multiresolution are standard wavelet theory. Ding-Xuan Zhou, *Stability of Refinable Functions, Multiresolution Analysis, and Haar Bases*, SIAM J. Math. Anal. 27:3 (1996), 891--904, DOI `10.1137/0527047`, explicitly treats `k`-scale refinement (`k>=2`) and classifies the associated characteristic-function multiresolution analyses. The `n`-child constant mask in (3) is precisely this elementary Haar subdivision architecture. Semigroup operator algebras over the positive integers and their relation to Bost--Connes/`ax+b` systems are likewise established terrain; for neighboring operator-algebra context see Joachim Cuntz, *C*-algebras associated with the ax+b-semigroup over N* (2008), DOI `10.4171/060-1/8`.

No novelty is claimed for Haar refinement, dilation operators, semigroup `C*`-algebras, cyclotomic factorization, or Bost--Connes dynamics. The durable contribution here is the **project-local exact obstruction**: once the source-forced weighted-cover construction is generated at prime shell levels, the cyclotomic weights themselves telescope into the universal Haar mask before finite products, adjoints, or canonical infinite-depth limits can extract a new geometric invariant.

## 7. Falsification boundary and research consequence

This result does **not** identify a no-go for every cross-level Prime-Circle operator. It specifically closes the algebra generated by the scalar prime weighted covers `W_p` and their adjoints, and it classifies every finite forward word of arbitrary `W_n` at the abstract-operator level.

The direct composite primitive operator `W_N` remains different from the prime-path operator `M_{S_N}C_N` when `N` is composite; equation (9) says that their discrepancy is exactly the old-layer factor. A construction that retains **both** direct composite primitive data and refinement-path data, or couples old/new fibers nontrivially before the Haar collapse, is not ruled out. Matrix-valued/non-Haar fiber sectors, genuinely growing tensor structure, nonlinear renormalization forced by the geometry, and global uniformization/monodromy also remain outside the theorem.

In particular, the accepted preimage/fiber-sector clue is not resolved by PC-210: that clue already requires a non-Cauchy/non-scalar sector that survives the simple finite weighted-composition reduction. What PC-210 removes is the tempting intermediate repair

\[
\boxed{
\text{prime shell weights}
\to
\text{cross-level weighted-cover products/adjoints}
\to
\text{refinement cocycle or infinite-depth spectrum}
\to
\text{new RH mechanism},
}
\]

when the state is only the scalar prime weighted-cover star algebra. At that level the exact geometry has already become universal Haar refinement, and any zeta-bearing multiplicative-semigroup structure is inherited prior art rather than a new Prime-Circle bridge.
