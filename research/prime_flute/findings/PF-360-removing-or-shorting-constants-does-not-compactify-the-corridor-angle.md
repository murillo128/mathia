# PF-360 — removing or shorting constants does not compactify the corridor angle

**Status:** EXACT-DERIVED + CLASSICAL-CAUCHY-RESIDUAL-METHOD + MEAN-ZERO-MODEL-OBSTRUCTION + ACTUAL-PANT-COMPARISON-OPEN.

The constant Fourier mode is not necessary for PF-359's infinite corridor obstruction. For the same sufficiently narrow fixed positive-width transition bands on exact prime-cuff periods, the **first nonzero cosine on each cuff** supplies an infinite-dimensional low sector whose angle with a bounded high strip has essential norm one. This holds both when constants are fixed to zero and when the entire constant sector is eliminated together with the transitions.

These are distinct operations. The second assertion follows from an exact isometry between their shorted energy spaces, not from monotonicity of correlation under relaxation. No common nonzero frequency, conductance conditioning, or bounded inverse on coefficient `ell^2` is required. The claim concerns the specified Cauchy corridor model; comparison to the actual globally shorted pant/seam form remains open.

## 1. Nonconstant carriers in one completed energy space

Use the half-line energy of PF-359, initially on finitely supported fields,

\[
\mathcal E[v]=\sum_{i\ge0}c_i\|v_{i+1}-v_i\|_{L^2(0,\infty)}^2
 +\sum_{i\ge1}g_i\|v_i\|_2^2,\qquad v_0=0,
\tag{1}
\]

where every `c_i>0` is finite and every `g_i>=0` is finite. At vertex `i` allow the exponentials with nodes in

\[
\{a_i\}\cup T_i\cup Y_i\subset(0,\infty).
\]

The finite sets are disjoint within each vertex. Require also `a_i` not to belong to `T_(i-1)` or `T_(i+1)`; set `T_0=empty`. The retained nodes `a_i` may all differ. They need not occur at any neighboring vertex. The eventual physical bands below satisfy these separations automatically.

Let `H_0` be the completion in (1), which is definite because the left endpoint is grounded and local exponentials are independent. Let `mathcal T` be the closure of the algebraic transition fields, and put `R_T=I-P_mathcal T`. Define

\[
\mathcal L=\overline{R_T\operatorname{span}_{\rm alg}\{(i,a_i)\}},
\qquad
\mathcal H=\overline{R_T\operatorname{span}_{\rm alg}\{(i,y):y\in Y_i\}},
\qquad Z_0=P_{\mathcal H}|_{\mathcal L}.
\tag{2}
\]

Closures and projections use `H_0`. For a finitely supported coefficient vector `u`, let `f_u=(u_i exp(-a_i t))_i` and set

\[
A[u]=\inf_{z\in T_{\rm alg}}\mathcal E[f_u+z],\qquad
E[u]=\inf_{z\in T_{\rm alg},\,y\in Y_{\rm alg}}
                 \mathcal E[f_u+z+y].
\tag{3}
\]

These are squared distances to the corresponding closed spaces. In particular, all remote transition variables are already free. For `x=R_T f_u`,

\[
E[u]=\|(I-P_{\mathcal H})x\|_E^2,
\qquad A[u]=\|x\|_E^2.
\tag{4}
\]

## 2. A certificate that does not require a common low node

For any positive `a` outside the relevant transition sets, write

\[
Q_j(a)=\prod_{t\in T_j}\left(\frac{a-t}{a+t}\right)^2,
\qquad
P_i(a)=\prod_{y\in Y_i}\left(\frac{a-y}{a+y}\right)^2,
\qquad Q_0(a)=1.
\tag{5}
\]

All products used below are positive; empty products are one. The classical scalar residual identity is

\[
\inf_{z_x}\left\|s e^{-at}+\sum_{x\in U}z_xe^{-xt}\right\|_2^2
 =\frac{|s|^2}{2a}\prod_{x\in U}\left(\frac{a-x}{a+x}\right)^2.
\tag{6}
\]

It follows by successive one-node Schur elimination from the kernel `1/(x+y)`; duplicate nodes in `U` count once.

Let `I` be a finite nonconsecutive set, and suppose `u` is supported on `I`. Each incident edge contains **only one retained exponential**, although the two endpoint transition sets are both free. Apply (6) to each edge and ground, relaxing their transition coefficients independently. Because each scalar product factor lies in `(0,1)`, the product over a union is at least the product with duplicate nodes counted twice. Thus

\[
A[u]\ge\sum_{i\in I}\frac{|u_i|^2Q_i(a_i)}{2a_i}
 \big[c_{i-1}Q_{i-1}(a_i)+c_iQ_{i+1}(a_i)+g_i\big].
\tag{7}
\]

This is a lower bound on every global trial, not an assertion that independently minimizing edge coefficients can be assembled. Taking the closure of the transition space preserves it.

For the further residual `E[u]`, use the scalar optimizer for `T_i union Y_i` on every `i in I`, and zero fields elsewhere. No edge joins two nonzero fields. With `d_i=c_(i-1)+c_i+g_i`,

\[
E[u]\le\sum_{i\in I}\frac{|u_i|^2d_iQ_i(a_i)P_i(a_i)}{2a_i}.
\tag{8}
\]

Consequently, for nonzero `u` supported on `I`,

\[
\frac{E[u]}{A[u]}\le\max_{i\in I}\varepsilon_i,
\qquad
\varepsilon_i=
\frac{d_iP_i(a_i)}{c_{i-1}Q_{i-1}(a_i)+c_iQ_{i+1}(a_i)+g_i}
\le\frac{P_i(a_i)}{\min\{Q_{i-1}(a_i),Q_{i+1}(a_i),1\}}.
\tag{9}
\]

Equation (7) makes the residual images of these coefficient vectors linearly independent. If an infinite nonconsecutive set satisfies `epsilon_i -> 0`, then

\[
\boxed{\|Z_0\|_{\rm ess}=1.}
\tag{10}
\]

Indeed, for every `epsilon>0`, its sufficiently far residual span is infinite dimensional and obeys `||Z_0 x||^2 >= (1-epsilon)||x||^2`. The kernel of any finite-rank operator meets that span in a unit vector. The distance of `Z_0` from every finite-rank operator is therefore at least `sqrt(1-epsilon)`. Finite-rank approximation of compact operators and contractivity give (10). No assertion about a unit eigenvalue, spatial localization after normalization, or an intersection of the two closed subspaces is needed.

Unlike PF-359's constant-fibre formula, (7) does not involve `u_(i+1)-u_i` at a common exponent. Independent support is exactly what permits different retained nodes without assuming that their difference is one exponential.

## 3. The first nonzero physical modes satisfy the certificate

Take a sufficiently far prime-flute tail, with physical periods `L_i`, and use the exact cosine kernel identification

\[
x=\cosh(\pi\xi),\quad y=\cosh(\pi\zeta),\quad \xi=2\pi k/L_i,
\qquad
\left\langle
\frac{\cos(\xi t)}{\sqrt{\pi(x+1)}},
\frac{\cos(\zeta t)}{\sqrt{\pi(y+1)}}
\right\rangle_{L^2(\mathbb R,\operatorname{sech}t\,dt)}
=\frac1{x+y}.
\tag{11}
\]

Fix `0<kappa_-<kappa_+<Omega`. Let `T_i` contain every positive cosine lattice node in `(kappa_-,kappa_+)` and `Y_i` every one in `[kappa_+,Omega]`. Retain

\[
\xi_i=2\pi/L_i,\qquad
a_i=\cosh(2\pi^2/L_i)=1+O(L_i^{-2}).
\tag{12}
\]

This is a mean-zero periodic cosine, eventually below `kappa_-`. Constants are absent in `H_0`. Different cuff lengths give different carriers, which causes no problem in (7).

Define the same positive exponents as PF-359:

\[
\delta=-\frac2\pi\int_{\kappa_-}^{\kappa_+}
           \log\tanh(\pi\xi/2)\,d\xi,
\qquad
\gamma=-\frac2\pi\int_{\kappa_+}^{\Omega}
           \log\tanh(\pi\xi/2)\,d\xi.
\tag{13}
\]

Bounded-variation Riemann sums give `log Q_j(1)=-delta L_j+O(1)` and `log P_i(1)=-gamma L_i+O(1)`, uniformly in rounding at the endpoints. The passage from `1` to `a_i` is controlled, rather than inferred from entrywise convergence. All transition and high nodes stay a fixed distance above `1`, and

\[
\partial_a\log\left(\frac{a-x}{a+x}\right)^2
=-\frac{4x}{x^2-a^2}
\tag{14}
\]

is uniformly bounded there for `a` near `1`. There are `O(L_j+1)` nodes on module `j`. Hence

\[
\log Q_j(a_i)=-\delta L_j+O(1)+O((L_j+1)L_i^{-2}),
\qquad
\log P_i(a_i)=-\gamma L_i+O(1).
\tag{15}
\]

If `L_i -> infinity` and `max(L_(i-1),L_(i+1))<=R L_i` eventually, (9) gives

\[
\varepsilon_i\le C\exp\{-\gamma L_i+
                 \delta\max(L_{i-1},L_{i+1})\}.
\tag{16}
\]

Thus `gamma>R delta` proves (10), using either spatial parity. Such fixed positive-width bands exist by holding `kappa_->0` and `Omega>kappa_-` fixed and choosing `kappa_+` sufficiently close to `kappa_-`.

PF-359, equations (16)–(17), derives from the exact cuff law and the Baker–Harman–Pintz gap bound that

\[
L_i\longrightarrow\infty,\qquad
\limsup_i\frac{\max(L_{i-1},L_{i+1})}{L_i}\le\frac{40}{19}.
\tag{17}
\]

Therefore any fixed `R>40/19` and bands satisfying `gamma>R delta` give the asserted mean-zero obstruction on the **exact unequal prime-cuff lattices**. Conductances remain arbitrary positive numbers, including the geometric corridor choices. Additional retained low modes and high modes preserve the lower bound by enlarging the corresponding closed subspaces in the same shorted energy. Sine sectors decouple in this even-weight model. Neither observation identifies the model with the actual face-parity seam form.

## 4. Eliminating all constants is exactly angle-equivalent

Adjoin the node `b=1` at every vertex to obtain the enlarged energy completion `H_+`, and let `mathcal C` be the closure of all finitely supported constant-mode fields. Here `exp(-t)` represents the physical constant in (11), not a constant function of the exponential coordinate.

The scalar `L^2(0,infinity)` projection `P_b` onto `exp(-bt)`, applied at every vertex, commutes with edge differences. Consequently (1) splits orthogonally into its `P_b` and `I-P_b` parts. On algebraic fields `P_b` has finitely supported constant coefficients. It extends as a contraction and is exactly the energy-orthogonal projection onto `mathcal C`. In particular it does not require solving an infinite network inverse.

For `x!=b` define

\[
r_x(t)=e^{-xt}-\frac{2b}{x+b}e^{-bt},\qquad
\theta_b(x)=\frac{x-b}{x+b}.
\]

Direct scalar integration gives

\[
\langle r_x,r_y\rangle
=\frac{\theta_b(x)\theta_b(y)}{x+y}.
\tag{18}
\]

This is PF-355's finite common-fibre identity at the level of the energy itself. Applying it to every edge and ground proves that

\[
U:(i,e^{-xt})\longmapsto(i,r_x/\theta_b(x))
\tag{19}
\]

extends from the algebraic nonconstant fields to an isometry from `H_0` onto `mathcal C^perp` in `H_+`. It is onto because residualized nonconstant algebraic fields are dense there. Every label factor is nonzero, so (19) maps each transition/low/high algebraic span onto the corresponding constant-residualized span. This statement remains valid after taking closures even though `theta_1(a_i)` tends to zero: no uniform invertibility on a coefficient `ell^2` space is asserted or needed.

Let `Z_C` be the low/high projection angle after eliminating the closure of the sum of the constant and transition algebraic fields in `H_+`. Sequential orthogonal residualization by `mathcal C` and then its residualized transition space equals this simultaneous elimination. The isometry (19) identifies both low and high closed residual spaces with those in (2). Therefore

\[
\boxed{Z_C\text{ is unitarily equivalent to }Z_0,
\qquad \|Z_C\|_{\rm ess}=\|Z_0\|_{\rm ess}=1.}
\tag{20}
\]

The equivalence of the two angles holds for arbitrary admissible nonconstant sectors in this model, without the band asymptotics; those asymptotics are needed to obtain the value one. Constants being absent and constants being freely minimized are not generally equivalent operations for a positive form. Equation (18), the complete common constant sector, and the frequency-independent edge/ground weights are essential to this equivalence.

## 5. Controls, prior art, and the remaining implication

The mathematical change is a closed model escape: discarding constant traces, or shorting them globally, cannot restore compactness for the stated narrow transition bands. PF-359's retained-constant witness alone did not imply this. The replacement uses actual nonzero lattice modes, an independent-support residual certificate, and an isometry of the completed spaces. The argument does not reuse a finite-section singular-value count as evidence for an infinite operator.

The scalar residual product is classical Müntz/Cauchy Gram algebra: Almira, *Müntz Type Theorems I*, Section 2.1, pp. 154–155 ([journal copy](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), S31). Under `r=exp(-t)`, the isometry sends `exp(-xt)` to `r^(x-1/2)` in `L^2(0,1)`, giving exactly (6). Positive shorting and infinite-network approximation have the classical context recorded in S33, including Morley, *Shorts of block operators and infinite networks—A note on the shorted operator: II* ([publisher](https://doi.org/10.1007/BF01236449)). Morley's bounded-operator hypothesis is not imported into (1). The finite common-fibre congruence is already proved in PF-355; (18)–(19) supply its completion argument here. Structure-directed searches also covered Blaschke residual kernels and Cauchy canonical correlations. No new general interpolation, shorting, or arithmetic theorem is claimed.

Supplementary Python `Fraction` checks covered 30 finite paths: `d=1,...,5`; unit conductances and grounds `g_i=(i+1)/7` (zero-based indexing), or conductances cycling through `10^(-8),1,10^8` with both endpoint conductances replaced by `10^(-24)` and no grounds. Carriers were `a_i=1+10^(-(i+2))`; transition sets were empty, the shared node `3`, or the two unequal nodes `2+i/11,3+i/13`; high sets were `5+i/17,7+i/19`, with the final high set empty in the weak-grounding/empty-transition cases. Exact positive-semidefinite elimination verified (7), (8), and the parity compression of `epsilon A-E`. Eliminating the full constant sector together with transitions also exactly gave the diagonal congruence of the transition-shorted nonconstant form. These checks stress near-constant carriers, duplicated nodes, empty sectors, extreme conductances and remote relaxation. They verify finite algebra only; (10) and (20) rest on the completion proofs above. Scratch is outside Git. No Lean verification or independent adversarial approval is claimed.

The following boundaries remain substantive:

- A fixed wider transition band need not satisfy `gamma>R delta`; failure of this sufficient condition proves no compactness.
- The model's ground terms multiply the same scalar Cauchy norm. Actual Fourier-diagonal seam energy, trace transport, and nonsingular pant terms are not automatically covered.
- Removing a finite set of global vectors, imposing an arbitrary constraint on means, or eliminating only selected module constants is not the complete-sector operation in Section 4.
- The theorem uses the closure of finitely supported fields and eliminated variables in the specified energy. It does not identify every finite-energy boundary condition at infinity with that completion.
- Comparable nonprime periods have the same obstruction. Essential angle norm one excludes compact Schatten and weak-Schatten classes for this model angle; it proves no intrinsic scattering formula, zeta-zero statement, or RH consequence.

The actual surface test is still the residual-scale comparison and completion identification stated in PF-359. This result prevents mean removal from being treated as an untested cure for the Cauchy model, but does not replace that PDE test with another model estimate.
