# NB-065 — persistent target transmission has a finite spectral budget

**Status:** `EXACT-DERIVED + SUMMABLE-TARGET-TRANSMISSION-BUDGET + MOVING-THRESHOLD-TRANSVERSALITY + NECESSARY-PERSISTENCE-CONDITION + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-064` proves that persistent collective late-quotient leakage can survive only if the normalized visible target direction concentrates in singular values of the one-cell forward-memory map `Gamma_R` tending to zero. The convergence obtained there is in fact quantitatively stronger: the target-weighted forward transmission has a **finite total budget** across all logarithmic cells.

Retain the notation of `NB-063` and `NB-064`,

\[
p_R=P_{\mathcal G_R}J_Rh_*,
\qquad
x_R=(J_{R+1}-J_R)h_*,
\qquad
T_R=\Gamma_R^*\Gamma_R,
\tag{1}
\]

and

\[
c_R:=\delta_R^2-\delta_{R+1}^2\ge0.
\tag{2}
\]

Define the unnormalized filtered target transmission

\[
\mathfrak t_R
:=
\left\langle
p_R,T_R(I+T_R)^{-1}p_R
\right\rangle.
\tag{3}
\]

Then unconditionally

\[
\boxed{
\sum_{R\ge2}\mathfrak t_R<\infty.
}
\tag{4}
\]

More precisely,

\[
\boxed{
\sum_{R\ge2}\mathfrak t_R
\le
2\sum_{R\ge2}\|x_R\|^2
+2\sum_{R\ge2}c_R
\le
2\|h_*\|^2+2\delta_2^2.
}
\tag{5}
\]

If the collective defect persists,

\[
\delta_\infty:=\lim_{R\to\infty}\delta_R>0,
\tag{6}
\]

then `||p_R|| -> delta_infinity`, so the normalized quantity from `NB-064`,

\[
u_R:=\frac{p_R}{\|p_R\|},
\qquad
q_R:=
\left\langle
u_R,T_R(I+T_R)^{-1}u_R
\right\rangle,
\tag{7}
\]

is not merely `o(1)` but summable:

\[
\boxed{
\sum_R q_R<\infty.
}
\tag{8}
\]

Consequently persistent leakage imposes a moving-threshold restriction stronger than the fixed-threshold criterion of `NB-064`. Let `eta_R>0`, and let `E_R^{\ge\eta_R}` be the spectral projection of `T_R` onto `[eta_R^2,\infty)`. If for some `kappa>0` and some index set `S`

\[
\|E_R^{\ge\eta_R}u_R\|\ge\kappa
\qquad(R\in S),
\tag{9}
\]

then persistence forces

\[
\boxed{
\sum_{R\in S}
\frac{\eta_R^2}{1+\eta_R^2}
<\infty.
}
\tag{10}
\]

Equivalently, if the series in (10) diverges while (9) holds, then necessarily

\[
\boxed{
\delta_\infty=0.
}
\tag{11}
\]

For thresholds `eta_R<=1`, a simpler sufficient condition is

\[
\sum_{R\in S}\eta_R^2=\infty.
\tag{12}
\]

Thus a persistent defect cannot merely drive the target toward smaller singular values. Any fixed positive fraction of target mass that recurs in a transmitted sector must have a transmission floor that is **square-summable in scale**. For example, fixed target mass transmitted at singular value at least `c R^{-alpha}` for every sufficiently large `R` already rules out persistence whenever `alpha<=1/2`. Sparse subsequences remain allowed exactly when their squared transmission floors are summable.

## 1. The one-cell capture law gives a summable filtered transmission

`NB-064` uses

\[
A_R:=(I+\Gamma_R\Gamma_R^*)^{-1/2}
\tag{13}
\]

and the exact `NB-063` capture identity to obtain

\[
\|A_Rz_R\|^2=c_R,
\qquad
z_R=x_R^\circ-\Gamma_Rp_R.
\tag{14}
\]

Since `A_R` is a contraction,

\[
\begin{aligned}
\|A_R\Gamma_Rp_R\|
&=\|A_R(x_R^\circ-z_R)\|\\
&\le \|x_R\|+\sqrt{c_R}.
\end{aligned}
\tag{15}
\]

The standard intertwining identity gives

\[
\|A_R\Gamma_Rp_R\|^2
=
\left\langle
p_R,T_R(I+T_R)^{-1}p_R
\right\rangle
=
\mathfrak t_R.
\tag{16}
\]

Therefore

\[
\mathfrak t_R
\le
2\|x_R\|^2+2c_R.
\tag{17}
\]

The cells supporting the `x_R` are pairwise orthogonal, so

\[
\sum_{R\ge2}\|x_R\|^2\le\|h_*\|^2.
\tag{18}
\]

The capture increments telescope because `delta_R^2` is decreasing:

\[
\sum_{R\ge2}c_R
=
\delta_2^2-\delta_\infty^2
\le\delta_2^2.
\tag{19}
\]

Summing (17) proves (5), hence (4). No persistence assumption is needed for this part.

The distinction from the pointwise conclusion in `NB-064` is material. Equation (4) says that appreciable target-weighted forward-memory transmission can occur only with finite accumulated energy over the entire causal flag; it cannot recur indefinitely at a nonsummable strength even if its singular direction changes at every cell.

## 2. Persistence converts the unnormalized budget into a normalized one

`NB-061` and `NB-064` give

\[
\delta_R^2
=
\|(I-J_R)h_*\|^2+\|p_R\|^2.
\tag{20}
\]

Since `J_R -> I` strongly, the first term tends to zero. Under (6), therefore

\[
\|p_R\|^2\longrightarrow\delta_\infty^2>0.
\tag{21}
\]

For all sufficiently large `R`, say

\[
\|p_R\|^2\ge\frac12\delta_\infty^2.
\tag{22}
\]

By (3) and (7),

\[
q_R=\frac{\mathfrak t_R}{\|p_R\|^2}
\le
\frac{2}{\delta_\infty^2}\mathfrak t_R
\tag{23}
\]

for all such `R`. Equation (4) then proves (8). The finite initial segment is irrelevant.

This is the exact analogue, for the current one-cell target-memory carrier, of the telescoping visibility principle already isolated much earlier in `NB-015`: a nonzero limiting defect leaves only a finite accumulated budget for the mechanism that could otherwise force further target capture. The present result is not a new abstract summability principle; its line-local content is identifying the `NB-063/064` filtered singular transmission as the relevant budget and obtaining it directly from the one-cell capture law.

## 3. Moving singular thresholds are controlled by the budget

On the spectral sector `T_R>=eta_R^2`, the multiplier

\[
f(t)=\frac{t}{1+t}
\tag{24}
\]

is at least

\[
\frac{\eta_R^2}{1+\eta_R^2}.
\tag{25}
\]

Therefore

\[
q_R
\ge
\frac{\eta_R^2}{1+\eta_R^2}
\|E_R^{\ge\eta_R}u_R\|^2.
\tag{26}
\]

If (9) holds, then

\[
q_R
\ge
\kappa^2
\frac{\eta_R^2}{1+\eta_R^2}
\qquad(R\in S).
\tag{27}
\]

Summability of `q_R` under persistence proves (10). Its contrapositive gives (11).

When `eta_R<=1`,

\[
\frac{\eta_R^2}{1+\eta_R^2}\ge\frac12\eta_R^2,
\tag{28}
\]

so divergence of the simpler square sum in (12) suffices. In particular, if (9) holds eventually with `eta_R=cR^{-alpha}`, then `sum eta_R^2` diverges for `alpha<=1/2`, yielding `delta_infinity=0`.

This strictly extends the fixed-`eta` transversality test of `NB-064`. A fixed positive threshold makes (10) diverge immediately on every infinite `S`; `NB-065` also admits thresholds tending to zero and quantifies how rapidly they must collapse if persistent leakage is to remain possible.

## 4. Adversarial controls and failure modes

The conclusion is one-sided. Summability of `q_R` does not imply persistence, and failure of a proposed divergent-threshold criterion does not produce a nonzero defect. In the flat `O=1` control, `Gamma_R=0`, so

\[
\mathfrak t_R=q_R=0
\tag{29}
\]

whenever the normalized quantity is defined, while the actual target tail still vanishes. The budget is therefore a necessary condition on the persistence branch, not a sufficient characterization of it.

No lower singular bound for all of `G_R` is asserted. The spectral mass in (9) is the distinguished target mass, exactly as required by the line-specific target-aware control. Nor is there any density assumption on `S`: a sparse recurrence set can evade (11) when its squared thresholds are summable. This prevents converting isolated well-transmitted scales into a closure claim.

The argument also does not import an RH-scale zeta or Möbius estimate. It uses only the exact `NB-063` one-cell recursion, the `NB-064` filtered-transmission identity, orthogonality of disjoint Paley--Wiener cells, and monotone telescoping of the defect distance.

## 5. Prior-art and novelty boundary

Summability from telescoping Hilbert-space energy decrements and the spectral inequality behind (26) are standard functional-analysis facts. Within this line, `NB-015` already exhibits the same abstract architecture for a different semigroup-enrichment visibility budget, so no novelty is claimed for the telescoping method itself.

A targeted literature audit found contemporary Nyman--Beurling work using Friedrichs/subspace-angle geometry (Jongho Yang, 2026) and Gram spectral/block-compressibility methods after Mellin smoothing (Hugh Carvill, 2025). Those works confirm that angle and singular/Gram language are established prior-art territory. The audit did not locate the source-specific statement here: the exact `NB-063` one-cell capture recursion forces a finite accumulated budget for the canonical target's filtered forward-memory transmission, yielding the moving-threshold criterion (10). No priority claim is made.

No specialized external theorem is load-bearing for the derivation, and the relevant neighboring literature is already represented by the line's existing source anchors where needed. `SOURCES.md` therefore requires no change.

## 6. Consequence for the live Nyman--Beurling frontier

`NB-064` reduced persistent collective leakage to target tracking of approximate right-kernel modes. `NB-065` now quantifies how severe that tracking must be. It is not enough that the target-bearing singular values tend to zero: whenever a fixed fraction of the target occupies a transmitted sector, the corresponding singular-value floor must be square-summable over the recurrence scales.

The next sufficient target can therefore be weaker than a fixed positive transmission gap. It is enough to prove an oracle-free source estimate producing a set `S`, a fixed `kappa>0`, and thresholds `eta_R` such that

\[
\|E_R^{\ge\eta_R}u_R\|\ge\kappa
\quad(R\in S),
\qquad
\sum_{R\in S}\eta_R^2=\infty
\tag{30}
\]

with `eta_R<=1`. Any such target-aware nonsummable transmission floor rules out a persistent collective defect. The remaining arithmetic problem is therefore not to prevent all near-kernel modes, but to show that the canonical target cannot track them with transmission collapsing at a square-summable rate across every sufficiently rich sequence of cells.