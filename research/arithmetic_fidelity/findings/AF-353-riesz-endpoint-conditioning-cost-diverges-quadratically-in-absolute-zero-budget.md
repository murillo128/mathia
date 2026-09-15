# AF-353 — Riesz endpoint conditioning has unavoidable norm blow-up and quadratic absolute zero-budget cost

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `BOUNDARY-CLARIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-352 proves that every fixed positive Riesz order is enough to make the sharp critical boundary norm RH-equivalent, while the unsmoothed endpoint is not. The approach to that open endpoint is necessarily non-uniform, and one natural spectral conditioning budget has an exact blow-up law.

Let the nontrivial zeros of `zeta` be `rho=beta+i gamma`, counted with multiplicity, and for `delta>0` define the positive-ordinate absolute multiplier budget

\[
\mathcal A_+(\delta)
:=
\sum_{\rho:\,\gamma>0}
\left|B(\rho,1+\delta)\right|,
\qquad
B(\rho,1+\delta)
=
\frac{\Gamma(\rho)\Gamma(1+\delta)}
     {\Gamma(\rho+1+\delta)}.
\tag{1}
\]

Then, **unconditionally**,

\[
\boxed{
\mathcal A_+(\delta)
=
\frac{1}{2\pi\delta^2}
-
\frac{\log(2\pi)+\gamma_E}{2\pi\delta}
+O(1)
\qquad(\delta\to0^+),
}
\tag{2}
\]

where `gamma_E` is Euler's constant. If both signs of the ordinates are included, conjugation doubles the budget:

\[
\mathcal A_{\mathrm{sym}}(\delta)
=
\frac{1}{\pi\delta^2}
-
\frac{\log(2\pi)+\gamma_E}{\pi\delta}
+O(1).
\tag{3}
\]

Thus AF-352's arbitrarily weak positive smoothing is not arbitrarily cheap: the canonical triangle-inequality budget for the surviving zero modes has a **second-order pole** at the unsmoothed endpoint.

There is also an exact statement for the actual prime Riesz profile. Define, avoiding the integer endpoint convention,

\[
K(\delta)
:=
\sup_{\substack{X\ge2\\X\notin\mathbb N}}
X^{-1/2}
\left|\mathcal R_\delta[\Lambda-1](X)\right|.
\tag{4}
\]

Under RH, AF-352 gives `K(delta)<infinity` for every fixed `delta>0`, but nevertheless

\[
\boxed{
\lim_{\delta\to0^+}K(\delta)=+\infty.
}
\tag{5}
\]

Equation (2) does **not** assert that the optimal profile norm `K(delta)` grows like `delta^{-2}`. It identifies the exact blow-up of the absolute zero-coefficient budget used by the unconditional summability/conditioning mechanism, while (5) shows separately that the actual critical profile cannot remain uniformly bounded as smoothing is removed.

## Derivation

### 1. The beta multiplier is asymptotically the secondary-zeta weight

Fix a small `delta_0>0`. Nontrivial zeros satisfy `0<beta<1`. The standard Gamma-ratio expansion, uniformly for `beta` and `delta` in compact ranges, gives as `|gamma|->infinity`

\[
\left|
\frac{\Gamma(\beta+i\gamma)}
     {\Gamma(\beta+1+\delta+i\gamma)}
\right|
=
|\gamma|^{-1-\delta}
\left(1+O_{\delta_0}(|\gamma|^{-1})\right),
\qquad 0<\delta\le\delta_0.
\tag{6}
\]

Therefore

\[
\left|B(\rho,1+\delta)\right|
=
\Gamma(1+\delta)\,\gamma^{-1-\delta}
+O_{\delta_0}(\gamma^{-2-\delta}).
\tag{7}
\]

The error is summable over the zeros uniformly for `0<delta<=delta_0`, because the Riemann--von Mangoldt count implies

\[
\sum_{\gamma>0}\gamma^{-2}<\infty.
\tag{8}
\]

Writing the secondary zeta over ordinates as

\[
G(s):=\sum_{\gamma>0}\gamma^{-s},
\qquad \Re s>1,
\tag{9}
\]

with multiplicity, (7)--(8) yield

\[
\mathcal A_+(\delta)
=
\Gamma(1+\delta)G(1+\delta)+O(1)
\qquad(\delta\to0^+).
\tag{10}
\]

No RH assumption enters this reduction: the leading Gamma-ratio magnitude depends on the ordinate, while the zero count and the convergence in (8) are unconditional.

### 2. The double pole of the secondary zeta gives the exact conditioning singularity

Bondarenko--Ivić--Saksman--Seip record the unconditional continuation near `s=1`

\[
G(s)
=
\frac{1}{2\pi(s-1)^2}
-
\frac{\log(2\pi)}{2\pi(s-1)}
+O(1).
\tag{11}
\]

Hence

\[
G(1+\delta)
=
\frac{1}{2\pi\delta^2}
-
\frac{\log(2\pi)}{2\pi\delta}
+O(1).
\tag{12}
\]

Using

\[
\Gamma(1+\delta)
=
1-\gamma_E\delta+O(\delta^2),
\tag{13}
\]

and substituting (12)--(13) into (10) proves (2). Conjugate zeros have equal multiplier modulus, so (3) follows immediately.

The order of the singularity is therefore not an artifact of a dyadic upper bound. It is exactly the pole order forced by the asymptotic zero density: roughly `T log T` target modes are being weighted by the barely summable kernel `gamma^{-1-delta}`.

### 3. The actual critical profile must also become unbounded as `delta->0+`

Assume RH. AF-352 proves that `K(delta)` in (4) is finite for every positive `delta`. Suppose, contrary to (5), that it does not tend to infinity. Then there are `M<infinity` and a sequence `delta_j->0+` such that

\[
K(\delta_j)\le M
\qquad\text{for all }j.
\tag{14}
\]

Fix any noninteger `X>=2`. The defining Riesz sum is finite, and every factor with `n<=X` has `1-n/X>0`. Thus termwise

\[
\left(1-\frac nX\right)^{\delta_j}\longrightarrow1,
\tag{15}
\]

so

\[
\mathcal R_{\delta_j}[\Lambda-1](X)
\longrightarrow
\mathcal R_0[\Lambda-1](X).
\tag{16}
\]

The uniform bound (14) would therefore imply

\[
|\mathcal R_0[\Lambda-1](X)|\le M\sqrt X
\tag{17}
\]

for every noninteger `X>=2`. Taking `X=N+1/2` gives exactly

\[
\mathcal R_0[\Lambda-1](N+1/2)
=
\psi(N)-N.
\tag{18}
\]

But the classical Hardy--Littlewood oscillation theorem used already in AF-352 gives

\[
\psi(x)-x
=
\Omega_\pm\!\left(\sqrt{x}\,\log\log\log x\right).
\tag{19}
\]

Passing from such real `x` to its integer part changes `\psi(\lfloor x\rfloor)-\lfloor x\rfloor` by at most `O(1)`, so (19) contradicts (17). Hence (5) follows.

This argument deliberately uses noninteger `X`: for positive `delta` the terminal factor at an integer cutoff is zero, whereas the `delta=0` summatory convention includes that terminal coefficient. The half-integer subsequence removes that irrelevant endpoint convention from the limiting argument.

## Prior art and novelty assessment

No novelty claim is made for the analytic ingredients.

- Andriy Bondarenko, Aleksandar Ivić, Eero Saksman, and Kristian Seip, **“On certain sums over ordinates of zeta-zeros II,”** *Hardy-Ramanujan Journal* 41 (2018), 85--97, DOI `10.46298/hrj.2019.5110`, arXiv:`1808.01763`. Their `G(s)=sum_{gamma>0} gamma^{-s}` and formula (4) give the unconditional double pole and the first two Laurent coefficients at `s=1` used in (11).
- Aleksandar Ivić, **“On certain sums over ordinates of zeta zeros,”** *Bulletin de l'Académie Serbe des Sciences et des Arts, Classe des Sciences Mathématiques et Naturelles, Sciences Mathématiques* 26 (2001), arXiv:`math/0312303`. Role: earlier study of the same secondary zeta over ordinates.
- NIST Digital Library of Mathematical Functions, **§5.11(iii), Eqs. 5.11.12--5.11.13**. Role: the Gamma-ratio asymptotic used in (6).
- Hardy--Littlewood's classical oscillation theorem and the Riemann--von Mangoldt zero count enter exactly as already audited in AF-351--AF-352.

The double pole of `G` and the Gamma-ratio asymptotic are classical. The Arithmetic Fidelity result is their synthesis with AF-352's endpoint question: it identifies an exact **conditioning price** for the compression channel and separates that absolute spectral price from the unknown sharp growth of the actual prime profile norm.

## Boundaries and failure modes

### The quadratic law is for the absolute spectral budget, not the best possible cancellation norm

`A_+(delta)` discards all phase cancellation among zero modes. Therefore (2) is an exact statement about the triangle-inequality conditioning resource behind AF-352's absolute-convergence proof, not an asymptotic formula for `K(delta)`. Establishing a rate for `K(delta)` would require quantitative control of cancellation among the critical frequencies as `delta` varies.

### The statement does not make the positive-order criterion uniform

AF-352 remains a fixed-`delta` theorem. Nothing here proves an RH criterion for a variable order `delta=delta(X)->0`, and (2) shows that any argument using the absolute zero budget loses uniformity at least quadratically as the endpoint is approached.

### The first two coefficients in (2) are insensitive to off-line horizontal positions

The secondary zeta `G` sees the ordinates with multiplicity, while the leading Gamma-ratio magnitude in (6) is independent of `beta`. This is why the budget asymptotic is unconditional. It does not imply that horizontal zero location is irrelevant to the RH discriminator: AF-352's reverse implication still relies on the Mellin singularity at the full complex zero `rho`.

### Divergence of `K(delta)` gives no rate

The compactness/pointwise-limit argument proves only `K(delta)->infinity` under RH. The endpoint omega theorem by itself does not convert into a `delta`-rate without a quantitative estimate comparing the positive-order kernel to the unsmoothed sum on an `X`-range that is itself controlled as `delta->0`.

## Consequence for Arithmetic Fidelity

AF-352 showed a striking qualitative fact: every positive decay gain in the zero multiplier crosses the summability threshold while retaining the off-critical Mellin discriminator. AF-353 supplies the missing quantitative counterweight. The threshold is open, but approaching it costs

\[
\mathcal A_+(\delta)\asymp\delta^{-2}.
\tag{20}
\]

The mechanism is now sharper: the useful resource of a compression is controlled not only by whether its multiplier exponent lies on the summable side of the target-mode density, but by **how far from the density pole the multiplier places the transformed signal**. Here the secondary zeta has a double pole at the exact boundary, so an arbitrarily small positive smoothing exponent buys boundedness only with a quadratically diverging absolute conditioning constant.

This separates three statements that should not be conflated in future compression audits: the discriminator may remain exactly present, each fixed transformed problem may be well conditioned in the declared norm, and yet the conditioning constants can become singular as the transformation approaches a less-smoothed or more information-rich boundary. A useful source-to-target theorem must price that singularity rather than infer practical recoverability from fixed-parameter fidelity alone.