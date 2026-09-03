# WP-123 — Finite-order local Sobolev renormalizations amplify critical prime shells

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + FINITE-ORDER-SOBOLEV + ENDPOINT-JET + BOUNDARY-LAYER + PRIME-CIRCLE-BRIDGE + MATCHED-CONTROL + PRIOR-ART-AUDITED`.

`WP-122` closes every nontrivial fixed zero-order jump-local positive Radon geometry for the canonical Gamma--Schoenberg increment

\[
u_t(y)
=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix},
\qquad y>0,
\tag{1}
\]

but deliberately leaves derivative/Sobolev local forms outside its theorem. The exact Cesaro Gram kernel behind that finding has a shrinking `y=O(1/T)` weak boundary layer, suggesting that one might concentrate and renormalize the positive geometry near `y=0` until a derivative or Sobolev form survives.

For every **fixed finite-order local positive differential geometry**, that escape fails more strongly than the zero-order route. Differentiation does not damp the logarithmic prime carrier: it multiplies the frequency `t=log p` by powers of `log p`. A multiplicative prime shell therefore acquires an additional factor `(log X)^r` at derivative order `r`, and positivity again leaves a nonzero phase-averaged shell energy. At the exact Weil exponent `sigma=1/2`, every nontrivial order-`r` channel has shell energy at least along a sequence of size

\[
\boxed{
X(\log X)^{2r}.
}
\tag{2}
\]

The same obstruction holds for any nonzero finite positive **endpoint jet form** obtained as a fixed boundary-layer limit. Thus a boundary-layer family can suppress a shell only by letting its scale continue to track the shell frequency itself. That produces a frequency/cutoff-dependent family of norms, not one fixed Mathia geometry whose positivity can imply a global Weil criterion.

This closes the finite-order local derivative/Sobolev interpretation of `CLUE-critical-jump-boundary-layer-renormalization`. It does **not** close genuinely nonlocal negative/fractional Sobolev geometries, infinite-order analytic/Gevrey jet spaces, quotients formed before the norm, prime-frequency-dependent forms, or nonseparable finite--archimedean structures.

## 1. Positive finite-order local differential forms

For an integer `m>=0`, write the finite jet

\[
\mathcal J_m g(y)
=
\bigl(g(y),g'(y),\ldots,g^{(m)}(y)\bigr)
\in \mathbb R^{2(m+1)}.
\tag{3}
\]

Let `Sigma` be a nonzero locally finite positive-semidefinite
`2(m+1) x 2(m+1)` matrix-valued Radon measure on `(0,infinity)`, and define the extended positive form

\[
\boxed{
\mathcal E_\Sigma(g)
=
\int_{(0,\infty)}
\mathcal J_m g(y)^T\,d\Sigma(y)\,\mathcal J_m g(y)
\ge0.
}
\tag{4}
\]

This class contains fixed finite sums of local squares of derivatives, matrix-valued weighted Sobolev energies, singular derivative measures, and their finite cross-order Gram couplings. The block positivity is important: arbitrary signed lower-order corrections that happen to be positive only after a global inequality are not being silently declared local Gram geometry.

As in `WP-122`, put

\[
\tau=\operatorname{tr}\Sigma,
\qquad
d\Sigma=W\,d\tau,
\qquad
W(y)\succeq0,
\qquad
\operatorname{tr}W(y)=1
\quad\tau\text{-a.e.}
\tag{5}
\]

Because `Sigma` is nonzero, choose a compact `K` inside `(0,infinity)` with `0<tau(K)<infinity`. Decompose `W` into `2 x 2` derivative-order blocks `W_{jk}`. Let `r` be the largest index for which

\[
\int_K \operatorname{tr}W_{rr}(y)\,d\tau(y)>0.
\tag{6}
\]

For every `j>r`, the nonnegative function `tr W_{jj}` has zero integral on `K`, hence `W_{jj}=0` almost everywhere there. Positivity of the full block matrix then forces the entire `j`-th row and column to vanish almost everywhere on `K`. Thus `r` is the highest derivative order genuinely seen by this restricted positive geometry.

The case `r=0` is exactly the zero-order compact restriction already handled by `WP-122`. The new issue is `r>=1`.

## 2. Differentiating the canonical Gamma increment multiplies the carrier by powers of log p

Use the complex representative

\[
c_t(y)=e^{ity}-1,
\tag{7}
\]

whose real and imaginary parts are the two components of (1). For every `j>=1`,

\[
\boxed{
c_t^{(j)}(y)
=
(it)^j e^{ity}.
}
\tag{8}
\]

Thus derivative order `j` does not provide high-frequency smoothing. It multiplies the rotating carrier by `t^j`.

Fix a multiplicative shell ratio `q>1`, `0<sigma<=1`, and define

\[
B_{X,\sigma,j,q}
:=
\sum_{X<p\le qX}
\frac{(\log p)^{j+1}}{p^\sigma}.
\tag{9}
\]

The same PNT plus Stieltjes-partial-summation argument used in `WP-121`--`WP-122`, with the slowly varying extra factor `(log p)^j`, gives for `0<sigma<1`

\[
\boxed{
B_{X,\sigma,j,q}
=
(\log X)^j X^{1-\sigma}
\left(J_{\sigma,q}(0)+o(1)\right),
}
\tag{10}
\]

where

\[
J_{\sigma,q}(y)=\int_1^q u^{-\sigma+iy}\,du.
\tag{11}
\]

At `sigma=1`,

\[
\boxed{
B_{X,1,j,q}
=
(\log X)^j\left(\log q+o(1)\right).
}
\tag{12}
\]

Define the normalized internal phase profile

\[
m_{X,\sigma,j,q}(y)
=
\frac{1}{B_{X,\sigma,j,q}}
\sum_{X<p\le qX}
\frac{(\log p)^{j+1}}{p^\sigma}
\left(\frac pX\right)^{iy}.
\tag{13}
\]

Since `log p/log X=1+O_q(1/log X)` uniformly on the shell, the extra logarithmic power disappears after normalization, and locally uniformly in real `y`

\[
\boxed{
m_{X,\sigma,j,q}(y)
\longrightarrow
m_{\sigma,q}(y)
:=
\frac{J_{\sigma,q}(y)}{J_{\sigma,q}(0)}.
}
\tag{14}
\]

For `0<sigma<1`, `m_{\sigma,q}(y)` has no real zeros, exactly as in `WP-122`. At `sigma=1`, a generic fixed `q` avoids any atoms of a given compact singular measure on the discrete zero set, again exactly as in `WP-122`.

## 3. The highest visible derivative order survives phase averaging with strictly positive energy

Let

\[
F_{X,\sigma,q}(y)
=
\sum_{X<p\le qX}
\frac{\log p}{p^\sigma}\,u_{\log p}(y)
\tag{15}
\]

be the prime-shell vector and write `L=log X`.

For `r>=1`, equations (8) and (13) imply that after dividing by `B_{X,sigma,r,q}`, the `r`-th derivative block of `F_X` is a fixed quarter-turn of

\[
\begin{pmatrix}
\operatorname{Re}\!\left(e^{iLy}m_{X,\sigma,r,q}(y)\right)\\
\operatorname{Im}\!\left(e^{iLy}m_{X,\sigma,r,q}(y)\right)
\end{pmatrix}.
\tag{16}
\]

Every lower derivative block is negligible at this normalization. Indeed, for `j<r`,

\[
\frac{B_{X,\sigma,j,q}}{B_{X,\sigma,r,q}}
=
O\!\left((\log X)^{j-r}\right)
\longrightarrow0.
\tag{17}
\]

The zero-order anchor `-1` in (7) has shell size `B_{X,sigma,0,q}` and is therefore negligible as well when `r>=1`.

Restrict (4) to `K` and normalize by `B_{X,sigma,r,q}^2`. Because all blocks above `r` vanish on `K`, the lower blocks vanish by (17), and (14) is locally uniform, the only surviving term is the `rr` block. Cesaro-average the shell location `L` over `[T,2T]`, as in `WP-122`. For every fixed `y>0` the linear and double rotating phases average to zero, while the positive quadratic phase average is isotropic. Therefore

\[
\boxed{
\frac1T\int_T^{2T}
\frac{\mathcal E_{\Sigma,K}
(F_{e^L,\sigma,q})}
{B_{e^L,\sigma,r,q}^{\,2}}
\,dL
\longrightarrow
C_{\sigma,q,K}^{(r)}(\Sigma),
}
\tag{18}
\]

with

\[
\boxed{
C_{\sigma,q,K}^{(r)}(\Sigma)
=
\frac12
\int_K
|m_{\sigma,q}(y)|^2
\operatorname{tr}W_{rr}(y)\,d\tau(y)
>0
}
\tag{19}
\]

for `0<sigma<1`; at `sigma=1` choose the same generic shell ratio as in `WP-122`.

Hence arbitrarily far out there are multiplicative shell tails satisfying

\[
\boxed{
\mathcal E_{\Sigma,K}(F_{X,\sigma,q})
\ge
\frac12 C_{\sigma,q,K}^{(r)}(\Sigma)
B_{X,\sigma,r,q}^{\,2}.
}
\tag{20}
\]

Since restricted energy is bounded above by the full positive energy, these shell tails cannot tend to zero in the global seminorm.

At the exact Weil value `sigma=1/2`, equations (10) and (11) give

\[
B_{X,1/2,r,q}
=
2(\sqrt q-1)\sqrt X\,(\log X)^r(1+o(1)),
\tag{21}
\]

so along a sequence `X_n->infinity`

\[
\boxed{
\mathcal E_\Sigma(F_{X_n,1/2,q})
\gg
X_n(\log X_n)^{2r}.
}
\tag{22}
\]

The zero-order case `r=0` recovers the `X` lower bound of `WP-122`; every genuine derivative order makes the critical obstruction stronger.

For `0<sigma<1` the same argument gives shell energy of order at least

\[
X^{2(1-\sigma)}(\log X)^{2r}
\tag{23}
\]

along a sequence. At `sigma=1`, `r=0` retains a nonzero shell floor as in `WP-122`, while every `r>=1` grows at least like `(log X)^{2r}`. Thus no nontrivial fixed finite-order local positive differential geometry makes the coherent prime series Cauchy anywhere through `sigma=1`.

## 4. A fixed endpoint-jet limit also amplifies rather than damps prime frequencies

The boundary layer in `CLUE-critical-jump-boundary-layer-renormalization` can concentrate all mass at `y=0` in the limit, which lies outside a Radon measure on the open jump coordinate. The natural finite-order positive limit is then a jet form.

For `m>=1`, let `Q\succeq0` be a fixed matrix on the derivative trace space

\[
\mathcal J_m^+g(0)
=
\bigl(g'(0),\ldots,g^{(m)}(0)\bigr),
\tag{24}
\]

and define

\[
\mathcal E_Q^0(g)
=
\mathcal J_m^+g(0)^T
Q
\mathcal J_m^+g(0).
\tag{25}
\]

For the canonical increment,

\[
u_t^{(j)}(0)=t^j v_j,
\qquad j\ge1,
\tag{26}
\]

where each `v_j` is a fixed signed coordinate vector: odd `j` lies in the sine component and even `j` in the cosine component.

Therefore the shell jet is exactly

\[
\boxed{
\mathcal J_m^+F_{X,\sigma,q}(0)
=
\sum_{j=1}^m
B_{X,\sigma,j,q}v_j.
}
\tag{27}
\]

Assume the endpoint form is nontrivial on the canonical prime carrier. Then `v_j^TQv_j>0` for at least one `j`. Let `r` be the largest such index. For a positive-semidefinite matrix, `v_j^TQv_j=0` implies `Qv_j=0`, so every higher `v_j` is completely invisible to the form. Using (17),

\[
\boxed{
\mathcal E_Q^0(F_{X,\sigma,q})
=
B_{X,\sigma,r,q}^{\,2}
\left(v_r^TQv_r+o(1)\right).
}
\tag{28}
\]

At `sigma=1/2` this again grows like

\[
\boxed{
X(\log X)^{2r}.
}
\tag{29}
\]

A positive trace form that acts only on `g(0)` is a degenerate control, not an escape: every canonical increment satisfies `u_t(0)=0`, so such a form sees **none** of the finite-prime carrier and cannot produce the finite Weil term.

Thus every nonzero fixed finite-jet boundary completion that actually sees the canonical Gamma--Schoenberg prime increments fails the critical Cauchy test.

## 5. Why the shrinking Cesaro boundary layer does not define a fixed positive rescue

The exact averaged matrix highlighted by the clue is

\[
M_T(y)
=
\frac1T\int_0^T u_t(y)u_t(y)^T\,dt
=
M(Ty).
\tag{30}
\]

Its weak eigenvalue is quartic as `Ty->0`, while the strong channel is quadratic. This is a real finite-scale feature, but it has only two possible interpretations.

First, **freeze a geometry** after renormalizing the shrinking region. Ordinary finite-order boundary concentration produces a nonzero derivative trace or finite Sobolev/jet form. Sections 3--4 show that such a fixed limit multiplies the prime frequency by powers of `log p` and therefore makes critical shell divergence at least as bad as the zero-order geometry.

Second, **keep changing the geometry with the shell** so that the concentration scale remains `y=O(1/log X)` while testing primes near `X`. Then the same parameter that labels the prime shell chooses the norm. This can exploit the weak finite-scale eigenchannel, but it no longer gives one fixed Hilbert/Dirichlet geometry in which the ordered prime series is Cauchy. It is precisely the prime-frequency/cutoff-dependent escape excluded by the research contract unless an independent Mathia object forces that two-scale family and supplies a fixed global limit theorem.

The order of limits is therefore decisive:

\[
\boxed{
\text{fixed renormalized endpoint geometry}
\Longrightarrow
\text{derivative-frequency amplification},
}
\tag{31}
\]

whereas synchronizing the geometric scale with `log X` abandons the fixed-geometry premise.

## 6. Matched controls and exact scope boundary

**Off-critical shell control.** For every fixed finite derivative order `r` and `sigma>1`,

\[
B_{X,\sigma,r,q}
\asymp
X^{1-\sigma}(\log X)^r
\longrightarrow0.
\tag{32}
\]

Thus the shell lower-bound mechanism disappears on the absolutely convergent side. No global convergence theorem is claimed for arbitrary unbounded derivative measures; the point is that the critical obstruction is not a tautology caused by differentiation alone.

**Zero-order control.** Setting `m=0` reduces exactly to the singular-measure theorem `WP-122`. The present result genuinely extends its stated scope rather than replacing its proof.

**Degenerate endpoint control.** A positive endpoint form supported only on the value `g(0)` vanishes identically on all `u_t`. Such zero cost cannot be interpreted as Weil positivity because it has discarded the finite-prime data.

**Negative/fractional-order control.** A fixed negative-order Sobolev multiplier can damp high frequencies and is not a finite-order local differential form of (4) or a finite jet form of (25). It remains outside this theorem. `WP-109`--`WP-110` give separate Sobolev obstructions for the prime-torus completion, but those product/Kronecker results are not being promoted into a universal statement about the Gamma jump coordinate.

**Nonlocal and pre-norm controls.** Integral kernels coupling distinct jump scales, quotients/primitive sectors formed before the positive norm, and genuinely nonseparable finite--archimedean geometry are not covered. They can change the phase-averaging argument rather than merely reweight its local derivatives.

## 7. Prior-art and novelty audit

The analytic ingredients are classical and no theorem-level novelty is claimed for them. Finite-order Sobolev/differential energies, boundary traces, and positive Gram forms are standard; Beurling--Deny theory already separates local/diffusion and jump contributions in Dirichlet forms, and the jump-form literature recorded in `research/weil_positivity/SOURCES.md` is the relevant comparison class. Concentrating thin boundary layers to trace energies is likewise a classical Sobolev phenomenon. The prime-number-theorem shell asymptotics and the shell-location Cesaro device are inherited from `WP-121`--`WP-122`.

A targeted literature audit found no basis for presenting differentiation, Sobolev boundary traces, or boundary-layer renormalization themselves as Mathia discoveries, and no external result was found that would supply the missing global Weil sign from this construction. The Mathia-specific durable content is narrower: **the exact Gamma--Schoenberg carrier identified in `WP-117` and the exact critical prime amplitudes force every fixed positive finite-order local derivative/endpoint-jet completion to amplify, rather than cure, the coherent shell obstruction explicitly left open by `WP-122`.**

This is therefore a structural negative within a classical analytic envelope, not evidence for a new proof of RH.

## 8. Consequence for Weil positivity

The shrinking weak channel after `WP-122` does not provide a finite-order local route to a global Weil positivity theorem. Once the renormalized geometry is fixed, its derivative or endpoint-jet positivity is independent and genuine, but the exact critical prime carrier is not even in its coherent Cauchy domain.

The local boundary-layer route is narrowed to mechanisms that change the mathematical category before positivity is applied:

- a genuinely nonlocal negative/fractional-order form with an intrinsic, not hand-picked, symbol;
- an infinite-order completion with an independently forced domain;
- a quotient or primitive sector that removes the coherent shell before taking the norm;
- or a nonseparable finite--archimedean object whose global coupling changes the carrier itself.

Any such survivor still has to generate the Gamma and polar/counterterm pieces from the same structure and pass the existing classical Weil/trace/cohomological prior-art audit. Merely synchronizing a positive local norm with the prime cutoff is not a fixed geometric positivity mechanism.
