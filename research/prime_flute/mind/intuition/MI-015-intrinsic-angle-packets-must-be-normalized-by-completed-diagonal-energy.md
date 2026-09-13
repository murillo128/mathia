# MI-015 — Completed packet locality is a relative pant-resolvent problem

**Evidence level:** exact finite-section algebra from [PF-329](../../findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md)--[PF-332](../../findings/PF-332-completed-square-root-defect-is-a-resolvent-dressed-pant-insertion.md). No uniform locality estimate, endpoint Hilbert--Schmidt bound, or infinite-section passage is claimed.

Let `A_0=Q+Lambda_LL` be the completed low energy and

`F=A_0^(1/2)Q^(-1/2)`.

PF-329--PF-330 show that final completed normalization does not damp the critical packet family. It rotates a tight frame and preserves the exact total-energy packet average. PF-331 then shows that the polar unitary extracted from `F` has a uniform gap and cannot amplify translation/localizer defects already controlled for `F`.

PF-332 identifies the right relative object. Put `G=F-I`. On every finite section,

`G=(1/pi) int_0^infty mu^(1/2)(A_0+mu)^(-1) Lambda_LL (Q+mu)^(-1)Q^(-1/2) dmu`,

and equivalently

`A_0^(1/2)G+GQ^(1/2)=Lambda_LL Q^(-1/2)`.

The baseline seam square-root nonlocality therefore cancels exactly. Every nonidentity contribution contains one explicit pant/core insertion. For physical translations `tau_t`, the seam block commutes with `tau_t`, so

`[F,tau_t]=(1/pi) int mu^(1/2)(A_0+mu)^(-1)[Lambda_LL,tau_t](A_0+mu)^(-1)Q^(-1/2) dmu`.

This changes the endpoint currency again. The task is not to prove locality of two unrelated square roots. It is to control a **relative resolvent transfer sourced by the actual pant/core translation defect**, with enough uniformity to compensate the potentially large `Q^(-1/2)` weight and the finite-boundary/escaping-boundary degeneration.

The trivial-pant control is exact: `Lambda_LL=0` gives `F=I`, regardless of how nonlocal `Q^(1/2)` or `Q^(-1/2)` look separately. Any proof that estimates those factors independently risks manufacturing a false locality obstruction by destroying the relative cancellation.

For spatial cutoffs the formula is less clean because the cutoff need not commute with `Q`, but `[F,chi]=[G,chi]` still keeps every seam commutator inside a term already carrying the pant insertion. The same relative viewpoint should therefore govern both translation and off-diagonal leakage estimates.

**Boundary.** PF-332 is an identity, not a decay theorem. The resolvents may spread mass, `Q^(-1/2)` may be singular in the degenerating scale, and cutoffs are harder than translations. The packet obstruction reaches the final angle only after these relative estimates are uniform across the terminal regimes.
