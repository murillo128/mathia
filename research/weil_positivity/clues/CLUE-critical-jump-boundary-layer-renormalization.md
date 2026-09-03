---
id: CLUE-weil-positivity-critical-jump-boundary-layer-renormalization
type: research-clue
status: proposed
origin: research-watch
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-122-singular-jump-local-positive-measures-still-diverge-at-critical-prime-coupling.md
  - research/visual_exploration/visualizations/wp122-cesaro-boundary-layer.md
---

# Can the shrinking jump boundary layer renormalize to a canonical derivative/Sobolev positive form?

## Observation

`WP-122` closes every nontrivial **fixed** jump-local positive matrix-valued Radon geometry by Cesàro averaging the common shell phase. For the canonical increment \(u_t(y)=(\cos(ty)-1,\sin(ty))^T\), the exact averaged Gram matrix

\[
M_T(y)=\frac1T\int_0^T u_t(y)u_t(y)^T\,dt
\]

depends only on \(z=Ty\). Its eigenvalues satisfy

\[
\lambda_{\max}(M(z))=\frac{z^2}{3}+O(z^4),
\qquad
\lambda_{\min}(M(z))=\frac{z^4}{320}+O(z^6)
\]

as \(z\to0\), while for fixed \(y>0\) they approach \(3/2\) and \(1/2\) as the averaging length grows. The retained visualization makes the resulting \(y=O(1/T)\) boundary layer explicit and shows the additional quartic weak matrix direction.

## Research question

Can an independently defined local positive geometry have a canonical dilation/renormalization toward \(y=0\) whose nontrivial limit is a derivative- or Sobolev-type form, while the exact critical prime shell series is Cauchy in that fixed limiting geometry?

Equivalently, classify whether the only remaining local escape suggested by the exact Cesàro kernel is genuine geometry or merely a disguised scale/frequency-dependent choice. The renormalization must be specified independently of individual prime shells; choosing a different form ad hoc for each shell does not count.

## Why it may matter

`WP-122` explicitly leaves derivative/Sobolev-type local forms outside its matrix-measure theorem. The exact phase-averaged Gram matrix now identifies the only local scale where its lower-bound mechanism can become weak and shows that a matrix orientation can suppress the leading quadratic channel to quartic order. If a canonical renormalized endpoint geometry exists, it would be a concrete escape from the broad fixed-measure closure. If no admissible renormalization survives, the jump-local program can be narrowed beyond the current Radon-measure boundary.

## Decisive test

Define an intrinsic admissible class of endpoint dilations \(y=z/T\) and matrix normalizations for which the local forms converge, in a fixed operator/domain sense, to a nonzero derivative/Sobolev-type positive form. Use the exact universal matrix \(M(z)\) to classify the possible scaling exponents and weak-channel orientations.

A decisive negative is a theorem that every nontrivial admissible limit either retains a shell-energy lower bound incompatible with critical Cauchy convergence or necessarily depends on the shell location/prime frequency and is therefore not a fixed geometric completion. A decisive positive is an explicit canonical limiting form, defined independently of the prime data, for which the critical ordered prime series has finite tail energy and whose positivity is not imported from RH.

## Evidence boundary

The visualization and Taylor expansion identify a quantitative boundary layer but do not produce a renormalized positive geometry. `WP-122` does not cover \(T\)-dependent concentrating measures, and such dependence may itself be the reason the apparent escape is illegitimate. No claim is made here that a derivative/Sobolev completion exists, is canonical, or avoids the critical divergence.
