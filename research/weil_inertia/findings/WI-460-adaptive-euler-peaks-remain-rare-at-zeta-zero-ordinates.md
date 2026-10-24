# WI-460 — Adaptive Euler peaks remain rare at zeta-zero ordinates

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-SAMPLING + SOURCE-FAMILY-OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** [WI-457](WI-457-normalized-euler-hankel-symbols-have-local-blindness-and-recurrent-peaks.md), for the normalized Euler family and deterministic height-depth bound; [WI-458](WI-458-euler-hankel-peaks-have-exponentially-small-height-density.md), for its finite-window mean; [WI-459](WI-459-safe-line-optimization-preserves-double-exponential-euler-peak-rarity.md), for safe-line localization, its finite parameter net, and rare-peak density.

## Claim: simultaneous adaptation and discrete sampling

Retain the Fourier phase \(e^{-it\xi}\), negative-frequency projection \(P_-\), and notation
\[
L(s)=-\zeta'(s)/\zeta(s),\quad A_\varepsilon=L(1+\varepsilon),\quad
\varphi_\varepsilon(t)=L(1+\varepsilon+it)/A_\varepsilon,
\]
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},\qquad
Q_\varepsilon(r,\gamma)=\|P_-(\varphi_\varepsilon k_{r,\gamma})\|_2^2.
\tag{1}
\]
Every symbol is bounded by one. Define
\[
M_r(\gamma)=\sup_{\varepsilon>0}Q_\varepsilon(r,\gamma),\qquad
\mathcal M_R(\gamma)=\sup_{0<r\le R}M_r(\gamma).
\tag{2}
\]
Both the safe line and the packet width may be selected separately at each ordinate. There is no positive lower cutoff on the allowed widths.

Let \(N(T)\) count all nontrivial zeta zeros with \(0<\Im\rho\le T\), with multiplicity, and write \(m_\rho\) for the multiplicity of a distinct zero. Put
\[
Z_R(T;\tau)=\sum_{\substack{\rho=\beta+i\gamma\text{ distinct}\\T<\gamma\le2T}}
m_\rho\,\mathbf1_{\{\mathcal M_R(\gamma)\ge\tau\}}.
\tag{3}
\]
For every fixed \(0<\tau<1\), there are constants \(c_\tau,C_\tau,R_\tau>0\) and \(T_\tau\) such that
\[
\boxed{\frac{Z_R(T;\tau)}{N(2T)-N(T)}
\le C_\tau\left(R^2+\frac{\log T}{T}\right)
\quad(0<R<R_\tau,\ T\ge T_\tau).}
\tag{4}
\]
The stronger fixed-\(R\) asymptotic estimate is
\[
\boxed{\limsup_{T\to\infty}
\frac{Z_R(T;\tau)}{N(2T)-N(T)}
\le\exp[-\exp(c_\tau/R)]
\quad(0<R<R_\tau).}
\tag{5}
\]
In particular, for **every** function \(R(T)>0\) tending to zero,
\[
Z_{R(T)}(T;\tau)=o(N(2T)-N(T)).
\tag{6}
\]
Equation (4), rather than an interchange of limits in (5), already proves this arbitrary-diagonal conclusion. No doubly exponential rate is asserted in (6).

These are bounds on zeros receiving a large response from a specified normalized source family. They neither count off-line zeros without an additional response lower bound nor distinguish critical-line multiplicity from horizontal displacement. In particular, they do not exclude a finite or zero-density exceptional set.

## Packet regularity supplies a sampling scale

Write \(F_r(\gamma)=\sqrt{M_r(\gamma)}\). The unit kernels in (1) satisfy
\[
\|\partial_{\log r}k_{r,\gamma}\|_2=\tfrac12,
\qquad
\|\partial_\gamma k_{r,\gamma}\|_2=\frac1{\sqrt2\,r}.
\tag{7}
\]
Indeed, putting \(u=t-\gamma\),
\[
r\partial_r k_{r,\gamma}
=\left(\tfrac12-\frac r{r-iu}\right)k_{r,\gamma},
\qquad
\left|\tfrac12-\frac r{r-iu}\right|=\tfrac12.
\]
For the second equality, integrate
\((r/\pi)(r^2+u^2)^{-2}\), whose integral is \(1/(2r^2)\).
Contractivity of multiplication by \(\varphi_\varepsilon\) and of \(P_-\), followed by the reverse triangle inequality, gives
\[
|F_r(\gamma)-F_{r'}(\gamma)|\le\tfrac12|\log(r/r')|,
\qquad
|F_r(\gamma)-F_r(\gamma')|
\le\frac{|\gamma-\gamma'|}{\sqrt2\,r}.
\tag{8}
\]
The same bounds hold before taking the supremum over \(\varepsilon\); a supremum of uniformly Lipschitz functions preserves the bound. No differentiability or maximizing selector for \(M_r\) is needed. Continuity in the positive parameters also expresses the suprema in (2) through countable dense parameter sets, so their superlevel sets are measurable.

Fix a threshold \(0<a<1\). If \(M_r(\gamma)\ge a\), then
\[
[\gamma-h,\gamma+h]\subseteq\{M_r\ge a/4\},
\qquad h=r\sqrt{a/2}.
\tag{9}
\]
This follows because the square root decreases by at most \(\sqrt a/2\) over that interval. Thus a sampled peak comes with positive width even when its location was selected using the zero set.

The unconditional Riemann--von Mangoldt formula gives, uniformly for \(u\in[T-1,2T+1]\),
\[
\sum_{|\gamma-u|\le1}m_\rho\ll\log T,
\qquad N(2T)-N(T)\asymp T\log T.
\tag{10}
\]
These counts include every real part and all multiplicities. For \(r<1/2\), integrate the intervals (9) over the zeros with \(T<\gamma\le2T\) and \(M_r(\gamma)\ge a\). Their overlap multiplicity is at most the first bound in (10), since \(h<1\). If their total zero count is denoted by \(n_r(T;a)\), Tonelli's theorem proves
\[
2h\,n_r(T;a)
\le C\log T\,
\big|\{M_r\ge a/4\}\cap[T-h,2T+h]\big|.
\tag{11}
\]
Consequently
\[
\boxed{\frac{n_r(T;a)}{N(2T)-N(T)}
\le\frac{C_a}{rT}
\big|\{M_r\ge a/4\}\cap[T-h,2T+h]\big|.}
\tag{12}
\]
There is no minimum-spacing assumption. Several mirror zeros or a high multiplicity at one ordinate are paid for by (10).

## Two complementary estimates for each fixed width

For each fixed positive threshold \(b\), the finite safe-line net in WI-459 gives constants \(\theta_1,\ldots,\theta_J>0\), independent of \(r\) and height, such that for all sufficiently small \(r\),
\[
\{M_r\ge b\}\subseteq
\bigcup_{\ell=1}^J\{Q_{\theta_\ell r}(r,\cdot)\ge b/4\}.
\tag{13}
\]
Its essential premises are the two-sided mismatch estimate
\(Q_\varepsilon(r,\gamma)\ll\min(r/\varepsilon,\varepsilon/r)\) for small \(r,\varepsilon\), the \(O(r)\) bound for \(\varepsilon\ge1\), and Lipschitz continuity of \(\sqrt Q\) in \(\log\varepsilon\). In particular (13) is not a union over infinitely many independently averaged safe lines.

WI-458's finite-window mean gives, on every interval \(I\) of length \(H>0\),
\[
\frac1H\int_I Q_\varepsilon(r,t)\,dt
=A_\varepsilon^{-2}
\sum_{n\ge2}\frac{\Lambda(n)^2}{n^{2+2\varepsilon}}(1-n^{-2r})
+O(H^{-1}),\qquad0<\varepsilon\le1.
\tag{14}
\]
The error is absolute and uniform in the starting height. For any of the finitely many \(\varepsilon=\theta_\ell r\), positivity, \(1-n^{-2r}\le2r\log n\), and \(A_\varepsilon\asymp\varepsilon^{-1}\) bound the main term by
\[
C\varepsilon^2r\sum_{n\ge2}\frac{\Lambda(n)^2\log n}{n^2}
\ll_{\theta_\ell}r^3.
\]
The series converges by \(\Lambda(n)\le\log n\). Markov's inequality and (13) therefore imply the useful all-window bound
\[
\boxed{\frac{|\{M_r\ge b\}\cap I|}{H}
\le C_b(r^3+H^{-1}).}
\tag{15}
\]
Using \(b=a/4\) in (12) yields
\[
\boxed{\frac{n_r(T;a)}{N(2T)-N(T)}
\le C_a\left(r^2+\frac1{Tr}\right).}
\tag{16}
\]

In contrast, the rare-peak bound of WI-459 gives, for a constant \(b_a>0\),
\[
\boxed{\limsup_{T\to\infty}
\frac{n_r(T;a)}{N(2T)-N(T)}
\le\frac{C_a}{r}\exp[-\exp(b_a/r)].}
\tag{17}
\]
The constants work for every sufficiently small fixed \(r\). To see this directly, apply its upper uniform height-density estimate at threshold \(a/4\) to the interval in (12), whose length is \(T+2h\). The factor \(1/r\) is the sampling cost; dropping it would not follow from local zero counts. Equations (16) and (17) serve different purposes: (17) controls a fixed finite collection of widths, whereas (16) controls the infinitely shrinking tail with its error retained.

## An infinite width bank with a controlled tail

Set
\[
\kappa=\sqrt\tau/2,\qquad r_j=Re^{-\kappa j}\quad(j=0,1,\ldots),
\qquad a=\tau/4.
\tag{18}
\]
If \(\mathcal M_R(\gamma)\ge\tau\), choose a width \(0<r\le R\) with \(F_r(\gamma)>3\sqrt\tau/4\). Some \(r_j\) satisfies \(r\le r_j<e^\kappa r\), with equality at a grid endpoint harmless. Equation (8) gives \(F_{r_j}(\gamma)>\sqrt\tau/2\). Therefore
\[
\{\mathcal M_R\ge\tau\}\subseteq\bigcup_{j\ge0}\{M_{r_j}\ge a\}.
\tag{19}
\]
This step also covers a supremum that is not attained.

One cannot sum the \(1/(Tr_j)\) errors in (16) over all \(j\). The deterministic growing-height estimate of WI-457 removes precisely that problem:
\[
M_r(\gamma)\le C r\log(2+|\gamma|),\qquad |\gamma|\ge4.
\tag{20}
\]
If a grid width contributes a zero in \((T,2T]\), then
\[
r_j\ge \ell_T:=\frac{a}{C\log(2+2T)}.
\tag{21}
\]
Thus only finitely many widths are active at each \(T\). The geometric sums satisfy
\[
\sum_{j\ge0}r_j^2\le\frac{R^2}{1-e^{-2\kappa}},\qquad
\sum_{r_j\ge\ell_T}\frac1{Tr_j}
\le\frac1{T\ell_T(1-e^{-\kappa})}
\ll_\tau\frac{\log T}{T}.
\tag{22}
\]
Summing (16) using (19)--(22) proves (4).

For the stronger asymptotic claim, fix \(0<\eta<R\). The grid widths \(r_j\ge\eta\) form a finite set, so (17) can be summed before taking a limsup. On the remaining active widths, (16) and (22) give the uniform bound
\[
\sum_{\ell_T\le r_j<\eta}
\frac{n_{r_j}(T;a)}{N(2T)-N(T)}
\ll_\tau\eta^2+\frac{\log T}{T}.
\tag{23}
\]
First take \(T\to\infty\), then \(\eta\downarrow0\). This legitimate finite-part/tail argument gives
\[
\limsup_{T\to\infty}\frac{Z_R(T;\tau)}{N(2T)-N(T)}
\le C_\tau\sum_{j\ge0}\frac1{r_j}
\exp[-\exp(b_a/r_j)].
\tag{24}
\]
For small \(R\) this series is bounded by twice its first term: the ratio of successive terms is
\[
e^\kappa\exp\{-e^{b_a/r_j}(e^{(e^\kappa-1)b_a/r_j}-1)\},
\]
which is at most \(1/2\) uniformly in \(j\) once \(R\) is small. Absorbing \(2C_\tau/R\) by reducing the positive inner-exponent constant proves (5). Neither countable subadditivity of upper asymptotic densities nor an unproved uniform convergence in width has been used.

## Mathematical consequence and adversarial boundaries

The earlier height-density estimates alone did not sample the divisor. The additional ingredient here is interval persistence (9), coupled to multiplicity-aware local zero counts. It converts peak measure into an upper bound for the number of **responsive** zeros, and the mean estimate plus (20) makes this work even after selecting both parameters at each zero. This closes an actual parameter/sampling gap for this family, without asserting random prime phases at zero ordinates.

For a Kunik packet with \(r=(1-\vartheta)d\), \(0<\vartheta<1\) fixed and horizontal depth \(d\), every off-line zero with \(r\le R\) and a response at least \(\tau\) is included in (3). Their count obeys the same upper bounds. No theorem here forces an off-line zero to have that response. Even such a hypothetical lower bound, combined with (6), would only control the corresponding population in density and could leave sparse exceptions.

The following controls delimit the result.

- Every zero is counted with its multiplicity and real part unrestricted. This is compatible with conjugation and functional-equation pairs, and assumes neither RH nor simplicity.
- An arbitrary null set may contain every zero; that objection is valid for unstructured sets. The transfer here uses the proved width of a lower-threshold neighborhood and explicitly pays \(1/r\). It is not a measure-only inference.
- The \(r^3\) mean becomes \(r^2\) after sampling. Losing a power of width still leaves a summable geometric tail. The \(O(H^{-1})\) error cannot be summed without (20)--(21).
- No lower width cutoff or attained joint supremum is assumed. Conversely the threshold is fixed and positive; thresholds tending to zero need new uniform constants.
- Equations (4)--(6) concern dyadic height intervals. They do not give a uniform upper Banach density for the all-width supremum on arbitrarily translated intervals of a prescribed length, nor a doubly exponential finite-height estimate for unrestricted \(R(T)\).
- Rare recurrent peaks remain compatible with the result. No claim says every zero avoids them, that any peak occurs at a zero, or that a lower fraction of zeros is responsive.
- The normalized symbols have a common pole center at height zero. Arbitrary translations of each symbol, coefficient redesign, or removal of the normalization change the observable and its input bounds.

The exact audit points are the two kernel norms in (7), multiplicity-aware overlap in (11), the uniform mean error in (14), the finite safe-line net, and the order of the two limits in (23)--(24). The argument is analytic; it is not numerical evidence or a Lean-checked theorem. Its auxiliary sampling and geometric-sum lemmas are classical.

## Prior art and novelty assessment

Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, **Journal of Number Theory 235** (2022), 219--241, Corollary 1.2 ([author-hosted paper](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf), [arXiv:2107.06506](https://arxiv.org/abs/2107.06506)), gives an explicit \(O(\log T)\) Riemann--von Mangoldt error. Subtracting at bounded-distance endpoints gives (10); the main term gives its dyadic normalization. Only these coarse classical consequences are used.

H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **J. London Math. Soc.** (2) 8 (1974), 73--82, Corollary 3, equation (1.11) ([author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)), is the source of the all-window mean (14), reconstructed in WI-458. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition revised by D. R. Heath-Brown (1986), Theorem 3.11, equation (3.11.7), pp. 59--60 ([university-hosted scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)), supplies the safe-line logarithmic-derivative bound used in WI-457 to derive (20). No new zero-free or prime-mean estimate is claimed.

Continuous-to-discrete large-value estimates and zeta-ordinate sampling are established methods. Locally, WI-389 already uses the unit-interval zero count to sample fixed-exponential-type Fourier transforms; it does not cover the adaptive Hankel family or the infinite width tail here. As neighboring arithmetic prior art, Hung M. Bui, Alexandra Florea and Micah B. Milinovich, *Negative discrete moments of the derivative of the Riemann zeta-function*, **Bull. London Math. Soc. 56** (2024), 2680--2703, [DOI 10.1112/blms.13092](https://doi.org/10.1112/blms.13092), §3, prove an RH-conditional discrete Dirichlet-polynomial mean formula with an explicit prime off-diagonal term. That stronger arithmetic sampling identity is not imported here; (11) needs only local counts and norm continuity and is unconditional.

The double-exponential input remains the classical-concentration specialization in WI-458--WI-459. The delta is its extension to actual zero-ordinate sampling with simultaneous safe-line and arbitrarily small width selection, together with the uniform finite-height bound (4). This is a derived application of classical regularity, sampling and tail truncation, with no literature-priority claim. It strengthens the diagnosis of this source family, not the established simple-critical proportion and not RH.
