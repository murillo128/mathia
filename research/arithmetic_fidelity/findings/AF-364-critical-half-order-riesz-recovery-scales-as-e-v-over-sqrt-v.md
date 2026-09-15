# AF-364 — critical half-order Riesz recovery scales as `e^v / sqrt(v)`

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-RELATIVE`, `QUANTITATIVE-FIDELITY`, `CRITICAL-SCALING`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

AF-363 leaves the critical Bessel/Sobolev exponent `beta=1/2` open because its target energy is spread across logarithmic zero scales rather than concentrating at either scaled band edge. That critical regime can nevertheless be priced sharply enough for the Riesz-fidelity question without assuming an asymptotic density for distinct zeta zeros.

Retain AF-363's exponential band

\[
\mathcal B_{\delta,T}(v)
=
\{\gamma:T<\gamma\le T e^{v/\delta}\},
\qquad
x_\gamma=\delta\log(\gamma/T),
\]

its normalized target-recovery modulus `K_beta(delta,T;v)`, and the source-native critical target

\[
a_\gamma=(1+\gamma^2)^{-1/4}e^{i\gamma y_0}.
\]

Write

\[
u_{\delta,T}:=\delta\log T,
\qquad
\kappa_d:=0.836250351839\ldots .
\]

The 2026 theorem of Alpöge--Furman gives unconditionally

\[
\liminf_{X\to\infty}\frac{N_d(X)}{N(X)}\ge \kappa_d,
\]

where `N_d` counts distinct nontrivial zeros and `N` counts with multiplicity. Under RH, distinct positive zeros are exactly distinct positive ordinates, so this is a lower bound for the counting function `D(X)` used by AF-363.

For every fixed `v>0`, along `delta->0`, `T->infinity`, and `u_{delta,T}->u in [0,infinity)`, define

\[
R(u,v)
:=
\frac{\int_0^v e^{2x}(u+x)\,dx}
     {\int_0^v (u+x)\,dx}
=
\frac{(2u+2v-1)e^{2v}-2u+1}
     {2v(2u+v)}.
\tag{1}
\]

Then every such critical recovery sequence satisfies the quantitative envelope

\[
\boxed{
\kappa_d\,R(u,v)
\le
\liminf K_{1/2}(\delta,T;v)^2
\le
\limsup K_{1/2}(\delta,T;v)^2
\le
\kappa_d^{-1}R(u,v).
}
\tag{2}
\]

If the distinct-zero proportion has an asymptotic density

\[
D(X)\sim \kappa_* N(X)
\qquad(\kappa_*>0),
\tag{3}
\]

then the unknown scalar density cancels between numerator and denominator and the critical limit becomes exact:

\[
\boxed{
K_{1/2}(\delta,T;v)^2\longrightarrow R(u,v).
}
\tag{4}
\]

The same formula has the endpoint interpretations

\[
R(0,v)=\frac{(2v-1)e^{2v}+1}{2v^2},
\qquad
R(\infty,v)=\frac{e^{2v}-1}{2v},
\tag{5}
\]

where the second means `u_{delta,T}->infinity` with fixed `v`.

More importantly, the exact asymptotic density `(3)` is **not needed to determine the growing-band scale**. Along any sequence

\[
\delta\downarrow0,
\qquad
T\to\infty,
\qquad
v=v_\delta\to\infty,
\tag{6}
\]

one has, under RH,

\[
\boxed{
K_{1/2}(\delta,T;v_\delta)
=
\Theta_{\kappa_d}\!\left(\frac{e^{v_\delta}}{\sqrt{v_\delta}}\right).
}
\tag{7}
\]

A concrete asymptotic envelope is

\[
\sqrt{\frac{\kappa_d}{2}}\,
\frac{e^v}{\sqrt v}(1-o(1))
\le K_{1/2}
\le
\frac{1}{\sqrt{\kappa_d}}\,
\frac{e^v}{\sqrt v}(1+o(1)).
\tag{8}
\]

Thus the half-order target is genuinely critical. It does not collapse to AF-363's supercritical cost `1`, but it also does not pay the full upper-edge factor `e^v`: logarithmic spreading of its target energy buys exactly a square-root bandwidth discount in the exponentiated scaled band.

The absolute noise price remains separate. By AF-362,

\[
\frac{\|D^{-*}a\|_2}{\|a\|_2}
=
\exp(u_{\delta,T}+o(1))K_{1/2},
\]

so in the growing-band regime `(6)` the absolute critical recovery cost is

\[
\boxed{
\Theta_{\kappa_d}\!\left(
\frac{e^{u_{\delta,T}+v_\delta}}{\sqrt{v_\delta}}
\right).
}
\tag{9}
\]

This resolves the conditioning side of AF-363's critical exponent. It still does not show that the half-order probe carries any rational-prime-specific discriminator.

## Derivation

### 1. The critical target is a harmonic sum over distinct ordinates

AF-362 gives, uniformly on the retained band,

\[
K_{1/2}^2
=
\frac{
\sum_{\gamma\in\mathcal B}
(1+\gamma^2)^{-1/2}e^{2x_\gamma}}
{
\sum_{\gamma\in\mathcal B}
(1+\gamma^2)^{-1/2}}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
\tag{10}
\]

Since `gamma>=T->infinity`, replacing `(1+gamma^2)^(-1/2)` by `1/gamma` changes both sums by relative `1+O(T^{-2})`. Put

\[
U:=Te^{v/\delta},
\qquad
h_0(t):=t^{-1},
\qquad
h_1(t):=t^{-1}(t/T)^{2\delta}.
\tag{11}
\]

For small `delta<1/2`, both `h_0` and `h_1` are positive decreasing functions. If `D(X)` counts distinct positive ordinates, the two sums in `(10)` are therefore Stieltjes integrals

\[
S_j(T,U)=\int_{(T,U]}h_j(t)\,dD(t),
\qquad j=0,1.
\tag{12}
\]

### 2. The modern distinct-zero bound transfers to the weighted sums

Let `N(X)` be the usual zero count with multiplicity. Alpöge--Furman imply that for every fixed `epsilon>0` and all sufficiently large `X`,

\[
(\kappa_d-\varepsilon)N(X)\le D(X)\le N(X).
\tag{13}
\]

For a positive decreasing `h`, Stieltjes integration by parts gives

\[
\int_{(T,U]}h\,dD
=
h(U)D(U)-h(T)D(T)
+
\int_T^U D(t)(-dh(t)).
\tag{14}
\]

Substituting `(13)` in the positive terms and using the opposite endpoint bound in the negative lower-edge term yields

\[
(\kappa_d-\varepsilon)J_h
-(1-\kappa_d+\varepsilon)h(T)N(T)
\le
\int h\,dD
\le
J_h+(1-\kappa_d+\varepsilon)h(T)N(T),
\tag{15}
\]

where

\[
J_h:=\int_{(T,U]}h(t)\,dN(t).
\]

For both `h_0` and `h_1`, the lower-edge correction in `(15)` is negligible relative to `J_h` whenever `v/delta->infinity`; this includes every fixed positive `v` and every growing `v`. Hence

\[
(\kappa_d-o(1))J_j
\le S_j\le
(1+o(1))J_j,
\qquad j=0,1.
\tag{16}
\]

This is the key point: an exact distinct-zero asymptotic is unnecessary. A positive lower density already makes the critical target-energy measure uniformly comparable to the full zero-counting measure after harmonic weighting.

### 3. Riemann--von Mangoldt gives the reference critical profile

The Riemann--von Mangoldt law

\[
N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+O(\log t)
\tag{17}
\]

and another partial summation give

\[
J_0
=
\frac{1+o(1)}{2\pi\delta^2}
\int_0^v (u_{\delta,T}+x)\,dx,
\tag{18}
\]

\[
J_1
=
\frac{1+o(1)}{2\pi\delta^2}
\int_0^v e^{2x}(u_{\delta,T}+x)\,dx.
\tag{19}
\]

The terms coming from `log(2pi)`, the `-t/(2pi)` part of `(17)`, and the Stieltjes endpoints are one order smaller after the `x=delta log(t/T)` scaling. Dividing `(19)` by `(18)` and then using `(16)` in `(10)` proves `(2)`.

If `(3)` holds, the same argument improves `(16)` to `S_j=(\kappa_*+o(1))J_j` for both `j`; the common factor cancels, proving `(4)`. No conjectural value of `kappa_*` is needed.

### 4. The critical growing-band law is universal up to the known density constant

For `u>=0`, direct integration gives `(1)`. As `v->infinity`, uniformly in the ratio `u/v`,

\[
R(u,v)
=
\frac{e^{2v}}{v}
\frac{u+v}{2u+v}
(1+o(1)).
\tag{20}
\]

Because

\[
\frac12\le\frac{u+v}{2u+v}\le1,
\tag{21}
\]

we have

\[
\frac{e^{2v}}{2v}(1-o(1))
\le R(u,v)
\le
\frac{e^{2v}}{v}(1+o(1)).
\tag{22}
\]

Combining `(22)` with `(2)` and taking square roots yields `(8)` and hence `(7)`.

The square-root discount has a transparent source. At `beta=1/2`, target energy per logarithmic frequency interval is of order `log gamma`, so the normalized energy occupies the whole scaled interval rather than an `O(delta)` neighborhood of the upper edge. Multiplication by the inverse-Riesz factor `e^{2x}` still makes the recovery numerator upper-edge dominated, but normalization by the total critical target energy contributes an additional factor of order `v`. Taking the square root converts that factor to `sqrt(v)`.

## Arithmetic-fidelity interpretation

AF-363's two strict Sobolev regimes are edge-selection phenomena. Below half order, the source-native target norm is upper-edge dominated and pays the full differential Riesz factor; above half order, it is lower-edge dominated and, for fixed `v`, pays none of it. The critical exponent is different: the *target itself* retains information from all logarithmic scales, and that retained profile survives strongly enough to alter the inverse-channel modulus by a polynomial factor.

This matters for the line's broader compression program because it separates three statements that can otherwise be conflated:

1. the Riesz multiplier has worst-case differential condition `e^v`;
2. a source-native critical target has recovery cost `e^v/sqrt(v)` on growing scaled bands;
3. neither statement says whether the target distinguishes rational primes from a matched non-arithmetic source.

The result therefore closes a conditioning ambiguity without manufacturing arithmetic specificity. Any matched frequency system whose distinct-point counting measure obeys the same positive-density harmonic bounds has the same critical scaling.

## Prior art and novelty assessment

No novelty is claimed for Riemann--von Mangoldt, Abel/Stieltjes partial summation, harmonic sums over zeta-zero ordinates, or converting a positive density estimate into weighted-sum bounds.

Richard P. Brent, David J. Platt, and Timothy S. Trudgian, *A harmonic sum over nontrivial zeros of the Riemann zeta-function* (Bull. Aust. Math. Soc. 2021; arXiv:2009.05251), prove the much sharper classical asymptotic for the multiplicity-counted sum `sum_{0<gamma<=T} 1/gamma`, with main term `(4pi)^(-1) log^2(T/(2pi))`. That is exactly the full-zero reference profile underlying `(18)`, but it does not address the distinct-ordinate weighting used by the present target.

Levent Alpöge and Ralph Furman, *More than two thirds of the zeta zeros are simple and on the critical line* (arXiv:2608.13637, 2026), prove unconditionally that at least `0.83625...` of zeta zeros are distinct and at least `0.67250...` are simple and on the critical line. Their theorem supplies the modern constant `kappa_d` in `(13)`; it does not study Riesz recovery or the critical Bessel target.

The mathematical delta here is the specialization of those classical/current zero-counting inputs to AF-362's target-relative inverse problem. It resolves AF-363's previously open half-order scale and shows that exact knowledge of the asymptotic distinct-zero proportion is unnecessary for the leading growing-band law.

## Boundaries and falsification

- RH is still required for the interpretation inherited from AF-358--AF-363 in which the endpoint zero channel is indexed by real critical-line frequencies. Alpöge--Furman's distinct-zero lower bound itself is unconditional; it does not remove that channel-level RH assumption.
- Inequality `(2)` is a density envelope, not an exact fixed-`v` limit. An exact limit follows from `(3)` or from another hypothesis strong enough to identify the limiting distinct-ordinate harmonic profile.
- The constants in `(8)` are not claimed sharp. The robust conclusion is the scale `e^v/sqrt(v)`; sharper constants would require more information about distinct-zero distribution across logarithmic scales.
- The target is the source-native Bessel probe from AF-363. Other critical-looking targets require their own energy measure and need not have the same polynomial correction.
- The result uses the coefficient `ell^2` noise geometry fixed by AF-362. Changing the observation norm changes the dual recovery modulus.
- The square-root discount is a conditioning result only. It is reproduced by matched non-arithmetic frequency controls with comparable counting density and therefore supplies no rational-prime discriminator by itself.
- For fixed `v`, `(2)` leaves a bounded multiplicative uncertainty because the known theorem controls a lower density rather than the exact distinct-zero harmonic profile. Treating `R(u,v)` itself as unconditional would overstate the evidence.

## Consequence for the research line

The half-order regularity frontier from AF-363 is now quantitatively resolved at the scale needed to classify broad-band conditioning. For the canonical critical source probe, widening the scaled Riesz band is still exponentially expensive, but the target's logarithmic energy spread saves a factor `sqrt(v)` relative to the full-vector or subcritical upper-edge cost.

The remaining Riesz question is no longer whether `beta=1/2` behaves like either strict side. It is whether an independently specified **arithmetic discriminator** has a source-native target profile whose Riesz recovery law can be priced similarly and, crucially, whether that profile separates the rational-prime source from matched controls. The conditioning theorem here cannot supply that specificity.