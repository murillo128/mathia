# NB-199 — Diagonal Brun–Titchmarsh localizes vanishing positive Euler returns to the logarithmic Mellin endpoint

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + ENDPOINT-DIAGONALIZATION + BRUN-TITCHMARSH + NB-198-EXTENSION`.

`NB-198` proves a fixed-exponent statement: for every fixed `beta>0`, the normalized positive Euler shell cannot make a sufficiently accurate return while `|t|<=x_a^(1-beta)`. Its certified gap is proportional to `beta`, but the proof chooses its auxiliary height and small-`a` thresholds only after fixing `beta`. Therefore `NB-198` cannot simply be diagonalized by substituting a shrinking `beta=beta_a` in its final theorem.

Tracking the same Brun--Titchmarsh argument before those thresholds are frozen gives a genuinely uniform endpoint estimate. Write

\[
x_a=e^{r_0/a},\qquad X_a:=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

and retain the normalized full positive von-Mangoldt shell

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

There are constants `U_0>1`, `c>0`, and `a_0>0`, depending at most on `r_0` and `Delta`, such that for `0<a<a_0` and

\[
X_a^2\le |t|\le \frac{x_a}{U_0X_a},
\]

one has

\[
\boxed{
\mathcal A_a(t)
\ge
c\,
\frac{
\log\!\left(\dfrac{x_a}{|t|X_a}\right)
}{X_a}.
}
\tag{1}
\]

Thus the fixed-power gap of `NB-198` continues, with its correct shrinking size, through every polylogarithmic endpoint layer down to a constant multiple of `x_a/log x_a`. In particular, if a return in this range has accuracy `mathcal A_a(t)<=eta`, then

\[
\boxed{
|t|
\ge
\frac{x_a^{\,1-C\eta}}{\log x_a}
}
\tag{2}
\]

for another constant `C>0`. If `eta_a=o(1/log x_a)=o(a)`, no such high-ordinate return can occur below `x_a/(U_0 log x_a)`. The positive endpoint escape is therefore narrower than the qualitative `x_a^(1-o(1))` frontier left by `NB-198`: super-`a`-accurate recurrence is forced into the final logarithmic Mellin layer.

## Derivation

### 1. Choose the phase window from the available spatial resolution

By symmetry take `t>0`. Put

\[
U:=\frac{x_a}{tX_a},
\qquad
L:=\log U.
\tag{3}
\]

In the range of (1), `U>=U_0` and hence `L>=log U_0>0`. Choose a small absolute constant `kappa>0` and set

\[
\delta:=\kappa\frac{L}{X_a}.
\tag{4}
\]

After increasing `U_0` and shrinking `a_0`, we may assume `0<delta<1`. Let

\[
W_{t,\delta}
:=
\left\{
 u\in[x_a,y_a):
 \operatorname{dist}(t\log u,2\pi\mathbb Z)\le\delta
\right\}.
\tag{5}
\]

The complete phase windows have centers `u_k=exp(2 pi k/t)` and lengths

\[
H_k=2u_k\sinh(\delta/t).
\tag{6}
\]

Since `sinh z>=z` for `z>=0`, every complete component meeting the shell satisfies, up to an inessential shell-boundary constant,

\[
H_k
\gg
\delta\frac{x_a}{t}
=
\kappa U L.
\tag{7}
\]

Choose `U_0` so large that

\[
\log H_k\ge \frac12L
\tag{8}
\]

for every such component. This is the endpoint replacement for the fixed-power inequality `log H_k>=beta log x_a` used in `NB-198`.

### 2. Brun--Titchmarsh converts window length into an occupancy bound

The arbitrary-interval Brun--Titchmarsh inequality used in `NB-198`,

\[
\pi(u+H)-\pi(u)\le \frac{2H}{\log H}\qquad(H\ge2),
\tag{9}
\]

implies, by the same monotonic-weight comparison as there, that the prime contribution in one favorable component is bounded by

\[
\sum_{p\in I_k}\frac{\log p}{p^{1+a}}
\ll_{r_0,\Delta}
\frac{X_a}{\log H_k}
H_k u_k^{-1-a}.
\tag{10}
\]

Summing components and enlarging the two shell-boundary fragments to complete windows gives

\[
\sum_{\substack{x_a\le p<y_a\\p\in W_{t,\delta}}}
\frac{\log p}{p^{1+a}}
\ll
\frac{X_a}{L}
\int_{W_{t,\delta}}u^{-1-a}\,du.
\tag{11}
\]

In logarithmic coordinates `u=x_a e^v`, `0<=v<=Delta`, the favorable set has period `2 pi/t` and duty cycle `delta/pi`. Elementary periodic averaging therefore yields

\[
\frac{
\int_{W_{t,\delta}}u^{-1-a}\,du
}{
\int_{x_a}^{y_a}u^{-1-a}\,du
}
\ll_\Delta
\delta+\frac1t.
\tag{12}
\]

The prime number theorem gives, as in `NB-198`,

\[
D_a
=
\int_{x_a}^{y_a}u^{-1-a}\,du+o(1)
=
e^{-r_0}\Delta+o(1),
\tag{13}
\]

while proper prime powers contribute `o(1)` absolute shell mass. Hence the normalized favorable mass

\[
M_a(t,\delta):=
\sum_{n\in W_{t,\delta}}w_{n,a}
\]

satisfies

\[
M_a(t,\delta)
\ll
\frac{X_a}{L}
\left(\delta+\frac1t\right)
+o(1).
\tag{14}
\]

Substituting (4) gives

\[
M_a(t,\delta)
\ll
\kappa+
\frac{X_a}{Lt}+o(1).
\tag{15}
\]

The lower-height assumption `t>=X_a^2` makes the second term `o(1)` uniformly because `L>=log U_0`. Choosing `kappa` sufficiently small, then taking `a` sufficiently small, gives for example

\[
\boxed{M_a(t,\delta)\le\frac12.}
\tag{16}
\]

No fixed exponent margin has been used.

### 3. Positive mass turns occupancy into a quantitative return gap

Outside `W_(t,delta)`,

\[
|e^{-it\log n}-1|
\ge
2\sin(\delta/2).
\tag{17}
\]

Because all `w_(n,a)` are nonnegative, (16) implies

\[
\mathcal A_a(t)
\ge
2\sin(\delta/2)(1-M_a(t,\delta))
\gg \delta.
\tag{18}
\]

Using (4) proves (1).

If `A_a(t)<=eta`, equation (1) gives

\[
\log\!\left(\frac{x_a}{tX_a}\right)
\le C\eta X_a.
\tag{19}
\]

Exponentiating and recalling `X_a=log x_a` gives (2):

\[
t
\ge
\frac{x_a e^{-C\eta\log x_a}}{\log x_a}
=
\frac{x_a^{1-C\eta}}{\log x_a}.
\]

For `eta=o(1/X_a)`, (19) would force `U=1+o(1)`, contradicting `U>=U_0`; hence such a return cannot occur anywhere in the range of (1).

### 4. Coupled physical blocks inherit a variable accuracy barrier

If a coupled scale `a_T->0` satisfies

\[
X_{a_T}^2\le T,
\qquad
2T\le\frac{x_{a_T}}{U_0X_{a_T}},
\tag{20}
\]

then (1), monotonically weakened at the top of the block, gives

\[
\boxed{
\inf_{t\in[T,2T]}\mathcal A_{a_T}(t)
\ge
c\,
\frac{
\log\!\left(\dfrac{x_{a_T}}{2T X_{a_T}}\right)
}{X_{a_T}}.
}
\tag{21}
\]

For example, if `T` is of order `x_a/(log x_a)^A` with fixed `A>1`, the certified gap is of order

\[
\frac{(A-1)\log\log x_a}{\log x_a}.
\tag{22}
\]

At the last scale covered uniformly here, `T asy x_a/log x_a`, the natural certified gap has fallen to order `1/log x_a asy a`. This identifies a concrete logarithmic endpoint scale that the fixed-`beta` formulation of `NB-198` could not see.

## Stress tests and limits

The logarithmic loss in (1) is not being presented as an intrinsic Nyman threshold. It comes from the specific sieve input `1/log H`: when `t` reaches order `x_a/log x_a` and the return tolerance is order `1/log x_a`, the favorable spatial components have only bounded length. Brun--Titchmarsh can still control them after choosing the fixed constant `U_0`, but it has no remaining logarithmic reserve with which to continue the same argument toward `t asy x_a`.

The lower restriction `t>=X_a^2` is technical and harmless for the endpoint question. Earlier fixed-power results already control much lower ordinates with much larger gaps. It is imposed here only so the two incomplete phase periods in (12) remain negligible after multiplication by `X_a/L`; no claim is made that `X_a^2` is sharp.

Positivity is again load-bearing. Equation (18) discards the favorable mass and keeps the unfavorable mass with the same sign. A signed or complex Euler aggregate may cancel between phase sectors, so neither (1) nor (2) transfers to the signed-synthesis frontier of `NB-187`--`NB-193`.

The result is also still an acquisition obstruction rather than a theorem about the optimal Nyman--Beurling distance. It does not show that a successful approximant must realize a positive shell return, and therefore it does not imply RH or a new approximation rate.

## Prior-art and representation boundary

The only load-bearing external estimates are already anchored in `SOURCES.md`: the Montgomery--Vaughan arbitrary-interval Brun--Titchmarsh bound and the prime number theorem used to normalize the shell. No new source dependency is required.

The phase-window device itself is classical. Searches around Brun--Titchmarsh phase slicing, near-maximal prime Dirichlet polynomials, pretentious `p^{it}` alignment, and Nyman--Beurling Euler recurrence did not locate this exact diagonal endpoint formulation; that search is a boundary check, not a novelty claim. The derived content here is the uniform choice `delta asy log(x_a/(t log x_a))/log x_a` inside the already established positive Euler-shell geometry, which turns a fixed-exponent obstruction into the explicit variable gap (1).

The representation audit is therefore narrow. Any positive prime-supported shell with comparable total mass and the same arbitrary-interval sieve upper bound would satisfy an analogous estimate. What is source-specific is the actual von-Mangoldt weighting, the negligible proper-prime-power remainder, and the Mellin phase `t log n` supplied by the Euler side of the Nyman program.

## Consequence for the research frontier

`NB-198` left the endpoint as `t=x_a^(1-o(1))`, which still covers many very different scales. Equation (1) resolves a substantial portion of that ambiguity: a return whose accuracy tends to zero must approach exponent one at the matching quantitative rate, and an `o(a)` positive return cannot occur before the final `x_a/log x_a` layer at high ordinate.

The surviving positive-source question is now genuinely local: what can be said when the favorable phase windows have bounded or sublogarithmic spatial length, roughly `t>=x_a/log x_a`? Pushing further requires information qualitatively different from the logarithmic denominator in Brun--Titchmarsh, or a direct argument about isolated near-maximal values of the actual Euler polynomial. The independent signed/complex acquisition route remains open for the separate reason that it lacks the monotone occupancy implication altogether.
