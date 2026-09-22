# MC-468 — Root-scale support makes well-factorability vacuous

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-DEFINITION-CONSEQUENCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Abstract well-factorability cannot by itself force coefficient spreading on sufficiently small support. More precisely, fix an integer `k>=2` and a level `Q>=1`. Say that a sequence `lambda` is `k`-fold well-factorable of level `Q` when for every factorization

\[
Q=Q_1\cdots Q_k,
\qquad Q_i\ge1,
\]

there are `1`-bounded sequences `gamma_i`, supported on `n<=Q_i`, such that

\[
\lambda=\gamma_1*\cdots*\gamma_k.
\tag{1}
\]

Then every `1`-bounded arithmetic sequence supported on

\[
\boxed{n\le Q^{1/k}}
\tag{2}
\]

is automatically `k`-fold well-factorable of level `Q`.

Indeed, for every split `Q=Q_1\cdots Q_k`, at least one factor satisfies `Q_j>=Q^{1/k}`. Put

\[
\gamma_j=\lambda,
\qquad
\gamma_i=\delta_1\quad(i\ne j),
\tag{3}
\]

where `delta_1(1)=1` and `delta_1(n)=0` for `n>1`. All support and boundedness conditions hold, and `(1)` follows because `delta_1` is the identity for Dirichlet convolution.

Consequently:

- ordinary two-fold well-factorability of level `Q` is completely nonrestrictive on arbitrary `1`-bounded sequences supported on `n<=sqrt(Q)`;
- triply well-factorable structure is completely nonrestrictive on arbitrary `1`-bounded sequences supported on `n<=Q^(1/3)`.

This gives an exact **root-scale support-vacuity radius** for the bare factorability definition. In particular, no coefficient anti-concentration theorem on that range can follow from well-factorability alone. If `E` is any subset of `[1,Q^{1/k}]`, then

\[
\lambda_n=\mathbf 1_E(n)
\tag{4}
\]

is already `k`-fold well-factorable, so the class permits complete concentration on an arbitrary prescribed set `E` inside the root-scale range. More generally arbitrary phases or signs on `E` are allowed as long as the coefficients remain `1`-bounded.

This materially narrows the open coefficient-mass test after `MC-467`. The phrase “actual well-factorable coefficient mass” must not be replaced by a generic spreading consequence of the well-factorable class. In a chosen split `lambda=alpha*beta`, the definition already permits the individual bounded factors `alpha` and `beta` to be concentrated arbitrarily inside their allowed supports; and at the root scale the entire coefficient sequence itself may be arbitrary. Therefore a proof that the surviving small-`r'`/small-lcm cells of `MC-467` carry negligible mass must use additional structure of the **specific** upper-sieve coefficient/decomposition being used—such as its Rosser–Iwaniec construction, support geometry, normalization, cancellation, or another exact coefficient identity—not merely the label “well-factorable.”

This does **not** prove that the concrete upper-sieve weight has large mass in the surviving cells, nor that the `MC-467` small-`r'` threshold always lies below a root-scale boundary for the relevant sieve level. It proves a generic no-go: factorability as an abstract class property supplies no such anti-concentration theorem.

No estimate for the staged character kernel, no bound for `M(x)`, and no RH consequence follows.

## 1. The root-scale lemma is forced by the definition

Let `lambda` be `1`-bounded and supported on `(2)`. For an arbitrary factorization `Q=Q_1\cdots Q_k`, the geometric-mean inequality gives

\[
\max_i Q_i\ge (Q_1\cdots Q_k)^{1/k}=Q^{1/k}.
\tag{5}
\]

Choose `j` attaining the maximum. The support of `lambda` is then contained in `[1,Q_j]`. The factors in `(3)` are all `1`-bounded and have the required supports, since every `Q_i>=1` contains the support of `delta_1`. Finally,

\[
\delta_1*\lambda=\lambda,
\tag{6}
\]

and repeated convolution with `delta_1` changes nothing. This proves the claim for every admissible split, which is exactly the well-factorability requirement.

The argument is sharp as a statement about what can be deduced from support alone. Once the support extends beyond `Q^{1/k}`, there are balanced splittings with every `Q_i` below some support points, so the trivial identity-factor construction no longer certifies an arbitrary sequence. No converse is asserted: many sequences with larger support are still well-factorable because they possess genuine convolutional structure.

## 2. Anti-concentration cannot be a class consequence below the root scale

Take any set

\[
E\subseteq\{1,2,\ldots,\lfloor Q^{1/k}\rfloor\}
\tag{7}
\]

and any coefficients `c_n` with `|c_n|<=1` supported on `E`. By the root-scale lemma the sequence

\[
\lambda_n=c_n\mathbf 1_E(n)
\tag{8}
\]

is `k`-fold well-factorable. Hence the class contains, on this range, every possible bounded support pattern and every possible bounded sign/phase pattern.

For example, choosing `c_n=1` gives

\[
\sum_{n\in E}|\lambda_n|=|E|.
\tag{9}
\]

Thus a purported universal estimate saying that well-factorability forces a small fraction of coefficient mass onto an arbitrary family of root-scale cells cannot beat the trivial cardinality bound. Any genuine mass saving must use information not present in the abstract factorability axiom.

There is a second, simpler warning relevant to the staged branch. Even outside the vacuity range, a representation

\[
\lambda=\alpha*\beta,
\qquad
|\alpha_r|,|\beta_s|\le1,
\tag{10}
\]

only bounds the factors pointwise and locates their supports. It does not say that `alpha` or `beta` is equidistributed inside that support. Treating the factor variables as though well-factorability itself supplied a density law would therefore be an extra assumption.

## 3. Consequence for the `MC-467` frontier

`MC-467` leaves three quantitative costs: the total outer coefficient mass on the surviving small-outer-scale cells, the near-complete source-interval endpoint, and—if enough mass survives—the weighted residual amplitude inside those cells.

The first of these costs cannot be discharged abstractly by saying that a well-factorable weight must spread its coefficients over many factor cells. The present lemma shows why at the level of the total coefficient class, while `(10)` shows the same issue at the level of a chosen factorization: the bare definition has no built-in anti-concentration mechanism.

Therefore the next legitimate coefficient calculation must pin down a concrete coefficient family and a concrete admissible factorization, then estimate the mass of the `MC-467` surviving region from that extra structure. In particular, one must check the actual relation among the sieve level, the chosen factor supports, and the `r'`/lcm cutoff before invoking any root-scale simplification. If the concrete Rosser–Iwaniec or beta-sieve construction supplies a stronger distribution law, that would be new input beyond well-factorability and remains live.

This also clarifies the role of `MC-456`. The successful triply-well-factorable dispersion literature does not gain because “factorable coefficients are spread.” It gains because a proof keeps specific convolution factors in distinct analytic roles long enough to exploit nonseparable arithmetic structure. `MC-468` rules out a different shortcut: deriving the needed outer-cell mass saving from factorability as a generic coefficient-class regularity statement.

## 4. Prior art and novelty boundary

The definition used above is standard well-factorability. `MC-453` already audits the classical two-factor formulation and `MC-409` the Iwaniec/Maynard upper-sieve context; `MC-456` audits the modern triply-well-factorable setting. A fresh prior-art check on 22 September 2026 also confirmed the same bounded-convolution definitions in current sieve literature, including the modern linear-sieve and triply-well-factorable formulations.

The root-scale observation itself is an elementary one-line consequence of that definition: one factor in every `k`-fold split must reach the geometric mean, and all other factors may be the Dirichlet identity. No novelty claim is made for the lemma or for the terminology “support-vacuity radius.” The durable value here is its application as a **frontier obstruction**: it prevents the current staged Möbius branch from assigning anti-concentration power to the abstract well-factorability label that the definition simply does not contain.

## Boundaries and falsification tests

- **The root scale is only a sufficient vacuity range.** The finding does not classify all well-factorable sequences or say that structure begins immediately above `Q^{1/k}`.
- **Specific sieve coefficients can be much more rigid.** Rosser–Iwaniec/beta-sieve coefficients carry construction-specific support and sign information not encoded by the abstract definition; such information may still price the surviving cells.
- **The current outer variables must be matched to the correct level.** No claim is made that every `r'` allowed by `MC-467` lies below `sqrt(Q)` or `Q^(1/3)` for whichever coefficient level is used. That parameter identification is part of the next test.
- **Existence of a factorization is not uniqueness.** A concentration statement about one chosen `alpha,beta` representation cannot be inferred from another representation without proof.
- **No source cancellation is obtained.** The lemma concerns coefficient-class freedom only; it gives no character-sum, dispersion, or completion estimate.
- **No RH input or conclusion.** The derivation is finite Dirichlet-convolution algebra.