# PC-434 — Prime-log completeness has a sharp spectral-decay threshold in a cusp control

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-ONLY. The analytic uniqueness argument in PC-433 uses the full exponential envelope \(\exp(-\pi|t|)\) of the actual Gamma-weighted Prime-Circle Hilbert--Schmidt sector. For an explicit positive, nonarithmetic spectral-cusp control, that decay exponent is **sharp**: the bare one-vector-per-prime shells and prime-log translates are complete precisely when the spectral exponential rate is at least \(\pi\). Below \(\pi\), each system has an infinite-dimensional orthogonal complement. The argument is a specialization of classical Hardy/Blaschke and Fourier-strip theory; it does not give a new zeta-zero criterion.

## 1. Exact threshold in the control Hilbert spaces

For every \(a>0\), fix the concrete even density
\[
 w_a(t)=|t|\exp\!\left(-a\sqrt{1+t^2}\right),\qquad
 \mathscr H_a=L^2(\mathbb R,w_a(t)\,dt).
 \tag{1}
\]
This is an integrable, positive-a.e. density with the same linear cusp at \(t=0\) as PC-431--PC-433; its exponential tail is controlled by the independent parameter \(a\). Fix any real \(0<\sigma<1\). For primes \(p\), put
\[
 q_p(t)=e^{it\log p},\qquad
 v_{p,\sigma}(t)=1-p^{1-\sigma}e^{it\log p}.
 \tag{2}
\]
These reproduce the normalized Fourier-coordinate *shape*, but not the source-dependent zeta/Gamma spectral weight, of the genuine PC-433 commutators.

**Theorem.** In the complex Hilbert space \(\mathscr H_a\),
\[
 \boxed{\ \overline{\operatorname{span}}\{q_p:p\text{ prime}\}
       =\mathscr H_a\quad\Longleftrightarrow\quad a\ge\pi,\ }
 \tag{3}
\]
and, separately,
\[
 \boxed{\ \overline{\operatorname{span}}\{v_{p,\sigma}:p\text{ prime}\}
       =\mathscr H_a\quad\Longleftrightarrow\quad a\ge\pi.\ }
 \tag{4}
\]
For every \(0<a<\pi\), **both orthogonal complements are infinite-dimensional**. The endpoint \(a=\pi\) belongs to the complete regime.

This supplies a converse *within the stated control family* to the sufficient-exponential-envelope theorem used in PC-433. It does not claim that an arbitrary positive spectral density with slower decay must be incomplete.

## 2. Completeness at and above the endpoint

Let \(a\ge\pi\), \(h\in\mathscr H_a\), and write
\[
 F(z)=\int_{\mathbb R}h(t)w_a(t)e^{-izt}\,dt.
 \tag{5}
\]
Since \(h w_a\in L^1\), \(F(x)\to0\) as \(x\to\pm\infty\). Because
\[
 0<w_a(t)\le |t|e^{-\pi|t|}\quad(t\ne0),
 \tag{6}
\]
Cauchy--Schwarz extends \(F\) holomorphically to
\(S=\{z:|\operatorname{Im}z|<\pi/2\}\), with
\[
 |F(x+iy)|\le
 \|h\|_{\mathscr H_a}
 \left(\int_{\mathbb R}|t|e^{-(\pi-2|y|)|t|}\,dt\right)^{1/2}
 =\frac{\sqrt2\,\|h\|_{\mathscr H_a}}{\pi-2|y|}.
 \tag{7}
\]

The following uniqueness implication therefore applies:
\[
 F(\log p)=c\,p^{\sigma-1}\ \text{for all primes }p
 \quad\Longrightarrow\quad F\equiv0,\quad c=0.
 \tag{8}
\]
For completeness, map the right half-plane \(D=\{\Re z>1\}\) to the strip by the principal logarithm. Put
\(G(z)=F(\operatorname{Log}z)-c z^{\sigma-1}\).
For \(z\in D\), writing \(r=|z|\) and \(u=\Re z>1\),
\[
 \pi-2|\arg z|=2\arcsin(u/r)\ge 2u/r.
 \tag{9}
\]
Thus (7) gives \(|F(\operatorname{Log}z)|\le C r/u\le Cr\); the remaining term \(c z^{\sigma-1}\) is bounded on \(D\). Consequently \(G(z)/(z+1)^2\) is bounded and holomorphic on \(D\). It vanishes at all primes by (8)'s hypothesis. Under the disk map
\[
 \phi(z)=\frac{z-2}{z},\qquad \phi(p)=1-\frac2p,
 \tag{10}
\]
the putative nonzero bounded holomorphic function would have zeros violating Blaschke:
\[
 \sum_{p}(1-|\phi(p)|)=2\sum_p\frac1p=\infty.
 \tag{11}
\]
Therefore \(G\equiv0\). By analytic continuation \(F(z)=ce^{(\sigma-1)z}\) throughout \(S\). Riemann--Lebesgue decay as \(x\to-\infty\) (indeed at both ends) forces \(c=0\). Fourier uniqueness then gives \(h=0\).

If \(h\) is orthogonal to all \(q_p\), then \(F(\log p)=0\), so (8) with \(c=0\) proves (3) for \(a\ge\pi\). If it is orthogonal to all \(v_{p,\sigma}\), then
\[
 0=\langle h,v_{p,\sigma}\rangle
   =F(0)-p^{1-\sigma}F(\log p),
 \tag{12}
\]
so (8) with \(c=F(0)\) proves (4). No RH hypothesis or estimate on prime gaps is used.

## 3. Explicit infinitely many annihilators below \(\pi\)

Now take \(0<a<\pi\). Choose once and for all \(b\) with
\[
 a<b<\pi,\qquad \alpha=\pi/b>1,\qquad
 S_b=\{z:|\Im z|<b/2\}.
 \tag{13}
\]
The map \(z\mapsto e^{\alpha z}\) sends \(S_b\) conformally onto the right half-plane. Since \(\sum_p p^{-\alpha}<\infty\), the product
\[
 B_b(z)=\prod_{p\text{ prime}}
 \frac{p^\alpha-e^{\alpha z}}{p^\alpha+e^{\alpha z}}
 \tag{14}
\]
converges locally uniformly in \(S_b\) to a **nonzero bounded holomorphic function** with \(|B_b|\le1\) and
\[
 B_b(\log p)=0\quad\text{for every prime }p.
 \tag{15}
\]
The local convergence follows directly from the summability of
\(2e^{\alpha z}/(p^\alpha+e^{\alpha z})\) on each compact subset. The factors have modulus \(<1\) because \(\Re(e^{\alpha z})>0\); the product is nontrivial, for example at \(z=0\).

For any complex polynomial \(P\), set
\[
 F_P(z)=z e^{-z^2}B_b(z)P(z).
 \tag{16}
\]
The factor \(z\) guarantees \(F_P(0)=0\), and (15) guarantees
\(F_P(\log p)=0\) for every prime. On every closed narrower strip
\(|\Im z|\le y<b/2\), \(F_P\) is holomorphic and rapidly decreasing as
\(|\Re z|\to\infty\), uniformly on horizontal lines. Impose one linear condition on \(P\):
\[
 \int_{\mathbb R}F_P(x)\,dx=0.
 \tag{17}
\]
The kernel of this linear functional in the infinite-dimensional polynomial space is itself infinite-dimensional; the multiplication \(P\mapsto F_P\) is injective because \(B_b\not\equiv0\).

Let
\[
 g_P(t)=\frac1{2\pi}\int_{\mathbb R}F_P(x)e^{ixt}\,dx.
 \tag{18}
\]
The Gaussian decay gives smoothness of \(g_P\), and (17) gives \(g_P(0)=0\), hence \(g_P(t)=O(|t|)\) near the origin. Cauchy's theorem permits shifting (18)'s contour to \(\Im z=\pm y\) for every \(y<b/2\), yielding
\[
 |g_P(t)|\le C_{P,y}e^{-y|t|}.
 \tag{19}
\]
Choose \(y\) with \(a/2<y<b/2\). As
\(w_a(t)\asymp |t|\) near zero and
\(w_a(t)\asymp |t|e^{-a|t|}\) at infinity, (19) and \(g_P(0)=0\) imply
\[
 \int_{\mathbb R}\frac{|g_P(t)|^2}{w_a(t)}\,dt<\infty.
 \tag{20}
\]
Thus \(h_P=g_P/w_a\) (defined a.e.) is a nonzero vector in \(\mathscr H_a\), and its weighted Fourier transform is precisely \(F_P\):
\[
 \widehat{h_P w_a}(\lambda)=F_P(\lambda).
 \tag{21}
\]
Equations (15)--(17) now yield
\(\langle h_P,q_p\rangle=0\) and
\(\langle h_P,v_{p,\sigma}\rangle=0\) for **every** prime. Fourier injectivity and injectivity of \(P\mapsto F_P\) show that the admissible polynomials give infinitely many linearly independent annihilators. This proves the two converse directions and the claimed infinite codimensions.

## 4. Prior art, controls, exact scope, and audit checks

**Classical inputs.** The zero-set necessity and sufficiency behind (10)--(15) are standard Blaschke/Hardy-space theory (P. L. Duren, *Theory of \(H^p\) Spaces*, Academic Press, 1970; R. Remmert, *Classical Topics in Complex Function Theory*, Springer GTM 172, 1998, DOI 10.1007/978-1-4757-2956-6). The connection between holomorphy in a horizontal strip and exponentially decaying inverse Fourier transforms is classical Paley--Wiener Fourier analysis (R. E. A. C. Paley and N. Wiener, *Fourier Transforms in the Complex Domain*, AMS Colloquium Publications 19, 1934, DOI 10.1090/coll/019); (18)--(20) are proved directly here by contour shifting. The number-theoretic distinction is only Euler's divergence of \(\sum_p1/p\) versus convergence of \(\sum_p p^{-\alpha}\) for \(\alpha>1\). The abstract theory is not claimed as new.

**Line-local increment.** PC-433 proved density of the *actual* prime-shell commutators using the squared-Gamma exponential rate \(\pi\); it did not prove that this rate is optimal among admissible spectral controls. The theorem here identifies the exact transition for a concrete nonarithmetic family sharing the Hilbert--Schmidt cusp and the same bare shell multipliers. The control changes the **envelope**, not the prime arithmetic, so its incompleteness below \(\pi\) does not contradict PC-433. It shows why the PC-433 uniqueness argument cannot be extended to arbitrary slower-decay densities just by retaining the prime-log sample set.

**What is not proved.** The theorem is not a necessity criterion for every positive density of rate \(a<\pi\); extra smoothness, support restrictions, or other analytic structure can change uniqueness. Neither the universal critical exponent \(\pi\) nor the completeness/incompleteness of this toy family selects \(\Re s=1/2\), detects nontrivial zeta zeros, or implies RH. The actual \(w_j\) from PC-433 retain the proven complete status.

**Decisive audit.** Check the half-width \(a/2\) in (7), the right-half-plane angle inequality (9), the reciprocal-prime Blaschke divergence at the endpoint, the use of \(\alpha=\pi/b>1\) for convergence of (14), the necessity of **both** \(F_P(0)=0\) and \(\int F_P=0\) in the below-threshold construction, and the strict choice \(a/2<y<b/2\) in (19)--(20). Dropping the moment condition (17) would invalidate integrability at the cusp \(|t|=0\); confusing the analytic strip's full width with its half-width would shift the claimed threshold by a factor of two.
