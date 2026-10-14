# VIS-456 — A one-sided modular cut phase survives in the FD-327 Haar sine spectrum

## Claim and evidence status

Use the **artificial same-prime Farey edge reassemblies** and their fixed-cut source-prime-limit transport steps \(g_m\) from VIS-455, not genuine Farey ordering. For \(m\ge3\), let \(b_m(r)=\sqrt2\int_0^1g_m(x)\sin(\pi r x)\,dx\) and \(\pi_m^{\sin}(r)=b_m(r)^2/\|g_m\|_2^2\), \(r\ge1\). For residues \(j\in\mathbb Z/m\mathbb Z\), define the **positive-frequency** pushforward
\[
\mu_m^{\sin}(j)=\sum_{r\ge1:\,r\equiv j\pmod m}\pi_m^{\sin}(r).
\tag{1}
\]
There is a uniform-in-residue limit, with \(\theta=j/m\),
\[
\boxed{\sup_{0\le j<m}\left|m\mu_m^{\sin}(j)
-\bigl[1-\kappa\sin(2\pi j/m)\bigr]\right|\longrightarrow0,\qquad
\kappa=\frac2\pi\log\frac{32}{27}=0.10816108613\ldots .}
\tag{2}
\]
Consequently, although VIS-455 proves weak convergence of the coarse frequency law \(r/m^2\) to the normalized Haar density \(f(u)=(1-\cos2\pi u)^2/(\pi^2u^2)\), the moving **one-sided residue view at modulus \(m\)** retains nonuniform phase:
\[
\boxed{\operatorname{TV}(\mu_m^{\sin},U_m)\longrightarrow
\frac{\kappa}{\pi}=\frac2{\pi^2}\log\frac{32}{27}
=0.0344287430\ldots .}
\tag{3}
\]
Its signed reflection average
\(\widetilde\mu_m^{\sin}(j)=\tfrac12[\mu_m^{\sin}(j)+\mu_m^{\sin}(-j)]\)
instead satisfies
\[
\boxed{\operatorname{TV}(\widetilde\mu_m^{\sin},U_m)\longrightarrow0.}
\tag{4}
\]
If the normalized modes are formed using the **cosine** basis,
\(\pi_m^{\cos}(r)=2|\int_0^1g_m(x)\cos(\pi r x)\,dx|^2/\|g_m\|_2^2\) for \(r\ge1\), the constant cosine mode vanishes and
\[
\boxed{\sup_{0\le j<m}\left|m\mu_m^{\cos}(j)
-\bigl[1+\kappa\sin(2\pi j/m)\bigr]\right|\longrightarrow0.}
\tag{5}
\]

**Evidence:** EXACT-DERIVED; CLASSICAL HALF-LINE FOURIER/HAAR SPECIALIZATION; NEGATIVE SIGN-FOLDING AND BASIS-CHOICE CONTROL. Equations (2)–(5) are new conclusions *for the explicit VIS-455/FD-327 artificial source*, not claims of new general Fourier theory, genuine-Farey arithmetic structure, or RH progress. The source-prime limit precedes \(m\to\infty\).

## Derivation: the exact surviving phase

Retain the definitions of VIS-455:
\(M=m^2\), \(\alpha_m=1-1/m\),
\(D_m=2m/(m+2)\), \(F_m=2m^2/[(m+2)(m+4)]\), and
\[
h_m(z)=\frac{D_m}{2}\mathbf1_{(0,F_m)}(z)
-\frac{F_m}{2}\mathbf1_{(F_m,F_m+D_m)}(z),\qquad
H_m(u)=\int_0^\infty h_m(z)e^{i\pi uz}\,dz.
\]
Then \(g_m(\alpha_m+z/M)=2h_m(z)/M\),
\(h_m\to h=\mathbf1_{(0,2)}-\mathbf1_{(2,4)}\), and
\(\|h\|_2^2=4\). VIS-455's **exact**, not averaged, sine coefficient identity is
\[
M\pi_m^{\sin}(r)=\frac{|H_m(r/M)|^2
-\Re[e^{-2\pi ir/m}H_m(r/M)^2]}{\|h_m\|_2^2}.
\tag{6}
\]
It contains a translation/boundary interference phase with period \(m\) in the **mode index** \(r\); coarse \(r/M\) weak convergence averages that phase out.

For \(r=j+km\), \(u=r/M=(k+\theta)/m\) and \(e^{-2\pi ir/m}=e^{-2\pi i\theta}\). Thus, including the harmless \(r=0\) term when \(j=0\), since \(H_m(0)=0\),
\[
m\mu_m^{\sin}(j)=
\frac1{m\|h_m\|_2^2}\sum_{k\ge0}
\left\{|H_m((k+\theta)/m)|^2-
\Re[e^{-2\pi i\theta}H_m((k+\theta)/m)^2]\right\}.
\tag{7}
\]
The uniformly compactly supported, bounded-variation \(h_m\) have zero mean and bounded first moment, giving
\(|H_m(u)|\le C\min(u,u^{-1})\) and a uniformly integrable derivative bound for the two quadratic integrands in (7). Consequently their shifted Riemann sums converge to their integrals **uniformly in** \(\theta\in[0,1]\). Further, \(h_m\to h\) in \(L^2\); Plancherel and Cauchy–Schwarz yield convergence of both half-line integrals. Therefore the limit of (7) is
\[
\frac1{4}\left\{\int_0^\infty|H(u)|^2\,du-
\Re\left[e^{-2\pi i\theta}\int_0^\infty H(u)^2\,du\right]\right\},
\quad H(u)=\int_0^\infty h(z)e^{i\pi uz}\,dz.
\tag{8}
\]
Positive-half-line Plancherel gives \(\int_0^\infty|H|^2\,du=\|h\|_2^2=4\).

For the *non-conjugated* square, use Abel regularization followed by the elementary identity
\(\int_0^\infty e^{i\pi u(z+w)}\,du=i/[\pi(z+w)]\)
for \(z+w>0\), understood as the Abel limit. Bounded compact support makes the singularity at \(z=w=0\) integrable. It follows that
\[
\int_0^\infty H(u)^2\,du=
\frac i\pi\,I,\qquad
I=\int_0^4\int_0^4\frac{h(z)h(w)}{z+w}\,dz\,dw.
\tag{9}
\]
Split the square into \((0,2)\times(0,2)\), \((2,4)\times(2,4)\), and twice the mixed rectangle. Integrating \(1/(z+w)\) with primitive \(v\log v-v\) gives
\[
I=8\log(32/27)>0.
\tag{10}
\]
Alternatively, \(1/(z+w)=\int_0^\infty e^{-t(z+w)}dt\) shows
\(I=\int_0^\infty(\int h(z)e^{-tz}dz)^2dt>0\),
an independent positivity check. Inserting (9)–(10) into (8) proves (2).

Because the limit is uniform on the residue grid, its Riemann-sum total variation converges to
\(\tfrac{\kappa}{2}\int_0^1|\sin2\pi\theta|d\theta=\kappa/\pi\), proving (3). Reflection sends \(\theta\) to \(-\theta\) and cancels the odd sine term, giving (4). Replacing sine by cosine changes the **minus** interference term in (6) to a **plus** term; \(\int g_m=0\) eliminates the constant cosine mode and cosine Parseval normalizes the rest, giving (5).

## Independent checks, source boundary, and prior art

As a check separate from (7)–(10), direct trigonometric coefficients from VIS-455's finite-\(m\) step function were squared and summed over positive modes \(r\le250m^2\). At \(m=20,60,120\) the maximum deviation of \(m\mu_m^{\sin}(j)\) from the limit curve on the respective residue grids was about \(0.0150,0.00556,0.00311\); the cosine phase has the opposite sign, while the folded sine total variations were about \(0.00037,0.00032,0.00031\). These are **truncated exploratory checks**: the omitted total spectral mass is \(O(1/250)\) by VIS-455's uniform tail bound. The exact proof does not rely on their precision, and no PNG is retained as evidence.

The Fourier-scale/translation and wavelet ingredients are standard (Stein–Shakarchi, *Fourier Analysis*, 2003; Strang–Nguyen, *Wavelets and Filter Banks*, 1996, both anchored in this line's SOURCES.md). The half-line Cauchy-kernel computation in (9) is elementary. The specifically useful conclusion is that **VIS-455's actual one-sided sine spectrum**, not VIS-451/453's different reflected quarter-mode law, retains a measurable modulus-\(m\) cut-phase bias that signed folding removes. This is a predictable representation effect, not a discriminating arithmetic null.

FD-327's paired \(m=3\) and \(m=t+3\) reassemblies are available along the **same fixed-\(t\) prime progression**. For every fixed \(m\), its relative \(L^2\) source-prime transport convergence and Parseval imply total-variation convergence of the sine (and cosine) spectral law, hence of its pushforward modulo \(m\). Only **after** that limit may \(t\to\infty\) invoke (2)–(5) for \(m=t+3\). This supplies no simultaneous uniform \(m=m(p)\) theorem: the vanishing transport energy has order \(m^{-6}\), so relative finite-prime approximation errors remain essential.

## Research consequence

A moving modulus can recover a persistent **sign-odd boundary/cut phase** from a spectral family whose coarse rescaled energy has the universal Haar weak limit. Signed residue folding erases this bias asymptotically, and changing from sine to cosine reverses it. Accordingly, apparent residue anomalies require a declared signed-frequency convention, boundary basis, modulus scale, and normalization. The outstanding question in the accepted fixed-defect clue remains a *source-natural* discriminator of genuine arithmetic order, rather than a phase produced by an artificial cut or a choice of sine/cosine basis.
