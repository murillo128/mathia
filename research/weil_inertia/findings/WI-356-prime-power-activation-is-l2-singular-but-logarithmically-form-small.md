# WI-356 — prime-power activation is L2-singular but logarithmically form-small at Suzuki thresholds

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + NON-RH`

## Claim

Suzuki's fixed-domain Rayleigh formula makes each prime-power contribution switch on when the aperture crosses a threshold
\[
a_q:=\frac12\log q,
\qquad q=p^k,
\tag{1}
\]
through a compressed translation on `L^2(-1,1)`. The new channel has a sharp and initially counterintuitive topology at activation:

1. as a bounded operator on `L^2(-1,1)`, its norm does **not** tend to zero as `a\downarrow a_q` from above; it jumps immediately to the full coefficient `\Lambda(q)/\sqrt q`;
2. relative to the universal logarithmic form appearing in Suzuki's equation (4.5), the same channel is nevertheless infinitesimally form-small, with an explicit coefficient tending to zero like the reciprocal of a logarithm.

More precisely, put
\[
\ell:=\log q,
\qquad
c_q:=\frac{\Lambda(q)}{\sqrt q},
\qquad
t(a):=\frac{\ell}{a},
\qquad
\varepsilon(a):=2-t(a).
\tag{2}
\]
For `a>a_q` sufficiently close to `a_q`, so `0<\varepsilon<1/2`, the isolated `q`-channel in the numerator of Suzuki's fixed-domain form is
\[
P_{q,a}(w)
=-2c_q\,\Re C_w(2-\varepsilon),
\qquad
C_w(t):=\int_{-1}^{1-t}w(x+t)\overline{w(x)}\,dx.
\tag{3}
\]
If `\mathcal L(w)` denotes Suzuki's universal logarithmic form,
\[
\mathcal L(w)
=
\frac14\int_{-1}^{1}\int_{-1}^{1}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-
\frac12\int_{-1}^{1}|w(x)|^2\log(1-x^2)\,dx,
\tag{4}
\]
then the exact endpoint estimate
\[
\boxed{
|C_w(2-\varepsilon)|
\le
\frac{\mathcal L(w)}{\log(1/(2\varepsilon))}
}
\tag{5}
\]
holds for every smooth compactly supported `w`, hence
\[
\boxed{
|P_{q,a}(w)|
\le
\frac{2c_q}{\log(1/(2\varepsilon(a)))}\,\mathcal L(w).
}
\tag{6}
\]
The relative-form coefficient in (6) tends to zero as `a\downarrow a_q`, even though the bounded-operator norm of the same prime channel stays exactly `c_q` for every `a>a_q` close enough to the threshold.

Therefore a threshold-by-threshold coercivity program following WI-355 cannot use `L^2` operator-norm smallness of newly activated prime atoms: that route is exactly false already at the first activation. The natural topology is instead Suzuki's logarithmic form topology. Any successful first-crossing exclusion must control bounded-`\mathcal L` states, exploit the exact null/source equation, or obtain a stronger source-specific coercivity estimate.

## 1. Exact source reduction at a prime-power threshold

The primary source is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026). In Section 4.2 Suzuki rescales the aperture `(-a,a)` to the fixed interval `(-1,1)` by writing `w(t)=v(at)`. His equation (4.5) expresses the Rayleigh quotient as an archimedean part containing the universal form (4), a finite prime-power sum over `n\le e^{2a}`, and a continuous-kernel remainder.

For one prime power `q`, the two translated overlap integrals in that finite sum have shift
\[
t=\frac{\log q}{a}.
\tag{7}
\]
They are complex conjugates, so their sum is `2 Re C_w(t)`. The coefficient is `c_q=\Lambda(q)/\sqrt q`, giving exactly (3) before division by `\|w\|_2^2`.

The source threshold is `t=2`, equivalently `a=a_q=\ell/2`. For `a<a_q`, `q>e^{2a}` and the term is absent. At `a=a_q`, the translated intervals meet only at an endpoint, so the overlap integral is zero. For every `a>a_q`, however close, the overlap has positive width
\[
\varepsilon=2-\frac{\ell}{a}>0.
\tag{8}
\]
Thus the question is not whether the coefficient tends to zero—it does not—but in which topology the compressed translation itself becomes small as its overlap strip collapses.

## 2. The isolated channel has an exact L2 norm jump

Let `H=L^2(-1,1)` and define the zero-extended compressed translation
\[
(S_t w)(x)=
\begin{cases}
w(x+t),&x,x+t\in(-1,1),\\
0,&\text{otherwise}.
\end{cases}
\tag{9}
\]
Then
\[
C_w(t)=\langle S_t w,w\rangle.
\tag{10}
\]
For `1\le t<2`, the initial and final support strips of `S_t` are disjoint, so
\[
S_t^2=0,
\qquad
\|S_t\|=1.
\tag{11}
\]
WI-306 already records the exact compressed-translation numerical-radius calculation: a square-zero contraction of this form has
\[
\sup_{\|w\|_2=1}|\langle S_t w,w\rangle|=\frac12.
\tag{12}
\]
For completeness, the lower bound is elementary here. Choose a unit vector `f` supported in the initial strip of `S_t`; then `S_tf` is unit, is supported in the disjoint final strip, and is orthogonal to `f`. For
\[
w=\frac{f+S_tf}{\sqrt2}
\tag{13}
\]
one obtains `|\langle S_tw,w\rangle|=1/2`. The reverse inequality follows from `S_t^2=0` (equivalently from the exact two-block form of `S_t`).

The self-adjoint prime channel is
\[
-c_q(S_t+S_t^*).
\tag{14}
\]
Because `S_t` is an isometry between two orthogonal strips, `\|S_t+S_t^*\|=1`; hence
\[
\boxed{
\|-c_q(S_t+S_t^*)\|=c_q
\qquad (1\le t<2).
}
\tag{15}
\]
At `t=2`, `S_2=0` almost everywhere. Consequently the isolated prime channel is **not norm-continuous at activation**:
\[
\lim_{a\downarrow a_q,\ a>a_q}
\|P_{q,a}\|_{L^2\to L^2}
=c_q,
\qquad
\|P_{q,a_q}\|_{L^2\to L^2}=0.
\tag{16}
\]
This is the decisive negative part of the finding. A proof scheme that tries to cross prime thresholds by saying that the newly opened overlap window is short and therefore the new arithmetic perturbation has small bounded-operator norm cannot work.

WI-305 and WI-306 are the direct local algebraic antecedents: they already establish nilpotence/numerical-radius obstructions for compressed translations in the earlier localized-comparison program. The new point here is their exact placement in Suzuki's **full growing-aperture Weil form** at a prime-power activation threshold, where the same channel simultaneously has the form-smallness proved next.

## 3. Endpoint logarithmic energy makes the same channel form-small

Assume `0<\varepsilon<1/2` and put `t=2-\varepsilon`. The overlap in (3) pairs the left endpoint strip
\[
I_-:=(-1,-1+\varepsilon)
\tag{17}
\]
with the right endpoint strip
\[
I_+:=(1-\varepsilon,1).
\tag{18}
\]
Set
\[
M_-:=\int_{I_-}|w|^2,
\qquad
M_+:=\int_{I_+}|w|^2,
\qquad
M_\varepsilon:=M_-+M_+.
\tag{19}
\]
Cauchy--Schwarz and the arithmetic--geometric mean inequality give
\[
|C_w(2-\varepsilon)|
\le\sqrt{M_-M_+}
\le\frac12M_\varepsilon.
\tag{20}
\]
On either endpoint strip,
\[
1-x^2=(1-|x|)(1+|x|)\le2\varepsilon.
\tag{21}
\]
The Gagliardo term in (4) is nonnegative, while the endpoint potential therefore gives
\[
\mathcal L(w)
\ge
\frac12\log\frac1{2\varepsilon}\,M_\varepsilon.
\tag{22}
\]
Combining (20) and (22) proves (5), and multiplying by `2c_q` proves (6).

In particular, for every `\eta>0`, the newly activated `q`-channel obeys
\[
|P_{q,a}(w)|\le\eta\,\mathcal L(w)
\tag{23}
\]
whenever
\[
0<\varepsilon(a)
<
\frac12\exp\!\left(-\frac{2c_q}{\eta}\right).
\tag{24}
\]
Thus the channel is arbitrarily small relative to Suzuki's universal logarithmic energy if the aperture is sufficiently close to the threshold from above.

Equation (22) also identifies why the `L^2` norm witnesses in Section 2 do not contradict this statement. To nearly saturate the norm jump, a unit vector must put order-one mass into endpoint strips whose width tends to zero. Such a sequence necessarily has
\[
\mathcal L(w)\gtrsim \frac12\log\frac1{2\varepsilon},
\tag{25}
\]
so its logarithmic form energy diverges. The norm-jump witnesses escape every bounded-`\mathcal L` set.

## 4. Consequence for the first-crossing program

WI-355 reduces any RH failure to a first zero crossing of Suzuki's lowest localized Weil eigenvalue. It leaves open how positivity might be propagated as the aperture crosses the discrete prime-power thresholds at which new arithmetic channels enter.

The present calculation gives a sharp topology distinction for that program. **Bounded-operator perturbation theory in `L^2` is the wrong interface:** a newly activated prime channel has fixed norm `c_q`, no matter how narrow its overlap strip is. In contrast, on bounded logarithmic-energy sets the new channel vanishes uniformly by (6). This is exactly the compactness topology that can plausibly coexist with Suzuki's continuity theorem for `\lambda(a)`.

The useful next target is therefore not an `L^2` estimate of the form `\|P_{q,a}\|\to0`. That target is impossible. A viable threshold bootstrap would need, for example, a quantitative lower bound on the pre-threshold coercive reserve measured against `\mathcal L`, an exact bound on the `\mathcal L`-energy of a hypothetical first-crossing null state, or source-specific constraints from the null equation that make (6) effective together with the already-active prime channels.

This is compatible with WI-257's earlier warning that bounded perturbations do not automatically upgrade translation regularity: (6) does not manufacture such regularity. It instead uses the endpoint logarithmic penalty already present in Suzuki's exact form.

## 5. What this does not prove

The estimate does **not** prove that positivity propagates across any prime threshold. The already-active prime channels, the archimedean terms, and the continuous-kernel remainder also vary with `a`; (6) controls only the newly activated `q`-channel. No spectral gap at `a_q` is established, and no uniform lower bound for `\lambda(a)` follows.

Nor does (6) imply that all first-crossing null modes have bounded `\mathcal L` energy in a way strong enough to iterate over infinitely many thresholds. Producing such a bound is a separate coercivity problem. The conclusion here is narrower but exact: **operator-norm-small threshold induction is ruled out, while logarithmic-form-small threshold induction remains mathematically compatible with the exact source term.**

Finally, the numerical-radius ingredient is not new; WI-306 already isolates the exact compressed-translation bound and its classical nilpotent-operator antecedent. The endpoint logarithmic form itself is Suzuki's equation (4.4). The derived contribution recorded here is the threshold dictionary (2)--(3), the endpoint-mass estimate (5)--(6), and the resulting norm-versus-form dichotomy for a newly activated Suzuki prime-power channel.

## 6. Novelty and prior-art audit

The local `weil_inertia` findings, current mind state, clues, and source ledger were checked around compressed translations, endpoint singularity, Suzuki localization, and prime-threshold activation. WI-305--WI-306 contain the exact nilpotent compressed-translation algebra in a different localized-comparison setting; WI-256 treats the opposite small-shift regime; WI-257 blocks an automatic regularity upgrade; WI-309 uses endpoint-singular localizers in the clipped-tail architecture. None of those findings contains the Suzuki-threshold estimate (5)--(6).

A targeted literature search found Suzuki's 2026 paper as the primary exact source and a recent numerical preprint by Taebong Kim et al., **A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator** (arXiv:2607.24830), which reports that the numerically computed lowest eigenvalue passes smoothly through the first prime threshold `a=log 2/2`. That numerical observation is consistent with the form-smallness mechanism above but does not supply the analytical endpoint estimate (5) or remove the caveats in Section 5. It is treated only as neighboring numerical prior art, not as load-bearing evidence.

No external source located in this audit states the exact norm-jump/form-smallness dichotomy above. This is a local novelty statement about the audited corpus, **not** a claim of external priority.

## Sources

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), DOI `10.48550/arXiv.2606.09096`. Primary source for the fixed-domain Rayleigh formula, universal logarithmic form `\mathcal L`, finite prime-power sum, and continuity framework.
- Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Junghoon Shin and Minseo Kim, **A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion**, arXiv:2607.24830 (23 Jul 2026). Recent unrefereed numerical prior art for smooth behavior across the first prime threshold; not used in the proof.
- WI-305 and WI-306. Internal antecedents for the nilpotent compressed-translation/numerical-radius algebra; the present finding transfers that exact structure to Suzuki's source activation and adds the logarithmic-form estimate.
