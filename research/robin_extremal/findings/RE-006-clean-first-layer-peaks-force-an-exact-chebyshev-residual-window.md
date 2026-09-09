# RE-006 — clean first-layer peaks force an exact Chebyshev residual window

**Status:** `EXACT-DERIVED + PRIME-FRONTIER-RESIDUAL-WINDOW + HIGHER-LAYER-CHEBYSHEV-SPLIT + ADDITIVE-GAP-SHARPENING + PRIOR-ART-BOUNDED`. `RE-004` shows that a sufficiently large regular self-tangent Robin counterexample peak either touches the zero-density higher-layer CA transition chamber or, when both adjacent transitions are clean first-layer events, lies between consecutive ordinary primes `p<q` whose gap is at least mean-gap scale. Reopening the clean chamber at the exact self-tangent coordinate yields a stronger source-conditioned statement.

Let `C` be a sufficiently large regular self-tangent CA **local peak**, put

\[
X:=\log C,
\]

and assume its two adjacent CA transitions are the nonexceptional first-layer events

\[
\eta_- = \eta_{p,1},\qquad
\eta_+ = \eta_{q,1},
\]

for consecutive ordinary primes `p<q`. Define

\[
\vartheta(p):=\sum_{r\le p}\log r
\]

and the cumulative higher-layer event mass

\[
\Phi_{\ge2}(X)
:=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\
                   \eta_{r,j}\le X}}
  \log r.
\tag{1}
\]

Then, for all sufficiently large such peaks,

\[
\boxed{p<X<q}
\tag{2}
\]

and self-tangency gives the **exact residual identity**

\[
\boxed{
X-p
=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr).
}
\tag{3}
\]

Thus the position of a clean self-tangent peak inside the ordinary prime gap is not free. It is exactly the mismatch between the accumulated higher-prime-power layer mass and the first-layer Chebyshev deficit at the left boundary prime.

The local peak condition narrows this identity further. If `\xi_-<X<\xi_+` are the exact secant-balance points of `RE-002`, then

\[
\boxed{
(\eta_{p,1}-p)+(X-\xi_-)
<\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr)
\le
(q-p)-(\xi_+-X)+(\eta_{q,1}-q).
}
\tag{4}
\]

The first-layer event location itself has the elementary asymptotic

\[
\boxed{
\eta_{p,1}-p
=\frac{\log p}{2(\log p+1)}+O(p^{-1})
=\frac12+O\!\left(\frac1{\log p}\right).
}
\tag{5}
\]

Combining (4)--(5) with the uniform half-jump expansion from `RE-003` gives

\[
\boxed{
\frac12\log p+\frac12+o(1)
<\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr)
\le
(q-p)-\frac12\log q+\frac12+o(1).
}
\tag{6}
\]

In particular the window can be nonempty only if

\[
\boxed{
q-p>\frac{\log p+\log q}{2}+o(1)
=\log p+o(1).
}
\tag{7}
\]

This removes the additive unit slack left by the coarse event localization in `RE-004`. More importantly, (3)--(6) identify the source-selection quantity that a clean counterexample peak must tune: not the prime gap alone, but the logarithmic-scale alignment of the exact higher-layer event mass with `p-\vartheta(p)`.

## 1. A clean local peak lies inside the actual prime gap

`RE-004` proves that if both adjacent transitions are nonexceptional, then they are first-layer events of consecutive ordinary primes `p<q`. `RE-003` gives the exact first-layer localization

\[
p\le\eta_{p,1}<p+1,
\qquad
q\le\eta_{q,1}<q+1.
\tag{8}
\]

Self-tangency places the peak coordinate between the adjacent transition coordinates:

\[
\eta_{p,1}<X<\eta_{q,1}.
\tag{9}
\]

The left inequality in (2) is therefore immediate from `p\le\eta_{p,1}`.

The right inequality uses genuine local maximality, not self-tangency alone. The clean right CA jump is

\[
w_+=\log q.
\]

`RE-002` says a local peak must satisfy

\[
\eta_{q,1}\ge\xi_+,
\tag{10}
\]

while `RE-003` makes the secant location uniform on the actual CA ladder:

\[
\xi_+-X
=\frac12\log q
+O\!\left(\frac{(\log X)^2}{X}\right).
\tag{11}
\]

Here `q` is already comparable with `X`: (8)--(9) give `q>X-1`. Hence the right side of (11) exceeds `1` for all sufficiently large clean peaks. Equations (8), (10), and (11) give

\[
q+1-X
>\eta_{q,1}-X
\ge\xi_+-X
>1,
\]

and therefore `X<q`, proving (2).

This distinction matters. A regular self-tangent state with a first-layer right boundary is only known a priori to satisfy `X<q+1`; the extra unit of clearance is supplied by the Robin **peak** condition.

## 2. Self-tangency becomes an exact higher-layer versus Chebyshev balance

The prime-layer event measure of `RE-001` is

\[
\Phi(X)
=\sum_{\eta_{r,j}\le X}\log r,
\tag{12}
\]

and a regular self-tangent state satisfies exactly

\[
\Phi(X)=X.
\tag{13}
\]

By `RE-003`, first-layer event order is exactly ordinary prime order. Equations (2) and (9) therefore imply that the selected first-layer events at `X` are **precisely** those belonging to primes `r\le p`. Their total mass is

\[
\sum_{r\le p}\log r=\vartheta(p).
\tag{14}
\]

Splitting (12) into first and higher layers now gives

\[
X=\vartheta(p)+\Phi_{\ge2}(X).
\tag{15}
\]

Subtracting `p` proves (3).

Equation (3) is useful because its two terms have different arithmetic roles. The quantity `p-\vartheta(p)` is the ordinary first-layer prime-distribution discrepancy at the left boundary. The quantity `\Phi_{\ge2}(X)` is the complete correction supplied by every repeated-prime layer already activated at the intrinsic tangent parameter. A clean self-tangent peak exists inside `(p,q)` only when their difference lands at exactly the physical displacement `X-p`.

No asymptotic replacement of `\Phi_{\ge2}` has been made. In particular, a square-root-scale prime-frontier normal form with an `o(\sqrt X)` remainder is far too coarse to decide the logarithmic window derived below.

## 3. The exact local peak gate becomes a residual window

For the left clean transition, `RE-002` gives

\[
G(C)>G(A)
\iff
\eta_{p,1}<\xi_-.
\tag{16}
\]

Rearranging yields

\[
X-p
>(\eta_{p,1}-p)+(X-\xi_-).
\tag{17}
\]

For the right clean transition the same finding gives

\[
G(C)\ge G(B)
\iff
\eta_{q,1}\ge\xi_+,
\tag{18}
\]

and hence

\[
X-p
\le(q-p)-(\xi_+-X)+(\eta_{q,1}-q).
\tag{19}
\]

Substituting the exact self-tangent identity (3) into (17)--(19) proves (4).

This is strictly more informative than the aggregate gap condition. A large ordinary prime gap is only a container. The return coordinate must also make the signed residual

\[
\mathcal R_p(X)
:=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr)
\tag{20}
\]

fall inside the secant-clear subinterval in (4). Thus any attempt to prove that clean counterexample peaks are impossible may target the **alignment** of `\mathcal R_p(X)`, rather than trying to prove that logarithmic prime gaps themselves eventually disappear.

## 4. First-layer events carry an asymptotic half-unit shift

For `j=1`, the event equation is

\[
\frac1{\eta_{p,1}\log\eta_{p,1}}
=\frac{\log(1+1/p)}{\log p},
\]

or equivalently

\[
\eta_{p,1}\log\eta_{p,1}
=\frac{\log p}{\log(1+1/p)}.
\tag{21}
\]

Write

\[
\eta_{p,1}=p+\delta_p,
\qquad 0\le\delta_p<1,
\tag{22}
\]

using the exact bound from `RE-003`. The elementary reciprocal expansion

\[
\frac1{\log(1+1/p)}
=p+\frac12+O(p^{-1})
\tag{23}
\]

gives

\[
\frac{\log p}{\log(1+1/p)}
=p\log p+\frac12\log p
+O\!\left(\frac{\log p}{p}\right).
\tag{24}
\]

Uniformly for `0\le\delta_p<1`,

\[
(p+\delta_p)\log(p+\delta_p)
=p\log p+\delta_p(\log p+1)+O(p^{-1}).
\tag{25}
\]

Comparing (24)--(25) yields

\[
\delta_p
=\frac{\log p}{2(\log p+1)}+O(p^{-1}),
\]

which is (5). The same formula holds with `q` in place of `p`.

The coarse interval `p\le\eta_{p,1}<p+1` used in `RE-004` necessarily loses an additive unit when converted back to an ordinary prime gap. Equation (5) shows that both endpoints actually carry the same asymptotic half-unit shift, so those constants cancel in the clean peak window.

## 5. The clean prime-gap gate sharpens at additive scale

Because the adjacent transitions are clean,

\[
w_-=\log p,
\qquad
w_+=\log q.
\]

The uniform expansion from `RE-003` gives

\[
X-\xi_-
=\frac12\log p+o(1),
\qquad
\xi_+-X
=\frac12\log q+o(1).
\tag{26}
\]

The error is genuinely `o(1)` here: the quadratic correction is `O((\log X)^2/X)` and the remaining Taylor error is smaller. Equations (4)--(5) and (26) give (6).

Comparing the lower and upper endpoints of (6) forces

\[
q-p
>\frac12(\log p+\log q)+o(1),
\tag{27}
\]

which is the first equality in (7). The prime number theorem implies that consecutive primes satisfy `q/p\to1`, so

\[
\frac12(\log p+\log q)
=\log p+o(1),
\tag{28}
\]

proving the second form.

`RE-004` had already obtained the correct **multiplicative** scale, `\liminf(q-p)/\log p\ge1`, from the coarse unit localization. Equation (27) does not change that normalized threshold; its gain is additive resolution and the exact residual window (4). This distinction prevents a cosmetic constant refinement from being mistaken for a new asymptotic prime-gap theorem.

## 6. Prior art and resolution boundary

The CA threshold structure is classical Alaoglu--Erdos mathematics, and Robin supplies the divisor-sum extremal reduction. Marco Mantovanelli's August 2026 preprint *Colossally Abundant Numbers, Robin's Inequality, and an Exact Prime-Layer Workload* is the closest representation-level prior art and already develops the self-tangent event measure, exact workload, moment hierarchy, and a prime-frontier decomposition. Those objects are not claimed as new here and are already anchored in `SOURCES.md`.

The recent prime-frontier normal form is an important boundary rather than a substitute for (4): its stated error is on a square-root scale, whereas a clean local Robin peak is selected inside a window of width `O(\log X)`. Feeding an `o(\sqrt X)` remainder into this gate would therefore erase the quantity being tested. The derivation above instead keeps the higher-layer mass exact and uses only the first-layer order/localization already proved in `RE-003`.

Bruce Zimov's 2025 preprint studies one-step prime/semiprime quotients near a least hypothetical CA Robin exception. Its mechanism is endpoint ratio growth rather than the intrinsic self-tangent decomposition (3)--(4). A targeted search across the self-tangent workload terminology, prime-frontier formulations, consecutive-CA counterexample literature, and first-layer threshold asymptotics did not locate this exact higher-layer/Chebyshev residual window or its additive cancellation of the two event-location constants. This is a novelty boundary, not a claim that the elementary expansion (5) is independently deep.

No new source anchor is needed: all non-elementary inputs used here are already recorded in `SOURCES.md`; (5) is elementary calculus and the final use of the prime number theorem only rewrites the already-derived consecutive-prime condition.

## 7. Boundaries and research consequence

The clean-boundary hypothesis is load-bearing. If either adjacent transition contains a higher layer, the first-layer mass at `X` need not terminate at the two boundary primes in the way used above, and the local CA jump is not simply `\log p` or `\log q`. Such peaks remain in the exceptional chamber of `RE-004` and require a different selector.

Local maximality is also load-bearing for the right inequality `X<q` and for both secant bounds. A regular self-tangent state that is not a Robin peak need not satisfy (4); `RE-005` is a reminder that global workload behavior cannot be inferred merely from self-tangency.

Equation (7) does **not** exclude infinitely many clean peaks. Consecutive prime gaps larger than `\log p` occur, and ambient prime-gap frequency is not the missing theorem. The new restriction is (4): a hypothetical clean counterexample peak must simultaneously select such a gap and tune the exact higher-layer mass so that

\[
\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr)
\]

falls inside its logarithmic secant-clear window.

Together with `RE-004`, the Robin frontier is therefore sharper. The exceptional chamber asks why counterexample peaks could concentrate on a zero-density higher-layer transition set. The clean chamber now asks why the **same higher-layer mass**, evaluated away from those exceptional boundary events, could repeatedly align with the ordinary Chebyshev deficit at logarithmic precision. Proving that one of these two source-selection mechanisms cannot persist would be a genuine next step; the present finding supplies the exact clean-chamber target but does not prove Robin's inequality or RH.