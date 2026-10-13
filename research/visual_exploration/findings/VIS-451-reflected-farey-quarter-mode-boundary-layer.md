# VIS-451 — reflected near-maximal Farey transport has a rare quarter-mode boundary layer

## Claim and evidence status

In the reflection-preserving, four-defect artificial Farey control of FD-324, fix an odd integer \(a\ge3\) and take the source prime limit first. Its continuum transport profile is
\[
g_a(t)=h_a\left(\mathbf 1_{(0,\alpha_a)}(t)-\mathbf 1_{(1-\alpha_a,1)}(t)\right),
\qquad h_a=1-\frac1a,\quad \alpha_a=\frac{a-1}{2a}.
\]
Let \(I_{a,m}=\int_0^1g_a(t)\sin(\pi mt)\,dt\), \(d_a=\int_0^1g_a(t)^2\,dt=h_a^3\), and \(P_a(m)=2I_{a,m}^2/d_a\). Reflection forces \(P_a(m)=0\) for every odd \(m\). As \(a\to\infty\), the limiting probability law lives only on \(m=2j\) with \(j\) odd and has weights \(8/(\pi^2j^2)\), as in FD-324.

There is nevertheless an **exact rare sector** invisible to every fixed-frequency limit: for indices divisible by four,
\[
\boxed{\quad P_a(4\mathbb N)=\frac1{2(a-1)}.\quad} \tag{1}
\]
Its **conditioned** frequency law is exactly
\[
\boxed{\quad
P_a(4\ell\mid4\mathbb N)
=\frac1a f\left(\frac\ell a\right),\qquad
f(x)=\frac{(1-\cos2\pi x)^2}{\pi^2x^2},\quad f(0)=0 .
\quad} \tag{2}
\]
Thus \(f\) is a probability density and, for the conditional cumulative law,
\[
\sup_{X\ge0}\left|
\sum_{1\le\ell\le aX}P_a(4\ell\mid4\mathbb N)
-\int_0^X f(x)\,dx\right|
=O(a^{-1}). \tag{3}
\]
In the **reflected** family the disappearing \(m=4\ell\) energy is located at absolute frequencies \(m\asymp a\). Formula (2) is the same sampling density as the disappearing even sector of the **unreflected** FD-323 family in VIS-449, but its physical mode index, reflection constraint, and normalizing energy are different.

**Evidence:** EXACT-DERIVED + CLASSICAL FOURIER/BERNOULLI IDENTITY + FD-324 SPECIALIZATION + NEGATIVE PARITY-NORMALIZATION CONTROL. No general Fourier novelty, genuine Farey spectral anomaly, or RH implication is claimed.

## Exact quarter-mode energy

Integrating the two reflected arcs gives, for \(j\ge1\),
\[
I_{a,2j}=\frac{h_a}{\pi j}
\bigl(1-\cos(2\pi j\alpha_a)\bigr)
=\frac{h_a}{\pi j}\bigl(1-(-1)^j\cos(\pi j/a)\bigr). \tag{4}
\]
The odd-mode integrals vanish by reflection. For \(j=2\ell\), equation (4) becomes
\[
I_{a,4\ell}=\frac{h_a}{2\pi\ell}
\bigl(1-\cos(2\pi\ell/a)\bigr). \tag{5}
\]
For \(0\le t\le1\), the classical Bernoulli-polynomial Fourier identity states
\[
\sum_{\ell\ge1}\frac{1-\cos2\pi\ell t}{\ell^2}
=\pi^2t(1-t). \tag{6}
\]
Using \((1-\cos u)^2=2(1-\cos u)-\tfrac12(1-\cos2u)\) in (6), with \(t=1/a\) and \(2/a\) (both in \([0,1]\) for \(a\ge3\)), gives
\[
\sum_{\ell\ge1}
\frac{(1-\cos(2\pi\ell/a))^2}{\ell^2}
=\frac{\pi^2}{a}. \tag{7}
\]
Consequently
\[
e_{4,a}:=\sum_{\ell\ge1}2I_{a,4\ell}^2
=\frac{h_a^2}{2a},\qquad
d_a=2\alpha_a h_a^2=h_a^3,
\]
proving (1). Dividing each term \(2I_{a,4\ell}^2\) by \(e_{4,a}\) gives (2) **without asymptotic approximation**. In particular \(\frac1a\sum_{\ell\ge1}f(\ell/a)=1\) exactly for every admitted \(a\).

## Why the scaled cumulative law is uniform

The function \(f\) is continuous at zero, with \(f(x)=4\pi^2x^2+O(x^4)\). At infinity \(f(x)=O(x^{-2})\) and \(f'(x)=O(x^{-2})\); near zero \(f'(x)=O(x)\). Hence \(f\) is bounded, integrable, and has finite total variation \(V(f)\) on \([0,\infty)\). For a right-endpoint mesh of size \(1/a\), comparison on every complete cell gives error at most \(V(f)/a\). The final partial cell adds at most \(\|f\|_\infty/a\), so the error in (3) is bounded by \([V(f)+\|f\|_\infty]/a\), uniformly over all \(X\ge0\). The identity
\[
\int_0^\infty\frac{(1-\cos2\pi x)^2}{\pi^2x^2}\,dx=1
\]
also follows directly from the standard cosine-integral formula; alternatively, equation (7) and the uniform Riemann-sum bound imply it. Therefore the limiting measure is a probability law, with no mass lost at infinity or the origin.

The \(m\asymp a\) scale can also be read directly from (5): for fixed \(\ell\), \(I_{a,4\ell}=O(\ell/a^2)\), but \(\sum_{\ell}2I_{a,4\ell}^2\asymp a^{-1}\). Fixed modes cannot account for the total rare-sector energy. At cutoff \(\ell/a\to X\), the conditional cumulative fraction approaches \(\int_0^X f\); cutoffs \(o(a)\) catch a vanishing fraction, whereas cutoffs \(\gg a\) catch all of it.

## Comparison with the unreflected energy-matched control

FD-323's near-maximal unreflected transport has limiting sine distribution
\[
P_{\rm unref}(m)=
\begin{cases}
8/(\pi^2m^2),&m\ {\rm odd},\\
0,&m\ {\rm even};
\end{cases}
\]
FD-324's reflected transport has
\[
P_{\rm ref}(m)=
\begin{cases}
8/(\pi^2j^2),&m=2j,\ j\ {\rm odd},\\
0,&\text{otherwise}.
\end{cases} \tag{8}
\]
Both normalized laws have total mass one and correspond to the same limiting total transport energy \(3/\pi^2\) **within their respective families**, but their absolute-mode supports are disjoint. Their spectral total-variation distance is therefore exactly one. If \(F_{\rm odd}(q)=\sum_{1\le j\le q,\ j\ {\rm odd}}8/(\pi^2j^2)\), then their absolute-mode cumulative distributions are respectively \(F_{\rm odd}(q)\) and \(F_{\rm odd}(q/2)\); their parity-indexed distributions are identical. For example the absolute first-mode cutoff has masses \(8/\pi^2\) and zero. These differences are wholly induced by reflection and index rescaling, **not** by a newly detected source-order invariant.

The quarter-mode boundary layer (1)–(3) adds a different diagnostic from the limiting disjoint-support observation: it identifies exactly where the tiny *allowed but asymptotically disappearing* reflected sector sits before the \(a\to\infty\) limit, and prevents declaring it absent merely because every fixed quarter-mode tends to zero. VIS-449 exhibits the analogous mechanism in the other family, with a distinct parity selection.

## Source transfer, tests, prior art, and limits

For each fixed odd \(a\), FD-324 provides an infinite arithmetic progression of permitted primes and an exact reflected edge-preserving reconstructed path. Its transport coefficients converge to \((\sqrt6/\pi)I_{a,m}\), with total continuum energy \((3/\pi^2)d_a>0\). The full-spectrum FD-320/VIS-447 transfer and sine Parseval then give convergence of the actual reassembled conditional quarter-mode law to (2), **first as \(p\to\infty\) with \(a\) fixed**. The quarter-mode transport denominator tends to \((3/\pi^2)e_{4,a}>0\) for every such \(a\).

A joint \(p,a\to\infty\) conclusion is **not automatic**: the finite quarter-mode transport energy must be bounded below at order \(1/a\), the finite transport profile must approximate (5) on frequencies \(m\asymp a\), and VIS-450's projected perturbation ratio must vanish. A sufficient conditional bound is \(\operatorname{TV}_{4\mathbb N}\le\sqrt{E_p/T_{4\mathbb N,p,a}}\), so \(aE_p\to0\) suffices **when** \(T_{4\mathbb N,p,a}\ge c/a\) and the separate continuum approximation gate holds. A sufficiently slow diagonal exists from the fixed-parameter limits, but this asserts no uniform prime-in-progression estimate.

Independent direct summation of the sine integrals for \(a=3,5,9,17,65,257\) agrees with \(e_{4,a}=h_a^2/(2a)\) to the expected \(O(1/M)\) tail at cutoff \(M=10^6\); the exact conditional probabilities in (2) agree coefficientwise. Numerically, the conditioned CDF at \(\ell/a\le2\) approaches the integrated value \(0.9251302294\) as \(a\) grows. An exploratory plotted comparison of the density and sampled cumulative laws was used to choose the \(m/a\) view; the equations above, not the plotted image, establish the result.

The identity (6) is classical: see NIST DLMF §24.8(i), Fourier series for Bernoulli polynomials (https://dlmf.nist.gov/24.8), and Stein–Shakarchi, *Fourier Analysis: An Introduction* (2003), already anchored in this line's SOURCES.md. The reflected Farey source construction and its **within-family** energy ceiling come from FD-324; the unreflected comparison is FD-323/VIS-449; the normalization/perturbation gate is VIS-450. The only added mathematics claimed here is this specific exact quarter-mode allocation, conditional mesoscopic scaling, and the caution it imposes on matched Farey controls. Nothing establishes a null ensemble for genuine Farey spectra, a source-natural order restriction, an improvement of Franel–Landau discrepancy, or RH.

## Research consequence

The reflection-parity equal-energy clue remains a genuine research question: the two artificial controls are equal-energy yet mutually singular in **absolute** mode indexing; matching by \(j\) erases that contrast. Moreover an asymptotically vanishing allowed parity subband can retain a universal mesoscopic conditioned spectrum. A meaningful genuine-Farey residual must freeze absolute vs reindexed cutoffs, each model's own total and conditional energy, and a source-natural exclusion test before regarding spectral allocation as arithmetic evidence.
