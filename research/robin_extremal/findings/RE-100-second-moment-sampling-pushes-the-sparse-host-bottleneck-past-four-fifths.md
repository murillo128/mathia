# RE-100 — second-moment sampling pushes the sparse-host bottleneck past four fifths

**Status:** `EXACT-DERIVED + DEFORMED-QUADRATIC-SPARSE-HOSTS + EXPLICIT-FORMULA-INTEGRAL + SECOND-MOMENT-LARGE-SIEVE + ZERO-DENSITY-SPLICE + INGHAM + GUTH-MAYNARD + BOURGAIN-DENSITY-HYPOTHESIS + FOUR-FIFTHS-BOTTLENECK-RELOCATION + FOURTH-MOMENT-STRESS-TEST + PRIOR-ART-AUDITED`.

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

the contribution of all explicit-formula slabs `1/2<=sigma<=sigma_0` to the bad-host set is

\[
\boxed{
O\!\left(X^{1/2-\delta}\right)
}
\tag{3}

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

Thus the unresolved sparse-host theorem no longer needs a new shifted-quartet estimate on the critical line, nor anywhere below roughly `0.814`--`0.815` in real part. The genuine residual analytic difficulty is the **high-beta tail** above that range. This also changes the interpretation of `RE-099`: its `3/8` floor is a real fourth-moment architectural obstruction, but not a barrier to the sparse-host target itself.

## 1. The exact explicit-formula slab is compatible with large-sieve sampling

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

`RE-096` proves

\[
\frac d{dn}\log x(n)
=\frac2n\left(1+O((\log n)^{-2})\right).
\tag{8}

Hence, on every fixed bounded-ratio host shell,

\[
|t_n-t_m|\gg \frac{|n-m|}{M},
\tag{9}

while the full `t_n` range has bounded length. The same remains true uniformly after replacing `x(n)` by `x(n)+u` with `|u|<=H`, because `H=o(X^(1/2))` whereas consecutive physical sample points are separated by `asymp X^(1/2)`. Splitting the bounded logarithmic range into `O(1)` intervals shorter than `2pi` if necessary, the normalized sample points are separated modulo one by `gg M^(-1)`.

Fix a real-part slab

\[
I_\sigma=
\left[\sigma,\sigma+\frac1{\log X}\right]
\tag{10}

and write its exact right-interval explicit-formula contribution as

\[
F_\sigma(n)
:=
\sum_{\substack{|\gamma|\le T\\\beta\in I_\sigma}}
\frac{(x(n)+H)^\rho-x(n)^\rho}{\rho}
=
\int_0^H
\sum_{\substack{|\gamma|\le T\\\beta\in I_\sigma}}
(x(n)+u)^{\rho-1}\,du.
\tag{11}

The left interval is identical after integrating over `-H<=u<=0`, so it is enough to treat (11). For fixed `u`, put

\[
t_{n,u}=\log(x(n)+u).
\tag{12}

After factoring the harmless shell-scale factor `X^(sigma-1)`, the inner sum is

\[
\sum_{\beta\in I_\sigma}
 e^{(\beta-\sigma)t_{n,u}}e^{i\gamma t_{n,u}}.
\tag{13}

The ordinates are not separated, so bin them into unit intervals. If `B_j` is the number of slab zeros with `j<=gamma<j+1`, the Riemann--von Mangoldt formula gives uniformly

\[
B_j\ll\log T.
\tag{14}

On one bounded `t`-subinterval write `t=t_0+v`, `gamma=j+r` with `0<=r<1`. Since also `0<=beta-sigma<=1/log X`, expand

\[
e^{((\beta-\sigma)+ir)v}
\tag{15}

in its absolutely convergent Taylor series. The coefficients at `t_0` have bounded modulus, and the `k`-th Taylor coefficient in a fixed frequency bin is bounded by `O(C^k B_j/k!)` for a shell-dependent absolute `C`. Applying the trigonometric large sieve to the integer frequencies `j` term by term and summing the convergent Taylor majorant yields, uniformly in `u`,

\[
\sum_{n\asymp M}
\left|
\sum_{\substack{|\gamma|\le T\\\beta\in I_\sigma}}
(x(n)+u)^{\rho-1}
\right|^2
\ll
X^{2\sigma-2}(T+M)
\sum_jB_j^2\,X^{o(1)}.
\tag{16}

By (14),

\[
\sum_jB_j^2
\le
\left(\max_jB_j\right)\sum_jB_j
\ll
N(\sigma,T)T^{o(1)}.
\tag{17}

Since `vartheta<1/2`, equation (6) has `T>>M`. Cauchy in the `u` integral of (11), followed by (16)--(17), therefore gives the exact slab second moment

\[
\boxed{
\sum_{n\asymp M}|F_\sigma(n)|^2
\ll
H^2X^{2\sigma-2}T\,N(\sigma,T)X^{o(1)}.
}
\tag{18}

This formulation avoids treating the explicit-formula coefficient `((1+H/x)^rho-1)/rho` as constant in `n`: its full dependence has been retained through the integral representation (11).

## 2. Bad-host Markov gives a simple zero-density exponent law

As in `RE-098`, the truncation error and the `O(log X)` real-part slabs are harmless at power scale. If a sampled interval is prime-free by the fixed proportion required in the bad-host definition, at least one slab has

\[
|F_\sigma(n)|\ge H X^{-o(1)}.
\tag{19}

Second-moment Markov and (18) therefore give

\[
\boxed{
\#\mathcal Z_{\vartheta,\sigma}(X)
\ll
X^{2\sigma-2+o(1)}T\,N(\sigma,T).
}
\tag{20}

Write a zero-density estimate in the standard form

\[
N(\sigma,T)
\ll
T^{A(\sigma)(1-\sigma)+o(1)}.
\tag{21}

Substituting `T=X^(1-vartheta+o(1))`, the host-count exponent in (20) is

\[
E_2(\sigma,\vartheta)
=
2\sigma-2
+(1-\vartheta)
\left(1+A(\sigma)(1-\sigma)\right).
\tag{22}

Thus a fixed polynomial saving below the trivial `M=X^(1/2)` host count follows whenever

\[
E_2(\sigma,\vartheta)<\frac12.
\tag{23}

At the critical slab itself, `N(1/2,T)=T^{1+o(1)}`, so (20) becomes

\[
\boxed{
\#\mathcal Z_{\vartheta,1/2}(X)
\ll
X^{1-2\vartheta+o(1)}.
}
\tag{24}

At the Robin endpoint `vartheta=73/200`, the exponent is only

\[
1-2\cdot\frac{73}{200}
=\frac{27}{100}=0.27,
\tag{25}

far below `1/2`. The critical line therefore has abundant room; the `3/8` phenomenon in `RE-099` comes from insisting on a fourth moment there, not from the sampled-host geometry itself.

## 3. Ingham and Guth--Maynard control the lower strip below the Bourgain handoff

For the lower half of the strip, use Ingham's classical density estimate

\[
A(\sigma)\le\frac{3}{2-\sigma}
\qquad\left(\frac12\le\sigma\le\frac7{10}\right).
\tag{26}

Substitution into (23) simplifies the threshold exactly to

\[
\boxed{\vartheta>\frac\sigma2.}
\tag{27}

Its maximum on this range is only `7/20=0.35`.

For

\[
\frac7{10}\le\sigma\le\frac{25}{32},
\]

use the Guth--Maynard zero-density bound in the convenient form

\[
A(\sigma)
\le
\frac{15}{3+5\sigma}.
\tag{28}

Inserting (28) into (23), the threshold becomes

\[
\vartheta>
G_{\rm GM}(\sigma)
:=
1-
\frac{\frac52-2\sigma}
{1+\frac{15(1-\sigma)}{3+5\sigma}}.
\tag{29}

The right-hand side is increasing on `[7/10,25/32]`, so its maximum occurs at `sigma=25/32`. Direct substitution gives

\[
\boxed{
G_{\rm GM}\!\left(\frac{25}{32}\right)
=
\frac{1901}{5216}
=0.3644555214\ldots .
}
\tag{30}

This is strictly below the Robin requirement `73/200=0.365`, by exactly (4), and it dominates the Ingham-side maximum `7/20`. Consequently every fixed `vartheta` in (1) controls **all** slabs from `1/2` through `25/32` with a uniform positive host saving. The numerical margin is narrow but genuine: `vartheta` is fixed before `X->infinity`, so every strict choice in (1) leaves a fixed positive exponent gap.

## 4. Bourgain's density-hypothesis range pushes the handoff beyond `4/5`

Bourgain proved the density hypothesis

\[
A(\sigma)\le2
\tag{31}

for

\[
\sigma\ge\frac{25}{32}.
\tag{32}

With (31), condition (23) simplifies exactly to

\[
\vartheta>
\frac{1}{2(3-2\sigma)}.
\tag{33}

For fixed `vartheta`, equality in (33) occurs at

\[
\boxed{
\sigma_*(\vartheta)
=
\frac{6\vartheta-1}{4\vartheta}.
}
\tag{34}

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
\tag{35}

while as `vartheta` approaches `73/200` from below, (5) gives `119/146=0.815068...`. So the second-moment argument relocates the unresolved beta range to roughly

\[
\boxed{
\beta\gtrsim0.814.
}
\tag{36}

This is a much smaller target than the full critical strip treated by the fourth-moment bookkeeping of `RE-098`--`RE-099`.

## 5. The fourth-moment `3/8` floor survives generic large-sieve coupling

The second-moment escape does not invalidate `RE-099`; it shows that its obstruction is specific to the fourth-moment architecture. The same exact-integral treatment gives a useful stress test.

For fixed `u`, square the zero sum in (13), bin the pair differences `gamma_1-gamma_2` into unit intervals, and apply the Taylor-plus-large-sieve argument to that pair-difference polynomial. The squared bin occupancies count four-zero additive coincidences. Jensen in the `u` integral of (11) then gives

\[
\boxed{
\sum_{n\asymp M}|F_\sigma(n)|^4
\ll
H^4X^{4\sigma-4}(T+M)
N^*(\sigma,T)X^{o(1)}.
}
\tag{37}

At `sigma=1/2`, the Heath-Brown bound used in `RE-098` has

\[
N^*(1/2,T)\ll T^{3+o(1)}.
\tag{38}

Since `T>>M`, fourth-moment Markov at the bad-host threshold `|F|>=HX^(-o(1))` yields

\[
\#\mathcal Z_{\vartheta,1/2}(X)
\ll
X^{-2}T^{4+o(1)}
=
X^{2-4\vartheta+o(1)}.
\tag{39}

Beating `X^(1/2)` again requires exactly

\[
\vartheta>\frac38.
\tag{40}

So even a genuinely coupled large-sieve treatment of the ordinary four-zero energy does not improve the `RE-099` critical fourth-moment exponent. This is not because the known exponent in (38) is loose at power scale. If `N=N(1/2,T)=T^(1+o(1))`, the `N^2` ordered pairs occupy only `O(T)` unit sum/difference bins, and Cauchy gives

\[
N^*(1/2,T)
\gg
\frac{N^4}{T}
=T^{3-o(1)}.
\tag{41}

Thus the power `3` is forced combinatorially on the critical line.

There is also a matched synthetic control showing that the extra factor `T` in (37) cannot be replaced generically by `M`. Let `T=KM`, take equally spaced frequencies `gamma_r=2pi r/L`, `1<=r<=T`, and sample points `t_n=Ln/M`, `0<=n<M`, on a fixed interval of length `L`. Then

\[
\sum_{r=1}^{T}e^{i\gamma_rt_n}
=
\begin{cases}
T,&n=0,\\
0,&1\le n<M,
\end{cases}
\tag{42}

while the corresponding unit-scale four-frequency additive energy is `Theta(T^3)`. Hence

\[
\sum_n|Z(t_n)|^4=T^4
\asymp T\,N^*.
\tag{43}

The control is not a model of zeta zeros; it is a falsification test for any claim that sample separation, bounded logarithmic range, and ordinary four-frequency energy alone remove the full bandwidth factor. They do not.

## 6. Prior-art boundary and research consequence

The trigonometric large sieve used above is classical; no novelty is claimed for that inequality. Montgomery--Vaughan's large-sieve work is the relevant primary source. The zero-density inputs are likewise external: Ingham supplies (26), Guth--Maynard supplies (28), and Bourgain supplies the density-hypothesis range (31)--(32). Bazzanella remains the closest sparse-start precedent, but its direct branch is organized around a fourth moment, a low/high quartet-shift split, and pointwise exponential-sum estimates. The line-specific result here is the splice of the **second-moment large sieve on the exact CA-deformed sample** with the `RE-095` Robin host-count target and the current zero-density exponents.

The consequence is a genuine redirect. `RE-099` correctly says that a fourth-moment proof cannot cross the Robin window by improving the pointwise CA phase kernel alone. But the next theorem no longer needs to repair that fourth moment across the whole critical strip. A hybrid proof can use the second moment for

\[
\frac12\le\beta<\sigma_*(\vartheta)
\]

and reserve shifted-quartet/oscillatory-kernel machinery only for the high-beta tail

\[
\boxed{
\beta\ge\sigma_*(\vartheta)\approx0.814\text{--}0.815.
}
\tag{44}

That is now the sharper analytic frontier. The most discriminating next calculation is not another global fourth-moment estimate. It is to re-optimize the high-shift branch **only on the residual beta tail**, where zero density is already much thinner, and determine whether the existing exponent-pair/shifted-energy inputs overlap the second-moment range. If they do not, the missing theorem can be stated on that narrow tail rather than on all zeta zeros.