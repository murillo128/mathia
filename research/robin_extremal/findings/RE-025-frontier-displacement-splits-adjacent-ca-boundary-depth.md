# RE-025 — frontier displacement splits adjacent CA boundary mass and layer depth

**Status:** `EXACT-DERIVED + DISPLACEMENT-SPLIT + ONE-SIDED-LAYER-DEPTH-LADDER + RACE-EVENT-GEOMETRY-COUPLING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-017` controls both adjacent CA boundary transitions of a regular self-tangent local peak using only the total ordinary-prime envelope width. `RE-023` separately identifies the displacement from the last active first-layer prime as the coordinate that parametrizes the selected Chebyshev/Mertens race. The two structures can be coupled before discarding which side of the peak carries the available clearance.

Let `C` be a sufficiently large regular self-tangent colossally abundant local peak, put

\[
X:=\log C,
\]

and let

\[
\eta_-<X<\eta_+
\]

be the adjacent CA transition coordinates. If `A<C<B` are the neighboring CA states, write

\[
w_-:=\log(C/A),\qquad w_+:=\log(B/C).
\tag{1}
\]

Let `p<q` be the consecutive ordinary primes whose first-layer events enclose the entire adjacent transition gap as in `RE-017`, and define

\[
g:=q-p,\qquad d:=X-p,
\tag{2}
\]

\[
\delta_p:=\eta_{p,1}-p,\qquad
\delta_q:=\eta_{q,1}-q.
\tag{3}
\]

Then the local peak gate splits the two boundary masses according to the actual position of the self-tangent state inside its first-layer prime envelope:

\[
\boxed{
w_-<2(d-\delta_p),
}
\tag{4}
\]

and

\[
\boxed{
w_+\le 2(g+\delta_q-d)
+O\!\left(\frac{(\log X)^2}{X}\right).
}
\tag{5}
\]

Using the first-layer event expansion already established in `RE-006`,

\[
\delta_r
=\frac{\log r}{2(\log r+1)}+O(r^{-1})
=\frac12+O((\log r)^{-1}),
\tag{6}
\]

and `p\sim q\sim X`, equations (4)--(5) become

\[
\boxed{
w_-<2d-1+O((\log p)^{-1}),
\qquad
w_+\le 2(g-d)+1+O((\log p)^{-1}).
}
\tag{7}
\]

In particular the additive unit slack in the aggregate mass budget of `RE-017` cancels between the two sides:

\[
\boxed{
w_-+w_+<2g+O((\log p)^{-1}).
}
\tag{8}
\]

The directional form is more informative than (8). If a prime `r` occurs in the left adjacent quotient `C/A`, and its event is in layer `j(r)`, then

\[
\boxed{
\log r<2(d-\delta_p),
\qquad
j(r)>
\frac{\log X-O(1)}{2(d-\delta_p)}.
}
\tag{9}
\]

If a prime `s` occurs in the right adjacent quotient `B/C`, in layer `j(s)`, then

\[
\boxed{
\log s\le 2(g+\delta_q-d)
+O\!\left(\frac{(\log X)^2}{X}\right),
}
\tag{10}
\]

and

\[
\boxed{
j(s)\ge
\frac{\log X-O(1)}
{2(g+\delta_q-d)+O((\log X)^2/X)}.
}
\tag{11}
\]

Thus the same displacement `d=X-p` that appears in the selected prime-race ray of `RE-023` also allocates the admissible prime bases and layer depths on the **two sides** of the CA peak. A small left displacement forces the previous CA transition into a deep small-prime tower even if the right side of the ordinary-prime envelope is wide; symmetrically, a small residual width `g-d` forces the next transition deep.

Two useful one-sided consequences are immediate. Along any unbounded family with

\[
d=o(\log X),
\tag{12}
\]

every left-boundary factor satisfies `r=X^{o(1)}` and every corresponding layer depth tends to infinity, with no assumption that `g=o(log X)`. If instead

\[
g-d=o(\log X),
\tag{13}
\]

the same conclusions hold on the right boundary. In the stronger regime `d=O(1)`, the left boundary factors come from a fixed finite prime alphabet and their layer depths are `Omega(log X)`; the analogous statement holds on the right when `g-d=O(1)`.

This is not a sign theorem for Robin height. Its role is to remove one independence that remained in the local picture: frontier displacement, selected mixed-race position, and boundary event depth cannot be chosen separately.

## 1. The first-layer envelope splits the geometric clearance

By definition of the enclosing consecutive first-layer events,

\[
\eta_{p,1}\le\eta_-<X<\eta_+\le\eta_{q,1}.
\tag{14}
\]

Hence the left and right clearances

\[
d_-:=X-\eta_-,\qquad d_+:=\eta_+-X
\tag{15}
\]

satisfy the exact bounds

\[
\boxed{d_-\le d-\delta_p,}
\tag{16}
\]

\[
\boxed{d_+\le g+\delta_q-d.}
\tag{17}
\]

The exact convexity argument in `RE-002` gives, for a strict left Robin rise,

\[
d_->\frac{w_-}{2}.
\tag{18}
\]

Combining (16) and (18) proves (4) without an asymptotic remainder.

For the right side, `RE-002`--`RE-003` give uniformly on genuine CA transitions

\[
d_+\ge
\frac{w_+}{2}
-\kappa(X)w_+^2
+O\!\left(\frac{(\log X)^3}{X^2}\right),
\tag{19}
\]

where `kappa(X)=O(X^{-1})`. The Alaoglu--Erdos prime-or-semiprime theorem, already used in `RE-003`, gives `w_+=O(log X)`. Rearranging (19) therefore yields

\[
w_+\le2d_++O\!\left(\frac{(\log X)^2}{X}\right).
\tag{20}
\]

Equation (17) now proves (5).

This asymmetry is genuine at the finite level. Convexity gives an exact half-jump lower clearance on the left, but not on the right; replacing (5) by an exact symmetric half-jump statement would overstate `RE-002`.

## 2. The first-layer half-unit offsets cancel in the total budget

`RE-006` proves (6). The unconditional ordinary-prime envelope used by `RE-021`--`RE-023` gives `q-p=O(p^{0.52})`, while `d=O(p^{0.52})`; hence

\[
p\sim q\sim X,
\qquad
\delta_p=\frac12+O((\log p)^{-1}),
\qquad
\delta_q=\frac12+O((\log p)^{-1}).
\tag{21}
\]

Substituting (21) into (4)--(5) proves (7). Adding the two inequalities cancels the `-1` and `+1` first-layer offsets and gives (8).

Equation (8) sharpens the earlier convenient estimate

\[
w_-+w_+<2g+2+o(1)
\]

from `RE-017`. At the level of the growing-envelope host count in `RE-024` this removes only a harmless absolute multiplicative constant, so it does not justify rewriting that finding. The substantive gain is the split (4)--(5), not the constant improvement in the aggregate product budget.

## 3. Boundary mass becomes a directional layer-depth bound

Take a prime factor `r` of `C/A`, occurring in layer `j(r)` at the left transition. Since the logarithmic mass of the whole quotient is `w_-`,

\[
\log r\le w_-.
\tag{22}
\]

Equation (4) gives the first half of (9).

The elementary event-size estimate from `RE-017` says that any layer event satisfies

\[
j(r)\log r>\log\eta_{r,j(r)}-\log3.
\tag{23}
\]

Here `eta_(r,j(r))=eta_-`. Equations (14), (21), and `d=O(p^{0.52})` imply `eta_-\sim X`, so

\[
\log\eta_-=\log X+o(1).
\tag{24}
\]

Combining (22)--(24) with (4) proves the second half of (9).

The same argument on the right uses `log s<=w_+`, (5), and `eta_+\sim X`, giving (10)--(11). No prime-number theorem is needed in this layer-depth conversion; the only external prime-spacing input is the already anchored short-interval estimate used elsewhere in the line to keep the enclosing first-layer frontier at `o(X)` distance.

Equations (12)--(13) now imply the one-sided deep-layer conclusions. They are strictly more directional than `RE-017`: that finding needs the **whole** envelope `g=o(log X)` to force both boundaries deep, whereas here one side can be forced deep by its own share of the frontier displacement even if the opposite side remains unconstrained.

## 4. Coupling to the selected prime-race coordinate

`RE-023` proves for the same last active first-layer prime `p` that

\[
\mathcal E_\vartheta(p)
=
\frac d{\sqrt p}
-
\sqrt{\frac{L_p}{\ell_p}}
+O_M(L_p^{-M}),
\qquad
L_p=\log p,
\quad
\ell_p=\frac12W(2pL_p),
\tag{25}
\]

and that a Robin counterexample must simultaneously satisfy

\[
\mathcal E_{\pi_\ell}(p)-\frac d{\sqrt p}
\ge\sqrt2-O((\log p)^{-1}).
\tag{26}
\]

The present result does not invert (25) at logarithmic accuracy from the normalized error alone; its all-logarithmic remainder is much too coarse for that. Instead, the coupling is structural: the **exact geometric variable `d`** entering the square-root race ray also bounds the left transition alphabet and depth through (4) and (9), while its complementary envelope share controls the right side through (5) and (11).

Thus a future selected-event argument need not treat `RE-023` race position and `RE-017`/`RE-024` event-ladder geometry as independent labels. For example, a hypothetical counterexample subsequence with unusually small exact `d` is automatically restricted to a much deeper left event ladder before any mixed-race estimate is applied. Conversely, a theorem about the selected event ladders may be conditioned on the same `d` that parametrizes the required prime-race corner.

No contradiction follows merely from this coupling: sparse or deep event hosts can still support exceptional deterministic prime-race values.

## 5. Prior-art and evidence boundary

The load-bearing ingredients are already anchored in `SOURCES.md`: Alaoglu--Erdos for consecutive-CA quotient structure, Mantovanelli for the self-tangent prime-layer representation, Runbo Li for the current unconditional short-interval envelope, and the Robin/Nicolas/Bhattacharya--Martin--Simpson boundaries for interpreting the selected race. No new external theorem is introduced here.

A targeted current-literature search across the Mantovanelli prime-layer workload terminology, local/consecutive CA counterexample work, and Zimov's adjacent-quotient analysis did not locate the directional split (4)--(11). No novelty is claimed for the secant expansion, first-layer half-unit offset, event-size estimate, or prime-race normalizations individually. The repository-level delta is their splice: the self-tangent frontier displacement allocates the two adjacent CA transition masses separately and therefore controls their prime alphabets and layer depths on opposite sides of the peak.

The local-peak hypothesis is load-bearing because (4)--(5) use the Robin secant-clearance gate. The conclusions are not asserted for arbitrary regular self-tangent states. Tied boundary transitions are allowed because `w_-` and `w_+` are the complete adjacent quotient masses; each individual tied factor still obeys `log r<=w_±`.

Finally, (12) or (13) alone does not force Robin's inequality, and (25)--(26) do not turn the directional depth bounds into a sign law for the finite-annulus mixed race of `RE-022`. The remaining theorem is still selection-sensitive: exploit this shared displacement/depth coordinate to rule out the required mixed-race excursion on the admitted CA host sequence, rather than deriving further sparsity detached from the race.