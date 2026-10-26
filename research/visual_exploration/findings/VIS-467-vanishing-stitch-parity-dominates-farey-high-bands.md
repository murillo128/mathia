# VIS-467 — Vanishing stitch parity dominates conditioned Farey high bands

## Claim and evidence boundary

For [[research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy|FD-319]]'s reflected four-defect reassembly, VIS-466 shows that the
right-endpoint transport has a globally vanishing odd-sine fraction
`1/(N−4)`. That error is **not negligible after high-band conditioning**.
For the upper half of the absolute sine modes, its odd fraction tends to

\[
\boxed{\quad \frac{\pi}{16-4\pi}=0.91494809158\ldots.\quad} \tag{1}
\]

This is also the limiting total-variation distance between raw transport
and its antisymmetric projection, each normalized inside that band. The
full reassembled discrepancy has exactly zero odd mass; whenever its
conditional law is defined, its distance from conditioned raw transport
is at least the raw odd fraction. No asymptotic transfer estimate for the
remaining even coefficients is needed for this lower bound.

**Evidence:** EXACT-DERIVED + CLASSICAL FINITE-SINE/RIEMANN-SUM
SPECIALIZATION + REPRESENTATION/CONDITIONING OBSTRUCTION. The claim is
about the explicit artificial control, not genuine Farey spectral
allocation, a new general Fourier theorem, or an RH implication.

## Exact vector and all four mode classes

Let \(N\ge10\) be even, \(b\ne0\), and \(h=N/2\). Define
\[
v_k=\begin{cases}
b,&2\le k\le h-1,\\
-b,&h+2\le k\le N-1,\\
0,&\text{otherwise},
\end{cases}
\qquad 1\le k<N.
\]
The Farey instance is \(N=N_p=\sum_{q\le p}\varphi(q)\),
\(b=1/(2p)\), for odd primes \(p\ge7\).
Write \((Jv)_k=v_{N-k}\), \(a=(v-Jv)/2\), and \(s=(v+Jv)/2\).
Then
\[
T=\|v\|^2=b^2(N-4),\quad \|s\|^2=b^2,\quad
\|a\|^2=b^2(N-5).
\]
With the orthonormal DST-I convention
\[
\widehat v_m=\sqrt{2/N}\sum_{k=1}^{N-1}v_k\sin(\pi mk/N),
\quad \theta_m=\pi m/N,
\]
put \(\widehat v_m=b\sqrt{2/N}\,A_m\). The complete finite formula is
\[
A_m=\begin{cases}
\cos\theta_m-\sin\theta_m,&m\equiv1\pmod4,\\
2\cos\theta_m\cot(\theta_m/2),&m\equiv2\pmod4,\\
-\cos\theta_m-\sin\theta_m,&m\equiv3\pmod4,\\
0,&m\equiv0\pmod4.
\end{cases} \tag{2}
\]
Consequently \(\pi_m(v):=|\widehat v_m|^2/T
=2A_m^2/[N(N-4)]\).

For odd \(m\), only the four symmetric stitch values contribute:
\(s_1=s_{N-1}=-b/2\), \(s_{h-1}=s_{h+1}=b/2\).
Their sine sum gives the first and third cases of (2).
For even \(m=2r\), reversing the negative block gives
\[
A_{2r}=2\sum_{k=1}^{h-1}\sin(k\theta_{2r})
       -\sin\theta_{2r}-\sin((h-1)\theta_{2r}).
\]
The finite geometric sum evaluates this as
\[
[1-(-1)^r]\,[\cot(\theta_{2r}/2)-\sin\theta_{2r}]
=[1-(-1)^r]\cos\theta_{2r}\cot(\theta_{2r}/2),
\]
which proves the other two cases. In particular, no continuum step
approximation is used at frequencies comparable with \(N\).

## Rescaled high-frequency measure

Fix \(0<\alpha<1\), and define the absolute-mode band
\(B_{N,\alpha}=\{m:1\le m<N,\ m/N\ge\alpha\}\).
The measures below are considered on \([\alpha,1]\), away from the
low-frequency singularity. Separate Riemann sums in the four residue
classes of (2) give
\[
N\sum_{\substack{m\in B_{N,\alpha}\\m\text{ odd}}}
 \pi_m(v)\,\delta_{m/N}\ \Longrightarrow\ dx,
\qquad
N\sum_{\substack{m\in B_{N,\alpha}\\m\text{ even}}}
 \pi_m(v)\,\delta_{m/N}\ \Longrightarrow\ g(x)\,dx,
\tag{3}
\]
where
\[
g(x)=2\cos^2(\pi x)\cot^2(\pi x/2).
\]
These are weak limits of finite measures, not probability laws on the
whole unit interval. Each residue class has spacing \(4/N\). Its
limiting density is \(A_r(x)^2/2\); adding the odd classes gives
\(\tfrac12[(\cos\pi x-\sin\pi x)^2+
(-\cos\pi x-\sin\pi x)^2]=1\). The only nonzero even class gives
\(g\). All integrands are continuous and bounded on \([\alpha,1]\),
so rounding the band edge changes these limits by zero.

Let
\[
M(\alpha)=1-\alpha+\int_\alpha^1g(x)\,dx>0.
\]
Then
\[
N\pi(v)(B_{N,\alpha})\to M(\alpha),\qquad
\pi(v)(m\text{ odd}\mid B_{N,\alpha})\to
q(\alpha):=\frac{1-\alpha}{M(\alpha)}. \tag{4}
\]
For numerical reproduction one may use the closed expression
\[
M(\alpha)=\frac4\pi\left[\cot\frac{\pi\alpha}{2}
+\sin\pi\alpha\right]+\frac{\sin2\pi\alpha}{2\pi}
-4(1-\alpha). \tag{5}
\]
Indeed, setting \(\theta=\pi x\),
\(\cos^2\theta\cot^2(\theta/2)
=\csc^2(\theta/2)-2-2\cos\theta-\cos^2\theta\)
provides an elementary antiderivative. At \(\alpha=1/2\),
\(M=8/\pi-2\); (4) gives (1).

Also \(g(1-u)=\pi^2u^2/2+O(u^4)\). Thus, with
\(\delta=1-\alpha\),
\[
M(\alpha)=\delta+\pi^2\delta^3/6+O(\delta^5),\qquad
q(\alpha)=1-\pi^2\delta^2/6+O(\delta^4).
\]
This last statement takes \(N\to\infty\) first at fixed \(\alpha\),
then \(\alpha\uparrow1\). It does not assert a uniform shrinking-band
limit with only finitely many modes.

## Exact conditional separation and the missing transfer gate

The sine transforms of \(a\) and \(s\) have disjoint even and odd
supports. Moreover \(\widehat a_m=\widehat v_m\) at every even mode.
For any band \(B\) with nonzero projected energy, this proves the exact
mixture identity
\[
\operatorname{TV}(\pi^B(v),\pi^B(a))
=\frac{\sum_{m\in B,\ m\text{ odd}}|\widehat v_m|^2}
       {\sum_{m\in B}|\widehat v_m|^2}. \tag{6}
\]
Here \(\pi^B\) always normalizes by its own energy inside \(B\).
For fixed \(\alpha<1\), both energies are positive for all sufficiently
large even \(N\), since \(\int_\alpha^1g>0\).
Globally (6) is \(1/(N-4)\); in \(B_{N,\alpha}\) it tends to
\(q(\alpha)>0\).

For the actual reflected reassembly \(y=e+v\), rank antisymmetry gives
\(\widehat y_m=0\) for odd \(m\). Thus whenever its band law exists,
\[
\operatorname{TV}(\pi^B(y),\pi^B(v))
\ge\pi^B(v)(m\text{ odd}). \tag{7}
\]
This is a deterministic lower bound using the odd event, not a claim
that \(y\) and \(a\) have the same even-band distribution.

The raw band energy is asymptotic to \(b^2M(\alpha)\), and the removed
odd band energy to \(b^2(1-\alpha)\). In the Farey instance both are of
order \(p^{-2}\), although full transport energy is of order one.
The residual must cancel precisely that odd contribution. Therefore
VIS-450's projected error-to-band-energy ratio cannot tend to zero for
raw transport in these fixed high bands. After removing \(s\), transfer
from \(a\) to \(y\) still requires an independent estimate for
\(\|\Pi_B Q_-e\|^2/\|\Pi_Ba\|^2\), with \(Q_-=(I-J)/2\).
Neither global \(E_p=o(1)\) nor the corrected full-spectrum energies
\(E_p-\|s\|^2,T_p-\|s\|^2\) supply that band estimate automatically.

## Falsification controls and prior art

Independent DST-I checks compared (2) at every mode for all even
\(10\le N\le256\), and \(N=1000,1002,4096,4098\). Maximum coefficient
error with \(b=1\) was below \(1.1\cdot10^{-14}\); complete odd energy
agreed with one to \(8\cdot10^{-16}\). Direct sine matrices at
\(N=10,18,40,64,128\) agreed within \(2.8\cdot10^{-14}\).
Conditioned mixture checks at \(\alpha=1/4,1/2,3/4,9/10\), omitting
undefined zero-energy projections, agreed within \(4\cdot10^{-16}\).
Scaling by \(-3\) and rank reversal changed normalized laws by less than
\(3.5\cdot10^{-15}\).

Integer Farey recurrence and independent gap reassembly at
\(p=7,11,19,43,101,211\) verified the actual block identity and full
reflection. The first three used exact rational arithmetic. Floating
vector residuals were below \(3\cdot10^{-15}\); full-discrepancy odd
energy was below \(8\cdot10^{-27}\), and all upper-half comparisons
satisfied (7). Totient counts and full DSTs at
\(p=7,11,19,43,101,211,503,1009\) verified the finite approach to (1).
At \(p=211\), \(N=13624\), global odd share is approximately
\(7.34214\cdot10^{-5}\), while the upper-half odd share is
\(0.914948091581\). Generic even dimensions obey the same formulas:
primality is not the source of this pattern. These checks falsify
implementation mistakes; finite sums and Riemann sums establish the claim.

[VIS-466](VIS-466-reflected-farey-transport-parity-is-a-stitch-boundary-term.md)
provides the four-stitch decomposition and global leakage identity;
[VIS-450](VIS-450-projected-parity-transfer-sharpens-farey-gate.md)
already explains why conditioning needs projected energy, including an
abstract counterexample. The additional result here is a **realized
Farey-control high-band obstruction**, with all four exact coefficient
classes, the explicit rescaled measure (3), and the quantitative
conditional distance (1). It is not another assertion of the generic
conditioning warning.

Classical boundary-convention references include Gilbert Strang,
[The Discrete Cosine Transform](https://doi.org/10.1137/S0036144598336745),
*SIAM Review* 41:1 (1999), 135–147, especially the meshpoint/midpoint
boundary distinction, and the
[FFTW real even/odd transform manual](https://www.fftw.org/fftw3_doc/Real-even_002fodd-DFTs-_0028cosine_002fsine-transforms_0029.html).
The [SciPy DST reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dst.html)
specifies the numerical convention. Searches covered endpoint/sampling
spectral leakage, conditional total variation, and Farey excursion
spectra. No general novelty is claimed for finite geometric sums,
reflection parity, conditioning instability, or Riemann-sum limits.
The exact source-specific constants above were independently derived.

The paired [high-band visualization](../visualizations/farey-stitch-high-band.md)
makes the two normalizations explicit. Its implication is narrow: a
high-frequency comparator cannot discard a globally small stitch term
without pricing its energy **inside the selected band**. The projected
transport is an analysis vector, not a second admissible Farey grid.
No matched-null expectation, genuine Farey anomaly, source-natural
ordering theorem, or Franel–Landau improvement is established.
