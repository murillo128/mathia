# MI-001 — Nyman target geometry remembers absolute scale, and the remaining coercivity problem is scale-coupled source visibility

**Evidence level:** exact augmented-Gram, semigroup, normal-equation, multichannel-saturation, and scale-coupled visibility results through NB-015

## Core intuition

The Nyman approximation problem is not determined by generator geometry alone: the fixed target supplies an absolute-scale coordinate that generic semigroup self-similarity can lose. The actual best residual is much more rigid. Its projection normal equations force finite target mismatch early, but converting that mismatch into stronger approximation-rate coercivity has now reached a precise saturation boundary.

Neither enlarging the linear normal-equation family nor taking arbitrary positive quadratic combinations creates a new asymptotic conversion. The surviving variable is **how much of the source-forced semigroup defect lands in the genuinely new section as the probe depth grows with the section**, relative to the compressed frame cost there.

## Strongest justified principle

NB-001--NB-009 separate target-aware residual structure from generic Gram/semigroup aliases and show that the actual best residual has polynomially early witnesses. NB-010--NB-012 aggregate that signal: prime normal equations force finite defect, while Ramanujan geometry proves the logarithmic linear amplification order is optimal.

NB-013 polarizes this ceiling. Every finite multichannel family and every positive-semidefinite quadratic channel form obey the same target-load domination, so positive cross-channel aggregation cannot beat the one-channel asymptotic order.

NB-014 gives the exact enrichment bridge. The visible defect is bounded by the compressed frame on `V_{MN}\ominus V_N` times the actual distance decrement. It also shows that the **full** frame norm equals `M-1` in the lcm-overlap regime and that a positive fixed-scale visibility fraction at arbitrarily large fixed depths would already force the limiting Nyman distance to zero.

NB-015 moves to the genuinely open diagonal regime. If the limiting residual is nonzero, then along every admissible nested path `N_{k+1}=M_kN_k` the source-visible fractions must obey

`sum_k rho_{N_k,M_k} log M_k / beta_{N_k,M_k} < infinity`,

where `beta` is the compressed new-section frame norm. Divergence of a source-controlled lower/upper comparison is therefore an explicit RH-closure criterion.

## Program consequence

The next theorem should target the scale-coupled pair `(rho_{N,M}, beta_{N,M})` on the actual residual and the genuinely new quotient section. The goal is not a generic frame improvement but a source-specific accumulated visibility estimate strong enough to violate the NB-015 summability budget along one controlled growth path.

This makes the desired coercivity quantitative without pretending it is modest: any proposed lower bound should be checked immediately against whether its accumulated strength is already closure-equivalent.

## Counterevidence / boundary

NB-015 supplies a conditional closure criterion, not the missing visibility lower bound. The exact full-frame norm does not determine the compressed new-section norm, and sparse visibility at very rapidly growing scales may remain summable. Nonlinear or differently normed certificates outside the positive normal-equation closure also remain open.

## Epistemic status

**Exact target-information and amplification boundaries plus an exact scale-coupled visibility budget; no improved Nyman distance bound or RH proof is established.**

## Falsification criterion

Produce a positive quadratic normal-equation lift beating NB-013, invalidate the NB-014 enrichment identity/frame saturation, or construct a nonzero limiting residual violating NB-015's summability law. A positive continuation should instead derive source-specific visibility/frame estimates whose accumulated budget forces `d_infinity=0`.