# MC-115 — Mean-absolute Mertens control gives a zero-free half-plane directly by Mellin convergence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CORRECTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
D_M(X)=\frac1X\int_1^X |M(u)|\,du.
\]

If for some real `alpha<1`

\[
D_M(X)=O(X^\alpha),
\tag{1}
\]

then the Riemann zeta function has no zero in

\[
\operatorname{Re}s>\alpha.
\tag{2}
\]

More generally, if for every `epsilon>0`

\[
D_M(X)=O_\varepsilon(X^{\alpha+\varepsilon}),
\tag{3}
\]

then `zeta(s)` has no zero with `Re(s)>alpha`. In particular,

\[
\boxed{
\mathrm{RH}
\iff
D_M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\tag{4}
\]

The reverse implication in `(4)` does **not** require the recent Pintz mean-absolute theorem audited in `MC-009`--`MC-012`. It follows directly from absolute convergence of the classical Mellin representation of `1/zeta(s)` once the absolute first moment of `M` has the required growth. Pintz's theorem is substantially stronger in a different direction: conditional on its still-pending full audit, it identifies the complete logarithmic order of `D_M(X)` and a near-end maximum with the rightmost zero boundary, rather than merely showing that an upper exponent excludes zeros to its right.

Thus `MC-009` remains valuable as a fresh zero-signature theorem, but its statement that Pintz is needed to make the RH-scale mean-absolute bound imply RH is too strong. The exact analytic bridge from the mean-absolute upper bound to zero exclusion is already elementary.

## 1. Mean-absolute growth makes the Mellin integral absolutely convergent

Set

\[
A(X):=\int_1^X |M(u)|\,du=X D_M(X).
\tag{5}
\]

Under `(1)`,

\[
A(X)=O(X^{\alpha+1}).
\tag{6}
\]

Fix `sigma>alpha`. Dyadically,

\[
\begin{aligned}
\int_1^\infty |M(x)|x^{-\sigma-1}\,dx
&=\sum_{k\ge0}
\int_{2^k}^{2^{k+1}}|M(x)|x^{-\sigma-1}\,dx\\
&\le
\sum_{k\ge0}2^{-k(\sigma+1)}A(2^{k+1})\\
&\ll
\sum_{k\ge0}2^{-k(\sigma-\alpha)}<\infty.
\end{aligned}
\tag{7}
\]

Equivalently, integration by parts against the increasing function `A` gives the same criterion. Hence

\[
F(s):=s\int_1^\infty M(x)x^{-s-1}\,dx
\tag{8}
\]

converges absolutely and locally uniformly throughout `Re(s)>alpha`, and therefore defines a holomorphic function there.

For `Re(s)>1`, ordinary Abel summation of the absolutely convergent Möbius Dirichlet series gives

\[
F(s)=\sum_{n\ge1}\frac{\mu(n)}{n^s}
=\frac1{\zeta(s)}.
\tag{9}
\]

So `(8)` is a holomorphic continuation of the reciprocal zeta function from `Re(s)>1` into the full half-plane `Re(s)>alpha`.

## 2. A zero to the right is incompatible with the holomorphic continuation

Suppose `rho` were a zero of `zeta` with `Re(rho)>alpha`. Since `F` is holomorphic at `rho`, while `(9)` holds on the nonempty open set `Re(s)>1`, uniqueness of analytic/meromorphic continuation forces `F` to agree with the reciprocal of the meromorphic continuation of `zeta` wherever the latter is defined in the connected half-plane.

Equivalently, on the punctured half-plane `Re(s)>alpha`, `s!=1`, the holomorphic function

\[
\zeta(s)F(s)
\]

agrees with `1` on `Re(s)>1`; the identity theorem therefore gives

\[
\zeta(s)F(s)=1.
\tag{10}
\]

At a nontrivial zero `rho`, however, the left side of `(10)` would be zero because `F(rho)` is finite. This is impossible. Thus `(1)` implies `(2)`.

For `(3)`, take any putative zero `rho` with `beta=Re(rho)>alpha` and choose `epsilon` with `0<epsilon<beta-alpha`. The bound `(3)` with that epsilon makes `(8)` holomorphic at `rho`, giving the same contradiction. Hence no zero lies to the right of `alpha`.

A useful contrapositive is therefore

\[
\zeta(\rho)=0,\quad \operatorname{Re}\rho=\beta
\quad\Longrightarrow\quad
D_M(X)\ne O(X^\alpha)
\quad\text{for every }\alpha<\beta.
\tag{11}
\]

In particular, any off-critical zero forces the **limsup** power exponent of the global mean absolute Mertens statistic to be at least its real part. This already gives a non-pointwise averaged zero signature without the sharper Pintz asymptotics.

## 3. The RH equivalence follows without a pointwise recovery theorem

If RH holds, the classical Mertens criterion gives for every `epsilon>0`

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon}).
\tag{12}
\]

Integrating `(12)` immediately gives the mean-absolute bound in `(4)`.

Conversely, assume the mean-absolute bound in `(4)`. For any `beta>1/2`, choose `epsilon<beta-1/2`. Section 1 then gives a holomorphic continuation of `1/zeta(s)` to a half-plane containing every point with real part `beta`, so Section 2 excludes every zeta zero with real part greater than `1/2`. Functional-equation symmetry then places every nontrivial zero on the critical line. This proves RH.

No estimate recovering individual values of `M(X)` from `D_M(X)` is used. Sparse spikes may indeed be invisible to the first absolute moment as a generic real-variable matter; what makes `(4)` RH-complete is instead that the first absolute moment is precisely strong enough to make the Möbius Mellin transform converge absolutely in the desired half-plane.

This is the correction to the dependency asserted in `MC-009`: the arithmetic target is genuinely weaker than pointwise Mertens control, but its implication to zero exclusion is already encoded in the classical Dirichlet/Mellin transform.

## 4. What Pintz still adds

The direct argument above is one-sided at the exponent level. From a zero at real part `beta` it yields only the failure of every bound `D_M(X)=O(X^alpha)` with `alpha<beta`, equivalently a lower bound on the limsup growth exponent. It does not show that `D_M(X)` has a limiting logarithmic exponent, does not prevent deep downward fluctuations along subsequences, and does not identify a near-end maximum.

The current arXiv version of Pintz's preprint, arXiv:2608.24878v2 (1 September 2026), states the much sharper relations

\[
\log D_M(X)\sim\log Z(X)
\]

and analogous equivalences for `S_{M,delta}(X)`, with `Z` built from the rightmost zero terms. Those statements, if the remaining proof audit succeeds, upgrade `(11)` from a limsup obstruction to a full logarithmic-order description and couple the global average to a terminal-window maximum.

The distinction matters for the research line:

- **RH completeness of the mean-absolute upper bound:** elementary Mellin continuation, now independent of `MC-S19`;
- **exact asymptotic zero-edge fidelity of the mean absolute and near-end maximum:** the stronger fresh Pintz theorem, still under the audit status recorded in `MC-009`--`MC-012`.

The v2 preprint still displays the three presentation defects already isolated in `MC-010`--`MC-012` (the signed `gamma` in `(2.10)`, the missing shifted-height factor in `(6.23)`, and the `epsilon/9` versus `epsilon/8` window mismatch in Section 7), so the stronger theorem should not be silently upgraded merely because a newer arXiv version exists.

## Prior art and novelty boundary

The mechanism in `(7)`--`(9)` is classical Abel/Mellin summation for a Dirichlet series. The same zero-exclusion pattern is already used internally in `MC-019` for the first Möbius Riesz sum. Pintz's current preprint itself starts from the standard reciprocal-zeta/Möbius transform and supplies the much deeper full logarithmic-order theorem.

A targeted search for an established separately named "mean-absolute Mertens criterion" did not surface a canonical named theorem. That absence is not evidence of novelty: `(4)` is an immediate consequence of standard Dirichlet-series continuation once `(7)` is written down. **No novelty claim is made.** The durable contribution here is the correction of the line's dependency graph and the explicit exact proof that the weaker mean-absolute target is RH-complete without relying on the fresh preprint.

Primary fresh-literature boundary:

- János Pintz, *Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*, arXiv:2608.24878v2, 1 September 2026. Theorems 2.1--2.2 state the stronger logarithmic-order comparison. The current v2 HTML still contains the audited presentation issues noted above.

## Boundaries and falsification tests

- The implication uses an **absolute** first moment. A signed average such as `X^(-1) integral M(u) du` can be small through cancellation and does not give `(7)`.
- A bound only on a sparse sequence of cutoffs `X` does not automatically control `A(X)` between those cutoffs unless the sequence has a bounded multiplicative gap or another interpolation argument is supplied.
- The exponent in `(1)` must be strictly to the left of the zero one wishes to exclude. Borderline convergence at `sigma=alpha` is not claimed.
- The result says nothing about the size of `1/zeta(s)` inside the continued half-plane beyond holomorphy, and it gives no unconditional improvement for `M` or `D_M`.
- Pintz's stronger full-limit statement remains logically separate. This finding cannot be used to certify the still-audited steps of that theorem.

A decisive falsifier would be a function `M` satisfying the exact Möbius Mellin identity `(9)` on `Re(s)>1` and `(1)` for some `alpha`, while `zeta` has a zero with real part greater than `alpha`. Absolute convergence and uniqueness of continuation rule this out.

## Consequence for the research line

The accepted mean-absolute transfer direction is stronger than previously recorded operationally. A source-natural local or multiscale mechanism does **not** need Pintz's new theorem to turn an RH-scale bound for `D_M` into RH: once it proves

\[
D_M(X)=O_\varepsilon(X^{1/2+\varepsilon}),
\]

the Mellin argument above closes the zero-free implication exactly.

This lowers the literature dependency of that route but does not lower its arithmetic information budget. `MC-001`, `MC-006`, and the later transfer obstructions still show that the currently controlled local/averaged inputs do not supply the required polynomial mean-absolute bound. The live problem is therefore cleanly separated: **produce the mean-absolute bound arithmetically; zero exclusion then follows by a classical transform.** Pintz remains relevant only for the stronger claim that the entire logarithmic growth profile of the mean is itself locked to the zero edge.