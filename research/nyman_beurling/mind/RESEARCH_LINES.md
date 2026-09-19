# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Control the nested depth-phase carrier only inside the carrier-width Ford window

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-061-ford-damping-is-the-laplace-dual-of-nested-depth-phase`.

NB-218--NB-224 isolate the exact source-side carrier. Keeping source and Mellin kernel coupled removes artificial primitive tariffs; generic strip analyticity is sharp for the ambient class; the actual zeta singularity spectrum plus Bellotti density reaches almost to Ford height; and a proportional logarithmic source shell narrows the vertical carrier enough to reach the exact Ford denominator.

NB-225--NB-227 show why population, phase and depth cannot be optimized separately. Every genuinely sublinear shell admits matched packets compatible with the audited zero information, fixed-power phase cancellation does not remove them, and every separable `M^vartheta/Q(D)` repair can be defeated by moving to a slowly growing depth where Ford damping compensates the permitted phase bias.

NB-228 identifies the nonseparable object consumed by the residue. With normalized zero depth `d_rho=R(1-beta)`, Ford ratio `Y=X/R`, full shell coefficient `b_rho`, and cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`,

Stieltjes/Abel summation makes the residue the Laplace-weighted integral of `C(D)` against `e^(-YD)`.

NB-229 first removes the deep formal Ford range: the smooth vertical carrier plus the classical zero count gives an absolute `Qe^(-YD_0)` tail, so depths beyond `O(log Q)` cannot contribute at order one.

NB-230 now compresses the remaining shallow frontier further by keeping the **carrier width** visible. Bellotti's local zero-disk estimate already gives, in its valid shallow range,

`M_(t,H)(D) << D + J`, with `J=1+R/H`.

Under the exact Ford damping this implies an integrated tail

`T(D_0,D_1) << e^(-Y D_0)(D_0+J+1)`.

Hence every moving depth with `YD_0-log J -> +infinity` is already absolutely harmless. The unresolved width-dependent layer is confined to

`1 << D \lesssim (1/Y) log(1+R/H)`

inside the Bellotti range, plus any `Theta(log Q)` transition interval not covered by the local-disk lemma before the coarse NB-229 cutoff. When `log(R/H)=o(log Q)`, this is a genuine asymptotic compression; for very narrow shells with `log(R/H)=Theta(log Q)` no such improvement should be claimed.

NB-231 shows that this transition is sharp for the same information set in the conservative capacity regime `1 << R/H <= log Q`. A packet using a fixed positive fraction of the `R/H` carrier slots can be placed at

`D=(log(R/H)+w)/Y`, with `w=O(1)`,

while obeying the Vinogradov--Korobov zero-free boundary, Bellotti's growing-density allowance, Bellotti's local `O(D)` disk count, and ordinary local zero counting. Its moving-shell phases are exactly aligned and its signed residue stays order one. Thus `YD-log J -> +infinity` is not merely sufficient: population-only information cannot force decay while `YD-log J=O(1)`. The next actual-zeta input must attack the bounded transition layer itself by coupling depth to phase or spacing.

The matched packets of NB-225--NB-227 and NB-231 therefore live on the same logarithmic carrier-width scale as the NB-230 upper cutoff. Available vertical population is roughly `J`, while Ford damping charges `e^(YD)`, so the critical balance is `J≈e^(YD)`. The next source theorem should be parameterized by `D/log(1+R/H)`, not by `D/log Q` alone.

Inside that window, population information may still be insufficient. Useful surviving inputs are genuinely joint: a local estimate coupling vertical population and horizontal depth more strongly than `D+R/H`, a phase-sensitive bound for `C(D)`, or an arithmetic restriction ruling out the matched packet geometry for actual zeta zeros. Improving zero density outside the carrier-width window attacks a region already subcritical under existing Bellotti input.

## Keep source width, cumulative depth phase, carrier capacity and Ford damping in one ledger

The relevant currencies are source width `H`, vertical capacity `J=1+R/H`, normalized horizontal depth `D`, the full profiled coefficient `b_rho`, cumulative signed carrier `C(D)`, and Ford damping `e^(-YD)`. NB-230 shows that the **linear** capacity cost `J` becomes only a **logarithmic** depth budget after attenuation; NB-231 shows that this logarithmic conversion, including the need for a diverging additive margin, is sharp in the audited `J<=log Q` regime.

This is stronger bookkeeping than asking for a theorem uniformly over the whole Ford strip. Near-wide shells, almost every moving shallow depth is already harmless; narrow shells retain a larger active band. The remaining theorem must therefore track width and depth together and remain source-specific enough not to recover the same Euler shell circularly.

The destination bridge is unchanged. These source-side residue estimates do not themselves prove a quantitative Nyman--Beurling distance bound; a successful destination argument must still force an approximant to realize the positive Euler return tested by this carrier rather than merely control an abstract zero sum.