# WI-457 — normalized Euler Hankel symbols have local blindness and recurrent peaks

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + SOURCE-FAMILY-OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** WI-438 (the shallow-packet/Poisson-variance test), WI-454 (a coherent frequency decomposition preserves energy but supplies no independent source estimate).

## A source-derived test of the scale-dependent escape

WI-438 leaves open bounded symbol families that develop oscillation at the unknown defect scale. A natural arithmetic family is already available without continuation into the critical strip. Put
\[
L(s)=-\frac{\zeta'(s)}{\zeta(s)},\qquad
A_\varepsilon=L(1+\varepsilon),\qquad
\varphi_\varepsilon(t)=\frac{L(1+\varepsilon+it)}{A_\varepsilon},
\quad \varepsilon>0.
\tag{1}
\]
The absolutely convergent Euler series gives
\[
\varphi_\varepsilon(t)=\sum_{n\ge2}a_{\varepsilon,n}e^{-it\log n},
\qquad a_{\varepsilon,n}=\frac{\Lambda(n)n^{-1-\varepsilon}}{A_\varepsilon}\ge0,
\qquad \sum_n a_{\varepsilon,n}=1.
\tag{2}
\]
Thus every symbol has supremum norm one and every associated Hankel operator
\(H_\varepsilon=P_-M_{\varphi_\varepsilon}|_{\mathcal H_+}\) has norm at most one. The parameter \(\varepsilon\) is freely tunable from the source side.

Use the unitary Fourier transform with phase \(e^{-it\xi}\), its positive/negative half-spaces \(\mathcal H_\pm\), and the unit positive-Hardy kernel
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},\qquad
|k_{r,\gamma}(t)|^2=P_r(t-\gamma)
=\frac1\pi\frac r{r^2+(t-\gamma)^2}.
\]
Write \(Q_\varepsilon(r,\gamma)=\|H_\varepsilon k_{r,\gamma}\|_2^2\). The following three assertions hold together.

1. **Optimizing the safe-line parameter still gives local shallow blindness.** For every compact \(K\subset\mathbb R\setminus\{0\}\),
   \[
   \boxed{\lim_{r\downarrow0}\ \sup_{\varepsilon>0,\ \gamma\in K}
   Q_\varepsilon(r,\gamma)=0.}
   \tag{3}
   \]
   There is also an absolute constant \(C>0\) such that, for every \(r>0\) and \(|\gamma|\ge4\),
   \[
   \boxed{\sup_{\varepsilon>0}Q_\varepsilon(r,\gamma)
   \le \min\{1,Cr\log(2+|\gamma|)\}.}
   \tag{3a}
   \]
   Thus blindness holds at growing heights whenever \(r\log(2+|\gamma|)\to0\), with the safe-line parameter allowed to depend arbitrarily on both \(r\) and \(\gamma\).
2. **The pole-scale response survives.** For fixed \(q>0\) and \(v\in\mathbb R\),
   \[
   \boxed{\lim_{\varepsilon\downarrow0}
   Q_\varepsilon(q\varepsilon,v\varepsilon)
   =\frac{q}{(1+q)^2+v^2}.}
   \tag{4}
   \]
   In particular the response tends to \(1/4\) when \(r=\varepsilon\) and \(\gamma=0\).
3. **Compact-height blindness is not uniform over all heights.** For every fixed \(\varepsilon,r>0\) and every finite \(R>0\),
   \[
   \boxed{\sup_{\gamma\in\mathbb R}Q_\varepsilon(r,\gamma)
   =\sup_{\gamma>R}Q_\varepsilon(r,\gamma)
   =Q_\varepsilon(r,0).}
   \tag{5}
   \]
   Consequently even for an arbitrary finite height cutoff \(R(\varepsilon)\),
   \[
   \lim_{\varepsilon\downarrow0}\sup_{\gamma>R(\varepsilon)}
   Q_\varepsilon(q\varepsilon,\gamma)=\frac{q}{(1+q)^2}.
   \tag{6}
   \]

The bounded arithmetic family therefore does develop persistent small-scale response, but this alone is not a detector aligned with hypothetical off-line zeros. It fails even after optimizing \(\varepsilon\) on every fixed nonzero compact ordinate set, and more quantitatively throughout the growing-height regime in (3a). At sufficiently large heights, almost-periodic prime phases reproduce the pole-centered maximum; no conclusion places those recurrent peaks at zeta-zero ordinates. These distinct quantifiers are essential.

## Exact arithmetic response

For a negative-frequency tone, shifting the Fourier transform of the kernel gives
\[
P_+(e^{-i\omega t}k_{r,\gamma})
=e^{-r\omega-i\gamma\omega}k_{r,\gamma}
\qquad(\omega>0).
\]
Uniform absolute convergence in (2) therefore proves
\[
P_+(\varphi_\varepsilon k_{r,\gamma})
=\frac{L(1+\varepsilon+r+i\gamma)}{A_\varepsilon}k_{r,\gamma}.
\]
Pythagoras yields the exact Poisson-variance identity
\[
Q_\varepsilon(r,\gamma)
=(P_r*|\varphi_\varepsilon|^2)(\gamma)
-\left|\frac{L(1+\varepsilon+r+i\gamma)}{A_\varepsilon}\right|^2.
\tag{7}
\]
This is equality, rather than just the general bounded-symbol inequality in WI-438, because the symbol is anti-analytic. Expanding both terms gives the absolutely convergent double series
\[
Q_\varepsilon(r,\gamma)
=\sum_{n,m\ge2}a_{\varepsilon,n}a_{\varepsilon,m}
\left(e^{-r|\log(n/m)|}-(nm)^{-r}\right)
\cos\!\left(\gamma\log(n/m)\right).
\tag{8}
\]
Every coefficient before the cosine is nonnegative, and their sum is at most one. In particular
\[
0\le Q_\varepsilon(r,\gamma)\le Q_\varepsilon(r,0).
\tag{9}
\]
The lower inequality follows from the norm definition, not from a claim that every oscillatory summand is positive. Formula (8) retains coherent prime-ratio phases; replacing it by a sum of individual tone energies would define a different object.

## Uniform local blindness, including arbitrary parameter selection

The simple pole of zeta at one implies
\[
L(1+z)=z^{-1}+O(1),\qquad
A_\varepsilon=\varepsilon^{-1}+O(1).
\tag{10}
\]
Zeta has no zeros on \(\Re s=1\). Given compact \(K\subset\mathbb R\setminus\{0\}\), choose \(\delta>0\) such that its closed \(\delta\)-neighborhood excludes zero. Analyticity and nonvanishing give a bound for \(L(1+\varepsilon+it)\) on this neighborhood, uniformly for sufficiently small \(\varepsilon\ge0\). Hence
\[
|\varphi_\varepsilon(t)|\le C_K\varepsilon
\quad\text{when }\operatorname{dist}(t,K)\le\delta.
\]
Outside that neighborhood use \(|\varphi_\varepsilon|\le1\). Dropping the nonnegative subtracted term in (7) gives, uniformly in \(\gamma\in K\),
\[
Q_\varepsilon(r,\gamma)
\le C_K^2\varepsilon^2+\frac{2r}{\pi\delta}
\qquad(0<\varepsilon\le\varepsilon_0).
\tag{11}
\]
This proves joint decay as \(\varepsilon,r\downarrow0\), without requiring a relation between their rates.

To include all \(\varepsilon>0\), fix \(0<\eta<\varepsilon_0\). For \(\varepsilon\ge\eta\), termwise differentiation of (2), and the single \(n=2\) term as a lower bound for \(A_\varepsilon\), give
\[
\|\varphi_\varepsilon'\|_\infty
\le \frac1{\log2}\sum_{n\ge2}\Lambda(n)\log n
\left(\frac2n\right)^{1+\eta}
=:C_\eta<\infty.
\tag{12}
\]
These symbols are uniformly bounded and Lipschitz. Since constants have zero Hankel part, splitting the Poisson integral at \(|t-\gamma|=h\) shows
\[
\sup_{\varepsilon\ge\eta,\gamma\in\mathbb R}Q_\varepsilon(r,\gamma)
\le C_\eta^2h^2+\frac{8r}{\pi h}\longrightarrow0
\tag{13}
\]
by taking, for example, \(h=r^{1/3}\). For \(0<\varepsilon<\eta\), (11) instead bounds the limsup by \(C_K^2\eta^2\). Letting \(\eta\downarrow0\) proves (3). Thus a depth-dependent selection of the safe line does not evade the local conclusion.

## A quantitative height-depth boundary, uniform in the safe line

The extra arithmetic input for (3a) is the classical logarithmic-derivative bound
\[
|L(\sigma+it)|\ll\log|t|
\quad\left(|t|\ge t_0,\quad
\sigma\ge1-\frac{c}{\log|t|}\right)
\tag{13a}
\]
for some absolute \(c,t_0>0\), inside a zero-free region. This is Titchmarsh's Theorem 3.11, specialization (3.11.7); it is unconditional and concerns the edge \(\Re s=1\), not a zero-free neighborhood of the critical line.

Put \(M_\gamma=\log(2+|\gamma|)\). For \(|u-\gamma|\le1\), sufficiently large \(|\gamma|\), and \(0<\varepsilon\le1\), a circle of radius \(c_1/M_\gamma\) about \(1+\varepsilon+iu\) lies inside the region of (13a), after fixing a sufficiently small absolute \(c_1>0\). Cauchy's derivative estimate gives
\[
|L'(1+\varepsilon+iu)|\ll M_\gamma^2.
\tag{13b}
\]
The same bound, with an enlarged constant, holds over the remaining compact range \(4\le|\gamma|\le\gamma_0\): the compact set \(1\le\sigma\le2\), \(3\le|u|\le\gamma_0+1\) contains neither a zero nor the pole of zeta. Analyticity in a neighborhood of that set bounds \(L'\).

The positive real normalization satisfies \(A_\varepsilon\asymp\varepsilon^{-1}\) throughout \(0<\varepsilon\le1\), by (10), positivity, and compactness away from zero. Consequently (13b) gives
\[
|\varphi_\varepsilon'(u)|\ll\varepsilon M_\gamma^2.
\tag{13c}
\]
Independently, absolute differentiation of the Euler series gives the global bound
\[
|\varphi_\varepsilon'(u)|
\le\frac{-L'(1+\varepsilon)}{A_\varepsilon}
\ll\varepsilon^{-1}
\qquad(0<\varepsilon\le1).
\tag{13d}
\]
Here \(-L'(1+\varepsilon)=\varepsilon^{-2}+O(1)\) near zero, and continuity covers the rest of the interval. The two bounds have complementary dependence on the normalization:
\[
\min\{\varepsilon M_\gamma^2,\varepsilon^{-1}\}
\le M_\gamma.
\]
For \(\varepsilon\ge1\), the global derivative bound (12) with \(\eta=1\) is an absolute constant. Combining these cases proves, for a fixed absolute \(C_1\ge1\),
\[
\boxed{\sup_{\varepsilon>0,\ |u-\gamma|\le1}
|\varphi_\varepsilon'(u)|\le C_1M_\gamma.}
\tag{13e}
\]
This is a local estimate at each ordinate, uniform in the entire parameter family. It does not assert a global Lipschitz constant independent of height.

For completeness, the passage from this derivative estimate to a Hankel response keeps the long Poisson tail. Since \(P_-k_{r,\gamma}=0\), subtracting the constant \(\varphi_\varepsilon(\gamma)\) and using contractivity yields
\[
Q_\varepsilon(r,\gamma)
\le\int_{\mathbb R}P_r(u)
|\varphi_\varepsilon(\gamma+u)-\varphi_\varepsilon(\gamma)|^2\,du.
\tag{13f}
\]
Set \(D=C_1M_\gamma\ge1\) and \(h=D^{-1}\le1\). On \(|u|\le h\), the squared difference is at most \(D^2u^2\); elsewhere it is at most four because \(\|\varphi_\varepsilon\|_\infty\le1\). Thus
\[
\begin{aligned}
Q_\varepsilon(r,\gamma)
&\le \frac{2D^2r}{\pi}\int_0^h
       \frac{u^2}{r^2+u^2}\,du
   +\frac{8r}{\pi}\int_h^\infty\frac{du}{r^2+u^2}\\
&\le \frac{2D^2rh}{\pi}+\frac{8r}{\pi h}
 =\frac{10Dr}{\pi}.
\end{aligned}
\tag{13g}
\]
The separate contraction bound \(Q_\varepsilon\le1\) proves (3a). Discarding the long tail or treating the Poisson kernel as having finite second moment would not justify this estimate.

One useful equivalent restriction concerns the recurrent peaks. For fixed \(q,\tau>0\), if \(|\gamma|\ge4\) and \(Q_\varepsilon(q\varepsilon,\gamma)\ge\tau\), then
\[
|\gamma|\ge
\exp\!\left(\frac{\tau}{Cq\varepsilon}\right)-2.
\tag{13h}
\]
This is a necessary height for such a peak, not an existence theorem at that height or an upper bound on recurrence time. The pole-centered peak in (4) is outside \(|\gamma|\ge4\). WI-458's doubly exponential window cost concerns a different question: a uniform rare-peak *fraction* over all interval placements. Neither statement locates peaks at zero ordinates.

## Exact pole-scale limit

For each fixed real \(x\), (10) gives
\[
\varphi_\varepsilon(\varepsilon x)\longrightarrow
\psi(x):=\frac1{1+ix}.
\tag{14}
\]
The symbols are bounded by one. Multiplication by the fixed \(L^2\) kernel \(k_{q,v}\), dominated convergence, and contractivity of \(P_-\) imply
\[
H_{\varphi_\varepsilon(\varepsilon\,\cdot)}k_{q,v}
\longrightarrow H_\psi k_{q,v}\quad\text{in }L^2.
\]
Positive dilations commute with the Hardy projections, so the squared norm on the left is \(Q_\varepsilon(q\varepsilon,v\varepsilon)\). Partial fractions compute the limit without approximation:
\[
\frac{1}{(1+ix)(q-i(x-v))}
=\frac{1}{1+q+iv}
\left(\frac1{1+ix}+\frac1{q-i(x-v)}\right).
\]
Only the first summand has negative Fourier support. Using \(\int_{\mathbb R}(1+x^2)^{-1}dx=\pi\) proves (4). This limit is supplied by the ordinary pole at \(s=1\), not by an off-critical zero or a new prime-cancellation estimate.

## Why the maximum recurs at arbitrarily large heights

For fixed \(\varepsilon\), (2) is a uniform limit of trigonometric polynomials. It is a Bohr almost-periodic function. For every \(b>0\), there are arbitrarily large positive translations \(\tau\) with
\[
\sup_t|\varphi_\varepsilon(t+\tau)-\varphi_\varepsilon(t)|<b.
\tag{15}
\]
Here only the elementary absolutely convergent case is needed: truncate (2) to make its coefficient tail small, simultaneously approximate the finitely many phases \(\tau\log n\) by multiples of \(2\pi\), then restore the tail. Finite-dimensional torus recurrence supplies arbitrarily large such translations; no quantitative bound on their size is used.

Translation invariance of \(P_-\), and \(k_{r,\tau}(t+\tau)=k_{r,0}(t)\), give
\[
\left|\sqrt{Q_\varepsilon(r,\tau)}-
\sqrt{Q_\varepsilon(r,0)}\right|\le b.
\tag{16}
\]
Together with (9), this proves (5), and then (4) at \(v=0\) proves (6). The recurrence is taken at each fixed \(\varepsilon,r\) before the small-\(\varepsilon\) limit. It provides no uniform recurrence time and no intersection theorem with any prescribed zero set.

## Consequence, controls, and evidence boundary

For a one-defect Kunik packet, WI-438 identifies \(r=(1-\theta)d\), with fixed \(0<\theta<1\) and horizontal depth \(d\). If its ordinate stays in a fixed compact set away from zero, (3) makes every normalized mixed response through this entire source family tend to zero, even after choosing \(\varepsilon\) as a function of \(d\): Cauchy--Schwarz bounds that response by \(\sqrt{Q_\varepsilon}\). Equation (3a) extends this conclusion to arbitrary growing ordinates satisfying \(d\log(2+|\gamma|)\to0\), uniformly over every selection \(\varepsilon=\varepsilon(d,\gamma)>0\). Thus this specific normalized Euler family cannot furnish an ordinate-uniform positive shallow-defect quantum, including in that growing-height regime.

This conclusion does not exclude actual off-line zeros. Fixed-height zeta zeros cannot be varied freely in depth. For a hypothetical sequence of growing-height exceptions, (3a) rules out a positive response quantum when \(d\log(2+|\gamma|)\to0\); it does not prove that actual off-line zeros satisfy or violate that condition. Outside this regime, (6) prevents global uniform decay. A useful application there still requires a new arithmetic statement relating the actual zero ordinates to the coherent phases in (8), with quantitative height/depth control. Neither recurrence nor operator norm one supplies it. Translating a symbol to a selected ordinate can also move the pole-scale peak; that operation alone carries no evidence about the divisor.

The normalization \(A_\varepsilon\) is part of the theorem. Removing it changes the operator budget; allowing signed coefficient redesign, arbitrary symbol translations or different pole-subtracted families changes the candidate and requires a separate test. No claim is made that (1) exhausts source-derived Hankel operators. No global \(L^2\) norm of the zeta logarithmic derivative is assumed: only bounded symbols times normalized \(L^2\) kernels enter the argument.

The exact checks are the negative-tone shift leading to (7), nonnegativity of the coefficient in (8), the uniform split (11)--(13), the complementary derivative bounds (13c)--(13e), the full Poisson-tail calculation (13g), and the rational partial fraction in (14). The pole-scale limit and far-height recurrence deliberately test and rule out an overstrong global-blindness interpretation. The logarithmic height threshold is sufficient for blindness, not claimed sharp. Multiplicities and critical-line simplicity are not used or inferred.

## Prior art and mathematical delta

The Euler expansion, simple pole and zero-free line are classical; see NIST DLMF [§25.2](https://dlmf.nist.gov/25.2), especially (25.2.11), and [§25.10(i)](https://dlmf.nist.gov/25.10#i). Logarithmic differentiation of the Euler product gives (2); the pole expansion gives (10). The quantitative growing-height bound also uses E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition revised by D. R. Heath-Brown, Clarendon Press (1986), Theorem 3.11 and (3.11.7), pp. 59--60 ([university-hosted scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)). This is the classical bound (13a); Cauchy's estimate, normalization, and the Poisson integral give (3a) directly. No new zero-free region or logarithmic-derivative estimate is claimed.

The anti-analytic Hankel reproducing-kernel/Poisson-variance identity is classical Garsia theory. Ana Čolović, *Reproducing Kernel Thesis of Hankel Operators on Weighted Hardy Spaces*, [arXiv:2406.03106](https://arxiv.org/abs/2406.03106), Introduction, Theorem 1.1 and §2, explicitly records the disk formulation; the half-plane identity required here is proved directly above. Ingo Schoolmann, *On Bohr's theorem for general Dirichlet series*, **Mathematische Nachrichten 293** (2020), 1591–1612, [DOI 10.1002/mana.201800542](https://doi.org/10.1002/mana.201800542), discussion preceding Corollary 3.9 on p. 1603, records the uniform-trigonometric-approximation characterization and vertical almost periodicity. Our absolutely convergent recurrence needs only the elementary finite-phase argument.

No new general Hankel, almost-periodicity, or zeta theorem is claimed. WI-438 treats fixed symbols or equicontinuous families, while the present family loses global equicontinuity and has the persistent response (4). WI-454 resolves a universal decomposition, rather than testing an arithmetic symbol. The additional result here is the complete response test for (1): uniform blindness on nonzero compact height sets even after safe-line optimization, its quantitative extension to \(r\log(2+|\gamma|)\to0\), the exact pole-scale limit, and recurrent global maxima. The quantitative extension supplies a deterministic pointwise restriction even under parameter adaptation; a height-density estimate for each fixed parameter cannot substitute for it. It closes this specific candidate for uniform shallow detection while preserving the unresolved alignment problem outside the proved height-depth regime. It provides no new zero proportion, zero-free region, or RH implication.
