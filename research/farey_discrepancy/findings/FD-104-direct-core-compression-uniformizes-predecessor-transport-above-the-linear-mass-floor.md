# FD-104 — direct core compression uniformizes predecessor transport above the linear mass floor

**Status:** `EXACT-DERIVED + DIRECT-SINGLE-STATE-COMPRESSION + HIGH-MASS-PREDECESSOR + PROJECTIVE-QUALITY-TRANSPORT + EFFECTIVE-LOGARITHMIC-DEPTH + LINEAR-MASS-FLOOR + FALSE-RH-ENTRY + SOURCE-SCALE-COUPLING-FRONTIER`.

`FD-097` reduced fixed-depth predecessor composition to a projective quality whose branch loss is only exponential, but its explicit remaining caveat was quantitative: the packet constructions in `FD-088`--`FD-095` were proved with fixed occupation constants, so their `o(1)` errors were not uniform once the certificate shrank with depth. `FD-103` then made that issue unavoidable by exhibiting physical dyadic carriers whose projective quality is only polynomial at logarithmic source-neutral depth.

The fixed-certificate restriction is not intrinsic to the predecessor geometry. The additive occupied block used historically in `FD-088`--`FD-089` can be removed from the one-step packet construction altogether. Starting from a **single physical state**, truncate only a terminal row tail, assign every remaining nonsquarefree row to one repeated prime, and compare it directly with the canonical predecessor `ceil(H/p)`. The two quotient-shell arguments differ by at most one, so the entire compression error is just one unit per retained row. If the nonsquarefree mass satisfies

\[
U_{H,1}\ge H^{1+\delta}
\tag{1}
\]

for any fixed `delta>0`, the terminal tail and this rowwise compression error are both `o(U_(H,1))` after taking the row cutoff sufficiently close to `H`. No occupation block, slow-doubling input, or fixed projective certificate is required.

Consequently the full odd/dyadic/head predecessor dichotomy of `FD-091`--`FD-095` becomes **uniform on every high-mass state**. For every fixed `1/2<sigma<Theta` there is a constant `b_sigma>0` such that every sufficiently large state satisfying (1) has a genuine predecessor `C<H` with

\[
\boxed{
\frac{U_{C,1}}{C^{2\sigma}}
\ge
b_\sigma\frac{U_{H,1}}{H^{2\sigma}}.
}
\tag{2}
\]

Since the historical normalized-energy maximum can only decrease when the horizon decreases, the intrinsic projective quality of `FD-097` obeys simultaneously

\[
\boxed{
\mathcal Q_\sigma(C)
\ge b_\sigma\mathcal Q_\sigma(H).
}
\tag{3}
\]

The important new point is that (2), not (3), supplies the induction currency. Starting from the sharp fixed-occupation entries of `FD-096`, the normalized occupied mass can lose only a fixed factor per predecessor. This makes predecessor composition effective for a **linear-in-`log H` number of steps**, unless the horizon has already descended into a fixed bounded range. Thus the quantitative-error obstruction named in `FD-097` is closed above the linear mass floor. The remaining frontier is to couple this long high-mass chain to the source-scale potential of `FD-102`, or otherwise recover enough frontier sharpness/tag information along the chain to force source progress.

## 1. Direct compression from one physical state

Retain

\[
V_H(r)
:=
\sqrt{w(r)}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{4}
\]

and

\[
U_H:=U_{H,1}
=
\sum_{\substack{1<r\le H\\\mu(r)=0}}|V_H(r)|^2.
\tag{5}
\]

Assume (1). By `FD-046`, for every fixed `tau>Theta`,

\[
|\mathcal H(n)|\ll_\tau n^\tau.
\tag{6}
\]

Choose a fixed `rho<1`, sufficiently close to one that

\[
(1-\rho)(2\tau-1)<\frac\delta2.
\tag{7}
\]

Put

\[
R:=\lfloor H^\rho\rfloor.
\tag{8}
\]

The nonsquarefree energy on rows `r>R` is bounded by the full row tail:

\[
\begin{aligned}
\sum_{r>R}|V_H(r)|^2
&\ll_\tau
H^{2\tau}\sum_{r>R}r^{-2\tau}\\
&\ll_\tau
H^{2\tau}R^{1-2\tau}\\
&=
H^{1+(1-\rho)(2\tau-1)+o(1)}
=o(U_H).
\end{aligned}
\tag{9}
\]

Thus almost all nonsquarefree mass lies on the single-state core

\[
\mathcal G_H
:=
\{2\le r\le R:\mu(r)=0\}.
\tag{10}
\]

For every `r in mathcal G_H`, choose deterministically the smallest prime `p=p(r)` with `p^2|r` and write

\[
r=ps.
\tag{11}
\]

Because `p|s`, removing one copy of `p` preserves the radical and hence the Jordan weight exactly:

\[
\boxed{w(s)=w(r).}
\tag{12}
\]

Now define the canonical lower horizon

\[
A_p:=\left\lceil\frac Hp\right\rceil.
\tag{13}
\]

There is no need to pass through the stitched future horizon `N_r` of `FD-088`. Directly,

\[
0\le
\frac{A_p}{s}-\frac{H}{ps}
<\frac1s<1,
\tag{14}
\]

so

\[
\boxed{
0\le
\left\lfloor\frac{A_p}{s}\right\rfloor
-
\left\lfloor\frac H{ps}\right\rfloor
\le1.
}
\tag{15}
\]

The exact source increment law from `FD-084` gives

\[
|\mathcal H(n+1)-\mathcal H(n)|\le1.
\tag{16}
\]

For each prime label let `S_(p,H)` be the lower rows `s=r/p` assigned to `p`, and dilate those lower coordinates back to their parent rows `r=ps`. Because of (12), this dilation has unit weight distortion. The parent output supports are disjoint across all labels, so if `mathcal C_H` denotes the resulting compressed vector, (15)--(16) give

\[
\boxed{
\|\mathcal C_H-P_{\mathcal G_H}V_H\|_2^2
\le \#\mathcal G_H
\le R.
}
\tag{17}
\]

But `R=H^rho=o(H^(1+delta))=o(U_H)`. Combining (9) and (17),

\[
\boxed{
\sum_p
\|P_{S_{p,H}}V_{A_p,1}\|_2^2
=\|\mathcal C_H\|_2^2
\ge(1-o(1))U_H.
}
\tag{18}
\]

Equation (18) is the quantitative replacement for the fixed-`eta` packet recurrence in `FD-089`. It starts from the actual nonsquarefree mass of one state, not from an occupied additive block.

Two scale facts will be used below. Since `p^2<=r<=R`, every first-stage prime satisfies

\[
p\le R^{1/2},
\tag{19}
\]

and therefore the odd square-reembedded horizon

\[
C_p:=4\left\lfloor\frac{A_p}{p}\right\rfloor
\tag{20}
\]

satisfies uniformly

\[
C_p=\frac{4H}{p^2}+O(1)
\gg H^{1-\rho}
\longrightarrow\infty.
\tag{21}
\]

Likewise, in the repaired dyadic nonhead branch of `FD-093`, every secondary prime is at most `R/4`, so its destination `4 floor(B/p)` is also `gg H^(1-rho)`. Thus **all** lower horizons produced from the retained core remain asymptotic physical states even though the core cutoff may be arbitrarily close to `H`.

## 2. Every branch transports a fixed fraction of normalized occupied mass

Fix

\[
\frac12<\sigma<\Theta.
\tag{22}
\]

Write

\[
M_{p,H}:=\|P_{S_{p,H}}V_{A_p,1}\|_2^2.
\tag{23}
\]

By (18), either the dyadic label carries at least half the mass asymptotically or the odd labels do.

For the odd branch, apply the exact second-prime stripping and four-adic reembedding of `FD-091`. Its Jordan distortion is bounded below by `1/zeta(2)`, all destination rows are divisible by `4`, and (21) holds uniformly. If `N_(p,H)` denotes the resulting nonsquarefree destination mask, then

\[
\sum_{p\ge3}N_{p,H}
\ge
\left(\frac1{2\zeta(2)}-o(1)\right)U_H.
\tag{24}
\]

Since

\[
C_p=\frac{4H}{p^2}(1+o(1))
\tag{25}
\]

uniformly over all occurring odd labels and

\[
\sum_{p\ge3}p^{-4\sigma}
\le\zeta(4\sigma)-1<\infty,
\tag{26}
\]

some odd label satisfies

\[
\boxed{
\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(c_{\rm odd}(\sigma)-o(1)\right)
\frac{U_H}{H^{2\sigma}},
}
\tag{27}
\]

where

\[
c_{\rm odd}(\sigma)
:=
\frac1{2\zeta(2)4^{2\sigma}(\zeta(4\sigma)-1)}.
\tag{28}
\]

This predecessor satisfies `C_p<=(4/9+o(1))H`.

If the dyadic label dominates, use exactly the support classification of `FD-093`. If at least half of the dyadic mask is already nonsquarefree after the first deflation, the half-scale state `A_2=H/2+O(1)` gives

\[
\frac{U_{A_2}}{A_2^{2\sigma}}
\ge
\left(2^{2\sigma-2}-o(1)\right)
\frac{U_H}{H^{2\sigma}}.
\tag{29}
\]

Otherwise the squarefree dyadic-terminal support has the exact decomposition

\[
M_{2,H}^{\rm term}
=
\frac34|\mathcal H(B)|^2
+
\frac34Q_{B,H}^+,
\qquad B=\frac H4+O(1).
\tag{30}
\]

If the nonhead term dominates, the odd-prime repair of `FD-093` and the convergent sum `sum p^(-2sigma)` give a predecessor with

\[
\boxed{
\frac{U_C}{C^{2\sigma}}
\ge
\left(c_{\rm term}(\sigma)-o(1)\right)
\frac{U_H}{H^{2\sigma}},
}
\tag{31}
\]

where

\[
c_{\rm term}(\sigma)
:=
\frac1{8(\zeta(2\sigma)-1)},
\tag{32}
\]

and `C<=(1/3+o(1))H`.

Finally, if the single head atom dominates, then

\[
S^2:=|\mathcal H(B)|^2\ge\left(\frac16-o(1)\right)U_H.
\tag{33}
\]

Take the fixed-fraction source retreat of `FD-095` with `lambda=1/2`,

\[
h:=\left\lfloor\frac S2\right\rfloor,
\qquad
C:=4(B-h).
\tag{34}
\]

The one-Lipschitz source law gives

\[
U_C
\ge
\left(\frac1{32}-o(1)\right)U_H,
\tag{35}
\]

and `C<=H`, hence

\[
\boxed{
\frac{U_C}{C^{2\sigma}}
\ge
\left(\frac1{32}-o(1)\right)
\frac{U_H}{H^{2\sigma}}.
}
\tag{36}
\]

This branch also gives genuine amplitude-scale physical progress:

\[
\boxed{
H-C=2S+O(1)\gg\sqrt{U_H}.
}
\tag{37}
\]

Thus the same four branch coefficients isolated in `FD-097` now hold with the **actual** parent occupied mass and with errors uniform whenever (1) holds. Define, as there,

\[
\boxed{
b_\sigma
:=
\frac12\min\left\{
 c_{\rm odd}(\sigma),
 2^{2\sigma-2},
 c_{\rm term}(\sigma),
 \frac1{32}
\right\}>0.
}
\tag{38}
\]

For every sufficiently large high-mass state, one branch therefore gives a genuine predecessor satisfying (2). The factor `1/2` in (38) absorbs all remaining uniform `o(1)` terms.

## 3. Projective quality is now a corollary of the stronger mass recurrence

Define the normalized occupied mass

\[
\boxed{
\mathfrak U_\sigma(H)
:=
\frac{U_H}{H^{2\sigma}}.
}
\tag{39}
\]

Then the one-step theorem is simply

\[
\boxed{
\mathfrak U_\sigma(C)
\ge b_\sigma\mathfrak U_\sigma(H).
}
\tag{40}
\]

For the historical complete-energy maximum retain

\[
\mathscr P_\sigma(H)
:=
\max_{2\le N\le H}\frac{E_{N,1}}{N^{2\sigma}}.
\tag{41}
\]

The intrinsic projective quality is

\[
\mathcal Q_\sigma(H)
=
\frac{\mathfrak U_\sigma(H)}{\mathscr P_\sigma(H)}.
\tag{42}
\]

Because `C<H`, one has `mathscr P_sigma(C)<=mathscr P_sigma(H)`. Hence (40) immediately yields

\[
\boxed{
\mathcal Q_\sigma(C)
\ge b_\sigma\mathcal Q_\sigma(H),
}
\tag{43}
\]

with no record-defect estimate and no fixed lower bound on `mathcal Q_sigma(H)`.

This gives the requested polynomial-quality uniformization on sharp states as a special case. If

\[
E_{H,1}=H^{2\Theta-o(1)}
\tag{44}
\]

and, for some fixed `c`,

\[
\mathcal Q_\sigma(H)
\ge H^{-c-o(1)},
\tag{45}
\]

then `mathcal Q_sigma(H)<=U_H/E_H`, so

\[
U_H\ge H^{2\Theta-c-o(1)}.
\tag{46}
\]

Therefore every

\[
\boxed{c<2\Theta-1}
\tag{47}
\]

falls inside the high-mass regime (1), and (43) applies with a fixed branch factor. In particular, the unspecified fixed-certificate `o(1)` terms of `FD-097` are **not** a barrier throughout this entire polynomial range.

The threshold (47) has a concrete meaning. The physical state always contains a linear nonsquarefree floor: for `H/2<r<=H` with `4|r`, the source quotient is `1`, `mathcal H(1)=1`, and `w(r)>=1/zeta(2)`. Hence

\[
\boxed{U_H\gg H.}
\tag{48}
\]

So `H` is not merely a proof artifact. It is the actual scale of an unavoidable low-source nonsquarefree sector. The theorem says that once occupied mass exceeds this floor by any fixed power, almost all of it can be moved into growing predecessors. At the exact linear scale, the present positive-energy argument has no power margin to discard that terminal sector. No impossibility is claimed there.

## 4. The `FD-096` entry now supports effective logarithmic composition

Take a strict-record entry horizon `H_0` supplied by `FD-096`. For fixed `1/2<sigma<Theta`, that theorem gives fixed occupation and sharp energy, hence

\[
\mathfrak U_\sigma(H_0)
=H_0^{2(\Theta-\sigma)-o(1)}.
\tag{49}
\]

As long as the current horizon stays above the fixed largeness threshold of the high-mass theorem, iterate (40). After `j` predecessor steps,

\[
\boxed{
\mathfrak U_\sigma(H_j)
\ge
b_\sigma^j
H_0^{2(\Theta-\sigma)-o(1)}.
}
\tag{50}
\]

Fix any

\[
\xi<
\frac{2(\Theta-\sigma)}{|\log b_\sigma|}.
\tag{51}
\]

For every `j<=xi log H_0`, the right side of (50) is at least `H_0^gamma` for some fixed `gamma>0`, once `H_0` is large. Therefore

\[
U_{H_j}
\ge
H_0^\gamma H_j^{2\sigma}
\ge
H_j^{2\sigma+\gamma},
\tag{52}
\]

because `H_j<=H_0`. Since `2sigma>1`, (52) is again a high-mass bound of the form (1), with a fixed positive exponent margin independent of `j`.

Thus the induction cannot fail because its packet errors outgrow a shrinking certificate. We obtain the explicit dichotomy:

\[
\boxed{
\text{either the predecessor chain reaches a fixed bounded range first,}
\quad\text{or it continues for every }
 j\le\xi\log H_0.
}
\tag{53}
\]

Along the entire realized chain, (43) also gives

\[
\mathcal Q_\sigma(H_j)
\ge
b_\sigma^j\mathcal Q_\sigma(H_0).
\tag{54}
\]

This is the effective depth relation missing from `FD-097`. It does **not** yet prove RH. The intermediate states need not remain sharp on the `2Theta` frontier for a positive fraction of `log H_0` steps, even though their occupied normalized mass remains large enough to continue the predecessor construction. Therefore the frontier-specific source quotient lower bound used in `FD-102` cannot simply be inserted at every step of (53).

That distinction is now the live gate: composition itself survives for logarithmic depth; what is missing is a theorem that couples this long high-mass chain to a persistent large source quotient, a renewed sharp mass-selection event, or another invariant that forces source-scale progress before the chain can spend its mass budget.

## 5. Stress tests and relation to `FD-103`

The direct construction deliberately removes two historical sources of loss. First, it never requires the stitched horizons `N_r` to lie inside a common occupied additive block. Equation (15) compares the parent and canonical lower quotient arguments directly. Second, it never truncates the repeated-prime labels at `p<=H^alpha`: once the parent rows are restricted to `r<=R<H`, every first repeated prime satisfies `p<=sqrt(R)`, so all odd square-reembedded destinations still tend to infinity, and the relevant `p^(-4sigma)` entropy is summable. The dyadic nonhead repair similarly has `p<=R/4` and summable `p^(-2sigma)` entropy.

A matched adversarial control explains why the high-mass hypothesis is necessary for this proof architecture. The rows with quotient `1` already contribute `gg H` nonsquarefree energy by (48). If `U_H=H^(1+o(1))`, that low-source sector may carry a macroscopic share, and repairing it can lead to bounded destination horizons. Thus the exact endpoint `U_H~H` cannot be crossed merely by choosing the core cutoff closer to `H`.

`FD-103` supplies the natural polynomial calibration. Its frontier-scaled tagged ladder has the guarantee

\[
\mathcal Q_\sigma(H)
\ge
H^{-2\Theta(1-\Theta)-o(1)}.
\tag{55}
\]

On a **sharp** parent, the new polynomial criterion (47) would cover that exponent whenever

\[
2\Theta(1-\Theta)<2\Theta-1,
\quad\text{i.e.}\quad
\Theta>\frac1{\sqrt2}.
\tag{56}
\]

This is only a calibration, not an application to the top of the `FD-103` ladder: that top state was explicitly not proved sharp. More importantly, (53) shows that a fixed polynomial quality threshold is no longer the correct continuation currency at all. The occupied normalized mass `mathfrak U_sigma` persists long enough to make the one-step errors uniformly absorbable through a logarithmic number of predecessors.

## 6. Prior-art and novelty boundary

The literature audit rechecked the classical Franel--Landau/Farey--Mertens line, Smith/GCD-matrix factorizations, floor-quotient Möbius recurrences, the 2025 rank/local-discrepancy formulas, and the July 2026 average-local-discrepancy work already represented in this line's source boundary. Those sources concern discrepancy identities, Mertens transforms, GCD/divisor algebra, or local Farey gap statistics. No located source states the single-state repeated-prime compression (15)--(18), the high-mass predecessor recurrence (40), or the resulting effective logarithmic-depth dichotomy (53).

No new external theorem is load-bearing here. The source envelope, exact increment law, Jordan Euler factors, and branch repairs are all internal consequences or already anchored dependencies of `FD-046`, `FD-084`, `FD-091`, `FD-093`, and `FD-095`. `SOURCES.md` therefore requires no update.

## 7. Updated frontier

`FD-097` left two issues entangled: exponential projective loss and nonuniform asymptotic errors. `FD-104` separates them. The projective loss remains a fixed factor per step, but the error control can be driven by the stronger quantity `U_H/H^(2sigma)`. Starting from `FD-096`, that quantity stays above the linear terminal floor for a definite multiple of `log H_0`, so predecessor composition itself is no longer restricted to a diagonal sequence of unspecified growing depth.

What remains is sharper and more arithmetic: **connect the effective high-mass chain to source-scale descent**. A useful next theorem must either keep a frontier-sized source quotient/tag alive along enough of (53) to invoke the `FD-102` potential, force recurrent re-entry into sharp mass-selected states, or exploit the head retreat (37) cumulatively. Merely improving the bookkeeping of fixed-certificate `o(1)` terms is no longer the active obstruction.