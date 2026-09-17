# MI-056 — Log-smooth additive readouts convert source motion into a reverse-discrimination tariff

**Evidence level:** exact finite-source/channel synthesis from [MC-349](../../findings/MC-349-destination-relative-edge-kl-reliability.md) through [MC-354](../../findings/MC-354-log-smooth-additive-readout-edge-tariff.md). The implication is exact for additive readouts with globally Lipschitz noise score; whether a concrete Möbius endpoint architecture has this factorization remains open.

MC-353 turns the required source information into a lower bound on the privacy-loss distribution across neighboring source states. MC-354 supplies a matching analytic upper currency for an important channel class instead of appealing generically to forward smoothness.

Suppose the complete observation factors through an additive readout

`Z=Phi(X)+N`,

with positive noise density `q`, log-density `f=log q`, and globally `beta`-Lipschitz score `grad f`. For a source edge `e={x,x'}` let

`h_e=Phi(x')-Phi(x)`.

Then the complete-transcript half-Jeffreys divergence obeys

`b_e <= (beta/2)||h_e||^2`.

Combining this with the exact endpoint lower bound from the source-information/dephasing argument gives the necessary asymptotic tariff

`beta_R G_(2,R)^2 >= 2 eta^2/C-o(1)`,

where `G_(2,R)` is the relevant average edge displacement, `C` the coefficient-energy budget and `eta` the nontrivial dephasing level. Thus an additive architecture whose neighboring readout shifts vanish too quickly relative to its inverse-noise curvature cannot carry the discrimination demanded by the endpoint.

The same mechanism also controls the rare-tail escape. MC-354 bounds moments of privacy loss by a linear score term plus a quadratic `beta` displacement term, so sufficiently small edge shifts together with uniform score moments imply the uniform integrability that MC-353 needs. Gaussian noise is the exact model case: `beta=1/sigma^2`, making the tariff an ordinary signal-to-noise requirement.

The reusable distinction is important. **Forward regularity is informative only after it is tied to the actual inverse likelihood geometry of the transcript channel.** A Lipschitz encoder by itself need not limit distinguishability; a log-smooth additive likelihood does, because source displacement is converted directly into Jeffreys/privacy-loss cost.

**Boundary.** MC-354 is not a theorem about arbitrary endpoint transcripts, deterministic/singular observations or the Mertens function. A concrete Möbius route still has to prove that its relevant source-edge channel admits this additive log-smooth factorization, or derive an analogous reverse-divergence upper bound for the channel class it actually uses.