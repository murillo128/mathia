# NB-196 — Short-interval prime density forbids positive Euler returns through the 13/30 Mellin corridor

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + SPECIFIC-BLOCK + POINTWISE-DEPHASING + NB-194/NB-195-REFINEMENT`.

`NB-195` shows that positive returns of the true normalized Euler shell are sparse on every sufficiently high block, but its mean-square argument cannot exclude one isolated return. `NB-194` does exclude every return pointwise, yet only while the oscillatory height is small enough for a global Vinogradov--Korobov PNT remainder to survive Stieltjes partial summation.

A stronger source-specific input changes that pointwise scale. Guth--Maynard's uniform prime number theorem in intervals of length `X^(17/30+epsilon)` resolves the positive Euler shell on spatial cells much shorter than the shell itself. On such a cell, the phase `u^(-it)` is essentially constant as long as `|t|` is below the reciprocal relative cell width. The complementary exponent is `1-17/30=13/30`.

For the exact full von-Mangoldt shell of `NB-194`--`NB-195`, this gives the uniform asymptotic

\[
\boxed{
\mathcal C_a(t)
=
e^{-it\log x_a}
\frac{a\bigl(1-e^{-(a+it)\Delta}\bigr)}
{(a+it)(1-e^{-a\Delta})}
+o_{\epsilon,r_0,\Delta}(1)
}
\tag{1}
\]

throughout

\[
1\le |t|\le x_a^{13/30-\epsilon},
\qquad x_a=e^{r_0/a}.
\tag{2}
\]

The continuum factor in (1) is `O_Delta(1/|t|)`. Hence, for every fixed positive-return tolerance `0<eta<1`, there is a fixed `T_eta` such that the actual shell has **no** positive return

\[
\boxed{
\mathcal A_a(t)>\eta
\qquad
(T_\eta\le |t|\le x_a^{13/30-\epsilon})
}
\tag{3}
\]

for all sufficiently small `a`.

Consequently, if `a=a_T->0` and

\[
\limsup_{T\to\infty}
\frac{a_T\log(2T)}{r_0}<\frac{13}{30},
\tag{4}
\]

then the whole physical block `[T,2T]` is eventually positive-return-free. This is a genuine pointwise closure of the isolated-return loophole over a much wider coupled corridor than `NB-194`; it does not rely on density estimates.

## Claim

Fix `r_0>0`, `Delta>0`, and define

\[
x_a=e^{r_0/a},\qquad y_a=e^\Delta x_a,
\tag{5}
\]

with the exact full Euler-shell normalization

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\tag{6}
\]

\[
\mathcal C_a(t):=\sum_n w_{n,a}e^{-it\log n},
\qquad
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\tag{7}
\]

For every fixed `epsilon>0`, uniformly for

\[
1\le |t|\le x_a^{13/30-\epsilon},
\tag{8}
\]

we have (1). In particular, for every fixed `0<eta<1` there are constants `T_eta>=1` and `a_0>0`, depending only on the displayed fixed parameters, such that

\[
0<a<a_0,
\quad
T_\eta\le |t|\le x_a^{13/30-\epsilon}
\quad\Longrightarrow\quad
\mathcal A_a(t)>\eta.
\tag{9}
\]

The endpoint `13/30` is not claimed. A fixed positive margin is essential in the present argument.

## Derivation

### 1. Short-interval prime density supplies spatial resolution `x^(17/30+epsilon)`

Guth--Maynard prove that for every fixed `delta>0`, uniformly for

\[
X^{17/30+\delta}\le H\le X^{0.99},
\tag{10}
\]

one has the prime number theorem in `[X,X+H]`. By partial summation, and after adding the negligible contribution of proper prime powers, this gives the equivalent Chebyshev form

\[
\psi(X+H)-\psi(X)=H(1+o_\delta(1))
\tag{11}
\]

uniformly in the same fixed-power range.

Choose

\[
h=x_a^{17/30+\epsilon/2}.
\tag{12}
\]

For `X` in the fixed multiplicative shell `[x_a,y_a]`, (12) lies above `X^(17/30+epsilon/4)` and below `X^0.99` once `a` is small. Therefore the shell can be partitioned into cells of length `h` (plus one shorter terminal cell) on which

\[
\sum_{X<n\le X+h}\Lambda(n)=h(1+o(1))
\tag{13}
\]

uniformly over all complete cells. The terminal remainder can be absorbed by merging it into the preceding cell, changing its length only by a bounded factor; alternatively one may use a variable final mesh length still inside the admissible short-interval range.

Proper prime powers are harmless directly: on the whole shell,

\[
\sum_{\substack{x_a\le p^k<y_a\\k\ge2}}
\frac{\log p}{p^{k(1+a)}}
\ll_{r_0,\Delta}
\frac{\log x_a}{\sqrt{x_a}}
=o(1).
\tag{14}
\]

Thus the local prime theorem is genuinely resolving the same full von-Mangoldt source used in `NB-194`--`NB-195`, not a flattened surrogate.

### 2. Spatial resolution transfers to a complementary Mellin-frequency corridor

Let

\[
f_t(u)=u^{-1-a-it}.
\tag{15}
\]

On a mesh cell `[X,X+h]` with `X\asymp x_a`,

\[
\sup_{u\in[X,X+h]}
\frac{|f_t(u)-f_t(X)|}{|f_t(X)|}
\ll
(1+|t|)\frac{h}{x_a}.
\tag{16}
\]

If `|t|<=x_a^(13/30-epsilon)`, then by (12)

\[
(1+|t|)\frac{h}{x_a}
\ll x_a^{-\epsilon/2}+x_a^{-13/30+\epsilon/2}
=o(1).
\tag{17}
\]

Combining (13), (16), and (17) cell by cell gives a Riemann-sum approximation uniform in the whole range (8):

\[
\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a-it}
=
\int_{x_a}^{y_a}u^{-1-a-it}\,du+o(1).
\tag{18}
\]

The accumulated error remains `o(1)` because the total absolute continuum mass on the fixed log-width shell is bounded:

\[
\int_{x_a}^{y_a}u^{-1-a}\,du
=
e^{-r_0}\frac{1-e^{-a\Delta}}a
=e^{-r_0}\Delta+o(1).
\tag{19}
\]

Setting `t=0` in the same argument gives

\[
D_a=
e^{-r_0}\frac{1-e^{-a\Delta}}a+o(1).
\tag{20}
\]

The exponent `13/30` has therefore appeared for a transparent reason: a source resolved uniformly on relative spatial scale `x_a^(-13/30+epsilon/2)` can be integrated against Mellin phases up to the reciprocal frequency scale.

### 3. The continuum shell dephases like `1/|t|`

The main integral in (18) is explicit:

\[
\int_{x_a}^{y_a}u^{-1-a-it}\,du
=
x_a^{-a-it}
\frac{1-e^{-(a+it)\Delta}}{a+it}.
\tag{21}
\]

Dividing (21) by (20), whose limit is the positive constant `e^(-r_0)Delta`, proves (1) uniformly in (8). For small `a` and `|t|>=1`,

\[
\left|
\frac{a(1-e^{-(a+it)\Delta})}
{(a+it)(1-e^{-a\Delta})}
\right|
\le
\frac{4}{\Delta|t|}.
\tag{22}
\]

Fix `0<eta<1` and choose, for example,

\[
T_\eta>\frac{8}{\Delta(1-\eta)}.
\tag{23}
\]

The uniform `o(1)` in (1) is then smaller than `(1-eta)/2` for sufficiently small `a`, so throughout the corridor in (9)

\[
|\mathcal C_a(t)|<1-\eta.
\tag{24}
\]

But positivity gives the elementary implication already used in `NB-194`--`NB-195`,

\[
\mathcal A_a(t)\le\eta
\quad\Longrightarrow\quad
|\mathcal C_a(t)|\ge1-\eta,
\tag{25}
\]

because `|C_a(t)-1|<=A_a(t)`. Equations (24)--(25) prove (9).

### 4. Coupled block consequence

Assume (4). Choose a fixed `epsilon>0` and a fixed margin so that eventually

\[
\log(2T)
\le
\left(\frac{13}{30}-\epsilon\right)\frac{r_0}{a_T}.
\tag{26}
\]

Then

\[
2T\le x_{a_T}^{13/30-\epsilon}.
\tag{27}
\]

Since `T->infinity`, eventually also `T>=T_eta`. Hence the entire block `[T,2T]` lies inside the pointwise no-return corridor (9), and

\[
\boxed{
R_{a_T}(T;\eta)=\varnothing
}
\tag{28}
\]

for all sufficiently large `T`.

This is much wider than the deterministic corridor obtained from the global PNT remainder in `NB-194`. It reaches the natural `a_T\asymp 1/\log T` scale with a fixed constant margin, although it does not approach the fixed-`a` almost-periodic recurrence regime.

## Relation to NB-194--NB-195

`NB-194` uses a global Vinogradov--Korobov PNT remainder and obtains pointwise dephasing only while the oscillatory integration-by-parts loss is dominated by that remainder. `NB-195` removes that restrictive relation between `a` and `T`, but pays by controlling only the measure of the return set.

`NB-196` inserts a different arithmetic input between those two results: **uniform local density of primes**. Rather than asking a global PNT remainder to absorb a rapidly rotating phase, it samples the source on cells shorter than one phase wavelength. This restores a pointwise theorem and closes the isolated-return loophole whenever the phase wavelength remains above the Guth--Maynard short-interval scale.

The result does not supersede `NB-195`. Beyond `x_a^(13/30-epsilon)`, (18) is no longer justified by this mesh, whereas the mean-square sparsity theorem continues to hold on arbitrary blocks under `a_TT->infinity`.

## Generality and representation audit

**Generality audited; classification: mixed, with a genuinely arithmetic input.** The transfer principle itself is generic: if a positive counting measure on `[x,e^Delta x]` has a uniform local-density asymptotic down to spatial scale `x^(theta+o(1))`, then its normalized Mellin transform follows the corresponding continuum transform uniformly up to frequencies `x^(1-theta-o(1))`. This is just a local Riemann-sum/Fourier-resolution statement and is not claimed as an arithmetic novelty.

The source-specific fact is that the actual Euler measure `dpsi`, with its von-Mangoldt prime-power amplitudes, has `theta=17/30+epsilon` uniformly by the Guth--Maynard theorem; proper prime powers are lower order on the selected shell. The numerical exponent `13/30` is therefore **not intrinsic to Nyman--Beurling geometry**. It is the complement of the best load-bearing uniform short-interval exponent used here. Any future improvement of the pointwise prime theorem in short intervals would automatically enlarge the Mellin dephasing corridor by the complementary amount.

Changing the source representation can therefore change the result drastically. A smooth absolutely continuous measure with the same coarse shell mass has immediate continuum dephasing; an arbitrary atomic measure need not have any comparable pointwise corridor. What is being certified here is the arithmetic distribution of the ordinary-prime Euler source, before destination-space conditioning enters.

## Prior-art audit

The load-bearing external theorem is Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), 623--675, Corollary 1.3. It gives the uniform prime number theorem in intervals of length `X^(17/30+delta)` for every fixed positive `delta`, improving the classical `7/12` threshold. This source is added to `research/nyman_beurling/SOURCES.md` because `NB-196` genuinely fails at the stated exponent without it.

The passage from a uniform short-interval counting asymptotic to (18) is elementary local partial summation/Riemann summation. Focused prior-art searches around Mellin transforms of von-Mangoldt short shells, prime exponential sums, and short-interval PNT applications did not reveal a theorem that needs to be imported for this transfer. No novelty is claimed for that generic harmonic-analysis step; the line-specific content is its insertion into the exact positive Euler acquisition obstruction of `NB-189`--`NB-195`.

## Self-adversarial audit

Several boundaries are load-bearing.

First, the theorem is **positive-topology only**. The implication (25) is what converts a source-weighted chord return into a near-maximal complex barycenter. Signed or complex aggregate synthesis can cancel source mass and is not ruled out by (9).

Second, the shell width `Delta` is fixed. If `Delta=Delta_a->0`, both the normalization and the mesh accounting change, and (22) need not provide the same fixed-height separation.

Third, the `13/30` endpoint is not obtained. The proof requires a fixed margin twice: once in the short-interval PNT and once in the phase-variation estimate. The safe statement is `13/30-epsilon` for arbitrary fixed positive `epsilon`.

Fourth, this theorem says nothing pointwise once `|t|` exceeds the complementary short-interval corridor. Almost periodicity guarantees eventual returns for every fixed `a`, so no all-height no-return statement is possible. `NB-195` remains the applicable statement there: returns are sparse in measure, but isolated near-maximal values are still logically available.

Finally, (18) deliberately uses only local density, not the deeper large-value machinery of Guth--Maynard. The exponent inherited from Corollary 1.3 is therefore a theorem-dependent frontier, not evidence that `13/30` is a natural phase transition of the Euler shell.

## Research consequence

The isolated-positive-return problem is now pointwise closed throughout the coupled corridor

\[
\limsup \frac{a_T\log(2T)}{r_0}<\frac{13}{30}.
\]

The live positive-recurrence frontier begins only beyond that complementary short-interval scale. A useful next theorem should either control isolated near-maximal values for `|t|>=x_a^(13/30-o(1))` by genuinely source-specific separated-large-value information, or show that a weaker **weighted local-density** statement suffices to push the Riemann-sum approximation farther than coordinatewise prime resolution. In parallel, signed/complex aggregate acquisition remains structurally open because positivity is essential to the present obstruction.