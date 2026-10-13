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
