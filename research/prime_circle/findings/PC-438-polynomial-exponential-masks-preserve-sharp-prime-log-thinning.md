# PC-438 — Polynomial-exponential masks preserve sharp prime-log thinning by finite Fourier jets

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CONTROL-ONLY. The sharp weighted completeness criterion of PC-435 persists under every nonzero *finite polynomial-exponential* spectral mask, including unbounded polynomial amplitudes and arbitrarily high-order real zeros. This is not covered by PC-436's bounded finite Fourier masks or by PC-437's bounded periodic analytic factorization. The new proof obligation is finite-order derivative interpolation at the shifted logarithmic sample points. All inputs are classical Blaschke/Paley--Wiener/Fourier calculus; the result is an auxiliary control classification, with no RH implication.

## 1. Precise finite differential-delay mask theorem

Fix \(a>0\), \(0<\sigma<1\), and a positive-a.e. density \(w\) satisfying the PC-435 envelope
\[
c\min\{|t|,1\}e^{-a|t|}
 \le w(t)\le C(1+|t|)^K e^{-a|t|}
\quad\text{a.e.},\qquad c,C>0,\ K\ge0. \tag{1}
\]
Let \(b_1,\ldots,b_J\in\mathbb R\), let \(P_1,\ldots,P_J\in\mathbb C[t]\), and suppose
\[
D(t)=\sum_{j=1}^J P_j(t)e^{ib_jt}\not\equiv0.
\tag{2}
\]
Repeated frequencies may be combined; the statement does not require the real zeros of \(D\) to be simple, periodically spaced, or finite in number. Since \(D\) is a nonzero entire function, its real zeros are discrete, so \(W=w|D|^2>0\) a.e. and \(\mathscr H_W=L^2(\mathbb R,W(t)\,dt)\) is well-defined.

For any distinct \(X\subset[2,\infty)\) tending to infinity, set
\[
q_x(t)=e^{it\log x},\qquad
v_{x,\sigma}(t)=1-x^{1-\sigma}e^{it\log x},\qquad
\alpha=\pi/a.
\tag{3}
\]
Then
\[
\boxed{\begin{aligned}
\overline{\operatorname{span}}\{q_x:x\in X\}=\mathscr H_W
&\iff
\overline{\operatorname{span}}\{v_{x,\sigma}:x\in X\}=\mathscr H_W\\[-2pt]
&\iff \sum_{x\in X}x^{-\alpha}=\infty.
\end{aligned}}\tag{4}
\]
When the series converges, the two orthogonal complements contain the **same infinite-dimensional linear subspace**, even if \(D(0)=0\) or \(D\) has real zeros of large multiplicity.

## 2. Divergent sampling: polynomial growth does not alter the strip

Put \(r=\max_j\deg P_j\), omitting zero polynomials. Because the frequencies \(b_j\) are real,
\[
|D(t)|\le C_D(1+|t|)^r,\qquad
W(t)\le C'(1+|t|)^{K+2r}e^{-a|t|}.
\tag{5}
\]
For \(h\in\mathscr H_W\), the weighted Fourier transform
\[
F_h(z)=\int_{\mathbb R}h(t)W(t)e^{-izt}\,dt
\tag{6}
\]
is holomorphic in \(S_a=\{|\Im z|<a/2\}\) by Cauchy--Schwarz, with a polynomial upper bound in \((a-2|\Im z|)^{-1}\). It tends to zero at both ends of the real axis because \(hW\in L^1\). As in PC-435 §2, composition with \(z=(a/\pi)\operatorname{Log}Z\) in \(\Re Z>1\), removal of a sufficiently large polynomial factor in \(Z\), and the half-plane Blaschke zero-set theorem imply
\[
F_h(\log x)=c_0x^{\sigma-1}\ \ (x\in X),
\quad\sum_{x\in X}x^{-\alpha}=\infty
\ \Longrightarrow\ F_h\equiv0,\quad c_0=0.
\tag{7}
\]
The negative-real-axis Riemann--Lebesgue limit eliminates the possible exponential \(c_0e^{(\sigma-1)z}\). Fourier uniqueness and \(W>0\) a.e. give \(h=0\). Taking \(c_0=0\) proves density for \(q_x\); taking \(c_0=F_h(0)\) proves density for \(v_{x,\sigma}\).

Only the upper spectral envelope was needed. Polynomial amplitude growth changes its boundary *power*, not the analytic strip width \(a/2\) or the critical exponent \(\alpha\).

## 3. Convergent sampling: kill finite shifted Fourier jets

Now suppose \(\sum_{x\in X}x^{-\alpha}<\infty\). Form the real zero set
\[
Z=\{-b_j:1\le j\le J\}
   \cup\{\log x-b_j:x\in X,\ 1\le j\le J\},
\qquad m=1+\max_j\deg P_j.
\tag{8}
\]
Ignore repetitions in \(Z\); the prescribed multiplicity \(m\) will be supplied separately. Because each \(b_j\) is fixed and there are finitely many of them,
\[
\sum_{z\in Z,\ z\to+\infty}e^{-\alpha z}
\le \Bigl(\sum_{j=1}^Je^{\alpha b_j}\Bigr)
     \sum_{x\in X}x^{-\alpha}<\infty.
\tag{9}
\]
Thus \(Z\) is a Blaschke zero set in \(S_a\), using \(z\mapsto e^{\alpha z}\) to the right half-plane. There is a nonzero \(B\in H^\infty(S_a)\), \(|B|\le1\), with \(B(z)=0\) for all \(z\in Z\). The finite set \(\{-b_j\}\) causes no difficulty.

For every complex polynomial \(Q\) define
\[
G_Q(z)=e^{-z^2}B(z)^m Q(z),\qquad
g_Q(t)=\frac1{2\pi}\int_{\mathbb R}G_Q(s)e^{ist}\,ds.
\tag{10}
\]
Restrict \(Q\) to the infinite-dimensional kernel of the one linear functional
\[
Q\longmapsto\int_{\mathbb R}G_Q(s)\,ds.
\tag{11}
\]
The condition makes \(g_Q(0)=0\); since \(sG_Q(s)\in L^1(\mathbb R)\), it also makes \(g_Q(t)=O(t)\) near zero. Boundedness of \(B\) on the *entire* strip and Gaussian decay give
\(\sup_{|y|<a/2}\int_{\mathbb R}|G_Q(s+iy)|^2ds<\infty\).
Contour shifting, Plancherel and Fatou at the two strip edges therefore yield
\[
\int_{\mathbb R}|g_Q(t)|^2e^{a|t|}\,dt<\infty.
\tag{12}
\]
Combining (11)--(12) with the **unmasked** lower estimate (1) gives
\[
\int_{\mathbb R}\frac{|g_Q(t)|^2}{w(t)}\,dt<\infty.
\tag{13}
\]

Away from the discrete real zero set of \(D\), define
\(h_Q(t)=g_Q(t)/[w(t)\overline{D(t)}]\), and give it any value on that null set. The cancellation is exact:
\[
\|h_Q\|_{\mathscr H_W}^2
=\int_{\mathbb R}\frac{|g_Q(t)|^2}{w(t)}\,dt,\qquad
h_Q(t)W(t)=g_Q(t)D(t)\quad\text{a.e.}
\tag{14}
\]
In particular, **no division by a zero of \(D\)** enters the norm estimate.

With the Fourier convention in (6),
\(\widehat{t^kg_Q}(z)=i^k\partial_z^kG_Q(z)\) and
\(\widehat{e^{ib_jt}g_Q}(z)=G_Q(z-b_j)\).
Consequently the weighted Fourier transform of \(h_Q\) obeys the exact *finite differential-delay identity*
\[
F_{h_Q}(z)=
\sum_{j=1}^J
  P_j(i\partial_z)\,G_Q(z-b_j).
\tag{15}
\]
All differentiations and interchanges are justified: (12) makes \(t^kg_Q\in L^1\) for every fixed \(k\), and the sum is finite. Every \(G_Q\) has a zero of order **at least \(m\)** at each point of \(Z\). Since \(\deg P_j<m\), (8) and (15) imply
\[
F_{h_Q}(0)=F_{h_Q}(\log x)=0
\qquad(x\in X).
\tag{16}
\]
Thus \(h_Q\) is simultaneously orthogonal to every \(q_x\) and \(v_{x,\sigma}\). The map \(Q\mapsto G_Q\mapsto g_Q\mapsto h_Q\) is injective because \(B\not\equiv0\), Fourier inversion is injective, and \(D\ne0\) almost everywhere. The kernel of (11) has infinite dimension, proving the joint infinite-codimension assertion.

The difference from PC-436 is substantive at the proof level: **frequency shifts alone are insufficient once polynomial amplitudes appear**. Each \(t^k\) demands a Fourier derivative; the common Blaschke product must therefore vanish to the full finite jet order \(m\) at every shifted sample and at every shifted origin.

## 4. Prime-Circle controls, prior art, and exact boundary

For the zero-free matched PC-424/PC-435 seed \(g_{0,\sigma}\), its weight \(w_{0,\sigma}=(2/\pi)|t||g_{0,\sigma}|^2\) satisfies (1) with \(a=\pi\). The multiplier \(D\) does not vanish a.e., so multiplication by \(Dg_{0,\sigma}\) identifies \(L^2(w_{0,\sigma}|D|^2)\) unitarily with the Hilbert--Schmidt Fourier-kernel sector \(\mathcal A\) of PC-433. Hence, for every prime subset \(\mathcal P\),
\[
\boxed{\;
\overline{\operatorname{span}}
\{\mathcal J[(1-p^{1-\sigma}e^{it\log p})Dg_{0,\sigma}]
  :p\in\mathcal P\}
=\mathcal A
\iff \sum_{p\in\mathcal P}p^{-1}=\infty.\;}
\tag{17}
\]
The masked marked translates satisfy the same criterion; when the sum converges both systems have infinite codimension. A concrete unbounded, multiply vanishing mask is \(D(t)=t^2(1-e^{ibt})\), \(b\in\mathbb R\setminus\{0\}\), which lies outside the bounded-mask hypotheses of PC-436--PC-437.

**Prior art.** The half-plane/strip Blaschke theorem and bounded products are classical (Duren, *Theory of H^p Spaces*, 1970; Remmert, *Classical Topics in Complex Function Theory*, 1998). The full-strip \(H^2\) Fourier inversion is classical Paley--Wiener theory (Paley and Wiener, *Fourier Transforms in the Complex Domain*, 1934), and \(t^k\leftrightarrow i^k\partial_z^k\) is the elementary Fourier differentiation law. These references are already anchored in this line's SOURCES.md. This is an exact finite-jet extension of PC-436, **not a claimed new theorem in abstract harmonic analysis**.

**Controls and limitations.** The theorem covers finite sums of polynomial amplitudes times *real-frequency* exponentials; arbitrary smooth, infinite-frequency, or exponentially growing masks are not covered. An arbitrary nonzero polynomial mask is included, regardless of its zeros. A bounded periodic real-analytic mask belongs separately to PC-437, but does not generally have form (2). No mask here is claimed to be forced by the roots-of-unity geometry.

For the genuine \(\Gamma(\sigma-it)\zeta(\sigma-it)\) seed, polynomial growth of \(\zeta\) on fixed vertical lines continues to give the divergent-sampling **sufficient** condition after (2). The convergent-sampling converse is not proved, because the genuine zeta factor is not a finite differential-delay mask and its spectral weight lacks the two-sided lower estimate. The theorem provides no critical-line selector, zeta-zero exclusion, or implication toward RH.

**Decisive audit points.** Verify the finite real-frequency restriction in (5), the Blaschke sum after each of the finitely many shifts in (9), the exact jet order \(m\), the sign \(z-b_j\) and factor \(i^k\) in (15), the origin constraints in (8), and the **separate** condition (11) needed to cancel the cusp of \(w\) at \(t=0\). Do not replace the full-strip bound (12) by decay on smaller strips; the theorem includes the endpoint \(a\) exactly.