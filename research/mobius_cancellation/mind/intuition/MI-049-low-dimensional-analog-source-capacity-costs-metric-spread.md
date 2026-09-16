# MI-049 — Low-dimensional analog source capacity costs metric spread

**Evidence level:** exact finite-endpoint synthesis from [MC-340](../../findings/MC-340-global-transcript-information-capacity.md) and [MC-341](../../findings/MC-341-analog-transcript-spread-capacity.md).

MC-340 makes joint source information the invariant capacity currency for reciprocal-endpoint dephasing. At bounded normalized coefficient energy, any constant improvement over full dephasing error requires `I(X;Y)=Omega(R)` for the complete source vector `X` and complete admitted observation `Y`. Near exact unit-energy matched filtering, the observation must carry almost the full source entropy.

A small number of real coordinates does not contradict that statement: one noiseless real number can encode exponentially many discrete states. MC-341 identifies the missing geometric price once the transcript comes with a source-natural Euclidean metric. For a deterministic transcript `T in R^d`, let `D_T` be the diameter of its support, `Delta_T` the minimum separation of distinct support states, and `spr(T)=D_T/Delta_T`. If the transcript must support the information required by MC-340, ordinary Euclidean packing gives

`spr(T) >= (1/2)(exp(L_R/d)-1)`,

where `L_R=Theta(R)` for fixed nontrivial dephasing at bounded energy.

Thus **analog compression trades dimension for precision/conditioning rather than removing the information bill**. Fixed metric dimension requires exponentially fine relative separation; polynomial spread requires at least `Omega(R/log R)` real dimensions. At exact matched filtering the transcript must be injective on essentially `2^R` source states, giving the sharper `2^(R/d)` scale.

The reusable lesson is deliberately metric-relative. Syntactic dimension is meaningless until the analytic construction supplies a canonical norm, noise scale, finite-precision model or stability notion. Once such a metric is intrinsic, however, hiding linear source information in a few analog coordinates forces a correspondingly large distinguishability budget.

The live arithmetic question is therefore to identify the actual Möbius transcript and its canonical metric, then prove either that its source information is sublinear at bounded energy or that any linear-information encoding has superpolynomial conditioning/precision cost at the relevant scale.

**Boundary.** The spread bound is classical packing composed with the MC-340 information theorem. Large spread is not itself a contradiction, and an arbitrary invertible reparameterization can change Euclidean spread. No estimate for `M(x)` follows until a source-natural metric and a genuine Möbius architecture connect this finite endpoint obstruction to arithmetic cancellation.