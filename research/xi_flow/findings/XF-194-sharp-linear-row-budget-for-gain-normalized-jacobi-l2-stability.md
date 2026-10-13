---
type: theorem
research_line: xi_flow
finding_id: XF-194
status: canonical
---

# XF-194 — Fixed-total ell-two Jacobi noise requires and admits a linear row budget

**Evidence:** EXACT-DERIVED + CLASSICAL-FRAME-ACCUMULATION + MODEL-SPECIFIC-SHARP-COUNT. The rowwise-max logarithmic scale-covering result XF-193 does **not** give a fixed-total Euclidean-noise acquisition bound without paying for response energy. For the same exact complete Jacobi defects and the same source-independent row gain, the sharp number of *prechosen distinct* complex observations needed for a uniform, unweighted ell-two *same-radius* physical-chord margin is linear in the largest admissible radius, not logarithmic.

## Observation model and sharp statement

Fix \(\alpha>0\), \(I=[-1/4,1/4]\), and the one-pair Jacobi defect
\[
J_{p,\tau}(x)=2\big(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x}\big)
-2x^{-1/2}\big(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}\big)
\quad(\Re x>0),
\tag{1}
\]
with the principal square root, exactly as in XF-192 and XF-193. For every real scale \(r>0\) use
\[
x_r=\pi^{-1}\big(\alpha r^{-2}+ir^{-1}\big),\quad
G_r=\max\{1,|x_r|^{-1/2}\},\qquad
F_{p,\tau}(r)=J_{p,\tau}(x_r)/G_r.
\tag{2}
\]
For integers \(Q\ge P\) and a finite **set of distinct prechosen** scales \(\mathcal R\subset(0,\infty)\), define
\[
\Gamma_{P,Q}(\mathcal R)
:=\inf_{\substack{p\in[P,Q]\cap\mathbb Z\\
                \eta,\zeta\in I,\ \eta\ne\zeta}}
\frac{\left(\sum_{r\in\mathcal R}
       |F_{p,\eta}(r)-F_{p,\zeta}(r)|^2\right)^{1/2}}
     {|\eta-\zeta|},
\tag{3}
\]
and let \(M_2(\gamma;P,Q)\) be the minimum cardinality of a bank with \(\Gamma_{P,Q}\ge\gamma\). The radius \(p\) is held fixed on **each chord**; the bank itself is chosen without knowing \(p\).

For every \(\gamma>0\) there are \(P_0(\alpha,\gamma)\) and positive constants \(c_{\alpha,\gamma},C_{\alpha,\gamma}\) such that for all integers \(Q\ge P\ge P_0\),
\[
\boxed{\quad
c_{\alpha,\gamma}Q\ \le\
M_2(\gamma;P,Q)\ \le\
C_{\alpha,\gamma}Q.
\quad}
\tag{4}
\]
The upper construction uses genuinely **distinct** real scales and no duplicated row or parameter-dependent rescaling. The comparison is a constant *physical* displacement margin (without the \(\sqrt p\) compensation present in XF-193). The error model is an adversarial perturbation whose **total** gain-normalized Euclidean norm is bounded independently of the number of rows.

## Necessity: a remote radius has at most order \(Q^{-1/2}\) signal per row

XF-192, equation (17), proves that some \(A_\alpha<\infty\) satisfies, uniformly for all \(r>0\), \(p\ge1\), \(\tau\in I\),
\[
|F_{p,\tau}(r)|\le A_\alpha p^{-1/2}.
\tag{5}
\]
Test \(p=Q\), \(\eta=1/4\), \(\zeta=-1/4\). Their chord has length \(d=1/2\), while (5) and the triangle inequality give for every \(r\)
\[
|F_{Q,1/4}(r)-F_{Q,-1/4}(r)|
\le2A_\alpha Q^{-1/2}.
\]
Consequently a bank of \(k\) rows obeys
\[
\Gamma_{P,Q}(\mathcal R)
\le4A_\alpha\sqrt{k/Q}.
\tag{6}
\]
If its margin is at least \(\gamma\), then
\(k\ge\gamma^2Q/(16A_\alpha^2)\). This lower bound holds for **arbitrary** choices of scales within (2), whether widely spaced, densely packed, or repeated. It makes no unsupported derivative estimate for the rapidly oscillating reciprocal phase.

## Sufficiency: allocate linearly many near-matched rows per geometric octave

XF-193, equation (10), proves that for some \(P_*(\alpha)\), every \(p\ge P_*\), \(r\in[p,2p]\), and finite chord \(\eta,\zeta\in I\),
\[
|J_{p,\eta}(x_r)-J_{p,\zeta}(x_r)|
\ge b_\alpha|\eta-\zeta|,
\qquad b_\alpha=\frac{3e^{-2\alpha}}{2\pi}.
\tag{7}
\]
At the same matched rows,
\[
G_r\le K\sqrt p,\qquad K=1+\sqrt{2\pi};
\quad
|F_{p,\eta}(r)-F_{p,\zeta}(r)|
\ge a_\alpha p^{-1/2}|\eta-\zeta|,
\quad a_\alpha=b_\alpha/K.
\tag{8}
\]
Take \(P\ge P_*(\alpha)\). Let \(s_j=P(3/2)^j\) for \(0\le j\le J=\lceil\log_{3/2}(Q/P)\rceil\). Set
\[
n_j=\left\lceil (\gamma/a_\alpha)^2s_j\right\rceil,
\qquad
r_{j,\ell}=s_j\left(1+\frac{\ell}{3(n_j+1)}\right),
\quad 1\le\ell\le n_j.
\tag{9}
\]
All rows are distinct: within each block they lie strictly between \(s_j\) and \(4s_j/3\), and the next block starts at \(3s_j/2\). Their union \(\mathcal R\) is independent of the unknown \(p\).

For every \(p\in[P,Q]\), choose the smallest \(j\) with \(s_j\ge p\). Then \(p\le s_j<(3/2)p\) (with the obvious equality at \(j=0\)), so *all* \(n_j\) rows in this block belong to \([p,2p]\). Summing just those rows and using (8) gives
\[
\left(\sum_{r\in\mathcal R}
|F_{p,\eta}(r)-F_{p,\zeta}(r)|^2\right)^{1/2}
\ge a_\alpha\sqrt{n_j/p}\,|\eta-\zeta|
\ge\gamma|\eta-\zeta|.
\tag{10}
\]
Finally the geometric sum obeys
\[
|\mathcal R|=\sum_{j=0}^{J}n_j
\le(\gamma/a_\alpha)^2\sum_{j=0}^Js_j+(J+1)
=O_{\alpha,\gamma}(Q),
\tag{11}
\]
because \((3/2)^J<(3/2)Q/P\) and \(J+1=O(Q)\) for \(P\ge1\). This proves (4), including global **finite-chord** stability rather than merely derivative sensitivity.

## Noise interpretation, prior art, and limitations

Suppose the active radius \(p\) is known when *fitting* the displacement and the observed vector is \(F_{p,\eta}|_{\mathcal R}+e\), with \(\|e\|_2\le\sigma\). Any feasible fit with residual at most \(\sigma\) obeys \(|\widehat\eta-\eta|\le2\sigma/\gamma\). The unknown \(p\) is used only in this conditional fit, not in selecting the bank. Different radii need not have separated response vectors, and the theorem **does not identify an unknown active radius**.

The \(\Theta(Q)\) count is not a new general frame-theory principle. It follows from the sharp single-row visibility ceiling in XF-192 and the matched finite-chord margin in XF-193, combined with standard Euclidean accumulation and geometric allocation. Related classical frame redundancy and the superresolution literature (Duffin--Schaeffer 1952; Moitra 2015; Aubel--Bölcskei 2019) do not by themselves establish or contradict the exact Jacobi row bounds. The mathematical delta is the **change of acquisition currency**: \(\Theta(1+\log(Q/P))\) rows suffice when the objective is a radius-compensated rowwise maximum (XF-193), whereas an absolute, fixed-total ell-two margin costs \(\Theta(Q)\) distinct rows.

This result is conditional on exact access to the complex Jacobi defect and on a fixed **total** gain-normalized \(\ell^2\) error budget. It is not an independent fixed-variance per-row noise theorem: if each row carries the same systematic error, total error grows with the number of rows. It does not rule out optimal adaptive schemes, other holomorphic probe families, unknown-radius discrimination, or actual Xi-source constraints. No Xi-zero collision exclusion, bound on the de Bruijn--Newman constant, or RH consequence follows.
