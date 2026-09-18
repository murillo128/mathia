# RE-215 — Continuous Kaiser window sharpens the prime-count capacity bound

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + CONTINUOUS-KAISER-BESSEL-TEST + WEIGHTED-PRIMITIVE-LOWER-BOUND + ORDINARY-PRIME-SOURCE + BOUNDED-MULTIPLICITY-CAPACITY + NO-KV-FIDELITY-ASSUMPTION + SECOND-ORDER-HEIGHT-SHARPENING`.

**Parent findings:** RE-213, RE-214.

`RE-214` separates the raw bounded-multiplicity capacity obstruction from Korobov--Vinogradov fidelity. Its source-independent converse uses two ordinary Kaiser factors. The square is needed there because one standard Kaiser transform has a nonintegrable `1/x` absolute tail in the weighted-primitive norm, and this produces

\[
R\gg \frac{e^{HT}}{(HT)^2}.
\]

There is a cheaper positive compact test. Subtract the endpoint value from the Kaiser profile before normalizing. The resulting density is the classical continuous Kaiser--Bessel window; unlike the standard Kaiser window it vanishes at the support endpoints. Its transform is a **difference of two sinc terms**. The leading `1/x` tails cancel after the two nearby phases become close, while the whole transition region costs only logarithmically in the shape parameter.

For the generic separated spectral-gap problem of `RE-209`, if

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad
\operatorname{supp}\nu\subset[H,\infty),
\]

and

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|,
\qquad
A:=HT,
\]

then for fixed `H>0`, `A\to\infty`, and `0\le\epsilon<1`,

\[
\boxed{
R\gg_H (1-\epsilon)\frac{e^A}{A\log A}.
}
\tag{1}
\]

The exponential coefficient is still the sharp unit rate from `RE-213`, but the subexponential loss improves from `A^2` in `RE-214` to `A\log A`.

For the ordinary-prime `{0,1,2}` repair architecture, `RE-214` supplies independently

\[
R\ll\sqrt Q
\tag{2}
\]

using only bounded multiplicity and the ordinary-prime carrier count, with no fidelity condition on the modified source. Combining (1) and (2) gives the sharper necessary condition

\[
\boxed{
HT_Q-\log(HT_Q)-\log\log(HT_Q)
\le \frac12\log Q+O_H(1).
}
\tag{3}
\]

Consequently

\[
\boxed{
HT_Q
\le
\frac12\log Q
+\log\log Q
+\log\log\log Q
+O_H(1).
}
\tag{4}
\]

Thus the source-independent boundary layer above the half-logarithmic height shrinks from the `2\log\log Q+O(1)` allowance in `RE-214` to `\log\log Q+\log\log\log Q+O(1)`. The exact endpoint is still not excluded without an additional source condition; `RE-213` remains strictly stronger there because KV fidelity forces a deficit `\omega(V(Q))` **below** the endpoint.

## 1. Endpoint cancellation turns one Kaiser factor into an integrable test

Let

\[
f(x):=\frac{\sin x}{x},
\qquad f(0):=1.
\]

For `\beta\ge2`, define on `[-1,1]`

\[
w_\beta(t)
:=
\frac{I_0\!\left(\beta\sqrt{1-t^2}\right)-1}
{2\left(\sinh\beta/\beta-1\right)}.
\tag{5}
\]

Because `I_0(u)\ge1` for real `u`, this is nonnegative; because

\[
\int_{-1}^{1}I_0\!\left(\beta\sqrt{1-t^2}\right)dt
=\frac{2\sinh\beta}{\beta},
\]

it has mass one. It is supported on `[-1,1]` and vanishes at both endpoints.

The standard Kaiser transform already used in `RE-212` gives, for `x\ge\beta`,

\[
\int_{-1}^{1}
I_0\!\left(\beta\sqrt{1-t^2}\right)e^{-ixt}dt
=2f\!\left(\sqrt{x^2-\beta^2}\right).
\]

Subtracting the transform of the constant function on `[-1,1]` therefore gives the exact transform

\[
\boxed{
F_\beta(x)
:=\widehat w_\beta(x)
=
\frac{
 f\!\left(\sqrt{x^2-\beta^2}\right)-f(x)
}{\sinh\beta/\beta-1},
\qquad x\ge\beta.
}
\tag{6}
\]

This is the useful difference from the standard Kaiser factor. Each sinc term separately has only a `1/x` absolute tail, but their difference becomes integrable once the phase displacement

\[
x-\sqrt{x^2-\beta^2}
=\frac{\beta^2}{x+\sqrt{x^2-\beta^2}}
\tag{7}
\]

falls below order one.

## 2. The complete tail norm is `O(beta log beta e^{-beta})`

Put

\[
y(x):=\sqrt{x^2-\beta^2},
\qquad
g_\beta(x):=f(y(x))-f(x).
\tag{8}
\]

We first prove the elementary unnormalized estimate

\[
\boxed{
\int_\beta^\infty
\left(|g_\beta(x)|+|g_\beta'(x)|\right)dx
\ll \log(2+\beta).
}
\tag{9}
\]

Use the standard bounds

\[
|f(u)|\ll\min(1,u^{-1}),
\qquad
|f'(u)|\ll\min(u,u^{-1}),
\qquad
|f''(u)|\ll u^{-1}\quad(u\ge1).
\tag{10}
\]

On `x\in[\beta,2\beta]`, changing variables from `x` to `y` gives

\[
dx=\frac{y}{\sqrt{y^2+\beta^2}}dy.
\]

Hence the `f(y)` contribution to the `L^1` norm is `O(1)`, while the `f(x)` contribution is also `O(1)`. For the derivative, the triangle inequality in differential form gives

\[
\int_\beta^{\beta^2}|g_\beta'(x)|dx
\le
\int_0^{\sqrt{\beta^4-\beta^2}}|f'(y)|dy
+
\int_\beta^{\beta^2}|f'(x)|dx
\ll\log\beta.
\tag{11}
\]

On `[2\beta,\beta^2]`, one has `y\asymp x`, so

\[
|g_\beta(x)|\le |f(y)|+|f(x)|\ll x^{-1},
\]

whose integral is `O(log beta)`.

It remains to control the infinite tail. For `x\ge\beta^2`, one has `y\asymp x` and, from (7),

\[
0\le x-y\ll\frac{\beta^2}{x}.
\tag{12}
\]

The mean-value theorem and (10) give

\[
|g_\beta(x)|\ll\frac{\beta^2}{x^2}.
\tag{13}
\]

Moreover

\[
g_\beta'(x)
=
[f'(y)-f'(x)]
+f'(y)\left(\frac{x}{y}-1\right),
\]

so again by (10)--(12),

\[
|g_\beta'(x)|
\ll
\frac{\beta^2}{x^2}
+
\frac{\beta^2}{x^3}.
\tag{14}
\]

Both terms are integrable from `\beta^2` to infinity with `O(1)` total contribution. Equations (11)--(14) prove (9). The apparent singularity of `y'(x)` at `x=\beta` is harmless because `f'(y)=O(y)` as `y\to0`; the change-of-variables argument already incorporates this cancellation.

Finally,

\[
\sinh\beta/\beta-1\asymp e^\beta/\beta
\qquad(\beta\ge2),
\]

so (6) and (9) yield the uniform tail estimate

\[
\boxed{
\int_\beta^\infty
\left(|F_\beta(x)|+|F_\beta'(x)|\right)dx
\ll
\beta\log(2+\beta)e^{-\beta}.
}
\tag{15}
\]

This is precisely what one standard Kaiser factor lacks: endpoint cancellation upgrades the tail from conditionally decaying `1/x` behavior to an absolutely integrable difference without squaring the transform.

## 3. The weighted-prefix tariff improves from `A^2` to `A log A`

Return to the generic separated measure. Scale `w_\beta` to the whole observation interval by

\[
W_{\beta,T}(t)
:=\frac1T w_\beta(t/T),
\qquad |t|\le T.
\tag{16}
\]

It is a nonnegative probability density supported on `[-T,T]`, with Fourier transform

\[
\phi(L)=F_\beta(LT).
\tag{17}
\]

Choose

\[
\boxed{\beta=A=HT.}
\tag{18}
\]

Then every repair frequency `L\ge H` lies in the tail regime `LT\ge\beta`. Pairing the spectral approximation against `W_{\beta,T}` gives, exactly as in `RE-209`,

\[
1-\epsilon
\le
\left|\int\phi(L)d\nu(L)\right|.
\tag{19}
\]

With `d\nu=e^{-L}dG`, Stieltjes integration by parts gives

\[
\left|\int\phi\,d\nu\right|
\le
R\int_H^\infty
\left(|\phi'(L)|+|\phi(L)|\right)dL.
\tag{20}
\]

Under `x=LT`,

\[
\int_H^\infty|\phi'(L)|dL
=
\int_A^\infty|F_A'(x)|dx,
\]

while

\[
\int_H^\infty|\phi(L)|dL
=
\frac1T\int_A^\infty|F_A(x)|dx.
\]

For fixed `H` and `A\to\infty`, (15) therefore gives

\[
\int_H^\infty
\left(|\phi'|+|\phi|\right)dL
\ll_H A\log A\,e^{-A}.
\tag{21}
\]

Combining (19)--(21) proves (1).

This does not improve the unit exponential coefficient of `RE-213`; that coefficient is already extremal for positive compact windows. It improves only the polynomial/logarithmic tariff that matters when the lower bound is compared with the finite ordinary-prime carrier capacity.

## 4. Ordinary-prime capacity now gives a one-logarithm boundary layer

Use the arithmetic normalization of `RE-214`: the local packet contains

\[
B\asymp\frac{\sqrt Q}{\log Q}
\]

ordinary primes near `X_0=2Q`, every remote ordinary prime is edited at most once, and the exact vertical Euler discrepancy is `o(d_Q)` uniformly on `|t|\le T_Q`. The exact-Euler to first-harmonic reduction and the definition of the normalized primitive are unchanged, so (1) applies with `\epsilon=o(1)`.

Independently, bounded ordinary-prime multiplicity gives

\[
R_Q
=
\sup_{L\ge H}
\frac{e^{-L}|C_Q(X_0e^L)|}{B}
\ll\sqrt Q,
\tag{22}
\]

where `C_Q` is the signed remote prime-count prefix. Combining (1) and (22), with `A_Q=HT_Q`, gives

\[
\frac{e^{A_Q}}{A_Q\log A_Q}
\ll_H\sqrt Q.
\tag{23}
\]

Taking logarithms proves (3). The same inequality first implies `A_Q=O(log Q)`; substituting this back into the logarithms yields (4).

For `T_Q=c\log Q` the leading threshold is unchanged:

\[
c\le\frac1{2H}+o(1).
\]

Hence for the current corridor `H=\log8`, every fixed `c>1/(2\log8)=0.2404491734\ldots` remains impossible without invoking KV fidelity. The improvement is genuinely second order: an excess above the half-log endpoint larger than

\[
\log\log Q+\log\log\log Q+O_H(1)
\]

is already incompatible with the finite ordinary-prime carrier, compared with the `2\log\log Q+O_H(1)` excess left by `RE-214`.

## 5. Prior-art boundary and adversarial checks

The endpoint-zero profile in (5) is not presented as a new signal-processing window. It is the continuous Kaiser--Bessel window studied in the NFFT literature; a directly relevant prior-art reference is Daniel Potts and Manfred Tasche, *Continuous window functions for NFFT*, Advances in Computational Mathematics **47** (2021), article 53, DOI `10.1007/s10444-021-09873-8`. That literature studies NFFT approximation/error constants, not the weighted primitive `R` in (1), the ordinary-prime prefix identity (22), or the resulting Robin-line source-capacity boundary. No theorem from that paper is load-bearing here: (6) follows directly by subtracting the rectangular transform from the standard Kaiser identity already derived in this line, and the complete tail norm needed here is proved in (9)--(15). `SOURCES.md` therefore needs no new theorem anchor.

Several failure modes were checked explicitly. The test is nonnegative and has unit mass, so pairing cannot amplify the assumed uniform spectral error. Its support is exactly the observed interval after scaling. The parameter `\beta=HT` may grow because every estimate above is uniform for `\beta\ge2`. The endpoint derivative is finite despite the square-root coordinate because `f'(y)=O(y)`. The cancellation in (13)--(14) is used only after `x\ge\beta^2`; before that point the proof pays the full `O(log beta)` variation, so no unjustified pointwise phase cancellation is assumed. Finally, the arithmetic capacity bound is exactly the signed-count bound from `RE-214`, so Chebyshev-weight cancellation, remote placement, and arbitrary finite sign interlacing do not evade it.

The result does **not** prove that the `A log A` loss is optimal, does not improve the constructive range of `RE-208`, and does not remove the need for KV fidelity at or below the exact half-log endpoint. A different positive window with an even cheaper absolutely integrable tail norm could sharpen the second-order source-capacity layer further. Conversely, the continuous Kaiser--Bessel calculation shows that the `A^2` loss in `RE-214` was a property of squaring a discontinuous-endpoint Kaiser factor, not a structural cost of bounded ordinary-prime multiplicity.

## Research consequence

The raw ordinary-prime carrier obstruction is closer to the half-logarithmic boundary than `RE-214` showed. Without assuming that the modified source satisfies any PNT/KV envelope, separated continuum hiding must obey

\[
HT_Q
\le
\frac12\log Q
+\log\log Q
+\log\log\log Q
+O_H(1).
\]

The remaining source-independent second-order question is now concrete: determine the smallest possible subexponential loss in the weighted-primitive test among positive compact windows with an absolutely integrable transform-plus-derivative tail. On the constructive side, the much larger leading constant gap remains unchanged: `RE-208` reaches only `c<1/(24H\log2)`, while bounded multiplicity already forbids every fixed `c>1/(2H)` and KV fidelity excludes the endpoint and its `V(Q)`-scale neighborhood.