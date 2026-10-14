# NB-348 — Rounded offset sampling gives positive-density physical source witnesses

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-345, NB-346, NB-347
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + SAMPLED-SOBOLEV-STABILITY + STRONG-L2-OFFSET-LIMIT + POSITIVE-DENSITY-FINITE-OFFSETS + UNBOUNDED-DILATION-UNIFORMITY + NON-TARGET-AWARE

## Claim

Retain the intrinsic phase profile and physical adjacent witness of NB-347:
\[
\mathfrak D(t)=\sum_{k\ge1}\frac{\|kt\|_{\mathbb Z}^{2}}{k^2},
\quad H=\frac{\pi^2}{72},\quad
E_{n,m}=\sqrt m\,P_{U_n}A_m|_{U_n}-R_n,\quad
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\]
For integer \(q\ge3\), let \(h_q(t)\) be a nearest integer to \(qt\), \(r_q(t)=h_q(t)/q\), on \([-1/2,1/2]\) (ties at bin boundaries are immaterial). For periodic \(f\in H^1(\mathbb T)\), use its unique continuous representative and put
\[
\mathscr T_qf(t)=q\left[f\left(r_q(t)+\frac{r_q(t)}{q-1}\right)-f(r_q(t))\right].
\]

**Sampled Sobolev theorem.** For every such \(f\),
\[
\boxed{\|\mathscr T_qf\|_{L^2(-1/2,1/2)}^2
 \le\frac{q}{2(q-1)}\|f'\|_{L^2(\mathbb T)}^2,\qquad
 \mathscr T_qf\longrightarrow t f'(t)\ \text{in }L^2(-1/2,1/2).}
\tag{1}
\]
In particular, with
\[
\mathcal L(t)=-\frac t4\mathfrak D'(t)-\frac12[H-\mathfrak D(t)],\qquad
\mathscr C_q(t)=-\frac14\mathscr T_q\mathfrak D(t)
-\frac12[H-\mathfrak D(r_q(t))],
\tag{2}
\]
one has \(\|\mathscr C_q-\mathcal L\|_2\to0\). Unlike NB-347's unsampled mean-square statement, this concerns the discontinuously rounded physical phase grid.

For every integer \(|h|\le q/2\), every integer \(a\ge2\), and every \(n\ge q\), set \(m=aq(q-1)+h\). The exact physical coefficient obeys the uniform reduction
\[
\boxed{m\langle E_{n,m}g_2,\nu_q\rangle
=\mathscr C_q(h/q)+O\!\left(\frac{\log(2q)}q\right),}
\tag{3}
\]
where the implied constant is absolute, independent of \(h,a,n\). Therefore even arbitrary choices \(a=a_{q,h}\ge2\), \(n=n_{q,h}\ge q\) at each grid point have the same strong sampled-phase \(L^2\) limit.

**Positive-density integer offsets.** With the exact constants of NB-347,
\[
\mu=\frac{5\pi^2}{1152},\quad
M_0^2=\frac{\pi^2(27200-521\pi^2)}{31334400},\quad
p_0=\frac{\mu^2}{4M_0^2}=0.06602848\ldots,
\]
define
\[
S_q=\{h\in\mathbb Z:|h|\le q/2,\ \mathscr C_q(h/q)\le-\mu/4\}.
\]
Then
\[
\boxed{\liminf_{q\to\infty}\frac{|S_q|}{q}\ge p_0>0.066.}
\tag{4}
\]
For all sufficiently large \(q\), *each* \(h\in S_q\), *every* integer \(a\ge2\), and *every* \(n\ge q\), writing \(m=aq(q-1)+h\), satisfy
\[
\boxed{\frac{m\sqrt{\log q}}q\|E_{n,m}\|
 \ge\frac{\mu}{16}\sqrt{\frac2{\log2}}
 =0.00454778\ldots .}
\tag{5}
\]
Thus a positive proportion of **simultaneous integer offsets at each large scale** admits one uniform physical source-side certificate, even when the dilation multiples have no upper growth bound.

## Sampled Sobolev estimate and convergence

Write \(x_h=h/q\) and \(\delta_h=h/[q(q-1)]\), and let \(I_{q,h}\) be the nearest-integer bin corresponding to \(h\), clipped to \([-1/2,1/2]\). It has length at most \(1/q\). Let \(J_{q,h}\) be the unoriented arc on the unit circle from \(x_h\) to \(x_h+\delta_h=h/(q-1)\), in the direction of the signed increment.

The arcs have pairwise disjoint interiors modulo one. Indeed, for \(h\ge0\), \(h/(q-1)\le(h+1)/q\) for the admissible indices, while the arcs for \(h<0\) lie in the reversed adjacent half-cells. The two extreme arcs, if crossing the identified endpoints \(\pm1/2\), still occupy disjoint sides of that point. All arcs are bounded by successive grid points of spacing \(1/q\).

The fundamental theorem of calculus in one-dimensional \(H^1\) and Cauchy–Schwarz give
\[
q^2|f(x_h+\delta_h)-f(x_h)|^2
\le q^2|\delta_h|\int_{J_{q,h}}|f'(s)|^2\,ds.
\]
Multiply by \(|I_{q,h}|\le1/q\), sum, use disjoint interiors and
\[
q|\delta_h|=\frac{|h|}{q-1}\le\frac{q}{2(q-1)}.
\]
This proves the uniform bound in (1). For \(f\) smooth and periodic, \(r_q(t)=t+O(q^{-1})\) and Taylor's formula yield \(\mathscr T_qf(t)=tf'(t)+O_f(q^{-1})\) uniformly. Smooth periodic functions are dense in \(H^1(\mathbb T)\); the uniform bound and \(\|tf'\|_2\le\frac12\|f'\|_2\) extend the strong \(L^2\) convergence to all \(H^1\) functions. The proof does not sample pointwise values of \(f'\).

By NB-347(1)–(2), \(\mathfrak D\in H^1(\mathbb T)\), is continuous, and
\(\|\mathfrak D'\|_2^2=\pi^2/18\). Equation (1) applies, while uniform continuity ensures \(\mathfrak D(r_q(t))\to\mathfrak D(t)\) uniformly. Equation (2) thus yields \(\mathscr C_q\to\mathcal L\) strongly in \(L^2\).

For the physical coefficient, NB-345(5) and NB-347(9) give, uniformly whenever \(q\ge8\), \(|h|\le q/2\), \(a\ge2\), \(n\ge q\),
\[
m\langle E_{n,m}g_2,\nu_q\rangle
=-\frac q4\left[\mathfrak D\left(\frac h{q-1}\right)
-\mathfrak D\left(\frac hq\right)\right]
-\frac12\left[H-\mathfrak D\left(\frac hq\right)\right]
+O\left(\frac{\log(2q)}q\right).
\]
The leading terms are exactly \(\mathscr C_q(h/q)\). In the Bernoulli derivation, \(m/q=a(q-1)+h/q\ge q\), all periodic phase differences are independent of \(a\), and the remaining terms decrease with \(m/q\). This proves (3) without growth restrictions.

## Quantitative parity-divisor sampling rate

The strong \(L^2\) limit in (2) has an unconditional quantitative rate for the exact arithmetic phase profile:
\[
\boxed{\displaystyle
\|\mathscr C_q-\mathcal L\|_{L^2(-1/2,1/2)}
\ll q^{-1/2}(\log(2q))^{3/2}.}
\tag{2a}
\]
Consequently, the *same* physical-offset sets from (4) satisfy
\[
\boxed{\displaystyle
\frac{|S_q|}{q}\ge p_0-O\!\left(\frac{(\log(2q))^3}{q}\right),
\qquad q\ge3.}
\tag{4a}
\]
All implied constants are absolute but not numerically optimized; no finite-\(q\) onset is certified. The improvement concerns source-side sampling, not the per-offset bound (5) or the Nyman--Beurling target distance.

For the proof, set \(s(j)=\sigma_{\pm}(j)\). NB-347(6) gives \(s(2^au)=(a-1)\tau(u)\) for odd \(u\). Dividing the modified \(2\)-Euler factor \(\sum_{a\ge0}(a-1)^2x^a=(1-3x+4x^2)/(1-x)^3\) by the ordinary factor \(\sum_{a\ge0}(a+1)^2x^a=(1+x)/(1-x)^3\) yields
\[
\boxed{\displaystyle
\sum_{j\ge1}\frac{s(j)^2}{j^z}
=\frac{1-3\,2^{-z}+4\,2^{-2z}}{1+2^{-z}}
\frac{\zeta(z)^4}{\zeta(2z)},\qquad \Re z>1.}
\tag{7a}
\]
At \(z=2\), this recovers NB-347's \(\sum s(j)^2/j^2=\pi^4/36\). At \(z\downarrow1\) the positive real Euler-factor ratio tends to \(1/3\), leaving a fourth-order divergence. Since the Fourier coefficient of \(\mathfrak D\) at frequency \(j\ne0\) is \(s(|j|)/(2\pi^2j^2)\), the regularity threshold is sharp:
\[
\boxed{\mathfrak D\in H^s(\mathbb T)\quad (s<3/2),
\qquad \mathfrak D\notin H^{3/2}(\mathbb T).}
\tag{7b}
\]

For quantitative approximation, \(|s(j)|\le\tau(j)\) and \(\tau(j)^2\le d_4(j)\), the latter following multiplicatively from \((a+1)^2\le{a+3\choose3}\). Summing the first three factors of the fourfold divisor function therefore proves the elementary estimate
\[
\sum_{j\le X}s(j)^2
\le\sum_{n\le X}d_4(n)
\le X\left(\sum_{a\le X}\frac1a\right)^3
\ll X(\log(2X))^3.
\tag{7c}
\]
Let \(\mathfrak D_N\) be the Fourier truncation of NB-347(1) through frequency \(N\), including its mean. Parseval gives
\(\|\mathfrak D_N''\|_2^2=8\sum_{j\le N}s(j)^2\) and
\(\|(\mathfrak D-\mathfrak D_N)'\|_2^2=(2/\pi^2)\sum_{j>N}s(j)^2/j^2\).
Applying (7c) and dyadic summation yields
\[
\|\mathfrak D_N\|_{H^2}\ll N^{1/2}(\log(2N))^{3/2},
\qquad
\|\mathfrak D-\mathfrak D_N\|_{H^1}
\ll N^{-1/2}(\log(2N))^{3/2}.
\tag{7d}
\]
The tail has zero mean, so its \(H^1\) norm is controlled by the derivative. No pointwise differentiated Fourier series is used.

The rounded sampling operator satisfies a stronger **\(H^2\)-consistency estimate**, in addition to the \(H^1\)-stability of (1):
\[
\boxed{\|\mathscr T_qf-tf'\|_2\ll q^{-1}\|f\|_{H^2(\mathbb T)}
\quad(f\in H^2(\mathbb T),\ q\ge3).}
\tag{7e}
\]
Indeed, on a nearest-grid bin \(I_{q,h}\), put \(g=f'\), \(x_h=h/q\),
\(\delta_h=h/[q(q-1)]\), and \(b_h=q\delta_h=h/(q-1)\). The exact decomposition is
\[
\mathscr T_qf(t)-tg(t)
=(b_h-t)g(t)
+b_h\int_0^1[g(x_h+\theta\delta_h)-g(t)]\,d\theta.
\]
The first term has \(|b_h-t|\ll q^{-1}\). The points in the integral lie in an enlarged circular bin \(K_{q,h}\) of length \(O(q^{-1})\); those enlarged bins have uniformly bounded overlap, including across the periodic endpoints. Absolute continuity, Cauchy--Schwarz, and Jensen bound the squared norm of the second term by
\[
O(q^{-2})\sum_h\int_{K_{q,h}}|g'(s)|^2\,ds
\ll q^{-2}\|f''\|_2^2.
\]
This proves (7e) without sampling derivative values at rational phases.

Use (7e) for \(f=\mathfrak D_q\) and the uniform \(H^1\) bound (1) for \(f=\mathfrak D-\mathfrak D_q\). Equation (7d) at \(N=q\) gives
\[
\|\mathscr T_q\mathfrak D-t\mathfrak D'\|_2
\ll q^{-1}\|\mathfrak D_q\|_{H^2}
+\|\mathfrak D-\mathfrak D_q\|_{H^1}
\ll q^{-1/2}(\log(2q))^{3/2}.
\]
Binwise absolute continuity also yields
\(\|\mathfrak D\circ r_q-\mathfrak D\|_2
\ll q^{-1}\|\mathfrak D'\|_2\).
Substitute both estimates in (2) to obtain (2a), then square the error in Chebyshev's estimate (6) to obtain (4a).

The cubic logarithm in the divisor-square mean is classical (Jia and Sankaranarayanan, *The Mean Square of Divisor Function*, Acta Arith. 164 (2014), 181--208, arXiv:1311.4041), but (7c) is proved directly and is the only divisor-moment input. The sampled \(H^2\) estimate is standard one-dimensional approximation theory. The line-specific addition is the rate for the actual rounded physical Nyman source coefficient. It provides no target-occupation, inverse-section, or RH consequence and remains pending independent adversarial review.

## Positive-density conversion and physical Hilbert norm

NB-347(11a)–(11d) establish
\[
\int_{-1/2}^{1/2}\mathcal L(t)\,dt=-\mu,\qquad
\|\mathcal L\|_2^2\le M_0^2,
\]
and consequently a measurable set \(A=\{t:\mathcal L(t)\le-\mu/2\}\) of measure at least \(p_0\). Let \(B_q=\{t:\mathscr C_q(t)\le-\mu/4\}\). On \(A\setminus B_q\), the absolute error \(|\mathscr C_q-\mathcal L|\) exceeds \(\mu/4\). By Chebyshev,
\[
|B_q|\ge p_0-\frac{16}{\mu^2}
\|\mathscr C_q-\mathcal L\|_2^2=p_0-o(1).
\tag{6}
\]
Because \(\mathscr C_q\) is constant on each bin \(I_{q,h}\), of length at most \(1/q\), the set \(B_q\) is, up to irrelevant boundaries, a union of bins indexed by \(S_q\). Thus \(|B_q|\le|S_q|/q\), proving (4).

For every \(h\in S_q\), equation (3) yields
\(|m\langle E_{n,m}g_2,\nu_q\rangle|\ge\mu/8\) uniformly over all \(a,n\), for large enough \(q\). The *physical* Cauchy–Schwarz estimate of NB-304, also used in NB-347, is
\[
\frac{m\sqrt{\log q}}q\|E_{n,m}\|
\ge\kappa_q|m\langle E_{n,m}g_2,\nu_q\rangle|,\qquad
\kappa_q=\frac{2\sqrt{\log q}}
{\sqrt{\log2}\sqrt{2H_{q-2}+1+\pi^2/18}}
\longrightarrow\sqrt{\frac2{\log2}}.
\]
For all large \(q\), take the conservative bound \(\kappa_q\ge\frac12\sqrt{2/\log2}\); combined with \(\mu/8\) this proves (5).

## Falsification, numerics, and prior art

The arcs in (1) are disjoint even at the periodic endpoints; the inequality would not follow for arbitrary overlapping long chords. The proof uses *differences of continuous function values*, not a sampled derivative at rational points. Fixed even-denominator rational phases may have logarithmically growing coefficients by NB-346, but the uniform \(H^1\) estimate controls their aggregate \(L^2\) contribution. Neither pointwise uniform convergence in phase nor an effective uniform onset is asserted.

As a finite arithmetic sign/sampling check, use the exact rational evaluation
\[
\mathfrak D(P/Q)=Q^{-2}\sum_{j=1}^{Q}
\left\|\frac{Pj}{Q}\right\|_{\mathbb Z}^2
\psi_1(j/Q),
\]
already recorded in NB-346. Computing (2) from this formula gives \(|S_{64}|=51\), \(|S_{128}|=107\), \(|S_{256}|=211\). These are diagnostics, not the proof of asymptotic density.

The Sobolev stability-plus-density lemma is classical one-dimensional analysis, not an asserted new numerical-analysis theorem. Eymard–Gallouët–Herbin, *A cell-centred finite-volume approximation for anisotropic diffusion operators on unstructured meshes in any space dimension*, IMA J. Numer. Anal. 26 (2006), 326–353, DOI 10.1093/imanum/dri036 (arXiv:math/0505109), is related discretization literature, not an input or an exact precedent claimed for (1). Balazard–Martin, *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et une fonction définie par J. R. Wilton*, arXiv:1305.4395, remains the nearby fractional-part regularity boundary already audited in NB-347. The line-local mathematical contribution beyond NB-347 is the **rounded physical-grid limit and the simultaneous integer-offset density bound**, not the generic sampling lemma. No new specialized external estimate is invoked, so no SOURCES.md update is required.

The result belongs entirely to the **source/operator channel**. It establishes neither occupation by the actual moving first-free target, nor an approximation-distance rate, inverse-section conditioning, a nonvanishing unscaled mixing gap, or a consequence for RH. Independent adversarial review remains pending.
