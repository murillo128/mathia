# PC-113 — one-new-prime Hardy microlocal limit is reflection tensor inflation

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-112 leaves a genuinely joint cross-conductor operator, formed before the PC-109 single-conductor universalization, as one of the remaining ways to escape the affine-scale and Möbius-birth collapses. The most canonical such test is to keep a fixed conductor `q>1`, adjoin one new prime `p\nmid q`, and resolve the new `p`-fiber microlocally before taking `p\to\infty`.

For the canonical Hardy/Hilbert trace-class remainder `T_n` of PC-075, remove only the universal lowest-Hardy `(0,0)` block as in PC-108 and write the resulting compact arithmetic residual as `R_n`. Then, after the exact residue split

\[
\mathbb C^{pq}\cong \mathbb C^p_{\rm new\ fiber}\otimes\mathbb C^q_{\rm coarse}
\]

and the canonical mesh embedding of the new-prime fiber into `L^2(0,1)`, one has the strong-operator limit

\[
\boxed{
\widehat R_{p,q}\xrightarrow[p\to\infty]{\rm strong}
\mathcal R\otimes R_q,
}
\]

along primes `p\nmid q`, where

\[
(\mathcal Rf)(x)=f(1-x)
\]

is reflection on `L^2(0,1)`. The exact finite-level decomposition behind the limit is

\[
\boxed{
R_{pq}\cong J_p\otimes R_q+G_{p,q},
}
\]

where `J_p` is the `p x p` reversal matrix and the genuinely new-prime term `G_{p,q}` tends strongly to zero after mesh embedding. Thus the joint limit does retain the fixed-`q` arithmetic residual, but only by inflating it through an infinite-dimensional reflection channel. If `R_q\neq0`, every nonzero eigenvalue of `R_q` becomes an eigenvalue of infinite multiplicity (with both signs) in the limit, so the limit is noncompact and cannot supply a compact/Fredholm Hilbert--Pólya mechanism.

This does **not** say that all two-conductor or two-scale limits are trivial. The generic term may retain norm or Schatten mass while escaping strongly, just as conductor mass escaped fixed coordinates in PC-108. The exact conclusion is narrower: the canonical one-new-prime strong microlocal limit of the off-origin Hardy residual contains no new discrete spectral locations beyond those already present at the fixed conductor `q`.

## 1. Off-origin Hardy residual and uniform Hilbert--Schmidt regularity

PC-075 gives, after the conductor-residue decomposition,

\[
(T_n)_{rs}
=-\frac{c_n(r+s+1)}n
D_{(r+s+1)/n},
\qquad
D_\alpha:=H_\alpha-H_1,
\]

with

\[
(H_\alpha)_{ab}=\frac1{a+b+\alpha}.
\]

Let

\[
P_0=|e_0\rangle\langle e_0|
\]

on the Hardy coordinate and set

\[
Q_n=I_{\mathbb C^n}\otimes P_0,
\qquad
\boxed{R_n:=T_n-Q_nT_nQ_n.}
\]

Equivalently, define `D_alpha^circ` by deleting only the Hardy matrix entry `(a,b)=(0,0)` from `D_alpha`. Then

\[
\boxed{
(R_n)_{rs}
=-\frac{c_n(r+s+1)}n
D^\circ_{(r+s+1)/n}.
}
\]

This is the same removal used in PC-108: it discards the singular lowest-Hardy corner but keeps all cross terms involving `e_0` and positive Hardy indices. Since `T_n` is trace class and `Q_nT_nQ_n` is finite rank, every `R_n` is trace class.

The deletion also makes the family `D_\alpha^\circ` uniformly Hilbert--Schmidt regular down to `\alpha=0`. For Hardy anti-diagonal index `m=a+b\ge1`,

\[
(D_\alpha)_{ab}
=\frac{1-\alpha}{(m+\alpha)(m+1)},
\]

and

\[
\frac{\partial}{\partial\alpha}(D_\alpha)_{ab}
=-\frac1{(m+\alpha)^2}.
\]

Hence, uniformly for `0\le\alpha\le2`,

\[
\|D_\alpha^\circ\|_{\mathcal S_2}<C,
\qquad
\left\|\frac{d}{d\alpha}D_\alpha^\circ\right\|_{\mathcal S_2}^2
\le
\sum_{m\ge1}\frac{m+1}{m^4}<\infty.
\]

Thus `alpha -> D_alpha^circ` is Lipschitz in `S_2` on the entire interval needed below. This is the compactness input that makes the new-prime oscillations harmless in the strong topology.

## 2. Exact new-prime split at conductor `pq`

Fix `q>1` and let `p` be a prime with `p\nmid q`. Write every residue modulo `pq` uniquely as

\[
R=pa+r,
\qquad
0\le a<q,
\quad
0\le r<p,
\]

and similarly `S=pb+s`. Put

\[
t=R+S+1=p(a+b)+(r+s+1).
\]

Because `(p,q)=1`, Ramanujan sums factor:

\[
c_{pq}(t)=c_p(t)c_q(t).
\]

For prime `p`,

\[
c_p(t)=p\,\mathbf1_{p\mid t}-1.
\]

Moreover `1\le r+s+1\le2p-1`, so

\[
p\mid t
\quad\Longleftrightarrow\quad
r+s+1=p.
\]

Insert this in the block formula for `R_{pq}`:

\[
-\frac{c_{pq}(t)}{pq}D^\circ_{t/(pq)}
=
-\mathbf1_{p\mid t}\frac{c_q(t)}qD^\circ_{t/(pq)}
+
\frac{c_q(t)}{pq}D^\circ_{t/(pq)}.
\]

On the spike `r+s+1=p`,

\[
t=p(a+b+1),
\qquad
c_q(t)=c_q(a+b+1),
\qquad
\frac{t}{pq}=\frac{a+b+1}{q},
\]

because multiplication by `p` is a unit modulo `q`. The spike block is therefore exactly

\[
-\frac{c_q(a+b+1)}q
D^\circ_{(a+b+1)/q},
\]

which is the `(a,b)` residue block of `R_q`.

Let `J_p` denote reversal,

\[
(J_p)_{rs}=\mathbf1_{r+s=p-1}.
\]

After the permutation that orders the new-prime fiber first, the exact finite-level identity is

\[
\boxed{
R_{pq}=J_p\otimes R_q+G_{p,q},
}
\]

where the `(r,a;s,b)` Hardy block of the remaining term is

\[
\boxed{
(G_{p,q})_{(r,a),(s,b)}
=
\frac{c_q\!\left(p(a+b)+r+s+1\right)}{pq}
D^\circ_{\frac{p(a+b)+r+s+1}{pq}}.
}
\]

This exact decomposition is the essential distinction from PC-078. When the adjoined prime is already present, the whole operator is a finite reversal tensor inflation. For a genuinely new prime there is an additional term; the question is whether that term survives the conductor-resolving limit.

## 3. Canonical mesh limit of the inherited spike

Embed the new-prime fiber by

\[
\mathcal J_p:\mathbb C^p\to L^2(0,1),
\qquad
\mathcal J_pe_r
=\sqrt p\,\mathbf1_{[r/p,(r+1)/p)}.
\]

Let `P_p=\mathcal J_p\mathcal J_p^*` be the projection onto the `p`-step functions. Reflection preserves this subspace and satisfies exactly

\[
\boxed{
\mathcal J_pJ_p\mathcal J_p^*
=\mathcal R P_p,
\qquad
(\mathcal Rf)(x)=f(1-x).
}
\]

Since `P_p\to I` strongly,

\[
\mathcal J_pJ_p\mathcal J_p^*
\longrightarrow\mathcal R
\]

strongly. Therefore the inherited part satisfies

\[
\boxed{
(\mathcal J_p\otimes I)(J_p\otimes R_q)(\mathcal J_p^*\otimes I)
\xrightarrow{\rm strong}
\mathcal R\otimes R_q.
}
\]

No asymptotic arithmetic is used here: the coarse conductor is retained literally as the already-existing operator `R_q`.

## 4. The genuinely new-prime term is a rapidly oscillating compact coupling

Use the root-of-unity Fourier formula

\[
\boxed{
c_q(m)=\sum_{u\in(\mathbb Z/q\mathbb Z)^\times}\xi_q^{um},
\qquad
\xi_q=e^{2\pi i/q}.}
\]

For fixed coarse residues `a,b`, define the unweighted `p x p` operator-valued Hankel block

\[
(B_p^{ab})_{rs}
=
\frac1{pq}
D^\circ_{\frac{p(a+b)+r+s+1}{pq}}.
\]

Then the corresponding block of `G_{p,q}` is the finite sum

\[
\boxed{
G_{p,q}^{ab}
=
\sum_{u\in U(q)}
\xi_q^{u(p(a+b)+1)}
M_{u,p}B_p^{ab}M_{u,p},
}
\]

where

\[
M_{u,p}e_r=\xi_q^{ur}e_r.
\]

Under the mesh embedding, `B_p^{ab}` converges in Hilbert--Schmidt norm to the compact operator `K_q^{ab}` on `L^2(0,1)\otimes\ell^2(\mathbb Z_{\ge0})` whose operator-valued kernel is

\[
\boxed{
k_q^{ab}(x,y)
=
\frac1q
D^\circ_{(a+b+x+y)/q}.}
\]

Indeed the transformed step kernel on the cell `I_r x I_s` is

\[
\frac1q
D^\circ_{\frac{a+b+(r+s+1)/p}{q}},
\]

while

\[
\left|
\frac{r+s+1}{p}-(x+y)
\right|\le\frac1p.
\]

The uniform `S_2` Lipschitz bound from Section 1 therefore gives `S_2` convergence of the full operator-valued kernel.

The diagonal modulation becomes multiplication by the step function

\[
m_{u,p}(x)=\xi_q^{u\lfloor px\rfloor}.
\]

For every unit `u mod q`, its mean over each complete group of `q` consecutive mesh cells is zero:

\[
\sum_{r=0}^{q-1}\xi_q^{ur}=0.
\]

Consequently

\[
\boxed{M_{u,p}\rightharpoonup0}
\]

in the weak operator topology after mesh embedding. One direct proof is to test against a continuous `L^1` function, group the integral into `q`-cell packets, use the exact zero mean and uniform continuity inside each packet, and then control the incomplete final packet; density extends the result to arbitrary `L^1` test functions and hence to matrix coefficients on `L^2`.

Now use only the elementary compactness principle: if `M_p` is uniformly bounded and `M_p f\rightharpoonup0`, then `KM_pf\to0` in norm for every compact `K`. Since

\[
B_p^{ab}\to K_q^{ab}
\]

in operator norm (in fact in `S_2`), for every fixed vector `f`,

\[
\begin{aligned}
\|B_p^{ab}M_{u,p}f\|
&\le
\|(B_p^{ab}-K_q^{ab})M_{u,p}f\|
+
\|K_q^{ab}M_{u,p}f\|\\
&\longrightarrow0.
\end{aligned}
\]

Left multiplication by `M_{u,p}` preserves norm. The sum over `u` is finite, and there are only `q^2` coarse blocks. Hence

\[
\boxed{
\widehat G_{p,q}\xrightarrow[p\to\infty]{\rm strong}0.
}
\]

This is where the new-prime information goes: its non-spike Ramanujan modes become rapidly oscillating compact couplings and disappear in the strong microlocal topology.

## 5. Strong cross-conductor limit

Combining the exact finite-level split with Sections 3 and 4 gives the theorem:

\[
\boxed{
\widehat R_{p,q}
\xrightarrow[p\to\infty,\ p\nmid q]{\rm strong}
\mathcal R\otimes R_q.
}
\]

Here the fixed Hilbert space is

\[
L^2(0,1)_{\rm new\ fiber}
\otimes
\mathbb C^q_{\rm coarse}
\otimes
\ell^2(\mathbb Z_{\ge0})_{\rm Hardy},
\]

and each finite `p` operator is extended by zero off the `p`-step subspace in the first factor.

Thus a joint conductor limit formed **before** the PC-109 single-prime universalization does preserve arithmetic information: it remembers the full compact residual `R_q`. But it does so only by copying that old information into the two infinite reflection sectors. No new compact spectral positions are generated by the large new prime.

## 6. Spectral consequence: inherited eigenvalues become essential

The reflection `\mathcal R` is a self-adjoint unitary with `+1` and `-1` eigenspaces both infinite-dimensional. The fixed-conductor residual `R_q` is compact self-adjoint. If

\[
R_qv=\lambda v,
\qquad
\lambda\ne0,
\]

then for every `f` in the even reflection subspace,

\[
(\mathcal R\otimes R_q)(f\otimes v)=\lambda(f\otimes v),
\]

while every odd-reflection `f` gives eigenvalue `-\lambda`. Hence

\[
\boxed{
R_q\ne0
\quad\Longrightarrow\quad
\mathcal R\otimes R_q\text{ is noncompact},
}
\]

and each nonzero `lambda` from the old compact block reappears as `+lambda` and `-lambda` with infinite multiplicity. These points belong to the essential spectrum of the limit.

Therefore the canonical one-new-prime microlocal limit does not yield a compact operator whose Fredholm determinant could have a new discrete zero divisor. It converts the old discrete `q`-spectrum into infinite-multiplicity channels. If exceptionally `R_q=0`, the limit is zero and is equally unable to produce a new spectral mechanism.

This is a different obstruction from PC-109/110. The prime-only limit became universal and then trace class off the origin. The present fixed-`q`/new-`p` limit is **not prime-blind**, but the retained arithmetic is inherited rather than newly generated and its infinite fiber multiplicity destroys compactness.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the ingredients used here. Ramanujan's root-of-unity expansion and multiplicativity are classical and are already anchored in `research/prime_circle/SOURCES.md`. The Hilbert/generalized-Hilbert and Hankel operator background is likewise classical there through Magnus, Rosenblum, Pushnitski--Yafaev, Ushiroya, and the PC-075 source bridge. The functional-analytic step that compact operators turn bounded weakly-null sequences into norm-null sequences is standard.

Internally, PC-078 and PC-079 are the closest controls. PC-078 proves exact reversal-tensor inflation when the adjoined prime already divides the conductor; it does **not** cover a new prime. PC-079 proves that the coefficient-dilation superoperators commute and that primitive shells are Möbius differences of Hilbert dilations; it does not classify this two-scale physical mesh limit. PC-108/109 classify only the prime-conductor limit, where the Ramanujan spike happens to multiply `D_1=0` and all residual arithmetic disappears.

The present line-specific content is therefore the exact decomposition of the **new-prime** composite residual into an inherited reversal tensor plus an oscillatory generic term, and the proof that the latter vanishes strongly under the canonical new-prime mesh scaling. Directed searches around Ramanujan-weighted Hankel operators, generalized Hilbert matrices, periodic coefficient decompositions, and rapidly oscillating compact couplings found broad classical operator/homogenization machinery but no reason to claim an independent new general theorem. The result is retained as a Prime-Circle classification and obstruction, not as a novelty claim about Hankel or homogenization theory.

## 8. Falsification surface and remaining boundary

The theorem has explicit failure points:

1. the PC-075 block formula for `T_n` and the PC-108 removal of only the lowest-Hardy block must be used exactly;
2. for `(p,q)=1`, `c_{pq}=c_pc_q`, and the prime factor must split as `c_p(t)=p 1_{p|t}-1`;
3. in the two-stage residue coordinates, `p|t` must be equivalent to the single reversal condition `r+s=p-1`;
4. the spike must reproduce the exact `R_q` block after using `c_q(pk)=c_q(k)`;
5. `D_alpha^circ` must be uniformly `S_2`-Lipschitz down to `alpha=0`;
6. the unweighted new-fiber blocks must converge in `S_2` to the compact operator-valued kernels `K_q^{ab}`;
7. every nontrivial character modulation of the `q`-periodic fiber must be weakly null under the physical `1/p` mesh;
8. compactness of the limiting unweighted blocks must then force the generic term to vanish strongly.

Each step is exact or follows from an elementary norm estimate; no numerical coincidence or analytic continuation is used.

The result does **not** rule out:

- a topology or renormalization designed to retain the escaping norm/Schatten mass of `G_{p,q}` rather than its strong limit;
- simultaneous `p,q\to\infty` limits in which there is no fixed inherited conductor;
- non-affine recenterings or geometry-forced weights not reducible to the PC-075 Hardy remainder;
- nonlinear cross-level operators outside the linear Hardy/Hankel branch;
- genuinely joint chord/old-new operators formed before the Ramanujan/Hilbert compression;
- the nonlinear uniformization/monodromy branch rooted at PC-017.

But the most direct cross-conductor repair left open by PC-112 is now sharply constrained: **adjoining one large new prime to a fixed conductor does not create a new compact microlocal spectrum. The fixed arithmetic residual survives only as reflection-tensor inheritance, while the genuinely new-prime part escapes strongly.**
