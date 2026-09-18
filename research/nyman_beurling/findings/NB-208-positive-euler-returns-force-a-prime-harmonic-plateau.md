# NB-208 — Positive Euler returns force a prime harmonic plateau

**Date:** 2026-09-18  
**Status:** `EXACT-DERIVED + SOURCE-ACQUISITION + POSITIVE-EULER + WEIGHTED-FOURIER + PRIME-REDUCTION + METHOD-BOUNDARY`.

`NB-207` isolates the remaining limitation of the source-blind Ford/Fejer route: once phase-window cardinality is converted to Euler mass only through the pointwise atom cap, one must drive the unweighted carrier Fourier error down to `O(1/X)`. The natural escape left there is to estimate the **actual source-weighted Fourier response** instead of counting carrier points.

There is a sharper exact reduction behind that suggestion. An `o(1/X)` positive Euler return does not merely put most source mass in a short phase window. It forces a whole block of `Theta(X)` **von-Mangoldt-weighted prime Dirichlet polynomial values**, sampled at the arithmetic progression of heights `t,2t,...`, to be phase-pinned at their maximal value. Conversely, a fixed real-part deficit at just one of those harmonics already rules out an `o(1/X)` return. Prime powers are exponentially negligible, and on a fixed multiplicative shell the true prime Euler weights are uniformly comparable with the uniform prime measure. Thus the remaining source-aware problem can be stated without the `X` atom tariff:

> prove that somewhere among the first `Theta(X)` harmonics, the prime-log polynomial has a fixed phase deficit from its maximal value.

This is stronger and more specific than asking for generic cancellation or a generic large-value bound.

## 1. Setup

Keep the positive shell notation of `NB-198`--`NB-207`. Fix `r_0>0` and `Delta>0`, let

\[
x=x_a=e^{r_0/a},\qquad y=e^\Delta x,\qquad X=\log x=\frac{r_0}{a},
\]

and define

\[
D_a:=\sum_{x\le n<y}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=
\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x,y)}(n).
\tag{1}
\]

By the PNT normalization already used throughout this shell program, `D_a asymp_{r_0,Delta} 1`. The normalized positive return is

\[
\mathcal A_a(t)
:=
\sum_n w_{n,a}|e^{-it\log n}-1|.
\tag{2}
\]

For an integer `h>=1`, write the full source Fourier coefficient

\[
\widehat\mu_{a,t}(h)
:=
\sum_n w_{n,a}e^{-iht\log n}.
\tag{3}
\]

The elementary factorization

\[
1-z^h=(1-z)(1+z+\cdots+z^{h-1}),\qquad |z|=1,
\]

gives the exact amplification inequality

\[
\boxed{
|1-\widehat\mu_{a,t}(h)|
\le h\,\mathcal A_a(t).
}
\tag{4}
\]

Taking real parts also gives

\[
\boxed{
1-\Re\widehat\mu_{a,t}(h)
\le h\,\mathcal A_a(t).
}
\tag{5}
\]

No Fourier truncation, discrepancy inequality, or atom bound is used here.

## 2. Prime powers carry exponentially vanishing shell mass

Let

\[
R_a:=
\sum_{\substack{x\le p^k<y\\k\ge2}}w_{p^k,a},
\qquad
P_a:=1-R_a.
\tag{6}
\]

The number of prime powers `p^k<y` with `k>=2` is `O_Delta(sqrt(x))` for this fixed-ratio shell, up to a harmless lower-order contribution from `k>=3`. Since every term in the unnormalized numerator is at most `O_Delta(X/x)`, while `D_a asymp 1`,

\[
\boxed{
R_a\ll_{r_0,\Delta} Xx^{-1/2}
=O\!\left(Xe^{-X/2}\right).
}
\tag{7}
\]

A cruder `O(X^2e^{-X/2})` bound would already suffice. In particular,

\[
P_a=1-o(1).
\tag{8}
\]

Define the normalized prime-only Euler Fourier response

\[
\mathcal P_a(u)
:=
\frac{
\displaystyle\sum_{x\le p<y}(\log p)p^{-1-a}e^{-iu\log p}
}{
\displaystyle\sum_{x\le p<y}(\log p)p^{-1-a}
}.
\tag{9}
\]

If `\mathcal R_a(u)` denotes the corresponding normalized prime-power response when `R_a>0`, then

\[
\widehat\mu_{a,t}(h)
=
P_a\mathcal P_a(ht)+R_a\mathcal R_a(ht).
\tag{10}
\]

Because `1-Re z>=0` on the closed unit disk, (10) implies

\[
1-\Re\widehat\mu_{a,t}(h)
=
P_a\bigl(1-\Re\mathcal P_a(ht)\bigr)
+
R_a\bigl(1-\Re\mathcal R_a(ht)\bigr)
\ge
P_a\bigl(1-\Re\mathcal P_a(ht)\bigr).
\tag{11}
\]

Combining (5) and (11),

\[
\boxed{
1-\Re\mathcal P_a(ht)
\le
\frac{h}{P_a}\,\mathcal A_a(t).
}
\tag{12}
\]

This is the source-aware transfer that the source-blind argument of `NB-207` cannot see.

## 3. An `o(1/X)` return forces `Theta(X)` phase-pinned prime harmonics

Fix any constant `c>0`. If a coupled sequence `(a_j,t_j)` satisfies

\[
X_j\,\mathcal A_{a_j}(t_j)\longrightarrow0,
\tag{13}
\]

then (8) and (12) give

\[
\boxed{
\max_{1\le h\le cX_j}
\left(1-\Re\mathcal P_{a_j}(h t_j)\right)
\longrightarrow0.
}
\tag{14}
\]

Since `|\mathcal P_a(u)|<=1`,

\[
|1-\mathcal P_a(u)|^2
\le 2\bigl(1-\Re\mathcal P_a(u)\bigr),
\tag{15}
\]

so (14) also yields the genuinely phase-pinned form

\[
\boxed{
\max_{1\le h\le cX_j}
|1-\mathcal P_{a_j}(h t_j)|
\longrightarrow0.
}
\tag{16}
\]

Thus a positive return at the scale relevant after `NB-207` creates not one exceptional large value but an arithmetic progression of `Theta(X)` near-maximal prime-weighted Dirichlet polynomial values, all with argument tending to zero.

The converse is equally useful. Suppose that for some fixed `c,delta>0` and every sufficiently small `a`, every height `t` in a proposed corridor admits an integer

\[
1\le h\le cX
\]

such that

\[
1-\Re\mathcal P_a(ht)\ge\delta.
\tag{17}
\]

Then (5), (11), and `P_a=1-o(1)` imply

\[
\boxed{
\mathcal A_a(t)
\ge
\frac{P_a\delta}{h}
\ge
\frac{\delta+o(1)}{cX}.
}
\tag{18}
\]

Therefore a **single fixed-deficit prime harmonic among the first `cX` harmonics excludes every `o(1/X)` positive return**. Unlike `NB-207`, (18) asks for no `1/X`-sized bound on an unweighted carrier exponential sum.

## 4. The true Euler amplitudes can be flattened on one fixed shell

The reduction can be stated using the ordinary uniform prime measure as well. Let

\[
N_a:=\pi(y)-\pi(x),
\qquad
\mathcal U_a(u)
:=
\frac1{N_a}\sum_{x\le p<y}e^{-iu\log p}.
\tag{19}
\]

By PNT on the fixed-ratio interval,

\[
N_a\asymp_\Delta \frac{x}{X}.
\tag{20}
\]

For `p in [x,y)`,

\[
(\log p)p^{-1-a}
\asymp_{r_0,\Delta}
\frac{X}{x},
\tag{21}
\]

and the prime normalization in (9) is `asymp 1`. Hence the probability weights in `\mathcal P_a` are uniformly comparable, with constants depending only on `r_0,Delta`, to `1/N_a`. Applied to the nonnegative quantity `1-cos(u log p)`, this gives fixed constants `0<c_1<=c_2<infinity` such that

\[
\boxed{
c_1\bigl(1-\Re\mathcal U_a(u)\bigr)
\le
1-\Re\mathcal P_a(u)
\le
c_2\bigl(1-\Re\mathcal U_a(u)\bigr)
}
\tag{22}
\]

for all sufficiently small `a` and all real `u`.

Consequently, (13) forces

\[
\boxed{
\max_{1\le h\le cX_j}
|1-\mathcal U_{a_j}(h t_j)|
\longrightarrow0,
}
\tag{23}
\]

and a fixed real-part deficit for `\mathcal U_a(ht)` at one harmonic implies (18), with a changed constant.

This is a useful simplification: **inside one fixed multiplicative shell, the obstruction is no longer an amplitude-balancing problem.** A putative `o(1/X)` positive Euler return forces near-total coherence of the ordinary prime phases themselves at `Theta(X)` consecutive harmonics.

## 5. Why this is not just another generic large-value problem

The conclusion in (23) is much more rigid than `|D(u)|` being large. It asks for near-maximal magnitude **and** phase pinned at `+1`, simultaneously at the structured heights

\[
t,2t,\ldots,\lfloor cX\rfloor t.
\tag{24}
\]

Modern large-value theory for Dirichlet polynomials, including Guth--Maynard, studies how often a bounded-coefficient polynomial can have large modulus on separated sets and is indispensable for prime-distribution applications. But its generic large-value formulation does not itself supply the deterministic fixed-deficit statement (17) on this arithmetic progression of sample heights. The threshold here is also near maximal: after rescaling the shell coefficients to be `O(1)`, the prime polynomial has length `x` and value scale `asymp x/X`, not the `x^{3/4}`-type regime that drives the Guth--Maynard breakthrough.

So the next source-aware task is not simply "get a better Dirichlet-polynomial large-value theorem." A theorem that closes this route must exploit at least one of the extra structures now exposed: near-maximality, phase pinning, the arithmetic progression `h t`, or the fact that the coefficients are the prime indicator / von-Mangoldt source rather than arbitrary bounded coefficients.

## 6. Representation and novelty audit

The inequality `|1-z^h|<=h|1-z|` and the passage from real-part deficit to Fourier concentration are elementary harmonic analysis. The negligibility of prime powers and the comparability of the prime weights on a fixed multiplicative shell are routine consequences of the same PNT normalization already used by `NB-187`--`NB-207`. No new external theorem is load-bearing, so `SOURCES.md` does not need an additional anchor.

The project-local mathematical delta is the **scale-matched source-aware reduction** after `NB-207`: an `o(1/X)` return forces a `Theta(X)` phase-pinned prime harmonic plateau, and one fixed deficit anywhere in that plateau gives the desired `Omega(1/X)` obstruction without paying the source-blind atom tariff. The result should not be read as a new theorem about prime Dirichlet polynomials themselves; it identifies the exact type of prime theorem that would improve the current positive-source frontier.

This also separates two superficially similar tasks. `NB-198`--`NB-207` bound how much source mass can occupy short phase windows by first controlling the underlying carrier. The present reduction instead says what **the actual prime Fourier response must do if such occupancy succeeds**. It therefore moves the open step from cardinality transfer to a concrete source-weighted / prime-weighted harmonic statement.

## 7. Boundaries and consequence

Positivity remains load-bearing. Equations (11)--(12) use that the real-part deficits of the prime and prime-power pieces are nonnegative. A signed or complex synthesis can cancel those deficits and is not controlled by this argument.

This is also still a source-acquisition theorem, not a lower bound for the optimal Nyman--Beurling distance. The destination bridge remains unchanged: one must prove that a successful Nyman approximant forces a positive Euler return of the form studied here before any prime-harmonic obstruction can bear on the approximation problem itself.

Within the positive source program, however, the next falsifiable target is now precise. To beat the source-blind Ford frontier of `NB-207`, it is enough to establish, in a larger height corridor, constants `c,delta>0` such that every admissible height `t` has some `1<=h<=cX` with

\[
1-\Re\left(
\frac1{\pi(e^\Delta x)-\pi(x)}
\sum_{x\le p<e^\Delta x}p^{-iht}
\right)
\ge\delta.
\tag{25}
\]

Conversely, any counterexample to such a statement that comes from an `o(1/X)` Euler return must exhibit a near-maximal, phase-pinned prime Dirichlet plateau on all the first `Theta(X)` harmonics. That is the concrete source-specific escape left by the exact `X` tariff in `NB-207`.