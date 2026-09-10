# MC-198 — Centered primorial residue polynomials retain a same-class top interaction

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

For an uncentered classwise polynomial in the signed/support residue aggregates of a ternary source, the collision-partition argument gives a triangular expansion whose highest polynomial degree is a genuine highest distinct-source interaction order. That part of the previous analysis is correct.

Centering needs a different argument. The centered averages are themselves source-dependent, so one cannot treat centering as translation by fixed constants. In particular, when there are exactly two classes, every odd homogeneous polynomial cancels after centering. Nevertheless, in the actual logarithmic-primorial regime, where the number of reduced residue classes is eventually larger than two, the intended top-interaction conclusion survives with an explicit coefficient.

Fix `phi>=2` residue classes. In class `b`, let the source values be

\[
x_{b,i}\in\{-1,0,1\},
\]

and define

\[
A_b=\sum_i x_{b,i},
\qquad
B_b=\sum_i x_{b,i}^2,
\qquad
S=\sum_b A_b,
\qquad
Q=\sum_b B_b.
\tag{1}
\]

Put

\[
u_a=A_a-\frac S\phi,
\qquad
v_a=B_a-\frac Q\phi.
\tag{2}
\]

Let `P(U,V)` have effective total degree `d>=2`, and write its top homogeneous part as

\[
H_d(U,V)=\sum_{r+s=d}c_{r,s}U^rV^s.
\tag{3}
\]

For each class `b`, let

\[
D_{r,s}(b)
:=
\sum_{\substack{i_1,\ldots,i_r,j_1,\ldots,j_s\\
\text{all distinct in class }b}}
 x_{b,i_1}\cdots x_{b,i_r}
 x_{b,j_1}^2\cdots x_{b,j_s}^2.
\tag{4}
\]

Then the order-`d` part of

\[
F_P:=\sum_{a=1}^{\phi}P(u_a,v_a)
\tag{5}
\]

contains the same-class distinct-source component

\[
\boxed{
\lambda_{\phi,d}
\sum_{b=1}^{\phi}\sum_{r+s=d}c_{r,s}D_{r,s}(b),
}
\tag{6}
\]

where

\[
\boxed{
\lambda_{\phi,d}
=
\frac{(\phi-1)^d+(\phi-1)(-1)^d}{\phi^d}.
}
\tag{7}
\]

The remaining order-`d` terms in `F_P` are genuine **cross-residue** interactions involving source sites from at least two distinct classes. They are not errors and cannot be discarded when estimating the full centered statistic.

For every `d>=2`,

\[
\lambda_{\phi,d}\ne0\qquad(\phi>2).
\tag{8}
\]

Moreover, for fixed `d`,

\[
\lambda_{\phi,d}=1-\frac d\phi+O_d(\phi^{-2})+O_d(\phi^{1-d}),
\tag{9}
\]

so at large primorial rank the same-class top interaction is not merely present: its coefficient tends to one.

Consequently, for the active primorial

\[
q=q_y=\prod_{p\le c\log X}p,
\qquad
\phi=\varphi(q),
\tag{10}
\]

one has `phi>2` for all sufficiently large `X`, and every source-independent fixed-degree centered classwise polynomial with nonzero top homogeneous part contains a nonzero same-residue distinct-source interaction of the same order. Centering therefore does **not** algebraically erase the fixed-degree same-residue correlation component in the asymptotic primorial regime.

The correction is equally important in the other direction: `(6)` does **not** prove that a bound for `F_P` must estimate that same-residue component separately. The cross-residue order-`d` terms created by centering may in principle cancel against it for the actual arithmetic source. Thus the valid conclusion is a decomposition theorem and a restriction on algebraic escapes, not a universal statement that every centered polynomial transfers the entire analytic burden to an isolated same-residue correlation.

## 1. Exact centering matrix

Write

\[
C_{ab}=\delta_{ab}-\frac1\phi.
\tag{11}
\]

Then

\[
u_a=\sum_b C_{ab}A_b,
\qquad
v_a=\sum_b C_{ab}B_b.
\tag{12}
\]

Because lower-degree terms of `P` cannot contribute an order-`d` distinct-source monomial, it is enough to analyze

\[
\sum_a H_d(u_a,v_a).
\tag{13}
\]

Fix one monomial `U^rV^s` with `r+s=d` and one residue class `b`. To obtain an order-`d` source term whose `d` distinct sites all lie in class `b`, every one of the `d` centered factors in `(13)` must select the class-`b` aggregate. The class-label coefficient is therefore

\[
\sum_{a=1}^{\phi} C_{ab}^d.
\tag{14}
\]

For `a=b`, `C_{bb}=(\phi-1)/\phi`; for the other `\phi-1` rows, `C_{ab}=-1/\phi`. Hence

\[
\sum_a C_{ab}^d
=
\frac{(\phi-1)^d+(\phi-1)(-1)^d}{\phi^d}
=
\lambda_{\phi,d},
\tag{15}
\]

independently of `b`, `r`, and `s`.

Inside the selected class aggregate, the no-collision part of `A_b^rB_b^s` is exactly `D_{r,s}(b)`. Every collision has fewer than `d` distinct source sites. Summing the top monomials of `H_d` proves `(6)`.

## 2. Why cross-residue terms cannot algebraically cancel the same-class projection

The expansion of `(13)` also contains terms for which the `d` centered factors select several residue labels `b_1,\ldots,b_d`. Those are genuine top-order interactions across different residue classes. They matter analytically, but they occupy a different source-monomial sector from `(6)`.

Functions on a finite ternary source cube have the tensor-product basis

\[
\prod_i x_i^{\epsilon_i},
\qquad
\epsilon_i\in\{0,1,2\},
\tag{16}
\]

because on `{-1,0,1}` every one-coordinate function is a linear combination of `1,x,x^2`. A monomial using `d` distinct sites all in one residue class and a monomial using sites from multiple residue classes are therefore linearly independent functions of the unrestricted ternary source values.

Within one class, the top-order combinations in `(6)` are also independent. If a class contains `p` entries `+1` and `m` entries `-1`, the top homogeneous part of `D_{r,s}` is

\[
(p-m)^r(p+m)^s.
\tag{17}
\]

For fixed `r+s=d`, these are the monomial basis in the invertible coordinates `U=p-m`, `V=p+m`. Thus a nonzero `H_d` gives a nonzero same-class top projection whenever `\lambda_{\phi,d}\ne0`.

This proves presence, not separate estimability: for the actual Möbius source, numerical cancellation between the same-class and cross-class sectors of the full statistic remains possible and would itself be additional arithmetic structure.

## 3. Exact rank boundary

Equation `(7)` factors as

\[
\lambda_{\phi,d}
=
\frac{\phi-1}{\phi^d}
\left((\phi-1)^{d-1}+(-1)^d\right).
\tag{18}
\]

For even `d`, this is positive for every `\phi>=2`. For odd `d>=3`, it vanishes exactly at `\phi=2` and is positive for `\phi>2`. For `d=1`, it vanishes for every `\phi`, as it must because

\[
\sum_a u_a=\sum_a v_a=0.
\tag{19}
\]

The `\phi=2`, odd-degree failure is not a technicality. There `u_2=-u_1` and `v_2=-v_1`, so every odd homogeneous `H_d` satisfies

\[
H_d(u_1,v_1)+H_d(u_2,v_2)=0.
\tag{20}
\]

Thus a universal centered theorem for all moduli is false. The active logarithmic primorial is different: once `q` contains `2,3,5`, `\phi(q)>=8`, and thereafter `(8)` applies.

For fixed `d`, `(9)` follows directly from expanding `(1-1/\phi)^d` in `(7)`. Hence the active large-`\phi` limit does not attenuate the same-class top sector by a small parameter.

## 4. What remains of the primorial sparse-shift barrier

For the rough Möbius coefficient

\[
g_y(n)=\mu(n)\mathbf 1_{(n,q)=1},
\tag{21}
\]

any `k=d` distinct source sites in one residue class have differences in `q\mathbb Z`. After anchoring one site, the same-class component `(6)` therefore lives on

\[
(q\mathbb Z)^{d-1}.
\tag{22}
\]

At `q=X^{c+o(1)}`, this is a polynomially sparse shift lattice. The generic restriction calculation already established for a fixed `p>=1` gives a loss

\[
q^{(d-1)/p}=X^{c(d-1)/p+o(1)}
\tag{23}
\]

when one tries to pass from a full-shift `L^p` correlation estimate to this prescribed sublattice without extra arithmetic structure. Existing audited outputs `MC-S13`, `MC-S29`, and `MC-S2` do not by themselves pay this fixed-power restriction cost; `MC-S45` supplies strong smooth-modulus dispersion only after separating the principal character and does not provide the required same-residue multipoint estimate.

The corrected centered theorem leaves two distinct analytic possibilities:

1. control the same-class component itself by a theorem specialized strongly enough to the growing primorial lattice; or
2. exploit a proved cancellation identity **between** the same-class and cross-residue top sectors of the full centered statistic.

Only the first option is subject directly to the black-box sparse-restriction bill `(23)`. Treating `(23)` as an impossibility theorem for the second option would repeat the same kind of information-loss mistake that the line is designed to avoid.

## 5. Prior-art and novelty audit

The uncentered collision expansion is classical set-partition/symmetric-function algebra, and the centered calculation above is elementary linear algebra on the projection matrix `C=I-\phi^{-1}11^T`. No novelty is claimed for either abstract ingredient.

The arithmetic prior-art boundary is unchanged from the audited sources used in the rough-primorial chain. `MC-S13` concerns averaged Chowla correlations over shifts; `MC-S29` gives recent quantitative logarithmically weighted correlation information; `MC-S2` gives powerful almost-all short-interval/higher-uniformity results; and `MC-S45` gives smooth-modulus multiplicative-function dispersion. None of those theorem statements is a ready-made estimate for the specific same-class term `(6)` together with the cross-residue centering terms at `q=X^{c+o(1)}`.

The durable contribution here is therefore not a new theorem in symmetric-function or invariant theory. It is the **correct source-level centering audit for the specific rough-primorial interface**: the universal centered claim fails at low class rank, the asymptotic primorial case survives with the exact coefficient `(7)`, and the full centered top interaction has an additional cross-residue sector that must remain visible in any subsequent cancellation argument.

## 6. Boundaries and falsification tests

- The theorem concerns a source-independent fixed-degree polynomial applied uniformly classwise after centering. Coefficients may depend on deterministic external parameters such as `X` or `q`, but the effective top degree and top homogeneous part are taken after specialization.
- The uncentered triangularity holds without the `phi>2` restriction. The restriction is specific to the centered same-class projection for odd degree.
- The theorem proves a nonzero same-class **component** for `phi>2`; it does not prove a lower bound for the full centered statistic and does not forbid cancellation against cross-residue components.
- The sparse-shift loss `(23)` applies to a strategy that isolates the same-class component and restricts a generic full-shift moment theorem. It does not bind a proof that controls the whole centered source expression by a new coupled identity.
- Mixed signed/support exponents remain present. A pure-sign Chowla estimate cannot silently replace the mixed correlations generated by powers of `B_b`.
- No Mertens exponent, zero-free region, or RH consequence is derived here.

A counterexample to the repaired core claim would be a nonzero top homogeneous `H_d` with `d>=2` and `phi>2` for which the all-distinct same-class order-`d` projection of `sum_a H_d(u_a,v_a)` vanishes identically on all ternary source configurations. Equations `(15)`--`(18)` and the independence argument in Section 2 exclude such a counterexample.

## Consequence for the line

Centering is not a free escape from the fixed-degree residue-polynomial correlation hierarchy at the active primorial. At large rank, the same-class top-order coefficient is asymptotically one, so subtracting the principal class mean does not remove that source interaction.

The frontier is nevertheless slightly wider than the previous formulation allowed: a centered polynomial also creates top-order cross-residue interactions, and a genuinely arithmetic cancellation between those sectors would be new information rather than a black-box same-residue estimate. The next nonlinear test should therefore distinguish **algebraic removal** of the same-residue term, which is now excluded at fixed degree and primorial rank, from **coupled cancellation** among the complete residue-pattern sectors, which remains open.