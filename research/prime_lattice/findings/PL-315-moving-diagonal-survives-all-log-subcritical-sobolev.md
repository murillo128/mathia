# PL-315 — Moving-diagonal transfer survives all-log and subcritical Sobolev regularity

**Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE/ROUTE-NARROWING`

**Status:** `ALL-LOG-REGULARITY-INSUFFICIENT + W11/BV-INSUFFICIENT + H-HALF-MINUS-INSUFFICIENT`

## Claim

`PL-314` proves that the small-order Green transfer can fail to converge to its rank-one corner limit when a fixed endpoint mismatch has sparse bumps at the moving physical scale `Q=r/s`, even if the mismatch belongs to `L^1(dQ)` and tends to zero. That counterexample can be strengthened substantially.

For every fixed outer coordinate `r>0` and every `epsilon>0`, one may choose the single fixed nonnegative mismatch `m(Q)` in the `PL-314` construction so that

\[
m\in C^\infty(0,\infty)\cap\bigcap_{k\ge0}W^{k,1}(0,\infty),
\qquad
\|m\|_{L^1}+\|m'\|_{L^1}<\varepsilon,
\]

and simultaneously

\[
\boxed{
\sup_{Q\gg1}Qm(Q)<\infty,
\qquad
\limsup_{Q\to\infty}Qm(Q)=r.
}
\tag{PL315-1}
\]

Thus the mismatch obeys the critical pointwise envelope `m(Q)=O(Q^{-1})`, but not the little-`o` condition `Qm(Q)->0` used in `PL-314`.

Pull this mismatch back to the physical endpoint by

\[
Q(y)=-\log\frac{1-y}{2},
\qquad
\widetilde m(y)=m(Q(y)),
\qquad -1<y<1,
\]

and extend it by zero to `R`. The extension `E\widetilde m` can be chosen with arbitrarily small `W^{1,1}(R)` norm. Consequently

\[
\boxed{
E\widetilde m\in H^\alpha(\mathbb R)
\quad\text{for every }\alpha<\frac12,
}
\tag{PL315-2}
\]

and, for every logarithmic Fourier order `j`,

\[
\boxed{
E\widetilde m\in X_j,
\qquad
\|E\widetilde m\|_{X_j}
\le C^{j+1}\sqrt{(2j)!}\,
\|E\widetilde m\|_{W^{1,1}}.
}
\tag{PL315-3}
\]

The permitted growth `exp(O(j log j))` in (PL315-3) is far below the `exp(Cj^2 log j)` upper bound obtained for the actual localized-Weil eigenstates in `PL-292`.

Nevertheless, along a sequence `s_n->0`, the same fixed `m` satisfies

\[
\boxed{
\mathcal A_{s_n}[m](r)\ge\frac34e^{-2r},
}
\tag{PL315-4}
\]

while the rank-one candidate can be made smaller than `e^{-2r}/4`. Hence neither all finite logarithmic Fourier moments, the quantitative hierarchy available in `PL-292`, physical `W^{1,1}`/BV regularity, nor every subcritical Sobolev exponent `H^alpha`, `alpha<1/2`, is sufficient by itself to suppress the moving diagonal.

This closes a natural shortcut left after `PL-314`: the needed endpoint control is not a generic consequence of the regularity already proved in `PL-291`--`PL-292`, and it would still not follow from an arbitrary positive Sobolev gain below the critical half derivative.

## 1. Strengthening the `PL-314` bump selection

Use the notation and Green measures `mu_{s,r}` of `PL-314`. Choose

\[
\chi\in C_c^\infty((-1,1)),
\qquad 0\le\chi\le1,
\qquad \chi=1\text{ on }[-1/2,1/2].
\]

Choose `delta_n>0` with

\[
\delta_n<\min\{r/4,1/2\},
\qquad
\sum_n\delta_n<
\min\left\{
\frac{\varepsilon}{4\|\chi\|_{L^1}},
\frac{e^{-r}}{4\|\chi\|_{L^1}}
\right\}.
\tag{PL315-5}
\]

For each fixed `delta_n`, the weak convergence used in `PL-314` permits `s_n` to be chosen arbitrarily small while retaining

\[
\mu_{s_n,r}
\bigl((r-\delta_n/2,r+\delta_n/2)\bigr)
\ge\frac34e^{-2r}.
\tag{PL315-6}
\]

Therefore the recursive choice in `PL-314` can impose, in addition to disjointness of

\[
J_n=\left(\frac{r-\delta_n}{s_n},
          \frac{r+\delta_n}{s_n}\right),
\]

the extra upper bounds

\[
s_n\le
\frac{\varepsilon\,2^{-n-2}}{1+\|\chi'\|_{L^1}},
\qquad
s_n\le2^{-n}\delta_n^n.
\tag{PL315-7}
\]

Define, exactly as in `PL-314`,

\[
m(Q)=\sum_{n\ge1}s_n
\chi\!\left(\frac{s_nQ-r}{\delta_n}\right).
\tag{PL315-8}
\]

The supports are pairwise disjoint and locally finite, so `m` is one fixed nonnegative `C^infty` function. Its mass is

\[
\|m\|_{L^1}
=\|\chi\|_{L^1}\sum_n\delta_n,
\tag{PL315-9}
\]

and for every integer `k>=1`,

\[
\|m_n^{(k)}\|_{L^1}
=\|\chi^{(k)}\|_{L^1}s_n^k\delta_n^{1-k}.
\tag{PL315-10}
\]

For fixed `k`, the second bound in (PL315-7) gives

\[
s_n^k\delta_n^{1-k}
\le2^{-nk}\delta_n^{k(n-1)+1}
\le2^{-nk}
\]

for all sufficiently large `n`; the finitely many initial terms are harmless. Hence

\[
\boxed{m\in\bigcap_{k\ge0}W^{k,1}(0,\infty).}
\tag{PL315-11}
\]

For `k=1`,

\[
\|m'\|_{L^1}
=\|\chi'\|_{L^1}\sum_ns_n,
\tag{PL315-12}
\]

so (PL315-5) and (PL315-7) give the stated arbitrarily small `L^1+W^{1,1}` size. The same extra upper bounds do not affect (PL315-6), because each `s_n` may be decreased after `delta_n` is fixed.

## 2. The spikes already satisfy the critical `1/Q` envelope

On the support of the `n`-th bump,

\[
r-\delta_n<s_nQ<r+\delta_n,
\qquad 0\le m(Q)\le s_n.
\]

Therefore

\[
0\le Qm(Q)\le r+\delta_n.
\tag{PL315-13}
\]

At the center `Q_n=r/s_n`, `chi(0)=1`, so

\[
\boxed{Q_nm(Q_n)=r.}
\tag{PL315-14}
\]

Since summability forces `delta_n->0`, (PL315-13)--(PL315-14) prove (PL315-1). The obstruction is not caused by a tail larger than the natural next-order scale `1/Q`; it is caused by sparse saturation of that scale exactly where the moving Green atom samples it.

In physical distance `delta=1-y=2e^{-Q}`, the same statement is

\[
|\widetilde m(1-\delta)|
\le\frac{C}{|\log(\delta/2)|},
\tag{PL315-15}
\]

with no little-`o` improvement along the selected centers.

## 3. Physical `W^{1,1}`, every all-log moment, and every `H^{1/2-}` exponent

The map `Q -> y=1-2e^{-Q}` is an increasing diffeomorphism from `(0,infty)` to `(-1,1)`, with

\[
\frac{dy}{dQ}=1-y=2e^{-Q}.
\]

Because `m(Q)->0` and its first support stays away from `Q=0`, the physical pullback tends to zero at both endpoints. Its zero extension therefore has no boundary jump. Moreover

\[
\widetilde m'(y)=\frac{m'(Q(y))}{1-y},
\]

and the Jacobian cancels exactly:

\[
\int_{-1}^{1}|\widetilde m'(y)|\,dy
=\int_0^\infty|m'(Q)|\,dQ.
\tag{PL315-16}
\]

Also

\[
\int_{-1}^{1}|\widetilde m(y)|\,dy
=2\int_0^\infty e^{-Q}|m(Q)|\,dQ
\le2\|m\|_{L^1}.
\tag{PL315-17}
\]

Thus `E\widetilde m in W^{1,1}(R)` with arbitrarily small norm.

For a compactly supported `W^{1,1}` function `f`, integration by parts gives

\[
|\widehat f(\xi)|
\le\frac{\|f'\|_{L^1}}{|\xi|},
\qquad |\xi|\ge1.
\tag{PL315-18}
\]

Hence for every `alpha<1/2`,

\[
\int_{|\xi|\ge1}|\xi|^{2\alpha}
|\widehat f(\xi)|^2\,d\xi
\le
\|f'\|_{L^1}^2
\int_1^\infty\xi^{2\alpha-2}\,d\xi<\infty,
\tag{PL315-19}
\]

which proves (PL315-2).

The same estimate is stronger than the all-log requirement. With

\[
\ell(\xi)=1+\log(2+|\xi|),
\]

we have

\[
\int_{|\xi|\ge1}\ell(\xi)^{2j}
|\widehat f(\xi)|^2\,d\xi
\le
C^{2j}\|f'\|_{L^1}^2
\int_0^\infty(1+t)^{2j}e^{-t}\,dt.
\]

The last integral is at most `C(2j)!`; the low-frequency part is controlled by `||f||_1`. This gives (PL315-3). Thus the counterexample lies in every `X_j` with logarithmic-moment growth only `exp(O(j log j))`.

The moving-diagonal obstruction is therefore not hidden in a grotesquely irregular physical mismatch that would automatically be excluded by `PL-291`--`PL-292`. It survives a function class substantially stronger than the regularity currently proved for the actual branch.

## 4. The moving atom still sees order one

At `s=s_n`, if `|q-r|<delta_n/2`, then

\[
m(q/s_n)
=s_n\chi\!\left(\frac{q-r}{\delta_n}\right)
=s_n.
\]

The normalized transfer of `PL-314` is

\[
\mathcal A_s[m](r)
=\frac1s\int_0^\infty m(q/s)\,d\mu_{s,r}(q).
\]

Positivity and (PL315-6) therefore give (PL315-4). On the other hand, (PL315-9) and (PL315-5) give

\[
e^{-r}\int_0^\infty m(Q)\,dQ
<\frac14e^{-2r}.
\tag{PL315-20}
\]

Thus the same fixed mismatch violates the rank-one candidate despite all the additional regularity. Its physical `W^{1,1}` norm can be made arbitrarily small while the selected transfer remains bounded below by `3e^{-2r}/4`. The defect is a moving-tail sampling phenomenon, not a bulk regularity defect.

## 5. Adversarial checks

**This does not prove that the actual completed-Weil mismatch contains such spikes.** It blocks implications from broad regularity classes to the moving-diagonal tail law. The actual eigen-equation may impose a pointwise asymptotic, monotonicity, a sign/ODE relation, or another source-structured restriction that excludes the construction.

**The half derivative is not crossed.** The Fourier argument gives every `H^alpha`, `alpha<1/2`, but no `H^{1/2}` claim. This is deliberate: `PL-293` identifies `1/2` as the critical zero-extension boundary threshold for the canonical logarithmic problem. The present result says that all subcritical Sobolev regularity is still too weak for the moving-corner transfer.

**Bare BV or `W^{1,1}` in the `Q` variable is not an escape.** The same `m` lies in every `W^{k,1}(dQ)`, including BV, yet sparsely saturates `Qm(Q)`. Thus the suggestion in `PL-314` that BV might supply missing anti-concentration can only work with additional structure, not through total variation alone.

**An `O(1/Q)` remainder is not enough.** A matching theorem based on a two-term boundary estimate must produce a genuine `o(1/Q)` remainder, or another condition that prevents sparse saturation, rather than only a big-`O` envelope.

**No arithmetic sign or RH conclusion is obtained.** The counterexample is universal small-order Green geometry. Its role is to sharpen the analytic gate that the rational-prime completed-Weil branch must cross before the scalar endpoint/source balance of `PL-313` can be used safely.

## 6. Prior-art and novelty audit

The load-bearing Green-measure convergence, diagonal atom, and original smooth `L^1` counterexample are already persisted in `PL-314`; the corner rank-one target comes from `PL-313`. The Fourier fact used here is elementary: compactly supported `W^{1,1}` gives `|hat f(xi)|=O(1/|xi|)`, which directly implies every logarithmic moment and every Sobolev exponent below `1/2`.

A structure-based literature search was run around moving test functions against weakly convergent concentrating measures, uniform-integrability/concentration defects, BV or `W^{1,1}` tail control, and small-order fractional-Laplacian Green kernels. It recovered standard concentration/uniform-integrability principles and the established small-order Green/boundary literature, but no direct theorem matching this `Q=q/s` transfer with the simultaneous `W^{1,1}`, all-log, and `H^{1/2-}` strengthening. Search absence is not treated as broad novelty evidence. The durable claim is the exact line-local strengthening of the `PL-314` obstruction.

## Consequence for the research line

The regularity gate is now narrower. The all-log bootstrap of `PL-291`, its quantitative refinement in `PL-292`, a generic `BV/W^{1,1}` bound, and even an arbitrary collection of subcritical Sobolev gains cannot justify the completed-Weil corner reduction. The Green atom probes a moving tail scale that these global regularity norms do not control.

A useful next theorem must therefore come from the actual branch equation and force one of the missing anti-concentration properties: `Qm(Q)->0`, a genuine asymptotic expansion with an `o(1/Q)` remainder, monotone/one-sided tail structure, or a direct estimate of the moving samples `m(r/s)` strong enough to replace pointwise decay. Only after such a source-structured statement is proved is the endpoint moment from `PL-313` a legitimate scalar matching datum.
