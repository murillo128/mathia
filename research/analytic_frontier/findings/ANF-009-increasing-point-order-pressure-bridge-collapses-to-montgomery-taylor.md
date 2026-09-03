# ANF-009 — increasing point order in the pressure bridge collapses back to Montgomery--Taylor

**Status:** `EXACT-DERIVED + FORMAL-SOURCE-BRIDGE + PRIOR-ART-CONFIRMED + NEGATIVE/STRUCTURAL-CEILING`. For the exact parametric `n_point_bound` bridge registered by `teal-sea/zeta-lab`, increasing the number of consecutive points cannot preserve a fixed gain over the Montgomery--Taylor baseline. For every `n >= 3`, every admissible theorem instance satisfies

\[
\Phi_n < H\frac{n}{n-1}=H+\frac{H}{n-1},
\]

while admissible instances exist arbitrarily close to `H` from below. Hence the optimal envelope of this pressure-certificate family converges exactly back to `H` as `n -> infinity`. Point count by itself is therefore a vanishing `O(1/n)` resource in this architecture.

## 1. The registered bridge and its admissible class

Write

\[
H=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=0.6725007036794116\ldots
\]

and put `r=n-1`. At the frozen Palomar source commit `84312e4477dfeb7e0d8a91c38897f225f5a52f19`, the generic local functional is

\[
F_{n,p}(g)=\frac1p\sum_{i=1}^{r}g_i+W_n(g),
\tag{1}
\]

where `g_i >= 0` are consecutive gaps and `W_n` is the nonnegative weighted sum of squared Montgomery--Taylor overlaps over all pairs of the resulting `n` ordered points. The theorem assumes a **global** finite certificate

\[
c\le F_{n,p}(g)\qquad\text{for every }g\in\mathbb R_{\ge0}^{r},
\tag{2}
\]

plus

\[
n\le m,\qquad p>0,\qquad c>0,
\qquad c\bigl(m-r\bigr)\le1.
\tag{3}
\]

Its asymptotic simple-critical-zero constant is exactly

\[
\Phi_n(c,m,p)
=
\frac{H-r(m-1)/(pm)}{1-c(m-r)/m}.
\tag{4}
\]

The formulas (1)--(4), including the global quantifier in (2) and the cap in (3), are present in the registered Lean source. No numerical certificate is needed for the upper bound below.

## 2. The cap alone gives an `O(1/n)` ceiling

Set

\[
D:=1-\frac{c(m-r)}m.
\]

From the cap in (3),

\[
D\ge1-\frac1m=\frac{m-1}{m}>0.
\tag{5}
\]

Let

\[
A:=H-\frac{r(m-1)}{pm}
\]

be the numerator of (4). If `A<0`, then `Phi_n<0`, so any positive ceiling is automatic. If `A>=0`, division by (5) gives

\[
\begin{aligned}
\Phi_n
&\le
\frac{A}{(m-1)/m}\\
&=H\frac{m}{m-1}-\frac rp\\
&<H\frac{m}{m-1}.
\end{aligned}
\tag{6}
\]

Because `m>=n` and `x/(x-1)` decreases for `x>1`,

\[
\boxed{
\Phi_n(c,m,p)<H\frac{n}{n-1}
=H+\frac{H}{n-1}
}
\qquad(n\ge3).
\tag{7}
\]

This estimate is uniform in the certificate quality `c`, the pressure `p`, the block length `m`, and the actual minimizing gap configuration. It is stronger conceptually than optimizing one more finite certificate: **the theorem's own cap prevents the high-point family from carrying a fixed positive gain.**

In particular, if a theorem instance is required to improve `H` by at least a fixed `delta>0`, then necessarily

\[
n-1<\frac{H}{\delta}.
\tag{8}
\]

So no sequence with `n -> infinity` inside this exact bridge can maintain that gain.

## 3. The ceiling really collapses to `H`, rather than merely lying below it

The upper estimate alone would allow the admissible family to become empty or collapse far below `H` for large `n`. It does neither.

Fix `n>=3` and any positive integer `p`. The function `F_{n,p}` is continuous on the nonnegative gap cone. Since `w=k^2>=0`,

\[
F_{n,p}(g)\ge\frac1p\sum_i g_i.
\tag{9}
\]

On the compact simplex `g_i>=0`, `sum g_i<=1`, `F_{n,p}` is strictly positive. Indeed a zero would force `sum g_i=0`, hence `g=0`; but at `g=0` all pair separations vanish and

\[
K(0)=\sqrt2\sin(1/\sqrt2)>0,
\qquad k(0)=1,
\qquad w(0)=1,
\]

so the pair term is strictly positive. Therefore `F_{n,p}` has a positive minimum on that simplex. Outside it, (9) gives `F_{n,p}>=1/p`. Consequently there exists some uniform `c_{n,p}>0` satisfying the global certificate (2); choose it also `<=1/2`.

Now take `m=n`. The cap becomes simply `c_{n,p}<=1`, and

\[
\Phi_n(c_{n,p},n,p)
=
\frac{H-(n-1)^2/(pn)}{1-c_{n,p}/n}.
\tag{10}
\]

For sufficiently large `p` the numerator is positive, while the denominator lies strictly between `0` and `1`. Hence

\[
\Phi_n(c_{n,p},n,p)
>
H-\frac{(n-1)^2}{pn}.
\tag{11}
\]

Given any `epsilon>0`, an integer `p` can be chosen so that the right side exceeds `H-epsilon`. Thus admissible theorem instances approach `H` arbitrarily closely from below for every fixed `n`.

If `B_n` denotes the supremum of (4) over all admissible instances of the registered bridge, (7) and (11) give the exact squeeze

\[
\boxed{
H\le B_n\le H\frac{n}{n-1},
\qquad
\lim_{n\to\infty}B_n=H.
}
\tag{12}
\]

## 4. Relation to `ANF-006`--`ANF-008`

`ANF-006` established that local ordered configuration processing can beat the global pair-moment ceiling, and the fully checked three- and four-point instances prove that this is not a formal loophole. `ANF-007` showed that two points are insufficient, so three points are the first useful local order. `ANF-008` then removed block size `m` as an independent optimization variable once a fixed improving certificate `(n,c,p)` is known.

The present result removes a different tempting escape: **keep adding points and hope the extra local compatibility accumulates into a fixed gain.** It cannot do so inside the same pressure bridge. Small finite `n` can improve `H`, but the theorem's cap dilutes the maximum possible headroom to at most `H/(n-1)`, and the optimal family returns to `H` at infinite order.

This means that higher-order work should be valued only when it changes the information architecture -- for example a different local functional, a genuine finite-memory/coboundary term, a different window, a sharper block deduction, or another pre-compression nonlinear observable. Merely increasing `n` in the current `F/Phi_n` family is asymptotically self-defeating.

## 5. Prior-art audit

The current public `teal-sea/zeta-lab` artifact `hunts/family_wall/FAMILY-LIMIT.md` independently studies this same pressure-certificate family and explicitly records the same qualitative conclusion: the family returns to `H` at large `n`. It also gives a much stronger numerical all-`n` upper envelope, `0.675142509660254`, using explicit finite witnesses and an adversarially repaired inequality chain.

That artifact is useful prior art but is not used as proof here. Its own trust boundary says the family-wall argument is not a proof-assistant theorem, and it records that an independent adversarial audit found two defects in the original chain before repairing them. The present finding uses only the registered `n_point_bound` formula, its cap, elementary sign splitting, and the positivity/continuity of the formal local functional. Accordingly no novelty is claimed for the asymptotic-limit observation itself.

A targeted web/literature check also found several August 2026 computer-assisted drafts using altered spectral deductions, windows, or Bellman/coboundary memory. Those are outside (1)--(4) and therefore do not contradict (12); they reinforce the need to state the ceiling at the level of the exact information architecture rather than as a ceiling on all configuration-level methods.

## 6. Falsification and trust boundary

The upper theorem would fail if the registered bridge did not require both `m>=n` and the cap `c(m-(n-1))<=1`, or if its `Phi_n` formula differed from (4). The frozen Palomar source contains exactly those hypotheses and that formula. No assumption about the truth of an external seven- or eight-point numerical certificate enters the argument.

The lower squeeze would fail if `F_{n,p}` could have zero global infimum for fixed positive `p`. The pressure term prevents escape to infinity, while continuity and `w(0)=1` prevent vanishing on the compact bounded region, giving a positive global floor.

The result is deliberately scoped. It does **not** prove that `0.675142509660254` is a rigorous universal ceiling at the same formal evidence tier, does not bound altered-window or Bellman/coboundary families, and does not say that higher correlations are useless. It says only that increasing point order within the registered Montgomery--Taylor pressure family cannot preserve a fixed improvement and has optimal envelope tending exactly to `H`.

## 7. Consequence for `analytic_frontier`

The configuration-level branch now has a sharp architectural boundary. Three points are the minimum order that helps; cap-saturating `m` is forced for a fixed improving certificate; and **unbounded point order in the same pressure family collapses back to the baseline**. Thus neither `m` tuning nor `n -> infinity` is a plausible source of a qualitatively larger gain.

The live frontier is correspondingly narrower: determine which modification of the local information carrier changes the pressure/cap balance itself, or prove a stronger finite-`n` ceiling for the current family at the same evidence tier. Any new candidate that keeps exactly (1)--(4) but only raises `n` should be rejected before expensive certificate search.