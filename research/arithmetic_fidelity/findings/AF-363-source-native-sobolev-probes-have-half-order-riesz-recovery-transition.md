# AF-363 — source-native Sobolev probes have a half-order Riesz recovery transition

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-RELATIVE`, `QUANTITATIVE-FIDELITY`, `STABILITY-GATE`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

AF-362 reduces recovery of any declared linear target through small-order Riesz smoothing to the exponential moment of that target's energy in the scaled log-frequency coordinate. A natural unresolved question is whether a target defined **before** the Riesz multiplier actually pays the full exponentially broad-band condition number from AF-361.

There is a sharp half-order answer for the canonical Sobolev/Bessel-potential probes of the endpoint arithmetic profile.

Retain AF-358--AF-362's logarithmically normalized endpoint profile

\[
E_0(y)=e^{-y/2}\mathcal R_0[\Lambda-1](e^y)
\]

and, under RH, its positive zero-frequency coordinates indexed by distinct ordinates `gamma`. On the exponential band

\[
\mathcal B_{\delta,T}(v)
=
\{\gamma:T<\gamma\le T e^{v/\delta}\},
\qquad v>0,
\tag{1}
\]

write

\[
x_\gamma=\delta\log(\gamma/T)\in(0,v],
\qquad
c_{\delta,T}=\Gamma(1+\delta)(iT)^{-\delta},
\tag{2}
\]

and let `D` be the diagonal Riesz transport from the endpoint zero-coefficient vector to the order-`delta` vector as in AF-362.

For `beta>=0` and a fixed physical log-location `y_0`, define the finite-band Bessel/Sobolev probe by the target vector

\[
a^{(\beta,y_0)}_\gamma
:=
(1+\gamma^2)^{-\beta/2}e^{i\gamma y_0}.
\tag{3}
\]

Equivalently, `(3)` is the positive-frequency coefficient rule for evaluating the band projection of

\[
(1-\partial_y^2)^{-\beta/2}E_0
\]

at `y_0`. The target is therefore fixed from the endpoint arithmetic profile and the ordinary Bessel-potential scale; it does not depend on `M_\delta`, `c_{\delta,T}`, or the inverse Riesz channel.

Let

\[
K_{\beta}(\delta,T;v)
:=
|c_{\delta,T}|
\frac{\|D^{-*}a^{(\beta,y_0)}\|_2}
{\|a^{(\beta,y_0)}\|_2}
\tag{4}
\]

be AF-362's target-relative recovery modulus after removing the common lower-edge attenuation. Then, for every fixed `v>0`, along every sequence

\[
\delta\downarrow0,
\qquad
T\to\infty,
\tag{5}
\]

one has the phase transition

\[
\boxed{
K_\beta(\delta,T;v)\longrightarrow
\begin{cases}
e^v,&0\le\beta<\tfrac12,\\[2mm]
1,&\beta>\tfrac12.
\end{cases}
}
\tag{6}
\]

The limit is independent of `y_0`. Thus ordinary point evaluation (`beta=0`) pays the **entire differential bandwidth cost** `e^v`, even though it is only a scalar target, whereas every probe smoothed by more than half a derivative asymptotically pays **none** of that differential cost.

The exponent `beta=1/2` is the unique critical regime. Its target energy is not forced to either edge by the argument below; it accumulates across logarithmic scales. In particular `(6)` deliberately makes no exact critical-limit claim.

The common attenuation is a separate currency. If

\[
u_{\delta,T}:=\delta\log T\to u\in[0,\infty],
\tag{7}
\]

then `|c_{\delta,T}|^{-1}->e^u`, so the absolute target-recovery cost satisfies

\[
\boxed{
\frac{\|D^{-*}a^{(\beta,y_0)}\|_2}
{\|a^{(\beta,y_0)}\|_2}
\longrightarrow
\begin{cases}
e^{u+v},&0\le\beta<\tfrac12,\\[2mm]
e^u,&\beta>\tfrac12,
\end{cases}
}
\tag{8}
\]

with the usual extended-real interpretation when `u=infinity`.

Hence AF-361's two recovery currencies are not merely worst-case operator artifacts. A canonical unsmoothed endpoint probe really does spend both. More than half a derivative of target-side regularity removes the bandwidth currency but **cannot remove the common attenuation currency**.

## Derivation

### 1. AF-362 turns the problem into a weighted zero-counting measure

Equation `(7)` of AF-362 gives uniformly on `(1)`

\[
\left|\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}\right|
=
e^{-x_\gamma}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
\tag{9}
\]

Since the phase in `(3)` has unit modulus, AF-362's exact target formula becomes

\[
K_\beta(\delta,T;v)^2
=
\frac{
\sum_{\gamma\in\mathcal B_{\delta,T}(v)}
(1+\gamma^2)^{-\beta}e^{2x_\gamma}
}{
\sum_{\gamma\in\mathcal B_{\delta,T}(v)}
(1+\gamma^2)^{-\beta}
}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
\tag{10}
\]

Thus only the target-energy distribution across the actual distinct zero ordinates remains to be classified.

Under RH, a classical theorem of Cheer and Goldston gives a fixed positive proportion of simple zeros; in fact their stated bound is greater than `0.67275` for all sufficiently large height. Consequently the number `D(X)` of distinct positive ordinates satisfies, on every sufficiently large dyadic shell,

\[
D(2X)-D(X)\asymp X\log X.
\tag{11}
\]

The upper bound follows from Riemann--von Mangoldt. For the lower bound, if `N_s(X)>=cN(X)` with any fixed `c>1/2`, then

\[
N_s(2X)-N_s(X)
\ge cN(2X)-N(X)
\gg X\log X.
\tag{12}
\]

Every zero counted by `N_s` is a distinct ordinate, which proves `(11)`.

It follows by dyadic summation that, for `U/T->infinity`,

\[
S_\beta(T,U)
:=
\sum_{T<\gamma\le U}(1+\gamma^2)^{-\beta}
\tag{13}
\]

obeys

\[
S_\beta(T,U)
\asymp
\begin{cases}
U^{1-2\beta}\log U,&\beta<\tfrac12,\\
(\log U)^2-(\log T)^2,&\beta=\tfrac12,\\
T^{1-2\beta}\log T,&\beta>\tfrac12.
\end{cases}
\tag{14}
\]

Only the two strict regimes are needed for the exact limits in `(6)`.

### 2. Subcritical targets concentrate all energy at the upper scaled edge

Fix `0<=beta<1/2` and `epsilon in (0,v)`. Put

\[
U=T e^{v/\delta},
\qquad
V=T e^{(v-\varepsilon)/\delta}.
\tag{15}
\]

The target-energy mass with `x_gamma<=v-epsilon` is

\[
\frac{S_\beta(T,V)}{S_\beta(T,U)}.
\tag{16}
\]

Using the upper and lower dyadic bounds behind `(14)`,

\[
\frac{S_\beta(T,V)}{S_\beta(T,U)}
\ll
\left(\frac VU\right)^{1-2\beta}
\frac{\log V}{\log U}
\le
\exp\!\left(-\frac{(1-2\beta)\varepsilon}{\delta}\right),
\tag{17}
\]

which tends to zero. Therefore the probability measures obtained by normalizing the weights in `(13)` and pushing them forward by `x_gamma` converge weakly to `delta_v`.

Because `e^{2x}` is bounded and continuous on `[0,v]`, `(10)` gives

\[
K_\beta^2\to e^{2v},
\tag{18}
\]

proving the first half of `(6)`.

This includes `beta=0`. A band-limited point evaluation assigns equal target energy to every retained zero coordinate. The zero count grows linearly in frequency up to logarithmic factors, so on an exponentially broad band almost all of that target energy sits near its high-frequency edge. The scalar observable therefore sees precisely the modes most attenuated by the Riesz envelope.

### 3. Supercritical targets concentrate at the lower scaled edge

Now fix `beta>1/2` and `epsilon in (0,v)`. Put

\[
V=T e^{\varepsilon/\delta}.
\tag{19}
\]

The target-energy tail with `x_gamma>=epsilon` is bounded by the entire tail above `V`:

\[
\sum_{\gamma\ge V}(1+\gamma^2)^{-\beta}
\ll
V^{1-2\beta}\log V,
\tag{20}
\]

while `(11)` on the first fixed dyadic shell gives

\[
S_\beta(T,U)
\gg
T^{1-2\beta}\log T.
\tag{21}
\]

Hence

\[
\frac{
\sum_{V\le\gamma\le U}(1+\gamma^2)^{-\beta}
}{S_\beta(T,U)}
\ll
\exp\!\left(-\frac{(2\beta-1)\varepsilon}{\delta}\right)
\left(1+\frac{\varepsilon}{\delta\log T}\right)
\longrightarrow0.
\tag{22}
\]

The exponential factor dominates the final parenthesis for every sequence in `(5)`. Thus the normalized target-energy measures converge weakly to `delta_0`, and `(10)` yields

\[
K_\beta^2\to1.
\tag{23}
\]

This proves the second half of `(6)`.

There is also an intrinsic interpretation of the same threshold. Equation `(14)` implies

\[
\sum_{\gamma>0}(1+\gamma^2)^{-\beta}<\infty
\quad\Longleftrightarrow\quad
\beta>\frac12.
\tag{24}
\]

So exactly in the supercritical regime the Bessel-smoothed point probe extends to a bounded linear functional on the full zero-coordinate `ell^2` space. The same half-order threshold that makes point evaluation Hilbert-bounded also prevents high-frequency target energy from following the exponentially widening band edge.

### 4. The critical target is genuinely scale-distributed

At `beta=1/2`, each large dyadic shell contributes order `log X` to `(13)`, so no geometric first- or last-shell domination occurs. Summing the shell bounds gives the middle line of `(14)`.

That is exactly the regime in which the scaled coordinate `x=delta log(gamma/T)` can retain a nontrivial target-energy distribution across `[0,v]`. Determining an exact limiting density from distinct ordinates would require finer local information than the positive-simple-zero proportion used here. No such density is assumed.

The absence of a critical formula is a boundary, not a gap in `(6)`: the theorem classifies the two regimes in which coarse zero counting alone forces an endpoint limit, and identifies `beta=1/2` as the only transition where it does not.

## Arithmetic-fidelity interpretation

The target family `(3)` is useful because it passes AF-362's anti-cheat test. It is defined from the endpoint source profile and a standard Bessel-potential operation before the Riesz multiplier is introduced. Choosing `beta` does not cancel or encode `M_delta`.

The result then gives a concrete meaning to target regularity as a **recovery resource**. For `beta<1/2`, exponentially broad source detail enters the target faster than the target weights suppress it, and the target pays the full differential Riesz condition number. For `beta>1/2`, the target itself suppresses enough high-frequency detail that its energy remains at the lower edge and differential conditioning disappears asymptotically.

But the common scale `T^{-delta}` survives both cases. Target smoothing can decide whether the `v` currency matters; it cannot refund the `u=delta log T` attenuation already paid by every mode in the band. This makes AF-362's open accounting problem concrete:

\[
\text{absolute target cost}
=
\text{base attenuation}
\times
\text{target-energy bandwidth cost}.
\tag{25}
\]

For point-like probes the second factor is `e^v`; for more-than-half-smoothed probes it is asymptotically `1`.

The threshold is still **not an arithmetic discriminator**. The proof uses only the Riesz multiplier, the frequency magnitude, and a coarse positive density of distinct zero ordinates. A matched non-arithmetic frequency family with the same shell-density law has the same phase transition. Rational-prime specificity must therefore enter through the incoming endpoint profile or through additional source relations; target-side Sobolev regularity only prices how much of that existing information is stably consumed.

## Boundaries and falsification

- RH is assumed so that the endpoint profile has the real zero-frequency channel used throughout AF-358--AF-362. The target-energy estimates themselves are statements about the positive ordinates once that channel is fixed.
- The distinct-zero shell lower bound `(11)` uses a positive proportion of simple zeros. Cheer--Goldston's classical RH-conditional result is more than sufficient; no simplicity conjecture is assumed.
- The target in `(3)` is finite-band for every `beta`. When `beta<=1/2`, `(24)` says that the corresponding evaluation rule is not a bounded functional on the unrestricted full `ell^2` zero-coordinate space. The actual arithmetic endpoint profile has additional coefficient decay, so this statement must not be misread as nonexistence of the arithmetic point value.
- Equation `(6)` is a stability theorem under AF-362's requirement of exact recovery for every finite-band endpoint vector. A smaller model class of admissible endpoint vectors could have a cheaper inverse if it supplies additional relations.
- The phase `e^{i gamma y_0}` plays no role in the Hilbert-noise cost because AF-362 depends on `|a_gamma|^2`. A phase-sensitive noise model or nonlinear target would be a different problem.
- `beta>1/2` removes only the differential `e^v` factor. If `delta log T->infinity`, the absolute inverse remains unstable because every retained mode is simultaneously attenuated.
- The critical case `beta=1/2` is intentionally not assigned an exact limit. Any stronger claim must supply the required local distinct-zero distribution rather than infer it from Riemann--von Mangoldt alone.

A direct falsification would be a failure of `(11)` under the stated RH/simple-zero input, or a target-energy sequence in one of the strict regimes whose scaled measure does not concentrate at the corresponding edge. The exponential estimates `(17)` and `(22)` make such a counterexample incompatible with the dyadic zero-density bounds.

## Source / prior-art audit

The Bessel-potential/Sobolev interpretation of `(3)` is classical Fourier analysis, and the half-derivative threshold for bounded point evaluation in one dimension is standard Sobolev mathematics. AF-358 already records the closely related Sobolev--Besicovitch embedding literature and derives the half-order threshold for the zeta-zero spectrum. No novelty is claimed for those functional-analytic ingredients.

The zero-density input is classical. A. Y. Cheer and D. A. Goldston, **“Simple zeros of the Riemann zeta-function,”** *Proceedings of the American Mathematical Society* **118** (1993), 365--372, DOI `10.1090/S0002-9939-1993-1132849-0`, proves under RH that more than `67.275%` of the zeros are simple; only the much weaker consequence `(11)` is used here. Current stronger simple/distinct-zero results are therefore unnecessary to the argument.

The exact target-recovery formula is inherited from AF-362 and is the finite-dimensional diagonal form of classical Picard/source-condition reasoning for inverse problems. Target regularity controlling inverse stability is established inverse-problems prior art; this finding does not claim otherwise.

A targeted prior-art search across Riesz means, Sobolev/Bessel-potential point probes, zeta-zero almost-periodic expansions, and Picard/source-condition recovery did not locate the combined phase law `(6)` for this moving Riesz endpoint channel. Absence from that search is not evidence of novelty. The durable Mathia result is narrower: a source-defined target family turns AF-362's abstract target moment into a sharp, falsifiable half-order recovery phase transition and shows exactly which of AF-361's two conditioning currencies a natural downstream observable must pay.