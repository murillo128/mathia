---
id: WP-333
title: Approximate faithful UCP rigidity is nonuniform at expanding Mangoldt cutoffs
branch: weil_positivity
status: supported
kind: ucp-readout-nonuniform-stability-boundary
claim_strength: exact quantitative faithfulness-modulus bound plus a sharp least-atom counterexample and a support-preserving martingale UCP self-map on the intrinsic dyadic prime-power ray, with scalar laws converging in total variation, every fixed polynomial moment, and every fixed Wasserstein metric while the Stinespring source coupling remains order one
created: 2026-09-16
related: [WP-329, WP-330, WP-331, WP-332]
prior_art:
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
  - Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner, A Continuity Theorem for Stinespring's Dilation, Journal of Functional Analysis 255 (2008), 1889-1904, DOI 10.1016/j.jfa.2008.07.023, arXiv:0710.2495
  - Volker Strassen, The Existence of Probability Measures with Given Marginals, Annals of Mathematical Statistics 36 (1965), 423-439, DOI 10.1214/aoms/1177700153
  - Lasse Leskela and Matti Vihola, Conditional convex orders and measurable martingale couplings, Bernoulli 23 (2017), 2784-2807, DOI 10.3150/16-BEJ827, arXiv:1404.0999
---

# WP-333 — Approximate faithful UCP rigidity is nonuniform at expanding Mangoldt cutoffs

## Claim

`WP-332` gives an exact finite-cutoff rigidity theorem: if a unital completely positive readout preserves the exact scalar law of the same self-adjoint source observable under a faithful output state, then the Kadison defect vanishes and the source observable lies in the multiplicative domain. Passing from exact finite cutoffs to an asymptotic/global statement has a sharp missing uniformity condition.

Let

\[
B_R=C(\Sigma_R),\qquad
\tau_R(f)=\sum_{x\in\Sigma_R}w_{x,R}f(x),
\qquad w_{x,R}>0,
\tag{1}
\]

and put

\[
m_R:=\min_{x\in\Sigma_R}w_{x,R}.
\tag{2}
\]

For any UCP map `Phi_R:A_R->B_R`, self-adjoint `X_R`, and

\[
b_R=\Phi_R(X_R),
\tag{3}
\]

the Kadison defect

\[
D_R:=\Phi_R(X_R^2)-b_R^2\ge0
\tag{4}
\]

satisfies the exact estimate

\[
\boxed{
\|D_R\|\le \frac{\tau_R(D_R)}{m_R}.
}
\tag{5}
\]

In Stinespring form, if `Phi_R(a)=V_R^* pi_R(a)V_R` and `P_R=V_RV_R^*`, then

\[
\|(I-P_R)\pi_R(X_R)V_R\|^2
=\|D_R\|
\le \frac{\tau_R(D_R)}{m_R}.
\tag{6}
\]

Thus approximate scalar second-moment preservation forces approximate multiplicative-domain rigidity only at the **relative** scale

\[
\tau_R(D_R)=o(m_R).
\tag{7}
\]

Absolute error `tau_R(D_R)->0` is insufficient when the faithfulness modulus `m_R` tends to zero.

For the finite pole-normalized Mangoldt source of `WP-329`--`WP-332`, `m_R` tends to zero at least exponentially fast. A least-atom construction shows that (5) is sharp in scale. More importantly, the escape does not require adding artificial support: the exact finite Mangoldt support itself admits a UCP self-map concentrated on three consecutive points of the dyadic prime-power ray. That map fixes the logarithmic source coordinate pointwise, its scalar source law converges back to the original source in total variation, every fixed polynomial moment, and every fixed Wasserstein metric, but its Kadison defect and Stinespring off-diagonal source coupling remain order one.

Therefore neither finite-cutoff faithfulness, asymptotic scalar-law recovery, support preservation, nor adjacency along an intrinsic prime-power ray is enough to globalize the exact rigidity of `WP-332`.

This is not a Weil-positivity mechanism. The least-atom construction is universal, and the support-preserving construction is a classical martingale-kernel move that works on any sufficiently thin equally spaced tail. The arithmetic content here is the exact placement of those generic mechanisms inside the canonical finite Mangoldt source and the resulting tightening of the global obstruction boundary.

**Classification:** `EXACT-DERIVED + QUANTITATIVE-BOUNDARY + UCP-READOUT + NONUNIFORM-STABILITY + SUPPORT-PRESERVING-MARTINGALE + EXPLICIT-MATCHED-CONTROL + MOVING-TAIL + NOT-WEIL-POSITIVITY`.

## 1. Finite faithfulness has an exact quantitative modulus

Because `D_R` is a positive function on the finite set `Sigma_R`,

\[
\tau_R(D_R)
=\sum_x w_{x,R}D_R(x)
\ge m_R\max_x D_R(x)
=m_R\|D_R\|.
\tag{8}
\]

This proves (5). The Stinespring factorization from `WP-332` is

\[
D_R=
\bigl((I-P_R)\pi_R(X_R)V_R\bigr)^*
\bigl((I-P_R)\pi_R(X_R)V_R\bigr),
\tag{9}
\]

which gives (6).

The distinction is therefore not between faithful and nonfaithful states at each fixed `R`: every `tau_R` here is faithful. It is between **pointwise faithfulness** and **uniform faithfulness along the expanding family**. The inverse constant in the exact implication is `1/m_R`; if `m_R` collapses, the exact theorem becomes badly conditioned.

In particular, equality of second moments still recovers `WP-332` at every fixed cutoff, but a sequence of second-moment errors tending to zero gives no operator-norm information unless it beats `m_R`.

## 2. The Mangoldt cutoff has exponentially vanishing least mass

For fixed `s>0`, write the unnormalized finite source weights as

\[
a_n=\frac{\Lambda(n)}{n+1}n^{-s},
\qquad n=p^k,
\tag{10}
\]

and

\[
Z_R=\sum_{\log n\le R}a_n,
\qquad
w_{n,R}=a_n/Z_R.
\tag{11}
\]

Take

\[
k_R=\left\lfloor\frac{R}{\log2}\right\rfloor,
\qquad n_R=2^{k_R}.
\tag{12}
\]

For sufficiently large `R`, `log n_R<=R` and `n_R>e^R/2`. Since `Z_R>=a_2`,

\[
\begin{aligned}
w_{n_R,R}
&\le \frac{a_{n_R}}{a_2}\\
&=3\,2^s\,\frac{n_R^{-s}}{n_R+1}\\
&\le 3\,2^{2s+1}e^{-(s+1)R}.
\end{aligned}
\tag{13}
\]

Hence

\[
\boxed{
m_R\le C_s e^{-(s+1)R}\to0.}
\tag{14}
\]

No prime-number theorem or zero information is used. A single fixed prime ray already makes the finite faithful states increasingly ill-conditioned for converting scalar expectation control into sup-norm control of a positive defect.

## 3. A sharp least-atom construction saturates the modulus

Choose an atom `x_R in Sigma_R` of mass `m_R`. For large `R`, choose `delta_R in [1,2]` so that neither `x_R-delta_R` nor `x_R+delta_R` lies in the finite set `Sigma_R`; such a choice always exists. Put

\[
K_R=\Sigma_R\cup\{x_R-\delta_R,x_R+\delta_R\},
\qquad A_R=C(K_R),
\tag{15}
\]

and let `X_R(t)=t` be the coordinate function. Define

\[
\Phi_R:C(K_R)\to C(\Sigma_R)
\tag{16}
\]

coordinatewise by identity away from `x_R` and by

\[
\Phi_R(f)(x_R)
=\frac12f(x_R-\delta_R)+\frac12f(x_R+\delta_R).
\tag{17}
\]

This map is unital and positive, hence completely positive because the domain is commutative. Symmetry gives `Phi_R(X_R)=x_R` at the modified coordinate, while

\[
D_R(y)=0\quad(y\ne x_R),
\qquad
D_R(x_R)=\delta_R^2.
\tag{18}
\]

Therefore

\[
\|D_R\|=\delta_R^2\in[1,4],
\qquad
\tau_R(D_R)=m_R\delta_R^2\to0.
\tag{19}
\]

The bound (5) is sharp in scale: the entire positive defect is concentrated at an atom attaining the minimum state weight, so `tau_R(D_R)=m_R||D_R||` exactly. The scalar law differs from the original by total-variation distance exactly `m_R`, and every fixed polynomial moment discrepancy tends to zero because `x_R<=R` while `m_R` decays exponentially.

This construction establishes the optimal faithfulness modulus, but it enlarges the support. The next construction removes that possible objection.

## 4. The same escape already exists inside the exact Mangoldt support

The dyadic prime-power ray supplies an intrinsic equally spaced log lattice. Put

\[
j_R=k_R-1,
\qquad
y_R=j_R\log2,
\qquad h=\log2.
\tag{20}
\]

For all sufficiently large `R`, the three points

\[
y_R-h,\qquad y_R,\qquad y_R+h
\tag{21}
\]

belong to `Sigma_R`; they are the logarithms of `2^{j_R-1}`, `2^{j_R}`, and `2^{j_R+1}=2^{k_R}`. Let

\[
r_R:=w_{2^{j_R},R}.
\tag{22}
\]

Since `2^{j_R}>e^R/4` and `Z_R>=a_2`, the same elementary estimate gives

\[
\boxed{
r_R\le 3\,2^{3s+2}e^{-(s+1)R}\to0.}
\tag{23}
\]

Now define a UCP **self-map**

\[
\Psi_R:C(\Sigma_R)\to C(\Sigma_R)
\tag{24}
\]

by

\[
\Psi_R(f)(y)=f(y),\qquad y\ne y_R,
\tag{25}
\]

and

\[
\Psi_R(f)(y_R)
=\frac12f(y_R-h)+\frac12f(y_R+h).
\tag{26}
\]

It is a Markov operator, hence unital and completely positive. For the coordinate function `X_R(t)=t`, barycentric symmetry gives

\[
\boxed{\Psi_R(X_R)=X_R}
\tag{27}
\]

pointwise on the entire finite source. Nevertheless its Kadison defect

\[
Q_R:=\Psi_R(X_R^2)-\Psi_R(X_R)^2
\tag{28}
\]

is

\[
Q_R(y)=0\quad(y\ne y_R),
\qquad
Q_R(y_R)=h^2=(\log2)^2.
\tag{29}
\]

Hence

\[
\boxed{
\|Q_R\|=(\log2)^2,
\qquad
\tau_R(Q_R)=r_R(\log2)^2\to0.
}
\tag{30}
\]

In a Stinespring dilation of `Psi_R`, equation (9) therefore gives an off-diagonal source-observable coupling of norm exactly

\[
\boxed{\log2,}
\tag{31}
\]

independent of `R`.

Thus the loophole is not an artifact of introducing external spectral points. It survives as a self-map of the exact finite arithmetic support, fixes the source coordinate exactly after compression, and uses only nearest-neighbor incidence on one canonical prime-power log ray.

At the map level nothing converges to the identity. Indeed choose `f_R` of sup norm one with

\[
f_R(y_R)=1,
\qquad f_R(y_R-h)=f_R(y_R+h)=-1.
\tag{32}
\]

Then `||(Psi_R-id)f_R||_infinity=2`, and since both maps are contractions,

\[
\boxed{\|\Psi_R-id\|=2.}
\tag{33}
\]

This is exactly the separation expected between weak scalarized convergence and genuinely strong map-level control.

## 5. Scalar laws converge even in every fixed Wasserstein metric

Let `nu_R` be the scalar law of the coordinate `X_R` under `tau_R`. Because `Psi_R(X_R)=X_R`, the output-coordinate law remains `nu_R`, whereas the source-coordinate law under `tau_R o Psi_R` is

\[
\nu_R'
=\nu_R-r_R\delta_{y_R}
+\frac{r_R}{2}\delta_{y_R-h}
+\frac{r_R}{2}\delta_{y_R+h}.
\tag{34}
\]

All three atoms are already in the exact Mangoldt support. The signed difference has masses `-r_R,r_R/2,r_R/2`, so

\[
\boxed{d_{\rm TV}(\nu_R,\nu_R')=r_R\to0.}
\tag{35}
\]

The first moment is preserved exactly. For every fixed integer `q>=2`,

\[
\frac12\bigl((y_R+h)^q+(y_R-h)^q\bigr)-y_R^q
=O_q(R^{q-2}),
\tag{36}
\]

and hence the `q`-th moment discrepancy is

\[
O_q(r_RR^{q-2})\to0.
\tag{37}
\]

There is also a direct transport coupling: leave all other mass fixed and move half of the `r_R` mass at `y_R` to each adjacent point. For every fixed `p>=1`,

\[
W_p(\nu_R,\nu_R')^p
\le r_Rh^p,
\tag{38}
\]

so

\[
\boxed{W_p(\nu_R,\nu_R')\le (\log2)r_R^{1/p}\to0.}
\tag{39}
\]

The normalized truncations `nu_R` themselves converge in total variation to the full tilted Mangoldt probability source `nu_s`, because they are normalized restrictions to an increasing exhaustion of its countable support. The modified laws `nu_R'` therefore converge to the same full source in total variation; equations (37) and (39) give the corresponding fixed-moment and fixed-Wasserstein comparisons between the two finite laws.

Thus even a support-preserving martingale perturbation can be invisible to a wide class of scalar convergence tests while retaining an order-one positive operator defect.

## 6. Prior-art and novelty audit

Kadison--Schwarz positivity, Stinespring factorization, and multiplicative-domain equality are classical and already anchor `WP-332`. Quantitative continuity of Stinespring dilations is also classical: Kretschmann--Schlingemann--Werner control dilations from a map-level completely bounded norm/Bures distance. That hypothesis is much stronger than convergence of one scalarized source law, and the exact norm identity (33) shows why their theory does not force the present channels to converge.

The support-preserving map (24)--(26) is a finite martingale Markov kernel: it preserves the coordinate because the conditional barycenter of the two neighboring states is the original point. Martingale couplings and their relation to convex order are classical, beginning with Strassen's theorem; modern probability-kernel formulations include Leskela--Vihola. Neither the barycentric split nor the general fact that degenerating faithful states lose uniform norm control is claimed as a new operator-algebra or probability theorem.

The Mathia-specific content is narrower: the canonical finite Mangoldt source itself contains an exponentially light, exactly equally spaced prime-power ray on which this classical martingale move realizes the nonuniform UCP escape **without leaving the arithmetic support**. Consequently, support preservation and prime-ray adjacency cannot be used as the missing selectivity condition in a positive Weil route.

No audited prior art supplies a theorem turning this moving martingale defect into the finite-plus-archimedean Weil quadratic form with an independent sign theorem. The mechanism remains a structural boundary, not a candidate proof of Weil positivity.

## 7. Matched controls and falsification

The least-atom construction of section 3 is deliberately non-arithmetic: any sequence of finite probability spaces with minimum atom `m_R->0` admits the same sharp hiding of a positive defect.

The internal construction is more source-specific but still fails matched controls. Any source with an equally spaced tail whose state mass tends to zero admits the same three-point martingale self-map. In particular, a generalized-prime/free-multiplicative source with powers of one fixed generator supplies the identical logarithmic arithmetic progression. The construction depends on the existence of that thin affine ray, not on the global arithmetic of the rational primes.

This falsifies a stronger interpretation than the original least-atom example. The following properties together are still insufficient to indicate a Weil-positive mechanism:

1. the channel acts only on the original arithmetic support;
2. the modified site lies on a canonical prime-power ray;
3. the source coordinate is fixed exactly by the UCP compression;
4. the scalar law converges in total variation, all fixed polynomial moments, and every fixed Wasserstein metric;
5. an order-one Stinespring coupling remains hidden in the moving tail.

A viable route therefore needs a **forcing rule** for the moving coupling whose location, scale, and interaction with the archimedean/global sector are genuinely arithmetic and fail matched controls. Merely choosing a natural thin ray is not enough. Conversely, a future global no-go extending `WP-332` must prove relative control such as (7), control the CP maps in a stronger topology, or otherwise exclude moving-tail concentration.

## 8. Boundary and implication for the Weil program

This finding does **not** produce a global positive form, a Gamma term, a polar counterterm, or an RH implication. It does not refute `WP-332`: exact scalar second-moment equality under a faithful state at each fixed cutoff still forces zero defect exactly.

What changes is the infinite-cutoff inference. The implication

\[
\text{scalar source laws converge}
\Longrightarrow
\text{source-observable coupling vanishes}
\tag{40}
\]

is false without a uniform faithfulness/error hypothesis. The strengthened construction shows that the failure persists even when every finite readout is a self-map of the exact source algebra and the compressed source coordinate is fixed pointwise.

The remaining positive route is therefore narrower than before. A moving-tail coupling may still exist, but its arithmetic value cannot come merely from being source-internal or sitting on prime powers. It must be **forced by a global finite--archimedean construction**, survive the final Weil readout at the correct normalization, carry an independent positivity theorem, and fail generalized-prime or other matched controls. Short of such structure, the moving UCP tail is generic martingale geometry rather than evidence for Weil positivity.
