# MI-024 — Arithmetic-image blind exclusion is directional leverage, and low-conductor shell richness does not supply it

**Evidence level:** exact variational reduction/certificate from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md), sharpened by the exact separated-prime matched control [MC-282](../../findings/MC-282-separated-simplex-leverage-failure.md) and the stretched-exponential shell-pattern obstruction [MC-284](../../findings/MC-284-page-siegel-stretched-exponential-shell-legendre-universality.md). No theorem is claimed that the required rank/leverage alternative holds for the actual full tight-shell feature matrix.

Let `A` be the degree-`m` feature matrix of the actual fixed-weight arithmetic shell and let `v=1_Z` be the virtual blind feature row. Instead of constructing a scalar decoder that is uniformly sharp on the full Boolean cube, optimize only on the arithmetic image:

`C = inf_(v^* a=1) ||A a||_2^2`.

Every blind row contributes exactly one to this energy, so the blind count satisfies `A_y(t)<=C`; in particular `C<1` is an exact blind-exclusion certificate. The dual quantity is the minimum signed shell-synthesis cost

`Lambda = inf{ ||c||_2^2 : A^* c = v }`,

with `C=1/Lambda`. If `v` is outside `ran(A^*)`, then a kernel vector separates the virtual endpoint exactly. If `v` lies in the row span, blindness is excluded once `Lambda>1`.

MC-282 shows that **even exact absence of blindness does not force this sufficient certificate to succeed** once tight localization is removed. A separated-prime realization of the simplex/Hamming Legendre pattern has no blind pair at all, yet at the same low source depth `m=t+1=3` its synthesis cost is

`Lambda_(3,d)^sep = Z_3(d)/((2^(d-1)-1)(2^d-Z_3(d)))`,

which is already `13/45<1` at `d=5` and tends to zero like `d^3/(3*4^d)`. The virtual endpoint can therefore be synthesized extremely cheaply from genuinely arithmetic, completely nonblind rows.

MC-284 adds a different obstruction **inside the localized shell itself**. For any finite lower-prime coordinate set `U` whose effective conductor

`Q(U)=4 product_(p in U) p`

satisfies `Q(U)<=exp(b sqrt(log y))`, every prescribed Legendre sign cell occurs among primes `r in (y,2y]`, uniformly with at least `y exp(-B sqrt(log y))` representatives. The fixed-weight product image is therefore the full Boolean cube on `U` throughout this conductor range at the live weight `t~log log y`. Page's theorem leaves at most one exceptional Fourier mode, and Siegel's lower bound prevents that mode from emptying a cell when the conductor constant is sufficiently small.

Consequently a Christoffel certificate with empirical energy below one cannot be supported entirely on such a coordinate set: its effective coordinate conductor must satisfy

`Q(a)>exp(b sqrt(log y))`

eventually. Tight localization by itself does not make moderate-conductor coordinates directionally special; on those coordinates the arithmetic image remains Boolean-complete. The certificate must import genuinely higher-conductor information, exploit interaction with coordinates beyond this range, or use a different source-native operator/inverse mechanism.

This sharpens the interpretation of the variational certificate. Favorable leverage is not a generic consequence of Legendre provenance, reciprocity, a feature surplus, low-degree moment geometry, shell localization, or even the truth of the desired no-blind conclusion. It is a **stronger directional property** that must be forced in a part of the arithmetic image not already saturated by the Page--Siegel pattern-realization mechanism.

Generic coefficient-uniform large-sieve/operator-norm control still cannot cross the threshold: the row norm forces any uniform bound `||Aa||_2^2<=D||a||_2^2` to have `D>=Z`, while the dual argument yields only `Lambda>=Z/D<=1`. MC-282 additionally rules out inferring `Lambda>1` from abstract nonblindness, and MC-284 rules out obtaining it merely by restricting to any stretched-exponential-conductor coordinate shadow of the actual shell.

The surviving theorem is consequently quantitative and source-specific: either prove that the full localized feature family forces the virtual endpoint out of the row span or makes it expensive to synthesize **because of information beyond the Page--Siegel-complete conductor window**, or construct a source-native arithmetic/operator inverse. Any proposed low-depth Christoffel separator should first expose which coordinates push its effective conductor past `exp(b sqrt(log y))`; otherwise MC-284 already embeds an all-positive shell cell on every coordinate it uses.

**Boundary.** `Lambda<=1` does not imply a blind row; MC-282 is an explicit counterexample. MC-284 gives a necessary support-complexity condition for the Christoffel route, not a proof that high-conductor support yields favorable leverage. Its constants inherit the ineffective Siegel input, and the result does not improve `M(X)` or exclude the blind row directly. The actual full tight-shell matrix may still have additional collective structure outside every bounded-conductor projection.