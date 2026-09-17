# NB-194 — Vinogradov–Korobov dephasing excludes positive Euler-band returns on specific high blocks

**Date:** 2026-09-17  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + SPECIFIC-BLOCK + VINOGRADOV-KOROBOV-DEPHASING + NB-193-REFINEMENT`.

`NB-193` proves that even the true-source-weighted positive `ell^1` phase defect of one Euler band has double-exponential **syndetic** inclusion length. That is a worst-gap statement, so it deliberately leaves open one escape: the particular block `[T,2T]` relevant to the coupled source-height problem might contain an unusually early return.

There is an unconditional regime where that escape can be closed. The full von-Mangoldt band used by `NB-193` has a normalized complex phase barycenter whose high-frequency response is controlled directly by the prime number theorem with Vinogradov--Korobov remainder. Partial summation gives

\[
\boxed{
|\mathcal C_a(t)|
\ll_{r_0,\Delta}
\frac1{1+|t|}
+(1+|t|)\exp[-cV(e^{r_0/a})]
}
\tag{1}
\]

with

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\tag{2}
\]

A positive weighted chord return of accuracy `eta<1` forces `|C_a(t)|>=1-eta`. Therefore, for every fixed `eta<1`, there are constants `T_eta,c_eta>0` such that, for all sufficiently small `a`,

\[
\boxed{
\mathcal A_a(t)>\eta
\qquad
\left(T_\eta\le |t|\le \exp\{c_\eta V(e^{r_0/a})\}\right).
}
\tag{3}
\]

Thus the true positive Euler mask has a deterministic **return-free corridor** reaching stretched-exponential height in the Vinogradov--Korobov scale. In particular, if `T>=T_eta` and `2T<=exp(c_eta V(e^{r_0/a}))`, then the actual block `[T,2T]` contains no such positive band return.

## Claim

Fix `r_0>0` and `Delta>0` in the first positive-mass band regime of `NB-189`--`NB-193`, and put

\[
x_a=e^{r_0/a},\qquad y_a=e^\Delta x_a.
\tag{4}
\]

Define

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n).
\tag{5}
\]

For sufficiently small `a`, the capped-character factor on this band is the common value `M_a(log n)=2`, so these are exactly the normalized **full prime-power Euler weights** entering the `NB-193` positive aggregate. Set

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|
\tag{6}
\]

and

\[
\mathcal C_a(t):=\sum_n w_{n,a}e^{-it\log n}
=\frac{\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a-it}}{D_a}.
\tag{7}
\]

Then there are constants `c,C>0`, depending only on the fixed band parameters, such that (1) holds for all sufficiently small `a` and all real `t`. Consequently (3) holds for every fixed `0<eta<1`.

For a coupled family `a=a_T->0`, the sufficient condition

\[
\boxed{
\log T=o\!\left(V(e^{r_0/a_T})\right)
}
\tag{8}
\]

excludes a positive `NB-193` return everywhere on `[T,2T]`. On the boundary where the two sides are comparable, inversion gives the implicit scale

\[
\boxed{
a\asymp (\log T)^{-5/3}(\log\log T)^{-1/3}}
\tag{9}
\]

up to fixed constants. Equation (9) is only the inversion scale of the available unconditional remainder, not a sharp phase transition.

## Derivation

### 1. Positive chord recurrence forces a large barycenter

For every real `theta`,

\[
1-\cos\theta\le |e^{i\theta}-1|.
\]

Hence

\[
1-\Re\mathcal C_a(t)
=\sum_n w_{n,a}(1-\cos(t\log n))
\le \mathcal A_a(t).
\tag{10}
\]

Therefore

\[
\boxed{
\mathcal A_a(t)\le\eta
\Longrightarrow
|\mathcal C_a(t)|\ge\Re\mathcal C_a(t)\ge1-\eta.
}
\tag{11}
\]

No prime-only reduction is needed. This uses the actual normalized von-Mangoldt source, including prime powers.

### 2. The PNT remainder dephases the full Euler shell

Bellotti's 2026 prime-number-theorem remainder, in the Korobov--Vinogradov regime, implies that for some absolute `c_0>0`,

\[
\boxed{\psi(u)=u+E(u),\qquad E(u)=O\!\left(u e^{-c_0V(u)}\right).}
\tag{12}
\]

On the fixed multiplicative interval `[x_a,e^Delta x_a]`, after decreasing the constant in the exponent if necessary,

\[
E(u)=O_{r_0,\Delta}\!\left(u e^{-c_1V(x_a)}\right)
\qquad (x_a\le u\le y_a).
\tag{13}
\]

Apply Stieltjes partial summation to `f_t(u)=u^{-1-a-it}`. The main term is

\[
J_a(t):=\int_{x_a}^{y_a}u^{-1-a-it}\,du
=x_a^{-a-it}\frac{1-e^{-(a+it)\Delta}}{a+it},
\tag{14}
\]

so, because `x_a^{-a}=e^{-r_0}`,

\[
|J_a(t)|\ll_{r_0,\Delta}(1+|t|)^{-1}.
\tag{15}
\]

The error contribution is

\[
E(y_a)f_t(y_a)-E(x_a)f_t(x_a)
-\int_{x_a}^{y_a}E(u)f_t'(u)\,du.
\tag{16}
\]

Since `|f_t'(u)|<=(1+a+|t|)u^{-2-a}`, (13) and the fixed logarithmic band width give

\[
\boxed{
\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a-it}
=J_a(t)+O_{r_0,\Delta}\!\left((1+|t|)e^{-c_1V(x_a)}\right).
}
\tag{17}
\]

Endpoint atoms contribute only `O((log y_a)/x_a)` and are absorbed. At `t=0`,

\[
J_a(0)=e^{-r_0}\frac{1-e^{-a\Delta}}a\longrightarrow e^{-r_0}\Delta,
\]

hence

\[
D_a=e^{-r_0}\Delta+o(1).
\tag{18}
\]

Dividing (17) by (18) proves (1). The factor `(1+|t|)` in the error is essential: it is the derivative cost of the oscillatory weight `u^{-it}`.

### 3. Uniform exclusion on a high block

Fix `0<eta<1`. Choose `T_eta` so the first term in (1) is below `(1-eta)/4` for `|t|>=T_eta`. Then choose `0<c_eta<c_1`. For sufficiently small `a`, the second term in (1) is also below `(1-eta)/4` whenever

\[
|t|\le \exp\{c_\eta V(x_a)\},
\]

because it is bounded by a constant times `exp(-(c_1-c_eta)V(x_a))`. Thus `|C_a(t)|<1-eta` throughout the corridor, contradicting (11) if `A_a(t)<=eta`. This proves (3) and the dyadic-block corollary (8).

The inversion behind (9) is simply

\[
\log T\asymp
\frac{a^{-3/5}}{(\log(1/a))^{1/5}},
\]

whose boundary solution has `a^{-1}` of order `(log T)^{5/3}(log log T)^{1/3}`.

## Relation to NB-192 and NB-193

`NB-192` and `NB-193` are entropy theorems: they make positive recurrence expensive in the **worst-gap** sense and force a log-log floor if recurrence must be guaranteed in every block. `NB-194` is instead a source-dephasing theorem. In the narrower Vinogradov--Korobov corridor (8), the particular block cannot be lucky: the full true-amplitude Euler barycenter is uniformly small throughout `[T,2T]`.

The ranges do not meet. The syndetic obstruction of `NB-193` becomes relevant near `a` of order `1/log log T`, while the unconditional specific-block exclusion above lives around the much smaller scale (9). The large intermediate regime is still open.

## Generality audit

**Generality audited.** The partial-summation mechanism is generic: any positive counting measure with main density `du` and a strong remainder yields a corresponding dephasing estimate for a normalized multiplicative shell. The implication from a positive chord defect to a large barycenter is also generic convex geometry.

The source-specific input is exact. Here the measure is the actual von-Mangoldt measure, the shell is the same normalized Euler-Wiener band used in `NB-189`--`NB-193`, and the available error term is the zeta prime-number-theorem remainder. No rational-independence or product-Haar surrogate is used.

## Prior-art audit

The load-bearing external theorem is the prime number theorem with Korobov--Vinogradov-scale remainder. Bellotti's peer-reviewed 2026 result gives an essentially optimal modern form; the weaker shape (12) is sufficient here. Abel/Stieltjes partial summation and the resulting finite Dirichlet-polynomial estimate are standard consequences.

Focused searches for von-Mangoldt Dirichlet polynomials `sum Lambda(n)n^(-1-a-it)`, multiplicative-interval PNT partial summation, and high-block prime-phase recurrence found the standard surrounding tools but no additional theorem needed for this line-specific consequence. No novelty claim is made for partial summation or for Vinogradov--Korobov dephasing itself. The durable source dependency is recorded in `research/nyman_beurling/SOURCES.md`.

## Self-adversarial audit

The theorem excludes only **positive `ell^1` recurrence of the normalized Euler coefficient mask**, exactly one escape left by `NB-193`. It does not lower-bound all scalar acquisition. Signed or complex aggregation can be small while individual coefficient phases are far from one, and a direct Fourier--Stieltjes measure supported in `[T,2T]` need not be obtained by recurrence of a low-height seed.

The result is also limited by the derivative factor `|t|` in (17). With the current unconditional PNT remainder, this gives only the stretched-exponential corridor (3) and does not bridge the gap to the log-log scale of `NB-193`. Sharper direct cancellation for the oscillatory von-Mangoldt shell could extend the blockwise exclusion without improving the ordinary PNT remainder.

## Research consequence

One explicit escape left by `NB-193` is now closed in a genuine coupled regime: **an exceptionally early positive return in the actual dyadic block cannot occur while `log T=o(V(e^{r_0/a_T}))`**. The next useful theorem should attack the intermediate regime directly, either by stronger blockwise estimates for `sum Lambda(n)n^{-1-a-it}` or by leaving the positive coefficient topology and pricing signed/complex aggregate cancellation in a source-safe response norm.