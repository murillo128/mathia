---
type: theorem
research_line: xi_flow
finding_id: XF-200
status: canonical
---

# XF-200 — Bounded smooth baselines have an inverse-square-root Jacobi alias threshold

**Evidence:** EXACT-DERIVED + CLASSICAL-DERIVATIVE-CONSTRAINED-APPROXIMATION + SOURCE-SPECIFIC-JACOBI-THRESHOLD. In XF-199's synthetic one-pair model, exact polynomial cancellation extends to a small smooth-drift budget, but a fixed positive budget eventually makes remote edits indistinguishable even from the entire permitted curve. The transition scale is \(Q^{-1/2}\), uniformly over separated candidate sets without a bound on \(Q/P\). For a singleton set there is an explicit asymptotic critical constant and sharp linear row cost at every fixed relative distance below the exact threshold. No physical Xi acquisition or zero-control theorem is asserted.

## Experiment and conclusions

Fix \(\alpha>0\), \(0<\tau_0\le1/4\), an integer \(m\ge1\), and total noise \(\sigma>0\). Let \(S\) be a known nonempty finite set of integer radii, \(P=\min S\), \(Q=\max S\). Assume \(P\) sufficiently large and successive radii separated by the factor \(\rho>2\) of XF-199. Use the complete responses
\[
\begin{aligned}
x_r&=\pi^{-1}(\alpha/r^2+i/r),\qquad G_r=\max\{1,|x_r|^{-1/2}\},\\
F_{p,\tau}(r)&=\frac{2}{G_r}
 (e^{-\pi(p+\tau)^2x_r}-e^{-\pi p^2x_r})
 -\frac{2x_r^{-1/2}}{G_r}
 (e^{-\pi(p+\tau)^2/x_r}-e^{-\pi p^2/x_r}),\\
F_\varnothing&=0,\qquad
\tau\in T=[-1/4,-\tau_0]\cup[\tau_0,1/4].
\end{aligned}
\tag{1}
\]
The square root is principal. An alternative edits exactly one symmetric unit-weight pair; all other atoms stay fixed. Restrict every query to
\[
I_S=[P,2Q],\qquad
\mathcal B_{m,L}(I_S)=\{B\in C^m(I_S;\mathbb C):\|B^{(m)}\|_\infty\le L\}.
\tag{2}
\]
Observe \(y_j=F_{p,\tau}(r_j)+B(r_j)+e_j\), with one shared \(B\) within each experiment and \(\sum_j|e_j|^2\le\sigma^2\). Competing hypotheses may choose different admissible baselines. Lower derivatives are unrestricted. The derivative budget is imposed in \(r\), **after** gain normalization.

Let \(\mathcal G_S\) contain all contrasts \(F_{p,\tau}\) against the null and \(F_{p,\tau}-F_{q,\zeta}\) with distinct \(p,q\in S\), \(\tau,\zeta\in T\). It does not contain contrasts between arbitrarily close displacements at the same support. Define
\[
L_*(S)=\frac12\min_{g\in\mathcal G_S}\|g^{(m)}\|_{C(I_S)}.
\tag{3}
\]
Then:

1. **Exact full-interval threshold.** Two different support labels (including the null) admit identical noiseless observation curves on \(I_S\) if and only if \(L\ge L_*(S)\). Equality is included.
2. **Uniform scale and robust bank.** There are constants \(c_-,c_+>0\), depending only on \(\alpha,\tau_0,m\), such that
   \[
   c_-Q^{-1/2}\le L_*(S)\le c_+Q^{-1/2}.
   \tag{4}
   \]
   If \(L\le c_-/(2\sqrt Q)\), a prechosen bank of \(O(Q)\) distinct rows identifies the null or active support under total noise \(\sigma\). Every always-correct deterministic adaptive procedure requires \(\Omega(Q)\) rows. Constants are uniform in \(S\) and \(Q/P\).
3. **Singleton critical constant.** For \(S=\{Q\}\),
   \[
   L_*(\{Q\})=\frac{\lambda_{\alpha,m,\tau_0}}{\sqrt Q}
       +O_{\alpha,m,\tau_0}(Q^{-3/2}),
   \quad
   \lambda_{\alpha,m,\tau_0}
   =\frac2{\sqrt\pi}\max_{1\le s\le2}
      s^{-2m-1/2}e^{-\alpha/s^2}\sin(\tau_0/s)>0.
   \tag{5}
   \]
   For every fixed \(0<\varepsilon<1\), if \(L\le(1-\varepsilon)L_*(\{Q\})\), detection has sharp cost \(\Theta(Q)\), with constants allowed to depend on \(\varepsilon\). At \(L=L_*\), even infinitely many noiseless queries cannot identify the label.

The multiple-support statement gives the order of the transition and an explicit sufficient subcritical range. It does not claim an optimized multiple-support constant or a uniform \(O(Q)\) theorem arbitrarily close to its exact threshold.

## Observation-class overlap and the factor two

The baseline difference class is exactly
\[
\mathcal B_{m,L}-\mathcal B_{m,L}=\mathcal B_{m,2L}.
\tag{6}
\]
One inclusion is the triangle inequality; the other writes \(b=b/2-(-b/2)\). For any finite bank \(\mathcal R\), the distance between two noiseless model classes with contrast \(g\) is therefore
\[
\inf_{b\in\mathcal B_{m,2L}}\|(g-b)|_{\mathcal R}\|_2.
\tag{7}
\]
Their full curves coincide precisely when \(g\in\mathcal B_{m,2L}\). If this holds, choosing baselines \(-g/2,+g/2\) for sources \(f_a,f_b\), where \(g=f_a-f_b\), gives the common curve \((f_a+f_b)/2\). Conversely, differentiating any full-curve equality forces \(\|g^{(m)}\|_\infty\le2L\).

The minimum in (3) is attained: the displacement sets are compact, the list of support pairs is finite, and the derivative norm is continuous in those parameters. Thus (3) is an exact alias threshold including its endpoint, not an inference from a zero asymptotic margin. The factor two in (6) is separate from the \(2\sigma\) separation needed for disjoint observation-noise balls.

## Finite differences tolerate a bounded shared drift

Write \(\Delta_h^m f(r)=\sum_{j=0}^m(-1)^{m-j}\binom mj f(r+jh)\). For \(h>0\) and a stencil contained in \(I_S\), the iterated fundamental theorem of calculus gives
\[
\Delta_h^m b(r)
=\int_{[0,h]^m}b^{(m)}(r+t_1+\cdots+t_m)\,dt_1\cdots dt_m,
\qquad |\Delta_h^m b(r)|\le2Lh^m
\tag{8}
\]
for every competing-baseline difference \(b\). This holds for complex functions; no ordered real mean-value argument is used.

Write
\[
a_\alpha=\frac{3e^{-2\alpha}}{2\pi(1+\sqrt{2\pi})},\quad
c_m=3\cdot2^{m-3}a_\alpha\tau_0,\quad
W_m=\binom{2m}{m}.
\tag{9}
\]
XF-199, (5) and (13), prove for every contrast \(g\in\mathcal G_S\), using the smaller active radius \(p\) (the sole radius for a null contrast),
\[
|\Delta_\pi^m g(r)|\ge c_m/\sqrt p\qquad(p<r<p+1).
\tag{10}
\]
All stencil nodes lie in \([p,2p]\subset I_S\) for large \(P\). These are full-Jacobi finite-chord bounds, including reciprocal terms and opposite-sign displacements. Combining (8) and (10) proves
\[
|\Delta_\pi^m(g-b)(r)|
\ge c_m/\sqrt p-2L\pi^m.
\tag{11}
\]
Equation (8) applied to \(g\) itself shows
\(\|g^{(m)}\|_\infty\ge c_m/(\pi^m\sqrt p)\).
Thus one may take \(c_-=c_m/(2\pi^m)\) in (4). If
\(L\le c_m/(4\pi^m\sqrt Q)\), (11) is at least \(c_m/(2\sqrt p)\).

For each \(p\), use \(n_p=\lceil Kp\rceil\) stencils starting at
\(r_{p,\ell}=p+\ell/(n_p+1)\), with step \(\pi\), and set
\[
K=(16\sigma\sqrt{W_m}/c_m)^2.
\tag{12}
\]
Their row coordinates are all distinct, as in XF-199. The binomial stencil vectors on disjoint tuples have squared norm \(W_m\) and disjoint row support. Hence every admissible \(b\) satisfies
\[
\|(g-b)|_{\mathcal R}\|_2^2
\ge\frac1{W_m}\sum_{\ell=1}^{n_p}
 |\Delta_\pi^m(g-b)(r_{p,\ell})|^2
\ge\frac{c_m^2 n_p}{4W_mp}\ge64\sigma^2.
\tag{13}
\]
This is a bound against **every** smooth drift, not polynomial projection used as if the drift were absent. A feasible model fit has the correct support, since distinct support classes are separated by at least \(8\sigma\). Geometric separation yields
\(M=(m+1)\sum_p n_p\le(m+1)(K+1)\rho Q/(\rho-1)\).

The lower row bound uses the admissible subclass \(B=0\). XF-192's all-scale ceiling \(|F_{Q,\tau}(r)|\le A_\alpha/\sqrt Q\) lets an adversary reproduce the null zero transcript for an adaptive policy using errors \(-F_{Q,\tau_0}(r_j)\), at squared cost at most \(A_\alpha^2M/Q\). For \(M\le\sigma^2Q/A_\alpha^2\), detection is impossible.

## Full-Jacobi derivative control on the entire allowed interval

For every fixed nonnegative integer \(k\),
\[
\sup_{r\ge P_0,\,|\tau|\le1/4}|\partial_r^k F_{p,\tau}(r)|
\le C_{\alpha,k}p^{-1/2},\qquad p\ge P_0.
\tag{14}
\]
Choose \(P_0\ge\max(1,\alpha)\) sufficiently large that \(G_r=|x_r|^{-1/2}\) throughout. The direct term is the difference of
\[
\frac{2}{\sqrt{\pi r}}(1+\alpha^2/r^2)^{1/4}
 e^{-\alpha a^2/r^2-ia^2/r},\qquad a=p+\tau\text{ or }p.
\tag{15}
\]
Repeated differentiation bounds each term by
\(C_{\alpha,k}r^{-1/2}(1+(p/r)^{2k})e^{-c_\alpha(p/r)^2}\).
Indeed each exponent derivative of order \(j\ge1\) is bounded by a constant times \((p/r)^2r^{1-j}\), and prefactor derivatives cost powers of \(r^{-1}\). With \(u=p/r\), the last bound is \(p^{-1/2}\) times a bounded polynomial-Gaussian function of \(u\).

For the reciprocal term set
\[
U(r)=x_r^{-1/2}/|x_r|^{-1/2},\qquad
w(r)=\pi/x_r=\pi^2\left(\alpha-ir-\frac{\alpha^2}{\alpha+ir}\right).
\tag{16}
\]
Then \(|U|=1\), all fixed-order derivatives of \(U\) are bounded for \(r\ge P_0\), \(\Re w\ge\pi^2\alpha/2\), and all positive-order derivatives of \(w\) are bounded there. The full reciprocal term is
\(-2U(r)(e^{-(p+\tau)^2w(r)}-e^{-p^2w(r)})\).
Its \(k\)th derivative is bounded by
\[
C_{\alpha,k}(1+p)^{2k}e^{-9\pi^2\alpha p^2/32},
\tag{17}
\]
uniformly over the **entire** half-line \(r\ge P_0\). This controls the rapid reciprocal phase rather than dropping it. Equations (15)--(17) prove (14).

Taking the contrast \(F_{Q,\tau_0}\) in (3) gives the upper bound in (4), for example \(c_+=C_{\alpha,m}/2\). The alias construction uses \(\pm F_{Q,\tau_0}/2\) on all of \([P,2Q]\), so it covers arbitrary adaptive queries, with no hidden finite-bank interpolation or range cutoff.

## Singleton asymptotics and the full fixed-fraction subcritical regime

Let \(p=Q\), \(r=Qs\), \(1\le s\le2\). The direct term has the exact form
\[
Q^{-1/2}e^{-iQ/s}A_{Q,\tau}(s),\qquad
A_{Q,\tau}(s)=\frac{2e^{-\alpha/s^2}}{\sqrt{\pi s}}
 (1+\alpha^2/(Q^2s^2))^{1/4}
 \left(e^{-(2Q\tau+\tau^2)(\alpha/(Q^2s^2)+i/(Qs))}-1\right).
\tag{18}
\]
Uniformly for \(|\tau|\le1/4\), this envelope differs in every fixed \(C^k[1,2]\) norm by \(O(Q^{-1})\) from
\[
A_\tau(s)=\frac{2e^{-\alpha/s^2}}{\sqrt{\pi s}}(e^{-2i\tau/s}-1).
\tag{19}
\]
Applying \(\partial_r=Q^{-1}\partial_s\) repeatedly to (18), the envelope recurrence is \(E\mapsto(i/s^2)E+Q^{-1}E'\). With (17) this proves
\[
\partial_r^m F_{Q,\tau}(Qs)
=Q^{-1/2}e^{-iQ/s}(i/s^2)^m A_\tau(s)+O(Q^{-3/2}).
\tag{20}
\]
The modulus of its leading coefficient is
\[
\frac4{\sqrt\pi}s^{-2m-1/2}e^{-\alpha/s^2}|\sin(\tau/s)|.
\tag{21}
\]
On the allowed ranges, \(|\sin(\tau/s)|\) is increasing in \(|\tau|\). Taking the supremum in \(s\), then the minimum over \(T\), and retaining the uniform error proves (5). The exact finite-\(Q\) minimizing displacement need not be asserted to equal \(\pm\tau_0\).

For the robust assertion fix \(\varepsilon>0\) and let \(s_*\) maximize (5). At \(r_*=Qs_*\), equations (20)--(21) imply uniformly over all allowed \(\tau\)
\[
|F_{Q,\tau}^{(m)}(r_*)|\ge2L_*(\{Q\})-O(Q^{-3/2}).
\tag{22}
\]
Choose a small fixed step \(h>0\), depending on \(\varepsilon,\alpha,m,\tau_0\). Put the base nodes in an interval of width \(h/2\) near \(r_*\), shifted inward when \(s_*=1\) or \(2\), so every length-\(mh\) stencil remains inside \([Q,2Q]\) and within \((2m+2)h\) of \(r_*\). By (14) for order \(m+1\) and the integral formula (8),
\[
\left|h^{-m}\Delta_h^m F_{Q,\tau}(r)-F_{Q,\tau}^{(m)}(r_*)\right|
\le C_{\alpha,m}(2m+2)h/\sqrt Q.
\tag{23}
\]
First choose \(h\) small and then \(Q\) large. The errors in (22)--(23) total at most \(\varepsilon L_*\). Subtracting the baseline allowance \(2L\) gives, whenever \(L\le(1-\varepsilon)L_*\),
\[
|\Delta_h^m(F_{Q,\tau}-b)(r)|
\ge h^m\varepsilon L_*\ge
 \frac{h^m\varepsilon\lambda_{\alpha,m,\tau_0}}{2\sqrt Q}.
\tag{24}
\]
Use \(n=\lceil K_\varepsilon Q\rceil\) distinct bases in that interval. The \(m+1\) clusters are disjoint since their width is less than \(h\). The same binomial-vector argument as (13), with sufficiently large fixed \(K_\varepsilon\), gives class separation \(8\sigma\) using \((m+1)n=O(Q)\) rows. This includes endpoint maximizers; no external query beyond \([Q,2Q]\) is needed. The zero-baseline lower bound again proves sharpness.

## Prior art, audit controls, and consequence

The derivative-constrained approximation class and finite-difference integral certificate are classical. Carl de Boor, *Divided Differences* (2005), §9, records the Genocchi integral representation used in (8). Mironenko, *Uniform approximation by perfect splines* (2017; translation 2018), studies the broader real uniform-approximation problem with a bounded highest derivative. Wiens, *Robust discrimination designs* (2009), studies discrimination between model neighbourhoods in a different stochastic setting. These sources delimit the general machinery, not the full-Jacobi asymptotic constant or this total-noise row theorem. The Master clue's authorized AF-572 source supplied the model-class-overlap question; its real ordered prime jets and small-window equality proof are not used here. Equations (16)--(24) are the destination-specific argument.

The change from XF-199 is material: an unrestricted exact polynomial remains removable, but a small nonpolynomial derivative budget must shrink with the most remote candidate. Increasing the number of rows cannot repair actual overlap of source-plus-baseline classes. For separated sets the scale \(L\sqrt Q\) needs no additional power of \(P\) or of the support range. Singleton criticality has the exact definition (3) and the expansion (5); setting \(L=\lambda/\sqrt Q\) alone does **not** decide which side of the finite-\(Q\) threshold one occupies.

Controls include two separate factors of two (baseline differences and noise balls), the binomial norm \(W_m\), derivatives of the reciprocal phase, inward stencils at interval endpoints, and compactness for the attained critical alias. Exact integer checks of polynomial annihilation and \(\sum_j\binom mj^2=W_m\) for \(m=1,\ldots,6\) passed. A scratch complex Taylor-jet check of (20), including the reciprocal expression, at \(\alpha\in\{0.2,1,10\}\), \(m\in\{1,2,3\}\), \(Q\in\{128,512,2048\}\), \(s\in\{1,1.2,1.6,2\}\), and \(\tau\in\{-0.25,-0.1,0.1,0.25\}\) was consistent with the proved error order; it is a floating-point audit, not evidence replacing the uniform proof or the exponentially small reciprocal bound.

The result identifies support labels, not exact displacement under a nonzero systematic budget. The assumed fixed total noise and arbitrarily fine distinct scale placement matter. No claim covers independent per-row noise, growing \(m\), close supports, multiple edits, unknown weights, a baseline imposed before gain, or acquisition outside the stated interval. A smooth-calibration bound supplied by an actual Xi interface, and a subsequent zero-sensitive estimate excluding positive transition time, both remain missing. This finding gives neither an upper bound on the de Bruijn–Newman constant nor an RH implication.
