# MI-062 — The fixed-width Chebyshev remainder is an RH detector, but not a positive repair reserve

**Evidence level:** exact analytic synthesis from [WI-382](../../findings/WI-382-fixed-scale-chebyshev-one-sided-boundedness-is-rh-equivalent.md) and [WI-383](../../findings/WI-383-fixed-scale-remainder-has-an-unconditional-negative-recurrence-floor.md), refining the WI-380--WI-381 critical-translation reduction. Mellin/Landau arguments, explicit formulas and uniform almost periodicity are classical ingredients; the line-specific content is their specialization to the certified source-zero trial kernel.

For the exact cosine-convolution profile selected by WI-380/WI-381, let `R_L(x)` denote the renormalized fixed-log-width Chebyshev remainder after subtracting the polar `sqrt(x)` main term. Its transform `Q(z)` has no zeros for `Re z>0`. Consequently WI-382 proves the unusually sharp criterion

`RH <=> R_L(x)=O_L(1) <=> R_L is eventually bounded from either one side`,

and the same one-sided criterion holds on the actual lattice `x=k+1`. The source-perforated arithmetic-plus-polar layer differs from `R_L(k+1)` by only `O_L(1)`.

This makes one-sided control of the limiting remainder an RH-equivalent detector, but it still does not provide the positive margin needed by Gate II. WI-383 closes that stronger hope. If RH fails, `liminf R_L(k+1)=-infinity`; if RH holds, the absolutely convergent zero expansion is uniformly almost periodic with nonnegative spectral weights and

`liminf R_L(k+1)=-A_L<0`,

with near-floor returns relatively dense on logarithmic scale. Therefore `liminf R_L(k+1)<0` unconditionally.

The limiting fixed-width critical remainder cannot by itself pay a uniform positive gamma tariff. The direct-repair frontier has moved to the `k`-dependent order-one term that WI-382 leaves in the exact source-perforation/rooted construction, or to an exact graph/domain relation that excludes these source-zero trials before the old--old form is evaluated. Treating that `O_L(1)` correction as harmless would discard the only remaining repair carrier in this trial family.

**Boundary.** The exact negative floor is for the limiting unperforated profile. The fully perforated rooted layer is only known to differ by `O_L(1)`, which is the same order as both the floor and the required fixed tariff. No sign theorem for that correction is established, and no RH conclusion follows without proving one of the equivalent one-sided bounds.