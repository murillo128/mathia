# MC-453 — Bounded factorable splitting cannot dilute a quadratic diagonal by a power

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The surviving escape after `MC-451`--`MC-452` is to exploit a genuine well-factorable linear-sieve surrogate **before** the coefficient family is recombined or squared. There are two logically different possible gains in that sentence:

1. gain merely from splitting the sieve coefficient into several well-factorable components; or
2. gain from the internal convolution variables of each component, or from interference retained before positivity.

The first possibility is now closed for any bounded-component decomposition followed by an ordinary positive quadratic estimate.

Let `H` be a Hilbert space, let `T` be any linear map from a coefficient space into `H`, and suppose

\[
\lambda=\sum_{j=1}^{J}\lambda^{(j)}.
\tag{1}
\]

Then

\[
T\lambda=\sum_{j=1}^{J}T\lambda^{(j)},
\]

so Cauchy--Schwarz gives

\[
\boxed{
\sum_{j=1}^{J}\|T\lambda^{(j)}\|_H^2
\ge \frac1J\|T\lambda\|_H^2.
}
\tag{2}
\]

The same statement covers a linear combination `lambda=sum_j c_j lambda^(j)` by absorbing `c_j` into the component vectors.

Therefore splitting a coefficient into `J` pieces and then estimating the pieces through **separate positive quadratic energies** can reduce the recombined diagonal by at most a factor `J`. In particular, if `J=O(1)` the possible dilution is only constant, and if `J=D^{o(1)}` it is only subpower. A fixed-power saving `D^{-delta}` cannot arise from component counting alone unless the number of pieces itself has polynomial size.

This applies directly to the well-factorable linear-sieve route motivating `MC-409`. Bienvenu--Shao--Teräväinen explicitly use the standard linear-sieve coefficients by invoking a result that “splits the linear sieve coefficients into a linear combination of boundedly many well-factorable sequences”; Shao--Teräväinen likewise state that Iwaniec's linear sieve weights are a bounded linear combination of well-factorable weights. Thus the classical well-factorable replacement has exactly the finite-component regime in which `(2)` rules out polynomial diagonal dilution by the decomposition index itself.

The conclusion is deliberately narrow but useful:

> a viable well-factorable escape from the `MC-415` quadratic diagonal must exploit the **internal factorization variables inside a component**, or cancellation/interference **before** the components are separated by absolute values or squares. Merely replacing one linear-sieve weight by boundedly many well-factorable pieces and paying a positive `L^2` diagonal for each piece cannot create a new exponent-saving channel.

No improved Möbius bound, prime-distribution exponent, character-sum estimate, or RH consequence follows.

## 1. Exact finite-component energy floor

Write

\[
v_j:=T\lambda^{(j)}\in H.
\tag{3}
\]

Then

\[
\left\|\sum_{j=1}^{J}v_j\right\|_H^2
\le
\left(\sum_{j=1}^{J}1^2\right)
\left(\sum_{j=1}^{J}\|v_j\|_H^2\right)
=J\sum_{j=1}^{J}\|v_j\|_H^2,
\tag{4}
\]

which is exactly `(2)`.

Nothing arithmetic enters this inequality. It is also sharp at the level of general Hilbert geometry: taking all `v_j=v/J` gives

\[
\sum_j\|v_j\|^2=\frac1J\|v\|^2,
\qquad
\sum_j v_j=v.
\tag{5}
\]

Thus no stronger universal lower factor than `1/J` is available without using additional structure of the components.

The relevant point for the present research branch is not the elementary inequality itself. It is what it forbids after the sieve decomposition has been inserted into a quadratic step. If a method reaches a diagonal of the form

\[
E(\lambda)=\|T\lambda\|_H^2
\tag{6}
\]

and replaces `lambda` by boundedly many well-factorable pieces before applying positivity separately, then its total component diagonal

\[
E_{\mathrm{split}}
:=\sum_j\|T\lambda^{(j)}\|_H^2
\tag{7}
\]

still satisfies

\[
E_{\mathrm{split}}\ge J^{-1}E(\lambda).
\tag{8}
\]

A bounded decomposition can reorganize the proof, but **cannot by itself shrink a positive quadratic obstruction by a power of the main scale**.

## 2. Why this applies to the classical linear-sieve factorization

The literature supplies exactly the bounded-component premise needed above.

Xuancheng Shao and Joni Teräväinen, *The Bombieri--Vinogradov theorem for nilsequences*, Discrete Analysis **2021:21** (2021), arXiv:`2006.05954`, Definition 1.5 and the paragraph immediately following it, define a well-factorable sequence of level `D` by the uniform convolution property

\[
\lambda=\beta*\gamma,
\qquad
\operatorname{supp}\beta\subset[1,R],
\quad
\operatorname{supp}\gamma\subset[1,S],
\quad RS=D,
\tag{9}
\]

with bounded factors, and state that Iwaniec's linear sieve weights arise as a bounded linear combination of such well-factorable weights. Their reference is Friedlander--Iwaniec, *Opera de Cribro*, Lemma 12.16.

A second direct modern use makes the cardinality point explicit. Pierre-Yves Bienvenu, Xuancheng Shao and Joni Teräväinen, *A transference principle for systems of linear equations, and applications to almost twin primes* (MPIM Preprint 2021 (39)), in the proof on p. 34, invoke *Opera de Cribro*, Corollary 12.17, saying that it splits the linear-sieve coefficients into a linear combination of **boundedly many** well-factorable sequences before applying their well-factorable Type II estimate.

James Maynard's *Primes in arithmetic progressions to large moduli II: well-factorable estimates*, Memoirs of the AMS **306** (2025), no. 1543, arXiv:`2006.07088`, gives the complementary boundary: standard sieve weights themselves are not well-factorable, while Iwaniec's slight upper-bound beta-sieve variant is a linear combination of well-factorable sequences; the analytic gain comes from exploiting the stronger factorization properties of those sequences in dispersion estimates, not from a large population of independent components.

These references are prior art for the sieve decomposition, not for `(2)`, which is just Cauchy--Schwarz. No novelty is claimed for either ingredient. The Mathia contribution is the frontier classification obtained by combining them with the exact diagonal re-squaring in `MC-415`.

## 3. Interaction with the existing diagonal obstruction

`MC-415` showed that if

\[
w(n)=\sum_{d\mid n}\lambda_d,
\tag{10}
\]

then the zero-shift term created by an ordinary van der Corput/Cauchy step is

\[
C_0(N)=\sum_{n\le N}|w(n)\chi(n)|^2,
\tag{11}
\]

and `|w(n)|^2` reintroduces the Selberg/lcm quadratic form exactly. Suppose now that the chosen Iwaniec variant is written

\[
\lambda=\sum_{j=1}^{J}\lambda^{(j)}
\tag{12}
\]

with bounded `J` and each `lambda^(j)` well-factorable. For any fixed linear realization of the coefficient family into the source sequence -- for example

\[
(T\lambda)(n)
:=
\chi(n)\sum_{d\mid n}\lambda_d
\mathbf 1_{n\le N},
\tag{13}
\]

we have

\[
C_0(N)=\|T\lambda\|_2^2.
\tag{14}
\]

If the proof now handles each factorable component separately after taking a positive quadratic energy, its aggregate diagonal is

\[
\sum_{j=1}^{J}\|T\lambda^{(j)}\|_2^2
\ge
\frac1J C_0(N).
\tag{15}
\]

Thus the finite decomposition does not remove the diagonal identified by `MC-415`; at best it changes it by a constant factor at this purely positive-energy level.

This also clarifies `MC-451`. That finding ruled out sign cancellation *inside* a fixed-lcm fiber for the standard beta-sieve sign pattern. The present result rules out a different proposed escape: spreading the coefficient among boundedly many factorable components and hoping that the sum of their positive diagonals is polynomially smaller. These are independent obstructions.

`MC-452` then explains why the obvious shortcut -- replacing the specialized Iwaniec surrogate by raw truncated Möbius -- is unavailable: truncated Möbius is not well-factorable at balanced level. The remaining route is therefore genuinely about what the **factor variables of the specialized sieve components** enable before positivity collapses them.

## 4. What remains live

Equation `(2)` does **not** say that well-factorability is useless. On the contrary, its standard analytic value lies precisely outside the hypothesis of this no-go.

For one component, well-factorability permits a representation

\[
\lambda^{(j)}=\beta_j*\gamma_j
\tag{16}
\]

adapted to a chosen factorization `D=RS`. Substituting `(16)` *before* Cauchy or absolute values exposes two modulus variables with controlled ranges. Dispersion, Type I/II estimates, incomplete Kloosterman sums, nilsequence estimates, or related tools may then gain from the resulting bilinear geometry. Shao--Teräväinen's Proposition 6.5 is an explicit example: their proof chooses the well-factorable convolution ranges to fit the Type II variables and only then invokes the deeper estimate.

There is a second possible escape. If the sum over components remains coherent until after an oscillatory transform, cross terms

\[
\langle T\lambda^{(j)},T\lambda^{(k)}\rangle,
\qquad j\ne k,
\tag{17}
\]

may cancel part of the diagonal. Inequality `(2)` says nothing against such cancellation because it applies to the sum of **separately squared** component norms. Any claimed gain of this type must retain and estimate the cross-component interference explicitly rather than discard it by the triangle inequality.

The frontier is therefore sharper than after `MC-451`--`MC-452`:

- the decomposition label `j` is not an exponent-saving resource by itself;
- separate positive component energies preserve the old diagonal up to a bounded factor;
- the only remaining factorability-specific leverage is inside the convolution variables or in interference retained before positive closure.

## Prior-art and novelty boundary

A targeted check on 22 September 2026 found the bounded-component linear-sieve decomposition explicitly in Bienvenu--Shao--Teräväinen and the bounded-linear-combination formulation in Shao--Teräväinen. Maynard records the same Iwaniec factorable-variant boundary and shows why stronger internal factorization properties matter for large-modulus distribution results.

The Hilbert-space estimate `(2)` is elementary Cauchy--Schwarz and is not presented as a new theorem. Nor is the well-factorable decomposition new. The durable result here is a **negative transfer statement for this research frontier**: once a bounded Iwaniec decomposition is passed through a componentwise positive quadratic step, component splitting alone cannot supply the polynomial gain required to defeat the `MC-415` diagonal.

## Boundaries and falsification tests

- **The same linear observable is required.** Equation `(2)` compares components only when they feed the same linear map `T`. If factorization changes the operator or introduces new variables before the quadratic step, that is additional structure and lies outside this no-go.
- **Only the sum of component energies is controlled from below.** No lower bound is asserted for any individual component. One piece may be tiny or zero.
- **Bounded component count is load-bearing.** If `J` were as large as `D^delta`, the sharp example `(5)` shows that `D^{-delta}` dilution is algebraically possible. The classical linear-sieve use cited above is specifically boundedly many components.
- **Cross-component cancellation remains live.** Recombining before squaring can exploit the cross terms in `(17)`. A proof that retains them has not reduced to `(7)`.
- **Internal well-factorability remains live.** The convolution variables in `(16)` can power bilinear/dispersion estimates before positivity. This is the main surviving route, not a contradiction to the finding.
- **No claim is made about the numerical size of `C_0(N)`.** `MC-415` already separates existence of the diagonal from whether a sharp second-moment theorem makes it affordable. The present result only limits what finite component splitting can do to that cost.
- **No zero-free or RH-scale input is used.** The exact obstruction is finite-dimensional Hilbert-space algebra plus the literature fact that the relevant sieve decomposition has bounded component count.

## Consequence for the research line

The next useful calculation should no longer ask whether the Iwaniec linear-sieve surrogate can be decomposed into well-factorable pieces; classical sieve theory already answers yes, and `(2)` shows that the finite list of pieces is not itself a power-saving channel.

The live question is more specific: choose one genuine well-factorable component, expose a balanced convolution `beta*gamma`, and carry its two factor variables through the incomplete shifted/source-dependent object **before** the first positive closure. One must then identify an off-diagonal estimate whose gain survives the `MC-415` diagonal budget. If the proof splits into boundedly many components and immediately applies absolute values or `L^2` independently to each without using `(16)`, it has not used the mathematical content of well-factorability strongly enough to change the exponent frontier.