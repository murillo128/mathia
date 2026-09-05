# WP-166 — off-diagonal radial incidence is still pure gauge as a matrix connection

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE-BRIDGE + MATRIX-CONNECTION + OFF-DIAGONAL-INCIDENCE + PURE-GAUGE + NONABELIAN + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-165` closes the scalar-connection route but explicitly leaves open a genuinely off-diagonal cross-shell connection. `PC-180` now supplies a canonical candidate for that escape: its unsymmetrized radial flux--potential coupling has a nonzero skew part that is invisible to the Mangoldt endpoint product. It is therefore natural to retain the **pointwise skew incidence density** before integration and use it as a matrix-valued connection coefficient.

That route also fails, for a structural reason stronger than the scalar calculation. On a one-dimensional radial base, every finite-dimensional skew-Hermitian matrix connection is globally pure gauge. Noncommutativity merely replaces the ordinary exponential by parallel transport; there is still no curvature two-form because the base has only one direction. Consequently the positive covariant energy of the canonical Prime-Circle skew incidence is exactly unitarily/orthogonally equivalent to free Dirichlet energy. Its positivity is source-blind even when the cross-shell carrier itself is provably nonzero.

For a finite set of shells `S`, write

\[
F_n(s):=\log\Phi_n(e^{-s}),
\qquad
\rho_n(s):=-F_n'(s),
\tag{1}
\]

and define the canonical real skew matrix

\[
\boxed{
K_{mn}(s)
:=
\frac12\bigl(\rho_m(s)F_n(s)-\rho_n(s)F_m(s)\bigr),
\qquad m,n\in S.
}
\tag{2}
\]

The integrated matrix is exactly the skew part of the `PC-180` coupling

\[
A_{mn}:=\int_0^\infty \rho_m(s)F_n(s)\,ds:
\qquad
\boxed{
\int_0^\infty K(s)\,ds
=
\frac{A-A^T}{2}.
}
\tag{3}
\]

Thus (2) is not a hand-picked matrix field: it is the pointwise incidence density of the precise cross-shell information that survives after the symmetric part collapses to the boundary identity

\[
A_{mn}+A_{nm}=\Lambda(m)\Lambda(n).
\tag{4}
\]

Now put

\[
\nabla_K:=\frac d{ds}+K(s)
\tag{5}
\]

on vector-valued radial functions. Let `Q(s)` solve

\[
Q'(s)=Q(s)K(s),
\qquad
Q(0)=I.
\tag{6}
\]

Since `K^T=-K`, `Q(s)` is orthogonal. Moreover

\[
(Qf)'=Q(f'+Kf)=Q\nabla_K f,
\tag{7}
\]

so for every compactly supported smooth vector `f`,

\[
\boxed{
\int_0^\infty\!\|\nabla_K f\|^2\,ds
=
\int_0^\infty\!\|(Qf)'\|^2\,ds.
}
\tag{8}
\]

The entire positive bulk form is therefore the free Dirichlet form in a moving orthonormal frame. This remains exact for a complex skew-Hermitian connection, with `Q` unitary. Path ordering changes the endpoint transport but not (8).

The matched pair `S={2,6}` makes the obstruction non-vacuous. `PC-180` gives

\[
\Lambda(2)=\log2,
\qquad
\Lambda(6)=0,
\qquad
A_{2,6}=-A_{6,2}\approx-0.1269,
\tag{9}
\]

so the source-native skew carrier is genuinely nonzero. In this two-shell sector

\[
K(s)=k(s)J,
\qquad
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\tag{10}
\]

with

\[
\int_0^\infty k(s)\,ds=A_{2,6}\neq0.
\tag{11}
\]

Nevertheless (8) still removes it completely from the bulk energy. Because this `2 x 2` skew algebra is one-dimensional, the endpoint frame is explicitly

\[
Q(\infty)=\exp\!\bigl(A_{2,6}J\bigr),
\tag{12}
\]

a nontrivial compact rotation. Hence even a **nonzero** off-diagonal arithmetic carrier does not make connection-energy positivity arithmetic. What survives gauge trivialization is boundary transport, not a new positive interior theorem.

This closes a specific escape left by `WP-165`:

\[
\boxed{
\text{canonical cross-shell skew incidence}
+\text{1D matrix connection}
+\text{covariant-energy positivity}
\not\Rightarrow
\text{arithmetic/Weil positivity}.
}
\tag{13}
\]

The result does **not** say that every matrix-valued continuation of the Prime-Circle carrier is trivial. A zero-order off-diagonal potential that is not absorbed as a connection coefficient, a genuinely non-gauge-invariant boundary response with an independently proved sign theorem, a construction with nontrivial base topology and an additional sign mechanism, or a geometry with at least two independent base directions can escape (8). In particular, two base directions would permit genuine curvature/commutator data; a one-dimensional interval does not. Likewise, the endpoint orthogonal/unitary transport may remain source-dependent, but compact holonomy alone does not supply the required global Weil quadratic form or its finite--archimedean decomposition.

## 1. Why the matrix field is source-native

The functions in (1) are the same cyclotomic radial potential and inward flux used in `WP-161`, `WP-162`, and `PC-180`. For each finite shell set `S`, the matrix field (2) is forced by antisymmetrizing the two possible radial incidences at the **density level**, before integration. It is automatically skew-symmetric:

\[
K_{nm}(s)=-K_{mn}(s).
\tag{14}
\]

Integrating (14) and using the definition of `A` gives (3) exactly. Therefore the construction retains precisely the information discarded by the symmetric boundary collapse (4).

The field is regular enough for the global frame used above. At the cyclotomic boundary,

\[
F_n(0)=\Lambda(n),
\qquad
\rho_n(0^+)=\frac{\varphi(n)}2,
\tag{15}
\]

while both `F_n(s)` and `rho_n(s)` decay exponentially as `s -> infinity` for fixed `n`. Hence every entry of `K` is continuous at the finite boundary and integrable on the half-line. Standard finite-dimensional ODE theory gives the global solution of (6), and the integrability gives a finite endpoint transport `Q(infinity)`.

No positivity was inserted in (2): the only positivity enters later through the norm square in (8). This is exactly the order of operations the research mandate requires us to test.

## 2. Exact gauge trivialization

Differentiate `Q Q^T` using (6):

\[
\frac d{ds}(QQ^T)
=Q(K+K^T)Q^T
=0.
\tag{16}
\]

Since `Q(0)=I`, `Q(s)` is orthogonal for every `s`. Equation (7) then follows by the product rule, and orthogonality gives the pointwise identity

\[
\|f'+Kf\|=\|(Qf)'\|.
\tag{17}
\]

Integrating yields (8). Equivalently,

\[
\nabla_K=Q^{-1}\frac d{ds}Q.
\tag{18}
\]

The same proof works for a skew-Hermitian matrix field with transpose replaced by adjoint. In a larger shell sector the matrices `K(s)` at different radii need not commute; then `Q` is the path-ordered exponential. Nothing in (16)--(18) uses commutativity. Thus the tempting genuinely nonabelian extension does not evade the obstruction.

For Dirichlet or compact-support bulk forms, multiplication by `Q` preserves the form domain and establishes unitary equivalence to the free derivative. If one fixes additional frames at both radial ends, the endpoint transport can matter to boundary conditions or a boundary response. That is a separate datum and must carry its own sign theorem; it cannot retroactively make the bulk positivity in (8) source-specific.

## 3. The `{2,6}` matched control

The control is useful because shell `6` has vanishing Mangoldt endpoint value but nontrivial radial profile. From (4),

\[
A_{2,6}+A_{6,2}
=\Lambda(2)\Lambda(6)=0.
\tag{19}
\]

`PC-180` evaluates the remaining skew component and finds `A_{2,6}\approx-0.1269`, so (11) is nonzero. The matrix coefficient therefore carries genuine cross-shell information that cannot be reduced to the endpoint pair `(Lambda(2),Lambda(6))`.

Yet in this same control the gauge elimination is maximally transparent: all `K(s)` are multiples of the single generator `J`, so (12) follows without path ordering and (8) is an elementary rotation of the free energy. The negative result is therefore not caused by accidentally testing a zero connection or by first scalarizing the cross-shell information.

## 4. Prior-art and novelty audit

The ambient geometric fact is classical, not a Mathia discovery. A connection on a contractible one-dimensional interval is trivialized by parallel transport; for a noncommuting matrix coefficient the trivializing frame is a path-ordered exponential. This is standard differential geometry/gauge theory, and the usual Wilson/parallel-transport formalism treats path ordering precisely as the nonabelian replacement for an ordinary exponential. The absence of a curvature two-form on a one-dimensional base is likewise standard.

The Mathia-specific content is narrower: `PC-180` exposes a canonical nonzero skew cyclotomic incidence density after its symmetric part collapses to the Mangoldt boundary; (2)--(3) identify that density as the most direct matrix-connection candidate left open by `WP-165`; and (8)--(12) show on a matched nonzero control that the resulting independent-looking positive energy is still gauge-trivial. No novelty is claimed for the general one-dimensional gauge theorem itself.

This is not a re-expression of Weil positivity, a zero-defined spectrum, or an RH-equivalent functional. It is a falsification of a Mathia-native route **before** any zeta-zero data or Weil kernel is introduced.

## 5. Research consequence

The frontier moves one step beyond “make the surviving skew carrier matrix-valued.” If Prime Circle is to contribute an independent global sign theorem, the nonseparable information from `PC-180` must enter through structure that is not merely a connection along the same single radial coordinate. The cleanest surviving possibilities are: a zero-order/off-diagonal operator with a source-forced sign mechanism; a boundary pairing whose positivity is not inherited from free bulk energy; or a genuinely higher-dimensional/cohomological construction in which curvature or intersection data survive gauge choice.

The finite--archimedean problem is therefore sharpened rather than solved. A second geometric direction would be valuable only if it is itself forced by Mathia and simultaneously explains the archimedean/global counterterms; adding a dimension merely to manufacture curvature would fail the mandate's anti-hand-picking gate.

## Evidence and dependencies

- `research/weil_positivity/findings/WP-161-radial-cyclotomic-boundary-value-is-mangoldt-but-its-differential-jet-is-jordan-totient.md`
- `research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md`
- `research/weil_positivity/findings/WP-165-cyclotomic-radial-flux-is-pure-gauge-as-a-scalar-connection.md`
- `research/prime_circle/findings/PC-180-symmetric-flux-potential-couplings-collapse-to-mangoldt-boundary.md`
- `research/prime_circle/findings/PC-181-skew-flux-coupling-needs-an-independent-second-structure-before-positive-scalarization.md`
- Standard differential-geometric fact: one-dimensional connections on an interval are trivialized by parallel transport; nonabelian transport is represented by a path-ordered exponential.

## Bottom line

Prime Circle does contain a canonical, nonzero, off-diagonal radial carrier beyond the scalar Mangoldt boundary data. But promoting that carrier to a finite-dimensional skew-Hermitian connection on the radial half-line does **not** produce new geometric positivity: its covariant energy is exactly free energy in a moving frame. The matrix/nonabelian upgrade therefore does not escape `WP-165` unless Mathia supplies additional structure beyond a one-dimensional connection.