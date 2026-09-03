# AF-099 — Uniform interpolation cost is the finite matrix-coefficient dual gauge

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `QUANTITATIVE-FIDELITY-REFINEMENT`, `CLASSICAL-DUALITY-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let `Z` be a closed linear subspace of a Banach space `X`, let `K` be a Banach space, and let

\[
R:\mathcal L(X,K)\to\mathcal L(Z,K),
\qquad R(S)=S|_Z.
\tag{1}
\]

For `T\in\mathcal L(Z,K)`, retain the finite interpolation cost from AF-098,

\[
e_E(T)
:=
\inf\{\|S\|:S\in\mathcal L(X,K),\ S|_E=T|_E\},
\tag{2}
\]

for finite-dimensional `E\subset Z`, and

\[
\lambda_{\rm fin}(T)
:=
\sup_{\substack{E\subset Z\\\dim E<\infty}}e_E(T).
\tag{3}
\]

Let `\mathcal M` denote the finite matrix-coefficient functionals on `\mathcal L(Z,K)`, namely

\[
\Phi(A)
=
\sum_{j=1}^m k_j^*(Az_j),
\qquad
z_j\in Z,
\quad k_j^*\in K^*.
\tag{4}
\]

Then the uniform finite interpolation cost has the exact dual formula

\[
\boxed{
\lambda_{\rm fin}(T)
=
\sup_{0\ne\Phi\in\mathcal M}
\frac{|\Phi(T)|}{\|\Phi\circ R\|}.
}
\tag{5}
\]

The denominator is nonzero for every nonzero `\Phi\in\mathcal M`: AF-097 proved that `\operatorname{ran}R` is strong-operator dense in `\mathcal L(Z,K)`, while every finite matrix coefficient is strong-operator continuous.

Equivalently, for `C\ge0` let

\[
D_C:=R\bigl(CB_{\mathcal L(X,K)}\bigr).
\tag{6}
\]

Then

\[
\boxed{
\lambda_{\rm fin}(T)
=
\inf\{C:T\in\overline{D_C}^{\,\mathrm{SOT}}\}
=
\inf\{C:T\in\overline{D_C}^{\,\mathrm{WOT}}\}.
}
\tag{7}
\]

Thus AF-097's qualitative density and AF-098's uniform-conditioning profile fit into one exact statement: the extendable range is unbudgetedly dense at every finite pointwise scale, but each fixed norm ball has a nontrivial convex closure whose Minkowski gauge is precisely `\lambda_{\rm fin}`.

Most importantly, every failed finite norm budget has a finite scalar certificate. If

\[
C<\lambda_{\rm fin}(T),
\tag{8}
\]

then there exist finitely many `z_1,\ldots,z_m\in Z` and `k_1^*,\ldots,k_m^*\in K^*` such that

\[
\boxed{
\left|
\sum_{j=1}^m k_j^*(Tz_j)
\right|
>
C\,
\sup_{\|S\|\le1}
\left|
\sum_{j=1}^m k_j^*(Sz_j)
\right|.
}
\tag{9}
\]

Consequently any `S:X\to K` agreeing with `T` on those finitely many points must satisfy `\|S\|>C`.

The reusable Arithmetic Fidelity boundary is therefore

\[
\boxed{
\text{finite values cannot witness unbudgeted nonextension, but every violated uniform budget is finitely dual-certifiable.}
}
\tag{10}
\]

This is stronger than merely knowing from AF-098 that some finite-dimensional interpolation cost exceeds `C`: the obstruction can always be compressed further to one scalar inequality built from finitely many source points and target dual functionals.

## Derivation

### 1. Each finite interpolation problem is a Banach quotient norm

Fix a finite-dimensional `E\subset Z` and define

\[
R_E:\mathcal L(X,K)\to\mathcal L(E,K),
\qquad R_E(S)=S|_E.
\tag{11}
\]

AF-097 gives exact finite-dimensional extension for every operator `A:E\to K`; hence `R_E` is surjective.

For `A\in\mathcal L(E,K)`, the quotient norm induced by `R_E` is

\[
q_E(A)
:=
\inf\{\|S\|:R_E(S)=A\}.
\tag{12}
\]

By definition,

\[
e_E(T)=q_E(T|_E).
\tag{13}
\]

Standard Banach-space quotient duality gives

\[
q_E(A)
=
\sup\left\{
|f(A)|:
 f\in\mathcal L(E,K)^*,
 \|R_E^*f\|\le1
\right\}.
\tag{14}
\]

Indeed, `q_E` is the norm transported from the Banach quotient

\[
\mathcal L(X,K)/\ker R_E,
\tag{15}
\]

and the dual of that quotient is isometrically the annihilator of `\ker R_E`; equation (14) is exactly the Hahn--Banach polar formula for this quotient norm.

### 2. Every dual functional on a finite source slice is a finite matrix coefficient

Choose a basis `e_1,\ldots,e_n` of `E`. The evaluation map

\[
\mathcal L(E,K)\to K^n,
\qquad
A\mapsto(Ae_1,\ldots,Ae_n)
\tag{16}
\]

is a Banach-space isomorphism. Therefore every

\[
f\in\mathcal L(E,K)^*
\tag{17}
\]

has the form

\[
f(A)
=
\sum_{i=1}^n k_i^*(Ae_i)
\tag{18}
\]

for suitable `k_i^*\in K^*`.

Viewed on `\mathcal L(Z,K)`, this is a functional `\Phi\in\mathcal M` supported on `E`. Moreover

\[
(R_E^*f)(S)
=f(S|_E)
=(\Phi\circ R)(S),
\tag{19}
\]

so

\[
\|R_E^*f\|=\|\Phi\circ R\|.
\tag{20}
\]

Substituting (18)--(20) into (14) gives

\[
e_E(T)
=
\sup_{\substack{\Phi\in\mathcal M\\\operatorname{supp}\Phi\subset E\\\|\Phi\circ R\|\le1}}
|\Phi(T)|.
\tag{21}
\]

Taking the supremum over all finite-dimensional `E\subset Z` exhausts exactly all finite matrix coefficients, so

\[
\lambda_{\rm fin}(T)
=
\sup_{\substack{\Phi\in\mathcal M\\\|\Phi\circ R\|\le1}}
|\Phi(T)|.
\tag{22}
\]

AF-097 showed

\[
\overline{\operatorname{ran}R}^{\,\mathrm{SOT}}
=
\mathcal L(Z,K).
\tag{23}
\]

If `\Phi\in\mathcal M` satisfies `\Phi\circ R=0`, then SOT continuity and (23) force `\Phi=0`. Thus every nonzero term in (22) has positive denominator and homogeneous rescaling yields (5).

### 3. The same quantity is the SOT/WOT gauge of norm-bounded extendable operators

Define

\[
\gamma(T)
:=
\inf\{C:T\in\overline{D_C}^{\,\mathrm{SOT}}\}.
\tag{24}
\]

First suppose `c=\lambda_{\rm fin}(T)` and choose `C>c`. A basic SOT neighborhood of `T` depends on finitely many vectors `z_1,\ldots,z_m\in Z`. Put

\[
E=\operatorname{span}\{z_1,\ldots,z_m\}.
\tag{25}
\]

Since `e_E(T)\le c<C`, there is `S:X\to K` with

\[
S|_E=T|_E,
\qquad
\|S\|<C.
\tag{26}
\]

Hence every SOT neighborhood meets `D_C`, so

\[
\gamma(T)\le c.
\tag{27}
\]

Conversely suppose

\[
T\in\overline{D_C}^{\,\mathrm{SOT}}.
\tag{28}
\]

Fix finite-dimensional `E\subset Z` with Auerbach basis `e_1,\ldots,e_n` and coordinate functionals `e_1^*,\ldots,e_n^*`. For arbitrary `\delta>0`, SOT closure supplies `S:X\to K` with `\|S\|\le C` and

\[
\|(T-S)e_i\|<\delta/n
\qquad(1\le i\le n).
\tag{29}
\]

Extend every `e_i^*` to `\widetilde e_i^*\in X^*` with norm one and set

\[
Qx
:=
\sum_{i=1}^n
\widetilde e_i^*(x)(T-S)e_i.
\tag{30}
\]

Then

\[
Q|_E=(T-S)|_E,
\qquad
\|Q\|<\delta.
\tag{31}
\]

Therefore `S+Q` agrees exactly with `T` on `E` and

\[
e_E(T)\le C+\delta.
\tag{32}
\]

Letting `\delta\downarrow0` gives `e_E(T)\le C`; taking the supremum over `E` gives

\[
\lambda_{\rm fin}(T)\le C.
\tag{33}
\]

Equations (27) and (33), with the infimum over `C`, prove the first equality in (7).

The sets `D_C` are convex. AF-097 records the classical fact that the SOT- and WOT-continuous linear duals of `\mathcal L(Z,K)` coincide and consist exactly of finite matrix coefficients. Hahn--Banach separation in locally convex spaces therefore gives

\[
\overline{D_C}^{\,\mathrm{SOT}}
=
\overline{D_C}^{\,\mathrm{WOT}},
\tag{34}
\]

which proves the second equality in (7).

### 4. Every failed budget has a finite scalar witness

If `C<\lambda_{\rm fin}(T)`, formula (5) gives a nonzero `\Phi\in\mathcal M` such that

\[
|\Phi(T)|>C\|\Phi\circ R\|.
\tag{35}
\]

Writing `\Phi` as in (4) gives exactly (9), because

\[
\|\Phi\circ R\|
=
\sup_{\|S\|\le1}
\left|
\sum_{j=1}^m k_j^*(Sz_j)
\right|.
\tag{36}
\]

If some `S:X\to K` agreed with `T` on all listed `z_j`, then

\[
|\Phi(T)|
=|\Phi(RS)|
\le
\|\Phi\circ R\|\,\|S\|.
\tag{37}
\]

Combining (35) and (37) forces `\|S\|>C`.

Thus the quantitative obstruction is not merely existential at a finite-dimensional subspace. It has a one-number certificate that can be checked from finitely many values of `T`, provided the admissible comparison class includes the global norm budget.

## Exact controls

### No-budget control recovers AF-097

Without the denominator/norm budget, no nonzero `\Phi\in\mathcal M` can separate `T` from the full extendable range: `\Phi\circ R=0` would imply `\Phi=0` by SOT density. Equation (5) therefore does not contradict AF-097. The witness works only because it compares the observed scalar against the maximum that a **unit-norm** global repair can produce.

### Scalar Hahn--Banach control

For `K=\mathbb R` or `\mathbb C`, Hahn--Banach gives

\[
\lambda_{\rm fin}(T)=\|T\|.
\tag{38}
\]

Formula (5) then reduces to an ordinary dual norm representation: there is no hidden extension penalty beyond the original operator norm.

### Dual/reflexive target control

If `K` is dual or reflexive, AF-098 gives

\[
\lambda_K(T)=\lambda_{\rm fin}(T),
\tag{39}
\]

where `\lambda_K(T)` is the least norm of a genuine global `K`-valued extension, with value `+\infty` when no extension exists. Hence in this category every strict lower bound

\[
C<\lambda_K(T)
\tag{40}
\]

has a finite matrix-coefficient certificate of the form (9). In particular, nonextension is equivalent to the existence of such certificates for arbitrarily large finite budgets.

### General target retains the AF-098 range gap

For arbitrary `K`, equation (5) computes `\lambda_{\rm fin}`, not `\lambda_K`. AF-098 showed only

\[
\lambda_{**}(T)
\le
\lambda_{\rm fin}(T)
\le
\lambda_K(T).
\tag{41}
\]

A finite witness for a failed `\lambda_{\rm fin}` budget therefore says nothing beyond that finite-uniform layer. If bidual coherence exists but target-valued recovery fails because `K` is not complemented in `K^{**}`, matrix-coefficient certificates need not detect that final range-retention defect.

### Noncanonical witness control

The theorem proves existence of a finite scalar certificate, but the separating vectors `z_j` and functionals `k_j^*` may depend on `T`, the threshold `C`, and the ambient operator geometry. Nothing here makes them canonical, computable, equivariant, positive, local, or arithmetically intrinsic.

For a later RH application, an after-the-fact Hahn--Banach certificate is therefore not yet an admissible arithmetic discriminator. The source category must independently explain why the relevant finite matrix coefficients or their generating family are available before the defect is known.

## Prior art and novelty assessment

The functional-analytic ingredients are classical, and **no novelty is claimed** for the quotient-norm duality, Hahn--Banach separation, strong/weak operator topologies, or finite matrix-coefficient description of their continuous dual.

- Nelson Dunford and Jacob T. Schwartz, ***Linear Operators. Part I: General Theory***, Interscience Publishers, New York (1958), Theorem VI.1.4. Role: classical operator-topology source used already in AF-097 for the equality of SOT/WOT continuous linear duals and their finite matrix-coefficient form.
- John B. Conway, ***A Course in Functional Analysis***, 2nd ed., Graduate Texts in Mathematics 96, Springer, New York (1990; later Springer eBook), DOI `10.1007/978-1-4757-4383-8`. Role: standard Banach-space and locally-convex duality background for quotient norms, annihilators, Hahn--Banach, and weak-topology separation.
- H. H. Schaefer and M. P. Wolff, ***Topological Vector Spaces***, 2nd ed., Graduate Texts in Mathematics 3, Springer, New York (1999), DOI `10.1007/978-1-4612-1468-7`. Role: authoritative locally convex treatment of Hahn--Banach and separation of convex sets, supplying the general closure/polar mechanism behind (34).

A targeted literature audit found these statements inside standard functional-analysis/operator-topology machinery rather than as a distinct new extension theorem. The durable Arithmetic Fidelity result is their exact organization at the AF-097/AF-098 boundary: the same finite matrix coefficients that are powerless for qualitative unbudgeted separation become complete dual witnesses for the quantitative uniform-repair gauge once a norm budget is part of the retained structure.

## Boundaries and failure modes

- The theorem concerns bounded linear extension and the ordinary operator norm. It does not automatically transfer to nonlinear Lipschitz extension, positivity-preserving maps, order structure, operator ideals, equivariant maps, completely bounded norms, or arithmetic admissibility classes; each changes the convex comparison set and possibly its dual witnesses.
- Formula (5) is an existence theorem. It does not provide an efficient algorithm for finding the maximizing or near-maximizing finite matrix coefficient.
- The supremum in (5) need not be attained. A strict failed budget `C<\lambda_{\rm fin}(T)` always has a witness, but there need not be one canonical extremal witness at the exact threshold.
- Finite scalar certification does not mean the underlying property is determined by finitely many values without auxiliary structure. The certificate explicitly contains the global norm calibration `\|\Phi\circ R\|`, which depends on the entire ambient extension class.
- The SOT/WOT closure equality is used only for the convex sets `D_C`. SOT and WOT remain different topologies, and arbitrary nonconvex observation classes need not have the same closures.
- No rational-prime specificity or RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-097 established a sharp qualitative impossibility: finite point evaluations cannot distinguish an arbitrary operator from the extendable range at all. AF-098 then identified uniform finite interpolation cost as the first quantitative structure that survives that collapse and, for dual/reflexive targets, exactly recovers global extension cost.

AF-099 closes the dual side of that refinement. Once a uniform budget is declared, **no additional infinite-dimensional separating functional is required to certify its failure**: finite matrix coefficients already form a complete polar family for the budgeted extendable set. The information missing from AF-097 was therefore not an exotic new observable but the scale against which finite observations are calibrated.

This produces a useful two-gate audit for future compression mechanisms. First ask whether the candidate observables distinguish the unbudgeted fiber at all. If not, ask whether the source supplies a canonical coercivity or norm budget. Only after such a budget is independently justified does finite dual separation become meaningful. For arithmetic applications, the next unresolved issue is not whether an abstract finite witness exists, but whether the relevant calibration and witness family arise intrinsically from the arithmetic source rather than being chosen after the compression defect has already been identified.