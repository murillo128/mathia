# MI-047 — Mesoscopic continuation phase can miss the prime-pair parity sector

**Evidence level:** exact route-restriction synthesis from [PL-399](../../findings/PL-399-growing-gap-arithmetic-complexity-pays-a-reciprocal-continuation-tariff.md) and [PL-400](../../findings/PL-400-mesoscopic-transition-parity-quadrature.md), with the fixed-gap completion in PL-396--PL-397 and the prime-pair context of PL-075. The phase conclusion is for the same-sign real Hardy quadratic channel in the regime `d->infinity`, `d=o(r^(1/3))`; it does not classify other channels or the broader `d=o(r)` range.

PL-399 showed that at the pair saddle `T=2 pi r(r+d)` the larger incomplete-gamma continuation mode pays magnitude `1/(sqrt(2) pi d)` for a growing mesoscopic gap. PL-400 retains the phase discarded by that magnitude estimate. After the standard Hardy normalization, the coefficient multiplying the universal radial factor satisfies

`P_(r,d)=(1+o(1))/(sqrt(2) pi d) exp(-i pi(d^2+1)/2)`.

For integral `d`, this locks the leading real projection to parity. When `d` is even, the coefficient is purely imaginary to leading order and `Re P_(r,d)=o(1/d)`. When `d` is odd, the leading coefficient is real negative, `Re P_(r,d)=-(1+o(1))/(sqrt(2) pi d)`.

The most canonical prime-sensitive compensation then fails for a structural reason. A bulk von-Mangoldt pair correlation can live on even gaps, while for odd `d` one of `r,r+d` must be even and nonzero `Lambda` support forces that member to be a power of two; uniformly `sum_(r<=X)Lambda(r)Lambda(r+d)=O((log X)^2)` for odd `d`. Thus the arithmetic bulk occupies the gap parity where the leading real continuation tail is in quadrature, while the parity with a leading real tail has no linear-size prime-pair bulk.

This is stronger than the reciprocal `1/d` tariff alone. A candidate arithmetic weight must be matched not just to the size of a continuation channel but to its **complex phase after the actual projection**. In this channel, multiplying the PL-399 tail by `Lambda(r)Lambda(r+d)` and appealing to Hardy--Littlewood amplification cannot recover a leading real contribution.

The surviving routes are specific rather than generic: use a different completed channel whose canonical phase couples to even-gap arithmetic, enter the cubic-phase regime `d` near or above `r^(1/3)` where the parity lock can rotate, aggregate gaps while retaining uniform complex-phase control, or use another arithmetic weight whose mass occupies the real tail sector and survives matched controls. Each requires a new estimate; none follows from the magnitude calculation alone.

**Boundary.** The parity lock is proved only for the same-sign `C^2+conjugate(C)^2` channel and the phase-pinned regime `d=o(r^(1/3))`. Mixed `|C|^2`, archimedean cross-terms, higher moments or other observables can have different phases. The pointwise `o(1/d)` even-gap remainder cannot be summed over a growing gap family without a uniform estimate. A square-free matched control can populate odd gaps, so the phase split itself is not RH-specific.