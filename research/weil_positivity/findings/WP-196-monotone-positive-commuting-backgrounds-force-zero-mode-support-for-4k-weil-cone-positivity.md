# WP-196 — Monotone positive commuting backgrounds force zero-mode support for `4k` Weil-cone positivity

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + COMMUTING-FINITE-DIMENSIONAL + MONOTONE-POSITIVE-PAIR + FULL-WEIL-AUTOCORRELATION-CONE + ZERO-MODE-CLASSIFICATION + DECISIVE-NEGATIVE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-195` shows that the scalar centering rigidity of `WP-194` disappears for general finite commuting backgrounds: off-center channels can recover full order-`4k` Weil-autocorrelation positivity when their spectral locations interfere through a positive-definite multiplicity pattern. That escape, however, uses spectrum on both sides of the origin. The smallest example is `diag(0,0,a,-a)`.

There is an exact obstruction in the natural **monotone positive-energy** category. Let `H` and `V` be commuting finite-dimensional self-adjoint operators with

\[
H\ge0,\qquad V\ge0,
\tag{1}
\]

and let the Taylor remainder have order `n=4k`. Then

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H,V)\ge0
\text{ for every real }g\in C_c^\infty(\mathbb R)
\iff
HV=0.
}
\tag{2}
\]

If `V!=0`, the inequality on the right-hand side of (2) is in fact strict for every nonzero `g`.

Thus a commuting positive Hamiltonian cannot use the off-center interference mechanism of `WP-195` while the perturbation is also positive. Full Weil-cone positivity forces every active perturbation channel to start at a zero mode of `H`; the construction then collapses exactly to a direct sum of the universal source-centered carriers from `WP-194` and gains no arithmetic selectivity.

This closes a natural attempt to make the higher-order spectral-shift route geometric by interpreting both the background and the added arithmetic contribution as positive energies. Any surviving source-specific route must leave at least one hypothesis of this classification: commutativity, finite-dimensionality, monotone positivity, or the bare `4k` Taylor-remainder functional.

## 1. Exact commuting reduction with unequal perturbation sizes

Because `H` and `V` commute and are finite-dimensional, diagonalize them simultaneously:

\[
H=\operatorname{diag}(c_1,\ldots,c_N),
\qquad
V=\operatorname{diag}(v_1,\ldots,v_N),
\tag{3}
\]

with

\[
c_j\ge0,\qquad v_j\ge0.
\tag{4}
\]

Fix

\[
n=4k,\qquad r=n-1.
\tag{5}
\]

For an active scalar channel `v_j>0`, the exact Taylor-remainder density from `WP-194` is

\[
q_j(x)
=
\frac{(c_j+v_j-x)^r}{r!}
\mathbf 1_{[c_j,c_j+v_j]}(x).
\tag{6}
\]

A channel with `v_j=0` contributes nothing. Direct-sum additivity therefore gives

\[
\boxed{
\eta_{n,H,V}(x)=\sum_{j:v_j>0}q_j(x).
}
\tag{7}
\]

Unlike `WP-195`, the perturbation sizes need not agree, so there is generally no common centered Fourier factor that can simply be pulled out. The relevant invariant appears instead in the high-frequency boundary asymptotics.

## 2. The source boundary controls the first Fourier tail

Each `q_j` vanishes to order `r` at its terminal endpoint `c_j+v_j`, but at the source endpoint it has the nonzero boundary value

\[
q_j(c_j)=\frac{v_j^r}{r!}.
\tag{8}
\]

One integration by parts gives, as `xi->+infinity`,

\[
\widehat q_j(\xi)
=
\frac{v_j^r}{r!}\frac{e^{-ic_j\xi}}{i\xi}
+O(\xi^{-2}).
\tag{9}
\]

Taking real parts and summing the finitely many channels yields the exact leading asymptotic for the even density:

\[
\boxed{
\widehat{\eta_{n,H,V}^{\rm ev}}(\xi)
=-\frac1{r!\,\xi}
\sum_{j=1}^N v_j^r\sin(c_j\xi)
+O(\xi^{-2}).
}
\tag{10}
\]

Define the finite sine polynomial

\[
S(\xi)=\sum_{j=1}^N v_j^r\sin(c_j\xi).
\tag{11}
\]

Equation (10) is the decisive source-boundary invariant. The terminal endpoints do not appear at order `1/xi`; the leading oscillation remembers only **where each positive perturbation starts**, weighted by its `(4k-1)`st power.

## 3. Full Weil-cone positivity forces the source sine polynomial to vanish

By `WP-193`, order-`4k` positivity on every real compactly supported smooth autocorrelation is equivalent to

\[
\widehat{\eta_{n,H,V}^{\rm ev}}(\xi)\ge0
\qquad\text{for every real }\xi.
\tag{12}
\]

Suppose `S` in (11) is not identically zero. A nonzero finite real sine polynomial assumes both positive and negative values along arbitrarily large positive arguments. One convenient proof is to view the phase vector

\[
\xi\longmapsto
(e^{ic_1\xi},\ldots,e^{ic_N\xi})
\tag{13}
\]

inside its compact torus closure. Translation on that compact subgroup is recurrent. Hence any point where `S` is positive, and its odd reflection where `S` is negative, recur arbitrarily far to the right with their signs preserved. Equivalently, this is the standard almost-periodicity of a finite trigonometric polynomial.

Choose a sequence `xi_m->infinity` on which

\[
S(\xi_m)\ge\varepsilon>0.
\tag{14}
\]

Then (10) gives

\[
\widehat{\eta_{n,H,V}^{\rm ev}}(\xi_m)
<0
\tag{15}
\]

for all sufficiently large `m`, because the `1/xi_m` term dominates the `O(1/xi_m^2)` remainder. This contradicts (12). Therefore

\[
\boxed{S\equiv0.}
\tag{16}
\]

This necessary condition is already stronger than pointwise positivity of the spectral-shift density: every `q_j` in (6) is nonnegative, yet a nonzero source sine polynomial forces failure on the Weil autocorrelation cone.

## 4. Positivity of both operators makes the cancellation impossible off zero

Group equal positive source values. If the distinct positive numbers among the `c_j` with `v_j>0` are `a_1,...,a_M`, then

\[
S(\xi)
=
\sum_{\ell=1}^M A_\ell\sin(a_\ell\xi),
\qquad
A_\ell
=
\sum_{j:c_j=a_\ell}v_j^r>0.
\tag{17}
\]

Distinct sine frequencies are linearly independent. Hence (16) can hold only when there are no positive active source values at all. Therefore

\[
v_j>0\Longrightarrow c_j=0
\qquad\text{for every }j.
\tag{18}
\]

In the simultaneous eigenbasis this is precisely

\[
\boxed{HV=0.}
\tag{19}
\]

This proves the necessary direction of (2).

The converse is immediate from `WP-194`. If `HV=0`, every active scalar channel has `c_j=0`; each centered order-`4k` scalar remainder is strictly positive on every nonzero autocorrelation. Their finite sum is therefore nonnegative, and is strictly positive whenever `V!=0`. Thus (2) is an exact classification, not merely a high-frequency obstruction.

## 5. Matched control: the `WP-195` escape is necessarily sign-indefinite in the background

The off-center positive example of `WP-195`,

\[
H_a=\operatorname{diag}(0,0,a,-a),
\qquad
V=vI,
\tag{20}
\]

works because the source phases combine as

\[
2+e^{-ia\xi}+e^{ia\xi}
=4\cos^2(a\xi/2)\ge0.
\tag{21}
\]

The negative spectral point `-a` is not cosmetic. If one translates the same four source locations by `+a` to make the background positive,

\[
H_a+aI=\operatorname{diag}(a,a,2a,0)\ge0,
\tag{22}
\]

while keeping `V=vI>0`, then `HV!=0`; theorem (2) forces failure of full Weil-cone positivity. This is consistent with the scalar translation sensitivity already seen in `WP-194`.

So the difference-spectrum construction of `WP-195` is a real operator-level escape from scalar centering, but **not** an escape available to a monotone pair of positive commuting energies. The sign-indefinite placement of source spectrum is carrying essential phase-cancellation information.

## 6. Aggressive falsification and exact scope

**The theorem is finite-dimensional.** The proof uses a finite trigonometric polynomial and a uniform finite sum of boundary asymptotics. Infinite commuting Schatten pairs may require summability assumptions strong enough to justify an analogous boundary series. No infinite-dimensional classification is claimed here.

**Commutativity is load-bearing.** Simultaneous diagonalization turns the trace remainder into scalar source intervals. A noncommuting pair can have genuinely matrix-valued multiple-operator-integral structure and is not covered by (2).

**Monotonicity is load-bearing.** If the diagonal perturbations have both signs, the leading coefficients in the source sine polynomial acquire orientations and can cancel even when all source locations are positive. The theorem deliberately isolates the natural category `H>=0`, `V>=0`, not arbitrary signed commuting perturbations.

**Positivity of the spectral-shift density is not enough.** At even order, the current higher-order spectral-shift theory supplies pointwise nonnegativity of the density in much greater generality. Equation (10) shows directly why that independent sign theorem does not imply the Fourier positive-definiteness required by the Weil cone.

**The zero-mode survivor is still nonarithmetic.** When `HV=0`, the sign theorem reduces channel-by-channel to `WP-194`. Arbitrary positive eigenvalues of `V` supported on `ker H` work. Hence the classification does not produce Mangoldt, Gamma, or polar terms; it shows instead that monotone positive spectral geometry collapses to a universal carrier before any arithmetic specificity appears.

**No RH-equivalent data entered the proof.** The argument uses only the exact scalar Taylor density, Fourier asymptotics, finite trigonometric recurrence, and the `WP-193` autocorrelation criterion. No zeta zero data, explicit-formula coefficient fitting, or RH assumption is inserted.

## 7. Prior-art and novelty boundary

The operator-theory framework is classical/current prior art, not claimed as Mathia novelty. Potapov--Skripka--Sukochev establish existence and `L^1` control of higher-order spectral-shift functions for Schatten perturbations; Pradhan--Skripka establish the much stronger pointwise nonnegativity theorem for even-order spectral-shift functions. Earlier work of Skripka studies sufficient positivity conditions for higher-order spectral-shift functions. The harmonic-analysis ingredients used above—endpoint integration by parts, linear independence of distinct exponentials, and almost periodicity of finite trigonometric polynomials—are standard.

A targeted search across higher-order spectral shift, monotone positive perturbations, commuting/diagonal pairs, Fourier positivity, positive-definite spectral-shift densities, and Taylor remainders found these surrounding results but did not expose an established theorem identifying the **full autocorrelation-cone** condition with `HV=0` in the finite commuting positive pair considered here. No standalone operator-theory novelty is asserted from absence of a wording match. The durable contribution is the branch-specific consequence of combining the exact `WP-193` Weil-cone gate with the source-boundary asymptotic: the natural positive-energy specialization eliminates the off-center interference freedom discovered in `WP-195`.

## 8. Consequence for `weil_positivity`

The higher-order spectral-shift route now has a sharper category boundary. `WP-195` prevented us from treating source-centering as an operator-level necessity in general. The present theorem restores a rigidity statement under a geometric hypothesis that is itself natural for energies:

\[
\boxed{
H\ge0,\ V\ge0,\ [H,V]=0
\quad+\quad
\text{full `4k` Weil-cone positivity}
\quad\Longrightarrow\quad
\operatorname{ran}V\subseteq\ker H.
}
\tag{23}
\]

Thus a construction that models the unperturbed geometry by a nonnegative commuting energy and arithmetic input by a monotone positive addition has only the zero-mode carrier available. That carrier is already known to be universal and nonselective. It cannot by itself explain why the same object should generate the finite-prime, Gamma, and polar/global pieces of the completed Weil functional.

The surviving higher-order route must therefore invoke genuinely additional structure before the sign theorem: noncommuting finite--archimedean coupling, sign-indefinite/intersection-type geometry, an infinite or renormalized category not reducible to finite source intervals, or a different canonical positive functional. Merely replacing the scalar background of `WP-194` by a positive commuting Hamiltonian does not create a new bridge.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-194-source-centered-4k-taylor-remainders-are-weil-cone-positive-and-scalar-centering-is-rigid.md`
- `research/weil_positivity/findings/WP-195-positive-definite-background-spectra-preserve-4k-weil-cone-positivity-off-center.md`

## Bottom line

For a finite commuting monotone positive pair `H>=0`, `V>=0`, the order-`4k` Taylor remainder is nonnegative on the entire real Weil autocorrelation cone **exactly when `HV=0`**. The proof is forced by the `1/xi` Fourier tail: every active off-zero source contributes a positive-weight sine phase, and with all source locations on the same half-line those phases cannot cancel identically; recurrence then produces arbitrarily large frequencies with the wrong sign.

This shows that the broad off-center interference family of `WP-195` depends essentially on sign-indefinite source placement. In the positive-energy category, full Weil-cone positivity collapses back to zero-mode perturbations and therefore to the universal nonarithmetic mechanism of `WP-194`, rather than yielding a source-specific global Weil geometry.