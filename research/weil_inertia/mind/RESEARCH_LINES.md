# Weil-inertia research lines

This file records mathematical questions that survive the current Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep source regularity separate from regularity of the canonical defect measure

WI-417--WI-422 identify sharp coercive source-space phenomena for translated-Blaschke probes. With an independently fixed planar density cap, one-target cost has the expected shallow-depth blow-up and critically separated target families converge to a Poisson-capacity problem. Generic TV/Carleson control is too weak because target-adaptive atoms remain cheap. For the bare translated-Blaschke response, ordinary global `L^p` control is bounded exactly for `1<p<2`, with a Lorentz endpoint and different behavior once a finite-TV budget is added.

WI-423 shows why those useful auxiliary spaces cannot simply be imposed on the canonical exact zeta source. The Riesz identity `-Delta U = 2 pi mu_off` makes that source the atomic counting measure of off-critical zeros; exact absolute continuity of the same source would already force the defect measure to vanish. A nontrivial route must therefore generate an auxiliary probe/coefficient source independently and prove an exact or quantitatively controlled coupling from its potential back to the canonical defect measure.

The live question is to derive such an auxiliary source and a target-independent concentration-and-tail budget from accessible prime-side, boundary or explicit-formula data. The norm must be fixed without inspecting hypothetical zero locations and must control the actual Poisson-capacity geometry consumed by the destination.

## Approach the boundary with independently controlled information; scale-mismatched Hankel repairs are asymptotically blind

WI-424 identifies the boundary logarithmic derivative of the Kunik Blaschke factor as a canonical positive Poisson defect counter. WI-425--WI-428 show why fixed safe lines and bounded positive or signed multiscale portfolios lose shallow defects unless their cost becomes singular. WI-429 supplies a different bounded category: the positive Hardy projection on `Re(s)=1/2+a` keeps exactly the zeros deeper than `a` and, as `a downarrow0`, retains a fixed fraction of the boundary defect energy. WI-430 extracts the corresponding first-defect quantum, making clear that an unconditional subquantum upper bound would already contain the missing zero-exclusion theorem.

WI-431--WI-434 then audit horizontal continuation from the absolutely convergent prime side. The global positive Hardy projection is zero on `Re(s)>1`; adiabatic localization does not create persistent positive-frequency source leakage; the exact horizontal transport identity splits the interior field into safe-line leakage, a window-edge term and transported residues; and the apparent principal-pole divergence of that edge disappears after exact semigroup transport.

WI-435 gives the decisive matched control. Even if the entire transported edge and safe-line leakage are both `o(1)`, a finite Kunik Blaschke block leaves a nonzero interior Hardy residue field with the full first-defect quantum. Horizontal transport therefore represents the defect more faithfully as its auxiliary errors vanish; it does not upper-bound that defect from independent source information.

WI-436 closes the most canonical translation-invariant mixed-frequency continuation. For a finite Kunik block and any probe line `0<a<d_*`, the non-Hermitian square of the interior logarithmic derivative satisfies the exact line-invariant identity

`int G_(F,a)(t)^2 dt = ||h_F||_2^2`,

where `h_F` is the positive boundary Poisson flux. Splitting `G_(F,a)=G_++G_-` into Hardy half-spaces gives

`2 int G_+(t)G_-(t) dt = ||h_F||_2^2`.

Thus the simplest bilinear positive/negative-frequency coupling sees the off-line defect perfectly, but the finite-Blaschke matched control saturates it identically. The signal is coercive without being independent source control.

WI-437 sharpens the surviving non-translation-invariant/Hankel branch. For one right-half Kunik defect of horizontal depth `d` and a probe line at fixed relative depth `a=theta d`, the normalized Hardy channels become uniformly weakly null as `d downarrow0`. Every **fixed compact** cross-channel operator therefore has normalized matrix element tending to zero uniformly in the zero ordinate, while the canonical WI-436 pairing remains the fixed fraction `sqrt(1-theta^2)` of the channel norms and has size `pi m^2/d`. Compact corrections are asymptotically lower order on arbitrarily shallow defects.

WI-438 shows that merely leaving the compact class is still far too weak. For a bounded Hankel symbol `varphi` and normalized upper-half-plane kernel `k_(r,gamma)`,

`||H_varphi k_(r,gamma)||_2^2 <= V_varphi(r,gamma)`,

where `V_varphi` is the Poisson/Garsia variance of the symbol at spatial scale `r`. At every common Lebesgue point of `varphi` and `|varphi|^2`, this variance tends to zero as `r downarrow0`; for bounded uniformly continuous symbols the convergence is uniform in `gamma`, even when `H_varphi` is noncompact. The explicit noncompact symbol `exp(-i omega t)` has norm-one Hankel operator but response `1-exp(-2 omega r)`, which still vanishes on shallow packets. Thus global noncompactness can live at infinity while being useless at the defect scale.

The exact surviving gate is **scale-matched local oscillation**. For the one-zero Kunik packet, the relevant scale is `r=(1-theta)d`; a viable bounded-symbol family must keep order-one Poisson variance at the actual defect ordinate on `r asymp d`. A fixed uniformly continuous symbol cannot do this, and an equicontinuous family cannot do it uniformly. A scale-dependent family can evade the barrier only by developing oscillation at frequency of order `1/d` (the model `varphi_d(t)=exp(-it/d)` does so). Whether admissible zeta source data supply and control such scale-matched roughness without importing the target zero is now the arithmetic question.

The live theorem is therefore narrower than “find a noncompact coupling.” Determine the small-scale Poisson-variance profile of any proposed source-derived cross-frequency symbol or operator family. If its local oscillation vanishes at the shallow Hardy-kernel scale, WI-438 rules it out regardless of global noncompactness. If order-one local oscillation survives, prove that it is fixed by independent source information and remains aligned with the defect channel without inspecting the hypothetical divisor. A mechanism outside bounded-symbol Hankel theory remains possible, but it must still pass the finite Kunik Blaschke adversarial test and the absence of a fixed probe depth to the left of all possible off-line zeros.
