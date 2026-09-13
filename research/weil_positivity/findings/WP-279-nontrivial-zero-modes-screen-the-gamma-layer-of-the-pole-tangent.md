---
id: WP-279
title: Nontrivial-zero modes screen the Gamma layer of the pole tangent
branch: weil_positivity
status: supported
kind: source-tangent-archimedean-obstruction
claim_strength: exact smoothed explicit-formula scale separation and scalar-renormalization no-go
created: 2026-09-13
related: [WP-270, WP-273, WP-277, WP-278]
prior_art:
  - von Mangoldt explicit formula for the Chebyshev function, including the pole, nontrivial-zero, constant, and trivial-zero terms
  - Delsarte/Weil explicit formula and the identification of the archimedean Gamma factor with the trivial-zero sector
  - J. Arias de Reyna, Explicit formula and quasicrystal definition, arXiv:2402.10604
---

# WP-279 — Nontrivial-zero modes screen the Gamma layer of the pole tangent

## Claim

`WP-278` shows that the canonical critical Mangoldt half-density has the exact pole continuum `cosh(x/2) dx` as its high-energy tangent measure. A natural next possibility is that the **same source**, expanded one order deeper around that tangent, might also force the missing archimedean/Gamma contribution.

The exact smoothed von-Mangoldt formula rules out that scalar asymptotic route. For every `0 <= sigma < 1`, after the pole tangent is removed, the local high-energy residual splits into

1. nontrivial-zero modes with exponential factors `e^{(rho-1)E}`; and
2. trivial-zero/Gamma modes with exponential factors `e^{-(2k+1)E}`, `k >= 1`.

Since every nontrivial zero satisfies `0 < Re rho < 1`, **every nontrivial-zero mode decays strictly more slowly than `e^{-E}`**, whereas the first nonconstant trivial-zero/Gamma mode appears only at `e^{-3E}`. The archimedean normalization constant is already annihilated when the Chebyshev primitive is differentiated to the positive Mangoldt measure.

Consequently, no scalar renormalization of the `WP-278` tangent residual can expose a nonzero first Gamma/trivial-zero limit on the full compactly supported smooth test space while keeping the nontrivial-zero sector bounded. In particular, any normalization `a_E` satisfying

\[
a_E e^{-3E}\longrightarrow c\ne0
\tag{1}
\]

would be strong enough to retain the first trivial-zero term, but `a_E R_{E,\sigma}` cannot converge in `D'(R)`. Reaching that layer requires removing the entire nontrivial-zero contribution first, or applying a test/filter that annihilates it. Either move is precisely the kind of zero-adapted preprocessing that this research line is not allowed to treat as an independent geometric source of positivity.

At the Weil half-density `sigma=1/2`, this means that the exact source-native chain discovered in `WP-278`

\[
\text{Mangoldt atoms}\longrightarrow\cosh(x/2)\,dx
\]

**does not continue as a source-only scalar tangent expansion to the Gamma term**. The pole is intrinsic at leading thermodynamic scale; the next archimedean layer is screened by the nontrivial zero divisor.

**Classification:** `EXACT-DERIVED + CLASSICAL-EXPLICIT-FORMULA + DECISIVE-NEGATIVE-FOR-SCALAR-TANGENT-HIERARCHY + ZERO-MODES-PRECEDE-TRIVIAL-ZERO-GAMMA-LAYER + RH-INDEPENDENT + PRIOR-ART-CLASSICALIZED-INGREDIENTS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Exact residual formula around the `WP-278` tangent

Use the symmetric high-energy measure from `WP-278`,

\[
\eta_{E,\sigma}
=\frac12 e^{-(1-\sigma)E}
\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}
\bigl(\delta_{\log n-E}+\delta_{E-\log n}\bigr).
\tag{2}
\]

For `phi in C_c^infty(R)`, define the even bilateral Laplace transform

\[
B_\phi(z)
:=\int_{\mathbb R}\phi(x)\bigl(e^{zx}+e^{-zx}\bigr)\,dx.
\tag{3}
\]

Let

\[
R_{E,\sigma}(\phi)
:=\langle\eta_{E,\sigma},\phi\rangle
-\int_{\mathbb R}\phi(x)\cosh((1-\sigma)x)\,dx.
\tag{4}
\]

For sufficiently large `E` relative to `supp phi`, the exact von Mangoldt formula may be differentiated distributionally on `(1,infinity)`:

\[
d\psi(t)
=dt
-\sum_\rho t^{\rho-1}\,dt
-\frac{dt}{t(t^2-1)}.
\tag{5}
\]

Here the zero sum is taken in the standard symmetric sense. Equation (5) is the distributional derivative of

\[
\psi_0(t)
=t-\sum_\rho\frac{t^\rho}{\rho}
-\frac{\zeta'(0)}{\zeta(0)}
-\frac12\log(1-t^{-2}).
\tag{6}
\]

Point values at prime-power jumps do not affect the distributional derivative, so `d psi_0=d psi=sum_n Lambda(n) delta_n`. The constant `-zeta'(0)/zeta(0)` disappears at this stage.

Insert (5) into (2). The `dt` term gives the pole tangent **exactly**, not merely asymptotically. On the positive edge, `t=e^{E+x}` produces `e^{(1-sigma)x}/2`; on the reflected edge it produces `e^{-(1-sigma)x}/2`. Their sum is the second term of (4).

For a nontrivial zero `rho`, the two edges give

\[
-\frac12 e^{(\rho-1)E}
B_\phi(\rho-\sigma).
\tag{7}
\]

The trivial-zero term has the convergent expansion

\[
-\frac1{t(t^2-1)}
=-\sum_{k\ge1}t^{-2k-1},
\qquad t>1,
\tag{8}
\]

so its two edges give

\[
-\frac12\sum_{k\ge1}
 e^{-(2k+1)E} B_\phi(2k+\sigma).
\tag{9}
\]

Therefore the exact smoothed residual is

\[
\boxed{
R_{E,\sigma}(\phi)
=-\frac12\sum_\rho
 e^{(\rho-1)E} B_\phi(\rho-\sigma)
-\frac12\sum_{k\ge1}
 e^{-(2k+1)E} B_\phi(2k+\sigma).
}
\tag{10}
\]

Because `phi` is smooth and compactly supported, `B_phi(beta+i gamma-sigma)` decays faster than any power of `|gamma|`, uniformly for `0<beta<1`. Together with the standard zero-counting bound, the first series in (10) is absolutely convergent after smearing and defines a legitimate distributional identity.

A useful structural point is that the **energy decay exponents in (10) are independent of `sigma`**. Changing the finite weight `n^{-sigma}` changes the local `x`-profiles, but it does not move the nontrivial-zero rates `rho-1` or the trivial-zero rates `-(2k+1)`.

## 2. The Gamma/trivial-zero layer sits strictly below every nontrivial zero

The first term of the trivial-zero series is

\[
G^{(1)}_{E,\sigma}(\phi)
=-\frac12e^{-3E}B_\phi(2+\sigma).
\tag{11}
\]

Thus, if the zero sector were absent,

\[
e^{3E}G^{(1)}_{E,\sigma}(\phi)
\longrightarrow
-\frac12B_\phi(2+\sigma).
\tag{12}
\]

At `sigma=1/2`, the corresponding smooth local correction is

\[
-\cosh(5x/2)\,dx.
\tag{13}
\]

Equation (13) is **not** the full Weil archimedean distribution; it is only the first high-energy term coming from the trivial-zero part of the classical Gamma completion. That distinction matters. The result here concerns whether the `WP-278` source tangent can reveal the archimedean completion as a successive scalar asymptotic layer.

For every nontrivial zero `rho=beta+i gamma`, however,

\[
e^{(\rho-1)E}
=e^{-(1-\beta)E}e^{i\gamma E},
\qquad 0<\beta<1.
\tag{14}
\]

Hence

\[
0<1-\beta<1<3.
\tag{15}
\]

Every nontrivial-zero contribution in (10) therefore lies exponentially **above** the first trivial-zero/Gamma correction. This remains true under RH: then `beta=1/2` and the zero modes have size `e^{-E/2}`, still exponentially larger than `e^{-3E}`.

Thus RH would not make the Gamma layer the next correction. The obstruction is a hierarchy statement about the explicit formula, not an off-critical-zero pathology.

## 3. Scalar renormalization no-go

The scale separation can be converted into a clean distributional obstruction.

Suppose a scalar normalization `a_E` is strong enough to retain the first trivial-zero term, so (1) holds. If `a_E R_{E,sigma}` converged in `D'(R)`, then for every test `phi`

\[
R_{E,\sigma}(\phi)=O_\phi(e^{-3E}).
\tag{16}
\]

The trivial-zero series already satisfies that bound. Therefore the nontrivial-zero part

\[
Z_{E,\sigma}(\phi)
:=-\frac12\sum_\rho
 e^{(\rho-1)E}B_\phi(\rho-\sigma)
\tag{17}
\]

would also have to be `O_phi(e^{-3E})`.

Fix any nontrivial zero `rho_0`. Choose an even smooth bump `phi` supported sufficiently close to the origin. Then

\[
B_\phi(\rho_0-\sigma)\ne0,
\tag{18}
\]

because on a sufficiently small support the integrand `2 cosh((rho_0-sigma)x)` is uniformly close to `2`.

For `Re s>0`, the Laplace transform in the edge parameter is obtained termwise from (17):

\[
\mathcal L Z_\phi(s)
=-\frac12\sum_\rho
\frac{e^{-(s+1-\rho)E_0}
 B_\phi(\rho-\sigma)}{s+1-\rho}.
\tag{19}
\]

The rapid decay of `B_phi` makes (19) normally convergent away from its poles. It therefore continues meromorphically with a pole at

\[
s=\rho_0-1,
\qquad -1<\Re(\rho_0-1)<0,
\tag{20}
\]

with nonzero residue (including the multiplicity of `rho_0`).

But the hypothetical bound (16) would make the Laplace integral for `Z_phi` holomorphic throughout

\[
\Re s>-3.
\tag{21}
\]

Equations (20) and (21) are incompatible. Therefore

\[
\boxed{
 a_Ee^{-3E}\to c\ne0
\quad\Longrightarrow\quad
 a_E R_{E,\sigma}
\text{ does not converge in }\mathcal D'(\mathbb R).
}
\tag{22}
\]

The same argument rules out any purported full-test-space `O(e^{-3E})` remainder after only the pole tangent has been subtracted.

## 4. What would be required to reach the archimedean layer

Equation (10) makes the necessary operation explicit. Before the first trivial-zero/Gamma term can become visible at its natural scale, one must remove

\[
\sum_\rho
 e^{(\rho-1)E}B_\phi(\rho-\sigma)
\tag{23}
\]

for the entire nontrivial zero divisor, or restrict to tests satisfying

\[
B_\phi(\rho-\sigma)=0
\qquad\text{for every nontrivial zero }\rho.
\tag{24}
\]

Neither is an innocent continuation of the PNT tangent argument. Equation (23) explicitly uses the zero data. Equation (24) defines a zero-adapted test space; on the full Weil test class it is unavailable unless some independent geometry forces exactly those annihilation conditions.

This is stronger than merely observing that the Gamma term was absent from `WP-278`. It identifies **why the same asymptotic mechanism cannot simply be iterated**. The pole appears before the zero data because it is the leading Weyl density. Once that leading term is removed, the nontrivial zero divisor is the next spectral layer, while the trivial-zero/Gamma tail occurs much later.

The constant `-zeta'(0)/zeta(0)` in (6) gives a second, simpler mismatch: it is destroyed by passage from the Chebyshev primitive to the positive measure `d psi`. Recovering that normalization requires retaining additional primitive/global information, not only the local measure tangent.

## 5. Aggressive falsification and boundary of the no-go

This result does **not** say that Gamma can never arise from Mathia geometry. It closes only the most direct continuation of `WP-278`: successive scalar renormalizations of the same high-energy local tangent residual.

Several escapes remain logically distinct:

- a genuinely global operator/cohomological construction may couple the finite and archimedean sectors **before** the thermodynamic limit;
- a non-scalar transformation may reorganize the zero and trivial-zero sectors through independently forced geometry;
- retaining the Chebyshev primitive rather than only `d psi` may preserve the normalization constant lost in (5);
- an independently constructed archimedean boundary sector may supply Gamma without claiming it is a subleading finite-prime tangent.

But a transformation designed to annihilate the locations `rho`, a factor built from `xi`, or a test class defined by (24) would merely insert the target zero divisor and fails the line's independence requirement.

The obstruction also survives the strongest obvious counterargument: assuming RH only moves all nontrivial modes to the common decay rate `e^{-E/2}`; it does not move them below `e^{-3E}`. The screening is therefore not equivalent to RH and does not rely on a hypothetical off-critical zero.

For generalized-prime systems with an analogous explicit formula, the same ordering occurs whenever a nontrivial zero strip lies between the pole and the trivial-zero sector. This makes the scale hierarchy a classical explicit-formula phenomenon rather than evidence that the Riemann arithmetic has already acquired a special positive geometry.

## 6. Prior-art and novelty audit

The ingredients of (10) are classical. The von Mangoldt explicit formula already decomposes `psi_0` into the pole at `1`, the nontrivial zeros, the constant `-zeta'(0)/zeta(0)`, and the logarithmic term packaging the trivial zeros `-2,-4,...`. Standard explicit-formula literature therefore contains the full analytic content from which the scale ordering follows. `WP-270` and Arias de Reyna's 2024 quasicrystal formulation already identify the exact critical Mangoldt comb and pole continuum used here.

A targeted search for high-energy/scaling-limit formulations did not locate this particular tangent-residual statement as a named theorem, but that absence is **not** a novelty claim. The mathematical delta is only the Mathia-specific consequence of putting the classical explicit formula into the exact `WP-278` edge coordinates: the energy exponents separate into `rho-1` versus `-(2k+1)`, proving that the pole tangent cannot be recursively refined to a Gamma layer before the zero divisor intervenes.

Accordingly this finding should be treated as a derived obstruction and search-narrowing result, not as a new theorem about zeta.

## Consequence for `weil_positivity`

`WP-278` solved one previously open provenance problem: the finite Mangoldt half-density intrinsically generates the exact polar continuum at leading high-energy scale. `WP-279` shows that this success **stops at the pole** for the scalar tangent hierarchy.

The hoped-for single-source sequence

\[
\text{finite Mangoldt carrier}
\longrightarrow
\text{pole continuum}
\longrightarrow
\text{Gamma completion}
\longrightarrow
\text{independent positive Weil form}
\tag{25}
\]

already fails at the second arrow. After pole subtraction, the next asymptotic information is the nontrivial zero divisor itself, not Gamma. Extracting the lower archimedean layer from this same residual would first require a zero-sensitive cancellation and would therefore cease to be the independent source-native explanation sought by the mandate.

The live burden is correspondingly sharper: any viable geometry must either supply the archimedean sector independently but canonically, or couple finite and infinite places globally **before** the high-energy tangent discards/organizes the zero fluctuations. Successive local scalar asymptotics of the `WP-278` carrier are no longer a viable route to the full Weil positivity mechanism.
