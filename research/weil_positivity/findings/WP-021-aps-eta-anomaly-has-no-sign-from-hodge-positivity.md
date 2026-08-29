# WP-021 — APS eta anomalies escape index cancellation but inherit no sign from Hodge positivity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
positive coupled Hodge/Dirac square Q^2 >= 0
    -> APS boundary eta anomaly
    -> anomaly inherits a geometric sign
    -> global Weil positivity.
```

WP-020 left boundary/APS/eta terms open because they genuinely evade the equivariant McKean--Singer cancellation of positive nonzero modes. That escape is real as an **information channel**, but not as an inherited positivity mechanism. The eta invariant is spectral asymmetry: replacing a self-adjoint boundary operator `B` by `-B` leaves the positive square `B^2` unchanged while reversing the eta invariant. An explicit circle family makes this obstruction exact: two boundary operators can have unitarily equivalent positive squares, hence identical Hodge-energy data, while their eta corrections are equal and opposite. Therefore no sign theorem depending only on `Q^2 >= 0`, the spectrum of `B^2`, or ordinary Hodge energy can make the APS anomaly into the missing positive Weil form. A viable eta/boundary route needs an additional Mathia-native orientation/order theorem that controls spectral asymmetry itself.

## 1. Why eta was a genuine escape after WP-020

WP-018 recovers the exact finite coefficient

\[
\Lambda(n)
\]

from the supertrace of the positive residual-energy operator on the canonical backward Boolean cube. WP-020 then proves the coupled-Hodge fork: if an even insertion commutes with an odd self-adjoint supercharge `Q`, every positive eigenvalue of `Q^2` cancels from the graded trace; if one keeps the exact Mangoldt insertion, it is intrinsically non-`Q`-invariant and ordinary Hodge positivity no longer controls the signed functional.

The Atiyah--Patodi--Singer mechanism appears to evade the first horn because a manifold with boundary contributes a secondary invariant of the induced self-adjoint boundary operator `B`. In the standard product-near-boundary setting the APS index formula has the schematic form

\[
\operatorname{ind}D_{\rm APS}
=
\int_M \operatorname{AS}(D)
-
\frac{\eta(B)+h(B)}{2},
\tag{1}
\]

where `h(B)=dim ker B`. The boundary eta term sees the **signs** of nonzero boundary eigenvalues, so it is not erased by replacing the bulk analysis with an index.

Thus eta is not another instance of the cancellation already killed by WP-019/020. The relevant question is different:

> Can the sign of the eta anomaly itself be inherited from the positive Dirac/Hodge square, so that the same geometric positivity supplies the missing Weil sign?

The answer is no, already at the abstract boundary-operator level.

## 2. Exact sign obstruction: the square forgets precisely what eta measures

For an invertible self-adjoint elliptic operator `B` with discrete spectrum, the eta function is initially

\[
\eta_B(s)
=
\sum_{\lambda\ne0}
\operatorname{sgn}(\lambda)|\lambda|^{-s},
\tag{2}
\]

and is continued to `s=0` in the APS setting. Replacing `B` by `-B` gives, wherever the defining sums converge and hence by meromorphic continuation,

\[
\boxed{\eta_{-B}(s)=-\eta_B(s)},
\qquad
\boxed{\eta(-B)=-\eta(B)}.
\tag{3}
\]

But exactly

\[
\boxed{(-B)^2=B^2\ge0.}
\tag{4}
\]

Consequently every quantity obtained solely from ordinary positive functional calculus of the boundary square is identical for the pair:

\[
F(B^2)=F((-B)^2),
\qquad
\operatorname{Tr}F(B^2)=\operatorname{Tr}F((-B)^2)
\tag{5}
\]

whenever defined, while the eta anomaly changes sign.

This is a direct information-theoretic obstruction to inherited positivity. A theorem whose hypotheses and proof use only the nonnegativity of `B^2`, its positive spectrum, a Dirichlet energy, or a norm square cannot distinguish `B` from `-B`. Therefore it cannot force a one-sided inequality for a nonzero eta correction.

The kernel term in (1) does not weaken the counterexample: take `B` invertible, so `h(B)=0` for both signs.

## 3. Matched circle control: identical positive squares, opposite eta anomalies

The obstruction can be made completely explicit without any high-dimensional index theory. On the unit circle with periodic Fourier basis

\[
e_n(\theta)=e^{in\theta},\qquad n\in\mathbb Z,
\]

consider, for `0<a<1`,

\[
B_a=-i\frac{d}{d\theta}+a.
\tag{6}
\]

Its spectrum is

\[
\operatorname{spec}(B_a)=\{n+a:n\in\mathbb Z\},
\]

so it is invertible. For `Re(s)>1`, splitting positive and negative modes gives exactly

\[
\eta_{B_a}(s)
=
\sum_{n\ge0}(n+a)^{-s}
-
\sum_{n\ge0}(n+1-a)^{-s}
=
\zeta(s,a)-\zeta(s,1-a).
\tag{7}
\]

The standard Hurwitz-zeta special value

\[
\zeta(0,a)=\frac12-a
\]

therefore yields

\[
\boxed{\eta(B_a)=1-2a.}
\tag{8}
\]

Hence this single canonical family realizes both signs:

\[
0<a<\frac12\Rightarrow\eta(B_a)>0,
\qquad
\frac12<a<1\Rightarrow\eta(B_a)<0.
\]

More strongly, define the unitary Fourier reflection

\[
Ue_n=e_{-n-1}.
\]

A direct basis calculation gives

\[
UB_aU^{-1}=-B_{1-a}.
\tag{9}
\]

Squaring,

\[
\boxed{UB_a^2U^{-1}=B_{1-a}^2,}
\tag{10}
\]

while (8) gives

\[
\boxed{\eta(B_{1-a})=-\eta(B_a).}
\tag{11}
\]

Thus `B_a` and `B_{1-a}` are a **matched control with unitarily equivalent positive Hodge data and opposite boundary anomalies**. This rules out not merely a particular formula but the entire claim that eta inherits a sign from its positive square.

## 4. What the APS term can do, and what it cannot do

The result does not say that eta is uninformative. On the contrary, equation (3) shows why it survives the cancellation in WP-020: it records information that `Q^2` has deliberately forgotten. Spectral asymmetry, spectral flow, orientation, and boundary conditions can all contribute nontrivially even when the positive square is fixed.

That is precisely why eta cannot simultaneously be credited with **ordinary Hodge positivity**. The escape from cancellation and the loss of automatic sign are the same structural fact:

```text
pass from B^2 to signed B
    -> recover spectral asymmetry / boundary anomaly
    -> lose determination by positive Hodge energy.
```

For the Weil-positivity problem, inserting an eta term that has been tuned so that its signed spectral asymmetry reproduces the archimedean/polar correction would therefore not solve the sign problem. One would still need an independent theorem proving that the **assembled** finite-plus-boundary functional is nonnegative. That theorem cannot be `Q^2 >= 0` alone.

## 5. Relation to the exact Prime-Lattice finite selector

WP-018/020 make the tension especially sharp. The finite Mangoldt selector is generated by the noncommuting residual-energy insertion

\[
[R_\alpha,Q_\alpha]\ne0,
\]

whose logarithmically weighted edge differential is exactly what preserves the local arithmetic information. An APS correction could in principle provide a second non-index channel at infinity, because eta also measures signed data invisible to a square.

But combining two signed information channels does not manufacture a positive form. The finite supertrace is not positive, and the eta anomaly is not positive. The desired global theorem would have to couple them before taking the sign, through some additional order/intersection/compression principle whose hypotheses distinguish the arithmetic geometry from the controls above.

In particular, the following implication is now ruled out:

\[
\boxed{
\text{positive coupled Dirac/Hodge geometry}
\Longrightarrow
\text{APS anomaly of a forced sign}
\Longrightarrow
\text{Weil positivity}.
}
\tag{12}
\]

The first arrow fails even for the circle family (6).

## 6. Comparison with Prime-Flute boundary response

This obstruction is compatible with, but distinct from, WP-015. There the ordinary Prime-Flute DtN energy loses real PSD on positive spectral energies; on continuous spectrum only universal Herglotz positivity of an imaginary part remains, and relative subtraction has no sign without an extra ordering theorem.

APS eta behaves similarly at a more topological/spectral-asymmetry level: relative or boundary data can survive after bulk cancellation, but their sign is not inherited from the underlying positive operator. The two results therefore point to the same requirement from different sides: **boundary information is a viable carrier, but boundary information is not yet a positivity theorem.**

## 7. Prior art and novelty audit

No novelty is claimed for the eta invariant, the APS index theorem, the sign reversal `eta(-B)=-eta(B)`, the circle Dirac spectrum, Hurwitz zeta continuation, determinant lines, or spectral flow.

- M. F. Atiyah, V. K. Patodi, and I. M. Singer, *Spectral asymmetry and Riemannian geometry. I*, Mathematical Proceedings of the Cambridge Philosophical Society **77** (1975), 43--69, DOI `10.1017/S0305004100049410`, is the primary boundary-index source. It introduces the nonlocal spectral-asymmetry correction that makes eta a genuine escape from a pure local/Hodge index density.
- NIST DLMF, §25.11(v), equation 25.11.13, records the standard special value `zeta(0,a)=1/2-a` used in the explicit control (8).
- Xianzhe Dai and Daniel S. Freed, *Eta-Invariants and Determinant Lines*, Journal of Mathematical Physics **35** (1994), 5155--5194, DOI `10.1063/1.530747`; arXiv `hep-th/9405012`, develops eta as determinant-line/global-anomaly data with gluing and variation formulas. This is the close prior-art boundary against relabeling a boundary eta/transgression package as a new positive quadratic geometry.

Directed searches around eta invariants, APS boundary terms, Riemann/Weil positivity, and explicit-formula language did not locate a theorem turning ordinary APS spectral asymmetry into a positive zeta-Weil form. That absence is not a novelty claim. The present Mathia-specific contribution is the exact falsification test (10)--(11) applied to the escape explicitly left open by WP-020.

## 8. Surviving boundary/anomaly routes

This finding does **not** rule out eta, APS, spectral-flow, or anomaly mechanisms altogether. It leaves open constructions in which additional structure supplies a sign that is sensitive to `B`, not merely `B^2`. Examples include:

- a Mathia-native orientation or operator-order theorem that canonically selects one spectral-asymmetry chamber and proves the assembled form nonnegative;
- a relative eta/rho or scattering defect equipped with a new monotonicity theorem strong enough to survive subtraction;
- a compression, Schur complement, or intersection form whose positivity is proved before eta appears as a boundary term;
- a global transgression in which the WP-018 logarithmic edge differential and the archimedean anomaly are two boundaries of one geometric object, with a separate positivity theorem for that object.

Those are genuinely stronger mechanisms. Merely attaching an APS eta correction to a positive Hodge complex is no longer one of them.

## 9. Audit / falsification tests

Withdraw or narrow this finding if any of the following fails:

1. for invertible self-adjoint `B`, the eta definition gives `eta(-B)=-eta(B)` after analytic continuation;
2. `(-B)^2=B^2`, so positive spectral functional calculus cannot distinguish the pair;
3. for `B_a=-i d/dtheta+a`, `0<a<1`, the eta function is exactly `zeta(s,a)-zeta(s,1-a)`;
4. `zeta(0,a)=1/2-a`, hence `eta(B_a)=1-2a`;
5. the Fourier reflection `Ue_n=e_{-n-1}` satisfies `UB_aU^{-1}=-B_{1-a}`, giving unitarily equivalent squares and opposite eta invariants;
6. ordinary positivity of a square alone therefore cannot imply a fixed sign for eta;
7. no claim is made against a stronger boundary construction possessing an additional sign/order theorem that depends on signed first-order data rather than only on the square.

Items 1--6 are exact and independent of RH. Item 7 is the intended boundary of the no-go.

## 10. Consequence for the research line

The boundary/anomaly fork left by WP-020 is now sharper. APS spectral asymmetry does solve the **information-loss** problem of an index: it can retain nonzero signed boundary spectrum. But it does so precisely by moving to information not determined by the positive Hodge square. Therefore it cannot solve the **positivity** problem for free.

A viable Mathia-native global construction must now do more than combine the WP-018 finite supertrace with an archimedean eta correction. It must produce a new geometric theorem that controls their coupled signed contribution. Equivalently, the desired mechanism has to explain why the particular orientation/asymmetry forced by the prime geometry lies in a positive cone that the matched pair `B_a`, `B_{1-a}` does not share.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-020-q-invariant-coupled-hodge-insertions-still-collapse-to-index.md`
- `research/weil_positivity/findings/WP-015-prime-flute-dtn-positivity-does-not-survive-critical-scattering-continuation.md`
