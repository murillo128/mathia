# WI-228 — global fixed-slope zero density cannot close the radial-source branch

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + BOOTSTRAP-INTERFACE + PRIOR-ART-REDIRECT`.

WI-227 reduces shallow screening of a Maynard--Pratt bow to a depth--localization dichotomy. At a fixed reciprocal harmonic `0<k<d`, either the screen carries order-`M` radial-weighted source beyond a threshold `a>A`,

\[
\sum_{a_\rho>A}\mu_\rho\cosh(k a_\rho)\gg M,
\tag{1}
\]

or order-`M` shallow source is forced into physical ordinate radius

\[
O\!\left((A+1)\frac{M}{\log T}\right).
\tag{2}
\]

A natural next attempt is to kill (1) with known zero-density estimates. The exact tail calculation below shows that this cannot work with a **global** zero-count bound having any fixed exponential slope on the normalized horizontal scale. The obstruction is not the exponential slope: Jutila's published near-line exponent is already steeper than the first reciprocal-harmonic radial weight. The obstruction is the global prefactor `N_T\asymp T\log T`, which is polynomially larger than a bow population `M=T^{\vartheta+o(1)}` with fixed `\vartheta<1`.

The same calculation identifies the theorem interface that would genuinely close the deep branch. In normalized horizontal depth

\[
Y=d a,
\qquad
\alpha:=\frac{k}{d}\in(0,1),
\tag{3}
\]

a source-relevant **local** tail of the form

\[
C_{\rm loc}(Y)\ll M e^{-\kappa Y}
\tag{4}
\]

with

\[
\boxed{\kappa>\alpha=\frac{k}{d}}
\tag{5}
\]

would make the radial-weighted tail `o(M)` after choosing a sufficiently large **fixed** depth cutoff. Then WI-227 would force the shallow alternative at physical scale `O(M/log T)`. The exponent condition (5) is sharp for this count-only exponential-tail interface: if `\kappa\le\alpha`, a tail satisfying (4) can still place order-`M` weighted source at arbitrarily large normalized depth.

Thus the live requirement has two independent parts: **bow-scale normalization** of the zero/source reservoir and **decay slope larger than the harmonic weight**. Current published inputs located in the line supply these separately but not together.

## 1. Exact count-tail to radial-weight conversion

Let a multiset of screen labels have normalized horizontal depths `Y_j>=0` and multiplicities absorbed into repetition. Define its tail count

\[
C(Y):=\#\{j:Y_j>Y\}
\tag{6}
\]

and, for a fixed `0<\alpha<1`, its weighted tail

\[
W(A):=\sum_{Y_j>A}\cosh(\alpha Y_j).
\tag{7}
\]

Suppose on the relevant reservoir that for every `Y>=A`,

\[
C(Y)\le P e^{-\kappa Y}
\tag{8}
\]

with `\kappa>\alpha`. Since `\cosh(\alpha Y)\le e^{\alpha Y}`, Stieltjes partial summation / layer cake gives

\[
\begin{aligned}
W(A)
&\le \sum_{Y_j>A}e^{\alpha Y_j}\\
&=e^{\alpha A}C(A)
+\int_A^\infty \alpha e^{\alpha y}C(y)\,dy\\
&\le
P e^{-(\kappa-\alpha)A}
+\alpha P\int_A^\infty e^{-(\kappa-\alpha)y}\,dy.
\end{aligned}
\tag{9}
\]

Therefore

\[
\boxed{
W(A)
\le
\frac{\kappa}{\kappa-\alpha}
P e^{-(\kappa-\alpha)A}.
}
\tag{10}
\]

This is an elementary identity/inequality, not a new zero-density theorem.

The slope threshold is exact for this interface. If `\kappa\le\alpha`, choose a large depth `Y_*` and place

\[
q=\left\lfloor cM e^{-\alpha Y_*}\right\rfloor
\tag{11}
\]

labels there, with `c>0` fixed and `Y_*` chosen so `q>=1`. Then

\[
q\cosh(\alpha Y_*)\asymp M,
\tag{12}
\]

while

\[
q\ll M e^{-\alpha Y_*}\le M e^{-\kappa Y_*}.
\tag{13}
\]

The resulting tail obeys an `M e^{-\kappa Y}` envelope up to a fixed constant but still carries order-`M` weighted mass at depth `Y_*`. Consequently a local exponential count tail can force the WI-227 deep mass to vanish at fixed cutoff only when its decay exponent beats the radial weight exponent.

## 2. A bow-normalized local tail with slope `>k/d` would close the deep alternative

Return to the WI-227 screen normalization and let

\[
M=T^{\vartheta+o(1)},
\qquad
Y_\rho=d a_\rho,
\qquad
\alpha=\frac{k}{d}.
\tag{14}
\]

Assume a future theorem controls **the same source-relevant screen reservoir** entering WI-227, not merely an unrelated global zero set, by

\[
C_{\rm loc}(Y)\le C M e^{-\kappa Y}
\qquad(Y\ge0)
\tag{15}
\]

for fixed `C` and `\kappa>\alpha`. Equation (10) gives

\[
\sum_{Y_\rho>A_Y}
\mu_\rho\cosh(\alpha Y_\rho)
\le
C\frac{\kappa}{\kappa-\alpha}
M e^{-(\kappa-\alpha)A_Y}.
\tag{16}
\]

Choose `A_Y` sufficiently large but **fixed** so that the right side is smaller than the fixed order-`M` constant required by WI-227's deep alternative. With

\[
A=\frac{A_Y}{d}=O(1),
\tag{17}
\]

alternative (1) is impossible and WI-227 forces order-`M` shallow source into

\[
\boxed{O(M/\log T)}
\tag{18}
\]

physical ordinate radius. Because the surviving radial depth is bounded, each label has bounded `\cosh(k a)`, so the weighted lower bound converts to `\Omega(M)` raw screen labels in that same local region.

This does not by itself prove a contradiction with Riemann--von Mangoldt: the bow plus screen must still be compared against the exact local label/multiplicity budget, and the inherited dyadic-screen model is still not the complete source-fixed explicit formula. But it is a genuine bootstrap interface: (15) with (5) eliminates the deep escape in WI-227 without requiring a growing detector cutoff.

## 3. A global fixed-slope tail necessarily pays a logarithmic-depth cutoff

Now replace the local prefactor `M` by a global zero-count prefactor

\[
P=N_T\asymp T\log T.
\tag{19}
\]

Even grant the optimistic uniform envelope

\[
C_{\rm glob}(Y)\le C N_T e^{-\kappa Y}
\tag{20}
\]

for all relevant `Y`, with any fixed `\kappa>\alpha`. This is stronger than what is needed for the obstruction; it gives the global density route every benefit of the doubt. Equation (10) becomes

\[
W_{\rm glob}(A_Y)
\ll
N_T e^{-(\kappa-\alpha)A_Y}.
\tag{21}
\]

To make this `o(M)` when `M=T^{\vartheta+o(1)}`, fixed `0<\vartheta<1`, one needs

\[
\frac{N_T}{M}
 e^{-(\kappa-\alpha)A_Y}=o(1).
\tag{22}
\]

Since

\[
\frac{N_T}{M}=T^{1-\vartheta+o(1)},
\tag{23}
\]

(22) forces

\[
\boxed{
A_Y
\ge
\left(\frac{1-\vartheta}{\kappa-\alpha}+o(1)\right)\log T.
}
\tag{24}
\]

In particular **no cutoff `A_Y=o(log T)` can close the deep branch through a global tail with fixed exponential slope**, no matter how favorable that fixed slope is.

This is not merely weakness of the upper-bound calculation. The theorem class is logically compatible with an order-`M` deep source at every sublogarithmic threshold. For `A_Y=o(log T)`, put

\[
q_T=\left\lfloor cM e^{-\alpha(A_Y+1)}\right\rfloor
\tag{25}
\]

labels at depth `A_Y+1`. Their radial weight is `\asymp M`. On the other hand,

\[
\frac{q_T}{N_T e^{-\kappa(A_Y+1)}}
\ll
T^{\vartheta-1+o(1)}
 e^{(\kappa-\alpha)A_Y}
=
T^{-(1-\vartheta)+o(1)}
\longrightarrow0.
\tag{26}
\]

Thus this adversarial tail obeys (20) with room to spare while retaining the WI-227 deep alternative. A count theorem with global prefactor and fixed microscopic slope therefore cannot, as a black box, rule out the source configuration that matters.

Finally, substituting (24) into WI-227's shallow localization radius gives

\[
O\!\left(\frac{A_Y M}{\log T}\right)=O(M),
\tag{27}
\]

not `o(M)` and certainly not the fixed-depth bow scale `O(M/log T)`. Hence conventional global zero density does not improve the localization order already known from WI-224--WI-225 when routed only through the deep radial-source ledger.

## 4. Published near-line inputs miss opposite halves of the interface

The literature already audited in this line makes the separation explicit.

### Global Jutila: adequate slope, wrong prefactor

WI-029 records Jutila's published near-line estimate

\[
N(\sigma,T)
\ll_\varepsilon
T^{1-(1-\varepsilon)(\sigma-1/2)}\log T.
\tag{28}
\]

On `Y=(\sigma-1/2)\log T`, this has microscopic exponential slope arbitrarily close to `1`. For every fixed interior reciprocal harmonic `k<d`, choose `\varepsilon` so that

\[
1-\varepsilon>\frac{k}{d}.
\tag{29}
\]

Thus Jutila is already on the **correct side of the slope threshold** (5). But its natural prefactor is the global `T\log T` zero population. WI-029 only needs and records fixed-depth exponential tightness; no unproved growing-depth uniformity is imported here. The stronger hypothetical envelope (20) shows that even granting such uniformity would still force a cutoff of order `log T` before the weighted tail reaches bow scale.

This explains why WI-029 and WI-227 are compatible rather than contradictory: global zero density can make very deep zeros rare relative to all zeros while still allowing more than enough of them to carry an `M=T^\vartheta` radial source.

### Local Karatsuba--Korolev: bow-scale prefactor, insufficient/live-range-missing slope

WI-199 extracts from the published Karatsuba--Korolev short-rectangle theorem, in its valid long-bow range, a local normalized-depth tail of schematic form

\[
C_{\rm KK}(Y)
\ll M e^{-(\eta/5)Y},
\qquad
0<\eta<10^{-3}.
\tag{30}
\]

This has the desired bow-scale prefactor `M`, but its normalized slope is only

\[
\kappa_{\rm KK}=\eta/5<2\times10^{-4}.
\tag{31}
\]

For example, in the concrete `2<d<3`, `k=1` regime used by the finite-harmonic screen constructions, the needed slope is

\[
\alpha=1/d>1/3,
\tag{32}
\]

so (31) is far below the exact threshold (5). More fundamentally for the current bow frontier, WI-199's normalized-depth tail starts only above `\vartheta>27/82`, whereas WI-202 lowers the remaining source-safe count-saturating bow range to

\[
0<\vartheta\le\frac{3943}{12011}
<\frac{27}{82}.
\tag{33}
\]

The currently established local tail therefore does not even overlap the live fixed-power range that still needs exclusion.

The generic Khayrulloev--Rakhmonov exponent-pair machinery used in WI-202 improves every-interval count/fixed-physical-depth exclusions, but WI-202 explicitly does **not** extend WI-199's normalized-depth screening tail below `27/82`. No current local theorem in the audited line supplies both (15) and (5) on the surviving bow range.

## 5. Relation to earlier barriers and novelty audit

The tail integration itself is classical partial summation. No novelty is claimed for Jutila's density theorem, Karatsuba--Korolev's local rectangle theorem, the Khayrulloev--Rakhmonov exponent-pair threshold, or any general principle that exponential moments require a tail exponent larger than their weight.

The closest existing Mathia results address different interfaces:

- WI-116 identifies a slope-`2` requirement for the **Tsang bad-pair kernel**, whose weight is `e^{2Y}` after a different symmetry reduction. It does not analyze WI-227's radial source weight `cosh((k/d)Y)` or the local-versus-global prefactor needed to close that dichotomy.
- WI-225 proves that a scalar fixed-support detector paid by **global total mass** needs a natural-frequency cutoff `Theta(log T)`. WI-227 then bypasses that stopband argument by shellwise local counting but leaves a deep radial-source branch. The present calculation shows that feeding ordinary global zero density into that new branch simply recreates a logarithmic-depth loss for a different reason: the polynomial ratio `N_T/M`.
- WI-029 shows positive-density off-line mass has a bounded-depth core, but its target scale is `N_T`, not a mesoscopic bow population `M`. The present obstruction is precisely the scale mismatch between those two populations.

A bounded prior-art audit around near-critical-line zero density, weighted zero-density/partial-summation arguments, short-interval zero-density, and recent large-value improvements found no established theorem matching the local bow-normalized weighted interface (15)--(16) in the surviving range. This absence is not used as a priority claim. Recent stronger **global** zero-density theorems farther into the critical strip do not alter the structural conclusion (24): any bound entering only as `T^{1+o(1)}` times a fixed exponential in microscopic depth still carries the same polynomial prefactor obstruction near the line.

The durable Mathia contribution is therefore the exact interface theorem: to use zero counts to eliminate WI-227's deep radial source at fixed cutoff, one needs simultaneously a source-relevant local prefactor of order `M` and normalized depth slope `\kappa>k/d`; a global fixed-slope density theorem cannot substitute for the local normalization.

## 6. Boundary conditions and failure modes

The claim is deliberately restricted.

First, it is a no-go for **count-only exponential-tail insertion into WI-227**. A direct weighted source estimate can beat the barrier without first proving a count tail, because it may exploit phases, the signed explicit formula, correlations, or arithmetic restrictions on which zeros can actually screen the distinguished bow source.

Second, a global theorem with depth suppression substantially stronger than every fixed exponential, or with an additional polynomial saving depending on the bow location/source, is outside the theorem class closed by (24). Likewise, a local theorem with prefactor `o(M)` can require less slope.

Third, the local tail in (15) must govern the actual source-relevant screen labels, with multiplicity and the same radial coordinate as WI-227. A theorem about all zeros in a geometrically different box is not automatically such a statement.

Fourth, eliminating the deep branch only forces `Omega(M)` shallow local screen labels; it does not by itself prove that the local zeta zero budget is exceeded. Multiple critical-line zeros, off-line mirror pairs, bow labels, and proof slack remain separate populations exactly as required by the line mandate.

Finally, WI-227 itself is conditional on the inherited dyadic-screen model for the complementary source. Non-dyadic zeros, `Lambda^sharp`, pole/trivial terms, and contour remainders remain outside that model until the source-fixed explicit formula is controlled.

## Research consequence

The proposed next step “use stronger global zero density to make the WI-227 deep branch impossible” is closed for every conventional fixed-microscopic-slope theorem: the global `N_T/M` scale gap forces a radial cutoff `Theta(log T)` and gives at best `O(M)` localization.

The useful target is now much sharper. A zero-density route must prove, in the actual source-relevant local reservoir,

\[
\boxed{
C_{\rm loc}(Y)\ll M e^{-\kappa Y}
\quad\text{with}\quad
\kappa>\frac{k}{d},
}
\tag{34}
\]

or replace count control by a direct weighted/covariant estimate strong enough to imply the same suppression. If such an estimate were available at the first reciprocal harmonic, WI-227 would convert it into an `Omega(M)` shallow screen population at bow-scale vertical radius, where a genuine local zero-budget contradiction could then be attempted. Current published global and local density inputs do not supply this combined interface.