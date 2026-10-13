---
type: theorem
research_line: xi_flow
finding_id: XF-195
status: canonical
---

# XF-195 — Adaptive Jacobi edit detection retains the linear fixed-total-noise tariff

**Evidence:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-ADVERSARIAL-TRANSCRIPT. The sharp prechosen gain-normalized Jacobi row budget of XF-194 remains sharp even for sequential, data-dependent scales when the task is only to detect *whether* an unknown-radius pair moved. A fixed total deterministic Euclidean noise budget forces and admits a linear-in-\(Q\) acquisition cost. With a fixed per-row normalized noise bound, arbitrarily remote edits cannot be detected uniformly, regardless of adaptivity.

## Exact observation and decision model

Fix \(\alpha>0\), \(0<\tau_0\le1/4\), and \(\sigma>0\). Retain the complete one-pair Jacobi defects \(J_{p,\tau}\), the holomorphic scales \(x_r=(\alpha/r^2+i/r)/\pi\) for \(r>0\), and the **source-independent** row gain \(G_r=\max\{1,|x_r|^{-1/2}\}\) of XF-192--XF-194. Put
\[
F_{p,\tau}(r)=G_r^{-1}J_{p,\tau}(x_r),\qquad
I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4].
\tag{1}
\]
The null is the unchanged reference, \(F_\varnothing(r)=0\). An alternative has exactly one unknown active integer radius \(p\in[P,Q]\) and some unknown \(\tau\in I_{\tau_0}\); all other atoms remain fixed.

A deterministic adaptive detector chooses \(r_j>0\) as a function of the preceding complex observations \(y_1,\ldots,y_{j-1}\), may stop early, and must decide null versus alternative correctly in every admissible case. On the actually queried scales,
\[
y_j=F(r_j)+e_j,\qquad \sum_j|e_j|^2\le\sigma^2.
\tag{2}
\]
The adversary may choose errors after query scales are revealed, subject to this **single total** bound; the detector knows \(\alpha,\tau_0,\sigma,P,Q\), not \(p\) or \(\tau\). Let \(M_{\rm ad}(\sigma;P,Q)\) be the least worst-case number of observations for deterministic perfect detection, with no requirement that scales be distinct.

For every fixed \(\alpha,\tau_0,\sigma\) there are \(P_0\) and constants \(0<c<C<\infty\), depending only on these parameters, such that for all integers \(Q\ge P\ge P_0\),
\[
\boxed{\qquad cQ\ \le\ M_{\rm ad}(\sigma;P,Q)\ \le\ CQ.\qquad}
\tag{3}
\]
The upper detector is nonadaptive, uses distinct scales, and **does not require an oracle revealing \(p\)**. Its output is a binary edit/no-edit decision, not the unknown radius or displacement.

## Adaptive lower bound: an admissible zero transcript

The all-scale single-row ceiling in XF-192, equation (17), gives a finite \(A_\alpha\) such that
\[
\sup_{r>0,\,|\tau|\le1/4}|F_{p,\tau}(r)|
\le A_\alpha p^{-1/2}\qquad(p\ge1).
\tag{4}
\]
Run any proposed \(k\)-query detector on the null with zero errors. Its observed transcript is identically zero, so the selected scales \(r_1,\ldots,r_m\), \(m\le k\), are fixed. Instead take \(p=Q\), \(\tau=\tau_0\), and set, on the same sequential queries,
\[
e_j=-F_{Q,\tau_0}(r_j).
\tag{5}
\]
By (4), \(\sum_{j=1}^{m}|e_j|^2\le A_\alpha^2m/Q\le A_\alpha^2k/Q\). If \(k\le\sigma^2Q/A_\alpha^2\), (5) is admissible and reproduces exactly the null's zero transcript, including every subsequent adaptive scale choice and stopping decision. A detector cannot correctly give different answers to the same data. Hence \(M_{\rm ad}>\sigma^2Q/A_\alpha^2\) (in particular (3) holds with \(c=\sigma^2/(2A_\alpha^2)\)).

This is a causal error construction: at step \(j\) it uses only the revealed \(r_j\). The obstruction persists even if the radius \(p=Q\) is announced in advance. Neither complex-profile ordering nor a prechosen probe sequence is assumed.

## Nonadaptive upper bound: norm detection needs no radius estimate

Choose any \(\gamma>2\sigma/\tau_0\). XF-194, equations (4) and (10), supplies, for sufficiently large \(P\), a bank of at most \(C_{\alpha,\gamma}Q\) **distinct prechosen** scales \(\mathcal R\) such that, for all \(p\in[P,Q]\) and \(\eta,\zeta\in[-1/4,1/4]\),
\[
\left(\sum_{r\in\mathcal R}
|F_{p,\eta}(r)-F_{p,\zeta}(r)|^2\right)^{1/2}
\ge\gamma|\eta-\zeta|.
\tag{6}
\]
Setting \(\zeta=0\), every alternative has noiseless norm at least \(\gamma\tau_0>2\sigma\), **without having to identify \(p\)**. Under (2), the observed vector has norm at most \(\sigma\) for the null and strictly greater than \(\sigma\) for an edit. Therefore
\[
\text{declare edit}\quad\Longleftrightarrow\quad
\|(y_r)_{r\in\mathcal R}\|_2>\sigma
\tag{7}
\]
is a worst-case-correct test. This proves (3). The complete same-radius finite-chord theorem XF-194 is stronger than this binary detector needs.

## A different currency: no uniformly stable per-row-noise detector

Suppose instead each normalized row independently permits \(|e_j|\le\varepsilon\), with \(\varepsilon>0\) fixed independently of \(p\). For every \(p\ge(A_\alpha/\varepsilon)^2\), the alternative \(F_{p,\tau_0}\) can be canceled **at every possible scale** by \(e_j=-F_{p,\tau_0}(r_j)\). The null and edit have identical zero transcripts no matter how many sequential queries occur. Thus uniform nonzero-displacement detection over arbitrarily remote candidates is impossible in this per-row model. This does not conflict with (3): a total \(\ell^2\) bound is not a constant per-row budget as the number of measurements increases.

XF-193's \(\sqrt p\)-compensated rowwise-max margin is only a same-radius mathematical comparison, not a physically available unknown-\(p\) prewhitening operation. Our theorem proves neither distinct-radius **identification** nor an adaptive lower bound for every support-dependent relative precision rule or independent stochastic noise model.

## Prior art, falsification controls, and Xi-flow boundary

The zero-transcript adversary is a classical sequential decision argument. Compare Rui M. Castro, *Adaptive sensing performance lower bounds for sparse signal detection and support estimation*, *Bernoulli* 20 (2014), 2217--2246, DOI 10.3150/13-BEJ555, and Eric Price--David P. Woodruff, *Lower Bounds for Adaptive Sparse Recovery*, SODA 2013, 652--663, DOI 10.1137/1.9781611973105.47. Those papers treat different sparse/statistical observation models and do not give this result as stated. The source-specific inputs are XF-192's complete-Jacobi all-scale ceiling and XF-194's uniform nonlinear-chord bank. The precise delta beyond XF-194 is **adaptive minimax necessity** together with a **source-oracle-free binary detection** upper bound.

Adversarial checks: the null and edit share a single admissible fixed reference; every query on the zero transcript is identical in both worlds; the noise sum includes only actually requested samples; the upper guarantee holds for both signs of \(\tau\), with no support estimate. The result does not require separation of different **nonzero** edit radii, so it cannot be promoted to support identification.

Complex Jacobi defect access, row gain, and the deterministic noise law remain **mathematical observation assumptions**, not established Xi-source observables. No zero-collision exclusion, upper bound on the de Bruijn--Newman constant \(\Lambda\), or RH conclusion follows.