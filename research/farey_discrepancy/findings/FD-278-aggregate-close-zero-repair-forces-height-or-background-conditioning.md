# FD-278 — Aggregate close-zero repair forces spectral height or background conditioning

- **Date:** 2026-09-22
- **Status:** proved aggregate complete-cluster height/cardinality/background tariff conditional on RH and simple zeros
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** zeta-zero clusters / aggregate spectral repair / Riemann--von Mangoldt / argument excursions / population-cardinality-background ledger
- **Depends on:** FD-261, FD-276, FD-277
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + LOAD-BEARING-S(T)-BOUND + AGGREGATE-CLUSTER-TARIFF`

## Claim

FD-277 prices a single complete reciprocal-log zero cluster whose grouped packet is already large enough by itself to reach the FD-261 positive-capacity threshold. Its explicit loophole is aggregate: many individually subthreshold complete components might add coherently, so no one component needs to pay the full single-cluster cardinality/background tariff.

That loophole is not free. Even granting perfect phase alignment between components, aggregate threshold repair has a deterministic exponent ledger. Under RH, the zero-counting formula then limits the largest component cardinality available below a prescribed spectral height. Combining the two statements forces aggregate repair to pay through spectral population/height, cluster cardinality, or desingularized background conditioning.

Keep the polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

and write

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta=0.4150374992788438\ldots,
\qquad
L:=\log(2Nx),
\qquad
a:=1+\frac1\lambda.
\tag{2}
\]

Thus

\[
L=(a+o(1))\log x.
\tag{3}
\]

Use the FD-276 partition into complete reciprocal-log components: consecutive simple critical zeros are joined when their ordinate gap is `<2/L`, and a complete component has the corresponding exterior gaps at least `2/L`. Let `mathscr C` be any finite family of such complete components, all with ordinates at most

\[
T=x^{\tau+o(1)}.
\tag{4}
\]

For `C in mathscr C`, let `m_C=|C|`, let `Q_C(N,d)` be its grouped packet from FD-274--FD-276, and let

\[
\mathfrak B_C:=\mathfrak B_C(L^{-1})
\]

be its desingularized collar background envelope. Put

\[
R:=|\mathscr C|,
\qquad
m_*:=\max_{C\in\mathscr C}m_C,
\qquad
\mathfrak B_*:=\max_{C\in\mathscr C}\max(1,\mathfrak B_C).
\tag{5}
\]

Suppose along the sequence under consideration that

\[
R=x^{r+o(1)},
\qquad
m_*=(\kappa+o(1))\frac{\log x}{\log\log x},
\qquad
\mathfrak B_*=x^{b+o(1)}.
\tag{6}
\]

If the aggregate real packet reaches the FD-261 threshold,

\[
\mathcal S_{\mathscr C}(N,x)
:=
\sum_{x<d\le2x}
\left|
2\Re\sum_{C\in\mathscr C}Q_C(N,d)
\right|
\ge
x^{2-\beta-o(1)},
\tag{7}
\]

then necessarily

\[
\boxed{r+\kappa+b\ge c.}
\tag{8}
\]

This is the aggregate replacement for FD-276's single-component condition `kappa+b>=c`.

Under RH, the sharp Carneiro--Chandee--Milinovich bound for `S(t)` further gives, uniformly for every complete component below `T`,

\[
\boxed{
\kappa
\le
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi a}\right)}
}
\qquad (0\le\tau<\pi a),
\tag{9}
\]

while the ordinary zero count gives

\[
\boxed{r\le\tau.}
\tag{10}
\]

Consequently aggregate threshold repair forces

\[
\boxed{
b+\tau+
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi(1+1/\lambda)}\right)}
\ge c.}
\tag{11}
\]

For a uniformly tame aggregate background, `b=0`, this gives a genuine polynomial spectral-height floor. Let `tau_*(lambda)` be the smaller positive root of

\[
\tau+
\frac{\tau}{2(1-\tau/(\pi a))}
=c.
\tag{12}
\]

Writing `A=pi a`,

\[
\boxed{
\tau_*(\lambda)
=
\frac{
\frac32A+c-
\sqrt{\left(\frac32A+c\right)^2-4Ac}
}{2}.
}
\tag{13}
\]

Hence a tame-background family of complete components cannot collectively supply threshold repair unless

\[
\boxed{T\ge x^{\tau_*(\lambda)-o(1)}.}
\tag{14}
\]

The weakest bound over all fixed `lambda>0` occurs as `lambda -> infinity` and is

\[
\boxed{T\ge x^{0.2683381468698344\ldots-o(1)}.}
\tag{15}
\]

At balanced depth `lambda=1`,

\[
\boxed{T\ge x^{0.2725714440906720\ldots-o(1)}.}
\tag{16}
\]

As `lambda -> 0+`, the exponent tends to

\[
\frac{2c}{3}=0.2766916661858959\ldots .
\tag{17}
\]

Thus the aggregate loophole left by FD-277 survives only by paying a quantitatively visible resource. Many complete clusters can lower the single-cluster height tariff, but they cannot move the whole repair to subpolynomial spectral height unless the desingularized background itself pays essentially the missing power.

## Evidence

### 1. Summing complete components gives the aggregate exponent ledger

FD-276 proves, with an absolute implied constant independent of cluster cardinality,

\[
\sum_{x<d\le2x}|Q_C(N,d)|
\ll
x(2L)^{m_C-1}\mathfrak B_C.
\tag{18}
\]

Therefore, without any assumption on the relative phases of distinct components,

\[
\begin{aligned}
\mathcal S_{\mathscr C}(N,x)
&\le
2\sum_{C\in\mathscr C}
\sum_{x<d\le2x}|Q_C(N,d)|\\
&\ll
xR(2L)^{m_*-1}\mathfrak B_*.
\end{aligned}
\tag{19}
\]

The triangle inequality makes (19) deliberately adversarial: it already allows every complete component to align perfectly with every other component in every divisor-band coordinate.

From (3),

\[
\log(2L)=\log\log x+O(1).
\tag{20}
\]

Using (6) in (19) therefore gives

\[
\mathcal S_{\mathscr C}(N,x)
\le
x^{1+r+\kappa+b+o(1)}.
\tag{21}
\]

Comparing (21) with the required `x^(1+c-o(1))` in (7) proves (8).

This already shows why aggregate coherence is weaker than the single-cluster problem by exactly one new resource: the number of available components. No cancellation theorem is being imported; component population is charged explicitly.

### 2. Spectral height limits component population

The family contains at most one component per zero, so

\[
R\le N_\zeta(T).
\]

Riemann--von Mangoldt gives

\[
N_\zeta(T)=T^{1+o(1)}
\tag{22}
\]

at power scale. Equations (4), (6), and (22) imply

\[
r\le\tau,
\]

which is (10). The extra `log T` in the classical zero count is only `x^{o(1)}` here.

### 3. The same height also caps every component cardinality

Let `C` be any complete component in the family, with `m=m_C` zeros and upper ordinate `Gamma<=T`. Because every internal gap is `<2/L`, its total ordinate span `h` obeys

\[
h<\frac{2(m-1)}L.
\tag{23}
\]

Choose endpoints immediately outside its two extreme zeros and let the offsets tend to zero inside the exterior gaps. Riemann--von Mangoldt then gives, exactly as in FD-277,

\[
m
\le
\frac{m\log(2T)}{\pi L}
+
|S(t_+)|+|S(t_-)|
+O(1).
\tag{24}
\]

The use of `T` rather than the actual `Gamma` only weakens the estimate and makes it uniform across the whole family.

Under RH, Carneiro--Chandee--Milinovich prove

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t}.
\tag{25}
\]

If `T=x^(tau+o(1))` with fixed `tau>0`, equations (3)--(5), (24), and (25) imply

\[
m
\left(1-\frac{\tau}{\pi a}+o(1)\right)
\le
\left(\frac\tau2+o(1)\right)
\frac{\log x}{\log\log x}.
\tag{26}
\]

Taking the maximum over all components yields (9). If `tau=0`, the same comparison gives `m_*=o(log x/log log x)`, so (9) holds in the limiting exponent sense with `kappa=0`. If `tau>=pi a`, inequality (11) is automatic for the small threshold `c<1`, so only the range displayed in (9) is relevant.

### 4. Combining population and packing gives the aggregate height tariff

Equations (8)--(10) imply

\[
c
\le
b+r+\kappa
\le
b+\tau+
\frac{\tau}{2(1-\tau/(\pi a))},
\tag{27}
\]

which proves (11).

For `b=0`, the right side of (27) is strictly increasing on the relevant interval starting at zero, so there is a unique small positive crossing. Rearranging (12),

\[
(c-\tau)\left(1-\frac\tau{\pi a}\right)=\frac\tau2,
\tag{28}
\]

or

\[
\tau^2-
\left(\frac32\pi a+c\right)\tau
+\pi ac=0.
\tag{29}
\]

The smaller root is exactly (13). It decreases as `a` decreases, hence its uniform minimum over fixed `lambda>0` is attained in the limit `a->1`, giving (15). Direct substitution gives (16), while `a->infinity` reduces (12) to `3 tau/2=c`, giving (17).

More generally, (11) can be read as a background lower bound at prescribed spectral height:

\[
\boxed{
b
\ge
\left[
c-\tau-
\frac{\tau}{2(1-\tau/(\pi a))}
\right]_+
-o(1).}
\tag{30}
\]

So low-height aggregate repair is possible in this ledger only if the external zero-free backgrounds become polynomially ill-conditioned.

## Stress tests

The first stress test is the single-component limit. If `R=1`, then `r=0` exactly and (8) becomes `kappa+b>=c`, recovering the FD-276 threshold ledger. Combining that sharper `r=0` statement with (9) reproduces the stronger single-cluster height tariff of FD-277. The weaker numerical floor `0.268338...` is therefore not a contradiction: it is precisely the price of allowing polynomially many subthreshold components to share the repair burden.

The second stress test is bounded or polylogarithmic clusters. If `kappa=0` and the background is tame, (8) itself forces `r>=c`; since `r<=tau`, one gets the stronger simple condition

\[
T\ge x^{c-o(1)}=x^{0.4150374992\ldots-o(1)}.
\]

The lower floor in (15) appears only when growing cluster cardinality and component population are both allowed to contribute.

The third stress test is subpolynomial spectral height. If `tau=0`, then (10) gives `r=0` and the uniform packing estimate gives `kappa=0`. Equation (8) therefore forces

\[
b\ge c.
\]

Thus arbitrarily many components at `x^(o(1))` height cannot collectively bypass the FD-276 mechanism unless the maximal desingularized background envelope is at least `x^(0.415037...-o(1))`.

The fourth stress test is phase coherence. Nothing in (19) assumes random phases, orthogonality, Bohr averaging, or integer-horizon equidistribution. Even if every component has the best possible sign at the same source-selected horizon, its total contribution is bounded by the population/cardinality/background budget. The new obstruction is therefore independent of the phase-cancellation results in FD-270--FD-273.

The fifth stress test is truncation. The theorem is stated for **complete** reciprocal-log components. If a finite zero packet is cut through one component at its upper edge, that single incomplete boundary component is not covered by (18) because its exterior collar has not yet been certified. This is a genuine boundary effect, not silently absorbed into the aggregate theorem. All complete components below the truncation obey the ledger above; the one cut component remains a separate single-component/remainder issue.

## Prior-art check

Riemann--von Mangoldt, the ordinary count `N_zeta(T)~(T/2pi) log(T/2pi)`, and the interpretation of `S(t)` as the zero-counting error are classical and are not claimed as new. The only load-bearing modern external input is the RH-conditional sharp bound

\[
|S(t)|\le(1/4+o(1))\log t/\log\log t
\]

from Emanuel Carneiro, Vorrapan Chandee and Micah B. Milinovich, *Bounding S(t) and S_1(t) on the Riemann hypothesis*, Mathematische Annalen **356**(3) (2013), 939--968, DOI `10.1007/s00208-012-0876-z`, already anchored in `SOURCES.md` for FD-277.

A fresh targeted search checked current literature on close zeta zeros, local zero-count tails, short-interval zero statistics, and `S(t)` excursions. It found neighboring results controlling atypically large local zero counts, but no result coupling those classical zero-count constraints to the FD-276 grouped consecutive-difference/divisor-replication repair budget to obtain the aggregate exponent ledger (8) or the combined height/background tariff (11). No additional source is load-bearing here, so `SOURCES.md` does not need another anchor.

## Implications

FD-277 left one structurally different loophole: perhaps no cluster is individually large, but many complete close-zero components add coherently. FD-278 prices exactly that alternative. The number of components can indeed replace part of the single-cluster cardinality bill, but their population itself is bounded by spectral height, while RH simultaneously bounds the largest component that can fit below the same height.

With tame background conditioning, perfect aggregate coherence below `x^(0.268338...-o(1))` is therefore impossible for all complete components combined. At still lower height, equation (30) quantifies the polynomial background anomaly that would be required to compensate.

This does not close the full spectral route. A surviving construction may use higher zeros, polynomially bad desingularized backgrounds, the incomplete component at a truncation boundary, a packet remainder, multiple/off-critical zeros outside the present hypotheses, or additional structure not represented by the complete-component packet. What is closed is the specific FD-277 loophole in which arbitrarily many low-height, tame-background complete components were treated as a free source of coherent amplification.

## Limitations

The result assumes RH and simple nontrivial zeros, inherits the FD-276 complete-component/collar construction, and uses the RH-conditional Carneiro--Chandee--Milinovich estimate for `S(t)`. The exponents are asymptotic and assume a fixed polynomial depth relation `x=N^(lambda+o(1))`.

The aggregate estimate uses a maximum background envelope `mathfrak B_*`; it does not exploit a distributional saving if only a few components have large background conditioning. Conversely, because it uses the triangle inequality, it cannot benefit from cancellation between components. This is intentional: the theorem is a worst-case obstruction to aggregate coherence.

The theorem does not control the one incomplete component created by truncating a finite zero packet through a reciprocal-log component, nor the explicit-formula remainder. Those remain separate spectral-boundary questions.
