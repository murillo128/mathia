# WP-043 — cycle-Laplacian shell log-determinants recover Mangoldt, but spectral positivity is the wrong pairing

**Status:** `EXACT-DERIVED + CLASSICAL-CYCLOTOMIC/GRAPH-STRUCTURE + DECISIVE-NEGATIVE` for the scalar spectral-calculus escape left open by `WP-041` and sharpened by `PC-067`. The compatible Prime-Circle cycle Laplacian has an exact primitive-shell determinant whose logarithm is the von Mangoldt function, and the real part of the singular Haar tangent from `WP-037` is exactly a logarithmic functional calculus of that same positive cycle operator. After the unique minimal constant Fourier shift, this produces a canonical nonnegative unbounded multiplier. However, its positivity is **convolution/spectral positivity**, whereas the Prime-Circle birth matrix carrying the finite Weil coefficients is obtained by applying the tangent to **pointwise products** of Ramanujan features. Scalar functional calculus preserves exact-order Fourier shells and therefore cannot generate the required cross-shell birth couplings. The minimal positive-definite shift changes the actual birth matrix only by rank one, while its negative index is unbounded on prime-power boxes, so even that closest positive repair remains indefinite in the relevant pointwise pairing.

This finding does not claim a new identity for `Lambda`: `PC-001` already records `log Phi_n(1)=Lambda(n)`, `PC-008` identifies polygon chord squares with cycle-Laplacian eigenvalues, and `PC-022` records exact-order spectral birth layers. The new content for the Weil-positivity line is their forced synthesis with `WP-037`/`WP-041`: the same intrinsic cycle geometry simultaneously contains an exact Mangoldt shell determinant and a genuine positive logarithmic operator, yet those two facts do **not** assemble into a Weil-positive quadratic form. Any surviving route must introduce a non-scalar/nonseparable operation that converts pointwise shell mixing into a positive pairing before the finite and archimedean sectors are separated.

## 1. The compatible cycle operator and exact-order shells

Let

\[
K=\widehat{\mathbb Z},
\qquad
\widehat K=\mathbb Q/\mathbb Z,
\]

with normalized Haar measure. `WP-041` derives from the actual compatible polygon edges the positive operator

\[
L_{\rm cyc}
=(U-I)^*(U-I)
=2I-U-U^*,
\tag{1}
\]

where `(Uf)(x)=f(x+1)`. On the character `chi_gamma`, with `gamma in Q/Z`,

\[
\boxed{
L_{\rm cyc}\chi_\gamma
=\lambda(\gamma)\chi_\gamma,
\qquad
\lambda(\gamma)
=|1-e^{2\pi i\gamma}|^2
=4\sin^2(\pi\gamma).
}
\tag{2}
\]

For `n>=1`, let `P_n` denote the projector onto characters of exact order `n`, as in the exact-order decomposition of `PC-022`/`PC-066`. Then

\[
\operatorname{rank}P_n=\varphi(n).
\tag{3}
\]

For `n>1`, the restriction `P_nL_{cyc}P_n` is strictly positive because no nontrivial character has `lambda=0`.

## 2. The primitive-shell determinant is exactly `exp(2 Lambda(n))`

The eigenvalues on the exact-order-`n` shell are

\[
\left\{|1-\zeta|^2:\operatorname{ord}(\zeta)=n\right\}.
\tag{4}
\]

Therefore its ordinary finite-dimensional determinant is

\[
\begin{aligned}
\det\!\left(L_{\rm cyc}|_{P_nL^2(K)}\right)
&=\prod_{\operatorname{ord}(\zeta)=n}|1-\zeta|^2\\
&=\left|\prod_{\operatorname{ord}(\zeta)=n}(1-\zeta)\right|^2\\
&=|\Phi_n(1)|^2.
\end{aligned}
\tag{5}
\]

The classical cyclotomic identity already recorded in `PC-001` is

\[
\Phi_n(1)
=\begin{cases}
p,&n=p^k,\\1,&n>1\text{ has at least two distinct prime factors},\end{cases}
\tag{6}
\]

hence

\[
\boxed{
\frac12\log\det\!\left(L_{\rm cyc}|_{P_nL^2(K)}\right)
=\log\Phi_n(1)
=\Lambda(n),
\qquad n>1.
}
\tag{7}
\]

So the compatible positive polygon-edge operator contains the exact prime-power selector in a spectral invariant of its primitive birth shells. This is not a fitted kernel and uses no zero data, zeta continuation, or explicit formula.

Equation (7) is nevertheless a **nonlinear shell readout**. Positivity of `L_cyc` alone does not imply `det>=1`; the arithmetic inequality in this particular spectrum is precisely the cyclotomic identity (6). Moreover the critical Weil coefficient would still require

\[
\frac{\Lambda(n)}{\sqrt n}
=\frac1{2\sqrt n}
\log\det(L_{\rm cyc}|_{P_n}),
\tag{8}
\]

and the factor `n^{-1/2}` is not produced by the compatible edge energy. Recovering exact order and then imposing a function such as `n^{-1/2}` is exactly the conductor-reweighting freedom isolated by `PC-066` and `PC-067` unless a separate geometric mechanism forces it.

## 3. The real Haar tangent is exactly a logarithm of the cycle energy

`WP-037` derives the canonical cylindrical first variation `eta` of the normalized Prime-Circle radial measure at profinite Haar. For every nontrivial character,

\[
\eta(\chi_\gamma)
=-\Log(1-e^{2\pi i\gamma}),
\qquad
\eta(1)=0.
\tag{9}
\]

Let `eta_R` be the reflection-symmetrized real part,

\[
\eta_R(f)
=\frac12\left(\eta(f)+\eta(f\circ[-1])\right)
\tag{10}
\]

on the locally constant Fourier algebra. Since reflection sends `gamma` to `-gamma`, equations (2) and (9) give, for `gamma !=0`,

\[
\boxed{
\eta_R(\chi_\gamma)
=-\log|1-e^{2\pi i\gamma}|
=-\frac12\log\lambda(\gamma).
}
\tag{11}
\]

Thus the singular tangent that carries the Prime-Circle birth operator is not unrelated to the compatible edge geometry: **its even part is the logarithmic spectral kernel of that geometry**.

This sharpens `WP-041`. Ordinary powers of `L_cyc` are bounded or fail to see conductor, but the radial tangent itself selects a singular logarithmic functional calculus at the soft endpoint `lambda=0`.

## 4. The unique minimal constant shift gives a positive unbounded multiplier

Because `0<lambda(gamma)<=4` for `gamma !=0`, equation (11) is bounded below by

\[
\eta_R(\chi_\gamma)\ge-\log2,
\tag{12}
\]

with equality at the order-two character `gamma=1/2`. Hence `log 2` is the **smallest constant Fourier shift** making every nontrivial coefficient nonnegative.

Let `delta_0` be point mass at the distinguished anchor `0 in K` and define the cylindrical functional

\[
\tau:=\eta_R+(\log2)\delta_0.
\tag{13}
\]

Since `delta_0(chi_gamma)=1`, its Fourier coefficients are

\[
\boxed{
\tau(\chi_\gamma)
=\log2-\log|1-e^{2\pi i\gamma}|
=-\log|\sin(\pi\gamma)|
\ge0
}
\tag{14}
\]

for `gamma !=0`, while `tau(1)=log2>0`.

Therefore there is a densely defined positive self-adjoint diagonal operator `A` on `L^2(K)` with

\[
A\chi_\gamma=a(\gamma)\chi_\gamma,
\qquad
a(0)=\log2,
\tag{15}
\]

and, for `gamma !=0`,

\[
\boxed{
a(\gamma)=-\log|\sin(\pi\gamma)|
=\frac12\log\frac4{\lambda(\gamma)}.}
\tag{16}
\]

Equivalently, on the orthogonal complement of constants,

\[
A=\frac12\log\frac4{L_{\rm cyc}}.
\tag{17}
\]

Finite Fourier sums form a dense core for the diagonal form. Its positivity is unconditional and comes from elementary circle geometry, not from RH.

The operator is genuinely unbounded: along `gamma=1/q`,

\[
a(1/q)=\log q-\log\pi+o(1).
\tag{18}
\]

But it is not a coercive conductor Hamiltonian. Along primitive characters tending to `1/2`, for example

\[
\gamma_q=\frac{q-1}{2q}
\quad(q\text{ odd}),
\tag{19}
\]

one has `ord(gamma_q)=q -> infinity` while

\[
a(\gamma_q)\longrightarrow0.
\tag{20}
\]

Thus the positive logarithmic operator has infinitely many high-conductor modes of arbitrarily small energy and no compact resolvent.

## 5. The positivity is convolution positivity, not the Prime-Circle birth pairing

The normalized Ramanujan feature of `WP-037` is

\[
u_n(x)=\frac{c_n(x)}{\sqrt{\varphi(n)}}.
\tag{21}
\]

Its Fourier expansion is exactly

\[
\boxed{
u_n
=\frac1{\sqrt{\varphi(n)}}
\sum_{\operatorname{ord}(\gamma)=n}\chi_\gamma.}
\tag{22}
\]

Hence different `u_n` have disjoint exact-order Fourier support. For **every** scalar spectral multiplier `F(L_cyc)` for which the matrix elements are defined,

\[
\boxed{
\langle u_m,F(L_{\rm cyc})u_n\rangle=0
\qquad(m\ne n).
}
\tag{23}
\]

In particular the positive form of `A` is diagonal in the birth-shell index.

The actual finite arithmetic operator is completely different. `WP-037` proves

\[
\boxed{
C_{mn}=\eta(u_mu_n),
}
\tag{24}
\]

where the product in (24) is **pointwise multiplication on `K`**. Since every `u_n` is real and even,

\[
C_{mn}=\eta_R(u_mu_n).
\tag{25}
\]

Those pointwise products convolve Fourier supports and produce the nonzero cross-shell entries of `C`; in particular `WP-034` gives the interior prime-ray coefficients

\[
C_{dp^k,d}
=-\frac{\log p}{p^{k/2}}
\qquad(p\mid d).
\tag{26}
\]

Equations (23) and (26) are incompatible. The positive operator whose symbol is the logarithmic tangent cannot be the birth pairing that carries the finite Weil comb.

This is the key category mismatch. Nonnegative Fourier coefficients of `tau` give positivity on **convolution squares**: for finite Fourier polynomials `f`,

\[
\tau(f*\widetilde f)\ge0.
\tag{27}
\]

The Weil-relevant matrix instead probes **pointwise products** `u_m u_n`. Positive-definiteness in the convolution algebra does not imply positivity of that pointwise Gram matrix.

## 6. The minimal positive shift still leaves the relevant pointwise matrix indefinite

The mismatch can be falsified without any asymptotic argument. Evaluate the shifted functional (13) on the same pointwise products:

\[
B_{mn}:=\tau(u_mu_n).
\tag{28}
\]

At the anchor,

\[
u_n(0)=\frac{c_n(0)}{\sqrt{\varphi(n)}}
=\sqrt{\varphi(n)}.
\tag{29}
\]

Therefore on any finite shell set,

\[
\boxed{
B=C+(\log2)vv^*,
\qquad
v_n=\sqrt{\varphi(n)}.
}
\tag{30}
\]

So the unique minimal constant shift that makes the Fourier coefficients nonnegative changes the relevant pointwise birth form by only a **rank-one positive perturbation**.

Now restrict to the one-prime divisor box

\[
\{1,p,p^2,\ldots,p^A\}
\tag{31}
\]

for any fixed prime `p>=3`. `WP-034` gives the exact spectrum of the corresponding birth block `H_{p,A}`:

\[
\operatorname{Spec}(H_{p,A})
=(\log p)
\left(
\{-A\}
\cup
\left\{\frac1{p-1}-j:0\le j<A\right\}
\right).
\tag{32}
\]

Hence

\[
n_-(H_{p,A})=A.
\tag{33}
\]

A rank-one Hermitian perturbation can change the negative index by at most one. Combining (30) and (33),

\[
\boxed{
n_-(B|_{\{1,p,\ldots,p^A\}})\ge A-1.}
\tag{34}
\]

Thus the pointwise matrix associated with the closest Fourier-positive repair remains strongly indefinite, with unbounded negative index. This is a decisive obstruction to the proposal

```text
singular Haar tangent
    -> logarithmic cycle multiplier
    -> minimal positive spectral shift
    -> positive Weil birth form.
```

The positivity is real, but it lives in the wrong multiplication structure.

## 7. The compatible inverse-square chord energy does not evade the obstruction

`PC-067` supplies a richer embedded transverse operator

\[
Q_\perp\chi_\gamma
=\sigma(\gamma)\chi_\gamma,
\qquad
\sigma(\gamma)=\frac12r(1-r),
\tag{35}
\]

where `r in [0,1)` represents `gamma`. It resolves exact order set-theoretically even though its spectrum is bounded.

The logarithmic multiplier above is already a scalar singular function of this chord operator. Since

\[
r=\frac{1-\sqrt{1-8\sigma}}2
\quad\text{up to }r\leftrightarrow1-r
\tag{36}
\]

and `sin(pi r)` is reflection invariant,

\[
\boxed{
a
=-\log\cos\!\left(
\frac\pi2\sqrt{1-8\sigma}
\right)
}
\tag{37}
\]

on the nontrivial point spectrum. Thus replacing `L_cyc` by the compatible inverse-square chord energy merely reparametrizes the same symmetrized tangent inside scalar Borel calculus.

More generally every scalar multiplier of `Q_perp` is still diagonal on individual characters, so equation (23)'s cross-shell obstruction remains. `PC-067` is correct that the embedded chord spectrum retains enough information to decode exact order; the present calculation shows that even when the **radial geometry itself selects a distinguished singular decoder**, scalar positivity still cannot produce the pointwise birth matrix.

## 8. What the determinant identity does and does not buy globally

Equation (7) is a stronger local certificate than a generic positive cycle energy: it says the exact finite-prime support is already visible inside a canonical positive operator. But three independent gaps remain.

First, `log det` is nonlinear in the operator and gives a scalar per exact-order shell, not a quadratic form on the Weil test-function space. Second, the critical attenuation `n^{-1/2}` is not selected by the compatible cycle energy. Third, neither `L_cyc`, `A`, nor their primitive-shell determinants generate the Gamma/digamma and polar pieces of the completed explicit formula.

`WP-036` remains relevant because a **different readout of the same pre-renormalized radial Prime-Circle geometry** produces the Riemann digamma scale. But no derived positive object currently couples that Mellin/archimedean readout to the pointwise profinite tangent before subtraction. The present result therefore strengthens the same-parent observation without closing the local-to-global gap.

A successful mechanism would have to perform a genuinely nonseparable operation before positivity is asserted, schematically

```text
radial / profinite / archimedean parent geometry
        -> cross-shell + finite-infinite coupling
        -> one geometric quadratic form
        -> independent sign theorem
        -> Weil functional.
```

Applying scalar positive functional calculus independently to the profinite cycle/chord sector cannot supply that missing mixing.

## 9. Matched controls and novelty audit

No historical novelty is claimed for the individual identities used here.

- `PC-001` already records the classical cyclotomic identity `log Phi_n(1)=Lambda(n)`. Equation (7) is that identity after recognizing each primitive chord square as an eigenvalue of the cycle Laplacian.
- `PC-008` already identifies regular-polygon chord squares with cycle-graph Laplacian eigenvalues and closes single-cycle spectral-zeta routes as prior-art RH reformulations.
- `PC-022` identifies exact-order character spaces as the canonical spectral birth layers of the cyclic cover tower.
- Logarithmic functional calculus of positive graph/Laplacian operators is a standard spectral construction; the research claim here is not the existence of a graph logarithm.
- `WP-037` and `WP-041` supply the Mathia-specific conjunction: the radial Haar tangent and the compatible polygon-edge operator are forced by independent limits of the same Prime-Circle refinement geometry, and equation (11) identifies them exactly.

The determinant/Mangoldt identity is also far below RH specificity. It is an elementary finite cyclotomic statement valid before any global analytic completion. It therefore survives every matched control that retains the ordinary cyclotomic root tower regardless of what global zeta-like object is later attached.

The substantive research consequence is negative but narrow: **a Mathia-native positive logarithmic operator really does exist and really does know the exact Mangoldt shell determinant, yet its scalar spectral positivity cannot be the Weil positivity because the required arithmetic lives in pointwise cross-shell mixing.** This distinguishes a promising-looking exact coefficient coincidence from the missing global sign theorem.

## 10. Boundary and falsification tests

This finding rules out only the scalar cycle/chord spectral-calculus route. It does **not** rule out:

- a matrix-valued or graded operator whose internal channels mix exact-order shells before taking a positive form;
- a non-translation-invariant compression or boundary response that converts pointwise products into a positive geometric pairing;
- a nonlinear determinant/intersection construction in which shell log-determinants enter only after a global finite--archimedean object has been formed;
- a genuinely nonseparable operator on the full arithmetic solenoid rather than on the anchor fiber alone;
- coupling the `WP-036` Mellin/digamma sector to the profinite tangent before either is renormalized;
- or a cohomological/intersection mechanism with its own independent Hodge-type sign theorem.

The claim can be falsified by failure of any of these exact checks:

1. `L_cyc` has character symbol `|1-e^{2 pi i gamma}|^2` as in `WP-041`;
2. the exact-order-`n` determinant is `|Phi_n(1)|^2`;
3. `1/2 log |Phi_n(1)|^2=Lambda(n)` for `n>1`;
4. the symmetrized `WP-037` tangent satisfies `eta_R(chi_gamma)=-1/2 log lambda(gamma)` for every nontrivial character;
5. `log 2` is the minimal constant shift making all those Fourier coefficients nonnegative;
6. the resulting positive multiplier is `a(gamma)=-log|sin(pi gamma)|` but has high-order modes with energy tending to zero near `gamma=1/2`;
7. the Ramanujan feature `u_n` has Fourier support exactly on characters of order `n`, so scalar spectral multipliers have zero matrix elements between distinct `u_m,u_n`;
8. the birth matrix instead satisfies `C_mn=eta_R(u_m u_n)` and has the nonzero prime-power cross-shell entries of `WP-034`;
9. the minimal Fourier-positive shift changes this pointwise matrix by the rank-one term `(log2)vv*` with `v_n=sqrt(phi(n))`;
10. on a `p>=3` prime-power box the original negative index is `A`, so the shifted pointwise matrix has negative index at least `A-1`;
11. the compatible inverse-square chord operator of `PC-067` reproduces the same logarithmic multiplier by the scalar relation (37), and therefore does not alter the shell-mixing obstruction;
12. none of these scalar constructions produces the archimedean Gamma/digamma and polar terms together with the finite birth form under one independent positivity theorem.
