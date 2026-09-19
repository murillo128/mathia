# WI-358 — the null-state log-energy budget does not give cofinal threshold continuity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + NON-RH`

## Claim

`WI-357` gives two exact ingredients for Suzuki's localized Weil form: every normalized null state at aperture `a` has an explicit logarithmic-energy budget

\[
\overline{\mathcal L}(w)\le B(a)
:=|\log a+(2A+1)|+2\Theta(a)+2aM(a),
\qquad
\Theta(a)=\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n},
\tag{1}
\]

and bounded-`\overline{\mathcal L}` sets have an inverse-logarithmic autocorrelation modulus. Those facts are sufficient for continuity near each **fixed** aperture, but they cannot by themselves be iterated through the cofinal sequence of prime-power thresholds.

More precisely, let

\[
q_1<q_2<\cdots
\tag{2}
\]

be the increasing sequence of prime powers and put

\[
a_j=\frac12\log q_j,
\qquad
\tau_j=\frac{\log 2}{a_j}.
\tag{3}
\]

There is an absolute `c>0` such that, for all sufficiently large `j`, one can find a **real-valued** normalized test function

\[
w_j\in C_c^\infty(-1,1),
\qquad
\|w_j\|_2=1,
\qquad
\overline{\mathcal L}(w_j)\le B(a_{j+1}),
\tag{4}
\]

for which

\[
\boxed{
|C_{w_j}(\tau_j)-C_{w_j}(\tau_{j+1})|\ge c.
}
\tag{5}
\]

One may take any fixed `c<1/2` after increasing `j`; the proof below records the safe choice `c=1/4`.

Thus the source-derived null-state budget does **not** force even the oldest active prime channel `n=2` to vary by `o(1)` between consecutive arithmetic thresholds. In Suzuki's fixed-domain source ledger the `n=2` term is

\[
P_{2,a}(w)
=-2\frac{\log2}{\sqrt2}\,\Re C_w\!\left(\frac{\log2}{a}\right),
\tag{6}
\]

so the same budget class permits

\[
|P_{2,a_j}(w_j)-P_{2,a_{j+1}}(w_j)|
\ge \frac{\log2}{2\sqrt2}
\tag{7}
\]

for all sufficiently large `j`.

This is a barrier only to the **budget-only continuity bootstrap**. The witnesses `w_j` are not claimed to satisfy Suzuki's null equation. Consequently the result does not obstruct a proof that exploits cancellation among the actual von-Mangoldt channels, the exact first-crossing eigen-equation, or a source-specific coercive reserve. It shows that such extra structure is necessary: finiteness of the logarithmic energy plus the explicit absolute budget from `WI-357` cannot make the shrinking threshold spacing do the work by itself.

## 1. Consecutive source thresholds still resolve frequencies of logarithmic cost only `O(a)`

Write

\[
a=a_j,
\qquad
b=a_{j+1},
\qquad
q=q_j,
\qquad
q'=q_{j+1},
\qquad
h=b-a.
\tag{8}
\]

Because distinct prime powers are distinct integers,

\[
q'\ge q+1.
\tag{9}
\]

Bertrand's postulate supplies a prime in `(q,2q)`, hence the next prime power satisfies `q'<2q`. Therefore

\[
\frac1{2(q+1)}
\le
h=\frac12\log\frac{q'}q
<\frac12\log2.
\tag{10}
\]

The lower bound uses `\log(1+x)\ge x/(1+x)`.

For the already-active `n=2` shift define

\[
\delta_j:=\tau_j-\tau_{j+1}
=(\log2)\frac{h}{ab}>0.
\tag{11}
\]

If `c_0=(1/2)\log2`, then `b\le a+c_0`, so (10) gives

\[
\delta_j
\ge
\frac{\log2}{2(q+1)a(a+c_0)}.
\tag{12}
\]

Since `q=e^{2a}`,

\[
\boxed{
\log\frac1{\delta_j}
\le 2a+2\log a+O(1).
}
\tag{13}
\]

On the other hand `h<c_0` gives `\delta_j=O(a^{-2})`, while

\[
\frac{\tau_{j+1}}{\delta_j}
=rac{a}{h}
\ge \frac{2a}{\log2}
\longrightarrow\infty.
\tag{14}
\]

Hence consecutive prime-power thresholds can distinguish oscillations of frequency `Z_j\asymp1/\delta_j`, but the logarithmic form charges such a frequency only by

\[
\log Z_j=O(a_j+\log a_j).
\tag{15}
\]

That is the scale mismatch used below.

## 2. Real smooth modulations produce order-one autocorrelation motion

Fix a real nonzero

\[
\phi\in C_c^\infty(-1/4,1/4),
\qquad
\|\phi\|_2=1,
\tag{16}
\]

and write

\[
C_\phi(t)=\int\phi(x+t)\phi(x)\,dx.
\tag{17}
\]

For `Z>0` define the real oscillatory test function

\[
w_Z(x)=N_Z^{-1}\phi(x)\cos(Zx),
\qquad
N_Z=\|\phi\cos(Z\cdot)\|_2.
\tag{18}
\]

Riemann--Lebesgue gives `N_Z^2\to1/2`. The product-to-sum identity gives, uniformly for `t` in a fixed small neighborhood of zero,

\[
C_{w_Z}(t)
=\cos(Zt)C_\phi(t)+o_{Z\to\infty}(1).
\tag{19}
\]

Indeed the second product-to-sum term is the Fourier transform at frequency `2Z` of the smooth compactly supported amplitude `x\mapsto\phi(x+t)\phi(x)`, hence decays uniformly on compact `t`-sets.

Put

\[
r_j:=\frac{\tau_{j+1}}{\delta_j}=\frac{a_j}{a_{j+1}-a_j}.
\tag{20}
\]

By (14), `r_j\to\infty`. For

\[
D_r(u):=\cos((r+1)u)-\cos(ru),
\tag{21}
\]

a direct average over `u\in[\pi,3\pi]` gives

\[
\frac1{2\pi}\int_\pi^{3\pi}|D_r(u)|^2\,du
\longrightarrow1
\qquad(r\to\infty).
\tag{22}
\]

The only fixed-frequency cross term is `\cos u`, whose integral over this interval is zero; all terms with frequency proportional to `r` have vanishing averages. Thus, for sufficiently large `j`, there is some `u_j\in[\pi,3\pi]` for which

\[
|D_{r_j}(u_j)|\ge\frac12.
\tag{23}
\]

Choose

\[
Z_j:=\frac{u_j}{\delta_j}.
\tag{24}
\]

Then `Z_j\to\infty`, `Z_j\delta_j=u_j`, and

\[
Z_j\tau_{j+1}=r_ju_j,
\qquad
Z_j\tau_j=(r_j+1)u_j.
\tag{25}
\]

Since `\tau_j,\tau_{j+1}\to0`, `C_\phi(\tau_j),C_\phi(\tau_{j+1})\to1`. Combining (19), (23), and (25) yields

\[
|C_{w_{Z_j}}(\tau_j)-C_{w_{Z_j}}(\tau_{j+1})|
\ge\frac14
\tag{26}
\]

for all sufficiently large `j`. This proves the real-valued order-one oscillation required in (5).

## 3. The witnesses lie far inside the source-derived null budget

Suzuki's Fourier identity, used in `WI-357`, is

\[
\overline{\mathcal L}(w)
=
\frac1{2\pi}\int_{\mathbb R}
(\log|z|+C_0)|\widehat w(z)|^2\,dz.
\tag{27}
\]

For the modulated bump (18), the Fourier transform is a fixed linear combination of translates of `\widehat\phi` by `\pm Z`. Since `\widehat\phi` is Schwartz and

\[
1+|u\pm Z|\le(1+|u|)(1+Z),
\tag{28}
\]

there are constants `K_1,K_2`, depending only on `\phi`, such that

\[
\overline{\mathcal L}(w_Z)
\le K_1\log(1+Z)+K_2
\qquad(Z\ge1).
\tag{29}
\]

Equations (12) and (24) imply

\[
\log(1+Z_j)\le2a_j+2\log a_j+O(1),
\tag{30}
\]

hence

\[
\overline{\mathcal L}(w_{Z_j})=O(a_j+\log a_j).
\tag{31}
\]

By the prime number theorem and partial summation,

\[
\Theta(a)
=
\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
=2e^a+o(e^a).
\tag{32}
\]

Therefore the explicit budget (1) satisfies

\[
B(a)\ge2\Theta(a)=4e^a+o(e^a).
\tag{33}
\]

Combining (31) and (33) proves

\[
\overline{\mathcal L}(w_{Z_j})\le B(a_{j+1})
\tag{34}
\]

for every sufficiently large `j`. Equations (26) and (34) establish (4)--(5). Multiplying (26) by the exact coefficient `2\log2/\sqrt2` of the prime-2 channel proves (7).

The comparison is very non-tight: the adversarial real modulation needs only `O(a)` logarithmic energy at the next-threshold resolution, while the absolute null-state budget available from the source equation is exponentially larger, `\gg e^a`.

## 4. What this closes

`WI-356` shows that a newly activated prime channel is singular in `L^2` operator norm but infinitesimally small relative to `\overline{\mathcal L}` when one approaches a **fixed** threshold from above. `WI-357` then proves that actual null states at a fixed aperture have finite `\overline{\mathcal L}` and derives an explicit inverse-logarithmic autocorrelation modulus.

A possible continuation was to hope that the source thresholds become so close that these local continuity neighborhoods can eventually be chained using only the budget `B(a)`. Equations (5) and (34) rule out that argument. At the scale of consecutive thresholds, the permitted logarithmic-energy class still contains real smooth states on which even the fixed `n=2` source channel changes by order one. The shrinking aperture spacing is exactly offset by the weak logarithmic price of high modulation frequency, long before the exponentially growing absolute source budget becomes restrictive.

Equivalently, no statement of the form

\[
\|w\|_2=1,
\qquad
\overline{\mathcal L}(w)\le B(a_{j+1})
\quad\Longrightarrow\quad
|C_w(\tau_j)-C_w(\tau_{j+1})|=o(1)
\tag{35}
\]

can hold. Thus the inverse-log modulus in `WI-357` cannot be upgraded to a cofinal threshold bootstrap merely by optimizing its generic Fourier split.

This leaves exactly the source-specific gate already suggested by the canonical research mandate: a successful no-crossing argument must use information beyond the absolute energy budget, such as cancellation/coercivity in the exact null equation, joint constraints among several prime translations, or a reserve estimate whose strength is tied to that source structure rather than to generic `H^{\log}` compactness.

## 5. Stress tests and evidence boundary

The finding does **not** construct a Suzuki null state, an off-critical zero, or a counterexample to RH. The witnesses `w_j` are deliberately generic elements of the budget class. Their role is to prove an information-content barrier: any argument that forgets the null equation after extracting only (1) cannot distinguish them from genuine null states.

Reality does not rescue the route: the witnesses in (18) are real. Smoothness does not rescue it either: they lie in `C_c^\infty(-1,1)`. Nor is this the `L^2` norm-jump obstruction from `WI-356`: the `n=2` channel has been active for all large apertures, and the obstruction here is cofinal high-frequency variation inside the logarithmic-energy class.

The result also does not say that Suzuki's full source ledger changes by order one on an actual ground state between consecutive thresholds. Other source terms can cancel the prime-2 motion, and the exact eigen-equation may forbid the oscillatory witnesses. Those are precisely the pieces of arithmetic/eigenfunction information that the budget-only relaxation discards.

## 6. Prior art and novelty audit

The load-bearing literature input is Suzuki's fixed-domain Weil-form identity and Fourier representation of the logarithmic form, together with the standard prime number theorem. `WI-356` and `WI-357` already import and verify the relevant Suzuki formulas. Classical compactness theory for logarithmic Sobolev/log-Laplacian spaces explains why a **fixed** logarithmic-energy ball is compact in `L^2`; it does not give uniform compactness when the allowed energy grows with the aperture.

The local `weil_inertia` corpus was checked against the recent Suzuki chain. `WI-257` proves that an abstract bounded-perturbation zero-mode equation gives no regularity upgrade; `WI-258` uses phase modulation as a positive variational family at one fixed first crossing; `WI-356` isolates the activation topology; and `WI-357` supplies the explicit budget and continuity modulus. None of those results compares the growth of `B(a)` with the actual consecutive prime-power threshold resolution or constructs the real smooth modulation witnesses (18)--(34).

A targeted literature search around logarithmic Fourier moments, translation/autocorrelation moduli, logarithmic-Laplacian compactness, and Suzuki's localized operator found the standard fixed-energy compactness framework but no result asserting a cofinal modulus at a growing source-controlled budget. No priority claim is made. The derived contribution here is the exact threshold-scale comparison and the resulting decisive no-go for the budget-only iteration.

## Sources

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), DOI `10.48550/arXiv.2606.09096`. Primary source for the fixed-domain Rayleigh/source formula, the logarithmic Fourier form, and the localized ground-state framework used by `WI-355`--`WI-357`.
- `WI-356` and `WI-357`. Persisted local derivations of the threshold channel, null-state budget, and inverse-logarithmic autocorrelation modulus whose cofinal iteration is tested here.
