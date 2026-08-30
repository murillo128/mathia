# WP-031 — Place-additive positive quadratic readouts cannot select prime powers

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for any attempt to turn the WP-030 incidence data into a single fixed positive quadratic readout by adding finite-place vectors linearly, even after adjoining a fixed archimedean/background vector. A positive semidefinite quadratic form that vanishes on every mixed-prime support must also vanish on every one-prime support. Therefore the exact Mangoldt support cannot arise from a fixed place-additive Hilbert feature followed by a norm square, positive compression, or positive linear functional. The nonlinear/support-dependent rank mechanism of WP-030 is not an accident: within this architecture it is structurally necessary.

## 1. Abstract place-additive setup

Let `V` be a complex vector space equipped with a positive semidefinite Hermitian form

\[
B:V\times V\to\mathbb C,
\qquad
q(x):=B(x,x)\ge0.
\tag{1}
\]

Allow a fixed global/archimedean vector

\[
h_\infty\in V
\]

and finite-place vectors `u_p in V`. For a finite set of distinct primes `S`, define the place-additive feature

\[
x_S
:=
h_\infty+\sum_{p\in S}u_p.
\tag{2}
\]

The same argument allows `u_p` to depend on a chosen exponent `k_p>=1`; one simply fixes those exponents while running the three-prime test below.

A direct positive realization of the von Mangoldt support through this architecture would need

\[
q(x_{\{p\}})>0
\tag{3}
\]

for prime powers, while

\[
q(x_S)=0
\qquad(|S|\ge2)
\tag{4}
\]

for integers having at least two distinct prime divisors. The exact positive value in (3) is irrelevant to the obstruction; it may be `log p`, `(log p)/p^{k/2}`, or any other strictly positive prime-power weight.

The claim is that (3) and (4) are incompatible as soon as there are three distinct primes.

## 2. The zero set of a positive semidefinite form is a linear radical

Define

\[
\mathcal R:=\{x\in V:q(x)=0\}.
\tag{5}
\]

For a positive semidefinite Hermitian form, Cauchy--Schwarz gives

\[
|B(x,y)|^2\le q(x)q(y).
\]

Hence if `x in R`, then `B(x,y)=0` for every `y`; therefore `R` is the radical of `B` and is a linear subspace.

This elementary fact is the entire sign input. Once a mixed-support feature has zero positive energy, it is not merely a point where cancellation happened: the feature lies in a linear nullspace.

## 3. Three primes force the singleton features into the radical

Choose three distinct primes `p,q,r`. By the desired Mangoldt support rule, the three pair features and the triple feature must all lie in the radical:

\[
x_{pq},\ x_{pr},\ x_{qr},\ x_{pqr}\in\mathcal R.
\tag{6}
\]

Using (2),

\[
\begin{aligned}
x_{pq}&=h_\infty+u_p+u_q,\\
x_{pr}&=h_\infty+u_p+u_r,\\
x_{qr}&=h_\infty+u_q+u_r,\\
x_{pqr}&=h_\infty+u_p+u_q+u_r.
\end{aligned}
\]

Because `R` is linear,

\[
x_{pq}+x_{pr}+x_{qr}-2x_{pqr}
=h_\infty
\in\mathcal R.
\tag{7}
\]

Subtracting (7) from the pair relations gives

\[
u_p+u_q,
\quad
u_p+u_r,
\quad
u_q+u_r
\in\mathcal R.
\tag{8}
\]

A second linear combination yields

\[
(u_p+u_q)+(u_p+u_r)-(u_q+u_r)
=2u_p
\in\mathcal R.
\tag{9}
\]

Thus `u_p in R`, and symmetrically `u_q,u_r in R`. Together with `h_infinity in R`,

\[
x_{\{p\}}=h_\infty+u_p\in\mathcal R.
\tag{10}
\]

Therefore

\[
\boxed{q(x_{\{p\}})=0,}
\tag{11}
\]

contradicting (3).

We have proved:

> **Place-additive PSD no-go.** For any fixed positive semidefinite Hermitian form and any feature map of the affine place-additive form `h_infinity + sum_{p in S} u_p`, vanishing on all supports of size at least two forces vanishing on every singleton support. Hence such a positive quadratic feature cannot realize the support of the von Mangoldt function.

The proof is finite-dimensional and uses only the support pattern on three generators.

## 4. Consequence for the WP-030 Gram operator

WP-030 starts from the canonical one-form incidence vector

\[
v_S=\sum_{p\in S}a_p e_p,
\qquad
a_p=\log p,
\]

and its positive rank-one Gram operator

\[
G_S=|v_S\rangle\langle v_S|\succeq0.
\tag{12}
\]

The support-dependent top determinant gives

\[
\sqrt{\det_{\mathbb C^S}G_S}
=
\begin{cases}
\log p,&S=\{p\},\\
0,&|S|\ge2.
\end{cases}
\tag{13}
\]

A natural hope after WP-030 is to replace this nonlinear determinant by a **single positive linear readout** on the globally embedded Gram operators. Embed every finite support canonically into the global one-particle space `ell^2(P)` by zero extension, and let `L` be a positive linear functional on the finite-rank operator system generated there.

On any three-prime subspace define

\[
q_L(v):=L(|v\rangle\langle v|).
\tag{14}
\]

Positivity of `L` makes `q_L` a positive semidefinite quadratic form. If `L(G_S)` vanished for the mixed supports `pq`, `pr`, `qr`, and `pqr`, the theorem above with `h_infinity=0` forces

\[
L(G_{\{p\}})=q_L(a_pe_p)=0.
\tag{15}
\]

Hence

\[
\boxed{
\text{no fixed positive linear functional on the global Gram cone can recover }\Lambda.
}
\tag{16}
\]

This includes ordinary positive traces after a fixed positive compression and, more generally, any architecture whose final scalar is a positive linear functional of `G_S`.

The reason WP-030 escapes is now exact: its readout is **support dependent and nonlinear**. The operator is first restricted to a degree-one space whose dimension is `|S|`, and then its top-dimensional volume is taken. The dimension participating in the invariant changes with the arithmetic support.

## 5. Positive compressions and norm-square feature maps are also covered

Suppose a fixed linear map `J:V->K` into a Hilbert space is used and the candidate coefficient is

\[
Q(S)=\|Jx_S\|^2.
\tag{17}
\]

This is (1) with

\[
B(x,y)=\langle Jx,Jy\rangle.
\]

Therefore the same theorem rules out

```text
place-additive feature
    -> fixed linear compression / boundary map
    -> Hilbert norm square
    -> Mangoldt support.
```

Likewise, a completely positive map followed by a positive trace remains a positive linear functional on the input operator system, so it cannot linearize the WP-030 Gram selector either.

This is stronger than the rank-one extension obstruction in WP-030 Section 5. There the naive addition of an independent infinite-place one-form killed the **top determinant** because the scalar vacuum channel had rank one. Here no rank assumption on the positive form or compression is needed: **every fixed PSD quadratic readout of an affine sum of place vectors fails.**

## 6. The fixed archimedean vector does not repair the support rule

Equation (7) is the useful global part of the obstruction. One might hope that a common archimedean/background feature `h_infinity` could shift the mixed-prime vectors into the null cone while leaving singleton vectors positive. Positive semidefiniteness prevents this.

Because the zero set is a linear radical rather than a curved cone, the pair and triple zero conditions reconstruct the common vector itself inside the radical. Once `h_infinity` is null, the finite generator vectors are forced there as well.

Thus a direct place decomposition of the schematic form

\[
\text{global feature}
=
\text{fixed infinity contribution}
+
\sum_{p\mid n}\text{local prime contribution}
\tag{18}
\]

cannot make the Mangoldt selector emerge from a single positive quadratic theorem.

The half-energy factor does not alter this conclusion. Multiplying the desired scalar by

\[
n^{-1/2}>0
\]

preserves exactly the same zero/nonzero support, so the theorem applies equally to `Lambda(n)` and `Lambda(n)/sqrt(n)`.

## 7. Matched generalized-prime control

Nothing in the proof uses the arithmetic values `log p`, unique factorization beyond the support labels, analytic continuation, or properties of the rational primes. The same contradiction holds for any free commutative monoid with at least three generators and any target coefficient that is positive on powers of one generator and zero on elements involving two or more distinct generators.

This universality is appropriate for a no-go theorem. It shows that the obstruction belongs to the **positive additive geometry**, not to a hidden theorem about `zeta`.

It also prevents overinterpretation: WP-031 supplies no RH evidence. It only removes a broad class of seemingly natural ways to turn the successful local incidence information of WP-030 into one global positive Hilbert pairing.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed.

- The radical property of a positive semidefinite Hermitian form and its Cauchy--Schwarz proof are elementary linear algebra.
- Positive linear functionals restricted to finite matrix algebras induce positive semidefinite quadratic forms through `v -> L(|v><v|)`.
- Fixed Hilbert compressions followed by a norm square are standard positive quadratic constructions.
- The support rule for the von Mangoldt function is classical.

A targeted search for von-Mangoldt/prime-power selectors expressed through fixed positive quadratic forms, Gram readouts, and exterior/Boolean incidence did not identify an authoritative source for this exact packaging. That absence is not used as a novelty claim. The Mathia-specific contribution is the specialization of the elementary radical argument to the live WP-030 globalization problem and the inclusion of a common archimedean/background feature in the same no-go.

This finding is therefore best viewed as an exact **architecture obstruction**, not as a new general theorem in linear algebra or analytic number theory.

## 9. Boundary of the obstruction

WP-031 does **not** rule out:

- the support-dependent exterior-degree/top-volume mechanism of WP-030 itself;
- nonlinear determinant, rank, or wedge constructions performed before the final positive form;
- a signed supertrace or indefinite intermediate pairing such as WP-018;
- an archimedean component that depends nonlinearly on the whole finite support or total energy rather than being a fixed additive place vector;
- tensor, exterior, cohomological, or correspondence constructions in which different places interact before the positive theorem is applied;
- an infinite-dimensional global operation on the Weil test-function space that is not obtained by first assigning one affine place-additive feature to each integer;
- a quotient/localization whose feature map is support dependent rather than a fixed linear compression.

These are genuine escape routes. The theorem should not be quoted as saying that local-to-global decompositions are impossible. It says that **a fixed additive sum of place features cannot be followed by an ordinary PSD quadratic form to create the prime-power support cancellation.**

## 10. Falsification tests and research consequence

The claim is falsified if any of the following fails:

1. the zero set of a positive semidefinite Hermitian form is a linear radical;
2. the four mixed-support zero relations in (6) imply `h_infinity in R` through (7);
3. the three pair relations then imply each local vector lies in `R` through (8)--(9);
4. therefore every singleton feature lies in `R`;
5. a positive linear functional on the globally embedded WP-030 rank-one Gram operators defines a PSD quadratic form as in (14);
6. a fixed positive compression/norm-square readout is a special case of the same theorem;
7. positive critical attenuation cannot alter the support contradiction.

All seven tests reduce to finite-dimensional linear algebra on three generators. No RH assumption, zero data, explicit formula, analytic continuation, or numerical experiment is involved.

The consequence for the research line is sharper than WP-030's rank warning. **The missing global mechanism cannot be an ordinary fixed Hilbert norm of a sum of local place vectors.** If Mathia is to obtain the exact finite Mangoldt cancellation and an independent global sign from one geometry, the interaction between places must become nonlinear, graded, tensorial, support dependent, or otherwise non-additive **before** positivity is taken.

That narrows the live target toward genuinely coupled finite/archimedean structures rather than a positive direct-sum completion of the current incidence data.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-029-even-commutator-energies-radialize-but-positive-one-sided-parts-retain-orientation.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
