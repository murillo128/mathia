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

WI-441 strengthens this obstruction for an entire fixed bank of pure-frequency Hankel shifts, even at unbounded frequencies. For a positive measure of shifts `dmu(omega)` and a normalized shallow Hardy packet of scale `r`, the exact squared bank response is

`F_mu(r)=int_(omega>0)(1-exp(-2r omega)) dmu(omega)`.

The bank is a single nonincreasing Fourier multiplier at the quadratic level. If its packet energy is finite at even one positive scale `r_0`, then `F_mu(r)->0` as `r->0`, uniformly over ordinates. Any bounded signed, non-diagonal mixing of the bank outputs remains blind. This forbids a finite-cost frequency-bank rescue, not all Hankel symbols or depth-dependent unbounded rescaling.

The exact surviving gate is **scale-matched local oscillation**. For the one-zero Kunik packet, the relevant scale is `r=(1-theta)d`; a viable bounded-symbol family must keep order-one Poisson variance at the actual defect ordinate on `r asymp d`. A fixed uniformly continuous symbol cannot do this, and an equicontinuous family cannot do it uniformly. A scale-dependent family can evade the barrier only by developing oscillation at frequency of order `1/d` (the model `varphi_d(t)=exp(-it/d)` does so). Whether admissible zeta source data supply and control such scale-matched roughness without importing the target zero is now the arithmetic question.

The live theorem is therefore narrower than “find a noncompact coupling.” Determine the small-scale Poisson-variance profile of any proposed source-derived cross-frequency symbol or operator family. If its local oscillation vanishes at the shallow Hardy-kernel scale, WI-438 rules it out regardless of global noncompactness. If order-one local oscillation survives, prove that it is fixed by independent source information and remains aligned with the defect channel without inspecting the hypothetical divisor. A mechanism outside bounded-symbol Hankel theory remains possible, but it must still pass the finite Kunik Blaschke adversarial test and the absence of a fixed probe depth to the left of all possible off-line zeros.


## Distinguish Wang's smooth-support endpoint from genuine support crossing

WI-354 identifies the `xL^3` zero-window localization term and the independent prime-polynomial mean-square loss for intervals `H=T^theta`. But WI-440 corrects the inference that these terms force **strict** support `lambda<theta`. For any fixed even real smooth test `g` supported in `[-theta,theta]`, its endpoint flatness gives `|g(theta-u)|<=C_g u^2`. Retaining this weight through localization makes

`L^3 int_0^theta |g(alpha)|T^alpha d alpha <= C_g H L^3 int_0^infty u^2 exp(-Lu)du=O_g(H)`.

Keeping the unsimplified Montgomery--Vaughan mean-square bound at `x=H` then proves Wang's pair-correlation formula **at equality** with an `O_g(H)` error. The former strict-endpoint objection is not current evidence.

The unsolved frontier is support **genuinely beyond** `theta`: for `alpha>theta`, `x=T^alpha>H`, so both the present localization majorant and prime mean-square error require a new source-independent, support-integrated estimate, rather than merely using the existing smooth flatness at the old endpoint. Nor does this fixed-`H=T^theta` conclusion automatically extend to logarithmically shorter intervals. WI-442 independently upgrades the proportion of **distinct zeros anywhere in the strip** to a positive lower bound for every fixed `0<theta<1`, but it does not provide the same conclusion for simple zeros **on the critical line** or exclude a sparse exceptional set.

A support-crossing result must specify which error survives integration over the added `alpha>theta` region and demonstrate an `o(H log T)` aggregate bound without assuming the desired zero distribution.
