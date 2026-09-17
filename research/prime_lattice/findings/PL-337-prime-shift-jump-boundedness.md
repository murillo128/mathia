# PL-337 — Prime shifts are positive atomic jumps, giving uniform `L^infinity` across the first activation

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-CLOSURE + ROUTE-ADVANCE`

**Status:** `FIRST-PRIME-LINFTY-GATE-CLOSED + FIRST-PRIME-REFLECTION-ORIENTED + NO-RH-CONSEQUENCE`

## Precise claim

Let

\[
a_0=\frac12\log 2,
\qquad
I=(-1,1),
\]

and let `A_a` be Suzuki's fixed-domain localized completed-Weil operator used in `PL-291` and `PL-336`. Fix a compact interval

\[
J=[a_0,a_1],
\qquad
a_1<\frac12\log 3.
\tag{PL337-1}
\]

Then for every `M<infinity` there is a constant `C=C(J,M)` such that every real normalized eigenpair

\[
A_a u=\lambda u,
\qquad
a\in J,
\qquad
\|u\|_2=1,
\qquad
|\lambda|\le M,
\tag{PL337-2}
\]

satisfies

\[
\boxed{\|u\|_{L^\infty(I)}\le C.}
\tag{PL337-3}
\]

The constant is uniform through the operator-norm-discontinuous activation of the `n=2` compressed translation at `a=a_0`.

The mechanism is that the symmetric prime correlation has the exact sign of a **positive atomic jump form**. Writing

\[
h(a)=\frac{\log2}{a},
\qquad
w_2=\frac{\Lambda(2)}{\sqrt2}=\frac{\log2}{\sqrt2}>0,
\tag{PL337-4}
\]

and denoting the one-sided compressed translation by `S_h`, the prime operator is

\[
-w_2(S_h+S_h^*)
=w_2D_h-2w_2I,
\qquad
D_h:=2I-S_h-S_h^*.
\tag{PL337-5}
\]

For zero extension `Eu` outside `I`,

\[
\langle D_hu,v\rangle
=
\int_{\mathbb R}
(Eu(x+h)-Eu(x))(Ev(x+h)-Ev(x))\,dx.
\tag{PL337-6}
\]

Hence `D_h` is a nonnegative Dirichlet-form jump channel. For every level `t>=0`, with

\[
T_t(r)=(r-t)^+,
\qquad
w_t=T_t(u),
\]

the scalar contraction inequality

\[
(r-s)(T_t(r)-T_t(s))
\ge
|T_t(r)-T_t(s)|^2
\tag{PL337-7}
\]

gives

\[
\boxed{
\langle D_hu,w_t\rangle
\ge
\langle D_hw_t,w_t\rangle
\ge0.
}
\tag{PL337-8}
\]

This lets the `n=2` shift stay on the coercive side of an `L^infinity` truncation argument instead of being treated as a nonsmoothing right-hand side.

Jarohs--Kassmann--Weth prove an `L^infinity` estimate for weak solutions of weakly singular nonlocal equations with bounded potential and forcing. Their infinite-mass case applies to the singular part of the one-dimensional logarithmic Laplacian. The proof of their estimate is stable under addition of the positive atomic form (PL337-6), because its contribution to the positive and negative truncation tests has the favorable sign (PL337-8). The remaining pieces of Suzuki's operator near the first activation map normalized `L^2` states uniformly into `L^infinity` or are uniformly bounded scalar potentials. This proves (PL337-3).

For the actual simple normalized odd branch `u_delta` of `PL-330`, with

\[
a_\delta=a_0+\delta,
\]

(PL337-3) discharges the sole hypothesis left in `PL-336`. Therefore the endpoint source satisfies `S_delta=O(1)`, the source-selected boundary coefficient satisfies

\[
C_\delta\longrightarrow C_0>0,
\]

and the sharp criterion of `PL-329` becomes

\[
\frac{1+S_\delta}{|C_\delta|\sqrt{L_\delta}}
=O(L_\delta^{-1/2})\longrightarrow0,
\qquad
L_\delta=\log\frac{a_\delta}{\delta}.
\tag{PL337-9}
\]

Consequently the newly active `p=2` reflected correlation of the actual odd branch has the favorable sign for every sufficiently small `delta>0`.

This closes the **first-prime sign gate only**. It does not prove positivity of the localized Weil form at all apertures and does not imply RH.

## 1. Exact prime-shift decomposition

On the interval (PL337-1), no rational-prime source beyond `n=2` is active. The exact prime contribution to Suzuki's quadratic form is, by the source formula used in `PL-324`,

\[
-2w_2 C_{\log2}(u),
\qquad
w_2>0.
\tag{PL337-10}
\]

After the standard unitary rescaling to `I`, this is the quadratic form of

\[
P_a=-w_2(S_{h(a)}+S_{h(a)}^*).
\tag{PL337-11}
\]

The shift is compressed by zero extension, so

\[
\langle S_hu,u\rangle
=
\int_{\mathbb R}Eu(x+h)Eu(x)\,dx.
\]

Expanding the square gives

\[
\int_{\mathbb R}|Eu(x+h)-Eu(x)|^2\,dx
=2\|u\|_2^2-2\langle S_hu,u\rangle
=\langle D_hu,u\rangle.
\tag{PL337-12}
\]

Polarization yields (PL337-6), and (PL337-5) is algebraic.

At the threshold `a=a_0`, one has `h=2`. The translated copies of `I` touch only at a null endpoint, hence `S_2=0` on `L^2(I)`. Therefore `D_2=2I` and

\[
w_2D_2-2w_2I=0,
\]

so the decomposition remains exact at activation. The jump term and its compensating scalar appear separately, but cancel exactly before positive-measure prime overlap begins. This is why the truncation estimate can remain uniform even though `a\mapsto S_{h(a)}` is not operator-norm continuous at the activation.

The key point is the sign. Because `w_2>0`, the non-scalar part `w_2D_h` is positive. If the correlation coefficient had the opposite sign, the same algebra would produce a negative jump energy and the argument below would fail.

## 2. The logarithmic principal operator has an infinite-mass positive core

Chen--Weth's singular-integral formula for the one-dimensional logarithmic Laplacian is

\[
L_\Delta u(x)
=
\int_{\mathbb R}
\frac{u(x)1_{\{|x-y|<1\}}-u(y)}{|x-y|}\,dy
+\rho_1u(x),
\tag{PL337-13}
\]

with the standard Fourier normalization `2 log|xi|`. For zero-exterior `u` and `x in I`, split

\[
\frac12L_\Delta
=\mathscr L_0+B_\infty+c_0I,
\tag{PL337-14}
\]

where

\[
\mathscr L_0u(x)
=
\frac12\int_{|x-y|<1}
\frac{Eu(x)-Eu(y)}{|x-y|}\,dy
\tag{PL337-15}
\]

is the positive singular part and

\[
B_\infty u(x)
=-\frac12\int_{|x-y|\ge1}
\frac{Eu(y)}{|x-y|}\,dy
\tag{PL337-16}
\]

is the far interaction. The latter is harmless for the present purpose:

\[
\|B_\infty u\|_\infty
\le C_I\|u\|_2,
\tag{PL337-17}
\]

because `|x-y|^{-1}<=1` on its integration region and `I` has finite measure.

The governing density for (PL337-15) is

\[
j_0(z)=\frac12\,1_{\{|z|<1\}}\frac1{|z|}.
\tag{PL337-18}
\]

For every fixed `gamma>0`,

\[
\int_{\mathbb R}\min\{1,|z|^\gamma\}j_0(z)\,dz<\infty,
\tag{PL337-19}
\]

while

\[
\boxed{
\int_{\mathbb R}j_0(z)\,dz=\infty.
}
\tag{PL337-20}
\]

Thus the base singular operator lies exactly in the infinite-mass regime of Jarohs--Kassmann--Weth. Their Theorem 1.3 says, in particular, that on a fixed bounded domain an equation

\[
\mathscr L_0u=Wu+f
\]

with zero bounded exterior data and `W,f in L^infinity` obeys

\[
\|u\|_\infty
\le C\bigl(\|f\|_\infty+\|u\|_2\bigr),
\tag{PL337-21}
\]

with arbitrary bounded potential `W` allowed when the governing density has infinite mass.

## 3. The boundedness proof survives the atomic prime jump

The published theorem is stated for kernels represented by measurable densities; `D_h` is an atomic translation channel and is therefore not inserted into that theorem by citation. What is used is the truncation argument in its proof.

For real numbers `r,s`, the map `T_t(r)=(r-t)^+` is monotone and `1`-Lipschitz. Hence

\[
(r-s)(T_t(r)-T_t(s))
\ge
(T_t(r)-T_t(s))^2.
\]

Applying this pointwise with

\[
r=Eu(x+h),\qquad s=Eu(x)
\]

and integrating proves (PL337-8). The same statement holds for the negative truncation by applying the positive truncation to `-u`.

Now suppose

\[
(\mathscr L_0+wD_h)u=Wu+f
\tag{PL337-22}
\]

weakly on `I`, with zero exterior data, `w>=0`, and bounded `W,f`. Testing with `w_t=(u-t)^+` gives the Jarohs--Kassmann--Weth truncation identity for `\mathscr L_0` plus the extra term

\[
w\langle D_hu,w_t\rangle\ge0.
\]

Every lower estimate in the infinite-mass boundedness proof therefore remains valid after the atomic term is added; the new term can simply be discarded from below. Repeating the proof for `-u` gives

\[
\boxed{
\|u\|_\infty
\le C\bigl(\|f\|_\infty+\|u\|_2\bigr)
}
\tag{PL337-23}
\]

with the same type of constant as for the density kernel. In particular, the constant does not deteriorate when `h` approaches `2`, because no inverse estimate for `D_h` is used.

This extension is elementary Dirichlet-form algebra, not a claimed new regularity theorem. The line-specific content is that Suzuki's prime term has exactly the sign and symmetry required to fit it.

## 4. Rewriting the completed-Weil eigen-equation

On `J`, the fixed-domain operator can be written using `PL-291`, `PL-324`, and `PL-336` as

\[
A_a
=
\frac12L_\Delta+b(a)I+R_a-w_2(S_{h(a)}+S_{h(a)}^*),
\tag{PL337-24}
\]

where `b(a)` is a bounded scalar coefficient on `J` and `R_a` is the continuous archimedean completion operator. Its kernel is uniformly bounded on the compact `(a,x,y)` set, so

\[
\boxed{
\sup_{a\in J}\|R_a\|_{L^2(I)\to L^\infty(I)}<\infty.
}
\tag{PL337-25}
\]

Insert (PL337-5) and (PL337-14) into the eigen-equation `A_au=lambda u`. After collecting scalar terms one obtains

\[
(\mathscr L_0+w_2D_{h(a)})u
=W_{a,\lambda}u+f_a,
\tag{PL337-26}
\]

where `W_{a,lambda}` is a scalar potential satisfying, for `a in J` and `|lambda|<=M`,

\[
\sup_{a,\lambda}|W_{a,\lambda}|<\infty,
\tag{PL337-27}
\]

and

\[
f_a=-B_\infty u-R_au.
\tag{PL337-28}
\]

By (PL337-17), (PL337-25), and `\|u\|_2=1`,

\[
\boxed{
\sup_{a\in J}\|f_a\|_\infty<\infty.
}
\tag{PL337-29}
\]

Eigenstates belong to the logarithmic graph domain by `PL-289`, hence in particular to the weak energy space of the singular form (PL337-15). Their zero extension supplies the bounded exterior datum required by the truncation theorem, namely identically zero. Applying (PL337-23) to (PL337-26) proves (PL337-3).

No simplicity, parity, or ground-state property is needed for this boundedness theorem. Those structures enter only when it is applied to the RH-facing odd branch.

## 5. The conditional gate in `PL-336` is now discharged

`PL-336` reduced the complete first-prime continuation problem for the simple odd branch to

\[
\sup_{0\le\delta\le\delta_0}\|u_\delta\|_\infty<\infty.
\tag{PL337-30}
\]

Norm-resolvent/simple-branch continuity from `PL-330` keeps `lambda_delta` in a compact set. Choose `delta_0` so that `a_delta` remains inside a `J` satisfying (PL337-1). Formula (PL337-3) then proves (PL337-30) unconditionally for that branch.

The chain already proved in `PL-336` may therefore be invoked without a new boundary argument:

\[
S_\delta=O(1),
\qquad
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le KQ^{-1}+Ke^{-\eta(Q-R)},
\tag{PL337-31}
\]

\[
C_\delta\to C_0>0,
\tag{PL337-32}
\]

and hence (PL337-9). By `PL-329`, the actual first-prime reflected overlap

\[
H_\delta(g_\delta)
=
\int_0^{2\delta}g_\delta(t)g_\delta(2\delta-t)\,dt
\tag{PL337-33}
\]

is strictly positive for all sufficiently small `delta>0`.

The hostile critical moving layer from `PL-327` is therefore excluded for the actual eigenbranch: producing it would require source amplitude of order `sqrt(L_delta)`, while the exact eigen-equation plus (PL337-3) gives a uniformly bounded source.

## 6. Adversarial and novelty audit

**The `L^infinity` regularity theorem is prior art.** Jarohs--Kassmann--Weth prove boundedness for weak solutions of weakly singular nonlocal equations and explicitly note that their infinite-mass hypothesis allows arbitrary bounded potentials. Chen--Weth provide the exact logarithmic-Laplacian singular-integral decomposition. No novelty is claimed for either ingredient.

**The atomic extension is proved, not attributed.** The prime translation is not an absolutely continuous kernel covered literally by the published theorem. The only imported part is its truncation mechanism. Inequality (PL337-8) proves directly that the added symmetric atomic jump can only improve that argument.

**No contradiction with `PL-324`.** The latter proves that the **odd-cone modulus** `u -> sgn(x)|u(x)|` ceases to contract the full odd-sector Weil form after the first prime event. Here the test is the ordinary scalar truncation `u -> (u-t)^+` on the full interval. The symmetric prime correlation is a positive jump form under that ordinary Markov contraction even though its folded cross-half contribution has the wrong sign for the odd-cone modulus. These are different order structures.

**No contradiction with `PL-304`.** That finding rules out an ambient `L^p`-to-`BV` or measure-to-`BV` resolvent gain. Formula (PL337-3) is only a zero-order `L^infinity` estimate for eigen-equations whose nonsmoothing prime shift has been kept inside a positive Dirichlet form. It supplies no derivative, variation, or generic resolvent smoothing.

**The boundedness mechanism is not uniquely arithmetic.** Any finite symmetric negative-correlation shift with positive coefficient admits the same decomposition into a positive atomic jump plus a scalar. Thus this theorem is not evidence that rational primes alone force RH. Its arithmetic relevance is narrower and exact: the actual `n=2` von-Mangoldt channel has the sign needed to close the already isolated source gate.

**The coefficient sign is load-bearing.** Replacing `-w_2(S_h+S_h^*)` by the opposite sign would yield `-w_2D_h+2w_2I`; then the atomic contribution would work against the truncation inequality and the proof would not apply.

**No hidden use of analytic continuation.** The argument concerns Suzuki's already-defined localized Weil operator, Chen--Weth's real-space logarithmic form, and weak-solution regularity. It makes no Euler-product continuation step and introduces no zeta zero data by hand.

A targeted literature audit did not locate a source stating this exact completed-Weil first-activation closure. Search absence is not treated as a novelty claim. The durable contribution is the exact bridge from the prime correlation sign to the weakly singular truncation theorem and the resulting discharge of `PL-336`.

## 7. Boundaries and failure modes

**Only the first source interval is proved.** The statement uses `a_1<(1/2)log3`, so there is only one active rational-prime lag. The same jump algebra extends to any finite collection of symmetric prime-power correlations with positive von-Mangoldt weights, but later apertures may have additional line-specific obstacles and no global continuation theorem is asserted here.

**No global odd positivity theorem.** Favorable sign of the actual first reflected overlap is much weaker than Beurling--Deny positivity of the odd sector and much weaker than positivity of the full localized Weil quadratic form.

**No simplicity theorem is added.** The uniform boundedness result applies to any bounded-eigenvalue family. Its RH-facing application assumes the simple odd branch already constructed and tracked in `PL-330`.

**No quantitative global constant is optimized.** The proof gives a finite uniform `L^infinity` constant on a compact first-threshold interval. `PL-329` needs only `S_delta=O(1)`, so no sharp value is required.

**Complex states.** The operator is real. For a complex eigenfunction, the estimate applies separately to its real and imaginary parts; the odd branch used downstream is chosen real.

**Later source activations require fresh bookkeeping.** Although each individual symmetric prime-power term has the same favorable full-space jump sign, the endpoint reflection geometry and branch-selection problem change when several channels overlap. Nothing here licenses induction across all prime events.

## Consequence for `prime_lattice`

The first-prime program no longer stops at the conditional sup-norm hypothesis of `PL-336`. The exact correlation sign supplies a positive atomic jump, while the logarithmic singular core has infinite jump mass and the remaining completed-Weil terms are uniformly `L^2 -> L^infinity` on the fixed domain. Therefore the actual normalized odd eigenbranch cannot develop the sup-norm concentration that remained invisible to its `L^2`, graph, and fixed logarithmic-moment controls.

Combining `PL-337` with `PL-329`, `PL-330`, `PL-332`, `PL-335`, and `PL-336` yields the first unconditional post-threshold statement in this continuation chain:

\[
\boxed{
H_\delta(g_\delta)>0
\quad\text{for all sufficiently small }\delta>0.
}
\tag{PL337-34}
\]

This is a genuine route advance but still a local one. The next mathematically meaningful question is not another first-prime regularity norm; it is whether the favorable source-selected mechanism can be propagated through subsequent prime-power activations or converted into a global form-sign principle without falling back to the odd-cone Beurling--Deny obstruction of `PL-324`.

## Dependencies and literature anchors

- `PL-291`: exact logarithmic principal operator, graph-domain control, and uniformly regular continuous completion on compact aperture intervals.
- `PL-304`: ambient `L^p`/measure-to-`BV` no-smoothing control, delimiting what the present result does not imply.
- `PL-324`: exact prime-correlation sign and first activation at `a=(1/2)log2`.
- `PL-329`: sharp source-amplitude criterion orienting the first reflected correlation.
- `PL-330`: norm-resolvent/simple-branch continuity and bounded branch eigenvalues.
- `PL-332`: transport of the source-selected boundary coefficient.
- `PL-335`: positive antisymmetric Hopf lower law at the threshold.
- `PL-336`: reduction of the entire first-prime sign gate to uniform branch `L^infinity` control.
- Source 56 in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- Source 96: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*.
- Source 97: Víctor Hernández-Santamaría, Luis Fernando López Ríos, and Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*.
- Source 104: Sven Jarohs, Moritz Kassmann, and Tobias Weth, *Continuity of solutions to equations with weakly singular nonlocal operators*, *Transactions of the American Mathematical Society* **379** (2026), 7097--7128, DOI `10.1090/tran/9675`.
