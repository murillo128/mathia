# RE-223 — Narrow separated corridors incur a superoscillatory Wiener surcharge

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + CAUSAL-PREDICTION + CORRIDOR-WIDTH-LOWER-BOUND + WIENER-NORM + SUPEROSCILLATION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-217, RE-219, RE-221, RE-222.

RE-217 gives the support-width-blind separated-prediction floor

\[
\log \|\mu_T\|_{TV}\ge (1-o(1))HT
\]

for any finite complex measure supported in `[H,\infty)` whose Fourier transform approximates `1` uniformly on `[-T,T]`. The current constructive predictors, however, live in a **fixed finite corridor**. RE-222 also leaves genuinely degenerate single-center parameters as the only possible escape from its uniform factor-two interior gap. In particular, a collapsing truncation ratio would collapse the available repair corridor toward the forbidden zero-delay frequency.

A finite corridor carries an additional, completely elementary superoscillatory cost. Let `R>1`, let `H>0`, and let `\mu` be any finite complex measure supported on

\[
[H,RH].
\tag{1}
\]

Assume

\[
\sup_{|t|\le T}\left|1-\widehat\mu(t)\right|\le\epsilon,
\qquad 0\le\epsilon<1,
\tag{2}
\]

where

\[
\widehat\mu(t)=\int e^{-iLt}\,d\mu(L).
\tag{3}
\]

Put

\[
q_R:=\cos\frac{\pi}{R+1},
\qquad
n:=\left\lfloor\frac{(R+1)HT}{\pi}\right\rfloor.
\tag{4}
\]

Whenever `n>=1`, one has the nonasymptotic bound

\[
\boxed{
\|\mu\|_{TV}
\ge
(1-\epsilon)q_R^{-n}.
}
\tag{5}
\]

Consequently, for fixed `R` and `HT\to\infty`,

\[
\boxed{
\liminf
\frac{\log\|\mu_T\|_{TV}}{HT}
\ge
B(R):=
\frac{R+1}{\pi}
\log\sec\frac{\pi}{R+1}.
}
\tag{6}
\]

Combining this with RE-217 gives the corridor-sensitive floor

\[
\boxed{
C_{\rm sep}(R)
\ge
\max\{1,B(R)\},
}
\tag{7}
\]

where `C_sep(R)` denotes the RE-217 extremal problem restricted to support in `[H,RH]`.

The new term is strongest when the repair band is narrow. It is strictly decreasing in `R`, diverges as `R\downarrow1`, and tends to zero as `R\to\infty`. The unique corridor ratio at which it meets the unit floor is

\[
\boxed{
R_1=1.4302646063627417\ldots,
\qquad
B(R_1)=1.
}
\tag{8}
\]

Thus any separated predictor family whose leading Wiener exponent approaches the global unit floor must use a corridor at least this wide. More directly for the single-center frontier, if the repair support is `[H,(1+\lambda)H+o(H)]` and the leading Wiener rate is at most two, then necessarily

\[
\boxed{
\liminf\lambda
\ge
0.06242231801357475\ldots .
}
\tag{9}
\]

Therefore the `\lambda\to0` degeneration left open by RE-222 cannot be the route through the factor-two barrier. This conclusion does not use the negative-binomial representation at all; it applies to arbitrary complex repair measures in the same corridor.

## 1. Modulate the forbidden frequency to a superoscillation problem

Define

\[
g(t):=e^{iHt}\widehat\mu(t),
\qquad
f(t):=e^{iHt}.
\tag{10}
\]

Equation (2) is exactly

\[
|g(t)-f(t)|\le\epsilon,
\qquad |t|\le T.
\tag{11}
\]

After the modulation, every source atom has frequency

\[
x=L-H\in[0,(R-1)H],
\tag{12}
\]

whereas the target `f` oscillates at frequency `+H`. The predictor is therefore forced to reproduce a frequency outside its shifted spectral band. This is the standard superoscillatory geometry; the useful point here is that a phase-aligned finite-difference operator gives an exact total-variation price.

Choose

\[
h:=\frac{2\pi}{(R+1)H}
\tag{13}
\]

and define

\[
(D_h u)(t):=u(t+h)+e^{iHh}u(t).
\tag{14}
\]

On the target exponential,

\[
D_h f(t)=2e^{iHh}f(t),
\tag{15}
\]

and hence

\[
|D_h^n f(t)|=2^n.
\tag{16}
\]

The coefficients of `D_h^n` have total absolute mass exactly `2^n`. Therefore, whenever all sample points `t,t+h,\ldots,t+nh` remain in `[-T,T]`, equation (11) gives

\[
|D_h^n g(t)-D_h^n f(t)|
\le\epsilon 2^n,
\tag{17}
\]

so

\[
|D_h^n g(t)|\ge(1-\epsilon)2^n.
\tag{18}
\]

This alignment is why no assumption on the rate at which `\epsilon` tends to zero is required. A generic finite-difference step would amplify the approximation error faster than the target response; the phase in (14) makes the two amplification factors exactly equal.

## 2. Every admissible source frequency is uniformly attenuated

For one shifted source exponential `e^{-ixt}`, `x\in[0,(R-1)H]`, the operator eigenvalue is

\[
e^{-ixh}+e^{iHh}.
\tag{19}
\]

Its modulus is

\[
2\left|\cos\frac{(H+x)h}{2}\right|.
\tag{20}
\]

By (13), as `x` traverses the whole source band,

\[
\frac{(H+x)h}{2}
\in
\left[
\frac{\pi}{R+1},
\pi-\frac{\pi}{R+1}
\right].
\tag{21}
\]

Hence

\[
\left|e^{-ixh}+e^{iHh}\right|
\le
2\cos\frac{\pi}{R+1}
=2q_R.
\tag{22}
\]

Integrating against an arbitrary complex measure and using total variation gives

\[
|D_h^n g(t)|
\le
(2q_R)^n\|\mu\|_{TV}.
\tag{23}
\]

Now take `t=-T` and

\[
n=\left\lfloor\frac{2T}{h}\right\rfloor
=
\left\lfloor\frac{(R+1)HT}{\pi}\right\rfloor.
\tag{24}
\]

All points used by `D_h^n` lie in `[-T,T]`. Combining (18) and (23) proves (5) exactly.

For fixed `R`, division of the logarithm of (5) by `HT` and passage to `HT\to\infty` gives (6). The factor `1-\epsilon` is subexponential whenever `\epsilon` stays bounded away from one; in particular it is harmless for the RE-217 regime `\epsilon_T\to0`.

## 3. The corridor surcharge is monotone and has explicit thresholds

Set

\[
x:=\frac{\pi}{R+1}\in\left(0,\frac\pi2\right).
\tag{25}
\]

Then

\[
B(R)=\frac{-\log\cos x}{x}.
\tag{26}
\]

The derivative with respect to `x` has numerator

\[
x\tan x+\log\cos x.
\tag{27}
\]

That numerator vanishes at `x=0` and has derivative `x\sec^2x>0`. Thus `B` increases with `x` and therefore decreases strictly with `R`. Moreover

\[
B(R)\to\infty
\quad(R\downarrow1),
\qquad
B(R)\sim\frac{\pi}{2(R+1)}
\quad(R\to\infty).
\tag{28}
\]

The numerical constants in (8)--(9) are merely evaluations of this exact monotone formula. The first is the unique solution of `B(R)=1`. For a single-center predictor with truncation ratio `\lambda=N/m`, the delays are

\[
L_j=(m+j)\delta,
\qquad 0\le j\le N,
\tag{29}
\]

so under `m\delta=H+o(H)` its corridor ratio is

\[
R=1+\lambda+o(1).
\tag{30}
\]

The unique solution of

\[
B(1+\lambda)=2
\tag{31}
\]

is

\[
\lambda_2
=0.0624223180135747507901\ldots .
\tag{32}
\]

If a family had `\lambda_m\to0` while its normalized Wiener rate remained at most two, (6) would eventually force a strictly larger rate, and in fact an unbounded one. This proves (9).

More generally, for every finite target rate `M>0` there is a unique `\lambda_M>0` satisfying `B(1+\lambda_M)=M`; any fixed-corridor family of rate at most `M` must have `\liminf\lambda\ge\lambda_M`. Thus a collapsing spectral corridor is never a cheap way to realize superoscillation.

## 4. Relation to RE-217 and to the RE-222 singular frontier

Equation (6) does **not** improve the global RE-217 statement `C_sep>=1`, because `B(R)<1` once `R>R_1` and tends to zero for broad corridors. Its content is geometric rather than a new global constant: the unit floor cannot be approached while the repair frequencies collapse toward the minimum delay.

This matters immediately for the exact real single-center program. RE-222 proves a uniform strict factor-two gap whenever `(alpha,a,lambda)` remains in a compact subset of the contracting parameter domain. A family that attempts to approach or cross the factor-two rate must therefore leave every such compact set. In the **fixed-corridor** version relevant to `C_sep`, `lambda` is already bounded above because the largest delay is `(1+lambda)H+o(H)`. Equation (9) now bounds it away from zero as well for every putative rate-two escape. The truncation coordinate can therefore be made compact; any remaining escape must come from the arc/center geometry itself — for example `alpha\to0`, loss of contraction margin, or an unbounded/endpoint center — together with genuine cancellation of the exact remainder.

This is a stronger localization than RE-222 alone, and it is representation-independent. Replacing the negative-binomial basis, using complex coefficients, or splitting one coefficient among many atoms does not evade (5), because only spectral support and total variation enter the proof.

The current explicit RE-218 predictor has a much broader corridor, so (6) does not sharpen its `5.996390` upper rate. The finding should therefore not be read as numerical progress on that endpoint. Its role is to rule out one entire degenerating direction and to add a corridor-width constraint to any future attempt to reach `C_sep=1`.

## 5. Prior-art boundary and adversarial checks

The modulation in (10) is the classical superoscillation picture: a band-limited combination locally reproduces a frequency outside its own spectral band only by paying a large coefficient/dynamic-range cost. Ferreira and Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Transactions on Signal Processing **54** (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, study the exponential energy/dynamic-range cost of such behavior. Difference-based band-limited prediction is also classical; Mugler and Splettstoesser, *Difference Methods for the Prediction of Band-Limited Signals*, SIAM Journal on Applied Mathematics **46** (1986), 930--941, DOI `10.1137/0146055`, is a direct neighboring reference. No novelty is claimed for superoscillation or finite differences themselves.

Neither external source is load-bearing for (5): the phase-aligned operator proof is finite and self-contained. The line-specific point is the exact total-variation lower bound in the `[H,RH]` repair geometry and its use to price the singular corridors left by RE-222. No `SOURCES.md` update is required.

Several boundary checks are decisive. The proof allows arbitrary complex or continuous measures, so sign cancellation and atom splitting do not help. As `R\downarrow1`, `q_R\downarrow0`; this correctly reflects that a single delay near `H` cannot mimic the zero-delay constant on an expanding symmetric interval. As `R\to\infty`, the new bound vanishes and RE-217's support-width-blind unit floor takes over, so there is no contradiction with broad-corridor predictors. The strict separation `H>0` is essential: for `H=0`, `\delta_0` predicts the constant with total variation one. Finally, the factor `(R+1)/pi` uses the full symmetric interval of length `2T`; on a one-sided observation window the same stencil would have only half as many admissible steps.

## Research consequence

A low-Wiener-cost separated predictor cannot obtain its savings by collapsing the repair band onto the first admissible delay. Quantitatively, approaching the global unit spectral floor requires an upper/lower delay ratio of at least `1.430264606...`, and any real single-center exact-remainder attempt to reach the factor-two boundary must keep `N/m` at least `0.062422318...` asymptotically.

The next single-center question is therefore narrower than after RE-222: with the truncation ratio confined to a compact positive interval, can a singular arc/center scaling exploit exact incomplete-beta cancellation to cross the factor-two barrier, or does the interior obstruction extend uniformly through those remaining boundary regimes? A genuinely different multi-center/minimax predictor remains a separate live route toward the global `C_sep=1` problem.