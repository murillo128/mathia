---
type: theorem
research_line: xi_flow
finding_id: XF-191
status: canonical
---

# XF-191 — One adaptive holomorphic Jacobi sample stably recovers a known moving atom

**Evidence classification:** EXACT-DERIVED + CLASSICAL-ONE-TONE-PHASE-SEPARATION + SOURCE-SPECIFIC-RECIPROCAL-BOUND. The \(O(m^2/N)\) observation count in XF-190 is a cost of its prescribed right-anchored Fejér bank, **not** an information-theoretic cost of resolving one known moving atom. For a known radius \(p=N+m\), one appropriately scaled complex Jacobi value has a uniform finite-chord physical-displacement modulus, for arbitrary \(m\). Conversely, any fixed compact collection of samples in the open right half-plane becomes exponentially blind as \(p\to\infty\). Both statements require the other atoms to remain fixed; neither locates an unknown atom or yields a Xi-zero or de Bruijn--Newman bound.

## Exact model and single-sample theorem

Fix \(\alpha>0\). Consider one unit-weight symmetric atom pair at \(\pm p\), \(p\ge1\), displaced to \(\pm(p+\tau)\), with \(\tau\in I=[-1/4,1/4]\). All other atoms of the reference source are fixed. Its complete Jacobi reciprocity defect *difference* is

\[
\mathcal J_{p,\tau}(x)
=2\left(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x}\right)
-2x^{-1/2}\left(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}\right),
\qquad\Re x>0,
\tag{1}
\]

using the principal square root. This is exactly the endpoint-\(m\) specialization of the XF-187/XF-190 source, where \(p=N+m\) and \(h_m=((p+\tau)^2-p^2)/R\). Other unchanged atoms disappear from the difference between candidate displacements, without requiring any approximation to the integer square lattice.

Choose the single, \(p\)-dependent complex observation point

\[
\boxed{\qquad x_p=\frac1\pi\left(\frac{\alpha}{p^2}+\frac{i}{p}\right).\qquad}
\tag{2}
\]

There exists \(P_\alpha<\infty\), depending only on \(\alpha\), such that for every \(p\ge P_\alpha\) and every \(\eta,\zeta\in I\),

\[
\boxed{\quad
|\mathcal J_{p,\eta}(x_p)-\mathcal J_{p,\zeta}(x_p)|
\ge \frac{3e^{-2\alpha}}{\pi}\,|\eta-\zeta|.
\quad}
\tag{3}
\]

The bound is independent of \(p\), hence independent of \(N\), \(m\), and all fixed background atoms. In particular, when a complex observation \(y=\mathcal J_{p,\eta}(x_p)+e\) has \(|e|\le\sigma\), every \(\widehat\eta\in I\) satisfying \(|y-\mathcal J_{p,\widehat\eta}(x_p)|\le\sigma\) obeys the deterministic feasible-fit estimate

\[
|\widehat\eta-\eta|\le\frac{2\pi e^{2\alpha}}3\,\sigma.
\tag{4}
\]

No optimizer, oracle-free location method, or physical access to the holomorphic source is asserted.

## Direct phase chord: a fixed physical displacement has order-one phase

Write the direct Gaussian contribution in (1), excluding its fixed baseline, as

\[
A_\tau=2q_\tau e^{-i\theta_\tau},\qquad
q_\tau=\exp[-\alpha(1+\tau/p)^2],\qquad
\theta_\tau=\frac{(p+\tau)^2}{p}.
\tag{5}
\]

For \(p\ge1\), \(\tau\in I\) gives \(q_\tau\ge e^{-2\alpha}\). Let \(d=|\eta-\zeta|\le1/2\) and \(v=(\theta_\eta-\theta_\zeta)/2\). The *exact* phase difference is

\[
v=(\eta-\zeta)\left(1+\frac{\eta+\zeta}{2p}\right),\qquad
\frac34d\le |v|\le\frac54d\le\frac58<\frac\pi2.
\tag{6}
\]

No derivative or small-\(d\) approximation enters. The elementary sine bound \(\sin u\ge2u/\pi\) for \(0\le u\le\pi/2\) gives \(|\sin v|\ge3d/(2\pi)\). Using the exact two-amplitude identity,

\[
\begin{aligned}
|A_\eta-A_\zeta|^2
&=4\big[(q_\eta-q_\zeta)^2
       +4q_\eta q_\zeta\sin^2v\big],\\
\therefore\qquad
|A_\eta-A_\zeta|
&\ge4\sqrt{q_\eta q_\zeta}\,|\sin v|
\ge\frac{6e^{-2\alpha}}\pi\,d .
\end{aligned}
\tag{7}
\]

Thus a single raw complex sample has a uniform *finite*, not merely infinitesimal, chord margin. It uses the order-\(1/p\) imaginary part of \(x_p\), while its positive real part is only order \(1/p^2\).

## Reciprocal Jacobi image stays exponentially below the margin

The nonconstant reciprocal contribution is

\[
B_\tau=-2x_p^{-1/2}e^{-\pi(p+\tau)^2/x_p},
\qquad
B_\tau'=4\pi(p+\tau)x_p^{-3/2}
          e^{-\pi(p+\tau)^2/x_p}.
\tag{8}
\]

For \(p\ge\max(1,\alpha)\),

\[
|x_p|\ge\frac1{\pi p},\qquad
\operatorname{Re}\frac{\pi(p+\tau)^2}{x_p}
=\frac{\pi^2\alpha(p+\tau)^2p^2}{p^2+\alpha^2}
\ge\frac{9\pi^2\alpha}{32}p^2 .
\tag{9}
\]

The lower bound uses \(p+\tau\ge3p/4\) and \(p^2/(p^2+\alpha^2)\ge1/2\). Also \(p+\tau\le5p/4\). Consequently

\[
\sup_{\tau\in I}|B_\tau'|
\le5\pi^{5/2}p^{5/2}
       \exp\!\left(-\frac{9\pi^2\alpha}{32}p^2\right).
\tag{10}
\]

Choose \(P_\alpha\ge\max(1,\alpha)\) so that the right-hand side of (10) is at most \(3e^{-2\alpha}/\pi\) for every \(p\ge P_\alpha\); such a threshold exists by Gaussian decay. Integrating \(B'\) along the real interval between \(\eta\) and \(\zeta\), then subtracting its norm from (7), proves (3). Combining (3) with two residual bounds of \(\sigma\) proves (4) by the triangle inequality. This argument is uniform for arbitrarily large \(m\): there is no bank-width factor to suppress or polynomially amplify.

## Necessity of position-adapted probing in the holomorphic category

A single complex sample is sufficient **when its scale can depend on the known atom radius**. Fix instead any nonempty compact set \(K\subset\{x\in\mathbb C:\Re x>0\}\), independent of \(p\). Both \(\Re x\) and \(\Re(1/x)\) have strictly positive minima on \(K\). Differentiating (1) in \(\tau\), bounding \(|x|\) and \(|x|^{-3/2}\) on \(K\), and using \(p+\tau\ge3p/4\), gives constants \(c_K,C_K>0\) with

\[
\boxed{\quad
\sup_{x\in K}
|\mathcal J_{p,\eta}(x)-\mathcal J_{p,\zeta}(x)|
\le C_Kp e^{-c_Kp^2}\,|\eta-\zeta|
\qquad(p\ge1).
\quad}
\tag{11}
\]

Hence no *fixed finite* collection of right-half-plane complex probes admits a \(p\)-uniform positive inverse-Lipschitz constant for a remote moving atom in the ordinary unweighted data norm. This does **not** rule out a position-adapted, growing, or boundary-approaching sampling family. The effective observation (2) approaches the imaginary boundary as \(p\to\infty\) and lies outside every such fixed compact \(K\).

## Relation to the Xi-flow corpus, prior art, and exclusions

XF-177 shows that unweighted **positive-real** Jacobi observations of a fixed remote atom displacement are only of order \(1/p\), even after optimizing the real heat scale. There is no contradiction: the present acquisition has a nonzero imaginary heat frequency of order \(1/p\), producing an order-one phase shift, with \(\Re x_p\asymp p^{-2}\). XF-188's loss of *normalized, high-frequency Fejér-bank* nonlinear chord coercivity and XF-190's positive *raw, many-row* endpoint result are also untouched: this theorem changes both the row set and the data norm. It proves precisely that XF-190's \(M=O(m^2/N)\) samples are unnecessary for the one-known-atom fiber, not that a single sample reconstructs an \(m\)-dimensional unknown packet.

The one-tone phase and sine separation in (5)--(7) are elementary classical Fourier inversion, not a new superresolution principle. Moitra, *Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices*, STOC 2015, DOI 10.1145/2746539.2746561, and Hockmann--Kunis, *Weak Sparse Superresolution is Well-Conditioned*, SIAM J. Imaging Sci. 16 (2023), DOI 10.1137/22M1521353, are the established multi-atom context already recorded in the line's SOURCES.md; no theorem from them is used in the proof. The line-specific calculation is the **complete** complex Jacobi finite-chord bound (3), including the reciprocal image (8)--(10), and the scale-adaptivity boundary (11). No broad independent novelty claim is made.

The only moving parameter is one known physical radius, all other atom positions and weights are held fixed, the moved pair has fixed unit weight, and the observation is a complex-valued holomorphic Jacobi defect with *absolute complex noise*. The theorem neither locates unknown support, separates simultaneous moving atoms, justifies access to these complex theta/Jacobi samples from the physical Xi deformation, nor transports recovered source data to a zero-sensitive quantity. In particular it implies no bound on the de Bruijn--Newman constant \(\Lambda\) and no conclusion about RH.
