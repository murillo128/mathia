# PC-114 — new-prime Hardy two-scale corrector is a Ramanujan reflection tensor

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-113 proves that, after adjoining one new prime `p\nmid q` to a fixed conductor `q`, the genuinely new-prime Hardy term `G_{p,q}` vanishes strongly under the ordinary `p`-mesh microlocalization. That leaves the same escape that occurred between PC-108 and PC-109: the term may carry nonzero Schatten mass in a rapidly oscillating microscopic coordinate that strong convergence forgets.

The canonical two-scale unfolding of the `q`-periodic oscillation can be computed exactly. After splitting the new-prime residue as `r=qk+i`, retaining the fast class `i mod q`, resolving the slow coordinate `k`, and applying the forced finite gauge coming from `p mod q`, one has

\[
\boxed{
\widetilde G_{p,q}
\xrightarrow[p\to\infty,\ p\nmid q]{\mathcal S_2}
S_q\otimes\mathcal K,
}
\]

where `\mathcal K` is exactly the universal off-origin Carleman--Hilbert defect of PC-109/110 and

\[
\boxed{
(S_q)_{ij}=\frac1q\,c_q(i+j+1),
\qquad 0\le i,j<q.
}
\]

The finite factor is not a new arithmetic channel. If

\[
(P_q)_{ij}=\frac1q\,c_q(i-j),
\]

then `P_q` is the classical exact-order Ramanujan projector and

\[
\boxed{S_q^*=S_q,\qquad S_q^2=P_q,\qquad \operatorname{rank}S_q=\varphi(q).}
\]

For `q>2`, `S_q` has `+1` and `-1` each with multiplicity `\varphi(q)/2`, and all remaining eigenvalues are zero. Thus the strongly invisible mass from PC-113 is real but classicalizes after the natural micro/macro separation: it is only a finite Ramanujan reflection tensoring the same trace-class universal operator `\mathcal K` already isolated in PC-110.

In particular,

\[
\boxed{
\lim_{p\to\infty\atop p\nmid q}
\|G_{p,q}\|_{\mathcal S_2}^2
=
\varphi(q)\bigl(\gamma-4+5\log2\bigr),
}
\]

so PC-113's strong disappearance hides a nonzero Hilbert--Schmidt defect, but its entire recovered nonzero spectral location set is independent of `q`; `q` changes only the finite exact-order multiplicity. For `q>2`,

\[
\boxed{
\det\!\left(I-z(S_q\otimes\mathcal K)\right)
=
\det(I-z^2\mathcal K^2)^{\varphi(q)/2}.
}
\]

Since `\mathcal K\in\mathcal S_1` by PC-110, this determinant again has a nuclear zero divisor and the `o(R)` counting law of PC-107. The canonical two-scale recovery therefore does not turn the PC-113 oscillatory new-prime correction into an RH spectral mechanism.

No historical novelty is claimed for periodic unfolding/two-scale convergence, Ramanujan-sum matrices, finite Fourier projectors, trace ideals, or Fredholm determinants. The durable Prime-Circle content is the exact identification of the particular `G_{p,q}` left open by PC-113 with `S_q\otimes\mathcal K` after its forced microscopic unfolding.

## 1. Start from the exact PC-113 new-prime remainder

Fix `q>1` and let `p` run through primes with `(p,q)=1`. PC-113 gives the exact decomposition

\[
R_{pq}=J_p\otimes R_q+G_{p,q},
\]

where, after writing the residue modulo `pq` as

\[
R=pa+r,
\qquad
0\le a<q,
\quad
0\le r<p,
\]

and similarly `S=pb+s`, the `(r,a;s,b)` Hardy block of the genuinely new-prime term is

\[
\boxed{
(G_{p,q})_{(r,a),(s,b)}
=
\frac{c_q\!\left(p(a+b)+r+s+1\right)}{pq}
D^\circ_{\frac{p(a+b)+r+s+1}{pq}}.
}
\]

Here

\[
D_\alpha=H_\alpha-H_1,
\qquad
(H_\alpha)_{uv}=\frac1{u+v+\alpha},
\]

and the superscript `\circ` deletes only the Hardy entry `(u,v)=(0,0)`. PC-113 proves that `\alpha\mapsto D_\alpha^\circ` is uniformly Lipschitz in `\mathcal S_2` on `[0,2]`.

The factor `c_q(p(a+b)+r+s+1)` is periodic in the fast new-prime residue. Ordinary `p`-mesh scaling averages that oscillation weakly and yields `G_{p,q}\to0` strongly. To test whether Schatten mass is being discarded, the correct next operation is therefore to retain the residue class modulo the fixed period `q` before taking the continuum limit.

## 2. Exact micro/macro split of the new-prime fiber

Write

\[
r=qk+i,
\qquad 0\le i<q,
\]

whenever `0\le r<p`, and define

\[
M_i(p)
:=\#\{0\le r<p:r\equiv i\pmod q\}.
\]

Thus each valid residue has a unique representation `r=qk+i` with `0\le k<M_i(p)`, and

\[
M_i(p)=\frac pq+O(1)
\]

uniformly in the finitely many classes `i`.

Define the exact isometry

\[
\mathcal U_{p,q}:\mathbb C^p
\longrightarrow
\mathbb C^q_{\rm micro}\otimes L^2(0,1)_{\rm slow}
\]

by

\[
\boxed{
\mathcal U_{p,q}e_{qk+i}
=
e_i\otimes
\sqrt{M_i(p)}\,
\mathbf1_{[k/M_i(p),(k+1)/M_i(p))}.
}
\]

Put

\[
\rho_p\equiv p\pmod q,
\qquad \rho_p\in(\mathbb Z/q\mathbb Z)^\times.
\]

For `r=qk+i` and `s=q\ell+j`, the Ramanujan coefficient becomes exactly

\[
\boxed{
c_q\!\left(p(a+b)+r+s+1\right)
=c_q\!\left(\rho_p(a+b)+i+j+1\right).}
\]

The dependence on the slow variables `k,\ell` has disappeared completely from the arithmetic coefficient.

There is a forced finite gauge which also removes the harmless dependence on the prime residue `\rho_p`. On the micro/coarse coordinates apply the unitary permutation

\[
\mathcal G_{\rho_p}:
 e_i\otimes e_a
\longmapsto
 e_{i+\rho_pa}\otimes e_a.
\]

After this permutation,

\[
c_q\!\left(\rho_p(a+b)+i+j+1\right)
\longmapsto
\boxed{c_q(i+j+1)}.
\]

Thus different prime congruence classes modulo `q` do not produce different limiting operators; they are related by an explicit finite coordinate gauge already forced by the residue split.

## 3. The unfolded kernel converges in Hilbert--Schmidt norm

Before merging the coarse coordinate `a` with the slow variable, the transformed kernel between micro classes `i,j`, coarse residues `a,b`, and slow cells `x,y` carries the scalar prefactor

\[
\frac{\sqrt{M_i(p)M_j(p)}}{pq}
\,c_q(i+j+1).
\]

Because `M_i(p)=p/q+O(1)`, uniformly in `i,j`,

\[
\boxed{
\frac{\sqrt{M_i(p)M_j(p)}}{pq}
\longrightarrow\frac1{q^2}.}
\]

On the same cells the generalized-Hilbert parameter is

\[
\alpha_{p}
=
\frac{p(a+b)+q(k+\ell)+i+j+1}{pq}.
\]

If `x` lies in the `k`-th slow cell for class `i` and `y` in the `\ell`-th slow cell for class `j`, then

\[
\boxed{
\alpha_p
=
\frac{a+b+x+y}{q}+O(p^{-1})
}
\]

uniformly over all cells. PC-113's uniform `\mathcal S_2` Lipschitz bound for `D_\alpha^\circ` therefore gives, for each of the finitely many micro/coarse blocks,

\[
\frac{\sqrt{M_iM_j}}{pq}
 c_q(i+j+1)D^\circ_{\alpha_p}
\longrightarrow
\frac{c_q(i+j+1)}{q^2}
D^\circ_{(a+b+x+y)/q}
\]

in the Hilbert--Schmidt norm of the operator-valued kernel. Summing over the finite `q^4` micro/coarse blocks preserves `\mathcal S_2` convergence.

Now merge the coarse residue and slow coordinate by the fixed unitary

\[
\mathcal W_q:
\mathbb C^q_{\rm coarse}\otimes L^2(0,1)_x
\longrightarrow L^2(0,1)_X,
\]

where on the `a`-th component

\[
X=\frac{a+x}{q},
\qquad
(\mathcal W_q(e_a\otimes f))(X)
=\sqrt q\,f(qX-a)
\]

for `X\in[a/q,(a+1)/q)`. Under this unitary an `(a,b)` integral kernel gains the Jacobian factor `q`, while

\[
\frac{a+b+x+y}{q}=X+Y.
\]

Consequently the final two-scale limit kernel is

\[
\boxed{
\frac{c_q(i+j+1)}q\,D^\circ_{X+Y}.}
\]

Let `\widetilde G_{p,q}` denote `G_{p,q}` after the exact micro/slow unfolding, the finite `\rho_p` gauge, and this coarse-cell merge. Then

\[
\boxed{
\widetilde G_{p,q}
\longrightarrow
S_q\otimes\mathcal K
\quad\text{in }\mathcal S_2,
}
\]

where

\[
(S_q)_{ij}=\frac1q c_q(i+j+1)
\]

and `\mathcal K` is precisely the PC-109 off-origin kernel

\[
(\mathcal K)_{uv}(X,Y)
=
(D^\circ_{X+Y})_{uv}.
\]

This convergence requires no subsequence: the only dependence on `p mod q` has been removed by the explicit finite gauge `\mathcal G_{\rho_p}`.

## 4. The finite microfactor is just the exact-order projector times reflection

Let

\[
\xi=e^{2\pi i/q},
\qquad
v_u(i)=q^{-1/2}\xi^{ui},
\qquad 0\le u<q,
\]

be the Fourier basis of `\mathbb C^q`. Using the classical root-of-unity expansion

\[
c_q(n)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}\xi^{an},
\]

a direct Fourier calculation gives

\[
\boxed{
S_qv_u=
\begin{cases}
\xi^{-u}v_{-u},& (u,q)=1,\\
0,&(u,q)>1.
\end{cases}}
\]

Therefore `S_q` is self-adjoint and

\[
\boxed{
S_q^2=P_q,
}
\]

where `P_q` is the orthogonal projector onto the primitive/exact-order Fourier modes,

\[
\boxed{
(P_q)_{ij}=\frac1q c_q(i-j).}
\]

Equivalently, if `\mathcal R_qe_j=e_{-j-1}` is the affine reflection of `\mathbb Z/q\mathbb Z`, then

\[
\boxed{S_q=P_q\mathcal R_q.}
\]

The reflection preserves the primitive Fourier subspace, so `S_q` is a self-adjoint partial isometry with initial and final projection `P_q`. Hence

\[
\boxed{
\operatorname{rank}S_q=\varphi(q),
\qquad
\|S_q\|_{\mathcal S_2}^2=\varphi(q).
}
\]

For `q>2`, a primitive residue never satisfies `u=-u mod q`, so primitive Fourier modes pair as `{u,-u}` and each two-dimensional pair contributes eigenvalues `+1,-1`. Thus

\[
\boxed{
\operatorname{Spec}(S_q)
=\{+1^{[\varphi(q)/2]},-1^{[\varphi(q)/2]},0^{[q-\varphi(q)]}\}
\qquad(q>2).}
\]

For the sole exceptional case `q=2`, the nonzero spectrum is just `{-1}`.

This is exactly the kind of finite Ramanujan channel already classicalized elsewhere in the line. PC-066 identifies `P_q` as the canonical exact-order projector with rank `\varphi(q)`; the present `S_q` adds only the intrinsic affine reflection coming from the Hankel `i+j+1` indexing.

## 5. The hidden Hilbert--Schmidt mass has an exact universal value

Hilbert--Schmidt convergence and tensor-product multiplicativity give

\[
\lim_{p\to\infty\atop p\nmid q}
\|G_{p,q}\|_2^2
=
\|S_q\otimes\mathcal K\|_2^2
=
\|S_q\|_2^2\,\|\mathcal K\|_2^2.
\]

PC-109 computed

\[
\boxed{
\|\mathcal K\|_2^2
=\gamma-4+5\log2.
}
\]

Therefore

\[
\boxed{
\lim_{p\to\infty\atop p\nmid q}
\|G_{p,q}\|_2^2
=
\varphi(q)\bigl(\gamma-4+5\log2\bigr).}
\]

This supplies the exact answer to the Schatten-mass caveat left in PC-113. The generic term does **not** become small in `\mathcal S_2`; its mass is transported to the period-`q` microscopic coordinate. But once that coordinate is retained, the mass contains only

\[
\text{exact-order multiplicity }\varphi(q)
\times
\text{the universal PC-109 constant}.
\]

As direct checks, `q=2` gives one copy of the universal mass, while `q=3,4,6` give two copies. The formula applies unchanged to prime and composite fixed conductors.

## 6. The recovered compact spectrum has no new locations

PC-110 strengthens the PC-109 classification to

\[
\boxed{\mathcal K\in\mathcal S_1.}
\]

Since `S_q` is finite rank,

\[
\boxed{S_q\otimes\mathcal K\in\mathcal S_1.}
\]

For `q>2`, the `+1` and `-1` multiplicities of `S_q` are both `\varphi(q)/2`. Hence the ordinary Fredholm determinant is

\[
\begin{aligned}
\det(I-zS_q\otimes\mathcal K)
&=
\det(I-z\mathcal K)^{\varphi(q)/2}
\det(I+z\mathcal K)^{\varphi(q)/2}\\
&=\boxed{
\det(I-z^2\mathcal K^2)^{\varphi(q)/2}.}
\end{aligned}
\]

Thus the nonzero zero locations are exactly the universal reciprocal eigenvalues of `\mathcal K`, together with their sign reflections. The fixed conductor `q` changes only multiplicity. For `q=2` the determinant is `det(I+z\mathcal K)` and the same conclusion holds without the paired sign copy.

If `\mu_j` are the nonzero eigenvalues of `\mathcal K`, then

\[
\sum_j|\mu_j|<\infty,
\]

and therefore the two-scale corrector also satisfies

\[
\sum_{\lambda\in\operatorname{Spec}_{\ne0}(S_q\otimes\mathcal K)}
|\lambda|
=
\varphi(q)\sum_j|\mu_j|<\infty.
\]

Its Fredholm zero divisor consequently has absolutely summable reciprocal moduli and counting function `o(R)`, exactly the PC-107 nuclear-density obstruction. Recovering the hidden oscillatory mass does not create a new Hilbert--Polya spectrum; it returns to a finite multiplicity of the same universal trace-class defect.

## 7. Prior-art and novelty audit

Every general mechanism used in the reduction is established classical machinery.

- The matrix `q^{-1}(c_q(i-j))` is the finite Fourier projector onto primitive frequencies by the defining root-of-unity expansion of Ramanujan sums. Noboru Ushiroya, *Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums*, *Journal of Integer Sequences* 21 (2018), Article 18.2.6, arXiv:1803.02970, studies precisely the finite Fourier spectra of Ramanujan-sum matrices. The present Hankel matrix `c_q(i+j+1)` differs from that circulant projector only by the explicit affine reflection above.
- Separating a rapidly oscillating periodic micro-variable from a continuum macro-variable is standard two-scale/unfolding technology. D. Cioranescu, A. Damlamian and G. Griso, *The Periodic Unfolding Method in Homogenization*, *SIAM Journal on Mathematical Analysis* 40:4 (2008), 1585--1620, DOI `10.1137/080713148`, develops periodic unfolding as a change of scale plus macro/micro separation and relates it to two-scale convergence. N. Wellander, *The two-scale Fourier transform approach to homogenization; periodic homogenization in Fourier space*, *Asymptotic Analysis* 62 (2009), 1--40, places two-scale convergence, unfolding, and Floquet--Bloch separation in one Fourier framework.
- The infinite operator factor is not new: it is exactly `\mathcal K` from PC-109, and PC-110 already proves that this Carleman--Hilbert discretization defect is trace class. The determinant and zero-density consequences are standard trace-ideal facts already audited in PC-107/110.

Directed searches across Ramanujan-sum matrices, periodic unfolding/two-scale Fourier transforms, rapidly oscillating compact kernels, and Hankel/Carleman discretization found broad classical frameworks but no reason to assign historical novelty to the abstract ingredients. The line-specific result is narrower: the exact PC-113 term `G_{p,q}`, when unfolded in the only finite period visible in its coefficient, converges in `\mathcal S_2` to the tensor product of the classical exact-order Ramanujan reflection and the already-classified Prime-Circle continuum defect.

The result therefore passes the novelty audit only as a **decisive internal classification/obstruction**, not as a new general theorem about homogenization or Ramanujan matrices.

## 8. Falsification surface and remaining boundary

The derivation has explicit failure points:

1. the exact PC-113 formula for `G_{p,q}` and the deletion of only the lowest Hardy entry must be used;
2. `q` is fixed while `p\to\infty` through primes coprime to `q`;
3. the micro-coordinate is the actual period `r mod q` forced by `c_q`, not an externally chosen oscillation;
4. the `p mod q` dependence must be removed only by the explicit finite residue permutation `i\mapsto i+\rho_pa`;
5. the `\mathcal S_2` convergence uses the uniform Lipschitz estimate for `D_\alpha^\circ`; without the PC-108/113 origin deletion that regularity fails at `\alpha=0`;
6. the identification of the limiting compact factor with `\mathcal K` uses the fixed coarse-cell merge `X=(a+x)/q` and no free scaling parameter.

The theorem deliberately does **not** classify a genuinely joint limit in which `q\to\infty` together with `p`. In that regime the microscopic period and the rank `\varphi(q)` both diverge, so the finite-factor argument above does not yield a fixed trace-class tensor and the accumulated trace/Schatten scale could change. It also does not cover nonlinear cross-level operations formed before the PC-113 split or a geometry-forced non-affine organization that is not equivalent to this period-`q` unfolding.

The exact closure is therefore

\[
\boxed{
\text{fixed }q\ +\ \text{one new }p\to\infty
\ +\ \text{canonical two-scale recovery of }G_{p,q}
\Longrightarrow
S_q\otimes\mathcal K,
}
\]

with `S_q^2=P_q` classical and `\mathcal K\in\mathcal S_1` universal. A surviving Hardy cross-level mechanism must move beyond a fixed coarse conductor before the new-prime limit, rather than recover more microscopic detail from this same one-new-prime oscillatory term.