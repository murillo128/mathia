# PC-430 — additive prime Hilbert cyclic subspaces are nonclosed, nondense, and strongly collapse at large primes

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for combining the uniformly Riesz one-prime orbits of PC-429 by **adding their closed linear cyclic subspaces** in the hope of recovering PC-427's complete two-prime translation sector. At each fixed \(0<\sigma<1\), two distinct one-prime cyclic subspaces intersect only in the marked seed line; their algebraic sum is neither closed nor dense in the common ambient Hilbert--Schmidt sector, although allowing **mixed products of the two shifts** generates that entire sector. Any finite additive family remains nondense. As \(p\to\infty\), the projections onto individual prime cyclic subspaces converge **strongly** to the seed-line projection but stay at operator-norm distance exactly one.

These statements hold for the actual regularized Bose/Prime-Circle seed and the zero-free matched control of PC-424. They are Hilbert-space consequences of periodicity, incommensurability, absolute continuity and fine-period averaging, not a new zero-location constraint. In particular, strong projection convergence is not norm convergence, and finite-family nondensity is **not** a claim about the multiplicatively generated two-prime orbit.

## 1. Exact fiber setup from PC-427 and PC-429

Fix \(0<\sigma<1\) and choose one of the two Hilbert--Schmidt Fourier seeds \(g=g_\sigma\) (genuine) or \(g=g_{0,\sigma}\) (zero-free control) from PC-429. The ambient sector is
\[
\mathcal E=L^2(\mathbb R,d\mu),\qquad d\mu(t)=\frac2\pi|t|\,dt,
\quad (U_af)(t)=e^{iat}f(t).
\tag{1}
\]
In both cases \(g\in\mathcal E\), \(g\ne0\) almost everywhere, and
\[
w(t):=\frac2\pi|t|\,|g(t)|^2,\qquad
M:=\int_{\mathbb R}w(t)\,dt=\|g\|_{\mathcal E}^2>0
\tag{2}
\]
is continuous, integrable, strictly positive off a discrete set, and has exponentially decaying tails (up to polynomial factors). In particular, \(w(t)\,dt\) is a finite measure equivalent to Lebesgue measure. Let
\[
J_g:L^2(\mathbb R,w(t)dt)\longrightarrow\mathcal E,
\qquad J_gh=gh.
\tag{3}
\]
This is a unitary **onto** \(\mathcal E\): division by \(g\) is defined almost everywhere, and its weighted norm is exactly the original \(\mathcal E\)-norm.

For a prime \(p\), put \(a_p=\log p\), \(T_p=2\pi/a_p\), and let
\[
V_p:=\{h\in L^2(wdt):h(t+T_p)=h(t)\ \text{a.e.}\}.
\tag{4}
\]
The orbit-span/folded-density theorem of PC-429 (in fact its strictly positive periodization) identifies
\[
\boxed{\mathcal H_p:=
\overline{\operatorname{span}}\{U_{ma_p}g:m\in\mathbb Z\}
=J_gV_p.}
\tag{5}
\]
Here periodicity is understood as equality of Lebesgue-almost-everywhere representatives, not invariance of the *weight*. Each \(V_p\) is a closed infinite-dimensional subspace containing the constants. The seed line \(L=\mathbb Cg\subset\mathcal E\) corresponds to \(\mathbb C1\subset L^2(wdt)\).

For any \(k\ge1\), the source-native prime-power shell \(g_{p^k,\sigma}\) equals \(g\) times PC-429's boundedly invertible \(T_p\)-periodic multiplier \(q_{p^k,\sigma}\). Hence its one-prime cyclic subspace is the same \(\mathcal H_p\); no shell-specific new subspace is assumed here.

## 2. Pairwise intersections are the marked seed line

For distinct primes \(p\ne q\),
\[
\frac{T_p}{T_q}=\frac{\log q}{\log p}\notin\mathbb Q
\tag{6}
\]
by unique prime factorization. A measurable function with these two almost-everywhere periods is almost everywhere constant. One precise proof replaces an arbitrary finite-a.e. measurable common-periodic \(h\) by the bounded injective transform \(h/(1+|h|)\), applies translation continuity in \(L^1_{\mathrm{loc}}\) to the dense subgroup \(\mathbb ZT_p+\mathbb ZT_q\), and obtains invariance under all real translations; a locally integrable translation-invariant function is a.e. constant. Injectivity then gives the same conclusion for \(h\).

Since the periodic representatives from \(V_p\) and \(V_q\) coincide almost everywhere (because \(w>0\) almost everywhere), this applies to their intersection:
\[
\boxed{V_p\cap V_q=\mathbb C1,\qquad
\mathcal H_p\cap\mathcal H_q=\mathbb Cg.}
\tag{7}
\]
This is an exact intersection statement for every distinct prime pair, irrespective of \(\sigma\) and of which seed was used.

## 3. Additive sums are incomplete, including any finite number of primes

Write \((S_a\varphi)(t)=\varphi(t-a)\). For distinct primes \(p,q\), choose a nonzero smooth bump \(\varphi\) supported in a sufficiently small interval \(I\) such that \(w\) has a positive lower bound on
\[
I,\ I+T_p,\ I+T_q,\ I+T_p+T_q.
\tag{8}
\]
This is possible because the zero set of \(w\) is discrete, and the four shifts are fixed; \(I\) may also be chosen to make the four supports pairwise disjoint.

Define
\[
d=(I-S_{T_p})(I-S_{T_q})\varphi,
\qquad
h(t)=\frac{d(t)}{w(t)}
\quad\text{on the union of these compact supports,}
\tag{9}
\]
and put \(h=0\) elsewhere. Then \(h\in L^2(wdt)\) and \(h\ne0\). For any \(v\in V_p\), changing variables in the compactly supported integrals gives
\[
\langle h,v\rangle_{L^2(wdt)}
=\int_{\mathbb R}d(t)\overline{v(t)}\,dt
=0,
\tag{10}
\]
because \(I-S_{T_p}\) annihilates the pairing with a \(T_p\)-periodic function. The analogous \(I-S_{T_q}\) argument gives \(h\perp V_q\). Hence
\[
\boxed{\overline{\mathcal H_p+\mathcal H_q}
\ \subsetneq\ \mathcal E.}
\tag{11}
\]
Varying the compact interval produces infinitely many orthogonal nonzero witnesses, so the orthogonal complement of this closed sum is infinite-dimensional.

The same finite-difference construction works for *any finite* prime set \(F\): choose \(\varphi\) supported sufficiently narrowly and away from the finitely many zero-set translates and set
\[
d_F=\prod_{p\in F}(I-S_{T_p})\varphi,\qquad h_F=d_F/w.
\tag{12}
\]
The function \(d_F\) is nonzero: its Fourier transform is the nonzero entire product
\(\widehat\varphi(\xi)\prod_{p\in F}(1-e^{-iT_p\xi})\).
For every \(p\in F\), \(h_F\perp V_p\), yielding the strictly stronger finite-family statement
\[
\boxed{
\overline{\sum_{p\in F}\mathcal H_p}
\ \subsetneq\ \mathcal E
\quad\text{for every finite nonempty }F.
}
\tag{13}
\]
This argument does not assert that sums with three or more terms are nonclosed: pairwise nonclosedness alone would not justify that inference.

**Contrast with PC-427:** mixed *products* \(U_{m\log p+n\log q}\) range over a dense additive group of spectral frequencies and their orbit is dense in \(\mathcal E\). The *sum of two separately generated cyclic subspaces* uses only frequencies from the union \(\mathbb Z\log p\cup\mathbb Z\log q\), not the additive group containing all mixed frequencies. Algebraic sums and the cyclic space of the jointly generated representation are different mathematical objects.

## 4. Two-prime sums are not closed: arbitrarily small Friedrichs angle

The irrationality in (6) gives integers \(m_j,n_j\to+\infty\) such that
\[
\delta_j=m_j\log p-n_j\log q\longrightarrow0
\tag{14}
\]
by rational approximation. In \(L^2(wdt)\) define
\[
x_j(t)=e^{im_j(\log p)t}-c_j,\quad
y_j(t)=e^{in_j(\log q)t}-d_j,
\tag{15}
\]
where \(c_j=M^{-1}\int e^{im_j(\log p)t}w(t)dt\) and
\(d_j=M^{-1}\int e^{in_j(\log q)t}w(t)dt\).
Then \(x_j\in V_p\ominus\mathbb C1\) and \(y_j\in V_q\ominus\mathbb C1\).

Since \(w\in L^1(\mathbb R)\), the Riemann--Lebesgue lemma gives \(c_j,d_j\to0\). Dominated convergence applied to
\(\left|e^{i\delta_jt}-1\right|^2w(t)\) gives
\[
\boxed{
\|x_j-y_j\|_{L^2(wdt)}\to0,\qquad
\|x_j\|_{L^2(wdt)},\|y_j\|_{L^2(wdt)}\to\sqrt M>0.
}
\tag{16}
\]
After normalization, the principal correlation between the two reduced subspaces can be arbitrarily close to one. By the classical closed-sum/Friedrichs-angle criterion for closed Hilbert subspaces with intersection \(\mathbb C1\), this forces
\[
\boxed{\mathcal H_p+\mathcal H_q
\text{ is not closed}\qquad(p\ne q).}
\tag{17}
\]
Equivalently, if it were closed the addition map from
\((V_p\ominus\mathbb C1)\oplus(V_q\ominus\mathbb C1)\)
would be bounded below, contradicted by \((x_j,-y_j)\) in (16).

Thus the sum is both nonclosed and nondense: its closure is a **proper** closed subspace, not the whole sector. Strict finite Gram positivity (PC-426) and uniform one-prime Riesz bounds (PC-429) do not prevent this cross-generator almost-parallelism.

## 5. Asymptotic strong collapse of individual prime projectors

Let \(Q_p\) be orthogonal projection in \(L^2(wdt)\) onto \(V_p\), and \(Q_1\) projection onto \(\mathbb C1\). From (5), \(P_p=J_gQ_pJ_g^{-1}\) projects onto \(\mathcal H_p\) in \(\mathcal E\), and \(P_g=J_gQ_1J_g^{-1}\) projects onto the marked seed line.

For \(T=T_p\), PC-429 provides
\[
F_T(\theta)=\sum_{k\in\mathbb Z}w(\theta+kT)>0,
\quad
TF_T(\theta)\to M
\tag{18}
\]
uniformly on the shrinking cell \(|\theta|\le T/2\) as \(T\downarrow0\). The exact weighted-periodic orthogonal projection is the conditional-average formula
\[
\boxed{
(Q_pf)(t)=
\frac{\sum_{k\in\mathbb Z}w(t+kT_p)f(t+kT_p)}
     {\sum_{k\in\mathbb Z}w(t+kT_p)}.
}
\tag{19}
\]
Here the right-hand side is \(T_p\)-periodic; the sums exist almost everywhere for \(f\in L^2(wdt)\).

For continuous compactly supported \(f\), both numerator and denominator satisfy the uniform shifted Riemann-sum theorem as \(T_p\to0\). Therefore the ratio (19) converges uniformly to
\[
\frac1M\int_{\mathbb R}f(t)w(t)\,dt=(Q_1f)(t).
\tag{20}
\]
Because \(C_c(\mathbb R)\) is dense in \(L^2(wdt)\) and \(\|Q_p\|=\|Q_1\|=1\), the convergence extends to every vector:
\[
\boxed{P_p\xrightarrow[p\to\infty]{\mathrm{strong}}P_g.}
\tag{21}
\]

But \(\mathbb Cg\subsetneq\mathcal H_p\) for **every** prime, and the projections are nested in that order. Hence \(P_p-P_g\) is the orthogonal projection onto \(\mathcal H_p\ominus\mathbb Cg\), which is nonzero. Thus
\[
\boxed{\|P_p-P_g\|_{\mathcal B(\mathcal E)}=1
\quad\text{for every prime }p.}
\tag{22}
\]
An operator-norm limit would contradict (22). The strong limit does not make the infinite-dimensional subspaces eventually one-dimensional.

## 6. Source specificity, prior art, and decisive boundaries

The weighted sector, exact seed and matched control are from PC-424 and PC-427; the one-prime Riesz/folded-density identification and uniform fine-period sums are from PC-429. The sum-closedness criterion is classical Hilbert-space geometry: I. E. Schochetman, R. L. Smith and S.-K. Tsui, *On the closure of the sum of closed subspaces*, *International Journal of Mathematics and Mathematical Sciences* **26** (2001), 257--267, DOI 10.1155/S0161171201005324. The irrational-period constancy, finite-difference annihilator, Riemann--Lebesgue lemma and weighted conditional expectation are elementary classical ingredients proved or directly specialized above. No novelty is claimed for their abstract versions.

**Line-local delta.** PC-427 says two prime shifts *jointly* generate the universal full cyclic sector. PC-429 says each *individually* provides a stable Riesz basis for its own cyclic subspace. The missing operation was whether **additive fusion** of finitely many of those stable subspaces recovers the joint orbit. Equations (7), (11)--(13) and (17) answer no: the pairwise overlap is exactly the seed, yet finite additive fusion remains incomplete and is already unstable for a pair. Equations (21)--(22) additionally identify the precise strong-versus-norm topology of the individual projector limit.

All assertions depend only on the positive a.e. integrable seed spectral weight (with enough regularity for the fine-period limit), not on off-critical zeta zeros, and remain true on the explicit zero-free control. The obstruction also holds for rapidly decaying nonarithmetic weights such as \(w(t)=e^{-t^2}\) with no zeros; primality only supplies independent irrational period pairs and an unbounded sequence of increasingly small periods. It does **not** rule out operators using mixed products/cross terms intrinsically coupled before scalar Mellinization, a source-dependent marked measure, or a genuinely non-diagonal infinite-dimensional construction. No conclusion here implies RH.

Audit the distinction between a normalized one-generator orbit and the full two-generator action; verify that the *weight* is used in the conditional expectation (19), whereas periodicity refers to Lebesgue-a.e. representatives; test the common-period result for measurable rather than assumed continuous functions; check the compactly supported witnesses (8)--(12) avoid zeros of \(w\); require \(m_j,n_j\to\infty\) for Riemann--Lebesgue in (16); and do not upgrade the strong limit (21) to norm convergence in (22).
