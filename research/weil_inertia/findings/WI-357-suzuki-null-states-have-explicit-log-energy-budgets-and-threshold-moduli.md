# WI-357 — Suzuki null states have explicit log-energy budgets and threshold moduli

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECT + NON-RH`

## Claim

The open subproblem left in WI-356 — obtaining a logarithmic-energy bound for a hypothetical first-crossing null state — is not an independent coercivity problem. Suzuki's fixed-domain identity already supplies such a bound directly from the null equation, and its Fourier representation gives an explicit modulus of continuity for every prime-power autocorrelation on bounded-`\mathcal L` sets.

Consequently, the apparent `L^2` singularity when a new prime-power channel activates is completely removable at the level relevant to an actual ground/null state. What remains missing for an RH bootstrap is not compactness or bounded `\mathcal L` energy, but a **positive source-side reserve** that can be propagated quantitatively.

More precisely, for a normalized null state `\|w\|_2=1`, `\bar q_a(w)=0`, define
\[
\Theta(a):=\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n},
\qquad
M(a):=\sup_{|u|\le2a}|r''(u)|.
\tag{1}
\]
Then Suzuki's equation (4.5) implies the explicit finite budget
\[
\boxed{
\overline{\mathcal L}(w)
\le
B(a):=
|\log a+(2A+1)|+2\Theta(a)+2aM(a).
}
\tag{2}
\]
Here `A` and `r` are exactly Suzuki's archimedean constants/remainder; `r` is `C^2`, so `M(a)<\infty` at every finite aperture.

For the zero-extended autocorrelation
\[
C_w(t):=\int_{\mathbb R}w(x+t)\overline{w(x)}\,dx,
\tag{3}
\]
put
\[
K_0:=|C_0|+\frac2\pi,
\tag{4}
\]
where `C_0` is Euler's constant in Suzuki's equation (4.6). For every `0<\delta:=|t-s|<1`, every `w` in the logarithmic form domain satisfies
\[
\boxed{
|C_w(t)-C_w(s)|
\le
\sqrt\delta\,\|w\|_2^2
+
\frac{4\bigl(\overline{\mathcal L}(w)+K_0\|w\|_2^2\bigr)}{\log(1/\delta)}.
}
\tag{5}
\]
Thus on every bounded-`\mathcal L` set the translated prime terms are uniformly continuous, with an explicit inverse-logarithmic modulus, even across activation thresholds where their `L^2` operator norm jumps as in WI-356.

Combining (2), (5), and the endpoint estimate of WI-356 gives a quantitative inherited-degeneracy statement: if a first null state occurs just above a prime-power threshold `a_q=(1/2)\log q`, then, up to an explicitly vanishing error, the form with the newly activated `q`-channel deleted was already null on the same state. Therefore a new prime atom cannot by itself create a first crossing out of a fixed positive reserve.

## 1. Primary-source input and correction to WI-356

The primary source is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026). After scaling `(-a,a)` to `(-1,1)`, Suzuki's equation (4.5) gives, for normalized `w`,
\[
\bar q_a(w)
=
-\log a-(2A+1)
+\overline{\mathcal L}(w)
-S_a(w)-R_a(w),
\tag{6}
\]
where
\[
S_a(w)
=2\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
\Re C_w\!\left(\frac{\log n}{a}\right)
\tag{7}
\]
and
\[
R_a(w)
=a\int_{-1}^{1}\int_{-1}^{1}
 r''(a(x-y))w(y)\overline{w(x)}\,dxdy.
\tag{8}
\]
The formulas extend to the closed form by Suzuki's closure argument in Sections 4.2--4.4.

For normalized `w`, Cauchy--Schwarz gives `|C_w(t)|\le1`, hence
\[
|S_a(w)|\le2\Theta(a).
\tag{9}
\]
Also `\|w\|_1^2\le2\|w\|_2^2=2`, so
\[
|R_a(w)|
\le aM(a)\|w\|_1^2
\le2aM(a).
\tag{10}
\]
If `\bar q_a(w)=0`, rearranging (6) and applying (9)--(10) proves (2).

This also matches an ingredient already present in Suzuki's proof of lower semicontinuity. In Section 4.4 he writes `\bar q_a=\bar q^0+\bar q_a^1`, with `\bar q^0=\overline{\mathcal L}-(2A+1)\|\cdot\|_2^2`, and observes that `\bar q_a^1` is uniformly `L^2`-bounded when `a` stays in a compact neighborhood. For normalized ground states with bounded eigenvalues this gives uniform boundedness of `\overline{\mathcal L}` and compactness in `L^2`.

Therefore the final caveat in WI-356 was too pessimistic: bounded logarithmic energy of a first-crossing state does **not** require a new coercivity theorem. The exact null equation already supplies it. The unresolved quantity is a lower bound for the pre-existing/source-deleted form.

## 2. Explicit autocorrelation modulus from the logarithmic Fourier moment

Suzuki's equation (4.6) is
\[
\overline{\mathcal L}(w)
=
\frac1{2\pi}\int_{\mathbb R}
(\log|z|+C_0)|\widehat w(z)|^2\,dz.
\tag{11}
\]
Let
\[
J_+(w):=\frac1{2\pi}\int_{|z|>1}\log|z|\,|\widehat w(z)|^2\,dz,
\qquad
J_-(w):=\frac1{2\pi}\int_{|z|<1}(-\log|z|)|\widehat w(z)|^2\,dz.
\tag{12}
\]
Because `w` is supported in `(-1,1)`,
\[
|\widehat w(z)|\le\|w\|_1\le\sqrt2\,\|w\|_2.
\tag{13}
\]
Since `\int_{|z|<1}-\log|z|\,dz=2`,
\[
J_-(w)\le\frac2\pi\|w\|_2^2.
\tag{14}
\]
Equation (11) therefore yields the safe one-sided bound
\[
J_+(w)
\le
\overline{\mathcal L}(w)+K_0\|w\|_2^2.
\tag{15}
\]

Plancherel gives
\[
C_w(t)
=
\frac1{2\pi}\int_{\mathbb R}|\widehat w(z)|^2e^{-izt}\,dz.
\tag{16}
\]
For `\delta=|t-s|`, split at `R=\delta^{-1/2}>1`. On `|z|\le R`, use `|e^{iz\delta}-1|\le|z|\delta`; on `|z|>R`, use the bound `2` and `\log|z|\ge\log R`. This gives
\[
|C_w(t)-C_w(s)|
\le
\delta R\|w\|_2^2
+
\frac{2J_+(w)}{\log R}.
\tag{17}
\]
Substituting `R=\delta^{-1/2}` and (15) proves (5).

The rate is deliberately crude. Its role is structural: the only vectors capable of seeing the `L^2` norm jump from WI-356 must drive `\mathcal L` to infinity, while actual null/ground states at finite aperture have a finite source-controlled `\mathcal L` budget.

## 3. Uniform aperture modulus on a compact interval

The same estimate controls all prime terms in Suzuki's finite source ledger simultaneously. Fix
\[
I=[\alpha,\beta]\subset(0,\infty),
\qquad
\Theta_\beta:=\sum_{n\le e^{2\beta}}\frac{\Lambda(n)}{\sqrt n},
\tag{18}
\]
and define
\[
M_\beta:=\sup_{|u|\le2\beta}|r''(u)|,
\qquad
\omega_\beta(\eta)
:=\sup_{\substack{|u|,|v|\le2\beta\\|u-v|\le\eta}}
|r''(u)-r''(v)|.
\tag{19}
\]
For `a,b\in I`, let `h=|a-b|` and
\[
H:=\frac{2\beta}{\alpha^2}h.
\tag{20}
\]
Every prime shift appearing anywhere in `I` obeys
\[
\left|\frac{\log n}{a}-\frac{\log n}{b}\right|\le H.
\tag{21}
\]
Terms not yet active can be included harmlessly because the zero-extended autocorrelation is exactly zero for shifts `t\ge2`.

For `H<1`, summing (5), bounding `|\log a-\log b|\le h/\alpha`, and using the uniform continuity of `r''` on `[-2\beta,2\beta]` gives, for normalized `w`,
\[
\boxed{
|\bar q_a(w)-\bar q_b(w)|
\le
\frac h\alpha
+2hM_\beta+2\beta\omega_\beta(2h)
+2\Theta_\beta
\left[
\sqrt H+
\frac{4(\overline{\mathcal L}(w)+K_0)}{\log(1/H)}
\right].
}
\tag{22}
\]
The right-hand side tends to zero with `h` on every set with bounded `\overline{\mathcal L}`. Equation (22) is a quantitative version of the continuity mechanism that Suzuki proves qualitatively through compactness in Section 4.4.

In particular, Suzuki's own argument already shows that normalized ground states in a compact aperture neighborhood have uniformly bounded `\overline{\mathcal L}`. Alternatively, a completely explicit (though crude) bound follows from (6): upper-bound the ground eigenvalue by evaluating `\bar q_a` on one fixed normalized smooth test function, then apply the finite bounds (9)--(10). Substituting that bound into (22) gives an explicit modulus for the lowest eigenvalue by the min--max principle.

No differentiability of `\lambda(a)` is asserted; only a computable modulus inherited from the common logarithmic form and the finite source ledger.

## 4. A newly activated prime atom can only inherit an existing near-null state

Let `q=p^k` and
\[
a_q=\frac12\log q,
\qquad
c_q=\frac{\Lambda(q)}{\sqrt q},
\qquad
\varepsilon(a)=2-\frac{\log q}{a}.
\tag{23}
\]
For `a>a_q` close enough that `0<\varepsilon<1/2`, WI-356 proves
\[
|P_{q,a}(w)|
\le
\frac{2c_q}{\log(1/(2\varepsilon))}\,\overline{\mathcal L}(w).
\tag{24}
\]
Write
\[
\bar q_a=\bar q_a^{(-q)}+P_{q,a}
\tag{25}
\]
with the `q`-channel deleted from `\bar q_a^{(-q)}`. If a normalized null state exists at aperture `a`, equations (2) and (24) give
\[
\boxed{
|\bar q_a^{(-q)}(w)|
\le
\frac{2c_q B(a)}{\log(1/(2\varepsilon(a)))}.
}
\tag{26}
\]
The right-hand side tends to zero as `a\downarrow a_q`.

Moreover, (22) can be applied to the source ledger with `q` omitted. Hence if the threshold form itself has a fixed positive reserve
\[
\lambda(a_q)=\delta>0,
\tag{27}
\]
then for a hypothetical null state just above the threshold,
\[
\delta
\le
|\bar q_{a_q}(w)-\bar q_a^{(-q)}(w)|
+|\bar q_a^{(-q)}(w)|,
\tag{28}
\]
and the two terms on the right tend explicitly to zero by (22), (2), and (26). Therefore there is an effective one-sided neighborhood of `a_q` in which no null state can occur.

Qualitatively, positivity in a neighborhood already follows from Suzuki's continuity theorem. The new information is the exact source-ledger mechanism: **a first crossing arbitrarily close above a threshold would force an approximate null vector for the form that was already present before the new atom was added.** The threshold channel itself cannot manufacture the crossing from a fixed reserve.

## 5. Consequence and remaining bottleneck

WI-355 reduces any RH failure to a finite first crossing of the localized ground energy. WI-356 then showed that newly activated prime atoms are singular in `L^2` norm but infinitesimally small relative to `\mathcal L`. The present finding closes the missing compatibility step: actual null/ground states cannot exploit the `L^2` norm jump because their logarithmic energy is bounded by the exact source equation, and the whole finite source ledger is uniformly continuous on such bounded-energy states.

This kills one possible obstruction but does **not** prove RH. Local continuity cannot be iterated to infinity without quantitative reserve. A sequence of positive threshold values `\lambda(a_q)` could in principle approach zero so rapidly that the exclusion neighborhoods shrink correspondingly. The remaining load-bearing target is therefore sharper and source-side:

- prove a positive lower bound for the source-deleted/pre-existing form that is compatible with the logarithmic topology; or
- derive from the first-crossing null equation an arithmetic cancellation/coercivity identity strong enough to contradict (26)--(28).

Thus `\mathcal L`-energy control and threshold continuity should no longer be treated as independent open gates. The open gate is **coercive reserve / arithmetic sign**, not regularity.

## 6. Novelty and prior-art audit

Suzuki's paper is load-bearing prior art for equations (4.5)--(4.6), the compact embedding of `H^{\log}(-1,1)`, qualitative continuity of the lowest eigenvalue, and the observation in his lower-semicontinuity proof that ground states near a fixed aperture have uniformly bounded logarithmic energy. Those points are not new here.

The derived contribution is the explicit null-state budget (2), the Fourier split producing the autocorrelation modulus (5), the assembled compact-aperture estimate (22), and their use with WI-356 to obtain the source-deleted near-null constraint (26)--(28). A targeted literature audit around logarithmic Sobolev spaces, Fourier log moments, and Suzuki's localized operator did not locate this exact quantitative package. This is only a statement about the audited corpus, not a claim of external priority.

Classical logarithmic Sobolev-space literature provides the surrounding function-space context, but no such general reference is needed for the proof: (5) follows directly from Suzuki's Fourier identity, Plancherel, `|e^{iu}-1|\le|u|`, and the elementary split at `|z|=\delta^{-1/2}`.

## Sources

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), DOI `10.48550/arXiv.2606.09096`. Primary source for equations (4.4)--(4.6), the fixed-domain source ledger, compactness of `H^{\log}(-1,1)`, and qualitative continuity/bounded-energy ground-state argument.
- D. E. Edmunds and H. Triebel, **Logarithmic Sobolev Spaces and Their Applications to Spectral Theory**, *Proceedings of the London Mathematical Society* s3-71 (1995), 333--371, DOI `10.1112/plms/s3-71.2.333`. Background only for logarithmic Sobolev spaces; not load-bearing.
- WI-355 and WI-356. Internal antecedents for the finite first-crossing reduction and the exact norm-jump/form-smallness dichotomy at a newly activated Suzuki prime-power channel.
