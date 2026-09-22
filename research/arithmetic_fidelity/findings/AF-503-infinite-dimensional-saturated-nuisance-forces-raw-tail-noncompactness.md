# AF-503 — Infinite-dimensional saturated nuisance forces raw tail noncompactness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `SATURATION`, `MEASURE-OF-NONCOMPACTNESS`, `FIBER-LOCALIZATION`, `DECISIVE-NEGATIVE`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-501 separates source saturation from compact lifting, and AF-502 shows that for a fixed family any noncompactness hidden by a quotient must localize inside arbitrarily thin quotient tubes once the quotient-visible tail is compact. There is a sharper obstruction when the nuisance equivalence is represented by a **fully saturated source**: if the nuisance fiber is infinite-dimensional, then every recurrent residual that enters the interior of a radius cutoff automatically carries an entire infinite-dimensional ball of nuisance-equivalent residuals. Raw tail compactness above the asymptotic separation threshold is then impossible.

Let `Y` be a Banach space, let `V subset Y` be a closed infinite-dimensional linear subspace, let

\[
\pi:Y\to Q:=Y/V
\]

be the quotient map, let `C subset Y` be nonempty, and put `D:=\overline C`. Assume the closed source is `V`-saturated,

\[
\boxed{D+V=D.}
\]

Fix `s in Y`. For `T>=0` define

\[
m_T:=\inf_{t\ge T}\operatorname{dist}_Y(ts,D),
\]

so that

\[
\lambda:=\lim_{T\to\infty}m_T
=\liminf_{t\to\infty}\operatorname{dist}_Y(ts,D).
\]

For the raw radius-truncated translated tail

\[
E^0_{T,R}(C,s)
:=
\bigcup_{t\ge T}
\bigl((D-ts)\cap\overline B_R^Y(0)\bigr),
\]

one has the finite-tail lower bound

\[
\boxed{
\chi_Y\bigl(E^0_{T,R}(C,s)\bigr)
\ge (R-m_T)_+.
}
\]

Consequently, whenever `lambda<infinity`,

\[
\boxed{
\nu_C^0(s;R)
\ge R-\lambda
\qquad(R>\lambda),
}
\]

where `nu_C^0` is the raw tail Hausdorff noncompactness profile of AF-499--AF-502.

The obstruction is already present inside every positive-width quotient tube. With the AF-502 tube profile

\[
\phi_{C,V}(s;R,\rho)
:=
\lim_{T\to\infty}
\sup_{q\in Q}
\chi_Y\!\left(
E^0_{T,R}(C,s)
\cap\pi^{-1}(B_Q(q,\rho))
\right),
\]

for every `rho>0` and every `R>lambda`,

\[
\boxed{
\phi_{C,V}(s;R,\rho)
\ge R-\lambda>0.
}
\]

Thus a fully saturated infinite-dimensional nuisance family can never satisfy the proposed “vanishing uniform near-fiber tail defect” above its finite asymptotic distance. The fiber itself forces a quantitative noncompactness floor.

Equivalently, under saturation and finite `lambda`,

\[
\boxed{
\nu_C^0(s;R)=0\text{ for some }R>\lambda
\quad\Longrightarrow\quad
\dim V<\infty.
}
\]

For this class of sources, AF-501's finite-dimensional compact-lifting gate is therefore not merely a universal sufficient condition over arbitrary bounded sets. It is necessary for **any individual saturated source** whose translated tail recurrently approaches to finite distance and is required to be raw-asymptotically compact at a radius strictly above that distance.

The practical consequence is a no-go for one tempting lift strategy. If an infinite-dimensional quotient is the correct nuisance reduction, one cannot recover an upstream compactness theorem by restoring the entire nuisance orbit. A viable lift must instead retain a compactly controlled transversal/marking, restrict the admissible nuisance representatives, or stay in the quotient. Full saturation and raw compactness are incompatible above threshold.

## Proof of the quantitative lower bound

Fix `T,R` with `m_T<R`. For every `epsilon>0` small enough that

\[
m_T+\varepsilon<R,
\]

there exist `t>=T` and `d in D` such that, with

\[
x:=d-ts,
\]

one has

\[
\|x\|_Y<m_T+\varepsilon<R.
\]

Set

\[
\delta:=R-\|x\|_Y>0.
\]

Because `D` is `V`-saturated, `d+v in D` for every `v in V`. Hence for every `v in V` with `\|v\|\le\delta`,

\[
(d+v)-ts=x+v\in D-ts
\]

and

\[
\|x+v\|
\le\|x\|+\|v\|
\le R.
\]

Therefore the raw tail contains a translated nuisance ball:

\[
\boxed{
x+\delta\overline B_V(0,1)
\subset E^0_{T,R}(C,s).}
\]

For an infinite-dimensional normed space, the Hausdorff measure of noncompactness of a closed ball of radius `delta` is exactly `delta`. Translation does not change the measure, and viewing the closed subspace `V` inside `Y` does not reduce this value. Thus

\[
\chi_Y(E^0_{T,R})
\ge\delta
>R-m_T-\varepsilon.
\]

Letting `epsilon downarrow 0` gives

\[
\chi_Y(E^0_{T,R})\ge R-m_T.
\]

If `m_T>=R`, the claimed bound is just nonnegativity. Hence for every `T,R`,

\[
\chi_Y(E^0_{T,R})\ge(R-m_T)_+.
\]

The functions `T mapsto m_T` increase to `lambda`, while the tail sets decrease with `T`. Passing to the tail limit therefore yields, for `R>lambda`,

\[
\nu_C^0(s;R)
=\lim_{T\to\infty}\chi_Y(E^0_{T,R})
\ge
\lim_{T\to\infty}(R-m_T)
=R-\lambda.
\]

No distance-attainment hypothesis is used: an arbitrarily good approximate residual already carries the required nuisance ball.

## The obstruction lives in an exact quotient fiber

The same witness proves more than raw noncompactness. For the point

\[
q:=\pi(x),
\]

all elements of the translated ball have exactly the same quotient image:

\[
\pi(x+v)=q
\qquad(v\in V).
\]

Hence for every `rho>0`,

\[
x+\delta\overline B_V(0,1)
\subset
E^0_{T,R}
\cap\pi^{-1}(B_Q(q,\rho)).
\]

The same Hausdorff-noncompactness estimate gives

\[
\sup_{q'\in Q}
\chi_Y\!\left(
E^0_{T,R}\cap\pi^{-1}(B_Q(q',\rho))
\right)
\ge(R-m_T)_+.
\]

Passing to `T->infinity` proves

\[
\phi_{C,V}(s;R,\rho)\ge R-\lambda
\qquad(R>\lambda,\ \rho>0).
\]

So AF-502's drifting-fiber pathology is not the only way a thin tube can remain noncompact. Under full saturation, noncompactness need not drift between nearby quotient labels at all: a single exact fiber already contains the whole obstruction.

This also sharpens the interpretation of AF-502. Its family-level replacement for the universal finite-dimensional gate is genuinely useful only when the admissible source does **not** restore an unrestricted infinite-dimensional nuisance ball around every relevant representative, or when compactness is evaluated solely after quotienting. Full source saturation is too strong for raw compactness lifting in infinite-dimensional nuisance directions.

## Relation to quotient distance and the critical radius

Because `D+V=D`, nuisance translation does not change the source set. Therefore

\[
\operatorname{dist}_Y(ts,D)
=\operatorname{dist}_Y(ts,D+V)
=\operatorname{dist}_Q(t\bar s,\pi(D)),
\]

with `\bar s=\pi(s)`. The `lambda` above is exactly the nuisance-relative asymptotic separation already studied in AF-500--AF-502.

The lower bound deliberately requires

\[
R>\lambda.
\]

At the exact critical radius `R=lambda`, it becomes zero and says nothing about whether contacts are attained, whether the critical-contact fiber is nonempty, or whether the critical tail is compact. Those are the separate attainment/contact questions isolated by AF-499 and AF-500. Infinite-dimensional saturation therefore kills compactness **strictly above** threshold without collapsing the distinct equality-case problem.

Likewise, if `lambda=infinity`, no bounded translated tail is forced and the theorem makes no compactness claim.

## Sharpness of the saturation hypothesis

The conclusion is specific to full nuisance saturation. If `D` is not `V`-saturated, an infinite-dimensional ambient nuisance space does not by itself force a ball inside the source residuals. A source may intersect each nuisance coset in a single point or in a compactly controlled set, and then quotient-visible compactness can lift for that particular family despite `dim V=infinity`.

This is precisely the distinction needed for a minimal lift. A lift that attaches the entire equivalence class recreates an infinite-dimensional ball and fails immediately; a lift that chooses a sufficiently regular transversal can preserve only the representatives needed to recover provenance. The theorem does not prove that such a transversal exists for a given arithmetic source. It identifies why **saturation itself cannot be the recovery mechanism** in the infinite-dimensional regime.

The radius lower bound is also sharp at the level of its forced fiber contribution. In the model

\[
Y=\mathbb R\oplus_2 V,
\qquad
D=\mathbb N\times V,
\qquad
s=(1,0),
\]

with infinite-dimensional `V`, one has `lambda=0`. At integer times, the raw radius-`R` tail contains `\{0\}\times\overline B_V(0,R)`, whose Hausdorff measure of noncompactness is exactly `R`. Hence the forced floor `R-lambda=R` is attained.

## Prior-art and novelty audit

No broad novelty is claimed for saturated quotient sets, infinite-dimensional noncompact balls, or Hausdorff measures of noncompactness.

- R. R. Akhmerov, M. I. Kamenskii, A. S. Potapov, A. E. Rodkina, and B. N. Sadovskii, *Measures of Noncompactness and Condensing Operators*, Operator Theory: Advances and Applications 55, Birkhauser (1992), DOI `10.1007/978-3-0348-5727-7`. Role: classical Hausdorff-measure-of-noncompactness machinery, including translation invariance, homogeneity, and the infinite-dimensional ball calculation used in the proof.
- Tomasz Zajac, **“The Concept of Measures of Noncompactness in Banach Spaces,”** *Symmetry* 17(8), 1248 (2025), DOI `10.3390/sym17081248`. Role: modern survey explicitly recording that in an infinite-dimensional Banach space the Hausdorff measure of noncompactness of a radius-`r` ball is `r`, while it vanishes in finite dimension.
- Robert E. Megginson, *An Introduction to Banach Space Theory*, Graduate Texts in Mathematics 183, Springer (1998), DOI `10.1007/978-1-4612-0603-3`. Role: standard closed-subspace and Banach-quotient background used for the nuisance interpretation.

The literature audit supports the ingredients as classical. The durable Arithmetic Fidelity result is the line-specific composition: **source saturation converts every interior translated residual into a full nuisance ball, so an infinite-dimensional nuisance direction imposes the exact lower floor `R-lambda` on both raw tail noncompactness and every positive-width quotient-tube profile.** This closes the proposed route of lifting quotient compactness through a fully saturated infinite-dimensional source by a uniform near-fiber compactness argument.

## Falsification and boundary audit

- The theorem uses the Hausdorff measure of noncompactness. The exact numerical lower bound for another compactness defect must be recomputed from that defect's value on infinite-dimensional balls.
- Saturation is required for the **closed source** `D=cl C`, matching the tail geometry used in AF-499--AF-502. Saturating only a sparse raw set `C` is not enough unless its closure is also saturated.
- Infinite dimensionality of `V` is essential. In finite dimension every bounded nuisance ball is relatively compact, and AF-501 shows that compact lifting can hold.
- The positive lower bound is forced only for radii strictly above finite `lambda`. The exact critical radius remains governed by the separate contact and distance-attainment gates.
- The theorem does not say that quotient-visible tails are noncompact. They may be perfectly compact while every raw lift is noncompact; the obstruction lies entirely in equivalence directions the quotient intentionally forgets.
- The result is a no-go for **full-saturation lifting**, not for quotient-based analysis or compactly controlled transversal lifts. Those remain the mathematically relevant alternatives.