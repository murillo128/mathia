# PL-330 — The first-prime activation is norm-resolvent continuous, but graph topology still does not orient its shrinking reflection

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-TOPOLOGY-REFINEMENT + DECISIVE-ROUTE-BOUNDARY`

**Status:** `NORM-RESOLVENT-CONTINUITY-ACROSS-FIRST-PRIME + GRAPH-BRANCH-CONTINUITY + GRAPH-SMALL-SIGN-REVERSAL-PERSISTS`

## Precise claim

`PL-325` shows that the first rational-prime overlap has a maximal bounded-operator jump: after scaling to the fixed interval `I=(-1,1)`, the newly active `p=2` compressed translation has norm `1` for every aperture just above

\[
a_0=\frac12\log 2,
\]

although it is exactly zero at and below the threshold. That jump does **not** propagate to the resolvent of the canonical localized-Weil operator.

Write Suzuki's fixed-domain operator near `a_0` as

\[
\widetilde A_a=T+K_a,
\]

where `T` is the aperture-independent logarithmic principal operator and `K_a` is bounded self-adjoint. In a sufficiently small neighborhood of `a_0`, all non-arithmetic bounded terms vary in operator norm and the only nonsmooth source event is the `p=2` channel. If

\[
\tau(a)=\frac{\log2}{a},
\qquad \varepsilon(a)=2-\tau(a),
\]

then for `a>a_0` that channel is, up to its smooth bounded scalar coefficient, the edge-flip operator `C_{\tau(a),1}` of `PL-325`, supported on edge strips of width `\varepsilon(a)`. As `a\downarrow a_0`,

\[
\boxed{
C_{\tau(a),1}\longrightarrow0
\quad\text{strongly on }L^2(-1,1),
\qquad
\|C_{\tau(a),1}\|=1.
}
\tag{PL330-1}
\]

Since `T+K_{a_0}` has compact resolvent, this strong-but-not-norm convergence is enough to upgrade the **full self-adjoint family** to norm-resolvent continuity:

\[
\boxed{
\|(\widetilde A_a-z)^{-1}-(\widetilde A_{a_0}-z)^{-1}\|
\longrightarrow0
\qquad(a\to a_0)
}
\tag{PL330-2}
\]

for every `z\in\mathbb C\setminus\mathbb R`. Hence every isolated finite spectral cluster has norm-continuous Riesz projection across the prime activation. In particular, if an eigenvalue at `a_0` is simple, its normalized eigenvector can be chosen to converge in `L^2`; in fact it converges in the graph norm of the fixed logarithmic operator `T`.

This removes one obstruction left explicit in `PL-329`: the raw norm jump of the prime translation does **not** prevent spectral/eigenbranch transport through the first source event.

However, the improvement is not the missing sign mechanism. The critical sign-reversing layer from `PL-327` can itself be chosen to vanish in the same fixed `T`-graph topology. If

\[
L_\delta=\log\frac{a_\delta}{\delta},
\qquad
a_\delta=a_0+\delta,
\]

and

\[
r_\delta(t)
=A L_\delta^{-1/2}\eta(t/\delta),
\qquad
\eta\in C_c^\infty((0,2)),
\qquad
\eta(2-s)=-\eta(s),
\tag{PL330-3}
\]

then

\[
\boxed{
\|r_\delta\|_2+\|Tr_\delta\|_2\longrightarrow0,
}
\tag{PL330-4}
\]

while for a canonical critical boundary profile `B_\delta` with fixed nonzero coefficient `C`, `PL-327` gives

\[
H_\delta(B_\delta+r_\delta)
=
\left(2C^2-A^2\|\eta\|_2^2+o(1)\right)
\frac{\delta}{L_\delta}.
\tag{PL330-5}
\]

Choosing `A^2\|\eta\|_2^2>2C^2` reverses the first-prime reflection although the perturbation tends to zero in the full logarithmic graph norm.

Thus the topology hierarchy is now exact:

\[
\text{bounded-operator norm}
\quad\text{is too strong and sees a fake jump,}
\]

whereas

\[
\text{norm-resolvent / }T\text{-graph continuity}
\quad\text{is available but still too weak to orient the shrinking arithmetic channel.}
\]

The live gate of `PL-329` therefore remains genuinely **source-amplitude / coefficient** control at the moving endpoint scale, not ordinary spectral continuity through the activation.

## 1. The edge flip converges strongly although its norm stays one

Let `b=\log2` and use the fixed interval `I=(-1,1)`. For `a>a_0=b/2`, `PL-325` identifies the scaled `p=2` channel with the symmetric compressed shift at lag

\[
\tau(a)=\frac ba<2.
\]

Its nonzero action is confined to

\[
E_a^-=(-1,-1+\varepsilon(a)),
\qquad
E_a^+=(1-\varepsilon(a),1),
\qquad
\varepsilon(a)=2-\tau(a)\downarrow0.
\]

The operator swaps the two edge strips unitarily and vanishes on the middle interval. Consequently, for every fixed `f\in L^2(I)`,

\[
\|C_{\tau(a),1}f\|_2^2
\le
\int_{E_a^-\cup E_a^+}|f(x)|^2\,dx
\longrightarrow0
\]

by absolute continuity of the `L^2` integral. This proves strong convergence to zero. At the same time `PL-325` gives

\[
\|C_{\tau(a),1}\|=1
\]

for every `a>a_0`, because the two shrinking edge spaces still contain normalized vectors. The activation is therefore a textbook strong/not-norm limit, but here it arises from the exact first-prime geometry.

In Suzuki's fixed-domain representation, write

\[
K_a-K_{a_0}=D_a.
\]

Near `a_0`, no other prime power activates. The scalar and continuous-completion pieces vary in operator norm, while the `p=2` piece is a uniformly bounded smooth scalar multiple of `C_{\tau(a),1}`. Hence

\[
\boxed{
D_a\to0\text{ strongly},
\qquad
\sup_{|a-a_0|<\epsilon}\|D_a\|<\infty.
}
\tag{PL330-6}
\]

The same conclusion holds from below, where the `p=2` channel is absent and only the norm-continuous pieces move.

## 2. Compact resolvent converts strong activation into norm-resolvent continuity

Source 56 (Suzuki), as used throughout `PL-265` and `PL-287`, gives a compact embedding of the logarithmic form domain into `L^2(I)` and therefore compact resolvent for every fixed localized-Weil realization. Set

\[
A_0=\widetilde A_{a_0}=T+K_{a_0},
\qquad
R_0(z)=(A_0-z)^{-1}.
\]

For non-real `z`, `R_0(z)` is compact. A uniformly bounded strongly convergent family converges uniformly on compact subsets of the Hilbert space, so (PL330-6) implies

\[
\boxed{
\|D_aR_0(z)\|\longrightarrow0.
}
\tag{PL330-7}
\]

For `A_a=A_0+D_a`, the resolvent identity is legitimate because `D_a` is bounded and all operators have the common domain `D(T)`:

\[
R_a(z)-R_0(z)
=-R_a(z)D_aR_0(z).
\]

Self-adjointness gives

\[
\|R_a(z)\|\le\frac1{|\operatorname{Im}z|},
\]

uniformly in `a`. Combining with (PL330-7) proves (PL330-2).

No general novelty is claimed for the lemma `uniformly bounded strong convergence times a compact operator implies norm convergence`, nor for the resolvent identity. The line-specific point is that the exact shrinking first-prime flip of `PL-325` falls precisely into that mechanism, so its unit operator-norm jump is invisible after composition with the compact localized-Weil resolvent.

## 3. Isolated eigenspaces and simple eigenvectors pass through the activation

Norm-resolvent convergence gives the usual spectral consequence without requiring bounded-operator norm convergence of `K_a`. Let `\Gamma` be a contour enclosing an isolated finite spectral cluster of `A_0` and no other spectrum. For all sufficiently close `a`, define

\[
P_a=\frac1{2\pi i}\int_\Gamma (A_a-z)^{-1}\,dz.
\]

Then

\[
\boxed{\|P_a-P_0\|\to0.}
\tag{PL330-8}
\]

The rank is therefore locally constant. If the cluster is a simple eigenvalue `\lambda_0`, one can choose normalized eigenvectors `u_a` with a fixed sign/phase convention such that

\[
\lambda_a\to\lambda_0,
\qquad
u_a:=u_a-u_0\to0\quad\text{in }L^2.
\]

There is a further useful upgrade. The eigen-equation gives

\[
Tu_a=(\lambda_a-K_a)u_a.
\]

Because `u_a\to u_0`, `\lambda_a\to\lambda_0`, and `K_a-K_{a_0}=D_a\to0` strongly with uniformly bounded norm,

\[
D_au_a
=D_a(u_a-u_0)+D_au_0
\longrightarrow0.
\]

The norm-continuous remainder is harmless, and therefore

\[
Tu_a\to Tu_0\quad\text{in }L^2.
\]

Thus

\[
\boxed{
\|u_a-u_0\|_2+\|T(u_a-u_0)\|_2\to0.
}
\tag{PL330-9}
\]

This is stronger than the source-static `H^\log` branch continuity in `PL-287`: it crosses the actual first-prime source event and uses the operator graph topology. It also sharpens the bookkeeping caveat in `PL-289`, which left source activations to separate analysis.

## 4. The critical sign-reversing layer is nevertheless graph-small

The graph improvement might appear to supply exactly the uniformity missing in `PL-326`--`PL-329`. It does not.

Use the critical counterfamily from `PL-327`, translated to an endpoint if necessary. Since translations contribute only a unimodular Fourier phase, it is enough to estimate

\[
r_\delta(t)=A L_\delta^{-1/2}\eta(t/\delta)
\]

on the real line, with `\eta\in C_c^\infty((0,2))`. Its Fourier transform has the scaling

\[
\widehat r_\delta(\xi)
=A\delta L_\delta^{-1/2}\widehat\eta(\delta\xi)
\]

up to the harmless endpoint phase. Hence

\[
\|r_\delta\|_2^2
=A^2\frac{\delta}{L_\delta}\|\eta\|_2^2.
\tag{PL330-10}
\]

For the whole-line logarithmic multiplier

\[
m(\xi)=\log|\xi|+\gamma,
\]

change variables `\zeta=\delta\xi`. Since

\[
L_\delta=\log(1/\delta)+O(1)
\]

and `\widehat\eta` is Schwartz,

\[
\begin{aligned}
\|m(D)r_\delta\|_2^2
&=
\frac{A^2\delta}{L_\delta}
\frac1{2\pi}
\int_{\mathbb R}
\left(\log\frac{|\zeta|}{\delta}+\gamma\right)^2
|\widehat\eta(\zeta)|^2\,d\zeta\\
&=O(\delta L_\delta)
\longrightarrow0.
\end{aligned}
\tag{PL330-11}
\]

The logarithmic singularity at `\zeta=0` is square-integrable against a Schwartz function; the antisymmetry of `\eta` in fact gives zero mean, but that extra cancellation is not needed for the estimate.

For a smooth bump supported strictly inside the interval, the fixed-domain principal operator `T` is the restriction of this whole-line multiplier, so

\[
\|Tr_\delta\|_2
\le \|m(D)r_\delta\|_2
=O\!\left(\sqrt{\delta L_\delta}\right).
\]

Together with (PL330-10), this proves (PL330-4).

But `PL-327` computes the first-prime reflection exactly. For

\[
B_\delta(t)=C\left(\log\frac{2a_\delta}{t}\right)^{-1/2}
\]

and the reflection-antisymmetric `\eta`,

\[
H_\delta(B_\delta+r_\delta)
=
\left(2C^2-A^2\|\eta\|_2^2+o(1)\right)
\frac{\delta}{L_\delta}.
\]

Thus an arbitrarily graph-small moving perturbation can reverse the sign by choosing `A` above the fixed critical threshold. The issue is not that the perturbation is large in the natural Hilbert/operator topology; it is large only **relative to the much smaller sign reserve** `\delta/L_\delta` of the shrinking reflection layer.

This strengthens the boundary in `PL-326`, which deliberately made no claim about the full localized-Weil graph norm: at the sharp half-log scale of `PL-327`, the hostile perturbation is small even there.

## 5. Prior-art and novelty audit

The load-bearing external operator facts are already stored in source 56 and used in `PL-265`, `PL-287`, and `PL-289`: Suzuki's fixed-domain decomposition, common logarithmic principal part, bounded aperture-dependent remainder, compact form embedding/discrete spectrum, and continuity of the localized spectral problem. `PL-325` independently reconstructs the exact first-prime edge flip and its norm jump.

A targeted audit of Suzuki's 2026 paper and the public first-prime material already audited in `PL-325` did not locate the specific norm-resolvent refinement (PL330-2), the graph-branch consequence (PL330-9), or the graph-small critical counterfamily (PL330-10)--(PL330-11). Search absence is not evidence of novelty. No general functional-analytic novelty is claimed: the compact-resolvent upgrade from bounded strong convergence is standard, and the Fourier scaling calculation is elementary.

The durable line-specific delta is the combination of these established ingredients at the exact arithmetic source event. It separates three notions that had remained entangled in the preceding findings:

1. the prime overlap is discontinuous in bounded-operator norm;
2. the full localized-Weil spectral problem is nevertheless norm-resolvent continuous, with graph-continuous isolated eigenbranches;
3. even that stronger continuity does not orient the first-prime reflected correlation, because the sharp critical hostile layer is graph-small.

No new entry in `research/prime_lattice/SOURCES.md` is required.

## 6. Adversarial boundary checks

**No contradiction with `PL-325`.** The edge flip still has norm one for every positive overlap. Norm-resolvent continuity follows only after the strongly vanishing edge operator is composed with the compact resolvent of the threshold operator.

**Compactness is essential.** Strong convergence of bounded perturbations alone does not imply norm-resolvent convergence in this argument. The compact localized-Weil resolvent is the mechanism converting strong convergence into operator-norm convergence after one resolvent factor.

**No claim of differentiability in aperture.** Norm-resolvent continuity across the source event does not give a norm derivative. The support edge appears nonsmoothly, and the first-prime channel remains discontinuous as a bounded operator.

**No contradiction with `PL-303`.** Graph continuity is much weaker than BV control. `PL-303` proves that even an ordinary localized-Weil resolvent with a spectral gap cannot map arbitrary `L^2` forcing boundedly into `BV_0`.

**The graph-small counterfamily is not an eigenstate.** It proves that graph-topological continuity by itself cannot determine the sign. The actual completed-Weil eigen-equation may still exclude the hostile component through source-amplitude control, coefficient noncollapse, a supercritical residual estimate, or another signed identity.

**No RH consequence is claimed.** The result is local to the first prime threshold. It removes an artificial topology obstruction and simultaneously proves that this removal does not solve the RH-facing orientation problem.

## Consequence for the live research target

`PL-329` left two issues intertwined: transport of the actual isolated state through the operator-norm-discontinuous source activation, and quantitative suppression of the critical moving-layer residual. The first issue is now separated from the second.

For an isolated simple threshold eigenvalue, the exact prime activation permits norm-resolvent, spectral-projection, `L^2`, and fixed-logarithmic-graph transport. None of these topologies can by itself force

\[
H_\delta(u_{a_\delta})>0.
\]

The remaining useful theorem must therefore estimate information that is **stronger at the shrinking layer than graph convergence**. In the notation of `PL-329`, the sharp source-amplitude gate

\[
\frac{1+S_\delta}{|C_\delta|\sqrt{L_\delta}}\to0
\]

remains a correctly scaled target: the graph-small counterfamily that reverses the sign is precisely capable of generating source amplitude at the critical `\sqrt{L_\delta}` scale. The next step should therefore prove, for the actual completed-Weil eigenbranch, a uniform subcritical source amplitude together with noncollapse of `C_\delta`, rather than spending further effort on ordinary operator/eigenvector continuity through `a_0`.