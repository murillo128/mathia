---
id: CLUE-weil-inertia-hilbert-cut-covariance-bottom-spectrum-reserve
type: research-clue
status: resolved
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-269-first-crossing-null-modes-induce-a-psd-signed-source-laplacian.md
  - research/weil_inertia/findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md
  - research/weil_inertia/findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md
  - research/weil_inertia/findings/WI-277-commensurate-cross-cut-shifts-obey-a-sharp-finite-toeplitz-reserve.md
  - research/weil_inertia/formalization/WI276CrossCutShiftReserve.lean
---

# Does retaining the Hilbert cut path replace the top-spectrum reserve by a stronger bottom-spectrum reserve?

## Observation

The WI-276 formalization proves null orthogonality and the three-piece bounds for an arbitrary real symmetric PSD form. Before Cauchy--Schwarz discards the mixed term, its proof retains the exact identity `q(w)=q(u)+q(z)+2 B(u,z)`. The inspected Lean source has SHA-256 `a404890e744551fe9448a0d526332af0fcaaef7e498c6114c3650294c0d7d1e0`.

In the source Hilbert quotient, write

\[
G(t)=[v\mathbf1_{(-a,t)}].
\]

Null orthogonality makes `G=0` outside `[-a,a]`. A window is the difference `G(t+h)-G(t)`, and `||G(t)||²=Q_t`. Thus replacing `G` by its norm `f=sqrt(Q)` forgets the signs and joint compatibility of its inner products. Subject to justifying this as a measurable Hilbert-valued path, WI-274's integrated energy and WI-276's window average suggest the exact identity

\[
C_G(h):=\int\langle G(t),G(t+h)\rangle\,dt,
\qquad \mathcal F_v(h/2)=\mathcal S_v-C_G(h).
\]

WI-277 instead bounds nonnegative correlations of `f` by the **top** eigenvalue of its finite Toeplitz matrix. Its sharpness statement concerns that norm-profile relaxation and does not settle the signed covariance retained here.

## Research question

Can the source identities, without added regularity or sign assumptions on `v`, justify the Hilbert-valued cut path and yield

\[
\mathcal S_v\ge
\frac{\sum_k\alpha_k kr\lambda_{kr}}
{\sum_k\alpha_k-\lambda_{\min}(H_N(\alpha))},
\quad
H_N(\alpha)=\tfrac12\sum_k\alpha_k(J_N^k+(J_N^*)^k),
\]

for `alpha_k>=0`, not all zero, `kr<a`, and `N=ceil(a/r)`? The proposed mechanism is a lower Rayleigh bound for the **same signed Hilbert-valued path** at all shifts. It restores a relation already present in the PSD cut geometry; it does not assume new Suzuki source structure.

## Why it may matter

For one shift the path spectrum is symmetric, so this recovers the WI-276 coefficient. Several shifts can create an odd cycle and break spectral symmetry. In the `N=3`, `alpha_1=alpha_2=1` case,

\[
H_3=(\mathbf1\mathbf1^T-I)/2,
\qquad \lambda_{\max}=1,\quad\lambda_{\min}=-1/2.
\]

The candidate is therefore `F_v(r)+F_v(2r)<=5 S_v/2`, whereas the same weights in WI-277 give `<=3 S_v`. The decisive distinction is loss of cut-vector orientation, not a smaller coefficient for the nonnegative-profile correlation problem that WI-277 has already solved.

## Decisive test

1. Construct the a.e. cut path in the completion of the real form quotient and prove the measurability and square-integrability needed for polarization and translation averaging. Use the existing sharp-cut domain and integrated-energy facts; do not assume `v in H_0^1` or pointwise admissibility at every cut. Verify `F_v(h/2)=S_v-C_G(h)` including the factor two.
2. Reuse the commensurate fiber decomposition of WI-277 with Hilbert-valued coordinates. A chain of length at most `N` is padded by zero, so the bottom eigenvalue of `H_N` bounds every fiber from below. Derive the displayed reserve or identify an exact failure of this transfer.
3. First settle the three-vertex test exactly. The scalar cut coordinates `(1,-1,0)` have energy `2` and shift covariances `(-1,0)`, attaining the proposed ratio `5/2`. They arise from a PSD null-partition model: take consecutive increments `d=(1,-2,1,0)` and the Gram form `B=d d^T`, for which `B 1=0`. These exact finite checks rule out claiming a still smaller generic coefficient from PSD cut geometry alone; they are not Suzuki realizations.
4. Compare the resulting optimized bottom-spectrum reserve with WI-277's optimized top-spectrum reserve and `R_harm`, keeping the same spectral-profile inputs. Kill the direction if the continuous identity fails under the available domain hypotheses, the improved reserve is already implied by those existing envelopes for every admissible profile, or an existing source already consumes this signed cut-covariance construction. A mere re-expression of the existing spectral-budget question is insufficient.

## Evidence boundary

This is a proposed source-to-formal information-loss lead. Lean proves the finite PSD and one-path statements; it does not define `G`, prove its Hilbert-valued measurability, identify its averaged signed covariance with `S_v-F_v`, or prove the multishift bottom-spectrum reserve. The finite three-vertex calculation is exact algebra, not a formal or analytic verification of that bridge.

The ordinary positive-ground-state/weighted-square proof and the nonnegative multishift candidate were eliminated as standalone leads: the former gives an immediate remainder identity, while WI-277 already proves the latter. The surviving question concerns a different endpoint of the joint operator spectrum after restoring the common cut-vector path. Finite shift spectral theory itself is classical; see Haagerup--de la Harpe, *The numerical radius of a nilpotent operator on a Hilbert space*, DOI `10.1090/S0002-9939-1992-1072339-6`, and WI-277's operator references. No novelty or priority claim is made.

Nothing here proves a spectral budget crossing, one-signedness of a null mode, arithmetic overlap for sign-changing modes, or RH. The rank-one extremizer only tests the abstract PSD relaxation and need not satisfy the exact Suzuki source equation.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-279-hilbert-cut-covariance-yields-a-bottom-toeplitz-reserve-but-does-not-break-the-scalar-profile-wall.md]]

`WI-279` proves the proposed covariance identity and bottom-spectrum reserve without adding regularity assumptions: the finite-shift argument can be run through scalar polarization of the a.e. sharp cuts, so a separate Bochner-measurability theorem is not load-bearing. The reserve dominates the `WI-277` top-spectrum bound for every fixed weight vector and is strictly stronger in the three-vertex odd-cycle example. However, `WI-278`'s scalar counterprofile still keeps every such bottom-spectrum reserve below `K_+`, so the clue is supported only as a refinement of the PSD cut geometry, not as an escape from the scalar-profile budget wall. Further RH-facing progress requires genuinely source/eigenfunction-specific information.
