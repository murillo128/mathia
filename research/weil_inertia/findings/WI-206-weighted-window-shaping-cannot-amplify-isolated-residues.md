# WI-206 — weighted window shaping cannot amplify an isolated near-line residue to diagonal scale

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

WI-205 shows that the explicit-formula residue of a bounded packet of near-critical off-line zeros is too small, by itself, to reach the diagonal scale of the exact Gallagher source norm when the physical prime window is the characteristic function of an interval. A natural escape is to replace that box by a smooth, signed, complex, or otherwise optimized short-window profile and hope that the target zero is amplified relative to the von-Mangoldt diagonal.

That escape does not work within the same linear weighted-prime observable. The zero residue is an exact rank-one linear functional of the window. Its operator norm is fixed by the `L^2` norm of the power function `y^(rho-iU-1)`. Consequently, after normalizing by the standard prime-square diagonal, every profile supported on the same additive scale obeys the same `L/X` visibility factor as the box. For translate-dilate windows on `[x,x+L]`, Cauchy--Schwarz gives an even sharper shape statement: the only profile factor is

\[
\kappa(v):=\frac{\|v\|_1^2}{\|v\|_2^2}\le 1,
\]

so the interval box already maximizes the worst-case coherent residue bound among all profiles with the same support. At the source-matched twist `U=gamma` and `L=o(X)`, the box is asymptotically a matched filter for one near-line zero because the optimal power profile is nearly constant across the window.

At the WI-195 bow scale `L=X/H`, this reproduces the WI-205 finite-packet fraction

\[
\frac{M_F^2 X^{2\delta_*}}{H\log X}
\]

uniformly over the window shape. Thus smoothing, edge tapering, Cesaro weighting, sign changes, or oracle tuning of a single local profile cannot turn a bounded normalized-depth zero packet into a diagonal-scale source defect. Smoothing may still improve the **arithmetic off-diagonal estimate of the full source**, and multiwindow or nonlinear observables remain outside this finding; what is closed is the simpler idea of amplifying the distinguished zero's own explicit-formula residue by reshaping the local window.

## 1. Exact weighted residue functional

Let

\[
M_U(y):=\sum_{n\le y}\Lambda(n)n^{-iU}.
\]

For a nontrivial zero `rho=beta+i gamma` of multiplicity `m_rho`, WI-205 records the classical Perron residue contribution

\[
M_U(y)\supset -m_\rho\frac{y^{\rho-iU}}{\rho-iU}.
\tag{1}
\]

Let `v` be a nonzero bounded-variation complex profile supported in `[0,1]`, extend it by zero outside that interval, and for `0<L<X` define the weighted local source observable

\[
S_{v,U}(x;L)
:=\sum_n\Lambda(n)n^{-iU}
 v\!\left(\frac{n-x}{L}\right).
\tag{2}
\]

Equivalently this is the Stieltjes integral of the profile against `dM_U`. Applying that linear functional to the residue term (1) gives exactly

\[
\boxed{
R_{\rho,U,v}(x;L)
=-m_\rho L\int_0^1
v(t)(x+Lt)^{\rho-iU-1}\,dt.
}
\tag{3}
\]

For the characteristic profile `v=1_[0,1]`, (3) is precisely the interval residue of WI-205,

\[
-m_\rho\int_x^{x+L}y^{\rho-iU-1}\,dy.
\]

No pair-correlation hypothesis or RH enters (3). It is just the weighted form of the same classical logarithmic-derivative explicit formula.

## 2. The residue functional has an exact Hilbert-space norm

For fixed `x,L,rho,U`, regard (3) as a linear functional of `v in L^2([0,1])`. Cauchy--Schwarz is sharp and gives

\[
\boxed{
\sup_{v\ne0}
\frac{|R_{\rho,U,v}(x;L)|^2}{\|v\|_2^2}
=
 m_\rho^2L^2
\int_0^1(x+Lt)^{2\beta-2}\,dt.
}
\tag{4}
\]

The phase `gamma-U` disappears from the norm. An extremizing profile is proportional to the conjugate of `(x+Lt)^(rho-iU-1)`. Therefore tuning the twist to `U=gamma` can make the matched profile real and nonoscillatory, but it cannot increase the operator norm.

If `x\asymp X`, `L\le X`, and `beta\le1/2+delta_*`, then

\[
\int_0^1(x+Lt)^{2\beta-2}dt
\le X^{-1+2\delta_*},
\]

and hence

\[
\boxed{
|R_{\rho,U,v}(x;L)|^2
\le
m_\rho^2 L^2X^{-1+2\delta_*}\|v\|_2^2.
}
\tag{5}
\]

This already shows that no `L^2`-normalized window shape can give a single residue a better power of `L/X` than the box calculation. The exact optimizer only changes a bounded shape constant.

For a finite packet `F` with total multiplicity

\[
M_F:=\sum_{\rho\in F}m_\rho
\]

and `beta_rho\le1/2+delta_*`, the triangle inequality applied before squaring gives the profile-sensitive bound

\[
|R_{F,U,v}(x;L)|
\le
M_F L X^{-1/2+\delta_*}\|v\|_1.
\tag{6}
\]

Integrating over `x in [X,2X-L]` yields

\[
\boxed{
\int_X^{2X-L}|R_{F,U,v}(x;L)|^2dx
\le
M_F^2L^2X^{2\delta_*}\|v\|_1^2.
}
\tag{7}
\]

The packet estimate is deliberately worst-case coherent. Functional-equation mirrors, conjugates, or repeated zeros can only improve the bound if their phases cancel; no such cancellation is assumed.

## 3. The actual von-Mangoldt diagonal fixes the profile normalization

For the weighted prime sum (2), define its integrated diagonal term

\[
D_{\Lambda,v}(X,L)
:=
\int_X^{2X-L}
\sum_n\Lambda(n)^2
\left|v\!\left(\frac{n-x}{L}\right)\right|^2dx.
\tag{8}
\]

Assume `L=o(X)`, as throughout the hard bow regime. For every integer

\[
X+L\le n\le2X-L,
\]

the whole translate interval `x=n-Lt`, `0\le t\le1`, lies inside `[X,2X-L]`; hence

\[
\int_X^{2X-L}
\left|v\!\left(\frac{n-x}{L}\right)\right|^2dx
=L\|v\|_2^2.
\tag{9}
\]

Since all omitted boundary terms in (8) are nonnegative,

\[
D_{\Lambda,v}(X,L)
\ge
L\|v\|_2^2
\sum_{X+L\le n\le2X-L}\Lambda(n)^2.
\tag{10}
\]

The classical prime number theorem for the second von-Mangoldt moment,

\[
\sum_{n\le Y}\Lambda(n)^2\sim Y\log Y,
\tag{11}
\]

therefore gives

\[
\boxed{
D_{\Lambda,v}(X,L)
\ge
(1-o(1))XL\log X\,\|v\|_2^2.
}
\tag{12}
\]

No short-interval prime theorem is being smuggled into (12): after integrating over all starting points `x`, the load-bearing prime-square sum is over a macroscopic interval of length `(1-o(1))X`.

Combining (7) and (12),

\[
\boxed{
\frac{
\int_X^{2X-L}|R_{F,U,v}(x;L)|^2dx
}{D_{\Lambda,v}(X,L)}
\le
(1+o(1))
M_F^2X^{2\delta_*}
\frac{L}{X\log X}
\frac{\|v\|_1^2}{\|v\|_2^2}.
}
\tag{13}
\]

Because the profile is supported on a set of measure at most one,

\[
\boxed{
\frac{\|v\|_1^2}{\|v\|_2^2}\le1.
}
\tag{14}
\]

Equality in (14) requires `|v|` to be constant almost everywhere on its support of full measure. Thus, at fixed physical support length, **window shaping cannot increase the coherent residue-to-diagonal upper bound beyond the box value**. Smooth tapers and profiles supported on a proper subset strictly decrease the shape factor unless they approach constant modulus.

The result is stronger than saying that one particular smoothing fails. The profile may depend on `X`, on the distinguished twist, and even on the hypothetical target zero; (14) is uniform. What is held fixed is the architecture: one translate-dilate linear window on the same prime measure, judged against its own von-Mangoldt square diagonal.

## 4. The WI-195 bow scale is therefore profile-invariant

Set the physical window length to the exact Gallagher scale

\[
L=K=\frac XH.
\tag{15}
\]

Equation (13) and (14) give

\[
\boxed{
\frac{
\text{finite-packet weighted residue }L^2
}{
\text{weighted prime-square diagonal}
}
\le
(1+o(1))
\frac{M_F^2X^{2\delta_*}}{H\log X}.
}
\tag{16}
\]

This is exactly the scale found for the characteristic short interval in WI-205, now uniformly over the window profile. In the source-compatible normalized-depth regime

\[
X=T^{1/2+o(1)},
\qquad
H=\frac{T^\vartheta}{\log T},
\qquad
\delta_*\log T=O(1),
\qquad
\vartheta>0\text{ fixed},
\tag{17}
\]

one gets

\[
\boxed{
\frac{
\text{bounded-packet residue }L^2
}{
\text{weighted diagonal}
}
\ll
M_F^2T^{-\vartheta+o(1)}.
}
\tag{18}
\]

Hence the polynomial invisibility of a bounded near-line packet is not an artifact of the triangular/box physical window chosen in WI-195. Any single weighted window on the same physical scale pays the same exponent.

Conversely, (13) identifies the only way a linear window could make a bounded normalized-depth packet diagonal-sized while keeping the standard prime-square normalization: its effective support would need to be of order at least

\[
L\gtrsim X\log X\,X^{-2\delta_*}/M_F^2,
\tag{19}
\]

up to constants. For bounded `M_F` and `delta_* log T=O(1)`, this is larger than a dyadic prime block by a logarithmic factor. Merely broadening or smoothing a local window inside one dyadic source block therefore cannot reach the required scale either.

## 5. Equality and near-equality: the box is already asymptotically matched

The exact Riesz optimizer in (4) shows what a hypothetical best window would look like. At the source-matched twist `U=gamma`, it is proportional to

\[
(x+Lt)^{\beta-1}.
\tag{20}
\]

When `L=o(X)`, this varies by only `O(L/X)` across the window. Therefore the constant profile `v=1` used implicitly by WI-205 satisfies

\[
R_{\rho,\gamma,1}(x;L)
=-m_\rho\int_x^{x+L}y^{\beta-1}dy
=-m_\rho Lx^{\beta-1}
\left(1+O\!\left(\frac LX\right)\right).
\tag{21}
\]

So in the hard local regime the original box is not merely a convenient profile. It is asymptotically the matched filter for the target residue itself. An optimized smooth power taper can recover only a `1+O(L/X)` local shape correction, never the missing factor `sqrt(H log X)` needed to reach the diagonal.

For a packet of several ordinates, an oracle complex profile can attempt phase matching, but (13)--(14) already grant worst-case coherent addition through `M_F`; no profile can improve the resulting scale. Any genuine gain must therefore come from information outside the selected residues themselves.

## 6. Prior-art and novelty audit

The weighted explicit-formula mechanism is classical. Smooth compactly supported test functions and Mellin transforms are standard in Weil/von-Mangoldt explicit formulas; Bombieri's treatment of Weil's quadratic functional is already a line-local literature anchor, while WI-205 records standard Davenport/Titchmarsh/Perron references for the residue (1).

Weighted short-interval and Gallagher/Selberg smoothing are also established prior art rather than a new idea. Giovanni Coppola and Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, *Siauliai Mathematical Seminar* 10:18 (2015), 29--47, arXiv:1411.1739, explicitly studies inserting weights into Gallagher's mean-square lemma and compares smoothing by different weights. Their related weighted-Selberg work likewise studies Cesaro and other profiles. Those papers motivate checking whether a better profile changes an arithmetic mean-square estimate; they do not supply a theorem that amplifies the explicit-formula contribution of one source-selected near-line zeta zero relative to the prime-square diagonal.

The Hilbert-space calculation (4) and the profile inequality (14) are elementary Cauchy--Schwarz/Riesz facts, so no novelty is claimed for either identity in isolation. A targeted audit did not locate the specific zeta-facing consequence (13)--(18), but absence from that search is not evidence of priority. The Mathia delta is the exact comparison with WI-195/WI-205: **the isolated-residue barrier is invariant under arbitrary single-window profile optimization on the same physical scale**.

This finding is distinct from nearby local barriers. WI-187 shows that black-box Montgomery--Vaughan short-height mean value loses arithmetic resolution; WI-196 shows that positivity, bandwidth, and twist averaging cannot de-exceptionalize a distinguished center; WI-205 shows that the box-window target residue is sub-diagonal. WI-206 closes the intervening kernel-optimization loophole without assuming any of those generic average-to-pointwise implications.

## 7. Falsification boundary and research consequence

The conclusion is intentionally limited to the target zero's **own linear explicit-formula residue** inside a single weighted local prime observable. It does not upper-bound the complete `Lambda-Lambda^sharp` source norm, and it does not prevent a smooth weight from making the full arithmetic off-diagonal easier to estimate. In fact, that is the classical reason to smooth, and it remains a legitimate route to the unresolved distinguished-twist covariance problem.

The finding is also evaded by architectures that change the signal model rather than just the profile: a genuinely coupled multiwindow observable, a nonlinear statistic, a second independent source relation, a coercive identity involving many zero residues at once, or arithmetic information forcing a packet with multiplicity at least the WI-205 threshold. Prime-adaptive weights whose own diagonal is anomalously suppressed would likewise require new arithmetic structure and are not licensed by the profile-only argument above.

For the canonical RH-facing mandate, the practical consequence is sharp: **do not spend further cycles optimizing one physical Gallagher window in order to make an isolated normalized-depth off-line zero visible through its own pole.** The box is already scale-optimal. Preserve the full signed source covariance and attack the source-fixed cancellation directly, or change to an observable whose individual-exception response is genuinely different from a weighted linear von-Mangoldt sum.

## Evidence status

- `CLASSICAL-IDENTITY`: the weighted logarithmic-derivative residue and the macroscopic asymptotic `sum Lambda(n)^2 ~ X log X`.
- `EXACT-DERIVED`: equations (3)--(18), including the exact residue-functional norm and the profile-uniform diagonal comparison.
- `LITERATURE+DERIVED`: weighted Gallagher/Selberg smoothing is established prior art; its role here is to delimit the natural kernel-optimization escape rather than to support a new arithmetic theorem.
- `DECISIVE-NEGATIVE`: single-window shaping cannot repair the isolated-residue sensitivity barrier, while the full distinguished-twist covariance and other observables remain open.