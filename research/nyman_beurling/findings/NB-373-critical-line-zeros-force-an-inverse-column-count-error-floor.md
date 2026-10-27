# NB-373 — Critical-line zeros force an inverse-column-count error floor

- **Status:** proved (classical inequality plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the continuous projected target; NB-371 and NB-372 for comparison with coefficient and range budgets
- **Classification:** LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + COLUMN-COUNT-BOUNDARY

## Claim and scope

Unbounded coefficients and arbitrarily large real dilations cannot replace a growing number of actual Nyman generators. More quantitatively, the squared error of every synthesis with at most \(J\) columns is at least \(c/J\), even for the unconditional projected target. This supplies a column-count restriction without the coefficient restrictions in NB-371 or the range restrictions in NB-372.

Use the fixed dictionary
\[
H=L^2(0,1;dx),\quad e=1,\quad
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad v>1,
\]
\[
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},\quad a\ge1,
\qquad \mathcal N=\overline{\operatorname{span}}\{g_v:v>1\}.
\]
Let \(t=P_{\mathcal N}e\). Write \(b=B(1)>0\), with the common inner factor normalized as in [NB-354](NB-354-finite-seed-real-dilation-spaces-have-an-exact-target-loss-classification.md). Then
\[
\mathcal Mt(s)=\frac{bB(s)}s,\qquad \|t\|=b,\qquad
\|e-t\|^2=1-b^2.
\tag{1}
\]
Fix any critical-line zero \(\rho=1/2+i\gamma\), of its actual multiplicity \(m\ge1\). There is a constant \(c_\rho>0\), specified below by local zeta data and independent of \(B\), such that for every integer \(J\ge1\),
\[
\boxed{\left\|t-\sum_{\nu=1}^J c_\nu A_{a_\nu}g_{v_\nu}\right\|^2
\ge\frac{c_\rho}{J}.}
\tag{2}
\]
The coefficients are arbitrary complex numbers, the seeds are arbitrary real numbers \(v_\nu>1\), and the dilations are arbitrary real numbers \(a_\nu\ge1\). No spacing, conditioning, common seed, maximal range, or coefficient-norm bound is imposed. Zero coefficients allow fewer than \(J\) columns. The same bound holds for the norm closure of this nonlinear set of syntheses.

Consequently physical error \(\varepsilon\) requires
\[
J\ge c_\rho\varepsilon^{-2}.
\tag{3}
\]
This is a necessary lower budget, not a matching upper rate. The statement neither removes the Burnol floor nor claims that the optimal squared error has order \(1/J\).

## 1. A frequency-independent interior norm inequality

If \(p\) is an exponential sum with at most \(N\ge1\) terms and arbitrary complex exponents, the classical Borwein--Erdélyi inequality gives
\[
\sup_{|u|\le r/2}|p(u)|^2
\le\frac{4N}{r}\int_{-r}^r|p(u)|^2\,du.
\tag{4}
\]
This is the \(p=2\) case of their shift-invariant-space theorem with interior margin \(r/2\). The dimension of the exponential span is at most \(N\), even after frequencies coincide. The bound does not depend on their sizes or separation.

The underlying Hilbert argument is short. On an interval of length \(d\), an orthonormal basis of a translation-invariant space of dimension \(n\) has integrated squared evaluation norm \(n\). Some point therefore has squared evaluation norm at most \(n/d\). Translating each function moves that evaluation to the center, while enlarging the integration interval to length \(2d\). Hence
\(|p(y)|^2\le(n/d)\int_{y-d}^{y+d}|p|^2\).
Taking \(d=r/2\) proves even \(2N/r\) in (4); the weaker displayed constant is retained throughout. For exponential spans all these local inner products are nondegenerate after duplicate exponents are removed.

## 2. Local zero lemma: use the approximation error in the norm estimate

Let \(z\) be a function on \([-r,r]\) satisfying
\[
\ell |u|^m\le |z(u)|\le L|u|^m,
\qquad \ell,L>0,\quad m\ge1.
\tag{5}
\]
Let \(F\) be any measurable function with \(|F(u)|=1\) almost everywhere. No continuity or phase regularity of \(F\) is assumed. For any exponential sum \(p\) of at most \(N\) terms, put
\[
E=\int_{-r}^r|F(u)-z(u)p(u)|^2\,du,
\qquad A=\int_{-r}^r|p(u)|^2\,du,
\qquad h=\frac{r}{16N}.
\tag{6}
\]
Define constants independent of \(N,p,F\):
\[
D=\frac4{\ell^2}\left(1+\frac2{2m-1}\right),\qquad
\theta=\min\{1,(L\sqrt D)^{-1/m}\}>0.
\tag{7}
\]
Then
\[
\boxed{E\ge\frac{\theta r}{32N}.}
\tag{8}
\]

To prove this, (4) implies
\[
\int_{-h}^h|p(u)|^2du
\le2h\frac{4N}{r}A=\frac A2.
\tag{9}
\]
Thus the norm outside the small central interval controls at least half of \(A\). Writing \(e_0=F-zp\), the identity \(zp=F-e_0\) and (5) give
\[
\begin{aligned}
A
&\le2\int_{h\le|u|\le r}|p(u)|^2du\\
&\le\frac4{\ell^2}
\left(\int_{h\le|u|\le r}|u|^{-2m}du
+h^{-2m}E\right)\\
&\le\frac4{\ell^2}
\left(\frac2{2m-1}h^{1-2m}+h^{-2m}E\right).
\end{aligned}
\tag{10}
\]
If \(E>h\), (8) already follows since \(\theta\le1\). Otherwise \(E\le h\), and (10) gives \(A\le D h^{1-2m}\). Returning to (4), and using \(4N/r=1/(4h)\), yields
\[
\sup_{|u|\le r/2}|p(u)|^2\le\frac D4 h^{-2m}.
\tag{11}
\]
On \(|u|\le\theta h\), which is inside that interval,
\[
|z(u)p(u)|\le\frac{L\sqrt D}{2}\theta^m\le\frac12.
\tag{12}
\]
The reverse triangle inequality therefore gives \(|F-zp|\ge1/2\) almost everywhere there. Integration proves
\(E\ge2\theta h/4=\theta r/(32N)\), as claimed.

The use of \(E\) in (10) is essential to this rate. Bounding the numerator only by the norm of the full approximant loses the singular profile \(|u|^{-m}\) that the target itself prescribes. The zero's multiplicity enters the constants but cancels out of the power \(N^{-1}\).

## 3. Apply the lemma to the actual Mellin numerator

For a finite synthesis \(w\), the exact classical Mellin identity is
\[
\mathcal Mw(s)=\frac{\zeta(s)}sP_w(s),\qquad
P_w(s)=\sum_{\nu=1}^Jc_\nu
a_\nu^{1/2-s}(v_\nu^{-1}-v_\nu^{-s}).
\tag{13}
\]
Along \(s=\rho+iu\), its numerator is
\[
P_w(\rho+iu)=\sum_{\nu=1}^Jc_\nu
\left[v_\nu^{-1}e^{-i(\gamma+u)\log a_\nu}
-v_\nu^{-1/2}e^{-i(\gamma+u)\log(a_\nu v_\nu)}\right].
\tag{14}
\]
There are at most \(2J\) real frequencies. Arbitrarily large coefficients and effective dilations change these coefficients and frequencies, but not this upper bound on dimension.

Choose \(r>0\) so small that \(\zeta(\rho+iu)/u^m\), with its removable value at zero, is nonzero throughout \([-r,r]\). Its minimum and maximum moduli supply \(\ell,L\) in (5) for
\(z(u)=\zeta(\rho+iu)\). Put
\[
W=\max_{|u|\le r}|\rho+iu|.
\]
Apply (8) with
\[
F(u)=B(\rho+iu)\quad\hbox{(boundary values)},\qquad
p(u)=P_w(\rho+iu)/b,\qquad N=2J.
\]
The target factor has unit modulus almost everywhere. No boundary evaluation functional or continuation of \(B\) is used. Mellin--Plancherel and restriction to this single interval give
\[
\begin{aligned}
\|t-w\|^2
&=\frac1{2\pi}\int_{\mathbb R}
\frac{|bB(1/2+iy)-\zeta(1/2+iy)P_w(1/2+iy)|^2}
{|1/2+iy|^2}\,dy\\
&\ge\frac{b^2}{2\pi W^2}
\int_{-r}^r|F-zp|^2du
\ge\frac{b^2\theta r}{128\pi W^2J}.
\end{aligned}
\tag{15}
\]
Hardy's theorem supplies a critical-line zero without RH or a simplicity assumption. Moreover, \(g_2\in\mathcal N\) has
\[
\langle e,g_2\rangle=\frac{\log2}{2},\qquad
\|g_2\|^2=\frac{\log2}{4},\qquad b^2\ge\log2.
\tag{16}
\]
These follow directly from \(g_2=1/2\) on the odd reciprocal cells and zero on the even ones. Thus one admissible constant in (2) is
\[
\boxed{c_\rho=\frac{(\log2)\theta r}{128\pi W^2}>0.}
\tag{17}
\]
This specifies a constant from local zeta bounds, not a certified decimal value. The zero synthesis is also covered by the lemma. Norm continuity passes (2) to the closure at fixed \(J\); parameter collisions or parameters escaping to infinity need no compactness assumption.

All columns belong to \(\mathcal N\), since
\(A_ag_v=\sqrt a(g_{av}-v^{-1}g_a)\), with \(g_1=0\). Therefore
\[
\|e-w\|^2=1-b^2+\|t-w\|^2
\ge1-b^2+\frac{c_\rho}{J}.
\tag{18}
\]
The inequality concerns excess above the floor even if that floor is positive. For an undilated anchored sum \(\sum_{\nu=1}^Jc_\nu g_{v_\nu}\), the numerator has at most \(J+1\) frequencies because all constant terms combine. Substituting \(N=J+1\) in (15)'s preceding argument gives the corresponding stronger constant, with the same inverse-count order.

## Consequence for finite-generator synthesis

Suppose selected lattice components and their anchor are replaced by actual finite dilation sums \(w_M\) satisfying \(\|t-w_M\|\le K M^{-1/2}\) for a fixed \(K\). Then
\[
\boxed{J_M\ge(c_\rho/K^2)M.}
\tag{19}
\]
Together with [NB-371](NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost.md) and [NB-372](NB-372-bounded-effective-dilation-range-retains-a-strict-projected-target-gap.md), every such synthesis must pay
\[
J_M=\Omega(M),\qquad
\sum_\nu|c_{M,\nu}|=\Omega_\rho(M^m),\qquad
\log\max_\nu(a_{M,\nu}v_{M,\nu})=\Omega(M).
\tag{20}
\]
These are three necessary restrictions, not a jointly attainable resource law. In particular, (19) survives even when the other two budgets are unlimited. The number of selected lattice slots, the lattice search horizon, and the number of actual dilation terms remain different quantities. A finite collection of full closed-orbit vectors is not a finite-column synthesis in this dictionary.

For the ordinary consecutive integer family, where effective range and column count have the same order, NB-372's logarithmic lower bound is stronger than (2). The new count restriction addresses sparse choices with unrestricted range; it does not improve Burnol's rate for consecutive sections.

## Prior art, controls, and evidence boundary

Borwein and Erdélyi, *Nikolskii-type inequalities for shift invariant function spaces*, Proc. Amer. Math. Soc. 134 (2006), 3243–3246, [main theorem and its Hilbert-space proof](https://people.tamu.edu/~terdelyi/papers-online/shift_sub.pdf), supply (4). This is a classical dimension bound, not a new norm inequality. Erdélyi's later *Inequalities for exponential sums*, Sbornik Math. 208 (2017), 433–464, [arXiv v1, Theorem 7.1 and Lemma 12.5](https://arxiv.org/pdf/1602.02315v1), also records the complex-exponent interior estimate; inequalities restricted to real exponents would not justify (14).

Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [equation (2.3) and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the source and projected-target factors. Hardy's theorem is the same unconditional critical-zero input used by NB-371 and NB-372. Only one zero is needed.

Jousse, *Étude d'un problème de continuité lié à l'hypothèse de Riemann*, Ann. Inst. Fourier 55 (2005), 1373–1410, [Sections 4.2–4.3](https://www.numdam.org/item/10.5802/aif.2127.pdf), is the closest fixed-count approximation comparison: Theorem 7 and its corollary treat attainment and strict decrease for variable unanchored dilates, and Theorem 8 treats the anchored projection-continuity variant. Fixed-count geometry is already classical. The local delta here is the explicit inverse-count excess estimate for the projected target with arbitrary real seeds and dilations. No bibliographic priority or sharpness is claimed.

The local mechanism is generic: a finite-dimensional translation-invariant numerator cannot compensate an isolated multiplier zero against a unit-modulus target at error smaller than the inverse dimension. Arithmetic enters through the actual zeta multiplier and the actual projected target. There is no additional arithmetic cancellation theorem hidden in (4).

- Coincident frequencies only reduce dimension; almost coincident frequencies and unbounded coefficients are allowed by (4). No inverse Gram-conditioning estimate is assumed.
- Arbitrarily large frequencies are allowed. Increasing dilation range alone cannot bypass (2).
- Multiple critical zeros do not need to be separated uniformly. One fixed zero and a sufficiently small fixed interval suffice; multiplicity is unrestricted.
- The argument uses an interval of positive measure, not evaluation at a single Hardy boundary point. The target phase can be arbitrary measurable unit modulus.
- A target that vanishes at the selected zero would violate the local unit-modulus hypothesis after normalization. The result is not a universal count obstruction for every vector in \(\mathcal N\); an individual generator is exactly one column.
- An arbitrary change of generators can alter column count. The claim fixes the actual dictionary above; it is not a basis-invariant statement about rank or the number of full orbit components.
- No matching upper approximation, optimal constant, source-only construction of \(B\), or exclusion of off-critical zeros follows. A vanishing lower bound does not establish closure of the original target.

Evidence is the analytic proof and the checked primary norm inequality. The decisive audit points are the two-frequency expansion (14), the absorbed central norm (9), retention of the residual term in (10), the almost-everywhere target modulus, and the physical Mellin weight in (15). No numerical optimum, Lean verification, or independent adversarial approval is asserted.
