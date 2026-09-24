# MC-504 — Profile/start participation obeys a product tariff

**Status:** `EXACT-DERIVED` · `CLASSICAL-HILBERT+DERIVED-APPLICATION` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-503` proves that once one incomplete lower-prime coefficient profile is fixed, its correlation with the quadratic conductor phase can be large only on a sparse set of conductor starts, with sparsity controlled by the profile effective support. The accepted first-exit clue leaves one precise loophole: the physical source may pair each changing profile with one of that profile's exceptional starts.

There is an exact weighted form of the same obstruction. It does not require the physical source to sample starts uniformly. Instead it charges **both** the effective support inside the profile and the effective participation of the actual source across conductor starts conditional on that profile.

Let `p` be an odd prime and let

\[
F:\mathbf F_p\to\mathbf C,
\qquad
\sum_{x\bmod p}F(x)=0,
\]

with unnormalized additive Fourier transform satisfying

\[
|\widehat F(k)|\le C\sqrt p
\qquad(k\ne0).
\tag{1}
\]

Fix a coefficient profile `b=(b_j)` supported on at most `p` distinct shifts and define

\[
T_b(x)=\sum_j b_jF(x+j).
\tag{2}
\]

For **arbitrary** source-start weights `a:\mathbf F_p\to\mathbf C`,

\[
\boxed{
\left|\sum_{x\bmod p}a(x)T_b(x)\right|
\le C\sqrt p\,\|a\|_2\,\|b\|_2.
}
\tag{3}
\]

When `a,b` are nonnegative and nonzero, put

\[
A=\|a\|_1,
\qquad
B=\|b\|_1,
\qquad
R_a=\frac{A^2}{\|a\|_2^2},
\qquad
R_b=\frac{B^2}{\|b\|_2^2}.
\tag{4}
\]

Then the normalized bias obeys the **profile/start product tariff**

\[
\boxed{
\frac{\left|\sum_xa(x)T_b(x)\right|}{AB}
\le
C\sqrt{\frac{p}{R_aR_b}}.
}
\tag{5}
\]

Consequently, fixed normalized bias `>=eta` is possible only if

\[
\boxed{
R_aR_b\le \frac{C^2p}{\eta^2}.
}
\tag{6}
\]

For an exact `0/1` hard-mask profile with `M` surviving positions, `R_b=M`. If the physical source carrying that same profile has equal mass on `K` distinct conductor starts, `R_a=K`, so order-one normalized bias requires

\[
\boxed{MK\ll_\eta p.}
\tag{7}
\]

Thus a large-support mask cannot remain dangerous merely because its exceptional starts exist: the source must also concentrate strongly on those starts **after conditioning on the profile**. Conversely, if the exact profile changes essentially every time the source start changes, then `R_a` may collapse to `1`; the theorem honestly exposes profile diversity itself as the remaining arithmetic resource rather than hiding it behind a uniform-start heuristic.

The same statement sums over profile classes. For classes `c` with fixed profiles `b_c` and actual conditional start weights `a_c`,

\[
\mathcal C
:=\sum_c\sum_x a_c(x)T_{b_c}(x)
\]

satisfies

\[
\boxed{
|\mathcal C|
\le
C\sum_c A_cB_c
\sqrt{\frac{p}{R_{a,c}R_{b,c}}},
}
\tag{8}
\]

where `A_c=||a_c||_1` and `B_c=||b_c||_1`. Hence the full source can sustain fixed normalized bias only through classes carrying non-negligible mass for which the participation product `R_{a,c}R_{b,c}` is at most conductor scale, or through failure of any useful profile-class factorization.

For the quadratic relative phase of `MC-495`/`MC-497`, hypothesis `(1)` holds uniformly with an absolute `C`. Therefore the surviving lower-prime hard-mask question is now sharper: **does the first-exit source create low product participation by tying many distinct profile shapes to individually exceptional starts, or can the source be grouped into recurrent high-support profiles whose conditional start participation forces cancellation by `(5)`?**

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Proof from the fixed-profile second moment

`MC-503` proves, under `(1)`,

\[
\sum_{x\bmod p}|T_b(x)|^2
\le C^2p\|b\|_2^2.
\tag{9}
\]

Pairing the actual source-start weight with this translate family and applying Cauchy--Schwarz gives

\[
\begin{aligned}
\left|\sum_xa(x)T_b(x)\right|
&\le \|a\|_2
\left(\sum_x|T_b(x)|^2\right)^{1/2}\\
&\le C\sqrt p\,\|a\|_2\,\|b\|_2,
\end{aligned}
\]

which is `(3)`.

For nonnegative `a,b`, substitute

\[
\|a\|_2=A/\sqrt{R_a},
\qquad
\|b\|_2=B/\sqrt{R_b}
\]

to obtain `(5)`. Equation `(6)` is immediate.

This is stronger for the physical-source question than applying the exceptional-set estimate of `MC-503` followed by a crude union bound. The source weights may be highly nonuniform; all of that nonuniformity is retained exactly in `R_a`. A source placing almost all mass on one exceptional start has `R_a\approx1` and pays essentially no start-dispersion gain. A source genuinely spread over many starts has large `R_a`, and that dispersion multiplies the profile support resource rather than being treated separately.

## 2. Multiple exact profile classes

Suppose the physical pairs have been partitioned into exact profile classes. For class `c`, collect all source mass producing the same coefficient vector `b_c` into

\[
a_c(x)=\text{total source weight in class }c\text{ at conductor start }x.
\tag{10}
\]

No equidistribution assumption is made: `a_c` is the exact pushforward of the source measure.

Applying `(3)` class by class gives

\[
\left|\sum_xa_c(x)T_{b_c}(x)\right|
\le C\sqrt p\|a_c\|_2\|b_c\|_2.
\tag{11}
\]

Summing `(11)` and rewriting the two `ell^2` norms via `(4)` gives `(8)`.

If

\[
W=\sum_cA_cB_c,
\qquad
\lambda_c=\frac{A_cB_c}{W},
\]

then

\[
\frac{|\mathcal C|}{W}
\le
C\sum_c\lambda_c
\sqrt{\frac{p}{R_{a,c}R_{b,c}}}.
\tag{12}
\]

Thus no single worst class needs to control the whole source. A small collection of low-participation classes is harmless if it carries negligible `lambda_c`-mass; a load-bearing obstruction must carry enough actual source mass while keeping the participation product small.

This is the correct weighted replacement for the informal statement that “most profiles should occur at many starts.” What matters is not the number of classes, the raw number of source pairs, or the raw number of distinct starts, but the classwise `ell^1/ell^2` participation seen by the actual reconstruction weights.

## 3. Approximate profile classes and the cost of grouping

Exact profile equality may be too fine for the first-exit source. A controlled approximation can still be used, but its error must be charged explicitly.

For each source item `alpha` in class `c`, suppose its exact profile has a decomposition

\[
b_\alpha=s_\alpha b_c+e_\alpha,
\qquad s_\alpha\ge0.
\tag{13}
\]

Absorb `s_alpha` into the source-start weight,

\[
a_c(x)=\sum_{\substack{\alpha\in c\\x_\alpha=x}}
w_\alpha s_\alpha.
\tag{14}
\]

The representative-profile contribution obeys `(8)`. The residual contribution is bounded directly by

\[
\left|
\sum_\alpha w_\alpha
\sum_j e_{\alpha,j}F(x_\alpha+j)
\right|
\le
\|F\|_\infty
\sum_\alpha w_\alpha\|e_\alpha\|_1.
\tag{15}
\]

For the centered quadratic character phase, `||F||_infty=O(1)`. Hence a profile compression is legitimate only when its total weighted `ell^1` distortion is smaller than the cancellation scale being claimed. Grouping profiles by an attractive combinatorial descriptor without proving `(15)` small is not a valid escape from exact profile diversity.

This gives a practical two-part admission test for the accepted clue: either find exact recurrent profiles with large `R_aR_b`, or construct approximate classes with a quantitatively small distortion budget and then apply the same product tariff to the representative profiles.

## 4. Application to the first-exit hard-mask branch

The live cross-root object after `MC-495` is a nonnegative source weight against the relative phase

\[
R_a(m)=\chi\!\left(1-\frac{h^2}{a^2m^2}\right),
\]

and `MC-503` shows that for the quadratic specialization its centered translate family has conductor-start second moment controlled solely by the `ell^2` mass of the exact incomplete coefficient profile.

The present result restores the next piece that `MC-503` deliberately left open: the **actual source measure on starts**. Once a collection of first-exit pairs shares one exact profile, no artificial averaging is needed. Their physical multiplicities and reconstruction weights define `a` in `(3)` directly.

For a `0/1` hard mask with `M` surviving positions and conditional source participation `R_a`, the class contribution is bounded by

\[
\frac{|\text{class bias}|}{\text{class mass}}
\ll \sqrt{\frac{p}{MR_a}}.
\tag{16}
\]

Therefore a class with `M R_a\gg p` cannot carry order-one bias. To evade this, the source must do at least one of the following:

- produce low-support profiles `M\lesssim p/R_a`;
- keep conditional start participation small by assigning a profile to only a few effective starts;
- vary the profile so rapidly that no high-mass recurrent class exists;
- or introduce a genuinely signed/complex pre-aggregation coefficient outside the nonnegative profile framework of `MC-495`.

The third item is now a precise target rather than a vague irregularity heuristic. Profile diversity is useful only if the resulting classes retain enough source mass to matter and cannot be compressed with small error as in `(13)`--`(15)`.

## 5. Prior art and novelty boundary

No novelty is claimed for `(3)`. It is Hilbert-space duality/Cauchy--Schwarz applied to the Parseval second moment already proved in `MC-503`. This sits inside the classical large-sieve/duality tradition; Bombieri's *On the large sieve* (Mathematika 12 (1965), 201--225, DOI `10.1112/S0025579300005313`) is a classical anchor, and Montgomery--Vaughan's large-sieve treatment presents mean-square forms as the basic language for deriving character-sum variants. A recent weighted large-sieve treatment by Olivier Ramaré, *The weighted large sieve through Parseval* (arXiv:2605.29470, 2026), further illustrates that weighted Parseval formulations are standard analytic machinery, not a Mathia novelty claim.

The durable contribution here is the **frontier specialization** forced by the current source representation: `MC-503` priced exceptional starts for one frozen profile, while `(5)` identifies the exact multiplicative participation quantity that controls the real source pushforward at fixed profile. The theorem does not discover a new large-sieve inequality; it converts the residual “profile/start alignment” loophole into a measurable arithmetic requirement on the first-exit family.

The literature audit did not identify a theorem that supplies the missing first-exit profile recurrence or the required classwise participation automatically. Those are source-specific arithmetic questions and remain unproved.

## Representation audit

The theorem preserves exactly the information it claims to use. Inside each class, `b_c` is the retained physical coefficient profile and `a_c(x)` is the exact pushforward of the physical source/reconstruction weight onto conductor starts. No uniform-start measure, random-mask model, smooth envelope, complete auxiliary period, or independence hypothesis is inserted.

The only compression occurs when source items are declared to share a profile class. Exact classes lose nothing. Approximate classes are legal only with the explicit `ell^1` error budget `(15)`. Thus the theorem cannot manufacture cancellation by hiding profile variation inside an uncontrolled representative.

## Boundaries and falsification tests

- **Quadratic application only through MC-503.** The abstract theorem needs `(1)`. The current first-exit application has that multiplier bound for the quadratic relative phase; other character orders require their own audit.
- **Profile recurrence is not proved.** The theorem does not show that the physical source produces repeated or compressible hard-mask profiles.
- **Small `R_a` is a genuine escape.** One heavily weighted start can defeat the participation gain even when the profile itself has large support.
- **Small `R_b` is a genuine escape.** Highly concentrated profiles remain dangerous and must be bounded arithmetically.
- **Approximate grouping must pay `(15)`.** Semantic or combinatorial similarity between profiles is irrelevant unless the actual coefficient distortion is quantitatively small.
- **No independence assumption.** Profile and start may be maximally dependent; `(5)` is conditional on the fixed profile and charges that dependence through `R_a`.
- **No converse.** `R_aR_b\lesssim p` only leaves order-one bias possible; it does not force negative correlation with the conductor phase.
- **No all-source conclusion without class control.** Equation `(8)` still requires a source-specific partition or compression with enough mass in classes of large participation product.
- **No global Möbius conclusion.** There is no new bound for `M(x)`, no zero-free region, and no RH consequence.

## Consequence for the accepted clue

The hard-mask branch of the accepted q-vdC clue no longer needs an unweighted exceptional-set argument. For every exact recurrent profile, the physical source-start pushforward can be inserted directly into `(5)`. The decisive source quantity is

\[
R_{\rm profile}\times R_{\rm start\mid profile}.
\]

The next arithmetic test is therefore to classify or compress the actual first-exit lower-prime profiles and measure, with reconstruction weights included, how much source mass sits in classes for which this product is only `O(p)`. If material source mass instead lies in classes with product `\gg p`, the quadratic hard-mask alignment route is closed there. If profile diversity prevents such classes, that diversity itself must be derived and quantified as the load-bearing resource rather than assumed from irregularity.
