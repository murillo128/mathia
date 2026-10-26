# VIS-465 — capped variation tariff for low-band Farey excursion transport

## Exact claim and evidence

Fix an integer \(N\ge2\) and a nonzero real vector \(v=(v_1,\ldots,v_{N-1})\). Set \(v_0=v_N=0\), and define its endpoint-inclusive discrete total variation, energy and dimensionless roughness by
\[
V(v)=\sum_{j=1}^{N}|v_j-v_{j-1}|,\qquad
T(v)=\sum_{j=1}^{N-1}v_j^2>0,\qquad
\mathcal R_N(v)=\frac{N V(v)^2}{T(v)}.
\]
For the orthonormal Dirichlet sine coefficients
\(\widehat v_m=\sqrt{2/N}\sum_{j=1}^{N-1}v_j\sin(\pi m j/N)\), let
\(F_{\le q}(v)=T(v)^{-1}\sum_{m=1}^q|\widehat v_m|^2\),
where \(1\le q<N\). Define the nonnegative Abel majorant
\[
B_q(v)=\frac{V(v)^2}{2NT(v)}
 \sum_{m=q+1}^{N-1}\csc^2\!\left(\frac{\pi m}{2N}\right).
\]
Then **without any reflection, block count or asymptotic hypothesis**,
\[
\boxed{\quad
1-F_{\le q}(v)
\le \min\{1,B_q(v)\}
\le \min\left\{1,\frac{\mathcal R_N(v)}{2q}\right\}.
\quad} \tag{1}
\]
The uncapped majorant need not be at most one. The two independently
proved facts are \(1-F_{\le q}(v)\le B_q(v)\) and
\(1-F_{\le q}(v)\le1\); neither asserts \(B_q(v)\le1\).
The empty sum at \(q=N-1\) is zero.

For the actual denominator-\(p\) Farey excursion permutation of FD-320, write \(D_p^\sigma=P_\sigma D_p+v_p^\sigma\), \(E_p=\|D_p\|_2^2=o(1)\), \(T_p=\|v_p^\sigma\|_2^2\), and \(\mathcal R_p=\mathcal R_{N_p}(v_p^\sigma)\). Whenever \(T_p>0\) and \(D_p^\sigma\ne0\), VIS-447 and (1) imply
\[
\boxed{\quad
1-F_{\le q}(D_p^\sigma)
\le \min\left\{1,\frac{\mathcal R_p}{2q}\right\}
 +\min\left\{1,\sqrt{\frac{E_p}{T_p}}\right\}.
\quad} \tag{2}
\]
Thus \(E_p/T_p\to0\) and \(\mathcal R_p=o(q_p)\) suffice for \(F_{\le q_p}(D_p^\sigma)\to1\), for any divergent cutoff \(q_p<N_p\). Conversely, if \(F_{\le q}(D_p^\sigma)\le1-\eta\) with \(0<\eta\le1\) and \(\sqrt{E_p/T_p}<\eta\), then necessarily
\[
\boxed{\quad
\mathcal R_p\ge 2q\left(\eta-\sqrt{E_p/T_p}\right).
\quad} \tag{3}
\]
The relative-energy gate is a sufficient transfer condition: absolute smallness of the original Farey discrepancy alone need not control the normalized spectrum of vanishing transport.

**Evidence/status:** EXACT-DERIVED + CLASSICAL BOUNDED-VARIATION FOURIER DECAY + FD-320/VIS-447 FAREY SPECIALIZATION + NECESSARY ROUGHNESS GATE. No novel general Fourier/BV theorem and no arithmetic or RH implication are claimed.

## Abel summation and the finite sine-tail estimate

For \(\theta=\pi m/N\) set \(G_m=\sum_{j=1}^{N-1}v_je^{ij\theta}\). The exact finite summation-by-parts identity with the zero boundary values is
\[
(1-e^{i\theta})G_m
=\sum_{j=1}^{N}(v_j-v_{j-1})e^{ij\theta}.
\]
Consequently
\[
|\widehat v_m|
=\sqrt{\frac2N}|\operatorname{Im}G_m|
\le\sqrt{\frac2N}\,\frac{V(v)}{2\sin(\pi m/(2N))}.
\]
Summing the coefficient bounds and using Dirichlet Parseval gives
\(1-F_{\le q}(v)\le B_q(v)\). Parseval also gives
\(1-F_{\le q}(v)\le1\), so their minimum is the first inequality
in (1). Since \(0<\pi m/(2N)<\pi/2\), concavity gives
\(\sin(\pi m/(2N))\ge m/N\); also
\(\sum_{m=q+1}^{\infty}m^{-2}\le1/q\).
These show
\[
\sum_{m>q}\frac{|\widehat v_m|^2}{T(v)}
\le\frac{NV(v)^2}{2T(v)}\sum_{m>q}\frac1{m^2}
\le\frac{\mathcal R_N(v)}{2q}.
\]
The same calculation bounds the majorant itself by
\(B_q(v)\le\mathcal R_N(v)/(2q)\). Monotonicity of
\(x\mapsto\min\{1,x\}\) now proves the second inequality in (1).
No continuum approximation, small-angle replacement, randomness or image
measurement is used in the proof.

The cap is essential even at the smallest nonempty tail. For
\(N=3\), \(v=(1,-1)\) and \(q=1\),
\[
V=4,\quad T=2,\quad \mathcal R_3=24,\quad
\widehat v_1=0,\quad\widehat v_2=\sqrt2.
\]
Thus
\[
1-F_{\le1}=1,\qquad
B_1=\frac{16}{12}\csc^2(\pi/3)=\frac{16}{9}>1,
\qquad \min\{1,B_1\}=1.
\]
This exact counterexample excludes any universal comparison of the
uncapped \(B_q\) with the probability ceiling, while attaining equality
in the capped tail bound. Scaling by any nonzero real constant, changing
the global sign, or reversing rank order leaves \(V^2/T\) and the
normalized sine energies unchanged, so the distinction is not an
amplitude or orientation artifact.

VIS-447 bounds the total-variation distance between the normalized sine energy distributions of \(D_p^\sigma\) and \(v_p^\sigma\) by \(\min\{1,\sqrt{E_p/T_p}\}\), simultaneously for all mode subsets. Apply it to the complementary high band \(m>q\) to obtain (2). If the observed high-band share is at least \(\eta\), rearrange its upper bound to obtain (3). No direct estimate of \(E_p/T_p\) is hidden in the roughness statistic.

## Exact block formula and two matched Farey controls

FD-320's transport is constant on each reordered excursion. With
\[
c_t=U_{\sigma(t)}-U_t^\sigma,\qquad
U_j=\sum_{i<j}\left(\frac{\ell_i}{N_p}-\frac1p\right),\qquad
U_t^\sigma=\sum_{s<t}\left(\frac{\ell_{\sigma(s)}}{N_p}-\frac1p\right),
\]
and positive block lengths \(\ell_{\sigma(t)}\), its complete rank-variation is exactly
\[
\boxed{\quad
V(v_p^\sigma)=|c_1|+
  \sum_{t=1}^{p-3}|c_{t+1}-c_t|+|c_{p-2}|,
\qquad
T_p=\sum_{t=1}^{p-2}\ell_{\sigma(t)}c_t^2.
\quad} \tag{4}
\]
Here rank 1 and the artificial endpoint rank \(N_p\) have zero displacement. Formula (4) is determined entirely by the excursion gap counts and their permutation. It does not ask whether the altered Hall–Shiu stitches are close to integers; stitch defects and variation are different summaries of ordering.

For FD-319's reflected four-defect exchange, the two nonzero steps are \(+1/(2p)\) and \(-1/(2p)\). Hence \(V=2/p\), \(T_p=(N_p-4)/(4p^2)\), and
\[
\mathcal R_p=\frac{16N_p}{N_p-4}\longrightarrow16. \tag{5}
\]
For FD-322's **unreflected** three-positive-near-one-defect exchange, \(v\) takes successive values \(w_A,-w_B,0\). Its exact limiting rank jumps give \(pV\to4/3\) in both prime congruence classes. Using \(N_p/p^2\to3/\pi^2\) and FD-322's two transport limits,
\[
\mathcal R_p\longrightarrow
\begin{cases}
32,&p\equiv1\pmod6,\\
64/3,&p\equiv5\pmod6.
\end{cases} \tag{6}
\]
Both families therefore retain asymptotically all normalized sine energy below *every divergent full-mode cutoff*, without first computing their fixed sine coefficients. This recovers a consequence of FD-319/FD-322 through an independently visible **rank-order smoothness** mechanism. It also extends the deduction to any further excursion permutation family satisfying the two quantitative conditions in (2), including families with an unbounded number of stitch defects.

For reflection-symmetric paths the odd sine coefficients vanish. VIS-032/VIS-034 index their band by the first \(q\) **even** modes \(m=2,4,\ldots,2q\); that share is \(F_{\le2q}\), not \(F_{\le q}\). In this special case (2) has \(\mathcal R_p/(4q)\) in place of \(\mathcal R_p/(2q)\). For FD-322, which does not preserve reflection, use the **full** sine basis and a newly computed null-specific band expectation.

## Falsification, geometric view and scope

The exact two-coordinate counterexample above is the decisive check on
where the cap belongs. Independent floating-point falsification evaluated
all nonzero vectors in \(\{-1,0,1\}^{N-1}\) for \(2\le N\le9\)
and every cutoff: 73,776 vector/cutoff cases. Direct sine-matrix
multiplication agreed with Parseval, and the largest excess over either
corrected capped inequality was below \(7\cdot10^{-16}\). Another
62,592 vector/cutoff cases used 128 standard Gaussian vectors at each
\(N\in\{16,31,64,127,256\}\), NumPy PCG64 seed 448465, and an
orthonormal type-I discrete sine transform; no violation exceeded
\(2\cdot10^{-12}\). These finite checks supplement the algebraic proof;
they do not establish a universal inequality by sampling.

Exact rational Farey grids at primes 101 and 211 independently supplied
excursion gap counts, the reflected FD-319 permutation, the unreflected
FD-322 permutation, and one complete-excursion random permutation per
prime, continuing the same PCG64 stream after the Gaussian checks and
processing the primes in ascending order. The transported vector, its exact rational variation/energy and
its independently reconstructed grid discrepancy satisfied the block
identity to floating-point precision. All full-mode cutoffs obeyed the
capped transport bound and (2). At \(p=211\), \(N_p=13624\), the
reflected transport has \(\mathcal R_p\approx16.00470\) and
\(F_{\le100}\approx0.9921822\); the unreflected transport has
\(\mathcal R_p\approx31.99086\) and
\(F_{\le100}\approx0.9825441\).

The paired [probability-cap visualization](../visualizations/sine-tail-probability-cap.md)
shows the exact two-coordinate family and the reflected finite Farey
transport. It records the mathematical construction and rendering
parameters; the picture is supporting context, not the proof.

The \(O(m^{-1})\) bounded-variation Fourier coefficient estimate is classical; compare Taibleson (1967) and [Wu (1993)](https://www.ams.org/proc/1993-117-03/S0002-9939-1993-1150658-3/), anchored in this line's SOURCES.md. Equation (1) is its elementary exact discrete Dirichlet-sine analogue. FD-320 provides the source-specific block decomposition and PNT-assisted \(E_p=o(1)\), while VIS-447 supplies the normalized full-spectrum transfer. The contribution here is the **variation-to-band quantitative test** on exact excursion transport, not a new harmonic-analysis theorem. VIS-032/VIS-034 supply the reflection-null normalizations that motivate the depletion question.

This is a **one-sided** smoothness criterion, not a spectral classification: large \(\mathcal R_p\) allows, but does not force, high-frequency allocation, and it can overestimate oscillation through cancellation. A sublinear \(q\) alone does not guarantee the result when \(\mathcal R_p\) grows. Near-zero transport requires an independently proved \(E_p/T_p\) estimate. Genuine Farey order corresponds to zero permutation transport, so neither (2) nor (3) constrains its actual spectral allocation. A null-normalized ratio \(S_q=F_{\le q}/f_{\rm null}(q)\) additionally depends on that null's own expected spectral fraction; a false-positive claim cannot borrow the same-gap null denominator. No improved Franel–Landau bound, exceptional-height selector, or RH consequence follows.

**Research consequence:** the accepted reflection-/transport-matched Farey clue now has a concrete additional control: compute \(\mathcal R_p\) from the exact block changes (4), verify the denominator gate \(E_p/T_p\), and compare it against the frozen cutoff \(q\). Any artificial excursion null satisfying both \(E_p/T_p\to0\) and \(\mathcal R_p/q\to0\) is incapable of reproducing persistent low-band depletion; a transport-dominated counterexample with low-band share bounded below one must have rank-variation roughness at least of order \(q\). A genuinely discriminating arithmetic test still requires a source-natural null and its independently normalized expected spectrum.
