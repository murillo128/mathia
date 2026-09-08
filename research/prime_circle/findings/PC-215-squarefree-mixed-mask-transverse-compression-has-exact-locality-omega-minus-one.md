# PC-215 — squarefree mixed-mask transverse compression has exact locality `omega(N)-1`

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `PRIOR-ART-CLASSICALIZATION` for the squarefree mixed-composite escape left open by PC-214: retain an individual cyclotomic coefficient mask `g_N`, compress multiplication by that mask to the exact-order transverse sector `E_N`, and ask whether the binary Kronecker-sum collapse persists when the conductor has more distinct prime factors.

It does not. For every squarefree composite

\[
N=\prod_{i=1}^k p_i,
\qquad k=\omega(N)\ge2,
\]

the canonical compression

\[
T_N:=P_NM_{g_N}P_N\big|_{E_N}
\]

has **exact tensor interaction locality**

\[
\boxed{\ell(T_N)=\omega(N)-1.}
\tag{1}
\]

Here the CRT identification

\[
E_N\cong
\bigotimes_{p\mid N}
\mathbb C^{(\mathbb Z/p\mathbb Z)^\times}
\tag{2}
\]

is intrinsic to the exact-order character sector, and `ell(T_N)` is the least integer `ell` for which `T_N` is a sum of operators supported on at most `ell` CRT tensor factors.

Thus PC-214 is exactly the first member of a growing hierarchy: for `N=pq`, `ell(T_N)=1`, explaining the one-coordinate Kronecker sum; for `N=pqr`, `ell(T_N)=2`, so genuine pair-coordinate terms are forced; for conductors with `k` distinct primes, interactions of order `k-1` occur and cannot be represented by a uniformly bounded-valence tensor decomposition.

The carrier is exact and source-derived, but this is **not yet an RH mechanism**. Its individual coefficients are values of `Phi_N` at lower-order roots of unity, a classical cyclotomic family, and the support/locality statement by itself can be reproduced by non-arithmetic masks with the same divisor-Fourier support. What survives PC-214 is growing incidence complexity, not a critical-line theorem.

## 1. Exact matrix entries are indexed by CRT change support

Retain the PC-212/PC-214 normalized coefficient field

\[
g_N(x)=\sqrt{\frac{N}{h_N}}\,a_N(x\bmod N),
\qquad
\Phi_N(z)=\sum_j a_N(j)z^j,
\qquad
h_N=\sum_j a_N(j)^2,
\tag{3}
\]

on `K=\widehat{\mathbb Z}`. For every divisor `d|N` and `(a,d)=1`, its Fourier coefficient is

\[
\boxed{
\widehat g_N(a/d)
=\frac{\Phi_N(e^{-2\pi ia/d})}{\sqrt{Nh_N}}.
}
\tag{4}
\]

Choose the exact-order basis of `E_N` indexed by the units `u mod N`. Under CRT, write

\[
u=(u_p)_{p\mid N},
\qquad
u_p\in(\mathbb Z/p\mathbb Z)^\times.
\tag{5}
\]

For two basis vectors `u,v`, define their change set

\[
S(u,v):=\{p\mid N:u_p\ne v_p\},
\qquad
d(u,v):=\prod_{p\in S(u,v)}p.
\tag{6}
\]

Because `N` is squarefree,

\[
\gcd(u-v,N)=\prod_{p\mid N,\ u_p=v_p}p,
\]

so the reduced character `(u-v)/N` has exact order precisely `d(u,v)`. Equations (4) and the multiplication-compression identity therefore give

\[
\boxed{
\langle e_u,T_Ne_v\rangle
=\frac{\Phi_N(e^{-2\pi ia/d(u,v)})}{\sqrt{Nh_N}},
}
\tag{7}
\]

where `a` is a unit modulo `d(u,v)` determined by `u-v` after reduction. For `u=v`, interpret `d=1`, so the entry is `Phi_N(1)/sqrt(Nh_N)`.

Now use only the defining zero set of the cyclotomic polynomial. The zeros of `Phi_N` are exactly the primitive `N`-th roots. Hence

\[
\boxed{
\langle e_u,T_Ne_v\rangle=0
\iff d(u,v)=N.
}
\tag{8}
\]

Every proper-divisor change pattern is therefore present with a nonzero coefficient. No magnitude estimate, limiting argument, or genericity assumption enters this support statement.

For odd squarefree `N`, equation (8) says that the only missing matrix entries are pairs differing in **every** CRT coordinate. For even squarefree `N`, the factor `(Z/2Z)^times` has dimension one, so its coordinate can never change; consequently `d(u,v)<N` for every pair and the entire exact-order matrix has nonzero entries.

## 2. The support decomposition contains every proper coordinate interaction

For each realizable change set `S`, define `H_S` on

\[
\bigotimes_{p\in S}
\mathbb C^{(\mathbb Z/p\mathbb Z)^\times}
\]

by keeping exactly those matrix entries of `T_N` whose CRT change set is `S`. Equality on the complementary coordinates contributes the identity there, so

\[
\boxed{
T_N=
\sum_{S\in\mathcal S_N}
H_S\otimes I_{S^c},
}
\tag{9}
\]

where `mathcal S_N` consists of all realizable proper change sets. By (8), every such `H_S` is nonzero.

If `N` is odd, all `k` CRT factors have dimension at least two, but the full set `S={p:p|N}` is absent because it would have exact order `N`. Thus every term in (9) has

\[
|S|\le k-1.
\tag{10}
\]

If `N` is even, the `p=2` factor is one-dimensional and never changes. There are exactly `k-1` nontrivial CRT factors, so again every term is supported on at most `k-1` factors. Therefore

\[
\ell(T_N)\le k-1.
\tag{11}
\]

The bound is sharp. For odd `N`, choose `u,v` differing in exactly `k-1` coordinates and agreeing in the remaining one. Then `d(u,v)<N`, so (8) gives a nonzero matrix element. For even `N`, choose `u,v` differing in all `k-1` odd-prime coordinates; then `d(u,v)=N/2<N`, and the corresponding entry is again nonzero.

Any operator supported on at most `k-2` tensor factors has zero matrix element between either of these pairs: at least one changed coordinate lies outside its support, where the complementary identity forces a Kronecker delta. The same is true for any sum of such operators. Hence

\[
\ell(T_N)\ge k-1.
\tag{12}
\]

Combining (11) and (12) proves (1).

This is stronger than saying that a particular expansion happens to use high-order terms. The CRT tensor structure itself certifies that no decomposition of `T_N` into interactions of uniformly lower valence exists.

## 3. Ternary conductors are the first genuine mixed-coordinate case

For `N=pqr`, equation (1) gives

\[
\boxed{\ell(T_{pqr})=2.}
\tag{13}
\]

Thus the exact-order compression contains genuine pair-coordinate operators, while the three-coordinate entry is absent when all three factors are nontrivial. Schematically,

\[
T_{pqr}
=cI
+H_p+H_q+H_r
+H_{pq}+H_{pr}+H_{qr},
\tag{14}
\]

with the harmless convention that a term involving the one-dimensional `p=2` factor may be absorbed into a lower-coordinate term. For three odd primes, all three pair terms are nonzero.

The pair coefficients are not abstract interaction parameters. They are forced lower-order cyclotomic values. For example, let `z` be a primitive `pq`-th root. Since `r` is coprime to `pq`,

\[
\Phi_{pqr}(x)=\frac{\Phi_{pq}(x^r)}{\Phi_{pq}(x)}.
\tag{15}
\]

Both numerator and denominator vanish at `x=z`, and cancellation of their simple zeros gives

\[
\Phi_{pqr}(z)
=r z^{r-1}
\frac{\Phi_{pq}'(z^r)}{\Phi_{pq}'(z)}.
\tag{16}
\]

Using

\[
\Phi_{pq}'(w)
=pq\,w^{-1}
\frac{w-1}{(w^p-1)(w^q-1)}
\qquad(w\text{ primitive }pq),
\tag{17}
\]

one obtains the explicit nonzero formula

\[
\boxed{
\Phi_{pqr}(z)
=r
\frac{z^r-1}{z-1}
\frac{z^p-1}{z^{pr}-1}
\frac{z^q-1}{z^{qr}-1}.
}
\tag{18}
\]

Thus the first genuine two-coordinate carrier retains joint residue information from two prime axes while also depending on the complementary prime. It is not the independent one-prime packet of PC-213 and it is not the binary rook/Kronecker-sum geometry of PC-214.

## 4. Prior-art and novelty audit

The arithmetic values in (7) and (18) are classical cyclotomic data, not a new number-theoretic family.

R. P. Kurshan and A. M. Odlyzko, **Values of cyclotomic polynomials at roots of unity**, *Mathematica Scandinavica* 49 (1981), 15--35, DOI `10.7146/math.scand.a-11919`, study exactly the problem of evaluating cyclotomic polynomials at roots of unity other than their own primitive zeros.

B. Bzdęga, A. Herrera-Poyatos and P. Moree, **Cyclotomic polynomials at roots of unity**, *Acta Arithmetica* 184 (2018), 215--230, DOI `10.4064/aa170112-20-12`, derive finite-Fourier formulas for `Phi_n` at other roots of unity and connect those values to classical resultant calculations. Their framework is a direct prior-art boundary for every scalar coefficient appearing in (7).

The CRT decomposition of units, exact-order characters, and tensor products of finite abelian Fourier spaces are also standard. A directed search did not locate the exact project-specific compression `P_N M_{g_N} P_N` or the locality identity (1). That absence is not evidence of novelty. The honest new-to-this-line content is the exact consequence obtained by combining the persisted source-derived operator with the classical root-value support law: binary separability does not continue, and the minimal interaction valence grows as `omega(N)-1`.

Accordingly, (1) should be treated as a **Prime-Circle structural carrier/boundary theorem**, not as a claim of new cyclotomic number theory.

## 5. Falsification controls and what the theorem does not establish

The theorem survives the main internal collapse test that killed PC-213--PC-214: for unbounded `omega(N)`, `T_N` cannot be represented by a fixed finite sum of uniformly bounded-valence prime-coordinate operators. In particular, ternary and higher mixed-composite masks retain incidence that is literally absent from binary Kronecker sums.

But the support statement alone is not arithmetic-specific. Any periodic mask whose Fourier transform is nonzero on every proper divisor conductor and vanishes on the top exact-order conductor would generate the same change-support pattern and the same locality count. A matched non-arithmetic control can therefore reproduce (1) without knowing primes as arithmetic objects. The cyclotomic content lies in the **values and coherent cross-level relations** of the nonzero coefficients, not merely in which coordinate supports occur.

Likewise, increasing tensor locality does not create a spectral parameter `s`, a gamma factor, an `s<->1-s` symmetry, a critical line, or a Hilbert--Polya operator. Forming a Mellin/Dirichlet aggregate with externally chosen weights would reintroduce the missing scale by hand and would not count as progress under the Prime-Circle mandate.

The result also concerns squarefree individual mixed-composite masks. Repeated prime powers, different intrinsic operators, and cross-level limits require separate analysis; equation (1) must not be silently extrapolated to them.

## 6. Consequence for the research frontier

PC-214 established that a binary mixed mask retains modular-inverse arithmetic but its direct exact-order compression is a bounded-complexity Kronecker sum. PC-215 shows that this is a **binary accident of divisor geometry**, not a general no-go for individual mixed-composite masks. Once three or more distinct primes coexist, proper-divisor Fourier sectors can change several CRT coordinates simultaneously, and the maximal forced interaction order grows without bound with the number of prime factors.

The next decisive question is therefore no longer whether mixed-composite masks can create irreducible finite incidence: they can. It is whether the **source-forced cyclotomic coefficients across these growing `(omega(N)-1)`-body sectors** possess a stable norm, spectral, positivity, transfer, or limiting property that differs from a conductor-matched non-arithmetic control and connects to the zeta target without an externally chosen transform.

A useful continuation must preserve the growing sectors before trace/determinant scalarization and test a source-native growing-level normalization. If the collective operator family reduces under CRT/Fourier or a natural renormalization to classical independent packets, bounded universal support geometry, or ordinary cyclotomic root-value algebra, this survivor is only another representation boundary. If a stable source-specific invariant survives those controls, it would be the first mechanism in this coefficient-mask branch that is not already visible at binary level.