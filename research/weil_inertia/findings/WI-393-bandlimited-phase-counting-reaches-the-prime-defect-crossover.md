# WI-393 — bandlimited phase counting reaches the prime/defect crossover

**Status:** `EXACT-DERIVED + CLASSICAL-EXPLICIT-FORMULA + CLASSICAL-BEURLING-SELBERG + SOURCE-EXACT + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-391 obtains a positive source-exact RH Weil floor from a dilute carrier packet by controlling the endpoint phase with the pointwise RH bound for `S(t)`. Its stated sufficient scale is

\[
A\to\infty,
\qquad
A=o(\log\log R).
\]

That phase gate is not intrinsic. A fixed Beurling--Selberg minorant of the carrier interval, inserted directly into the Guinand--Weil explicit formula, extends the same positive-floor mechanism to the much larger uniform regime

\[
\boxed{
A\to\infty,
\qquad
\frac{e^{A/2}}{\log R}\longrightarrow0.
}
\tag{1}
\]

Equivalently, one may approach

\[
A=2\log\log R-\omega(1).
\tag{2}
\]

More precisely, fix the packet half-width `delta_0>0` supplied by WI-388, on which the dilute one-lobe carrier satisfies

\[
|\widehat g_R(\xi)|^2\ge \frac{c_0c}{\log R}
\qquad (|\xi-R|\le\delta_0).
\tag{3}
\]

Then, assuming RH, there is a fixed constant `c_delta>0` such that every sufficiently large pair `(R,A)` satisfying (1) obeys

\[
\boxed{
\sum_{|\gamma-R|\le\delta_0}
 m_\gamma\sin^2\!\left(\frac{A\gamma}{2}\right)
\ge c_\delta\log R.
}
\tag{4}
\]

Consequently the unperforated WI-391 trial has an order-one RH spectral reserve, and the same exact Desogus source-slot perforation remains negligible. Thus the source-exact WI-391 positive Weil floor survives throughout (1); the earlier doubly exponential choice `R=exp(exp(A^2))` is sufficient but far from necessary. For example one may take

\[
\boxed{
\log R=Ae^{A/2},
}
\tag{5}
\]

for which `e^{A/2}/log R=1/A` and

\[
A=2\log\log R-2\log A.
\]

The same scale also identifies a barrier for the sparse-defect bootstrap. WI-392 proves that one off-critical zero in the moving packet contributes at most

\[
q(A,R)
=
\frac{e^{A/2}}{\log R}
+\frac{e^{-A/2}}{A^2}
+e^{A/2}R^{-2M}
\tag{6}
\]

up to a fixed constant, uniformly over the critical strip. Under (1), `q(A,R)->0`. Therefore the entire regime in which a fixed bandlimited minorant plus absolute prime-side control guarantees the RH carrier reserve is also a regime in which every fixed number of moving-packet off-line zeros is asymptotically invisible at order-one scale to that same channel.

At the crossover

\[
\boxed{e^{A/2}\asymp\log R}
\qquad\Longleftrightarrow\qquad
A=2\log\log R+O(1),
\tag{7}
\]

the shifted prime-power term in the explicit formula becomes order `log R`, the same size as the local-zero-density main term, exactly when the worst-case critical-strip envelope in (6) first becomes order one. Crossing (7) is therefore not a free continuation of WI-391: it requires genuinely new information about cancellation of the relevant prime Dirichlet polynomial at the defect-anchored ordinate, or a different defect-sensitive channel.

This is not an impossibility theorem beyond (7). The prime polynomial can in principle cancel, and if `R` is freely selectable one may try to choose favorable carrier centers. The barrier is the **uniform-in-`R`, defect-anchored route using only absolute prime-side estimates**. No unconditional positive Weil gap, RH proof, or improved simple-critical-zero proportion is claimed.

## 1. A Selberg minorant converts phase counting into one explicit-formula test

Use the angular-frequency convention

\[
\widehat h(u)=\int_{\mathbb R}h(t)e^{-iut}\,dt.
\tag{8}
\]

Classical Beurling--Selberg theory gives, for the fixed interval

\[
I=[-\delta_0,\delta_0],
\]

a real entire function `m` of some fixed exponential type `B>0` such that

\[
m(u)\le \mathbf 1_I(u),
\qquad
\operatorname{supp}\widehat m\subset[-B,B],
\qquad
M:=\int_{\mathbb R}m(u)\,du>0.
\tag{9}
\]

Choose `B` once and for all large enough that the minorant has positive integral. The standard Selberg construction also has quadratic decay on horizontal strips, so it is admissible in the Guinand--Weil formula.

For `A>B` define

\[
H_{R,A}(t)
=m(t-R)\sin^2\!\left(\frac{At}{2}\right).
\tag{10}
\]

Under RH every nontrivial zero is `1/2+i\gamma`, and because `sin^2>=0` on the real axis while `m<=1_I`, termwise

\[
\sum_{|\gamma-R|\le\delta_0}
 m_\gamma\sin^2\!\left(\frac{A\gamma}{2}\right)
\ge
\sum_\gamma m_\gamma H_{R,A}(\gamma).
\tag{11}
\]

The advantage over the `S(t)` integration-by-parts proof of WI-391 is that the Fourier support of (10) tells us exactly what new arithmetic is purchased by the phase oscillation.

Since

\[
\sin^2(At/2)=\frac{1-\cos At}{2},
\]

the Fourier transform of (10) is supported in the union

\[
[-B,B]
\cup[A-B,A+B]
\cup[-A-B,-A+B].
\tag{12}
\]

Moreover, because `A>B`,

\[
\widehat H_{R,A}(0)
=\int H_{R,A}(t)\,dt
=\frac M2;
\tag{13}
\]

the oscillatory pieces vanish exactly at zero frequency because `\widehat m(\pm A)=0`.

## 2. The explicit formula leaves an `O(e^{A/2})` prime term

Apply the Guinand--Weil explicit formula to (10). The archimedean integral has local density `log R/(2\pi)` at height `R`. Using (13), the digamma asymptotic, and the quadratic decay of the translated minorant gives

\[
\mathcal A(H_{R,A})
=
\frac{M}{4\pi}\log R
+O_B\!\left(1+\frac{\log R}{R}\right).
\tag{14}
\]

The estimate is uniform in `A` in the range considered here because `|sin^2(At/2)|<=1` on the real axis; the large complex values enter only in the fixed pole terms, discussed below.

The central Fourier band in (12) samples only the fixed set of prime powers with `log n<=B`, so its prime contribution is `O_B(1)`. The two shifted bands sample prime powers with

\[
|\log n-A|\le B.
\tag{15}
\]

Since `\widehat m` is bounded, their absolute contribution is at most a fixed multiple of

\[
\sum_{n\le e^{A+B}}\frac{\Lambda(n)}{\sqrt n}.
\]

Chebyshev's bound `\psi(x)\ll x` and partial summation give

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\ll\sqrt X,
\]
so

\[
\boxed{
\mathcal P(H_{R,A})=O_B(e^{A/2}).
}
\tag{16}
\]

The pole/trivial-zero evaluation terms are

\[
O_B(e^{A/2}R^{-2}),
\tag{17}
\]

because the Selberg minorant is `O_B(R^{-2})` at horizontal distance `R` and `sin^2(Az/2)` grows only like `e^{A/2}` on `|Im z|=1/2`.

Combining (14)--(17) gives the phase-count asymptotic

\[
\boxed{
\sum_\gamma m_\gamma H_{R,A}(\gamma)
=
\frac{M}{4\pi}\log R
+O_B(1+e^{A/2})
+o(\log R).
}
\tag{18}
\]

Hence (1) implies (4). Notice that no pointwise estimate for `S(t)` is used. The price of modulation is exposed directly as the square-root prime scale `e^{A/2}` coming from prime powers near `n\asymp e^A`.

## 3. The stronger phase count transfers to the exact source-zero trials

For the unperforated WI-391 odd pair

\[
f^0_{A,R}(y)
=g_R(y-A/2)-g_R(y+A/2),
\]
RH gives

\[
\mathcal W[f^0_{A,R}]
=4\sum_{\gamma>0}m_\gamma
|\widehat g_R(\gamma)|^2
\sin^2\!\left(\frac{A\gamma}{2}\right).
\tag{19}
\]

Using (3)--(4),

\[
\mathcal W[f^0_{A,R}]
\ge 4c_0c\,c_\delta+o(1).
\tag{20}
\]

The exact source-slot perforation in WI-391 does not use the old condition `A=o(log log R)` except in its phase-count step. With `x=e^A`, its removed-slot measure and cutoff energy satisfy

\[
\mu_A\ll\frac{e^{-A/2}}{A},
\qquad
\kappa_A\ll e^{-A/2}.
\tag{21}
\]

For the carrier component, the `1/log R` dilution cancels the `O(log R)` carrier energy, leaving perforation cost

\[
O(c\mu_A)+O\!\left(\frac{c\kappa_A}{\log R}\right)=o(1),
\tag{22}
\]

while the fixed base component costs `O(\mu_A+\kappa_A)=o(1)`. The RH spectral sampling comparison of WI-391 therefore still gives vanishing Weil-seminorm perturbation. After normalization, the exact source-zero trials retain a fixed positive lower bound in (20).

Thus (1), rather than `A=o(log log R)`, is a sufficient scale for the WI-391 source-exact positive RH floor.

## 4. The same ratio controls sparse-defect visibility

WI-392 derives, without assuming RH for the individual zero calculation, the moving-packet bound

\[
|T_\rho(f_{A,R})|
\ll
\frac{e^{A/2}}{\log R}
+\frac{e^{-A/2}}{A^2}
+e^{A/2}R^{-2M}
\tag{23}
\]

uniformly for every zero in the critical strip. Under (1) all three terms tend to zero. Therefore

\[
M_{\rm off}(A,R)q(A,R)\to0
\]
still implies that the whole off-line packet is `o(1)` in the moving-frequency channel, and in particular every fixed number of off-line zeros is invisible at order one.

For the concrete near-critical diagonal (5),

\[
q(A,R)
\ll
\frac1A+rac{e^{-A/2}}{A^2}+e^{A/2}R^{-2M}
\sim\frac1A.
\tag{24}
\]

So this substantially slower carrier growth improves individual sensitivity relative to WI-391's original `R=exp(exp(A^2))`, but it does not make an isolated defect order one.

There is also a sharper fixed-depth comparison. If

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<|\delta|<\frac12
\]
has fixed horizontal depth, the leading individual envelope is

\[
\frac{e^{A|\delta|}}{\log R}.
\tag{25}
\]

Its order-one scale is

\[
A\sim\frac1{|\delta|}\log\log R,
\tag{26}
\]
which is strictly beyond `2 log log R` for every fixed `|delta|<1/2`. Thus the absolute prime term becomes load-bearing before this channel can robustly amplify a fixed-depth isolated defect. The uniform critical-strip envelope reaches order one exactly at the limiting edge `|delta|=1/2`, explaining the common crossover (7).

## 5. What the crossover does and does not close

Equation (18) is a uniform phase-reserve theorem obtained with no cancellation in the shifted prime sum. It therefore gives a precise barrier, not a global no-go. If the carrier center `R` is free, averaging or selecting `R` may make the short prime polynomial in (15) unusually small. One could also design a more arithmetic-dependent test whose Fourier values cancel some prime-power samples. Neither possibility is excluded here.

For a defect-to-zero bootstrap, however, `R` is naturally tied to the ordinate of the exceptional zero one wants to detect. At that defect-anchored ordinate, crossing (7) requires new control of a Dirichlet polynomial supported at

\[
n\asymp e^A\asymp(\log R)^2
\]
at the critical crossover. Absolute Chebyshev control is no longer enough. The next useful input would therefore have to be one of:

- cancellation of this short prime polynomial at the relevant zero ordinates;
- a source-exact trial whose per-defect response is stronger than the `e^{A|delta|}/log R` law of WI-392;
- a multi-packet or global coupling that aggregates sparse exceptional zeros before dilution makes them invisible.

Simply increasing `A` in the existing dilute-carrier construction is not itself a bootstrap.

## 6. Prior art and novelty boundary

The ingredients are classical. Selberg's interval minorants and their compact Fourier support are part of the Beurling--Selberg extremal-function theory; a standard reference is Jeffrey D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. Amer. Math. Soc. 12 (1985), 183--216, DOI `10.1090/S0273-0979-1985-15349-2`. Emanuel Carneiro's survey, *A survey on Beurling-Selberg majorants and some consequences of the Riemann hypothesis*, Matemática Contemporânea 40 (2011), 149--172, DOI `10.21711/231766362011/rmc408`, records the standard use of bandlimited extremals together with the Guinand--Weil explicit formula for zeta. Landau--Gonek type formulas provide the classical complementary viewpoint that Fourier modulation of zero sums is sensitive to prime-power arithmetic; see Farzad Aryan, *On an extension of the Landau--Gonek formula*, J. Number Theory 233 (2022), 389--404, arXiv:`1902.05473`.

For comparison, the pointwise RH estimate `|S(t)|<=(1/4+o(1)) log t/log log t` is due to Emanuel Carneiro, Vorrapan Chandee and Micah B. Milinovich, *Bounding S(t) and S1(t) on the Riemann hypothesis*, Math. Ann. 356 (2013), 939--968, DOI `10.1007/s00208-012-0876-z`. Feeding that stronger constant into WI-391's original integration-by-parts proof improves its numerical phase range, but it still pays an `A sup|S|` error. The direct bandlimited explicit-formula argument above exposes the larger natural square-root-prime scale instead.

A line-local audit checked WI-388, WI-391, WI-392, the current research contract, recent `weil_inertia` carrier/phase findings, and the active clue set. External searches covered Beurling--Selberg interval extremals, Guinand--Weil applications, RH bounds for `S(t)`, and Landau--Gonek weighted zero sums. No source located in that audit states this exact source-exact adaptive-carrier synthesis or the coincidence with WI-392's sparse-defect envelope. That is not a priority claim; the novelty asserted here is only the derived relation inside the Mathia research program.

## Research consequence

WI-391's positive RH floor is therefore stronger than previously recorded: logarithmic spectral mass may escape almost up to the critical phase scale `2 log log R` while preserving exact prime-power source slots. But WI-392 and the present explicit-formula calculation meet at the same ratio `e^{A/2}/log R`. The natural next gate is not another larger carrier frequency by itself; it is arithmetic cancellation at the defect-anchored prime side, or a construction that changes the per-defect dilution law.
