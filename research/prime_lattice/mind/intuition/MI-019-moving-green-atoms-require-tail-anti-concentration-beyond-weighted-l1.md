# MI-019 — Moving Green atoms need anti-concentration, but a convergent source trace makes it Tauberian after boundary matching

**Evidence level:** exact moving-diagonal obstruction and sufficient tail criterion from [PL-314](../../findings/PL-314-moving-diagonal-tail-threshold.md), strengthened by [PL-315](../../findings/PL-315-moving-diagonal-survives-all-log-subcritical-sobolev.md), [PL-316](../../findings/PL-316-critical-half-derivative-still-misses-moving-diagonal.md), [PL-317](../../findings/PL-317-supercritical-zero-extension-forces-moving-tail-decay.md), the bounded-forcing obstruction [PL-318](../../findings/PL-318-bounded-logarithmic-forcing-moving-diagonal-obstruction.md), and the source-trace Tauberian reduction [PL-319](../../findings/PL-319-endpoint-log-source-trace-tauberian.md).

A weak integrated tail norm can miss the exact region sampled by a singularly moving kernel. In the Prime-Lattice stretched coordinate, the Green measure develops an atom at fixed `q=r`, while the corresponding physical logarithmic distance moves to `Q=r/s`. The normalized transfer therefore probes `m(r/s)/s`, not just total tail mass.

PL-314 constructs one fixed smooth nonnegative `m in L^1(dQ)` whose sparse bumps have vanishing total mass but height `Theta(s_n)` at `Q=r/s_n`. PL-315--PL-316 show that this obstruction survives `C^infty` regularity, every `W^{k,1}(dQ)`, all finite logarithmic Fourier moments, every zero-extension `H^alpha` with `alpha<1/2`, and even arbitrarily small critical `H^{1/2}` norm. PL-317 places a generic Sobolev success boundary just above that: any fixed `H^{1/2+eta}` zero-extension gain forces the moving sample to decay. PL-318 then shows that bounded logarithmic-Laplacian forcing, even arbitrarily small after scaling, still does not exclude sparse `Qm(Q)=Theta(1)` saturation.

PL-319 identifies the missing structural distinction. In logarithmic endpoint coordinates the one-dimensional Dirichlet logarithmic Laplacian satisfies

`F(Q)=2Qm(Q)-int_(Q0)^Q m(P)dP+H_(Q0)m(Q)+c_(Q0)(Q)m(Q)`.

If the residual is integrable and its singular translation remainder vanishes, `H_(Q0)m(Q)->0`, then

`F(Q)=2Qm(Q)-M+o(1)`.

Therefore a **convergent endpoint source trace is equivalent to `Qm(Q)->0`**. `W^{2,1}` is merely a convenient sufficient residual class; the load-bearing condition is integrability plus decay of the singular remainder.

This matters because the completed-Weil eigen-equation supplies the source-trace convergence structurally. Its zero-order source consists of fixed translations, a continuous archimedean completion term and scalar multiples of the state, all of which have one-sided endpoint limits once the known boundary behavior is used. The PL-315--PL-318 counterexamples show why this is stronger than bounded forcing: sparse moving-diagonal saturation forces the source to retain endpoint oscillation instead of converging.

There is one essential matching caveat. The canonical logarithmic-Laplacian boundary profile is `C Q^(-1/2)`, which is not integrable in `dQ`; its `2Qm` growth cancels the accumulated-mass term at leading order and is compatible with a finite source trace. The Tauberian mechanism applies to the **residual after the leading `Q^(-1/2)` coefficient is matched**. The actual branch still needs a theorem of the form

`u(x_Q)=C Q^(-1/2)+m(Q)`

with `m in L^1` and `H_(Q0)m(Q)->0`, or a direct proof of those residual properties.

The reusable diagnostic is therefore sharper than “moving observers need pointwise control.” A moving observer can defeat every aggregate norm currently tested, but an exact source equation may convert a pointwise tail condition into a Tauberian consequence of **trace convergence plus residual integrability**. When such an identity exists, prove the boundary decomposition and the residual class rather than imposing a stronger generic Sobolev norm than the source actually supplies.

**Boundary.** PL-319 is universal one-dimensional logarithmic-Laplacian geometry and does not itself supply rational-prime specificity or the leading boundary coefficient. The completed-Weil equation supplies source-trace convergence, not yet the required residual class. Until leading matching and `H_(Q0)m(Q)->0` are proved for the actual branch, PL-314's moving-diagonal gate remains open.