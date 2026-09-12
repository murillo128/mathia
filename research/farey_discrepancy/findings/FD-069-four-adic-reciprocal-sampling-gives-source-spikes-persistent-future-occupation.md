# FD-069 — four-adic reciprocal sampling gives source spikes persistent future occupation

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + POINTWISE-SPIKE-TO-OCCUPATION + FOUR-ADIC-RECIPROCAL-SAMPLING + MOVING-HEAD + ZERO-FRONTIER-CALIBRATED + QUANTIFIER-STRENGTHENING`.

`FD-051` pushes source-independent nonsquarefree terminal occupation to quotient depths `o(sqrt(T))`, and shows that the square-root boundary is genuine for arbitrary shell profiles because individual quotient blocks can become singletons. `FD-054` and `FD-059` then use the one-Lipschitz physical shell source to carry a spike at `X` to a nearby nonsquarefree row when the physical horizon is deliberately chosen as `T=qX`; the natural transfer scale is `q asymp X/|mathcal H(X)|`.

The exact-host restriction is not intrinsic. At an **arbitrary** later horizon `T`, the reciprocal-floor samples supplied by rows divisible by four have mesh `O(X^2/T)` near quotient argument `X`. Since the physical source can change by at most one per integer step, every spike whose height dominates that mesh must be seen by at least one nonsquarefree row. Concretely, let

\[
A_X:=|\mathcal H(X)|,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\]

and

\[
U_{T,D}:=
\sum_{\substack{D<r\le T\\ \mu(r)=0}}
w(r)\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2.
\]

For integers `T,X>=1`, define the four-adic reciprocal sampler

\[
\boxed{
r_{T,X}:=
4\left\lceil\frac{\lceil T/X\rceil}{4}\right\rceil.}
\tag{1}
\]

Whenever `D<r_(T,X)<=T`, one has the pointwise lower bound

\[
\boxed{
U_{T,D}
\ge
\frac1{\zeta(2)}
\left(
A_X-\frac{4X^2}{T}-1
\right)_+^2.
}
\tag{2}
\]

Equivalently, every admissible past quotient point obeys the backward envelope

\[
\boxed{
A_X
\le
\sqrt{\zeta(2)U_{T,D}}
+\frac{4X^2}{T}+1.
}
\tag{3}
\]

Thus a low nonsquarefree numerator at one horizon constrains **all earlier physical source spikes simultaneously** by a parabolic penalty `X^2/T`. This is the pointwise source-to-occupation coupling left open after the logarithmic-density results `FD-067`--`FD-068`.

If `A_X -> infinity` and the selected row remains above the head, then the natural capture threshold is

\[
\boxed{T\asymp \frac{X^2}{A_X}.}
\tag{4}
\]

For every fixed `C>4`, every admissible horizon satisfying

\[
T\ge C\frac{X^2}{A_X}
\tag{5}
\]

obeys

\[
\boxed{
U_{T,D}
\ge
\frac1{\zeta(2)}
\left(
\left(1-\frac4C\right)A_X-1
\right)^2.
}
\tag{6}
\]

If instead

\[
\frac{TA_X}{X^2}\longrightarrow\infty,
\tag{7}
\]

then the same row carries the spike to first order and

\[
\boxed{
U_{T,D}
\ge
\left(\frac1{\zeta(2)}-o(1)\right)A_X^2.
}
\tag{8}
\]

For a fixed head `D`, once a spike has crossed the scale (4), equations (6)--(8) apply at **every sufficiently later horizon**, not merely on a selected multiplicative ray or residue class. The result does not prove a positive lower bound for `U_(T,D)/E_(T,D)`: the total energy denominator can still overwhelm the captured row. Its gain is the quantifier and the exact localization of the remaining denominator problem.

## 1. Multiples of four form a reciprocal net of mesh `O(X^2/T)`

Put

\[
y:=\frac TX,
\qquad
m:=\lceil y\rceil,
\qquad
r:=r_{T,X}=4\left\lceil\frac m4\right\rceil.
\tag{9}
\]

By construction `4|r`, so `r` is nonsquarefree. Moreover

\[
y\le m\le r<y+4.
\tag{10}
\]

Set

\[
n:=\left\lfloor\frac Tr\right\rfloor.
\tag{11}
\]

Since `r>=T/X`, one has `n<=X`. The reciprocal displacement before flooring is

\[
\begin{aligned}
0\le X-\frac Tr
&=X\left(1-\frac yr\right)\\
&=X\frac{r-y}{r}\\
&<\frac{4X}{r}\\
&\le\frac{4X^2}{T}.
\end{aligned}
\tag{12}
\]

Taking the floor costs at most one, hence

\[
\boxed{
0\le X-n\le \frac{4X^2}{T}+1.}
\tag{13}
\]

This is the entire geometric mechanism. Near quotient value `X`, moving four rows in the Jordan index changes the reciprocal quotient by only `O(X^2/T)`.

The physical source from `FD-033` has the exact increment law

\[
\mathcal H(N)=\sum_{j\le N}c(j),
\qquad
|c(j)|\le1,
\tag{14}
\]

so it is one-Lipschitz on the integers. Equations (13)--(14) give

\[
\left|\mathcal H(n)-\mathcal H(X)\right|
\le \frac{4X^2}{T}+1,
\tag{15}
\]

and therefore

\[
|\mathcal H(n)|
\ge
\left(A_X-\frac{4X^2}{T}-1\right)_+.
\tag{16}
\]

Whenever `D<r<=T`, this single row occurs in `U_(T,D)`. The uniform Jordan bound

\[
w(r)=\prod_{p\mid r}(1-p^{-2})\ge\frac1{\zeta(2)}
\tag{17}
\]

then proves (2). Rearranging (2) proves (3).

The row-admissibility condition is mild in the regimes of interest. If `X>=2`, `T>=8`, and `T/X>D`, then `r>D`; also `r<T/X+4<=T/2+4<=T`, so the selected multiple of four belongs to the physical tail. More generally, (2) is stated with the exact condition `D<r_(T,X)<=T` so no asymptotic assumption is hidden.

## 2. The deterministic capture threshold is exactly the natural host scale in dual coordinates

The transfer error in (16) is negligible compared with the spike precisely when

\[
\frac{X^2/T}{A_X}\to0,
\]

which is equation (7). Constant-factor preservation begins already when `T` is a sufficiently large constant multiple of `X^2/A_X`, proving (6).

This is exactly the `FD-054`/`FD-059` host threshold written without choosing a host first. If one writes

\[
q:=\frac TX,
\tag{18}
\]

then

\[
\frac{TA_X}{X^2}=\frac{qA_X}{X}.
\tag{19}
\]

`FD-054` starts from an integer host `q` and sets `T=qX`. The present argument starts from an arbitrary integer horizon `T`, regards `T/X` as a real target row, and rounds **that row** upward to the next multiple of four. The same dimensionless threshold appears, but the divisibility condition on `T` and the host-selection quantifier disappear.

`FD-059` improves the constant at the threshold by selecting a squarefree host `q==3 mod 4`, so its nonsquarefree twin is exactly `q+1`. That selected-host statement and (2) are complementary. The present worst-case four-adic mesh has width `<4`, which is why the universal arbitrary-horizon constant is `4`; the gain is that every horizon is covered.

For fixed `D`, a single spike therefore leaves a persistent future trace. If `A_X->infinity` and `X/A_X->infinity`, then for every fixed `C>4` all sufficiently large horizons in the half-line

\[
T\ge C\frac{X^2}{A_X}
\tag{20}
\]

satisfy the row-admissibility condition and hence (6). Increasing `T` only refines the reciprocal mesh around the fixed quotient value `X` while moving the witnessing row farther out in the Jordan tail.

## 3. Zero-frontier spikes turn the natural row exponent into a persistence onset

Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\]

and consider a zero-frontier spike sequence in the range `1/2<Theta<1` with

\[
A_X=X^{\Theta+o(1)}.
\tag{21}
\]

Equation (4) becomes

\[
\boxed{
T_{\rm cap}(X)
=X^{2-\Theta+o(1)}.}
\tag{22}
\]

At this onset scale the witnessing Jordan row is

\[
r\asymp\frac{T_{\rm cap}}X
=X^{1-\Theta+o(1)}.
\tag{23}
\]

Expressed relative to the physical horizon,

\[
\boxed{
r
=T_{\rm cap}^{\alpha_\Theta+o(1)},
\qquad
\alpha_\Theta:=\frac{1-\Theta}{2-\Theta}.}
\tag{24}
\]

This is exactly the critical row exponent isolated in `FD-054` and attained by adaptive host selection in `FD-059`. The new interpretation is stronger: `alpha_Theta` is not only the exponent at which a favorable host **can be selected**. It is the exponent at which a frontier spike begins to be visible, up to constants, on **every subsequent physical horizon** through some nonsquarefree four-adic row.

The result also crosses the source-independent square-root block boundary of `FD-051`. At the capture scale,

\[
\frac{X}{\sqrt{T_{\rm cap}}}
=X^{\Theta/2+o(1)}
=A_X^{1/2+o(1)}\to\infty.
\tag{25}
\]

So the relevant quotient argument is far beyond `sqrt(T)`, precisely where quotient blocks can be singletons and no arbitrary-profile density theorem is possible. The physical one-Lipschitz source supplies the missing regularity: although the reciprocal sample is sparse, its mesh `X^2/T` is already smaller than the spike height. Thus the square-root boundary is a boundary for **source-independent occupation**, not for source-specific spike capture.

## 4. A moving Schur head produces a second, independent onset scale

Let the head grow polynomially,

\[
D_T=T^{\delta+o(1)},
\qquad 0\le\delta<1.
\tag{26}
\]

For a horizon `T=X^{\tau+o(1)}`, the witnessing row has size

\[
r\asymp\frac TX=X^{\tau-1+o(1)},
\tag{27}
\]

while the head has size

\[
D_T=X^{\delta\tau+o(1)}.
\tag{28}
\]

The row survives the head whenever

\[
\tau-1>\delta\tau,
\qquad\text{equivalently}\qquad
\tau>\frac1{1-\delta}.
\tag{29}
\]

Constant-factor source capture requires `tau>=2-Theta` at the power level. Hence the infimum power exponent at which both constraints can hold is

\[
\boxed{
\tau_*(\delta,\Theta)
=
\max\left\{2-\Theta,\frac1{1-\delta}\right\}.}
\tag{30}
\]

The two branches meet exactly when

\[
\boxed{
\delta=\alpha_\Theta
=\frac{1-\Theta}{2-\Theta}.}
\tag{31}
\]

Thus the same exponent that `FD-059` identified as the natural critical host row also separates two obstructions for moving heads. Below `alpha_Theta`, reciprocal sampling of the source is the first limitation; above it, the Schur head deletes the natural witness before the source mesh becomes the bottleneck. Endpoint constants and subpower factors matter at equality, so (30) is a power-exponent statement rather than a claim of uniform endpoint capture.

This calibration is consistent with `FD-065`--`FD-068`: increasing the head can improve denominator-side occupation bookkeeping while simultaneously removing the low rows that carry the strongest scalar witness. Equation (30) makes that tradeoff explicit for a single physical spike.

## 5. Backward exclusion cone for low-occupation horizons

The most useful form for future work may be the contrapositive (3). Fix a horizon `T` and head `D`. For every `X` whose four-adic sampler lies in the tail,

\[
\boxed{
|\mathcal H(X)|
\le
1+\frac{4X^2}{T}
+\sqrt{\zeta(2)U_{T,D}}.}
\tag{32}
\]

Hence one small value of `U_(T,D)` does not merely say that the rows visible at `T` are individually small. It carves out a complete deterministic exclusion region in the past `(X,|mathcal H(X)|)` plane. A frontier-sized spike can coexist with that horizon only if at least one of three things happens: the horizon lies before the reciprocal capture scale `X^2/A_X`, the corresponding row has already been removed by the Schur head, or `U_(T,D)` itself is large enough to pay for the spike.

This is stronger in quantifier than the fixed-ray recurrence of `FD-067` and the global logarithmic lower-tail theorem of `FD-068`, but weaker in normalization. Those findings constrain the ratio

\[
\nu_{T,D}=\frac{U_{T,D}}{E_{T,D}}
\]

on multiplicative chains or in logarithmic measure. Equation (32) controls the numerator pointwise at every horizon but says nothing by itself about how large `E_(T,D)` can be there. A future argument can therefore combine (32) with any same-horizon denominator control without first having to locate a favorable host.

In particular, (32) does **not** cross the `FD-066` two-thirds barrier by itself. It captures one forced nonsquarefree row, not a polynomial packet, and the generic zero-frontier upper envelope for `E` can still swamp that one-row contribution. Its role is different: it removes host selection as an obstacle from the pointwise-coupling route explicitly left open after `FD-068`.

## 6. Falsification boundary and matched controls

The claim uses three pieces only: the exact reciprocal geometry (10)--(13), the physical one-Lipschitz law, and positivity of a multiple-of-four Jordan row. It is falsified by any `T,X` for which the constructed row satisfies the stated tail condition but (13) fails, or by any physical source value violating (15). No cancellation theorem, prime distribution estimate, or regular-variation hypothesis is involved.

The one-Lipschitz hypothesis is essential. `FD-051` shows that an arbitrary nonnegative shell profile can concentrate on a singleton squarefree quotient block at the square-root boundary; no version of (2) can hold for such a profile because its value may drop discontinuously before the nearest four-adic reciprocal sample. The present result succeeds beyond that boundary only because a physical spike of height `A_X` must occupy an additive width comparable to its height before it can disappear.

There is also no conflict with the synthetic escape of `FD-039`. A sparse one-Lipschitz profile can still arrange bad normalized-occupation horizons before a spike enters its capture cone, and even after capture the total energy denominator may dominate the single forced nonsquarefree term. Equation (2) forbids only the stronger scenario in which a large past physical spike leaves **no absolute nonsquarefree trace** at a sufficiently later admissible horizon.

The constant `4` is not claimed optimal. It comes from using the deterministic net of multiples of four, whose gaps are four. Favorable residue classes can improve constants when one is allowed to select the host, as in `FD-059`; the arbitrary-horizon quantifier is the point here.

## 7. Prior-art boundary and next use

A targeted prior-art search around Farey/Mertens discrepancy, Jordan-totient energies, squarefree denominator restrictions, and reciprocal-floor sampling located the expected literature on local Farey discrepancy and classical Jordan-totient identities, but no theorem matching the pointwise spike-to-nonsquarefree-energy envelope (2)--(3). No novelty is claimed for bounded gaps between multiples of four, the reciprocal derivative `d(T/r)/dr`, or the one-Lipschitz observation separately. The Mathia-specific content is their use inside the exact physical Jordan energy to convert a source spike into an arbitrary-horizon occupation witness.

No external theorem is load-bearing, so `SOURCES.md` is unchanged.

The durable next target is now sharper. `FD-067`--`FD-068` show that very low normalized occupation cannot be common in multiplicative or logarithmic scale, while (32) shows that every individual low-`U` horizon excludes a deterministic cone of large earlier source values. To advance the RH-relevant obstruction one must couple these two facts to the **same-horizon denominator** or prove that zero-frontier spikes and candidate low-occupation horizons cannot remain separated by the capture scales (22) and (30). Repeating host selection or adding more fixed nonsquarefree dilation classes does not address that remaining normalization problem.