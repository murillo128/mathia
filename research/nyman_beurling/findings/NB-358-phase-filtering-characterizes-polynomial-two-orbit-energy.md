# NB-358 — Phase filtering characterizes polynomial two-orbit energy

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the orbit factors and target projection; NB-355 for the logarithmic lower bound; NB-356 for the bounded lattice lift; NB-357 for the preceding index-cutoff bound
- **Classification:** LITERATURE+DERIVED + EXACT-RATE-THRESHOLD + CONSTRUCTIVE-UPPER-BOUND

## Claim and scope

Filtering samples by their phase denominator, instead of their index, closes the polynomial-exponent gap in the two-orbit approximation problem. For every positive exponent, a polynomial bound on the **squared physical component norms** is equivalent to a uniform Diophantine bound on the seed log ratio. This prices approximation to the projected Nyman target; it does not remove the Burnol floor or price discrete generator resolution.

In \(H=L^2(0,1;dx)\), set
\[
e=1,\quad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\qquad
\mathcal C_j=\overline{\operatorname{span}}\{A_ag_j:a\ge1\text{ real}\}.
\]
Fix real seeds \(p,q>1\) with irrational \(\alpha=\log p/\log q\). Let \(\mathcal N\) be the full continuous Nyman space, \(t=P_{\mathcal N}e\), and \(b=B(1)>0\) its normalized Burnol factor. Define
\[
\mathcal E(\varepsilon)=\inf\{\|u\|^2+\|v\|^2:
 u\in\mathcal C_q,\ v\in\mathcal C_p,\ \|t-u-v\|\le\varepsilon\},
\qquad \delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z}.
\tag{1}
\]
For each fixed \(\kappa>0\),
\[
\boxed{\mathcal E(\varepsilon)=O(\varepsilon^{-\kappa})
\quad(\varepsilon\downarrow0)
\quad\Longleftrightarrow\quad
\inf_{n\ge1}n^{1+\kappa/2}\delta_n>0.}
\tag{2}
\]
The constants may depend on the seeds, \(b\), the exponent, and the positive infimum. Equivalently, if \(\delta_n\ge\gamma n^{-\nu}\) for every \(n\ge1\), with \(\gamma>0\) and \(\nu>1\), then
\[
\boxed{\mathcal E(\varepsilon)\ll_{p,q,b,\gamma,\nu}
\varepsilon^{-2(\nu-1)}.}
\tag{3}
\]
This improves NB-357's \(\varepsilon^{-4(\nu-1)}\) upper bound using exactly the same Diophantine hypothesis. At \(\nu=1\) the construction gives the already sharp order
\(\mathcal E(\varepsilon)\asymp\log(1/\varepsilon)\); (2) is **not** asserted with \(\kappa=0\).

If \(\mu(\alpha)\in[2,\infty]\) denotes the irrationality exponent, then a consequence is
\[
\boxed{\limsup_{\varepsilon\downarrow0}
\frac{\log(1+\mathcal E(\varepsilon))}{\log(1/\varepsilon)}
=2\bigl(\mu(\alpha)-2\bigr).}
\tag{4}
\]
This is a limsup exponent, not a two-sided power asymptotic or an assertion that the bound at the endpoint exponent is attained.

## 1. Retain the physical norm through the lattice lift

Under the unitary Mellin map to \(H^2(\Re s>1/2)\), NB-354--NB-356 give
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}},\qquad
\mathcal Mt=Bf,\quad f(s)=b/s.
\tag{5}
\]
These formulas hold for real \(j>1\). Each \(\Theta_j\) is precisely the simple-zero Blaschke product at \(1+2\pi i\ell/\log j\), \(\ell\ne0\). The singularity at \(s=1\) is removable and nonzero. Inner multiplication preserves the Hardy norm, whose square is \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\).

Put \(L=\log q\), \(\tau=2\pi/L\), \(s_\ell=1+i\tau\ell\). For data \(d\in\ell^2(\mathbb Z)\), define
\[
P_d(x)=\frac1L\sum_{\ell\in\mathbb Z}d_\ell e^{i\tau\ell x},\qquad
(R_qd)(s)=\int_0^L P_d(x)e^{-(s-1)x}\,dx.
\tag{6}
\]
The Fourier series is an \(L^2(0,L)\) series. The Laplace density is \(e^{x/2}P_d(x)\mathbf1_{[0,L)}\), so Parseval proves
\[
(R_qd)(s_\ell)=d_\ell,\qquad
\|R_qd\|^2=\int_0^L e^x|P_d(x)|^2dx
\le\frac qL\sum_\ell|d_\ell|^2.
\tag{7}
\]
This is a full-norm lift, not an inference from finitely many small samples.

For \(\ell\ne0\), the explicit factors imply
\[
|f(s_\ell)|\asymp_{q,b}|\ell|^{-1},\qquad
|\Theta_p(s_\ell)|\asymp_{p,q}\delta_{|\ell|}.
\tag{8}
\]
Indeed the phase numerator \(|1-e^{-2\pi i\ell\alpha}|\) lies between \(4\delta_{|\ell|}\) and \(2\pi\delta_{|\ell|}\), while \(|1-p^{-1}e^{-2\pi i\ell\alpha}|\) lies between \(1-p^{-1}\) and \(1+p^{-1}\). The remaining factor is \(|s_\ell|/(\tau|\ell|\sqrt p)\), uniformly bounded above and below. All these constants are fixed before the cutoff moves.

## 2. Sparse returns control discarded target mass

Assume \(\delta_n\ge\gamma n^{-\nu}\), \(\nu\ge1\). For \(0<x\le1/2\), define the weighted return mass
\[
F_\alpha(x)=\sum_{\substack{n\ge1\\\delta_n\le x}}\frac1{n^2}.
\tag{9}
\]
List the positive return indices as \(n_1<n_2<\cdots\). The first index satisfies \(n_1\ge(\gamma/x)^{1/\nu}\). For any distinct return indices, the circle triangle inequality and the same Diophantine hypothesis give
\[
\gamma|n_j-n_i|^{-\nu}
\le\|(n_j-n_i)\alpha\|\le2x.
\tag{10}
\]
Thus every successive gap is at least \(Q_x=(\gamma/(2x))^{1/\nu}\), and \(n_j\ge jQ_x\). The argument also applies to a finite list. Consequently
\[
\boxed{F_\alpha(x)\le\frac{\pi^2}{6}
\left(\frac{2x}{\gamma}\right)^{2/\nu}.}
\tag{11}
\]
No equidistribution rate or independence of returns is used. Merely using the first-return bound and then summing over every later integer would lose a power; the gap bound in (10) is load-bearing.

The energy of the retained samples is
\[
G_\alpha(h)=\sum_{\substack{n\ge1\\\delta_n\ge h}}
\frac1{n^2\delta_n^2},\qquad 0<h<1/2.
\tag{12}
\]
The identity \(\delta^{-2}=4+\int_\delta^{1/2}2x^{-3}\,dx\), for \(0<\delta\le1/2\), and Tonelli give
\[
G_\alpha(h)\le4\sum_{n\ge1}n^{-2}
+2\int_h^{1/2}F_\alpha(x)x^{-3}\,dx.
\tag{13}
\]
Applying (11) yields
\[
\boxed{G_\alpha(h)\ll_{\gamma,\nu}
\begin{cases}
1+\log(1/h),&\nu=1,\\
h^{-2+2/\nu},&\nu>1.
\end{cases}}
\tag{14}
\]
The constant for \(\nu>1\) is not uniform as \(\nu\downarrow1\). The elementary bound \(G_\alpha(h)\le h^{-2}\sum n^{-2}\) also shows that the retained infinite data are square summable before using any Diophantine estimate.

## 3. Phase-filtered physical approximants

For \(0<h<1/2\), use the symmetric lattice data
\[
d_\ell=
\begin{cases}f(s_\ell)/\Theta_p(s_\ell),&\ell\ne0,\ \delta_{|\ell|}\ge h,\\0,&\text{otherwise},\end{cases}
\qquad
a_\ell=
\begin{cases}f(s_\ell),&\ell\ne0,\ \delta_{|\ell|}<h,\\0,&\text{otherwise}.
\end{cases}
\tag{15}
\]
Both belong to \(\ell^2\), by (8), (12), and \(\sum n^{-2}<\infty\). Define
\[
V_h=R_qd,\qquad r_h=R_qa,\qquad
U_h=\frac{f-r_h-\Theta_pV_h}{\Theta_q}.
\tag{16}
\]
At every nonzero lattice index either \(d_\ell\) supplies the target sample or \(a_\ell\) does. Hence the numerator in (16) vanishes at **all** zeros of \(\Theta_q\). Division by its pure Blaschke factor gives \(U_h\in H^2\) and preserves the norm of that numerator. No condition at \(s_0=1\) is required.

Return to physical vectors \(u_h=\mathcal M^{-1}(B\Theta_qU_h)\), \(v_h=\mathcal M^{-1}(B\Theta_pV_h)\). Equations (7)--(15) prove, for constants independent of \(h\),
\[
\|t-u_h-v_h\|^2=\|r_h\|^2\le C F_\alpha(h)
\le C_{p,q,b,\gamma,\nu}h^{2/\nu},\qquad
\|v_h\|^2\le C G_\alpha(h).
\tag{17}
\]
The first component is priced as well:
\[
\|u_h\|\le b+\|r_h\|+\|v_h\|,\qquad
\|u_h\|^2+\|v_h\|^2
\le2(b+\|r_h\|)^2+3\|v_h\|^2.
\tag{18}
\]
Choose \(h=c\varepsilon^\nu\), with a sufficiently small fixed \(c>0\). Then (17) gives the prescribed error, while (14) and (18) give (3). For \(\nu=1\), they give \(O(\log(1/\varepsilon))\), matching NB-355's universal logarithmic lower bound. This proves the sufficient direction of (2).

Even without finite type, \(F_\alpha(h)\to0\) by dominated convergence since every \(\delta_n>0\). Thus (15)--(18) give finite-energy approximants at every positive accuracy for every irrational ratio. They need not have any polynomial energy bound.

## 4. One sample supplies the converse and the limsup exponent

Let \(S=\sqrt{1+\tau^2}\), and fix \(K>0\) so that \(|\Theta_p(s_n)|\le K\delta_n\) for all \(n\ge1\). Evaluation at \(s_n\) has norm one in this Hardy normalization: its Laplace kernel has squared norm \(\int_0^\infty e^{-x}dx=1\).

For any admissible pair in (1), write its residual after removing \(B\) as
\(r=f-\Theta_qU-\Theta_pV\). At \(s_n\), \(\Theta_q(s_n)=0\). Set \(\varepsilon_n=b/(2Sn)\). When \(\|r\|\le\varepsilon_n\),
\[
|\Theta_p(s_n)V(s_n)|\ge |f(s_n)|-|r(s_n)|
\ge\frac b{2Sn},\qquad
\|v\|=\|V\|\ge\frac b{2SKn\delta_n}.
\]
Taking the infimum over pairs gives
\[
\boxed{\mathcal E(\varepsilon_n)\ge
\frac{b^2}{4S^2K^2}\frac1{n^2\delta_n^2}.}
\tag{19}
\]
No minimizer is assumed. If \(\mathcal E(\varepsilon)\le C\varepsilon^{-\kappa}\) for all sufficiently small \(\varepsilon\), (19) implies \(\delta_n\ge c n^{-1-\kappa/2}\) for all sufficiently large \(n\). Finitely many initial positive denominators can be absorbed into \(c>0\). This proves necessity in (2).

For completeness, write
\[
\omega(\alpha)=\limsup_{n\to\infty}\frac{-\log\delta_n}{\log n}
=\mu(\alpha)-1\ge1.
\tag{20}
\]
The equality follows directly from \(|\alpha-m/n|=\delta_n/n\) for the nearest integer \(m\); the usual irrationality exponent is the supremum of rational-approximation powers occurring infinitely often. If \(\omega<\infty\), every \(\nu>\omega\) admits a positive uniform constant \(\gamma\), so (3) bounds the left side of (4) by \(2(\omega-1)\) after \(\nu\downarrow\omega\). If \(\omega>1\), every \(1<\eta<\omega\) has infinitely many \(n\) with \(\delta_n<n^{-\eta}\); (19) gives the opposite limsup inequality \(2(\eta-1)\). Let \(\eta\uparrow\omega\), allowing \(\omega=\infty\). When \(\omega=1\), nonnegativity of the logarithmic ratio supplies the lower bound zero. This proves (4), including both endpoints.

## Consequences, prior art, and evidence boundary

For a squared component budget \(R^2\), (3) constructs projection error \(O(R^{-1/(\nu-1)})\), improving NB-357's exponent by a factor two. Every fixed multiplicatively independent integer seed pair has some effective finite \(\nu>1\): the positive-rational Matveev bound in Languasco, Luca, Moree and Togbé, [Theorem 2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9), applies to \(p^nq^{-m}-1\), with \(m\) nearest to \(n\alpha\). It yields \(|n\log p-m\log q|\gg n^{-\nu}\), as detailed in NB-357. No optimal exponent or bounded-type property for any specified integer log ratio is established here.

Real seeds expose the boundary without assumptions about logarithms of integers: a ratio with \(\mu(\alpha)=2\) has subpolynomial component energy but still the divergent logarithmic lower bound; a Liouville ratio admits no uniform polynomial energy bound. Neither statement asserts a uniform rate over different seed pairs.

The classical anchors are Burnol's [Section 2, Lemma 2.4](https://arxiv.org/pdf/math/9910055) for (5), and bounded Hardy lattice interpolation, explicitly reconstructed in (6)--(7). Borda, *On the theorem of Davenport and generalized Dedekind sums*, [Section 4, Theorem 3](https://arxiv.org/pdf/1606.07946), treats the squared reciprocal sums underlying NB-355--NB-357 through continued fractions. Reciprocal-phase sums and Diophantine small denominators are established mathematics; (10)--(14) use elementary spacing and integration, not a new number-theoretic input.

There is also established inverse-problem prior art for norm-budget distance functions and power rates: Hofmann, Schieck and von Wolfersdorf, *On the analysis of distance functions for linear ill-posed problems with an application to the integration operator in L2*, J. Inverse Ill-Posed Probl. 15 (2007), 83--98, [author manuscript, Sections 1--4](https://www.tu-chemnitz.de/mathematik/inverse_probleme/fulltext/hsw.pdf). It supplies context for filtering small denominators and balancing error against source norm; no theorem from that paper is needed for (11)--(19).

The mathematical delta is the source-specific phase filter with a bounded full-norm residual lift, the sharpened exponent (3), and the necessary-and-sufficient polynomial threshold (2). The index truncation of NB-357 omitted the entire high-index target tail; the present filter retains all well-separated samples, regardless of index. No novelty is claimed for spectral filtering, Hardy factorization, or Diophantine approximation in general, and search absence is not evidence of novelty.

- Every physical pair still satisfies
  \(\|e-u-v\|^2=1-b^2+\|t-u-v\|^2\).
  The target floor is untouched. The construction involves \(B\) and \(b\) and is not an algorithm for computing that projection without zero information.
- Only squared norms of the two resulting orbit vectors are priced. Infinite real-dilation orbits are allowed; no bound on finite generator count, dilation range, absolute coefficients, or discrete-section error follows.
- Both signs of the lattice are retained and the zero index is excluded correctly. Division in (16) is by an actual inner divisor, not by an assumed bounded reciprocal.
- The return-gap estimate uses the Diophantine bound for **all differences** as well as for the first return. Irrationality alone does not supply (11) with a fixed power.
- A limsup exponent does not control fluctuations or endpoint constants. In particular, \(\mu=2\) does not imply bounded partial quotients or an \(O(\log(1/\varepsilon))\) upper bound.

Evidence is the analytic derivation and the inspected classical sources. The decisive audit points are the index-gap argument (10), the layer integral (13), square summability of both infinite data sets, all-zero cancellation in (16), and the squared-energy normalization in (19). No numerical optimum, Lean verification, independent adversarial approval, discrete Nyman rate, or proof of RH is asserted.
