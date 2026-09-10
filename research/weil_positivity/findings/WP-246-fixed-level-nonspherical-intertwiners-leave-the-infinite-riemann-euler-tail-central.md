# WP-246 — Fixed-level non-spherical intertwiners leave the infinite Riemann Euler tail central

**Status:** `LITERATURE+EXACT-DERIVED + FIXED-LEVEL-NONSPHERICAL-CONTROL + RESTRICTED-TENSOR-PRODUCT + ALMOST-EVERYWHERE-SPHERICAL + SCALAR-GLOBAL-L-NORMALIZER + FINITE-RAMIFICATION-OPERATOR-BOUNDARY + UNITARY-GENERATOR-HERMITIAN-NOT-POSITIVE + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-244` closes the spherical higher-rank escape from the Maaß--Selberg/scattering line but deliberately leaves a more serious possibility open: use non-spherical or vector-valued inducing data, where the normalized global intertwining operator can be genuinely operator-valued, and hope that the Riemann arithmetic remains inside that noncentral operator until an independent unitary/positive theorem can act on it.

At **fixed finite level**, the first half of that hope fails for a structural reason. Flath's restricted-tensor-product theorem makes every irreducible automorphic inducing representation unramified at almost every finite place. On the standard fixed-level sector, the vector is therefore the distinguished spherical vector at every prime outside one finite set `S`. The normalized local intertwiner acts trivially on that one-dimensional spherical line, while the global automorphic `L`-functions occur as **scalar normalizing factors** of the global intertwiner. Consequently the infinitely many unramified Euler factors -- in particular the cofinite Riemann Euler tail whenever the target scalar contains `zeta` -- remain central. Genuinely noncentral arithmetic can survive at the archimedean place and at the finitely many ramified/non-spherical primes in `S`, but it cannot turn the all-prime Riemann Euler product into an operator coefficient at fixed level.

There is a second, independent failure. On the unitary axis the normalized intertwiner is unitary under the standard hypotheses, so its logarithmic generator is Hermitian. Unitarity alone does **not** make that generator positive: an arbitrary unitary curve `exp(itA)` has generator `A` with unrestricted Hermitian inertia. This must be distinguished from `WP-171`, where positivity of boundary delay follows from the much stronger hypothesis that the unitary boundary family is the boundary value of an analytic **Schur-contracting** function. Standard normalized-intertwiner unitarity by itself supplies no such positive cone.

Thus fixed-level non-sphericalization does not supply the missing bridge. It can add real operator geometry, but the global Riemann Euler tail remains in the scalar normalizer and the inherited unitary theorem gives self-adjointness rather than sign. This does **not** close full non-spherical Maaß--Selberg theory: a source-defined truncation/boundary form may still couple the scalar normalizer to noncentral local/archimedean operators before scalarization; an infinite-level/profinite limit may activate genuinely non-spherical data at unboundedly many primes; or an additional global operator may couple distinct automorphic sectors. Those are category changes and require separate tests.

## 1. Fixed-level automorphic data are spherical at almost every finite place

Let `M` be the Levi subgroup supplying the inducing data and let

\[
\pi \simeq \bigotimes_v' \pi_v
\tag{1}
\]

be an irreducible automorphic representation of `M(A_Q)`. Flath's tensor-product theorem gives precisely this restricted-product factorization, with `pi_p` unramified for all but finitely many finite primes.

Fix a standard finite level

\[
K_f=\prod_p K_p
\tag{2}
\]

with `K_p` hyperspecial maximal compact outside a finite set of level primes. Enlarge a finite set `S` so that it contains every finite place where the group/model, the representation, the level, or the chosen `K_f`-finite tensor data are ramified or non-spherical. Then for every `p notin S` the relevant local fixed space is the distinguished spherical line

\[
\dim \pi_p^{K_p}=1,
\qquad
\pi_p^{K_p}=\mathbb C f^0_p.
\tag{3}
\]

A fixed algebraic restricted-tensor vector is equal to `f^0_p` at all but finitely many places, and a fixed finite-level `K_f`-invariant sector has no additional local channel outside `S`. This is the exact point at which the proposed non-spherical escape meets the global automorphic architecture: **non-spherical finite-place support is finite at fixed level**.

The claim is intentionally about the fixed-level sector. The Hilbert completion of the automorphic representation can of course contain infinite superpositions, and one can vary the level through a family. Neither operation changes (3) for one fixed finite-level vector/sector; an infinite-level limit is treated separately below as a genuine category change.

## 2. Global `L`-arithmetic is a scalar normalizer before the normalized operator acts

For a standard global intertwining operator associated with a Weyl element `w`, write on a regular spectral region

\[
M(w,\lambda)=r(w,\pi,\lambda)\,R(w,\pi,\lambda),
\tag{4}
\]

where `r` is the scalar global normalizing factor and `R` is the normalized intertwining operator. Conventions sometimes place the reciprocal scalar on the other side; nothing below depends on that choice.

In the Langlands--Shahidi framework, Kim makes explicit the automorphic `L`-functions occurring as the normalizing factors `r` of the global intertwiners in Eisenstein constant terms. Schematically,

\[
r(w,\pi,\lambda)
=
\prod_j
\frac{L(a_j(\lambda),\pi,r_j)}{L(1+a_j(\lambda),\pi,r_j)}
\times \text{epsilon/conductor factors},
\tag{5}
\]

with the precise shifts and representations `r_j` determined by the root data. The structural fact needed here is only that (5) is **scalar on the representation fiber**.

The normalized operator factors locally,

\[
R(w,\pi,\lambda)
=\bigotimes_v' R_v(w,\pi_v,\lambda).
\tag{6}
\]

At every unramified `p notin S`, standard spherical normalization fixes the normalized spherical vector up to the canonical target identification,

\[
R_p(w,\pi_p,\lambda)f^0_{p,\lambda}
=f^0_{p,w\lambda}.
\tag{7}
\]

Hence on the fixed-level restricted-tensor sector the operator part has the schematic form

\[
R(w,\pi,\lambda)
=
R_S(w,\pi,\lambda)
\otimes I_{S^c,\mathrm{sph}},
\tag{8}
\]

where `R_S` includes the archimedean component and the finitely many exceptional finite places. Equation (8) does not assert that `R_S` is scalar; it may be genuinely matrix/operator-valued. It says that the cofinite set of unramified primes contributes no independent noncentral channel after standard normalization.

## 3. The cofinite Riemann Euler tail therefore cannot become a noncentral operator coefficient

Factor the scalar normalizer into the exceptional finite set and its complement,

\[
r(w,\pi,\lambda)
=r_S(w,\pi,\lambda)\,r^{S}(w,\pi,\lambda).
\tag{9}
\]

The factor `r^S` is built from the Euler factors at every `p notin S`. If a proposed Riemann channel is chosen so that one of the global `L`-factors in (5) contains the Riemann zeta function, then after deleting the finitely many exceptional Euler factors its cofinite part is still

\[
\zeta^S(s)
=
\prod_{p\notin S}(1-p^{-s})^{-1},
\tag{10}
\]

possibly with the standard shifted/ratio form dictated by the intertwining normalization. By (4) and (8), this entire infinite product multiplies the identity on the operator fiber.

This gives a sharp finite-versus-global separation. Changing a local `K`-type at a ramified prime, changing the level at finitely many primes, or using a nontrivial archimedean `K`-type can alter `R_S` and the finitely many local factors in `r_S`. It cannot move the infinitely many factors in (10) into a noncentral matrix at fixed level. If instead the inducing representation is globally nontrivial at almost every unramified place through its Satake parameters, the resulting scalar normalizer carries a different automorphic `L`-function; the local operator still acts on the one-dimensional spherical line outside `S`. One has changed the scalar arithmetic, not converted it into an operator-valued Riemann channel.

This also blocks a common apparent escape. Packaging several scalar `L`-normalizers into a matrix by changing basis, or coupling finitely many ramified `K`-types, can make the displayed scattering matrix dense. Returning to the restricted-product decomposition shows that the cofinite Euler tail is still central. Density of coordinates is not invariant noncentral arithmetic.

## 4. The logarithmic derivative splits exactly into central arithmetic plus normalized operator motion

Differentiate (4) along any real spectral parameter `t` on which both factors are regular. Since `r` is scalar,

\[
M^{-1}\dot M
=
\frac{\dot r}{r}I+R^{-1}\dot R.
\tag{11}
\]

The first term contains the logarithmic derivatives of the scalar global `L`-normalizers, hence the Euler, Gamma, conductor and polar data that later participate in explicit-formula decompositions. The second term records motion of the normalized operator.

Equation (11) is the non-spherical analogue of the centrality identity in `WP-238`, but the conclusion here is stronger in one specific direction left open by `WP-244`: allowing non-spherical fixed-level data does not transfer the **cofinite** Euler tail from the first term to the second. The operator term can contain ramified finite-place and archimedean structure, but the all-prime Riemann content remains scalar before the explicit formula is formed.

Therefore any projection or positive readout acting only on `R^{-1}\dot R` cannot by itself be the global Riemann Weil functional. To recover the zeta tail it must also use `dot r/r`; once that scalar is reintroduced, zeros, primes, Gamma and polar terms are again tied together in the same global normalizer unless a new source-defined coupling acts before the scalarization described by (4).

## 5. Normalized-intertwiner unitarity gives Hermiticity, not positivity

On the regular unitary axis, normalized intertwining operators satisfy the standard unitary relation. Write simply

\[
R(t)^*R(t)=I.
\tag{12}
\]

Then

\[
Q_R(t):=-iR(t)^*\dot R(t)
\tag{13}
\]

is Hermitian, because differentiating (12) gives

\[
\dot R^*R+R^*\dot R=0.
\tag{14}
\]

But there is no sign conclusion. The matched abstract control is the unitary curve

\[
U_A(t)=e^{itA}
\tag{15}
\]

for an arbitrary bounded Hermitian matrix `A`. It satisfies the same unitary identity, while

\[
-iU_A(t)^*\dot U_A(t)=A,
\tag{16}
\]

whose inertia can be positive, negative, or mixed. Thus **unitarity alone cannot be the independent positivity theorem required by the line mandate**.

This does not contradict `WP-171`. There the boundary-delay matrix is positive because the unitary boundary values come from an analytic matrix **Schur contraction** in a half-plane; the positive de Branges--Rovnyak kernel supplies the missing order structure. A normalized automorphic intertwiner being unitary on the unitary axis does not, by that fact alone, establish the Schur/passive hypothesis. Any attempt to invoke `WP-171` must first prove the requisite contractive analytic realization for the same global operator and then survive the Gamma/sign obstructions already recorded there.

Likewise, this section does not claim that a particular automorphic `Q_R` is indefinite. The decisive negative is one of logical sufficiency: the standard unitary theorem supplies self-adjointness but no nonnegative cone from which Weil positivity could follow.

## 6. Matched controls: finite exceptional support versus an infinite-level category change

Let `S_1 subset S_2` be two finite exceptional sets. Enlarging the level or choosing additional non-spherical local data can enlarge the operator block

\[
R_{S_1}\longrightarrow R_{S_2},
\tag{17}
\]

and can move finitely many Euler factors between `r^S` and `r_S`. But for every finite `S_2`, the complement still contains infinitely many primes and

\[
\zeta^{S_2}(s)
=
\prod_{p\notin S_2}(1-p^{-s})^{-1}
\tag{18}
\]

remains a scalar tail. No finite stage converts the Riemann product into a genuinely noncentral operator coefficient.

To evade this conclusion by making infinitely many prime places non-spherical one must leave the fixed finite-level category. A profinite/infinite-level completion could in principle carry an infinite restricted collection of local channel spaces, but then the candidate must newly prove all of the properties that fixed-level automorphic theory supplied for free: a well-defined Hilbert/form domain, convergence or renormalization independent of the target zero data, a canonical global coupling, and an independent sign theorem. Merely taking `S` to infinity after seeing which Euler factors are desired is not such a construction.

A second control is direct sums of automorphic sectors. If

\[
\mathcal H=\bigoplus_a \mathcal H_{\pi_a},
\tag{19}
\]

then the standard normalized scattering and Parseval structures preserve the sector decomposition unless an additional source-defined operator mixes it. The scalar normalizer in each block remains scalar. This is the same boundary exposed concretely for congruence Eisenstein oldclasses in `WP-243`: a dense basis change is not a new coupling.

## 7. Prior-art and novelty audit

The representation-theoretic ingredients are classical.

- D. Flath, *Decomposition of representations into tensor products*, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1 (1979), 179--183, DOI `10.1090/pspum/033.1/546596`, is the standard tensor-product theorem behind (1)--(3): irreducible admissible adelic representations decompose as restricted tensor products and are unramified at almost all finite places.
- Henry H. Kim, *On Local L-Functions and Normalized Intertwining Operators*, Canadian Journal of Mathematics 57 (2005), 535--597, DOI `10.4153/CJM-2005-023-x`, explicitly identifies the Langlands--Shahidi `L`-functions that occur as scalar normalizing factors of global intertwining operators and studies the corresponding normalized local operators.
- C. David Keys and Freydoon Shahidi, *Artin L-functions and normalization of intertwining operators*, Annales scientifiques de l'École Normale Supérieure (4) 21 (1988), 67--89, DOI `10.24033/asens.1551`, is a classical local normalization/L-factor anchor and guards against treating the scalar-factor/normalized-operator separation as a Mathia discovery.

A bounded literature audit around `Weil positivity`, `Maaß--Selberg`, fixed-level non-spherical Eisenstein series, restricted tensor products, Langlands--Shahidi normalization, and normalized intertwining found the standard theory above and the already-audited trace/Weil programs, but no source in the checked set where **fixed-level non-sphericalization itself** moves the cofinite Riemann Euler product into a noncentral normalized operator and then obtains the full Weil sign from ordinary intertwiner unitarity. This absence is not a completeness claim.

The substantive content of `WP-246` is therefore a line-specific obstruction synthesis, not a new theorem in automorphic representation theory. It closes exactly the fixed-level version of the non-spherical escape left open by `WP-244`: the operator-valued part can be real and nontrivial, but almost-everywhere sphericality keeps the infinite Euler tail scalar, and unitary normalization supplies no independent sign.

## 8. Research consequence

The candidate chain

\[
\text{fixed-level non-spherical inducing data}
\to
\text{noncentral all-prime Riemann arithmetic}
\to
\text{unitary/positive Weil form}
\tag{20}
\]

fails at both arrows in its direct form. The first fails because the cofinite unramified Euler product remains in the scalar global normalizer; the second fails because normalized-intertwiner unitarity yields only a Hermitian logarithmic generator.

The Maaß--Selberg/scattering line nevertheless remains live in narrower categories. A viable continuation must now exhibit at least one genuinely additional mechanism: a source-defined global truncation/boundary form that couples the scalar `L`-normalizer to noncentral local or archimedean operators **before** taking the sign; an infinite-level/profinite construction with a canonical well-posed positive limit and non-spherical support at unboundedly many primes; an intrinsic operator coupling distinct primitive/global automorphic sectors before scalarization; or a higher-rank boundary/truncation identity that combines the rootwise scalar normalizers and has its own sign theorem. `WP-246` supplies no such construction and proves no case of RH.