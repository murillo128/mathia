# PL-268 — Translation symmetry forces strict domain monotonicity of the localized Weil ground energy

**Evidence:** `LITERATURE+DERIVED`

**Status:** `STRUCTURAL-SHARPENING + ZERO-PLATEAU-EXCLUSION`

## Claim

Let `Q_W^a` be the closed completed Weil form localized to `L^2(-a,a)` and let `A_a` be its associated lower-bounded self-adjoint operator. Write

\[
\lambda_a=\min\sigma(A_a)
=\inf_{0\ne u\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(u)}{\|u\|_2^2}.
\]

Then the domain monotonicity of `PL-266` is in fact strict:

\[
\boxed{0<a<b\quad\Longrightarrow\quad \lambda_b<\lambda_a.}
\]

The mechanism is elementary but stronger than the support reformulation in `PL-267`. The global Weil form is exactly invariant under common translation because

\[
Q_W(v)=W(v*\widetilde v)
\]

and translating `v` leaves its autocorrelation unchanged. If equality `\lambda_a=\lambda_b` held, a ground vector from the smaller interval could be translated through a continuum of shifts while remaining inside the larger interval; every translate would still attain the larger-domain minimum. Distinct translates of a nonzero compactly supported `L^2` function are linearly independent, forcing the ground eigenspace of `A_b` to be infinite-dimensional. This contradicts the compact-resolvent/discrete-spectrum theorem for `A_b`.

Consequently a zero plateau is impossible. Since Suzuki proves continuity of `a\mapsto\lambda_a` and positivity for sufficiently small `a`, failure of RH produces a **unique** finite radius `a_0` such that

\[
\lambda_{a_0}=0,
\qquad
\lambda_a>0\ (a<a_0),
\qquad
\lambda_a<0\ (a>a_0).
\]

Equivalently, the earliest degeneracy radius and the onset of strict negativity from `PL-266` coincide. Under RH, `\lambda_a` is strictly positive at every finite radius: if `\lambda_{a_0}=0` for some finite `a_0`, strict decrease would force negativity for every larger radius and violate Weil positivity.

This does **not** prove RH or provide a source-side reason for positivity. Strict decrease follows from translation symmetry plus finite spectral multiplicity and therefore organizes the sign transition without deciding whether the transition occurs.

## 1. The global Weil form is translation invariant

For `h\in\mathbb R`, define

\[
(\tau_hv)(x)=v(x-h).
\]

Suzuki recalls the defining identity

\[
Q_W(v_1,v_2)=W(v_1*\widetilde{v_2}),
\qquad
\widetilde v(x)=\overline{v(-x)}.
\]

For the quadratic form,

\[
\widetilde{\tau_hv}=\tau_{-h}\widetilde v,
\]

and convolution shifts add. Hence

\[
(\tau_hv)*\widetilde{\tau_hv}
=(\tau_hv)*(\tau_{-h}\widetilde v)
=v*\widetilde v,
\]

so for compactly supported smooth `v`,

\[
Q_W(\tau_hv)=Q_W(v),
\qquad
\|\tau_hv\|_2=\|v\|_2.
\]

The same invariance is visible in Suzuki's difference-kernel realization: the localized form on smooth functions is obtained from a kernel depending only on `x-y`.

## 2. Translation invariance extends to the relevant closed form domains

Fix `0<a<b` and `|h|<b-a`. Let `u\in\mathfrak D(Q_W^a)`. For the application below it is enough to take a minimizer of the Rayleigh quotient. Suzuki's Corollary 1.2 states that every minimizer belongs to the closure of `C_c^\infty(-a,a)` in the form norm of `Q_W^a`.

Choose `u_n\in C_c^\infty(-a,a)` converging to `u` in that form norm. Since `|h|<b-a`, every `\tau_hu_n` belongs to `C_c^\infty(-b,b)`. On smooth differences, global translation invariance gives

\[
Q_W^b(\tau_h(u_n-u_m))=Q_W^a(u_n-u_m),
\]

while the `L^2` norm is unchanged. After adding any fixed lower-bound shift that makes the form norms positive, the translated sequence is therefore Cauchy in the closed form norm of `Q_W^b`. Its `L^2` limit is `\tau_hu`, so

\[
\tau_hu\in\mathfrak D(Q_W^b)
\]

and closure preserves

\[
Q_W^b(\tau_hu)=Q_W^a(u),
\qquad
\|\tau_hu\|_2=\|u\|_2.
\]

Thus the smaller-domain Rayleigh quotient can be moved freely inside the larger interval without changing its value. This is stronger information than mere nesting by zero extension.

## 3. Equality of two ground energies would create infinitely many ground states

Assume for contradiction that

\[
\lambda_a=\lambda_b.
\]

Let `u_a` be a normalized ground eigenvector of `A_a`, extended by zero outside `(-a,a)`. The ordinary domain inclusion already gives

\[
Q_W^b(u_a)=Q_W^a(u_a)=\lambda_a=\lambda_b.
\]

For every `|h|<b-a`, Section 2 gives

\[
Q_W^b(\tau_hu_a)=\lambda_b\|\tau_hu_a\|_2^2.
\]

Hence each `\tau_hu_a` attains the minimum of the closed semibounded form `Q_W^b`. By the representation theorem for closed quadratic forms, every such minimizer belongs to the bottom eigenspace:

\[
\tau_hu_a\in\ker(A_b-\lambda_b).
\]

There are infinitely many allowable distinct shifts. It remains only to exclude the possibility that they span a finite-dimensional space.

## 4. Distinct translates of a compactly supported nonzero vector are linearly independent

The zero extension of `u_a` has compact support, hence belongs to `L^1(\mathbb R)\cap L^2(\mathbb R)`. Its Fourier transform extends to an entire function of exponential type and is not identically zero.

Suppose distinct real numbers `h_1,\dots,h_m` satisfied a finite relation

\[
\sum_{j=1}^m c_j\tau_{h_j}u_a=0.
\]

Taking Fourier transforms gives on the real axis

\[
\widehat{u_a}(z)
\sum_{j=1}^m c_je^{ih_jz}=0
\]

(up to the harmless sign convention for the Fourier transform). Both factors extend holomorphically. Since `\widehat{u_a}` is not identically zero, the exponential polynomial must vanish on a nonempty open set and hence identically. Distinct exponential characters are linearly independent, so all `c_j=0`.

Therefore every finite family of distinct translates is linearly independent. The continuum of shifts `|h|<b-a` would make

\[
\dim\ker(A_b-\lambda_b)=\infty.
\]

## 5. Compact resolvent rules out the equality case

Suzuki records the Connes--Consani--Moscovici theorem that `A_b` has lower-bounded discrete spectrum with `+\infty` as its only accumulation point. In the proof framework he also recalls the compact embedding of the form domain into `L^2(-b,b)`, which is the compactness input behind this spectral discreteness. In particular every eigenspace, including the ground eigenspace, has finite multiplicity.

This contradicts Section 4. Therefore equality is impossible, and the non-strict variational inequality from `PL-266` sharpens to

\[
0<a<b\quad\Longrightarrow\quad\lambda_b<\lambda_a.
\]

This argument does not require a unique-continuation theorem for the nonlocal Weil operator. It also does not require simplicity of the ground eigenvalue; finite multiplicity is enough.

## 6. The zero crossing is unique

Suzuki proves that `a\mapsto\lambda_a` is continuous and that `\lambda_a>0` for sufficiently small `a`. Weil positivity gives

\[
\mathrm{RH}\iff \lambda_a\ge0\quad\text{for every }a>0,
\]

while failure of RH is equivalent to `\lambda_a<0` for some finite radius.

Strict decrease therefore sharpens the alternatives.

If RH holds, no finite `a` can satisfy `\lambda_a=0`, since every larger `b` would have `\lambda_b<0`. Thus

\[
\mathrm{RH}\quad\Longrightarrow\quad \lambda_a>0
\quad\text{for every finite }a>0.
\]

If RH fails, continuity supplies a zero between the small positive regime and a negative radius, and strict decrease makes it unique. Writing

\[
a_0:=\inf\{a>0:\lambda_a=0\},
\qquad
a_-:=\inf\{a>0:\lambda_a<0\},
\]

one has

\[
\boxed{a_0=a_-}
\]

with the exact sign trichotomy stated in the claim. Consequently the finite strict-negativity thresholds of `PL-266` converge to the unique continuum degeneracy radius, not merely to the right endpoint of a possible zero plateau.

## 7. Prime-lattice interpretation and limitation

Through `PL-265`, increasing `a` enlarges the completed source window and admits prime-power exponent vectors

\[
r e_p\quad\text{with}\quad r\log p\le2a.
\]

It is tempting to attribute the strict fall of `\lambda_a` to the newly entering von-Mangoldt atoms. The proof shows that this interpretation would be wrong. Strictness is already forced by a much more universal structure: the **global translation symmetry of the quadratic form**, the support restriction to a bounded interval, and compact spectral multiplicity.

Accordingly the result passes no rational-prime specificity test. A matched translation-invariant closed form with compact localized resolvent has the same strict-domain mechanism. The zeta-specific question remains whether the particular completed Weil form ever reaches zero. The result removes the plateau ambiguity but does not supply the missing arithmetic sign theorem emphasized by `MI-016` and `PL-264`.

## 8. Prior-art and novelty audit

The load-bearing source is already registered as source 56 in `research/prime_lattice/SOURCES.md`:

- Masatoshi Suzuki, **“Weil's quadratic form via the screw function,” arXiv:2606.09096v2**. Equations (1.1), (1.7), and Corollary 1.2 provide the closed localized form, attained ground energy, and smooth form-core approximation of minimizers; Theorem 1.3 gives continuity. The introduction records the Connes--Consani--Moscovici discrete-spectrum theorem, and Section 4.1 recalls the compact form-domain embedding behind it. The definition `Q_W(v)=W(v*\widetilde v)` gives the translation invariance used here immediately.

A targeted search of Suzuki's paper and nearby localized-Weil literature found domain/nested-core monotonicity and continuity, but did not locate an explicit statement of the strict inequality `\lambda_b<\lambda_a`. The argument is nevertheless a short general symmetry-plus-compactness lemma once the published ingredients are assembled, so **no claim of general mathematical originality is made**. The durable line-specific delta is that the zero-plateau caveat left open by `PL-266` and reduced to proper-support ground states by `PL-267` is eliminated without importing a nonlocal unique-continuation theorem.

## 9. Adversarial checks and falsification boundary

The proof was checked against the main possible failure points.

- **Translation only on smooth functions:** sufficient. Corollary 1.2 supplies form-norm smooth approximants to a minimizer, and exact translation invariance makes their shifted copies Cauchy in the larger closed form.
- **Boundary escape:** shifts are restricted to `|h|<b-a`, so every smooth approximant remains inside `(-b,b)`.
- **A minimum of the form need not be an operator eigenvector:** for a closed semibounded form, equality in the bottom Rayleigh quotient gives the Euler--Lagrange relation and hence membership in the associated operator's bottom eigenspace.
- **Ground-state simplicity:** not used. The contradiction needs only finite multiplicity, supplied by compact resolvent/discrete spectrum.
- **Translated vectors could be dependent:** compact support plus the Fourier-transform argument gives linear independence of every finite set of distinct translates.
- **Arithmetic interpretation:** explicitly excluded. The strictness mechanism survives matched non-zeta translation-invariant forms and therefore does not itself favor rational primes or prove Weil positivity.

The result would fail if the localized objects were not restrictions of one translation-invariant global form, if minimizers could not be approximated in form norm by compactly supported smooth functions while preserving translation, or if the larger localized operator allowed an infinite-dimensional bottom eigenspace. Suzuki's/CCM's cited construction supplies exactly the opposite hypotheses.

## Consequence for the research line

The localized-Weil branch no longer needs a unique-continuation theorem merely to rule out a zero plateau. The qualitative crossing geometry is now rigid: the ground energy decreases strictly with aperture, and any RH failure has one and only one finite zero-crossing radius.

The remaining RH-facing work is therefore not support propagation of a hypothetical plateau state. It is the harder source-side problem already isolated by the line: explain why the **specific unshifted completed Weil form** should stay positive for every finite support window, or find a genuinely zeta-specific global relation among prime-power events and completion data that forces that sign. Quantitative slope/rate control and expanding-window transform convergence remain separate stronger questions.