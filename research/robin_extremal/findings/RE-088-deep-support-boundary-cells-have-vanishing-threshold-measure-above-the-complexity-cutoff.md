# RE-088 — deep support-boundary cells have vanishing threshold measure above the complexity cutoff

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-RH-FAILURE + SELECTION-WEIGHTED-HIGHER-LAYER-TAIL + THRESHOLD-MEASURE-COLLAPSE + FIXED-DEPTH-CUTOFF + SECOND-LAYER-BARRIER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-085` shows that higher-layer event mass is asymptotically negligible on stretched mixed fans, but leaves singular effects such as adjacency and support selection untouched. `RE-086` then shows that a fixed-layer event selected as an actual support boundary must satisfy an anchored ordinary-prime-gap resonance, while `RE-087` proves that summing those marginal gap capacities over all candidate primes cannot close the channel: after the CA small-height conversion there is asymptotically more than enough candidate one-sided gap capacity.

The correct next summation is therefore not over **candidate base primes**, but over the **actual exceptional support coordinates that can carry selected threshold cells**. In the strongly off-critical regime where `RE-051` forces every fan cell to be polynomially small, the higher-layer counting hierarchy of `RE-004` makes that selected sum convergent above an explicit depth cutoff.

Let `theta in (1/2,1)` be any exponent for which every sufficiently large interval

\[
[x-x^\theta,x]
\tag{1}
\]

contains a prime. Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\theta.
\tag{2}
\]

Fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\theta)
\tag{3}
\]

and define the positive fan-complexity exponent

\[
\boxed{\delta:=1-b_1-\theta>0.}
\tag{4}
\]

On a sufficiently late common positive CA counterexample block `B` from `RE-040`, let `E(B,J)` be the states exposed by the rightmost adaptive threshold fan and write

\[
Y_C:=\log C,
\qquad
I_C:=\{b\in J:C\text{ is the rightmost maximizer of }A_b\}.
\tag{5}
\]

Fix an integer `r>=2`. Call an exposed state `C` **`r`-deep-boundary** if at least one of its two adjacent physical support coordinates contains a genuine CA event `(p,j)` with `j>=r`; ties count if any participating event has depth at least `r`. Let

\[
\mathcal D_r(\mathcal B,J)
:=\{C\in\mathcal E(\mathcal B,J):C\text{ is }r\text{-deep-boundary}\}
\tag{6}
\]

and let

\[
J_{\ge r}(\mathcal B)
:=\bigcup_{C\in\mathcal D_r(\mathcal B,J)} I_C.
\tag{7}
\]

Finally put

\[
X_{\mathcal B}:=
\min_{C\in\mathcal E(\mathcal B,J)}Y_C.
\tag{8}
\]

If

\[
\boxed{\delta>\frac1r,}
\tag{9}
\]

then

\[
\boxed{
|J_{\ge r}(\mathcal B)|
\ll_{J,r,\delta}
X_{\mathcal B}^{\,1/r-\delta}
(\log X_{\mathcal B})^{1/r}
\longrightarrow0.
}
\tag{10}
\]

Thus, whenever (9) holds, asymptotically almost every threshold `b in J` is selected by a state whose **two adjacent support transitions contain no event of depth `j>=r`**. Deep events may still exist elsewhere in the CA staircase, and they may still be crossed inside skipped physical spans; what disappears is their threshold-measure capacity as actual adjacent boundaries of the selected fan.

With the currently anchored unconditional exponent `theta=0.52`, every false-RH frontier `Theta>0.52` admits some finite cutoff. Indeed, choose any fixed integer `r` satisfying

\[
\boxed{\frac1r<\Theta-0.52.}
\tag{11}
\]

Then one can choose `b_1` with

\[
1-\Theta<b_1<0.48-\frac1r,
\tag{12}
\]

so that (9) holds. For example,

\[
\Theta>0.52+\frac13
\tag{13}
\]

allows `r=3`; on a suitable compact threshold interval, cells whose adjacent support boundary contains any layer `j>=3` then have vanishing total threshold measure.

There is also a sharp negative boundary for this mechanism. Taking `r=2` would require `delta>1/2`, but from `b_1>1-\Theta` and `\Theta\le1`,

\[
\delta
=1-b_1-\theta
<\Theta-\theta
\le1-\theta
<\frac12.
\tag{14}
\]

Hence **no prime-in-short-interval exponent `theta>1/2`, even arbitrarily close to the square-root barrier, can make this counting-plus-cell-width argument eliminate second-layer support selection.** The route provably bottoms out at the `j=2` chamber. Any attempt to close the singular support-boundary mechanism completely must therefore use extra structure at layer two: anchored-gap selection, tied-state compatibility, rightmost-maximizer geometry, or another source coupling not visible in ambient event counts.

## 1. Every selected cell has a polynomial width ceiling at its own support scale

`RE-051` applies on the present interval `J` and gives, uniformly over all exposed states on all sufficiently late blocks,

\[
\boxed{
|I_C|
\ll_J
\frac{Y_C^{-\delta}}{\log Y_C}.
}
\tag{15}
\]

The same proof also localizes the two actual adjacent support coordinates. Let

\[
\xi_-(C)<Z_b(C)<\xi_+(C)
\tag{16}
\]

be the physical CA event coordinates bracketing any regular selector belonging to `C`. `RE-040` gives

\[
\frac{Z_b(C)}{Y_C}\to1
\tag{17}
\]

uniformly on the compact fan. The short-interval prime mesh used in `RE-051` places genuine first-layer events on each side of `Z_b(C)` within `O(Y_C^\theta)`, so adjacency forces

\[
\xi_+(C)-\xi_-(C)
\ll Y_C^\theta=o(Y_C).
\tag{18}
\]

Because `Z_b(C)` lies between those boundaries, (17)--(18) imply uniformly

\[
\boxed{
\frac{\xi_\pm(C)}{Y_C}\to1.
}
\tag{19}
\]

Therefore if `\xi` is either adjacent support coordinate of `C`, then for sufficiently late blocks

\[
\boxed{
|I_C|
\ll_J
\frac{\xi^{-\delta}}{\log\xi}.
}
\tag{20}
\]

This is the selection-sensitive currency needed below. `RE-087` summed gap capacities over every candidate prime in a shell and found divergence. Equation (20) instead charges the width of an **actually selected state** to one of its actual adjacent support coordinates.

## 2. The depth-at-least-`r` event family has a summable weighted tail exactly above `1/r`

Let

\[
M_{\ge r}(T)
:=
\#\{(p,j):j\ge r,\ \eta_{p,j}\le T\},
\tag{21}
\]

where event occurrences are counted with their layer identity, even when several events tie at one physical coordinate. `RE-004` proves, for every fixed `r>=2`,

\[
\boxed{
M_{\ge r}(T)
=O_r\!\left((T\log T)^{1/r}\log T\right)
=O_r\!\left(T^{1/r}(\log T)^{1+1/r}\right).
}
\tag{22}
\]

Consider the weighted tail

\[
W_r(X)
:=
\sum_{\substack{(p,j):\,j\ge r\\ \eta_{p,j}\ge X}}
\frac{\eta_{p,j}^{-\delta}}{\log\eta_{p,j}}.
\tag{23}
\]

Decompose the event axis dyadically. On the shell

\[
2^kX\le\eta_{p,j}<2^{k+1}X,
\tag{24}
\]

there are at most

\[
M_{\ge r}(2^{k+1}X)
\ll_r
(2^kX)^{1/r}
\bigl(\log(2^kX)\bigr)^{1+1/r}
\tag{25}
\]

occurrences, while every weight is at most

\[
\frac{(2^kX)^{-\delta}}
{\log(2^kX)}.
\tag{26}
\]

Hence the shell contributes

\[
\ll_r
(2^kX)^{1/r-\delta}
\bigl(\log(2^kX)\bigr)^{1/r}.
\tag{27}
\]

If `delta>1/r`, the power of `2^k` is strictly negative and dominates the logarithmic factor. Summing over `k>=0` yields

\[
\boxed{
W_r(X)
\ll_{r,\delta}
X^{1/r-\delta}(\log X)^{1/r}.
}
\tag{28}
\]

This is the exact cutoff behind (10). At `delta=1/r` the dyadic series is not forced to converge by the available counting theorem, and below that threshold it grows at the level of this estimate. No stronger claim is made there.

## 3. Actual support selection has bounded multiplicity, so the weighted tail controls threshold measure

Take an `r`-deep-boundary state `C` and choose one adjacent support coordinate `\xi(C)` that contains an event `(p,j)` with `j>=r`. By (20),

\[
|I_C|
\ll_J
\frac{\xi(C)^{-\delta}}{\log\xi(C)}.
\tag{29}
\]

A distinct physical transition coordinate can border at most two open CA chambers, one on each side. Every positive-width rightmost fan cell belongs to an exposed regular state whose selector lies in such an open support chamber by `RE-040`. Therefore, after charging each state in `D_r(B,J)` to one chosen deep adjacent coordinate, **the multiplicity of the charge is at most two**.

Ties do not create a loophole. If several layer events occupy one transition coordinate, that coordinate is still one physical boundary and still borders at most two chambers. Conversely, the cumulative count (22) counts tied event occurrences separately, so it only overcounts the number of available deep transition coordinates. Thus

\[
\sum_{C\in\mathcal D_r(\mathcal B,J)}|I_C|
\ll_J
\sum_{\substack{(p,j):\,j\ge r\\
\eta_{p,j}\ge (1-o(1))X_{\mathcal B}}}
\frac{\eta_{p,j}^{-\delta}}{\log\eta_{p,j}}.
\tag{30}
\]

For sufficiently late blocks, the uniform comparison (19) lets us replace the lower cutoff by `X_B/2`. Combining (28) and (30),

\[
\begin{aligned}
|J_{\ge r}(\mathcal B)|
&\le
\sum_{C\in\mathcal D_r(\mathcal B,J)}|I_C|\\
&\ll_{J,r,\delta}
X_{\mathcal B}^{1/r-\delta}
(\log X_{\mathcal B})^{1/r},
\end{aligned}
\tag{31}
\]

which proves (10) because the counterexample blocks escape and `1/r-delta<0`.

The estimate is independent of the upper physical extent of the block. This matters because the long-fan branch can stretch by an unbounded factor: a crude bound using the number of deep events only up to the block endpoint would reintroduce that uncontrolled stretch. The convergent tail (28) instead pays for every possible future deep boundary at once.

## 4. The strong off-critical fan has a finite singular-depth cutoff

Insert the best all-large short-interval exponent already used by this line, `theta=0.52`. If `Theta>0.52`, choose a fixed integer `r` with (11). Then

\[
1-\Theta
<0.48-\frac1r,
\tag{32}
\]

so there exists a compact interval `J` satisfying (3) and (12). On that interval,

\[
\delta=1-b_1-0.52>\frac1r,
\tag{33}
\]

and (10) applies.

Thus the support-boundary singularity left by `RE-085` does not remain an unrestricted all-layer phenomenon in the strong off-critical regime. For every fixed `Theta>0.52`, one can choose a finite depth cutoff `r=r(Theta)` so that the union of selected threshold cells touching layers `j>=r` has vanishing measure. The remaining adjacent-boundary problem is finite-layer.

The numerical examples should not be overinterpreted. `r=3` becomes available only for

\[
\Theta>0.853\overline3,
\tag{34}
\]

while a frontier only slightly above `0.52` requires a much larger fixed `r`. The theorem does not say that low-layer singularities are rare, only that sufficiently deep ones cannot carry a positive proportion of a fixed threshold interval once the cell-width exponent beats their ambient count exponent.

Equation (14) identifies the non-negotiable obstruction. Since the depth-two event family naturally lives on the square-root counting scale and the prime-mesh cell exponent satisfies `delta<1/2`, the present mechanism can never reach `r=2`. Improving the short-interval exponent toward `1/2` only lets the inequality approach equality from the wrong side. A second-layer theorem therefore needs information beyond ambient counting and generic cell width.

## 5. Stress tests and exact boundary of the claim

Equation (10) is a **threshold-measure** statement, not a pointwise exclusion. A vanishing set of thresholds may still carry infinitely many deep-boundary states, and the rightmost fan may concentrate delicate arithmetic behavior there. The result says only that those states cannot occupy a positive fraction of the fixed interval `J` under (9).

The theorem concerns adjacent support boundaries. A depth-`j>=r` event may lie inside a physical span skipped by two successive selected fan states, alter an exponent vector, or affect a nonlocal rightmost-maximizer comparison without ever becoming one of the two adjacent boundaries of a positive-width selected cell. Those singular mechanisms remain outside (10), exactly as already separated in `RE-085`--`RE-087`.

The depth `r` is fixed before the asymptotic limit. The constants in `RE-004` are fixed-depth constants, so (10) does not justify taking `r=r(X_B)` tending to infinity with scale.

The strongly off-critical hypothesis is load-bearing. With current unconditional prime intervals, `RE-051` gives the required positive `delta` only when `Theta>0.52`. The near-critical region `1/2<Theta<=0.52` is untouched.

Finally, (10) does not contradict the divergent marginal capacity of `RE-087`. That result distributes abstract cell widths over **all potential base primes** in a dyadic shell and deliberately forgets whether the adaptive fan can select them. The present proof uses no gap-capacity scarcity at all. It sums only the actual support coordinates capable of hosting deep selected cells and combines their ambient occurrence count with the independently forced cell-width ceiling.

## 6. Prior-art boundary and research consequence

The load-bearing external input is the same all-large prime-in-short-interval theorem already anchored for `RE-051`; no new source entry is required. The higher-layer event count is internal to `RE-004`, derived from the exact CA event equation, and the selection width comes from the regular compact fan of `RE-040` plus `RE-051`.

A targeted current search of the recent CA/Robin literature found Mantovanelli's prime-layer event/workload framework and Zimov's work on consecutive CA transitions, but no statement equivalent to the selection-weighted tail (28)--(31), the finite singular-depth cutoff (10)--(12), or the second-layer impossibility boundary (14). No blanket novelty claim is made: the weighted-tail argument is elementary once the two line-specific exponents are placed on the same scale.

The durable consequence is a sharper decomposition of the post-`RE-087` frontier. **Marginal ordinary-gap capacity is abundant, but arbitrarily deep adjacent-boundary selection is not.** In every strong off-critical case covered by the current short-interval theorem, the support-boundary problem can be reduced, in threshold measure, to finitely many low layers. The next source-sensitive target is therefore not generic all-layer sparsity. It is the irreducible low-layer chamber — especially `j=2` — together with tied low-layer resonances, skipped-span conditioning, and discontinuous rightmost-maximizer effects.