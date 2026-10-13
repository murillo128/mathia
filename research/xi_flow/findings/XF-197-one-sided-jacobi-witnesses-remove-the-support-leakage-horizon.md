---
type: theorem
research_line: xi_flow
finding_id: XF-197
status: canonical
---

# XF-197 — One-sided Jacobi witnesses identify separated radii without a leakage horizon

**Evidence:** EXACT-DERIVED + SOURCE-SPECIFIC-ONE-SIDED-SEPARATION + CLASSICAL-ROBUST-DECODING. For the full gain-normalized Jacobi one-atom defects of XF-192--XF-195, a multiplicatively separated *known* candidate set admits robust **unknown-radius support identification** at the sharp fixed-total Euclidean-noise cost \(\Theta(Q)\), with **no upper restriction on \(Q/P\)**. The formerly imposed \(\log Q\lesssim P^2\) cutoff resulted from requiring the *larger* radius's matched rows to distinguish a very small off-target atom. Pairwise identification needs only the **smaller** radius's block, on which the larger atom's reciprocal image is exponentially suppressed. This is a synthetic inverse-Jacobi result, not a theorem about Xi zero motion.

## Observation model and theorem

Fix \(\alpha>0\), \(0<\tau_0\le1/4\), \(\sigma>0\), and
\[
I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4].
\]
For an integer \(p\ge1\), a real displacement \(\tau\in[-1/4,1/4]\), and \(r>0\), use the **complete**, not direct-only, pair defect
\[
J_{p,\tau}(x)
 =2(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x})
 -2x^{-1/2}(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}),
\quad \Re x>0,
\tag{1}
\]
with the principal square root, and its source-independent gain-normalized observation
\[
x_r=\pi^{-1}(\alpha/r^2+i/r),\qquad
G_r=\max\{1,|x_r|^{-1/2}\},\qquad
F_{p,\tau}(r)=J_{p,\tau}(x_r)/G_r.
\tag{2}
\]
The null is \(F_\varnothing=0\); an alternative moves **exactly one** symmetric unit-weight atom pair at an unknown radius \(p\) by an unknown nonzero \(\tau\in I_{\tau_0}\). All other source atoms remain fixed. At a finite prechosen bank \(\mathcal R\) of distinct positive real scales, data are \((F_{p,\tau}(r))_{r\in\mathcal R}+e\) with a **single total deterministic** budget \(\|e\|_2\le\sigma\).

There exist \(P_0=P_0(\alpha,\tau_0)\), a factor \(\rho=\rho(\alpha,\tau_0)>2\), and constants \(0<c<C<\infty\) depending on \(\alpha,\tau_0,\sigma\), such that for **every** nonempty finite set \(S\subset\mathbb Z\) with \(P=\min S\ge P_0\), \(Q=\max S\), and consecutive members separated by a factor at least \(\rho\), the following hold **without any bound on \(Q/P\)**:

1. A bank \(\mathcal R\) of at most \(CQ\) distinct prechosen scales permits perfect worst-case identification of the unknown active radius \(p\in S\), or of the null, under the stated total noise budget. Conditional on the identified radius, its displacement admits a stable finite-chord fit.
2. Any deterministic adaptive procedure which always distinguishes the null and correctly identifies the support under this same budget uses at least \(cQ\) samples in the worst case, even when repeated scales are allowed.

In particular, for this specific experiment,
\[
\boxed{M_{\rm support}(\sigma;S)=\Theta_{\alpha,\tau_0,\sigma}(Q)}
\tag{3}
\]
uniformly over separated finite \(S\), regardless of the ratio \(Q/P\).

## One-sided off-target lemma: compare only at the smaller radius

Write
\[
c_0=9\alpha/16,\quad \kappa=9\pi^2\alpha/32,\quad
A=5\,2^{3/4}/\sqrt\pi,\quad
a_\alpha=\frac{3e^{-2\alpha}}{2\pi(1+\sqrt{2\pi})}>0.
\tag{4}
\]
The complete-Jacobi matched finite-chord estimate of XF-193, equation (10), says that for all sufficiently large \(p\), all \(r\in[p,2p]\), and \(\eta,\zeta\in[-1/4,1/4]\),
\[
|F_{p,\eta}(r)-F_{p,\zeta}(r)|
 \ge a_\alpha|\eta-\zeta|p^{-1/2}.
\tag{5}
\]
In particular, for \(\tau\in I_{\tau_0}\), the matched source satisfies
\[
|F_{p,\tau}(r)|\ge a_\alpha\tau_0p^{-1/2}.
\tag{6}
\]

For an off-target radius \(q>p\), split its complete defect as \(J=D+B\), the direct and reciprocal Gaussian differences. Exact differentiation of \(D\), followed by integration over \(|\zeta|\le1/4\) and the gain inequality \(G_r\ge 2^{-1/4}\sqrt{\pi r}\) when \(r\ge\alpha\), gives
\[
\frac{|D_{q,\zeta}(x_r)|}{G_r}
\le A|\zeta|\,q\,r^{-3/2}\exp[-c_0(q/r)^2].
\tag{7}
\]
This direct-row estimate follows from exact differentiation of (1); the all-scale Gaussian bounds are consistent with XF-192. For \(r\ge\alpha\), \(\pi\Re(1/x_r)\ge\pi^2\alpha/2\) and \(q+\zeta\ge3q/4\); bounding the **finite reciprocal amplitudes**, not their oscillatory derivatives, yields
\[
\frac{|B_{q,\zeta}(x_r)|}{G_r}\le4e^{-\kappa q^2}.
\tag{8}
\]
Consequently, for \(s=q/p>1\), \(p\ge\alpha\), and any \(r\in[p,2p]\),
\[
\sqrt p\,|F_{q,\zeta}(r)|
\le\frac A4s e^{-c_0s^2/4}
       +4\sqrt p\,e^{-\kappa q^2}.
\tag{9}
\]
Choose \(\rho>2\) sufficiently large that
\[
\frac A4\sup_{s\ge\rho}s e^{-c_0s^2/4}
\le a_\alpha\tau_0/4.
\tag{10}
\]
Since \(q\ge\rho p\), the reciprocal error in (9) satisfies
\[
4\sqrt p\,e^{-\kappa q^2}
\le4\sqrt p\,e^{-\kappa\rho^2p^2}
\le a_\alpha\tau_0/4
\quad(p\ge P_0),
\tag{11}
\]
after enlarging \(P_0\) depending only on \(\alpha,\tau_0\). Critically, this bound depends on the **smaller radius \(p\)** and never on \(Q\).

Equations (6), (9)--(11) establish, for all \(q\ge\rho p\), every \(r\in[p,2p]\), and all allowed nonzero \(\tau,\zeta\),
\[
|F_{q,\zeta}(r)|\le\frac{a_\alpha\tau_0}{2\sqrt p},
\qquad
\boxed{|F_{p,\tau}(r)-F_{q,\zeta}(r)|
  \ge\frac{a_\alpha\tau_0}{2\sqrt p}}.
\tag{12}
\]
The two-source inequality is **asymmetric in its proof but symmetric in its conclusion**: for any distinct candidate radii, use the matched block of their minimum. It does not assert that the larger radius's matched block dominates the smaller source; that stronger and unnecessary demand is precisely where the earlier reciprocal leakage horizon entered.

## Robust bank, decoder, and sharp lower bound

For each \(p\in S\), choose
\[
n_p=\left\lceil\left(\frac{8\sigma}{a_\alpha\tau_0}\right)^2p\right\rceil,
\quad
r_{p,\ell}=p\left(1+\frac{\ell}{3(n_p+1)}\right),
\quad1\le\ell\le n_p.
\tag{13}
\]
Each block lies in \((p,4p/3)\). Since successive candidate radii differ by more than a factor \(2\), all blocks and all rows are distinct; the design needs no knowledge of the active \(p\) or \(\tau\).

Equation (6), summed over the block of an active \(p\), gives
\[
\|F_{p,\tau}|_{\mathcal R}\|_2
\ge a_\alpha\tau_0\sqrt{n_p/p}\ge8\sigma.
\tag{14}
\]
For distinct \(p,q\in S\), apply (12) on the block belonging to \(m=\min(p,q)\). Its \(n_m\) matched rows give, **independently of how large the other radius is**,
\[
\|F_{p,\tau}|_{\mathcal R}-F_{q,\zeta}|_{\mathcal R}\|_2
\ge(a_\alpha\tau_0/2)\sqrt{n_m/m}\ge4\sigma.
\tag{15}
\]
Within each fixed radius, the full-chord estimate (5) also gives
\[
\|F_{p,\eta}|_{\mathcal R}-F_{p,\zeta}|_{\mathcal R}\|_2
\ge a_\alpha\sqrt{n_p/p}\,|\eta-\zeta|.
\tag{16}
\]
Thus a nearest-model fit among the null and the curves \(F_{p,\tau}\), \(p\in S\), identifies the support: a noisy true model has residual at most \(\sigma\), but every wrong-radius model has residual at least \(3\sigma\), and the null is still farther. A feasible displacement fit on the identified radius obeys
\[
|\widehat\tau-\tau|\le
\frac{2\sigma}{a_\alpha\sqrt{n_p/p}}\le\tau_0/4.
\tag{17}
\]

Let \(K=(8\sigma/(a_\alpha\tau_0))^2\). Since \(n_p\le(K+1)p\) for integer \(p\ge1\), geometric separation implies
\[
|\mathcal R|=\sum_{p\in S}n_p
\le(K+1)\sum_{p\in S}p
\le(K+1)\frac{\rho}{\rho-1}Q.
\tag{18}
\]
This bound is valid even when \(Q\) grows faster than every exponential of \(P^2\).

For necessity, XF-192, equation (17), supplies \(A_\alpha<\infty\) with
\[
\sup_{r>0,\,|\tau|\le1/4}|F_{Q,\tau}(r)|
\le A_\alpha Q^{-1/2}.
\tag{19}
\]
Run any deterministic adaptive detector with at most \(k\) queries on the null, returning zero observations. Against the alternative \((Q,\tau_0)\), answer the same queries with causal adversarial errors \(-F_{Q,\tau_0}(r_j)\). Their total squared norm is at most \(kA_\alpha^2/Q\); if \(k\le\sigma^2Q/A_\alpha^2\), this is admissible and produces the identical zero transcript. No detector, hence no support identifier, can be correct in both cases. Taking a smaller fixed positive constant proves the \(\Omega(Q)\) half of (3), even with adaptive sampling.

## Prior art, falsification controls, and Xi boundary

The triangle-inequality witness argument and geometric sample allocation are elementary; there is no claim of a new general sparse-recovery principle. Hockmann--Kunis, *Weak Sparse Superresolution is Well-Conditioned* (SIAM J. Imaging Sci. 2023, DOI 10.1137/22M1521353), studies a **different Fourier-moment/measure metric**; Castro, *Adaptive sensing performance lower bounds for sparse signal detection and support estimation* (Bernoulli 2014, DOI 10.3150/13-BEJ555), studies a **different stochastic adaptive model**. Both are already recorded in this line's SOURCES.md. The local increment is the one-sided application of the complete-Jacobi bounds (7)--(12), removing the artificial bound \(Q\le e^{\kappa P^2}\) previously imposed by a two-sided domination argument, without new observations or a stronger noise assumption.

Falsification controls: use finite **complex** Jacobi defects, not the direct Gaussian alone; the bound on the off-target reciprocal term must use \(q\ge\rho p\), not \(q\ge P\) while testing a row matched to an arbitrary huge \(p\). No radius-dependent whitening is allowed in the data. If \(\tau_0=0\), every support shares the zero signal at \(\tau=0\) and uniform identification fails. If candidates are adjacent or insufficiently separated, (10) gives no guarantee; the theorem makes no claim for them. The total deterministic \(\ell^2\) budget is not independent per-row noise, and extremely crowded banks can demand unrealistic scale precision.

Most importantly, **holomorphic defect access and the row-gain law are assumed rather than derived from the actual Xi theta kernel**. The model has exactly one edited known-weight source pair and an already known candidate set; unrestricted sparse support, multiple edits, unknown weights, and the bridge to Xi zero collisions remain open. This result neither gives an upper bound for the de Bruijn--Newman constant nor advances RH directly.
