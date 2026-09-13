# MC-275 — Witness normalization has an OR approximate-degree barrier

**Status:** `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the flat Christoffel source formulation of `MC-268`–`MC-274`. Write the lower-prime signs as

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad
n_i(x):=\frac{1-x_i}{2},
\qquad
b(x):=\sum_{i=1}^k n_i(x),
\]

and let

\[
g_m(x)=\sum_{|S|\le m}x_S.
\]

`MC-273` proved that whenever `n_i(x)=1`,

\[
g_m(x)=e_m(x_{\widehat i}),
\tag{1}
\]

where `e_m` is the homogeneous degree-`m` elementary symmetric sum with coordinate `i` deleted. Therefore the **overlapping sum over every negative witness** is cheap:

\[
\boxed{
U_m(x)
:=\sum_{i=1}^k n_i(x)e_m(x_{\widehat i})
=b(x)g_m(x).
}
\tag{2}
\]

It has Walsh/source degree at most `m+1`. In fact it is radial and satisfies the adjacent-shell identity

\[
\boxed{
U_m(x)
=\frac12\Big((k-m)e_m(x)-(m+1)e_{m+1}(x)\Big).
}
\tag{3}
\]

Thus the deep first-witness conditioning tax of `MC-274` is **not** a tax on merely summing all witnesses. One may keep all negative witnesses simultaneously with only one extra source degree.

The obstruction appears at the next step: turning this overlapping cover into a normalized witness decomposition that counts every nonblind row once. Put

\[
\operatorname{NB}(x)
:=\mathbf 1_{\{b(x)>0\}}
=1-\mathbf 1_{\{x=(1,\ldots,1)\}}.
\tag{4}
\]

Any exact polynomial witness normalization whose total weight is `1` on every nonblind sign vector and `0` on the blind vector has total selector exactly `NB`. The unique multilinear polynomial for `(4)` is

\[
\boxed{
\operatorname{NB}(x)
=1-2^{-k}\prod_{i=1}^k(1+x_i),
}
\tag{5}
\]

so

\[
\boxed{\deg_{\mathrm W}\operatorname{NB}=k.}
\tag{6}
\]

Consequently, for **every** exact polynomial witness allocation `\phi_1,\ldots,\phi_k` satisfying

\[
\sum_{i=1}^k\phi_i(x)=\operatorname{NB}(x),
\tag{7}
\]

at least one selector has Walsh/source degree `k`. This remains true even if the allocation is not produced by a coordinate decision tree and even if the selectors are allowed to use arbitrary real coefficients. Requiring additionally that `\phi_i(x)=0` unless `x_i=-1` does not weaken the lower bound.

The canonical symmetric normalization makes the same cost visible as division by the witness count. On `b\ge1`, `(2)` would become a genuine one-count decomposition only after multiplication by `1/b`. If a polynomial `q(b)` satisfies

\[
bq(b)=1\qquad(b=1,\ldots,k),
\tag{8}
\]

then necessarily

\[
\boxed{\deg q\ge k-1.}
\tag{9}
\]

Indeed `bq(b)-1` has `k` distinct roots; if `\deg q<k-1`, it would be a nonzero polynomial of degree `<k` with `k` roots. Thus the cheap identity `(2)` does not become a cheap exact partition after radial normalization: the missing `1/b` factor reconstructs endpoint-scale degree.

There is also a quantitative barrier for **approximate** normalization. Classical approximate-degree theory for the OR function gives, for `2^{-k}\le\varepsilon\le1/3`,

\[
\boxed{
\deg_\varepsilon(\operatorname{NB})
=\Theta\!\left(\sqrt{k\log(1/\varepsilon)}\right).
}
\tag{10}
\]

Hence if polynomial selectors `\phi_i` have a total

\[
P(x)=\sum_i\phi_i(x)
\]

satisfying

\[
|P(x)-\operatorname{NB}(x)|\le\varepsilon
\qquad\text{for every }x\in\{-1,+1\}^k,
\tag{11}
\]

then

\[
\boxed{
\max_i\deg_{\mathrm W}\phi_i
\ge
\Omega\!\left(\sqrt{k\log(1/\varepsilon)}\right).
}
\tag{12}
\]

Already at constant error this is `Omega(sqrt(k))`, far above the live Christoffel depth `m=Theta(log log y)`. If a pointwise polynomial normalization is accurate enough that summing it over

\[
C=\binom{N_y}{t}
\]

target rows determines the integer blind count with aggregate deterministic error `<1/2`, then one needs `\varepsilon<1/(2C)`. Using the live asymptotics from `MC-274`,

\[
k\sim\frac{y}{\log y},
\qquad
\log C
=\left(\frac1{\log2}+o(1)\right)\log y\,\log\log y,
\tag{13}
\]

so `(12)` forces

\[
\boxed{
\deg P
=\Omega\!\left(\sqrt{y\log\log y}\right).
}
\tag{14}
\]

By contrast the unconditioned Christoffel energy uses source degree

\[
2m=\Theta(\log\log y).
\tag{15}
\]

Therefore a generic pointwise-stable polynomial normalization of negative witnesses cannot be inserted into the support-matched Christoffel hierarchy at logarithmic source depth. This closes a broader escape than `MC-274`: replacing the first-negative decision tree by an arbitrary low-degree polynomial partition of unity still fails on the full Boolean cube.

The result does **not** rule out an arithmetic theorem restricted to the actual tightly localized Legendre-sign image. That restriction is now the essential escape hatch. `MC-252` showed that once the shell localization of the upper primes is removed, arbitrary finite binary sign patterns are exactly realizable by genuine Legendre-symbol matrices. Thus bare quadratic reciprocity and primality cannot by themselves invalidate the Boolean-cube lower bound; any successful low-depth normalization must use the moving shell `r\in(y,2y]`, source coupling, or another arithmetic restriction absent from the separated-prime realization.

No blind relation is excluded, no flat-energy estimate is proved, and no bound for `M(X)` follows.

## 1. Overlapping witnesses cost one degree, not decision-tree depth

For a negative coordinate `i`, identity `(1)` gives

\[
n_i(x)e_m(x_{\widehat i})=n_i(x)g_m(x).
\]

Summing over `i` proves `(2)`. This operation is nonadaptive: no first witness is selected, no cells are made disjoint, and no all-positive prefix is queried.

Equation `(3)` follows directly by expanding the two sums. Every degree-`m` monomial `x_S` appears in

\[
\sum_i e_m(x_{\widehat i})
\]

for exactly `k-m` indices `i`, while

\[
\sum_i x_i e_m(x_{\widehat i})
=(m+1)e_{m+1}(x).
\]

Therefore

\[
U_m
=\frac12\sum_i(1-x_i)e_m(x_{\widehat i})
=\frac12\big((k-m)e_m-(m+1)e_{m+1}\big).
\]

This is a classical neighboring-shell/Krawtchouk recurrence in another form, consistent with the information-neutral radial recurrence already isolated in `MC-267`. The new frontier point is not the recurrence itself. It is the separation between a cheap **overlapping** witness cover and the expensive operation of normalizing that cover into one unit of mass per nonblind row.

## 2. Exact normalization reconstructs the endpoint projector

The blind vector is `1^k=(1,\ldots,1)`. Its indicator is

\[
\delta_{1^k}(x)=2^{-k}\prod_i(1+x_i),
\]

whose degree-`k` Walsh coefficient is `2^{-k}`. Equation `(5)` follows, and the coefficient of `x_1\cdots x_k` in `NB` is `-2^{-k}\ne0`. Therefore `(6)` is exact.

Suppose an allocation `\phi_i` assigns polynomial weight to candidate witnesses and its weights sum to one on every nonblind input and zero on the blind input. Then `(7)` holds as an identity on the Boolean cube. Multilinearizing each selector does not change its values or increase its degree. If every selector had degree `<k`, their sum would also have degree `<k`, contradicting `(6)`.

This argument does not depend on sequential querying, positivity, symmetry, or a chosen ordering of the primes. It is an endpoint-projector obstruction for **all exact polynomial witness partitions**.

The reciprocal formulation `(8)` identifies the same endpoint cost in the most natural symmetric allocation. The unnormalized cover counts each row `b` times, and removing that multiplicity requires interpolating `1/b` across every nonzero Hamming weight. Exact polynomial interpolation necessarily reaches degree `k-1`.

## 3. Uniformly approximate normalization still costs square-root source depth

For a Boolean function `f`, its `\varepsilon`-approximate degree is the least degree of a real polynomial that approximates `f` pointwise to error at most `\varepsilon` on the Boolean cube. Since `NB` is OR applied to the negative bits `n_i`, the classical small-error OR theorem applies directly.

Buhrman, Cleve, de Wolf and Zalka, *Bounds for Small-Error and Zero-Error Quantum Algorithms*, FOCS 1999, DOI `10.1109/SFFCS.1999.814607`, derive the tight small-error search bound underlying

\[
\deg_\varepsilon(\mathrm{OR}_k)
=\Theta\!\left(\sqrt{k\log(1/\varepsilon)}\right)
\]

in the relevant range. See also https://arxiv.org/abs/cs/9904019.

Ronald de Wolf, *A note on quantum algorithms and the minimal degree of epsilon-error polynomials for symmetric functions*, arXiv:0802.1816 (2008), states this OR bound explicitly and places it in the general tight theory of small-error approximation for symmetric Boolean functions; see https://arxiv.org/abs/0802.1816. Alexander Sherstov, *Approximate Inclusion-Exclusion for Arbitrary Symmetric Functions*, ECCC TR07-116 (2007), treats the same polynomial-approximation phenomenon from the approximate inclusion-exclusion viewpoint; see https://eccc.weizmann.ac.il/report/2007/116/.

Equation `(12)` is then immediate: `P=\sum_i\phi_i` has degree at most the maximum selector degree, but `(11)` makes `P` an `\varepsilon`-approximating polynomial for OR.

The `1/C` specialization is not an external complexity theorem. It is the elementary accounting needed if a proof intends to recover an integer count by summing a pointwise approximation over `C` rows: the worst-case total approximation error is at most `C\varepsilon`. Requiring this to be `<1/2` yields the stated atom-sensitive scale. Substituting `(13)` into the classical OR lower bound gives `(14)`.

## 4. Separated-prime Legendre universality keeps the control arithmetic

The lower bound above is a theorem on the full Boolean cube, whereas the actual vectors

\[
x_p(T)=\prod_{r\in T}\left(\frac pr\right)
\]

come from a tightly localized arithmetic shell. It would be invalid to infer from generic approximate degree alone that the actual shell cannot have a much cheaper certificate.

`MC-252` supplies the relevant matched control. Once the upper primes may move arbitrarily far beyond `y`, every prescribed lower-prime Legendre column is realizable by CRT, quadratic reciprocity and Dirichlet's theorem. For any desired sign vector `x` and any fixed shell cardinality `t\ge1`, choose one separated-prime column realizing `x` and `t-1` distinct columns realizing the all-positive vector. Their coordinatewise product is exactly `x`. Thus the relaxed separated-prime model realizes the entire cube even at fixed positive target degree.

Therefore a proposed low-depth witness-normalization theorem that uses only the formal Legendre-symbol algebra, reciprocity, or primality but not the tight size coupling cannot evade `(10)`–`(12)`. The actual shell may still evade it, but only through information destroyed by the separated-prime control—precisely the localization/source coupling already isolated by `MC-252`.

## 5. What this closes and what remains open

`MC-274` showed that a **disjoint first-witness partition** implemented by coordinate queries pays one unit of source degree per query and reaches atom scale only after `J\asymp\log C` queries. The present result separates three notions that should no longer be conflated:

- keeping all witnesses with overlap is cheap: `(2)` costs only one extra source degree;
- converting the overlap into an exact polynomial partition of unity costs full degree `k`;
- even uniformly approximate normalization on the generic cube costs `Omega(sqrt(k))` at constant error and `Omega(sqrt(k log C))` at atom-sensitive error.

Thus the low-depth escape is **not** to discover or normalize witnesses more cleverly on a generic sign cube. A surviving proof must avoid generic pointwise OR approximation altogether. Viable possibilities include a theorem specific to the tightly localized Legendre image, a distributional rather than worst-case approximation whose error is controlled on that arithmetic image, or a signed aggregate that exploits `(2)` without dividing by `b` and without converting it into a positive endpoint classifier.

## Prior-art and novelty boundary

Exact OR representation, polynomial interpolation on Hamming weight, approximate degree of OR, approximate inclusion-exclusion, and the Krawtchouk/neighboring-shell algebra behind `(3)` are classical. No novelty is claimed for any of those ingredients.

The durable Mathia contribution claimed here is the **frontier synthesis** forced by `MC-273` and `MC-274`: simultaneous negative-witness aggregation avoids the decision-tree depth tax, but the normalization needed to turn the overlapping cover into one unit per nonblind row is precisely an OR/union problem. Classical exact and approximate-degree bounds then show that generic polynomial normalization lies far outside the live support depth, while `MC-252` identifies tight prime-shell localization as the arithmetic hypothesis that a successful escape must exploit.

## Boundaries

- **No lower bound on arithmetic-shell approximate degree.** Equations `(10)`–`(14)` apply to pointwise approximation on the full Boolean cube. They do not prove the same degree lower bound after restricting to the actual shell image.
- **No obstruction to overlapping signed identities.** Equation `(2)` is itself a low-degree exact overlapping identity. The obstruction concerns normalization/classification, not all witness use.
- **No obstruction to distributional approximation.** A polynomial may approximate `NB` much better on the actual empirical shell distribution than in worst-case norm; that requires arithmetic evidence not supplied here.
- **No claim that source degree alone measures analytic difficulty.** Degree is relevant because it is exactly lower-prime support depth in the existing source hierarchy.
- **No hidden independence model.** The only probabilistic-looking quantity is the classical worst-case approximation parameter `\varepsilon`; no random-sign law is imposed on the arithmetic vectors.
- **No Möbius or RH consequence.** Nothing here excludes blind support or improves `M(X)`.

## Consequence for the research line

The live `MC-273` witness idea now has a sharper normal form. The negative witnesses may be kept simultaneously at depth `m+1`, so `MC-274` should not be read as saying that every use of a witness requires deep conditioning. What is expensive is making the overlapping witness cover behave like a normalized indicator of nonblindness.

The next useful theorem should therefore target the **arithmetic restricted image** directly: either prove that the localized Legendre shell admits a much lower-degree or distributionally accurate nonblindness surrogate than the generic cube, or exploit the unnormalized signed identity `(2)` in a way that never divides by `b`. A construction that merely replaces the first-witness tree by a generic polynomial OR surrogate is now quantitatively ruled out at the support-matched scale.