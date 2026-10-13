# VIS-447 — uniform stability of normalized Farey excursion transport spectra

## Exact claim and evidence

Let \(p\) range over primes, \(N=N_p=\sum_{q\le p}\varphi(q)\), and \(D_p=(x_k-k/N)_{1\le k<N}\) be the genuine Farey rank-discrepancy vector. For a permutation \(\sigma\) of complete denominator-\(p\) excursions, retain the exact FD-320 decomposition
\[
D_p^\sigma=P_\sigma D_p+v_p^\sigma,\qquad
E_p=\|D_p\|_2^2=o(1),\qquad T_p=\|v_p^\sigma\|_2^2.
\]
Here \(P_\sigma\) is an orthogonal coordinate permutation; the unconditional \(E_p=o(1)\) uses the prime number theorem as established in FD-318/FD-320.

For a nonzero real rank-discrepancy vector \(z\), let \(\widehat z_m\) be its orthonormal Dirichlet sine coefficients, and write the **normalized spectral distribution**
\[
\pi_m(z)=\frac{|\widehat z_m|^2}{\|z\|_2^2},
\qquad
F_J(z)=\sum_{m\in J}\pi_m(z)
\quad (J\subseteq\{1,\ldots,N-1\}).
\]
For every \(\sigma\) with \(T_p>0\) and \(D_p^\sigma\ne0\),
\[
\boxed{\quad
\frac12\sum_{m=1}^{N-1}|\pi_m(D_p^\sigma)-\pi_m(v_p^\sigma)|
\ \le\ \min\{1,\sqrt{E_p/T_p}\}.
\quad} \tag{1}
\]
Consequently, **simultaneously for every frequency subset**, including even-only bands under reflection and full bands without reflection,
\[
\boxed{\quad
\sup_J|F_J(D_p^\sigma)-F_J(v_p^\sigma)|
\ \le\ \min\{1,\sqrt{E_p/T_p}\}.
\quad} \tag{2}
\]
No restriction on the number, position, or growth rate of modes is needed. For any sequence of excursion permutations, \(E_p=o(T_p)\) is a sufficient condition for uniform relative spectral-allocation transfer, even when \(T_p\to0\); the weaker statement \(T_p\to0\) alone gives no such transfer.

**Evidence/status:** EXACT-DERIVED + CLASSICAL NORMALIZED-VECTOR/PROJECTOR PRINCIPLE + PNT-ASSISTED FAREY SPECIALIZATION + NEGATIVE SMALL-TRANSPORT GATE. The general Hilbert-space inequality is elementary prior art, not a new theorem of perturbation theory.

## Proof and exact denominator gate

Put \(y=D_p^\sigma\), \(v=v_p^\sigma\), and \(e=P_\sigma D_p\), so \(y=v+e\), \(\|e\|=\sqrt{E_p}\), and \(\|v\|=\sqrt{T_p}\). Normalize the real sine-coordinate vectors \(a=\widehat y/\|y\|\) and \(b=\widehat v/\|v\|\). Orthonormality gives \(\|a\|=\|b\|=1\), and Cauchy–Schwarz yields
\[
\begin{aligned}
\frac12\sum_m|a_m^2-b_m^2|
&=\frac12\sum_m|(a_m-b_m)(a_m+b_m)|\\
&\le\frac12\|a-b\|\|a+b\|\\
&=\sqrt{1-\langle a,b\rangle^2}=\sin\theta,
\end{aligned}
\]
where \(\theta\in[0,\pi/2]\) is the angle between the **unoriented lines** spanned by \(y,v\). The distance from \(v\) to the line \(\mathbb R y\) equals \(\|v\|\sin\theta\), which is no greater than \(\|v-y\|=\|e\|\). Hence \(\sin\theta\le\sqrt{E_p/T_p}\); total variation is also at most one. This proves (1). The defining property of total variation proves (2) for every subset \(J\), without taking a union bound or paying the dimension \(N\).

The constant one in the general projector inequality cannot be improved without extra geometry: for unit \(v=(1,0)\), \(0<r<1\), and \(y=(1-r^2,r\sqrt{1-r^2})\), one has \(\|y-v\|=r\) and \(\sin\theta=r\). Choosing an orthogonal observation basis that diagonalizes \(yy^\top/\|y\|^2-vv^\top\), the two-outcome spectral total variation is exactly \(r\). This is a **generic sharpness control**, not a claim that every Farey sine cutoff attains equality.

In the VIS-034 notation, for any fixed comparison null with its **own** expected spectral fraction \(f_{\mathrm{null}}(J)=\mu_J/\mu_{\mathrm{tot}}>0\), define \(S_J(z)=F_J(z)/f_{\mathrm{null}}(J)\). Equations (1)–(2) give
\[
\boxed{\quad
|S_J(D_p^\sigma)-S_J(v_p^\sigma)|
\le\frac{\min\{1,\sqrt{E_p/T_p}\}}{f_{\mathrm{null}}(J)}.
\quad} \tag{3}
\]
Thus relative null-normalized allocation additionally requires control of the **null fraction denominator**. If \(f_{\mathrm{null}}(J)\to0\), even \(E_p=o(T_p)\) need not suffice for \(S_J\); the sufficient condition is \(\sqrt{E_p/T_p}=o(f_{\mathrm{null}}(J))\). If \(T_p\) is comparable to \(E_p\), the original FD-320 absolute error does not identify the normalized spectrum.

## Reflection-matched and unreflected controls

FD-319's four-defect reflection-preserving reassembly has \(T_p\to3/(4\pi^2)>0\). FD-322's three-defect **unreflected** positive-near-one family has \(T_p\to1/(6\pi^2)\) on \(p\equiv1\pmod6\) and \(T_p\to1/(4\pi^2)\) on \(p\equiv5\pmod6\). Equation (1) therefore transfers their respective **entire normalized spectra** from the explicit displacement vector to the actual reassembled discrepancy with \(o(1)\) total-variation error. FD-318 and FD-321 admit the analogous conclusion because their nonzero limiting transport energies are already established there.

For FD-319 and FD-322, the source-side fixed sine coefficients exhaust the nonzero limiting total energy. Equations (1)–(2) upgrade this fact to the moving-band statement
\[
F_{\{1,\ldots,q_p\}}(D_p^\sigma)\longrightarrow1
\qquad\text{for every }q_p\longrightarrow\infty,\quad q_p<N_p,
\tag{4}
\]
with the **even-mode** interpretation for FD-319 and all modes for FD-322. Thus these macroscopic low-frequency transport artifacts do not themselves demonstrate a false-positive low-band *depletion* comparable to the finite genuine-Farey observation in VIS-032. They only show that edge inventories and a small number of index defects do not determine total energy or fixed-mode shape.

An exact arithmetic illustration of the full-mode rule uses FD-322's two limiting Fourier coefficient profiles:
\[
b_m^+=3-4\cos(\pi m/6)+\cos(2\pi m/3),\qquad
b_m^-=4-3\cos(\pi m/6)-\cos(\pi m/2).
\]
The corresponding limiting low-band shares are
\[
F_q^+=\frac1{\pi^2}\sum_{m=1}^q\frac{(b_m^+)^2}{m^2},
\qquad
F_q^-=\frac2{3\pi^2}\sum_{m=1}^q\frac{(b_m^-)^2}{m^2}.
\tag{5}
\]
At \(q=10\), these give \(F_{10}^+\approx0.8590373\) and \(F_{10}^-\approx0.8859088\); both tend to one as \(q\to\infty\). A direct independent summation of the displayed coefficients and a cumulative-mode visualization agreed with (5). Odd coefficients must not be discarded in the unreflected case. This is a control derived from FD-322's already established formulas, not new arithmetic data.

For other sequences of permutations with \(T_p\to0\), such as FD-320's many-defect disjoint adjacent swaps, (1) is decisive **only if** an independent estimate proves \(E_p/T_p\to0\). Since FD-320 proves merely \(E_p=o(1)\) and the swap example gives an upper bound \(T_p=O(m/p)\), neither comparison of vanishing quantities nor the absolute sine error alone settles relative spectral allocation. Likewise macroscopic \(T_p\) alone does not force low-mode tightness for arbitrary rapidly oscillating displacement profiles.

## Prior art, falsification and research boundary

The norm-to-angle step and the Cauchy–Schwarz total-variation contraction are classical finite-dimensional geometry; Davis–Kahan's 1970 invariant-subspace perturbation work (already anchored in this line's SOURCES.md) is more general prior art, not a theorem needed in this proof. FD-320 supplies the source-specific exact transport decomposition, FD-318 its PNT input, FD-319/FD-322 the matched explicit control families, and VIS-032/VIS-034 the distinction between low-band share, scalar discrepancy energy and null normalization. García, *Mathematics* 14 (2026), 2543, already treats Farey gap-permutation discrepancy questions; this result does not claim novelty for general spectral stability, permutations or Franel–Landau.

The algebraic derivation is independent of rendering and finite samples. Numerical falsification of (1) under random real vectors, perturbations and orthogonal projectors found no violation; (5) was checked by direct finite cosine sums. A counterexample to this finding would need to violate FD-320's exact vector identity, orthonormality of the sine transform or the elementary angle/total-variation inequality.

**Research consequence:** the live Farey visual clue can compare *shapes* against stronger reflection-matched and unreflected controls by analyzing their exact displacement spectra, without a separate moving-cutoff error for \(T_p\gg E_p\). The remaining genuine-arithmetic test still needs a source-natural order restriction or an independently specified, transport-matched null distribution with its **own** expected total and band energies. Neither normalized transport stability nor low-mode saturation of the artificial grids proves actual Farey suppression, a stronger discrepancy bound, exceptional prime cancellation or RH.