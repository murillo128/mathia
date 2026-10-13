# VIS-450 — conditioning on a vanishing Farey parity sector has a sharp projected-energy tariff

## Exact claim and evidence

Let \(H\) be a real finite-dimensional Hilbert space with a fixed orthonormal observation basis, let \(J\) be any subset of basis coordinates, and let \(P_J\) be its orthogonal projection. For nonzero \(P_J v\) and \(P_J y\), define the **sector-conditioned energy law**
\[
\pi_m^{\,J}(z)=\frac{|\langle z,e_m\rangle|^2}{\|P_Jz\|^2}
\quad(m\in J).
\]
Writing \(y=v+e\), the entire conditional spectral law obeys the dimension-free bound
\[
\boxed{\quad
\frac12\sum_{m\in J}|\pi_m^{\,J}(y)-\pi_m^{\,J}(v)|
\le \min\!\left\{1,\frac{\|P_Je\|}{\|P_Jv\|}\right\}
\le\min\!\left\{1,\frac{\|e\|}{\|P_Jv\|}\right\}.
\quad} \tag{1}
\]
Thus **energy inside the selected sector**, not the full-spectrum perturbation followed by division by its small mass, controls the conditional distribution. The bound is simultaneous for every subband of \(J\).

For the exact FD-320 prime-Farey excursion decomposition
\(D_p^\sigma=P_\sigma D_p+v_p^\sigma\), \(E_p=\|D_p\|^2=o(1)\),
and any sector \(J\) with \(T_{J,p}=\|\Pi_Jv_p^\sigma\|^2>0\),
\[
\boxed{\quad
\sup_{B\subseteq J}
\big|F_B^{\,J}(D_p^\sigma)-F_B^{\,J}(v_p^\sigma)\big|
\le \min\!\left\{1,\sqrt{\frac{E_p}{T_{J,p}}}\right\}
\quad} \tag{2}
\]
whenever the conditioned reconstructed law is defined; here \(\Pi_J\) denotes the corresponding Dirichlet-sine spectral projection. One may strengthen the numerator to \(\|\Pi_J P_\sigma D_p\|^2\), without making any assumption about reflection.

For the unreflected three-defect FD-323 family with fixed \((a,b)=(k,k+1)\), the limiting **even-sine** transport energy is \((3/\pi^2)e_k\), where
\[
e_k=\tfrac12\left[
\frac1{k+1}\left(1-\frac1k\right)^2+
\frac1k\left(\frac{k}{k+1}\right)^2\right]
\sim\frac1k. \tag{3}
\]
On any joint sequence of admissible primes and \(k=k(p)\) for which the **finite** even transport energy satisfies \(T_{\mathrm{even},p,k}\ge c/k\) for some fixed \(c>0\), equation (2) gives
\[
\sup_{B\subseteq 2\mathbb N}
\big|F_B^{\,\mathrm{even}}(D_{p,k}^\star)
     -F_B^{\,\mathrm{even}}(v_{p,k})\big|
\le\sqrt{\frac{kE_p}{c}}. \tag{4}
\]
Consequently \(kE_p\to0\) suffices for conditional even-spectrum transfer on **all** even-mode subsets, including cutoffs \(m\asymp k\). This replaces the stronger sufficient requirement \(k\sqrt{E_p/T_p}\to0\), or \(E_p=o(k^{-2})\) when \(T_p\asymp1\), that results from applying VIS-447 globally and dividing by the vanishing even-sector fraction. The projected condition only asks \(E_p=o(k^{-1})\), together with the stated lower bound on finite even transport energy.

**Evidence/status:** EXACT-DERIVED + CLASSICAL NORMALIZED-PROJECTION GEOMETRY + FD-320/VIS-447/VIS-449 SPECIALIZATION + SHARP INFORMATION-LOSS CONTROL. Neither a novel general perturbation theorem nor a genuine Farey spectral anomaly or an RH implication is claimed.

## Projection proof and the correct denominator

Apply the same normalized-vector argument underlying VIS-447 **after** projecting to \(J\). Put \(a=P_Jy/\|P_Jy\|\) and \(b=P_Jv/\|P_Jv\|\). In the selected orthonormal coordinates,
\[
\begin{aligned}
\frac12\sum_{m\in J}|a_m^2-b_m^2|
&\le\tfrac12\|a-b\|\|a+b\|\\
&=\sqrt{1-\langle a,b\rangle^2}
 =\sin\theta,
\end{aligned}
\]
where \(\theta\in[0,\pi/2]\) is the unoriented angle between the projected lines. The distance from \(P_Jv\) to the line through \(P_Jy\) equals \(\|P_Jv\|\sin\theta\) and is at most
\(\|P_J(v-y)\|=\|P_Je\|\). This proves (1), including the automatic cap of one. Total variation equals the supremum of differences of subset probabilities, proving (2). Neither the number of selected modes nor their locations enter this proof.

The construction is fundamentally different from bounding the **unconditioned** total variation by \(\sqrt{E_p/T_p}\) and then using
\[
\left|\frac{P_y(B)}{P_y(J)}-\frac{P_v(B)}{P_v(J)}\right|
\]
with separately perturbed denominators. Such a route pays a factor of order the reciprocal sector mass; the projection argument prices the perturbation in the **square-root sector energy** instead. This difference matters when the sector's normalized mass tends to zero.

## Even-parity boundary layer of the three-defect control

VIS-449 gives the explicit continuum transport step \(g_k\), full energy
\(d_k=\int_0^1g_k(t)^2\,dt\to1\), and exact even-sine energy (3). In the FD-323 limit **with \(k\) fixed and \(p\to\infty\) along its prescribed reduced residue class**, each transport sine coefficient converges to \((\sqrt6/\pi)\int_0^1g_k(t)\sin(\pi mt)\,dt\). The total sine energy also converges, so the even-sector energy converges to
\[
T_{\mathrm{even},p,k}\longrightarrow
\frac6{\pi^2}\sum_{j\ge1}
\left(\int_0^1g_k(t)\sin(2\pi jt)\,dt\right)^2
=\frac3{\pi^2}e_k. \tag{5}
\]
The last equality uses the sine-Parseval convention in VIS-449. Since \(ke_k\to1\), a **sufficiently slow diagonal** \(k\to\infty\), with each prime chosen sufficiently large for its fixed \(k\), can guarantee \(T_{\mathrm{even},p,k}\ge c/k\), \(kE_p\to0\), and finite-transport spectral approximation at the desired \(m/k\) scale. Then (4), together with VIS-449's independently established continuum limit, transfers the conditioned even spectrum to
\[
f(x)\,dx=\frac{(1-\cos2\pi x)^2}{\pi^2x^2}\,dx
\]
for frequencies \(m/k\) in the nested/slow-diagonal sense.

Equation (5) is **not** a rate uniform in growing \(k\). The simple bound \(kE_p\to0\) alone does not imply the required finite even transport-energy lower bound, nor does it control finite-transport convergence to \(g_k\) with growing \(k\). Any specified simultaneous prime/parameter sequence must establish these independently. Also, Dirichlet's theorem supplies infinitely many primes for each **fixed** congruence class; no quantitative uniform prime-in-progressions estimate is claimed.

## Sharp generic countercontrol

Let \(o,a,b\) be mutually orthonormal observation modes, with \(o\) outside \(J\) and \(a,b\) inside \(J\). For every integer \(k\ge1\), set
\[
v_k=o+k^{-1/2}a,\qquad
y_k=v_k+k^{-1/2}b,\qquad
e_k^{\mathrm{pert}}=k^{-1/2}b.
\]
Then the perturbation is negligible globally:
\[
\frac{\|e_k^{\mathrm{pert}}\|^2}{\|v_k\|^2}=\frac1{k+1}\to0,
\qquad
\operatorname{TV}(\pi(y_k),\pi(v_k))=\frac1{k+2}\to0.
\]
Yet \(\|P_Jv_k\|^2=1/k\), and the conditioned spectra inside \(J\) are respectively \((1/2,1/2)\) and \((1,0)\); their total-variation distance is **exactly \(1/2\)** for all \(k\). Therefore global normalized spectral convergence does *not* imply convergence after conditioning on a vanishing parity sector. The sector-energy ratio in (1) captures the correct order for a universal guarantee. The witness is an abstract matched-coordinate perturbation, **not an admissible Farey excursion permutation**.

A finite numerical falsification control for the actual \((a,b)=(4,5)\) artificial reassemblies, along primes \(p=31,71,131,211,431\), checked the orthonormal discrete sine projections of the exact block displacement and the reassembled discrepancy. The conditioned even-spectrum total variations were approximately \(0.2083,0.1416,0.0982,0.0649,0.0416\), respectively, below the corresponding direct \(E_p/T_{\mathrm{even},p}\) square-root bounds. The exact theorem, not these finite calculations or an exploratory plotted comparison, establishes the result.

## Prior art, boundaries, and consequence

The normalized-vector angle inequality, orthogonal projection, spectral Parseval, and contraction of measurement outcome probabilities are elementary Hilbert-space/finite-probability geometry. Davis and Kahan, *The Rotation of Eigenvectors by a Perturbation. III*, SIAM J. Numer. Anal. **7** (1970), 1–46, and Stein and Shakarchi, *Fourier Analysis: An Introduction* (2003), already anchored in this line's SOURCES.md, delimit the perturbation and Fourier prior art; no theorem of theirs is used beyond these standard principles. FD-320 supplies the exact excursion-permutation identity, VIS-447 supplies the global all-mode baseline, and VIS-449 the **vanishing-even-sector** family and continuum density. The useful additional statement is the quantitative projected-energy tariff and its sharp failure example, not a new general Fourier theorem.

The lower bound in (4) is only a **sufficient stability gate**. Large perturbation energy inside \(J\) can leave the conditioned spectrum unchanged (for example when it is collinear with \(P_Jv\)); the toy control shows only why no universal conclusion can follow from small global energy alone. No transport estimate for the **genuine** Farey order follows, because its artificial permutation displacement is zero. In particular, these arguments neither establish the full-mode or even-conditioned null expectations of a source-natural Farey control ensemble nor improve the Franel–Landau/RH-equivalent discrepancy bound.

**Research consequence:** for the accepted near-maximal Farey parity clue, assess any conditional even-mode spectral comparison using the **finite** \(T_{\mathrm{even},p,k}\) and \(\|\Pi_{\mathrm{even}}P_\sigma D_p\|^2\), not merely the full transport \(T_p\) or a vanishing unconditional even share. The correct universal transfer condition is sector-specific, and for the slow-diagonal near-maximal family it reduces the sufficient true-Farey energy requirement by one power of \(k\).
