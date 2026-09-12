# MI-005 — A persistent Nyman tail is a locally natural mode whose global extension cost has finite Schur certificates

**Evidence level:** supported by the exact causal recursion and stable-tail theorems NB-063--NB-066 and the finite future Gram/Schur characterization NB-067; no uniform bounded certificate is yet proved.

The late Nyman--Beurling quotient is not blocked by missing rank. NB-062--NB-063 show that visible natural spaces form a full causal flag and that old visible information enters the next logarithmic cell only through the finite-rank continuation map `Gamma_R`.

NB-064--NB-066 show what persistence would require. The canonical target would converge to one fixed nonzero stable-tail mode

\[
t_*\in\mathcal T_\infty
=\{t:J_Rt\in\mathcal G_R\text{ for every }R\},
\]

which is exactly natural on every finite window while globally orthogonal to the natural closure. Its one-cell transmitted energy is square summable, but every exact global natural continuation of its finite trace has future norm tending to infinity. Equivalently, the worst minimal continuation constant `Lambda_R` must diverge. A bounded subsequence of `Lambda_R` rules out the entire stable-tail space.

NB-067 makes this criterion finite and source-only. The kernel of `J_R` on the natural space is exactly the closed span of future innovations `D_j`, `j>=R`. If `A_R` is the visible prefix Gram and `S_(R,N)` is the finite Schur complement after optimizing over `D_R,...,D_N`, then

\[
\Xi_{R,N}
:=
\lambda_{\max}(A_R^{-1/2}S_{R,N}A_R^{-1/2})
\downarrow 1+\Lambda_R^2.
\]

Thus every finite future horizon gives a rigorous **upper** bound on the true continuation cost. A uniform inequality

\[
S_{R_k,N_k}\preceq C^2A_{R_k}
\]

on any unbounded sequence `R_k` already forces `T_infinity={0}`. If a stable tail exists, every choice of finite horizon schedule must instead make `Xi_(R,N(R))` diverge.

The reusable lesson is sharper than near-kernel tracking. **Local exact representability, one-step transmission, infinite-horizon continuation cost, and finite certifiability are distinct resources.** Here the infinite obstruction is not hidden beyond all finite access: its decisive upper bounds are monotone finite generalized eigenvalues, provided they are normalized by the actual visible Gram rather than by a global ambient norm.

The remaining arithmetic task is concrete: bound these source-defined generalized eigenvalues on an unbounded window sequence, analytically or with rigorous finite certification. Failure is also informative because the growing extremal generalized eigenvectors identify the exact causal directions responsible for the continuation blow-up.

**Boundary.** NB-067 does not supply the required bounded sequence; it only proves that such a finite certificate would be sufficient and cannot be a truncation artefact. Ordinary global Gram conditioning or floating-point spectra without rigorous control do not substitute for the normalized Schur inequality.
