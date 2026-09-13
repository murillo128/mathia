# RE-100 — second-moment sampling pushes the sparse-host bottleneck past four fifths

**Status:** `EXACT-DERIVED + DEFORMED-QUADRATIC-SPARSE-HOSTS + SECOND-MOMENT-LARGE-SIEVE + ZERO-DENSITY-SPLICE + GUTH-MAYNARD + BOURGAIN-DENSITY-HYPOTHESIS + FOUR-FIFTHS-BOTTLENECK-RELOCATION + FOURTH-MOMENT-STRESS-TEST + PRIOR-ART-AUDITED`.

`RE-098` and `RE-099` isolate a genuine obstruction inside the direct **fourth-moment** route for the residual mixed first/depth-two Robin channel. Near-resonant four-zero energy is already strong enough below the Robin window, but a high-shift fourth moment that separates the sample kernel from the zero quartets has a `3/8` floor. That left the critical real-part slab `sigma=1/2` looking like the natural source of the obstruction.

It is not. The same deformed-quadratic sample admits a direct **second-moment** estimate by the trigonometric large sieve. Combined with current zero-density bounds, this gives a polynomial saving in the number of bad sampled hosts uniformly through a real-part range extending strictly beyond `4/5`. More precisely, for every fixed

\[
\boxed{
\frac{1901}{5216}<\vartheta<\frac{73}{200}
}
\tag{1}
\]

and every fixed

\[
\boxed{
\sigma_0<\sigma_*(\vartheta)
:=\frac{6\vartheta-1}{4\vartheta},
}
\tag{2}
\]

the contribution of all explicit-formula slabs `1/2<=sigma<=sigma_0` to the bad-host set is

\[
\boxed{
O\!\left(X^{1/2-\delta}\right)
}
\tag{3}
\]

for some `delta=delta(vartheta,sigma_0)>0`. The interval (1) is nonempty because

\[
\frac{73}{200}-\frac{1901}{5216}
=\frac{71}{130400}>0,
\tag{4}
\]

and at the limiting Robin endpoint

\[
\sigma_*\!\left(\frac{73}{200}\right)
=\frac{119}{146}
=0.8150684931\ldots>\frac45.
\tag{5}
\]

Thus the unresolved sparse-host theorem no longer needs a new shifted-quartet estimate on the critical line, nor anywhere below roughly `0.814`--`0.815` in real part. The genuine residual analytic difficulty is the **high-beta tail** above that range. This also changes the interpretation of `RE-099`: its `3/8` floor is a real fourth-moment architectural obstruction, but not a barrier to the sparse-host target itself.

## 1. The deformed CA sample is a large-sieve sampling set

Keep the notation of `RE-096`--`RE-099`:

\[
M=X^{1/2},\qquad
H=X^\vartheta,\qquad
T=\frac XH(\log X)^3=X^{1-\vartheta+o(1)},
\tag{6}
\]

and

\[
t_n:=\log x(n),
\qquad
x(n)=\eta_1^{-1}(\eta_2(n)),
\qquad n\asymp M.
\tag{7}
\]

`RE-096` proves

\[
\frac d{dn}\log x(n)
=\frac2n\left(1+O((\log n)^{-2})\right).
\tag{8}
\]

Hence, on every fixed bounded-ratio host shell,

\[
|t_n-t_m|\gg \frac{|n-m|}{M},
\tag{9}
\]

while the full `t_n` range has bounded length. Splitting that bounded interval into `O(1)` subintervals shorter than `2pi` if necessary, the points `t_n/(2pi)` are separated modulo one by `gg M^(-1)`. This is exactly the geometry required by the trigonometric large sieve.

Fix a real-part slab of width `1/log X`, beginning at `sigma`, and write

\[
Z_\sigma(t)
:=
\sum_{\substack{|\gamma|\le T\\
\beta\ \mathrm{in\ the\ slab}}}
 e^{i\gamma t}.
\tag{10}
\]

The coefficients in the explicit formula vary only by logarithmic factors inside one slab and are already absorbed into the `X^{o(1)}` bookkeeping used in `RE-098`. The only issue for a second moment is that the ordinates `gamma` are not separated. Bin them into unit intervals. If `B_j` is the number of slab zeros with

\[
j\le\gamma<j+1,
\tag{11}
\]

then the Riemann--von Mangoldt formula gives uniformly

\[
B_j\ll\log T.
\tag{12}
\]

On one bounded `t`-subinterval, write `gamma=j+u`, `0<=u<1`, and expand `e^{iu(t-t_0)}` into its absolutely convergent Taylor series. Applying the trigonometric large sieve to the integer frequencies `j` term by term, then summing the Taylor tail, gives

\[
\sum_{n\asymp M}|Z_\sigma(t_n)|^2
\ll
(T+M)\sum_j B_j^2\,X^{o(1)}.
\tag{13}
\]

By (12),

\[
\sum_jB_j^2
\le
\left(\max_jB_j\right)\sum_jB_j
\ll
N(\sigma,T)\,T^{o(1)}.
\tag{14}
\]

Since `vartheta<1/2`, equation (6) has `T>>M`, and therefore

\[
\boxed{
\sum_{n\asymp M}|Z_\sigma(t_n)|^2
\ll
T\,N(\sigma,T)\,X^{o(1)}.
}
\tag{15}
\]

No fourth moment, additive energy, or pointwise estimate for the CA phase kernel is used here.

## 2. Bad-host Markov gives a simple zero-density exponent law

The explicit-formula reduction in `RE-098` says that a bad sampled host forces at least one real-part slab to contribute at the scale of the missing interval mass. For a slab beginning at `sigma`, after the same harmless logarithmic losses, this means

\[
|Z_\sigma(t_n)|
\ge X^{1-\sigma-o(1)}.
\tag{16}
\]

Second-moment Markov and (15) therefore give

\[
\boxed{
\#\mathcal Z_{\vartheta,\sigma}(X)
\ll
X^{2\sigma-2+o(1)}T\,N(\sigma,T).
}
\tag{17}
\]

Write a zero-density estimate in the standard form

\[
N(\sigma,T)
\ll
T^{A(\sigma)(1-\sigma)+o(1)}.
\tag{18}
\]

Substituting `T=X^(1-vartheta+o(1))`, the host-count exponent in (17) is

\[
E_2(\sigma,\vartheta)
=
2\sigma-2
+(1-\vartheta)
\left(1+A(\sigma)(1-\sigma)\right).
\tag{19}
\]

Thus a fixed polynomial saving below the trivial `M=X^(1/2)` host count follows whenever

\[
E_2(\sigma,\vartheta)<\frac12.
\tag{20}
\]

At the critical slab itself, `N(1/2,T)=T^{1+o(1)}`, so (17) becomes

\[
\boxed{
\#\mathcal Z_{\vartheta,1/2}(X)
\ll
X^{1-2\vartheta+o(1)}.
}
\tag{21}
\]

At the Robin endpoint `vartheta=73/200`, the exponent is only

\[
1-2\cdot\frac{73}{200}
=\frac{27}{100}=0.27,
\tag{22}
\]

far below `1/2`. The critical line therefore has abundant room; the `3/8` phenomenon in `RE-099` comes from insisting on a fourth moment there, not from the sampled-host geometry itself.

## 3. Guth--Maynard controls the whole lower strip up to the Bourgain handoff

Guth--Maynard's current zero-density bound can be written

\[
A(\sigma)
\le
\frac{15}{3+5\sigma}
\qquad(1/2<\sigma<1),
\tag{23}
\]

with the bound outside its genuinely new middle range also following from the classical Ingham/Huxley estimates. Inserting (23) into (20), the threshold for `vartheta` is

\[
\vartheta>
G_{\rm GM}(\sigma)
:=
1-
\frac{\frac52-2\sigma}
{1+\frac{15(1-\sigma)}{3+5\sigma}}.
\tag{24}
\]

On the range relevant here the right-hand side is increasing beyond the Ingham--Guth--Maynard crossover, so its maximum on

\[
\frac12\le\sigma\le\frac{25}{32}
\]

occurs at `sigma=25/32`. Direct substitution gives

\[
\boxed{
G_{\rm GM}\!\left(\frac{25}{32}\right)
=
\frac{1901}{5216}
=0.3644555214\ldots .
}
\tag{25}
\]

This is already strictly below the Robin requirement `73/200=0.365`, by exactly (4). Consequently every fixed `vartheta` in (1) controls **all** slabs up to `25/32` with a uniform positive host saving.

The numerical closeness of (25) to the Robin endpoint is real, but the conclusion is robust: `vartheta` is fixed before `X->infinity`, so any strict choice in (1) leaves a fixed positive exponent margin.

## 4. Bourgain's density-hypothesis range pushes the handoff beyond `4/5`

Bourgain proved the density hypothesis

\[
A(\sigma)\le2
\tag{26}
\]

for

\[
\sigma\ge\frac{25}{32}.
\tag{27}
\]

With (26), condition (20) simplifies exactly to

\[
\vartheta>
\frac{1}{2(3-2\sigma)}.
\tag{28}
\]

For fixed `vartheta`, equality in (28) occurs at

\[
\boxed{
\sigma_*(\vartheta)
=
\frac{6\vartheta-1}{4\vartheta}.
}
\tag{29}
\]

Therefore every compact slab range

\[
\frac{25}{32}\le\sigma\le\sigma_0<\sigma_*(\vartheta)
\]

also contributes only `O(X^(1/2-delta))` bad hosts. Combining this with Section 3 proves (1)--(3).

At the bottom of the admissible `vartheta` window,

\[
\sigma_*\!\left(\frac{1901}{5216}\right)
=
\frac{3095}{3802}
=0.8140452393\ldots,
\tag{30}
\]

while as `vartheta` approaches `73/200` from below, (5) gives `119/146=0.815068...`. So the second-moment argument relocates the unresolved beta range to roughly

\[
\boxed{
\beta\gtrsim0.814.
}
\tag{31}
\]

This is a much smaller target than the full critical strip treated by the fourth-moment bookkeeping of `RE-098`--`RE-099`.

## 5. Why the fourth-moment `3/8` floor remains a real method obstruction

The second-moment escape does not invalidate `RE-099`. It shows instead that the obstruction there is specific to the fourth-moment architecture. Indeed, the strongest generic Hilbert-space coupling of the fourth moment still reproduces the same floor.

Write

\[
|Z_\sigma(t)|^2
=
\sum_{\rho_1,\rho_2}
 e^{i(\gamma_1-\gamma_2)t}.
\tag{32}
\]

Bin the pair differences `gamma_1-gamma_2` into unit intervals and apply exactly the same Taylor-plus-large-sieve argument as in Section 1 to the polynomial (32). The squared bin occupancies count four-zero additive coincidences, so

\[
\boxed{
\sum_{n\asymp M}|Z_\sigma(t_n)|^4
\ll
(T+M)N^*(\sigma,T)X^{o(1)}.
}
\tag{33}
\]

At `sigma=1/2`, the Heath-Brown bound used in `RE-098` has

\[
N^*(1/2,T)\ll T^{3+o(1)}.
\tag{34}
\]

Since `T>>M`, fourth-moment Markov yields

\[
\#\mathcal Z_{\vartheta,1/2}(X)
\ll
X^{-2}T^{4+o(1)}
=
X^{2-4\vartheta+o(1)}.
\tag{35}
\]

Beating `X^(1/2)` again requires exactly

\[
\vartheta>\frac38.
\tag{36}
\]

So even a genuinely coupled large-sieve treatment of the ordinary four-zero energy does **not** improve the `RE-099` critical fourth-moment exponent. This is not because the known exponent in (34) is loose at power scale. If `N=N(1/2,T)=T^{1+o(1)}`, the `N^2` ordered pairs occupy only `O(T)` unit sum/difference bins, and Cauchy gives

\[
N^*(1/2,T)
\gg
\frac{N^4}{T}
=T^{3-o(1)}.
\tag{37}
\]

Thus the power `3` is forced combinatorially on the critical line.

There is also a matched synthetic control showing that the extra factor `T` in (33) cannot be replaced generically by `M`. Let `T=KM`, take equally spaced frequencies `gamma_r=2pi r/L`, `1<=r<=T`, and sample points `t_n=Ln/M`, `0<=n<M`, on a fixed interval of length `L`. Then

\[
\sum_{r=1}^{T}e^{i\gamma_rt_n}
=
\begin{cases}
T,&n=0,\\
0,&1\le n<M,
\end{cases}
\tag{38}
\]

while the corresponding unit-scale four-frequency additive energy is `Theta(T^3)`. Hence

\[
\sum_n|Z(t_n)|^4=T^4
\asymp T\,N^*.
\tag{39}
\]

The control is not a model of zeta zeros; it is a falsification test for any claim that sample separation, bounded physical `t`-length, and ordinary four-frequency energy alone remove the full bandwidth factor. They do not.

## 6. Prior-art boundary and research consequence

The trigonometric large sieve used in (13) and (33) is classical; no novelty is claimed for that inequality. Montgomery--Vaughan's large-sieve work is the relevant primary source. The zero-density inputs are likewise external: Guth--Maynard supply (23), while Bourgain supplies the density-hypothesis range (26)--(27). Bazzanella remains the closest sparse-start precedent, but its direct branch is organized around a fourth moment, a low/high quartet-shift split, and pointwise exponential-sum estimates. The line-specific result here is the splice of the **second-moment large sieve on the exact CA sample** with the `RE-095` Robin host-count target and the current zero-density exponents.

The consequence is a genuine redirect. `RE-099` correctly says that a fourth-moment proof cannot cross the Robin window by improving the pointwise CA phase kernel alone. But the next theorem no longer needs to repair that fourth moment across the whole critical strip. A hybrid proof can use the second moment for

\[
\frac12\le\beta<\sigma_*(\vartheta)
\]

and reserve shifted-quartet/oscillatory-kernel machinery only for the high-beta tail

\[
\boxed{
\beta\ge\sigma_*(\vartheta)\approx0.814\text{--}0.815.
}
\tag{40}
\]

That is now the sharper analytic frontier. The most discriminating next calculation is therefore not another global fourth-moment estimate. It is to re-optimize the high-shift branch **only on the residual beta tail**, where zero density is already much thinner, and determine whether the existing exponent-pair/shifted-energy inputs overlap the second-moment range. If they do not, the missing theorem can be stated on that narrow tail rather than on all zeta zeros.