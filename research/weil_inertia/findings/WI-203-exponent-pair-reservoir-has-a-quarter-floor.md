# WI-203 — the generic exponent-pair reservoir has a sharp one-quarter floor

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-201 preserved the generic Khayrulloev--Rakhmonov theorem surface after withdrawing the unsupported Bourgain--Watt numerical specialization, and WI-202 inserted the strongest ordinary exponent pair currently recorded by ANTEDB to lower the source-safe bow cutoff to

\[
\theta_*=\frac{3943}{12011}=0.3282824077928565\ldots .
\]

There is an exact endpoint barrier on this entire route. For every ordinary exponent pair `(\kappa,\lambda)`, the standard exponent-pair triangle has

\[
\kappa\ge0,\qquad \lambda\ge\frac12.
\]

The generic short-interval threshold used by both Khayrulloev and Rakhmonov is

\[
\theta(\kappa,\lambda)=\frac{\kappa+\lambda}{2\kappa+2}.
\]

Therefore

\[
\boxed{
\theta(\kappa,\lambda)-\frac14
=\frac{\kappa+2\lambda-1}{4(\kappa+1)}
\ge0.
}
\]

Equality is possible only at

\[
\boxed{(\kappa,\lambda)=(0,1/2),}
\]

which is exactly the exponent-pair conjecture point. Consequently **even the full exponent-pair conjecture can lower the generic Khayrulloev--Rakhmonov interval exponent only to `1/4`, never below it**.

For the source-compatible count-saturating bow, whose vertical span is

\[
L_T=T^{\vartheta+o(1)}/\log T
\]

up to a bounded positive scale factor, the packing argument used in WI-198--WI-202 requires a theorem interval `T^(theta+epsilon)` with a fixed positive `epsilon` satisfying `theta+epsilon<vartheta`. Hence this entire exponent-pair reservoir architecture can at best exclude fixed-power bows with

\[
\boxed{\vartheta>\frac14.}
\]

It cannot reach any fixed `0<\vartheta<1/4`; and at the endpoint `\vartheta=1/4`, the bow's extra factor `1/log T` makes it shorter than `T^(1/4+epsilon)` for every fixed positive `epsilon`, so the endpoint is not recovered either. The same one-quarter floor applies to the fixed-physical-depth Rakhmonov pruning that uses the identical interval threshold. It does **not** improve or replace WI-199's separate normalized-depth screening statement.

Thus improving ordinary exponent pairs can still reduce the current numerical frontier `3943/12011`, but it can never eliminate the source-fixed covariance problem all the way down to arbitrarily short fixed-power bows through these generic theorem surfaces. Any RH-facing closure of the surviving `0<\vartheta\le1/4` regime must use arithmetic information not compressed solely into an ordinary exponent pair and the Khayrulloev--Rakhmonov threshold, or must attack the distinguished source-fixed covariance directly.

## 1. Exact minimization over the full exponent-pair region

The maintained Analytic Number Theory Exponent Database defines an exponent pair as a point of

\[
\mathcal E\subseteq
\left\{(\kappa,\lambda):
0\le\kappa\le\frac12\le\lambda\le1,
\ \kappa+\lambda\le1
\right\}.
\tag{1}
\]

Only the two inequalities `\kappa>=0` and `\lambda>=1/2` are needed here. Since `\kappa+1>0`, direct subtraction gives

\[
\begin{aligned}
\theta(\kappa,\lambda)-\frac14
&=
\frac{\kappa+\lambda}{2(\kappa+1)}-\frac14\\
&=
\frac{2\kappa+2\lambda-(\kappa+1)}{4(\kappa+1)}\\
&=
\boxed{
\frac{\kappa+2\lambda-1}{4(\kappa+1)}.
}
\tag{2}
\end{aligned}
\]

Equation (1) implies

\[
\kappa+2\lambda-1
=\kappa+2\left(\lambda-\frac12\right)\ge0,
\tag{3}
\]

so

\[
\boxed{\theta(\kappa,\lambda)\ge1/4}
\tag{4}
\]

for every ordinary exponent pair, known or conjectural.

Equality in (3) forces simultaneously `\kappa=0` and `\lambda=1/2`. Conversely that point gives `\theta=1/4`. ANTEDB records precisely `(0,1/2)` as the **Exponent Pair Conjecture**. Hence

\[
\boxed{
\inf_{(\kappa,\lambda)\text{ exponent pair}}
\theta(\kappa,\lambda)=\frac14
}
\tag{5}
\]

*conditional on the exponent-pair conjecture*, while the unconditional statement needed for the barrier is the weaker but exact universal lower bound (4). In other words, the conjecture shows that the algebraic floor is expected to be sharp; it is not needed to prove that no ordinary exponent pair can cross it.

This is the same classical quarter boundary that exponent-pair theory predicts for the Dirichlet divisor problem: the standard exponent-pair reduction has exponent `(\kappa+\lambda)/(2\kappa+2)`, and the exponent-pair conjecture yields the divisor exponent `1/4`. That classical context explains the appearance of the same scalar functional here. The bow consequence below is a separate application of the already-audited zeta short-interval theorem surfaces.

## 2. Consequence for the every-interval critical-line reservoir

Khayrulloev's generic theorem, as audited in WI-201 and reused in WI-202, states that for an ordinary exponent pair `(\kappa,\lambda)`, fixed sufficiently small positive `\epsilon`, and

\[
h=T^{\theta(\kappa,\lambda)+\epsilon},
\tag{6}
\]

every sufficiently high interval of length `h` contains `\gg_\epsilon h\log T` odd-order critical-line zeros.

For a count-saturating source-compatible bow with

\[
m_T=T^{\vartheta+o(1)},
\qquad
L_T=(c_T+o(1))\frac{m_T}{\log T},
\tag{7}
\]

where `c_T` stays at bounded positive scale, the WI-198/WI-202 packing requires

\[
\frac{L_T}{h}
=T^{\vartheta-\theta-\epsilon+o(1)}\frac{c_T}{\log T}
\longrightarrow\infty.
\tag{8}
\]

For fixed `\vartheta>\theta`, one chooses a fixed `\epsilon>0` with `\theta+\epsilon<\vartheta`, and the contradiction goes through. But (4) implies that no ordinary exponent pair permits `\theta<1/4`. Therefore the strongest possible consequence obtainable from this generic theorem by improving the exponent pair alone is

\[
\boxed{\vartheta>1/4.}
\tag{9}
\]

The endpoint remains outside the theorem interface even under the exponent-pair conjecture. If `\vartheta=1/4` and `\theta=1/4`, then for every fixed `\epsilon>0`,

\[
\frac{L_T}{T^{1/4+\epsilon}}
=T^{-\epsilon+o(1)}\frac{c_T}{\log T}
\longrightarrow0.
\tag{10}
\]

Thus neither endpoint bookkeeping nor a better known exponent pair can turn the current every-interval theorem into a contradiction at `\vartheta=1/4`.

This is a theorem-interface barrier, not a statement that every-interval critical-line information below `T^(1/4)` is impossible. A future theorem proved by a method not funneled through the scalar exponent-pair threshold (6) could evade it.

## 3. The Rakhmonov fixed-depth route has the same floor

Rakhmonov's generic narrow-rectangle theorem uses the identical admissibility condition

\[
H>T^{\theta(\kappa,\lambda)+\epsilon}.
\tag{11}
\]

WI-200's algebra, retained generically by WI-201 and instantiated correctly in WI-202, applies this theorem to the whole bow interval and excludes the explicit Maynard--Pratt fixed-physical-depth plateau once the bow exponent lies strictly above the chosen `\theta`.

Since every ordinary exponent pair obeys (4), improving the exponent pair can push this fixed-depth pruning no lower than

\[
\boxed{\vartheta>1/4.}
\tag{12}
\]

The endpoint again fails for the same `1/log T` span loss and fixed positive `\epsilon`. This conclusion concerns fixed physical horizontal depth in the range where Rakhmonov's density exponents give a saving after normalization. It does **not** create WI-199's exponentially decaying tail at normalized depth `(\beta-1/2)\log T=O(1)`, and no screening-scale claim is strengthened here.

## 4. Relation to WI-193: the same quarter appears in a different bottleneck

WI-193 proves a different one-quarter obstruction. There the source covariance is first split into individual shifted-prime sums `S_h`; even if every fixed shift is granted ideal square-root cancellation, absolute assembly over the physical shift family still misses the bow target for bow exponent below `1/4`. That is an information-loss barrier caused by discarding relative phases between shifts.

The present finding does not reprove WI-193 and WI-193 does not imply (4). Here no hypothetical fixed-shift cancellation estimate is used. Instead, the obstruction is the geometry of the **ordinary exponent-pair parameter space itself** combined with the exact threshold in the Khayrulloev--Rakhmonov theorem surfaces. The two routes therefore arrive independently at the same quarter scale:

- fixed-shift square-root control plus absolute assembly cannot close below one quarter (`WI-193`);
- every-interval/fixed-depth reservoir pruning obtained solely through an ordinary exponent pair cannot close at or below one quarter (this finding).

This coincidence narrows the surviving target rather than proving a universal quarter law. A genuinely joint source estimate, a stronger every-interval zero theorem outside the exponent-pair interface, or another arithmetic observable can evade both barriers.

## 5. Prior art and novelty audit

**Literature-backed inputs.** The exponent-pair triangle, the conjectural endpoint `(0,1/2)`, and the relation of the scalar functional `(\kappa+\lambda)/(2\kappa+2)` to the divisor problem are classical exponent-pair theory; the current definitions and conjectural endpoint were checked against the maintained ANTEDB exponent-pair chapter. Olivier Robert's review of van der Corput exponent pairs also records that the exponent-pair conjecture yields divisor exponent `1/4`. Khayrulloev's every-interval odd-order-zero theorem and Rakhmonov's every-center narrow-rectangle theorem are the primary zeta theorem surfaces already audited in WI-201--WI-202.

**Exact repository deduction.** Equations (2)--(5) are elementary exact minimization of the theorem's threshold over the full ordinary exponent-pair region, not merely over the currently known convex hull. Equations (8)--(12) propagate that floor through the already-established bow bookkeeping. The result is stronger in a different sense from WI-202: WI-202 identifies the best cutoff supplied by the **currently known** exponent pairs, whereas the present finding proves an absolute floor for this theorem architecture even under the standard conjectural completion of exponent-pair theory.

A bounded novelty search for the exact threshold formula together with `1/4`, for the exponent-pair conjecture together with short-interval odd-order zeta zeros, and for the same conjunction with narrow-rectangle zero density found the classical divisor-problem quarter boundary but did not locate a published statement applying this minimization to the Khayrulloev--Rakhmonov bow reservoir. Absence of a search hit is not evidence of priority, and no priority claim is made.

Primary/current sources:

- Terence Tao, Tim Trudgian and Andrew Yang, **Analytic Number Theory Exponent Database**, exponent-pair chapter, Definition 5.1 and Heuristic 5.6, https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html (current state audited 8 Sep 2026).
- Olivier Robert, **On van der Corput's k-th derivative test for exponential sums**, *Indagationes Mathematicae* 27:2 (2016), 559--589, DOI `10.1016/j.indag.2015.11.009`. Role: standard exponent-pair definition and the classical statement that the exponent-pair conjecture gives divisor exponent `1/4`.
- Sh. A. Khayrulloev, **On the estimate of the number of odd-order zeros of the Riemann zeta function lying on the critical line**, *Izvestiya of the National Academy of Sciences of Tajikistan*, 2024, No. 4 (197), 51--64, https://journals.anrt.tj/files/News_m/news_m_2024_04.pdf. Role: generic every-interval theorem with threshold `(\kappa+\lambda)/(2\kappa+2)`.
- Z. Kh. Rakhmonov, **Density of zeros of the Riemann zeta function in narrow rectangles of the critical strip**, *Chebyshevskii Sbornik* 26:5 (2025), 158--183, DOI `10.22405/2226-8383-2025-26-5-158-183`. Role: generic every-center narrow-rectangle theorem with the same exponent-pair threshold.

## 6. Evidence boundary and falsification

The finding would fail if the generic Khayrulloev or Rakhmonov threshold were not actually parameterized by an ordinary exponent pair in the standard sense used by (1), or if their theorem required a different scalar than `theta=(\kappa+\lambda)/(2\kappa+2)`. Those interfaces were primary-source audited in WI-201 and are independently restated in WI-202. The inequality (4) itself then follows exactly from the defining exponent-pair region.

This result does **not** prove that zeta has off-critical zeros, does not prove that Maynard--Pratt bows occur, does not exclude every off-line configuration above or below one quarter, and does not claim a universal lower bound for all possible short-interval zero theorems. It says only that the specific generic exponent-pair reservoir architecture cannot descend below the quarter scale by improving its ordinary exponent-pair input.

A decisive falsification would be either:

1. an ordinary exponent pair in the theorem's sense with `theta<1/4`, which would contradict the standard exponent-pair triangle; or
2. a valid reformulation of the Khayrulloev/Rakhmonov argument whose short-interval exponent is not constrained by (4), in which case it is a genuinely different theorem interface and lies outside this barrier.

## Research consequence

The current known cutoff `3943/12011` from WI-202 remains worth improving if the aim is to shrink the source-covariance workload. But **ordinary exponent-pair optimization is now known not to be a route to eliminating that workload entirely**. Even granting the exponent-pair conjecture, count-saturating fixed-power bows with

\[
0<\vartheta\le\frac14
\]

remain outside the generic every-interval reservoir contradiction, and the endpoint is not rescued by the existing `+epsilon` theorem form.

For the RH-facing mandate, this closes a tempting asymptotic escape: one cannot hope that progressively better exponent pairs alone will eventually prune every fixed-power bow before source coercivity is needed. The surviving quarter-and-below regime requires a source-fixed covariance theorem, a different local zero reservoir with genuinely stronger interval dependence, or another observable that detects the off-line geometry without passing through this scalar exponent-pair bottleneck.