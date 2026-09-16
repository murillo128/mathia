---
id: WP-333
title: Approximate faithful UCP rigidity is nonuniform at expanding Mangoldt cutoffs
branch: weil_positivity
status: supported
kind: ucp-readout-nonuniform-stability-boundary
claim_strength: exact quantitative faithfulness-modulus bound plus explicit sharp finite-cutoff UCP construction showing that scalar source laws can converge in total variation and every fixed polynomial moment while the Stinespring source coupling remains order one
created: 2026-09-16
related: [WP-329, WP-330, WP-331, WP-332]
prior_art:
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
  - Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner, A Continuity Theorem for Stinespring's Dilation, Journal of Functional Analysis 255 (2008), 1889-1904, DOI 10.1016/j.jfa.2008.07.023, arXiv:0710.2495
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

For the finite pole-normalized Mangoldt source of `WP-329`--`WP-332`, `m_R` does tend to zero, in fact at least exponentially fast along a simple prime-power witness. More strongly, there is an explicit sequence of UCP readouts for which

\[
d_{\rm TV}(\operatorname{Law}_{\tau_R\circ\Phi_R}(X_R),
             \operatorname{Law}_{\tau_R}(b_R))
=m_R\to0,
\tag{8}
\]

all fixed polynomial moments converge to the same Mangoldt moments, but

\[
\|D_R\|\ge1
\quad\text{and hence}\quad
\|(I-P_R)\pi_R(X_R)V_R\|\ge1.
\tag{9}
\]

So the exact rigidity of `WP-332` has **no cutoff-uniform stability consequence from scalar-law convergence alone**. A moving thin tail can carry order-one dilation/boundary coupling while becoming invisible to the scalar source law.

This is not a Weil-positivity mechanism. The same construction works for arbitrary expanding finite probability laws whose least atom tends to zero. Its value is to identify a real escape from an over-strong extrapolation of `WP-332`: any global no-go must control the readout defect uniformly relative to the vanishing faithfulness modulus, while any positive route that exploits the escape must prove that the moving defect is source-forced and survives the eventual Weil readout.

**Classification:** `EXACT-DERIVED + QUANTITATIVE-BOUNDARY + UCP-READOUT + NONUNIFORM-STABILITY + EXPLICIT-MATCHED-CONTROL + MOVING-TAIL + NOT-WEIL-POSITIVITY`.

## 1. Finite faithfulness has an exact quantitative modulus

Because `D_R` is a positive function on the finite set `Sigma_R`,

\[
\tau_R(D_R)
=\sum_x w_{x,R}D_R(x)
\ge m_R\max_x D_R(x)
=m_R\|D_R\|.
\tag{10}
\]

This proves (5). The Stinespring factorization from `WP-332` is

\[
D_R=
\bigl((I-P_R)\pi_R(X_R)V_R\bigr)^*
\bigl((I-P_R)\pi_R(X_R)V_R\bigr),
\tag{11}
\]

which gives (6).

The distinction is therefore not between faithful and nonfaithful states at each fixed `R`: every `tau_R` here is faithful. It is between **pointwise faithfulness** and **uniform faithfulness along the expanding family**. The inverse constant in the exact implication is `1/m_R`; if `m_R` collapses, the exact theorem becomes badly conditioned.

In particular, equality of second moments still recovers `WP-332` at every fixed cutoff, but a sequence of second-moment errors tending to zero gives no operator-norm information unless it beats `m_R`.

## 2. The Mangoldt cutoff has exponentially vanishing least mass

For fixed `s>0`, write the unnormalized finite source weights as

\[
a_n=\frac{\Lambda(n)}{n+1}n^{-s},
\qquad n=p^k,
\tag{12}
\]

and

\[
Z_R=\sum_{\log n\le R}a_n,
\qquad
w_{n,R}=a_n/Z_R.
\tag{13}
\]

Take

\[
k_R=\left\lfloor\frac{R}{\log2}\right\rfloor,
\qquad n_R=2^{k_R}.
\tag{14}
\]

For sufficiently large `R`, `log n_R<=R` and `n_R>e^R/2`. Since `Z_R>=a_2`,

\[
\begin{aligned}
w_{n_R,R}
&\le \frac{a_{n_R}}{a_2}\\
&=3\,2^s\,\frac{n_R^{-s}}{n_R+1}\\
&\le 3\,2^{2s+1}e^{-(s+1)R}.
\end{aligned}
\tag{15}
\]

Hence

\[
\boxed{
m_R\le C_s e^{-(s+1)R}\to0.}
\tag{16}
\]

No prime-number theorem or zero information is used. A single fixed prime ray already makes the finite faithful states increasingly ill-conditioned for converting scalar expectation control into sup-norm control of a positive defect.

## 3. A sharp UCP construction hides order-one coupling in the least atom

Choose an atom `x_R in Sigma_R` of mass `m_R`. For large `R`, choose `delta_R in [1,2]` so that neither `x_R-delta_R` nor `x_R+delta_R` lies in the finite set `Sigma_R`; such a choice always exists. Put

\[
K_R=\Sigma_R\cup\{x_R-\delta_R,x_R+\delta_R\},
\qquad A_R=C(K_R),
\tag{17}
\]

and let `X_R(t)=t` be the coordinate function. Define

\[
\Phi_R:C(K_R)\to C(\Sigma_R)
\tag{18}
\]

coordinatewise by

\[
\Phi_R(f)(y)=f(y),\quad y\ne x_R,
\tag{19}
\]

and

\[
\Phi_R(f)(x_R)
=\frac12f(x_R-\delta_R)+\frac12f(x_R+\delta_R).
\tag{20}
\]

This map is unital and positive, hence completely positive because the domain is commutative. Symmetry gives

\[
\Phi_R(X_R)(x_R)=x_R,
\tag{21}
\]

so `Phi_R(X_R)=b_R` exactly. But

\[
D_R(y)=0\quad(y\ne x_R),
\qquad
D_R(x_R)=\delta_R^2.
\tag{22}
\]

Therefore

\[
\|D_R\|=\delta_R^2\in[1,4],
\qquad
\tau_R(D_R)=m_R\delta_R^2\to0.
\tag{23}
\]

Equations (6) and (23) show that the off-diagonal Stinespring source coupling stays order one even though its scalar second-moment cost vanishes.

The bound (5) is sharp in scale: this construction concentrates the entire positive Kadison defect at an atom attaining the minimum state weight, so `tau_R(D_R)=m_R||D_R||` exactly.

## 4. Even strong scalar-law convergence does not see the coupling

Let `nu_R` be the scalar law of `b_R` under `tau_R`. The law of `X_R` under `tau_R o Phi_R` differs from `nu_R` only by replacing the atom

\[
m_R\delta_{x_R}
\tag{24}
\]

with

\[
\frac{m_R}{2}\delta_{x_R-\delta_R}
+\frac{m_R}{2}\delta_{x_R+\delta_R}.
\tag{25}
\]

The added points are disjoint from `Sigma_R`, so the total-variation distance is exactly

\[
d_{\rm TV}=m_R\to0.
\tag{26}
\]

Moreover the first moment is preserved exactly by symmetry. For every fixed integer `q>=2`,

\[
\frac12\bigl((x_R+\delta_R)^q+(x_R-\delta_R)^q\bigr)-x_R^q
=O_q(x_R^{q-2}),
\tag{27}
\]

because only even powers of `delta_R` remain. Since `x_R<=R` while `m_R` admits the exponential upper bound (16), the discrepancy of every fixed `q`-th moment tends to zero.

The normalized truncations `nu_R` themselves converge in total variation to the full probability source `nu_s`, because they are normalized restrictions to an increasing exhaustion of its countable support. Hence the modified scalar laws also converge to the same full `nu_s` while their source-observable dilation coupling remains order one.

This is stronger than a weak-convergence loophole. Neither total-variation convergence to the exact source nor convergence of every fixed polynomial moment forces the coupling to disappear.

## 5. Prior-art and novelty audit

Kadison--Schwarz positivity, Stinespring factorization, and multiplicative-domain equality are classical and already anchor `WP-332`. Quantitative continuity of Stinespring dilations is also classical: Kretschmann--Schlingemann--Werner prove continuity when the **completely bounded norm of the CP maps** is controlled, equivalently through the corresponding Bures distance. That is a substantially stronger, map-level hypothesis than convergence of one scalarized source law.

There is therefore no conflict with the standard continuity theory. The present construction exploits exactly what scalarization forgets: the map can change by order one on an output coordinate whose state mass tends to zero while the induced scalar law changes by only `m_R`.

The elementary estimate (5), the atom-splitting channel, and the general fact that degenerating faithful states lose uniform norm control are not claimed as new operator-algebra theorems. The Mathia-specific result is the exact placement of this stability boundary in the `WP-332` Mangoldt architecture, including the exponential degeneration supplied intrinsically by the prime-power cutoff and the resulting warning for global finite-to-infinite passage.

No searched prior art supplied a Weil or arithmetic theorem that turns this thin-tail freedom into a source-selective positive form. The mechanism remains a structural boundary, not a novelty claim about CP maps.

## 6. Matched controls and falsification

The counterexample is deliberately non-arithmetic. Let any sequence of finite probability spaces have least atom `m_R->0`. Splitting one least-mass atom symmetrically by a fixed displacement reproduces (23)--(26). Thus the ability to retain hidden dilation coupling while the scalar law converges is universal whenever the readout family loses a uniform lower weight bound.

This kills the interpretation that thin-tail coupling itself is a Riemann-specific resource. To become relevant to Weil positivity, a proposed construction must derive from the arithmetic source at least three additional facts:

1. where the moving defect/coupling is placed and why that placement is canonical;
2. how its scale survives the final finite-plus-archimedean response rather than disappearing in scalarization;
3. what independent positivity theorem gives the required Weil orientation and fails on matched controls.

Conversely, a future attempt to extend `WP-332` into a genuine global obstruction cannot cite finite-cutoff faithfulness alone. It must prove a uniform estimate such as (7), a stronger operator/cb-norm approximation, or another topology in which the moving tail cannot hide an order-one positive defect.

## 7. Boundary and implication for the Weil program

This finding does **not** produce a global positive form, a Gamma term, a polar counterterm, or an RH implication. It also does not refute `WP-332`: exact scalar second-moment equality at each finite cutoff still forces zero defect exactly.

What changes is the infinite-cutoff inference. The implication

\[
\text{scalar source laws converge}
\Longrightarrow
\text{source-observable coupling vanishes}
\tag{28}
\]

is false without a uniform faithfulness/error hypothesis. The first possible escape from the same-observable UCP no-go is therefore mathematically concrete: coupling may migrate into source regions whose scalar mass vanishes faster than the coupling strength.

That escape is simultaneously dangerous and useful. It prevents an unjustified global no-go, but matched controls show that it gives no arithmetic sign for free. A viable Mathia-native construction would have to make the moving tail geometrically canonical and couple it to the archimedean/global sector before scalarization, with positivity proved independently of the final arithmetic identification.
