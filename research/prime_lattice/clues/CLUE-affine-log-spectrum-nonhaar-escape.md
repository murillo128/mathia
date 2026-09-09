---
id: CLUE-prime-lattice-affine-log-spectrum-nonhaar-escape
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-172-hilbert-schmidt-affine-liouville-chowla-trace-removal.md
  - research/prime_lattice/findings/PL-173-affine-liouville-averaging-collapse.md
  - research/prime_lattice/findings/PL-174-logarithmic-affine-liouville-haar-flat.md
  - research/prime_lattice/findings/PL-175-logarithmic-affine-liouville-walsh-collapse.md
  - research/prime_lattice/findings/PL-176-liouville-additive-cube-gowers-flattening.md
  - research/prime_lattice/findings/PL-177-prime-axis-affine-closure-flattening.md
  - research/prime_lattice/findings/PL-178-prime-axis-single-average-shifted-prime-parity-boundary.md
  - research/prime_lattice/findings/PL-179-oriented-prime-axis-phase-closure-shifted-prime-data.md
  - research/prime_lattice/findings/PL-180-kronecker-affine-phase-pnt-universality.md
  - research/prime_lattice/findings/PL-181-short-interval-pnt-kronecker-frequency-horizon.md
  - research/prime_lattice/findings/PL-182-growing-source-primes-kronecker-flattening.md
  - research/prime_lattice/findings/PL-183-smooth-target-weight-kronecker-flattening.md
  - research/prime_lattice/findings/PL-184-bounded-variation-target-kronecker-flattening.md
  - research/prime_lattice/findings/PL-185-siegel-walfisz-congruence-target-kronecker-flattening.md
  - research/prime_lattice/findings/PL-186-shifted-prime-kubilius-mobius-tail-barrier.md
  - research/prime_lattice/findings/PL-187-affine-prime-phase-window-l2-flattening.md
  - research/prime_lattice/findings/PL-188-shifted-prime-tail-sieve-parity-barrier.md
  - research/prime_lattice/findings/PL-189-bounded-effective-window-fourier-uniqueness.md
  - research/prime_lattice/findings/PL-190-shrinking-affine-window-pointwise-collapse.md
  - research/prime_lattice/findings/PL-191-escaping-positive-window-pnt-flattening.md
  - research/prime_lattice/findings/PL-192-escaping-affine-window-almost-periodic-recurrence.md
---

# What source-forced affine statistic survives logarithmic two-point Haar flattening?

## Observation

The affine Liouville route has now separated several regimes sharply. Fixed-shift ordinary correlations retain the unresolved Chowla difficulty; canonical uniform shift averaging collapses or reduces to simpler summatory data; and `PL-174` shows that every fixed finite second-order logarithmic shift filter has the universal Haar spectrum. `PL-175` further shows that “higher-order or nonlinear” is not by itself an escape: all odd Walsh sectors vanish under logarithmic averaging, the degree-two sector vanishes, and every bounded observable of three distinct fixed Liouville translates has the complete independent-fair-sign joint law.

Thus the first fixed-shift Walsh sector not removed by the cited published correlation theorems is even degree four. This is only an information boundary: `PL-175` does not show that any fourth- or higher-even-order statistic has a non-Haar limit or carries RH-sensitive data.

`PL-176` removes the most canonical diffuse use of that boundary. If the degree-four parity is sampled on the additive parallelogram `(x,x+h,x+k,x+h+k)` and summed over all positive base points and both positive directions, its normalized average is unconditionally `o(1)`. The exact statistic is a Fourier fourth moment / additive `U^2` cube, so Davenport's uniform exponential-sum bound already flattens it. Modern higher-uniformity results show analogous Gowers flattening on average for all fixed cube orders in mesoscopic intervals, and do so for general nonpretentious bounded multiplicative functions. Therefore “go to degree four and average all directions” is not a surviving non-Haar mechanism.

`PL-177` removes a natural source-forced sparse repair at prime density. If the two directions come from multiplicative source elements `a,b` through the additive parallelogram `(n,an,bn,(a+b-1)n)`, complete multiplicativity collapses its parity exactly to `lambda(a)lambda(b)lambda(a+b-1)`. For any source family `A_X subset (X,2X]`, the complete double-source sum is a single Fourier integral and is bounded by `||sum_{m<=4X} lambda(m)e(m theta)||_infty |A_X|`. Davenport therefore makes the normalized statistic logarithmically flat for every polylogarithmically dense source family, including the primes. Source forcing and prime sparsity alone are consequently not enough if both source axes are still averaged independently and broadly.

`PL-178` classicalizes the most obvious one-axis repair. Freezing one prime source `r` in the same additive closure and averaging the other prime `q` gives pointwise `lambda(q+r-1)`, so the entire lattice/base geometry collapses to the classical fixed-shift Liouville-on-shifted-primes problem with `h=r-1`. Peer-reviewed theory proves cancellation after averaging over the shift but treats a prescribed fixed shift as the parity frontier. Thus “freeze one prime axis” is not by itself a new non-Haar mechanism; it merely trades the Fourier-flat double average for a classical hard scalar correlation.

`PL-179` removes the bare total-exponent phase lift of that same one-axis closure. For any unitary completely multiplicative `f`, the oriented phase plaquette `f(n) overline{f(rn)} overline{f(qn)} f((r+q-1)n)` cancels the base point exactly. For the intrinsic exponent character `f_z(m)=z^Omega(m)`, with the same phase `z` on every prime direction, the residual is exactly `z^(Omega(q+r-1)-2)`. Thus replacing Liouville parity by the full one-parameter `Omega` phase does not retain a new lattice holonomy: it lands on the classical theory of multiplicative functions on shifted primes. Hildebrand and Timofeev already treat that setting, Khripunova gives a nontrivial fixed-shift cube-root phase estimate, and current dynamical work proves broad shift-averaged `Omega`-phase statements while leaving prescribed shifts distinct. A surviving “phase-conditioned” construction must therefore add a non-product/source/target ingredient before this oriented multiplicative cancellation, not merely change the character read out from total exponent parity.

`PL-180` specializes the surviving prime-dependent phase to the canonical vertical/Kronecker character `f_t(m)=m^(it)`. For fixed source prime `r`, the oriented residual simplifies further to `r^(-it)(1+(r-1)/q)^(it)`. After demodulating the known source phase, bounded normalized time and the first mesoscopic scale `t(r-1)/X -> tau` converge to the deterministic PNT kernel `J(tau)=integral_0^1 exp(i tau/u)du`; the readout sees only macroscopic prime density there.

`PL-181` closes most of the super-mesoscopic version of that exact branch for fixed `r`. Guth--Maynard's published almost-all prime number theorem in intervals of length `X^(2/15+epsilon)`, combined with a good-offset partition of the fixed global prime sum, gives uniformly for every fixed `eta>0`

`B_X(X tau/(r-1)) = J(tau)+o(1)` for `|tau|<=X^(13/15-eta)`.

Hence the same broad fixed-source Kronecker readout tends to zero whenever `|tau|->infinity` inside that polynomial window. The exponent `13/15` is the dual resolution supplied by current short-interval prime-counting technology, not a new lattice spectral constant.

`PL-182` removes the separate escape of merely letting the frozen source prime grow. For arbitrary `h_X=r_X-1`, no matter how `h_X/X` behaves, the exact phase derivative is controlled by

`nu_X = |t_X| h_X/(X+h_X)`.

Within `nu_X<=X^(13/15-eta)`, the same short-interval argument gives the deterministic continuum profile `I_(h_X/X,t_X)=integral_0^1 exp(i t_X log(1+(h_X/X)/u))du+o(1)`, and elementary integration by parts gives `|I|<=2/nu_X`. Thus the broad Kronecker readout tends to zero whenever `nu_X->infinity` in that window, uniformly across arbitrary source growth. Source growth alone is not a live non-Haar escape; the phase must cross the current resolution horizon or change another load-bearing ingredient.

`PL-183` removes the cheapest smooth target-relative repair inside that same band. If a bounded target enters only through a scaled one-point envelope `w_X(q/X)` with Lipschitz complexity `L_X`, then uniformly whenever `L_X+nu_X<=X^(13/15-eta)` the prime average is still only the continuum one-point-density integral. If additionally `nu_X->infinity` and `L_X=o(nu_X)`, the prime average tends to zero.

`PL-184` shows that smoothness was not the load-bearing assumption. The same conclusion holds for every bounded one-point target of total variation `V_X` whenever `V_X+nu_X<=X^(13/15-eta)`, including arbitrary jumps and step functions; if `nu_X->infinity` and `V_X=o(nu_X)`, the readout again tends to zero. In particular, a discontinuous or finitely windowed target is not an escape merely because its jumps occur below the local prime-counting mesh.

`PL-185` closes the first genuinely arithmetic high-variation one-point repair: every bounded residue-class target modulo `m<=(log X)^A` still scalarizes by Siegel--Walfisz to its residue mean times the same continuum phase profile throughout the corresponding controlled phase range. Congruence oscillation therefore does not survive merely because its real-variable total variation is large.

`PL-186` then moves from congruences to the exponent vector of the shifted target itself. Ford's shifted-prime Kubilius theorem shows that all coordinates `(v_ell(q+h))_(ell<=y)` with `y=X^{o(1)}` are asymptotically governed in total variation by an independent local model. In particular the truncated Möbius parity over every subpower coordinate cutoff has mean tending to zero. The unresolved fixed-shift Möbius/Liouville information is necessarily in the large-prime exponent tail above every such cutoff or in a coupling involving that tail.

`PL-188` identifies why merely extending local divisor resolution is not a credible way to recover that missing sign. The classical sieve parity problem supplies matched sequences with opposite global Liouville parity but essentially indistinguishable deep local divisor data; Friedlander--Iwaniec's parity-breaking input is genuinely bilinear. Thus any live large-tail mechanism must be parity-sensitive through a bilinear, signed, or otherwise nonlocal coupling rather than another accumulation of one-point local exponent marginals.

The phase-window alternatives are also now classified much more tightly. `PL-187` proves that averaging over any diverging effective affine phase width washes out **every** bounded target, including the full shifted Möbius/Liouville sign, uniformly in the window center. At bounded positive width and bounded normalized center, `PL-189` gives the opposite rigidity: flattening already forces the underlying signed macroscopic coefficient measure to vanish weak-*, so it is not an easier spectral bypass around the hard zero-frequency cancellation. `PL-190` shows that shrinking windows reduce to a pointwise readout and add no averaging rigidity.

Finally, center escape by itself has no coefficient-blind meaning. `PL-191` gives unweighted PNT-flat matched controls on fixed-width windows whose centers escape inside the current short-interval resolution horizon, while `PL-192` uses Bohr almost periodicity to produce arbitrarily large recurrent centers for the **same** unweighted carrier with a fixed positive amount of local mass. A surviving high-frequency construction must therefore prescribe its center arithmetically and couple it to nontrivial target/source data; arbitrary or merely escaping phase centers are not evidence of a rational-prime invariant.

## Research question

Is there a canonical prime-lattice operation in which the **large-prime exponent tail** of a shifted affine target enters through a genuinely parity-sensitive bilinear or nonlocal coupling, together with a source-forced or arithmetically prescribed phase/target relation, so that the observable survives without reducing to a classical shifted-prime scalar, a local Kubilius/sieve statistic, a universal broad-window erasure, or generic almost-periodic recurrence?

The live question is deliberately narrower than “find any non-Haar affine statistic.” A candidate must change the information geometry before the one-point/local-divisor or coefficient-blind phase-window collapses above. Merely moving farther in frequency, increasing coordinate resolution, or using a complicated bounded target does not suffice.

## Why it may matter

The remaining branch is now tied to a classical and genuinely arithmetic obstruction rather than to a generic lack of estimates. `PL-186` and `PL-188` locate the missing information in a parity-sensitive global tail that local exponent statistics and Type-I/sieve data cannot recover. If a canonical affine/lattice construction could couple that tail to a source-forced phase or completed operator before averaging destroys it, it would preserve information not present in the matched local-product controls.

Conversely, another negative theorem at this stage would be valuable because it would close not just a smoothness or frequency window but the first structurally plausible escape from the sieve parity barrier inside this affine prime-lattice branch. Acceptance of the clue records only that this narrow coupling question is worth testing; it is not evidence for existence, novelty, analytic continuation, or RH relevance.

## Decisive test

Choose one concrete operation before inspecting its outcome and state exactly which theorem-controlled sector it leaves. For a fixed finite family of shifted Liouville parities, first expand the proposed readout in Walsh characters. If every nonconstant component has odd degree or degree two, reject it immediately by `PL-175`.

If a proposed even-degree statistic subsequently averages its shifts over a complete additive cube, test the resulting Gowers/Fourier moment before assigning it any spectral interpretation. The canonical two-direction degree-four average is already rejected by `PL-176`, and higher complete cube averages must be compared with the strongest available higher-uniformity theorem.

If the shifts are source-forced by multiplicative elements, test whether complete multiplicativity removes the base variable before interpreting the geometry. Any independent two-source construction equivalent to `(n,an,bn,(a+b-1)n)` with `|A_X| >= X/(log X)^K` is already rejected by `PL-177`. If one source is instead frozen at a fixed prime `r` and the other is broadly averaged over primes, `PL-178` shows that the canonical parity becomes exactly `lambda(q+r-1)`; treating that scalar as an unexplored lattice invariant is rejected by prior art unless an additional structure changes the problem before the collapse.

For a unitary phase refinement, apply the same reduction before assigning holonomy or spectral language. If the candidate is the oriented plaquette `f(n) overline{f(rn)} overline{f(qn)} f((r+q-1)n)`, `PL-179` gives the exact residual `overline{f(r)} overline{f(q)} f(r+q-1)`. In particular the canonical total-exponent family `f_z=z^Omega` becomes only `z^(Omega(q+r-1)-2)`. A new phase-conditioned candidate must therefore explain what non-product condition, prime-dependent source structure, target transport, or completion prevents reduction to an already-classical shifted-prime multiplicative mean.

If the phase is the canonical vertical character `f_t(n)=n^(it)`, demodulate the explicit source phase and use the exact parameter `nu=|t|(r-1)/(X+r-1)` before assigning zero-sensitive meaning. `PL-180`--`PL-182` show that for every fixed `eta>0`, a broad prime average with `nu<=X^(13/15-eta)` is forced to a continuum one-point-density profile, uniformly even when `r=r(X)` grows; if `nu->infinity`, the average tends to zero. Beyond that phase-resolution horizon the present theorem is silent, but `PL-191`--`PL-192` show that arbitrary center escape is nonselective: a candidate there must supply an independently justified arithmetic prescription for the center and an estimate coupling it to the target, not merely rely on lack of current PNT control.

If the proposed repair is a bounded one-point target factor `w_X(q/X)`, compute its total variation `V_X` before assigning target-relative meaning. `PL-184` rejects sub-resolution variation, and `PL-185` separately rejects bounded residue targets of polylogarithmic modulus in its Siegel--Walfisz phase range. If the target depends on finitely or subpower-many shifted exponent coordinates, compare directly with `PL-186`: every bounded cylinder observable below `y=X^{o(1)}` is already controlled by the independent Kubilius model.

If the candidate tries to reconstruct full Möbius/Liouville orientation by increasing local divisor resolution, apply the parity matched control of `PL-188`. A source claim based only on Type-I/divisor/congruence marginals does not pass; the construction must expose a genuinely signed bilinear/global-tail input before averaging.

For any phase-window construction, compute the effective width first. If it tends to infinity, `PL-187` erases every bounded target and the candidate is rejected. If it has fixed positive width at bounded normalized center, `PL-189` shows that flattening is already as hard as macroscopic signed coefficient cancellation. If it shrinks, `PL-190` reduces it to a pointwise readout. If its center escapes, test both the PNT-flat matched control of `PL-191` and the recurrent matched control of `PL-192`; center escape alone has no invariant asymptotic content.

A surviving candidate must therefore expose a source-forced relation that simultaneously avoids scalar shifted-prime reduction, local-product/Kubilius classicalization, the sieve parity barrier, and coefficient-blind phase averaging. Keep the large-tail truncation, bilinear structure, phase center, window scale, target transport, topology/completion, and matched control explicit. Merely renaming an unresolved shifted-prime parity correlation as a trace, determinant, spectrum, or holonomy does not pass.

## Evidence boundary

`PL-174`--`PL-184` remove second-order logarithmic structure, all odd Walsh sectors plus degree two, complete diffuse degree-four cube averaging, independently averaged prime-density affine closure, raw fixed-one-prime shifted parity, total-exponent phase lifts, and the canonical vertical character with bounded-variation one-point targets through the current short-interval phase-resolution range. `PL-185` extends the one-point collapse to polylogarithmic congruence targets. `PL-186` shows that every bounded subpower shifted-exponent cylinder is Kubilius-generic, while `PL-188` identifies the remaining global sign with the classical sieve parity barrier and hence with the need for a bilinear/global-tail input. `PL-187`--`PL-192` classify the basic phase-window escapes: diverging widths erase every bounded target; bounded positive widths at bounded center do not bypass the underlying cancellation; shrinking widths are pointwise; and escaping centers admit both generic PNT flattening and generic almost-periodic recurrence.

None of these results proves cancellation for a prescribed shifted-prime Möbius/Liouville sum, settles any fixed even-order Chowla case beyond the theorem-controlled sectors, supplies a bilinear parity-breaking theorem for the shifted-prime tail, controls an arithmetically prescribed superhorizon phase coupled to that tail, or rules out a genuinely nonlocal/completed target coupling that changes the averaging law before these reductions. No non-Haar survivor, analytic continuation, or RH implication is established here.

## Research disposition

Accepted for active investigation, **narrowed by `PL-185`--`PL-192`**. High real-variable variation, polylogarithmic congruence complexity, every subpower exponent-coordinate cylinder, broad phase-window averaging, bounded-center positive-width averaging, shrinking windows, and arbitrary escaping centers are no longer live escapes by themselves. The fixed-shift nonlinear branch also remains subject to the earlier Walsh/Gowers and scalar shifted-prime reductions.

The live target is now a source-forced construction that reaches the large-prime exponent tail through a genuinely parity-sensitive bilinear/nonlocal relation **before** coefficient-blind averaging, or a comparably strong completed/target-relative coupling with an arithmetically prescribed phase that cannot be reproduced by the matched local-product, sieve-parity, PNT-flat, or almost-periodic controls. Acceptance records only that this sharply delimited question remains worth testing; it is not evidence for its truth, novelty, or RH relevance.