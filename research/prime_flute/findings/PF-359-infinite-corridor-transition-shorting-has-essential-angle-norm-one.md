# PF-359 — infinite corridor transition shorting has essential angle norm one

**Status:** EXACT-DERIVED + CLASSICAL-SHORTING-AND-APPROXIMATION-METHODS + INFINITE-CORRIDOR-MODEL-OBSTRUCTION + ACTUAL-PANT-COMPARISON-OPEN.

The retained-constant obstruction survives elimination of the entire infinite transition space in a specified energy completion of the nearest-neighbor Cauchy corridor model. For sufficiently narrow fixed positive-width transition bands on the exact prime-cuff periods, its constant/high-strip canonical-correlation operator has **essential norm one**, independently of every positive corridor conductance. In particular it is not compact.

This closes the finite-section compatibility gap for this model. It does not close the residual-scale comparison to the actual pant/seam form. The operator below is defined by the same corridor energy used in PF-352–PF-358, not identified with an intrinsic surface operator.

## 1. One infinite energy space and one shorted angle

Fix `a>0`. At each vertex `i>=1`, let `T_i` and `Y_i` be finite sets of positive real nodes, distinct within the vertex and disjoint from each other and from `a`. Nodes may coincide between vertices. Let `c_i>0` for `i>=0` be finite edge conductances, and let `g_i>=0` be finite on-site weights. No uniform upper/lower bounds or summability are assumed. Put `v_0=0` and initially allow only finitely supported fields

\[
v_i(t)=\sum_{x\in\{a\}\cup T_i\cup Y_i}z_{i,x}e^{-xt},
\qquad t>0,
\]
\[
\mathcal E[v]=\sum_{i\ge0}c_i\|v_{i+1}-v_i\|_2^2
             +\sum_{i\ge1}g_i\|v_i\|_2^2.
\tag{1}
\]

All sums are finite on this initial space. The norm is definite: zero energy makes all fields equal to `v_0=0`, and independence of the local exponentials makes every coefficient zero. Let `H_E` be its Hilbert completion. Equivalently it is the closure of the weighted edge/ground fields in the corresponding Hilbert direct sum. This defines the completion even when the coefficient matrix is unbounded on ordinary `ell^2`.

Let `T_alg`, `L_alg`, and `H_alg` denote the algebraic spans of all transition labels, all labels `(i,a)`, and all high labels, respectively. These consist of finitely supported coefficient fields. Define

\[
\mathcal T=\overline{T_{\rm alg}}^{H_E},\qquad R=I-P_{\mathcal T},
\qquad \mathcal L=\overline{RL_{\rm alg}},\qquad
\mathcal H=\overline{RH_{\rm alg}}\subset\mathcal T^\perp,
\]
\[
Z=P_{\mathcal H}|_{\mathcal L}:\mathcal L\longrightarrow\mathcal H.
\tag{2}
\]

This contraction is the canonical-correlation operator (the adjoint convention gives the same singular data). Finite positive forms give the usual diagonally normalized mixed block. Formula (2) needs no bounded inverse for an infinite transition matrix or low/high diagonal.

For a finitely supported constant coefficient vector `u`, write `f_u=(u_i e^{-at})_i` and

\[
A[u]=\|Rf_u\|_E^2=\inf_{t\in T_{\rm alg}}\mathcal E[f_u+t],
\]
\[
E[u]=\inf_{t\in T_{\rm alg},\,y\in H_{\rm alg}}\mathcal E[f_u+t+y]
=\|(I-P_{\mathcal H})Rf_u\|_E^2.
\tag{3}
\]

The equalities follow from closure and orthogonal projection. In particular the second infimum allows transitions and high coefficients arbitrarily far from the support of `u`. It does not fix a finite reservoir or assume convergence of independently normalized finite matrices.

## 2. An edgewise residual certificate survives every remote transition

Define

\[
Q_i=\prod_{t\in T_i}\left(\frac{a-t}{a+t}\right)^2>0,
\quad P_i=\prod_{b\in Y_i}\left(\frac{a-b}{a+b}\right)^2>0,
\quad Q_0=1,
\quad d_i=c_{i-1}+c_i+g_i.
\tag{4}
\]

Empty products equal one. The classical scalar Cauchy distance identity is

\[
\inf_{z_x}\left\|s e^{-at}+\sum_{x\in U}z_xe^{-xt}\right\|_2^2
=\frac{|s|^2}{2a}\prod_{x\in U}\left(\frac{a-x}{a+x}\right)^2.
\tag{5}
\]

It follows by iterating the one-node Schur identity
`1/(x+y)-2t/((x+t)(y+t))=((x-t)/(x+t))((y-t)/(y+t))/(x+y)`.

For any finitely supported transition field in (3), edge `i` contains constant coefficient `u_(i+1)-u_i` and transition nodes in `T_i union T_(i+1)`. Relax each edge's transition coefficients independently. Repeated nodes count only once in the union, so its product is at least `Q_i Q_(i+1)`. Apply (5) separately to edges and grounds. The result holds for every trial and hence for the global infimum:

\[
A[u]\ge\frac1{2a}\left\{
\sum_{i\ge0}c_iQ_iQ_{i+1}|u_{i+1}-u_i|^2
+\sum_{i\ge1}g_iQ_i|u_i|^2\right\}.
\tag{6}
\]

Here `u_0=0`, `T_0` at vertex zero is empty, and only finitely many terms on the right are nonzero. No simultaneous edge optimizer is claimed. Independent edge minimization is a lower bound even though actual neighboring trials share coefficients. Taking the energy closure does not weaken (6), since the infimum over the dense algebraic transition space already equals the closed-space distance.

Now suppose the support `I` of `u` contains no consecutive vertices. Then (6) becomes

\[
A[u]\ge\frac1{2a}\sum_{i\in I}
 Q_i(c_{i-1}Q_{i-1}+c_iQ_{i+1}+g_i)|u_i|^2.
\tag{7}
\]

For an upper trial in `E[u]`, use the scalar optimizer (5) for `T_i union Y_i` on each `i in I`, and set all other vertex fields to zero. No edge joins two nonzero fields. Therefore the trial energy is exactly a sum of local energies, without a factor-two estimate:

\[
E[u]\le\frac1{2a}\sum_{i\in I}d_iQ_iP_i|u_i|^2.
\tag{8}
\]

Set

\[
\varepsilon_i=
\frac{d_iP_i}{c_{i-1}Q_{i-1}+c_iQ_{i+1}+g_i}
\le\frac{P_i}{\min\{Q_{i-1},Q_{i+1},1\}}.
\tag{9}
\]

Equations (7)–(8) prove on every such coordinate subspace

\[
\frac{E[u]}{A[u]}\le\max_{i\in I}\varepsilon_i.
\tag{10}
\]

In particular its residual images are linearly independent by (7). Their normalized images need not be spatially localized or mutually orthogonal. The certificate uses subspace dimension, not those additional properties.

## 3. Essential norm, proved inside the completed space

Suppose there is an infinite nonconsecutive set `I` along which `epsilon_i -> 0`. Then

\[
\boxed{\|Z\|_{\mathrm{ess}}=1.}
\tag{11}
\]

Indeed for every `epsilon>0`, discard finitely many indices so that `epsilon_i<=epsilon`. The algebraic residual span `V_epsilon` of the remaining constants is infinite dimensional, and (3), (10) imply

\[
\|Zx\|_E^2\ge(1-\varepsilon)\|x\|_E^2
\qquad(x\in V_\varepsilon).
\tag{12}
\]

For every finite-rank operator `F: L -> H`, this span contains a unit vector in `ker F`. Hence `||Z-F||>=sqrt(1-epsilon)`. Finite-rank operators are norm dense in the compact operators between Hilbert spaces. Taking the infimum over compact `F`, then `epsilon -> 0`, gives `||Z||_ess>=1`; contractivity gives the reverse inequality.

More generally a uniform bound `epsilon_i<=epsilon<1` on an infinite independent set gives essential norm at least `sqrt(1-epsilon)`. Equation (11) excludes every compact Schatten or weak-Schatten class. It does not assert that one is an eigenvalue or that the two closed subspaces have a nontrivial intersection.

This is the new infinite-section step beyond PF-358: every witness already lives in the **same globally shorted Hilbert space**, and (6) prices remote transition relaxation before taking a limit.

## 4. Complete physical bands and the prime-cuff realization of the model

Use `a=1`, `x=cosh(pi xi)`, `xi=2pi k/L_i`. The kernel `1/(x+y)` is also the Gram kernel of

\[
k_x(t)=\frac{\cos(\xi t)}{\sqrt{\pi(x+1)}}
\quad\hbox{in }L^2(\mathbb R,\operatorname{sech}t\,dt),
\tag{13}
\]

including `x=1`, the constant mode. This is PF-352's cosine corridor realization. Positive physical Fourier rescalings are coefficient congruences and preserve the closed subspaces and angle after isometric identification. Sines decouple in this even-weight model; adding them to the transition space does not change the cosine calculation.

Fix `0<kappa_-<kappa_+<Omega`. Take every positive cosine lattice mode in `(kappa_-,kappa_+)` as `T_i`, and every such mode in `[kappa_+,Omega]` as `Y_i`. As in PF-357/PF-358, set

\[
\delta=-\frac2\pi\int_{\kappa_-}^{\kappa_+}
 \log\tanh(\pi\xi/2)\,d\xi>0,
\quad
\gamma=-\frac2\pi\int_{\kappa_+}^{\Omega}
 \log\tanh(\pi\xi/2)\,d\xi>0.
\tag{14}
\]

Bounded-variation Riemann sums, with uniform endpoint-rounding error, give
`Q_i=exp(-delta L_i+O(1))`, `P_i=exp(-gamma L_i+O(1))`. Thus away from the finite head,

\[
\varepsilon_i\le C\exp\{-\gamma L_i+
             \delta\max(L_{i-1},L_{i+1})\}.
\tag{15}
\]

If `L_i -> infinity` and neighboring periods satisfy
`max(L_(i-1),L_(i+1))<=R L_i` eventually for some fixed `R`, then `gamma>R delta` implies (11), using either spatial parity. Such bands exist: fix `kappa_->0` and `Omega>kappa_-`, then choose `kappa_+` sufficiently close to `kappa_-` and keep that positive width fixed. This is a sufficient condition, not a sharp threshold.

For the exact prime cuffs, PF-032 gives

\[
L_i=2\log\coth(h_i/4),\qquad
h_i=\log\frac{\cot(\pi/p_i)}{\cot(\pi/p_{i-1})}
\asymp\frac{p_i-p_{i-1}}{p_i}.
\tag{16}
\]

The last estimate follows from the derivative of `log cot(pi/x)`, which is asymptotic to `1/x`, and consecutive-prime ratios tending to one. Baker–Harman–Pintz gives `p_i-p_(i-1)=O(p_i^(21/40))`, while odd-prime gaps are at least two. Consequently

\[
\frac{19}{20}\log p_i-O(1)\le L_i\le2\log p_i+O(1),
\quad
\limsup_i\frac{\max(L_{i-1},L_{i+1})}{L_i}\le\frac{40}{19}.
\tag{17}
\]

Choose any fixed `R>40/19` and bands with `gamma>R delta`. The completed model then has essential angle norm one on these **exact unequal prime-cuff lattices**. One may take the geometric corridor conductances `c_i=1/s_i`, `s_i=(h_i+h_(i+1))/2`, since (11) allows arbitrary positive conductances. No adjacent-gap ratio bound, exact shared nonzero frequency, or finite-section grounding estimate is needed.

## 5. Boundaries, controls, and changed implication

- The theorem fixes the energy completion of finitely supported fields and the closure of finitely supported transition fields. It does not equate every possible boundary condition at infinity, or all finite-energy trace fields, with this completion.
- Constants are retained low variables. A mean-zero representation or further shorting of constants is a different problem. Enlarging retained low/high spaces in the same energy model preserves the obstruction by (12); enlarging the eliminated space beyond the prescribed transitions requires a new certificate.
- The grounds `g_i` multiply the same Cauchy norm. They are not the actual Fourier-diagonal symmetric seam term. Nor does arbitrary conductance robustness authorize replacing the frequency kernel, the trace transport, or the positive shifted pant energy.
- The local products are essential. A vertex with empty high set has `P_i=1`; a sufficiently large neighboring transition product cost can make (9) uninformative. Failure of (15) to decay proves no compactness.
- This is universal within the stated corridor class: nonprime periods with the same neighboring-period growth satisfy the same conclusion. It supplies no primality selector, intrinsic scattering identity, zeta relation, or RH implication.
- PF-356's dense rank-one control and PF-352's zero correlation for one nonconstant pair do not contradict (11): the first changes spatial locality, and the second does not eliminate the whole retained-constant/high-strip correlation.

The model's compatible infinite completion is therefore no longer an escape from its retained-constant obstruction. To use that obstruction for the actual flute, the next load-bearing step remains a justified comparison of the **actual globally shorted pant/seam form** at the residual scale and with the relevant completion. PF-348's local Dirichlet comparison and PF-350's face-parity bound do not provide that step. No further finite-model counting is needed to establish (11).

## 6. Prior art and verification

The ingredients are classical. Almira, *Müntz Type Theorems I*, Section 2.1, pp. 154–155 ([primary journal copy](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), S31), records the scalar Gram-distance product underlying (5). Anderson–Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71 ([publisher](https://doi.org/10.1137/0128007)), develops Hilbert-space shorting. Morley, *Shorts of block operators and infinite networks—A note on the shorted operator: II*, Circuits, Systems, and Signal Processing 9 (1990), 161–170 ([publisher](https://doi.org/10.1007/BF01236449)), studies finite approximations to infinite-network shorts under a bounded-positive-operator hypothesis. Here (1)–(3) define an energy completion directly; no unverified ordinary-`ell^2` boundedness or norm convergence of normalized finite sections is imported. The essential-norm argument is proved in Section 3.

The arithmetic input is only the established `0.525` prime-gap bound of Baker, Harman and Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532–562 ([publisher](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/83.3.532), S6). No optimality claim for that exponent is needed.

Structure-directed searches covered infinite-network shorting and truncation, Hilbert-space projections, Cauchy/Müntz residual products and canonical correlations. No new general shorting or approximation theorem is claimed. The derived addition is the edge-local certificate (6)–(10) and its application to a single infinite corridor angle on complete unequal lattices, including the exact prime periods. The classical network results alone do not identify this angle or the actual surface operator.

Supplementary Python `Fraction` checks covered 45 finite path models: `d=1,...,5`; unit conductances with `g_i=(i+1)/7` (zero-based `i`), conductances cycling through `10^(-8),1,10^8` without on-site grounds, and the latter paths with both endpoint conductances replaced by `10^(-24)`. Transition sets were empty, the shared node `3`, or unequal nodes `2+i/11,3+i/13`; high sets were `5+i/17,7+i/19`, with the last high set omitted in the weak-grounding/empty-transition family. Exact Schur elimination and rational positive-semidefinite pivot checks verified (7), (8), and the compression of `epsilon A-E` for both spatial parities in every case. These audit algebra and degenerate controls, not the infinite limit or actual geometry; those conclusions have only the proof and evidence boundary stated above. Scratch remains outside Git. No Lean verification or independent adversarial approval is claimed.
