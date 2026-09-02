# Shared-source full-packing constraint weave

![Simultaneous full-packing constraints](shared_source_full_packing_constraints.png)

## Question

When two positive-defect full-packed Ramanujan interactions share the same source prime `p` at one observation length `N`, can their exact row-kernel modes coexist in the shared `p`-frequency coordinates? The proposed orbit-quotient clue asks first whether coprime quotient orders force trivial intersection and, more generally, whether the pullback geometry of the two collapsed rotations imposes stronger simultaneous rigidity.

## Mathematical construction

For each close-prime pair `p<q<2p`, write `d=q-p` and reduce the observation window to the nearest boundary length

\[
\delta_N(p,q)=\min\{N\bmod pq,\ pq-(N\bmod pq)\}=kq+s.
\]

In the full-packing regime of `WI-102`, the residual geometry has

\[
R=s-d=[kd]_p,\qquad
t=p-d,\qquad
g=\gcd(R,t)>1,
\]

with deleted interval `C={R,...,R+d-1}`. Collapsing `C` conjugates the free permutation to rotation by `R` on `Z/tZ`. By `WI-096`, the true row kernel consists exactly of `p`-periodic, zero-mean functions that vanish on `C` and are constant on each of the `g` free cycles. Thus an intersection can be computed without floating-point linear algebra: union the equality relations supplied by both cycle decompositions, mark every component touching either deleted interval as zero, and impose the common zero-mean relation on any surviving components.

The rendered exact example uses one source prime and one actual shared observation length:

\[
p=47,\qquad N=95{,}384.
\]

For `q_1=59`, one gets

\[
\delta_1=1102,\quad d_1=12,\quad k_1=18,\quad
R_1=28,\quad t_1=35,\quad g_1=7,
\]

so `C_1={28,...,39}` and `dim K_1=6`. For `q_2=61`,

\[
\delta_2=773,\quad d_2=14,\quad k_2=12,\quad
R_2=27,\quad t_2=33,\quad g_2=3,
\]

so `C_2={27,...,40}` and `dim K_2=2`. Here `gcd(g_1,g_2)=1`. Neither deleted interval by itself meets every free cycle of the other kernel, so the vanishing of the intersection is not a one-hole screening artifact. After both cycle-equality systems are superposed, however, every combined equality component touches `C_1\cup C_2`, forcing

\[
K_1\cap K_2=\{0\}.
\]

An independent exact integer residue-sum rank calculation gives `dim K_1=6`, `dim K_2=2`, and `dim(K_1 intersection K_2)=0`, agreeing with the cycle-constraint computation.

There is also a simple exact alignment hidden by the original coordinates. Define the integer center of a full-packed deleted interval by

\[
c=R+\frac d2.
\]

Because `p,q` are odd, `d` is even. Full packing gives `s=R+d` and `R=[kd]_p`, hence

\[
\delta=kq+s\equiv 2R+d=2c\pmod p.
\]

At one shared observation length, the nearest-boundary convention gives \(N\equiv \pm\delta_i\pmod{p q_i}\); reducing modulo `p` shows

\[
c_1\equiv \pm c_2\pmod p.
\]

Since both centers lie strictly between `0` and `p`, simultaneous full-packed holes are therefore either concentric (`c_1=c_2`) or antipodal (`c_1+c_2=p`). In the rendered example both centers are exactly `34`, which explains the visibly nested zero intervals.

## Observation and robustness

An exact finite sweep was run over every odd source prime `5 <= p < 300`, every pair of distinct target primes `p<q_1<q_2<2p`, and every positive-defect full-packed configuration for each target. A configuration pair was counted as simultaneous when there existed signs `\varepsilon_i\in\{+1,-1\}` for which the two congruences

\[
N\equiv \epsilon_i\delta_i\pmod{p q_i}
\]

were CRT-compatible. The sweep found `84,983` simultaneous positive-defect configuration pairs. Every one had

\[
K_1\cap K_2=\{0\}.
\]

Among them, `14,051` had coprime quotient orders `gcd(g_1,g_2)=1`; none gave a counterexample to the sharp conjecture in the existing clue. More strongly, `2,256` simultaneous pairs were cases where neither deleted interval alone met every cycle of the other kernel, and `782` of those also had coprime quotient orders. All still had trivial combined intersection. Thus the observed rigidity is not explained merely by one zero interval directly killing every cycle of the other pair.

The enumeration used only exact integer congruences, cycle decompositions, and connected-component propagation. It did not use numerical rank thresholds, rendered pixel geometry, random sampling, or a selected favorable parameter window.

## Research consequence and evidence boundary

This visualization materially strengthens `research/weil_inertia/clues/CLUE-full-packing-orbit-quotient-characters.md`. The original coprime-order conjecture survives a broad exact finite search, while the same search suggests the stronger possibility that **any two distinct simultaneous positive-defect full-packed target primes sharing one source prime have trivial row-kernel intersection**, independent of `gcd(g_1,g_2)`.

The concentric/antipodal center law is exact, but the general zero-intersection statement is not proved here. The finite sweep is computational evidence and a clue generator, not a canonical finding. A useful next derivation is to express the two pulled-back quotient-character systems in coordinates centered on their aligned or antipodal deleted intervals and determine whether the combined equality graph must always propagate one of the zero intervals through every free cycle.
