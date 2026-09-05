# XF-053 — finite heat jets cannot repopulate the endpoint memory band

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC-BOUNDARY` + `NONPERTURBATIVE-REDUCTION`. XF-051 gives the exact one-sided distributional Burgers/Volterra carrier, and XF-052 identifies the endpoint datum below the first prime-power frequency as a simple-pole archimedean background with no arithmetic fluctuation. The remaining question is whether positive heat time can rebuild an order-one XF-050 memory-band coefficient from the singular endpoint.

There is an exact perturbative obstruction. Let

\[
\lambda_2:=\frac{\log 2}{2},
\]

fix any horizontal line `a>1`, and write

\[
U_t(\xi):=\widehat Q_a(\xi,t),
\qquad
Q_a(x,t)=\frac{H_t'(x+ia)}{H_t(x+ia)}.
\]

As in XF-051,

\[
\operatorname{supp}U_t\subset[0,\infty)
\]

and

\[
\boxed{
\partial_tU_t
=
\xi^2U_t
-
\frac{i\xi}{2\pi}(U_t*U_t)
}
\tag{1}
\]

as a tempered-distribution identity. XF-052 gives at `t=0` an exact decomposition

\[
U_0=A_0+P_0,
\tag{2}
\]

where `A_0` contains the rational, gamma and zero-frequency terms and the arithmetic term satisfies

\[
\boxed{
\operatorname{supp}P_0\subset[\lambda_2,\infty).
}
\tag{3}
\]

For every fixed integer `n>=0`, the heat-time jet

\[
U_n:=\left.\partial_t^nU_t\right|_{t=0}
\]

has the following property:

\[
\boxed{
U_n\big|_{(0,\lambda_2)}
\text{ is determined entirely by }A_0.
}
\tag{4}
\]

Equivalently, prime-power data from frequencies `>=lambda_2` cannot enter the prime-free endpoint band at **any finite order in heat time**.

There is a second, quantitative consequence for the XF-050 moving probe. Let

\[
\omega=\Theta(1/\log T),
\qquad
W=\Theta(\log^3T),
\]

and let `psi_T` be any of the compact one-sided probe amplitudes used there, supported in

\[
I_T=[\omega-W^{-1},\omega+W^{-1}]
\subset(0,\lambda_2).
\]

Then for each fixed `n`,

\[
\boxed{
\left\langle
\left.\partial_t^n\mathcal Z_t\right|_{t=0},
\psi_T
\right\rangle=o(1),
\qquad T\to\infty,
}
\tag{5}
\]

where

\[
\mathcal Z_t(\xi)=\frac{i}{2\pi}e^{a\xi}U_t(\xi)
\]

on the open positive half-line. Hence every fixed Taylor polynomial in the heat parameter remains invisible to the memory-band selector:

\[
\boxed{
\sum_{n=0}^{N}
\frac{t^n}{n!}
\left\langle
\left.\partial_t^n\mathcal Z_t\right|_{t=0},
\psi_T
\right\rangle
=o(1)
}
\tag{6}
\]

for every fixed `N`, uniformly for `t` in a fixed bounded interval.

Thus an order-one adverse coefficient at positive heat time, if it exists, is necessarily **nonperturbative in the shrinking-band limit**. It must come from heat orders tending to infinity with `T`, equivalently from a failure of uniform analyticity/quasianalytic control as `omega downarrow 0`. No finite collection of heat derivatives can supply the missing replenishment.

This does **not** prove that the full positive-time statistic is `o(1)`, does not justify summing the Taylor series uniformly in `T`, and does not give an upper bound on `Lambda`. It identifies the remaining endpoint problem much more sharply: the obstruction is no longer finite-order transport from the prime spectrum or finite-order self-interaction of the explicit singular background, but possible infinite-order accumulation at the moving spectral endpoint.

## 1. The high-frequency sector is an exact convolution ideal

Let

\[
\mathcal D'_+
:=
\{D\in\mathcal D'(\mathbb R):
\operatorname{supp}D\subset[0,\infty)\}.
\]

Convolution is canonical on this cone: addition is proper on

\[
[0,\infty)^2
\]

above every compact target-frequency set. For `lambda>0`, define

\[
\mathcal I_\lambda
:=
\{D\in\mathcal D'_+:
\operatorname{supp}D\subset[\lambda,\infty)\}.
\tag{7}
\]

Then `I_lambda` is a two-sided convolution ideal. Indeed, if

\[
D\in\mathcal I_\lambda,
\qquad
V\in\mathcal D'_+,
\]

then the elementary support inclusion gives

\[
\operatorname{supp}(D*V)
\subset
\operatorname{supp}D+\operatorname{supp}V
\subset
[\lambda,\infty).
\tag{8}
\]

Multiplication by `xi` or `xi^2` also preserves `I_lambda`. Therefore the Burgers vector field

\[
\mathfrak F(U)
:=
\xi^2U
-
\frac{i\xi}{2\pi}(U*U)
\tag{9}
\]

respects the quotient by the high-frequency ideal:

\[
U-V\in\mathcal I_\lambda
\quad\Longrightarrow\quad
\mathfrak F(U)-\mathfrak F(V)
\in\mathcal I_\lambda.
\tag{10}
\]

To see the quadratic step explicitly,

\[
U*U-V*V
=(U-V)*U+V*(U-V),
\tag{11}
\]

and both terms lie in `I_lambda` by (8).

This is stronger than merely saying that one instantaneous convolution is triangular. It says that the entire nonlinear vector field descends to the quotient

\[
\mathcal D'_+/\mathcal I_\lambda.
\]

The part of a distribution below `lambda` is therefore algebraically closed under every finite differentiation of the flow.

## 2. All finite heat jets below `lambda_2` are background-only

The defining integral for `H_t` is smooth to every real heat-time order, and on the fixed zero-free line `Im z=a>1` the logarithmic derivative and its required derivatives are tempered as in XF-051. Thus the jets `U_n` exist in the distributional sense.

Differentiating (1) `n` times gives the exact recurrence

\[
\boxed{
U_{n+1}
=
\xi^2U_n
-
\frac{i\xi}{2\pi}
\sum_{j=0}^{n}
\binom nj
U_j*U_{n-j}.
}
\tag{12}
\]

Define a formal background jet sequence `A_n` by the same recurrence, starting from the non-arithmetic datum `A_0` in (2):

\[
A_{n+1}
=
\xi^2A_n
-
\frac{i\xi}{2\pi}
\sum_{j=0}^{n}
\binom nj
A_j*A_{n-j}.
\tag{13}
\]

At order zero,

\[
U_0-A_0=P_0\in\mathcal I_{\lambda_2}.
\]

Assume inductively that

\[
U_j-A_j\in\mathcal I_{\lambda_2}
\qquad(0\le j\le n).
\]

Every difference of convolution terms in (12)--(13) contains at least one factor `U_j-A_j`, hence lies in `I_{lambda_2}` by the ideal property. The linear term does as well. Therefore

\[
U_{n+1}-A_{n+1}
\in\mathcal I_{\lambda_2}.
\]

By induction,

\[
\boxed{
U_n-A_n\in\mathcal I_{\lambda_2}
\qquad\text{for every fixed }n\ge0.
}
\tag{14}
\]

Restriction to `(0,lambda_2)` proves (4). Multiplication by the smooth nonvanishing factor `e^{a xi}` does not change support, so the same statement holds for every finite jet of the canonical carrier `mathcal Z_t` on the open positive band.

The conclusion is source-specific because XF-052 supplies the exact initial separation (2)--(3). The ideal argument itself is generic for one-sided quadratic convolution flows; what is special to Xi is that the first arithmetic source is separated from the memory scale by the fixed gap `lambda_2`.

## 3. The background jets remain only polyhomogeneously singular at the endpoint

Equation (14) eliminates prime data from the moving band, but (5) also needs control of the background jets as the band approaches zero. The explicit XF-052 normal form provides exactly the required starting class.

On `0<xi<lambda_2`,

\[
\mathcal Z_0(\xi)
=-\frac1{4\xi}
+\frac74
+O(\xi),
\tag{15}
\]

and the closed-half-line version inherited from `U_0` can differ at `xi=0` only by endpoint-supported terms coming from the `x`-independent factors omitted in the open-half-line Fourier formula. Those terms do not meet the XF-050 probe, whose support stays strictly positive.

A convenient local bookkeeping device is the standard half-line analytic family

\[
Y_\alpha(\xi)
:=
\frac{\xi_+^{\alpha-1}}{\Gamma(\alpha)}.
\tag{16}
\]

For `Re alpha,Re beta>0`, the beta integral gives

\[
Y_\alpha*Y_\beta=Y_{\alpha+\beta},
\tag{17}
\]

and analytic continuation preserves this identity distributionally. At `alpha=0`, `Y_0=delta_0`, while the restriction of `partial_alpha Y_alpha|_{alpha=0}` to `xi>0` is `1/xi`. Derivatives in `alpha` generate the usual finite-part logarithmic powers.

After a cutoff supported below `lambda_2`, the datum (15) is therefore a finite sum of an endpoint-supported distribution, one `Y'_0` singularity, and a smooth analytic germ. The recurrence (13) uses only convolution, multiplication by powers of `xi`, and finite sums. Using (17), an induction shows that for every fixed jet order `n` and ordinary derivative order `m`, the restriction of `A_n` to `xi>0` has at worst a finite polyhomogeneous singularity. In particular, there exist finite integers `r_{n,m},s_{n,m}` and a constant `C_{n,m}` such that

\[
\boxed{
|\partial_\xi^m A_n(\xi)|
\le
C_{n,m}\,
\xi^{-r_{n,m}}
(1+|\log\xi|)^{s_{n,m}}
}
\tag{18}
\]

for all sufficiently small positive `xi`.

No uniformity in `n` is asserted. That omission is essential: the constants and exponents may grow rapidly with the heat-jet order, and precisely that growth is where a nonperturbative endpoint effect could hide.

## 4. Every fixed jet is killed by the moving oscillatory probe

For the compact one-sided XF-050 probe, write its positive-frequency amplitude schematically as

\[
\psi_T(\xi)
=
W e^{iT\xi+i\vartheta_T}
\chi\!\left(W(\xi-\omega)\right),
\tag{19}
\]

with fixed `chi in C_c^infty((-1,1))`. Since

\[
\omega\asymp\frac1{\log T},
\qquad
W\asymp\log^3T,
\qquad
\frac{W^{-1}}\omega=O(\log^{-2}T),
\]

the whole support lies in a fixed relative neighborhood of `omega` and remains below `lambda_2` for large `T`.

By (14), prime-power terms vanish identically on this support at every fixed jet order. By (18), for fixed `n,m`,

\[
\sup_{\xi\in I_T}
|\partial_\xi^m A_n(\xi)|
\le
(\log T)^{C_{n,m}}
(\log\log T)^{C_{n,m}}
\tag{20}
\]

for a possibly larger constant `C_{n,m}`.

Integrating (19) by parts `N` times transfers derivatives onto the compact amplitude. Derivatives of the cutoff cost powers of `W`, while (20) costs only powers of `log T` and `log log T`. Therefore, for each fixed `n` and any fixed sufficiently large `N`,

\[
\left|
\langle A_n,\psi_T\rangle
\right|
\ll_{n,N}
\left(\frac WT\right)^N
(\log T)^{C_{n,N}}
(\log\log T)^{C_{n,N}}
=o(1).
\tag{21}
\]

The smooth multiplier converting `U_n` to `partial_t^n mathcal Z_t|_0` changes only the polylogarithmic factor. This proves (5). The `n=0` case agrees with the direct integration-by-parts estimate already recorded in XF-052.

For fixed `N` and bounded `t`, summing finitely many estimates (21) proves (6). Crucially, nothing here controls the sum as `N to infinity` with `T`.

## 5. What a surviving replenishment mechanism must now do

The accepted endpoint-transport clue had two broad possibilities after XF-052: either the explicit endpoint background is dynamically harmless at the memory scale, or its zero-frequency singularity can rebuild an order-one coefficient at positive time. The present result excludes the entire **finite-order** version of the second possibility.

A surviving adverse mechanism must exploit a genuinely nonuniform limit. Concretely, at least one of the following must occur along the shrinking band:

- heat derivatives of increasing order grow quickly enough that orders `n=n(T) to infinity` overcome the oscillatory `T`-scale cancellation;
- the heat-time Taylor expansion of the relevant distributional pairing has a radius or remainder bound that degenerates as `omega downarrow0`;
- an equivalent nonperturbative resummation of the endpoint singularity produces an order-one term even though every fixed jet is `o(1)`.

These are descriptions of one remaining mechanism, not three independent hypotheses. Any proof that supplies a `T`-uniform analytic or quasianalytic bound strong enough to rule them out would upgrade (6) to the desired finite-time transport estimate. Conversely, a counterexample must now exhibit this infinite-order accumulation explicitly; finite-order source mixing is impossible.

## 6. Prior-art and novelty boundary

The algebraic ingredients are classical. One-sided support under convolution, the high-support ideal (7), and the Riemann--Liouville analytic family (16)--(17) are standard distribution/fractional-calculus facts. A targeted literature audit did not identify an Xi/de Bruijn--Newman result asserting the present shrinking-band heat-jet consequence, and no novelty is claimed for those generic tools.

The durable Mathia delta is their source-faithful combination with XF-051--XF-052: the exact Xi carrier starts with all prime-power data at frequencies `>=log2/2`, its nonlinear Fourier evolution is one-sided, and therefore **every finite heat-time jet of the memory band is both arithmetic-independent and probe-small**. The first unresolved mechanism is necessarily an infinite-order endpoint effect.

No additional literature theorem is load-bearing in the derivation, so `SOURCES.md` does not require a new anchor.

## 7. Boundaries and falsification controls

The strongest falsification checks are structural.

First, replacing `lambda_2` by any smaller positive cutoff must leave the ideal proof unchanged; it does, because only support addition is used. Second, inserting a synthetic atom at frequency `mu<lambda_2` must immediately destroy the conclusion below `lambda_2`; it does, since the base difference no longer belongs to `I_{lambda_2}`. Third, endpoint-supported terms may alter the background jets but cannot invalidate the arithmetic-support statement (14), because they remain in the low-frequency quotient rather than in the prime ideal.

The result is deliberately finite-order. It does not establish real- or complex-time analyticity of `t mapsto mathcal Z_t` in a topology uniform as the probe support collapses to zero. It does not justify exchanging `T to infinity` with an infinite heat-time Taylor series. It does not prove a positive-time prime-free support gap in the literal sense: the deterministic background can populate the low band under its own nonlinear evolution. What is excluded is **dependence on the initial prime-power sector at every fixed perturbative order**, together with any order-one response of a fixed finite jet to the XF-050 probe.

## 8. Consequence for `xi_flow`

XF-048 found the endpoint selector, XF-050 made it compact and collision-safe, XF-051 supplied the exact infinite one-sided carrier, and XF-052 made the singular endpoint datum explicit. The present result closes the next perturbative escape route:

\[
\boxed{
\text{prime spectrum}
\not\longrightarrow
\text{memory band at any fixed heat order},
\qquad
\text{fixed background jet}
\stackrel{\psi_T}{\longrightarrow}0.
}
\]

The remaining endpoint theorem is therefore a **uniform infinite-order transport problem**. A successful route should seek a heat-time analyticity/quasianalyticity or Duhamel remainder estimate whose constants remain controlled as `omega~1/log T`, rather than compute more fixed derivatives. A negative route must construct an explicit infinite-order endpoint resummation that survives the oscillatory memory probe. Neither outcome is supplied here.