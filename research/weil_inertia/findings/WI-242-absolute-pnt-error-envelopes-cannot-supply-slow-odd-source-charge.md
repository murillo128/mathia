# WI-242 — Absolute PNT-error envelopes cannot supply the slow odd source charge

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

WI-241 reduces the large-support odd-sector source problem to the signed von Mangoldt discrepancy

\[
\Delta_\Lambda^a(v)
=\int_1^{e^{2a}}x^{-1/2}C_v(\log x)\,d(\psi(x)-x),
\]

and shows that Weil positivity would require an order-one negative charge on every fixed finite-dimensional family of slowly varying odd dilates. That finding left open whether ordinary pointwise Prime Number Theorem error estimates could control this discrepancy after the exact pole/main-density cancellation.

For slow dilates the discrepancy admits an exact integration-by-parts formula. It shows that the critical source weight is precisely `x^{-3/2}` against `E(x)=psi(x)-x`. Consequently every standard absolute-envelope argument is on the wrong scale: classical unconditional PNT error bounds give an exponentially growing majorant after this weighting, while even the usual RH pointwise bound gives only a polynomially growing `O(a^3)` estimate. More generally, a regular power-log absolute majorant can yield an `a`-uniform bound only below the square-root scale, or at square-root scale with more than one logarithm of decay; Littlewood's oscillation rules out such a uniform envelope.

There is also a sharper structural identification. Under RH itself, the slow-dilate discrepancy converges to the exact constant required by WI-241,

\[
\boxed{
\Delta_\Lambda^a(U_a\phi)
\longrightarrow
\frac{M(0)}2
=2-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=-0.6860917096\ldots
}
\]

for every fixed real odd smooth compactly supported unit vector `phi`. Thus the missing source charge is genuinely an RH-scale cancellation effect, not something that follows from making `psi(x)-x` absolutely small. A neighboring theorem of Suzuki is especially relevant prior art: eventual nonpositivity of a closely related `n^{-1/2}`-weighted von Mangoldt average is itself equivalent to RH. This does not make the present autocorrelation condition equivalent to RH, but it materially redirects the source-side program away from generic PNT-error envelopes and toward cancellation-preserving identities tied to the first-crossing/finite-radius geometry.

## 1. Slow dilates turn WI-241 into an exact weighted PNT-remainder integral

Fix a real odd function

\[
\phi\in C_c^\infty(-1,1),
\qquad \|\phi\|_2=1,
\]

and define the unitary dilation

\[
(U_a\phi)(x)=a^{-1/2}\phi(x/a).
\tag{1}
\]

Let

\[
C(u):=\int_{\mathbb R}\phi(t+u)\phi(t)\,dt.
\tag{2}
\]

Then `C` is smooth, supported in `[-2,2]`, `C(0)=1`, and by Cauchy--Schwarz

\[
|C(u)|\le1.
\tag{3}
\]

The autocorrelation rescales exactly as

\[
C_{U_a\phi}(h)=C(h/a).
\tag{4}
\]

Writing

\[
E(x):=\psi(x)-x,
\tag{5}
\]

WI-241 therefore becomes

\[
\Delta_a:=\Delta_\Lambda^a(U_a\phi)
=
\int_1^{e^{2a}}
 x^{-1/2}C\!\left(\frac{\log x}{a}\right)dE(x).
\tag{6}
\]

Take `psi` to be the ordinary right-continuous Chebyshev function. There is no von Mangoldt atom at `x=1`, so `E(1)=-1`. At the upper endpoint the test weight vanishes because `C(2)=0`. Stieltjes integration by parts is therefore exact and gives

\[
\boxed{
\Delta_a
=1+
\int_1^{e^{2a}}
E(x)x^{-3/2}
\left[
\frac12 C\!\left(\frac{\log x}{a}\right)
-\frac1a C'\!\left(\frac{\log x}{a}\right)
\right]dx.
}
\tag{7}
\]

The boundary constant `+1` is not an asymptotic term. It is the lower-endpoint contribution `-f(1)E(1)` for

\[
f(x)=x^{-1/2}C((\log x)/a).
\]

Using a half-jump convention for `psi` gives the same original discrete discrepancy because the upper endpoint has zero weight; equation (7) may also be checked directly from the discrete-minus-continuum definition in WI-241.

Equation (7) is the exact partial-summation bridge left open there. The decisive point is the critical factor `E(x)x^{-3/2}`.

## 2. The absolute-envelope route has the wrong scale

Suppose one discards the sign and oscillation of `E` and inserts a pointwise envelope

\[
|E(x)|\le B(x).
\tag{8}
\]

From (3) and (7),

\[
\boxed{
|\Delta_a-1|
\le
\left(\frac12+\frac{\|C'\|_\infty}{a}\right)
\int_1^{e^{2a}} B(x)x^{-3/2}\,dx.
}
\tag{9}
\]

Thus an absolute-envelope proof can even hope for an `a`-uniform order-one estimate only if the weighted majorant on the right stays uniformly bounded. For the standard model

\[
B(x)=Kx^\theta(\log x)^A
\qquad(x\ge e),
\tag{10}
\]

putting `t=log x` gives

\[
\int_e^{e^{2a}}B(x)x^{-3/2}\,dx
=K\int_1^{2a}e^{(\theta-1/2)t}t^A\,dt.
\tag{11}
\]

Hence:

- if `theta>1/2`, the majorant grows exponentially in `a`;
- if `theta=1/2`, it grows like `a^{A+1}` for `A>-1` and like `log a` for `A=-1`;
- an `a`-uniform bound from this regular power-log family requires `theta<1/2`, or `theta=1/2` with `A<-1`.

This already excludes the usual PNT estimates as a mechanism for WI-241. A classical unconditional bound

\[
E(x)=O\!\left(xe^{-c\sqrt{\log x}}\right)
\tag{12}
\]

leads after `t=log x` to an integrand `exp(t/2-c sqrt(t))`, so (9) grows exponentially. The same conclusion holds for any zero-free-region bound of the form

\[
B(x)=x\exp(-o(\log x)).
\tag{13}
\]

Even assuming RH, the standard pointwise estimate

\[
E(x)=O(\sqrt{x}\log^2x)
\tag{14}
\]

only gives

\[
|\Delta_a-1|=O_\phi(a^3)
\tag{15}
\]

through (9), because

\[
\int^ {e^{2a}}x^{-1}(\log x)^2dx\asymp a^3.
\]

So a black-box pointwise PNT error estimate plus triangle inequality does not merely miss the desired sign; at the currently relevant scales it fails even to keep the discrepancy uniformly bounded.

The threshold in (11) is also not a plausible target for a stronger generic majorant. Littlewood's classical oscillation, in the form recorded in Suzuki's 2025 paper,

\[
E(x)=\Omega_\pm(\sqrt{x}\log\log\log x),
\tag{16}
\]

rules out any eventual uniform estimate such as

\[
E(x)=O\!\left(\frac{\sqrt{x}}{(\log x)^{1+\varepsilon}}\right).
\tag{17}
\]

The barrier is deliberately about **absolute-envelope arguments**. Equation (7) does not rule out estimates that preserve cancellation, sign, Mellin structure, zero information, or a specially chosen autocorrelation. It says that replacing `E` by `|E|` and then invoking a standard PNT magnitude bound destroys exactly the order-one information needed by the source-side program.

## 3. The required constant is exactly `2-zeta'/zeta(1/2)`

WI-241 defines

\[
M(z)=
\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)
-\log\pi
+\frac1{z^2+1/4}
\tag{18}
\]

and obtains

\[
M(0)=4+\psi(1/4)-\log\pi.
\tag{19}
\]

The functional equation gives `xi'(1/2)=0`. Taking the logarithmic derivative of the completed zeta function at `1/2`, the `1/s+1/(s-1)` terms cancel, so

\[
0=
\frac{\zeta'}{\zeta}\!\left(\frac12\right)
+\frac12\psi\!\left(\frac14\right)
-\frac12\log\pi.
\tag{20}
\]

Therefore

\[
\boxed{
\frac{M(0)}2
=2-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=-0.6860917096\ldots .
}
\tag{21}
\]

This identifies the fixed charge isolated in WI-241 with the same logarithmic-derivative constant that appears in weighted Chebyshev bias formulas. The numerical value is only explanatory; the identity (21) is exact.

## 4. Under RH the slow-dilate discrepancy converges to that constant

Suzuki's exact zero-side representation of Weil's quadratic form is

\[
Q_W(v_1,v_2)
=
\sum_{\gamma\in\Gamma}
 m_\gamma\widehat v_1(\gamma)
 \overline{\widehat v_2(\bar\gamma)},
\tag{22}
\]

where `Gamma` is the zero set of `z -> xi(1/2-iz)` and `m_gamma` is the multiplicity. This is equation (3.1) of **Weil's quadratic form via the screw function**.

Assume RH. Then every `gamma` in (22) is real, and for the real test `U_a phi`,

\[
Q_W(U_a\phi)
=
 a\sum_{\gamma\in\Gamma}m_\gamma
 |\widehat\phi(a\gamma)|^2.
\tag{23}
\]

The Fourier transform of `phi` is Schwartz. Also `gamma=0` is absent because `zeta(1/2)\ne0`, and the zero counting law implies

\[
\sum_{\gamma\in\Gamma}m_\gamma|\gamma|^{-2N}<\infty
\]

for every sufficiently large `N`. Hence (23) is bounded by

\[
O_{\phi,N}(a^{1-2N})
\sum_\gamma m_\gamma|\gamma|^{-2N},
\]

and therefore

\[
\boxed{Q_W(U_a\phi)\longrightarrow0.}
\tag{24}
\]

On the other hand, WI-241 proves unconditionally for each fixed `phi`

\[
Q_{\rm mean}(U_a\phi)\longrightarrow M(0)
\tag{25}
\]

and the exact identity

\[
Q_W(U_a\phi)
=Q_{\rm mean}(U_a\phi)-2\Delta_a.
\tag{26}
\]

Combining (24)--(26) yields the RH-conditional exact limit

\[
\boxed{
\Delta_a
\longrightarrow
\frac{M(0)}2
=2-\frac{\zeta'}{\zeta}\!\left(\frac12\right).
}
\tag{27}
\]

Thus the necessary inequality from WI-241 is asymptotically saturated on each fixed slow odd mode under RH. The result does **not** assert the converse: no claim is made here that convergence (27) for one test, or even for a specified family of tests, implies RH.

## 5. Suzuki's weighted Chebyshev criterion is a prior-art warning about one-sided source bias

Masatoshi Suzuki, **On variants of Chebyshev's conjecture**, *The Ramanujan Journal* 68 (2025), article 95, DOI `10.1007/s11139-025-01238-9`, studies the weighted Chebyshev function

\[
\psi_{1/2}(x)=\sum_{n\le x}'\frac{\Lambda(n)}{\sqrt n}.
\tag{28}
\]

Its Theorem 1 proves that RH is equivalent to eventual nonpositivity of

\[
\boxed{
\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}\log\frac xn
-4\sqrt x
\le0.
}
\tag{29}
\]

Equivalently, this is the eventual negative bias of an integrated `psi_{1/2}(x)-2 sqrt(x)` discrepancy. The same theorem gives the corresponding Riesz-type limit involving `-zeta'/zeta(1/2)`. Suzuki also records Littlewood's two-sided oscillation used in (16).

A published correction, DOI `10.1007/s11139-025-01289-y` (19 Dec 2025), corrects notation in Sect. 1.2 and formulas in later Theorems 7--8; it does not alter Theorem 1 used here. The current online article incorporates those corrections.

Theorem 1 is not the same statement as (27). Its weight is the one-sided logarithmic kernel `log(x/n)`, whereas WI-241/WI-242 use autocorrelations of compactly supported odd test functions. Therefore no equivalence with RH is imported for the present discrepancy. The prior-art lesson is narrower but important: **one-sided sign information for `n^{-1/2}`-weighted prime sums can already encode RH exactly**. A plan to prove the needed source deficit by discovering a broad, eventually signed weighted-Chebyshev inequality should therefore be treated as potentially target-equivalent rather than as a routine PNT refinement.

## 6. Prior-art and novelty audit

The provenance separates as follows.

1. **Literature-backed exact input.** Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), supplies the exact localized Weil form and the zero-side representation (22). WI-241 supplies the already-persisted pole/main-density cancellation and mean multiplier.
2. **Classical arithmetic input.** The ordinary PNT remainder `E(x)=psi(x)-x`, classical zero-free-region error bounds, the RH square-root-logarithmic error estimate, and Littlewood's `Omega_+-` oscillation are established background. Suzuki's 2025 paper records the particular versions used above.
3. **Direct prior art that redirects the route.** Suzuki's 2025 Theorem 1 proves the RH equivalence of the neighboring weighted-Chebyshev sign condition (29). Its correction was checked and does not change that theorem.
4. **Mathia deduction.** Equation (7), the scale tariff (9)--(15), the exact constant identification (21), and the RH-conditional slow-dilate limit (27) are derived here from WI-241 plus the cited exact formulas. No priority claim is made for elementary partial summation or for an equivalent formulation that may exist elsewhere.

Targeted searches around Suzuki's localized Weil form, `psi(x)-x`, weighted Chebyshev bias, and the `n^{-1/2}` source scale found the above literature but did not locate the specific slow-autocorrelation formula (7) or the absolute-envelope tariff (11). Search absence is not used as evidence of priority.

## 7. Stress tests and boundaries

- **The `+1` in (7) is real.** It comes from `E(1)=-1` and `C(0)=1`; dropping the lower endpoint changes the constant and corrupts the comparison with (21).
- **The obstruction is method-specific.** A divergent right-hand side in (9) does not imply that the true signed discrepancy diverges. Under RH, (27) shows the opposite: the true discrepancy converges because of cancellation that (9) discards.
- **RH is used only in Section 4.** Equations (6)--(21) and the absolute-envelope barrier are unconditional. Equation (27) is explicitly conditional and is not fed back as unconditional source evidence.
- **Oddness remains load-bearing for the WI-241 decomposition.** The partial summation identity itself is an arithmetic identity for the chosen autocorrelation, but its role as the exact residual source in (26) uses the odd-sector pole cancellation proved in WI-241.
- **No off-line population is inferred.** The result concerns the source-side defect mechanism. It does not identify the uncertified simple-zero complement with off-critical zeros and does not alter any density theorem.
- **Suzuki 2025 is adjacent, not identical.** Its RH-equivalent sign kernel must not be substituted for the compact-support autocorrelation kernel without a proved transform/dictionary.

## 8. Research consequence

The broad route

\[
\text{known pointwise PNT error}
\;\longrightarrow\;
|E(x)|\text{ envelope}
\;\longrightarrow\;
\text{slow-source coercivity}
\]

is closed. It destroys the signed critical-scale information and, with all standard available envelopes, does not even produce an `a`-uniform bound before sign is considered.

The surviving source-side routes must preserve cancellation. Examples that remain logically open are: an exact first-crossing identity that constrains (7) without absolute values; a finite-radius source functional coupled to the zero-side mode; Mellin/explicit-formula control retaining phases; or a test-family argument showing that an off-critical zero forces a failure of the slow-source limit before one asks for global source positivity.

Equation (27) gives a clean calibration target for such work. Under RH, every fixed slow odd mode must asymptotically see precisely the charge `2-zeta'/zeta(1/2)`. Any proposed unconditional bootstrapping mechanism should therefore explain this signed order-one limit rather than attempt to manufacture it from absolute smallness of the PNT remainder.
