# MI-039 — Periodic scale switching can create a supercritical blind mode from individually harmless root filters

**Evidence level:** exact synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md), interpreted against the fixed-family dichotomy of FD-210--FD-211 and the common-depth inversion of FD-207--FD-209.

Let `Delta_A(n)=A(2n)-A(n)` for a bounded source and observe only one dyadic root filter at each scale. FD-212 takes the periodic depth schedule

`q_j = 0,3,3,0,3,3,...`

on `n=2^j`, so the endpoint sequence satisfies the switched recurrence

`(E-I)^(q_j+1) a_j = 0`.

Each local annihilator is spectrally harmless by itself: the only characteristic root of `(z-1)` and `(z-1)^4` is `1`. The fixed finite family `{1,(z-1)^3}` acting on `Delta_A` also has gcd `1`, so simultaneous pointwise control of both filters would be destination-complete by FD-211. But diagonal switching reveals only one member at each scale, and the period-three monodromy has the exact multiplier

`lambda=-(7+3sqrt(5))/2=-phi^4`.

Its per-dyadic-step modulus is

`rho=|lambda|^(1/3)=phi^(4/3)`,

with `sqrt(2)<rho<2`. Thus the nonautonomous recurrence has a physical super-square-root Floquet mode even though none of its instantaneous filters has an annular root.

The mode is not merely an unconstrained sequence-space artifact. Because `rho<2`, FD-212 embeds its dyadic endpoint values exactly into the summatory function of a real bounded source by choosing blockwise constant increments. Along the dyadic ray the switched observations vanish identically while

`|A(2^(3m))| asymp (2^(3m))^alpha`, `alpha=log_2 rho>1/2`.

The escape also does not pay the growing-depth random tariff: only depths `0` and `3` occur, so the squarefree-Rademacher second moment remains `Theta(H)` up to a constant Delannoy factor. The obstruction is therefore **scale-selection coherence**, not large degree or an expensive random benchmark.

This refines the fixed-filter dichotomy. A fixed finite family is classified by its common characteristic roots, but a diagonal schedule is a nonautonomous system whose relevant spectrum belongs to the ordered product of scale-dependent transfer maps. Testing each filter independently, or taking the gcd of the set of filters while ignoring which one is observed at which scale, loses the switching multiplier.

The remaining all-integer question is stricter than the dyadic-ray construction. FD-212 does not build a multiplicative source and does not annihilate the diagonal sensor for every integer `n`. Different binary rays are coupled because they are partial sums of one physical source. The decisive unresolved issue is whether this **cross-ray source coherence** forces every all-integer switched schedule back into the square-root-complete regime, or whether a bounded source can retain a supercritical switched mode while satisfying the selected filter on a sufficiently rich set of scales.

**Boundary.** The exact obstruction is a sparse dyadic-ray bounded-source countermodel. It does not disprove an all-integer diagonal RH criterion for Möbius, establish a joint/constrained spectral-radius classification for arbitrary schedules, or show that Möbius can realize the Floquet mode. Its durable content is narrower: bounded-depth scale variation alone already escapes every proof that applies the fixed-filter dichotomy independently at each scale.
