# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by source-resolvable motion, repertoire and approximate linear complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-040-source-complexity-should-be-measured-at-poisson-resolution`.

NB-165--NB-167 isolate the capped Poisson transport metric actually seen by a compact signed sampler near `Re s=1`. NB-168 shows one fixed stationary template cannot produce logarithmic Euler rescue on positive density under the subcritical transport budget. NB-169--NB-171 then price ordered height adaptation by refresh count, total variation and finite `p`-variation measured at that same source resolution.

NB-172 removes temporal regularity entirely: the rescue density is controlled by the internal covering number of the template range in capped Poisson transport. NB-173 gives a different compression when the range lies **exactly** in a stationary linear span: if `m_T` normalized source directions generate every template with coefficient `ell^2` energy at most `Y_T^2`, then rescue density is bounded by `m_T Y_T^2/log^2 T` times the inherited ultra-thin factor.

NB-174 unifies those unordered compressions at the resolution the arithmetic source actually sees. Define `mathfrak L_T(epsilon)` by allowing every adaptive template to be represented by a normalized stationary dictionary plus a residual of capped-Poisson size at most `epsilon q_T`. The residual is pointwise invisible up to `C_B epsilon H_T`, while the stationary core is controlled by the NB-168 mean-square theorem. Consequently positive-density logarithmic rescue forces large **approximate** linear source complexity whenever `epsilon` stays below a fixed fraction of `log T/H_T`.

The new currency has the correct endpoints and comparison bounds:

`mathfrak L_T(0)=mathfrak L_T`,

and, at the same normalized tolerance,

`(X_T-epsilon)_+^2 <= mathfrak L_T(epsilon) <= N_T(epsilon) X_T^2`.

Thus exact rank can be enormous while the source-resolvable approximate rank is small, and small range entropy automatically bounds approximate linear complexity at the same scale. Conversely, a continuum may have huge covering entropy while remaining near a well-conditioned low-dimensional source span.

The surviving adaptive escape is therefore sharper than “large range” or “high exact rank.” A positive-density rescue must generate large complexity **after quotienting all template motion below the Poisson resolution of `zeta'/zeta`**, or exploit the known ultra-thin limitation of the stationary mean-square theorem. A concise nonlinear arithmetic rule is relevant only if its realized range remains complicated at that specific resolution.

The next structural question is to characterize or lower-bound `mathfrak L_T(epsilon_T)` for source-natural nonlinear template families at the admissible tolerance `epsilon_T=Theta(log T/H_T)`, ideally by an invariant dual quantity rather than syntactic model complexity. Large approximate complexity is only necessary, not sufficient; the stationary directions may still be arithmetically ineffective.

## Keep target conditioning and arithmetic-source persistence separate

NB-168--NB-174 are source-side persistence theorems. They control the density on which compact arithmetic samplers can create logarithmic Euler rescue after the sampler family has been compressed at the source's own resolution. They do not turn a density obstruction into pointwise exclusion at a selected sparse sequence, remove the `a_T\lesssim T^(-1/2)` ultra-thin regime, or by themselves connect surviving source response back to global Nyman approximation.