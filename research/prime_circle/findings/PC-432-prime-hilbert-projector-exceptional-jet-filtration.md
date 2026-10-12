# PC-432 — Exceptional prime Hilbert projector rates form a sharp Bernoulli jet filtration

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-BLIND. This completes the exceptional-vector question explicitly left open by PC-431. For every fixed \(0<\sigma<1\), the first nonzero derivative at the spectral cusp of a centered smooth vector determines the **exact** polynomial rate and Bernoulli profile of its one-prime cyclic projection error. Every finite jet order is realized, and nonzero smooth vectors flat at the cusp converge faster than any algebraic power of \((\log p)^{-1}\). The same complete hierarchy holds for PC-424's zero-free control; it supplies no new zeta-zero criterion or implication toward RH.

## 1. The exact source-generated projection

Use the common Hilbert--Schmidt Fourier sector \(\mathcal E=L^2(\mathbb R,(2/\pi)|t|dt)\) of PC-427. For \(j=1\) (actual Prime-Circle Bose seed) or \(j=0\) (the matched zero-free control), set

\[
g_{1,\sigma}(t)=\frac{\Gamma(\sigma-it)\zeta(\sigma-it)}{\sqrt{2\pi}},
\qquad
g_{0,\sigma}(t)=-\frac{1+\sigma-it}{2(1-\sigma+it)}
             \frac{\Gamma(\sigma-it)}{\sqrt{2\pi}},
\]
\[
w_j(t)=\frac2\pi|t||g_{j,\sigma}(t)|^2
      =|t|A_j(t),\qquad M_j=\int_{\mathbb R}w_j(t)dt>0.
\tag{1}
\]

The functions \(A_j\) are smooth, even and have integrable, exponentially decaying derivatives of every fixed order. Their cusp coefficients are strictly positive:

\[
A_1(0)=\frac{|\Gamma(\sigma)\zeta(\sigma)|^2}{\pi^2},
\qquad
A_0(0)=\frac{|\Gamma(\sigma)|^2}{\pi^2}
       \left(\frac{1+\sigma}{2(1-\sigma)}\right)^2.
\tag{2}
\]

Identify \(L^2(w_jdt)\) unitarily with \(\mathcal E\) by \(J_j f=g_{j,\sigma}f\). For a prime \(p\), write \(a=\log p\), \(T=2\pi/a\), and let \(Q_{j,p}\) project onto the \(T\)-periodic subspace in \(L^2(w_jdt)\), while \(Q_{j,1}\) projects onto constants. By PC-429--PC-430 these are well-defined and

\[
Q_{j,p}f(x)=
\frac{\sum_{\ell\in\mathbb Z}w_j(x+\ell T)f(x+\ell T)}
     {\sum_{\ell\in\mathbb Z}w_j(x+\ell T)},
\qquad
Q_{j,1}f=\mu_j(f):=\frac1{M_j}\int f(t)w_j(t)dt.
\tag{3}
\]

The corresponding Hilbert--Schmidt projectors are \(P_{j,p}=J_jQ_{j,p}J_j^{-1}\) and \(P_{g_j}=J_jQ_{j,1}J_j^{-1}\).

## 2. All finite exceptional orders and exact constants

Fix \(f\in C_c^\infty(\mathbb R)\), possibly complex-valued, and put \(h=f-\mu_j(f)\). Suppose \(h\) has a zero of exact finite order \(k\ge0\) at the cusp \(t=0\):

\[
h^{(r)}(0)=0\quad(0\le r<k),
\qquad c_k=\frac{h^{(k)}(0)}{k!}\ne0,
\qquad m=k+2.
\tag{4}
\]

For \(k=0\) this says only \(f(0)\ne\mu_j(f)\). Let \(\widetilde B_m(u)=B_m(\{u\})\) be the periodic Bernoulli polynomial. The following asymptotic holds **uniformly in the periodic coordinate** \(x\in\mathbb R\):

\[
\boxed{
Q_{j,p}f(x)-\mu_j(f)
=-\frac{2(2\pi)^m A_j(0)c_k}{mM_j(\log p)^m}
  \widetilde B_m(x/T)
 +O_{f,j,k}((\log p)^{-(m+1)}).}
\tag{5}
\]

Weighted periodic averaging then gives the sharp squared-norm limit

\[
\boxed{
\lim_{p\to\infty}(\log p)^{2m}
 \|(P_{j,p}-P_{g_j})(g_{j,\sigma}f)\|_{\mathcal E}^2
 =\frac{4(2\pi)^{2m}A_j(0)^2|c_k|^2}{m^2M_j}
   \int_0^1 B_m(u)^2du.}
\tag{6}
\]

The Bernoulli integral is explicitly

\[
\int_0^1B_m(u)^2du
=\frac{(-1)^{m-1}(m!)^2B_{2m}}{(2m)!}>0
\qquad(m\ge2),
\tag{7}
\]

so the **vector norm** has exact order \((\log p)^{-(k+2)}\), not just an upper bound. Every integer \(k\ge0\) is possible. In particular:

- \(k=0\): (5)--(6) reduce exactly to PC-431's \(B_2\) profile and its \(4\pi^4A_j(0)^2/(45M_j)\) squared-norm coefficient multiplying \(|f(0)-\mu_j(f)|^2\).
- \(k=1\): when \(f(0)=\mu_j(f)\) but \(f'(0)\ne0\), the \(B_3\) profile yields
  \[
  \lim_{p\to\infty}(\log p)^6
   \|(P_{j,p}-P_{g_j})(g_{j,\sigma}f)\|^2
   =\frac{32\pi^6 A_j(0)^2}{945M_j}|f'(0)|^2.
  \tag{8}
  \]
- \(k=2\): when also \(f'(0)=0\) but \(f''(0)\ne0\), the \(B_4\) profile yields
  \[
  \lim_{p\to\infty}(\log p)^8
   \|(P_{j,p}-P_{g_j})(g_{j,\sigma}f)\|^2
   =\frac{4\pi^8 A_j(0)^2}{525M_j}|f''(0)|^2.
  \tag{9}
  \]

Here and below limits are along primes \(p\to\infty\); nothing requires a continuous choice of prime scale.

## 3. Proof from the first surviving cusp jet

Let \(v(t)=w_j(t)h(t)\). Its integral is zero by the definition of \(\mu_j\). Since \(A_j\) is smooth and even, near the origin

\[
v(t)=A_j(0)c_k\,t^k|t|+
      \text{terms of strictly higher local order}.
\tag{10}
\]

On the two sides of zero, \(t^k|t|=\pm t^{k+1}\), so its derivative of order \(k+1=m-1\) has jump \(2(k+1)!\). Piecewise integration by parts, or equivalently the distributional derivative of this jump, gives for the Fourier convention \(\widehat v(\xi)=\int v(t)e^{-i\xi t}dt\)

\[
\widehat v(\xi)=
\frac{2(m-1)!A_j(0)c_k}{(i\xi)^m}
+O_{f,j,k}(|\xi|^{-(m+1)})
\qquad(|\xi|\to\infty).
\tag{11}
\]

The remainder follows by localizing (10), integrating the next cusp Taylor terms, and integrating the smooth rapidly decreasing remainder sufficiently many times. All estimates hold for fixed \(f,\sigma,k\); no uniformity in \(f\) or in \(\sigma\) is claimed.

Poisson periodization applies with absolutely summable Fourier coefficients:

\[
T\sum_{\ell}v(x+\ell T)
=\sum_{n\ne0}\widehat v(na)e^{ina x}
=-\frac{2(2\pi)^m A_j(0)c_k}{m a^m}
     \widetilde B_m(x/T)+O(a^{-(m+1)}),
\tag{12}
\]

using the classical uniformly convergent Bernoulli series

\[
\sum_{n\ne0}\frac{e^{2\pi inu}}{n^m}
=-\frac{(2\pi i)^m}{m!}B_m(\{u\}),\qquad m\ge2.
\tag{13}
\]

For the denominator, PC-431 already proves

\[
T\sum_\ell w_j(x+\ell T)=M_j+O(a^{-2})
\tag{14}
\]

uniformly in \(x\). Divide (12) by (14). Its denominator correction is of order \(a^{-(m+2)}\), smaller than the stated remainder, proving (5).

Finally, the \(L^2(w_jdt)\) norm of \(Q_{j,p}f-Q_{j,1}f\) is computed by inserting (5), integrating against \(w_j\), and using weak averaging of a continuous 1-periodic function against an \(L^1\) density:

\[
\int_\mathbb R w_j(t)
      |\widetilde B_m(t/T)|^2dt
\longrightarrow M_j\int_0^1B_m(u)^2du.
\tag{15}
\]

The uniform error in (5) is negligible in the scaled norm. Equation (7) is the classical Bernoulli-product integral. This proves (6) and the displayed special cases.

## 4. Flat centered vectors and sharpness of every level

If every derivative of \(h=f-\mu_j(f)\) vanishes at zero, then \(w_jh=|t|A_j(t)h(t)\) extends to a smooth rapidly decreasing function on all of \(\mathbb R\). Its Fourier transform decays faster than every inverse power. Because its zero Fourier coefficient is \(\int w_jh=0\), Poisson summation and the positive denominator imply that for every integer \(N\ge1\)

\[
\boxed{\quad
\sup_x|Q_{j,p}f(x)-\mu_j(f)|
+\|(P_{j,p}-P_{g_j})(g_{j,\sigma}f)\|_{\mathcal E}
=O_{f,j,N}((\log p)^{-N}).\quad}
\tag{16}
\]

There are nonzero examples: take two smooth compact bumps supported away from zero and scale their coefficients to make their \(w_j\)-weighted integral zero. Then \(\mu_j(f)=0\) and \(h=f\) vanishes in a neighborhood of the cusp. More generally, prescribe the germ \(h(t)=c_k t^k\) with a compact cutoff near zero and use one additional bump away from zero to cancel its weighted integral; the resulting \(f=h\) has \(\mu_j(f)=0\) and realizes **any** selected finite \(k\) and nonzero leading coefficient. Thus the rates in (6) are not formal or empty.

This vectorwise hierarchy is consistent with PC-430: for **every** prime \(\|P_{j,p}-P_{g_j}\|_{\mathcal B(\mathcal E)}=1\). No operator-norm convergence or uniform error over smooth vectors is asserted. A vector flat at the unique cusp removes all algebraic aliasing tails; it does not reduce the dimension of the prime cyclic subspace.

## 5. Prior art, controls, and RH boundary

The underlying mechanism is classical: a jump in a derivative produces a corresponding inverse-power Fourier tail; Poisson summation converts those tails into periodic Bernoulli polynomials; the exact \(L^2\) constants follow from Bernoulli Fourier orthogonality. See NIST DLMF §§24.8 (Bernoulli Fourier series), 24.13 (Bernoulli-product integrals) and 2.10 (Euler--Maclaurin), together with the modern Euler--Maclaurin references already recorded in the line's SOURCES.md for PC-431. **No independent novelty is claimed for this analytic lemma.** The line-local increment is its complete sharp exceptional-vector classification for the actual PC-427--PC-430 Hilbert--Schmidt prime orbit and its genuine/nonarithmetic matched pair.

The analytic argument uses only \(w=|t|A(t)\) with a smooth even positive cusp coefficient and sufficient derivative decay. Thus it applies unchanged to the explicitly zero-free seed \(j=0\) and to the nonarithmetic control \(w(t)=|t|e^{-t^2}\), for which \(M=A(0)=1\). For the latter, \(f(t)=t e^{-t^2}\) has zero weighted mean and first jet \(1\), and \(f(t)=(t^2-t^4)e^{-t^2}\) has zero weighted mean and second jet \(f''(0)=2\); their exact \(B_3/B_4\) limits follow by the same Schwartz-class proof. The Gaussian illustrations extend beyond the displayed compactly supported test class but satisfy the same decay assumptions; they are controls, not additional claims about primes.

This closes PC-431's **smooth exceptional-vector rate question**, not the main geometric-to-RH bridge. The cusp \(|t|\) is universal to the Hilbert--Schmidt commutator measure and its derivative filtration does not distinguish actual zeta zeros from the zero-free matched model. The exact Fourier numerator retains the original Mellin spectral density, but the asymptotic rates and Bernoulli profiles use only its local smooth Taylor coefficients and cannot exclude a nonreal off-critical zero. Neither this finding nor PC-431 yields an RH implication.
