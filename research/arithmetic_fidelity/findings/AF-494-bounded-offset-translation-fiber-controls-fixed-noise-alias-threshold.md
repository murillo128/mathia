# AF-494 — Bounded-offset translation fibers control the fixed-noise alias threshold beyond horizon scaling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NONCONVEX-NUISANCE`, `TRANSLATION-LIMIT`, `MINIMAX-RESOLUTION`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-493 identifies the horizon/scaling set `C^infty` as the exact first-order invariant governing the normalized escape rate

\[
\liminf_{t\to\infty}\frac{\operatorname{dist}(ts,C)}{t}.
\]

That invariant is intentionally too coarse for fixed deterministic noise: when `s in C^infty`, the normalized distance can vanish whether the absolute distance stays bounded, converges to a positive constant, diverges sublinearly, or returns arbitrarily close to zero. The missing next layer is the set of **bounded offsets that actually recur after translating the nuisance set back along the discriminator ray**.

Let `Y` be a finite-dimensional normed real vector space, let `C subset Y` be nonempty, and let `s in Y`. Define the bounded-offset translation fiber

\[
\mathcal A_C(s)
:=
\left\{
 a\in Y:
 \exists\ t_n\to\infty,\ c_n\in C,
 \ c_n-t_n s\to a
\right\}.
\]

Also define the absolute asymptotic separation level

\[
\lambda_C(s)
:=
\liminf_{t\to\infty}\operatorname{dist}(ts,C)
\in[0,\infty].
\]

With the convention `dist(0,emptyset)=+infinity`, one has the exact identity

\[
\boxed{
\lambda_C(s)=\operatorname{dist}(0,\mathcal A_C(s)).
}
\]

Moreover `mathcal A_C(s)` is closed. Hence:

- `mathcal A_C(s)=emptyset` exactly when every nuisance alias escapes to unbounded absolute distance along the ray;
- if `mathcal A_C(s)` is nonempty, its nearest offset to the origin is attained and its norm is the sharp asymptotic fixed-noise threshold;
- for the ambiguity profile

\[
\Delta_C(\rho;s)
:=
\sup\{t\ge0:\operatorname{dist}(ts,C)\le2\rho\},
\]

one has

\[
\boxed{
2\rho>\lambda_C(s)
\Longrightarrow
\Delta_C(\rho;s)=\infty,
}
\]

while

\[
\boxed{
2\rho<\lambda_C(s)
\Longrightarrow
\Delta_C(\rho;s)<\infty.
}
\]

At the critical boundary `2rho=lambda_C(s)`, either behavior can occur. Thus `lambda_C(s)/2` is the sharp open fixed-noise phase boundary, but equality requires finer recurrence information than the translation fiber norm alone.

The distinction from AF-493 is structural. The horizon set records offsets after division by `t`; `mathcal A_C(s)` records offsets that remain `O(1)` **before** that division. These are different asymptotic layers.

## Exact translation-fiber theorem

First, `mathcal A_C(s)` is closed. Let `a_j in mathcal A_C(s)` and suppose `a_j -> a`. For each `j`, choose one witness pair `(t_j,c_j)` far enough along a sequence witnessing `a_j` that

\[
t_j\ge j,
\qquad
\|c_j-t_js-a_j\|\le\frac1j.
\]

Then `t_j->infinity` and

\[
\|c_j-t_js-a\|
\le
\|c_j-t_js-a_j\|+\|a_j-a\|
\to0,
\]

so `a in mathcal A_C(s)`.

Now set

\[
\lambda:=\liminf_{t\to\infty}\operatorname{dist}(ts,C).
\]

For every `a in mathcal A_C(s)`, choose witnesses `t_n->infinity` and `c_n in C` with `c_n-t_ns->a`. Then

\[
\operatorname{dist}(t_ns,C)
\le
\|t_ns-c_n\|
\to\|a\|,
\]

and therefore

\[
\lambda\le\|a\|.
\]

Taking the infimum gives

\[
\lambda\le\operatorname{dist}(0,\mathcal A_C(s)).
\]

For the reverse inequality, suppose first `lambda<infinity`. Choose `t_n->infinity` such that

\[
\operatorname{dist}(t_ns,C)\to\lambda.
\]

Choose `c_n in C` with

\[
\|t_ns-c_n\|
\le
\operatorname{dist}(t_ns,C)+\frac1n.
\]

The offsets `c_n-t_ns` are bounded. Finite-dimensional compactness gives a subsequence converging to some `a in Y`. By definition `a in mathcal A_C(s)`, and along that subsequence

\[
\|a\|=\lambda.
\]

Hence

\[
\operatorname{dist}(0,\mathcal A_C(s))\le\lambda.
\]

If `lambda=infinity`, then `mathcal A_C(s)` must be empty, because any bounded-offset witness would force a finite subsequential upper bound on `dist(t_ns,C)`. This proves the identity in all cases.

Closedness of `C` is not needed for this identity because approximate minimizers suffice. When `C` is closed in finite dimension, exact nearest points may be used instead.

## Fixed-noise phase transition

If

\[
\lambda_C(s)<2\rho,
\]

choose `eta>0` with `lambda_C(s)+eta<2rho`. By the definition of liminf there are arbitrarily large `t` for which

\[
\operatorname{dist}(ts,C)<\lambda_C(s)+\eta<2\rho.
\]

Thus the admissible set in `Delta_C(rho;s)` is unbounded and

\[
\Delta_C(\rho;s)=\infty.
\]

If instead

\[
\lambda_C(s)>2\rho,
\]

choose `eta>0` with `lambda_C(s)-eta>2rho`. The defining property of a liminf gives a threshold `T` after which

\[
\operatorname{dist}(ts,C)>\lambda_C(s)-\eta>2\rho.
\]

Hence no `t>=T` is admissible and `Delta_C(rho;s)<infinity`.

This gives an exact open-threshold statement. The equality case cannot be inferred from `lambda_C(s)` alone. A sequence can approach the critical radius entirely from above, or it can hit the critical ball infinitely often.

For an actual nuisance family `K` with `C=K-K`, any unbounded sequence satisfying `dist(ts,C)<=2rho` gives the usual two-target collision from AF-491 whenever the distance is attained (in particular for closed `C`). Consequently `Delta_C(rho;s)=infinity` implies infinite deterministic minimax target radius in that observation model.

## The critical equality case really contains extra information

Fix `L>=0` in `R^2` with Euclidean norm and `s=e_1`. Consider any closed set whose only large bounded-offset points relative to the positive `e_1` ray have offsets `(0,g_n)` at horizontal positions `n`.

If

\[
g_n\equiv L,
\]

then

\[
\lambda_C(e_1)=L
\]

and the critical sublevel is hit at every integer:

\[
\operatorname{dist}(ne_1,C)\le L.
\]

Thus `Delta_C(L/2;e_1)=infinity`.

If instead

\[
g_n=L+\frac1n,
\]

with all other large points farther than `L` from the ray, then still

\[
\lambda_C(e_1)=L,
\]

but eventually

\[
\operatorname{dist}(te_1,C)>L
\]

for every `t`; hence the critical sublevel is bounded. The same translation-fiber norm therefore permits opposite behavior exactly at the threshold.

The missing datum at equality is not another first-order cone. It is whether the translated sets actually meet the closed critical ball arbitrarily far out, rather than merely converging to its boundary from outside.

## Same horizon geometry, every fixed-noise threshold, using genuine difference sets

AF-493 gave a sparse curved closed-set example showing that horizon membership does not force bounded absolute aliases, but explicitly noted that the example was not presented as a nuisance difference set. The phenomenon persists for exact difference sets `K-K`.

Work in `Y=R^2` with `s=e_1`. Let

\[
H_n:=2^{2^n},
\]

and let `(g_n)` be any nonnegative sequence satisfying

\[
g_n=o(n).
\]

Define the closed discrete nuisance family

\[
K_g
:=
\{a_n,b_n:n\ge1\},
\qquad
 a_n=(0,H_n),
\qquad
 b_n=(n,H_n+g_n),
\]

and put

\[
C_g:=K_g-K_g.
\]

The set `C_g` is closed. Indeed, if both indices in a cross-pair difference become large and unequal, the vertical coordinate has magnitude comparable to the dominant double-exponential height gap and therefore escapes every compact set. Same-index pair differences are

\[
b_n-a_n=(n,g_n),
\qquad
a_n-b_n=(-n,-g_n),
\]

which also escape every compact set as `n->infinity`. Thus no new finite accumulation point is created.

The asymptotic directions of `C_g` are independent of the particular sublinear sequence `g_n`. Same-index pair differences give the horizontal direction because

\[
\frac{(n,g_n)}{n}\to e_1.
\]

Unequal-index differences are asymptotically vertical because the height gap `|H_n-H_m|` dominates every horizontal coordinate and every `g_j`. Consequently the horizon/scaling set is

\[
\boxed{
C_g^\infty
=
\operatorname{span}(e_1)
\cup
\operatorname{span}(e_2).
}
\]

Yet the bounded-offset threshold along the horizontal discriminator is

\[
\boxed{
\lambda_{C_g}(e_1)=\liminf_{n\to\infty}g_n.
}
\]

The upper bound is immediate from the same-index differences `(n,g_n)`. For the reverse direction, suppose `t_j->infinity` and `c_j in C_g` remain within a fixed bounded distance of `t_je_1`. Then the first coordinate of `c_j` tends to `+infinity` while its second coordinate remains bounded. Unequal-index differences are impossible eventually because their vertical coordinates diverge through the double-exponential height gaps. The only remaining positive-horizontal differences are therefore `(n,g_n)` from matched pairs. Hence every bounded-offset alias sequence has asymptotic norm at least `liminf g_n`, proving the identity.

This gives a family of **genuine nuisance difference sets with exactly the same horizon geometry but arbitrary fixed-noise asymptotics**:

- `g_n=0` gives exact aliases at arbitrarily large displacement and `lambda=0`;
- `g_n=L` gives any prescribed finite threshold `lambda=L`;
- `g_n=L+1/n` has the same `lambda=L` but can avoid the critical closed ball eventually;
- `g_n=sqrt(n)` still has `g_n=o(n)` and therefore the same horizon set, but `lambda=infinity`, so every fixed noise budget is eventually escaped.

Thus the horizon invariant can remain literally unchanged while the fixed-noise phase boundary ranges over every value in `[0,infinity]`.

## Two asymptotic layers

For arbitrary nonconvex nuisance geometry there are therefore at least two logically distinct asymptotic questions.

The AF-493 blow-down

\[
t^{-1}C
\]

asks which **directions** survive after scale normalization. It determines the linear escape coefficient

\[
\liminf_{t\to\infty}\frac{\operatorname{dist}(ts,C)}t.
\]

The present translated family

\[
C-ts
\]

asks which **bounded offsets** recur after following one declared discriminator direction. It determines

\[
\liminf_{t\to\infty}\operatorname{dist}(ts,C).
\]

A direction may survive the blow-down while having no bounded translated offset at all. This is exactly what happens for `g_n=sqrt(n)`: the horizontal direction is present in `C_g^infty`, but the translated fiber is empty and every fixed-radius noise ball eventually separates from the nuisance difference set.

Conversely, if `mathcal A_C(s)` contains `0`, then there are asymptotically exact aliases along the ray even if the ray never meets `C` exactly. Exact zero-noise collisions require the stronger condition that `ts in C` for unbounded `t`; asymptotic approach to zero is not the same statement.

This is a concrete instance of the general Arithmetic Fidelity principle that a compression can preserve the correct first-order direction while losing the finer relational scale needed by the downstream task.

## Relation to hyperspace and second-order asymptotic prior art

No broad novelty is claimed for studying translated closed sets or finer asymptotics beyond recession/horizon cones.

- J. M. G. Fell, **“A Hausdorff Topology for the Closed Subsets of a Locally Compact Non-Hausdorff Space,”** *Proceedings of the American Mathematical Society* 13 (1962), 472–476. Role: foundational hyperspace topology for local limits of closed sets. The family `C-ts` can be viewed through this local/Fell convergence language; `mathcal A_C(s)` records all finite points appearing in subsequential translated limits.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Springer (1998), DOI `10.1007/978-3-642-02431-3`. Role: horizon cones, Painleve-Kuratowski limits, distance-function convergence, and the first-order variational framework used already in AF-493.
- Fabian Flores-Bazan, Nicolas Hadjisavvas, and Felipe Lara, **“Second Order Asymptotic Analysis: Basic Theory,”** *Journal of Convex Analysis* 22(4) (2015), 1173–1196. Role: explicit prior art that first-order asymptotic cones can be refined by second-order asymptotic structure. The present bounded-offset fiber is not claimed to be a renaming of their specific second-order cone; it is the task-adapted translated-set invariant that exactly represents the AF fixed-noise liminf.

The durable Arithmetic Fidelity contribution is the exact placement of these two scales in the nuisance-recovery chain and the true-difference-set separation example: **the horizon set fixes only normalized linear escape, while the translated bounded-offset fiber fixes the sharp open fixed-noise alias threshold; even exact nuisance difference sets can share the same horizon geometry and realize every possible bounded-offset threshold.**

## Falsification and boundary audit

- Finite dimensionality is used only in the reverse direction of the translation-fiber identity, to extract a convergent subsequence from bounded offsets. In infinite-dimensional spaces, bounded offsets need not have norm-convergent subsequences; an appropriate weak, compactness, or hyperspace formulation would be required.
- The identity concerns `liminf` and therefore subsequential recurrence. It does not assert convergence of the translated sets `C-ts`, uniqueness of a local/Fell limit, or a full asymptotic expansion.
- `lambda_C(s)` does not decide the equality case `2rho=lambda_C(s)`. The explicit `g_n=L` versus `g_n=L+1/n` construction shows why.
- The difference-set examples are deliberately synthetic. They prove that no theorem based only on the horizon set can recover the fixed-noise threshold for arbitrary nuisance difference sets. They do not assert that naturally occurring arithmetic control families have this pathology.
- The double-exponential heights are a separation device ensuring cross-pair differences cannot create unintended bounded horizontal aliases. Their numerical form is not canonical and carries no arithmetic meaning.
- `s in C^infty` remains a necessary condition for finite `lambda_C(s)`, but it is far from sufficient. AF-493's first-order horizon test and the present translation-fiber test answer different questions and should not be substituted for one another.
- Nothing here identifies a rational-prime discriminator, proves arithmetic provenance, or advances RH directly. The result is a general obstruction/representation theorem for what a coarse asymptotic compression can and cannot retain.

## Relationship to AF-491–AF-493

AF-491 identifies `dist(ts,K-K)` as the exact bounded-nuisance ambiguity profile. AF-492 shows that closed convex symmetric difference sets simplify dramatically: recession directions form a quotient and the residual nuisance body is compact. AF-493 shows why that convex picture fails for general nonconvex sets and replaces recession geometry by the horizon set for first-order normalized escape.

AF-494 now resolves the next scale left open by AF-493. Once a discriminator lies in the horizon set, the correct invariant for **fixed-radius** ambiguity is not another normalized cone but the bounded-offset translation fiber `mathcal A_C(s)`. The chain is therefore

\[
\text{recession quotient in the convex case}
\;\longrightarrow\;
\text{horizon direction for first-order nonconvex escape}
\;\longrightarrow\;
\text{translated bounded-offset fiber for fixed-noise recurrence}.
\]

The synthetic difference-set family proves that the last arrow adds irreducible information: identical horizon data can correspond to exact recurrent aliases, any positive alias threshold, or eventual escape from every fixed noise budget.