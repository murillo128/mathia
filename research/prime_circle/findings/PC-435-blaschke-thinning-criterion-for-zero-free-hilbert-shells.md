# PC-435 — Sharp Blaschke thinning criterion for zero-free prime Hilbert shells

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-ONLY. The completeness theorem of PC-433 and the sharp spectral-envelope control of PC-434 admit one common strengthening. For an explicit class of positive cusp weights, an arbitrary subfamily of logarithmic shell vectors is complete **if and only if** its sample points violate the corresponding strip Blaschke condition. Consequently the *actual zero-free matched* Prime-Circle Hilbert--Schmidt shells remain complete after retaining only selected primes precisely when those primes have divergent reciprocal sum; otherwise both bare shells and marked translates have infinite-dimensional orthogonal complements. The analytic theorem is classical in mechanism (Hardy/Blaschke/Paley--Wiener); no independent novelty or implication for RH is claimed.

## 1. Exact weighted theorem

Let \(a>0\), and let \(w:\mathbb R\to(0,\infty)\) be positive almost everywhere. Assume constants \(c,C>0\), \(K\ge0\) give the two-sided envelope
\[
c\min\{|t|,1\}e^{-a|t|}
 \ \le\ w(t)\ \le\
C(1+|t|)^K e^{-a|t|}
\quad\text{for almost every }t.
\tag{1}
\]
Put \(\mathscr H_w=L^2(\mathbb R,w(t)\,dt)\). Let \(X\subset[2,\infty)\) be a set of distinct real numbers tending to infinity, and fix \(0<\sigma<1\). For \(x\in X\), put
\[
q_x(t)=e^{it\log x},\qquad
v_{x,\sigma}(t)=1-x^{1-\sigma}e^{it\log x}.
\tag{2}
\]

**Sharp weighted Blaschke dichotomy:**
\[
\boxed{
\overline{\operatorname{span}}_{\mathbb C}\{q_x:x\in X\}
=\mathscr H_w
\iff
\overline{\operatorname{span}}_{\mathbb C}\{v_{x,\sigma}:x\in X\}
=\mathscr H_w
\iff
\sum_{x\in X}x^{-\pi/a}=\infty.}
\tag{3}
\]
When the series converges, *both* orthogonal complements have infinite dimension. More strongly, they contain the same explicit infinite-dimensional subspace. This includes the exact endpoint: there is no assumption of prime density, regular variation, or a larger analytic strip.

The exponent \(\pi/a\) arises because the Fourier strip has half-width \(a/2\), and the map \(z\mapsto e^{\pi z/a}\) sends it onto the right half-plane.

## 2. Divergence gives completeness

For \(h\in\mathscr H_w\), define
\[
F(z)=\int_{\mathbb R}h(t)w(t)e^{-izt}\,dt.
\tag{4}
\]
Cauchy--Schwarz and the *upper* bound in (1) show that \(F\) is holomorphic on \(S_a=\{z:|\Im z|<a/2\}\), with
\[
|F(s+iy)|\le C_{h,w,a,K}(a-2|y|)^{-(K+1)/2}.
\tag{5}
\]
Also \(hw\in L^1\), hence \(F(s)\to0\) as \(s\to\pm\infty\). Suppose \(\sum_{x\in X}x^{-\pi/a}=\infty\) and, for some \(c_0\in\mathbb C\),
\[
F(\log x)=c_0x^{\sigma-1}\quad(x\in X).
\tag{6}
\]
In the right half-plane \(D=\{\Re Z>1\}\), set
\[
H(Z)=F((a/\pi)\operatorname{Log}Z)
       -c_0 Z^{(a/\pi)(\sigma-1)}.
\tag{7}
\]
With \(r=|Z|\), \(u=\Re Z>1\), the inequality
\(\pi-2|\arg Z|=2\arcsin(u/r)\ge2u/r\)
bounds the first term by \(O(r^{(K+1)/2})\); the second is bounded because \(\sigma<1\). Thus \(H(Z)/(Z+1)^N\) is bounded and holomorphic on \(D\) for any integer \(N>(K+1)/2\).

It vanishes at \(Z=x^{\pi/a}\). The disk map \(\phi(Z)=1-2/Z\) sends these zeros, apart from finitely many irrelevant initial points, to a sequence with
\[
1-|\phi(x^{\pi/a})|=2x^{-\pi/a}.
\tag{8}
\]
The divergent sum violates the Blaschke condition for a nonzero bounded holomorphic function. Hence \(H=0\). The identity theorem extends \(F(z)=c_0e^{(\sigma-1)z}\) throughout \(S_a\). Its decay as \(\Re z\to-\infty\) forces \(c_0=0\), so \(F\equiv0\). Fourier uniqueness then gives \(h=0\). Orthogonality to \(q_x\) is (6) with \(c_0=0\), and orthogonality to \(v_{x,\sigma}\) is (6) with \(c_0=F(0)\), proving both density implications.

## 3. Convergence yields a joint infinite-dimensional nullspace at the same exponent

Assume \(\sum_{x\in X}x^{-\pi/a}<\infty\), and set \(\alpha=\pi/a\), \(\lambda_x=x^\alpha>1\). On \(S_a\), the product
\[
B(z)=\prod_{x\in X}
 \frac{\lambda_x-e^{\alpha z}}{\lambda_x+e^{\alpha z}}
\tag{9}
\]
converges locally uniformly: each factor has modulus at most one since \(\Re(e^{\alpha z})>0\), and convergence follows from \(\sum_x\lambda_x^{-1}<\infty\). It is nonzero (the product at \(z=0\) is positive), bounded, and vanishes at every \(\log x\).

For a polynomial \(P\) define
\[
F_P(z)=z e^{-z^2}B(z)P(z).
\tag{10}
\]
Because \(|B|\le1\), its Gaussian decay gives a uniform horizontal \(L^2\) bound on **the full open strip** \(S_a\), not merely on a smaller strip. Thus \(F_P\in H^2(S_a)\), while \(F_P(\log x)=F_P(0)=0\). Restrict \(P\) to the infinite-dimensional kernel of the single linear functional
\[
P\longmapsto\int_{\mathbb R}F_P(s)\,ds.
\tag{11}
\]
The inverse Fourier transform
\[
g_P(t)=\frac1{2\pi}\int_{\mathbb R}F_P(s)e^{ist}\,ds
\tag{12}
\]
then satisfies \(g_P(0)=0\) and \(g_P(t)=O(t)\) near the origin, since \(sF_P(s)\in L^1\).

For \(|y|<a/2\), contour shifting and Plancherel give
\[
\int_{\mathbb R}|g_P(t)|^2e^{2yt}\,dt
 =\frac1{2\pi}\int_{\mathbb R}|F_P(s+iy)|^2\,ds
 \le C_P.
\tag{13}
\]
Letting \(y\to\pm a/2\) and using Fatou's lemma on the positive and negative half-lines yields
\[
\int_{\mathbb R}|g_P(t)|^2e^{a|t|}\,dt<\infty.
\tag{14}
\]
The *lower* bound in (1), (14), and \(g_P(t)=O(t)\) at zero imply
\[
\int_{\mathbb R}\frac{|g_P(t)|^2}{w(t)}\,dt<\infty.
\tag{15}
\]
Therefore \(h_P=g_P/w\in\mathscr H_w\), and its weighted Fourier transform equals \(F_P\). Both \(F_P(0)\) and \(F_P(\log x)\) vanish, so \(h_P\) annihilates **both** \(q_x\) and \(v_{x,\sigma}\) for all \(x\in X\). Multiplication by the nonzero analytic factor in (10), Fourier inversion, and positivity of \(w\) make \(P\mapsto h_P\) injective. The nullspace is infinite-dimensional.

This strengthens PC-434's below-threshold construction, which used a strict auxiliary strip \(b>a\). Here the \(H^2\) estimate (13) closes the **critical boundary at the original exponent** and proves the full converse under the two-sided weight hypothesis.

## 4. Zero-free Prime-Circle shell application and exact limitations

The PC-434 nonarithmetic cusp control
\[
w_a(t)=|t|\exp(-a\sqrt{1+t^2})
\tag{16}
\]
satisfies (1) for its indicated exponent \(a\). Hence (3) gives an exact criterion for *every* thinned log-level sample set in that model. In particular, for any subset \(\mathcal P\) of the primes, its two families are complete iff \(\sum_{p\in\mathcal P}p^{-\pi/a}\) diverges.

For the actual **zero-free matched PC-424/PC-433 seed**, put
\[
g_{0,\sigma}(t)=
-\frac{1+\sigma-it}{2(1-\sigma+it)}
 \frac{\Gamma(\sigma-it)}{\sqrt{2\pi}},\qquad
w_{0,\sigma}(t)=\frac2\pi|t|\,|g_{0,\sigma}(t)|^2.
\tag{17}
\]
The rational factor is nonvanishing and bounded away from zero on the real line. Two-sided Stirling asymptotics yield
\[
w_{0,\sigma}(t)\asymp_\sigma |t|^{2\sigma}e^{-\pi|t|}
\quad(|t|\to\infty),\qquad
w_{0,\sigma}(t)\asymp_\sigma |t|
\quad(t\to0).
\tag{18}
\]
Since \(2\sigma>0\) and the density is positive away from its cusp, (1) holds with \(a=\pi\). By the PC-433 unitary multiplication \(L^2(w_{0,\sigma})\to\mathcal E\) and Hilbert--Schmidt embedding, the *actual control shell commutators*
\[
C_{0,p,\sigma}
 =\mathcal J[(1-p^{1-\sigma}e^{it\log p})g_{0,\sigma}]
\tag{19}
\]
obey the sharp thinning law
\[
\boxed{
\overline{\operatorname{span}}\{C_{0,p,\sigma}:p\in\mathcal P\}
=\mathcal A
\quad\Longleftrightarrow\quad
\sum_{p\in\mathcal P}\frac1p=\infty.}
\tag{20}
\]
Exactly the same equivalence holds for the control's marked translates \(\{U_{\log p}g_{0,\sigma}:p\in\mathcal P\}\). In the convergent case both spans have infinite codimension. For example \(\mathcal P=\{p_{2^k}:k\ge1\}\), with \(p_m\) the \(m\)-th prime, is an infinite incomplete subfamily since \(p_{2^k}\ge2^k\).

For the **genuine zeta-weighted** seed \(g_{1,\sigma}\), the divergent-reciprocal-sum implication toward completeness survives unchanged from PC-433. The reverse implication does **not** follow: \(|\zeta(\sigma-it)|^2\) does not provide the uniform spectral *lower* envelope (1), and dividing a Hardy inverse transform by the genuine density may fail at zeta zeros or small values. Formula (20) is therefore asserted **only for the zero-free matched model**; no sparse-family converse, critical-line selection, or RH consequence is proved for the genuine model.

## 5. Prior art and audit boundary

The abstract tools are classical Hardy/Blaschke zero-set theory and horizontal-strip Fourier/Paley--Wiener \(H^2\) theory (Duren, *Theory of H^p Spaces*, 1970; Remmert, *Classical Topics in Complex Function Theory*, 1998; Paley and Wiener, *Fourier Transforms in the Complex Domain*, 1934), already anchored in Prime Circle's SOURCES.md for PC-433/PC-434. Classical Müntz-type completeness problems are nearby context, not an independent novelty claim. The Mathia-specific new statement is the exact **arbitrary-subfamily and zero-free Hilbert--Schmidt control-shell** specialization.

Decisive audit checks: the \(\pi/a\) conformal exponent; the separate use of *upper* and *lower* bounds in (1); the full-strip uniform \(H^2\) bound (13) needed for (14), rather than mere boundedness on narrower strips; the moment condition (11) eliminating the spectral cusp singularity; the positive \(2\sigma\) exponent in (18); and the strict exclusion of a genuine-zeta converse. Completeness does not imply a Bessel or Riesz bound, and the same mechanism is reproduced by the nonarithmetic weight (16).
