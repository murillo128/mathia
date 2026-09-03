# XF-012 — near-endpoint gap moments recover the `h^2` scale with a logarithmic Hilbert loss

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `BOUNDARY/OBSTRUCTION`. XF-011 identified a fixed-`p` tradeoff: the raw adjacent-gap moment has size `h^{2p}`, while strong control of the Cauchy driver through the Hilbert transform is available only for `p>1`; at `p=1` the raw signal reaches `h^2` but the strong `L^1` bound fails. Allowing the exponent itself to approach one with height changes that conclusion quantitatively. A variable exponent

\[
p_h=1+\frac{c}{\log(1/h)},\qquad c>0,
\]

keeps the raw local moment at the same **power scale** `h^2` as total variation, losing only the constant factor `e^{-2c}`, while the sharp Hilbert-transform constant grows only like `log(1/h)`. At Xi height `T`, this becomes a `log^{-2} T` raw signal with only a `log log T` operator loss.

The logarithmic loss is unavoidable within this `L^p` route if one insists that the raw moment remain a fixed positive fraction of the `h^2` scale. Thus the fixed-`p` power-scale obstruction in XF-011 is not uniform as `p -> 1+`; the true near-endpoint frontier is **power-scale recovery versus logarithmic operator degeneration**.

## 1. Claim

Use the notation of XF-011. For a periodic relative gap perturbation sampled on the mesoscopic Xi lattice,

\[
u_j=U(h^2j),\qquad h^2=\frac{2\pi}{N},
\]

with nonconstant `U in C^2(T)`, define

\[
M_{p,h}(u):=\frac1N\sum_{j=0}^{N-1}|u_{j+1}-u_j|^p.
\tag{1}
\]

Let

\[
L_h:=\log(1/h),\qquad p_h:=1+\frac{c}{L_h},\qquad c>0.
\tag{2}
\]

Then as `h -> 0`,

\[
\boxed{
M_{p_h,h}(u)
=e^{-2c}h^2
\left(
\frac1{2\pi}\int_0^{2\pi}|U'(X)|\,dX
+o(1)
\right).
}
\tag{3}
\]

Thus the raw `p_h`-moment has the same `h^2` power scale as the `p=1` total-variation statistic.

For the periodic Hilbert transform `H`, Pichorides' sharp theorem gives, for `1<p<=2`,

\[
\|\mathcal H f\|_{L^p}
\le C_p\|f\|_{L^p},
\qquad
C_p=\tan\!\left(\frac{\pi}{2p}\right).
\tag{4}
\]

Since `|D|U=H U'`, equation (2) implies

\[
\boxed{
C_{p_h}
=\frac{2}{\pi c}L_h+O(1).
}
\tag{5}
\]

Hence

\[
\boxed{
\||D|U\|_{L^{p_h}}
\le
\left(\frac{2}{\pi c}L_h+O(1)\right)
\|U'\|_{L^{p_h}}.
}
\tag{6}
\]

On the normalized circle, `||f||_1 <= ||f||_p`, so the same right-hand side also controls `|| |D|U||_1`. The price for retaining `h^2` raw visibility is therefore logarithmic, not a new power of `h`.

## 2. Uniform variable-exponent asymptotic

Write `delta=h^2`. Taylor expansion gives uniformly in the lattice index

\[
U(X+\delta)-U(X)
=\delta U'(X)+O(\delta^2).
\tag{7}
\]

For all sufficiently small `h`, equation (2) places `p_h` in a fixed compact interval, say `[1,3/2]`. On bounded sets the maps `x -> |x|^p` are uniformly Lipschitz for `p` in that interval away from no point that matters here: by the mean-value bound

\[
\big||a|^p-|b|^p\big|
\le p\,\max(|a|,|b|)^{p-1}|a-b|,
\tag{8}
\]

and the factor `max(|a|,|b|)^{p-1}` stays uniformly bounded for the fixed smooth profile. Therefore the finite-difference error and the periodic Riemann-sum error are uniform as `p_h -> 1`, and

\[
M_{p_h,h}(u)
=h^{2p_h}
\left(
A_{p_h}(U)+o(1)
\right),
\qquad
A_p(U):=\frac1{2\pi}\int|U'|^p.
\tag{9}
\]

Because `p_h -> 1`, dominated convergence gives

\[
A_{p_h}(U)\to A_1(U)>0.
\tag{10}
\]

Finally,

\[
h^{2p_h}
=h^2\exp\!\left(2(p_h-1)\log h\right)
=h^2e^{-2c},
\tag{11}
\]

which proves (3). No fixed-`p` asymptotic is being extrapolated beyond its range; the dependence on `p_h` is controlled uniformly.

## 3. The logarithmic loss is the sharp order for preserving an `h^2` raw moment

More generally let

\[
p_h=1+\varepsilon_h,
\qquad
\varepsilon_h\downarrow0.
\]

The same argument gives

\[
\frac{M_{p_h,h}(u)}{h^2}
=
\exp(-2\varepsilon_hL_h)
\left(A_1(U)+o(1)\right).
\tag{12}
\]

Suppose the raw moment is required to retain a fixed positive fraction of the `h^2` scale along the limit, i.e. for some `a>0`,

\[
M_{p_h,h}(u)\ge a h^2
\]

for all sufficiently small `h`. Since `A_1(U)>0`, equation (12) forces

\[
\varepsilon_hL_h=O(1).
\tag{13}
\]

But Pichorides' sharp constant satisfies

\[
C_p
=\tan\!\left(\frac{\pi}{2p}\right)
=\frac{2}{\pi(p-1)}+O(1)
\qquad(p\downarrow1).
\tag{14}
\]

Combining (13) and (14) yields

\[
\boxed{
C_{p_h}=\Omega(L_h)
}
\tag{15}
\]

for every near-endpoint `L^p` scheme that preserves a constant-order `h^2` raw moment. The choice `p_h=1+c/L_h` attains this order by (5), so the `Theta(log(1/h))` loss is optimal within this precise tradeoff.

Conversely, forcing `C_{p_h}=o(L_h)` requires `p_h-1 >> 1/L_h`; then `\varepsilon_hL_h -> infinity`, and (12) gives

\[
\frac{M_{p_h,h}(u)}{h^2}\to0.
\tag{16}
\]

Thus one cannot make the Hilbert-transform constant sublogarithmic while keeping the raw adjacent-gap moment at a fixed fraction of the `h^2` scale.

## 4. Translation to Xi height

XF-008 gives the high-zero spacing

\[
h_T\sim\frac{4\pi}{\log T}.
\tag{17}
\]

Therefore

\[
L_{h_T}
=\log\frac1{h_T}
=\log\log T+O(1).
\tag{18}
\]

Choose

\[
p_T
=1+\frac{c}{\log(1/h_T)}.
\tag{19}
\]

Then equations (3) and (5) become

\[
\boxed{
M_{p_T,h_T}(u)
=\Theta\!\left(\frac1{\log^2T}\right),
\qquad
C_{p_T}
=\Theta(\log\log T).
}
\tag{20}
\]

The first relation is at exactly the power scale of the `R-2` equilibrium defect from XF-008. The second says that the price of using an exponent for which the Hilbert transform is strongly bounded need only be iterated-logarithmic in height.

This materially sharpens the information-interface diagnosis of XF-011. A theorem capable of resolving a variable-exponent adjacent-gap moment near `p=1+Theta(1/log log T)` would not need `log^{-2p}T` precision for any fixed `p>1`; it would need `log^{-2}T` power precision together with enough quantitative room to absorb a `log log T` loss.

## 5. Prior art and novelty boundary

The boundedness of the conjugate/Hilbert transform on `L^p`, `1<p<infinity`, is classical M. Riesz theory and was already anchored for XF-011. The exact best constant used here is due to S. K. Pichorides, **On the best values of the constants in the theorem of M. Riesz, Zygmund and Kolmogorov**, *Studia Mathematica* 44:2 (1972), 165–179, DOI `10.4064/sm-44-2-165-179`. For the periodic Hilbert transform it gives `tan(pi/(2p))` on `1<p<=2` and the dual `cot(pi/(2p))` formula on `2<=p<infinity`.

No novelty is claimed for Pichorides' norm, its `1/(p-1)` endpoint blowup, variable-exponent limits as an abstract analytic device, or the elementary asymptotic `h^{2p_h}`. The Mathia-specific result is their exact combination with the Xi-flow scaling already established in XF-008 and the adjacent-gap Lyapunov/statistical interface of XF-011. It shows that the apparent fixed-`p` power loss has a near-endpoint escape, and identifies the unavoidable replacement cost as `Theta(log log T)` at Xi height.

A targeted prior-art search for de Bruijn–Newman zero dynamics combined with Pichorides/Hilbert-transform near-endpoint gap observables did not identify an existing formulation of this scale tradeoff. That absence is not used as evidence of novelty; the durable claim consists only of the derived asymptotics and boundary above.

## 6. Falsification controls and remaining boundary

This does **not** supply an upper bound for `Lambda`. The discrete `W^{1,p}` contraction in XF-011 is a property of the universal arithmetic-lattice linearization and is shared by matched controls. The present exponent tuning inherits that universality and remains non-Xi-specific.

It also remains a linearized, real-ordered-gap statement. Under a hypothetical positive `Lambda`, one still cannot assume that the relevant lower-time configuration is real merely to define consecutive gaps. Any upstream arithmetic input must be applied at a real-rooted time or reformulated in a configuration-level way that remains meaningful in the presence of nonreal zeros.

Finally, equation (20) is an information-scale target, not a theorem that current unconditional zero statistics control the required variable-exponent moment. A usable argument would need quantitative estimates uniform as `p_T -> 1`, with errors small enough to survive the `Theta(log log T)` Hilbert loss. If such uniformity fails, the route remains blocked at the statistical interface rather than at the Cauchy dynamics.

## 7. Consequence for `xi_flow`

The fixed-`p` dichotomy from XF-011 should no longer be read as “choose `p=1` and lose strong control, or choose `p>1` and pay a strictly finer power of `log T`.” There is an intermediate, asymptotically optimal `L^p` regime:

\[
p_T-1\asymp\frac1{\log\log T},
\]

for which the raw local statistic remains at the `log^{-2}T` scale while strong Hilbert-transform control costs only `log log T`.

The most concrete statistical target is therefore narrower: determine whether unconditional, real-rootedness-safe zero information can control adjacent-gap or configuration-level analogues of these **near-endpoint variable-exponent moments** with an error budget better than the `log log T` loss. A negative result would need to rule out this tuned regime, not merely fixed exponents `p>1`.