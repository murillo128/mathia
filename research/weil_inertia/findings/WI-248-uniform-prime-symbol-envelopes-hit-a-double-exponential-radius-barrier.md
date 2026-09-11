# WI-248 — Uniform prime-symbol envelopes hit a doubly exponential finite-radius barrier

## Status

- **Evidence:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.
- **Scope:** this closes a specific source-side route after `WI-241`--`WI-247`: proving finite-radius Weil positivity by replacing the finite von Mangoldt cosine comb with a radius-dependent **uniform pointwise constant envelope**. It does not rule out phase-sensitive, autocorrelation-specific, averaged, or first-zero-mode estimates for the signed source.
- **Novelty boundary:** the one-stroke finite-window reduction and its doubly exponential envelope barrier are stated in Marcus Chuk's recent preprint `arXiv:2608.24827` (current manuscript dated 4 Sep 2026). The line-local contribution here is to audit the load-bearing recurrence argument independently and connect the barrier explicitly to the odd first-crossing/source program of `WI-241`--`WI-247`. No priority claim is made.

## Claim

For a support radius `L>0`, write the finite prime-power cosine comb in the geometric Weil symbol as

\[
P_L(t)
:=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n),
\qquad
A_L:=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}.
\]

Then

\[
\boxed{
\limsup_{t\to\infty}P_L(t)=A_L.
}
\]

Consequently every uniform tail envelope

\[
P_L(t)\le C_L\qquad(t\ge T_0)
\]

must satisfy

\[
\boxed{C_L\ge A_L.}
\]

Thus no argument that discards the prime phases and retains only a constant pointwise upper envelope can beat the triangle/supremum constant `A_L`, even after moving arbitrarily far out in frequency.

The archimedean part of the Weil symbol grows only logarithmically. In the normalization used by Chuk,

\[
\Psi_L(t)
=\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi-P_L(t),
\]

and a pointwise positive tail based only on the envelope `P_L\le A_L` therefore cannot begin before frequency of exponential size in `A_L`. Chuk's one-stroke reduction makes this explicit with the necessary threshold

\[
\boxed{T_1(L)=2\pi e^{A_L}.}
\]

By partial summation and the Prime Number Theorem,

\[
A_L
=2\sum_{n<e^{2L}}\frac{\Lambda(n)}{\sqrt n}
=(4+o(1))e^L,
\]

so

\[
\boxed{
T_1(L)
=2\pi\exp\!\big((4+o(1))e^L\big).
}
\]

Any finite-basis implementation that must resolve frequencies up to this tail cutoff consequently has doubly exponential scale in the support radius. The obstruction is not a loose PNT estimate: the prime phases themselves recur arbitrarily close to simultaneous alignment and force the same worst-case comb height on every sufficiently late tail.

For the current `weil_inertia` source branch, this means that the finite odd zero mode forced by `WI-247` cannot plausibly be excluded at arbitrary radius by an operator-norm/triangle strategy that replaces the signed finite-prime source by its uniform symbol supremum. A scalable theorem must retain information deliberately destroyed by that envelope: the directional autocorrelation of the first-crossing vector, non-alignment of prime phases on the relevant spectral mass, a weighted/averaged source invariant, or another zeta-specific finite-radius constraint.

## 1. Independent recurrence audit

Only finitely many primes occur in `P_L`. Write every prime power as `n=p^k`. Unique factorization implies that the numbers

\[
\{\log p: p<e^{2L}\}
\]

are linearly independent over `\mathbb Q`: a rational relation clears denominators to an integer relation, which exponentiates to a multiplicative relation among distinct primes and is therefore trivial.

Kronecker--Weyl recurrence on the resulting finite torus implies that for every `epsilon>0` and every `T_0`, there is `t>T_0` such that simultaneously for all relevant primes

\[
\operatorname{dist}(t\log p,2\pi\mathbb Z)<\epsilon.
\]

For a fixed finite set of powers `p^k`, choosing the prime phases sufficiently close to zero also makes every `k t\log p` sufficiently close to zero modulo `2\pi`. Hence every cosine in `P_L(t)` is arbitrarily close to `1`, while all coefficients `2\Lambda(n)/\sqrt n` are positive. Therefore

\[
\limsup_{t\to\infty}P_L(t)=A_L.
\]

The opposite inequality `P_L(t)\le A_L` is immediate from `cos\le1`. This proves that `A_L` is not merely a crude triangle bound: it is the exact recurrent tail supremum.

## 2. The radius scale of the obstruction

Let `X=e^{2L}`. Partial summation against `\psi(x)=\sum_{n\le x}\Lambda(n)=x+o(x)` gives

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
=2\sqrt X+o(\sqrt X),
\]

and therefore

\[
A_L=(4+o(1))e^L.
\]

Meanwhile the digamma asymptotic gives

\[
\Re\psi\!\left(\frac14+\frac{it}{2}\right)
=\log\frac{|t|}{2}+O(t^{-2}).
\]

So a proof that lower-bounds the Weil symbol by replacing `P_L(t)` with the constant `A_L` cannot obtain a positive tail until `log t` has overtaken `A_L` (up to fixed normalization constants). Chuk's Theorem 7 packages this in the exact sufficient-tail parameter `T_1=2\pi e^{A_L}`, and Theorem 3 records the resulting doubly exponential matrix-size barrier for that one-stroke certificate family.

The important point for this line is qualitative and exact: shifting the start of the tail does not make the worst prime phase smaller. Arbitrarily late near-alignments survive.

## 3. Relation to the finite odd first crossing

`WI-247` proves that if RH fails, there is a finite first odd radius `a_*^-` and a normalized odd zero mode `v_*` with

\[
Q_W^{a_*^-}(v_*)=0.
\]

`WI-241` rewrites the odd form as

\[
Q_W^a(v)=Q_{\rm mean}(v)-2\Delta_\Lambda^a(v),
\]

and `WI-244`--`WI-246` quantify the finite-radius mean reserve. The live problem is therefore to show that the actual signed source on the first-crossing class cannot pay that reserve.

A uniform prime-symbol estimate does not use the first-crossing class at all: it bounds the finite shift/cosine source on the whole `L^2` window by the worst simultaneously aligned prime phases. The recurrence calculation above shows that this loss is intrinsic to that compression. It cannot be repaired by a better constant, a larger frequency cutoff, or a sharper asymptotic evaluation of the total von Mangoldt mass.

This is narrower than the global barrier of `WI-243`. `WI-243` shows that even a weak subexponential bound on one signed large-radius discrepancy is already RH-equivalent. The present barrier says something different: **before** reaching that arithmetic difficulty, a phase-blind uniform symbol envelope has already destroyed exactly the cancellation one would need to scale a compact-window positivity certificate.

The surviving source-side targets are therefore directional rather than uniform. Examples include an estimate only on the first-crossing zero mode, a theorem preventing simultaneous prime-phase alignment on the spectral mass of that mode, or a bilinear/averaged source constraint that uses the zero-mode equation rather than the operator norm of the complete prime comb.

## 4. Audit of the recent compact-window claim

Chuk's preprint also reports an unconditional computer-assisted lower certificate at `L=0.8`:

\[
Q(f)\ge 8.9\times10^{-18}\|f\|_2^2
\]

for arbitrary complex `f` supported in `[-0.8,0.8]`, with an odd-sector certificate quoted at about `8.2\times10^{-15}` and a simple even ground state. It also reports geometric-side interval upper bounds, including `2.27\times10^{-17}` at `L=0.8` and values down to about `3.2\times10^{-283}` at `L=2`.

Those numerical certificates are **not imported here as established line evidence**. In the targeted audit for this pass, the arXiv manuscript supplies the algorithmic description (Legendre truncation, Gauss--Legendre quadrature error control, verified Cholesky residual, interval arithmetic), but no independent public replay artifact was located. They therefore remain `RECENT-PREPRINT + COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY` for Mathia purposes.

The analytic recurrence/barrier used in this finding does not depend on those computations. It is checkable directly from the finite cosine comb, unique factorization/Kronecker--Weyl recurrence, the PNT, and the standard digamma asymptotic.

## 5. Prior art and provenance

Primary recent source:

- Marcus Chuk, **Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law**, arXiv:2608.24827, submitted 25 Aug 2026, current manuscript dated 4 Sep 2026. Theorem 7 gives the one-stroke reduction; Lemma 6 identifies the optimal comb constant; Theorem 3 states the doubly exponential barrier. The same manuscript contains the `L=0.8` computational positivity claim, which this finding deliberately keeps below established-evidence status pending independent replay.

Classical inputs used in the independent audit are the Kronecker--Weyl simultaneous approximation/equidistribution theorem, the Prime Number Theorem in Chebyshev form `\psi(X)\sim X`, and the standard vertical-line asymptotic of the digamma function.

Repository-local comparison:

- `WI-241` isolates the signed von Mangoldt discrepancy after exact pole/main-density cancellation.
- `WI-242` shows that absolute PNT envelopes destroy the cancellation at the slow-dilate scale.
- `WI-243` shows that generic subexponential control of one signed discrepancy is already RH-equivalent.
- `WI-244`--`WI-246` quantify and optimize the finite-radius odd mean reserve.
- `WI-247` forces a finite odd zero mode under every RH failure.

The present finding closes the remaining tempting **uniform symbol-envelope** shortcut between the finite source and that zero mode. It does not close phase-sensitive source estimates.

## Falsification and next gate

The exact no-go is falsified only if the finite prime logarithms fail the stated rational independence/recurrence step, if the prime-power phases cannot be simultaneously inherited from prime-phase recurrence, or if `A_L` does not have the PNT asymptotic above. All three checks are elementary/classical.

The next high-value gate is not another bound on `\sup_t P_L(t)`. It is to exploit the **specific first-crossing vector** from `WI-247`: derive a source estimate that is weaker than global RH-equivalent discrepancy control but stronger than the phase-blind operator norm. A useful candidate must retain where the spectral mass of `v_*` lies or impose a bilinear constraint coming from the zero-mode equation.