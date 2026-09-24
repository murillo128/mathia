---
id: CLUE-prime-lattice-rank-two-defect-schur-ellipse
type: research-clue
status: accepted
origin: independent-review
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-437-mod5-orientation-defect-rank-two.md
  - research/prime_lattice/formalization/PL437Mod5OrientationDefect.lean
  - research/prime_lattice/findings/PL-421-local-factor-dephasing-image-cone.md
  - research/prime_lattice/findings/PL-436-scalar-variance-lower-bounds-do-not-close-oriented-cone.md
---

# Can the residual PL-437 cone test be reduced to a source-estimable Schur ellipse?

## Observation

The explicit PL-437 matrix also admits the wedge form below, obtained by reading the columns of `leftFactor` as `u,v` and the rows of `rightFactor` as `-v^T,u^T`:

\[
B(b,d,f)=v u^T-u v^T,
\qquad u=(0,1,0,-1)^T,\quad v=(b,0,d,-f)^T.
\]

For the fixed-diagonal residual, `b=d=s/2`. Removing the component of `v` parallel to `u` gives

\[
v_\perp=(s/2,-f/2,s/2,-f/2)^T,\qquad u^Tv_\perp=0.
\]

Thus the residual character-space perturbation admits the exact form

\[
iB_{s,f}=g(s,f)h^*+h g(s,f)^*,\qquad
h=u/\sqrt2,\quad g(s,f)=i\sqrt2\,v_\perp,
\]

where `h` is fixed, `h^*g=0`, and `\|g(s,f)\|^2=s^2+f^2`. In the PL-437 cone decomposition, the residual therefore changes only the block coupling one fixed unit vector to its orthogonal complement. The canonical finding records the Euclidean Weyl bound and notes that a sharper test may use orientation relative to `H_known`, but does not record this fixed-vector form.

## Research question

Write `P=I-hh^*`, `a=h^*H_known h`, `w=PH_known h`, and let `C` be the restriction of `PH_knownP` to `h^\perp`. On the branch `C\succ0`, the Schur complement gives the exact condition

\[
H_{known}+iB_{s,f}\succeq0
\quad\Longleftrightarrow\quad
a-(w+g(s,f))^*C^{-1}(w+g(s,f))\ge0.
\]

Does this source-adapted quadratic condition yield a genuinely weaker and arithmetically accessible target than bounding `\sqrt{s^2+f^2}` by the smallest eigenvalue of `H_known`? In particular, can the actual mod-5 source control this scalar Schur budget from the real-product data, residue diagonal, and the two oriented coherences without proving the same full complex lower-frame estimate already isolated in PL-436?

## Why it may matter

The exact condition is an ellipse in `(s,f)` when `C\succ0`; its axes and center depend on the visible block and its coupling to `h`. It can use anisotropic margins that the Euclidean Weyl condition discards. For example, a block-diagonal `H_known` with `a=1` and `C=9I` permits residual norm up to `3` by this criterion, while the Weyl sufficient condition only permits norm at most `1`. Whether the actual source geometry supplies a useful version of this anisotropy is unresolved.

## Decisive test

First derive the displayed fixed-vector factorization and Schur criterion from the exact PL-437 matrices, including the `C\succ0` hypothesis and the map from `(s,f)` to `g`. Compare the resulting feasible ellipse with the Weyl disk on the PL-428 matched controls and on simple exact `H_known` examples: if it never gives a strict, data-compatible relaxation, kill the proposed advantage. If it does, identify which coefficients of `a,w,C` and which linear combinations of `s,f` are actually accessible from the source observables. Then determine whether a non-circular estimate of the resulting scalar inequality follows at the source parameters required by PL-421; reject the direction if it requires the same or stronger arbitrary-complex coercivity as the existing lower-frame target.

## Evidence boundary

Lean proves finite matrix identities and the residual two-coordinate structure; it does not formalize this Schur criterion, establish `C\succ0` for the actual source, or prove any arithmetic bound on `s,f`. PL-428's positive-semidefinite matched controls show that basic covariance positivity and the already visible data do not force cone admission. This clue asserts neither that the ellipse closes the prime-lattice gate nor that its source-side inequality is easier.

## Research disposition

The direction survives initial triage and is **accepted** for continued investigation. `PL-438` derives an exact `1+2+1` residue-space normal form, reduces the strict positive branch to a two-dimensional Schur ellipse, and gives an admissible positive covariance for which that ellipse certifies the `PL-421` cone while the `PL-437` Weyl disk fails. The ellipse coefficients and center are determined by the real-product sector plus the residue diagonal; only the two oriented combinations remain unresolved.

The still-open part of the clue is arithmetic rather than representational: determine whether the actual fixed-mod-5 prime source controls the resulting scalar Schur budget at variance scale by an unconditional input genuinely weaker than the full complex lower-frame estimate. Acceptance does not assert that such an estimate exists or that the ellipse advances RH by itself. Durable evidence is in `research/prime_lattice/findings/PL-438-mod5-oriented-schur-ellipse.md`.
