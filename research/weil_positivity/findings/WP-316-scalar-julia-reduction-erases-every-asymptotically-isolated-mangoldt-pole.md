---
id: WP-316
title: Scalar Julia reduction erases every asymptotically isolated Mangoldt pole
branch: weil_positivity
status: supported
kind: support-side-isolated-pole-julia-trivialization
claim_strength: exact local classification for classical scalar Julia–Nevanlinna reduction near a moving Mangoldt pole; if the focal atom dominates the boundary derivative, the canonically normalized local Julia profile converges to a removable real constant, so every nonconstant support-side tangent must contain order-one background derivative and is therefore genuinely multipole rather than a one-atom geometric completion
created: 2026-09-15
related: [WP-304, WP-305, WP-312, WP-314, WP-315]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for classical Julia–Nevanlinna reduction and its Schur-complement positivity
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for the Herglotz representation used to control the positive background
---

# WP-316 — Scalar Julia reduction erases every asymptotically isolated Mangoldt pole

## Claim

`WP-315` shows that the most obvious support-side localization of the reflected Mangoldt Herglotz source, namely the single-atom mass scale, is not uniformly an isolated-pole geometry: bounded prime clusters force arbitrarily many comparable atoms to collapse into that chart. This leaves a possible escape in the opposite regime. One could choose a source gap and a moving regular Julia node on a scale at which one focal Mangoldt pole really **is** isolated.

Classical scalar [[research/prior_art/incremental/PA-julia-nevanlinna-boundary-reduction|Julia–Nevanlinna reduction]] then removes precisely the structure one hoped to use.

Let `f` be a Pick/Herglotz function with a simple real pole at `x`, written

\[
f(z)=-\frac{a}{z-x}+h(z),
\qquad a>0,
\tag{1}
\]

where `h` is again Pick/Herglotz. Choose a regular real node

\[
t=x+\sigma r,
\qquad r>0,
\qquad \sigma\in\{-1,+1\},
\tag{2}
\]

in a support-free interval, and put

\[
d=f'(t)=\frac{a}{r^2}+h'(t)>0.
\tag{3}
\]

The unit-log-normalized Julia response used in `WP-312` is

\[
\mathcal J_t[f](z)
=
\frac{d(z-t)(f(z)-f(t))}
{d(z-t)-(f(z)-f(t))}
+\beta,
\qquad \beta\in\mathbb R.
\tag{4}
\]

Define the exact dimensionless background-to-pole derivative ratio

\[
\kappa(t;x,a,r)
:=\frac{r^2}{a}h'(t)\ge0.
\tag{5}
\]

If along any moving-pole sequence

\[
\boxed{\kappa_j\longrightarrow0,}
\tag{6}
\]

then, locally uniformly for `zeta` in the upper half-plane,

\[
\boxed{
\frac{r_j}{a_j}
\bigl(\mathcal J_{t_j}[f_j](x_j+r_j\zeta)-\beta_j\bigr)
\longrightarrow \sigma_j
}
\tag{7}
\]

on every subsequence with fixed side `sigma_j=sigma`. The limit is a real constant. Since `beta_j` is already an arbitrary real translation in the canonical Julia normalization, this constant carries no nontrivial local Pick geometry.

For the pure one-pole matched control `h=constant`, the collapse is exact at every scale:

\[
\boxed{
\mathcal J_t\!\left[-\frac{a}{\,\cdot-x\,}+c\right](x+r\zeta)-\beta
=\sigma\frac{a}{r}.
}
\tag{8}
\]

Thus the focal pole mass `a` and the gap scale `r` survive only through a removable real scalar. Every nonconstant local Julia tangent requires the complement `h` to contribute at the same derivative scale as the focal pole:

\[
\limsup_j\kappa_j>0.
\tag{9}
\]

For the reflected Mangoldt source of `WP-304`, this ratio is itself an exact positive multipole observable. At the focal prime-power atom `x_n=-\log n`, with

\[
a_n=\frac{\Lambda(n)}{n+1},
\tag{10}
\]

remove that atom and choose `t_n=x_n+sigma r_n`. Then

\[
\boxed{
\kappa_n
=
\sum_{m=q^k\ne n}
\frac{a_m}{a_n}
\left(\frac{r_n}{x_m-t_n}\right)^2.
}
\tag{11}
\]

There is no cancellation in (11). Therefore a nontrivial scalar support-side Julia tangent is **necessarily collective**: other prime-power atoms must retain order-one positive influence on the boundary derivative before the Julia sign theorem is applied. A one-pole gap-adapted completion cannot be the missing finite–archimedean Weil geometry.

This does not rule out a genuinely multipole or cluster-normalized scalar construction, and it does not address matrix/operator-valued reductions. It does close the isolated-pole escape left by `WP-315` without assuming any further theorem on prime-gap statistics.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SUPPORT-SIDE-JULIA + ISOLATED-POLE-TRIVIALIZATION + PURE-POLE-MATCHED-CONTROL + POSITIVE-MULTIPOLE-COLLECTIVITY-INDEX + PICK/HERGLOTZ-POSITIVITY + NO-PRIME-GAP-ASSUMPTION + NOT-WEIL-POSITIVITY`.

## 1. Exact local normal form

Write the local observation coordinate as

\[
z=x+r\zeta,
\qquad t=x+\sigma r.
\tag{12}
\]

The focal pole increment is

\[
-\frac{a}{z-x}+\frac{a}{t-x}
=
\frac{a}{r}
\left(\sigma-\frac1\zeta\right).
\tag{13}
\]

Normalize the background increment by the same pole amplitude,

\[
b_r(\zeta)
:=
\frac{r}{a}
\bigl(h(x+r\zeta)-h(t)\bigr),
\tag{14}
\]

and set

\[
s_r:=\frac{r^2}{a}h'(t)=\kappa.
\tag{15}
\]

Then

\[
f(x+r\zeta)-f(t)
=
\frac{a}{r}
\left(
\sigma-\frac1\zeta+b_r(\zeta)
\right),
\tag{16}
\]

while

\[
d(z-t)
=
\frac{a}{r}(1+s_r)(\zeta-\sigma).
\tag{17}
\]

Substitution into (4) gives the exact identity

\[
\boxed{
\frac{r}{a}
\bigl(\mathcal J_t[f](x+r\zeta)-\beta\bigr)
=
\frac{(1+s_r)(\zeta-\sigma)
\left(\sigma-\zeta^{-1}+b_r(\zeta)\right)}
{(1+s_r)(\zeta-\sigma)
-\left(\sigma-\zeta^{-1}+b_r(\zeta)\right)}.
}
\tag{18}
\]

For a pure pole, `b_r=0` and `s_r=0`. Since

\[
\sigma-\frac1\zeta
=\sigma\frac{\zeta-\sigma}{\zeta},
\tag{19}
\]

both numerator and denominator in (18) contain the same quadratic factor, and their quotient is exactly `sigma`. This proves (8).

This is not a loss of Pick positivity. Formula (4) is the classical Julia–Nevanlinna reduction followed by the uniquely normalized inversion already analyzed in `WP-312`; the transformed function remains in the Pick class. The failure is more specific: the one-pole positive geometry becomes a scalar boundary normalization rather than a nonconstant positive response.

## 2. Positivity makes the derivative ratio control the whole local background

Condition (6) is stronger than a statement about one derivative only. For a positive Herglotz background it forces the full normalized background increment (14) to vanish on every upper-half-plane compact set.

Use the standard Herglotz representation

\[
h(z)=c+\alpha z
+\int_{\mathbb R}
\left(
\frac1{\lambda-z}-\frac{\lambda}{1+\lambda^2}
\right)d\nu(\lambda),
\qquad \alpha\ge0,
\quad \nu\ge0.
\tag{20}
\]

At a regular real point `t`,

\[
h'(t)
=
\alpha+
\int_{\mathbb R}\frac{d\nu(\lambda)}{(\lambda-t)^2}.
\tag{21}
\]

For `z=t+r q`, subtracting the boundary value gives

\[
\frac{h(z)-h(t)}{z-t}
=
\alpha+
\int_{\mathbb R}
\frac{\lambda-t}{\lambda-z}
\frac{d\nu(\lambda)}{(\lambda-t)^2}.
\tag{22}
\]

If `q` ranges over a compact subset of the upper half-plane, then for real `u`

\[
\left|\frac{u}{u-q}\right|
=\left|1+\frac{q}{u-q}\right|
\le
1+\frac{|q|}{\operatorname{Im}q},
\tag{23}
\]

so (21)-(22) imply

\[
|h(t+r q)-h(t)|
\le
C_K\,r|q|\,h'(t)
\tag{24}
\]

uniformly on that compact set. In the coordinates (12), `q=zeta-sigma`; therefore

\[
\boxed{
|b_r(\zeta)|
\le
C_K|\zeta-\sigma|\,s_r.
}
\tag{25}
\]

Hence `s_r->0` implies `b_r->0` locally uniformly in `H`. Taking the limit in (18) proves (7).

The key point is positivity: no signed cancellation is used to make the background small. The single number `kappa` is exactly the ratio between the positive derivative supplied by all other channels and the positive derivative supplied by the focal pole. If that ratio vanishes, the complete local background increment vanishes at the same normalized scale.

## 3. The Mangoldt source turns `kappa` into an exact collectivity index

For the reflected source

\[
m(z)=
\sum_{m=q^k}
a_m
\left(
-\frac1{\log m+z}
+\frac{\log m}{1+(\log m)^2}
\right),
\qquad
a_m=\frac{\Lambda(m)}{m+1},
\tag{26}
\]

put `x_m=-log m`. Fix a focal atom `n` and absorb its real regularizing constant into the background. Then

\[
m(z)=-\frac{a_n}{z-x_n}+h_n(z),
\tag{27}
\]

where `h_n` is again Herglotz with the focal positive atom removed. At every regular node `t_n`, termwise differentiation gives

\[
h_n'(t_n)
=
\sum_{m\ne n}\frac{a_m}{(x_m-t_n)^2}.
\tag{28}
\]

The sum converges at each support-free real node exactly as in `WP-312`. Multiplying (28) by `r_n^2/a_n` gives (11).

The focal derivative is

\[
\frac{a_n}{r_n^2},
\tag{29}
\]

so the total boundary slope is

\[
d_n
=
\frac{a_n}{r_n^2}(1+\kappa_n).
\tag{30}
\]

Thus `kappa_n` has a direct geometric meaning independent of the target Weil sign:

- `kappa_n->0` is the asymptotically isolated one-pole regime, and (7) says its normalized Julia tangent is a removable real constant;
- `limsup kappa_n>0` means the background contributes an order-one fraction of the boundary slope, so any nonconstant tangent already depends on a positive collective of other prime-power poles.

No prime-gap conjecture enters this dichotomy. Prime spacing only determines which of the two regimes a chosen moving node occupies.

## 4. Relation to WP-315 and the remaining scalar route

`WP-315` and the present result close complementary interpretations of a support-side scalar Julia completion.

At the intrinsic single-atom mass scale `r~a_n`, bounded Maynard clusters make the local source nonprecompact: arbitrarily many comparable prime atoms can collapse into one chart. Calling that chart a one-pole geometry is therefore false on unavoidable subsequences.

Suppose instead that one adapts `r_n` to a source gap or selects a subsequence precisely so that the focal pole becomes dominant. The present theorem then applies. Once `kappa_n->0`, classical Julia reduction turns the entire focal pole into the removable constant `sigma a_n/r_n`; the local nonconstant profile disappears.

Consequently the scalar route now has a sharp structural fork:

\[
\boxed{
\text{one-pole dominated}
\Longrightarrow
\text{Julia tangent is constant},
\qquad
\text{nonconstant Julia tangent}
\Longrightarrow
\text{order-one multipole background}.
}
\tag{31}
\]

The second alternative remains open, but it is no longer an isolated prime-power construction. It must derive a canonical **collective** normalization or coupling of several source atoms before applying the classical Pick positivity theorem, and that collective object must still produce the archimedean/Gamma and polar terms with the correct orientation.

This is materially narrower than merely saying that gap-adapted scaling fluctuates. It identifies what classical scalar Julia reduction itself does to an isolated arithmetic atom, independently of how the gap was selected.

## 5. Aggressive falsification and exact scope

The theorem does **not** claim that every support-side moving node has `kappa->0`. `WP-315` already gives important subsequences where nearby atoms make such a hypothesis implausible, and a deliberate cluster-scale construction may keep `kappa` finite or large.

It also does not claim that a nonzero `kappa` automatically produces a useful arithmetic tangent. A synthetic positive multipole Herglotz measure can generate the same local normal form (18). Any surviving profile must therefore be tested against matched non-arithmetic controls and must show that its collective source law is canonically forced by Mathia rather than chosen after inspecting prime locations.

The arbitrary real translation `beta` cannot rescue the isolated regime. It can remove or shift the constant in (7), but it cannot create `zeta`-dependence. Conversely, introducing a second scale that amplifies the vanishing `O(kappa)` remainder would be a new renormalization not supplied by classical Julia reduction; its scale and positivity would require an independent derivation.

Reducing exactly at the pole does not reopen the route. The classical pole version of Julia–Nevanlinna reduction used in `WP-312` simply subtracts the focal term `-a/(z-x)` and leaves `h`. Thus both ways of approaching an isolated atom agree structurally: the pole itself is removed rather than converted into a nontrivial positive local geometry.

Finally, nothing here rules out matrix/operator-valued Julia reduction, a nonseparable finite–archimedean coupling, or a genuinely collective scalar cluster construction. Those are now the relevant category changes. The result only says that **no asymptotically isolated Mangoldt pole can carry the missing Weil positivity through the classical scalar Julia mechanism.**

## 6. Prior-art and novelty audit

Julia–Nevanlinna reduction, its Pick-class preservation, and its interpretation as Schur complementation are classical and are not claimed as new. Herglotz representation and the positive derivative formula (21) are classical as well.

The new content for this line is the exact moving-pole normalization (18), the pure-pole matched control (8), and the positive collectivity index (11) for Mathia's fixed reflected Mangoldt source. Together they show that the previously open gap-adapted **isolated-pole** escape is structurally vacuous: the scalar Julia theorem consumes the focal atom as interpolation data, and a nonconstant tangent can survive only through the other source atoms at comparable derivative strength.

A bounded literature search around boundary Julia–Nevanlinna reduction, Herglotz point masses, and simple-pole interpolation found the classical reduction/augmentation machinery but no theorem stated in terms of this Mangoldt moving-pole collectivity dichotomy. The result should therefore be read as an exact Mathia-specific corollary of classical theory, not as a new theorem about Pick functions in isolation.

## Consequence for the research line

The scalar support-side frontier is now more precise. `WP-314` eliminates the empty-side moving node by universality. `WP-315` eliminates the interpretation of the atom-mass chart as a uniform isolated-pole geometry. `WP-316` eliminates **every** moving regular-node chart that actually becomes one-pole dominated.

What remains scalar is necessarily collective: a source-forced cluster/multipole normalization in which the positive background contributes at order one before Julia reduction. Otherwise the search should move to matrix/operator-valued boundary geometry or to a nonseparable finite–archimedean construction with its own independent sign theorem. None of these surviving routes yet supplies global Weil positivity.