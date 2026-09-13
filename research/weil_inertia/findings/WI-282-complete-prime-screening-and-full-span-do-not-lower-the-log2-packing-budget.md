# WI-282 — complete prime screening and qualitative full span do not lower the log-2 packing budget

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed** first-crossing branch isolated in `WI-274` and sharpened in `WI-281`. This finding asks whether the two most immediate pieces of unused information in `WI-281`—all prime-power lags, rather than only powers of two, and the qualitative fact that a first null mode must occupy the full aperture—force a strict reduction below the packing budget `K_pack`.
- **Result:** they do not. For every aperture `a>(log 2)/2`, complete active prime-power screening already has exact relaxed supremum `K_pack`, and imposing full essential span `2a` leaves the same supremum. Thus neither “use the other primes” nor “use first-crossing full span” can by itself produce a uniform decrement below `K_pack`.
- **What it does not claim:** this does not construct a Suzuki null mode, does not show that the exact null equation can attain `K_pack`, does not address sign-changing first modes, and does not weaken the first-crossing program. It closes only the relaxation consisting of nonnegativity, normalization, aperture support, prime-power autocorrelation screening, and qualitative full span.
- **Novelty boundary:** measurable distance-avoiding sets and finite forbidden-distance optimization are classical subjects. The exact `K_pack` upper bound is inherited from `WI-281`. The new line-local point is the sharp lower approximation showing that **all** zeta prime-power lags and full essential span still fail to lower that bound. A focused prior-art search found no Suzuki/zeta statement of this finite-aperture sharpness result; no priority claim is made.

## Claim

Retain the notation of `WI-281`. Put

\[
L:=\log 2,
\qquad
I_L:=(-L/2,L/2),
\tag{1}
\]

and let

\[
K(t)=|t|w(|t|)\mathbf 1_{|t|<h_0},
\qquad
B_+(f):=\frac12\iint f(x)f(y)K(x-y)\,dx\,dy.
\tag{2}
\]

Let `T_L` be the integral operator on `L^2(I_L)` with kernel `K(x-y)` and

\[
K_{\rm pack}:=\frac12\lambda_{\max}(T_L).
\tag{3}
\]

As proved in `WI-281`, powers-of-two screening implies the sharp upper bound

\[
B_+(f)\le K_{\rm pack}
\tag{4}
\]

for every normalized nonnegative screened profile.

Fix now any

\[
a>L/2
\tag{5}
\]

and define the finite active prime-power lag set

\[
D_a:=\{\log n:\Lambda(n)>0,\ \log n<2a\}.
\tag{6}
\]

For a function supported in `(-a,a)`, every prime-power lag at least `2a` has zero autocorrelation automatically. Hence screening `D_a` is equivalent, on this aperture, to screening every prime-power lag.

Then two sharp statements hold.

### 1. Complete prime-power screening has exact budget `K_pack`

Among all `f\in L^2(-a,a)` satisfying

\[
f\ge0,
\qquad
\|f\|_2=1,
\qquad
C_f(d):=\int f(x+d)f(x)\,dx=0\quad(d\in D_a),
\tag{7}
\]

one has

\[
\boxed{\sup B_+(f)=K_{\rm pack}.}
\tag{8}
\]

The upper bound is (4), since `L\in D_a`. For the reverse inequality, let `\phi\ge0` be a normalized top eigenfunction of `T_L`, extended by zero outside `I_L`. Then

\[
B_+(\phi)=K_{\rm pack}.
\tag{9}
\]

Every positive von-Mangoldt lag is at least `L` because every prime power is an integer `n\ge2`. The support of `\phi` has diameter `L`, so

\[
C_\phi(\log n)=0
\qquad
(\Lambda(n)>0),
\tag{10}
\]

with the endpoint case `\log n=L` contributing only a null set. Since `a>L/2`, `I_L\subset(-a,a)`. Thus the `WI-281` extremizer already screens **all** prime-power lags, not only the powers of two.

This sharpens the interpretation of `WI-281`: the other primes do not lower the relaxed support-packing budget at all.

### 2. Qualitative full span still gives the same supremum

Impose in addition the first-crossing support condition

\[
\operatorname*{ess\,inf}\{x:f(x)>0\}=-a,
\qquad
\operatorname*{ess\,sup}\{x:f(x)>0\}=a.
\tag{11}
\]

Then

\[
\boxed{\sup B_+(f)=K_{\rm pack}}
\tag{12}
\]

still holds. Here the statement is about the supremum; the construction below need not attain it.

The upper bound remains (4). To prove sharpness, fix `\eta>0` and truncate the packing optimizer to

\[
J_\eta:=(-L/2+\eta,L/2-\eta).
\tag{13}
\]

Because `D_a` is finite and nonempty, write

\[
d_{\max}:=\max D_a<2a.
\tag{14}
\]

Choose `\delta>0` small enough that

\[
\delta<L,
\qquad
2a-2\delta>d_{\max},
\qquad
a-\delta>L/2-\eta.
\tag{15}
\]

Introduce two thin boundary satellites

\[
S_+=(a-\delta,a),
\qquad
S_-=(-a,-a+\delta).
\tag{16}
\]

and remove from the core every point that would form a forbidden prime-power distance with either satellite:

\[
H_\delta
:=J_\eta\cap
\bigcup_{d\in D_a}
\bigl((S_++d)\cup(S_+-d)\cup(S_-+d)\cup(S_--d)\bigr).
\tag{17}
\]

The crude measure bound

\[
|H_\delta|\le4|D_a|\delta
\tag{18}
\]

is enough. Set

\[
E_{\eta,\delta}
:=(J_\eta\setminus H_\delta)\cup S_+\cup S_-.
\tag{19}
\]

This set avoids every distance in `D_a`, up to null endpoints. Indeed:

- two core points have distance strictly below `L`, while `L=\min D_a`;
- two points in the same satellite have distance below `\delta<L`;
- points in opposite satellites have distance above `d_{\max}` by (15);
- every core--satellite pair at a distance `d\in D_a` was removed by (17).

Thus

\[
|E_{\eta,\delta}\cap(E_{\eta,\delta}-d)|=0
\qquad(d\in D_a).
\tag{20}
\]

Normalize the boundary mass by

\[
h_\delta:=(2\delta)^{-1/2}
\bigl(\mathbf1_{S_+}+\mathbf1_{S_-}\bigr)
\tag{21}
\]

and, for `\varepsilon>0`, define

\[
g_{\eta,\delta,\varepsilon}
:=\phi\,\mathbf1_{J_\eta\setminus H_\delta}
+\varepsilon h_\delta,
\qquad
f_{\eta,\delta,\varepsilon}
:=\frac{g_{\eta,\delta,\varepsilon}}
{\|g_{\eta,\delta,\varepsilon}\|_2}.
\tag{22}
\]

The function `f_{\eta,\delta,\varepsilon}` is nonnegative, normalized, supported in `(-a,a)`, has full essential span by the two satellites, and satisfies all correlations in (7) because its positive set lies in the distance-avoiding set (19).

Now send first `\eta\downarrow0`, then `\delta\downarrow0`, and finally `\varepsilon\downarrow0`. The core truncation tends to `\phi` in `L^2`; (18) and absolute continuity of the integral of `|\phi|^2` show that deleting `H_\delta` costs `o(1)` in `L^2`; and the satellites have `L^2` norm exactly `\varepsilon` before final normalization. Hence one can choose a diagonal sequence with

\[
f_{\eta,\delta,\varepsilon}\longrightarrow\phi
\quad\text{in }L^2(\mathbb R).
\tag{23}
\]

The kernel `K` is compactly supported and belongs to `L^1`: near zero the factor `|t|` cancels the simple singularity of `w(|t|)`. Young's inequality therefore gives a bounded convolution operator on `L^2`, and consequently `B_+` is `L^2`-continuous on bounded sets. From (23),

\[
B_+(f_{\eta,\delta,\varepsilon})\longrightarrow
B_+(\phi)=K_{\rm pack}.
\tag{24}
\]

Together with the upper bound, this proves (12).

## Consequence for the first-crossing bootstrap

`WI-281` left two natural possibilities for a further decrement: exploit prime lags not generated by `2^k`, or exploit the mismatch between an interval-supported `K_pack` optimizer and the full-span property forced by firstness. Equations (8) and (12) close both possibilities **as standalone scalar constraints**.

In particular, there is no constant `c(a)>0` such that

\[
B_+(f)\le K_{\rm pack}-c(a)
\tag{25}
\]

follows solely from

\[
f\ge0,
\quad \|f\|_2=1,
\quad \operatorname{supp}f\subset(-a,a),
\quad C_f(\log n)=0\ \text{for all active prime powers},
\quad \text{full essential span }2a.
\tag{26}
\]

Any strict bootstrap beyond `WI-281` must therefore consume information that the relaxation (26) discards. Plausible surviving inputs include the exact null equation `A_av=0`, quantitative lower mass in separated regions rather than mere full span, regularity or nodal information forced by the localized operator, the distributional balance between the archimedean and prime-power source terms, a positive first-crossing spectral-area margin, or simultaneous-cut identities that couple more than the autocorrelation zero set.

This is a barrier, not a counterexample to Suzuki first crossing: the approximating profiles satisfy the coarse necessary conditions but are not asserted to lie in `\ker A_a`.

## Stress tests and boundaries

1. **Why `a>L/2`.** This is exactly the regime in which `\log2` is an active lag and the `WI-281` packing upper bound applies directly. The theorem does not need an endpoint statement at `a=L/2`.
2. **Finiteness is essential only for the approximation.** For fixed `a`, `D_a` is finite because `\log n<2a` implies `n<e^{2a}`. This lets the forbidden core--satellite holes have total measure `O(|D_a|\delta)`.
3. **No hidden unscreened prime powers.** Lags at least `2a` have zero autocorrelation automatically for functions supported in `(-a,a)`, so the construction screens the full von-Mangoldt support, not merely the finite active list.
4. **The full-span condition is genuinely satisfied.** The satellites are positive on intervals reaching arbitrarily close to both endpoints; their mass may tend to zero, but their essential support endpoints remain `-a` and `a` for every member of the approximating sequence. This is precisely why a merely qualitative span condition cannot yield a quantitative budget gap.
5. **No statement about the sign-changing branch.** The deduction uses nonnegativity both in the screening-to-distance-avoidance step inherited from `WI-281` and in the support construction.

## Prior-art audit

The primary operator source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 (submitted 8 June 2026; revised 17 August 2026). Suzuki's paper gives the localized self-adjoint operators `A_a` representing the Weil quadratic form on `L^2(-a,a)` and the explicit screw-function framework; it does **not** state the packing barrier above.

For the geometric relaxation, Fernando Mário de Oliveira Filho and Frank Vallentin, *Fourier analysis, linear programming, and densities of distance avoiding sets in R^n*, JEMS 12 (2010), 1417--1428, DOI `10.4171/JEMS/236`, studies measurable sets avoiding a finite set of prescribed distances. Evan DeCorte, Fernando Mário de Oliveira Filho and Frank Vallentin, *Complete positivity and distance-avoiding sets*, Mathematical Programming 191 (2022), 487--558, DOI `10.1007/s10107-020-01562-6`, gives a later convex-optimization characterization of distance-avoiding density problems. These are prior art for the distance-avoidance viewpoint, not sources for (8) or (12).

A focused search across Suzuki/Weil first-crossing terminology, finite forbidden-distance optimization, and autocorrelation screening did not locate the specific statement that the `WI-281` top-eigenfunction budget remains sharp under **all** zeta prime-power lags and qualitative full aperture span. Search absence is not evidence of priority, and none is claimed.

## Research decision

Treat the following two proposed refinements of `WI-281` as closed unless a new quantitative hypothesis is added:

\[
\text{other prime-power lags alone},
\qquad
\text{qualitative full-span firstness alone}.
\tag{27}
\]

The next useful one-signed first-crossing test must act on the actual null equation or another quantitative source/operator constraint, not only on which autocorrelation lags vanish or on the essential diameter of the support.
