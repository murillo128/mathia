# NB-195 — Mean-square dephasing makes positive Euler-band returns sparse on every high block

**Date:** 2026-09-17  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + SPECIFIC-BLOCK + MEAN-SQUARE-DEPHASING + NB-194-REFINEMENT`.

`NB-194` eliminates positive recurrence pointwise on a deterministic Vinogradov--Korobov corridor, but its uniform estimate stops well before the log-log scale where the entropy obstruction of `NB-192`--`NB-193` becomes relevant. The remaining gap should not be read as a regime in which positive returns are plentiful.

For the same normalized full von-Mangoldt band, the classical Montgomery--Vaughan mean-value theorem gives a blockwise statement that is much more uniform in the coupled limit. The true Euler weights are sufficiently diffuse that their squared coefficient mass is only `O((a x_a)^(-1))`, where `x_a=exp(r_0/a)`. Consequently the normalized shell barycenter has very small `L^2` mass on every dyadic high block:

\[
\boxed{
\int_T^{2T}|\mathcal C_a(t)|^2\,dt
\ll_{r_0,\Delta}
\frac{T}{a x_a}+\frac1a.
}
\tag{1}
\]

Since a positive chord return forces `|C_a(t)|` close to one, the return set

\[
R_a(T;\eta):=\{t\in[T,2T]:\mathcal A_a(t)\le\eta\},
\qquad 0<\eta<1,
\tag{2}
\]

satisfies

\[
\boxed{
\frac{|R_a(T;\eta)|}{T}
\ll_{r_0,\Delta,\eta}
\frac{e^{-r_0/a}}a+\frac1{aT}.
}
\tag{3}
\]

Thus for every coupled family `a=a_T->0` with `a_T T->infinity`, positive true-source Euler-band returns have **vanishing relative measure on the actual block `[T,2T]`**. This includes the large intermediate regime in which `NB-194` does not give pointwise exclusion.

The conclusion is deliberately weaker than a no-return theorem. Equation (3) does not exclude one isolated lucky return, and one such return could still be enough for a recurrence-based transplant. What it does exclude is any positive-density or macroscopic reservoir of such returns. The remaining positive-recurrence escape is therefore an exceptional-large-value problem rather than a generic blockwise recurrence problem.

## Claim

Fix `r_0>0` and `Delta>0` in the first positive-mass band regime of `NB-189`--`NB-194`. Put

\[
x_a=e^{r_0/a},\qquad y_a=e^\Delta x_a,
\tag{4}
\]

and retain the exact normalized full prime-power Euler weights of `NB-194`,

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n).
\tag{5}
\]

Define

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|
\tag{6}
\]

and

\[
\mathcal C_a(t):=\sum_n w_{n,a}e^{-it\log n}.
\tag{7}
\]

For sufficiently small `a`, uniformly for every `T>0`,

\[
\boxed{
\int_T^{2T}|\mathcal C_a(t)|^2\,dt
\ll_{r_0,\Delta}
\frac{T}{a e^{r_0/a}}+\frac1a.
}
\tag{8}
\]

Consequently, for every fixed `0<eta<1`,

\[
\boxed{
|R_a(T;\eta)|
\ll_{r_0,\Delta,\eta}
\frac{T}{a e^{r_0/a}}+\frac1a,
}
\tag{9}
\]

and therefore

\[
\boxed{
a_T\to0,\quad a_TT\to\infty
\quad\Longrightarrow\quad
\frac{|R_{a_T}(T;\eta)|}{T}\to0.}
\tag{10}
\]

No Vinogradov--Korobov relation between `T` and `a` is required for (8)--(10).

## Derivation

### 1. The actual Euler shell has small squared coefficient mass

`NB-194` already proves, from the prime number theorem on the fixed multiplicative shell, that

\[
D_a=e^{-r_0}\Delta+o(1).
\tag{11}
\]

Hence `D_a` is bounded above and below by positive constants depending only on the fixed band parameters. Since `Lambda(n)<=log y_a` on the shell,

\[
\Lambda(n)^2
\le (\log y_a)\Lambda(n).
\tag{12}
\]

Also

\[
n^{-2-2a}
=n^{-1-a}n^{-1-a}
\le x_a^{-1-a}n^{-1-a}.
\tag{13}
\]

Therefore

\[
\begin{aligned}
\sum_n w_{n,a}^2
&=D_a^{-2}\sum_{x_a\le n<y_a}\Lambda(n)^2n^{-2-2a}\\
&\le
D_a^{-2}(\log y_a)x_a^{-1-a}
\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a}\\
&\ll_{r_0,\Delta}
\frac{1}{a x_a}.
\end{aligned}
\tag{14}
\]

Here `log y_a=r_0/a+Delta` and `x_a^{-a}=e^{-r_0}`. Because `n<y_a=e^Delta x_a`, the same estimate gives

\[
\boxed{
\sum_n n w_{n,a}^2
\ll_{r_0,\Delta}\frac1a.}
\tag{15}
\]

This is the source-specific input: after normalization to unit positive mass, the true von-Mangoldt shell spreads that mass over enough arithmetic labels that its `ell^2` coefficient energy is exponentially smaller than its `ell^1` mass.

### 2. Montgomery--Vaughan converts coefficient diffuseness into time-mean dephasing

For a finite Dirichlet polynomial

\[
F(t)=\sum_n c_n n^{-it},
\]

the classical Montgomery--Vaughan mean-value theorem gives, on any interval of length `T`,

\[
\int_T^{2T}|F(t)|^2\,dt
=
T\sum_n|c_n|^2
+O\!\left(\sum_n n|c_n|^2\right).
\tag{16}
\]

The translated interval causes no change in the coefficient moduli: replacing `t` by `T+u` only multiplies `c_n` by the unit phase `n^{-iT}`. Applying (16) with `c_n=w_{n,a}` and using (14)--(15) proves (8).

The estimate does not use cancellation inside the coefficients. In particular, it retains the exact positive prime-power Euler amplitudes rather than flattening the shell or replacing it by independent phases.

### 3. A positive return is a near-maximal large value

As in `NB-194`, positivity gives

\[
1-\Re\mathcal C_a(t)
=\sum_n w_{n,a}(1-\cos(t\log n))
\le\mathcal A_a(t).
\tag{17}
\]

Therefore

\[
\mathcal A_a(t)\le\eta
\quad\Longrightarrow\quad
|\mathcal C_a(t)|\ge1-\eta.
\tag{18}
\]

Chebyshev applied to (8) yields

\[
(1-\eta)^2|R_a(T;\eta)|
\le
\int_T^{2T}|\mathcal C_a(t)|^2\,dt,
\tag{19}
\]

which is (9). Dividing by `T` gives

\[
\frac{|R_a(T;\eta)|}{T}
\ll_{r_0,\Delta,\eta}
\frac1{a e^{r_0/a}}+\frac1{aT}.
\tag{20}
\]

The first term tends to zero for every `a->0`; the second tends to zero exactly under the mild high-block condition `aT->infinity`. This proves (10).

## Relation to NB-192--NB-194

`NB-192`--`NB-193` say that positive recurrence is expensive in the worst-gap/syndetic sense. `NB-194` is much stronger pointwise, but only in the Vinogradov--Korobov corridor

\[
\log T=o(V(e^{r_0/a_T})).
\]

`NB-195` trades pointwise exclusion for range. Its mean-square estimate applies on every block and shows that positive returns have density zero as soon as `a_TT->infinity`, including the broad intermediate regime between the `NB-194` corridor and the log-log recurrence scale.

This does **not** close the exact loophole isolated by `NB-193`: a transplant that needs only one recurrence time can still use a measure-zero exceptional set. The gain is that any such construction must now target near-maximal exceptional values of the actual Euler Dirichlet polynomial; it cannot rely on a macroscopic family of positive returns hidden outside the deterministic corridor.

## Generality audit

**Generality audited; classification: mixed.** The analytic mechanism behind (16)--(20) is representation-generic. Any normalized positive Dirichlet polynomial with small squared coefficient mass has a small large-value set by the classical mean-square theorem. There is nothing specifically Nyman--Beurling about that implication.

The source-specific content is the input (14)--(15): these are the exact full von-Mangoldt amplitudes of the Euler-Wiener band used by `NB-189`--`NB-194`, normalized by their actual source mass, at the source-selected shell scale `x_a=e^{r_0/a}`. The resulting exponentially small coefficient energy is what turns the generic mean-square inequality into the coupled statement (10).

Accordingly, this finding should be used as a source-acquisition obstruction, not as a new abstract theorem about Nyman approximation spaces. It constrains one concrete positive recurrence mechanism before the destination geometry is applied.

## Prior-art audit

The load-bearing analytic engine is classical: Montgomery--Vaughan mean-value theory for Dirichlet polynomials, obtained from their generalized Hilbert inequality, is already anchored in `research/nyman_beurling/SOURCES.md`. Modern large-value theory for Dirichlet polynomials is much stronger in other regimes; for example Guth--Maynard study how often Dirichlet polynomials attain unusually large values. No novelty is claimed for mean-square or large-value technology itself.

Focused prior-art searches for mean-square Dirichlet-polynomial estimates, large values of Dirichlet polynomials, and prime/von-Mangoldt phase recurrence found this classical and modern surrounding literature but no additional theorem needed for (8)--(10). The line-specific contribution is only the consequence obtained after inserting the true Euler-band normalization and coefficient-energy scale. No new durable source dependency is required.

## Self-adversarial audit

The main limitation is sharp and consequential: **density zero is not emptiness**. An isolated `t` with `A_a(t)<=eta` is compatible with every estimate above, and a recurrence-based construction may need only one such height. The `O(1/a)` mean-value error in (8) is also far too large to turn the argument into a pointwise no-return theorem merely by using continuity of `C_a`.

The result remains restricted to the positive source-weighted `ell^1` recurrence topology of `NB-193`--`NB-194`. Signed or complex aggregate synthesis can exploit cancellations that are invisible to `A_a`, and a direct source-safe Fourier--Stieltjes construction need not arise by translating a low-height seed at all.

Finally, the bound `sum w_n^2 << 1/(a x_a)` is intentionally robust rather than sharp. Sharpening its constant would not change the qualitative conclusion; the live problem is exceptional near-maximal values, not the average energy.

## Research consequence

The specific-block gap left by `NB-194` is now narrower in kind, not merely in scale. Outside the deterministic return-free corridor, positive recurrence can survive only on a vanishing-density exceptional set whenever `a_TT->infinity`. The next useful positive-recurrence theorem should therefore address **isolated near-maximal values** of the true Euler shell on `[T,2T]`, for example through a separated-large-values or source-specific pointwise argument. In parallel, the more structural escape remains signed/complex aggregate acquisition, where positivity no longer converts recurrence into a near-unit barycenter.