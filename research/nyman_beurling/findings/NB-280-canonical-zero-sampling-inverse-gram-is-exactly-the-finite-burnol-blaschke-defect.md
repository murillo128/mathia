# NB-280 — Canonical zero-sampling inverse Gram is exactly the finite Burnol Blaschke defect

**Status:** `EXACT-DERIVED + INTERNAL-COLLISION + PRIOR-ART-CLASSICALIZATION + NB-279-QUANTITY-EVALUATED + BURNOL-BLASCHKE-IDENTITY + HIGH-ZERO-ROUTE-CLOSURE`.

`NB-279` reduces every finite contour repair based on the legal Nyman residual

\[
r_P(s)=\frac1s-\mathcal N[P](s)
\]

to the Hardy interpolation constraints

\[
r_P(\rho_j)=\frac1{\rho_j}
\]

at right-half zeta zeros. For distinct points `\rho_1,\ldots,\rho_n` in `\Re s>1/2`, it identifies the exact least-norm sampling cost as

\[
\mathcal E(Z)
:=v^*G^{-1}v,
\qquad
G_{jk}=\frac1{\rho_j+\overline{\rho_k}-1},
\qquad
v_j=\frac1{\rho_j}.
\tag{1}
\]

The open interpretation in `NB-279` was that the size of `(1)` might depend on delicate inverse-Gram conditioning of the Ford-scale zero geometry. For the **canonical data vector** `v_j=1/\rho_j`, it does not. There is an exact identity

\[
\boxed{
\mathcal E(Z)
=
1-|B_Z(1)|^2
=
1-
\prod_{j=1}^n
\left|\frac{1-\rho_j}{\rho_j}\right|^2
=
1-
\prod_{j=1}^n
\left(
1-
\frac{2\Re\rho_j-1}{|\rho_j|^2}
\right),
}
\tag{2}
\]

where `B_Z` is the finite half-plane Blaschke product with zeros `Z`.

Thus the inverse-Gram quantity introduced in `NB-279` is exactly the finite **Burnol target defect** `\tau(Z)` already used in `NB-114`--`NB-116`. Pairwise spacing, Cauchy-Gram condition number, and Ford phase alignment do not provide an additional coercive degree of freedom for this particular target vector. The matrix may become arbitrarily ill-conditioned while `(2)` remains determined only by the one-point Blaschke factors.

This collision closes the point-evaluation version of the boundary route at high ordinate. `NB-116` already proves for every finite packet `Z` of actual right-half zeta zeros with `|\Im\rho|\ge G` that

\[
\tau(Z)\ll \frac1G.
\tag{3}
\]

Combining `(2)` and `(3)` gives

\[
\boxed{
v^*G^{-1}v\ll \frac1G.
}
\tag{4}
\]

Hence no actual high-zero Ford packet can make the `NB-279` point-sampling certificate order one, regardless of its rank, ordinate spread, clustering, or Gram conditioning. The remaining source-native frontier must use information not equivalent to this finite point-evaluation projection: for example a genuinely finite arithmetic-section interaction, higher jets at a multiple zero, or a different nonlinear/boundary mechanism. Merely proving better conditioning of the sampling matrix cannot rescue `(1)`.

## 1. The data vector is the sample vector of one Hardy kernel

Work in

\[
\mathcal H^2=H^2(\Re s>1/2)
\]

with the normalization used in `NB-279`. Its reproducing kernel at `w` is

\[
k_w(s)=\frac1{s+\overline w-1}.
\tag{5}
\]

In particular,

\[
k_1(s)=\frac1s,
\qquad
\|k_1\|^2=1.
\tag{6}
\]

Let

\[
K_Z:=\operatorname{span}\{k_{\rho_1},\ldots,k_{\rho_n}\}.
\tag{7}
\]

The sampling vector in `NB-279` is not arbitrary:

\[
v_j
=\frac1{\rho_j}
=k_1(\rho_j)
=\langle k_1,k_{\rho_j}\rangle.
\tag{8}
\]

Therefore the least-norm function satisfying the interpolation conditions `f(\rho_j)=v_j` is exactly the orthogonal projection of `k_1` onto `K_Z`. The standard Gram calculation gives

\[
\boxed{
v^*G^{-1}v
=
\|P_{K_Z}k_1\|^2.
}
\tag{9}
\]

Equation `(9)` is the crucial specialization missing from the conditioning interpretation of `NB-279`. For a generic prescribed vector `v`, inverse conditioning is genuinely independent information. Here `v` moves with the nodes because it is itself the trace of a fixed Hardy kernel.

## 2. The kernel span is a finite model space

Let

\[
B_Z(s)=\prod_{j=1}^n b_{\rho_j}(s)
\tag{10}
\]

be any unimodular normalization of the finite half-plane Blaschke product, with

\[
|b_\rho(s)|
=
\left|\frac{s-\rho}{s+\overline\rho-1}\right|.
\tag{11}
\]

For distinct simple nodes, the finite model space

\[
\mathcal K_{B_Z}
:=
\mathcal H^2\ominus B_Z\mathcal H^2
\tag{12}
\]

has dimension `n` and is exactly the span in `(7)`. The model-space reproducing kernel is

\[
k_w^{B_Z}(s)
=
\frac{1-\overline{B_Z(w)}B_Z(s)}
{s+\overline w-1}.
\tag{13}
\]

Since `k_w^{B_Z}=P_{\mathcal K_{B_Z}}k_w`, evaluating its norm at `w=1` gives

\[
\|P_{K_Z}k_1\|^2
=
k_1^{B_Z}(1)
=1-|B_Z(1)|^2.
\tag{14}
\]

Combining `(9)` and `(14)` proves the first equality in `(2)`.

This is classical Hardy/model-space geometry. Burnol's 1999 Nyman note, already anchored in `SOURCES.md` and used in `NB-052`, identifies the corresponding full Nyman projection through the same Blaschke value at `1`. No novelty is claimed for `(13)`--`(14)` or for the abstract Blaschke projection mechanism. The line-local result is the identification of the apparently new `NB-279` inverse-Gram currency with the already-audited finite Burnol defect.

## 3. The Cauchy inverse disappears from the canonical quadratic form

At `s=1`, one Blaschke factor satisfies

\[
|b_\rho(1)|^2
=
\frac{|1-\rho|^2}{|\rho|^2}.
\tag{15}
\]

Writing `\rho=\beta+i\gamma`,

\[
|\rho|^2-|1-\rho|^2
=
\beta^2+\gamma^2-
\bigl((1-\beta)^2+\gamma^2\bigr)
=2\beta-1.
\tag{16}
\]

Hence

\[
|b_\rho(1)|^2
=
1-
\frac{2\beta-1}{|\rho|^2}.
\tag{17}
\]

Multiplying `(17)` over `Z` and inserting it into `(14)` proves the complete product formula `(2)`.

Define

\[
\delta_\rho
:=
\frac{2\Re\rho-1}{|\rho|^2},
\qquad
S_Z:=\sum_{\rho\in Z}\delta_\rho.
\tag{18}
\]

Then the elementary bounds already used in `NB-114` and `NB-116` become directly a statement about the inverse Gram:

\[
1-e^{-S_Z}
\le
v^*G^{-1}v
\le
S_Z.
\tag{19}
\]

Whenever `S_Z=o(1)`,

\[
\boxed{
v^*G^{-1}v
=S_Z+O(S_Z^2).
}
\tag{20}
\]

So the canonical zero-sampling cost is a weighted one-point mass, not a hidden pair-correlation statistic. Relative ordinate geometry can make the matrix `G` nearly singular, but the simultaneous motion of `v` cancels that instability in the quadratic form `(1)`.

## 4. The matched Ford packet of NB-231 is sampling-invisible

The distinction between the source-side Ford obstruction and the target-side sampling cost is especially sharp on the matched control of `NB-231`.

There the packet has

\[
M\sim\delta J_0,
\qquad
J_0=\frac RH,
\qquad
J_0\le \log\log |t|,
\tag{21}
\]

up to the harmless logarithmic conventions of that finding, with points

\[
\rho_j
=1-\frac DR+i\gamma_j,
\qquad
\gamma_j
=t+\frac{2\pi qj}{X},
\tag{22}
\]

and

\[
D=\frac{\log J_0+O(1)}Y.
\tag{23}
\]

The exact Ford residue of this packet stays bounded away from zero because the moving-shell phases align and the damping `e^{-YD}` is balanced by `M\asymp J_0`.

For the Hardy sampling quantity, however,

\[
2\Re\rho_j-1
=1-\frac{2D}{R}
=1+o(1),
\tag{24}
\]

while `|\rho_j|^2=t^2(1+o(1))` uniformly over the packet. Thus

\[
\delta_{\rho_j}
=\frac{1+o(1)}{t^2},
\qquad
S_Z
=\frac{M}{t^2}(1+o(1)).
\tag{25}
\]

Since `M=O(\log\log|t|)`, equation `(20)` gives

\[
\boxed{
v^*G^{-1}v
\sim
\frac{M}{t^2}
\asymp
\frac{J_0}{t^2}
\longrightarrow0.
}
\tag{26}
\]

Thus the same compatible packet can carry an order-one **Ford residue** and a vanishing **Hardy point-sampling energy**. This is stronger than saying that the packet might be poorly conditioned: its conditioning is simply not the relevant variable for the canonical data vector.

As throughout `NB-225`--`NB-231`, this packet is a matched compatibility control, not a claim about the actual zeta zero set.

## 5. Actual high zeros are already ruled out by NB-116

For actual right-half zeta zeros, `NB-116` proves from Selberg zero density that

\[
\sum_{\substack{\zeta(\rho)=0\\\Re\rho>1/2\\|\Im\rho|\ge G}}
\frac{2\Re\rho-1}{|\rho|^2}
\ll \frac1G.
\tag{27}
\]

It then concludes for every finite packet `Z` in that tail that the finite Burnol target defect obeys

\[
\tau(Z)
=1-|B_Z(1)|^2
\ll \frac1G.
\tag{28}
\]

Equation `(2)` shows that `\tau(Z)` is **exactly** the `NB-279` inverse-Gram quantity. Therefore `(28)` is precisely `(4)`.

This is an internal collision rather than a new zero-density theorem. `NB-279` had isolated a quantity that looked like a new Ford-scale conditioning problem, but `NB-114` had already identified the same finite target mass and `NB-116` had already proved its uniform inverse-height decay for every actual high-zero packet. The earlier results were expressed in Blaschke/model-space coordinates, while `NB-279` arrived at the same object through contour duality and a Cauchy sampling Gram.

The collision is useful because it eliminates a false frontier: no theorem improving pairwise separation, local spacing, or Cauchy-Gram condition number can make the canonical point-value certificate in `(1)` order one at high height. The exact product formula has already integrated out that geometry.

## 6. Adversarial checks and boundaries

### 6.1 Ill-conditioning is real but irrelevant only for this data vector

Take two distinct points approaching one another. Their kernel Gram becomes arbitrarily ill-conditioned. Equation `(2)` nevertheless remains stable because `v_j=k_1(\rho_j)` coalesces at the matching rate. In the confluent limit the second nearby interpolation condition tends toward derivative information for the same analytic target. There is no contradiction with the large condition number.

For a generic externally prescribed vector `v`, no product collapse like `(2)` is available. The conclusion is specific to the canonical Nyman target data `1/\rho_j`.

### 6.2 Point multiplicity and zero multiplicity are different

`NB-279` forms `G` from **distinct zero locations**. Repeating the same point does not add an independent point-evaluation constraint, so `(2)` uses each distinct node once. If a zeta zero has multiplicity greater than one, the Nyman synthesized part has corresponding higher-order vanishing and one may impose derivative-jet constraints. The correct model space then uses the Blaschke factor with multiplicity, and derivative reproducing kernels enter.

Nothing here claims that the point-value channel alone exhausts those higher jets. For the simple-zero matched Ford controls used in this line, `(2)` is exact as stated. For actual zeros with possible multiplicity, the distinct-point point-value quantity is bounded above by the multiplicity-counted Burnol tail controlled in `NB-116`, so `(4)` remains valid for the channel under audit.

### 6.3 Critical-line zeros are not interior sampling nodes

The derivation assumes `\Re\rho>1/2`. At `\Re\rho=1/2`, point evaluation lies on the Hardy boundary and is not a bounded functional. Formula `(2)` is not being extended to critical-line zeros by continuity as an interpolation theorem.

The vanishing factor `2\Re\rho-1` is instead consistent with the fact that the Burnol inner obstruction records zeros strictly to the right of the Hardy boundary.

### 6.4 This closes one boundary mechanism, not the Nyman problem

The result kills the proposal that the contour route of `NB-279` might become coercive through favorable inverse conditioning of its finite point-evaluation Gram. It does not show that every possible finite boundary identity, nonlinear transform, higher-jet channel, or finite arithmetic-section interaction reduces to `(1)`.

In particular, `NB-114` already identified the possible escape correctly: any high-zero mechanism with order-one target access must exploit a finite arithmetic section/window in a way absent from the continuum Burnol projection, or move to a genuinely different representation.

## 7. Prior-art and representation audit

The finite model-space identity behind `(2)` is classical. Burnol's *A note on Nyman's equivalent formulation of the Riemann Hypothesis* proves the corresponding full Blaschke projection formula and product at `s=1`; it is already a durable source in `SOURCES.md` and load-bearing in `NB-052`. The generic model-space kernel formula used in `(13)` is standard Hardy-space theory.

`NB-114` already derives the finite product

\[
\tau(Z)=1-\prod_{\rho\in Z}(1-\delta_\rho)
\]

for arbitrary high zero packets, and `NB-116` already combines that product with Selberg density to obtain the `O(1/G)` actual-zeta tail. No novelty is claimed for those ingredients.

The substantive line-local outcome is the **identification of the `NB-279` Cauchy inverse-Gram expression with that pre-existing Burnol quantity**. This corrects the representation-level interpretation of the live frontier: the canonical vector `v=(1/\rho_j)` is not a generic inverse-Gram direction, so Ford-scale kernel conditioning is not a new arithmetic currency here.

No new durable external dependency is introduced, so `SOURCES.md` does not change.

## Conclusion

The finite boundary repair of `NB-279` is even more rigid than its zero-sampling formulation suggested. For the canonical Nyman target values,

\[
\boxed{
v^*G^{-1}v
=
1-|B_Z(1)|^2.
}
\]

The apparent inverse-Gram conditioning problem is exactly the finite Burnol/Blaschke target defect already analyzed earlier in the line. Consequently the matched Ford packets that remain dangerous source-side are target-poor in this channel, and every packet of actual right-half zeros above height `G` has sampling energy `O(1/G)` by `NB-116`.

The next non-circular source-native step must therefore leave this finite point-evaluation span rather than try to condition it better.