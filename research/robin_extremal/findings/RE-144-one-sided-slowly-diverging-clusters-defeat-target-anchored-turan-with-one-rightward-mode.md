# RE-144 — one-sided slowly diverging clusters defeat target-anchored Turán with one rightward mode

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-ZERO-EDGE + TARGET-ANCHORED-TURAN + ONE-SIDED-LEFT-CLUSTER + SINGLE-RIGHTWARD-MODE + ARBITRARILY-SLOW-SCALED-ESCAPE + DECISIVE-NEGATIVE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-143` removes the rightmost-transfer loss from the leading Robin packet by anchoring Turán's First Main Theorem at an algebraically strong atom `rho_0` and applying it only to zeros on or to its right. After the far-left and high-height tails are separated, the unresolved term is the one-sided slab

\[
\beta_0-H\frac{\log U}{U}<\beta<\beta_0.
\]

A natural hope is that this new architecture might close once the rightward mode count is small, because the Turán loss then becomes harmless. The formal control from `RE-133` shows that this is false in a substantially stronger form than was visible when that finding was created.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad A>0,
\qquad 0<\kappa<\frac12,
\tag{1}
\]

and let `W(U)` and `L(T)` be arbitrary nondecreasing functions tending to infinity. There exists a **single** formal simple spectrum `Z_ctl`, closed under conjugation and `rho -> 1-rho`, with an attained finite right edge `Re rho=Theta`, together with phases `U_j->infinity`, height cutoffs `T_j`, and strict-subedge target atoms

\[
\rho_{0,j}=\beta_{0,j}+i\gamma_{0,j},
\tag{2}
\]

such that, for the leading Robin coefficient

\[
a_{\rho,0}(u)
:=
\frac{e^{-(\Theta-\beta)u}}{\rho(1-\rho)},
\tag{3}
\]

the following hold simultaneously.

First, the target is algebraically strong and asymptotically dominant in the entire strict-subedge packet:

\[
M_0^{\rm ctl}(U_j)
:=
\max_{\substack{\rho\in Z_{\rm ctl}\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,0}(U_j)|
=
(1+o(1))|a_{\rho_{0,j},0}(U_j)|
\asymp U_j^{-A}.
\tag{4}
\]

Second, after truncation at `T_j`, the target is the **only** strict-subedge mode on or to its right:

\[
\boxed{
N_{+,j}
:=
\#\left\{
\rho:\ 0<\Im\rho\le T_j,
\ \sigma_0\le\Re\rho<\Theta,
\ \Re\rho\ge\beta_{0,j}
\right\}
=1.
}
\tag{5}
\]

Third, every current-stage atom responsible for order-one cancellation lies immediately to the **left** of the target and inside an arbitrarily slowly diverging reciprocal-scale box:

\[
0<
U_j(\beta_{0,j}-\beta)
\le W(U_j),
\qquad
U_j|\gamma-\gamma_{0,j}|
\le W(U_j).
\tag{6}
\]

All strict-subedge modes outside the target plus this current near-left cluster contribute `o(M_0^{ctl}(U_j))` uniformly on the fixed-relative observation window. Nevertheless the complete packet satisfies

\[
\boxed{
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_0^{\rm ctl}(u)|
=
o\!\left(M_0^{\rm ctl}(U_j)\right).
}
\tag{7}
\]

The one-level off-critical counting function can at the same time obey the arbitrary divergent envelope

\[
N_{\rm ctl}(\sigma_0,T)\le L(T)
\tag{8}
\]

for all sufficiently large `T`, up to the same immaterial fixed enlargement used in `RE-133` if the attained-edge quartet is included in the count.

Thus the target-anchored First-Main-Theorem route can fail in the matched class even when its **rightward complexity is minimal**. The escape is carried entirely by a one-sided near-left cluster whose scaled diameter tends to infinity as slowly as prescribed.

## 1. Reuse the `RE-133` product cluster but order it from its dominant atom

Choose `0<r<1` as in `RE-133` so that, with

\[
\lambda:=-\log r>0,
\tag{9}
\]

the factor

\[
F(s)=1-r^{1+s}e^{i\pi s}
\tag{10}
\]

satisfies

\[
q:=\max_{|s|\le\kappa}|F(s)|<1.
\tag{11}
\]

At stage `j`, choose `U_j` and put

\[
\Gamma_j:=U_j^{A/2},
\qquad
\delta_j:=U_j^{-2}.
\tag{12}
\]

For every subset `S` of `{1,...,j}`, use the same simple coordinates as `RE-133`:

\[
\Theta-\beta_{j,S}
=
\delta_j+rac{|S|\lambda}{U_j},
\tag{13}
\]

\[
\gamma_{j,S}
=
\Gamma_j+
\frac1{U_j}
\sum_{\ell\in S}(\pi+\varepsilon_{j,\ell}),
\qquad
\varepsilon_{j,\ell}=U_j^{-3}3^{-\ell}.
\tag{14}
\]

The ternary perturbations make the ordinates distinct without changing the contraction mechanism. Let

\[
\rho_{0,j}:=\rho_{j,\varnothing}
=
(\Theta-U_j^{-2})+i\Gamma_j.
\tag{15}
\]

For every nonempty `S`, equations (13)--(15) give the exact one-sided ordering

\[
\boxed{
\beta_{j,S}<\beta_{0,j},
\qquad
U_j(\beta_{0,j}-\beta_{j,S})=|S|\lambda.
}
\tag{16}
\]

The same atom is the unique asymptotic coefficient maximizer because at the center

\[
\frac{|a_{\rho_{j,S},0}(U_j)|}
{|a_{\rho_{0,j},0}(U_j)|}
=
r^{|S|}(1+o(1)),
\tag{17}
\]

while

\[
|a_{\rho_{0,j},0}(U_j)|
=(1+o(1))\Gamma_j^{-2}
=(1+o(1))U_j^{-A}.
\tag{18}
\]

Thus the cancellation geometry of `RE-133` was already one-sided in the direction exposed later by `RE-143`: all nontrivial members of the active product cluster lie to the left of the dominant target.

## 2. The rightward truncated count is exactly one

Take

\[
T_j:=2\Gamma_j.
\tag{19}
\]

The phases may be chosen with the same strong lacunarity as in `RE-133`, in particular `U_{j+1}>=U_j^4`. Then for large `j` the complete stage-`j` cluster lies below `T_j`, while the first ordinate of stage `j+1` lies above `T_j`.

No earlier stage contributes a point on or to the right of `rho_(0,j)`. Indeed, for `n<j`,

\[
\max_S\beta_{n,S}
=
\Theta-U_n^{-2}
<
\Theta-U_j^{-2}
=
\beta_{0,j}.
\tag{20}
\]

Inside stage `j`, equation (16) shows that only the empty subset reaches `beta_(0,j)`. Future stages have targets closer to `Theta`, but they are excluded by the height cutoff `T_j`. Hence (5) follows.

This is the key splice with `RE-143`. Its rightward packet now contains only the target atom. Consequently the First-Main-Theorem cost

\[
e^{-\Lambda_\kappa^{(1)}N_{+,j}}
\tag{21}
\]

is a fixed nonzero constant. There is no growing rightward-complexity tax available to explain the eventual hiding.

The fixed attained-edge quartet used to make the formal edge attained is irrelevant here: both `RE-143` and the present count concern the strict-subedge packet `beta<Theta`.

## 3. The entire active cluster fits any prescribed diverging scaled radius

For the current stage, (13)--(14) give

\[
U_j(\beta_{0,j}-\beta_{j,S})
\le j\lambda,
\tag{22}
\]

and

\[
U_j|\gamma_{j,S}-\gamma_{0,j}|
\le j\pi+o(1).
\tag{23}
\]

Because `W(U)->infinity`, the recursive choice of `U_j` can be enlarged until

\[
W(U_j)
\ge
j\bigl(1+\lambda+\pi\bigr).
\tag{24}
\]

This adds no tension with the existing `RE-133` requirements: all of them become easier after enlarging `U_j`. Equations (22)--(24) prove (6).

The conclusion is stronger than the `O(log U/U)` generic localization in `RE-143`. For example, choosing

\[
W(U)=\log\log\log U
\tag{25}
\]

for sufficiently large `U` produces hiding clusters contained in a two-dimensional box of width

\[
O\!\left(\frac{\log\log\log U}{U}\right)
=o\!\left(\frac{\log U}{U}\right),
\tag{26}
\]

while the scaled radius still diverges.

This does not contradict `RE-135`. That finding proves a cardinality-free visibility floor only when the scaled reciprocal-box radius `R` is **fixed**. Here the radius grows, although it may grow arbitrarily slowly. The divergence is the essential escape currency.

## 4. Logarithmic scaled radius already supports polynomial suppression in local cardinality

The current stage has

\[
B_j:=2^j
\tag{27}
\]

simple positive-ordinate right-half-strip atoms. On `u=U_j(1+s)`, `|s|<=kappa`, their frozen leading sum factors exactly as

\[
a_{\rho_{0,j},0}(u)e^{i\Gamma_j u}
\prod_{\ell=1}^{j}
\left[
1-r^{1+s}e^{i\pi s}
 e^{i\varepsilon_{j,\ell}(1+s)}
\right].
\tag{28}
\]

For all sufficiently large `j`, every factor has modulus at most some fixed `q_1<1`. The coefficient-bracket variation in `RE-133` is bounded by

\[
O(\eta_j)
\left(1+r^{1-\kappa}\right)^j
|a_{\rho_{0,j},0}(u)|,
\qquad
\eta_j\to0.
\tag{29}
\]

The phase recursion is free enough to impose the stronger quantitative requirement

\[
\eta_j
\left(1+r^{1-\kappa}\right)^j
\le q_1^j.
\tag{30}
\]

Likewise, strengthen the old-stage and future-tail lacunarity conditions so that their total contribution on the stage-`j` window is at most `q_1^j M_0^{ctl}(U_j)`. Therefore

\[
\boxed{
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_0^{\rm ctl}(u)|
\ll q_1^j M_0^{\rm ctl}(U_j).
}
\tag{31}
\]

Writing

\[
\eta_\kappa:=
\frac{-\log q_1}{\log2}>0,
\tag{32}
\]

this becomes

\[
\boxed{
\sup|\mathcal S_0^{\rm ctl}|
\ll
B_j^{-\eta_\kappa}M_0^{\rm ctl}(U_j).
}
\tag{33}
\]

At the same time, the scaled two-dimensional radius of the cluster is only

\[
O_\kappa(j)=O_\kappa(\log B_j).
\tag{34}
\]

Thus the matched obstruction has an explicit complexity--radius law: logarithmic growth of scaled radius in the local cardinality already permits polynomial suppression of the dominant atom.

Finally, `U_j` can simultaneously be enlarged until

\[
L(\Gamma_j)\ge2^{j+3},
\tag{35}
\]

exactly as in `RE-133`. Hence the complete spectrum may still satisfy any preassigned divergent one-level off-critical counting envelope. Global sparsity does not constrain the rare local cardinality needed by (28).

## 5. The near-left slab, not the rightward Turán packet, carries the cancellation

The strengthened lacunarity has a useful target-relative interpretation. At stage `j`:

- previous stages are below `T_j` but lie strictly to the left of `beta_(0,j)` and are exponentially negligible on the observation window;
- the current nonempty subsets lie in the near-left box (6) and realize the product cancellation;
- future stages are above `T_j` and their complete coefficient tail is `o(M_0^{ctl}(U_j))`;
- the rightward truncated packet consists only of `rho_(0,j)`.

Therefore subtracting the near-left current cluster destroys the hiding: the remaining rightward target plus all far-left/high-tail errors has size comparable to the target at suitable phases, while restoring that one-sided cluster yields (31). In the decomposition introduced by `RE-143`, the **only order-`M_0` escape term is precisely the thin left remainder**.

This rules out the matched-class implication

\[
\begin{gathered}
N_+(U,T)=O(1),
\quad
\text{far-left}=o(M_0),
\quad
\text{high-tail}=o(M_0),
\\
\text{near-left width}=o(\log U/U)
\end{gathered}
\quad\Longrightarrow\quad
\text{full-packet visibility}.
\tag{36}
\]

The width condition in (36) is still too weak whenever its **scaled** radius is allowed to diverge.

## 6. Adversarial and prior-art audit

This is a matched-control theorem, not an assertion about actual zeta zeros. The construction satisfies simplicity, conjugation/functional-equation symmetry, an attained finite edge, the exact leading Robin coefficient law, an algebraically strong dominant atom, and an arbitrarily sparse one-level off-critical count. It does not assert an Euler product, zeta explicit-formula compatibility, pair-correlation law, determinant positivity, or any other source-specific relation that could forbid the cluster.

The count `N_(+,j)=1` is not obtained by deleting inconvenient farther-right atoms. Later stages do contain stricter-edge targets, but their ordinates are above the explicit cutoff `T_j` and their full coefficient contribution is already included in the controlled high tail. Earlier stages are retained below the cutoff and are genuinely farther left by (20).

No multiplicity is used. The ternary ordinate perturbations from `RE-133` make all stage coordinates simple. The active local cardinality grows, but `RE-135` is not contradicted because the scaled radius grows with it. Conversely, the result does not show that growing cardinality is necessary for every possible hiding mechanism; it only gives a source-faithful-within-the-matched-class obstruction to any localization theorem that permits arbitrary slowly diverging scaled radius.

The harmonic-analysis mechanism is the same elementary finite-product/Riesz-product mechanism already audited in `RE-133`; the Turán ingredient is exactly the target-anchored classical theorem already audited in `RE-143`. A targeted check of current zero-distribution literature did not supply an unconditional deterministic theorem excluding rare off-critical reciprocal-scale clusters of this type. No external result is load-bearing in the derivation, so `SOURCES.md` requires no new anchor.

## 7. Research effect

`RE-143` correctly removes the rightmost-transfer exponent, but it does not make the finite-edge packet coercive by itself. `RE-144` shows that even the strongest possible rightward count, `N_+=1`, can coexist with superconstant one-sided left complexity that hides the target on the full macroscopic window.

The next source-specific theorem therefore cannot be merely

\[
\beta_0-W(U)/U<\beta<\beta_0
\quad\text{with}\quad
W(U)=o(\log U).
\tag{37}
\]

Any divergent `W(U)` remains compatible with the matched control. A **localization-only** closure modeled on the fixed-box theorem `RE-135` would need a bounded two-dimensional scaled radius `U|rho-rho_0|=O(1)`, or an equivalent condition that makes the family compact. Otherwise the missing input must be genuinely relational: a zeta-specific one-sided occupancy/correlation law, a phase restriction, or an explicit-formula/Euler-product constraint that destroys the product organization even when the scaled radius grows.

This identifies the finite-edge frontier more sharply than a generic request for stronger zero density. The rightward Turán cost, far-left damping, and high-height tail can all be made harmless simultaneously; **arbitrarily slow escape of the near-left scaled radius is enough to retain the formal obstruction**.