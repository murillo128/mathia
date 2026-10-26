# NB-370 — Adaptive lattice selection removes the three-orbit cutoff logarithm

- **Status:** proved (classical approximation mechanism plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 for the orbit realization and bounded lattice sampler/lift; NB-368 for the specified cubic phase pair; NB-369 for the contrasting contiguous-cutoff cost
- **Classification:** LITERATURE+DERIVED + EXACT-SHARPNESS + CONSTRUCTIVE-CONTROL

## Claim and scope

[[research/nyman_beurling/findings/NB-369-critical-return-energy-makes-three-orbit-lattice-truncation-logarithmically-sharp|NB-369]]'s logarithmic loss belongs to a contiguous lattice cutoff. Under the same simultaneous bad-approximation hypothesis, allowing a budget of selected lattice-index pairs removes it: the optimal squared physical component cost is of order \(1/M\), rather than \(\log M/M\). A phase-only selection attaining that order needs to inspect at most \(O_\gamma(M^2)\) positive indices. This is a different approximation family, not a stronger bound for NB-369's fixed cutoff.

Fix positive real \(\alpha,\beta\) with
\[
R_n:=\max(\|n\alpha\|_{\mathbb R/\mathbb Z},\|n\beta\|_{\mathbb R/\mathbb Z})
\ge\gamma n^{-1/2}\quad(n\ge1),\qquad \gamma>0.
\tag{1}
\]
Put
\[
D_n^2=\|n\alpha\|^2+\|n\beta\|^2,\qquad
w_n=\frac1{n^2D_n^2},\qquad C_\gamma=2+8\gamma^{-2}.
\]
Let \(w_j^*\) be the decreasing rearrangement of \((w_n)_{n\ge1}\). Then
\[
\boxed{\frac2{j^2}\le w_j^*\le\frac{C_\gamma^2}{j^2}\quad(j\ge1).}
\tag{2}
\]
Consequently, for every integer \(M\ge1\),
\[
\boxed{\frac2{M+1}\le
\inf_{\substack{\Lambda\subset\mathbb N\\|\Lambda|\le M}}
\sum_{n\notin\Lambda}w_n
\le\frac{C_\gamma^2}{M}.}
\tag{3}
\]
The upper bound is attained as an inequality by choosing the \(M\) largest weights. Every index in such a choice satisfies
\[
\boxed{n\le\frac{M^2}{2\gamma^2}.}
\tag{4}
\]
Thus the selection has a certified finite search horizon, although no bound on the bit precision needed to compare arbitrary real phases is claimed.

Here is the physical cost being controlled. Fix \(q>1\), set \(p=q^\alpha,r=q^\beta\), and retain
\[
H=L^2(0,1;dx),\quad e=1,\quad
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},
\quad\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},\quad t=P_{\mathcal N}e.
\]
Under the unitary Mellin map to \(H^2=H^2(\Re s>1/2)\), write
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bb/s,\qquad b=B(1)>0,
\quad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})}.
\tag{5}
\]
Here \(B\) is the common zeta inner factor, retained exactly as in NB-356. Let
\[
L=\log q,\quad\tau=2\pi/L,\quad z_k=1+i\tau k,
\]
and, for finite \(\Lambda\subset\mathbb N\), define the closed spaces
\[
\mathcal H_\Lambda=
\{V\in H^2:V(z_k)=0\text{ for }k\ne0\text{ with }|k|\notin\Lambda\},
\qquad
\mathcal E_{v,\Lambda}=\mathcal M^{-1}(B\Theta_v\mathcal H_\Lambda).
\tag{6}
\]
These spaces retain the entire kernel of the lattice sampler and the free value at \(z_0=1\). They are infinite-dimensional. The budget \(M\) counts positive indices, or \(2M\) nonzero lattice slots, shared by the two non-anchor components.

Define
\[
\mathfrak A_M=
\inf_{\substack{\Lambda\subset\mathbb N, |\Lambda|\le M\\
u_v\in\mathcal C_v, u_q+u_p+u_r=t}}
\left[\operatorname{dist}_H(u_p,\mathcal E_{p,\Lambda})^2
+\operatorname{dist}_H(u_r,\mathcal E_{r,\Lambda})^2\right].
\tag{7}
\]
The exact-decomposition set is nonempty and
\[
\boxed{\mathfrak A_M\asymp_{q,\alpha,\beta,b,\gamma}M^{-1}.}
\tag{8}
\]
In particular (1)--(8) apply to \((\alpha,\beta)=(\sqrt[3]2,\sqrt[3]4)\), with [[research/nyman_beurling/findings/NB-368-cubic-logarithmic-seeds-give-deterministic-finite-energy-target-completion|NB-368]]'s explicitly proved \(\gamma\). The phase selection in (4) attains the upper order in (8) for one fixed exact decomposition, independent of \(M\). It is not asserted to minimize the physical cost exactly.

## 1. Count large weights across all index scales

The first-return and gap argument behind NB-368 gives a useful counting statement. For \(0<y\le1/2\), enumerate the indices with \(R_n\le y\) as \(n_1<n_2<\cdots\). Applying (1) to the first index and to consecutive differences gives
\[
n_1\ge\gamma^2/y^2,\qquad
n_{j+1}-n_j\ge\gamma^2/(4y^2),\qquad
n_j\ge j\gamma^2/(4y^2).
\]
Therefore, for every real \(Y>0\),
\[
\#\{1\le n<Y:R_n\le y\}\le4\gamma^{-2}Yy^2.
\tag{9}
\]
The first-return bound removes an additive exceptional point. A bound based only on separation of consecutive returns would not justify (9) on every scale.

For \(X>0\), a weight \(w_n>X^{-2}\) requires \(R_n<X/n\). There are at most \(2X\) positive integers below \(2X\). For each of the disjoint blocks
\[
A_j\le n<2A_j,\qquad A_j=2^{j+1}X,\quad j\ge0,
\]
apply (9) with \(Y=2A_j\) and \(y=X/A_j\le1/2\). The number of large weights in that block is at most
\[
8\gamma^{-2}X^2/A_j.
\]
Summing the geometric series, including arbitrarily high indices, proves
\[
\boxed{\#\{n:w_n>\lambda\}\le C_\gamma\lambda^{-1/2}
\qquad(\lambda>0).}
\tag{10}
\]
This is a weak-\(\ell^{1/2}\) estimate for the squared sample-cost sequence. The block sum is geometric; the logarithm in the fixed-prefix energy estimate does not enter it.

## 2. Rearrangement, sharpness, and the search horizon

By (1),
\[
\frac2{n^2}\le w_n\le\frac1{\gamma^2n}.
\tag{11}
\]
The lower inequality uses \(D_n^2\le1/2\), and the upper inequality ensures \(w_n\to0\). Thus the decreasing rearrangement exists, and the largest \(M\) weights can be chosen for each finite \(M\), with ties resolved arbitrarily.

For every \(j\), the first \(j\) indices in their original order already supply \(j\) weights at least \(2/j^2\). This proves the lower bound in (2). If \(0<\lambda<w_j^*\), at least \(j\) weights exceed \(\lambda\), so (10), followed by \(\lambda\uparrow w_j^*\), proves the upper bound in (2).

Because the nonnegative series is summable by that upper bound, discarding all but the \(M\) largest weights minimizes its remaining sum. Summing (2) for \(j>M\) and using
\[
\frac1{M+1}\le\sum_{j>M}j^{-2}\le\frac1M
\]
proves (3). Its lower bound holds for every subset of at most \(M\) retained indices; no equidistribution assumption is used.

Every selected weight is at least \(w_M^*\ge2/M^2\). Combining this with the upper bound in (11) proves (4). Inspecting the positive integers through \(\lfloor M^2/(2\gamma^2)\rfloor\) therefore suffices to select a global set of \(M\) largest weights. Consistent tie-breaking gives nested selections as \(M\) grows. The number of inspected indices and the number of retained indices are different costs.

## 3. Transfer the optimized sample tail to physical component distance

Put \(f=b/s\), and for \(k\ne0\) set
\[
a_k=|\Theta_p(z_k)|^2+|\Theta_r(z_k)|^2,\qquad
t_k=\frac{|f(z_k)|^2}{a_k},\qquad
T_{\Lambda^c}=\sum_{\substack{k\ne0\\|k|\notin\Lambda}}t_k.
\]
The elementary factor bounds in [[research/nyman_beurling/findings/NB-356-finite-orbit-target-assembly-is-equivalent-to-a-reciprocal-phase-series|NB-356]] give constants \(0<c_0\le C_0<\infty\), depending only on \(q,\alpha,\beta,b\), such that
\[
t_{-n}=t_n,\qquad c_0 w_n\le t_n\le C_0 w_n\quad(n\ge1).
\tag{12}
\]
In particular, the full sample cost is finite by (2). The sampler and right inverse obey
\[
\sum_{k\in\mathbb Z}|F(z_k)|^2\le C_q\|F\|_{H^2}^2,
\quad C_q=\frac L{1-q^{-1}},\qquad
(R_qd)(z_k)=d_k,\quad\|R_qd\|^2\le(q/L)\|d\|_2^2.
\tag{13}
\]

For any exact decomposition
\(f=\Theta_qU_q+\Theta_pU_p+\Theta_rU_r\), evaluation at \(z_k\), \(k\ne0\), kills the anchor. Cauchy--Schwarz gives
\[
t_k\le |U_p(z_k)|^2+|U_r(z_k)|^2.
\]
For any \(V_p,V_r\in\mathcal H_\Lambda\), the omitted samples of \(U_v\) equal those of \(U_v-V_v\). Applying (13), and using that multiplication by \(B\Theta_v\) is isometric, proves the lower comparison
\[
\inf_{u_q+u_p+u_r=t}
\sum_{v=p,r}\operatorname{dist}_H(u_v,\mathcal E_{v,\Lambda})^2
\ge C_q^{-1}T_{\Lambda^c}.
\tag{14}
\]
This holds for every exact split, including arbitrary changes in the sampler kernel.

For the reverse comparison take the complete minimum-norm data
\[
d_{v,k}=f(z_k)\overline{\Theta_v(z_k)}/a_k\quad(k\ne0, v=p,r),
\qquad d_{v,0}=0,
\qquad U_v=R_qd_v.
\]
The numerator \(f-\Theta_pU_p-\Theta_rU_r\) vanishes at every zero of the pure Blaschke factor \(\Theta_q\). Hence
\[
U_q=(f-\Theta_pU_p-\Theta_rU_r)/\Theta_q\in H^2.
\]
This is one exact decomposition with finite anchor norm, valid for all choices of \(\Lambda\). The removable point \(z_0=1\) is not a zero and imposes no extra condition. Set
\[
V_v=R_q(d_v\mathbf1_{\{|k|\in\Lambda\}})\in\mathcal H_\Lambda.
\]
Then (13) gives
\[
\sum_{v=p,r}\|U_v-V_v\|^2\le(q/L)T_{\Lambda^c}.
\tag{15}
\]
Combining (14)--(15), taking the infimum over \(|\Lambda|\le M\), and applying (3) and (12) yields the explicit bounds
\[
\boxed{\frac{4c_0}{C_q(M+1)}\le\mathfrak A_M
\le\frac{2qC_0C_\gamma^2}{LM}.}
\tag{16}
\]
The upper bound uses the \(M\) largest \(w_n\), so the sample-index rule requires neither \(B\) nor \(b\). Constructing the physical orbit vectors still uses both through (5); the selection does not remove that boundary.

## Prior art, mathematical delta, and limits

The rearrangement mechanism is classical [[research/prior_art/incremental/PA-best-term-hilbert-approximation-weak-sequence|nonlinear approximation]]. DeVore, *Nonlinear approximation*, Acta Numerica 7 (1998), 51--150, DOI `10.1017/S0962492900002816`, [author manuscript, Section 2, equations (2.18)--(2.19), and Section 5](https://people.math.sc.edu/devore/publications/nlacta.pdf), relates best-term Hilbert error to decreasing coefficients and weak sequence spaces. Here the sample amplitudes have rearranged size of order \(j^{-1}\), giving squared tail of order \(M^{-1}\). The Hardy lift is bounded, not an orthonormal coordinate identification; inequalities (14)--(15) supply the required physical comparison rather than assuming Parseval for that lift.

Fregoli, *Sums of reciprocals of fractional parts*, [Section 1, gap argument preceding Theorem 1.2](https://pure.royalholloway.ac.uk/ws/files/34774891/1805.00865v1.pdf), is the neighboring classical return-gap source already used in NB-368. Its linear-form denominator differs from the sum of two squared distances here. Equations (9)--(10) directly establish the precise counting estimate needed for this sequence. No new general gap, interpolation, or nonlinear-approximation theorem is claimed.

The local result resolves the explicit adaptive-selection boundary left by NB-369. For the same seeds and the same physical norm, contiguous retention of \(M\) positive indices costs \(\Theta(\log M/M)\), whereas adaptive retention costs \(\Theta(1/M)\), even after optimizing the exact split in either case. The finite search horizon also prevents the adaptive upper bound from silently assuming an unlimited search over sample locations. This is a derived application of classical tools, with no claim to bibliographic priority.

- The budget counts lattice-index pairs shared by two components, not arbitrary measurement functionals, dilation generators, or coefficients in a discrete Nyman section.
- Each space in (6) contains an unrestricted infinite-dimensional sampler kernel. The anchor is also unrestricted. Neither (8) nor (16) is a finite-generator approximation rate.
- The lower bound is on the sum of squared component distances. It is not a lower bound on the residual of their sum, where errors can cancel.
- The \(O_\gamma(M^2)\) search bound is sufficient, not asserted optimal. It counts indices, not arithmetic operations or required precision, and does not give a numerically certified selector for arbitrary uncomputable real input phases.
- Condition (1) controls all positive integers, including differences of returns. Finiteness of the completion series alone does not justify (10). No adaptive rate is asserted for every completing phase pair or for the specified integer seeds \(2,3,5\).
- The Burnol floor is retained: every orbit sum \(w\) satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The result neither supplies source-only access to \(B\) nor advances the RH closure implication.

Evidence is the analytic derivation and inspected primary/authoritative literature. An ephemeral exact-rational audit used 15 collision-free finite phase prefixes of lengths 64, 128, and 256, with the bad-approximation constant chosen only for each prefix. It passed 63,151 ordered-return checks, 2,238 level-set checks, 2,240 rearrangement checks, and 90 finite selection/horizon checks. These controls audit finite inequalities and ties, not infinite bad approximability, series tails, or Hardy membership. The load-bearing analytic checks are the first return in (9), summation over all index blocks in (10), the lower rearrangement bound independent of ordering, and the all-decompositions lower bound (14). No Lean verification or independent adversarial approval is asserted.
