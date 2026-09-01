# PC-115 — growing-prime two-scale corrector has a zero-free Gaussian determinant

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-114 classifies, for each fixed coarse conductor `q`, the two-scale recovery of the one-new-prime Hardy term as the trace-class tensor

\[
A_q:=S_q\otimes\mathcal K,
\qquad
(S_q)_{ij}=\frac1q c_q(i+j+1),
\]

where `\mathcal K` is the universal off-origin Carleman--Hilbert defect of PC-109/110. PC-114 deliberately leaves `q\to\infty` open because `rank S_q=\varphi(q)` diverges and the accumulated Schatten scale could change.

Along prime coarse conductors that remaining iterated limit can be classified exactly. After the canonical step-function embedding of the finite micro-coordinate, `S_q` converges strongly to reflection with its constant mode removed. Hence `A_q` has a noncompact strong limit and no scalar normalization can produce a nonzero compact strong limit. On the other hand the unique scalar scale that keeps the Hilbert--Schmidt mass finite is `\varphi(q)^{-1/2}`; at that scale the operators converge to zero in operator norm, while both their ordinary and `det_2` Fredholm determinants converge locally uniformly to the zero-free Gaussian

\[
\boxed{
\exp\!\left[-\frac{\gamma-4+5\log2}{2}\,z^2\right].
}
\]

Thus the growing multiplicity left open by PC-114 does cross from finite trace-class multiplicity to a noncompact reflection channel, but its canonical Hilbert--Schmidt renormalization still cannot create an RH zero divisor. No theorem-level historical novelty is claimed for finite Ramanujan projectors, step-function convergence, trace ideals, or Fredholm determinant asymptotics. The durable Prime-Circle content is the exact classification of this specific `q\to\infty` escape of the PC-114 two-scale corrector.

## 1. Prime coarse conductors make the Ramanujan factor an exact reflection defect

Let `q>2` be prime. The prime Ramanujan sum is

\[
c_q(t)=q\,\mathbf1_{q\mid t}-1.
\]

Therefore the exact-order Ramanujan projector from PC-114 is

\[
(P_q)_{ij}=\frac1q c_q(i-j)
=\delta_{ij}-\frac1q.
\]

If

\[
u_q=q^{-1/2}(1,\ldots,1)^T,
\]

then

\[
\boxed{P_q=I-u_qu_q^*.}
\]

PC-114 also gives

\[
S_q=P_q\mathcal R_q,
\qquad
\mathcal R_qe_j=e_{-j-1\ ({\rm mod}\ q)}.
\]

The affine reflection fixes the constant vector, `\mathcal R_qu_q=u_q`, so at prime level

\[
\boxed{S_q=\mathcal R_q-u_qu_q^*.}
\]

This already shows that the increasing finite factor contains no hidden prime-dependent eigenvalue locations. For every odd prime `q`,

\[
\operatorname{Spec}(S_q)
=\{+1^{[(q-1)/2]},-1^{[(q-1)/2]},0\},
\]

and in particular

\[
\boxed{
\operatorname{Tr}S_q=0,
\qquad
\|S_q\|=1,
\qquad
\|S_q\|_2^2=q-1.
}
\]

The only quantity growing with the prime conductor is multiplicity.

## 2. The canonical continuum limit is reflection minus the constant mode

Embed the micro-coordinate by the same canonical uniform-mesh construction used elsewhere in the Hardy conductor limits,

\[
\mathcal J_q:\mathbb C^q\longrightarrow L^2(0,1),
\qquad
\mathcal J_qe_j
=\sqrt q\,\mathbf1_{[j/q,(j+1)/q)}.
\]

Let

\[
E_q=\mathcal J_q\mathcal J_q^*
\]

be the orthogonal projection onto the `q`-step functions, let

\[
(\mathcal Rf)(x)=f(1-x),
\]

and let `P_{\mathbf1}` denote orthogonal projection onto the constant function `\mathbf1`. The affine finite reflection reverses the mesh cells exactly, while `\mathcal J_qu_q=\mathbf1`; hence

\[
\boxed{
\mathcal J_qS_q\mathcal J_q^*
=\mathcal R E_q-P_{\mathbf1}.
}
\]

Because the mesh size tends to zero,

\[
E_q\xrightarrow[q\to\infty]{\rm strong}I
\]

also along the prime subsequence. Therefore

\[
\boxed{
\mathcal J_qS_q\mathcal J_q^*
\xrightarrow[q\to\infty\atop q\ {m prime}]{\rm strong}
\mathcal S:=\mathcal R-P_{\mathbf1}.
}
\]

The operator `\mathcal S` is reflection on the mean-zero subspace. Its `+1` and `-1` eigenspaces are both infinite dimensional, while the constant mode is its kernel. Thus it is bounded but noncompact.

Tensoring with the fixed PC-110 operator preserves strong convergence:

\[
\boxed{
(\mathcal J_qS_q\mathcal J_q^*)\otimes\mathcal K
\xrightarrow{\rm strong}
(\mathcal R-P_{\mathbf1})\otimes\mathcal K.
}
\]

Since PC-109 gives `\|\mathcal K\|_2^2=\gamma-4+5\log2>0`, the operator `\mathcal K` is nonzero. Taking one vector `g` with `\mathcal Kg\ne0` and an orthonormal sequence in either infinite-dimensional reflection eigenspace shows that the tensor limit is noncompact.

## 3. No scalar normalization produces a nonzero compact strong limit

Write

\[
\widehat A_q
:=(\mathcal J_qS_q\mathcal J_q^*)\otimes\mathcal K.
\]

For every odd prime `q`,

\[
\boxed{\|\widehat A_q\|=\|\mathcal K\|.}
\]

Suppose a scalar sequence `a_q` were such that `a_q\widehat A_q` converged strongly to a bounded operator `T`. Uniform boundedness forces `a_q` to be bounded. Every convergent scalar subsequence `a_{q_k}\to a` then gives, by the strong convergence above,

\[
a_{q_k}\widehat A_{q_k}
\xrightarrow{\rm strong}
a\,\mathcal S\otimes\mathcal K.
\]

Since the strong limit `T` is unique and `\mathcal S\otimes\mathcal K\ne0`, all scalar subsequential limits must agree. Hence `a_q\to a` and

\[
\boxed{T=a\,\mathcal S\otimes\mathcal K.}
\]

If `a=0`, the limit is zero. If `a\ne0`, it is noncompact. Therefore

\[
\boxed{
\text{no scalar normalization of the growing prime microfactor has a nonzero compact bounded strong limit.}
}
\]

This is the two-scale analogue of the scalar-normalization obstruction in PC-108, but it applies after the hidden PC-113 mass has already been recovered by the PC-114 microscopic unfolding.

## 4. Hilbert--Schmidt normalization preserves mass but kills operator norm

For prime `q`, put

\[
m=q-1=\varphi(q)
\]

and choose the unique scalar order that keeps the PC-114 Hilbert--Schmidt mass finite,

\[
\boxed{B_q:=m^{-1/2}(S_q\otimes\mathcal K).}
\]

Then

\[
\boxed{
\|B_q\|=m^{-1/2}\|\mathcal K\|\longrightarrow0,
}
\]

whereas

\[
\begin{aligned}
\|B_q\|_2^2
&=m^{-1}\|S_q\|_2^2\|\mathcal K\|_2^2\\
&=\boxed{\|\mathcal K\|_2^2}.
\end{aligned}
\]

PC-109 computes the universal constant

\[
\boxed{
c:=\|\mathcal K\|_2^2
=\gamma-4+5\log2
\approx0.0429515677012593.}
\]

Thus the normalization does not concentrate the escaped mass into a compact limiting operator. It spreads a fixed amount of `\mathcal S_2` mass over `m` reflection channels whose individual operator scale is `m^{-1/2}`.

More generally,

\[
\|a_q(S_q\otimes\mathcal K)\|_2^2
=|a_q|^2m\,c.
\]

So any scalar normalization with a finite nonzero Hilbert--Schmidt scale must satisfy `|a_q|\asymp m^{-1/2}`, and therefore its operator norm tends to zero. The strong/noncompact scale and the Schatten-preserving scale are incompatible.

## 5. The Schatten-preserving Fredholm determinant has an exact Gaussian limit

PC-110 proves

\[
\mathcal K=\mathcal K^*\in\mathcal S_1.
\]

Hence every `B_q` is trace class. For `q>2`, the nonzero finite-factor eigenvalues are `+1` and `-1`, each with multiplicity `m/2`. Therefore the ordinary Fredholm determinant factors exactly as

\[
\begin{aligned}
D_q(z)
&:=\det(I-zB_q)\\
&=\det\!\left(I-\frac z{\sqrt m}\mathcal K\right)^{m/2}
  \det\!\left(I+\frac z{\sqrt m}\mathcal K\right)^{m/2}\\
&=\boxed{
\det\!\left(I-\frac{z^2}{m}\mathcal K^2\right)^{m/2}.}
\end{aligned}
\]

Since `\mathcal K^2\in\mathcal S_1` and

\[
\operatorname{Tr}\mathcal K^2
=\|\mathcal K\|_2^2=c,
\]

the standard trace-log expansion gives, uniformly for `z` in every compact subset of `\mathbb C`,

\[
\begin{aligned}
\log D_q(z)
&=\frac m2\operatorname{Tr}
\log\!\left(I-\frac{z^2}{m}\mathcal K^2\right)\\
&=-\frac{z^2}{2}\operatorname{Tr}\mathcal K^2+O_z(m^{-1}).
\end{aligned}
\]

Consequently

\[
\boxed{
D_q(z)
\longrightarrow
\exp\!\left(-\frac c2z^2\right)
\quad\text{locally uniformly on }\mathbb C.}
\]

The limit is entire and **zero-free**. In particular the only scalar normalization that retains a nonzero finite Hilbert--Schmidt mass does not merely have the wrong Riemann-zero density: its limiting ordinary Fredholm divisor is empty.

The same conclusion holds for the Hilbert--Schmidt regularized determinant. Because

\[
\operatorname{Tr}B_q
=m^{-1/2}(\operatorname{Tr}S_q)(\operatorname{Tr}\mathcal K)=0,
\]

one has exactly

\[
\boxed{
\det_2(I-zB_q)=\det(I-zB_q)
}
\]

for every odd prime `q`. Thus the `det_2` escape identified as analytically compatible with Riemann zero density in PC-107 also collapses to the same zero-free Gaussian on this canonical growing-multiplicity branch.

## 6. Stress tests and falsification surface

The derivation has several exact checks.

1. For `q=3,5,7,11`, direct construction from `q^{-1}c_q(i+j+1)` gives `S_q=\mathcal R_q-u_qu_q^*` to machine precision and the spectrum `+1,-1,0` with the predicted multiplicities. This is only a computational stress test; the matrix identity above is exact.
2. The determinant formula can be checked eigenvalue by eigenvalue: each `+\mu_j/\sqrt m` copy is paired with `-\mu_j/\sqrt m`, producing `1-z^2\mu_j^2/m`, repeated `m/2` times.
3. The exceptional prime `q=2` has only one nonzero finite-factor eigenvalue and is irrelevant to the `q\to\infty` statement.
4. The local-uniform Gaussian limit depends only on `\mathcal K^2\in\mathcal S_1`; higher trace terms are suppressed by at least one extra power of `m^{-1}`.

The claim would fail if the PC-114 factorization `S_q\otimes\mathcal K` failed, if `S_q` ceased to be the exact-order projector times affine reflection, if the PC-110 trace-class theorem for `\mathcal K` failed, or if the prime Ramanujan identity above were wrong. All four inputs are exact persisted results or classical identities.

## 7. Prior-art and novelty audit

The general ingredients are classical and do not support a theorem-level novelty claim.

- The prime identity `c_q(t)=q 1_{q|t}-1` and the associated finite Ramanujan projector are classical. PC-066 and PC-114 already classify the exact-order projector, and Noboru Ushiroya, *Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums*, *Journal of Integer Sequences* 21 (2018), Article 18.2.6, is the persisted neighboring literature anchor for Ramanujan-sum matrix spectra.
- Strong convergence of uniform step-function projections to the identity and convergence of the corresponding cell reflection are standard approximation facts. The continuum reflection obtained here is not a new operator-theoretic object.
- Fredholm products, `det_2`, and the trace-log expansion for trace-class/Hilbert--Schmidt operators are standard trace-ideal theory. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, AMS (2005), is already the literature anchor used in PC-107 for these determinant facts.
- PC-108 already exhibits the general warning that conductor growth can preserve or diverge Schatten mass while converging strongly through a universal Hilbert channel. The present result is not a rediscovery of that principle: it applies specifically to the **second, microscopic PC-114 factor that remains after the PC-113 strong limit has discarded it** and computes its exact normalized determinant.

Directed searches across Ramanujan-sum matrix spectra, Hilbert--Schmidt regularized determinants, trace ideals, and multiplicity limits found broad established frameworks but no independent source suggesting that this exact Prime-Circle iterated limit carries a new zeta mechanism. The durable contribution is therefore an internal obstruction: after the canonical two-scale recovery, growing prime multiplicity either yields a noncompact reflection tensor or, at the Schatten-preserving scalar scale, a zero-free Gaussian determinant.

## 8. Significance and remaining boundary

PC-114 left increasing coarse conductor open because the finite rank `\varphi(q)` diverges. Along prime coarse conductors the two canonical scalar regimes are now exact:

\[
\boxed{
\begin{array}{ccl}
\text{operator scale }1
&\Longrightarrow&
(\mathcal R-P_{\mathbf1})\otimes\mathcal K
\quad\text{noncompact},\\[2mm]
\text{Hilbert--Schmidt scale }(q-1)^{-1/2}
&\Longrightarrow&
B_q\to0\text{ in norm},\quad
\det_2(I-zB_q)\to e^{-cz^2/2}.
\end{array}}
\]

Neither regime produces a discrete RH-type spectral divisor.

The scope is intentionally narrower than a simultaneous two-conductor theorem. PC-114 first takes `p\to\infty` with `q` fixed; the present result then lets that coarse `q\to\infty` through primes. No uniform-in-`q` error estimate for the finite operators `G_{p,q}` is proved here, so arbitrary joint paths `p,q\to\infty` remain outside the claim. The result also does not cover nonlinear operations formed before the PC-113 split, non-scalar `q`-dependent conjugations that introduce a genuinely different geometric scale, or other Prime-Circle operator families outside the Hardy two-scale corrector.

What it does close is the most direct continuation of PC-114:

\[
\boxed{
\text{fixed-}q\text{ two-scale corrector}
\to q\to\infty\text{ through primes}
\to\text{scalar compact/determinant repair}
}
\]

cannot supply a Riemann-zero mechanism. Any surviving joint Hardy route must use genuinely simultaneous conductor structure or a non-scalar/nonlinear organization before this finite Ramanujan multiplicity has already classicalized.