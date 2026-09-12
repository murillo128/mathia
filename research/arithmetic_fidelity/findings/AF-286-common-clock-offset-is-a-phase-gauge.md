# AF-286 — Common clock offset is a phase gauge with inverse-log calibration scale

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `TIMING`, `GAUGE`, `STABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-285 closes the raw observation-count question for the known Dirichlet prefix `1,...,N`: there exists a linearly sized unweighted subset of two-prime mixed samples whose nominal least-squares inverse is uniformly stable under additive sample error. The next acquisition resource is timing precision. A first exact distinction is that a **common clock-origin error is not ordinary additive noise**. It acts as a diagonal phase gauge on the coefficient vector.

Let

\[
F(c+it)=\sum_{n=1}^N b_n e^{-it\log n}
\]

and let `t_1,...,t_q` be any nominal sampling times whose observation matrix

\[
A_{j,n}=e^{-it_j\log n}
\]

has full column rank. AF-285 supplies such a set with `q<=8N` inside the two-prime mixed square. If every requested time is shifted by the same unknown offset `tau`, then the observed vector is

\[
\widetilde y=A D_\tau b,
\qquad
D_\tau=\operatorname{diag}(1^{-i\tau},2^{-i\tau},\ldots,N^{-i\tau}).
\]

Consequently:

1. the nominal exact least-squares decoder returns **exactly** `D_tau b`, not `b`;
2. if `tau` is unknown and the source class permits arbitrary complex coefficients, `(b,tau)` is not identifiable: the same observations are produced at nominal clock origin by the coefficient vector `D_tau b`;
3. the worst-case relative coefficient displacement caused by an unknown common offset of radius `T` is exactly

\[
R_N(T)
:=
\sup_{|\tau|\le T}\sup_{b\ne0}
\frac{\|D_\tau b-b\|_2}{\|b\|_2}
=
\begin{cases}
2\sin\!\left(\dfrac{T\log N}{2}\right),&0\le T\le \dfrac{\pi}{\log N},\\[1.2ex]
2,&T\ge \dfrac{\pi}{\log N};
\end{cases}
\]

4. therefore, for any fixed target distortion `0<rho<2`, guaranteeing `R_N(T)<=rho` is equivalent to

\[
\boxed{
T\le
\frac{2\arcsin(\rho/2)}{\log N}.
}
\]

Thus the common-clock calibration scale is sharply

\[
\boxed{T=\Theta(1/\log N)}.
\]

In a fixed time unit, a binary clock quantizer whose worst-case rounding uncertainty is half a step therefore needs only `Theta(log log N)` **fractional** bits to keep a fixed worst-case relative coefficient distortion. This is far milder than the `Theta(N)` mixed-degree/time-horizon growth of AF-283--AF-285.

The result also separates common clock drift from independent per-sample jitter. For arbitrary offsets `|tau_j|<=T`, AF-285 gives the rigorous sufficient bound

\[
\|\widehat b-b\|_2
<
\frac{64\sqrt2}{27}
T\log N\,\|b\|_1.
\]

Hence independent jitter is source-norm dependent, whereas a common offset is an exact unitary gauge. The common-offset family is a special case of adversarial per-sample jitter, so any uniform relative-jitter theorem must at least respect the `Omega(1/log N)` calibration obstruction above.

## Exact common-offset factorization

For a nominal time `t_j`, the shifted observation is

\[
\begin{aligned}
F(c+i(t_j+\tau))
&=\sum_{n=1}^N b_n e^{-i(t_j+\tau)\log n}\\
&=\sum_{n=1}^N
\left(e^{-it_j\log n}\right)
\left(e^{-i\tau\log n}b_n\right).
\end{aligned}
\]

Therefore the complete shifted sample vector satisfies

\[
\widetilde y=A D_\tau b.
\]

Because `A` has full column rank,

\[
A^\dagger A=I_N,
\]

and the nominal least-squares decoder gives

\[
\boxed{
A^\dagger\widetilde y=D_\tau b.
}
\]

No condition number enters this identity. Common timing offset does not perturb the nominal frame arbitrarily; it moves the source along the one-parameter unitary orbit

\[
b\mapsto D_\tau b.
\]

More generally, for any real `epsilon`,

\[
A D_\tau b
=
A D_{\tau-\epsilon}(D_\epsilon b).
\]

Thus the data determine only the equivalence class of the pair `(b,tau)` under

\[
(b,\tau)
\sim
(D_\epsilon b,\tau-\epsilon)
\]

unless some extra clock-origin marking or source constraint breaks that gauge.

This is a direct instance of the line's general fidelity principle: a missing piece of acquisition provenance becomes an exact symmetry of the compressed observations.

## Exact worst-case calibration law

Since `D_tau-I` is diagonal,

\[
\sup_{b\ne0}
\frac{\|(D_\tau-I)b\|_2}{\|b\|_2}
=
\|D_\tau-I\|_{2\to2}
=
\max_{1\le n\le N}
|e^{-i\tau\log n}-1|.
\]

Using

\[
|e^{-ix}-1|=2|\sin(x/2)|,
\]

we obtain

\[
\|D_\tau-I\|_{2\to2}
=
2\max_{1\le n\le N}
\left|\sin\frac{\tau\log n}{2}\right|.
\]

If `|tau|<=pi/log N`, all arguments lie in `[0,pi/2]` in absolute value, so monotonicity of sine gives

\[
\|D_\tau-I\|_{2\to2}
=
2\sin\frac{|\tau|\log N}{2}.
\]

Taking the supremum over `|tau|<=T` yields

\[
R_N(T)
=
2\sin\frac{T\log N}{2}
\qquad
\left(T\le\frac\pi{\log N}\right).
\]

If instead `T>=pi/log N`, the allowed offset

\[
\tau=\frac\pi{\log N}
\]

makes the `n=N` phase equal to `-1`, so the relative displacement on the coefficient vector `e_N` is exactly `2`. Since two unit vectors cannot be farther apart than `2` under a diagonal unitary phase rotation,

\[
R_N(T)=2
\qquad
\left(T\ge\frac\pi{\log N}\right).
\]

This proves the displayed piecewise formula.

For `0<rho<2`, define

\[
T_\rho(N)
=
\frac{2\arcsin(\rho/2)}{\log N}.
\]

Because `2 arcsin(rho/2)<pi`, this lies in the monotone regime. Hence

\[
R_N(T)\le\rho
\quad\Longleftrightarrow\quad
T\le T_\rho(N).
\]

The inverse-log dependence is therefore not just a sufficient Lipschitz estimate; it is the exact worst-case calibration threshold for this common-offset model.

## Fractional clock bits

Suppose the time unit is fixed and a binary fractional clock has step

\[
\Delta=2^{-k},
\]

with adversarial rounding uncertainty bounded by `Delta/2`. To guarantee relative coefficient distortion at most `rho`, it is enough and, under this uncertainty model, necessary that

\[
\frac{2^{-k}}2
\le
\frac{2\arcsin(\rho/2)}{\log N}.
\]

Equivalently,

\[
k
\ge
\log_2\log N
-
\log_2\!\bigl(4\arcsin(\rho/2)\bigr).
\]

For fixed `rho`, the required number of fractional timing bits is therefore

\[
\boxed{k=\Theta(\log\log N)}.
\]

This statement prices the **clock-origin resolution**, not the integer bits required to represent the full time horizon. AF-283--AF-285 still use mixed indices of size `Theta(N)`, so absolute timestamps themselves can grow linearly with `N` and require `Theta(log N)` integer bits in a fixed time unit.

## Independent per-sample jitter is a different fidelity class

Now allow separate timing errors `tau_j` with

\[
|\tau_j|\le T.
\]

Let

\[
y_j=\sum_{n=1}^N b_n e^{-it_j\log n},
\qquad
\widetilde y_j
=\sum_{n=1}^N b_n e^{-i(t_j+\tau_j)\log n}.
\]

Then, using `|e^{-ix}-1|<=|x|`,

\[
\begin{aligned}
|\widetilde y_j-y_j|
&\le
\sum_{n=1}^N
|b_n|\,
|e^{-i\tau_j\log n}-1|\\
&\le
T\sum_{n=1}^N |b_n|\log n\\
&\le
T\log N\,\|b\|_1.
\end{aligned}
\]

Apply AF-285's unweighted raw subset and its additive-error bound. Treating the timing mismatch as the samplewise perturbation above gives

\[
\boxed{
\|\widehat b-b\|_2
<
\frac{64\sqrt2}{27}
T\log N\,\|b\|_1.
}
\]

Using `||b||_1<=sqrt(N)||b||_2` yields the coarser uniform relative estimate

\[
\frac{\|\widehat b-b\|_2}{\|b\|_2}
<
\frac{64\sqrt2}{27}
T\sqrt N\log N.
\]

This is a sufficient bound only; no sharp `sqrt N` loss is claimed. The common-offset construction above is already an admissible independent-jitter pattern, so any theorem claiming a breadth-uniform relative inverse under `|tau_j|<=T` must in particular have `T=O(1/log N)` for fixed distortion. The current elementary upper estimate leaves a `sqrt N` gap between that necessary scale and the sufficient scale inherited from AF-285.

That gap is now the precise live timing-stability question: does a better arithmetic subset or a derivative-frame argument remove the `sqrt N` loss for genuinely independent timing jitter, or is extra precision forced by adversarial rowwise phase perturbations?

## Prior art and novelty assessment

No time-shift, jitter, Fourier, or inverse-problem novelty is claimed.

The identity

\[
\sum b_n e^{-i(t+\tau)\lambda_n}
=
\sum (b_ne^{-i\tau\lambda_n})e^{-it\lambda_n}
\]

is the elementary vertical-translation/modulation symmetry of exponential sums and general Dirichlet series. The ordinary Dirichlet case uses `lambda_n=log n`; this sits inside the classical theory of general Dirichlet series going back to Hardy and Riesz, *The General Theory of Dirichlet's Series* (Cambridge, 1915), and modern Bohr/Dirichlet-series treatments.

Sampling-time uncertainty and its frequency-weighted error propagation are likewise classical in signal processing. As a recent adjacent reference, D. H. Shim and J. H. Lee, **“Analytical evaluation of the estimation accuracy in the LS-Prony method for natural frequency estimation under sampling jitter and additive noise,”** *Measurement* 277 (2026), 121450, DOI `10.1016/j.measurement.2026.121450`, studies perturbation propagation for Prony estimation under sampling jitter and additive noise. That literature is methodologically adjacent, not the source of the exact gauge identity proved here.

The retained Mathia contribution is the resource classification inside the AF-283--AF-285 arithmetic channel: common-mode timing error is exactly a source-side phase gauge with a sharp `Theta(1/log N)` calibration radius, while rowwise timing jitter belongs to a different perturbation class and currently has a wider stability gap.

## Boundaries and failure modes

- The exact gauge nonidentifiability assumes the source class permits arbitrary complex coefficient vectors. Real, nonnegative, phase-marked, or otherwise constrained coefficient classes can break the orbit and may allow clock-origin inference.
- The theorem concerns the finite known prefix `1,...,N`. It does not establish timing stability for an unrestricted infinite Dirichlet source.
- `Theta(1/log N)` is the common-offset calibration scale for fixed relative `ell^2` coefficient distortion. It is not the required precision for every timing-noise model.
- The `Theta(log log N)` statement counts fractional bits in a fixed time unit under a worst-case half-step clock-quantization model. It does not include the `Theta(log N)` integer bits needed to represent an `O(N)` time horizon.
- The independent-jitter estimate depends on `||b||_1`; this is unavoidable for the displayed elementary samplewise bound, but the resulting `sqrt N` relative loss may be nonsharp.
- An unknown common offset does not destroy every target. Any downstream functional invariant under `b -> D_tau b` remains identifiable on the quotient. Conversely, phase-sensitive coefficient targets require an external clock marking or a source constraint that fixes the gauge.
- No analytic continuation, zero-location statement, functional equation, or RH consequence follows from this timing theorem alone.

## Decisive audit test

When timing uncertainty is cited as an obstruction to the finite two-prime acquisition mechanism, first classify the timing error structurally.

For a common clock-origin offset, do not model the effect as unrelated additive errors at the selected samples. It factors exactly through the unitary coefficient action `D_tau`, creating a one-parameter gauge ambiguity. The exact worst-case relative coefficient distortion under an offset uncertainty radius `T` is `2 sin(T log N/2)` until saturation at `2`, so fixed distortion requires and only requires `T=Theta(1/log N)`.

For genuinely independent sample jitter, the common-mode gauge is only a lower-bound obstruction; additional rowwise model error can be worse. Any stronger precision claim must therefore identify the extra jitter geometry, source norm, derivative-frame conditioning, or target sensitivity responsible for it rather than attributing the cost to clock uncertainty generically.

## Consequence for the research line

The timing-precision frontier now splits cleanly. **Common clock calibration is not a severe acquisition bottleneck:** its exact coefficient-fidelity radius decays only as `1/log N`, corresponding to `Theta(log log N)` fractional timing bits at fixed distortion. More importantly, an uncalibrated common origin is an exact provenance/gauge ambiguity, so the right repair is a clock/source marking rather than more samples.

The remaining hard timing question is independent jitter. AF-285 plus the elementary perturbation bound gives a sufficient relative scale `T=O(1/(sqrt(N) log N))`, while the common-offset subclass proves only the necessary scale `T=O(1/log N)`. Closing that `sqrt N` gap, preferably by analyzing the derivative frame of an `O(N)` raw subset, is the next concrete stability target. A separate branch may ask which RH-relevant downstream functionals are invariant under the common phase gauge and therefore need no clock-origin lift at all.