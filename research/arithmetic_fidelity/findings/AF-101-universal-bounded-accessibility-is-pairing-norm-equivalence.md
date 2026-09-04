# AF-101 — Universal bounded accessibility is pairing-norm equivalence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `QUANTITATIVE-FIDELITY-REFINEMENT`, `CLASSICAL-TENSOR-DUALITY-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let `X` and `K` be Banach spaces. Retain AF-100's canonical embedding

\[
J_K:K\to K^{**}
\]

and bounded pointwise weak-star accessibility gauge

\[
a_K(U)
=
\inf\Bigl\{C\ge0:
U\in\overline{\{J_KS:\|S\|\le C\}}^{\,\tau_{pw^*}}
\Bigr\},
\qquad
U\in\mathcal L(X,K^{**}).
\tag{1}
\]

On the algebraic tensor product `X\otimes K^*`, define the `K`-valued operator-pairing norm

\[
\alpha_{X,K}(u)
:=
\sup_{\|S\|\le1}
\left|
\sum_{j=1}^m k_j^*(Sx_j)
\right|,
\qquad
u=\sum_{j=1}^m x_j\otimes k_j^*.
\tag{2}
\]

Write `\varepsilon` and `\pi` for the injective and projective tensor norms on `X\otimes K^*`.

Then:

### 1. The original and relaxed target categories induce two exact tensor gauges

`\alpha_{X,K}` is a genuine crossnorm and

\[
\boxed{
\varepsilon(u)\le\alpha_{X,K}(u)\le\pi(u)
\qquad(u\in X\otimes K^*).
}
\tag{3}
\]

The upper gauge is exactly the same pairing optimized over the relaxed bidual target:

\[
\boxed{
\pi(u)
=
\sup_{\substack{U\in\mathcal L(X,K^{**})\\\|U\|\le1}}
\left|
\sum_{j=1}^m\langle Ux_j,k_j^*\rangle
\right|.
}
\tag{4}
\]

Thus the ratio `\pi(u)/\alpha_{X,K}(u)` is the exact finite-observation advantage obtained by allowing the target to enlarge from `K` to `K^{**}` at the same operator-norm budget.

### 2. AF-100's accessibility gauge is exactly the dual norm of `\alpha_{X,K}`

Let

\[
E_{X,K}
:=
\overline{X\otimes K^*}^{\,\alpha_{X,K}}.
\tag{5}
\]

For `U\in\mathcal L(X,K^{**})`, define on algebraic tensors

\[
f_U\!\left(\sum_jx_j\otimes k_j^*\right)
:=
\sum_j\langle Ux_j,k_j^*\rangle.
\tag{6}
\]

Then

\[
\boxed{
f_U\in E_{X,K}^*
\iff
a_K(U)<\infty,}
\tag{7}
\]

and in that case

\[
\boxed{
\|f_U\|_{E_{X,K}^*}=a_K(U).
}
\tag{8}
\]

Hence there is a canonical isometric identification

\[
\boxed{
E_{X,K}^*
\cong
\mathcal A(X,K)
:=
\{U\in\mathcal L(X,K^{**}):a_K(U)<\infty\},
}
\tag{9}
\]

where `\mathcal A(X,K)` carries the norm `a_K`.

### 3. The universal accessibility constant has an exact primal tensor formula

For nonzero `X,K`, define the extended constant

\[
C_{\mathrm{acc}}(X,K)
:=
\sup_{0\ne U\in\mathcal L(X,K^{**})}
\frac{a_K(U)}{\|U\|}
\in[1,+\infty].
\tag{10}
\]

Then

\[
\boxed{
C_{\mathrm{acc}}(X,K)
=
\sup_{0\ne u\in X\otimes K^*}
\frac{\pi(u)}{\alpha_{X,K}(u)}.
}
\tag{11}
\]

Thus the worst bidual-to-target accessibility overhead is already completely encoded by finite tensors. No separate infinite observational invariant is needed to compute the universal constant.

### 4. Pointwise finite accessibility automatically upgrades to one uniform constant

Because `\alpha_{X,K}\le\pi`, the algebraic identity extends to a contractive dense-range map

\[
q_{X,K}:
X\widehat\otimes_\pi K^*
\longrightarrow
E_{X,K}.
\tag{12}
\]

Its adjoint is exactly the canonical inclusion

\[
q_{X,K}^*:
\mathcal A(X,K)
\hookrightarrow
\mathcal L(X,K^{**}).
\tag{13}
\]

The following are equivalent:

1. every `U\in\mathcal L(X,K^{**})` has `a_K(U)<\infty`;
2. there exists one finite `C` such that
   \[
   a_K(U)\le C\|U\|
   \qquad(U\in\mathcal L(X,K^{**}));
   \tag{14}
   \]
3. there exists one finite `C` such that
   \[
   \pi(u)\le C\alpha_{X,K}(u)
   \qquad(u\in X\otimes K^*);
   \tag{15}
   \]
4. `q_{X,K}` is a Banach-space isomorphism.

The least admissible `C` in (14)--(15) is exactly `C_{\mathrm{acc}}(X,K)` and equals `\|q_{X,K}^{-1}\|` when the equivalent conditions hold.

Consequently there is a sharp global dichotomy:

\[
\boxed{
C_{\mathrm{acc}}(X,K)=+\infty
\Longrightarrow
\exists U\in\mathcal L(X,K^{**})\text{ with }a_K(U)=+\infty.
}
\tag{16}
\]

It is impossible for every bidual-valued operator to be individually accessible with finite cost while the required costs merely drift to infinity without a common multiplicative bound.

The reusable Arithmetic Fidelity principle is therefore

\[
\boxed{
\text{universal bounded recovery from a relaxed target is exactly norm equivalence of the original and relaxed finite-observation gauges.}
}
\tag{17}
\]

## Derivation

### 1. `\alpha_{X,K}` is a norm between `\varepsilon` and `\pi`

For an elementary tensor,

\[
\alpha_{X,K}(x\otimes k^*)
=
\sup_{\|S\|\le1}|k^*(Sx)|
=
\|x\|\,\|k^*\|,
\tag{18}
\]

so the elementary crossnorm condition holds.

More generally, if

\[
u=\sum_jx_j\otimes k_j^*,
\tag{19}
\]

then every `S` with `\|S\|\le1` gives

\[
\left|\sum_jk_j^*(Sx_j)\right|
\le
\sum_j\|x_j\|\,\|k_j^*\|.
\tag{20}
\]

Taking the infimum over representations gives

\[
\alpha_{X,K}(u)\le\pi(u).
\tag{21}
\]

For the reverse injective bound, rank-one maps already suffice. If `x^*\in B_{X^*}` and `k\in B_K`, then

\[
S_{x^*,k}(x)=x^*(x)k
\tag{22}
\]

has norm at most one, so

\[
\alpha_{X,K}(u)
\ge
\sup_{\substack{x^*\in B_{X^*}\\k\in B_K}}
\left|
\sum_jx^*(x_j)k_j^*(k)
\right|.
\tag{23}
\]

For fixed `x^*`, the supremum over `k\in B_K` is the norm of

\[
\sum_jx^*(x_j)k_j^*\in K^*.
\tag{24}
\]

This is exactly the standard injective norm formula, hence

\[
\varepsilon(u)\le\alpha_{X,K}(u).
\tag{25}
\]

In particular `\alpha_{X,K}` is nondegenerate.

Equation (4) is the standard projective-tensor duality

\[
\bigl(X\widehat\otimes_\pi K^*\bigr)^*
\cong
\mathcal L(X,K^{**}).
\tag{26}
\]

### 2. AF-100's polar formula is precisely `\alpha`-duality

Every finite matrix-coefficient functional from AF-100 has the form

\[
\Phi_u(V)
=
\sum_j\langle Vx_j,k_j^*\rangle
\tag{27}
\]

for some algebraic tensor `u=\sum_jx_j\otimes k_j^*`. Its AF-100 denominator is

\[
h_K(\Phi_u)
=
\sup_{\|S\|\le1}
\left|\sum_jk_j^*(Sx_j)\right|
=
\alpha_{X,K}(u).
\tag{28}
\]

Therefore AF-100 equation (9) becomes exactly

\[
a_K(U)
=
\sup_{0\ne u\in X\otimes K^*}
\frac{|f_U(u)|}{\alpha_{X,K}(u)}.
\tag{29}
\]

This is the operator norm of `f_U` on the `\alpha`-completion when finite, proving (7)--(8).

Conversely, every `f\in E_{X,K}^*` is automatically projective-continuous because

\[
|f(u)|\le\|f\|\alpha_{X,K}(u)
\le
\|f\|\pi(u).
\tag{30}
\]

Hence (26) represents `f` uniquely as some `f_U` with `U\in\mathcal L(X,K^{**})`. This proves the surjectivity of the identification (9), not merely an embedding.

### 3. The universal constant is the ratio of the two finite gauges

Using (29) and homogeneity,

\[
\begin{aligned}
C_{\mathrm{acc}}(X,K)
&=
\sup_{\|U\|\le1}a_K(U)\\
&=
\sup_{\|U\|\le1}
\sup_{0\ne u}
\frac{|f_U(u)|}{\alpha_{X,K}(u)}\\
&=
\sup_{0\ne u}
\frac{
\sup_{\|U\|\le1}|f_U(u)|
}{\alpha_{X,K}(u)}\\
&=
\sup_{0\ne u}
\frac{\pi(u)}{\alpha_{X,K}(u)}.
\end{aligned}
\tag{31}
\]

This proves (11), including the value `+\infty`.

### 4. Open mapping rules out unbounded finite costs for all operators

The map `q_{X,K}` in (12) is well-defined and contractive by `\alpha\le\pi`, and its range is dense because it contains the algebraic tensors densely in `E_{X,K}`.

By (9) and (26), its adjoint is exactly (13). If every bidual-valued operator has finite accessibility cost, then (13) is a bounded bijection between Banach spaces

\[
(E_{X,K}^*,a_K)
\quad\text{and}\quad
(\mathcal L(X,K^{**}),\|\cdot\|).
\tag{32}
\]

The bounded inverse theorem therefore gives a finite `C` with (14). This proves `1 => 2`.

The equivalence of (14) and (15) follows directly from (31), and (15) says exactly that the algebraic identity has a bounded inverse from the `\alpha` norm back to the projective norm. Hence `2 <=> 3 <=> 4`. The same argument identifies the optimal inverse norm with (11).

Equation (16) is the contrapositive of `1 => 2`: failure of every uniform comparison constant forces at least one genuinely inaccessible bidual-valued operator.

## Exact controls

### Finite-dimensional source

AF-100 proved that when `X` is finite-dimensional,

\[
a_K(U)=\|U\|
\qquad
(U:X\to K^{**}).
\tag{33}
\]

Therefore

\[
C_{\mathrm{acc}}(X,K)=1,
\qquad
\alpha_{X,K}=\pi.
\tag{34}
\]

This is the local-reflexivity control. The distinction between the two gauges is necessarily an infinite-source phenomenon.

### Reflexive target

If `K` is reflexive, then `K^{**}=K` canonically and every relaxed operator is already target-valued. Hence again

\[
a_K(U)=\|U\|,
\qquad
C_{\mathrm{acc}}(X,K)=1,
\qquad
\alpha_{X,K}=\pi.
\tag{35}
\]

A merely dual or complemented-in-bidual target does not automatically give (35); AF-100 already records that a retraction `K^{**}\to K` solves a particular extension problem without identifying an arbitrary `U:X\to K^{**}` with its retracted image.

### Finite source slices do not remove the global extension constraint

If `u` is supported on a finite-dimensional `E\subset X`, local reflexivity shows that the relaxed projective pairing can be approximated by some operator `A:E\to K` with essentially the same norm. But `\alpha_{X,K}(u)` optimizes only over those local values arising as restrictions of global `S:X\to K` with the declared norm budget.

Thus the possible strict inequality

\[
\alpha_{X,K}(u)<\pi(u)
\tag{36}
\]

is not a failure of finite-dimensional bidual-to-target approximation. It is a global extension/compatibility defect: the locally adequate `K`-valued repair cannot be realized from the whole source at the same budget.

### Three quantitative regimes

The pair `(X,K)` has exactly three norm-level possibilities:

- `C_{\mathrm{acc}}=1`: isometric fidelity, `\alpha=\pi`, and `a_K(U)=\|U\|` for all `U`;
- `1<C_{\mathrm{acc}}<\infty`: every relaxed operator is recoverably accessible, but a universal multiplicative distortion is unavoidable;
- `C_{\mathrm{acc}}=+\infty`: some relaxed operator has infinite accessibility cost.

The third statement is stronger than saying that finite-dimensional witnesses can have arbitrarily bad ratios; completeness upgrades unbounded global distortion to actual failure of accessibility somewhere in the operator space.

### Pair-dependent crossnorm, not an automatic Grothendieck tensor norm

`\alpha_{X,K}` is a canonical norm for the declared dual pairing between `\mathcal L(X,K)` and `X\otimes K^*`, and it lies between `\varepsilon` and `\pi`. This finding does **not** claim that the assignment `(X,K^*)\mapsto\alpha_{X,K}` is a Grothendieck tensor norm under arbitrary operators on both tensor factors.

The second factor is tied specifically to the predual relation `K^*` and the admissible operator class `\mathcal L(X,K)`. Functoriality must be checked in whatever category an application declares rather than inferred from the word "tensor".

## Prior art and novelty assessment

The mechanisms are classical, and **no novelty is claimed** for tensor-product duality, trace duality, polar norms, the bounded inverse theorem, local reflexivity, operator-extension theory, or the relationship between tensor norms and operator ideals.

- Raymond A. Ryan, ***Introduction to Tensor Products of Banach Spaces***, Springer Monographs in Mathematics, Springer London (2002), DOI `10.1007/978-1-4471-3903-4`. Role: standard source for projective/injective tensor norms, projective duality, and trace-duality language connecting tensors with spaces of operators.
- Andreas Defant and Klaus Floret, ***Tensor Norms and Operator Ideals***, North-Holland Mathematics Studies 176, North-Holland (1993), ISBN `0-444-89091-2`. Role: standard systematic framework relating tensor norms, finite-dimensional structure, trace duality, and Banach operator ideals.
- Steven F. Bellenot, **“Local reflexivity of normed spaces, operators, and Fréchet spaces,”** *Journal of Functional Analysis* 59(1) (1984), 1--11, DOI `10.1016/0022-1236(84)90050-8`. Role: operator-level local-reflexivity prior art already used by AF-100 for bounded finite representability of bidual-valued behavior.
- Frank Oertel, **“Operators with extension property and the principle of local reflexivity,”** *Acta Universitatis Carolinae. Mathematica et Physica* 37(2) (1996), 55--63; arXiv:`math/9604220`. Role: established operator-ideal literature explicitly connecting extension properties, local reflexivity, tensor norms, and accessibility.
- Frank Oertel, **“The principle of local reflexivity for operator ideals and its implications,”** arXiv:`math/0101213` (2001). Role: survey of the operator-ideal local-reflexivity framework and its applications.

The term **accessibility** is overloaded here. Floret/Oertel accessibility is an established technical property of operator ideals. AF-100's `a_K` is a Mathia-defined bounded pointwise weak-star accessibility gauge for the specific inclusion `K\subset K^{**}`. The present theorem gives a trace-dual/polar reformulation of that gauge; it does not identify the two notions without an additional theorem establishing the corresponding operator-ideal dictionary.

The substantive result is therefore a structural reorganization of classical functional analysis: AF-100's operator-side bounded-accessibility condition has an exact finite tensor-side norm, an exact optimal distortion constant, and a completeness dichotomy. These formulas are treated as derived classification, not as a theorem-level novelty claim.

## Boundaries and failure modes

- The norm `\alpha_{X,K}` depends on the declared original target category `K` and admissible class `\mathcal L(X,K)`. Positivity-preserving, equivariant, order-compatible, completely bounded, arithmetic, local, or other constrained operator classes induce different pairing gauges.
- Equation (11) compares the full projective bidual relaxation with the full bounded `K`-valued operator class. Restricting the observable family changes both the polar norm and the resulting accessibility constant.
- `C_{\mathrm{acc}}<\infty` does not produce a canonical pointwise recovery map from `K^{**}` to `K`, nor one approximating sequence. It states norm equivalence of the finite-observation completions and bounded accessibility of each operator by the AF-100 net notion.
- `C_{\mathrm{acc}}>1` is quantitative distortion, not information loss in the zero-error sense: every relaxed operator remains accessible when the constant is finite.
- `C_{\mathrm{acc}}=+\infty` guarantees existence of at least one inaccessible operator but does not identify a concrete one. An explicit witness requires additional geometry.
- No approximation property, separability, reflexivity of `X`, or sequence-versus-net assumption is silently imposed.
- No rational-prime specificity, zeta-zero statement, or RH consequence follows.

## Consequences for Arithmetic Fidelity

AF-097--AF-100 progressively separated finite observation, uniform interpolation budget, bidual recovery, and target-valued accessibility. AF-101 puts that chain into one exact primal/dual object. The original category `K` equips finite observations with `\alpha_{X,K}`; the relaxed category `K^{**}` equips the same observations with `\pi`; and their distortion is exactly the worst accessibility overhead.

This gives a reusable audit pattern beyond Banach biduals. Whenever a proposed recovery argument enlarges the destination category, define the two finite-observation polar gauges induced by the original and relaxed admissible objects. If the gauges coincide, the enlargement adds no power at that layer. If they are uniformly equivalent, the enlargement changes conditioning but not qualitative accessibility. If no uniform equivalence exists and the corresponding dual spaces are complete, one should expect a genuinely inaccessible relaxed object rather than merely worsening finite constants.

For later arithmetic applications, this sharpens the warning from AF-100: a discriminator recovered only after passing to a completion, distributional space, bidual, spectral envelope, or other relaxed category is not yet an intrinsic recovery. The decisive question is whether the original and relaxed finite-observation gauges are equal or at least uniformly equivalent under the source-natural admissibility constraints.