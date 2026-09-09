# ANF-132 — iterated positive saddle annihilators face a Gaussian entropy barrier

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GROWING-ANNIHILATOR-DEPTH + GAUSSIAN-HIGH-MOMENT-LAW + POSITIVE-TRANSLATION-BUDGET + RENORMALIZED-CASCADE-GATE`. `ANF-129` produces a fixed-`q` critical exponential digit cloud whose original `ANF-115` saddle is evacuated while the complete Montgomery--Taylor source mass remains comparable to one packet. `ANF-130` then shows that the finitely many regenerated Gaussian source chambers can be annihilated by a fixed positive translation polynomial, and every fixed power of that polynomial buys another factor `A^{-1}` of source suppression. `ANF-131` closes the diagonal critical regime with an analogous bounded positive filter.

A possible escape is to let the annihilator order itself grow with `A`, hoping to suppress a critical chamber at a genuinely exponential rate while keeping the new translation budget subexponential. That does **not** work for iterates of a uniformly conditioned finite positive annihilator. The Gaussian chamber moves outward under the high power: the mass that survives `m` repeated zeros is concentrated at distance `Theta(sqrt(m/A))`, not at the original `A^{-1/2}` core. Consequently the gain from `m=o(A)` repeated zeros is only

\[
\boxed{
\log\frac{E_0(Y_A^{(m)})}{E_A}
=-m\log\frac{A}{m}+O_q(m+1),
\qquad 1\le m=o(A),
}
\tag{1}
\]

for the canonical simple-zero annihilator constructed below. In particular

\[
\boxed{
\frac1A\log\frac{E_0(Y_A^{(m)})}{E_A}\longrightarrow0
\qquad(m=o(A)).
}
\tag{2}
\]

Thus a sublinear number of repeated positive annihilation layers can make the block source-negligible, even faster than any fixed polynomial if `m->infinity`, but it can never provide a fixed-rate suppression `exp(-sigma A)`. Any such exponential suppression inside this iterated-filter architecture forces `m=Omega(A)`, and because the positive expansion has `2^{Jm}` translated copies, it forces a **positive exponential outer copy budget**.

This identifies a quantitative barrier between the finite excision of `ANF-130` and a true recursive exponential cascade. Repeating the same local positive notch more and more deeply cannot cross that barrier at subexponential cost; a live cascade must instead use an `A`-dependent/non-product Fourier molecule, unbounded translation geometry, coalescing chambers, or another mechanism not equivalent to repeated fixed zeros.

## 1. Exact source model and an `A`-dependent physical annihilator

Fix `gamma>0` and a sufficiently large fixed digit arity `q` in `ANF-129`. Let `X_A` be its critically tuned physical cloud, and keep the packet scale

\[
E_A=E_0(P_A).
\]

`ANF-129` and `ANF-130` give

\[
0<c_q\le \frac{E_0(X_A)}{E_A}\le C_q<\infty
\tag{3}
\]

and a finite positive-frequency critical set

\[
\mathcal K_q^+=\{\alpha_1,\ldots,\alpha_J\}\subset(0,1)
\tag{4}
\]

of nondegenerate maxima of the limiting source exponent. For fixed sufficiently large `q`, every member of `K_q^+` lies in the `Theta(q^{-2})` leakage zone around the cancelled packet saddle `a=a_gamma`; in particular the ratios of two distinct critical points are eventually bounded away from every odd integer different from `1`.

The exact physical source density differs from the limiting exponent by bounded smooth terms on fixed critical neighborhoods. Hence, after shrinking those neighborhoods once and for all, each limiting chamber contains a unique exact maximizer

\[
\xi_{j,A}=\alpha_j+O_q(A^{-1}),
\qquad 1\le j\le J,
\tag{5}
\]

and there are constants

\[
0<c_1<C_1<\infty,
\qquad
0<c_2<C_2<\infty
\tag{6}
\]

depending only on the fixed `q,gamma` such that, with `x=alpha-xi_{j,A}` and `|x|<=delta_q`,

\[
-C_1Ax^2-C_2A|x|^3-C_2
\le
\log\frac{\mathscr D_A(\xi_{j,A}+x)}{\mathscr D_A(\xi_{j,A})}
\le
-c_1Ax^2+C_2A|x|^3+C_2,
\tag{7}
\]

where

\[
\mathscr D_A(\alpha)=J_0(\alpha)|S_{X_A}(\alpha)|^2.
\]

The source outside the union of these fixed neighborhoods and their reflections has a fixed exponential gap,

\[
\int_{\mathrm{far}}\mathscr D_A(\alpha)\,d\alpha
\le e^{-c_3A}E_A.
\tag{8}
\]

These are the fixed-`q` Gaussian-skeleton estimates already underlying `ANF-130`; (7) merely keeps the cubic remainder because the relevant location will now move with the annihilator order.

Use the **exact** chamber maximizers to define

\[
Q_A(\alpha)
:=
\prod_{j=1}^{J}
\left(1+e^{-2\pi i\alpha/(2\xi_{j,A})}\right).
\tag{9}
\]

Each factor is the modulation of the union of one untranslated and one positively translated copy, so `Q_A` has a positive physical expansion with exactly `2^J` terms counted with multiplicity. It vanishes at both signs of every `xi_{j,A}`. Because the critical points remain in a fixed compact interval and, for sufficiently large fixed `q`, no distinct ratio `xi_{j,A}/xi_{k,A}` approaches an odd integer, every one of these zeros is simple and uniformly conditioned. Therefore there are constants `b_q,B_q,delta_q>0` such that

\[
b_q|x|
\le
|Q_A(\xi_{j,A}+x)|
\le
B_q|x|
\qquad(|x|\le\delta_q)
\tag{10}
\]

for every `j` and all large `A`.

For an integer `m=m_A>=1`, let `Y_A^{(m)}` be the positive translation cloud of the complete block `X_A` whose multiplier is

\[
Q_A(\alpha)^m.
\tag{11}
\]

Its unsigned outer copy count is exactly

\[
\boxed{
V_A=2^{Jm}.
}
\tag{12}
\]

Thus `m=o(A)` is precisely a subexponential outer-copy regime for this architecture.

## 2. Repeated zeros push the surviving chamber to `sqrt(m/A)`

Fix one exact chamber and abbreviate `xi=xi_{j,A}`. Equations (7) and (10) show that its contribution to the filtered source is trapped, up to factors `exp(O_q(m+1))`, between Gaussian high moments of the form

\[
\int_{|x|\le\delta_q}
|x|^{2m}e^{-C_qAx^2-C_qA|x|^3}\,dx
\tag{13}
\]

and the corresponding expression with different positive constants.

Assume

\[
1\le m=o(A).
\tag{14}
\]

The natural rescaling is no longer `x=u/sqrt(A)` but

\[
x=\sqrt{\frac mA}\,u.
\tag{15}
\]

On every fixed `u`-annulus around the maximizer of the rescaled exponent, (14) gives

\[
A|x|^3
=\frac{m^{3/2}}{\sqrt A}|u|^3
=o(m),
\tag{16}
\]

while the Taylor error in `log|Q_A|` contributes only

\[
O_q(m|x|)=o(m).
\tag{17}
\]

The leading exponent is therefore

\[
2m\log|x|-cAx^2
=
-m\log\frac A m
+m\left(2\log|u|-cu^2\right).
\tag{18}
\]

The second bracket has a finite nondegenerate maximum at `|u|=Theta_q(1)`. Elementary Laplace upper and lower bounds on a fixed neighborhood of that maximizer yield

\[
\boxed{
\log I_{j,A}^{(m)}
=
-m\log\frac A m+O_q(m+\log(m+2))
+\log I_{j,A}^{(0)},
}
\tag{19}
\]

where `I_{j,A}^{(m)}` is the filtered source contribution of the `j`th chamber and `I_{j,A}^{(0)}` the unfiltered one. Equivalently, one may compare with the exact Gaussian moment

\[
\frac{\int_{\mathbb R}|x|^{2m}e^{-cAx^2}\,dx}
{\int_{\mathbb R}e^{-cAx^2}\,dx}
=
(cA)^{-m}\frac{\Gamma(m+1/2)}{\Gamma(1/2)},
\tag{20}
\]

and use Stirling,

\[
\log\Gamma(m+1/2)
=m\log m-m+O(\log(m+2)).
\tag{21}
\]

The interpretation is important. A zero of order `m` does **not** force the surviving source to remain in the original core `|x|=Theta(A^{-1/2})`, where the naive factor would be `A^{-m}`. The weighted source optimizes at

\[
\boxed{
|x|=Theta_q\!\left(\sqrt{m/A}\right).
}
\tag{22}
\]

That outward motion supplies the entropy term `m log m` in (21), turning `A^{-m}` into the much larger scale `(m/A)^m` up to exponential-in-`m` constants.

## 3. The complete source obeys the same high-moment law

There are only finitely many critical chambers. Their unfiltered Laplace masses are all bounded above by `O_q(E_A)` and at least one is bounded below by `Omega_q(E_A)` because of (3) and the far-gap estimate (8). The exact annihilator has a uniformly simple zero at every chamber, so summing (19) over the finite critical set gives

\[
\sum_j I_{j,A}^{(m)}
=
E_A\exp\left[
-m\log\frac A m+O_q(m+\log(m+2))
\right].
\tag{23}
\]

On the far region,

\[
|Q_A(\alpha)|\le2^J,
\]

and hence by (8)

\[
E_{\mathrm{far}}(Y_A^{(m)})
\le
\exp\left[-c_3A+2Jm\log2\right]E_A.
\tag{24}
\]

When `m=o(A)`, (24) is `exp(-Omega_q(A))E_A`, whereas the chamber term (23) is only `exp(-o(A))E_A`. The latter therefore dominates. We obtain the advertised uniform growing-order law

\[
\boxed{
\log\frac{E_0(Y_A^{(m)})}{E_A}
=
-m\log\frac A m+O_q(m+\log(m+2)),
\qquad 1\le m=o(A).
}
\tag{25}
\]

For fixed `m`, this reduces to the `O_q(A^{-m})` mechanism of `ANF-130`, now with a matching lower scale. If `m->infinity` while `m=o(A)`, the source tends to zero faster than every fixed polynomial as soon as `m` grows sufficiently, so the aggregate remains excisable. But because

\[
\frac mA\log\frac A m
=x_A\log\frac1{x_A}\longrightarrow0
\qquad
\left(x_A=\frac mA\to0\right),
\tag{26}
\]

its suppression is always subexponential in `A`. This proves (2).

## 4. Fixed exponential suppression forces a positive exponential copy budget

Let `sigma>0` be fixed. Suppose an iterated annihilator of the form (11) satisfies along an infinite sequence

\[
E_0(Y_A^{(m)})
\le e^{-\sigma A}E_A.
\tag{27}
\]

Equation (25) rules out `m=o(A)`. More quantitatively, the lower half of the Laplace comparison gives constants `C_q,C_q'>0` such that whenever `m<=delta A`,

\[
-\log\frac{E_0(Y_A^{(m)})}{E_A}
\le
C_qm\log\frac{eA}{m}+C_q'm.
\tag{28}
\]

Since `x log(e/x)->0` as `x->0`, for every fixed `sigma` there is a constant `theta_{q,sigma}>0` such that (27) implies

\[
\boxed{
m\ge\theta_{q,\sigma}A
}
\tag{29}
\]

for all sufficiently large members of that sequence. By the exact positive expansion (12),

\[
\boxed{
\liminf_{A\to\infty}
\frac1A\log V_A
\ge
J\theta_{q,\sigma}\log2
>0.
}
\tag{30}
\]

So an outer layer that uses repeated `ANF-130`-type positive saddle zeros to beat a downstream **fixed positive exponential rate** must itself enter the positive exponential copy-budget regime. There is no intermediate choice such as

\[
m=\frac{A}{\log A},
\qquad
m=\frac{A}{\log\log A},
\qquad
m=A^{1-\varepsilon},
\]

that keeps `log V_A=o(A)` while buying `exp(-sigma A)` suppression. All such choices remain on the subexponential side because of (26).

This is the promised Gaussian entropy barrier: increasing zero multiplicity suppresses the core, but the Gaussian source reoptimizes farther from the zero. The entropy of that moving annulus exactly prevents sublinear annihilator depth from competing with a fixed exponential amplification rate.

## 5. Adversarial controls and exact scope

The result deliberately does **not** claim that every positive translation polynomial with subexponential coefficient mass obeys (25). The proof uses a uniformly conditioned finite annihilator, or equivalently a fixed finite collection of bounded translation factors, repeated `m` times. An `A`-dependent positive Fourier molecule may let its frequencies, number of primitive factors, zero locations, or conditioning change with `A`; that is precisely the architecture not settled here.

Nor does the theorem rule out an exponential cascade. It shows that a naive recursive strategy cannot use increasingly high powers of the same local annihilator while paying only a subexponential outer budget. Once `m=Theta(A)`, the tilted location in (22) is macroscopic rather than infinitesimal, the local Gaussian Taylor model no longer controls the full integral, and new source maxima can appear. That is the same saddle-migration phenomenon exploited constructively by `ANF-127`--`ANF-129`, so no conclusion beyond the threshold (29) is asserted.

The fixed-`q` hypothesis is also essential to the clean form of (25). In the diagonal regime `q=q(A)->infinity`, critical chambers coalesce and the annihilator itself becomes `A`-dependent; `ANF-131` handles the first critical diagonal layer but not arbitrary growing-order recursions. Similarly, a profile-transverse companion with a different underlying packet landscape is outside this same-orbit calculation.

Finally, source suppression is not the same as fatal notch exposure. For `m->infinity`, (25) still makes the combined block source-negligible and hence compatible with the excision logic of `ANF-130`; the new statement is about **how much exponential rate that excision buys for a given physical copy budget**. It neither constructs a fatal near-extremizer nor proves an upper bound on the near-extremizer exposure envelope `beta_eta`.

## 6. Prior-art boundary and next gate

The analytic ingredients are classical. Gaussian high moments are exactly (20), and Stirling converts them to the entropy term `m log m`. Laplace asymptotics with amplitudes vanishing at a fixed finite order are standard; NIST DLMF §2.3 gives the classical asymptotic framework. Prescribed zeros of nonnegative trigonometric polynomials are also classical; Stephan Ruscheweyh, *Non-Negative Trigonometric Polynomials with Constraints*, Z. Anal. Anwend. 5 (1986), 169--177, DOI `10.4171/ZAA/191`, is a nearby prior-art boundary. Signal-processing literature on high-order notch filters likewise treats the familiar order-versus-notch-width tradeoff.

None of those results is load-bearing for (25)--(30). The proof is the direct Gaussian rescaling (15)--(21) applied to the exact positive translation architecture already present in `ANF-130`. The Mathia-specific delta is the coupling of the growing zero order to the **physical unsigned copy budget** and to the fixed-rate exponential reservoir scale created by the preceding digit-cloud findings. The prior-art audit found no source asserting this Montgomery--Taylor cascade budget law, so no new durable dependency is added to `research/analytic_frontier/SOURCES.md`.

The next gate is now narrower. To evade (30), a recursive critical construction must not merely increase the power of a finite annihilator. It must use an `A`-dependent positive Fourier molecule whose broad Gaussian suppression is more efficient than its coefficient/copy budget, or exploit coupled chambers so that cancellation at one scale is paid for by coherent regeneration at another. A decisive next theorem would be a general inequality of the form

\[
\text{Gaussian suppression rate}
\le
\mathcal F\bigl(A^{-1}\log V_A,\ \text{translation geometry}\bigr)
\tag{31}
\]

for arbitrary positive translation polynomials, with equality or counterexamples identifying the true exponential cascade boundary. The present finding proves that the canonical repeated-notch family lies strictly on the expensive side of that boundary.