# PC-433 — The bare prime Hilbert-commutator shells are complete despite having no frame bounds

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-BLIND. For every fixed real \(0<\sigma<1\), the actual prime-indexed Hilbert--Schmidt commutators from PC-424 and PC-426 have dense complex linear span in the complete embedded Fourier-kernel sector of PC-427. A single primitive-shell commutator per prime suffices: no prime powers, inverse shifts, mixed products, or extra closure-generating operators are needed. PC-426 nevertheless proves that even the normalized family is neither Bessel nor Riesz. The result holds verbatim for the zero-free matched shell family, so neither completeness nor its extreme ill-conditioning constrains the nontrivial zeros of zeta or implies RH.

## 1. The exact source-generated family and new completeness claim

Fix \(0<\sigma<1\) and let \(\mathcal K=\mathcal S_2(L^2(\mathbb R))\). In PC-427, the Hilbert--Schmidt kernel embedding \(\mathcal J:\mathcal E\longrightarrow\mathcal K\) is isometric, where
\[
\mathcal E=L^2\!\left(\mathbb R,\frac2\pi |t|\,dt\right),
\qquad
\mathcal A=\mathcal J(\mathcal E),
\qquad
(U_a g)(t)=e^{iat}g(t).
\tag{1}
\]
For \(j=1\) (genuine) and \(j=0\) (zero-free PC-424 control), write the two fixed seeds as
\[
g_{1,\sigma}(t)=
 \frac{\Gamma(\sigma-it)\zeta(\sigma-it)}{\sqrt{2\pi}},
\qquad
g_{0,\sigma}(t)=
 -\frac{1+\sigma-it}{2(1-\sigma+it)}
 \frac{\Gamma(\sigma-it)}{\sqrt{2\pi}},
\tag{2}
\]
and let \(w_j(t)=\frac2\pi |t|\,|g_{j,\sigma}(t)|^2\).
Both \(w_j\) are integrable and positive Lebesgue-almost-everywhere. By PC-424/PC-426, the *actual* primitive prime-shell commutators in the two models are
\[
C_{j,p,\sigma}
 =\mathcal J\bigl[(1-p^{1-\sigma}e^{it\log p})g_{j,\sigma}(t)\bigr],
\qquad p\text{ prime}.
\tag{3}
\]
For \(j=1\), this is \(B_\sigma-p^{1-\sigma}\mathcal T_{\log p}B_\sigma\), not merely the translate of an arbitrary seed.

**Claim.** For each \(j\in\{0,1\}\) and fixed \(0<\sigma<1\),
\[
\boxed{\displaystyle
\overline{\operatorname{span}}^{\,\mathcal K}_{\mathbb C}
 \{C_{j,p,\sigma}:p\text{ prime}\}=\mathcal A.}
\tag{4}
\]
In particular, the *normalized* family \(C_{j,p,\sigma}/\|C_{j,p,\sigma}\|\) is complete while being neither a Bessel nor a Riesz family (PC-426). This is completeness of the bare one-vector-per-prime shell family, a question not settled by PC-427's mixed two-shift cyclicity or by PC-430's finite sums of single-prime cyclic subspaces.

## 2. Exponential spectral envelope and a strip-to-half-plane uniqueness lemma

Stirling's bound on a fixed vertical line gives
\[
|\Gamma(\sigma-it)|^2
 \ll_\sigma (1+|t|)^{2\sigma-1}e^{-\pi|t|}.
\tag{5}
\]
The zeta factor has polynomial growth on the fixed vertical line \(0<\sigma<1\), and the rational factor of \(g_{0,\sigma}\) is bounded on the real axis. Thus for some finite \(K\ge0\) and \(D>0\), depending on \(j,\sigma\),
\[
0<w_j(t)\le D(1+|t|)^K e^{-\pi|t|}
\quad\text{a.e.}
\tag{6}
\]
The exponent is \(\pi\), from the **squared** Gamma modulus. The whole proof depends on retaining that exponent rather than weakening it to an arbitrary smaller strip.

More generally, let \(w\) be any finite positive-a.e. density obeying (6) and let \(h\in L^2(w\,dt)\). Set
\[
F(\lambda)=\int_{\mathbb R}h(t)w(t)e^{-i\lambda t}\,dt.
\tag{7}
\]
Cauchy--Schwarz implies that \(F\) is holomorphic in the open strip
\[
S=\{\lambda:|\operatorname{Im}\lambda|<\pi/2\}
\]
and has the uniform bound
\[
|F(x+iy)|
\le\|h\|_{L^2(w)}
 \left(\int w(t)e^{2yt}\,dt\right)^{1/2}
\le C_{h,w}(\pi-2|y|)^{-(K+1)/2}.
\tag{8}
\]
For the last inequality, split the integral at zero and integrate the elementary polynomial-exponential majorant. Also \(hw\in L^1\), so \(F(x)\to0\) as \(x\to\pm\infty\) by Riemann--Lebesgue.

**Prime-log uniqueness lemma.** If \(F\) obeys (7)--(8) and for some complex \(c\) and fixed real \(0<\sigma<1\)
\[
F(\log p)=c\,p^{\sigma-1}
\qquad\text{for every prime }p,
\tag{9}
\]
then \(F\equiv0\) and \(c=0\). The same conclusion holds when \(c=0\), without any restriction on \(\sigma\).

To prove this, use the principal logarithm on the half-plane \(D=\{z:\operatorname{Re}z>1\}\) and put
\[
H(z)=F(\operatorname{Log}z)-c\,z^{\sigma-1}.
\tag{10}
\]
For \(z\in D\), \(|\arg z|<\pi/2\). Writing \(r=|z|\) and \(u=\operatorname{Re}z>1\), elementary geometry gives
\[
\pi-2|\arg z|
=2\arcsin(u/r)\ge 2u/r.
\tag{11}
\]
Consequently (8) implies
\[
|F(\operatorname{Log}z)|\le C_{h,w}(r/u)^{(K+1)/2}
\le C_{h,w}r^{(K+1)/2}.
\tag{12}
\]
As \(\sigma-1<0\) and \(r>1\), the term \(c z^{\sigma-1}\) is bounded on \(D\). Thus \(H(z)/(z+1)^N\) is a bounded holomorphic function on \(D\) for any integer \(N>(K+1)/2\), since \(|z+1|>|z|\) there. By (9) it vanishes at every prime \(z=p\ge2\).

The Möbius map
\[
\phi(z)=\frac{z-2}{z}=1-\frac2z
\tag{13}
\]
maps \(D\) conformally to the unit disk and sends a prime \(p\ge2\) to the distinct point \(1-2/p\in[0,1)\). The zeros of a nonzero bounded holomorphic disk function must satisfy the classical Blaschke condition. Here that condition fails:
\[
\sum_{p\text{ prime}}(1-|\phi(p)|)
=\sum_p\frac2p=\infty
\tag{14}
\]
by Euler's divergence of the prime harmonic series. Hence \(H/(z+1)^N\equiv0\), and
\[
F(\operatorname{Log}z)=c\,z^{\sigma-1}
\quad(z\in D).
\tag{15}
\]
The identity theorem extends \(F(\lambda)=ce^{(\sigma-1)\lambda}\) to the entire connected strip \(S\). Since \(F(x)\to0\) as \(x\to-\infty\), while \(e^{(\sigma-1)x}\to\infty\), necessarily \(c=0\). Thus \(F\equiv0\). For \(c=0\) the Blaschke argument already gives the conclusion. Finally Fourier uniqueness for the finite complex measure \(h(t)w(t)\,dt\) implies \(hw=0\) a.e. and hence \(h=0\) in \(L^2(w\,dt)\).

## 3. Application to the actual shell commutators

Multiplication by either \(g_{j,\sigma}\) is a unitary map
\[
J_j:L^2(w_j\,dt)\longrightarrow\mathcal E,\qquad J_jh=g_{j,\sigma}h,
\tag{16}
\]
because \(g_{j,\sigma}\ne0\) a.e. Suppose \(J_jh\) is orthogonal in \(\mathcal E\) to the Fourier preimage of every \(C_{j,p,\sigma}\) in (3). With \(F\) from (7),
\[
0=
\langle h,1-p^{1-\sigma}e^{it\log p}\rangle_{L^2(w_j)}
=F(0)-p^{1-\sigma}F(\log p).
\tag{17}
\]
Thus \(F(\log p)=F(0)p^{\sigma-1}\). Apply the uniqueness lemma with \(c=F(0)\); it yields \(h=0\). The orthogonal complement of the complex span in (4) is therefore trivial, which proves (4) for both the genuine and zero-free models.

The simpler system of single prime shifts of the marked seed is already complete:
\[
\boxed{\displaystyle
\overline{\operatorname{span}}
 \{U_{\log p}g_{j,\sigma}:p\text{ prime}\}
=\mathcal E.}
\tag{18}
\]
Indeed, orthogonality to those shifts is the special case \(F(\log p)=0\) of the same lemma. The proof applies as well to any distinct real labels \(x_n\ge2\) with \(\sum_n1/x_n=\infty\), using \(\log x_n\) and the zero-set points \(1-2/x_n\); such controls need not be primes.

## 4. Finite/infinite closure, prior art, controls and audit

For every **finite** prime set \(E\), PC-430 constructs an infinite-dimensional orthogonal complement to the closure of the additive sum of the full one-prime cyclic subspaces \(\mathcal H_{j,p}\), \(p\in E\). Yet each \(\mathcal H_{j,p}\) contains the single shifted seed \(U_{\log p}g_j\) and the shell \(C_{j,p,\sigma}\). From (4) or (18) follows the strict finite/infinite transition
\[
\boxed{\displaystyle
\overline{\sum_{p\in E}\mathcal H_{j,p}}
\subsetneq\mathcal E
\quad(E\text{ finite}),\qquad
\overline{\sum_{p\text{ prime}}\mathcal H_{j,p}}
=\mathcal E.}
\tag{19}
\]
There is no contradiction with PC-426's non-Bessel/non-Riesz theorem: density of a span imposes no uniform synthesis bound, and the normalized prime vectors have arbitrarily ill-conditioned finite Gram blocks. Nor does (4) contradict PC-430's strong convergence of each individual projector to the seed line: the vectors needed for completeness vary with the prime and with the coefficients, and there is no uniform finite-dimensional approximation theorem here.

**Prior art.** The strip-to-half-plane argument uses classical Stirling asymptotics (NIST DLMF §5.11), standard polynomial vertical-strip bounds for zeta, the bounded-holomorphic-function Blaschke zero-set theorem (R. Remmert, *Classical Topics in Complex Function Theory*, Graduate Texts in Mathematics 172, Springer, 1998, chapter on holomorphic functions with prescribed zeros, DOI 10.1007/978-1-4757-2956-6), Fourier uniqueness and the classical divergence of \(\sum_p1/p\). The mechanism is in the spirit of classical completeness/uniqueness theorems for exponential systems; no independent novelty is claimed for the abstract complex-analysis lemma. The line-local increment is its specialization to the **unweighted, actual source-generated prime-shell Hilbert--Schmidt commutators** left unclassified by PC-426--PC-430, with a complete zero-free matched-control calculation.

**Source-specificity and failure mode.** No step used RH, zero location, prime gaps, or even the special value of the smooth spectral factor beyond the positive-a.e. exponential envelope. The zero-free PC-424 seed has the same density and completeness, and nonprime labels with divergent reciprocal sum also work. Therefore this is a precise closure theorem, not a Hilbert--Pólya spectrum or RH-facing positivity statement. The lemma supplies a sufficient divergence criterion, not a claimed converse when \(\sum1/x_n<\infty\).

**Decisive audit points.** Verify (3)'s sign and scaling directly from PC-424/PC-426, the \(\pi\) exponent in (5)--(6) from **squared** Gamma, the Cauchy--Schwarz strip half-width \(\pi/2\) for *arbitrary* \(L^2(w)\) vectors, the polynomial boundary growth (11)--(12), the exact disk map and failure of Blaschke (13)--(14), and the Riemann--Lebesgue step on the negative real axis (necessary for the nonzero \(c\) case). No analytic continuation through the strip boundary is used, and no assertion of stable/invertible synthesis follows from completeness.
