# MI-007 — Bow variance is an absolute endpoint-charge problem after cubic-scale localization

**Evidence level:** exact Fejer-minus-completion identity, Selberg-calibrated localization, all-interval source controls, and matched endpoint-charge obstruction through ANF-166

## Core intuition

The bow endpoint problem is no longer primarily about finding stronger relative cancellation on long intervals. The strongest current source estimates already push dangerous completion beyond every fixed polylogarithmic enlargement of the cubic total-variation scale, yet a deterministic matched control shows that all such increment bounds can coexist with target-sized endpoint energy if the absolute primitive is charged once and then remains nearly constant.

The decisive currency is therefore the size and persistence of the **absolute endpoint primitive**, not the number of logarithms saved in later interval increments.

## Strongest justified principle

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-158--ANF-165 progressively sharpen the source localization and show that, in the current subcritical regime, target-sized completion cannot occur inside any fixed polylogarithmic multiple of `R_TV=(X K log X)^(1/3)` under the available all-interval decorrelation and Cramer--Granville normalization.

ANF-166 then proves the missing information boundary. It constructs source-budget-matched data whose long-interval discrepancy is stronger than every fixed logarithmic saving above an activation length `H_0`, but whose prefix/suffix primitive reaches `asymp sqrt(X log X)` and stays there for a macroscopic fraction of the endpoint horizon. The resulting endpoint square remains a fixed fraction of `XK log X`.

Consequently an estimate `|sum_I b_n| <= rho_X |I|` for `|I|>=H_0` cannot by itself imply negligible endpoint completion unless `rho_X H_0=o(sqrt(X log X))`. For the present `H_0=X^(5/8+eta)`, this requires `rho_X=o(X^(-1/8-eta)sqrt(log X))`: a true power-scale gain. Arbitrary fixed powers of `1/log X` are polynomially insufficient.

## Program consequence

Target one of the currencies that the matched control cannot fake: an absolute prefix/suffix anchor below `sqrt(X log X)`, cancellation beginning essentially at square-root physical length, a direct square-function bound for the endpoint primitive, or a source-faithful prime/rough constraint that rules out charge-and-hold behavior.

Do not treat another logarithmic improvement of all-interval discrepancy as progress unless it crosses the exact product gate `rho_X H_0=o(sqrt(X log X))`.

## Counterevidence / boundary

ANF-166 is synthetic and is not asserted to equal the actual demodulated prime residual. It therefore does not prove the arithmetic endpoint square is large. It proves only that the aggregate source information extracted through ANF-165 is insufficient. A genuinely prime-specific support, sign, factorization, or multiscale law may forbid persistent charge even when generic interval bounds do not.

The positive Fejer term may also dominate completion through a coupled inequality not visible from separate discrepancy estimates.

## Epistemic status

**Exact information boundary: current long-interval source controls, even strengthened beyond every fixed logarithmic saving, do not control bow completion unless they also force an absolute-prefix gain; the surviving theorem must rule out persistent endpoint charge in the actual arithmetic source.**

## Falsification criterion

Show that the ANF-166 matched control violates one of the source hypotheses actually used in the endpoint theorem, or prove from those same hypotheses alone that `rho_X H_0=o(sqrt(X log X))` or an equivalent primitive-square estimate already follows.
