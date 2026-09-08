# PF-221 — coefficient weight transfer reduces to a reciprocal-prime Schur commutator

**Status:** `EXACT-DERIVED + OPERATOR-THEORETIC + POSITIVE/ROUTE-NARROWING`. PF-220 isolates the remaining smooth-interface obstruction to coefficient-side cross-frequency Schur leakage: the physical `O(P_n^{-1})` seam coefficient sits on the module reached *after* `PDH/HDP` transport, while the universal weak-`S_2` estimate of PF-220 places the prime weight on the low source endpoint. There is an exact way to move a canonical reciprocal-prime envelope to that endpoint without pretending the Schur factor is local. Let

\[
D=(I+K)^{-1},\qquad 0\le D\le I,
\]

be a PF-211 normalized Schur factor, let `P` be the PF-212 low projection, `H=I-P`, and put

\[
\Omega:=\bigoplus_n \omega_n I_{\mathcal B_n},
\qquad
\omega_n:=P_n^{-1},
\]

on the normalized boundary modules. The low compression `\Omega P` is weak trace class by the same prime-density rank count as PF-210. Since the PF seam coefficient is module diagonal with `\|F_n\|\le C/P_n`, it factors as the corresponding bulk module weight times a uniformly bounded coefficient. Module locality of the normalized Poisson factor then gives, for every coefficient-adjacent cross-frequency word,

\[
\boxed{
PDH\,\Omega
=
\Omega\,PDH+P[D,\Omega]H.
}
\]

The first term is automatically in `\mathcal S_{1,\infty}` after the surrounding bounded factors are restored. Therefore the entire missing coefficient-weight transfer is concentrated in the **bounded Schur commutator** `P[D,\Omega]H` (and its adjoint orientation), not in raw `PDH` itself.

This commutator has an exact module kernel

\[
\boxed{
\Pi_m[D,\Omega]\Pi_n
=(\omega_n-\omega_m)\Pi_mD\Pi_n,
}
\]

where `\Pi_n` is the projection onto the full module `\mathcal B_n`. Thus same-module Schur mixing cancels identically, and every transported block is charged only the change in reciprocal-prime weight between its endpoints. At the local precision level PF-214 gives a further structural explanation: on every bounded finite truncation (and, in the infinite realization, whenever the corresponding commutator form is justified),

\[
[D,\Omega]=-D[K,\Omega]D,
\]

while block-Jacobi support gives

\[
\Pi_{n+1}[K,\Omega]\Pi_n
=(\omega_n-\omega_{n+1})\Pi_{n+1}K\Pi_n,
\qquad
\omega_n-\omega_{n+1}
=
\frac{P_{n+1}-P_n}{P_nP_{n+1}}.
\]

Hence the raw adjacent hopping that diverges in PF-215 is not the quantity that the coefficient-transfer problem naturally asks to control: it appears, if this precision-side representation is used, multiplied by an adjacent reciprocal-prime difference. This is a sharp new target, **not a completed estimate**. PF-215 supplies only a lower bound on raw hopping and gives no upper bound that would justify claiming cancellation.

## Claim

Use one metric label at a time and suppress it. Write the simultaneous normalized boundary space and PF-212 frequency split as

\[
\mathcal B=\bigoplus_n\mathcal B_n,
\qquad
P=\bigoplus_nP_n^{\rm lo},
\qquad
H=I-P.
\tag{1}
\]

To avoid confusing the low projection with the prime-size parameter of PF-205--PF-220, denote by `\Pi_n` the orthogonal projection onto the **whole** module `\mathcal B_n`, and retain `P_n` for the prime-scale parameter used there. Let

\[
D=\Lambda_Q^{1/2}(\Lambda_Q+\Lambda_E)^{-1}\Lambda_Q^{1/2}
=(I+K)^{-1},
\qquad 0\le D\le I,
\tag{2}
\]

with the PF-214 block-Jacobi precision

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}.
\tag{3}
\]

Define the canonical reciprocal-prime module weight

\[
\boxed{
\Omega=\bigoplus_n\omega_n I_{\mathcal B_n},
\qquad
\omega_n=P_n^{-1}.
}
\tag{4}
\]

Because the PF-212 low rank obeys

\[
\operatorname{rank}P_n^{\rm lo}\le C(1+\log P_n),
\tag{5}
\]

PF-210's singular-value counting applies to the positive block family

\[
\Omega P=\bigoplus_nP_n^{-1}P_n^{\rm lo}
\]

and gives

\[
\boxed{\Omega P\in\mathcal S_{1,\infty}.}
\tag{6}
\]

Now let `F=\bigoplus_nF_n` be any PF-205--PF-220 seam coefficient satisfying

\[
\|F_n\|\le \frac C{P_n}.
\tag{7}
\]

On the disjoint strip/buffer direct sum define the scalar bulk module weight `\Omega_Q` by the same sequence `\omega_n`. Then

\[
F=\Omega_Q\widetilde F,
\qquad
\sup_n\|\widetilde F_n\|<\infty.
\tag{8}
\]

The simultaneous strip-side normalized Poisson factor is module local, so

\[
\boxed{A^*\Omega_Q=\Omega A^*.}
\tag{9}
\]

All fixed finite matrix fibres and finite colorings are harmless as in PF-220.

Consider the unresolved one-sided cross-frequency term from PF-220,

\[
T
=M P D H A^*F G_D.
\tag{10}
\]

Using (8)--(9), then the fact that `\Omega` commutes with `P,H`, gives

\[
\begin{aligned}
T
&=M P D H\Omega A^*\widetilde F G_D\\
&=M P D\Omega H A^*\widetilde F G_D\\
&=M\Omega P D H A^*\widetilde F G_D
 +M P[D,\Omega]H A^*\widetilde F G_D.
\end{aligned}
\tag{11}
\]

Call these two summands `T_{\rm wt}` and `T_{\rm com}`. Equation (6) and the boundedness of `M,D,H,A^*,\widetilde F,G_D` imply

\[
\boxed{T_{\rm wt}\in\mathcal S_{1,\infty}.}
\tag{12}
\]

Therefore

\[
\boxed{
T\in\mathcal S_{1,\infty}
\quad\Longleftrightarrow\quad
T_{\rm com}\in\mathcal S_{1,\infty}.
}
\tag{13}
\]

The same algebra applies to the adjoint orientation. In a double-boundary word, choose either coefficient-adjacent leakage factor, factor the same module weight through the local coefficient, and obtain a weak-trace main term plus one Schur-commutator remainder; the other Schur/Poisson factors remain bounded or retain their PF-212 local ideal role. Thus (13) is not peculiar to the one-sided display: it identifies the common weight-transfer obstruction in the exact coefficient-adjacent cross-frequency family.

## 1. The commutator charges only endpoint weight differences

The main advantage of (11) is that `[D,\Omega]` is a bounded operator with a completely exact block identity; no domain statement about the possibly unbounded precision `K` is needed. Since `\Omega\Pi_n=\omega_n\Pi_n`,

\[
\begin{aligned}
\Pi_m[D,\Omega]\Pi_n
&=\Pi_mD\Omega\Pi_n-\Pi_m\Omega D\Pi_n\\
&=(\omega_n-\omega_m)\Pi_mD\Pi_n.
\end{aligned}
\tag{14}
\]

Hence

\[
\boxed{
\Pi_n[D,\Omega]\Pi_n=0
}
\tag{15}
\]

for every module. For `m>n`,

\[
\omega_n-\omega_m
=\sum_{j=n}^{m-1}(\omega_j-\omega_{j+1}),
\tag{16}
\]

so even long-range Schur transport is weighted by the telescoped variation of the reciprocal-prime sequence rather than by the absolute source or target weight.

For adjacent modules the arithmetic factor is exact:

\[
\boxed{
\omega_n-\omega_{n+1}
=
\frac{P_{n+1}-P_n}{P_nP_{n+1}}.
}
\tag{17}
\]

This is the first point in the PF-211--PF-220 smooth-interface chain where the ordered neighboring-prime increment enters the **Schur transport operator itself** rather than only the geometric coefficient envelope.

Equation (14) alone does not imply compactness or any Schatten estimate for `[D,\Omega]`: the full module spaces are infinite-dimensional, and `\Omega` without the low projection is not being claimed compact. The gain is structural placement, not an automatic ideal theorem.

## 2. PF-214 localizes the formal source of the commutator to adjacent edges

PF-214 proves that the normalized precision `K` is positive and block Jacobi:

\[
\Pi_mK\Pi_n=0
\qquad (|m-n|>1)
\tag{18}
\]

at form level. On every finite module truncation on which all blocks are bounded, the elementary inverse-commutator identity gives

\[
\boxed{
[D,\Omega]
=-D[K,\Omega]D.
}
\tag{19}
\]

Moreover the diagonal precision blocks commute with `\Omega`, while the only nonzero off-diagonal commutator blocks are

\[
\boxed{
\Pi_{n+1}[K,\Omega]\Pi_n
=(\omega_n-\omega_{n+1})
\Pi_{n+1}K\Pi_n
}
\tag{20}
\]

and their adjoints.

Equations (19)--(20) explain why an **edge-weighted precision estimate** is a plausible route to (13): the source term is local even though `D` is global, and every local edge carries the reciprocal-prime difference (17).

There is an important infinite-dimensional boundary. PF-214 allows the neighboring precision blocks to be unbounded as operators, and PF-215 proves that their bounded realizations cannot be uniformly bounded. Therefore PF-221 does **not** assume that `[K,\Omega]` is a bounded operator on the infinite boundary space or silently use (19) there. To promote (19) from finite truncations/formal cores to the full PF realization, one must prove the relevant form-domain invariance and bounded/Schatten extension. The unconditional global identity used by this finding is (14), not (19).

## 3. Why PF-215's divergent hopping does not decide the new gate

PF-215 proves, on the low symmetric constant mode, a lower bound of the form

\[
\|\Pi_{n+1}K\Pi_n\|
\gtrsim
\frac1{s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}},
\tag{21}
\]

and in particular a polynomially diverging unconditional envelope. That kills PF-214's uniform-hopping Combes--Thomas hypothesis.

Equation (20) changes the quantity that matters for coefficient transfer to

\[
(\omega_n-\omega_{n+1})\Pi_{n+1}K\Pi_n.
\tag{22}
\]

The prefactor is of reciprocal-prime-difference scale rather than reciprocal-prime scale. Heuristically, if the relevant adjacent hopping were also known from above to have its expected thin-corridor scale, the factor (17) would cancel the alarming `P^2/g` part of that scale and leave only logarithmic strength. **No such conclusion is proved here.** PF-215 supplies a lower bound, not the matching upper bound required for this cancellation argument, and consecutive gap ratios can fluctuate strongly. The correct next question is therefore an upper/form estimate for the edge-weighted commutator itself, not another bound on raw hopping.

This distinction is useful even if the answer is negative. A PF-compatible counterexample now has to show that the reciprocal-prime differences in (17), after the two resolvent factors implicit in (19) or directly in the bounded kernel (14), still fail the weak endpoint required by the exact coefficient word.

## 4. Prior art and novelty audit

No novelty is claimed for the algebraic identities `D\Omega-\Omega D`, the inverse commutator formula in the bounded setting, or the fact that a scalar diagonal weight converts a matrix commutator into endpoint differences. These are standard operator-algebra manipulations.

The closest classical locality literature also does not by itself close the PF gate. Demko, Moss and Smith, *Decay rates for inverses of band matrices*, Mathematics of Computation 43 (1984), 491--499, DOI `10.1090/S0025-5718-1984-0758197-9`, proves exponential decay of inverses of banded positive-definite matrices with rates controlled by spectral conditioning. Jaffard, *Propriétés des matrices « bien localisées » près de leur diagonale et quelques applications*, Annales de l'I.H.P. Analyse non linéaire 7 (1990), 461--476, DOI `10.1016/S0294-1449(16)30287-6`, proves inverse-closedness/locality for matrices with prescribed off-diagonal decay. Both are relevant background for PF-214's inverse-locality route, but both require quantitative locality/conditioning hypotheses that the raw PF hopping obstruction of PF-215 prevents us from importing uniformly.

The project-specific deduction in PF-221 is narrower: **the exact physical coefficient placement lets its reciprocal-prime envelope be moved across the cross-frequency Schur factor at the price of one commutator, and that commutator charges endpoint weight differences rather than absolute weights.** The literature audit did not identify this PF-specific consequence as an already named theorem; search absence is not used as novelty evidence, and no general commutator theorem is claimed.

## 5. Falsification and boundary checks

A later adversary should check all of the following.

1. The coefficient factorization (8) uses only the established uniform envelope `\|F_n\|\le C/P_n`; it does not replace the physical coefficient by a scalar model.
2. Equation (9) requires the simultaneous strip-side Poisson factor to remain module local before the global exterior Schur factor acts. If a different global identification mixes modules inside `A`, (11) must be rederived rather than assumed.
3. The low weight in (6) is `P_n^{-1}P_n^{\rm lo}`. The full boundary weight `\Omega` is not asserted to be compact or trace ideal.
4. The commutator convention is `[D,\Omega]=D\Omega-\Omega D`; with that convention the sign in (19) is negative.
5. Equation (14) is unconditional because `D` and `\Omega` are bounded. Equation (19) is only a bounded-truncation/full-domain identity when the precision commutator is actually defined in the required sense.
6. PF-215's lower bound cannot be recycled as an upper bound for (22). No cancellation estimate is established merely from matching powers heuristically.
7. Equation (13) closes only the one-sided displayed word at weak trace if the commutator remainder is controlled. Other PF-212 local high/Dirichlet factors must retain the exact ideal exponents required by their words.
8. Nothing here proves `P[D,\Omega]H\in\mathcal S_{1,\infty}`, PF-213's unweighted Schur decay, the complete first relative resolvent in weak trace class, PF-204's unsmoothed endpoint, PF-183's true-short-collar splice, wave operators, determinants/resonances, prime/clone separation, or any RH consequence.

## Consequences for the research line

PF-220's coefficient-side weight-transfer gate can now be stated without the vague instruction “move the prime weight through `PDH`.” For the smooth simultaneous-cut route, the bounded part of that move is exact: the transferred low-endpoint term is already weak trace class, and the entire unresolved cost is the commutator `P[D,\Omega]H` (or its adjoint), whose module kernel carries reciprocal-prime endpoint differences.

The next smooth-route calculation should therefore target one of two genuinely discriminating statements: prove a form/operator estimate for the edge-weighted precision commutator in (20) strong enough, after the two Schur factors and PF-212 local smoothing are restored, to give the required weak endpoint; or construct a PF-compatible family showing that even the difference-weighted Schur commutator in (14) is too large. Further work on scalar damping of `PDP`, coefficient-adjacent `P/P` sectors, or uniform raw hopping would repeat branches already closed by PF-217--PF-220.