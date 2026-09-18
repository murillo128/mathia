# PL-347 — Endpoint-modulation Gram matrices reconstruct the localized Weil form rather than add new lattice rigidity

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`

**Status:** `MODULATION-FAMILY-FORM-CORE + MATRIX-POSITIVITY-EQUALS-LOCALIZED-WEIL-POSITIVITY + DIAGONAL-RIESZ-CHANNEL-EXTENDS-TO-FULL-OLD-FORM + NO-INDEPENDENT-RH-MECHANISM`

## Precise claim

`PL-345` and `PL-346` close the single completed endpoint state: after PNT centering and full Weil completion its diagonal response is the classical first logarithmic Riesz zero residual plus a fixed constant. A natural remaining escape is to keep the same geometric endpoint envelope but retain a **matrix-valued family of vertical modulations** and hope that the cross terms contain rigidity absent from the scalar diagonal.

They do contain strictly more information than one diagonal Riesz channel, but in the maximal natural modulation family that extra information is not new arithmetic structure. It reconstructs the already-classical localized Weil form on a form core.

Fix `A>0`, put

\[
N_A:=1-e^{-A},
\]

and take the normalized endpoint envelope from `PL-346`,

\[
u_A(x)
=
\frac{e^{-(A-|x|)/2}}{\sqrt{2N_A}}
\mathbf 1_{|x|<A}.
\tag{PL347-1}
\]

For

\[
\tau_k:=\frac{\pi k}{A},\qquad k\in\mathbb Z,
\]

define the modulated endpoint states

\[
u_{A,k}(x):=e^{i\tau_k x}u_A(x).
\tag{PL347-2}
\]

Let `Q_W^A` denote the completed Weil quadratic form localized to `[-A,A]`, with associated sesquilinear form also denoted `Q_W^A(\cdot,\cdot)`, and define the infinite Hermitian matrix

\[
K_A(k,\ell):=Q_W^A(u_{A,k},u_{A,\ell}).
\tag{PL347-3}
\]

Then the algebraic span

\[
\mathcal E_A:=\operatorname{span}\{u_{A,k}:k\in\mathbb Z\}
\tag{PL347-4}
\]

is a form core for the localized Weil form. Consequently

\[
\boxed{
K_A\text{ is positive semidefinite on every finite index set}
\iff
Q_W^A\ge0\text{ on its full form domain}.
}
\tag{PL347-5}
\]

Taking every aperture,

\[
\boxed{
RH
\iff
K_A\succeq0
\quad\text{for every }A>0.
}
\tag{PL347-6}
\]

Equation (PL347-6) is exact, but it is **not a new RH mechanism**. It is Weil positivity written in a particular countable modulation frame. Suzuki's localized screw-function operator already realizes the same completed form by a continuous kernel and a self-adjoint localized operator. The endpoint envelope merely supplies an invertible multiplier on the finite interval, while the Fourier modulation family supplies an ordinary complete basis.

Thus the matrix-valued extension suggested after `PL-346` has a sharp boundary: keeping **all** cross-modulations does escape the scalar Riesz diagonal, but only by recovering the whole known Weil problem. A genuinely new Prime-Lattice continuation would have to derive a substantially smaller, source-forced subfamily or extra relation among those matrix entries whose positivity/localization is not equivalent by density to simply assuming the entire localized Weil form.

## 1. Why the modulations are genuinely prime-sensitive

The negative conclusion is not that the off-diagonal entries are empty. They do retain the vertical prime phases required by the Prime-Lattice mandate.

Let

\[
f_k(x):=u_A(x)e^{i\tau_k x},
\qquad
\widetilde f_\ell(x)=\overline{f_\ell(-x)}.
\]

For the correlation appearing in the explicit formula,

\[
H_{k\ell}(y)
:=(f_k*\widetilde f_\ell)(y),
\]

a direct change of variables gives

\[
H_{k\ell}(y)
=
e^{i\tau_\ell y}
\int_{\mathbb R}
 u_A(x)u_A(x-y)
 e^{i(\tau_k-\tau_\ell)x}\,dx.
\tag{PL347-7}
\]

At an arithmetic event `y=log n`,

\[
H_{k\ell}(\log n)
=
n^{i\tau_\ell}
\int
 u_A(x)u_A(x-\log n)
 e^{i(\tau_k-\tau_\ell)x}\,dx.
\tag{PL347-8}
\]

The factor

\[
n^{i\tau_\ell}
=
\exp\!\left(i\tau_\ell\langle v(n),(\log p)_p\rangle\right)
\tag{PL347-9}
\]

is exactly the Kronecker/prime-frequency character singled out by the exponent lattice. The difference frequency `tau_k-tau_ell` additionally probes the geometry of the overlap of the endpoint envelope with its translate by `log n`.

On the diagonal `k=ell`, (PL347-7) reduces to

\[
H_{kk}(y)=e^{i\tau_k y}\phi_A(y),
\qquad
\phi_A=u_A*\widetilde u_A,
\tag{PL347-10}
\]

so the prime term is the vertically modulated endpoint channel of `PL-345`. The new cross terms therefore are real extra data relative to one scalar diagonal. The issue is what that extra data amounts to after all modulations are retained.

## 2. The endpoint envelope is only an invertible multiplier on a fixed window

Inside `(-A,A)`, the envelope is bounded and bounded away from zero:

\[
0<c_A\le u_A(x)\le C_A<\infty.
\tag{PL347-11}
\]

Apart from the harmless cusp at `x=0`, it is piecewise smooth; after extension by zero it has the same endpoint jumps already audited in `PL-346`. Those jumps lie in the logarithmic Fourier form domain of the localized Weil form.

The frequencies `tau_k=pi k/A` are the ordinary Fourier frequencies for the interval of length `2A`. Hence

\[
\{e^{i\tau_k x}:k\in\mathbb Z\}
\]

is the standard complete trigonometric system in `L^2(-A,A)`, and multiplication by `u_A` is an invertible bounded map on `L^2(-A,A)`. Thus `mathcal E_A` is already dense in the localized `L^2` space.

For the quadratic-form statement one needs more than `L^2` density, because the completed Weil form is unbounded. The required upgrade follows from the logarithmic form norm used in the Bombieri/Suzuki realization.

## 3. Form-core derivation

On a fixed compact window, the principal archimedean part of the localized Weil form has the logarithmic Fourier weight used in `PL-346` and in Suzuki's operator realization. It is enough here to work with the model norm

\[
\|f\|_{\log}^2
:=
\int_{\mathbb R}
\log(2+|\xi|)\,|\widehat f(\xi)|^2\,d\xi
+
\|f\|_2^2.
\tag{PL347-12}
\]

The finite prime contribution at fixed `A`, the pole term and the remaining bounded pieces are form-bounded relative to this norm; this is the localized form-domain framework already used in `PL-346` and established in Suzuki's 2026 construction. Therefore convergence in a slightly stronger Sobolev norm gives convergence in the Weil form norm.

Fix any

\[
0<s<\frac12.
\]

Since

\[
\log(2+|\xi|)\le C_s(1+|\xi|^{2s}),
\tag{PL347-13}
\]

one has the continuous embedding

\[
H^s(\mathbb R)\hookrightarrow D_{\log}.
\tag{PL347-14}
\]

Now take `f in C_c^infty(-A,A)` and put `g=f/u_A` on the interval. Because `f` vanishes near the endpoints and `u_A` is positive and piecewise Lipschitz with positive inverse, `g` has an `H^s` periodic extension for every `s<1/2` (in fact it has much more local regularity away from the harmless center cusp). Its Fourier partial sums

\[
p_m(x)=\sum_{|k|\le m}c_k e^{i\tau_kx}
\]

converge to `g` in `H^s(-A,A)`.

For `s<1/2`, multiplication by the interval indicator is bounded on `H^s`, and multiplication by the bounded piecewise-Lipschitz factor `e^{|x|/2}` is bounded as well. Hence

\[
\|u_Ap_m-f\|_{H^s(\mathbb R)}\to0.
\tag{PL347-15}
\]

By (PL347-13),

\[
\|u_Ap_m-f\|_{\log}\to0.
\tag{PL347-16}
\]

Every `u_Ap_m` belongs to `mathcal E_A`. Since smooth compactly supported functions are a core for the localized completed form in the Bombieri/Suzuki framework, (PL347-16) proves

\[
\boxed{
\overline{\mathcal E_A}^{\,\text{form}}=D(Q_W^A).
}
\tag{PL347-17}
\]

The use of `s<1/2` is important: the endpoint jumps of `u_A` are compatible with this subcritical Sobolev control, while the logarithmic Weil form is weaker than every positive fractional Sobolev power. No unjustified smooth-endpoint assumption is being made.

## 4. Gram positivity is exactly localized Weil positivity

For any finitely supported sequence `(c_k)`, sesquilinearity gives

\[
\sum_{k,\ell}c_k\overline{c_\ell}K_A(k,\ell)
=
Q_W^A\!\left(
\sum_k c_k u_{A,k}
\right).
\tag{PL347-18}
\]

Therefore positivity of every finite principal Gram matrix of `K_A` is exactly positivity of `Q_W^A` on `mathcal E_A`. By the form-core identity (PL347-17) and closedness of the localized form, this is equivalent to positivity on the full form domain, proving (PL347-5).

Weil's positivity criterion says that RH is equivalent to nonnegativity of the completed quadratic form on all compactly supported admissible test functions. Equivalently, every finite localization is nonnegative. Hence (PL347-5), for all `A>0`, gives (PL347-6).

This implication uses the **completed** Weil form. It does not continue an Euler product through `Re(s)=1`, and it does not infer the zero expansion of an entry by formal continuation. At fixed `A` the prime side contains only the finitely many prime powers with `log n<2A`; the global equivalence enters only through the already-established completed Weil criterion.

## 5. Why this is a prior-art redirect rather than a new matrix mechanism

The identity (PL347-18) is abstract polarization, while the core statement says that the chosen vectors are merely a concrete complete coordinate system for the localized form. The arithmetic content remains entirely in `Q_W^A` itself.

This sits directly inside established prior art:

- Weil's criterion already identifies global completed-form positivity with RH.
- Bombieri studies the localized quadratic functional and its variational/spectral structure.
- Suzuki's 2023 screw-function work rewrites Weil positivity as positive-definiteness of a continuous kernel.
- Suzuki's 2026 preprint gives a continuous screw-kernel realization of the localized Weil form and its self-adjoint operator, including the form-domain machinery used here.

The targeted novelty audit on 18 September 2026 found no reason to regard the endpoint-modulation frame itself as an independent RH construction. More importantly, no novelty claim is needed for the negative conclusion: **any** complete family in the same localized form domain produces an equivalent Gram-matrix criterion by exactly the same argument. The endpoint envelope is not selected by the arithmetic at this stage; any bounded positive window multiplier with bounded inverse and adequate form regularity would yield an analogous complete modulation family.

This generic replaceability is the decisive control. The matrix criterion looks richer than the scalar endpoint residual because it is richer, but its richness comes from restoring enough coordinates to reconstruct the pre-existing localized operator, not from a new prime-lattice constraint.

## 6. Adversarial audit

### Audit A — Does the result claim that diagonal modulation is already complete?

No. The diagonal values

\[
Q_W^A(u_{A,k})
\]

alone do not determine the full localized form. `PL-345`/`PL-346` correctly identify one diagonal channel with a Riesz-type zero signal. `PL-347` requires the **cross terms** `K_A(k,ell)` and uses their full finite-matrix positivity.

### Audit B — Does one fixed aperture prove RH?

No. For a fixed `A`, (PL347-5) is only the positivity problem for the localized Weil operator at that aperture. Suzuki/Bombieri localization can remain positive on finite windows without RH. The RH equivalence requires the statement for every `A>0`.

### Audit C — Is the form-core step merely `L^2` density?

No. The proof deliberately upgrades Fourier density through `H^s`, `0<s<1/2`, and then uses `log(2+|xi|) <<_s 1+|xi|^(2s)` to enter the logarithmic form norm. This is precisely why endpoint jumps do not invalidate the argument.

### Audit D — Is the critical line newly selected by the modulation matrix?

No. The critical normalization is already built into the completed Weil form and into the endpoint envelope inherited from `PL-341`--`PL-346`. The Gram construction does not derive `1/2` from a new spectral law.

### Audit E — Could a smaller modulation subset still be interesting?

Yes. The negative result applies to a modulation family large enough to be a form core. It does **not** rule out a sparse, source-forced subset of frequencies, a nontrivial coupling law between aperture and frequency, or a different state family whose span is not automatically a core but whose positivity nevertheless forces RH. Such a result would need a theorem explaining why the reduced family is arithmetically sufficient; ordinary Fourier completeness would no longer do the work.

### Audit F — Does this collapse every matrix-valued Prime-Lattice route?

No. It closes only the most direct continuation of the `PL-346` endpoint state: retain the same envelope and promote vertical modulations to their full Gram matrix. Matrix-valued objects with genuinely new noncommutative/source relations remain logically open.

## 7. Research consequence

The completed same-state diagonal is classical Riesz data (`PL-346`). The full cross-modulation matrix is the entire localized Weil form (`PL-347`). These are the two natural extremes:

\[
\text{one endpoint channel}
\longrightarrow
\text{classical Riesz residual},
\]

while

\[
\text{complete endpoint-modulation Gram family}
\longrightarrow
\text{classical localized Weil operator}.
\]

The next useful question is therefore **not** to add more modulations to this same envelope. It is to find an intermediate structure forced by prime-exponent geometry whose information content is strictly between one Riesz diagonal and a complete coordinate reconstruction of the Weil form.

A candidate should be rejected early if either of the following occurs:

1. after completion each observable scalarizes to a classical one-parameter explicit-formula/Riesz criterion; or
2. after polarization the proposed family is a form core, so its matrix positivity is merely Weil positivity in coordinates.

A surviving proposal must instead justify a nontrivial arithmetic sufficiency theorem for a restricted family, or introduce a source-defined coupling/noncommutative relation that is not invariant under arbitrary changes of complete frame.

## Literature / novelty audit

Uses existing entries in `research/prime_lattice/SOURCES.md`:

- source 25: André Weil, explicit-formula / positivity criterion.
- source 26: Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers. I*.
- source 56: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2.
- source 87: Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), 1448--1487.

Fresh audit on 18 September 2026 additionally checked the current public versions/descriptions of Suzuki's 2023 and 2026 screw-function frameworks. They explicitly identify positive-definite kernel / localized-operator formulations equivalent to Weil positivity. No new source entry is required.

The exact endpoint-modulation-core lemma above is stored as an internal derived control, not claimed as external novelty. Its purpose is to prevent future Prime-Lattice passes from mistaking a complete change of coordinates for new RH rigidity.