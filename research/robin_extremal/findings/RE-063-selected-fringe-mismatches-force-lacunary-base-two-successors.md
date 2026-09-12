# RE-063 — selected fringe mismatches force lacunary base-two successors

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GENERAL-FRINGE-HOST-CLASSIFICATION + BASE-2-SUCCESSOR-LOCK + LACUNARY-HOST-SPARSITY + ZERO-DIMENSION-FRINGE-CAPACITY + EGYPTIAN-RESONANCE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-049` proves that a nonzero fringe bit at an **adjacent first-layer fan switch** forces the entered CA state to have immediate physical successor quotient `2`. That entering-transition hypothesis is stronger than the mechanism actually needs. The endpoint correction of `RE-059` is defined for every selected regular CA state, regardless of how the fan entered it. Once that correction is nonzero, the still-unfired first-layer event of the fringe prime lies less than one half-unit to the right of the selected tangent. Amplitude maximality then supplies the same curvature clearance used in `RE-049`. The two facts alone force the outgoing physical event onto the deep base-two ladder.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

and fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12).
\tag{1}
\]

Work on the sufficiently late common positive CA counterexample blocks of `RE-040`. Fix any `b\in J` and **any** exposed regular CA maximizer `C` at that threshold, including either member of a breakpoint tie. Put

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h},
\tag{2}
\]

and let `Z=Z_b(C)` be its regular adaptive tangent,

\[
g(Z)=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.
\tag{3}
\]

Let `D` be the immediate next physical CA state after `C`, let

\[
\Delta:=\log(D/C)>0,
\tag{4}
\]

and let `\xi` be the corresponding outgoing CA event coordinate, so that

\[
\log\frac{\sigma(D)/D}{\sigma(C)/C}=g(\xi)\Delta.
\tag{5}
\]

Suppose the ordinary first-layer endpoint correction of `RE-059` is nonzero. Thus there is one unique ordinary prime `r` with

\[
\boxed{r\le Z<\eta_{r,1},}
\tag{6}
\]

where `\eta_{r,1}` is the delayed first-layer CA event of `r`. Then, uniformly over all such selected states and `b\in J`,

\[
\boxed{
\frac{\log2}{2}-o_J(1)
\le \xi-Z<\frac12,
}
\tag{7}
\]

and the immediate physical successor is forced to be

\[
\boxed{\frac DC=2.}
\tag{8}
\]

Consequently the outgoing event is one unique deep base-two layer,

\[
\boxed{\xi=\eta_{2,j},\qquad j\to\infty,}
\tag{9}
\]

and the fringe prime itself is encoded by the integer part of that event coordinate:

\[
\boxed{
\lfloor\eta_{2,j}\rfloor=r\ \text{is prime},
\qquad
\frac{\log2}{2}-o_J(1)
\le\{\eta_{2,j}\}<\frac12.
}
\tag{10}
\]

No hypothesis is made on the physical transition **into** `C`. It may be first-layer, higher-layer, tied, or may be skipped entirely by the exposed fan. Thus (8)--(10) strictly extend the host classification of `RE-049` from adjacent first-layer fan switches to every selected state carrying a nonzero endpoint fringe correction.

There are two aggregate consequences. First, distinct selected fringe hosts inject into distinct base-two layers. If `N_fr(X)` counts distinct sufficiently late selected CA states with nonzero fringe correction and outgoing event coordinate `\xi\le X`, then

\[
\boxed{
N_{\rm fr}(X)
\le \log_2X+O(\log\log X)
=O(\log X).
}
\tag{11}
\]

If their distinct outgoing coordinates are `\xi_1<\xi_2<\cdots`, then

\[
\boxed{
\liminf_{n\to\infty}\frac{\xi_{n+1}}{\xi_n}\ge2.
}
\tag{12}
\]

Second, let

\[
F_C:=\{b\in I_C^\circ:\chi_C(Z_b)=1\}
\tag{13}
\]

be the portion of the exposed threshold cell on which the cell's unique fringe atom is present. Then

\[
\boxed{
|F_C|
\ll_J\frac{Y^{b_1-1}}{\log Y}.
}
\tag{14}
\]

Because the host scales are multiplicatively lacunary, for every `s>0`,

\[
\boxed{
\sum_C |F_C|^s<\infty,
\qquad
\dim_H\!\left(\limsup_C F_C\right)=0.
}
\tag{15}
\]

This upgrades the zero-dimensional support-edge result of `RE-050`: the summability is not tied to adjacent first-layer **entry** switches. It applies to the complete nonzero-fringe portions of all selected cells on the late common fan.

Finally, `RE-062` acquires a source-specific successor constraint. Every asymptotically cancelling bounded packet of Egyptian-core type has

\[
\chi_-=0,
\qquad
\chi_+=1.
\tag{16}
\]

Therefore its upper exposed endpoint is necessarily one of the lacunary hosts (9)--(12), and its immediate next physical event is a deep base-two event. If the fan has a later exposed state, the next physical packet must cross that base-two event. Hence an Egyptian cancellation cannot recur as an unconstrained independent architecture: it can occur only at a logarithmically sparse base-two predecessor and it deterministically hands the following fan motion a diverging-depth base-two atom. In the other vanishing-charge branch of `RE-062`, a `1\to1` deep-layer packet pins **both** endpoints to this same host family; only the `0\to0` deep-layer escape remains free of the fringe-host quantization.

## 1. A nonzero endpoint correction puts the outgoing event inside one half-unit

`RE-059` defines the nonzero endpoint correction by the existence of an ordinary prime `r` satisfying (6). The point is that `\eta_{r,1}` is a genuine future CA event, independently of the event type that produced the selected state `C`.

Because `C` is regular at `Z`, its support chamber has the form

\[
\xi_-<Z<\xi,
\tag{17}
\]

where `\xi` is the immediate outgoing event coordinate. Since `\eta_{r,1}>Z` is one future event, the immediate one can only occur earlier:

\[
\boxed{Z<\xi\le\eta_{r,1}.}
\tag{18}
\]

The exact first-layer staggering already used in `RE-042`--`RE-049` gives, for sufficiently large ordinary primes,

\[
r<\eta_{r,1}<r+\frac12.
\tag{19}
\]

Together with `r\le Z`, equations (18)--(19) yield

\[
\boxed{0<\xi-Z<\frac12.}
\tag{20}
\]

This is the only source-specific upper-clearance input needed below. In particular, no relation between `r` and the transition into `C` has been used.

## 2. Amplitude maximality forces the physical successor quotient to be two

Put

\[
c:=A_b(C)=Y^b(e^h-1)>0,
\qquad
\tau(x):=\log(1+cx^{-b}),
\qquad
H(x):=\log\log x+\tau(x).
\tag{21}
\]

At `C`,

\[
H(Y)=\log\log Y+h,
\qquad
H'(Y)=g(Y)-\frac{ba}{Y}=g(Z).
\tag{22}
\]

The selected state is a blockwise amplitude maximizer. If its immediate successor `D` lies in the same positive block, maximality gives

\[
h(D)\le\tau(\log D).
\tag{23}
\]

If `D` is the first state outside the block, then `h(D)\le0<\tau(\log D)`, so (23) again holds. Using `\log D=Y+\Delta` and the physical support identity (5),

\[
g(\xi)
\le
\frac{H(Y+\Delta)-H(Y)}{\Delta}.
\tag{24}
\]

The uniform late-block regime of `RE-040` gives, across the neighboring CA interval,

\[
-H''(x)=(1+o_J(1))|g'(Y)|,
\tag{25}
\]

because consecutive CA neighbors satisfy `\Delta=O(\log Y)` and the adaptive barrier curvature is lower order. The exact tangent-minus-secant identity therefore gives

\[
\begin{aligned}
g(Z)-g(\xi)
&\ge H'(Y)-\frac{H(Y+\Delta)-H(Y)}{\Delta}\\
&=\frac1\Delta\int_0^\Delta(\Delta-u)(-H''(Y+u))\,du\\
&=\left(\frac12+o_J(1)\right)|g'(Y)|\Delta.
\end{aligned}
\tag{26}
\]

On the other hand, (20) and `Z\sim Y` imply by the mean-value theorem

\[
g(Z)-g(\xi)
=(1+o_J(1))|g'(Y)|(\xi-Z).
\tag{27}
\]

Cancelling the common derivative scale between (26) and (27),

\[
\boxed{
\xi-Z
\ge\left(\frac12-o_J(1)\right)\Delta.
}
\tag{28}
\]

Combining (20) and (28),

\[
\Delta<1+o_J(1).
\tag{29}
\]

The CA event representation gives

\[
\Delta
=\sum_{(q,k)\text{ firing at }\xi}\log q
=\log Q,
\qquad Q:=D/C\in\mathbf Z_{\ge2}.
\tag{30}
\]

Since `1<\log3`, equation (29) eventually gives `\Delta<\log3`, hence `Q=2`. No tied event can remain: any tie would have event product at least `4`, while any unique generator `q\ge3` gives quotient at least `3`. Thus the outgoing event is exactly one exponent increment of the prime `2`, proving (8)--(9).

Substituting `\Delta=\log2` into (28) proves the lower half of (7). Equations (18)--(20) and `\xi=\eta_{2,j}` then give

\[
r\le Z<\eta_{2,j}<r+\frac12,
\tag{31}
\]

so `\lfloor\eta_{2,j}\rfloor=r` and the fractional part is less than `1/2`. Moreover

\[
\eta_{2,j}-r
\ge\eta_{2,j}-Z
\ge\frac{\log2}{2}-o_J(1),
\tag{32}
\]

which proves (10). Since the event coordinate tends to infinity while the base is fixed, necessarily `j\to\infty`.

## 3. Every selected nonzero-fringe host belongs to one lacunary base-two ladder

For the base-two depth `j`, write

\[
S_{2,j}=2+2^2+\cdots+2^j=2^{j+1}-2.
\tag{33}
\]

The exact CA event equation, already used in `RE-049`, gives

\[
S_{2,j}
\le
\frac{\eta_{2,j}\log\eta_{2,j}}{\log2}
\le
S_{2,j}+1.
\tag{34}
\]

Therefore `\eta_{2,j}\le X` implies

\[
j\le\log_2X+O(\log\log X).
\tag{35}
\]

A physical CA state has one immediate outgoing event. Distinct selected states with nonzero fringe correction therefore inject into distinct base-two depths, proving (11).

Equation (34) also yields

\[
\eta_{2,j}\log\eta_{2,j}
=(\log2)2^{j+1}(1+o(1)),
\tag{36}
\]

and hence

\[
\frac{\eta_{2,j+1}}{\eta_{2,j}}\longrightarrow2.
\tag{37}
\]

Any increasing subsequence of distinct layers is asymptotically at least as lacunary, proving (12). Since every selected host satisfies `Z\sim Y` by `RE-040` and (20) gives `\xi-Z=O(1)`, we also have

\[
Y\sim Z\sim\xi.
\tag{38}
\]

Thus the selected **state scales themselves** inherit the same multiplicative lacunarity.

## 4. The complete nonzero-fringe part of the fan has zero recurrent threshold dimension

Fix one selected host state `C`. `RE-059` shows that its fringe bit can switch at most once across the cell because `Z_C(b)` is increasing. Whenever the bit is one, (6) and (19) place the selector inside

\[
Z\in[r,\eta_{r,1}),
\tag{39}
\]

an interval of length less than `1/2`.

For fixed `C`, solve the tangent equation (3) for `b`:

\[
b(Z)=\frac{Y}{a}\bigl(g(Y)-g(Z)\bigr).
\tag{40}
\]

Hence

\[
\frac{db}{dZ}
=-\frac{Yg'(Z)}a
=\frac{1+o_J(1)}{aY\log Y}
\tag{41}
\]

uniformly over the half-unit fringe window, because `Z\sim Y`. Therefore

\[
|F_C|
\le
\left(\frac12+o_J(1)\right)
\frac1{aY\log Y}.
\tag{42}
\]

The quantitative false-RH amplitude inherited in `RE-040` gives, for every selected state on the compact fan,

\[
a\gg_JY^{-b_1}.
\tag{43}
\]

Equations (42)--(43) prove (14).

Order the distinct nonzero-fringe hosts by scale. From (12) and (38), for every fixed `q<2`, eventually

\[
Y_{n+1}\ge qY_n.
\tag{44}
\]

Since `1-b_1>1/2`, (14) gives for every `s>0` a geometric majorant

\[
\sum_n |F_{C_n}|^s
\ll_{J,s}
\sum_n
\left(\frac{Y_n^{b_1-1}}{\log Y_n}\right)^s
<\infty.
\tag{45}
\]

The standard Hausdorff covering criterion then gives the second part of (15). This is a statement about the full selected fringe regions `F_C`, not merely the post-switch support slacks of the special adjacent first-layer hosts treated in `RE-050`.

## 5. Egyptian cancellation now has a forced sparse successor geometry

Take the bounded-packet setting of `RE-062`. Its layer-uniform charge law is

\[
Q_n
=-\sum_i\frac1{j_{i,n}}
+\chi_{+,n}-\chi_{-,n}
+o_{J,K}(1).
\tag{46}
\]

If `Q_n\to0` through the Egyptian-core branch, `RE-062` proves that eventually

\[
\chi_{-,n}=0,
\qquad
\chi_{+,n}=1,
\tag{47}
\]

and the bounded-depth core has reciprocal-depth sum exactly one. Apply the present theorem to the selected upper endpoint `C_{+,n}`. Its immediate physical successor satisfies

\[
\boxed{
D_n/C_{+,n}=2,
\qquad
\xi_n=\eta_{2,k_n},
\qquad
k_n\to\infty.
}
\tag{48}
\]

Distinct Egyptian upper endpoints therefore inject into distinct base-two layers and obey the logarithmic count/lacunarity laws (11)--(12). If `C_{+,n}` is not the final exposed state of its block, every later exposed state is physically larger than `C_{+,n}`; the physical event packet to the next exposed state must therefore include the immediate event (48). Thus the next packet contains at least one fixed-base deep event whose depth diverges.

The same observation sharpens the other escape branch. If a deep-layer packet has `\chi_- = \chi_+ =1`, then **both** exposed endpoints are base-two predecessor hosts. The only vanishing-charge bounded architecture on which this theorem is silent is therefore the `0\to0` deep-layer branch. It remains possible, and `RE-063` does not supply the source estimate needed to exclude it.

This does not yet combine with `RE-051` into a contradiction. `RE-051` forces polynomially many exposed states only in the strongly off-critical regime and measures fan complexity relative to a block scale; the present result gives logarithmic sparsity in the absolute outgoing event coordinate. Without an independent bound on how far one positive block can stretch, or a theorem forcing a positive proportion of switches to carry nonzero endpoint fringe, those two counts cannot simply be compared.

## 6. Stress tests and prior-art boundary

The proof never assumes the Alaoglu--Erdos conjecture that every pair of consecutive CA numbers has prime quotient. The quotient `2` is deduced only **after** the half-unit source window and amplitude-curvature lower clearance force `\log(D/C)<\log3`; tied events and all bases `q\ge3` are then excluded arithmetically.

The theorem also does not claim that nonzero fringe regions exist infinitely often. If every sufficiently late selected state has `\chi=0`, all host-count and Hausdorff conclusions are vacuous, and the `0\to0` deep-layer escape from `RE-062` remains untouched. Likewise, the floor-prime condition in (10) is necessary, not sufficient: no equidistribution or recurrence statement for the fractional parts of the base-two event ladder is assumed.

Alaoglu--Erdos supplies the classical CA prime-exponent threshold/support structure, while Mantovanelli's August 2026 preprint is the closest current event/workload representation and Zimov studies restrictions on neighboring CA transitions; all are already anchored in `SOURCES.md`. A targeted current search of CA/Robin transition work found no theorem coupling an **arbitrary selected adaptive Robin state** with a raw ordinary-prime/first-layer mismatch to a forced base-two physical successor, nor the resulting Egyptian-resonance handoff. The external ingredients used here are therefore unchanged and `SOURCES.md` requires no update.

The mathematical delta is the removal of the entering-transition hypothesis from `RE-049`--`RE-050`. The source window `r\le Z<\eta_{r,1}` belongs to the selected endpoint itself, and amplitude maximality belongs to that same selected state; neither depends on how the fan arrived there. Once separated from the historical adjacent-first-layer derivation, they classify every nonzero-fringe selected host and feed directly into the exceptional packet architectures of `RE-062`.

## Consequence

The endpoint bit in the packet law is no longer a free binary correction. Whenever it is `1`, the selected CA state is immediately followed by a deep exponent increment of the fixed prime `2`, with the event coordinate lying in a narrow prime-floor window. Consequently every Egyptian-core cancellation from `RE-062` lands on a logarithmically sparse, multiplicatively lacunary host set and forces the following physical motion to begin with a diverging-depth base-two event.

The surviving bounded-packet obstruction is correspondingly sharper: a closing argument can focus on the `0\to0` deep-layer regime, or prove that the false-RH fan must use nonzero-fringe endpoints too often for the base-two ladder to support. The Egyptian-core branch is not eliminated, but it is no longer an arbitrary finite catalogue repeated at arbitrary scales.