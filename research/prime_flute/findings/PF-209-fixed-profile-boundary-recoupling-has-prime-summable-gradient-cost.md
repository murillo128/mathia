# PF-209 — fixed-profile boundary recoupling has prime-summable gradient cost

**Status:** `LITERATURE+DERIVED + EXACT-MODEL + STRONG-S1-ERROR-CONTROL + POSITIVE/ROUTE-NARROWING`. PF-207 proves that dilation of the whole Dirichlet critical block restores the physical `w_n^2` scale lost by coefficient-only normalization, and PF-208 proves that scale-matched cutoff commutators preserve that scale and are strongly trace-summable. The next possible failure mode is the artificial boundary introduced by those Dirichlet cells. Classical boundary pseudodifferential/Krein theory shows that, on a fixed smooth two-dimensional buffer, an uncut-versus-Dirichlet-cut first-resolvent correction is a singular Green operator of order `-2`. After one gradient it is order `-1`, hence weak trace class on the one-dimensional interface and in every strong `S_p`, `p>1`. Exact physical dilation then gives a factor `w` for the gradient recoupling correction. Pairing one such correction with the ordinary Dirichlet gradient-resolvent factor makes every quadratic coefficient error **strong trace class with cost `O(w^2 ||F||_infty)`**. For the PF-205/PF-206 seam mesh this is `O(d_n^3)` per cell and `O(d_n^3+a_n d_n^2)` per module, which is prime-summable. Thus a fixed-profile finite-buffer transmission correction has exactly the currency needed by the smooth-seam endpoint route. What remains open is the genuinely global step: proving that the native two-metric hyperbolic resolvents can be reduced uniformly to this fixed-buffer calculus without a low-frequency exterior/identification loss, together with the still-separate PF-204 piecewise-transport and PF-183 true-short-collar gates.

## Claim

Let `Q` be a fixed bounded smooth planar domain with outer Dirichlet boundary, and let a smooth compact interior interface `Sigma` split it into two smooth subdomains `Q_-` and `Q_+`. Let `A` be a positive self-adjoint second-order uniformly strongly elliptic realization on `Q`, with Dirichlet condition on the outer boundary and ordinary transmission across `Sigma`. Let

\[
A^D=A_-^D\oplus A_+^D
\tag{1}
\]

be the decoupled realization obtained by imposing an additional Dirichlet condition on both sides of `Sigma`. For `0\le t\le1` write

\[
R_t=(A+t)^{-1},\qquad R_t^D=(A^D+t)^{-1},
\tag{2}
\]

and, using the natural scalar-to-cotangent gradient for the same elliptic metric,

\[
\Gamma_t=\nabla R_t,\qquad
\Gamma_t^D=\nabla R_t^D,\qquad
B_t:=\Gamma_t-\Gamma_t^D
      =\nabla(R_t-R_t^D).
\tag{3}
\]

For one fixed smooth model, and uniformly for a bounded smooth elliptic family with the same fixed interface geometry and a common positive Dirichlet gap, classical boundary calculus gives

\[
\boxed{
\sup_{0\le t\le1}
\|B_t\|_{\mathcal S_{4/3}}<\infty,
\qquad
\sup_{0\le t\le1}
\|\Gamma_t^D\|_{\mathcal S_4}<\infty.
}
\tag{4}
\]

More precisely, `R_t-R_t^D` is a boundary singular Green correction of order `-2`; composition with the first-order gradient gives a singular Green operator of order `-1`. In dimension two the interface has dimension one, so the latter lies in

\[
\mathcal S_{1,\infty}
\subset \mathcal S_p
\qquad(p>1),
\tag{5}
\]

and in particular in `S_{4/3}`. The ordinary Dirichlet gradient-resolvent has singular values of order `k^{-1/2}` on a bounded planar domain and therefore belongs uniformly to `S_p` for every `p>2`, in particular `S_4`.

Now scale the whole local model isotropically. Let `Q_w=wQ`, `Sigma_w=wSigma`, `0<w\le1`, and let `A_w,A_w^D` be the corresponding scaled realizations. Put

\[
R_w=(1+A_w)^{-1},\qquad
R_w^D=(1+A_w^D)^{-1},
\tag{6}
\]

\[
G_w=\nabla R_w,\qquad
G_w^D=\nabla R_w^D,\qquad
C_w:=G_w-G_w^D.
\tag{7}
\]

With the scalar and vector-valued two-dimensional unitary dilations `U_w,V_w` used in PF-207/PF-208, exact scaling gives

\[
U_wR_wU_w^{-1}=w^2(A+w^2)^{-1},
\qquad
U_wR_w^DU_w^{-1}=w^2(A^D+w^2)^{-1},
\tag{8}
\]

and therefore

\[
\boxed{
V_wC_wU_w^{-1}=wB_{w^2},
\qquad
V_wG_w^DU_w^{-1}=w\Gamma_{w^2}^D.
}
\tag{9}
\]

Consequently

\[
\boxed{
\|C_w\|_{\mathcal S_{4/3}}\le Cw,
\qquad
\|G_w^D\|_{\mathcal S_4}\le Cw.
}
\tag{10}
\]

The same estimate holds for two fixed-profile source/target elliptic models `g,h` with uniform constants. Let `F_w` be a bounded scalar or fixed-fibre matrix coefficient on `Q_w`, and compare the uncut and Dirichlet-decoupled quadratic gradient-resolvent words

\[
T_w=(G_{h,w})^*M_{F_w}G_{g,w},
\qquad
T_w^D=(G_{h,w}^D)^*M_{F_w}G_{g,w}^D.
\tag{11}
\]

Writing `C_{k,w}=G_{k,w}-G_{k,w}^D`, the exact expansion is

\[
T_w-T_w^D
=C_{h,w}^*M_{F_w}G_{g,w}^D
+(G_{h,w}^D)^*M_{F_w}C_{g,w}
+C_{h,w}^*M_{F_w}C_{g,w}.
\tag{12}
\]

Schatten Holder, (10), and `S_{4/3}\subset S_2` imply

\[
\boxed{
\|T_w-T_w^D\|_1
\le Cw^2\|F_w\|_\infty.
}
\tag{13}
\]

Indeed the two cross terms use

\[
\frac1{4/3}+\frac14=1,
\tag{14}
\]

while the double-recoupling term may be estimated in `S_1` from the two `S_2` norms.

For one PF-205/PF-206 natural-width seam cell,

\[
w_n\asymp d_n,
\qquad
\|C_{n,j}\|_\infty\le Cd_n,
\tag{15}
\]

so the fixed-profile boundary-recoupling model has

\[
\boxed{
\|T_{n,j}-T_{n,j}^D\|_1\le Cd_n^3.
}
\tag{16}
\]

PF-206 gives

\[
N_n\le C\left(1+\frac{a_n}{d_n}\right),
\tag{17}
\]

hence the complete model family obeys

\[
\boxed{
\sum_{j\le N_n}
\|T_{n,j}-T_{n,j}^D\|_1
\le C(d_n^3+a_nd_n^2).
}
\tag{18}
\]

Since PF-107/PF-205 give `d_n\asymp P_n^{-1}` and `a_n=O(log P_n)`, the right-hand side is summable over the prime/shift tail:

\[
\boxed{
\sum_n(d_n^3+a_nd_n^2)<\infty.
}
\tag{19}
\]

Equation (19) is deliberately a **fixed-profile finite-buffer boundary statement**. It proves that the microlocal transmission correction generated by a scale-matched Dirichlet cut has the correct Schatten and physical-scale currency once it is embedded in the quadratic gradient-resolvent word. It does **not** yet prove that the native PF global resolvents admit this reduction with a uniform bounded exterior/interface map.

## 1. Boundary calculus gives order `-2`, and the gradient leaves weak trace order

The required scalar boundary fact is classical. For a second-order elliptic operator on a smooth domain, Krein resolvent formulas express the difference between two elliptic realizations through Poisson and boundary Dirichlet-to-Neumann/Neumann-to-Dirichlet operators. The Dirichlet-versus-Neumann or mixed-versus-Dirichlet first-resolvent correction is a singular Green operator of order `-2`. The same calculus applies after cutting a fixed smooth interface and writing ordinary transmission as an elliptic matrix boundary condition on the disjoint union of the two sides.

In the smooth case, a singular Green operator of negative order `-s` on an `n`-dimensional domain has boundary-controlled singular values

\[
s_k=O\!\left(k^{-s/(n-1)}\right).
\tag{20}
\]

Thus for `n=2` the scalar order-`-2` correction has `s_k=O(k^{-2})` and is much better than trace class. Composing on the left with a first-order differential operator respects the Boutet de Monvel order rule and turns it into an order-`-1` singular Green operator. Therefore

\[
s_k(B_t)=O(k^{-1}),
\tag{21}
\]

which is precisely weak `S_1`; every strong `S_p`, `p>1`, follows. Choosing `p=4/3` is not an endpoint claim but merely the exponent that pairs exactly with the ordinary `S_4` gradient-resolvent factor in (14).

The parameter `t\in[0,1]` does not create a small-eigenvalue problem in this fixed-buffer theorem because the outer Dirichlet problem has a positive first eigenvalue. The resolvent family therefore stays in one compact parameter set away from the spectrum, and the finite collection of boundary-symbol/operator seminorms entering the estimates remains uniformly bounded.

This is also why the result should not be applied blindly to a global noncompact exterior problem after rescaling. There, the scaled spectral parameter can approach the bottom of continuous spectrum and a low-frequency exterior Dirichlet-to-Neumann mode may require separate control. The present finding isolates exactly what boundary microlocal order contributes **once that global-to-buffer reduction has been justified**.

## 2. Exact dilation returns the same `w^2` budget as PF-207/PF-208

The key bookkeeping is identical to the previous two findings but now applied to a boundary correction. Under two-dimensional unitary dilation, a first resolvent contributes `w^2` and a gradient costs one `w^{-1}`. Therefore both the ordinary Dirichlet gradient-resolvent and its recoupling difference carry one net factor `w`, as shown in (9).

This matters because estimating a boundary operator only by its abstract membership in a fixed Schatten class would forget the physical cell size in exactly the same way that PF-206's coefficient-only unit-box normalization did. The full scaled operator gives

\[
\text{gradient recoupling}\sim w,
\qquad
\text{ordinary gradient resolvent}\sim w,
\tag{22}
\]

so a quadratic word with one boundary correction has the physical factor `w^2` before the coefficient is charged. The small PF seam coefficient then contributes one further `d_n\asymp w_n`, yielding the per-cell `d_n^3` budget in (16).

The double-recoupling word is not worse. Although each `C_w` is only weak trace at the sharp boundary order, using the nonendpoint inclusion `S_{4/3}\subset S_2` on both sides makes the product trace class with the same `w^2` scaling. No endpoint product theorem is required.

## 3. Relation to PF-172: no contradiction with the zero-mode recoupling obstruction

PF-172 proves a superficially opposite statement for a collapsing hyperbolic collar: the **scalar** first-resolvent difference between an uncut collar and a central Dirichlet cut is trace class, but its absolute trace norm has a positive lower bound independent of the shrinking core length. The angular zero mode survives the collapse and prevents one from summing scalar single-surface recoupling corrections by interface length alone.

PF-209 does not weaken that obstruction. There are two decisive differences.

First, the object here is the **gradient of the resolvent correction inside a quadratic coefficient word**, not the scalar resolvent correction itself. Boundary calculus loses one order under the gradient but the second order-`-1` gradient factor in the quadratic word restores the full `w^2` physical dilation. PF-172's scalar zero-mode lower bound therefore cannot be inserted as a lower bound for (13).

Second, the PF-205/PF-206 seam cells are **isotropically scale-matched**: both local directions are `O(w_n)`. PF-172 studies a genuinely anisotropic collar collapse in which the core circumference tends to zero while a fixed radial width survives. Its order-one radial zero-mode correction is exactly the geometry that isotropic cell dilation does not model.

Accordingly the safe conclusion is narrow: PF-172 still forbids absolute scalar recoupling of infinitely many true shrinking collar interfaces. PF-209 says that **finite-buffer isotropic artificial cell boundaries**, when they arise inside the critical gradient-resolvent seam factorization, have a much cheaper quadratic Schatten currency.

## 4. What this closes and what remains open

PF-208 left four effects grouped around the smooth-seam global/local bridge: cutoff commutators, artificial boundary/transmission, varying-metric comparison, and global reassembly. Its exact commutator algebra closed the first item. PF-209 closes the next item only at the fixed-profile finite-buffer level:

\[
\boxed{
\text{fixed-buffer boundary microlocal order + physical dilation}
\Longrightarrow
\text{prime-summable strong-}S_1\text{ quadratic error}.
}
\tag{23}
\]

Therefore a later global proof does not need an unexpectedly strong boundary Schatten theorem. The classical order `-2` resolvent correction is already enough after the PF gradient structure and exact cell dilation are included.

The unresolved step is more specific. One must produce a global-to-local identity for the **native** PF source/target resolvents in which the finite-buffer boundary terms really occur with uniformly bounded outer maps. In particular, one must rule out a low-frequency loss from the large/noncompact exterior after rescaling, control the source/target varying-metric identification on those buffers, and reassemble the cells without replacing a bounded-overlap Hilbert estimate by an unjustified absolute sum of scalar recoupling norms.

This is consistent with PF-201's lesson on the regular Lambert body: whenever possible, keep the global resolvents intact and move critical bookkeeping to an auxiliary local direct sum. The present boundary theorem is a fallback/local bridge for the shrinking seam cells, not a reason to introduce Dirichlet cuts where they are unnecessary.

PF-204's unsmoothed two-Hilbert-space factorization remains independent: it may avoid these artificial boundaries entirely if the piecewise cotangent transport admits a direct critical estimate. PF-183's true-short-collar conservative splice also remains untouched.

## 5. Prior-art and novelty audit

The boundary analysis is classical. Relevant sources include:

- **G. Grubb**, *The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates*, Journal of Mathematical Analysis and Applications **382** (2011), 339--363, DOI `10.1016/j.jmaa.2011.04.055`, arXiv:1104.0785. The mixed-versus-Dirichlet resolvent difference has boundary-dimensional asymptotics `s_j\asymp j^{-2/(n-1)}` in the principally Laplace case.
- **J. Behrndt, M. Langer, I. Lobanov, V. Lotoreichik, I. Yu. Popov**, *A remark on Schatten-von Neumann properties of resolvent differences of generalized Robin Laplacians on bounded domains*, Journal of Mathematical Analysis and Applications **371** (2010), 750--758, DOI `10.1016/j.jmaa.2010.06.006`, arXiv:0911.2443. This records strong Schatten estimates for boundary-condition resolvent differences and the classical Dirichlet/Neumann scale.
- **G. Grubb**, *Spectral asymptotics for nonsmooth singular Green operators*, Communications in Partial Differential Equations **39** (2014), 530--573, DOI `10.1080/03605302.2013.864207`, arXiv:1205.0094. It identifies Krein boundary corrections as singular Green operators, gives the boundary-dimensional weak-ideal estimate for negative-order singular Green operators, and develops composition rules with truncated pseudodifferential operators. It also treats order-`-2` Dirichlet-versus-Neumann-type corrections under `W^1_q`, `q>n`, coefficient regularity.
- **J. Behrndt, G. Grubb, M. Langer, V. Lotoreichik**, *Spectral asymptotics for resolvent differences of elliptic operators with delta and delta-prime interactions on hypersurfaces*, Journal of Spectral Theory **5** (2015), 697--729, DOI `10.4171/JST/111`. Its interface Krein calculus is nearby prior art for viewing a smooth separating hypersurface through coupled/decoupled boundary realizations.

No novelty is claimed for the Krein formula, singular Green classification, boundary Weyl law, ideal inclusions, or Schatten Holder inequality. A structure-directed search found the expected boundary-condition/interface literature and therefore rules out presenting the fixed-cell operator statement as new abstract spectral theory.

The project-specific deduction is the scale-sensitive conjunction with PF-205--PF-208: **after taking the gradient, dilating the complete boundary correction, and pairing it with the second gradient-resolvent factor, the classical boundary ideal gives exactly `O(w_n^2 ||C_{n,j}||_infty)` strong-trace error; the PF seam geometry turns this into the summable module budget `O(d_n^3+a_nd_n^2)`.** That is the new information for the prime-flute research line. Search absence is not used as evidence of novelty beyond this construction-specific deduction.

## 6. Falsification and boundary checks

A later adversary can audit PF-209 by:

1. checking the precise realization used for the fixed buffer: outer Dirichlet boundary, ordinary transmission across the smooth interior interface, and additional Dirichlet conditions on both interface sides for `A^D`;
2. deriving the Krein/Poisson representation of `R_t-R_t^D` after cutting along `Sigma`, or reducing through standard Dirichlet/Neumann/mixed realizations, and verifying that the correction is singular Green order `-2`;
3. applying the boundary calculus composition rule to one gradient and checking that the result is order `-1`, class zero, hence weak `S_1` in dimension two;
4. checking the uniformity in `t\in[0,1]` from the fixed outer Dirichlet spectral gap rather than assuming uniformity at a noncompact spectral threshold;
5. reproducing the scalar/vector unitary dilations in (8)--(10), with one net factor `w` for each gradient-resolvent or gradient-recoupling factor;
6. checking the exponent arithmetic `S_{4/3} S_4 subset S_1` and the `S_2 S_2 subset S_1` estimate for the double-recoupling term;
7. inserting PF-205/PF-206's actual `w_n`, coefficient `L^infty` envelope and cell count to reproduce (16)--(19);
8. refusing to transfer the fixed-buffer constant to a rescaled noncompact exterior unless the low-frequency boundary map and required coefficient regularity are controlled uniformly;
9. keeping PF-172's anisotropic scalar zero-mode obstruction intact and not using (13) to sum absolute true-collar recoupling corrections;
10. keeping varying-metric global identification, PF-204 piecewise cotangent transport, PF-183 short-collar splicing, wave/scattering/determinant conclusions and every RH claim outside the finding.

The result would need narrowing if the relevant artificial interface cannot be represented by a uniformly smooth fixed-profile buffer after scaling, if the global-to-buffer reduction introduces an outer factor whose norm grows faster than the available `w_n` budget, or if a proposed reassembly estimates scalar recoupling corrections before the gradient/coefficient cancellation in (12) is formed.

## Consequences for the research line

The smooth seam endpoint has now passed three increasingly realistic scale tests. PF-207 shows that the principal Dirichlet critical block retains `w_n^2`; PF-208 shows that scale-matched cutoff commutators retain it and even become strongly trace class; PF-209 shows that **the classical fixed-buffer transmission correction also retains it once measured in the actual quadratic gradient-resolvent word**.

The next smooth-route question is therefore no longer whether a two-dimensional artificial boundary has enough Schatten smoothing. It does. The useful question is whether the native global hyperbolic resolvents admit a uniformly bounded global-to-buffer factorization at the shrinking seam scale, especially through the low-frequency exterior/interface map, and whether the source/target metric comparison can be carried through that factorization without consuming the prime-summable `a_nd_n^2` budget.

As in PF-207/PF-208, this is analytic control shared by the exact prime flute and its all-composite shift clone. It supplies no prime/clone separator and no RH mechanism by itself.