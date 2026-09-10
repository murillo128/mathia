# PF-257 — normalized Robin injection is a polar-free resolvent transform

**Status:** `EXACT-DERIVED + NONCOMMUTATIVE-ROBIN-FACTORIZATION + POLAR-RECOMBINATION + RESOLVENT-TRANSFORM + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-254-normalized-noncommuting-robin-injection-splits-square-root-amplitude-from-polar-transport|PF-254]] writes the energy-normalized Robin source factor as `h(\mathcal R)U`, with `h(\lambda)=\sqrt\lambda/(1+\lambda)` and `U` the polar partial isometry of `K^{-1/2}Q^{1/2}`. That factorization is exact, but it can make the live locality gate look stronger than the physical map requires: the Poisson problem never contains the naked polar factor `U`.

There is an equally exact **polar-free recombination**. Put

\[
X:=K^{-1/2}Q^{1/2},
\qquad
\mathcal R=XX^*,
\qquad
\mathcal S=X^*X.
\]

Then on every bounded positive regularization used in PF-254,

\[
\boxed{
K^{1/2}(K+Q)^{-1}Q^{1/2}
=(I+XX^*)^{-1}X
=X(I+X^*X)^{-1}.
}
\tag{1}
\]

Equivalently, if

\[
\mathbb D_X=
\begin{pmatrix}
0&X\\
X^*&0
\end{pmatrix},
\qquad
F(t)=\frac{t}{1+t^2},
\]

then the normalized Robin injection in (1) is exactly the upper-right block of `F(\mathbb D_X)`. The scalar transform is regular at the zero edge and satisfies `|F(t)|\le1/2`. In particular, a polar partial isometry may be unstable or nonlocal near small singular values of `X` while the **combined physical factor** remains controlled because those directions are weighted by the same singular values before the Robin denominator is applied.

This does not prove the PF-243 separated smoothing estimate. PF-244 remains a valid obstruction: an `X` with bad high-to-low conversion can make the combined factor in (1) bad as well. What changes is the decisive test. A failure to prove graph locality of `U` alone is no longer a reason to kill the route. The canonical object to estimate is the regularized transform in (1), or equivalently the block resolvent of `\mathbb D_X`, because that is what the actual Robin source map sees.

## Claim

Let `H` be a Hilbert space. On a bounded regularization let `K=K^*>0` have bounded inverse and let `Q=Q^*\ge0` be bounded. Define

\[
A_Q:=(K+Q)^{-1}Q^{1/2},
\qquad
X:=K^{-1/2}Q^{1/2},
\]

and `\mathcal R=XX^*`, `\mathcal S=X^*X`. Then:

1. the energy-normalized source factor has the two push-through forms
   \[
   \boxed{
   K^{1/2}A_Q
   =(I+\mathcal R)^{-1}X
   =X(I+\mathcal S)^{-1};
   }
   \tag{2}
   \]
2. if `X=\mathcal R^{1/2}U` is the left polar decomposition from PF-254, then
   \[
   \boxed{
   h(\mathcal R)U
   =(I+\mathcal R)^{-1}X,
   \qquad
   h(\lambda)=\frac{\sqrt\lambda}{1+\lambda};
   }
   \tag{3}
   \]
3. for the self-adjoint block operator
   \[
   \mathbb D_X=
   \begin{pmatrix}0&X\\X^*&0\end{pmatrix},
   \tag{4}
   \]
   one has
   \[
   \boxed{
   F(\mathbb D_X)
   =
   \begin{pmatrix}
   0&X(I+X^*X)^{-1}\\
   X^*(I+XX^*)^{-1}&0
   \end{pmatrix},
   \qquad
   F(t)=\frac{t}{1+t^2};
   }
   \tag{5}
   \]
4. consequently
   \[
   \boxed{\|K^{1/2}A_Q\|\le\frac12;}
   \tag{6}
   \]
5. the two Gram operators are polar-free:
   \[
   \boxed{
   (K^{1/2}A_Q)(K^{1/2}A_Q)^*
   =\frac{\mathcal R}{(I+\mathcal R)^2},
   }
   \tag{7}
   \]
   and
   \[
   \boxed{
   (K^{1/2}A_Q)^*(K^{1/2}A_Q)
   =\frac{\mathcal S}{(I+\mathcal S)^2};
   }
   \tag{8}
   \]
6. the combined factor is stable under perturbation of `X`: if `Y` is another bounded operator and `B_X=X(I+X^*X)^{-1}`, then
   \[
   \boxed{
   \|B_X-B_Y\|\le\|X-Y\|.
   }
   \tag{9}
   \]
   More generally, for `1\le p<\infty`, if `X-Y\in\mathcal S_p`, then
   \[
   \|B_X-B_Y\|_{\mathcal S_p}
   \le 2^{1/p}\|X-Y\|_{\mathcal S_p}.
   \tag{10}
   \]

The same block-functional-calculus identities extend in the standard way to a closed densely defined `X` whenever the corresponding relative square-root map has been constructed. PF-257 does **not** assert that the full unbounded complete-lift Prime-Flute operator has already passed that domain/closure gate; the exact project claim is first made on the same finite/Galerkin regularizations for which PF-254 is exact.

## 1. The push-through identity recombines amplitude and orientation

PF-254 gives

\[
K+Q
=K^{1/2}(I+\mathcal R)K^{1/2}.
\]

Therefore

\[
K^{1/2}A_Q
=(I+\mathcal R)^{-1}K^{-1/2}Q^{1/2}
=(I+XX^*)^{-1}X.
\tag{11}
\]

The elementary intertwining identity

\[
(I+XX^*)X=X(I+X^*X)
\]

implies

\[
(I+XX^*)^{-1}X=X(I+X^*X)^{-1},
\tag{12}
\]

which proves (2).

Now use the PF-254 polar decomposition `X=\mathcal R^{1/2}U`. Since functions of `\mathcal R` commute,

\[
(I+\mathcal R)^{-1}X
=\mathcal R^{1/2}(I+\mathcal R)^{-1}U
=h(\mathcal R)U.
\tag{13}
\]

Thus the polar split and the polar-free form are the **same operator**, not competing approximations. The latter keeps the singular amplitude and its orientation correlated instead of bounding them separately.

This distinction matters at the critical edge. The partial isometry `U` records only direction and can change discontinuously when singular values approach zero. The product `(I+XX^*)^{-1}X`, by contrast, vanishes linearly with the singular value of `X` at zero. Therefore an estimate that first replaces `h(\mathcal R)U` by `\|h(\mathcal R)\|\,U` or demands an independent weighted bound on `U` can discard a cancellation that the actual Robin map retains.

## 2. A self-adjoint block linearization removes the polar variable completely

Squaring (4) gives

\[
\mathbb D_X^2=
\begin{pmatrix}
XX^*&0\\
0&X^*X
\end{pmatrix}.
\tag{14}
\]

Hence ordinary self-adjoint functional calculus gives

\[
\mathbb D_X(I+\mathbb D_X^2)^{-1}
=
\begin{pmatrix}
0&X(I+X^*X)^{-1}\\
X^*(I+XX^*)^{-1}&0
\end{pmatrix},
\]

which is (5). Since

\[
\sup_{t\in\mathbb R}\left|\frac{t}{1+t^2}\right|=\frac12,
\]

(6) follows immediately.

Equations (7)--(8) are equally direct. Using the left form of (2),

\[
B_XB_X^*
=(I+\mathcal R)^{-1}\mathcal R(I+\mathcal R)^{-1},
\]

while the right form gives the analogous identity in `\mathcal S`.

The important Prime-Flute point is not the norm `1/2`, which is elementary. It is that **no naked polar factor occurs in the block functional calculus**. If a useful mode-local algebra can be proved for the actual `\mathbb D_{X_w}`, the normalized injection should be studied as the rational transform `F(\mathbb D_{X_w})`, rather than by separately estimating `h(\mathcal R_w)` and `U_w`.

## 3. The combined factor is stable even when the polar factor is not

The rational function in (5) has the resolvent representation

\[
F(\mathbb D)
=\frac12\left((\mathbb D-iI)^{-1}+(\mathbb D+iI)^{-1}\right).
\tag{15}
\]

For self-adjoint `\mathbb D_X,\mathbb D_Y`, the resolvent identity gives

\[
(\mathbb D_X\mp iI)^{-1}-(\mathbb D_Y\mp iI)^{-1}
=(\mathbb D_X\mp iI)^{-1}
(\mathbb D_Y-\mathbb D_X)
(\mathbb D_Y\mp iI)^{-1}.
\tag{16}
\]

Both resolvents have norm at most `1`. Combining the two signs and taking the upper-right block proves (9), because

\[
\|\mathbb D_X-\mathbb D_Y\|=\|X-Y\|.
\]

The same argument in `\mathcal S_p`, using the ideal property, gives

\[
\|F(\mathbb D_X)-F(\mathbb D_Y)\|_{\mathcal S_p}
\le
\|\mathbb D_X-\mathbb D_Y\|_{\mathcal S_p}
=2^{1/p}\|X-Y\|_{\mathcal S_p},
\]

and an off-diagonal block cannot have larger Schatten norm than the full block operator. This proves (10).

There is no analogous uniform continuity statement for the polar partial isometry at a closing singular-value gap. That is precisely why the combined transform is the safer perturbative object.

## 4. Consequence for the current Prime-Flute endpoint gate

The accepted critical-Jacobi clue currently asks for

\[
h(\mathcal R_w)U_wK_a^RP_Z
\]

to remain controlled for some `R>1`. PF-257 shows that this should be regarded as the single operator

\[
\boxed{
B_wK_a^RP_Z,
\qquad
B_w:=X_w(I+X_w^*X_w)^{-1},
\qquad
X_w:=K_a^{-1/2}(Q_w^{\rm act})^{1/2}.
}
\tag{17}
\]

A proof may still choose the PF-254 polar split if it is useful, but **locality of `U_w` is sufficient, not necessary**. A nonlocal `U_w` does not kill the route unless that nonlocality survives the singular-value weight and the Robin denominator in `B_w`.

This opens a more faithful fixed-axis route. After factoring the already-controlled PF-255/PF-256 hypercycle and variable-corridor transports, derive `X_w` itself in the PF-247 Gegenbauer/parity representation. Then test the regularized block operator `F(\mathbb D_{X_w})` directly for high-to-low decay. If the relation to PF-247's Jacobi edge is best expressed through `\mathcal R_w=X_wX_w^*`, PF-253's square-root window remains available. But it is no longer necessary to force the proof through a separate theorem about the polar partial isometry.

PF-254's reflection factors also remain polar-free:

\[
c(\mathcal R_w)=\frac{I-\mathcal R_w}{I+\mathcal R_w}.
\]

Thus the actual two-boundary product formula contains the combined injection `B_w`, rational functions of `\mathcal R_w`, and longitudinal propagation. The polar factor appears only after an optional algebraic split. This identifies the minimal noncommutative data that the fixed-axis analysis really has to control.

## 5. Why PF-244 is not bypassed

PF-244 constructs a legitimate abstract failure of separated spectral smoothing. PF-257 does not remove it. If `X` itself sends high `K` input into a low-cost output direction with non-negligible singular amplitude, then

\[
X(I+X^*X)^{-1}
\]

can retain that high-to-low channel. The block rational transform is bounded and stable, not automatically local.

The new exclusion is narrower: **bad behavior of `U` by itself is not evidence of bad behavior of the Robin injection**. A counterexample relevant to the current Prime-Flute route must be a counterexample for the combined factor `B_w` (and, where needed, the reflection transforms), in the actual fixed-axis geometry.

This also prevents a false negative near the critical zero edge. The polar factor is least stable exactly where `X` is small, while the physical map suppresses those same directions. Any adversarial test should preserve that correlation.

## 6. Prior-art and novelty audit

The operator theory in PF-257 is classical. The push-through identity is elementary, polar decomposition and the self-adjoint `2x2` linearization of an operator are standard, and bounded-transform/functional-calculus methods for closed operators are established operator-theory machinery. A targeted audit of bounded-transform literature confirms that treating an unbounded or nonnormal operator through bounded functions of a self-adjoint transform is standard; no general operator-theory novelty is claimed here.

PF-254 already records the relevant Robin/boundary-map prior art and explicitly classifies its noncommutative factorization as a project-specific organization rather than a new theorem about Robin maps. PF-257 has the same status. Its mathematical delta is **internal to the Prime-Flute proof strategy**: the exact source factor can be recombined into a regular rational transform, so separate polar locality is not a logically necessary gate and must not be used as a standalone falsification criterion.

No claim is made that `F(\mathbb D_{X_w})` has exponential, polynomial, Jacobi, or pseudodifferential off-diagonal decay. Establishing such a property for the actual fixed-axis seam remains new work.

## 7. Boundary conditions and falsification

- Equations (1)--(16) are exact on every bounded positive/Galerkin regularization. Passing to the full complete-lift form requires construction and closure of the actual relative square-root map `X_w`; PF-257 does not silently assume that step.
- `\|B_X\|\le1/2` is only an unweighted bound. It does not imply `B_XK_a^R` is bounded for any `R>0`.
- Schatten stability (10) concerns perturbations measured directly in `X`; PF-235/PF-256 do not by themselves prove that the actual fixed-axis `X_w` is close to a reference in such a norm.
- PF-253's `R<3` theorem for literal `J_\varepsilon^{1/2}` is not automatically a theorem for `B_w`. An explicit dictionary or direct block estimate is still required.
- Reflection factors `c(\mathcal R_w)` can also mix modes unless their relation to the actual Jacobi/local structure is controlled.
- A standalone failure of graph locality for `U_w` is no longer a decisive negative. A failure of the combined estimate in (17) is.

## Decisive next test

Derive the fixed-axis regularized operator

\[
X_w=K_a^{-1/2}(Q_w^{\rm act})^{1/2}
\]

after removing the PF-255/PF-256-controlled hypercycle coordinate/density factors. In the actual `K_a` mode basis, test directly whether

\[
E_{\le M}\,B_w\,E_{\ge N},
\qquad
B_w=X_w(I+X_w^*X_w)^{-1},
\]

has enough uniform separated decay to yield `B_wK_a^RP_Z\in\mathcal B` for some `R>1`.

There are two legitimate positive routes: derive `X_wX_w^*` in a form to which PF-253's Jacobi square-root analysis applies **without discarding the correlation with `X_w`**, or establish graph/locality estimates for the block operator `\mathbb D_{X_w}` and pass them through the rational resolvent representation (15). Kill the route only if the combined physical transform still has a non-summable high-to-low tail, or if the full form realization destroys the finite-regularization identity. Do not kill it merely because the auxiliary polar partial isometry is nonlocal.