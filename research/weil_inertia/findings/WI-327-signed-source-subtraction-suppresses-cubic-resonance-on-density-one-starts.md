# WI-327 — signed source subtraction suppresses cubic resonance on density-one starts

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECT`.

WI-325 and WI-326 show that the endpoint cubic carrier can survive both snapping to an actual zeta-zero ordinate and insertion of the raw positive von Mangoldt weights. The exact Gallagher/BOW source, however, is not weighted by `\Lambda` alone: its arithmetic coefficient is the signed difference

\[
f_X(n):=\Lambda(n)-\Lambda_X^\sharp(n),
\qquad
\Lambda_X^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}1_{(n,P(R))=1},
\qquad
R=\exp((\log X)^{1/10}).
\]

That subtraction changes the picture sharply. On the same snapped cubic scale used by WI-326, existing almost-all short-interval prime number theorems imply that for a density-one set of integer starts the two positive pieces `\Lambda` and `\Lambda_X^\sharp` each carry mass `L+o(L)`, while their signed difference has untwisted mass `o(L)`. Because the WI-325 carrier is uniformly within `\pi/768+o(1)` of `1` on a block of length `L=\lfloor X^{1/3}/8\rfloor`, this forces the *twisted* signed source to satisfy

\[
\boxed{
\left|
\sum_{j=1}^{L}
(\Lambda-\Lambda_X^\sharp)(M+j)
 e\!\left(
 \frac{\gamma_M}{2\pi}
 \log\frac{M+j}{M}
 \right)
\right|
\le
\left(\frac{\pi}{384}+o(1)\right)L
}
\]

for all but `O_A(X\log^{-A}X)` integer starts `M\in[X,3X/2]`, for every fixed `A>0`. Numerically `\pi/384\approx0.00818123`.

Thus the exact signed subtraction destroys the **generic** raw-positivity resonance mechanism exposed by WI-326: on almost every start, two individually almost fully coherent positive contributions cancel to below one percent of the coherent block length. But this is not a solution of the distinguished-BOW problem. A single source-compatible bow may live forever in the thin exceptional set, exactly the obstruction isolated by WI-190 and WI-204. The result therefore redirects the live clue from generic resonance to **de-exceptionalization**: one now needs pointwise signed control at the distinguished start, or a structural argument coupling the bow geometry to the almost-all exceptional set.

## 1. The snapped cubic carrier is uniformly close to one

Let

\[
L=\left\lfloor\frac{X^{1/3}}8\right\rfloor,
\qquad
X\le M\le\frac{3X}{2},
\]

with `M` an integer. WI-325 supplies, for every sufficiently large `M`, an actual nontrivial zero ordinate `\gamma_M` with

\[
2\pi M\left(M+\frac12\right)
<\gamma_M
\le
2\pi M\left(M+\frac12\right)+2.
\]

Write the relative carrier

\[
C_M(j):=
 e\!\left(
 \frac{\gamma_M}{2\pi}
 \log\left(1+\frac jM\right)
 \right),
\qquad 1\le j\le L.
\tag{1}
\]

The exact Taylor bookkeeping in WI-325 gives the carrier phase modulo integers as a residual `r_{M,j}` satisfying

\[
|r_{M,j}|
\le
\frac{j^2}{4M}
+
\left(1+\frac1{2M}\right)\frac{j^3}{3M}
+
\frac{j}{\pi M}.
\tag{2}
\]

On the present block, `j\le L\le X^{1/3}/8` and `M\ge X`, so

\[
\frac{j^2}{4M}
\le\frac1{256X^{1/3}},
\qquad
\left(1+\frac1{2M}\right)\frac{j^3}{3M}
\le\frac{1+o(1)}{1536},
\qquad
\frac{j}{\pi M}
\le\frac1{8\pi X^{2/3}}.
\tag{3}
\]

Therefore, uniformly in all such `M,j`,

\[
\sup_{j\le L}|r_{M,j}|
\le\frac1{1536}+o(1).
\tag{4}
\]

Since `|e(t)-1|=2|\sin(\pi t)|\le2\pi|t|`, this yields

\[
\boxed{
\sup_{j\le L}|C_M(j)-1|
\le\frac{\pi}{768}+o(1).
}
\tag{5}
\]

This is stronger than the sector bound needed in WI-326: on the shorter `X^{1/3}/8` block, the snapped carrier is not merely in a fixed positive half-plane; it is uniformly very close to the constant phase `1`.

## 2. Almost-all short-interval cancellation is already available below the cubic scale

Matomäki--Radziwiłł--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals* (arXiv:2411.05770v2, 2026), define exactly the approximant `\Lambda_X^\sharp` above. In their Section 1.1 they record the following earlier short-interval consequences of zero-density estimates and the fundamental lemma of the sieve. For every fixed `\varepsilon>0` and `A>0`, throughout

\[
H\ge X^{2/15+\varepsilon},
\]

one has outside a set of real `x\in[X,2X]` of measure `O_{A,\varepsilon}(X\log^{-A}X)` both

\[
\sum_{x<n\le x+H}(\Lambda(n)-1)
=
O_A(H\log^{-A}X)
\tag{6}
\]

and the maximal analogue

\[
\left|
\sum_{x<n\le x+H}
(\Lambda(n)-\Lambda_X^\sharp(n))
\right|^*
\le H\log^{-A}X.
\tag{7}
\]

The exponent `2/15` in (6) is the Guth--Maynard improvement of the older `1/6` range; the same regime for (7) is stated there after replacing `1` by `\Lambda^\sharp` via the fundamental lemma. This finding needs only the untwisted progression consisting of the full interval, so the maximal strength in (7) is more than enough.

Take, for example, `\varepsilon=1/10`. Then

\[
\frac{2}{15}+\frac{1}{10}=\frac7{30}<\frac13,
\]

and consequently the fixed-factor cubic length

\[
H=L=\left\lfloor\frac{X^{1/3}}8\right\rfloor
\]

lies in the valid range for all sufficiently large `X`. This use of the older short-interval PNT regime is important: Theorem 1.1(ii) of the same paper requires `H\ge X^{1/3+\varepsilon}` and therefore does **not** directly cover the block `X^{1/3}/8`.

## 3. The real exceptional-set statement transfers to integer starts

Equations (6)--(7) are stated for real starts `x`. For the present application one must not silently replace a small-measure exceptional set by a sparse set of integers. Here the transfer is nevertheless exact because `L` is an integer.

For every integer `M` and every real

\[
M<x<M+1,
\]

the integers in `(x,x+L]` are exactly

\[
M+1,M+2,\ldots,M+L.
\tag{8}
\]

Hence if the integer block beginning at `M` violates (6), then the same sum violates it for **every** `x\in(M,M+1)`; the whole unit interval must be contained in the corresponding exceptional set. The same argument applies to (7). Since these unit intervals are disjoint, after taking the union of the two exceptional sets, for every fixed `A>0` all but

\[
O_A(X\log^{-A}X)
\tag{9}
\]

integers `M\in[X,3X/2]` satisfy simultaneously

\[
\sum_{j=1}^{L}\Lambda(M+j)
=L+O_A(L\log^{-A}X)
\tag{10}
\]

and

\[
\sum_{j=1}^{L}f_X(M+j)
=O_A(L\log^{-A}X).
\tag{11}
\]

Subtracting (11) from (10) gives

\[
\sum_{j=1}^{L}\Lambda_X^\sharp(M+j)
=L+O_A(L\log^{-A}X).
\tag{12}
\]

Both `\Lambda` and `\Lambda_X^\sharp` are nonnegative. Therefore on every good integer start

\[
\begin{aligned}
\sum_{j=1}^{L}|f_X(M+j)|
&\le
\sum_{j=1}^{L}\Lambda(M+j)
+
\sum_{j=1}^{L}\Lambda_X^\sharp(M+j)\\
&=2L+O_A(L\log^{-A}X).
\end{aligned}
\tag{13}
\]

This `L^1` control is the only coefficient norm needed below.

## 4. The signed twisted residual is at most `pi/384` on density-one starts

For a good start `M`, decompose the signed twisted sum as

\[
\sum_{j=1}^{L}f_X(M+j)C_M(j)
=
\sum_{j=1}^{L}f_X(M+j)
+
\sum_{j=1}^{L}f_X(M+j)(C_M(j)-1).
\tag{14}
\]

Using (5), (11), and (13),

\[
\begin{aligned}
\left|
\sum_{j=1}^{L}f_X(M+j)C_M(j)
\right|
&\le
O_A(L\log^{-A}X)
+
\left(\frac{\pi}{768}+o(1)\right)
\left(2L+O_A(L\log^{-A}X)\right)\\
&\le
\left(\frac{\pi}{384}+o(1)\right)L.
\end{aligned}
\tag{15}
\]

Thus, for every fixed `A>0`, equation (15) holds for all but `O_A(X\log^{-A}X)` integer starts in `[X,3X/2]`.

The cancellation is not caused by either positive component being small. Equation (5) implies

\[
\Re C_M(j)
\ge
\cos\left(\frac{\pi}{768}+o(1)\right),
\]

so (10) and (12) separately give

\[
\left|
\sum_{j=1}^{L}\Lambda(M+j)C_M(j)
\right|
\ge
\left(\cos\frac{\pi}{768}+o(1)\right)L
\tag{16}
\]

and

\[
\left|
\sum_{j=1}^{L}\Lambda_X^\sharp(M+j)C_M(j)
\right|
\ge
\left(\cos\frac{\pi}{768}+o(1)\right)L.
\tag{17}
\]

Each positive term is therefore almost maximally coherent, while their signed difference is bounded by only

\[
\frac{\pi}{384}+o(1)
\]

times the block length. In particular, for any fixed

\[
c>\frac{\pi}{384},
\]

a lower bound

\[
\left|
\sum_{j=1}^{L}f_X(M+j)C_M(j)
\right|\ge cL
\tag{18}
\]

can occur at only `O_A(X\log^{-A}X)` integer starts for every `A>0`.

## 5. What this closes, and why the distinguished bow remains open

WI-326 deliberately stopped before the subtraction `\Lambda-\Lambda^\sharp`. Equations (15)--(17) show that this omission is decisive at generic starts. The raw positive prime mass does not merely fail to prove resonance for the exact source: in the almost-all regime the structured approximant supplies another nearly coherent positive mass of the same size, and the exact subtraction cancels it.

This closes the proposed continuation

\[
\text{snapped cubic carrier}
+\text{raw positive prime mass}
\Longrightarrow
\text{generic large signed BOW source}.
\]

It does **not** close the accepted distinguished-twist clue. The exceptional-set estimate (9) has density zero but is still enormous compared with one distinguished source-compatible start. WI-190 already proves abstractly that an almost-all prime-uniformity theorem can hide the entire deterministic B-process alias locus; WI-204 similarly shows that an almost-all Karatsuba exception budget cannot prune a single bow. The present result identifies the exact source-level version of that dichotomy:

- on density-one starts, the signed subtraction quantitatively suppresses the WI-325 cubic resonance;
- any persistent fixed-proportion signed resonance is forced into a super-logarithmically thin exceptional set;
- no theorem used here says that a distinguished bow start cannot always belong to that exceptional set.

Accordingly, the next source-side gate is no longer to ask whether `\Lambda^\sharp` *might* cancel the raw resonance: generically, it provably does. The live question is whether the zeta/BOW geometry can **de-exceptionalize the distinguished start**. A successful route needs either pointwise signed short-interval control at that source-compatible logarithmic phase, a coupling showing that the bow start cannot remain inside the exceptional sets across the relevant nested scales, or additional full-window/source geometry not present in the cubic subblock model.

## 6. Evidence and novelty boundary

The ingredients and deductions are separated as follows.

1. **Line-local exact input.** WI-325 supplies the actual-zero snap and the explicit phase residual (2). WI-326 supplies the raw-positive-weight stress test but does not treat the signed source.
2. **Literature-backed arithmetic input.** Matomäki--Radziwiłł--Shao--Tao--Teräväinen define the same `\Lambda_X^\sharp` used by the BOW/Gallagher bridge and, in their Section 1.1 equations (1.5)--(1.6), record the almost-all short-interval estimates (6)--(7), with the `2/15` threshold attributed to Guth--Maynard. This source is already anchored in `research/weil_inertia/SOURCES.md`.
3. **New line-local deduction.** The integer-start transfer, the combination of the two untwisted estimates with WI-325's near-constant snapped carrier, and the explicit `\pi/384` residual in (15) are exact deductions from those inputs.
4. **Prior-art boundary.** WI-190 and WI-204 already establish that almost-all estimates cannot by themselves control a distinguished bow. WI-195 already identifies `\Lambda-\Lambda^\sharp` as the exact source coefficient. This finding does not claim otherwise and makes no external priority claim for the synthesis above.

The status is therefore `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECT`: exact relative to the cited line-local and published inputs, and a material redirection because the signed subtraction is now known to kill the generic WI-326 mechanism while simultaneously exposing the exceptional-set barrier as the remaining source-side obstruction.

## Research consequence

Do not continue the WI-326 raw-positivity route by searching for more typical prime mass on snapped cubic blocks. At the exact signed coefficient, typical mass is precisely what cancels. Concentrate instead on the exceptional locus: prove that source-compatible distinguished bow starts cannot persist there, obtain pointwise control tailored to their logarithmic phase, or use full-window structure that couples the cubic block to the rest of the BOW source.