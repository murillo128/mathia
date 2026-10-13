# PC-436 — Finite Fourier masks preserve sharp prime-log completeness

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-ONLY. PC-435 requires a lower spectral envelope for its incomplete-family converse. Multiplication by the modulus squared of a nonzero finite exponential polynomial destroys that lower bound, possibly at infinitely many real zeros, yet preserves the exact completeness/incompleteness threshold and infinite-codimension converse. The mechanism is finite-union stability of classical strip Blaschke zero sets; it does not constrain Riemann zeros.

## 1. Exact finite-mask theorem

Fix \(a>0\), \(0<\sigma<1\). Let the positive-a.e. base density \(w\) satisfy the PC-435 two-sided cusp envelope
\[
c\min\{|t|,1\}e^{-a|t|}
\le w(t)\le C(1+|t|)^K e^{-a|t|},
\qquad c,C>0,\ K\ge0.
\tag{1}
\]
For real frequencies \(b_1,\ldots,b_m\) and complex coefficients \(d_1,\ldots,d_m\), assume the finite exponential polynomial
\[
D(t)=\sum_{j=1}^m d_j e^{ib_jt}
\tag{2}
\]
is not identically zero. Set \(W(t)=w(t)|D(t)|^2\). The real-analytic function \(D\) has a discrete real zero set, so \(W>0\) almost everywhere although it need not satisfy any pointwise lower envelope.

For distinct \(X\subset[2,\infty)\) tending to infinity put
\[
q_x(t)=e^{it\log x},\quad
v_{x,\sigma}(t)=1-x^{1-\sigma}e^{it\log x},\quad
\alpha=\pi/a.
\tag{3}
\]
**Theorem:** in \(\mathscr H_W=L^2(\mathbb R,W(t)\,dt)\),
\[
\boxed{
\overline{\operatorname{span}}\{q_x:x\in X\}=\mathscr H_W
\iff
\overline{\operatorname{span}}\{v_{x,\sigma}:x\in X\}=\mathscr H_W
\iff
\sum_{x\in X}x^{-\alpha}=\infty .
}
\tag{4}
\]
If the series converges, the orthogonal complements of *both* systems contain the same infinite-dimensional subspace. The conclusion holds even if \(D(0)=0\), or if \(D\) has arbitrarily high-order or infinitely many real zeros. For instance \(D(t)=1-e^{ibt}\), \(b\ne0\), vanishes at all \(2\pi k/b\) without altering (4).

## 2. Divergence: the upper envelope already suffices

The trivial bound \(|D(t)|\le\sum_j|d_j|\) gives
\[
W(t)\le C_D(1+|t|)^K e^{-a|t|}.
\tag{5}
\]
Given \(h\in\mathscr H_W\), define
\[
F_h(z)=\int_{\mathbb R}h(t)W(t)e^{-izt}\,dt.
\tag{6}
\]
Cauchy--Schwarz extends it to \(|\Im z|<a/2\) with the polynomial boundary-growth estimate of PC-435 §2. Also \(hW\in L^1\), hence \(F_h(s)\to0\) at both real infinities. The strip-to-half-plane Blaschke argument from PC-435 needs only (5) and positivity almost everywhere: if \(\sum_{x\in X}x^{-\pi/a}=\infty\), either \(F_h(\log x)=0\) for all \(x\), or
\[
F_h(\log x)=F_h(0)x^{\sigma-1}
\quad(x\in X),
\tag{7}
\]
forces \(F_h\equiv0\). Fourier uniqueness then implies \(h=0\). These two conditions are orthogonality to the two systems in (3), proving the complete half of (4).

## 3. Convergence: factor the mask before taking the weighted quotient

Suppose \(\sum_{x\in X}x^{-\alpha}<\infty\). Prescribe the real zero multiset
\[
Z=\{\log x-b_j:\ x\in X,\ 1\le j\le m\}
  \ \cup\ \{-b_j:\ 1\le j\le m\}.
\tag{8}
\]
Its translated prime-log tails obey
\[
\sum_j e^{-\alpha(\log x-b_j)}
=\left(\sum_j e^{\alpha b_j}\right)x^{-\alpha}.
\tag{9}
\]
Thus \(Z\) satisfies the Blaschke condition in the strip \(S_a=\{|\Im z|<a/2\}\). There is a bounded, nonzero analytic \(B\in H^\infty(S_a)\) vanishing on \(Z\). For example, enumerating \(Z=(z_k)\), setting \(\lambda_k=e^{\alpha z_k}>0\), and retaining harmless repetitions, one may take
\[
B(z)=\prod_k\frac{\lambda_k-e^{\alpha z}}
                       {\lambda_k+e^{\alpha z}}.
\tag{10}
\]
Every factor has modulus at most one; the tail converges normally by (9), and the finitely many initial factors do not spoil convergence.

For any complex polynomial \(P\), set
\[
F_P(z)=e^{-z^2}B(z)P(z),\qquad
g_P(t)=\frac1{2\pi}\int_{\mathbb R}F_P(s)e^{ist}\,ds.
\tag{11}
\]
Choose \(P\) in the infinite-dimensional kernel of the single moment functional
\[
P\longmapsto\int_{\mathbb R}F_P(s)\,ds.
\tag{12}
\]
Then \(g_P(0)=0\), and \(sF_P(s)\in L^1\) implies \(g_P(t)=O(t)\) at the origin. Since \(B\) is bounded throughout the *full* strip and the Gaussian dominates every polynomial, \(F_P\) has uniformly bounded horizontal \(L^2\) norms. Contour shifting, Plancherel and Fatou as the horizontal lines approach both edges give
\[
\int_{\mathbb R}|g_P(t)|^2e^{a|t|}\,dt<\infty.
\tag{13}
\]
Together with \(g_P(t)=O(t)\) and the *unmasked* lower estimate in (1), this yields
\[
\int_{\mathbb R}\frac{|g_P(t)|^2}{w(t)}\,dt<\infty.
\tag{14}
\]

Define \(h_P(t)=g_P(t)/[w(t)\overline{D(t)}]\) wherever \(D(t)\ne0\), arbitrarily on its measure-zero zero set. Its weighted norm is exactly
\[
\|h_P\|_{\mathscr H_W}^2
=\int_{\mathbb R}\frac{|g_P(t)|^2}{w(t)}\,dt<\infty,
\qquad h_P(t)W(t)=g_P(t)D(t)\ \text{a.e.}
\tag{15}
\]
Thus the real zeros of \(D\) introduce no divisibility or integrability obstruction. With the Fourier convention of (6),
\[
F_{h_P}(z)=\sum_{j=1}^m d_jF_P(z-b_j).
\tag{16}
\]
By (8), every summand vanishes at \(z=0\) and at \(z=\log x\) for every \(x\in X\). Consequently
\[
F_{h_P}(0)=F_{h_P}(\log x)=0\quad(x\in X),
\tag{17}
\]
so \(h_P\) is orthogonal simultaneously to \(q_x\) and \(v_{x,\sigma}\). Because \(B\not\equiv0\), Fourier inversion, positivity of \(w\) and \(D\ne0\) a.e. make \(P\mapsto h_P\) injective on the infinite-dimensional polynomial kernel (12). This proves the infinite-codimension converse.

The decisive device is *factor-before-division*: construct the Fourier-annihilator density as \(g_PD\), then divide by \(w|D|^2\), so the factor \(D\) cancels exactly in (15). Applying PC-435's lower-envelope theorem directly to \(W\) would be invalid.

## 4. Source bridge, prior art, boundaries and falsification

This is a finite-mask extension of PC-435, relying on classical bounded-holomorphic Blaschke theory (Duren, *Theory of H^p Spaces*; Remmert, *Classical Topics in Complex Function Theory*) and strip Fourier/Paley--Wiener theory (Paley--Wiener, *Fourier Transforms in the Complex Domain*). These sources already appear in Prime Circle's SOURCES.md. The abstract zero-set and multiplier tools are prior art, not claimed to be new; the local mathematical increment is the explicit sharp thinning law for the masked PC-435 Hilbert controls, despite infinitely many missing lower-bound points.

For the zero-free matched Prime-Circle seed \(g_{0,\sigma}\), the masked control seed \(Dg_{0,\sigma}\) has \(W=|D|^2w_{0,\sigma}\). Under the PC-433 isometric embedding \(\mathcal J\), the masked prime shell family obeys
\[
\overline{\operatorname{span}}\{
\mathcal J[(1-p^{1-\sigma}e^{it\log p})Dg_{0,\sigma}]:
p\in\mathcal P\}=\mathcal A
\iff
\sum_{p\in\mathcal P}\frac1p=\infty.
\tag{18}
\]
The sparse case has infinite codimension, as do the corresponding marked translates. This mask is an *auxiliary control*, not asserted to be intrinsic to roots-of-unity geometry.

For the genuine zeta-weighted seed, (5) preserves the divergent-sum **sufficient** condition after a bounded finite mask, but there is no matching converse here: its unmasked density has a \(|\zeta(\sigma-it)|^2\) factor and lacks the required uniform lower envelope. The full zeta factor is not a finite Fourier polynomial on the critical strip. Thus spectral zeros by themselves do not destroy the PC-435 criterion, but (4) gives no zeta-zero exclusion, critical-line selection, or RH implication.

**Audit checks:** the minus sign in each Fourier shift of (16); both parts of the zero set (8), including \(z=-b_j\); the *full-strip* Hardy bound for (13) at the endpoint \(a/2\); the moment condition (12) for the cusp; and exact norm cancellation (15). An infinite/continuous mask introduces infinitely many translates and need not preserve Blaschke summability.
