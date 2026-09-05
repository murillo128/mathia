# VIS-034 — Farey low-band suppression factors into total-discrepancy suppression and spectral reallocation

## Claim

Use the reflection-symmetric Farey/Dirichlet notation of `VIS-032`. For a fixed ordered discrepancy path `D`, let

`E_q(D)=sum_(r=1)^q d_(2r)^2`

be the first-`q` even-mode energy, and let

`E_tot(D)=sum_(r=1)^(M-1) d_(2r)^2`

be the complete even-mode energy. By Farey reflection, the odd modes vanish, so `E_tot(D)` is the full squared discrepancy energy.

For the reflection-preserving same-gap null, write

`mu_q=E_sym[E_q]`

and

`mu_tot=E_sym[E_tot]`.

Define three dimensionless quantities:

`Q_q = E_q/mu_q`,

`A = E_tot/mu_tot`,

and

`S_q = (E_q/E_tot)/(mu_q/mu_tot)`

whenever `E_tot>0`.

Then the first-null-normalized band suppression from `VIS-032` factors **exactly** as

`Q_q = A S_q`.

The factors have distinct meanings. `A` measures how much the **total** discrepancy energy is suppressed relative to the reflection-preserving same-gap null. `S_q` measures how the surviving discrepancy energy is **reallocated across the spectrum** relative to the null's expected allocation. Therefore a small `Q_q` alone is not evidence for a specifically low-frequency mechanism: it conflates global discrepancy suppression with spectral redistribution.

If

`F_actual(q)=E_q/E_tot`

and `F_null(q)=mu_q/mu_tot`, then

`S_q=F_actual(q)/F_null(q)`.

By `VIS-032`, whenever `q->infinity` and `q=o(N)`, `F_null(q)->1`. Hence in that regime

`S_q = F_actual(q) + o(1)`

uniformly in the trivial bound `0<=F_actual<=1`. For the endpoint-safe Farey bands with `q->infinity`, `q=o(n)`, the null expects asymptotically all Green energy in the band, so any persistent `S_q<1` is a genuine **spectral-allocation** effect rather than a restatement of the total discrepancy norm.

**Evidence/status:** `EXACT-DERIVED NORMALIZATION FACTORIZATION + NEGATIVE INTERPRETIVE CONTROL + FINITE DIAGNOSTIC + NO-NOVELTY-CLAIM`.

No limiting law for `A`, `S_q`, or `Q_q`, no stronger Franel–Landau criterion, and no RH implication is claimed.

## Exact factorization

The identity is purely algebraic but removes an important confound. Starting from the definitions,

`A S_q`
` = (E_tot/mu_tot) [(E_q/E_tot)/(mu_q/mu_tot)]`
` = E_q/mu_q`
` = Q_q`.

Thus changing the cutoff `q` changes only the spectral factor `S_q`; the global amplitude factor `A` is common to every band for the same Farey order and null ensemble.

Equivalently,

`Q_(q1)/Q_(q2)=S_(q1)/S_(q2)`

for any two valid cutoffs at the same order. Ratios of `Q_q` across bands automatically cancel the total-discrepancy suppression. Conversely, comparing a single `Q_q` with one does not say how much of the deviation comes from the scalar discrepancy norm and how much comes from where that energy sits spectrally.

This distinction matters especially here because the same-gap null was introduced precisely to test **ordering**. Ordering can reduce the total size of a cumulative discrepancy path and can also move the remaining energy between Dirichlet scales. Those are different effects and should not be counted twice as one visual mechanism.

## Sublinear-band consequence

`VIS-032` proves

`F_null(q) -> 1`

for every diverging sublinear cutoff `q=o(N)`. Therefore

`S_q-F_actual(q)`
` = F_actual(q)(1/F_null(q)-1)`
` -> 0`.

For Farey order `n`, the endpoint-safe regime from `VIS-031` uses the stronger restriction `q=o(n)`, which automatically implies `q=o(N)` because `N=Theta(n^2)`. In that regime the two control statements now separate cleanly:

- fixed-`nx` endpoint layers contribute asymptotically no `n`-scaled band energy by `VIS-031`;
- the reflection-preserving same-gap null allocates asymptotically all of its expected discrepancy energy to the band by `VIS-032`;
- `A` records the scalar/global suppression of the complete Farey path;
- `S_q` records the additional redistribution of that already-suppressed path away from the null's low-frequency Green profile.

A specifically spectral claim must therefore survive after conditioning on or dividing out `A`.

## Finite diagnostic from the existing Farey table

The finite values in `VIS-032` already show that both factors are active. Reconstructing `A=Q_q F_null/F_actual` from the rounded table gives the same value from the two pre-registered cutoffs up to rounding, as the exact identity requires.

| `n` | `A` | `S_sqrt` for `q=floor(sqrt(n))` | `S_2/3` for `q=floor(n^(2/3))` |
| ---: | ---: | ---: | ---: |
| 100 | `0.04698` | `0.2034` | `0.3963` |
| 200 | `0.02432` | `0.2488` | `0.4123` |
| 400 | `0.01023` | `0.1586` | `0.3248` |
| 800 | `0.00455` | `0.1071` | `0.2638` |
| 1200 | `~0.00284` | `0.0813` | `0.2380` |

At `n=1200`, for example, the reported `Q_q` values `2.31e-4` and `6.77e-4` are not one undifferentiated suppression. They are approximately

`2.84e-3 x 0.0813`

and

`2.84e-3 x 0.2380`,

respectively. The common factor is the total discrepancy suppression; the cutoff-dependent factor is the spectral reallocation. The numbers are finite diagnostics only. No monotonicity or asymptotic exponent is inferred from them.

The table also shows why the distinction is not cosmetic. At these orders the global factor `A` is already much smaller than one, while `S_q` supplies an additional but numerically separate depletion of the low sublinear band. The two-band difference belongs entirely to `S_q`, not to `A`.

## Prior art and novelty assessment

The underlying ingredients are already classical or previously audited in this line. The Farey discrepancy literature and García's fixed-gap permutation study are anchored in `SOURCES.md`; `VIS-027` and `VIS-032` supply the exact reflection-conditioned Dirichlet/Green null used here. A targeted structure-based check found the expected Farey discrepancy and gap-permutation literature, but this finding does not require or claim a new external theorem.

The factorization `Q_q=A S_q` is elementary normalization algebra and is **not** claimed as a new mathematical identity. Its durable value is epistemic and experimental: it prevents a very small first-null-normalized spectral statistic from being interpreted as a new low-mode phenomenon when most of its suppression may already be present in the total scalar discrepancy norm.

## Boundary conditions and falsification

`A` and `S_q` use null **expectations**, not random-null realizations. In particular, `S_q` is not asserted to have null expectation one; ratios of random quadratic energies would require a distributional analysis that `VIS-032` explicitly leaves open.

The factorization does not explain why `A` is small, why `S_q` is below one in the finite Farey data, or whether either quantity has a stable limit. A stronger local-order, denominator, or mediant-preserving null can change both `mu_tot` and the expected spectral allocation, so both factors must be recomputed for that null rather than inherited from the same-gap ensemble.

The result also does not make `A` mathematically uninteresting. It isolates `A` as the global ordering/discrepancy channel. What it forbids is counting the same global suppression again as specifically spectral evidence through `Q_q`.

A material falsification would require a mismatch in the definitions of the actual or null energies. The algebraic factorization itself is exact wherever `E_tot>0` and the null expectations are nonzero.

## Research consequence

The cross-line Farey clue should no longer use `Q_q` alone as the primary diagnostic. For each pre-registered band and each progressively stronger matched null, report the pair

`(A, S_q)`

with `Q_q=A S_q` retained as a derived combined quantity.

A genuinely low-band visual mechanism requires stable suppression in `S_q` after the total-discrepancy factor `A` has been separated. If only `A` survives under stronger controls while `S_q` returns to one, the spectral branch has collapsed to a global discrepancy-ordering effect. If `S_q` remains nontrivial, the next question is where that spectral reallocation is encoded: bounded local gap order, denominator/mediant structure, long-range order, or another interior channel.