# MI-057 — Away-from-five repair is an indefinite block supertrace, not a scalar spectral shortcut

**Evidence level:** exact source/representation synthesis from [PL-414](../../findings/PL-414-away-from-5-residue-variance-projection.md), [PL-415](../../findings/PL-415-away-from-5-dirichlet-character-variance-supertrace.md), [PL-416](../../findings/PL-416-mod5-virtual-artin-supertrace-scalarization-obstruction.md), and [PL-417](../../findings/PL-417-mod5-pontryagin-selfadjointness-nonreal-spectrum-obstruction.md), refining the actual-prime transfer boundary left by MI-056.

The source-realized `p=5` de-aliasing has exact additive and multiplicative finite representations. PL-414 writes the local repair as five rational-frequency variance sectors. PL-415 diagonalizes the same factor on the unit group modulo `5`; up to explicit power-of-5 terms, the actual-prime bridge depends only on one signed combination of principal, quadratic and quartic Dirichlet-character variance channels. Componentwise bounds are therefore sufficient but not intrinsic, and can erase cancellation that the exact source bridge preserves.

PL-416 shows that this signed combination cannot be faithfully compressed into one scalar Artin or Dirichlet `L`-function at quadratic order. After multiplying by `15`, the channel metric is

`D=diag(15,-1,-1,-1)`.

The corresponding local source is the virtual character `15 chi_0-chi_2-chi_4-bar(chi_4)`, and there is a natural scalar quotient `(1-5^(-s))^15 zeta(s)^16/zeta_Q(zeta_5)(s)`. But squaring a single scalar logarithmic-derivative channel always produces a rank-one positive semidefinite form `cc^*`, whereas the required variance is a full-rank form of signature `(1,3)`. Scalarization therefore preserves the first-order virtual character while destroying the exact second-order observable.

PL-417 tests the most economical way to retain that information. The metric factors canonically as `D=R J R` with `J=diag(1,-1,-1,-1)`, so the source supertrace has a natural Pontryagin-space realization. However `J`-selfadjointness is weaker than Hilbert selfadjointness in precisely the dangerous way: an explicit `2 x 2` `J`-selfadjoint block has spectrum `{i,-i}`, and it embeds into the actual `(1,3)` signature. Indefinite selfadjointness alone therefore cannot localize a zero parameter to the critical line.

The reusable lesson is that **preserving a signed quadratic source statistic requires block information, and preserving it in an indefinite metric does not automatically restore spectral reality**. A scalar determinant/quotient can lose the quadratic statistic; a Krein/Pontryagin lift can retain it while still allowing nonreal conjugate spectrum. The missing theorem is arithmetic, not representational.

For the live bridge, one must either estimate the signed character-variance supertrace directly, or find block/explicit-formula structure that produces the required PL-407 power saving without importing auxiliary GRH. An operator route must additionally prove a reality-forcing property stronger than `J`-selfadjointness—such as an arithmetic `J`-nonnegativity, a justified positive intertwining metric, or another coercive invariant that excludes every nonreal block while retaining the signed source information.

**Boundary.** PL-416 does not prove that the signed supertrace lacks arithmetic cancellation; it proves only that one scalar `L`-product does not represent its quadratic form. PL-417 does not rule out Krein/Pontryagin methods; it rules out automatic spectral localization from indefinite selfadjointness alone. The missing power-saving estimate and any reality-forcing arithmetic property remain unproved.
