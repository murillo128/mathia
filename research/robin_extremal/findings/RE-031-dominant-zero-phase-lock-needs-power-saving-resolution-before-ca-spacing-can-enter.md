# RE-031 — dominant-zero phase lock needs power-saving resolution before CA spacing can enter

**Status:** `EXACT-DERIVED + CONDITIONAL-DOMINANT-ZERO + PHASE-RESOLUTION-BUDGET + SUPER-SQUARE-ROOT-CROSSING-OFFSET + NEGATIVE/OBSTRUCTION + PRIOR-ART-ALIGNED`. `RE-030` converts the `RE-029` threshold-selected opposite-sign prime-race cone, under an explicitly stated one-dominant-zero hypothesis, into a logarithmic phase lock near the reciprocal-positive zero-crossing branch of the standard Chebyshev mode. The shrinking phase offset is real, but by itself it is not yet an event-spacing constraint. Converting it back to the physical `Z` coordinate exposes a resolution loss that is stronger than the qualitative warning in `RE-030`.

Let

\[
\rho=\beta+i\gamma,\qquad \frac12<\beta<1,\qquad \gamma>0,
\]

and fix

\[
1-\beta<b<\frac12.
\]

Write

\[
a=\beta-\frac12,
\qquad d=\frac12-b,
\qquad \delta=a-d=\beta+b-1>0.
\tag{1}
\]

Along an actual threshold-selected sequence `Z` satisfying the dominant-zero hypotheses of `RE-030`, let `c_b>0` be the quantitative Robin constant and let

\[
A:=\frac{b c_b|\rho|}{2}.
\tag{2}
\]

If

\[
Z^{(0)}
=
\exp\!\left(
\frac{\alpha+3\pi/2+2\pi m}{\gamma}
\right),
\qquad \alpha=\arg\rho,
\tag{3}
\]

is the reciprocal-positive zero crossing selected by `RE-030`, then its phase law implies

\[
\boxed{
Z-Z^{(0)}
=
\left(\frac{b c_b|\rho|}{2\gamma}+o(1)\right)
Z^{\,2-\beta-b}\log Z.
}
\tag{4}
\]

This displacement is always super-square-root:

\[
\boxed{
\frac{Z-Z^{(0)}}{\sqrt Z}\to+\infty,
}
\tag{5}
\]

because

\[
2-\beta-b-\frac12
=
\frac32-\beta-b
=
\frac12-\delta>0.
\tag{6}
\]

Moreover, with the exact threshold defect `D(Z)=Z-\Phi(Z)` from `RE-027`,

\[
\boxed{
\frac{Z-Z^{(0)}}{D(Z)}
=
\left(\frac{|\rho|}{2\gamma}+o(1)\right)
Z^{1-\beta}
\to+\infty.
}
\tag{7}
\]

Thus the phrase "phase lock" must be interpreted in logarithmic phase, not as an additive near-collision between the CA-selected parameter and the spectral zero crossing. The selected point is relatively close to the crossing but additively much farther away than both `sqrt(Z)` and the already super-square-root CA defect.

The more important consequence is a **resolution budget**. Suppose the combined `RE-029` source asymptotic and the dominant-zero approximation determine the standard mode only to relative error `epsilon(Z)->0` at the threshold scale. Then the resulting phase uncertainty is of order

\[
Z^{-\delta}\log Z\,\epsilon(Z).
\tag{8}
\]

To use any CA/event-spacing input at additive scale `h(Z)=o(Z)`, that phase uncertainty has to be smaller than the phase change produced by moving `Z` through one such additive scale, namely `h(Z)/Z`. Therefore a spacing-based contradiction needs

\[
\boxed{
\epsilon(Z)
=o\!\left(
\frac{h(Z)}{Z^{\,1-\delta}\log Z}
\right).
}
\tag{9}
\]

In particular, to reach square-root additive resolution one needs the genuine power saving

\[
\boxed{
\epsilon(Z)
=o\!\left(
\frac{1}{Z^{\,1/2-\delta}\log Z}
\right),
\qquad
\frac12-\delta=\frac32-\beta-b>0.
}
\tag{10}
\]

No estimate of the form `epsilon(Z)=O((log Z)^(-N))` for a fixed `N` can meet (10). Hence **no finite logarithmic refinement of the current dominant-zero asymptotic can make local CA spacing coercive**. A future phase-lock exclusion based on event granularity needs a power-saving spectral/selector remainder at the appropriate scale, or it must use genuinely different global event information.

## 1. Physical displacement of the phase-locked point

`RE-030` gives, on the reciprocal-positive branch,

\[
\gamma\log Z-\alpha
=
\frac{3\pi}{2}+2\pi m
+
\left(A+o(1)\right)Z^{-\delta}\log Z.
\tag{11}
\]

Subtracting the defining equation (3) for `Z^(0)` gives

\[
\log\frac{Z}{Z^{(0)}}
=
\left(\frac{A}{\gamma}+o(1)\right)
Z^{-\delta}\log Z.
\tag{12}
\]

The right-hand side tends to zero because `delta>0`. Therefore

\[
1-\frac{Z^{(0)}}Z
=
1-
\exp\!\left(
-\log\frac{Z}{Z^{(0)}}
\right)
=
\left(\frac{A}{\gamma}+o(1)\right)
Z^{-\delta}\log Z,
\tag{13}
\]

which proves (4), since `1-delta=2-beta-b`. Equation (5) follows from (6).

This calculation distinguishes two notions that must not be conflated. The **phase offset** from the exact zero crossing is asymptotically fixed by (11). The **uncertainty** with which that offset is known depends on the remainder in the source/dominance approximation. A large physical offset does not itself provide a wide admissible window, and a shrinking logarithmic offset does not itself provide fine additive localization.

## 2. The crossing displacement is much larger than the CA defect

`RE-027` gives on the same threshold-selected states

\[
D(Z)
=
\left(bc_b+o(1)\right)
Z^{1-b}\log Z.
\tag{14}
\]

Dividing (4) by (14) gives

\[
\frac{Z-Z^{(0)}}{D(Z)}
=
\left(\frac{|\rho|}{2\gamma}+o(1)\right)
Z^{(2-\beta-b)-(1-b)},
\]

which is exactly (7). Notice that the exponent `1-beta` is independent of the threshold exponent `b`. Changing `b` therefore changes the phase accuracy and the CA defect together, but it cannot collapse the physical spectral crossing displacement down to the defect scale.

There is also a useful phase-amplitude reciprocity inside the pure-mode control. `RE-030` gives

\[
\frac{L_\rho(Z)}{-\Theta_\rho(Z)}
=
\left(
\frac{2\gamma}
{b c_b|\rho|\,|\rho-1|^2}
+o(1)
\right)
\frac{Z^\delta}{\log Z}.
\tag{15}
\]

Combining this with (13) yields

\[
\boxed{
\left(
\frac{L_\rho(Z)}{-\Theta_\rho(Z)}
\right)
\left(
\frac{Z-Z^{(0)}}Z
\right)
\longrightarrow
\frac1{|\rho-1|^2}.
}
\tag{16}
\]

The large reciprocal-mode surplus and the small *relative* crossing displacement are therefore two sides of the same coefficient geometry; they are not independent constraints that can be multiplied into a contradiction.

## 3. Quantitative phase uncertainty needed for an event-scale test

The dominant-zero statement in `RE-030` is deliberately formulated with little-`o` remainders. To expose what a spacing argument would actually require, write the combined threshold-scale standard-mode relation in the quantitative form

\[
\Theta_\rho(Z)
=
-bc_b Z^d\log Z\,(1+r(Z)),
\qquad |r(Z)|\le\epsilon(Z),
\qquad \epsilon(Z)\to0.
\tag{17}
\]

Near the branch (3), put

\[
t
:=
\gamma\log Z-\alpha-
\left(\frac{3\pi}{2}+2\pi m\right).
\tag{18}
\]

The exact trigonometric form from `RE-030` is

\[
\Theta_\rho(Z)
=-\frac{2Z^a}{|\rho|}\sin t.
\tag{19}
\]

Hence

\[
\sin t
=A Z^{-\delta}\log Z\,(1+r(Z)).
\tag{20}
\]

Define the nominal phase target without linearizing the sine,

\[
t_0(Z)
:=
\arcsin\!\left(A Z^{-\delta}\log Z\right).
\tag{21}
\]

Since its argument tends to zero, the derivative of `arcsin` is `1+o(1)`. Equations (20)--(21) therefore give

\[
\boxed{
|t-t_0(Z)|
=O\!\left(
Z^{-\delta}\log Z\,\epsilon(Z)
\right).
}
\tag{22}
\]

Now consider the phase residual

\[
F(Z)
:=
\gamma\log Z-\alpha-
\left(\frac{3\pi}{2}+2\pi m\right)
-t_0(Z).
\tag{23}
\]

Because `t_0(Z)=O(Z^(-delta) log Z)`, differentiation gives

\[
F'(Z)
=
\frac{\gamma+o(1)}Z.
\tag{24}
\]

Thus moving an additive distance `h=o(Z)` changes the residual by

\[
F(Z+h)-F(Z)
=
\left(\gamma+o(1)\right)\frac hZ.
\tag{25}
\]

For (22) to distinguish points or chambers at that additive scale, its right-hand side must be `o(h/Z)`. This is exactly (9).

For a power scale `h(Z)=Z^kappa` with `kappa<1-delta`, condition (9) becomes

\[
\epsilon(Z)
=o\!\left(
\frac1{Z^{\,1-\delta-\kappa}\log Z}
\right).
\tag{26}
\]

The square-root specialization `kappa=1/2` is (10). Since `delta<1/2` follows from `beta<1` and `b<1/2`, the exponent in (10) is always strictly positive. Any fixed inverse power of `log Z` is asymptotically too large.

## 4. What this rules out, and what it does not

This is a negative resolution theorem, not a contradiction to hypothetical RH failure. It does **not** show that threshold-selected CA states can realize the phase law, and it does not turn the one-zero source model into an admissible prime sequence. It also does not assume that CA event gaps themselves are square-root size. The square-root scale in (10) is only a clean diagnostic threshold because the physical phase displacement is forced to lie strictly above it for every admissible `b` and every fixed off-critical `beta<1`.

The result does rule out an imprecise next step suggested by the words "shrinking phase lock": one cannot combine the little-`o` statement of `RE-030` directly with a fine event-spacing or host-sparsity theorem and infer incompatibility. The phase offset and the phase uncertainty are different objects. Before local event granularity can enter, the spectral dominance and the `RE-029` source asymptotic must be sharpened enough to satisfy the quantitative budget (9).

Nor can this requirement be met merely by taking more fixed orders in a logarithmic asymptotic expansion. For every fixed `N`,

\[
(\log Z)^{-N}
\gg
Z^{-(1/2-\delta)}/\log Z,
\tag{27}
\]

so finite all-log accuracy remains too coarse for square-root resolution. This separates the present obstruction from the logarithmic normal forms already useful elsewhere in the line.

A viable continuation has two genuinely different options. One is to prove a **power-saving remainder** for the standard-error spectral approximation along the threshold-selected CA sequence, at least as strong as (9) for an independently useful event scale. The other is to abandon local spacing and use a global selector invariant that acts directly at logarithmic phase resolution. Multi-zero interference remains a separate possibility: `RE-031` only quantifies what is needed if a one-dominant-zero reduction is retained.

## 5. Prior-art and novelty boundary

The zero coefficients and standard/reciprocal correlation are classical explicit-formula material and are already bounded by Bhattacharya--Martin--Simpson in `SOURCES.md`. The CA event process and tangent parameter are likewise bounded by Alaoglu--Erdos, Robin, and Mantovanelli. No novelty is claimed for those ingredients, for the trigonometric inversion, or for the elementary conversion between logarithmic phase and additive displacement.

A targeted current search for Robin/colossally-abundant phase locking, zero-crossing constraints, and joint Mertens--Chebyshev off-critical phase conditions found no source combining the quantitative Robin threshold selector with this additive resolution budget. The repository-level delta is the conjunction of the existing Mathia reductions: `RE-027` fixes the CA defect scale, `RE-029` fixes the same-parameter standard race scale, and `RE-030` supplies the one-mode phase law. Equations (4), (7), and especially (9)--(10) expose the precision that any **spacing-based** continuation would actually have to achieve.

No new load-bearing external theorem is introduced, so `SOURCES.md` does not require expansion.