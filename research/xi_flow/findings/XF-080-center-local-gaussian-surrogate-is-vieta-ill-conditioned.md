# XF-080 — center-local Gaussian surrogate is Vieta-ill-conditioned

**Status:** `EXACT-DERIVED` + `NEGATIVE/INTERFACE` + `VIETA-NORMALIZATION-OBSTRUCTION` + `STRUCTURAL/BRIDGE`. XF-078 proves that the matched Gaussian quotient can be approximated exponentially well on the safe center rectangle by an explicit trigonometric polynomial with exactly the `N+1` Fourier modes available to an `N`-zero periodic Vieta carrier. XF-079 then removes the center-averaging mismatch and reduces the remaining source interface to an object/dictionary problem at one safe center.

The mode count is nevertheless not enough. If the **explicit XF-078 approximant itself** is interpreted as an `N=2D` Vieta carrier by normalizing one outer Fourier mode, its first log-Vieta/root-power mode is macroscopic:

\[
\boxed{
|P_1|\asymp D\asymp N.
}
\tag{1}
\]

More precisely, the two possible outer normalizations give

\[
\boxed{
P_1^{(+)}
=\frac{2D(2D-1)}{2D-3},
\qquad
P_1^{(-)}
=\frac{2D(2D+1)}{2D-1},
\qquad D\ge2.
}
\tag{2}
\]

The same coefficient calculation also gives

\[
\boxed{
\left|\frac{p_{-D,D}}{p_{D,D}}\right|
=\frac{2D-1}{2D+1}<1,
}
\tag{3}
\]

so the canonical surrogate cannot even be the trigonometric carrier of `2D` real periodic roots: a real-root carrier has unit-modulus terminal Vieta coefficient. Allowing complex auxiliary roots does not repair the source bridge, because (2) violates by a factor `Theta(N)` the bounded-infrared hypothesis used by XF-070--XF-071 for a bounded-displacement periodic state.

Thus XF-078 remains a valid **function approximation theorem**, but its explicit finite-band approximant cannot be inserted naively into XF-067--XF-071 as a zero carrier. The live interface needs an additional divisor/outer-mode conditioning statement, or a different construction that transfers the Xi quotient directly into the weighted log-Vieta resource without interpreting the locally accurate Fourier extension as a root polynomial.

## 1. Extreme coefficients of the XF-078 approximant are exponentially small

Use the notation of XF-078,

\[
\theta=\frac{2\pi z}{L},
\qquad
\nu=\frac{1-\cos\theta}{2},
\tag{4}
\]

and its explicit degree-`D` approximant

\[
A_D(\theta)
:=
\sum_{n=0}^{D}a_n\nu^n
+\frac{i}{2}\sin\theta
\sum_{n=0}^{D-1}b_n\nu^n,
\tag{5}
\]

where

\[
a_n=(-1)^n\binom{1/2}{n},
\qquad
b_n=4^{-n}\binom{2n}{n}.
\tag{6}
\]

Write

\[
A_D(\theta)
=\sum_{k=-D}^{D}p_{k,D}e^{ik\theta}.
\tag{7}
\]

Set `w=e^{i theta}`. Since

\[
\nu
=\frac{2-w-w^{-1}}4
=-\frac{(w-1)^2}{4w},
\tag{8}
\]

direct coefficient extraction gives, for `|k|<=n`,

\[
[w^k]\nu^n
=(-1)^k4^{-n}\binom{2n}{n+k}.
\tag{9}
\]

Also

\[
\frac i2\sin\theta=\frac{w-w^{-1}}4.
\tag{10}
\]

Only the top one or two terms in (5) can contribute to the outer Laurent coefficients. Using

\[
\binom{1/2}{D}
=(-1)^{D-1}\frac{b_{D-1}}{2D},
\tag{11}
\]
none of the needed estimates is asymptotic: one obtains exactly

\[
\boxed{
 p_{D,D}
 =(-1)^{D-1}
 \frac{2D+1}{2D}
 \frac{b_{D-1}}{4^D},
}
\tag{12}
\]

and

\[
\boxed{
 p_{-D,D}
 =(-1)^D
 \frac{2D-1}{2D}
 \frac{b_{D-1}}{4^D}.
}
\tag{13}
\]

In particular,

\[
|p_{\pm D,D}|
=\Theta(4^{-D}D^{-1/2}).
\tag{14}
\]

This is the hidden conditioning parameter in the statement that `A_D` uses only `2D+1` Fourier modes. The center-local approximation error in XF-078 is geometric in `D`, but converting a Laurent polynomial into normalized Vieta coordinates divides by an outer coefficient that is itself exponentially small.

## 2. Outer normalization creates a macroscopic first Vieta mode

Interpret (7) in the XF-067 carrier convention with `N=2D`. Normalizing the positive outer mode gives

\[
A_D(\theta)
=p_{D,D}
\sum_{j=0}^{2D}
(-1)^jE_j^{(+)}e^{i(D-j)\theta},
\tag{15}
\]

so

\[
E_1^{(+)}=-\frac{p_{D-1,D}}{p_{D,D}}.
\tag{16}
\]

A second direct use of (9), now retaining the `n=D,D-1,D-2` terms that can reach frequency `D-1`, yields

\[
\boxed{
-\frac{p_{D-1,D}}{p_{D,D}}
=\frac{2D(2D-1)}{2D-3}.
}
\tag{17}
\]

Newton's first identity is simply `E_1=P_1`. Therefore (17) is the first positive root-power/log-Vieta mode of this normalized carrier, proving the first formula in (2).

The result is not an artifact of choosing the wrong outer edge. Reversing the carrier and normalizing `p_{-D,D}` gives

\[
\boxed{
-\frac{p_{-D+1,D}}{p_{-D,D}}
=\frac{2D(2D+1)}{2D-1},
}
\tag{18}
\]

which is again `2D+O(1)`. Multiplying `A_D` by a nonzero scalar cannot help: every ratio in (3), (17), and (18) is scale invariant.

Equation (3) follows immediately from (12)--(13). For a carrier with real periodic roots `x_j`, the unit-circle variables `u_j=e^{2\pi i x_j/L}` satisfy

\[
|E_{2D}|=\prod_j|u_j|=1.
\tag{19}
\]

But the terminal coordinate of (15) has modulus `(2D-1)/(2D+1)`. Hence the explicit XF-078 surrogate necessarily has complex auxiliary root geometry if treated as a Vieta polynomial.

## 3. The size mismatch is exactly the one XF-071 cannot absorb

For the arithmetic-lattice normalization of XF-067--XF-071, a bounded-displacement state has bounded low power sums after quotienting uniform translation. Indeed, with period `N` and `x_j=j+a_j`, the elementary estimate

\[
|e^{2\pi i a_j/N}-1|
\le\frac{2\pi|a_j|}{N}
\tag{20}
\]

and cancellation of the exact lattice give `|P_1|=O(A)` when the displacement oscillation is `A=O(1)`. XF-070 uses the corresponding bound `|P_m|=O(Am)`; XF-071 then assumes bounded low log-Vieta coefficients

\[
c_m=(-1)^{m-1}\frac{P_m}{m}.
\tag{21}
\]

The surrogate (17) instead has

\[
|c_1|=|P_1|=2D+O(1).
\tag{22}
\]

At the Xi matching choice `D=M=q^2`, this is `Theta(q^2)`, not `O(1)`. Consequently the nonlinear Burgers forcing in the exact log-Vieta flow is not perturbative on this artificial carrier. In particular its first quadratic scale is

\[
a|c_1|^2
=\Theta(q^{-3})\Theta(q^4)
=\Theta(q),
\tag{23}
\]

using the XF-071 coefficient `a=4 pi^2/L^2=Theta(q^{-3})`. This is the opposite of the small-cascade regime used to protect the source-unresolved infrared block.

There is a parallel statement directly in the XF-070 weight. If one formally inserts the positive normalized carrier into the full weighted coefficient sum, the `k=1` contribution is

\[
w_1|P_1|^2
=
\left(
\int_{-1}^{1}(\pi+u)^4|\chi(u)|^2\,du
\right)
\left(\frac{2D-1}{2D-3}\right)^2,
\tag{24}
\]

because `w_1=(4D^2)^{-1}\int(\pi+u)^4|\chi(u)|^2du`. Thus it approaches a strictly positive constant whenever `chi` is nonzero. This observation by itself does **not** contradict a source band that deliberately omits fixed `k`; rather, it records why the omitted block can no longer be treated as a bounded harmless infrared reservoir.

## 4. Stress test: local Fourier accuracy does not control divisor conditioning

The obstruction is compatible with every approximation estimate in XF-078. On the safe rectangle `|nu|<=rho<1`, the function `nu^D` is `O(rho^D)`, while its outer Laurent coefficients are of size `4^{-D}`. Hence exponentially tiny changes in the center-local function norm can alter exponentially tiny outer coefficients by order-one relative factors. Normalized Vieta coordinates divide by precisely those coefficients.

This makes the logical boundary sharp. XF-078 proves

\[
\|A_D-e^{i\theta/2}\|_{C^J(\text{center})}
\le C_J e^{-cD},
\tag{25}
\]

but no estimate of the form

\[
\text{small center error}
\Longrightarrow
\text{small/bounded normalized Vieta resource}
\tag{26}
\]

can be obtained from that information alone. The explicit `A_D` already falsifies the naive inference. What remains possible is a **different** surrogate selected with additional outer-mode/divisor constraints, or a direct analytic map from the Gaussian quotient to the XF-079 selector/log-Vieta observable that never normalizes the finite Fourier extension as a zero polynomial.

This finding does not rule out the center-local Gaussian strategy and does not weaken XF-073, XF-074, XF-078, or XF-079. It only removes the shortest proposed dictionary: `center-local Fourier approximation + matching mode count => usable Vieta carrier`.

## 5. Independent verification

The coefficient identities were reconstructed from (5) rather than read from a numerical artifact. As a separate exact-arithmetic check, equations (3), (17), and (18) were evaluated from the Laurent expansion for every integer `2<=D<=40`; all three identities held exactly as rational equalities. The proof above is symbolic and does not depend on that finite check.

Two additional edge cases were checked explicitly. First, rescaling the surrogate leaves all normalized Vieta ratios unchanged. Second, reversing the Laurent orientation merely exchanges (17) for (18), so the macroscopic first mode is not a convention artifact.

## 6. Prior-art and novelty boundary

The broad approximation phenomenon is classical. Fourier-extension work such as Huybrechs, *On the Fourier Extension of Nonperiodic Functions* (SIAM J. Numer. Anal., 2010), and Adcock--Huybrechs--Martin-Vaquero, *On the numerical stability of Fourier extensions* (Found. Comput. Math., 2014), studies spectrally accurate approximation of nonperiodic functions by trigonometric systems on a larger period and the associated severe coefficient/system conditioning. Remez/Turan-type local-to-global inequalities for trigonometric or exponential polynomials describe the same general possibility of large global behavior behind accurate control on a proper subarc.

No theorem from that literature is load-bearing here, so `SOURCES.md` does not need a new dependency. The line-specific result is the exact coefficient extraction (12)--(18) for the canonical XF-078 half-frequency approximant and its translation into the XF-067/XF-071 Vieta semantics. In particular, the macroscopic `P_1` and non-unit terminal Vieta coordinate are not being attributed to general Fourier-extension theory.

## 7. Consequence for `xi_flow`

XF-079 correctly identifies the remaining source interface as an object/dictionary problem. XF-080 makes that gate stricter: **center-local accuracy and a Vieta-sized mode budget are insufficient unless the outer carrier normalization/divisor is also controlled**. The explicit surrogate that proved local compressibility is too ill-conditioned in Vieta coordinates to supply the bounded source state required by the guarded periodic transport.

The next useful positive gate is therefore one of two equivalent forms: construct a center-local periodic surrogate whose relevant outer coefficient and low log-Vieta modes satisfy the bounded-displacement/weighted-source scale while retaining the XF-073 relative error, or derive the XF-079 one-center weighted selector directly from the Gaussian quotient/logarithmic derivative without promoting the XF-078 Fourier extension to a zero carrier. A positive-`Lambda` transition must still be shown to leave nontrivial mass in the same destination observable afterward.