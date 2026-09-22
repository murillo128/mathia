# PL-430 — Conjugate-Poisson quadrature makes zero-shift coherence finite-aperture stable

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + QUANTITATIVE-STABILITY-REFINEMENT`.

**Parent finding:** `PL-429`.

## Claim

`PL-429` shows that the imaginary character coherences hidden from same-shift scalar products are exactly recoverable from the real vertical-shift response

\[
R(t)=2\Re C(t),
\qquad
C(t)=\sum_{2\le n\le N}\beta_n e^{it\log n}.
\]

Its global Hilbert-transform formula leaves an analytic concern: coefficientwise Fourier--Bohr recovery must distinguish the increasingly close frequencies `log n`. That concern is real if one wants the individual coefficients `beta_n`, but it is **not** the conditioning barrier for the quantity actually needed by the mod-5 matrix route, namely the aggregate quadrature

\[
\Im C(0)=\sum_{n=2}^N\Im\beta_n.
\]

There is an explicit regularized finite-aperture estimator whose error depends on the fixed spectral gap `log 2`, the upper bandwidth only through `log N`, and a coefficient-mass bound, but **not on the minimum spacing between distinct `log n`**.

For `epsilon>0` and `T>=epsilon`, define

\[
\boxed{
Q_{\epsilon,T}[R]
:=-\frac1{2\pi}
\int_{-T}^{T}
R(t)\frac{t}{t^2+\epsilon^2}\,dt.
}
\tag{1}
\]

Put

\[
B:=\sum_{n=2}^N|\Im\beta_n|
\le \sum_{n=2}^N|\beta_n|.
\tag{2}
\]

Then

\[
\boxed{
\left|Q_{\epsilon,T}[R]-\Im C(0)\right|
\le
\left(
\epsilon\log N+
\frac{4}{\pi T\log2}
\right)B.
}
\tag{3}
\]

If only an approximate scalar response `\widetilde R` is known on `[-T,T]` with

\[
\|\widetilde R-R\|_{L^\infty[-T,T]}\le\eta,
\tag{4}
\]

then

\[
\boxed{
\left|Q_{\epsilon,T}[\widetilde R]-\Im C(0)\right|
\le
\left(
\epsilon\log N+
\frac{4}{\pi T\log2}
\right)B
+
\frac{\eta}{2\pi}
\log\!\left(1+\frac{T^2}{\epsilon^2}\right).
}
\tag{5}
\]

For any target relative quadrature error `0<delta<=1`, the choice

\[
\epsilon=\frac{\delta}{2\log N},
\qquad
T=\frac{8}{\pi\delta\log2}
\tag{6}
\]

gives deterministic reconstruction error at most `delta B`, while the amplification of a uniform scalar-response error is only

\[
\frac{\eta}{2\pi}
\log\!\left[
1+
\left(
\frac{16\log N}{\pi\delta^2\log2}
\right)^2
\right].
\tag{7}
\]

Thus for fixed accuracy the **vertical-shift aperture is bounded independently of `N`**. Growing support requires a finer Abel regularization scale `epsilon~1/log N`, and uniform measurement/theorem error is amplified only logarithmically in that scale. Near-collisions such as `log(n+1)-log n~1/n` do not force a shift horizon of order `n` when the target is `Im C(0)` rather than the individual Fourier coefficients.

This materially sharpens the analytic frontier after `PL-429`. A useful arithmetic theorem need not resolve the whole `log n` spectrum coefficient by coefficient. It is enough to control the scalar shifted-product response on a bounded shift interval, with an error strong enough to survive the explicit logarithmic loss in (5), together with a usable bound on `B`.

## 1. Conjugate-Poisson regularization diagonalizes the one-sided spectrum

Let

\[
\beta_n=a_n+i b_n,
\qquad
\omega_n=\log n>0.
\]

Then

\[
R(t)
=2\sum_n
\left(a_n\cos(\omega_nt)-b_n\sin(\omega_nt)\right).
\tag{8}
\]

The kernel

\[
q_\epsilon(t)=\frac{t}{t^2+\epsilon^2}
\tag{9}
\]

is odd, so the cosine terms vanish in the symmetric integral. The standard conjugate-Poisson Fourier integral, which is also immediate by differentiating the Fourier transform of `(t^2+epsilon^2)^{-1}`, is

\[
\int_{-\infty}^{\infty}
q_\epsilon(t)\sin(\omega t)\,dt
=
\pi e^{-\epsilon\omega},
\qquad \omega>0.
\tag{10}
\]

Hence the infinite-aperture regularized functional is exactly

\[
Q_{\epsilon,\infty}[R]
=\sum_{n=2}^N b_n e^{-\epsilon\omega_n}
=\sum_{n=2}^N b_n n^{-\epsilon}.
\tag{11}
\]

This is the Abel-regularized quadrature. Since `1-e^{-x}<=x` for `x>=0` and `omega_n<=log N`, we obtain

\[
\left|
Q_{\epsilon,\infty}[R]-\Im C(0)
\right|
\le
\epsilon\log N\,B.
\tag{12}
\]

The upper bandwidth therefore enters only through the regularization bias. No separation between two distinct positive frequencies is used.

## 2. Truncating the shift aperture costs only the fixed `log 2` gap

For `T>=epsilon`, the positive function

\[
q_\epsilon(t)=\frac{t}{t^2+\epsilon^2}
\]

is decreasing on `[T,infinity)` and satisfies `q_epsilon(T)<=1/T`. Dirichlet's oscillatory-integral bound gives, for every `omega>0`,

\[
\left|
\int_T^\infty q_\epsilon(t)\sin(\omega t)\,dt
\right|
\le
\frac{2q_\epsilon(T)}{\omega}
\le
\frac{2}{T\omega}.
\tag{13}
\]

For one coefficient `b_n`, the two symmetric tails therefore contribute at most

\[
\frac{4|b_n|}{\pi T\omega_n}.
\tag{14}
\]

Because the arithmetic source has no `n=1` term,

\[
\omega_n=\log n\ge\log2.
\tag{15}
\]

Summing (14) gives

\[
\left|
Q_{\epsilon,T}[R]-Q_{\epsilon,\infty}[R]
\right|
\le
\frac{4B}{\pi T\log2}.
\tag{16}
\]

Combining (12) and (16) proves (3).

The load-bearing spectral fact is therefore the **gap from zero frequency**, not pairwise spacing within the positive spectrum. This distinction is specific to reconstructing the single aggregate quadrature at zero shift. If one asks for each `beta_n` separately, the Fourier-resolution warning in `PL-429` remains valid.

## 3. Uniform scalar-response error has only logarithmic amplification

For an additive response error

\[
E(t)=\widetilde R(t)-R(t),
\qquad |E(t)|\le\eta,
\]

one has directly

\[
|Q_{\epsilon,T}[E]|
\le
\frac{\eta}{2\pi}
\int_{-T}^T
\frac{|t|}{t^2+\epsilon^2}\,dt.
\tag{17}
\]

The integral is elementary:

\[
\int_{-T}^T
\frac{|t|}{t^2+\epsilon^2}\,dt
=
\log\!\left(1+\frac{T^2}{\epsilon^2}\right).
\tag{18}
\]

This proves (5). Unlike the principal-value kernel `1/t`, the regularized kernel is nonsingular at zero, so a uniform theorem error can be propagated quantitatively without assuming cancellation in that error.

Choosing (6) splits the deterministic error budget evenly:

\[
\epsilon\log N=\frac\delta2,
\qquad
\frac4{\pi T\log2}=\frac\delta2,
\tag{19}
\]

which proves (7).

The tradeoff is now explicit. To obtain `o(B)` rather than a fixed fractional accuracy, one may let `delta=delta_N->0`; then the required aperture grows only like `1/delta_N`, while the regularization scale shrinks like `delta_N/log N`. The theorem-level scalar error must beat the logarithmic factor in (7). Nothing in this estimate requires resolving adjacent frequencies individually.

## 4. The coefficient-mass term has an operator bound

In the finite-window notation of `PL-429`, write `G=T^*T`. The coefficient of `e^{it\log n}` is

\[
\beta_n=\overline{b_n}(Ga)_n.
\tag{20}
\]

Consequently

\[
\sum_n|\beta_n|
\le
\|b\|_2\,\|Ga\|_2
\le
\|T\|^2\|a\|_2\|b\|_2.
\tag{21}
\]

Thus the stability estimate can be closed by an ordinary operator/coefficient-energy bound; it does not intrinsically contain the support cardinality. In a concrete prime-window normalization, the relevant task is to compare this upper bound with the covariance scale at which the `PL-421` `1/4` margin is tested.

Equation (21) is only an a priori bound. It does not assert that the arithmetic normalization makes `B` bounded or small enough; that has to be checked in the source-transfer theorem actually used.

## 5. Consequence for the mod-5 matrix route

The three imaginary coherences isolated in `PL-428` are values `Im C_{jk}(0)`. `PL-429` proves exact recovery from the full shift response, but its Fourier-Bohr coefficient formula might suggest that an arithmetic theorem must track shifts out to the inverse spacing of nearby `log n` frequencies.

Equations (3)--(7) show that this is unnecessarily strong for the matrix-admission target. For a fixed desired margin in the `PL-421` spectral-floor test, the vertical aperture can remain bounded. What must instead be proved is a scalar shifted-product estimate of the form

\[
\widetilde R_{jk}(t)=R_{jk}(t)+E_{jk}(t),
\qquad |t|\le T_\delta,
\tag{22}
\]

with `E_jk` uniformly small enough that

\[
\|E_{jk}\|_\infty
\log\!\left(1+\frac{T_\delta^2}{\epsilon_\delta^2}\right)
\tag{23}
\]

is below the available covariance margin, and with a compatible bound for the coefficient mass `B_jk`. Since `epsilon_delta~delta/log N`, the regularization loss is logarithmic in `log N` for fixed `delta`.

This is a materially easier analytic target than coefficientwise spectral tomography, although it is still not supplied by the current GRH-free literature audited in `PL-427`--`PL-429`. In particular, nothing here removes the source/model replacement problem or the circularity of GRH-based zero-side estimates.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. The Hilbert transform/analytic-signal identity, the Poisson and conjugate-Poisson kernels, Abel damping `e^{-epsilon|omega|}`, and Dirichlet bounds for oscillatory tails are standard harmonic analysis. The sine-integral form of the unregularized truncation gives the same `1/(T omega)` tail scale. No novelty is claimed for any of those facts.

A targeted literature search around analytic signals, conjugate-Poisson regularization, truncated Hilbert transforms, finite-window Kramers--Kronig recovery, and vertical shifts of Dirichlet series found substantial generic prior art on the individual ingredients and on the ill-posedness of generic finite-interval analytic continuation. It did not locate a theorem whose content is the line-specific conclusion above: for the `PL-429` prime-log response, the mod-5 **zero-shift aggregate coherence** has a gap-controlled finite-aperture estimator, so adjacent `log n` spacing is not the relevant conditioning parameter.

That conclusion is an elementary specialization, not a claim of a new harmonic-analysis theorem. Its value is to correct the analytic target of this research line: the close-frequency warning applies to coefficient recovery, whereas the matrix cone only needs a sign-of-frequency quadrature functional.

## 7. Adversarial audit and boundaries

1. **This does not recover individual Fourier-Bohr coefficients stably.** Near-collisions among `log n` remain a serious obstacle for coefficientwise tomography. The result concerns only `Im C(0)`, for which every positive frequency receives the same Hilbert-transform sign.
2. **The zero-frequency gap is essential.** If an `n=1` term is present, its imaginary coefficient cannot be recovered from the real response. The von Mangoldt source has no such term, exactly as in `PL-429`.
3. **The support must have a finite upper energy for the displayed Abel-bias bound.** For support `n<=N`, this is `log N`. Infinite systems require a weighted summability condition such as `sum |beta_n| log n<infinity` or a separate limiting argument.
4. **Small uniform response error is still arithmetic input.** Formula (5) does not produce an estimate for `R(t)`; it only quantifies what an external scalar theorem would have to deliver.
5. **Coefficient mass may be the real conditioning bottleneck.** If `B` is much larger than the covariance scale, fixed relative quadrature accuracy is insufficient. Equation (21) exposes rather than solves that normalization issue.
6. **Centering must still shift consistently.** The estimator is linear, but any deterministic source/model subtraction must be modulated and transported exactly as required in `PL-429`.
7. **No analytic continuation or zero localization is inferred.** All derivations concern finite exponential polynomials and scalar-response stability. They neither assume nor prove RH/GRH.

## Consequence

The next analytic pass should not demand enough vertical-shift range to resolve the spacing `log(n+1)-log n`. For the actual mod-5 matrix gate, the relevant target is instead:

\[
\boxed{
\text{bounded-aperture uniform scalar shifted-product control}
+\text{coefficient-mass control}
\Longrightarrow
\text{stable recovery of the missing complex covariance}.}
\]

If an unconditional or genuinely weaker-than-RH variance/explicit-formula theorem can provide (22) with an error surviving the logarithmic factor in (5), the representation obstruction of `PL-428` remains bypassed without a growing shift horizon. If no such theorem exists because the required bounded-shift uniformity itself imports critical-line control, that is now the analytic obstruction to isolate.