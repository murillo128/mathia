# AF-499 — Vanishing tail noncompactness restores norm-fiber fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TRANSLATION-LIMIT`, `MEASURE-OF-NONCOMPACTNESS`, `MINIMAX-RESOLUTION`, `MINIMAL-LIFT`, `INFINITE-DIMENSION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-496–AF-498 show that finite-dimensionality cannot simply be dropped from the AF-494/AF-495 norm-fiber laws: in every infinite-dimensional normed space there are exact nuisance difference sets whose bounded critical residuals disperse without a norm-convergent subsequence. The constructive replacement is not ambient finite dimensionality. It is **asymptotic compactness of the task-visible translated residuals**, and that condition can be measured directly by a tail measure of noncompactness.

Let `Y` be a Banach space, let `C subset Y` be nonempty, put `D=cl C`, and fix `s in Y`. For `R>=0` and `T>=0`, define the radius-truncated tail residual set

\[
E_{T,R}(C,s)
:=
\bigcup_{t\ge T}
\bigl((D-ts)\cap \overline B_R(0)\bigr).
\]

Let `chi` denote the Hausdorff measure of noncompactness,

\[
\chi(E)
:=
\inf\{\varepsilon>0:E\text{ has a finite }\varepsilon\text{-net in }Y\},
\]

with `chi(emptyset)=0`, and define the **tail noncompactness profile**

\[
\boxed{
\nu_C(s;R)
:=
\lim_{T\to\infty}\chi(E_{T,R}(C,s)).
}
\]

The limit exists because the tail sets decrease with `T`.

Then:

1. `nu_C(s;R)=0` if and only if every sequence `t_n->infinity` and `d_n in D` satisfying

\[
\|d_n-t_ns\|\le R
\]

has a subsequence for which the residuals `d_n-t_ns` converge in norm.

2. If

\[
\lambda_C(s)
:=
\liminf_{t\to\infty}\operatorname{dist}(ts,C)
<\infty
\]

and `nu_C(s;R)=0` for some `R>lambda_C(s)`, then the AF-494 translation-fiber law extends verbatim to this family in arbitrary Banach dimension:

\[
\boxed{
\lambda_C(s)
=
\min_{a\in\mathcal A_C(s)}\|a\|
=
\operatorname{dist}(0,\mathcal A_C(s)).
}
\]

If `lambda_C(s)=infinity`, then `mathcal A_C(s)=emptyset` and the same identity holds with the usual `+infinity` convention without any compactness assumption.

3. Define the **actual-contact profile** at radius `r` by

\[
\widehat\Delta_C(r;s)
:=
\sup\{t\ge0:(D-ts)\cap\overline B_r(0)\ne\varnothing\}.
\]

If `nu_C(s;r)=0`, then the AF-495 task-truncated contact fiber satisfies

\[
\boxed{
\widehat\Delta_C(r;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
}
\]

4. The original AF-495 distance-defined profile

\[
\Delta_C(r/2;s)
=
\sup\{t\ge0:\operatorname{dist}(ts,C)\le r\}
\]

contains a second, logically independent issue: distance need not be attained by a general closed subset of an infinite-dimensional Banach space. Always

\[
\widehat\Delta_C(r;s)\le\Delta_C(r/2;s),
\]

and equality holds whenever `D` is proximinal along the discriminator ray at radius `r`; in particular it holds if `D` is globally proximinal. Under this attainment condition plus `nu_C(s;r)=0`, the exact AF-495 equivalence is restored:

\[
\boxed{
\Delta_C(r/2;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
}
\]

Thus finite-dimensionality in AF-494/AF-495 was supplying two resources at once: **tail norm compactness** and, for the equality/contact statement, **distance attainment**. Both can be replaced by family-level conditions that are strictly weaker than finite-dimensional ambient geometry.

## Tail noncompactness is exactly raywise asymptotic compactness

Fix `R>=0`. The sets `E_{T,R}` are bounded and decrease as `T` increases, so `chi(E_{T,R})` is monotone nonincreasing and `nu_C(s;R)` is well-defined.

Assume first

\[
\nu_C(s;R)=0.
\]

Take arbitrary `t_n->infinity` and `d_n in D` with

\[
x_n:=d_n-t_ns\in\overline B_R(0).
\]

For each integer `k>=1`, choose `T_k` so large that `E_{T_k,R}` has a finite `2^{-k}`-net. The tail of `(x_n)` eventually lies in `E_{T_k,R}`. Passing successively to infinite subsequences, at stage `k` choose one ball of that finite net containing infinitely many remaining terms. A diagonal subsequence is Cauchy because its sufficiently late terms lie in one ball of arbitrarily small radius. Completeness of `Y` gives a norm-convergent subsequence.

Conversely, suppose `nu_C(s;R)>0`. Choose `epsilon>0` strictly below this limit. For every sufficiently large `T`, the set `E_{T,R}` has no finite `epsilon`-net. Recursively choose `T_n->infinity` and

\[
x_n\in E_{T_n,R}
\]

outside the union of the `epsilon`-balls centered at the previously chosen points. Each `x_n` is some residual

\[
x_n=d_n-t_ns,
\qquad t_n\ge T_n,
\qquad d_n\in D,
\qquad \|x_n\|\le R,
\]

and the sequence is `epsilon`-separated. It has no norm-convergent subsequence. Hence the sequential compactness property fails.

Therefore

\[
\boxed{
\nu_C(s;R)=0
\iff
\text{all radius-}R\text{ residual sequences escaping along }s\text{ are norm-precompact.}
}
\]

This is a task-local version of classical asymptotic compactness: compactness is required only for translated aliases that remain inside the declared observation/noise scale, not for the entire nuisance family or the ambient space.

## Recovery of the AF-494 threshold

Assume `lambda:=lambda_C(s)<infinity` and choose `R>lambda` with `nu_C(s;R)=0`.

By the definition of `liminf`, choose `t_n->infinity` such that

\[
\operatorname{dist}(t_ns,C)\to\lambda.
\]

Choose approximate minimizers `c_n in C` with

\[
\|c_n-t_ns\|
\le
\operatorname{dist}(t_ns,C)+\frac1n.
\]

Their norms converge to `lambda`, so eventually the residuals lie in `E_{T,R}` at the relevant tail scale. Vanishing tail noncompactness gives a subsequence

\[
c_{n_j}-t_{n_j}s\to a
\]

in norm. Hence `a in mathcal A_C(s)` and continuity of the norm gives

\[
\|a\|=\lambda.
\]

For every `a in mathcal A_C(s)`, the defining witnesses always imply

\[
\lambda_C(s)\le\|a\|.
\]

Therefore the lower bound is attained and

\[
\lambda_C(s)
=
\min_{a\in\mathcal A_C(s)}\|a\|.
\]

If `lambda_C(s)=infinity`, any bounded translated cluster would contradict the infinite liminf, so `mathcal A_C(s)=emptyset` automatically.

The point is sharper than “assume compactness.” It identifies **which compactness** is needed: only a radius slightly above the asymptotically optimal residual level must become compact in the tail.

## Actual contact and the independent proximinality gate

For the equality predicate at a declared radius `r`, two operations must be separated.

The actual-contact profile asks whether the translated closed nuisance set itself enters the radius-`r` ball arbitrarily far out:

\[
\widehat\Delta_C(r;s)=\infty.
\]

If `nu_C(s;r)=0`, choose actual contacts `d_n-t_ns in overline B_r` with `t_n->infinity`. Tail compactness gives a convergent subsequence, producing a point of `mathcal B_C(s;r)`. The converse is immediate from the definition of `mathcal B_C`. Thus

\[
\widehat\Delta_C(r;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
\]

The distance-defined profile is different in a non-proximinal setting. The condition

\[
\operatorname{dist}(ts,D)\le r
\]

only guarantees arbitrarily close approximants to the closed radius-`r` ball; it does not force an actual point of `D` inside that ball when the infimum is not attained. Therefore vanishing tail noncompactness by itself cannot turn `Delta_C(r/2;s)=infinity` into a contact point of `mathcal B_C(s;r)`.

A sufficient additional condition is raywise radius-`r` proximinality:

\[
\operatorname{dist}(ts,D)\le r
\Longrightarrow
(D-ts)\cap\overline B_r(0)\ne\varnothing
\]

for the relevant large `t`. Global proximinality of `D` is stronger and therefore sufficient. Standard best-approximation theory supplies important classes: for example, nonempty closed convex subsets of reflexive Banach spaces are proximinal, and weakly compact subsets attain distance because the norm is weakly lower semicontinuous.

This separates two failure modes that finite-dimensionality hides:

\[
\text{distance sublevel}
\xrightarrow{\text{attainment}}
\text{actual contact}
\xrightarrow{\text{tail compactness}}
\text{norm contact cluster}.
\]

The first arrow is a best-approximation/proximinality question; the second is an asymptotic-compactness question. AF-496–AF-498 attack the second arrow with examples where actual contacts already exist, so their obstruction is genuinely noncompactness rather than nonattainment.

## The criterion is strictly weaker than finite-dimensional ambient geometry

Let `Y` be any infinite-dimensional Banach space, choose nonzero `s in Y`, choose any fixed `a in Y`, and set

\[
K:=\{0\}\cup\{ns+a:n\ge1\},
\qquad
C:=K-K.
\]

Then `K` is closed, unbounded, and noncompact. The exact difference set is

\[
C
=
\{0\}
\cup
\{\pm(ns+a):n\ge1\}
\cup
\{qs:q\in\mathbb Z\}.
\]

It is closed, and every element lies in the finite-dimensional subspace

\[
F:=\operatorname{span}\{s,a\}.
\]

For each fixed `R`, every tail residual set satisfies

\[
E_{T,R}(C,s)
\subset
F\cap\overline B_R(0).
\]

The right-hand side is compact because `F` is finite-dimensional. Hence

\[
\boxed{
\nu_C(s;R)=0
\quad\text{for every }R<\infty,
}
\]

even though the ambient space is infinite-dimensional and the nuisance family is unbounded and noncompact.

So AF-496's finite-dimensional characterization remains correct only as a **universal statement over all nuisance sets**. For a fixed family, the relevant dimension is not the dimension of `Y`; it is whether the residual geometry visible near the discriminator ray is asymptotically norm-tight.

## AF-498 has a quantitative noncompactness defect

The Elton–Odell construction in AF-498 makes the new obstruction profile explicit rather than merely nonzero.

At its critical times `t=a_n=2^n`, the exact residuals are

\[
r u_n,
\qquad
\|u_n\|=1,
\]

and their quotient images satisfy

\[
\|q_n-q_m\|_Q\ge1+\varepsilon.
\]

Because the quotient map is contractive,

\[
\|r u_n-r u_m\|
\ge
r\|q_n-q_m\|_Q
\ge
(1+\varepsilon)r.
\]

Every tail set `E_{T,r}` therefore contains an infinite `(1+epsilon)r`-separated family. A finite collection of balls of radius strictly below `(1+epsilon)r/2` cannot cover such a family. Consequently

\[
\boxed{
\nu_C(s;r)
\ge
\frac{(1+\varepsilon)r}{2}
>0.
}
\]

Thus AF-498 is diagnosed exactly by the family-level gate introduced here: its critical residual mass does not become metrically tight in the tail. The obstruction is not merely “infinite dimension”; it is a positive task-visible noncompactness defect.

## Prior-art and novelty audit

No broad novelty is claimed for asymptotic compactness, Hausdorff/Kuratowski measures of noncompactness, or proximinal sets.

- Junya Nishiguchi, **“Asymptotic compactness in topological spaces,”** *Topology and its Applications* 287 (2021), 107451, DOI `10.1016/j.topol.2020.107451`. This develops asymptotic compactness for nets of subsets and proves, in uniformizable spaces, equivalences between asymptotic compactness and convergence from above to compact limit sets; its sequential metric-space formulation is directly adjacent to the tail-residual criterion used here.
- Tomasz Zając, **“The Concept of Measures of Noncompactness in Banach Spaces,”** *Symmetry* 17(8) (2025), 1248, DOI `10.3390/sym17081248`. This surveys Kuratowski, Hausdorff, and related measures of noncompactness, including their compactness kernels and Cantor-intersection properties. The present `nu_C(s;R)` is a task-local tail specialization of this classical machinery.
- Standard best-approximation theory distinguishes proximinality from compactness. In particular, closed convex subsets of reflexive Banach spaces are proximinal; distance attainment is therefore a separate geometric resource from norm-precompactness.

The literature already contains the abstract ingredients. The durable Arithmetic Fidelity result is their exact placement in the AF-494–AF-498 recovery chain: **vanishing measure of noncompactness of the radius-truncated translated tail is the family-level replacement for ambient finite dimensionality, while critical equality additionally requires distance-sublevel attainment.** This converts AF-498's qualitative request for “compactness or metric tightness” into an exact falsifiable quantity and identifies which part of the fixed-noise theorem each resource controls.

## Falsification and boundary audit

- Completeness of `Y` is used when tail total boundedness produces a Cauchy subsequence. In a merely normed noncomplete space, the subsequence may converge only in the completion.
- `nu_C(s;R)=0` is a local-in-radius condition. Recovery of `lambda_C(s)` needs it only at one radius strictly above the liminf level; it need not hold for arbitrarily large residuals.
- The contact statement at radius `r` uses `nu_C(s;r)=0` for **actual** radius-`r` residuals. It does not manufacture an exact contact from an unattained distance infimum.
- Proximinality and tail compactness are independent in principle. A set may attain nearest points while its recurrent residuals disperse, as AF-496–AF-498 demonstrate; conversely a family can have tight near-minimizing residuals while exact distance attainment fails at isolated radii.
- The example showing strict weakness of ambient finite dimensionality has task-visible residuals contained in a finite-dimensional subspace. This proves the logical separation cleanly but does not claim that natural arithmetic families will have such a simple residual model.
- Positive `nu_C(s;r)` is an obstruction to the compactness route, not by itself a proof that the AF-494 scalar identity must fail for that particular family. The identity can hold accidentally without full asymptotic compactness. What `nu=0` supplies is a robust family-level sufficient gate, and AF-498 shows that its failure can be decisive.
- Nothing here identifies a rational-prime discriminator or advances RH directly. The result sharpens the abstract preservation theorem that an eventual arithmetic application would have to satisfy.

## Relationship to AF-494–AF-498

AF-494 and AF-495 obtain exact translation/contact-fiber laws in finite-dimensional normed observation spaces. AF-496 proves that no such norm-fiber law can hold uniformly over all closed nuisance sets in every infinite-dimensional space. AF-497 and AF-498 then show that exact nuisance difference-set structure does not rescue the theorem, even at the exact critical radius.

AF-499 identifies the constructive boundary left open by those obstructions. The correct replacement is not a weaker ambient dimension assumption but a **task-local tail condition**:

\[
\boxed{
\nu_C(s;R)=0
\quad\Longleftrightarrow\quad
\text{radius-}R\text{ translated aliases are asymptotically norm-precompact.}
}
\]

That gate is sufficient to restore the AF-494 threshold identity in arbitrary Banach spaces. For the AF-495 equality/contact law, it restores the compactness half, while proximinality separately supplies the exact-contact half. This gives later arithmetic work a concrete audit: compute or bound the noncompactness of the translated control family at the task-relevant radius instead of asking whether the entire ambient representation is finite-dimensional.