# PF-208 — scale-matched Dirichlet cutoff commutators are trace-summable

**Status:** `EXACT-DERIVED + CLASSICAL-TOOLS + STRONG-S1-ERROR-CONTROL + POSITIVE/ROUTE-NARROWING`. PF-207 restores the physical `w_n^2` scale for the critical Dirichlet model blocks attached to PF-205/PF-206 seam cells, but leaves a concrete warning: differentiating a cutoff on a `w_n`-cell costs `w_n^{-1}`, so a global-to-Dirichlet comparison could in principle spend the restored scale. That raw derivative loss is **not intrinsic to the scale-matched Dirichlet gradient-resolvent algebra**. If the cutoff is kept inside the commutator with the full order-`-1` factor `G_w=\nabla(1-\Delta^D_{Q_w})^{-1}`, exact dilation gives

\[
[G_w,M_{\chi_w}]
\quad\longleftrightarrow\quad
w\,[\nabla(A+w^2)^{-1},M_\chi],
\]

not a factor `w^{-1}`. On one fixed two-dimensional Dirichlet reference cell the rescaled commutator is uniformly in `\mathcal S_{4/3}`, while the rescaled gradient-resolvent is uniformly in `\mathcal S_4`. Hence every quadratic coefficient word containing one such cutoff commutator is **strong trace class** with trace norm `O(w^2\|F\|_\infty)`; words containing two commutators obey the same scale. For the PF-205/PF-206 isotropic seam mesh, `w_n\asymp d_n`, `\|F_{n,j}\|_\infty=O(d_n)`, and `N_n=O(1+a_n/d_n)`, so the complete family of these model cutoff-commutator errors has total trace norm

\[
O(d_n^3+a_nd_n^2)
\]

per module and is absolutely summable over the prime/shift tail. Thus the **bare derivative of a scale-matched partition is not itself the remaining PF-207 obstruction**. What remains genuinely open is the comparison of the native global hyperbolic gradient resolvents with the independently Dirichlet-decoupled cells, including artificial-boundary/transmission terms, varying-metric comparison and global reassembly; the PF-204 piecewise cotangent transport remains separate in the unsmoothed architecture. The PF-183 true-short-collar endpoint splice is also untouched.

## Claim

Let `Q\subset\mathbb R^2` be one fixed bounded Lipschitz reference cell and `Q_w=wQ`, with `0<w\le1`. Write

\[
A_w=-\Delta^D_{Q_w},
\qquad
A=-\Delta^D_Q,
\qquad
R_w=(1+A_w)^{-1},
\qquad
G_w=\nabla R_w.
\tag{1}
\]

Let

\[
(U_wu)(y)=w\,u(wy),
\qquad
(V_w\alpha)(y)=w\,\alpha(wy)
\tag{2}
\]

be the scalar and vector-valued two-dimensional unitary dilations from `Q_w` to `Q`. Put

\[
t=w^2,
\qquad
R_t=(A+t)^{-1},
\qquad
\Gamma_t=\nabla R_t.
\tag{3}
\]

Then

\[
U_wR_wU_w^{-1}=w^2R_t,
\qquad
V_wG_wU_w^{-1}=w\Gamma_t.
\tag{4}
\]

For one fixed `\chi\in W^{2,\infty}(Q)` and the scale-matched cutoff

\[
\chi_w(x)=\chi(x/w),
\tag{5}
\]

interpret the gradient commutator as

\[
[G_w,M_{\chi_w}]
:=G_wM_{\chi_w}-M_{\chi_w}G_w,
\tag{6}
\]

where the second multiplier acts on vector fields. Exact dilation gives

\[
\boxed{
V_w[G_w,M_{\chi_w}]U_w^{-1}
=wJ_t,
\qquad
J_t:=[\Gamma_t,M_\chi].
}
\tag{7}
\]

There is a constant depending only on the fixed cell and cutoff such that, uniformly for `0\le t\le1`,

\[
\boxed{
\|\Gamma_t\|_{\mathcal S_4}\le C,
\qquad
\|J_t\|_{\mathcal S_{4/3}}\le C.
}
\tag{8}
\]

In particular `J_t\in\mathcal S_2` uniformly as well.

Let `F_w` be a bounded scalar or fixed-fibre matrix coefficient on `Q_w` and `\widetilde F_w(y)=F_w(wy)`. Then the three model localization-error words

\[
E_w^{(L)}=[G_w,M_{\chi_w}]^*M_{F_w}G_w,
\tag{9}
\]

\[
E_w^{(R)}=G_w^*M_{F_w}[G_w,M_{\chi_w}],
\tag{10}
\]

and, for another fixed scale-matched cutoff `\psi_w`,

\[
E_w^{(2)}=[G_w,M_{\chi_w}]^*M_{F_w}[G_w,M_{\psi_w}]
\tag{11}
\]

are trace class and satisfy

\[
\boxed{
\|E_w^{(L)}\|_1+
\|E_w^{(R)}\|_1+
\|E_w^{(2)}\|_1
\le Cw^2\|F_w\|_\infty.
}
\tag{12}
\]

For the PF-205/PF-206 seam mesh, take `w=w_n\asymp d_n` and `F_w=C_{n,j}`. The established pointwise and counting estimates are

\[
\|C_{n,j}\|_\infty\le Cd_n,
\qquad
N_n\le C\left(1+\frac{a_n}{d_n}\right).
\tag{13}
\]

Therefore the sum of the trace norms of all model error words of the forms (9)--(11) in module `n` obeys

\[
\boxed{
\sum_{j\le N_n}\|E_{n,j}\|_1
\le C\left(d_n^3+a_nd_n^2\right),
}
\tag{14}
\]

and PF-107/PF-205 give

\[
d_n\asymp P_n^{-1},
\qquad
a_n=O(\log P_n),
\tag{15}
\]

so

\[
\boxed{
\sum_n\sum_{j\le N_n}\|E_{n,j}\|_1<\infty.
}
\tag{16}
\]

Equation (16) is a **model localization statement**. It does not identify the actual PF seam resolvent with a direct sum of these Dirichlet cells.

## 1. Whole-operator dilation reverses the apparent cutoff loss

PF-207 already uses

\[
U_wA_wU_w^{-1}=w^{-2}A.
\tag{17}
\]

Since

\[
(1+w^{-2}A)^{-1}=w^2(A+w^2)^{-1},
\tag{18}
\]

the first identity in (4) follows. The gradient itself scales by

\[
V_w\nabla U_w^{-1}=w^{-1}\nabla,
\tag{19}
\]

and combining (18)--(19) yields the second identity in (4).

The cutoff multiplier is scale-free under these unitaries:

\[
U_wM_{\chi_w}U_w^{-1}=M_\chi,
\qquad
V_wM_{\chi_w}V_w^{-1}=M_\chi.
\tag{20}
\]

Consequently (7) is exact. This is the key bookkeeping point. If one differentiates `\chi_w` in isolation, one sees `\|\nabla\chi_w\|_\infty=O(w^{-1})`. If instead one keeps the derivative inside the resolvent commutator from which it arose, the resolvent and gradient scaling contribute enough positive powers that the **entire commutator is `w` times a fixed-cell operator**.

This does not say that every possible localization scheme is harmless. It says that the specific `w^{-1}` derivative visible in a scale-matched IMS/geometric-resolvent expansion must not be charged before the accompanying resolvent factors are included.

## 2. The fixed-cell commutator gains one Schatten order

Let `\lambda_k` be the Dirichlet eigenvalues of `A`. On a fixed bounded planar cell,

\[
\lambda_k\asymp k.
\tag{21}
\]

Hence, uniformly for `0\le t\le1`,

\[
R_t\in\mathcal S_p
\quad(p>1),
\qquad
A^{1/2}R_t\in\mathcal S_p
\quad(p>2).
\tag{22}
\]

The Dirichlet form identity gives

\[
\Gamma_t^*\Gamma_t=R_tAR_t,
\tag{23}
\]

so the singular values of `\Gamma_t` are

\[
s_k(\Gamma_t)=\frac{\sqrt{\lambda_k}}{\lambda_k+t},
\tag{24}
\]

up to the natural identification with the closure of gradients. Thus `\Gamma_t\in\mathcal S_p` uniformly for every `p>2`, in particular `\mathcal S_4` and `\mathcal S_{8/3}`.

The resolvent commutator identity is

\[
[R_t,M_\chi]
=-R_t[A,M_\chi]R_t,
\tag{25}
\]

and the product rule gives

\[
\boxed{
J_t
=M_{\nabla\chi}R_t
-\Gamma_t[A,M_\chi]R_t.
}
\tag{26}
\]

For the Dirichlet Laplacian,

\[
[A,M_\chi]
=-M_{\Delta\chi}-2\nabla\chi\cdot\nabla.
\tag{27}
\]

Multiplication by `\chi\in W^{2,\infty}` preserves `H_0^1(Q)`, and therefore

\[
[A,M_\chi]A^{-1/2}:L^2(Q)\to L^2(Q)
\tag{28}
\]

is bounded. It follows from (22) that

\[
[A,M_\chi]R_t
=([A,M_\chi]A^{-1/2})(A^{1/2}R_t)
\in\mathcal S_p
\quad(p>2)
\tag{29}
\]

uniformly in `t`.

Choose `p=8/3`. The second term in (26) is then a product of two `\mathcal S_{8/3}` operators and belongs to `\mathcal S_{4/3}` by Schatten Hölder. The first term belongs to `\mathcal S_{4/3}` because `R_t\in\mathcal S_{4/3}`. This proves the second estimate in (8). No endpoint commutator theorem is needed for this fixed-cell strong-ideal gain.

## 3. One commutator makes the quadratic error strongly trace class

Under the scalar/vector unitary dilations, (9) becomes

\[
U_wE_w^{(L)}U_w^{-1}
=w^2J_t^*M_{\widetilde F_w}\Gamma_t.
\tag{30}
\]

Using

\[
\frac1{4/3}+\frac14=1,
\tag{31}
\]

Schatten Hölder and (8) give

\[
\|E_w^{(L)}\|_1
\le Cw^2\|\widetilde F_w\|_\infty
=Cw^2\|F_w\|_\infty.
\tag{32}
\]

The right-commutator term is identical after taking adjoints. For the double-commutator word, `\mathcal S_{4/3}\subset\mathcal S_2`, so

\[
\|J_t^*M_{\widetilde F_w}J_t'\|_1
\le
\|J_t\|_2\|F_w\|_\infty\|J_t'\|_2,
\tag{33}
\]

again with the physical prefactor `w^2`. This proves (12).

The estimate is deliberately in the **strong** trace ideal. The principal Dirichlet block in PF-207 is critical and only requires weak `\mathcal S_1`; the localization commutator has gained enough smoothing that it is cheaper than the principal term. Thus, inside this fixed-cell algebra, the dangerous object is not the derivative of the cutoff by itself but any boundary/global comparison term that cannot be organized into a commutator with the full resolvent factor.

The same proof tolerates a fixed finite-dimensional cotangent fibre: multiplication by a matrix coefficient contributes only its operator norm and a fixed fibre constant.

## 4. PF seam counting preserves the restored area scale

PF-205 supplies the natural seam width and pointwise coefficient scale, while PF-206 supplies the isotropic cell count. Substituting (13) into (12) gives, per cell,

\[
\|E_{n,j}\|_1
\le Cw_n^2d_n
\asymp Cd_n^3.
\tag{34}
\]

Therefore

\[
\sum_{j\le N_n}\|E_{n,j}\|_1
\le
Cd_n^3\left(1+\frac{a_n}{d_n}\right)
=C(d_n^3+a_nd_n^2),
\tag{35}
\]

which is (14). The tail is summable because

\[
a_nd_n^2
=O\!\left(\frac{\log P_n}{P_n^2}\right).
\tag{36}
\]

This is slightly different from PF-207's principal-block mechanism. PF-207 multiplies the **normalized critical `L\log L` budget** by the dilation factor `w_n^2`. Here the commutator has already gained a strong Schatten order, so the bounded coefficient envelope is enough; the same `w_n^2` physical scale survives after summing the `O(a_n/d_n)` cells.

Consequently PF-207's warning can be narrowed:

\[
\boxed{
\text{raw }\nabla\chi_{w_n}\sim w_n^{-1}
\quad\not\Rightarrow\quad
\text{loss of the }w_n^2\text{ endpoint budget}.
}
\tag{37}
\]

A loss occurs only if the localization algebra separates that derivative from the order-`-1` resolvent structure or creates additional boundary/transmission operators whose scaling has not been controlled.

## 5. Prior-art and novelty audit

The ingredients used in the proof are classical: unitary dilation of the Dirichlet Laplacian, the resolvent commutator identity, Weyl eigenvalue growth on a fixed bounded planar domain, boundedness of first-order differential operators from `H_0^1` to `L^2`, and Hölder inequalities for Schatten ideals. No novelty is claimed for the abstract statement that commutators with smooth multipliers gain operator order.

Nearby modern endpoint work includes **R. L. Frank, F. Sukochev, D. Zanin**, *Endpoint Schatten class properties of commutators*, Advances in Mathematics **450** (2024), 109738, DOI `10.1016/j.aim.2024.109738`, arXiv:2405.10652. Their results concern commutators of fractional powers of the Euclidean Laplacian on `\mathbb R^d` and are not imported to prove (8); the fixed-cell resolvent identity above already gives the stronger-than-needed nonendpoint classes used here.

The next PF-207 gate has substantial classical boundary-resolvent prior art but is not automatically solved by it. **J. Behrndt, M. Langer, I. Lobanov, V. Lotoreichik, I. Yu. Popov**, *A remark on Schatten-von Neumann properties of resolvent differences of generalized Robin Laplacians on bounded domains*, J. Math. Anal. Appl. **371** (2010), 750--758, DOI `10.1016/j.jmaa.2010.06.006`, arXiv:0911.2443, obtains strong Schatten estimates for boundary-condition resolvent differences and recalls classical Birman Dirichlet/Neumann results. **G. Grubb**, *The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates*, J. Math. Anal. Appl. **382** (2011), 339--363, DOI `10.1016/j.jmaa.2011.04.055`, arXiv:1104.0785, gives Krein-type formulas and boundary-dimensional singular-value asymptotics for mixed-versus-Dirichlet resolvent differences.

Those boundary results strengthen the case that the **artificial-boundary term itself is the right next object to isolate**, but they do not identify the PF global two-metric gradient-resolvent seam operator with the required decoupled family, do not provide the PF scale bookkeeping automatically, and do not handle the PF-204 cotangent transport. Search absence is not used as evidence of novelty.

The project-specific result is therefore the conjunction of exact scale bookkeeping with PF-205/PF-206: **the particular `w_n^{-1}` cutoff derivative flagged by PF-207 is absorbed when it is kept in the full Dirichlet gradient-resolvent commutator, and all quadratic coefficient error words generated that way are strongly trace-summable across the entire seam mesh.**

## 6. Falsification and boundary checks

A later adversary can test PF-208 by:

1. checking the scalar and vector unitary dilations (2), especially the factor `w^{-1}` in (19) and the resulting factor `w` in (4);
2. verifying (7) directly, rather than estimating `\nabla\chi_w` separately;
3. using the Dirichlet form identity to reproduce the singular values (24) and the uniform `\mathcal S_p`, `p>2`, bound for `\Gamma_t`;
4. deriving (25)--(27) with the correct commutator sign and checking that `[A,M_\chi]A^{-1/2}` is bounded on the fixed cell;
5. checking the exponent arithmetic `\mathcal S_{8/3}\mathcal S_{8/3}\subset\mathcal S_{4/3}` and `\mathcal S_{4/3}\mathcal S_4\subset\mathcal S_1`;
6. checking that the coefficient multiplier in (30) is bounded and that finite fibre dimension changes only the constant;
7. inserting PF-205/PF-206's actual `\|C_{n,j}\|_\infty`, `w_n` and `N_n` bounds to reproduce (35)--(36);
8. refusing to infer from (16) that the native global hyperbolic resolvent has been replaced by a Dirichlet direct sum;
9. keeping boundary Poisson/Krein terms, transmission across artificial cell boundaries, varying-metric comparison and finite-overlap global reassembly outside the claim unless separately proved;
10. keeping the PF-204 piecewise transport, PF-183 true-short-collar splice, wave/scattering/determinant consequences and every RH claim outside this finding.

The result would need narrowing if the cutoff is not scale-matched to a fixed reference profile, if a proposed localization creates terms not representable by the model words (9)--(11), or if an artificial-boundary operator has worse scaling than these internal commutators. None of those possibilities contradicts the exact model estimate proved here.

## Consequences for the research line

PF-206 showed that coefficient-only normalization can erase the small physical area. PF-207 showed that dilation of the **whole principal Dirichlet critical block** restores it. PF-208 now shows the same lesson survives the first natural localization stress test: **scale-matched cutoff commutators are not only scale-correct but strongly trace-summable** when the whole gradient-resolvent factor is retained.

The smooth-seam route is therefore narrower again. It no longer needs a generic theorem saying that every `w_n^{-1}` partition derivative is harmless. It needs an explicit global-to-local resolvent identity whose nonprincipal pieces are separated into (a) internal cutoff commutator words of the kind closed here and (b) genuine artificial-boundary/transmission and varying-metric comparison terms. The latter class is now the first unresolved operator gate. Alternatively, PF-204's unsmoothed two-Hilbert-space route can still bypass artificial Dirichlet boundaries if its piecewise cotangent transport admits a direct critical estimate.

As with PF-207, this is analytic control shared by the exact prime flute and its all-composite shift clone. It provides no prime/clone separator and no RH mechanism by itself.