---
id: WP-398
title: Critical-centralizer quotient positivity is order-trivial
branch: weil_positivity
status: supported
kind: bost-connes-critical-kms-centralizer-quotient-order-unit-positivity-degeneracy
claim_strength: exact RH-independent obstruction showing that after the critical Bost--Connes centralizer shadow is discarded, the image of the bounded positive cone is the entire self-adjoint information quotient; even on the normalized slice with fixed centralizer average 1, every bounded noncentral direction occurs with both signs locally, so ambient positivity alone cannot orient the surviving Fourier correlations
created: 2026-09-21
related: [WP-216, WP-222, WP-395, WP-396, WP-397]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - V. I. Paulsen and M. Tomforde, Vector spaces with an order unit, Indiana Univ. Math. J. 58 (2009), 1319--1360, DOI 10.1512/iumj.2009.58.3518, arXiv:0712.2613
  - M. Takesaki, Conditional expectations in von Neumann algebras, Journal of Functional Analysis 9 (1972), 306--321, DOI 10.1016/0022-1236(72)90004-3
  - standard order-unit inequality -||h||1 <= h <= ||h||1 for self-adjoint elements of a unital C-star algebra
---

# WP-398 — Critical-centralizer quotient positivity is order-trivial

## Claim

`WP-397` leaves a deliberately narrower bounded critical-factor route open: tolerate the unavoidable diffuse centralizer shadow and use the surviving nonzero gauge-frequency correlations themselves as arithmetic data. A natural version of that proposal is to regard the centralizer component as an uninformative positive floor and ask whether positivity of the full operator induces a useful sign or order on the remaining noncentral information.

It does not.

Let

\[
M=\pi_{\phi_1}(A_{BC})'',
\qquad
N=M_{\phi_1}=M^K,
\]

be the critical Bost--Connes factor and its gauge-fixed modular centralizer from `WP-395`, and let

\[
E:M\to N
\]

be the faithful normal gauge expectation used in `WP-397`. On the real self-adjoint spaces write

\[
V=M_{\rm sa},
\qquad
W=N_{\rm sa},
\qquad
q:V\to V/W.
\]

This is only the **real information quotient** that forgets the centralizer component; `N` is not being asserted to be an ideal, so no C-star-algebra quotient is intended.

Then

\[
\boxed{q(M_+)=V/W.}
\tag{1}
\]

In other words, every noncentral information class has a positive representative. The projected positive cone is the whole quotient and hence is not a proper cone at all.

The degeneracy persists even if the centralizer shadow is normalized instead of freely shifted. Because `E` is a projection,

\[
V=W\oplus \ker(E|_V).
\tag{2}
\]

For every self-adjoint `k in ker E` with `||k||<1`,

\[
1+k\ge0,
\qquad
1-k\ge0,
\qquad
E(1\pm k)=1.
\tag{3}
\]

Thus the normalized positive slice

\[
\mathcal S_1=\{a\in M_+:E(a)=1\}
\]

contains both orientations of every sufficiently small bounded noncentral direction. Equivalently, `q(S_1)` contains a balanced neighborhood of zero in the canonical `ker E` model of `V/W`.

For finite gauge-frequency data this is completely explicit. If

\[
h=\sum_{r\in F}(x_r+x_r^*),
\qquad
x_r\in M_r,
\qquad
1\notin F,
\tag{4}
\]

with the sum self-adjoint and `E(h)=0`, then for every real `t` with

\[
|t|<\|h\|^{-1}
\]

one has

\[
a_t=1+t h\ge0,
\qquad
E(a_t)=1,
\tag{5}
\]

while every nonzero Fourier coefficient of `a_t` is just `t` times the prescribed coefficient of `h`. Replacing `t` by `-t` reverses all those noncentral correlations while preserving positivity and the **same** centralizer shadow.

Therefore the open route after `WP-397` cannot obtain a Weil orientation merely by "ignoring the diffuse diagonal and reading positivity from the off-diagonal correlations." Once the centralizer is forgotten, ambient positivity supplies no nontrivial order whatsoever; even with the shadow fixed to `1`, it supplies no first-order orientation of noncentral directions. A surviving construction must impose additional source-derived structure coupling the frequencies to the shadow, or use a genuinely joint nonlinear/global readout whose sign is not inherited from the projected positive cone.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-GNS + MODULAR-CENTRALIZER + ORDER-UNIT + SELF-ADJOINT-INFORMATION-QUOTIENT + PROJECTED-POSITIVE-CONE-IMPROPER + FIXED-SHADOW-SYMMETRIC-NEIGHBORHOOD + NONCENTRAL-FOURIER-SIGN-PROGRAMMABILITY + MATCHED-CONTROL-UNIVERSAL + SOURCE-SELECTION-GATE + BOUNDED-POSITIVE-NO-GO + NOT-A-WEIL-BRIDGE`.

## 1. Forgetting a subspace containing the order unit destroys the inherited order

The mechanism is elementary and exact. Let `h=h^* in M`. Functional calculus gives the standard order-unit estimate

\[
-\|h\|1\le h\le \|h\|1.
\tag{6}
\]

Hence for any `c>=||h||`,

\[
c1+h\ge0.
\tag{7}
\]

But `1 in N`, so `c1 in W` and therefore

\[
q(c1+h)=q(h).
\tag{8}
\]

Every class in `V/W` has the form `q(h)` for some self-adjoint `h`, and (7)--(8) give a positive representative of that class. This proves (1).

The same argument applied to `-h` shows that both `q(h)` and `-q(h)` belong to `q(M_+)`. Consequently the projected cone satisfies

\[
q(M_+)\cap -q(M_+)=V/W,
\]

rather than intersecting only at zero. The preorder inherited by simply projecting positivity through `q` is therefore completely degenerate.

This is a general order-unit fact, not a special theorem about Bost--Connes. Paulsen--Tomforde provide a standard modern framework for ordered star-vector spaces, order units, Archimedeanization, and quotients. The present point is that the naive quotient relevant to the current Mathia escape discards a subspace that already contains the order unit, so its raw projected cone cannot retain a proper order.

## 2. The critical expectation gives a canonical representative of every quotient class

Although `V/W` is only a vector-space quotient, the source gauge expectation makes it concrete. For `h in V`, set

\[
k=h-E(h).
\tag{9}
\]

Then `k=k^*`, `E(k)=0`, and

\[
q(k)=q(h).
\tag{10}
\]

Moreover, if `k in W` as well as `ker E`, then `k=E(k)=0`. Thus every quotient class has a unique representative in the real space

\[
K_0=\ker(E|_V),
\]

and algebraically

\[
V=W\oplus K_0.
\tag{11}
\]

So "discard the diffuse critical centralizer shadow" has an exact source-selected interpretation: replace each self-adjoint element by its centered part `a-E(a)`.

Equation (1) then says that **being the centered part of some positive element places no sign restriction on that centered datum**. Given any `k in K_0`, the positive element

\[
a=\|k\|1+k
\tag{12}
\]

has centered part exactly `k`.

This is stronger than saying that arbitrary centralizer shifts can hide a small defect. There is no excluded bounded noncentral direction at all once the size of the centralizer floor is allowed to adjust.

## 3. Fixing the shadow removes the trivial scale shift but not the local sign degeneracy

A possible objection to (12) is that the centralizer floor was chosen after the desired noncentral datum. The critical state supplies a canonical normalization, so fix instead

\[
E(a)=1.
\tag{13}
\]

Now take arbitrary nonzero `k in K_0`. For

\[
0<\varepsilon<\|k\|^{-1},
\]

functional calculus gives

\[
1\pm\varepsilon k>0.
\tag{14}
\]

Because `E(k)=0`, both operators satisfy (13). Their centered parts are opposite:

\[
(1+\varepsilon k)-E(1+\varepsilon k)=\varepsilon k,
\]

\[
(1-\varepsilon k)-E(1-\varepsilon k)=-\varepsilon k.
\tag{15}
\]

Thus every bounded noncentral direction is two-sided inside the normalized positive slice near the source-selected base point `1`.

One immediate dual consequence is useful. Suppose a real linear functional

\[
L:V/W\to\mathbf R
\]

is claimed to inherit positivity from `M_+`, meaning

\[
L(q(a))\ge0
\qquad(a\ge0).
\tag{16}
\]

Since (1) puts both every class and its negative in `q(M_+)`, (16) forces

\[
L=0.
\tag{17}
\]

Even the weaker claim that `L(q(a))>=0` only for all `a in S_1` already forces `L=0`: equations (14)--(15) give both signs of every direction in a neighborhood of zero, and linear homogeneity propagates the conclusion to the whole quotient.

Hence no nonzero **linear Weil-sign functional on the noncentral quotient** can be justified solely by positivity of the ambient critical-factor element.

## 4. Fourier form: arbitrary bounded off-central directions admit positive lifts

Use the compact gauge grading from `WP-395`--`WP-397`:

\[
M_r=\{x:\theta_\chi(x)=\chi(r)x\},
\qquad r\in\mathbf Q_+^\times.
\]

Every nonzero homogeneous mode has zero gauge expectation. Therefore a finite self-adjoint Fourier polynomial with no zero-frequency term has the form (4) after grouping inverse frequencies, and it belongs to `K_0`.

Equations (5) now show that positivity with a fixed scalar shadow does not choose the sign of any such finite Fourier direction. If one starts with a specific `x in M_r`, `r!=1`, then

\[
a_\pm=1\pm\varepsilon(x+x^*)
\tag{18}
\]

are both positive for sufficiently small `epsilon`, satisfy

\[
E(a_\pm)=1,
\]

and have opposite `r` and `r^{-1}` Fourier coefficients.

More generally, any bounded finite collection of actually available spectral coefficients can be assembled into a self-adjoint `h`, scaled into the order interval `[-1,1]`, and embedded into the positive slice `S_1`. Positivity constrains the **allowed amplitude at fixed shadow**—as the `2 x 2` block inequality in `WP-397` makes explicit—but it does not select an arithmetic orientation of the available directions.

This distinction matters. `WP-397` is not contradicted: its support-domination theorem says the coefficients of a positive element must live over the support of the centralizer shadow and obey positive-definite block constraints. The present result says that once a faithful diffuse shadow such as `1` is accepted, those constraints leave a symmetric neighborhood of every noncentral direction around zero. Support domination is a real constraint; arithmetic sign selection is not supplied by it.

## 5. Matched controls and falsification value

Nothing in Sections 1--4 uses primes, the Riemann zeta function, or even the type-III nature of `M`, except to identify the source-selected fixed algebra and Fourier decomposition relevant to the current route. The same quotient degeneracy occurs for **every unital C-star algebra** when one modds out by a self-adjoint subspace containing the identity, and the normalized local symmetry occurs for any unital compact-group dynamical system with a unital conditional expectation onto its fixed algebra.

That universality is the decisive matched control. If a proposed critical-factor construction says only

1. take a positive multi-frequency element;
2. disregard its diffuse fixed-point component;
3. interpret the remaining nonzero frequencies as the arithmetic positive datum,

then the claimed sign mechanism survives unchanged in non-arithmetic systems and admits both orientations of every bounded small spectral perturbation. It therefore fails the research mandate's requirement that the sign be forced by independent arithmetic/geometric structure.

The result does **not** say that the nonzero-frequency coefficients are useless. They can carry source-specific arithmetic relations. What fails is the inference

\[
\text{ambient positivity}
\quad\Longrightarrow\quad
\text{positive/order-oriented noncentral quotient datum}.
\]

To revive the route one must add a relation not present in the generic order-unit argument: for example a canonical correspondence that fixes which coefficients can coexist, a source-derived non-scalar shadow tied quantitatively to those coefficients, a modular/domain equation, a finite--archimedean coupling, or a nonlinear invariant whose sign theorem genuinely uses the joint structure rather than forgetting `N`.

## 6. Relation to earlier findings

`WP-395` shows that the centralizer itself is too diffuse to retain exact point support on the standard prime-power orbit. `WP-396` shows that positivity formed from a single homogeneous mode collapses back into that centralizer. `WP-397` then proves that a bounded multi-frequency positive element cannot cancel its centralizer floor and that every Fourier coefficient is support-dominated by that floor.

The present finding attacks the immediate surviving interpretation of those facts. Keeping the floor but declaring it irrelevant does not make the off-central part inherit a meaningful positive cone: quotienting out the floor makes the projected cone equal to the entire information quotient, while fixing the floor to `1` still leaves both local orientations of every bounded centered direction.

This is also distinct from `WP-222`. There the quotient is a **Hilbert-space coinvariant compression** of one prime Toeplitz defect, and sign-programmability comes from choosing different finite Blaschke model spaces. Here no model-space quotient or target-selected inner function is used. The degeneracy arises before any such operator geometry, from forgetting an order-unit-containing centralizer subspace in the critical KMS factor.

Thus the bounded critical-factor frontier narrows again. A candidate cannot claim a Weil sign because it is positive before centralizer removal, nor because its off-diagonal coefficients survive that removal. It must explain a source-forced relation among the surviving correlations and the diffuse shadow whose sign remains nontrivial under the universal matched control above.

## 7. Prior-art and novelty audit

The general mathematics is classical. The estimate (6) is basic unital C-star order theory. Paulsen--Tomforde develop ordered star-vector spaces with order units and the correct Archimedean quotient framework; standard ordered-vector-space theory likewise warns that the image of a cone under an arbitrary vector-space quotient need not remain proper. Takesaki supplies the conditional-expectation framework, while the Bost--Connes source and `WP-395`--`WP-397` identify the specific critical fixed algebra and gauge decomposition used here.

A bounded literature search for order-unit quotients, critical Bost--Connes KMS factors, and projected positive cones found the general ordered-space quotient machinery and the standard Bost--Connes type-III/KMS structure, but no claim that this elementary quotient degeneracy yields a Riemann-specific theorem. **No general novelty is claimed.**

The durable Mathia delta is instead a falsification result for the exact live escape left by `WP-397`: once the diffuse centralizer shadow is tolerated, simply quotienting it away cannot transfer ambient positivity to the noncentral arithmetic correlations. The projected order is globally trivial, and even a fixed unit shadow leaves the noncentral tangent directions sign-symmetric.

## Research consequence

The bounded critical Bost--Connes factor still contains noncentral arithmetic structure, but positivity alone does not orient that structure after the unavoidable diffuse centralizer component is ignored. The next viable question is therefore **not** whether positive multi-frequency elements with arithmetic-looking correlations exist—they are locally generic. It is whether the Bost--Connes source, or a canonical finite--archimedean/global enlargement, imposes an additional nonprogrammable relation among those correlations and the shadow from which a genuine sign theorem follows.

No Weil positivity theorem or RH consequence follows from the present obstruction.