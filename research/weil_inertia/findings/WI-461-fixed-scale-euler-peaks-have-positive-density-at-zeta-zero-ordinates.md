# WI-461 — Fixed-scale Euler peaks have positive density at zeta-zero ordinates

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-EQUIDISTRIBUTION + SOURCE-FAMILY-BOUNDARY + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** [WI-457](WI-457-normalized-euler-hankel-symbols-have-local-blindness-and-recurrent-peaks.md), for the response, its global maximum and pole limit; [WI-458](WI-458-euler-hankel-peaks-have-exponentially-small-height-density.md), for the tail-uniform prime phase box; [WI-459](WI-459-safe-line-optimization-preserves-double-exponential-euler-peak-rarity.md), for the optimized maximum; [WI-460](WI-460-adaptive-euler-peaks-remain-rare-at-zeta-zero-ordinates.md), for the upper bound after simultaneous safe-line and width selection.

## Claim: rarity does not imply avoidance by the divisor

Use the normalized Euler symbols and Hardy kernels
\[
L(s)=-\zeta'(s)/\zeta(s),\quad A_\varepsilon=L(1+\varepsilon),\quad
\varphi_\varepsilon(t)=L(1+\varepsilon+it)/A_\varepsilon,
\]
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},\qquad
Q_\varepsilon(r,\gamma)=\|P_-(\varphi_\varepsilon k_{r,\gamma})\|_2^2,
\quad \varepsilon,r>0.
\tag{1}
\]
The Fourier phase is \(e^{-it\xi}\). Let \(\Gamma\) be the positive ordinates of **all** nontrivial zeta zeros, and let \(N(T)\) count those with ordinate at most \(T\). Count each zero with its multiplicity in \(N\) and every sum. Different real parts at the same ordinate contribute separately. Define
\[
D_T=N(2T)-N(T),\qquad
M_r(t)=\sup_{\varepsilon>0}Q_\varepsilon(r,t),\qquad
\mathcal M_R(t)=\sup_{0<r\le R}M_r(t).
\]

For each fixed \(0<\tau<1/4\), there are \(0<c_\tau<C_\tau\) and \(R_\tau>0\) such that, for every **fixed** \(0<R<R_\tau\),
\[
\boxed{
\begin{aligned}
\exp[-\exp(C_\tau/R)]
&\le \liminf_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{Q_R(R,\gamma)>\tau\}}\\
&\le \liminf_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{\mathcal M_R(\gamma)\ge\tau\}}\\
&\le \limsup_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{\mathcal M_R(\gamma)\ge\tau\}}
\le \exp[-\exp(c_\tau/R)].
\end{aligned}}
\tag{2}
\]
Thus at any fixed sufficiently small scale, peaks occur at a positive, very small asymptotic lower fraction of actual zero ordinates. Safe-line or width adaptation is unnecessary for the lower bound.

There is also an exact range statement: for every fixed \(\varepsilon,r>0\) and every finite \(B\ge0\),
\[
\boxed{\sup_{\gamma\in\Gamma,\ \gamma>B}Q_\varepsilon(r,\gamma)
=Q_\varepsilon(r,0).}
\tag{3}
\]
Consequently
\[
\sup_{\gamma\in\Gamma,\ \gamma>B}M_r(\gamma)=M_r(0),
\qquad
\lim_{r\downarrow0}\sup_{\gamma\in\Gamma,\ \gamma>B(r)}M_r(\gamma)=\frac14
\tag{4}
\]
for any finite nonnegative cutoff \(B(r)\). These are suprema, not assertions that a maximum is attained at a zero.

Neither (2) nor (3) restricts the real parts of the responsive zeros. They do not show that any off-line zero exists or responds, nor that any responsive zero is simple. They are fully compatible with RH. The lower bound in (2) does **not** apply with an arbitrary shrinking \(R=R(T)\); its order of limits is essential.

## Classical arithmetic input and the finite-prime sampling law

The input is the unconditional equidistribution of \(\alpha\gamma\) modulo one for every fixed real \(\alpha\ne0\), with all zeros counted with multiplicity. In character form,
\[
\frac1{N(T)}\sum_{0<\gamma\le T}e^{i\omega\gamma}\longrightarrow0
\quad\text{for every fixed }\omega\ne0.
\tag{5}
\]
This is the classical Elliott--Hlawka conclusion discussed in Ford--Zaharescu, §1, and stated in Ford--Soundararajan--Zaharescu, equation (1.1). The unconditional assertion must not be confused with the sharper RH-conditional discrepancy bounds or conjectured lower-order formulas in those papers.

For a fixed finite set of primes \(P\), put
\[
z_P(t)=(e^{-it\log p})_{p\in P}\in\mathbb T^P,
\qquad \mathbb T=\{z\in\mathbb C:|z|=1\}.
\]
If \((j_p)_{p\in P}\) is a nonzero integer vector, unique prime factorization gives
\(\sum_{p\in P}j_p\log p\ne0\). Applying (5) to this frequency shows that every nontrivial character of \(z_P(\gamma)\) has limiting mean zero. Finite Fourier approximation therefore proves convergence to product Haar measure for all continuous functions on \(\mathbb T^P\), and for finite phase boxes whose boundaries have Haar measure zero.

The same conclusion holds on \((T,2T]\): subtract the two cumulative sums and use \(N(2T)/D_T\to2\), \(N(T)/D_T\to1\). In particular, for fixed \(0<\eta<\pi\),
\[
\frac1{D_T}\sum_{T<\gamma\le2T}
\mathbf1_{\{|\arg z_p(\gamma)|<\eta\ \forall p\in P\}}
\longrightarrow (\eta/\pi)^{|P|}.
\tag{6}
\]
This is joint equidistribution deduced using every mixed character. Separate equidistribution of the individual prime phases alone would not establish (6). Powers of the same prime remain powers of one coordinate, never independent coordinates.

## The fixed-parameter response has its prime-torus law at zeros

For \(\omega>0\) define \(h_\omega=P_-(e^{-i\omega t}k_{r,0})\), so \(\|h_\omega\|_2\le1\). On the infinite product prime torus, with product Haar probability \(m\), set
\[
V_{\varepsilon,r}(z)=A_\varepsilon^{-1}
\sum_p\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}z_p^k h_{k\log p},
\qquad \mathscr Q_{\varepsilon,r}(z)=\|V_{\varepsilon,r}(z)\|_2^2.
\tag{7}
\]
The sum of coefficient norms is at most one. Hence finite truncations converge uniformly in every phase choice, and \(\mathscr Q_{\varepsilon,r}\) is continuous with values in \([0,1]\). Translation of (1) gives
\(Q_\varepsilon(r,t)=\mathscr Q_{\varepsilon,r}(z(t))\).

For every continuous \(F:[0,1]\to\mathbb R\), finite truncation, (6)'s continuous-function version, and uniform continuity of \(F\) prove
\[
\boxed{\lim_{T\to\infty}\frac1{D_T}
\sum_{T<\gamma\le2T}F(Q_\varepsilon(r,\gamma))
=\int F(\mathscr Q_{\varepsilon,r}(z))\,dm(z).}
\tag{8}
\]
The truncation is fixed before taking \(T\to\infty\), then removed. The same torus law governs continuous-height averages, by finite-prime Kronecker equidistribution and the identical uniform truncation. Thus (8) is a leading-order sampling law for this fixed observable, not a postulate of random prime phases at selected zeros.

Weak convergence alone does not give equality for every threshold indicator: a level set might have positive Haar measure. The lower bound below uses a finite box with null boundary and pointwise inclusion, avoiding that issue entirely.

## A phase box forces responsive zeros

Fix \(\tau\in(0,1/4)\), put \(\Delta=1/2-\sqrt\tau>0\), and take \(\varepsilon=r=R\). The pole limit in WI-457 gives
\[
\|V_{R,R}(1)\|_2\ge\sqrt\tau+3\Delta/4
\tag{9}
\]
for sufficiently small \(R\). Retain primes \(p\le y=\exp(K/R)\), with \(K\) a large fixed constant depending on \(\tau\). The normalized coefficient tail satisfies
\[
A_R^{-1}\sum_{p>y,k\ge1}\frac{\log p}{p^{k(1+R)}}
\le y^{-R/2}\frac{A_{R/2}}{A_R}\le3e^{-K/2}.
\tag{10}
\]
Here \(p^k>y\), and \(A_{R/2}/A_R\to2\). Also
\[
\sum_{p,k\ge1}\frac{k\log p}{p^{k(1+R)}}
\le A_R+D,\qquad
D=\sum_p\frac{\log p}{(p-1)^2}<\infty.
\tag{11}
\]
If \(|\arg z_p|<\eta\) for all \(p\le y\), then \(|z_p^k-1|\le k\eta\). Equations (10)--(11) and \(\|h_\omega\|_2\le1\) give, for small \(R\),
\[
\|V_{R,R}(z)-V_{R,R}(1)\|_2\le2\eta+6e^{-K/2}.
\tag{12}
\]
Choose \(\eta>0\) small and \(K\) large so this is at most \(\Delta/2\). The finite phase box lies in \(\mathscr Q_{R,R}>\tau\) for **every** choice of tail phases. This reconstructs the WI-458 box without assuming that the tail is typical.

At each fixed \(R\), equation (6) now gives a zero-sampled lower proportion at least
\[
(\eta/\pi)^{\pi(y)}
\ge\exp[-\log(\pi/\eta)e^{K/R}]
\ge\exp[-\exp(C_\tau/R)]
\tag{13}
\]
for a larger \(C_\tau\). Only \(\pi(y)\le y\) is used. The upper bound in (2) is WI-460's simultaneous-selection upper bound at the same fixed threshold; taking \(C_\tau>c_\tau\) is harmless.

For (3), use arbitrary fixed \(\varepsilon,r>0\). Uniform convergence in (7) lets a sufficiently large finite phase box make \(V_{\varepsilon,r}(z)\) arbitrarily close to \(V_{\varepsilon,r}(1)\), regardless of the tail. Equation (6) puts a positive limiting fraction of zeros in each such box, hence infinitely many beyond any finite \(B\). This gives the lower bound for the supremum in (3). The reverse bound is WI-457's pointwise inequality \(Q_\varepsilon(r,t)\le Q_\varepsilon(r,0)\). Interchanging two suprema proves the first equality in (4); WI-459's \(M_r(0)\to1/4\) proves its limit, including a finite cutoff depending on \(r\).

## Consequence and limits of the conclusion

WI-460 proves upper rarity and explicitly leaves peak occurrence at zeros undecided. Classical fixed-frequency equidistribution supplies that missing qualitative arithmetic input: actual zero ordinates sample the full fixed-parameter response range and meet every robust near-maximum phase box. Their positive lower fraction has the same broad double-exponential scale as the established upper bound.

This resolves **fixed-scale overlap with the full divisor**, not the alignment question for a hypothetical exceptional subpopulation. The relevant distinctions are:

- All zeros and multiplicities enter (5)--(8). Restricting to off-line zeros, simple zeros, or any other selected subpopulation requires a new sampling theorem. In particular, the result supplies no lower bound for the response at every off-line zero.
- At scale \(R\), the number of constrained primes is finite but can be as large as \(\exp(K/R)\). Nothing here bounds the convergence height uniformly as \(R\downarrow0\). The positive fixed-\(R\) lower density is compatible with WI-460's vanishing fraction for **every** \(R(T)\to0\).
- A slowly chosen diagonal can retain some responsive zeros at widths tending to zero, by (3)--(4). This is existence with freely chosen heights and widths; it identifies neither a zero's horizontal depth nor the physical relation \(r=(1-\vartheta)d\) for a Kunik defect.
- The leading Haar law loses lower-order arithmetic biases. Ford--Zaharescu's nonzero prime-resonant correction occurs at order \(T\), whereas the normalization here is \(T\log T\). It is not contradicted or eliminated by (8).
- No maximum attainment, atom-free response law, sharp rare-peak constant, finite-height lower estimate, or uniform distribution for growing frequency sets is asserted.

The analytical audit points are the unconditional quantifier in (5), nonzero mixed prime frequencies, dyadic normalization, uniform Hilbert-valued truncation, the tail-uniform box inclusion, and the fixed-scale order of limits. No numerical evidence, Lean proof, new critical-line or simplicity proportion, or RH conclusion is claimed. The general sampling argument is classical and does not present a separate formalization-fertility question.

## Prior art and novelty assessment

Kevin Ford and Alexandru Zaharescu, *On the distribution of imaginary parts of zeros of the Riemann zeta function*, **Journal für die reine und angewandte Mathematik 579** (2005), 145--158, [arXiv:math/0405459](https://arxiv.org/abs/math/0405459), §1 and equation (3.8), describe unconditional fixed-frequency equidistribution and its zero-density/Landau bridge; §1 specifies multiplicity counting. Their investigation of lower-order prime-resonant bias is stronger information than the leading Haar law used here.

Kevin Ford, K. Soundararajan and Alexandru Zaharescu, *On the distribution of imaginary parts of zeros of the Riemann zeta function, II*, **Mathematische Annalen 343** (2009), 487--505, [DOI 10.1007/s00208-008-0280-x](https://doi.org/10.1007/s00208-008-0280-x), [arXiv:0805.2745](https://arxiv.org/abs/0805.2745), equation (1.1), explicitly states the fixed-frequency continuous-test law. Its later conjectures and RH-conditional refinements are not inputs here. The original Hlawka reference is *Über die Gleichverteilung gewisser Folgen, welche mit den Nullstellen der Zetafunktionen zusammenhängen*, **Sitzungsberichte der Österreichischen Akademie der Wissenschaften, Math.-Naturw. Klasse, Abteilung II 184** (1975), 459--471; the theorem was checked here through the two primary research papers above.

Finite-dimensional character testing, passage to uniformly convergent almost-periodic observables, and positive measure of a phase box are standard. The local delta is the proved sampling transfer for the normalized Euler--Hankel family and the resulting positive rare-peak fraction and exact sampled supremum. This is a classical-theorem specialization resolving a previously unfilled implication, with no claim of literature priority or a new equidistribution theorem.
