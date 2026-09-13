# MI-037 — Support height and time height form a two-resource conditioning window

**Evidence level:** supported by [AF-324](../../findings/AF-324-bounded-prime-height-quantifies-fixed-time-phase-covering.md) and [AF-325](../../findings/AF-325-bounded-support-height-uniformizes-prime-antipodal-conditioning.md), building on AF-322--AF-323. No exact middle-singular incidence theorem or sharp covering asymptotic is claimed.

The support parameter missing from the AF-322/AF-323 quantifier split can be priced explicitly. Fix `m` and `tau != 0`, and let `rho_(m,tau)(H)` be the covering radius in `(S^1)^m` of distinct-prime phase tuples with every prime at most `H`. AF-324 proves

`pi/pi(H) <= rho_(m,tau)(H) <<_(m,tau) H^(-19/40)`.

Thus bounding support height does not restore a fixed phase-space gap. It gives a finite-resolution net whose mesh still shrinks polynomially. In the eight-point singular problem, supports below `H` approach the bad set `s_1=e_4=s_3=0` at `O_tau(H^(-19/40))`; any Lipschitz finite-phase compression inherits the same upper filling scale.

AF-325 supplies the opposite inequality in the resource direction relevant to conditioning. For every eight-prime support `P` with `max P<=H` and `|t|>=1`, its distance from the four-antipodal-pair locus satisfies

`delta_P(t) >= exp[-C (log H)^2 log(e+|t| log H)]`.

On a hypothetical exact middle-singular hit, the same joint `H,t` envelope transfers by a support-independent Łojasiewicz inequality to `|s_3|`. At fixed nonzero `tau`, if `Delta_tau(H)` is the smallest antipodal distance among supports below `H`, the two results give

`exp[-C (log H)^2 log(e+|tau| log H)] <= Delta_tau(H) <<_tau H^(-19/40)`.

The important object is therefore not a support-independent condition number but a **two-resource modulus**. Time recurrence degrades conditioning on each fixed support; increasing support height enlarges the admissible family and lets actual prime configurations approximate ambient collision geometry. The exact prime labels contain more information than the scalar height `H`, but retaining only `H` is already enough to make the degeneration quantitatively visible and uniform.

This sharpens the fidelity question. A downstream theorem that varies supports must state which source-height/provenance resource it retains and compare the modulus it consumes with the joint `H,t` window above. Merely declaring each support finite is not a stability statement, while AF-323's unrestricted density does not erase the useful finite-height lower envelope supplied by AF-325.

**Boundary.** AF-324 is a near-incidence theorem, not exact incidence or equidistribution. AF-325 does not decide whether `s_1=e_4=0` is ever attained by an eight-prime orbit. The lower and upper `H` scales are far apart, so no sharp asymptotic for `Delta_tau(H)` is known.