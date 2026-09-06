# PL-187 — Diverging affine phase windows flatten every bounded prime target in averaged `L^2`

## Claim

`PL-180`--`PL-184` show pointwise PNT/short-interval flattening for the canonical affine Kronecker phase through the currently controlled phase-resolution horizon, while `PL-186` shows that a genuinely arithmetic target such as `mu(q+h)` escapes every subpower exponent-coordinate cylinder because its large-prime factorization tail remains uncontrolled. A natural residual escape is therefore to move to a high vertical frequency and retain that hard target.

Frequency **averaging** does not preserve this escape. On every fixed macroscopic prime band, any bounded target is washed out in mean square as soon as the width of the affine phase window diverges, independently of the location of that window.

Fix constants

\[
0<a<b<\infty,
\]

let `h=h_X>=1` be arbitrary, and put

\[
\mathcal P_X=\{q\text{ prime}:aX<q\le bX\},
\qquad M_X=|\mathcal P_X|.
\]

For coefficients `c_q=c_{q,X}` satisfying `|c_q|<=1`, define

\[
F_{X,h,c}(t)
:=\frac1{M_X}\sum_{q\in\mathcal P_X}
 c_q\exp\!\left(it\log\left(1+\frac hq\right)\right).
\]

Let `I_X` be an arbitrary real interval of length `L_X>0`, with no restriction on its center, and define the effective affine phase width

\[
\Delta_X
:=L_X\frac{h_X}{X+h_X}.
\]

Then, uniformly in `h_X`, in the interval center, and in all coefficient choices with `|c_q|<=1`,

\[
\boxed{
\frac1{L_X}\int_{I_X}|F_{X,h_X,c}(t)|^2dt
\ll_{a,b}
\frac1{M_X}
+
\begin{cases}
\dfrac{1+\log \Delta_X}{\Delta_X},&1\le\Delta_X\le X,\\[6pt]
\dfrac{\log X}{\Delta_X},&\Delta_X\ge X.
\end{cases}
}
\]

Consequently,

\[
\boxed{
\Delta_X\longrightarrow\infty
\quad\Longrightarrow\quad
\frac1{L_X}\int_{I_X}|F_{X,h_X,c}(t)|^2dt\longrightarrow0
}
\]

uniformly for every bounded arithmetic target. In particular this applies to

\[
c_q=\mu(q+h_X),\qquad
c_q=\lambda(q+h_X),
\]

or to any bounded function of the full shifted factorization vector, without requiring any cancellation theorem for those coefficients.

**Evidence/status:** `EXACT-DERIVED + SIEVE-INPUT + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT` for the route

\[
\text{high-frequency affine Kronecker phase}
+\text{broad phase-window averaging}
+\text{hard shifted arithmetic target}
\longrightarrow
\text{RH-sensitive survivor}.
\]

The estimate is a direct nonharmonic-Fourier expansion combined with the same unconditional dimension-two prime-pair upper-bound sieve already audited in `PL-081`. No novelty is claimed for the sieve or for mean-square exponential-sum methods. The durable line-specific conclusion is the width threshold in the affine variable used by `PL-182`: averaging over **any diverging effective phase width** destroys every bounded target, even targets whose pointwise zero-frequency value lies at the shifted-prime parity frontier.

## 1. The affine prime frequencies are a rescaled prime point process

Write

\[
\lambda_h(x)=\log\left(1+\frac hx\right).
\]

Then

\[
\lambda_h'(x)
=-\frac{h}{x(x+h)}.
\]

For `q,r in mathcal P_X`, the mean-value theorem gives a point `xi` between `q` and `r` such that

\[
|\lambda_h(q)-\lambda_h(r)|
=\frac{h|q-r|}{\xi(\xi+h)}.
\]

Because `xi/X` remains in the fixed compact interval `[a,b]`, uniformly for every `h>=1`,

\[
\boxed{
|\lambda_h(q)-\lambda_h(r)|
\asymp_{a,b}
\frac{h}{X(X+h)}|q-r|
=
\frac1X\frac{h}{X+h}|q-r|.
}
\]

Thus the nonlinear affine frequencies are, on a macroscopic prime band, bi-Lipschitz equivalent to the ordinary prime locations with the deterministic scale factor

\[
\rho_X:=\frac{h_X}{X+h_X}.
\]

This is the same factor that appears in the exact phase-resolution parameter of `PL-182`,

\[
\nu=|t|\frac{h}{X+h}.
\]

For a signed phase coordinate `u=t rho_X`, the interval `I_X` therefore has width exactly `Delta_X=L_X rho_X`.

## 2. Every time-window kernel is controlled by additive prime gaps

For distinct `q,r`, define

\[
K_I(q,r)
:=\frac1L\int_I
 e^{it(\lambda_h(q)-\lambda_h(r))}\,dt.
\]

Translation of the interval only multiplies this quantity by a unimodular phase, so its magnitude is independent of the interval center. The elementary integral gives

\[
|K_I(q,r)|
\le
\min\left\{1,\frac{2}{L|\lambda_h(q)-\lambda_h(r)|}\right\}.
\]

Using the frequency comparison above and writing

\[
H_X:=\frac{X}{\Delta_X},
\]

one obtains

\[
\boxed{
|K_I(q,r)|
\ll_{a,b}
\min\left\{1,\frac{H_X}{|q-r|}\right\}.
}
\]

So a phase window of effective width `Delta_X` resolves an ordinary additive prime-gap scale

\[
H_X=\frac{X}{\Delta_X}.
\]

This is the affine analogue of the logarithmic Fourier resolution `H=X/T` in `PL-077` and the prime-support scale in `PL-081`, but the observable here is different: it is one normalized arithmetic readout with arbitrary bounded coefficients rather than the empirical spectrum of the whole Gram matrix.

## 3. The prime-pair sieve makes the normalized off-diagonal mass summable

Expanding the square gives

\[
\frac1L\int_I|F_{X,h,c}(t)|^2dt
=
\frac1{M_X^2}
\sum_{q,r\in\mathcal P_X}
 c_q\overline{c_r}K_I(q,r).
\]

The diagonal contributes at most `1/M_X`. For the off-diagonal part, discard the coefficient phases and group by the additive gap `d=|q-r|`. Let

\[
N_d(X)
:=\#\{q\in\mathcal P_X:q+d\in\mathcal P_X\}.
\]

The dimension-two Selberg/Brun upper-bound sieve used in `PL-081` gives, uniformly for relevant even `d`,

\[
N_d(X)
\ll_{a,b}
\frac{X}{(\log X)^2}\,\mathfrak S_+(d),
\]

where one may take

\[
\mathfrak S_+(d)
=\prod_{\ell\mid d,\ \ell>2}
\frac{\ell-1}{\ell-2},
\]

and `PL-081` records the elementary average estimate

\[
\sum_{d\le Y}\mathfrak S_+(d)\ll Y.
\]

Hence

\[
\sum_{q\ne r}|K_I(q,r)|
\ll_{a,b}
\frac{X}{(\log X)^2}
\sum_{d\ll X}
\mathfrak S_+(d)
\min\left\{1,\frac{H_X}{d}\right\}.
\]

If `1<=H_X<=X`, partial summation yields

\[
\sum_{d\ll X}
\mathfrak S_+(d)
\min\left\{1,\frac{H_X}{d}\right\}
\ll
H_X\left(1+\log\frac{X}{H_X}\right).
\]

If `H_X<=1`, the same average bound gives instead

\[
\sum_{d\ll X}
\mathfrak S_+(d)
\min\left\{1,\frac{H_X}{d}\right\}
\ll H_X\log X.
\]

Finally the prime number theorem gives

\[
M_X\asymp_{a,b}\frac{X}{\log X}.
\]

Dividing by `M_X^2` and substituting `H_X=X/Delta_X` proves the displayed mean-square estimate.

The logarithmic factor is not being interpreted as a new arithmetic constant. It is simply the harmonic tail of the sharp interval kernel after the pair sieve. A compact-Fourier-support time smoothing would alter that tail, but it would only make the same information-loss conclusion stronger, not restore an arithmetic survivor.

## 4. The hard Möbius tail survives pointwise but not after broad phase averaging

`PL-186` isolates the exact parity boundary for the shifted target. For fixed `h`,

\[
\frac1{\pi(X)}\sum_{q\le X}\mu(q+h)
\]

is not currently known to tend to zero for each prescribed shift, while every subpower block of exponent coordinates is already modeled by an independent Kubilius law. The unresolved information is in the nonlocal factorization tail.

The present estimate does **not** solve that pointwise problem. Instead it shows that one can erase it without understanding it. On a macroscopic band, set

\[
c_q=\mu(q+h).
\]

For any phase interval whose effective width `Delta_X` tends to infinity,

\[
\frac1L\int_I
\left|
\frac1{M_X}
\sum_{q\in\mathcal P_X}
\mu(q+h)e^{it\lambda_h(q)}
\right|^2dt
\longrightarrow0.
\]

Thus the unresolved large-prime parity tail cannot be promoted into a robust spectral signal merely by averaging it over a broad high-frequency band. The phase average becomes universal **before** one has learned anything about the arithmetic cancellation of the coefficients themselves.

This is a useful falsification control. Any regularization, trace, spectral density, or experimental statistic that first averages the affine vertical parameter over a window with `Delta_X->infinity` can display cancellation for purely Fourier/sieve reasons even when its zero-frequency arithmetic content remains completely open.

## 5. Relation to the current Kronecker frequency horizon

`PL-182` proves a pointwise theorem for the unweighted affine character throughout

\[
\nu_X
=|t_X|\frac{h_X}{X+h_X}
\le X^{13/15-\eta},
\]

using almost-all short-interval prime counts. It explicitly leaves larger pointwise frequencies open. The present statement is transverse to that horizon: it places **no upper bound on the center frequency** at all. Its control parameter is the width

\[
\Delta_X
=L_X\frac{h_X}{X+h_X}
\]

of the observation window.

Therefore the high-frequency branch now has a sharper information requirement. A candidate above the short-interval-PNT horizon cannot obtain new arithmetic content merely by integrating over a phase band whose normalized width diverges. To escape this finding it must retain at least one of the following genuinely different structures:

- a prescribed or otherwise rigid **pointwise** high frequency;
- a phase window of bounded effective width;
- coefficients or a target that themselves vary with the phase parameter in a justified arithmetic way;
- a joint/nonlocal construction not reducible to a single normalized affine prime sum.

The first two remain live. This finding does not bridge the unresolved pointwise range between current short-interval technology and genuinely ultra-oscillatory estimates.

## 6. Prior art and novelty audit

The ingredients are established and are not claimed as discoveries.

- `PL-081` already derives and audits the required dimension-two prime-pair upper-bound sieve and the bounded-average local factor `mathfrak S_+(d)`, citing Halberstam--Richert and Green--Tao as standard sieve/harmonic-analysis anchors.
- `PL-072` and `PL-077` already place finite-time mean squares of logarithmic frequency systems under the Montgomery--Vaughan/Gallagher nonharmonic-Fourier umbrella. The present calculation changes the frequency set to the **affine** values `log(1+h/q)` and tracks the exact scale `h/(X+h)` used by the current affine branch.
- Green--Tao's Selberg-sieve restriction theory and the broad large-sieve literature are close prior art for the general principle that prime-supported exponential systems become controllable after suitable averaging. A targeted search did not locate a reason to regard the displayed affine-window estimate as a novel theorem; it is best classified as an exact line-specific synthesis of classical ingredients.

The important distinction from `PL-081` is the observable and therefore the threshold. `PL-081` studies the **whole prime Gram spectrum** and needs phase resolution beyond the mean prime-gap scale to force bulk diagonalization. Here the normalized scalar readout carries a factor `M_X^{-2}`; after summing the sieve-controlled pair kernel, every diverging affine phase width already forces its averaged `L^2` mass to zero. No statement about operator-norm Gram convergence follows.

## 7. Adversarial checks and failure modes

- **Mean square is not pointwise cancellation.** The theorem permits exceptional phase values. Indeed, for an arbitrary chosen `t_0`, the programmable coefficients `c_q=e^{-it_0\lambda_h(q)}` make `F(t_0)=1`. Therefore no coefficient-blind pointwise theorem can be inferred from the window estimate.
- **The interval width, not its center, is the control parameter.** Moving the entire window to arbitrarily large frequency changes only harmless phases in the kernel. A high center with bounded `Delta_X` is not covered by the asymptotic flattening conclusion.
- **Macroscopic-band localization is deliberate.** The derivative comparison is uniform on `aX<q<=bX`. A full `q<=X` statement can be assembled by dyadic decomposition plus control of the small-prime mass, but that adds no new arithmetic mechanism and is not needed for the falsification result.
- **The pair-sieve input is upper-bound information only.** No Hardy--Littlewood prime-pair asymptotic, pair-correlation conjecture, or RH input is used.
- **Bounded coefficients are essential to the stated uniformity.** Unbounded weights such as raw `Lambda(q)` require renormalization and can route back into the weighted correlation/explicit-formula channels audited elsewhere in the line.
- **No continuation is present.** The entire argument is finite Fourier analysis plus an unconditional sieve estimate. It cannot by itself single out `Re(s)=1/2` or distinguish the rational zeta zero divisor from a matched sparse control with comparable pair-count bounds.
- **No claim is made about bounded-width high-frequency windows.** Those are precisely where a pointwise or locally coherent arithmetic target could still survive this averaging obstruction.

## Consequence

The affine/Kronecker branch has now separated a pointwise arithmetic frontier from a smoothing artifact. `PL-186` shows that the full shifted Möbius sign can remain hard because of its nonlocal large-prime tail. `PL-187` shows that this hardness disappears from any scalar statistic that averages the affine phase over a window of diverging normalized width:

\[
\boxed{
\text{hard bounded shifted target}
+\text{diverging affine phase-window width}
\quad\Longrightarrow\quad
\text{universal averaged }L^2\text{ flattening}.
}
\]

Accordingly, a surviving non-Haar mechanism should not spend further effort on broad high-frequency phase averages of a single affine prime sum. The live frequency questions are now **pointwise or bounded-width**, or must introduce a justified joint/completed coupling that changes the one-sum Fourier geometry before the averaging step.