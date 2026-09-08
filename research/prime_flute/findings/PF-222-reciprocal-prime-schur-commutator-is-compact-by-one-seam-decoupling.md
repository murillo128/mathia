# PF-222 — reciprocal-prime Schur commutator is compact by one-seam decoupling

**Status:** `EXACT-DERIVED + ELLIPTIC-BOUNDARY + POSITIVE/ROUTE-NARROWING`. PF-221 reduces the unresolved smooth coefficient-transfer term to the bounded commutator `P[D,\Omega]H`, where `D=(I+K)^{-1}` is the simultaneous energy-normalized Schur factor and `\Omega=\bigoplus_n P_n^{-1}I_{\mathcal B_n}` is the reciprocal-prime module weight. The remaining endpoint estimate is still open, but **noncompactness is not the obstruction**. The reciprocal-prime weight has an exact norm-convergent prefix-cut decomposition, and every fixed prefix cut can be decoupled by removing one compact off-diagonal pant DtN block. Hence each cut commutator `[D,E_j]` is trace class and `[D,\Omega]` is an operator-norm limit of compact operators. In particular

\[
\boxed{[D,\Omega]\in\mathcal K(\mathcal B),\qquad P[D,\Omega]H\in\mathcal K(\mathcal B).}
\]

This avoids the full-space domain problem in the formal identity `[D,\Omega]=-D[K,\Omega]D`: compactness follows without first proving that `[K,\Omega]` is a bounded global operator and without any uniform bound on the divergent adjacent hopping of PF-215. The live smooth-route question is therefore quantitative singular-value decay of the compact cut fluxes, not whether the coefficient-weight commutator is compact at all.

## Claim

Retain the simultaneous boundary-energy decomposition of PF-214 and PF-221,

\[
\mathcal B=\bigoplus_{n\ge1}\mathcal B_n,
\qquad
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\qquad
D=(I+K)^{-1},
\tag{1}
\]

with module projections `\Pi_n`. Put

\[
\omega_n=P_n^{-1},
\qquad
\Omega=\bigoplus_n\omega_n I_{\mathcal B_n},
\qquad
\delta_j:=\omega_j-\omega_{j+1}>0,
\tag{2}
\]

and let

\[
E_j:=\sum_{n\le j}\Pi_n
\tag{3}
\]

be the prefix projection through module `j` (after absorbing the harmless finite head into the first block when necessary).

Then:

1. The reciprocal-prime weight has the exact layer decomposition
   \[
   \boxed{\Omega=\sum_{j\ge1}\delta_jE_j}
   \tag{4}
   \]
   with convergence in operator norm. If
   \[
   \Omega_N:=\sum_{j=1}^N\delta_jE_j,
   \tag{5}
   \]
   then
   \[
   \boxed{\|\Omega-\Omega_N\|=\omega_{N+1}\longrightarrow0.}
   \tag{6}
   \]

2. For every fixed `j`, the only exterior-precision coupling crossing the cut `E_j\mathcal B\oplus(1-E_j)\mathcal B` is the one-pant block
   \[
   B_j:=\Pi_{j+1}K\Pi_j.
   \tag{7}
   \]
   On that fixed pant, `B_j` is a smoothing operator between the two compact seam boundary circles in the normalized boundary-energy rigging; in particular
   \[
   \boxed{B_j\in\mathcal S_p\quad\text{for every }p>0.}
   \tag{8}
   \]
   No estimate uniform in `j` is asserted.

3. Let `K^{(j)}` be the positive closed-form operator obtained by deleting only the cross term between the prefix and tail:
   \[
   k^{(j)}[u,v]
   :=k[E_ju,E_jv]+k[(1-E_j)u,(1-E_j)v].
   \tag{9}
   \]
   Then `K^{(j)}` commutes with `E_j`, and the difference from `K` is represented by the bounded trace-class crossing operator
   \[
   C_j=B_j+B_j^*.
   \tag{10}
   \]
   Writing
   \[
   D^{(j)}=(I+K^{(j)})^{-1},
   \tag{11}
   \]
   the resolvent identity gives
   \[
   D-D^{(j)}=-D C_j D^{(j)}\in\mathcal S_p
   \qquad(p>0),
   \tag{12}
   \]
   and therefore
   \[
   \boxed{[D,E_j]=[D-D^{(j)},E_j]\in\mathcal S_p\quad(p>0).}
   \tag{13}
   \]

4. Combining (4) with (13),
   \[
   [D,\Omega_N]
   =\sum_{j=1}^N\delta_j[D,E_j]
   \tag{14}
   \]
   is compact for every `N`, while
   \[
   \|[D,\Omega]-[D,\Omega_N]\|
   \le2\|D\|\,\|\Omega-\Omega_N\|
   \le2\omega_{N+1}\to0.
   \tag{15}
   \]
   Hence
   \[
   \boxed{[D,\Omega]\in\mathcal K(\mathcal B).}
   \tag{16}
   \]
   Since the low/high projections of PF-220--PF-221 are bounded,
   \[
   \boxed{P[D,\Omega]H,\ H[D,\Omega]P\in\mathcal K.}
   \tag{17}
   \]

Moreover (14) is an exact norm-convergent **one-seam flux decomposition** of the PF-221 obstruction:

\[
\boxed{
P[D,\Omega]H
=
\sum_{j\ge1}
\left(\frac1{P_j}-\frac1{P_{j+1}}\right)
P[D,E_j]H.
}
\tag{18}
\]

Thus the arithmetic coefficient has finite total variation,

\[
\sum_{j\ge1}\delta_j=\omega_1,
\tag{19}
\]

and all unresolved endpoint difficulty sits in quantitative ideal control of the individual geometric cut-flux operators `P[D,E_j]H`, not in accumulation of the scalar reciprocal-prime variation itself.

## 1. Why the fixed pant crossing block is smoothing

PF-214 proves that after all natural seam strips are removed, the exterior is the disjoint union of one-cusp pant cores. A fixed core `E_j` meets only the two compact seam circles `\Sigma_j^+` and `\Sigma_{j+1}^-`. At the positive shifted equation `(\Delta+1)u=0`, boundary data on one circle produce a solution that is elliptically smooth in a neighborhood of the other circle because source and target boundary components are disjoint. Equivalently, the cross-component kernel of the local Dirichlet-to-Neumann map is smooth: the singular pseudodifferential part of a DtN map lives on the diagonal of the *same* boundary component.

A smooth kernel between compact one-dimensional boundaries has super-polynomial singular-value decay. The two factors `\Lambda_Q^{-1/2}` used in (1) are finite-order elliptic boundary operators on the fixed strip module; composing a smoothing cross-component operator with them remains smoothing. This proves (8) for each fixed `j`.

The cusp does not create a new local singularity. The `+1` shift gives a coercive resolvent, and the two seam circles are compact and positively separated inside the fixed pant core. What can degenerate with `j` are the **constants and singular-value scales** of these smoothing blocks as the pant becomes thinner. PF-215 already shows that no uniform operator-norm bound on the normalized adjacent hopping can hold. Equation (8) is only a fixed-edge compactness statement and is fully compatible with that divergence.

## 2. Cut decoupling avoids the unbounded global precision commutator

PF-221 records the formal finite-truncation identity

\[
[D,\Omega]=-D[K,\Omega]D,
\tag{20}
\]

but correctly leaves a domain/extension gate because the global adjacent precision family is not uniformly bounded. The prefix-cut argument does not need (20).

For fixed `j`, the form in (9) is simply the direct sum of the prefix and tail compressions of the positive form `k`; hence it is positive and has no coupling across the cut. The exact block-Jacobi support of PF-214 says that restoring the original form adds only `B_j+B_j^*`. By the fixed-edge smoothing argument this is a bounded compact, indeed trace-class, perturbation. Standard resolvent perturbation at `-1` therefore gives (12).

Because `D^{(j)}` commutes with `E_j`, its commutator vanishes. Thus the entire failure of `D` to preserve one prefix/tail decomposition is carried by the compact resolvent difference `D-D^{(j)}`, proving (13). This is a domain-safe statement about bounded resolvents rather than a formal manipulation of an unbounded global precision commutator.

A useful quantitative sufficient condition also follows. For every `j`,

\[
\|[D,E_j]\|_1
\le 2\|D-D^{(j)}\|_1
\le 2\|C_j\|_1
\le 4\|B_j\|_1.
\tag{21}
\]

Hence

\[
\sum_j\delta_j\|B_j\|_1<\infty
\tag{22}
\]

would imply the much stronger conclusion `[D,\Omega]\in\mathcal S_1`. No such summability is claimed here; (21) is deliberately only a sufficient local target. In particular, the weak-`S_1` endpoint may require using the two Schur factors and the PF-212 low/high smoothing more efficiently than the crude trace norm of the raw normalized pant crossing block.

## 3. Compactness follows from reciprocal-prime layer approximation, not from compactness of `\Omega`

The full module weight `\Omega` is **not compact**: each scalar value `\omega_n` acts with infinite multiplicity on `\mathcal B_n`. What matters is that its step approximants have only finitely many jumps and converge in norm.

For coordinate `n\le N`, equation (5) acts by

\[
\sum_{j=n}^N\delta_j
=\omega_n-\omega_{N+1},
\tag{23}
\]

while for `n>N` it acts by zero. Therefore the largest coefficient error is exactly `\omega_{N+1}`, proving (6). Since commutation with the contraction `D` is norm-continuous, (15) follows immediately.

This is stronger than the endpoint-difference observation in PF-221 in one precise sense: **it proves that the exact coefficient-weight commutator is already compact in the actual block-Jacobi PF realization**, even though neither `\Omega` nor the global unweighted Schur leakage is known to be compact in the relevant strong ideals. The unresolved issue is the rate at which the singular values of the compact limit fall.

## 4. Prior art and novelty audit

No novelty is claimed for any of the three abstract ingredients: a monotone diagonal weight can be written as a layer-cake sum of prefix projections; compact perturbations have compact resolvent differences; and off-diagonal kernels of elliptic boundary operators between disjoint smooth boundary components are smoothing.

A close classical reference for the last point is P. D. Hislop and C. V. Lutzer, *Spectral asymptotics of the Dirichlet-to-Neumann map on multiply connected domains in R^d*, Inverse Problems 17 (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`. They decompose the DtN map on a multiply connected smooth bounded domain into componentwise pseudodifferential pieces plus a smoothing remainder. Their global hypotheses are not the PF one-cusp pant setting and are **not** imported as a black-box theorem here; the fixed-pant cross-component smoothing used above follows directly from local elliptic regularity at the positive shift.

There is also a broad operator-algebraic analogy with essential commutation of quasi-local/Roe-type operators with slowly varying diagonal multipliers, but PF-222 does not invoke such a theorem. The project-specific deduction is the combination of the exact PF-214 one-pant block-Jacobi geometry, fixed-edge DtN smoothing in the PF energy normalization, and the exact reciprocal-prime coefficient weight from PF-221 to settle compactness of the physical Schur weight-transfer remainder.

The literature audit did not identify a theorem that supplies the missing **uniform weak-Schatten singular-value estimate** for the degenerating PF pant family. General DtN commutator estimates on fixed smooth domains and general endpoint commutator theorems do not provide the required `j`-dependent control through the thin-pant degeneration.

## 5. Falsification and boundary checks

1. The conclusion uses compactness of each **fixed** normalized adjacent pant block, not a uniform norm bound. It does not contradict PF-215.
2. The smooth-kernel argument is cross-component. The diagonal DtN blocks remain first-order pseudodifferential operators and are not claimed compact.
3. The one-cusp interior causes no cross-component kernel singularity at the positive shift, but no uniform cusp/thin-pant estimate is inferred from this fixed-edge regularity.
4. `K^{(j)}` is defined by the positive prefix/tail form split (9), not by an arbitrary deletion that might destroy self-adjointness or positivity.
5. Equation (16) does not use or justify a global bounded operator `[K,\Omega]`; this is exactly why the decoupled-resolvent proof is useful.
6. `\Omega` itself is not compact because every module is infinite-dimensional. Only its commutator with `D` is proved compact.
7. A norm limit of trace-class cut commutators need not lie in `\mathcal S_1`, `\mathcal S_{1,\infty}`, or any prescribed Schatten ideal without quantitative control. Compactness alone does not close PF-221's endpoint gate.
8. The coefficient-transfer remainder becoming compact does not prove the complete first relative resolvent is weak trace class, PF-204's unsmoothed endpoint, PF-183's true-short-collar splice, wave operators, determinants/resonances, prime/clone separation, or any RH consequence.

## Consequences for the research line

The smooth PF-221 frontier can be narrowed again. A counterexample based only on **noncompact** reciprocal-prime Schur transport is impossible in the actual simultaneous-cut geometry. The physical commutator remainder is compact before any prime-gap upper estimate or global precision-commutator domain theorem is supplied.

The discriminating question is now quantitative: determine the singular-value counting of the norm-convergent cut-flux series (18), retaining the exact low/high placement and PF-212 local smoothing. A positive proof may estimate the trace/weak-trace size of `P[D,E_j]H` directly, or exploit the single-pant factorization behind (12) together with the reciprocal-prime jump `\delta_j`. A negative proof must produce a PF-compatible degenerating sequence whose **compact** cut fluxes accumulate too slowly for `\mathcal S_{1,\infty}`. Merely showing divergent raw hopping, lack of exponential Schur locality, or failure of a global `[K,\Omega]` operator bound no longer decides the coefficient-weight endpoint.