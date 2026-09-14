# MI-024 — Arithmetic-image blind exclusion is directional leverage, and localization must control that direction

**Evidence level:** exact variational reduction/certificate from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md), sharpened by the exact separated-prime matched control [MC-282](../../findings/MC-282-separated-simplex-leverage-failure.md). No theorem is claimed that the required rank/leverage alternative holds for the actual tight arithmetic shell matrix.

Let `A` be the degree-`m` feature matrix of the actual fixed-weight arithmetic shell and let `v=1_Z` be the virtual blind feature row. Instead of constructing a scalar decoder that is uniformly sharp on the full Boolean cube, optimize only on the arithmetic image:

`C = inf_(v^* a=1) ||A a||_2^2`.

Every blind row contributes exactly one to this energy, so the blind count satisfies `A_y(t)<=C`; in particular `C<1` is an exact blind-exclusion certificate. The dual quantity is the minimum signed shell-synthesis cost

`Lambda = inf{ ||c||_2^2 : A^* c = v }`,

with `C=1/Lambda`. If `v` is outside `ran(A^*)`, then a kernel vector separates the virtual endpoint exactly. If `v` lies in the row span, blindness is excluded once `Lambda>1`.

MC-282 shows that **even exact absence of blindness does not force this sufficient certificate to succeed** once tight localization is removed. A separated-prime realization of the simplex/Hamming Legendre pattern has no blind pair at all, yet at the same low source depth `m=t+1=3` its synthesis cost is

`Lambda_(3,d)^sep = Z_3(d)/((2^(d-1)-1)(2^d-Z_3(d)))`,

which is already `13/45<1` at `d=5` and tends to zero like `d^3/(3*4^d)`. The virtual endpoint can therefore be synthesized extremely cheaply from genuinely arithmetic, completely nonblind rows.

This sharpens the interpretation of the certificate. Favorable leverage is not a generic consequence of Legendre provenance, reciprocity, a feature surplus, low-degree moment geometry, or even the truth of the desired no-blind conclusion. It is a **stronger directional property** that must be forced by the specific source/target coupling of the live shell.

Generic coefficient-uniform large-sieve/operator-norm control still cannot cross the threshold: the row norm forces any uniform bound `||Aa||_2^2<=D||a||_2^2` to have `D>=Z`, while the dual argument yields only `Lambda>=Z/D<=1`. MC-282 additionally rules out the hope that one could justify `Lambda>1` merely from abstract nonblindness of the arithmetic image.

The surviving theorem is consequently quantitative prime localization. A proof must use a property that the separated simplex realization cannot preserve—most naturally that all target primes occupy the same moving shell `(y,2y]`, or another comparably strong coupling—to show that the virtual endpoint leaves the row span or becomes expensive to synthesize. A source-native arithmetic/operator inverse remains a qualitatively different escape.

**Boundary.** `Lambda<=1` does not imply a blind row; MC-282 is an explicit counterexample. Conversely the separated control says nothing about the actual tight shell. The certificate remains sufficient and potentially useful, but any proof of it must exploit localization-specific arithmetic rather than generic matrix geometry.