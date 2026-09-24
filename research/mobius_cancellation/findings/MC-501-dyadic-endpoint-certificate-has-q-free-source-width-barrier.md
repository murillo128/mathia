# MC-501 — Dyadic endpoint certificate has a Q-free source-width barrier

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-BUCHSTAB/INTERVAL-COUNT+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Connection

`MC-484` records that a first-exit row with label `q` shortens a physical source interval by the factor `q`, while `MC-497`--`MC-500` price the quadratic repeated-residue endpoint branch by the number of distinct physical conductor starts available after that shortening. `MC-499` gives the per-block label-population ceiling and `MC-500` gives a Q-free ceiling in terms of the source location. The source **width** imposes a second Q-free gate that is independent of that location ceiling.

## Claim

Let the original source interval `I` have integer length `Y>=1`. Fix an odd prime conductor `p`, one repeated conductor residue `a mod p`, and a dyadic first-exit block

\[
Q\le q,r\le 2Q,
\qquad q\equiv r\equiv a\pmod p.
\tag{1}
\]

After the exact root reparameterizations `n=qm` and `n+h=rm`, let `J_q^+` and `J_r^-` be the corresponding shortened source intervals. For any selected nonempty pair overlap

\[
J_{q,r}=J_q^+\cap J_r^-,
\qquad L_{q,r}=|J_{q,r}|,
\tag{2}
\]

one has the elementary row-length bound

\[
\boxed{
L_{q,r}\le 1+\frac{Y}{Q}.
}
\tag{3}
\]

Now restrict to one dyadic overlap-length band as in `MC-498`,

\[
\frac H2\le L_{q,r}\le H,
\qquad H>2.
\tag{4}
\]

If the band is nonempty, `(3)` forces

\[
\boxed{
Q\le \frac{2Y}{H-2}.
}
\tag{5}
\]

Combining `(5)` with the exact repeated-residue start-support ceiling from `MC-499`,

\[
R_{\rm start}\le 2\left(1+\frac Qp\right),
\tag{6}
\]

gives the Q-free source-width ceiling

\[
\boxed{
R_{\rm start}
\le
2+\frac{4Y}{p(H-2)}.
}
\tag{7}
\]

The corrected `MC-498` maximal-second-moment tariff is

\[
T_{p,H}:=\frac pH\log^2(2H),
\qquad
\frac{|B|}{M}
\ll
\sqrt{\frac{T_{p,H}}{R_{\rm start}}}.
\tag{8}
\]

Therefore a necessary condition for this endpoint-start certificate to prove a fixed target saving `|B|/M<=delta` is

\[
\boxed{
T_{p,H}
\ll_\delta
2+\frac{4Y}{p(H-2)}.
}
\tag{9}
\]

Once `T_{p,H}` is larger than a fixed constant depending only on `delta`, `(9)` forces

\[
\boxed{
Y
\gg_\delta
p^2\frac{H-2}{H}\log^2(2H).
}
\tag{10}
\]

In particular, throughout every dyadic overlap band with `H>=4`,

\[
\boxed{
Y\gg_\delta p^2\log^2(2H)
}
\tag{11}
\]

is a necessary feasibility condition for the present exceptional-start dispersion certificate.

Thus increasing the dyadic first-exit scale cannot rescue a physically narrow source interval. The same `Q` that supplies more labels in one conductor residue also shortens every root row like `Y/Q`; the two effects cancel, leaving a conductor-square source-width barrier up to logarithms. This is a ceiling on the current endpoint certificate, not evidence that the true endpoint bias is large and not an estimate for `M(x)`.

## Derivation

### 1. Exact source shortening

For one root `n=qm`, membership in an integer source interval of length `Y` restricts `m` to an interval containing at most

\[
1+\frac Yq
\tag{12}
\]

integers. The translated root `n+h=rm` has the identical bound `1+Y/r`; translation changes the endpoints but not the width. Since `q,r>=Q`, every intersection in `(2)` therefore satisfies

\[
L_{q,r}
\le
\min\left(1+\frac Yq,1+\frac Yr\right)
\le1+\frac YQ,
\]

which is `(3)`. This is exactly the source-shortening mechanism already retained in the Buchstab first-exit representation of `MC-484`; no continuum interpolation or new coordinate is introduced.

If `(4)` contains even one overlap, then

\[
\frac H2\le1+\frac YQ.
\]

For `H>2`, rearrangement gives `(5)`.

### 2. Label growth and row shortening cancel

`MC-499` is independent of prime-distribution input: one residue class modulo `p` contains at most `1+Q/p` integer labels in `[Q,2Q]`, and every physical overlap start is one of the two endpoint images. Hence `(6)` holds even before restricting labels to primes or active first-exit rows.

Substituting `(5)` into `(6)` yields

\[
R_{\rm start}
\le
2\left(1+\frac{2Y}{p(H-2)}\right),
\]

which is `(7)`. The apparent freedom to increase `Q` has disappeared because the physical overlap band itself forbids `Q` from exceeding the scale `Y/H`.

Equivalently, the asymptotic `MC-499` population requirement

\[
Q\gg_\delta \frac{p^2}{H}\log^2(2H)
\tag{13}
\]

and the physical row-length compatibility `Q\ll Y/H` are simultaneously possible only when `Y\gg_\delta p^2\log^2(2H)`. Equation `(7)` is the constant-safe support formulation of the same cancellation.

### 3. Fixed-saving feasibility

`MC-498` gives `(8)` with an absolute implied constant. To force `|B|/M<=delta`, the certificate therefore needs

\[
R_{\rm start}\gg_\delta T_{p,H}.
\tag{14}
\]

Combining `(14)` with `(7)` proves `(9)`. When the tariff dominates the additive constant `2`, `(10)` follows. For `H>=4`, `(H-2)/H>=1/2`, giving `(11)`.

The small bands `2<H<4` carry only bounded overlap lengths and can be treated directly; no claim that the displayed logarithmic asymptotic is informative there is needed.

## Representation audit

The deduction retains every variable that is load-bearing for the endpoint certificate: the original physical source width `Y`, the actual first-exit scale `Q`, the conductor `p`, and the physical overlap length `H`. The passage from `(3)` to `(7)` removes `Q` only after intersecting two exact constraints that hold for the same dyadic block. It does not identify different source rows, average away a sign, or replace the hard first-exit support by a smoother model.

The result is therefore a genuine obstruction for the `MC-498` representation rather than a restatement of the tariff in new notation: it says that a source variable not present in `MC-499` alone — the pre-dilation physical interval width — limits how much repeated-residue start diversity can exist at a prescribed overlap length.

## Prior art and novelty boundary

No new theorem about Buchstab decompositions, arithmetic progressions, or interval lattice-point counts is claimed. The first-exit identity and the shortening of a source interval to length `Y/q+O(1)` are classical sieve bookkeeping; `MC-484` already audits Buchstab first exit against Halberstam--Richert and higher-dimensional sieve literature. The support estimate in `MC-499` is elementary residue-class counting plus Cauchy, while the analytic tariff in `MC-498` comes from the Fourier--Weil/Parseval estimate of `MC-497` and standard dyadic maximalization.

A targeted prior-art check found the expected classical Buchstab short-interval/sifting literature but no reason to reclassify the present statement as an external theorem. No novelty is claimed for any ingredient. The durable Mathia delta is their exact composition in the current physical source frame, exposing the Q-free source-width feasibility gate `(9)`--`(11)`.

## Boundaries and falsification tests

- **Endpoint-only certificate.** The result constrains the `MC-497`/`MC-498` exceptional-start method. Lower-prime pair-sieve phase selectivity and genuinely q-dependent signed or complex pre-aggregation coefficients remain outside it.
- **Method ceiling, not true bias.** Failure of `(9)` means only that this effective-start-support certificate cannot prove the requested saving on that band.
- **One repeated conductor residue.** Pooling different residues changes the conductor-phase geometry and is not covered by `(6)`.
- **One dyadic q-block and one dyadic overlap band.** Global reconstruction must still charge the number and weights of bands.
- **Physical source interval.** `Y` is the width before rowwise division by `q`; substituting a post-dilation or smoothed width would erase the exact cancellation behind `(5)`.
- **No prime-distribution assumption.** Restricting labels to primes or active first-exit rows only decreases `R_start`, so irregular prime availability cannot invalidate the obstruction.
- **No claim of sharp attainment.** Passing `(9)` does not show that enough active labels, distinct quotient starts, or flat reconstruction weights actually occur.
- **Independent of the MC-500 location gate.** A source may have very large location `Z_*` but small width `Y`, or conversely. The source-height gate of `MC-500` and the source-width gate here must both be checked.
- **No global Möbius conclusion.** There is no new estimate for `M(x)`, zero-free region, or RH.

## Consequence for the research line

The endpoint audit now has two cheap Q-free admission tests before any per-block coefficient work. `MC-500` asks whether the physical source **location** can support enough reciprocal-quotient start diversity; this finding asks whether the physical source **width** can simultaneously support overlaps long enough to exploit that diversity. In every material band with `H>=4`, failure of

\[
Y\gg_\delta p^2\log^2(2H)
\]

closes the present endpoint-dispersion certificate for every dyadic first-exit scale at once.

Only source regimes passing both Q-free gates should proceed to the `MC-499` per-block population test and then the exact `MC-498` winning-endpoint participation/fibre audit. The lower-prime hard-mask correlation and genuinely q-specific pre-aggregation routes remain independent live channels.

## Sources

- `MC-484`: exact Buchstab first exit and physical row shortening by `q`.
- `MC-497`: Fourier--Weil/Parseval start mean square.
- `MC-498`: corrected maximal endpoint-start tariff and effective-support certificate.
- `MC-499`: repeated-residue source-population ceiling.
- `MC-500`: complementary Q-free source-location ceiling.
