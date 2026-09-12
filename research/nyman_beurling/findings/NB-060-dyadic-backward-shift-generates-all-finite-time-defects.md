# NB-060 — dyadic backward shift generates all finite-time defects

**Status:** `EXACT-DERIVED + DYADIC-COFINALITY + GENERALIZED-KERNEL + FIXED-WINDOW-DICHOTOMY + TARGET-TAIL-CRITERION + FLAT-CONTROL + METHOD-REDUCTION`.

`NB-058` identifies the collective late quotient with the orthogonal complement of the finite-time arithmetic defect sectors

\[
\mathcal K_R
=
\mathcal D\cap\ker U_{\log R}^*,
\qquad
\mathcal D=\mathcal A^\perp,
\tag{1}
\]

for integer `R>=2`. The open question was left as an apparently scale-dependent family: determine whether these sectors are trivial, and if not whether their union can approximate the canonical residual. The present finding collapses that entire family to **one fixed backward shift at the first dyadic scale**.

Put

\[
B_2:=U_{\log 2}^*\big|_{\mathcal D}.
\tag{2}
\]

Integer-log invariance of the natural Nyman space, proved in `NB-053` and used in `NB-058`, makes `D` invariant under `U_(log 2)^*`, so `B_2` is a well-defined contraction on `D`. Then for every integer `k>=1`,

\[
\boxed{
\mathcal K_{2^k}=\ker B_2^k.
}
\tag{3}
\]

Since the dyadic cutoffs are cofinal among all finite integer cutoffs,

\[
\boxed{
\mathcal K_{\rm fin}
=
\overline{\bigcup_{R\ge2}\mathcal K_R}
=
\overline{\bigcup_{k\ge1}\ker B_2^k}.
}
\tag{4}
\]

Thus the finite-time defect space is exactly the closed generalized nullspace of one operator. In particular,

\[
\boxed{
\mathcal K_2=\{0\}
\iff
\mathcal K_R=\{0\}\ \text{for every finite }R
\iff
\mathcal K_{\rm fin}=\{0\}.
}
\tag{5}
\]

Equivalently, **if any nonzero compact-time arithmetic defect exists at any finite scale, then one already exists with Paley--Wiener support inside `[0,log 2]`**. This removes the moving-cutoff existence question entirely. What remains scale-dependent is not existence but whether iterated preimages of that first-window defect space are rich enough to approximate the canonical target residual.

## 1. The compressed integer-log shifts form a multiplicative semigroup

Retain the notation of `NB-058`:

\[
\mathcal A=
\overline{\operatorname{span}}\{F_{\log n}:n\ge2\},
\qquad
Q=I-P_{\mathcal A},
\qquad
\mathcal D=\mathcal A^\perp,
\tag{6}
\]

and for every integer `R>=2`,

\[
V_R:=Q U_{\log R}\big|_{\mathcal D}.
\tag{7}
\]

Because `U_(log R) A subseteq A`,

\[
Q U_{\log R}P_{\mathcal A}=0.
\tag{8}
\]

Hence for integers `R,S>=2` and `x in D`,

\[
\begin{aligned}
V_RV_Sx
&=Q U_{\log R}Q U_{\log S}x\\
&=Q U_{\log R}U_{\log S}x\\
&=V_{RS}x.
\end{aligned}
\tag{9}
\]

The compressed shifts therefore preserve the multiplicative semigroup exactly:

\[
\boxed{V_RV_S=V_{RS}=V_SV_R.}
\tag{10}
\]

`NB-058` also gives

\[
V_R^*=U_{\log R}^*\big|_{\mathcal D},
\qquad
\mathcal T_R=\overline{\operatorname{Ran}V_R},
\qquad
\mathcal K_R=\ker V_R^*.
\tag{11}
\]

Taking `R=2` and iterating (10),

\[
V_{2^k}=V_2^k,
\qquad
V_{2^k}^*=(V_2^*)^k=B_2^k,
\tag{12}
\]

which proves (3). No boundedness or inverse property of the arithmetic multiplier `O` is used.

## 2. Dyadic cofinality turns every finite-time sector into a generalized kernel

The spaces `K_R` increase with `R`, because under Paley--Wiener they are precisely

\[
\mathcal K_R
=
\{h\in\mathcal D:
\operatorname{supp}(\mathcal P^{-1}h)\subseteq[0,\log R]\}.
\tag{13}
\]

Given any integer `R>=2`, choose `k` with `R<=2^k`. Then

\[
\mathcal K_R\subseteq\mathcal K_{2^k}=\ker B_2^k.
\tag{14}
\]

Conversely every dyadic cutoff is one of the integer cutoffs. Taking unions and closures gives (4).

There is also a direct support proof of the strongest existence statement. Suppose `0!=h in K_R`. Since `h` has finite Paley--Wiener support, sufficiently many applications of the backward translation `B_2` annihilate it. Choose the last nonzero iterate:

\[
0\ne g=B_2^j h,
\qquad
B_2g=0.
\tag{15}
\]

Backward-shift invariance keeps every iterate in `D`, so

\[
0\ne g\in\ker B_2=\mathcal K_2.
\tag{16}
\]

Thus any localized defect at any finite scale has a nonzero descendant in the first dyadic window. Conversely `K_2 subseteq K_R` for every integer `R>=2`, so a first-window defect persists as a nontrivial finite-time sector at all larger cutoffs.

Equation (5) also follows operator-theoretically. If `K_2=ker B_2={0}`, then `B_2` is injective, every power `B_2^k` is injective, every dyadic `K_(2^k)` vanishes, and (14) forces every `K_R` to vanish.

## 3. The collective tail is the stable range of one operator

The same dyadic cofinality applies to the decreasing late-tail spaces. From (11)--(12),

\[
\boxed{
\mathcal T_{2^k}
=
\overline{\operatorname{Ran}V_2^k}.
}
\tag{17}
\]

Since the dyadic cutoffs are cofinal,

\[
\boxed{
\mathcal T_\infty
:=
\bigcap_{R\ge2}\mathcal T_R
=
\bigcap_{k\ge1}\overline{\operatorname{Ran}V_2^k}
=
\mathcal D\ominus
\overline{\bigcup_{k\ge1}\ker B_2^k}.
}
\tag{18}
\]

For the canonical residual `h_*=Qe`, `NB-058` therefore becomes the one-operator criterion

\[
\boxed{
\lim_{R\to\infty}
\|P_{\mathcal T_R}h_*\|^2
=
\operatorname{dist}\!\left(
 h_*,
 \overline{\bigcup_{k\ge1}\ker B_2^k}
\right)^2.
}
\tag{19}
\]

Thus collective late-tail target gain tends to zero exactly when `h_*` belongs to the closed generalized nullspace of `B_2`. Full density of that generalized nullspace in `D` would be stronger than necessary; the canonical problem asks only for membership of one distinguished vector.

There is a sharp negative branch. If

\[
\mathcal K_2=\{0\},
\tag{20}
\]

then (5) gives `K_R={0}` for every `R`, hence by `NB-058`

\[
\boxed{
\mathcal T_R=\mathcal D
\quad\text{and}\quad
\|P_{\mathcal T_R}h_*\|=\|h_*\|
\qquad(R\ge2).
}
\tag{21}
\]

In that case the collective late quotient retains the **entire** arithmetic defect at every finite cutoff, even though `NB-053`--`NB-057` force every individual sufficiently late shifted block to become nearly invisible to the canonical residual. The individual-versus-collective distinction is therefore exact, not a conditioning heuristic.

If instead `K_2!=0`, this does **not** prove (19) tends to zero. A nonzero first-window kernel is only the seed. The remaining question is whether its generalized root tower

\[
\ker B_2\subseteq\ker B_2^2\subseteq\cdots
\tag{22}
\]

is large enough to approximate `h_*`.

## 4. The unit-outer model realizes the dense generalized-kernel branch

For the `O=1` calibration of `NB-056`--`NB-058`, the defect space is the orthogonal direct sum of logarithmic-cell detail spaces. The first sector is

\[
\mathcal K_2^{(0)}
=
L^2([0,\log2])
\ominus
\operatorname{span}\{e^{t/2}\mathbf1_{[0,\log2]}\},
\tag{23}
\]

which is already nonzero. More generally,

\[
\ker (B_2^{(0)})^k
=
\mathcal K_{2^k}^{(0)}
=
\bigoplus_{j<2^k}
\left(
L^2(I_j)
\ominus
\operatorname{span}\{e^{t/2}\mathbf1_{I_j}\}
\right).
\tag{24}
\]

The dyadic generalized kernels therefore exhaust the entire flat defect space:

\[
\overline{\bigcup_{k\ge1}
\ker (B_2^{(0)})^k}
=
\mathcal D^{(0)}.
\tag{25}
\]

Equation (19) then forces the collective tail to vanish for every flat defect target. For the canonical target it recovers the explicit `NB-056`/`NB-058` law along the dyadic subsequence,

\[
\|P_{\mathcal T_{2^k}^{(0)}}Q_0e\|^2
=
\frac{1}{36\,2^{3k}}+O(2^{-4k}).
\tag{26}
\]

This calibration is useful because it separates two issues cleanly. The semigroup/root-space reduction is universal once integer-log invariance is present; the arithmetic difficulty is entirely whether the actual deflated Nyman defect space has the same generalized-kernel abundance.

## 5. Consequence for the live adjoint-dual route

The accepted `CLUE-early-cell-adjoint-duals-certify-target-tail` asks whether one can construct nonzero compact-time arithmetic defects and use them to approximate the canonical residual. `NB-058` reduced this to the family `K_R`. The present finding shows that the **existence** half of that question is fixed-scale:

\[
\exists R<\infty:\mathcal K_R\ne\{0\}
\quad\Longleftrightarrow\quad
\mathcal K_2\ne\{0\}.
\tag{27}
\]

So there is no need to search for a first defect at a growing or specially tuned cutoff. Either an arithmetic defect already fits inside `[0,log2]`, or no compact-time defect exists anywhere. The quantitative target problem is then the separate root-space question (19).

This also avoids the representation error that invalidated the withdrawn `NB-059`: no local-Dirichlet theorem is transported from one disk boundary point to another, and no regularity class is inferred from compact support by an unproved conjugacy. The argument uses only the exact half-plane semigroup invariance and Paley--Wiener support identity already established in `NB-053` and `NB-058`.

A practical next theorem is consequently much smaller than the previous moving-window formulation. One may first decide the fixed question

\[
\boxed{
\mathcal A^\perp\cap
L^2([0,\log2])
\stackrel{?}{=}\{0\}
}
\tag{28}
\]

under the `NB-058` Paley--Wiener identification. A proof of triviality kills the finite-time adjoint-certificate route globally by (21). A nonzero construction supplies a genuine arithmetic seed, after which the relevant problem is the generalized-kernel approximation of `h_*`, not existence at larger scales.

## 6. Prior-art boundary

The operator-theoretic notions used here are classical. For a bounded operator `B`, the increasing family `ker B^k` and its closed union are the generalized nullspace/root space at zero; the literature on generalized backward shifts commonly singles out density of `union ker B^k` as a defining structural property. Likewise, cofinal subsequences of an increasing family and `(closure Ran V)^perp=ker V^*` are standard Hilbert-space facts. No novelty is claimed for those general principles.

The Nyman--Beurling literature already anchored in `SOURCES.md` supplies the arithmetic Hardy space, the discrete dilation family, and orthogonal-complement/shift-invariance context. In particular Calderaro--Manzur--Noor--Santos study the size of the relevant Hardy orthogonal complement using shift/operator methods. A targeted search did not locate the specific Blaschke-deflated reduction (3)--(5), in which **all finite Paley--Wiener support sectors of the natural arithmetic defect collapse to the generalized kernel of the single `log 2` backward translation**, nor the exact consequence (21) for the complete late quotient. This finding makes no priority claim.

No new specialized external theorem is load-bearing: (3)--(28) follow from the exact semigroup and support identities already persisted in `NB-053` and `NB-058`. `SOURCES.md` therefore remains unchanged.

The durable line-local delta is the fixed-scale dichotomy. The finite-time defect route no longer has an existence problem at arbitrarily many cutoffs: **one first-window kernel decides whether compact-time arithmetic defects exist at all**, while the canonical tail-decay problem becomes membership of `h_*` in the generalized nullspace generated by iterating that one backward shift.