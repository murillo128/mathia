# AF-102 — Second-leg alpha functoriality is exactly bidual accessibility

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CATEGORY-EXPLICIT-FIDELITY`, `CLASSICAL-OPERATOR-IDEAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let `K` and `L` be Banach spaces. For a bounded operator

\[
C:L^*\longrightarrow K^*,
\tag{1}
\]

define its canonical transposed bidual realization

\[
\widetilde C
:=C^*J_K:K\longrightarrow L^{**},
\tag{2}
\]

so that

\[
\langle \widetilde Ck,\ell^*\rangle
=(C\ell^*)(k).
\tag{3}
\]

The correspondence `C -> \widetilde C` is an isometric linear bijection

\[
\mathcal L(L^*,K^*)
\cong
\mathcal L(K,L^{**}).
\tag{4}
\]

Retain AF-100/AF-101's bounded pointwise weak-star accessibility gauge `a_L` and define the extended second-leg cost

\[
\beta_{K,L}(C)
:=a_L(\widetilde C)
\in[0,+\infty].
\tag{5}
\]

Also retain AF-101's pair-dependent finite-observation norm

\[
\alpha_{X,K}\!\left(\sum_jx_j\otimes k_j^*\right)
=
\sup_{\substack{S\in\mathcal L(X,K)\\\|S\|\le1}}
\left|\sum_jk_j^*(Sx_j)\right|.
\tag{6}
\]

Then the following hold.

### 1. `beta` is the exact second-leg functoriality cost

For every Banach space `X`, the algebraic map

\[
I_X\otimes C:
X\otimes L^*
\longrightarrow
X\otimes K^*
\tag{7}
\]

satisfies

\[
\boxed{
\alpha_{X,K}((I_X\otimes C)u)
\le
\beta_{K,L}(C)\,\alpha_{X,L}(u).
}
\tag{8}
\]

Moreover the constant is sharp already at the single source `X=K`:

\[
\boxed{
\beta_{K,L}(C)
=
\|I_K\otimes C:
(K\otimes L^*,\alpha_{K,L})
\to
(K\otimes K^*,\alpha_{K,K})\|.
}
\tag{9}
\]

Consequently

\[
\boxed{
\beta_{K,L}(C)
=
\sup_X
\|I_X\otimes C\|_{\alpha_{X,L}\to\alpha_{X,K}},
}
\tag{10}
\]

where an unbounded algebraic map is assigned norm `+\infty`.

Thus the following are equivalent:

1. `\beta_{K,L}(C)<\infty`;
2. `I_K\otimes C` is bounded for the AF-101 norms;
3. `I_X\otimes C` is bounded for every Banach source `X`;
4. the maps `I_X\otimes C` extend boundedly to every completion
   \[
   E_{X,L}\longrightarrow E_{X,K}.
   \tag{11}
   \]

A possible second-factor morphism therefore does not require a separate test over all source spaces: the self-source `X=K` is already complete and gives the optimal universal cost.

### 2. Finite-beta maps form the maximal second-leg category for the alpha family

Define

\[
\mathsf{AF}(K,L)
:=
\{C\in\mathcal L(L^*,K^*):\beta_{K,L}(C)<\infty\}.
\tag{12}
\]

Then `\mathsf{AF}(K,L)` is a Banach space in the norm `\beta_{K,L}`. Identity maps satisfy

\[
\beta_{K,K}(I_{K^*})=1,
\tag{13}
\]

and composable maps

\[
C:L^*\to K^*,
\qquad
D:M^*\to L^*
\tag{14}
\]

obey

\[
\boxed{
\beta_{K,M}(C\circ D)
\le
\beta_{K,L}(C)\,\beta_{L,M}(D).
}
\tag{15}
\]

Hence Banach spaces become a normed category if an arrow `K -> L` is represented contravariantly by an element of `\mathsf{AF}(K,L)`.

This category is maximal for the declared requirement: if a class of dual-side maps is required to make `I_X\otimes C` bounded for every source `X`, every such `C` must lie in `\mathsf{AF}(K,L)`. Any proposed universal bound `N(C)` must satisfy

\[
N(C)\ge\beta_{K,L}(C).
\tag{16}
\]

The first tensor leg remains fully functorial. If `A:X_0\to X` is bounded and `C\in\mathsf{AF}(K,L)`, then

\[
\boxed{
\|A\otimes C\|_{\alpha_{X_0,L}\to\alpha_{X,K}}
\le
\|A\|\,\beta_{K,L}(C).
}
\tag{17}
\]

Thus AF-101's pair-dependent crossnorms acquire an exact category-explicit mapping property: arbitrary bounded maps are allowed on the source leg, while the admissible dual-side maps are precisely those whose transposed bidual realization is accessible in the original target category.

### 3. Ordinary target maps embed isometrically, but do not exhaust the category

Every bounded map

\[
B:K\to L
\tag{18}
\]

induces `C=B^*:L^*\to K^*`, and

\[
\widetilde{B^*}
=B^{**}J_K
=J_LB.
\tag{19}
\]

Therefore

\[
\boxed{
\beta_{K,L}(B^*)=\|B\|.
}
\tag{20}
\]

So ordinary target morphisms are always admitted isometrically.

The converse fails in general. If `L` is nonreflexive, choose

\[
z\in L^{**}\setminus J_L(L)
\tag{21}
\]

and let `K=\mathbb F`. Define

\[
C_z:L^*\to\mathbb F,
\qquad
C_z(\ell^*)=\langle z,\ell^*\rangle.
\tag{22}
\]

Then

\[
\widetilde C_z(\lambda)=\lambda z.
\tag{23}
\]

Since the source `\mathbb F` is finite-dimensional, AF-100's local-reflexivity control gives

\[
\boxed{
\beta_{\mathbb F,L}(C_z)=\|z\|=\|C_z\|.
}
\tag{24}
\]

But `C_z` cannot equal `B^*` for any `B:\mathbb F\to L`, because that would force `z=J_L(B1)`.

Hence weak-star continuity / existence of a genuine preadjoint is a sufficient but not necessary condition for AF second-leg functoriality. The admissible category is strictly larger whenever nonreflexive targets permit accessible bidual-valued behavior not represented by one fixed target-valued map.

### 4. AF-101's accessibility constant is exactly the distortion of this category

Because (4) is an isometric bijection, AF-101's universal accessibility constant satisfies

\[
\boxed{
C_{\mathrm{acc}}(K,L)
=
\sup_{0\ne C\in\mathcal L(L^*,K^*)}
\frac{\beta_{K,L}(C)}{\|C\|}.
}
\tag{25}
\]

Therefore:

- `C_acc(K,L)=1` exactly when every bounded dual-side map is admitted isometrically;
- `1<C_acc(K,L)<infinity` exactly when every bounded dual-side map is admitted with one uniform multiplicative distortion;
- `C_acc(K,L)=+infinity` exactly when some bounded dual-side map is not an AF morphism at all.

In particular, AF-101's original-versus-relaxed target distortion is not merely an operator-side recovery constant. It is precisely the obstruction to extending the pair-dependent `alpha` gauges to a full metric-mapping rule on arbitrary bounded maps of the second dual factor.

## Derivation

### 1. The transpose correspondence is isometric and onto

For `C:L^*\to K^*`, equation (3) gives

\[
\|\widetilde C\|
=
\sup_{\|k\|\le1,\|\ell^*\|\le1}
|(C\ell^*)(k)|
=
\|C\|.
\tag{26}
\]

Conversely, given `U:K\to L^{**}`, define

\[
(C_U\ell^*)(k)
:=
\langle Uk,\ell^*\rangle.
\tag{27}
\]

Then `C_U\in\mathcal L(L^*,K^*)`, `\|C_U\|=\|U\|`, and `C_U^*J_K=U`. This proves (4).

AF-101 identified the accessible operator space

\[
\mathcal A(K,L)
:=
\{U\in\mathcal L(K,L^{**}):a_L(U)<\infty\}
\tag{28}
\]

isometrically with the dual of the `alpha_{K,L}` completion. Hence (4) restricts to an isometric identification

\[
(\mathsf{AF}(K,L),\beta_{K,L})
\cong
(\mathcal A(K,L),a_L),
\tag{29}
\]

which proves completeness and the extended-norm assertions.

### 2. Accessibility is stable under precomposition

Let `U:X\to L^{**}` have `a_L(U)<\infty`, and let `A:X_0\to X`. If

\[
J_LS_i\longrightarrow U
\quad\text{pointwise weak-star},
\qquad
\|S_i\|\le C,
\tag{30}
\]

then

\[
J_L(S_iA)\longrightarrow UA
\quad\text{pointwise weak-star},
\qquad
\|S_iA\|\le C\|A\|.
\tag{31}
\]

Taking infima gives

\[
\boxed{
a_L(UA)\le a_L(U)\|A\|.
}
\tag{32}
\]

This elementary stability is the mechanism behind the universal source bound.

### 3. Upper bound for every source

Write

\[
u=\sum_jx_j\otimes\ell_j^*\in X\otimes L^*.
\tag{33}
\]

For `S:X\to K` with `\|S\|\le1`, equations (3) and (33) give

\[
\begin{aligned}
\sum_j(C\ell_j^*)(Sx_j)
&=
\sum_j\langle\widetilde C(Sx_j),\ell_j^*\rangle\\
&=
f_{\widetilde C S}(u).
\end{aligned}
\tag{34}
\]

By (32),

\[
a_L(\widetilde C S)
\le
\beta_{K,L}(C).
\tag{35}
\]

AF-101's dual formula therefore gives

\[
|f_{\widetilde C S}(u)|
\le
\beta_{K,L}(C)\alpha_{X,L}(u).
\tag{36}
\]

Taking the supremum over all such `S` proves (8).

### 4. The source `K` gives the matching lower bound

Set `X=K`. For every `u=\sum_jk_j\otimes\ell_j^*`, the definition of `alpha_{K,K}` allows the test operator `I_K`, so

\[
\begin{aligned}
\alpha_{K,K}((I_K\otimes C)u)
&\ge
\left|\sum_j(C\ell_j^*)(k_j)\right|\\
&=
|f_{\widetilde C}(u)|.
\end{aligned}
\tag{37}
\]

Divide by `alpha_{K,L}(u)` and take the supremum over nonzero algebraic tensors. AF-101's exact dual formula yields

\[
\|I_K\otimes C\|
\ge
\sup_{u\ne0}
\frac{|f_{\widetilde C}(u)|}{\alpha_{K,L}(u)}
=
a_L(\widetilde C)
=
\beta_{K,L}(C).
\tag{38}
\]

Together with (8), this proves (9)--(10) and all four boundedness equivalences.

### 5. Identities, composition, and the first leg

For the identity, `\widetilde{I_{K^*}}=J_K`, and AF-100 gives

\[
a_K(J_K)=1.
\tag{39}
\]

For composition, equations (9)--(10) and algebraic functoriality give, for every `X`,

\[
I_X\otimes(C\circ D)
=
(I_X\otimes C)(I_X\otimes D).
\tag{40}
\]

Thus

\[
\|I_X\otimes(C\circ D)\|
\le
\beta_{K,L}(C)\beta_{L,M}(D),
\tag{41}
\]

and taking the supremum over `X` proves (15).

Finally, for `A:X_0\to X`,

\[
\alpha_{X,K}((A\otimes I_{K^*})v)
\le
\|A\|\alpha_{X_0,K}(v),
\tag{42}
\]

because every unit-ball `S:X\to K` produces `SA:X_0\to K` of norm at most `\|A\|`. Combining (42) with (8) proves (17).

## Exact controls and counterexamples

### Finite-dimensional original source

If `K` is finite-dimensional, every `\widetilde C:K\to L^{**}` satisfies AF-100's exact local-reflexivity control

\[
a_L(\widetilde C)=\|\widetilde C\|.
\tag{43}
\]

Hence

\[
\boxed{
\beta_{K,L}(C)=\|C\|
\qquad
(\dim K<\infty).
}
\tag{44}
\]

This explains the non-preadjoint example (22)--(24): finite source data can be reproduced in the original target with no norm loss even when no single globally defined preadjoint exists.

### Reflexive original target

If `L` is reflexive, `L^{**}=J_L(L)`, so every `\widetilde C` is genuinely `L`-valued. Therefore

\[
\boxed{
\beta_{K,L}(C)=\|C\|
\qquad
(L\text{ reflexive}).
}
\tag{45}
\]

In this case every bounded `C:L^*\to K^*` is in fact the adjoint of the corresponding map `K\to L` supplied by (4).

### No extra source can expose more than `K` itself

Equation (9) is a strong control against false universalization. If a proposed obstruction to second-leg functoriality appears only after choosing a more elaborate source `X`, it must already be visible through `X=K`; otherwise it is not an obstruction for this `alpha` family.

Conversely, if `I_K\otimes C` is unbounded, no enlargement of the source family is needed to certify failure. The category boundary is exact at one canonical test object.

## Prior art and novelty assessment

The underlying machinery is classical Banach-space tensor duality and operator-ideal theory, and **no theorem-level novelty is claimed for those mechanisms**.

- Raymond A. Ryan, ***Introduction to Tensor Products of Banach Spaces***, Springer Monographs in Mathematics, Springer (2002), DOI `10.1007/978-1-4471-3903-4`. Role: standard tensor-product duality, projective/injective norms, and the metric mapping property that a genuine Grothendieck tensor norm must satisfy.
- Andreas Defant and Klaus Floret, ***Tensor Norms and Operator Ideals***, North-Holland Mathematics Studies 176, North-Holland (1993), ISBN `0-444-89091-2`. Role: systematic framework relating tensor norms, trace duality, operator ideals, accessibility, and functorial mapping properties.
- Frank Oertel, **“Operators with extension property and the principle of local reflexivity,”** *Acta Universitatis Carolinae. Mathematica et Physica* 37(2) (1996), 55--63; arXiv:`math/9604220`. Role: direct prior art connecting extension properties, local reflexivity, tensor norms, and accessibility of operator ideals.
- Frank Oertel, **“Local properties of accessible injective operator ideals,”** *Czechoslovak Mathematical Journal* 48(1) (1998), 119--133. Role: established accessibility/trace-duality/operator-ideal framework and explicit warning that good functorial behavior is a nontrivial structural property rather than automatic from a crossnorm formula.
- Sten Kaijser and Oleg Reinov, **“On alpha-nuclearity and total accessibility for some tensor norms alpha,”** *Acta et Commentationes Universitatis Tartuensis de Mathematica* 5 (2001), DOI `10.12697/ACUTM.2001.05.05`. Role: established technical notion of tensor-norm accessibility and examples showing that total accessibility can fail.

The word **accessibility** remains overloaded. `a_L` is AF-100's specific bounded pointwise weak-star accessibility gauge for the inclusion `L -> L**`; Oertel/Defant--Floret accessibility is an established technical property of tensor norms and operator ideals. This finding does not identify them as the same notion.

The Arithmetic Fidelity contribution is therefore a category-explicit reorganization of the AF-100/AF-101 object: for the particular pair-dependent norms `alpha_{X,K}`, the exact second-leg mapping class and its optimal cost are not left as an unspecified functoriality warning. They are identified internally as the dual maps whose transposed bidual operators have finite AF accessibility cost. This should be treated as a derived structural classification unless a stronger literature audit later shows that this precise construction already has a standard name.

## Boundaries and failure modes

- `\mathsf{AF}(K,L)` is not claimed to be a Pietsch operator ideal. Its arrows are dual-side maps `L^* -> K^*`, its geometry is tied to the pair-dependent `alpha` family, and identifying it with a standard ideal or ideal hull requires a separate theorem.
- Finite `beta` means uniform boundedness of all induced `alpha` tensor maps, not existence of a canonical preadjoint `K -> L` and not pointwise recovery by one fixed `L`-valued operator.
- The non-preadjoint example shows that imposing weak-star continuity would define a stricter category than the exact `alpha` mapping property requires.
- Equation (25) is pair-specific. It does not imply a universal bound independent of `K,L`.
- Positivity-preserving, completely bounded, equivariant, lattice, order, local, arithmetic, or other source-constrained morphisms require their own admissible operator class and their own polar gauge. The present category is maximal only for the unrestricted bounded-operator class used in AF-101.
- The classification concerns bounded linear maps between Banach-space representations. It does not by itself transfer to nonlinear, probabilistic, measurable, smooth, spectral, or arithmetic categories.
- No rational-prime discriminator, zeta-zero statement, or RH consequence follows.

## Consequences for Arithmetic Fidelity

AF-101 ended with a deliberate boundary: `alpha_{X,K}` is a canonical pair-dependent crossnorm but is not automatically a Grothendieck tensor norm because second-factor functoriality had not been classified. AF-102 closes exactly that gap.

The resulting audit rule is sharper than “check functoriality.” Given an intended transformation of retained dual observables `C:L^* -> K^*`, transpose it to the relaxed target map `\widetilde C:K -> L**` and compute its original-target accessibility cost. If `beta(C)=+infinity`, the transformation is incompatible with the original `alpha` representation before any later invariant is considered. If `beta(C)<infinity`, it acts on every source with the same optimal cost, and the source `K` alone certifies that cost.

This also clarifies what a future arithmetic application must derive from its source rather than choose after the fact. It is not enough to exhibit a mathematically legal transformation after enlarging the destination category. The transformation must lie in the **source-declared morphism class** induced by the original target representation, or the passage to the relaxed category has introduced genuine new expressive power. AF-102 supplies the exact linear Banach-space prototype of that category gate.