# NB-143 — xi-type entire realizability still permits sparse logarithmic confluence packets

**Status:** `EXACT-DERIVED + SOURCE-REALIZABILITY + XI-TYPE-ENTIRE-COMPLETION + RIEMANN-FUNCTIONAL-EQUATION + RIEMANN-VON-MANGOLDT-ENVELOPE + SELBERG-DENSITY-COMPATIBLE + VINOGRADOV-KOROBOV-COMPATIBLE + HAMBURGER-BOUNDARY + TARGET-AWARE-CONFLUENCE-SPLICE + DECISIVE-METHOD-BOUNDARY`.

`NB-141` left a real realizability gap in its matched control. It produced one zeta-symmetric synthetic divisor with sparse logarithmic-rank packets that survive the current zero-count, zero-density and zero-free envelopes, but explicitly did **not** assert that the divisor comes from an entire function with the analytic structure of `xi`. `NB-142` then identified the local source bill of such a packet: an order-`log G` positive short increment of the zero-count remainder.

The divisor gap can be closed without closing the Nyman obstruction. Fix

\[
0<a<\frac12,
\qquad
0<c<0.05038,
\qquad
B>c\log\!\left(\frac4a-3\right).
\tag{1}
\]

There exists a single entire function `Xi_*` of order exactly one such that

\[
\boxed{
\Xi_*(s)=\Xi_*(1-s),
\qquad
\Xi_*(\overline s)=\overline{\Xi_*(s)},
\qquad
\Xi_*(0)=\Xi_*(1)=\frac12,
}
\tag{2}
\]

whose nonreal zero divisor is simple, lies in `0<Re s<1`, has the standard critical-line bulk count, and contains infinitely many right-half packets

\[
\mathcal P_k
\subset
\left\{
\rho:
\left|\rho-\left(\frac12+a+iG_k\right)\right|
\le G_k^{-B}
\right\}
\tag{3}
\]

with

\[
|\mathcal P_k|=\lfloor c\log G_k\rfloor.
\tag{4}
\]

The positive-ordinate counting function `N_*(T)` can simultaneously satisfy, for every sufficiently large `T`, the same Bellotti--Wong envelope used throughout this line,

\[
\boxed{
\left|
N_*(T)-
\frac{T}{2\pi}\log\frac{T}{2\pi e}
\right|
\le
0.10076\log T
+0.24460\log\log T
+8.08344.
}
\tag{5}
\]

At the near-critical threshold

\[
\sigma_a:=\frac12+\frac a2,
\tag{6}
\]

the same divisor has only

\[
N_{*,>} (\sigma_a,T)=O(\log T)
\tag{7}
\]

right-half zeros, hence lies far below the Selberg density envelope used in `NB-116` and `NB-141`. Its fixed off-critical real part also remains compatible with the Vinogradov--Korobov zero-free region for all sufficiently large heights.

Define from `Xi_*`

\[
\boxed{
Z_*(s)
:=
\frac{2\pi^{s/2}\Xi_*(s)}
{s(s-1)\Gamma(s/2)}.
}
\tag{8}
\]

Then `Z_*` has a simple pole at `s=1` of residue one, `Z_*(0)=-1/2`, simple trivial zeros at the negative even integers, no nontrivial zeros for `Re s>=1`, and satisfies the **exact standard zeta functional equation**

\[
\boxed{
\pi^{-s/2}\Gamma(s/2)Z_*(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)Z_*(1-s).
}
\tag{9}
\]

Moreover `(s-1)Z_*(s)` is entire of finite order.

Nevertheless every packet `(3)` lies in the `NB-140` confluence regime, so its complete simple-state span remains asymptotically target-poor:

\[
\boxed{
\frac{\|P_{\mathcal S_{G_k}^{\rm split}}e_{G_k}\|}
{\|e_{G_k}\|}
\longrightarrow0.
}
\tag{10}
\]

Thus adding an order-one `xi`-type entire completion and the exact zeta functional equation does **not** supply the missing local occupancy law. The first classical hypothesis in this direction that actually destroys the matched control is arithmetic rather than merely entire-function-theoretic: if `Z_*` also had a Dirichlet series absolutely convergent in `Re s>1`, Hamburger's converse theorem would force `Z_*=zeta`, which the construction explicitly avoids.

This is a zero-geometry realizability statement. `Z_*` is not claimed to be a replacement Nyman source, and its synthetic zeros do not become Nyman orthogonality zeros. The conclusion is narrower and exact: all `xi`-side analytic structure listed above is still compatible with the specific local zero geometry that defeats the present target argument.

## 1. A critical-line bulk with superlacunary right-half packets

Put

\[
M(T):=
\frac{T}{2\pi}\log\frac{T}{2\pi e}.
\tag{11}
\]

For all sufficiently large integers `n`, let `tau_n` be the unique solution of

\[
M(\tau_n)=n.
\tag{12}
\]

Use the simple critical-line baseline

\[
\rho_n^{(0)}=\frac12+i\tau_n
\tag{13}
\]

and its conjugate. After a finite initial adjustment, its positive-ordinate count satisfies

\[
N_0(T)=M(T)+O(1).
\tag{14}
\]

Choose heights `G_k->infinity` so rapidly that

\[
\sum_{j<k}\log G_j=o(\log G_k).
\tag{15}
\]

For example, `G_k=exp(exp(k^2))` is more than sufficient. Put

\[
d_k:=\lfloor c\log G_k\rfloor.
\tag{16}
\]

Choose pairwise-distinct real perturbations

\[
|\varepsilon_{j,k}|\le\frac12G_k^{-B},
\qquad 1\le j\le d_k,
\tag{17}
\]

and place the positive-ordinate quartet representatives

\[
\rho_{j,k}^{+}
=
\frac12+a+i(G_k+\varepsilon_{j,k}),
\qquad
\rho_{j,k}^{-}
=
\frac12-a+i(G_k+\varepsilon_{j,k}).
\tag{18}
\]

Include their complex conjugates. The perturbations may also be chosen so that at least one, and in fact every, `rho_(j,k)^+` avoids the actual zeta zero set. At each finite stage only a discrete set of ordinates is forbidden, while `(17)` contains a continuum of choices.

The positive-ordinate contribution of the `k`th off-critical packet and its functional-equation partner is `2d_k`. Therefore, uniformly for large `T`,

\[
N_*(T)-N_0(T)
\le
2\sum_{G_k\le T}d_k+O(1).
\tag{19}
\]

By `(15)`, if `G_m<=T<G_(m+1)`,

\[
2\sum_{k\le m}d_k
\le
(2c+o(1))\log G_m
\le
(2c+o(1))\log T.
\tag{20}
\]

Since `2c<0.10076`, equations `(14)` and `(20)` fit eventually inside `(5)` with a fixed positive margin. This verifies the same explicit zero-count envelope as `NB-141`, now for the zero divisor of one entire function constructed below.

At the threshold `(6)`, the critical-line baseline and the left partners do not contribute. Hence

\[
N_{*,>}(\sigma_a,T)
\le
\sum_{G_k\le T}d_k
=O(\log T),
\tag{21}
\]

which is much smaller than

\[
T^{1-a/8}\log T.
\tag{22}
\]

Finally, every off-critical zero has fixed real part `1/2+a` or `1/2-a`. The Bellotti Vinogradov--Korobov zero-free boundary tends to one, so `(18)` lies strictly to its left for all sufficiently large `k`. The three coarse source laws used in `NB-140`--`NB-142` therefore remain satisfied.

## 2. The prescribed divisor has an order-one xi-type canonical product

Center at the critical line by writing

\[
z=s-\frac12.
\tag{23}
\]

Let `Lambda_+` contain one centered coordinate `lambda=rho-1/2` for every positive-ordinate zero in the construction, including both members of `(18)`. The counting estimate `(5)` implies

\[
\#\{\lambda\in\Lambda_+:|\lambda|\le T\}
=O(T\log T).
\tag{24}
\]

Therefore

\[
\sum_{\lambda\in\Lambda_+}\frac1{|\lambda|^2}<\infty.
\tag{25}
\]

Indeed, the dyadic shell `2^m<|lambda|<=2^(m+1)` contains `O(2^m m)` points and contributes `O(m/2^m)` to `(25)`.

Consequently the paired product

\[
P(z)
:=
\prod_{\lambda\in\Lambda_+}
\left(1-\frac{z^2}{\lambda^2}\right)
\tag{26}
\]

converges locally uniformly and defines an entire even function. For a critical-line zero `lambda=i tau`, the factor in `(26)` is real on the real axis. For every right-half coordinate

\[
\lambda=a+i\gamma,
\tag{27}
\]

the left partner is

\[
-\overline\lambda=-a+i\gamma,
\tag{28}
\]

so the two corresponding factors are complex conjugates on real `z`. Hence

\[
P(\overline z)=\overline{P(z)},
\qquad
P(x)>0\quad(x\in\mathbb R).
\tag{29}
\]

The strict positivity follows because no prescribed zero is real and the logarithms of the paired factors converge absolutely at each fixed real `x` by `(25)`.

Normalize by

\[
C:=\frac1{2P(1/2)},
\qquad
\Xi_*(s):=C P\!\left(s-\frac12\right).
\tag{30}
\]

Equations `(26)`--`(30)` give `(2)` and exactly the prescribed nonreal zero divisor.

The order is exactly one. For `|z|=r`, the factors with `|lambda|<=2r` contribute at most

\[
O(r\log r)\,O(\log r)
=O(r(\log r)^2)
\tag{31}
\]

to `log M_P(r)`, while `(25)` and `(24)` give `O(r log r)` for the outer tail after the standard split of `log(1-z^2/lambda^2)`. Thus

\[
\log M_P(r)=O(r(\log r)^2),
\tag{32}
\]

so the order is at most one. Conversely the baseline alone gives `asymp r log r` zeros in `|z|<=r`; Jensen's formula rules out every order strictly below one. Hence

\[
\boxed{\operatorname{ord}(\Xi_*)=1.}
\tag{33}
\]

No external canonical-product theorem beyond the standard locally uniform product criterion is load-bearing here; the required summability and growth estimates are explicit in `(24)`--`(33)`.

## 3. The associated synthetic zeta has the exact gamma factor and functional equation

Define `Z_*` by `(8)`. Because `Xi_*(1)=1/2` and `Gamma(1/2)=sqrt(pi)`, one has

\[
Z_*(s)=\frac1{s-1}+O(1)
\qquad(s\to1),
\tag{34}
\]

so the residue is one. At the origin,

\[
\Gamma(s/2)=\frac2s+O(1),
\tag{35}
\]

and `Xi_*(0)=1/2`, hence

\[
Z_*(0)=-\frac12.
\tag{36}
\]

The reciprocal gamma factor has simple zeros at the nonpositive even integers. The zero at `s=0` is consumed by the removable singularity in `(8)`, while `Xi_*` has no real zeros, so the remaining negative even integers are simple trivial zeros of `Z_*`.

The completed function is

\[
\Lambda_*(s)
:=
\pi^{-s/2}\Gamma(s/2)Z_*(s)
=
\frac{2\Xi_*(s)}{s(s-1)}.
\tag{37}
\]

Both numerator and denominator are invariant under `s -> 1-s`; this proves `(9)` exactly. Since `Xi_*` has order one and both `1/Gamma(s/2)` and `pi^(s/2)` have finite order, `(s-1)Z_*(s)` is entire of finite order after the removable singularity at zero is filled in.

Thus the matched divisor can be promoted from the bookkeeping object of `NB-141` to a single meromorphic function carrying the standard zeta gamma factor, pole normalization, trivial zeros and functional equation.

## 4. Hamburger identifies the arithmetic structure that the control cannot also carry

The analytic realization above is deliberately not claimed to be a Dirichlet series. This is not merely an omitted construction; the classical Hamburger converse theorem shows that it is impossible.

Kaczorowski--Molteni--Perelli record Hamburger's theorem in the form needed here: if `f` and `g` are Dirichlet series absolutely convergent for `Re s>1`, if `(s-1)f(s)` and `(s-1)g(s)` are entire of finite order, and if

\[
\pi^{-s/2}\Gamma(s/2)f(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)g(1-s),
\tag{38}
\]

then

\[
f(s)=g(s)=C\zeta(s).
\tag{39}
\]

Suppose `Z_*` admitted such an absolutely convergent Dirichlet series. Taking

\[
f=g=Z_*
\tag{40}
\]

uses `(9)` and the finite-order continuation established above, so `(39)` would give

\[
Z_*=C\zeta.
\tag{41}
\]

The residue normalization at `s=1` forces `C=1`. But the perturbations in `(17)` were chosen so that `Z_*` vanishes at a point where the actual zeta function does not. This contradicts `(41)`.

Therefore

\[
\boxed{
Z_*\text{ has no Dirichlet-series expansion absolutely convergent in }\Re s>1.
}
\tag{42}
\]

The point of `(42)` is not to elevate the Dirichlet-series hypothesis into the final Nyman theorem. It identifies a precise realizability boundary. Entire continuation, order one, the standard gamma factor and functional equation still allow the dangerous packet; the ordinary integer Dirichlet-series structure does not.

This is also the correct prior-art boundary. Functional-equation nonuniqueness outside a Dirichlet-series class and Hamburger-type converse theorems are classical. The line-local contribution here is the splice with the quantitative `NB-140` confluence cell while preserving the explicit zero-count, density and zero-free envelopes already imported by the Nyman program.

## 5. Splicing analytic realizability back into the Nyman target obstruction

For each `k`, the right-half points `(18)` lie in the disk `(3)` and have rank `(4)`. Set

\[
D_a:=\frac4a-3.
\tag{43}
\]

The hypothesis in `(1)` gives

\[
G_k^{-B}G_k^{c\log D_a}(\log G_k)^{25/2}
\longrightarrow0.
\tag{44}
\]

Therefore `NB-140` applies directly to the packet and yields `(10)`. No minimum-gap hypothesis is being smuggled in: the `epsilon_(j,k)` may be arbitrarily crowded subject only to pairwise distinctness and the common radius bound.

The consequence is a strict hierarchy of source information.

The Bellotti--Wong count and Selberg density control global population. `NB-142` converts a forbidden packet into an order-`log G` short increment of the zero-count remainder. The present construction adds the full order-one `xi`-type canonical product and exact zeta functional equation and still realizes the packet. Therefore none of those inputs, separately or together, implies the required worst-cell `o(log G)` occupancy law.

Hamburger shows where this particular matched control finally breaks: at arithmetic half-plane structure strong enough to recover the ordinary Dirichlet-series source. A useful next theorem need not literally invoke Hamburger, but it must exploit information absent from a bare `xi`-type completion — for example prime-side/Dirichlet-series coherence, an explicit-formula constraint that is genuinely local at the packet scale, or a direct theorem forcing an actual crowded zeta packet to occupy a target-bearing Nyman direction.

## 6. Adversarial audit

**Not an RH counterexample.** `Z_*` is a synthetic matched-control function. Its off-critical zeros are inserted deliberately, and `(42)` proves that it is outside the ordinary zeta Dirichlet-series class.

**Not a new Nyman source.** The Nyman generators remain those of the actual zeta problem. Equation `(10)` concerns the state geometry attached to the formal packet parameters, exactly as in `NB-140`; it does not assert that `Z_*` generates the same orthogonality identities as `zeta`.

**No hidden minimum-gap assumption.** The packet ordinates in `(17)` need only be distinct. `NB-140` was specifically proved with complex divided differences so that the span comparison is independent of reciprocal pairwise gaps.

**The global count is checked at all large heights, not only at packet endpoints.** Between consecutive `G_k` the packet contribution is constant; while crossing one packet it increases by at most `2d_k`. Equation `(20)` therefore controls every sufficiently large `T`, with the strict margin `2c<0.10076`.

**The density statement is stronger than needed.** The right-half exceptional population is only `O(log T)`, not merely below the polynomial Selberg envelope. This still says nothing about worst-cell occupancy because the population is concentrated at superlacunary heights.

**The canonical product does not assume the desired analytic function.** Its convergence follows directly from `(25)`, and order one is proved from `(31)`--`(33)`. The functional equation is then an algebraic consequence of evenness about `1/2`.

**Hamburger is used only at the final arithmetic boundary.** The construction and all target-poor geometry are complete before invoking the converse theorem. `SOURCES.md` records the Kaczorowski--Molteni--Perelli anchor for the exact classical statement.

## Outcome

`NB-141`'s strongest caveat can be removed: sparse logarithmic confluence packets are compatible not only with a zeta-symmetric counting divisor but with a single order-one `xi`-type entire completion carrying the exact standard zeta functional equation and all currently used quantitative zero envelopes. The obstruction therefore survives substantially more analytic realizability than the previous matched control showed.

The surviving frontier is correspondingly sharper. **The missing rigidity is not generic entire-function structure on the `xi` side.** It must enter through arithmetic half-plane structure or through a target-aware local law special to the actual zeta divisor. Hamburger supplies a clean classical witness for that distinction: once an ordinary absolutely convergent Dirichlet series is added to the same functional equation and finite-order continuation, the synthetic control collapses back to `zeta`.