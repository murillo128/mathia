# WP-133 — Anchored zero-mode renormalization cannot inherit Gamma-semigroup contractivity

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + FINITE-CYCLIC-KERNEL + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-132` closes bounded and distributional exact intertwiners between the radial/Mellin Gamma carrier and the Prime-Circle solenoid carrier, but exposes a genuine category-changing escape: replace critical point samples by anchored differences

\[
f(\lambda)-f(0).
\]

At reciprocal prime-power frequencies this supplies the extra vanishing needed to make the critical weighted star energy locally summable. Because the subtraction changes the exact diagonal Gamma intertwining law, `WP-132` leaves open whether the resulting positive boundary form might nevertheless inherit its sign from the already-canonical Gamma heat semigroup through an energy-contraction theorem.

That inheritance route is empty already on every finite one-sided sample block.

Let

\[
0<\lambda_1<\cdots<\lambda_N,
\qquad
m_j=e^{-\tau H_\infty(\lambda_j)},
\qquad \tau>0,
\]

where

\[
H_\infty(t)=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\psi\!\left(\frac14\right)
\]

is the Prime-Circle-selected Gamma symbol of `WP-117`/`WP-129`. Since `WP-129` proves that `H_\infty` is strictly increasing on `(0,\infty)`,

\[
1>m_1>\cdots>m_N>0.
\]

Put

\[
T=\operatorname{diag}(1,m_1,\ldots,m_N)
\]

on the finite value space with coordinates `(f(0),f(lambda_1),...,f(lambda_N))`, and let

\[
\mathbf 1=(1,1,\ldots,1)^T.
\]

Then the following exact finite-dimensional statement holds:

\[
\boxed{
P\succeq0,
\quad P\mathbf1=0,
\quad T^*PT\preceq P
\quad\Longrightarrow\quad
P=0.
}
\tag{1}
\]

Equivalently, there is no nonzero positive quadratic form that both kills constants, as an anchored-difference renormalization must, and is contractive under even one nontrivial time step of the existing diagonal Gamma heat dynamics.

The proof is a one-line kernel-propagation argument plus a Vandermonde determinant. If

\[
Q(x)=x^*Px,
\]

then `P>=0` and `Q(1)=0` imply `P 1=0`. Contractivity gives

\[
0\le Q(T^n\mathbf1)\le Q(\mathbf1)=0
\qquad(n\ge0),
\]

so every orbit vector

\[
T^n\mathbf1=(1,m_1^n,\ldots,m_N^n)^T
\]

lies in `ker P`. The `N+1` vectors with `n=0,...,N` form a Vandermonde matrix on the pairwise distinct nodes

\[
1,m_1,\ldots,m_N.
\]

They therefore span the entire value space, forcing `ker P` to be the whole space and hence `P=0`.

Thus the zero-mode subtraction in `WP-132` is more than merely non-intertwining. **Any nontrivial positive anchored form on distinct positive Gamma frequencies must abandon contractivity under the old Gamma semigroup.** If this boundary renormalization contributes to a Weil-positive mechanism, its independent sign theorem must belong to a genuinely new coupled operator or geometry rather than being inherited from the already-positive Gamma Markov dynamics.

This is a structural negative, not a global Weil theorem. It does not rule out an independently positive anchored Dirichlet form such as `WP-072`, a new triangular generator, a Schur complement, a quotient with changed dynamics, a nonlocal finite--archimedean form, or a cohomological construction. It rules out only the tempting claim that the `WP-132` counterterm can change the sampling category while retaining the old Gamma semigroup as the source of its contraction/Dirichlet sign.

## 1. The finite Gamma value dynamics

`WP-129` proves

\[
H_\infty(t)=F(t^2)
\]

with `F` a strictly increasing complete Bernstein function on `[0,\infty)`. Hence for every fixed `tau>0`,

\[
m_\tau(t):=e^{-\tau H_\infty(t)}
\]

is strictly decreasing in `t>0`, satisfies `m_tau(0)=1`, and lies strictly between zero and one away from the origin.

Choose any finite set of distinct positive frequencies `lambda_j`. Evaluation of the radial Gamma heat multiplier on these values is therefore represented exactly by

\[
T=\operatorname{diag}(1,m_\tau(\lambda_1),\ldots,m_\tau(\lambda_N)).
\tag{2}
\]

No arithmetic assumption is needed here. The reciprocal prime-power frequencies singled out in `WP-132` are one admissible specialization.

An anchored-difference quadratic form depends only on differences from the zero mode. In particular every constant value vector is null. For a Hermitian positive-semidefinite matrix `P`, this means

\[
Q(\mathbf1)=\mathbf1^*P\mathbf1=0
\quad\Longleftrightarrow\quad
P\mathbf1=0,
\tag{3}
\]

because `P^{1/2}\mathbf1=0`.

The natural way to inherit the existing Gamma Markov sign is energy contractivity:

\[
Q(Tx)\le Q(x)
\qquad\text{for every }x,
\tag{4}
\]

or equivalently

\[
T^*PT\preceq P.
\tag{5}
\]

This is the standard Dirichlet/Lyapunov-type compatibility one would expect if the old Gamma heat evolution were still the dynamics responsible for the new form's sign.

## 2. Contractivity propagates the null constant through the whole cyclic subspace

From (3)--(5),

\[
0\le Q(T\mathbf1)\le Q(\mathbf1)=0,
\]

so `T 1 in ker P`. Iterating (4),

\[
\boxed{T^n\mathbf1\in\ker P\qquad(n\ge0).}
\tag{6}
\]

This observation is independent of diagonalization. For any positive semidefinite contractive seminorm, a null vector carries its entire forward orbit into the nullspace.

For the present diagonal Gamma dynamics, however, the constant vector is cyclic on every finite block with distinct positive frequencies. The matrix whose columns are

\[
\mathbf1,T\mathbf1,\ldots,T^N\mathbf1
\]

has rows

\[
(1,1,\ldots,1),
\quad
(1,m_1,m_1^2,\ldots,m_1^N),
\ldots,
(1,m_N,m_N^2,\ldots,m_N^N).
\]

Its determinant is the Vandermonde product

\[
\boxed{
\prod_{0\le i<j\le N}(\mu_j-\mu_i),
\qquad
(\mu_0,\mu_1,\ldots,\mu_N)=(1,m_1,\ldots,m_N),
}
\tag{7}
\]

which is nonzero because all `mu_j` are distinct. Thus (6) places a basis of the value space in `ker P`, proving (1).

The argument uses only finite-dimensional positivity and the strictly separated Gamma multipliers. No zeta zeros, RH assumption, explicit-formula positivity, asymptotic prime estimate, or regularization enters it.

## 3. The explicit WP-132 star energy already fails on one edge

The general theorem can be seen in the smallest block. For one nonzero frequency with multiplier `0<m<1`, an anchored edge of weight `a>0` has

\[
Q_a(x_0,x_1)=a|x_1-x_0|^2,
\]

with matrix

\[
P_a=a
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\tag{8}
\]

Under `T=diag(1,m)`, energy contraction would require

\[
P_a-T^*P_aT\succeq0.
\]

But

\[
P_a-T^*P_aT
=
a
\begin{pmatrix}
0&m-1\\
m-1&1-m^2
\end{pmatrix},
\]

whose determinant is

\[
\boxed{-a^2(1-m)^2<0.}
\tag{9}
\]

So even one anchored Gamma edge is not contractive under the old diagonal heat evolution. Adding more edges or allowing arbitrary positive cross-couplings cannot repair this while keeping the constant mode null, because the cyclic-kernel theorem already forces the entire PSD form to vanish.

This sharpens the observation in `WP-132`. There the subtraction was shown not to satisfy exact intertwining. Here even the weaker requirement that the same Gamma heat dynamics merely **decrease** the new positive energy is impossible for any nonzero finite anchored form.

## 4. Application to reciprocal prime-power samples

`WP-132` considers the one-sided frequencies

\[
\lambda_{p,k}=2\pi p^{-k}
\]

with critical amplitudes

\[
c_{p,k}=\frac{\log p}{p^{k/2}}.
\]

For a finite set `S` of distinct prime powers, the natural renormalized positive boundary energy is of star type,

\[
E_S(f)
=
\sum_{(p,k)\in S}
\frac{(\log p)^2}{p^k}
\left|f(2\pi p^{-k})-f(0)\right|^2.
\tag{10}
\]

The extra difference factor regularizes the accumulation at zero for smooth `f`, exactly as `WP-132` records. But the frequencies in a finite one-sided prime-power block are distinct, so their Gamma heat multipliers are distinct. Equation (1) therefore applies without using the particular weights in (10):

\[
\boxed{
E_S\text{ cannot be contractive under the existing Gamma heat semigroup unless }E_S=0.
}
\tag{11}
\]

The obstruction is therefore orthogonal to the critical summability improvement. Zero-mode subtraction fixes the local `ell^2` divergence by changing the observable, but that same change destroys the possibility of deriving its sign as a contracted seminorm of the unchanged diagonal Gamma flow.

For an infinite projectively consistent anchored construction, every finite restriction that retains the same contraction law is forced to vanish. Thus a locally assembled positive star/graph completion cannot evade the theorem by taking an infinite limit. This statement does **not** cover an intrinsically nonlocal infinite form whose finite-coordinate restrictions are not closed under the proposed dynamics; such a construction would already be a different architectural category and requires its own analysis.

## 5. Repeated Gamma levels are the exact boundary of the theorem

The distinct-node hypothesis is load-bearing. Since `H_infty` is even, the pair `+lambda,-lambda` has the same Gamma multiplier. If a finite block contains repeated spectral levels, the orbit of the constant vector spans only one direction inside each repeated eigenspace. Contractivity then forces `P` to vanish on that cyclic subspace but may leave directions orthogonal to it inside the repeated eigenspaces.

For the simplest `+-lambda` pair, the surviving direction is antisymmetric between the two equal-energy samples. That is a genuine boundary condition of (1), not a counterexample. It does not implement the zero-to-positive-frequency anchor used by the reciprocal prime-power construction, whose one-sided positive frequencies have distinct Gamma levels.

More generally, the exact statement behind (1) is

\[
\boxed{
\overline{\operatorname{span}}\{T^n\mathbf1:n\ge0\}
\subseteq\ker P.
}
\tag{12}
\]

On a finite simple-spectrum block the cyclic subspace is everything; with multiplicities only within-level contrasts can survive. Thus any proposed escape based on Gamma-degenerate sectors must explain how such same-level contrasts generate the finite Mangoldt selector and the archimedean/global terms rather than merely exploiting the `t\leftrightarrow -t` symmetry.

## 6. Why this does not contradict the pointed Dirichlet survivor

`WP-072` constructs the independently positive Prime-Circle base-point form

\[
D_1(F)
=
\left\|
\frac{F(z)-F(1)}{z-1}
\right\|_{H^2}^2
\]

and proves that the Mangoldt anchor `F_n(1)=Lambda(n)` is bounded in that geometry. That result is not threatened by (1). `D_1` is a new pointed Hardy/Dirichlet norm with its own positivity theorem; it was never claimed to be contractive under the radial Gamma heat multiplier considered here.

This comparison clarifies the remaining burden. Breaking the zero mode or privileging a base point can indeed regularize arithmetic data positively. What cannot be done is to perform that symmetry breaking and then say that the **old Gamma semigroup** is still the theorem forcing the new energy's sign. Once the anchor is introduced, the successful sign mechanism must be justified in the altered geometry itself.

That is exactly the distinction required by the branch mandate: nonnegativity must precede identification with the desired arithmetic consequence, and the finite and archimedean pieces must arise from one audited construction rather than from a positive finite norm plus an unrelated positive Gamma flow.

## 7. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the linear-algebra mechanism. The implications

\[
P\succeq0,\quad T^*PT\preceq P
\quad\Longrightarrow\quad
\ker P\text{ contains the forward orbit of every null vector}
\]

belong to standard finite-dimensional Lyapunov/contractive-seminorm reasoning, and the cyclicity of `(1,...,1)` for a diagonal matrix with simple spectrum is exactly the classical Vandermonde determinant criterion.

A directed search across discrete Lyapunov inequalities, invariant kernels/unobservable subspaces, contractive seminorms, cyclic vectors, diagonal simple-spectrum operators, and Vandermonde criteria found only these standard ambient mechanisms; no source located in that search treats the specific Gamma multiplier plus zero-mode renormalization and reciprocal-prime-power boundary problem. That absence is not evidence of historical novelty. The durable contribution is the Mathia-specific specialization that closes an explicit escape left by `WP-132`.

The nearest internal prior-art controls are different. `WP-131` rules out bounded exact radial--solenoid intertwiners by spectral type; `WP-132` classifies distributional exact intertwiners and observes that anchored subtraction necessarily changes covariance; `WP-072` supplies a positive pointed norm but no Gamma/global completion. Equation (1) fills the gap between them by proving that **changing exact covariance to mere Gamma energy contractivity still does not preserve a nontrivial anchored form**.

## 8. Consequence for the Weil-positivity search

The post-`WP-132` boundary is now sharper. The chain

\[
\text{critical point sampler}
\longrightarrow
\text{zero-mode subtraction}
\longrightarrow
\text{positive anchored energy}
\]

is mathematically real and fixes the local critical summability defect, but it cannot continue with

\[
\text{same Gamma heat flow}
\longrightarrow
\text{contractive/Dirichlet sign theorem}.
\]

A viable finite--archimedean construction must therefore alter the operator **before or together with** the anchoring: for example a source-forced triangular generator, non-passive boundary response, Schur complement, genuinely nonlocal completion, or cohomological coupling whose own positivity theorem is established directly. Such mechanisms remain outside this theorem.

No finite Mangoldt-plus-Gamma-plus-polar Weil form is obtained here. The result is a decisive negative on one natural inherited-sign route and further supports the current requirement that the missing Mathia mechanism be a genuinely joint finite--archimedean operation rather than a counterterm applied after the positive local components have already been separated.

## Cross-references

- `research/weil_positivity/findings/WP-072-base-point-local-dirichlet-energy-regularizes-mangoldt-anchor-but-is-not-global-weil-form.md`
- `research/weil_positivity/findings/WP-117-riemann-gamma-digamma-variation-is-markov-positive-but-critical-prime-coupling-diverges.md`
- `research/weil_positivity/findings/WP-129-gamma-symbol-is-subordinate-brownian-so-unrestricted-cnd-warps-are-tautological.md`
- `research/weil_positivity/findings/WP-131-bounded-radial-solenoid-gamma-intertwiners-vanish-by-spectral-type.md`
- `research/weil_positivity/findings/WP-132-exact-distributional-gamma-intertwiners-are-point-samplers-and-nonclosable-in-natural-l2.md`
