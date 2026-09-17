# PL-339 — Compressed prime shifts have exact path-chain gaps, and the full jump sector is PNT-scale coercive

**Evidence:** `EXACT-DERIVED + POSITIVE-GLOBAL-COERCIVITY + PNT-MATCHED-CONTROL`

**Status:** `SCALABLE-MULTI-CHANNEL-TAIL + SOURCE-NORM-IMPROVEMENT + NET-SOURCE-STILL-INDEFINITE + NO-RH-CONSEQUENCE`

## Precise claim

`PL-337` rewrites every active rational-prime channel in Suzuki's fixed-domain localized Weil operator as a positive atomic jump plus a scalar compensation,

\[
-w_n(S_h+S_h^*)=w_nD_h-2w_nI,
\qquad
D_h:=2I-S_h-S_h^*,
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}>0,
\]

on `I=(-1,1)`, where `S_h` is the zero-exterior compressed translation by `h`. Positivity of `D_h` was enough for the compact-aperture truncation argument in `PL-337`, but it did not quantify whether the positive jump sector remains strong when the number of active prime powers becomes large.

It does. The compression geometry gives an exact spectral gap. For `0<h<=2`, put

\[
m(h):=\left\lceil\frac{2}{h}\right\rceil.
\tag{PL339-1}
\]

Then

\[
\boxed{
\|S_h+S_h^*\|
=2\cos\frac{\pi}{m(h)+1}
}
\tag{PL339-2}
\]

and therefore

\[
\boxed{
D_h\ge
\lambda_*(h)I,
\qquad
\lambda_*(h)
:=2-2\cos\frac{\pi}{m(h)+1}>0.
}
\tag{PL339-3}
\]

At the exact activation point `h=2`, `S_h=0`, so `m(2)=1` and `lambda_*(2)=2`. Immediately after activation, `1<h<2`, one has `m(h)=2` and hence the particularly simple identities

\[
\boxed{
\|S_h+S_h^*\|=1,
\qquad
D_h\ge I.
}
\tag{PL339-4}
\]

Thus a newly active prime-power edge is not merely a nonnegative jump form: throughout the outer half of the logarithmic source window it carries a unit Poincare gap.

Now set

\[
h_n(a)=\frac{\log n}{a},
\qquad
W_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n},
\tag{PL339-5}
\]

and split the active weight into

\[
W_a^{\rm in}:=
\sum_{\log n<a}\frac{\Lambda(n)}{\sqrt n},
\qquad
W_a^{\rm out}:=
\sum_{a\le\log n<2a}\frac{\Lambda(n)}{\sqrt n}.
\tag{PL339-6}
\]

The positive jump sector

\[
J_a:=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}D_{h_n(a)}
\tag{PL339-7}
\]

then satisfies the exact global lower bound

\[
\boxed{J_a\ge W_a^{\rm out}I.}
\tag{PL339-8}
\]

Since the weighted Chebyshev sum

\[
A(x):=\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}
\]

obeys, by partial summation and the prime number theorem,

\[
A(x)\sim2\sqrt x,
\tag{PL339-9}
\]

we have

\[
W_a\sim2e^a,
\qquad
W_a^{\rm in}=O(e^{a/2+o(a)}),
\qquad
W_a^{\rm out}\sim2e^a.
\tag{PL339-10}
\]

Consequently

\[
\boxed{
J_a\ge(1-o(1))W_aI
=(2+o(1))e^aI.
}
\tag{PL339-11}
\]

The positive atomic part therefore remains coercive at the scale of the **entire** von-Mangoldt source mass as the aperture and the number of active channels grow. The many-channel jump tail does not soften by accumulation.

There is a matched limitation. The actual prime operator is

\[
P_a=-\sum_{\log n<2a}w_n(S_{h_n(a)}+S_{h_n(a)}^*)
=J_a-2W_aI.
\tag{PL339-12}
\]

From (PL339-2), the outer channels have norm exactly `w_n`, while every inner channel has norm at most `2w_n`. Hence

\[
\boxed{
\|P_a\|
\le W_a^{\rm out}+2W_a^{\rm in}
=W_a+W_a^{\rm in}
=(1+o(1))W_a
=(2+o(1))e^a.
}
\tag{PL339-13}
\]

This improves the naive triangle bound `||P_a||<=2W_a=(4+o(1))e^a` by an asymptotic factor two. Equivalently,

\[
P_a\ge-(W_a+W_a^{\rm in})I.
\tag{PL339-14}
\]

But (PL339-14) is still negative on the same exponential scale as the source mass. The exact jump coercivity therefore supplies a scalable positive tail estimate without proving positivity of the prime block, of the completed operator, or of any RH-facing branch.

## 1. Exact direct-integral decomposition of one compressed translation

It is enough to work on `(0,2)` by translation of coordinates. Fix `0<h<=2` and write

\[
2=Nh+r,
\qquad
N=\left\lfloor\frac2h\right\rfloor,
\qquad
0\le r<h.
\tag{PL339-15}
\]

Choose the representative coordinate `t in (0,h)`. The points

\[
t,\ t+h,\ t+2h,\ldots
\]

that remain in `(0,2)` form a finite chain. If `r>0`, its length is `N+1` for `0<t<r` and `N` for `r<t<h`; if `r=0`, its length is `N` for almost every `t`. Therefore `L^2(0,2)` is unitarily a direct integral of finite chain spaces of those sizes.

On a chain of length `m`, the operator `S_h+S_h^*` is exactly the adjacency matrix of the path graph `P_m`,

\[
A_m=
\begin{pmatrix}
0&1&&\\
1&0&1&\\
&\ddots&\ddots&\ddots\\
&&1&0
\end{pmatrix}.
\tag{PL339-16}
\]

Its eigenvalues are the standard path values

\[
2\cos\frac{j\pi}{m+1},
\qquad j=1,\ldots,m.
\tag{PL339-17}
\]

The longest chain occurring on a positive-measure set has length

\[
m_{\max}=\left\lceil\frac2h\right\rceil=m(h).
\tag{PL339-18}
\]

The largest absolute eigenvalue of `A_m` increases with `m`, so the direct-integral norm is exactly (PL339-2). Since

\[
D_h=2I-(S_h+S_h^*),
\]

its lower spectral edge is `2-||S_h+S_h^*||`, giving (PL339-3). This also explains the operator-norm discontinuities already seen in the activation analysis: at `h=2` all chains have length one and the shift vanishes, whereas for every `h<2` sufficiently close to two a positive-measure family of two-point chains appears immediately.

For `1<h<2`, the only fiber sizes are one and two. Thus

\[
\sigma(S_h+S_h^*)=\{-1,0,1\},
\qquad
\sigma(D_h)=\{1,2,3\},
\tag{PL339-19}
\]

which proves (PL339-4) without an estimate.

## 2. The outer logarithmic half-window carries almost all source mass

For an active prime power `n`, the scaled lag is `h_n(a)=log n/a`. Every source in the outer logarithmic half-window

\[
a\le\log n<2a
\tag{PL339-20}
\]

therefore satisfies `1<=h_n(a)<2`, and (PL339-3)--(PL339-4) give

\[
D_{h_n(a)}\ge I.
\]

All inner channels remain nonnegative by `PL-337`. Summing the positive forms with the von-Mangoldt weights proves (PL339-8) exactly.

The PNT input is only the size comparison. From `psi(x)~x`, Stieltjes partial summation gives

\[
A(x)
=\frac{\psi(x)}{\sqrt x}
+\frac12\int_1^x\frac{\psi(t)}{t^{3/2}}dt
\sim2\sqrt x.
\tag{PL339-21}
\]

Hence the entire source window has weight `2e^a(1+o(1))`, while the old inner half-window has only `2e^{a/2}(1+o(1))`. The recently activated outer half-window therefore carries asymptotically all of the weighted source mass, and every one of those channels has the same unit lower gap.

This is stronger than summing the nonnegativity in `PL-337`: it prevents the positive jump sector from becoming nearly singular merely because the aperture contains more and more small-lag prime channels.

A slightly sharper exact coefficient can be retained if useful:

\[
J_a\ge
\left(
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\lambda_*\!\left(\frac{\log n}{a}\right)
\right)I.
\tag{PL339-22}
\]

The coarse outer-window bound is preferable for the current route because it isolates the PNT-dominant shell and requires no bookkeeping over the smaller path-length strata.

## 3. What this closes, and what remains

The current multi-prime frontier after `PL-338` asks whether a positive tail can scale with the growing number of source channels rather than relying on the special first-prime order cone. Equations (PL339-8)--(PL339-11) close one precise version of that concern: the **positive Dirichlet jump part itself has a global Poincare constant comparable to total source mass**. Accumulating old prime shifts cannot make this part soft.

This does not propagate the first-prime reflected-correlation sign. The Weil prime block contains the compensating scalar `-2W_aI`; after that subtraction, (PL339-14) still permits a negative contribution of order `e^a`. Nor does the estimate prevent a later source-selected boundary coefficient from vanishing, control branch crossings, or compare the prime block with the archimedean/completed low spectral sector. Those are genuinely separate gates in `PL-338`.

The result does, however, remove one possible explanation for loss of global control. If a completed-Weil branch becomes unstable after many source activations, it is not because the favorable atomic jump sector has diluted to zero relative to the accumulated von-Mangoldt mass. The obstruction must lie in the scalar compensation, the signed correlation geometry/branch selection, or its interaction with the completion.

## 4. Adversarial and novelty audit

The fiber decomposition is elementary operator/graph theory. The eigenvalues (PL339-17) are the classical path-graph spectrum, and (PL339-2) is its direct-integral specialization to a zero-exterior translation on an interval. A targeted search around compressed translations, truncated shifts, and finite-interval Wiener--Hopf operators found broad spectral literature but no need for a new external dependency: the proof above is self-contained and uses only finite path matrices. No broad novelty is claimed for that spectral calculation.

The PNT asymptotic is classical and already part of the line's source ledger; no new `SOURCES.md` entry is required. The durable line-specific delta is the combination with Suzuki's exact positive-jump decomposition from `PL-337`: **the outer half of the active log-energy window carries asymptotically all von-Mangoldt mass and every channel in that half-window has unit compressed-shift gap**, yielding the scalable coercivity (PL339-11) and the sharpened source norm bound (PL339-13).

This is not rational-prime rigidity at RH strength. Any positive atomic source whose weighted mass is asymptotically concentrated in the outer half of its lag window would satisfy the same operator inequality, and a Beurling/generalized-prime system with the same PNT-scale weighted mass could reproduce the leading asymptotic. The result is therefore a **route advance and matched control**, not evidence for a new characterization of the rational primes or for RH.

It is also compatible with the older negative findings. `PL-276`/`PL-278` show that an active finite positive source can have infinite two-sided Morse structure before the noncompact completion; a lower scalar bound of size `W_a` does not contradict that. `PL-059` shows that the completed pole cancels the universal PNT boundary mode while an essential prime-log recurrence remains; the present bulk coercivity is likewise a PNT-scale statement and does not remove that recurrence.

## Consequence for `prime_lattice`

The many-channel source ledger can now be sharpened from

\[
J_a\ge0
\]

to

\[
\boxed{J_a\ge(1-o(1))W_aI.}
\]

Thus future global branch arguments should not spend effort proving that the accumulated positive jump part remains coercive; it already does so at the correct total-mass scale. The unresolved target is to exploit structure beyond this PNT-universal estimate: either a cancellation/control of the scalar compensation and completion, or a rational-prime-specific constraint on the low/mesoscopic branch that survives the matched generalized-prime control and can propagate through successive thresholds.

## Dependencies

- `PL-337`: exact decomposition of every prime-power channel as `w_nD_h-2w_nI` with `D_h` a positive zero-exterior jump form.
- `PL-338`: all finite prime-power activations are norm-resolvent continuous; the remaining frontier is multi-channel branch persistence and later boundary-trace noncollapse.
- `PL-059`: PNT-scale boundary main mode and its canonical pole cancellation, used only as an adversarial interpretation of what leading PNT asymptotics can and cannot prove.
- Classical prime number theorem and Stieltjes partial summation for (PL339-21), already within the line's prior-art surface.
