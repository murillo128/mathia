---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical.md
  - research/prime_flute/findings/PF-249-positive-separation-preserves-free-jacobi-square-root-threshold.md
  - research/prime_flute/findings/PF-250-half-line-fractional-edge-powers-retain-supercritical-separated-window.md
  - research/prime_flute/findings/PF-251-exact-zero-edge-solutions-select-growing-inverse-square-jacobi-branch.md
  - research/prime_flute/findings/PF-252-zero-edge-ground-state-transform-has-bessel-four-scaling.md
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/findings/PF-254-normalized-noncommuting-robin-injection-splits-square-root-amplitude-from-polar-transport.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
  - research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform.md
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Can the fixed-axis combined Robin injection spend the Jacobi smoothing margin?

## Observation

PF-247--PF-253 identify the critical fixed-axis parity-Jacobi edge and prove a sharp positive fractional-power window. For `0<\sigma<1`, the actual parity chains satisfy in the separated cone

\[
\left|\langle e_i,J_\varepsilon^\sigma e_j\rangle\right|
\asymp
(i+1)^{3/2}(j+1)^{-5/2-2\sigma},
\]

with

\[
E_dJ_\varepsilon^\sigma N^R\in\mathcal S_2
\iff R<2+2\sigma.
\]

Thus a literal Jacobi square root has the proven window `R<3`, comfortably above PF-243's required `R>1`.

PF-254 writes the energy-normalized noncommuting Robin injection as

\[
h(\mathcal R)U,
\qquad
h(\lambda)=\frac{\sqrt\lambda}{1+\lambda},
\qquad
\mathcal R=K^{-1/2}QK^{-1/2},
\]

where `U` is the polar partial isometry of `X=K^{-1/2}Q^{1/2}`. PF-255 and PF-256 then remove the width-dependent hypercycle transport and the variable-corridor `A\leftrightarrow T_a` basis change as independent sources of catastrophic high-to-low leakage: already graph-local factors retain a two-derivative window in the actual `K_a=T_a^{1/2}` modes.

PF-257 changes how the remaining fixed-axis noncommutativity should be attacked. The physical Robin factor never contains the naked polar partial isometry. On every bounded regularization,

\[
\boxed{
h(\mathcal R)U
=(I+XX^*)^{-1}X
=X(I+X^*X)^{-1}.}
\]

Equivalently it is an off-diagonal block of the regular rational transform

\[
F(\mathbb D_X),
\qquad
\mathbb D_X=
\begin{pmatrix}0&X\\X^*&0\end{pmatrix},
\qquad
F(t)=\frac{t}{1+t^2}.
\]

The combined factor is norm-stable in `X` even when the auxiliary polar factor is unstable near a closing singular-value gap. Therefore **standalone locality of `U` is sufficient but not necessary**. The live question is whether the actual combined fixed-axis injection has enough high-to-low decay; splitting amplitude from orientation must not discard correlations that the Robin map retains.

## Research question

After removing the PF-255/PF-256-controlled hypercycle coordinate/density transport, derive the actual fixed-axis relative square-root map

\[
X_w:=K_a^{-1/2}(Q_w^{\rm act})^{1/2}
\]

in the correct finite/form realization and study the combined Robin transform

\[
\boxed{
B_w:=X_w(I+X_w^*X_w)^{-1}
=(I+X_wX_w^*)^{-1}X_w.
}
\]

Can `B_w` be related to PF-247's parity-Jacobi structure, or controlled directly through the block operator `\mathbb D_{X_w}`, strongly enough that

\[
B_wK_a^RP_Z
\]

has a uniform bound for some `R>1` before separated longitudinal propagation?

If the most efficient dictionary passes through `\mathcal R_w=X_wX_w^*`, can PF-253's square-root edge window be used **without separating off and independently estimating the polar factor**? Alternatively, can graph/locality information for `X_w` or `\mathbb D_{X_w}` be propagated through PF-257's resolvent formula directly?

The two-boundary reflection factors from PF-254 are already polar-free rational functions `c(\mathcal R_w)=(I-\mathcal R_w)(I+\mathcal R_w)^{-1}`. They must still be controlled where reflection cycles matter, but no physical factor requires a theorem about the naked `U_w`.

## Why it may matter

PF-243 reduces the remaining high-high shear gate to one-sided separated Robin-Poisson smoothing of any fixed order `R>1`. PF-253 supplies a substantial square-root exponent budget, while PF-255/PF-256 protect a `1<R<2` window through the known geometric transports.

PF-257 removes a potentially artificial proof obligation from the remaining fixed-axis stage. A polar partial isometry can look extremely nonlocal near a zero singular value even when the product actually appearing in the Robin source map is small there. If the route insists on proving `U_w` graph-local by itself, it can produce a false negative by throwing away exactly the singular-value weight that regularizes those directions.

A positive result for `B_w` would connect the actual seam directly to PF-243 without first solving an unnecessarily strong polar-locality problem. A negative result remains decisive if the **combined** transform itself has a non-summable high-to-low tail. The clue therefore preserves PF-244's obstruction while making its relevant target more faithful to the physical operator.

## Decisive test

Work in the fixed-axis `L^2((0,\pi),d\theta)` representation and keep the actual complete-lift seam fixed. Factor out only the hypercycle coordinate/density operators already controlled by PF-255 and transfer those estimates to the actual `K_a` scale using PF-256.

Then derive `X_w=K_a^{-1/2}(Q_w^{\rm act})^{1/2}` on canonical finite spectral/form regularizations. Test the separated blocks of

\[
B_w=X_w(I+X_w^*X_w)^{-1}
\]

directly. There are two acceptable proof routes:

1. identify `X_wX_w^*` with PF-247's `J_\varepsilon`, or with a controlled functional/graph perturbation of it, tightly enough that PF-253 supplies the load-bearing square-root decay while the exact PF-257 recombination keeps amplitude and orientation correlated; or
2. derive graph-locality or resolvent off-diagonal estimates for the self-adjoint block `\mathbb D_{X_w}` and pass them through
   \[
   F(\mathbb D)=\frac12\bigl((\mathbb D-i)^{-1}+(\mathbb D+i)^{-1}\bigr).
   \]

Account explicitly for reflection factors `c(\mathcal R_w)` and for every remaining conjugation. Use PF-256 only after the factor under consideration has actual graph-locality; form order or eigenvalue comparability alone does not transfer matrix decay.

Kill the route if `B_w` itself has a high-to-low tail that defeats every uniform `R>1`, if a reflection factor creates an equally fatal tail, or if the full unbounded/form realization loses the finite-regularization transform. **Do not kill it merely because the auxiliary polar partial isometry `U_w` is nonlocal or lacks a stable limit.**

## Evidence boundary

PF-253 proves the actual parity-Jacobi fractional kernel and its sharp square-root window. PF-254 proves the noncommutative Robin factorization on bounded positive regularizations. PF-255 proves two-derivative graph locality for the canonical hypercycle coordinate/density transport, and PF-256 transfers that already-established locality to the actual variable-corridor scale.

PF-257 proves only the exact polar-free recombination and its elementary bounded/resolvent stability. It does **not** prove that the actual fixed-axis `X_w`, `B_w`, `\mathbb D_{X_w}`, or reflection transforms are graph-local; it does not identify `X_wX_w^*` with `J_\varepsilon`; and it does not justify the full unbounded complete-lift domain/closure passage.

Nothing here proves PF-243's separated source-to-bulk estimates, the high-high trace-class shear conclusion, global flute scattering/determinant statements, or any theorem about zeta zeros or RH. This remains an accepted research clue rather than mathematical evidence.

## Research disposition

Accepted for continued investigation. The frontier is now the **combined fixed-axis Robin transform**, not the polar factor in isolation. The next material outcome must either prove a uniform `R>1` high-to-low bound for `B_w` (with the needed reflection factors and full realization) or exhibit an actual-seam counterexample for that combined physical operator. A standalone failure of `U_w` locality no longer resolves the clue.