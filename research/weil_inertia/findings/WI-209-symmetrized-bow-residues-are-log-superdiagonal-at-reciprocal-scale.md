# WI-209 — symmetrized bow residues are logarithmically superdiagonal at reciprocal scale

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY`.

The bounded-packet obstruction in WI-205 leaves one important escape hatch open: a Maynard--Pratt bow is not a bounded packet.  It contains a mesoscopic family of off-critical labels, and the functional equation supplies a mirror at the same ordinate for every right-half-plane label.  At the reciprocal Montgomery scale identified in WI-184, those mirror-pair residues are automatically phase coherent.

That coherence is strong enough to cross the Gallagher diagonal by a logarithmic factor.  More precisely, for an arithmetic symmetrized bow of length `m` with a positive-density off-critical subset `J`, choose the reciprocal source exponent `alpha_T=2*pi/c_T` and `X=T^{alpha_T}`.  On a physical translation slab of width

\[
\ell=\eta\,\frac{X\log T}{m},
\]

which is a fixed constant multiple of the bow-scale window in WI-195, the selected mirror-pair residue contribution has

\[
\int_X^{X+\ell}|R_J(x,\ell)|^2\,dx
\gg |J|^2\frac{\ell^3}{X}.
\]

If `|J|/m -> kappa>0`, comparison with the natural raw-prime diagonal `X ell log X` gives an **Omega(log T)** excess.  Thus a positive-density arithmetic bow cannot hide because its own explicit-formula residue is too small.  It can survive only if the *complementary source contribution* -- all other zeros together with the pole/trivial terms, contour remainder, and the `Lambda^sharp` subtraction -- cancels this coherent residue at the same logarithmically superdiagonal scale.

This does **not** exclude the bow unconditionally and does not resolve the accepted distinguished-twist clue: the missing theorem remains a pointwise source-fixed statement about that complementary cancellation.  What changes is the burden of proof.  WI-205 showed that a bounded isolated packet is subdiagonal; the present calculation shows that the mesoscopic bow packet itself is superdiagonal by `log T`, so any diagonal-scale source theorem would force an asymptotically near-opposite complementary vector on a concrete reciprocal translation slab.

No unconditional zeta-zero proportion changes here.

## 1. Setup and provenance

Use the Maynard--Pratt arithmetic-bow geometry already audited in WI-183--WI-184.  Put

\[
L=\log T,
\qquad
\gamma_j=\gamma_0+\frac{c_T j}{L},
\]

for consecutive integer labels `j` in a set of cardinality `m`, and assume `c_T` stays in a fixed compact subinterval

\[
0<c_-\le c_T\le c_+<\infty.
\]

The Maynard--Pratt model has fixed `c` and `m=T^epsilon` (up to harmless integer conventions), so in particular

\[
\frac{m}{L}\longrightarrow\infty.
\tag{1}
\]

Let `J` be any selected set of right-half-plane off-critical labels, with

\[
\rho_j=\beta_j+i\gamma_j,
\qquad \beta_j>\frac12,
\qquad j\in J.
\]

The functional equation forces the companion zero

\[
1-\overline{\rho_j}=(1-\beta_j)+i\gamma_j
\tag{2}
\]

at the same ordinate and with the same multiplicity.  This is exactly the symmetrization used in WI-184.  No assumption is made that `J` contains every bow label; later only its relative cardinality matters.

Choose a grid label `j_0`, set

\[
U=\gamma_{j_0},
\qquad
\alpha_T=\frac{2\pi}{c_T},
\qquad
X=T^{\alpha_T}.
\tag{3}
\]

For a source-compatible long symmetrized bow, WI-184 gives `c_T >= 4*pi-o(1)` and hence `alpha_T <= 1/2+o(1)`.  The calculation below does not need count saturation and keeps the exact rate-free value `alpha_T=2*pi/c_T`.

The explicit-formula residue identity needed below is the classical one already isolated in WI-205.  For the twisted short von-Mangoldt sum with twist `n^{-iU}`, a zero `rho` contributes

\[
-\frac{(x+\ell)^{\rho-iU}-x^{\rho-iU}}{\rho-iU}
=-\int_x^{x+\ell}y^{\rho-iU-1}\,dy.
\tag{4}
\]

Thus no new external source is needed beyond the Maynard--Pratt geometry and the classical explicit formula already anchored in `SOURCES.md`.

## 2. Reciprocal phase locking persists on a physical slab

For `delta_j=gamma_j-U`, (3) gives the exact reciprocal identity

\[
\delta_j\log X
=
\frac{c_T(j-j_0)}{L}\,\frac{2\pi}{c_T}L
=2\pi(j-j_0).
\tag{5}
\]

Fix `eta>0` sufficiently small that

\[
\theta_0:=2c_+\eta<\frac\pi2
\tag{6}
\]

(for instance `2c_+ eta <= pi/6`), and define

\[
\ell:=\eta\frac{XL}{m}.
\tag{7}
\]

By (1), `ell/X -> 0`.  For every `x in [X,X+ell]`, every `y in [x,x+ell]`, and every bow label with `|j-j_0|<=m`,

\[
\begin{aligned}
|\delta_j\log(y/X)|
&\le \frac{c_+m}{L}\log\!\left(1+\frac{2\ell}{X}\right)\\
&\le \frac{c_+m}{L}\frac{2\ell}{X}
=2c_+\eta
=\theta_0.
\end{aligned}
\tag{8}
\]

Combining (5) and (8), every selected residue phase `exp(i delta_j log y)` lies in the same fixed cone about the positive real axis throughout the entire two-parameter slab

\[
X\le x\le X+\ell,
\qquad
x\le y\le x+\ell.
\tag{9}
\]

This is stronger than coherence at the single reciprocal Fourier point: it survives the full bow-scale physical window used by the Gallagher bridge.

The same argument is stable under near-arithmetic spacing.  If instead one only knows

\[
\sup_{j\in J}\operatorname{dist}\!\left((\gamma_j-U)\log X,2\pi\mathbb Z\right)\le\theta_1
\tag{10}
\]

and the drift estimate in (8) is at most `theta_2`, then everything below remains valid with `cos(theta_0)` replaced by `cos(theta_1+theta_2)`, provided `theta_1+theta_2<pi/2`.  No such perturbative hypothesis is needed for the exact arithmetic model.

## 3. Functional-equation pairs give a depth-independent positive amplitude

For one selected right-half-plane zero and its mirror (2), the two integrands in (4) have the same phase.  Their sum, after removing the common minus sign, is

\[
\left(y^{\beta_j-1}+y^{-\beta_j}\right)e^{i\delta_j\log y}.
\tag{11}
\]

Writing `a=beta_j-1/2>0`, the amplitude is

\[
y^{\beta_j-1}+y^{-\beta_j}
=y^{-1/2}\left(y^a+y^{-a}\right)
\ge 2y^{-1/2}
\tag{12}
\]

by AM--GM.  The inequality is uniform in the horizontal depth `a`: pushing a zero farther from the critical line can only increase the pair amplitude.

Let `M=|J|`, counting multiplicity if desired, and let `R_J(x,ell)` denote the sum of the selected mirror-pair residues.  Rotate away the common sign.  Equations (8), (11), and (12) imply pointwise for every `x in [X,X+ell]`

\[
\begin{aligned}
|R_J(x,\ell)|
&\ge \Re R_J(x,\ell)\\
&\ge 2\cos\theta_0\sum_{j\in J}
\int_x^{x+\ell}y^{-1/2}\,dy\\
&\ge
\frac{2\cos\theta_0\,M\ell}{(X+2\ell)^{1/2}}.
\end{aligned}
\tag{13}
\]

Consequently the selected residue energy on the same translation slab satisfies the exact lower bound

\[
\boxed{
\int_X^{X+\ell}|R_J(x,\ell)|^2\,dx
\ge
\frac{4\cos^2\theta_0\,M^2\ell^3}{X+2\ell}.
}
\tag{14}
\]

Nothing arithmetic beyond the bow spacing and functional-equation symmetry enters (14).

## 4. A positive-density bow is logarithmically superdiagonal

WI-195 identifies the raw-prime Gallagher diagonal at physical length `ell` as

\[
D_\ell:=X\ell\log X.
\tag{15}
\]

Divide (14) by (15), use `ell=eta XL/m` and `log X=alpha_T L`, and obtain

\[
\frac{\int_X^{X+\ell}|R_J(x,\ell)|^2dx}{D_\ell}
\ge
\frac{4\eta^2\cos^2\theta_0}{\alpha_T}
\left(\frac{M}{m}\right)^2
\frac{L}{1+2\eta L/m}.
\tag{16}
\]

Hence, along any sequence for which

\[
\frac{M}{m}\ge\kappa>0,
\tag{17}
\]

we have

\[
\boxed{
\frac{\int_X^{X+\ell}|R_J(x,\ell)|^2dx}{X\ell\log X}
\ge
\left(\frac{4\eta^2\cos^2\theta_0}{\alpha_T}\kappa^2+o(1)\right)\log T.
}
\tag{18}
\]

Because `c_T` lies in a fixed compact interval, so does `alpha_T`; the right side is `Omega(log T)`.  In Hilbert norm, the selected bow residue is therefore larger than diagonal scale by `Omega(sqrt(log T))`.

This is fully compatible with WI-205.  That finding showed that a packet of total multiplicity `M_F=O(1)` is subdiagonal and that diagonal scale requires a growing coherent population.  The Maynard--Pratt bow supplies exactly such a population: `M` is of order `m`, and (5)--(9) prove rather than assume the needed coherence.

## 5. The surviving bow must pay a quantitative complement-cancellation charge

The selected residue piece is not the full source-fixed error.  On the same slab write schematically

\[
E_{\rm src}(x)=R_J(x,\ell)+C(x),
\tag{19}
\]

where `C` contains every term not deliberately selected into `R_J`: all complementary nontrivial zeros, the pole and trivial-zero terms appropriate to the chosen explicit formula, contour/remainder terms, and crucially the `Lambda^sharp` subtraction required by WI-195.  Equation (14) by itself therefore does **not** give a lower bound for the full source norm.

It does, however, quantify exactly what any diagonal-scale source theorem would have to prove.  Suppose a future pointwise source argument yielded on this slab

\[
\|E_{\rm src}\|_2^2\le A D_\ell
\tag{20}
\]

with `A=O(1)`.  From (18), write `||R_J||_2^2 >= B_T L D_ell`, where `liminf B_T>0`.  Then the reverse triangle inequality forces

\[
\boxed{
\|C\|_2
\ge
\left(\sqrt{B_TL}-\sqrt A\right)D_\ell^{1/2}.
}
\tag{21}
\]

Even more rigidly, (19)--(20) say directly

\[
\|C+R_J\|_2\le\sqrt{A D_\ell},
\tag{22}
\]

while `||R_J||_2 >= sqrt(B_T L D_ell)`.  Thus relative to the selected bow vector, the complementary contribution must approximate `-R_J` to `O(L^{-1/2})` in `L^2` norm.  A surviving positive-density arithmetic bow is therefore not merely compatible with some unspecified cancellation: **it requires logarithmically superdiagonal, asymptotically near-opposite source cancellation on its distinguished reciprocal slab**.

Equation (21) is a conditional burden, not a source theorem.  At present WI-195/WI-196 and the accepted clue explicitly record that no available pointwise arithmetic estimate controls this distinguished signed covariance at the required scale.

## 6. Novelty audit and relation to the existing chain

The ingredients are deliberately separated by provenance.

- **Literature-backed geometry:** Maynard--Pratt's arithmetic bow and its slowly drifting off-critical labels are the external model already audited in WI-183.  Functional-equation symmetrization and the reciprocal exponent `alpha_T=2*pi/c_T` were extracted in WI-184.
- **Classical identity:** the twisted explicit-formula residue (4) is classical and was already persisted in WI-205.
- **Existing Mathia bridge:** the physical bow-scale window and diagonal `X ell log X` come from WI-195; WI-205 supplied the bounded-packet comparison and explicitly left growing coherent populations open.
- **New exact deduction here:** the uniform reciprocal cone on the whole physical translation slab, the mirror-pair lower bound (14), the `Omega(log T)` diagonal ratio (18), and the quantitative complement-cancellation charge (21)--(22).

A bounded prior-art audit around Maynard--Pratt bows, twisted von-Mangoldt short intervals, additive/multiplicative hybrid prime twists, and Gallagher-type variance did not locate a direct formulation of (14)--(22).  This absence is **not** used as a priority claim; the finding claims only the exact deduction from already sourced inputs.

The result is also distinct from the nearby findings.  WI-184 proves reciprocal coherence of the symmetrized bow at a Fourier point but leaves extraction from the complementary zero population open.  WI-188 identifies the self-dual twisted prime covariance generated by a count-saturating bow.  WI-195 identifies the exact multiplicative Gallagher `L^2` gate.  WI-205 proves bounded near-line residue packets are subdiagonal.  The present result closes precisely the bounded-packet escape hatch for a positive-density bow packet while preserving, rather than hiding, the complementary-cancellation problem.

## 7. Boundaries and falsifiers

This finding does **not** claim any of the following:

1. that every conceivable off-critical configuration contains an arithmetic Maynard--Pratt bow;
2. that the full `Lambda-Lambda^sharp` source norm is bounded above or below at diagonal scale on the distinguished slab;
3. that complementary zeros, `Lambda^sharp`, or other explicit-formula terms cannot cancel `R_J`;
4. that an approximate bow inherits (18) without quantitative reciprocal phase control such as (10);
5. that the accepted distinguished-twist clue is resolved.

The exact statement can be falsified only by an error in the residue formula, functional-equation pairing, reciprocal phase identity, cone estimate, or Gallagher-scale normalization.  A source-side cancellation theorem would not falsify it; instead such a theorem would have to realize the charge (21)--(22).

The next useful test is therefore narrower than before: **expand the complementary source term `C` on this exact reciprocal slab and determine whether its source-fixed arithmetic structure can carry an `Omega(sqrt(log T))` diagonal-normalized component aligned within `O(1/sqrt(log T))` of `-R_J`.**  Typical-twist averages, absolute-value estimates, and bounded-packet arguments cannot answer that question.