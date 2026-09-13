# RE-098 — resonant four-zero energy already clears the Robin host window

**Status:** `EXACT-DERIVED + DEFORMED-QUADRATIC-SPARSE-HOSTS + EXPLICIT-FORMULA-FOURTH-MOMENT + ZERO-ADDITIVE-ENERGY + RESONANT-THRESHOLD-0.341216 + ROBIN-WINDOW-OVERLAP + SHIFTED-FOUR-ZERO-FRONTIER + PRIOR-ART-AUDITED`.

`RE-097` leaves a precise analytic target for the residual mixed first/depth-two Robin channel: for the deterministic CA sample

\[
x(n)=\eta_1^{-1}(\eta_2(n)),\qquad n\asymp X^{1/2},
\]

find some `vartheta<73/200` for which the number of one-sided prime-free intervals of length `X^vartheta` adjacent to `x(n)` has a fixed power saving below the trivial `X^(1/2)` host count. The natural direct route is a fourth moment of the explicit formula, because its near-resonant part is governed by the four-zero additive energy

\[
N^*(\sigma,T)
=
\#\{(\rho_1,\rho_2,\rho_3,\rho_4):
\Re\rho_j\ge\sigma,
|\Im\rho_j|\le T,
|\gamma_1+\gamma_2-\gamma_3-\gamma_4|\le1\}.
\]

This finding evaluates that part exactly enough to locate the real obstruction. The result is unexpectedly favorable: **the known Heath-Brown four-zero energy bound already gives a power saving on the resonant contribution once**

\[
\boxed{
\vartheta>\vartheta_{\rm res}
:=\frac{69-16\sqrt3}{121}
=0.3412164221\ldots,
}
\]

and this lies strictly below the Robin requirement

\[
\vartheta<\frac{73}{200}=0.365.
\]

Thus there is a genuine interval of exponents in which the resonant zero quartets are already harmless. Within this fourth-moment route, the missing theorem is not an improvement to ordinary zero additive energy. It is control of the **shifted/nonresonant** combinations `|gamma_1+gamma_2-gamma_3-gamma_4|>1` together with the deformed-quadratic phase sum from `RE-096`.

## 1. A bad CA sample feeds the standard fourth-moment zero sum

Put

\[
M=X^{1/2},\qquad H=X^\vartheta,
\qquad
T=\frac XH(\log X)^3=X^{1-\vartheta+o(1)}.
\tag{1}
\]

Consider one orientation, say `(x(n),x(n)+H]`; the left interval is identical for the estimates below. If this interval contains no ordinary prime, its von Mangoldt mass from prime powers is `X^{o(1)}` when `vartheta<1/2`, hence `o(H)`. Therefore a bad host forces

\[
|\psi(x(n)+H)-\psi(x(n))-H|
\ge (1-o(1))H.
\tag{2}
\]

The explicit formula used by Bazzanella gives, uniformly on a bounded-ratio shell,

\[
\psi(y+H)-\psi(y)-H
=-\sum_{|\gamma|\le T}y^\rho c_\rho(y)+o(H),
\qquad
|c_\rho(y)|\ll \min\!\left(\frac HX,\frac1{|\gamma|}\right).
\tag{3}
\]

The same Montgomery-density/zero-free-region truncation used there removes the real-part range outside a fixed

\[
I=[1/2,1-d],\qquad d>0,
\tag{4}
\]

at cost `o(H)` uniformly in `y`. Split `I` into `O(log X)` slabs of width `1/log X`. For one slab with left endpoint `sigma`, all logarithmic losses can be absorbed into `X^{o(1)}`, and fourth-moment Markov gives the model bound

\[
\#\mathcal Z_{\vartheta,\sigma}(X)
\ll
X^{4\sigma-4+o(1)}
\sum_{n\asymp M}
\left|
\sum_{\substack{|\gamma|\le T\\
\beta\ \mathrm{in\ the\ slab}}}
e^{i\gamma\log x(n)}
\right|^4.
\tag{5}
\]

This reduction uses only `x(n)\asymp X`; the physical drift of `RE-096` causes no loss in the coefficient size.

Expanding the fourth power introduces

\[
\Omega=\gamma_1+\gamma_2-\gamma_3-\gamma_4
\tag{6}
\]

and the sample kernel

\[
S_X(\Omega)
:=
\sum_{n\asymp M}e^{i\Omega\log x(n)}.
\tag{7}
\]

For the resonant quartets `|Omega|<=1` no phase estimate is needed: trivially

\[
|S_X(\Omega)|\le M.
\tag{8}
\]

Consequently their entire contribution to (5) is

\[
\boxed{
\mathcal B_{\rm res}(\sigma)
\ll
X^{4\sigma-4+1/2+o(1)}N^*(\sigma,T).
}
\tag{9}
\]

In particular, this part of the argument is completely insensitive to whether the sample is the exact quadratic lattice or the CA deformation. The only source-specific issue begins once `|Omega|>1` and cancellation in (7) matters.

## 2. The exact resonant threshold is 0.341216..., below 73/200

The four-zero estimate used in Bazzanella, originating in Heath-Brown's zero-density work, has the form

\[
N^*(\sigma,T)\ll_\varepsilon T^{e(\sigma)+\varepsilon},
\tag{10}
\]

with

\[
e(\sigma)=
\begin{cases}
\dfrac{10-11\sigma}{2-\sigma},&1/2\le\sigma\le2/3,\\[6pt]
\dfrac{18-19\sigma}{4-2\sigma},&2/3\le\sigma\le3/4,\\[6pt]
\dfrac{12(1-\sigma)}{4\sigma-1},&3/4\le\sigma\le1.
\end{cases}
\tag{11}
\]

Substituting `T=X^(1-vartheta+o(1))` into (9), the resonant block has a power saving below the `M=X^(1/2)` host count whenever

\[
\Delta_\vartheta(\sigma)
:=
4(1-\sigma)-(1-\vartheta)e(\sigma)>0.
\tag{12}
\]

Equivalently,

\[
\vartheta>
F(\sigma)
:=1-\frac{4(1-\sigma)}{e(\sigma)}.
\tag{13}
\]

The three pieces can be optimized exactly. On `[1/2,2/3]`, the maximum occurs at

\[
\sigma_0=\frac{10-2\sqrt3}{11}=0.59417258\ldots
\tag{14}
\]

and

\[
\max F(\sigma)
=
\boxed{
\frac{69-16\sqrt3}{121}
=0.3412164221\ldots
}.
\tag{15}
\]

On `[2/3,3/4]` the corresponding maximum is

\[
\frac{193-32\sqrt5}{361}
=0.3364150269\ldots,
\tag{16}
\]

while on `[3/4,1]` one has simply

\[
F(\sigma)=\frac{4(1-\sigma)}3\le\frac13.
\tag{17}
\]

Thus (15) is the global threshold. For every fixed

\[
\boxed{
\vartheta_{\rm res}<\vartheta<\frac{73}{200}
}
\tag{18}
\]

and the fixed compact real-part range (4),

\[
c_{\vartheta,d}
:=
\min_{\sigma\in[1/2,1-d]}
\Delta_\vartheta(\sigma)>0,
\tag{19}
\]

so the resonant contribution satisfies

\[
\boxed{
\mathcal B_{\rm res}
\ll
X^{1/2-c_{\vartheta,d}+o(1)}.
}
\tag{20}
\]

The interval (18) is not marginal: its width is

\[
\frac{73}{200}-\vartheta_{\rm res}
=0.0237835778\ldots.
\tag{21}
\]

Hence the `RE-095` requirement of **some** polynomial host saving below `vartheta=73/200` is already compatible with the existing resonant four-zero input.

## 3. The unresolved object is shifted additive energy weighted by the CA phase kernel

For `|Omega|>1`, the fourth moment no longer reduces to `N^*(sigma,T)`. Define the dyadic shifted energy

\[
N^*_{\rm sh}(\sigma,T;U)
:=
\#\left\{
(\rho_1,\ldots,\rho_4):
U<|\Omega|\le2U
\right\},
\qquad 1\le U\ll T,
\tag{22}
\]

with the same zero range as above, and

\[
K_X(U)
:=
\sup_{U<|\omega|\le2U}
|S_X(\omega)|.
\tag{23}
\]

Up to logarithmic factors, the complete nonresonant term is bounded by

\[
\boxed{
X^{4\sigma-4}
\sum_{U\ {m dyadic}}
K_X(U)N^*_{\rm sh}(\sigma,T;U).
}
\tag{24}
\]

Therefore a direct route to the `RE-096` target is now explicit: for some `vartheta` in (18), prove that (24) is

\[
\ll X^{1/2-\delta}
\tag{25}
\]

uniformly over the beta slabs, for one fixed `delta>0`. This is a **shifted four-zero/phase-cancellation** theorem, not an unshifted zero-energy theorem.

There is a useful matched control showing that the distinction is real. Discretize the pair sums `gamma_1+gamma_2` into unit bins and let `A_j` be their occupancies. The ordinary energy is, up to harmless neighboring-bin factors, `sum_j A_j^2`. For every fixed integer shift `h`, Cauchy gives

\[
\sum_j A_jA_{j+h}
\le
\left(\sum_jA_j^2\right)^{1/2}
\left(\sum_jA_{j+h}^2\right)^{1/2}
\ll N^*(\sigma,T).
\tag{26}
\]

Summing `O(U)` unit shifts yields only

\[
N^*_{\rm sh}(\sigma,T;U)
\ll U\,N^*(\sigma,T).
\tag{27}
\]

If one combines (27) merely with the trivial `K_X(U)<=M`, the critical-line block `sigma=1/2`, where `N^*(1/2,T)\ll T^{3+o(1)}`, gives

\[
X^{-2}\,M\,T\,N^*(1/2,T)
\ll
X^{2.5-4\vartheta+o(1)}.
\tag{28}
\]

To make (28) smaller than the trivial host count `X^(1/2)` requires

\[
\vartheta>\frac12.
\tag{29}
\]

So **unshifted additive energy plus a generic shift count reproduces the square-root barrier exactly**. The gain from (15) can only be realized by using cancellation in `K_X(U)`, a genuinely stronger shifted-energy estimate than (27), or both.

`RE-096` supplies the relevant phase geometry:

\[
\frac d{dt}\log x(t)
=\frac2t\left(1+O((\log t)^{-2})\right),
\qquad
\frac{d^2}{dt^2}\log x(t)
=-\frac2{t^2}\left(1+O((\log t)^{-2})\right).
\tag{30}
\]

Thus (24) is now the precise place where the deformed-quadratic structure can matter. The resonant estimate (20) did not use (30) at all.

## 4. Stress tests and prior-art boundary

The first stress test is the exact quadratic control `x(n)=n^2/2`. Equations (9)--(21) are unchanged, because they use only the trivial bound on `S_X` in the resonant range. Therefore `RE-098` is **not** evidence that the CA deformation itself supplies extra cancellation; it only proves that near-resonant zero energy is already quantitatively strong enough.

The second stress test is (27)--(29). It prevents an invalid leap from `N^*` to the complete fourth moment. The unit-scale additive energy controls every fixed translated unit window by Cauchy, but paying for all shifts destroys the gain and returns to `vartheta>1/2`. Any successful argument must use information that couples the shift `Omega` to the oscillatory sample kernel.

The closest prior art remains Bazzanella, *Prime Numbers in Intervals Starting at a Fixed Power of the Integers* (J. Aust. Math. Soc. **87** (2009), 83--99, DOI `10.1017/S1446788709000020`). Its fourth-moment calculation explicitly splits the four-zero combination into a near-resonant term controlled by `N^*(sigma,T)` and a complementary term controlled by exponential-sum technology. The estimates (10)--(11) are the same Heath-Brown bounds used there. The original source is D. R. Heath-Brown, *Zero Density Estimates for the Riemann Zeta-Function and Dirichlet L-Functions*, J. London Math. Soc. (2) **19** (1979), 221--232, DOI `10.1112/jlms/s2-19.2.221`.

The line-specific content here is the splice with the Robin exponent law of `RE-095`: optimizing the resonant condition gives the exact threshold (15), and comparing it with `73/200` proves that the existing zero-energy input already crosses the only interval window needed to improve the `173/200` Robin frontier. No priority claim is made for the additive-energy estimates or for Bazzanella's fourth-moment decomposition. `SOURCES.md` already anchors Bazzanella as the load-bearing sparse-start source, so no new durable dependency is required by this finding.

## 5. Research consequence

`RE-097` left several plausible analytic resources bundled together: fourth moments, zero additive energy, and the deformed-quadratic phase. `RE-098` separates them. **Ordinary near-resonant four-zero energy is not the bottleneck.** It already has enough exponent room:

\[
0.3412164221\ldots
<
\frac{73}{200}.
\tag{31}
\]

The next theorem target should therefore be formulated directly in terms of (24): obtain a power-saving weighted bound for the shifted zero quartets over

\[
1<|\Omega|\ll X^{1-\vartheta+o(1)}
\]

against

\[
S_X(\Omega)=\sum_{n\asymp X^{1/2}}e^{i\Omega\log x(n)}.
\]

That target is substantially narrower than "improve primes near deformed squares". It asks for a specific shifted-additive-energy/oscillatory-kernel estimate, and it identifies exactly where the CA phase stability from `RE-096` must enter if the fourth-moment route is to lower the `173/200` frontier.