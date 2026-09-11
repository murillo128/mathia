# PF-280 — one-sided frequency-decoupled Schur transfer is stable against same-sector reservoirs

**Status:** `EXACT-DERIVED + CLASSICAL-BLOCK-RESOLVENT + CONDITIONAL-SYMMETRIC-IDEAL + POSITIVE/ROUTE-NARROWING`. [[research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain|PF-279]] shows that a small local corridor transmission coefficient does not control the **unprojected** complete-cut Schur inverse: long same-channel reservoirs can inflate endpoint-normalized extension mass and erase the local gain. That counterexample is decisive for any argument that extrapolates a local seam coefficient directly to the full cut. It does not, however, identify the quantity that appears in the surviving physical `P/H` leakage words of [[research/prime_flute/findings/PF-220-coefficient-adjacent-low-recoupling-is-weak-trace-without-schur-locality|PF-220]]--[[research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling|PF-222]].

For the physical low/high split there is an exact block-resolvent identity that separates these issues. Let `K>=0` be the simultaneous normalized boundary precision and write the boundary space as

\[
\mathcal B=P\mathcal B\oplus H\mathcal B,
\qquad H=I-P,
\]

where `P` is the modulewise fixed-physical-frequency projection of [[research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate|PF-212]]. Delete only the `P/H` cross form and let

\[
K_0=K_P\oplus K_H,
\qquad D=(I+K)^{-1},
\qquad D_0=(I+K_0)^{-1}.
\]

If the cross form is represented by a bounded operator

\[
B:H\mathcal B\to P\mathcal B,
\]

then, with

\[
A=I+K_P,
\qquad C=I+K_H,
\]

one has the exact factorizations

\[
\boxed{
PDH=-A^{-1}B\,(HDH)
     =-(PDP)\,B C^{-1}.
}
\]

Since `0<=D<=I`, both `HDH` and `PDP` are contractions. Therefore **same-sector reservoir completion cannot worsen the symmetric-ideal class of a one-sided decoupled `P/H` transfer**:

\[
\boxed{
A^{-1}B\in\mathcal J\ \Longrightarrow\ PDH\in\mathcal J,
\qquad
BC^{-1}\in\mathcal J\ \Longrightarrow\ PDH\in\mathcal J
}
\]

for every two-sided symmetric operator ideal `\mathcal J`, including `\mathcal S_p` and weak `\mathcal S_{p,\infty}`. The same conclusion holds for the adjoint orientation `HDP`.

This also propagates directly to the reciprocal-prime coefficient-transfer obstruction. If `\Omega` is the module scalar weight of PF-221, then `\Omega` commutes with the physical `P/H` split and

\[
\boxed{
P[D,\Omega]H
=(PDH)\Omega_H-\Omega_P(PDH).
}
\]

Hence any symmetric-ideal estimate for either one-sided decoupled transfer `A^{-1}B` or `BC^{-1}` gives the same ideal membership for `P[D,\Omega]H`, up to the standard bounded-multiplication and finite-sum constants of that ideal.

The implication for PF-279 is narrow but important. Its scalar reservoir amplifier lives inside one scalar channel. Under a consistent physical low/high classification that channel lies entirely on one side of the split, so it contributes no `P/H` cross block at all. Thus PF-279 remains a genuine obstruction to **unprojected cut transfer**, but its extension-mass mechanism is not by itself a counterexample to the mixed physical-frequency commutator required by PF-221. The next gate is sharper: estimate an actual PF one-sided **frequency-decoupled** transfer such as `A^{-1}B` or `BC^{-1}`, or prove that the canonical geometry fails to place either one in the ideal needed at the weak-trace endpoint.

## Claim

Let `\mathcal B` be a Hilbert space with an orthogonal projection `P` and `H=I-P`. Let `k` be a densely defined closed nonnegative quadratic form with associated positive self-adjoint operator `K`. Assume:

1. `P` and `H` preserve the form domain of `k`;
2. the diagonal restrictions
   \[
   k_P[p,q]=k[p,q],\quad p,q\in P\operatorname{Dom}k,
   \qquad
   k_H[h,g]=k[h,g],\quad h,g\in H\operatorname{Dom}k
   \]
   are closed;
3. the off-diagonal form is represented by a bounded operator `B:H\mathcal B\to P\mathcal B` in the sense that
   \[
   k[p,h]=\langle p,Bh\rangle
   \]
   on the form core, with the adjoint relation in the opposite orientation.

Let `K_P,K_H` be the operators associated with `k_P,k_H`, put

\[
K_0=K_P\oplus K_H,
\qquad
A=I+K_P,
\qquad
C=I+K_H,
\tag{1}
\]

and

\[
D=(I+K)^{-1},
\qquad
D_0=(I+K_0)^{-1}=A^{-1}\oplus C^{-1}.
\tag{2}
\]

Then the bounded perturbation from the decoupled form to the full form is

\[
V=
\begin{pmatrix}
0&B\\
B^*&0
\end{pmatrix},
\qquad
K=K_0+V
\tag{3}
\]

in the form/operator sense, and the resolvent identities give

\[
D-D_0=-D_0VD=-DVD_0.
\tag{4}
\]

Taking the `P/H` corner of the first identity yields

\[
\boxed{
PDH=-A^{-1}B\,HDH.
}
\tag{5}
\]

Taking the `P/H` corner of the second yields

\[
\boxed{
PDH=-PDP\,BC^{-1}.
}
\tag{6}
\]

Because `K>=0`,

\[
0\le D\le I,
\qquad
\|PDP\|\le1,
\qquad
\|HDH\|\le1.
\tag{7}
\]

Consequently, for every singular index `j`,

\[
\boxed{
s_j(PDH)\le s_j(A^{-1}B),
\qquad
s_j(PDH)\le s_j(BC^{-1})
}
\tag{8}

whenever the corresponding right side is compact. More generally, for every two-sided symmetric ideal `\mathcal J`,

\[
\boxed{
A^{-1}B\in\mathcal J\quad\Longrightarrow\quad PDH\in\mathcal J,
}
\tag{9}
\]

and

\[
\boxed{
BC^{-1}\in\mathcal J\quad\Longrightarrow\quad PDH\in\mathcal J.
}
\tag{10}
\]

No estimate of the complete unprojected cut inverse is used.

Now let `\Omega` be bounded and commute with `P` (equivalently with `H`). Write

\[
\Omega_P=P\Omega P,
\qquad
\Omega_H=H\Omega H.
\tag{11}
\]

Then

\[
\begin{aligned}
P[D,\Omega]H
&=PD\Omega H-P\Omega DH\\
&=(PDH)\Omega_H-\Omega_P(PDH).
\end{aligned}
\tag{12}
\]

Thus any ideal membership in (9) or (10) implies

\[
\boxed{
P[D,\Omega]H\in\mathcal J.
}
\tag{13}
\]

For `\mathcal S_p`, `p\ge1`, the usual ideal norm gives

\[
\|P[D,\Omega]H\|_{\mathcal S_p}
\le
2\|\Omega\|\,\|PDH\|_{\mathcal S_p}.
\tag{14}
\]

For weak ideals the same membership follows from bounded multiplication and the Fan singular-value inequality; no exact quasi-norm constant is needed here.

## 1. Why the decoupled one-sided transfer is the correct reservoir currency

PF-279's exact scalar formula shows why the bare local crossing coefficient is not enough. In scalar Schur-complement notation the full cut transfer contains endpoint extension masses, equivalently derivatives of reservoir Weyl functions, and those factors can compensate a small corridor coefficient. The full resolvent is therefore not controlled by the local crossing block alone.

Equations (5)--(6) insert the physical `P/H` split **before** asking for a global ideal estimate. The diagonal same-sector reservoirs are retained inside `K_P` and `K_H`. One may then decouple only the off-frequency interaction. Restoring that interaction produces a single cross operator, while the opposite full resolvent corner is merely a compression of the positive contraction `D`.

The useful input is therefore not `B` by itself unless that is already cheap enough. It is enough to prove either one-sided dressed transfer

\[
A^{-1}B=(I+K_P)^{-1}B
\tag{15}
\]

or

\[
BC^{-1}=B(I+K_H)^{-1}
\tag{16}
\]

lies in the desired ideal. This is strictly weaker than demanding an ideal estimate for the raw off-frequency precision block `B`. Same-sector reservoir geometry is allowed to participate in the dressing on the side where it is useful, but **cannot reappear as an uncontrolled multiplicative extension-mass factor on the other side** because that side is represented by `HDH` or `PDP`, whose norm is at most one.

This is the precise sense in which the mixed physical-frequency problem is reservoir-stable. It does not say reservoirs are harmless for arbitrary unprojected transfer; PF-279 proves the opposite.

## 2. The reciprocal-prime commutator inherits the same reduction

PF-221 isolates coefficient transfer in

\[
P[D,\Omega]H,
\qquad
\Omega=\bigoplus_n P_n^{-1}I_{\mathcal B_n}.
\tag{17}
\]

The PF-212 physical frequency projection is modulewise, while `\Omega` is scalar on every entire module. Hence

\[
[P,\Omega]=[H,\Omega]=0.
\tag{18}
\]

Equation (12) is therefore exact for the actual reciprocal-prime weight. It is conceptually different from the formal precision commutator

\[
[D,\Omega]=-D[K,\Omega]D,
\]

whose global domain problem motivated PF-222's prefix-cut proof. The present reduction never forms `[K,\Omega]`. It says that the **mixed corner** of the already-bounded Schur commutator is controlled once the mixed Schur corner `PDH` is controlled, and equations (5)--(6) reduce that corner to a one-sided decoupled transfer.

Accordingly, a proof of

\[
(I+K_P)^{-1}B\in\mathcal S_{1,\infty}
\tag{19}
\]

or of the symmetric right-dressed version would close the coefficient-weight commutator gate of PF-221 for that metric. Stronger membership such as `\mathcal S_1` would of course propagate as well. The theorem does **not** assert (19) for the PF geometry.

## 3. PF-279 does not furnish a mixed-frequency counterexample

The scalar reservoirs in PF-279 were intentionally constructed to test whether local corridor attenuation survives complete-cut extension. There is only one scalar channel on each side. If that channel is assigned consistently to the physical low sector, then `H` annihilates it; if it is assigned consistently to the high sector, then `P` annihilates it. In either case the scalar model has

\[
B=PKH=0
\tag{20}
\]

for the physical low/high decomposition and therefore

\[
PDH=P[D,\Omega]H=0.
\tag{21}
\]

This does not weaken PF-279. It identifies a category error that would arise from using its unprojected amplification as if it automatically refuted PF-221's mixed-frequency word. To threaten the physical coefficient-transfer route, a counterexample must combine reservoir extension with **genuine low/high mode conversion** in the canonical normalized precision.

PF-227 supplies an important warning in the opposite direction. A fixed physical high-pass does not remove the large raw **high/high** thin-pant channel multiplicity. Hence nothing in PF-280 licenses assuming that the off-frequency block `B`, or either dressed transfer (15)--(16), is compact merely because the split is by physical frequency. The remaining estimate must be proved in the actual geometry.

## 4. Prior art and novelty audit

The abstract ingredients are classical. Resolvent identities for bounded perturbations, Schur-complement/block-operator factorizations, and the ideal property under bounded multiplication are standard operator theory. Christiane Tretter's monograph *Spectral Theory of Block Operator Matrices and Applications* (Imperial College Press, 2008, ISBN 978-1-86094-768-1) surveys bounded and unbounded block operator matrices, resolvent estimates, Schur complements and their factorization. Barry Simon's *Trace Ideals and Their Applications*, 2nd ed. (AMS, 2005), already used in PF-220, is a standard source for the symmetric-ideal facts. No novelty is claimed for (4), for the block extraction (5)--(6), or for ideal stability.

A structure-directed literature audit for block-operator resolvent/Schur factorizations found the expected general theory but no reason to treat the abstract lemma as new. The project-specific mathematical delta is instead its placement in the PF-220--PF-222/PF-279 junction: **the unprojected Weyl-extension-mass obstruction and the physical mixed-frequency coefficient-transfer obstruction are not the same gate**. Once the split is made first, same-sector reservoirs are absorbed into diagonal resolvents and the unresolved quantity can be narrowed to a one-sided frequency-decoupled transfer.

No external theorem is used as a black box in the proof above; equations (4)--(14) follow directly from the stated form-domain/bounded-cross-block hypotheses and standard resolvent/ideal identities.

## 5. Boundary conditions and falsification checks

1. **The cross form must be bounded in the stated realization.** For the actual PF simultaneous precision, `K` is generally unbounded. PF-280 does not silently identify `PKH` with a bounded everywhere-defined operator. The line must verify the form-domain split and bounded representation, or formulate a weaker graph-norm/weighted version before applying the theorem.
2. **The diagonal restrictions must be legitimate closed forms.** If the physical `P/H` projection does not preserve the form domain, `K_P` and `K_H` in (1) are not available in this form. This is a real application gate, not notation.
3. **One-sided dressing is sufficient, not necessary.** Failure to prove (19) does not imply `PDH` is outside weak trace class. Cancellation involving both sides of the full Schur inverse may still be stronger than either sufficient estimate.
4. **No raw-`B` compactness is claimed.** PF-227 rules out naive arguments that physical high-pass dimensional truncation removes the thin-pant multiplicity. The relevant test is the dressed cross-frequency operator, not the count of low modes alone.
5. **PF-279 remains valid for unprojected transfer.** Equations (5)--(6) say nothing about `\mathbf1_R D\mathbf1_L` for a spatial cut that does not coincide with the physical frequency decomposition. Same-channel reservoir extension can still erase local corridor attenuation there.
6. **No commutation with `D` is assumed.** Only `[P,\Omega]=0` is used in (12). The whole point is that `D` may mix modules and frequencies.
7. **No precision commutator is formed.** The proof does not require `[K,\Omega]` to be a bounded global operator and therefore does not reopen PF-221's domain issue.
8. **No full weak-trace theorem follows yet.** PF-112's non-trace-class result, PF-222's nested cut-flux endpoint, the physical `P/H` ideal estimate, finite-pant completion, neighboring-cell extension, true-short-collar splice, wave operators, determinants/resonances, prime/clone separation, zeta zeros, and RH remain unresolved.

## Consequences for the research line

The reservoir question exposed by PF-279 should no longer be attacked by trying to bound the complete unprojected cut norm and then importing that bound into PF-221. That is both stronger than necessary and vulnerable to the exact scalar amplifier already constructed.

For the coefficient-transfer branch, the next discriminating calculation is instead local-to-global in **frequency**: construct the physical PF-212 `P/H` form split for the simultaneous normalized precision and estimate either

\[
(I+K_P)^{-1}(PKH)
\quad\text{or}\quad
(PKH)(I+K_H)^{-1}
\tag{22}
\]

in the ideal actually required by the surrounding PF-212 factors. If one of these is weak trace class, PF-280 and equation (12) close the reciprocal-prime mixed commutator without any separate reservoir-extension-mass estimate. If neither admits the required control, a negative result must exhibit **genuine physical low/high conversion** whose one-sided dressed singular values are too large; a scalar same-channel reservoir is no longer sufficient.

This narrows, but does not resolve, the accepted variable-reservoir and weak-trace clues. The unprojected spatial-cut problem and the mixed physical-frequency problem should remain explicitly separate until the exact PF geometry proves a bridge between them.