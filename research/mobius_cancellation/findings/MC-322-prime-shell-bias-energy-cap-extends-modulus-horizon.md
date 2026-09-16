# MC-322 — Prime-shell bias energy is bounded below the cubic modulus horizon

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The prime Halász–Montgomery estimate used in `MC-321` is stronger than the `q\le y^{8/3-\delta}` fixed-bias family obstruction recorded there. Using the allowed choice `k=3` rather than `k=2` gives an almost-cubic modulus horizon and, more importantly, a quantitative **total shell-bias energy bound**.

Fix `0<\delta<3`. Let

\[
\mathcal A_y\subset\{p:y<p\le2y,\ p\text{ prime}\},
\qquad
|\mathcal A_y|\asymp \frac{y}{\log y},
\tag{1}
\]

let `q\le y^{3-\delta}`, and let `\Xi` be a set of `m` distinct Dirichlet characters modulo `q`. Define the normalized prime-shell bias

\[
\beta_\chi
:=
\frac{1}{|\mathcal A_y|}
\left|\sum_{p\in\mathcal A_y}\chi(p)\right|,
\qquad
E(\Xi):=\sum_{\chi\in\Xi}\beta_\chi^2.
\tag{2}
\]

Then the classical prime Halász–Montgomery estimate of Puchta, in the form of Lemma 12.4 of Klurman–Mangerel–Teräväinen (`MC-S45`), gives the quantitative bound

\[
\boxed{
E(\Xi)
\ll_\delta
1+m\,y^{-\delta/24}\log y.
}
\tag{3}
\]

Consequently, for every family with `m=y^{o(1)}`,

\[
\boxed{E(\Xi)=O_\delta(1).}
\tag{4}
\]

In particular, a growing number of distinct characters cannot each carry a fixed nonzero bias on the same dense dyadic prime shell anywhere in the modulus range `q\le y^{3-\delta}`. More quantitatively, if

\[
\mathcal B_\tau
=
\{\chi\pmod q:\beta_\chi\ge\tau\},
\tag{5}
\]

and

\[
\tau^2\gg_\delta y^{-\delta/24}\log y,
\tag{6}
\]

then

\[
|\mathcal B_\tau|\ll_\delta \tau^{-2}.
\tag{7}
\]

Thus the actual obstruction supplied by the classical theorem is an `\ell^2` budget on simultaneous prime-shell character bias, not merely the fixed-bias/all-directions special case used in `MC-321`.

For the reciprocal-endpoint program this materially shrinks the surviving escape surface. Enlarging the common modulus from `y^{8/3+o(1)}` to any fixed power strictly below `y^3` does **not** escape the same prime-family obstruction, provided the endpoint still exposes sufficiently many distinct characters with non-negligible total squared shell bias.

No estimate for `M(x)` follows.

## 1. Start from the `k=3` prime Halász–Montgomery inequality

Lemma 12.4 of Klurman–Mangerel–Teräväinen states that for a set `\Xi` of characters modulo one integer `q`, `k\in\{2,3\}`, `\eta>0`, `2\le B<\sqrt N`, and arbitrary complex prime coefficients `a_p`,

\[
\sum_{\chi\in\Xi}
\left|\sum_{p\le N}a_p\chi(p)\right|^2
\ll_{k,\eta}
\left(
\frac{N}{\log B}
+N^{1-1/k}q^{(k+1)/(4k^2)+\eta}|\Xi|B^{2/k}
\right)
\sum_{p\le N}|a_p|^2.
\tag{8}
\]

`MC-321` specialized `(8)` with `k=2`. Instead take

\[
k=3,
\qquad
N=2y,
\qquad
a_p=\mathbf 1_{\{p\in\mathcal A_y\}}.
\tag{9}
\]

Then `(8)` becomes

\[
\sum_{\chi\in\Xi}
\left|\sum_{p\in\mathcal A_y}\chi(p)\right|^2
\ll_{\eta}
\left(
\frac{y}{\log B}
+y^{2/3}q^{1/9+\eta}mB^{2/3}
\right)|\mathcal A_y|.
\tag{10}
\]

After division by `|\mathcal A_y|^2` and use of `(1)`,

\[
E(\Xi)
\ll
\frac{\log y}{\log B}
+y^{-1/3}q^{1/9+\eta}mB^{2/3}\log y.
\tag{11}
\]

This is already the desired bias-energy inequality before parameter optimization.

## 2. The cubic threshold follows from one fixed power choice of `B`

Choose

\[
\eta:=\frac{\delta}{36(3-\delta)},
\qquad
B:=y^{\delta/16}.
\tag{12}
\]

For fixed `0<\delta<3`, eventually `2\le B<\sqrt{2y}`. Moreover,

\[
(3-\delta)\left(\frac19+\eta\right)
=
\frac13-\frac{\delta}{12}.
\tag{13}
\]

Hence `q\le y^{3-\delta}` implies

\[
q^{1/9+\eta}
\le
y^{1/3-\delta/12}.
\tag{14}
\]

The first term of `(11)` is now `O_\delta(1)`. For the second term,

\[
y^{-1/3}q^{1/9+\eta}B^{2/3}
\le
y^{-\delta/12}y^{\delta/24}
=
y^{-\delta/24}.
\tag{15}
\]

Substitution into `(11)` proves `(3)`. If `m=y^{o(1)}`, then the second term in `(3)` tends to zero, giving `(4)`.

The exponent `3` is not mysterious: with `k=3`, the off-diagonal factor in `(8)` is `N^{2/3}q^{1/9+\eta}`. After normalizing by the density `|\mathcal A_y|\asymp y/\log y`, the power balance is `y^{-1/3}q^{1/9}`, whose neutral line is `q\asymp y^3`.

## 3. Large-bias characters satisfy a counting law

Apply `(3)` to any finite subset `\Xi\subset\mathcal B_\tau` of size `m`. Since every member has `\beta_\chi\ge\tau`,

\[
m\tau^2
\le E(\Xi)
\ll_\delta
1+m y^{-\delta/24}\log y.
\tag{16}
\]

When `(6)` holds with a sufficiently large implied constant, the second term on the right can be absorbed into the left, yielding

\[
m\ll_\delta \tau^{-2}.
\tag{17}
\]

Because this applies to every finite subset of `\mathcal B_\tau`, `(7)` follows. In particular, for fixed `\tau>0`, only `O_{\delta,\tau}(1)` distinct characters modulo `q` can have `\tau`-sized bias on the same shell once `q\le y^{3-\delta}`.

This formulation is strictly more useful for endpoint variants than the hypothesis that **every** one of `R` directions has the same fixed bias. Uneven defect patterns are also ruled out whenever their normalized squared biases have unbounded total energy.

## 4. Relation to `MC-321`

`MC-321` chose `k=2`, for which the normalized off-diagonal power is

\[
y^{-1/2}q^{3/16+\eta},
\tag{18}
\]

and therefore recorded the subcritical modulus range `q\le y^{8/3-\delta}`. That choice was already more than sufficient for the natural endpoint because its common modulus satisfies `q\le4y^2`.

The same cited lemma explicitly permits `k=3`. Klurman–Mangerel–Teräväinen themselves use the `k=3` form later in their proof, obtaining the term

\[
N^{2/3}q^{1/9}|\Xi|B^{2/3},
\tag{19}
\]

and note that the prime character sums must be long compared with `q^{1/3+\varepsilon}`. Thus the improvement from the `8/3` horizon to the `3` horizon is not a new analytic estimate; it is the sharper specialization of the same classical theorem that `MC-321` had not yet exploited.

The natural reciprocal endpoint remains impossible for the original simpler reason `q\le4y^2`. The new information concerns **nearby escape variants**: a common modulus of size, for example, `y^{2.9}` still lies inside the classical prime-family energy barrier and cannot by itself rescue a construction carrying growing fixed shell-bias energy.

## Prior art and novelty boundary

The analytic input is entirely classical prior art. Equation `(8)` is Lemma 12.4 of Oleksiy Klurman, Alexander P. Mangerel and Joni Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. London Math. Soc. 127 (2023), 366–446, DOI `10.1112/plms.12546`, arXiv `1909.12280`, retained as `MC-S45`; that lemma is attributed there to J.-C. Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), Theorem 3.

The primary-source audit also shows that KMT explicitly apply Lemma 12.4 with `k=3` in Section 12, where the relevant term is `N^(2/3) q^(1/9) |Xi| R^(2/3)` and the accompanying note identifies the `q^(1/3+epsilon)` prime-sum length scale. Therefore no novelty is claimed for the cubic power balance or for the mean-square inequality.

The durable line-specific contribution is the exact corollary `(3)`–`(7)` and its interpretation for the reciprocal endpoint frontier: the classical theorem supplies a bounded `\ell^2` budget for simultaneous normalized shell biases and leaves a fixed-power modulus escape only at the cubic boundary or beyond.

## Boundaries and falsification tests

- **Dense prime support is load-bearing.** The normalization uses `|\mathcal A_y|\asymp y/\log y`. Sparser prime sets change the balance and are not covered by `(3)` as stated.
- **One common modulus is load-bearing.** Lemma 12.4 sums a set of characters modulo the same `q`. Families whose relevant characters genuinely cannot be embedded into one controlled common modulus require a different inequality.
- **The cubic boundary is not crossed.** The argument needs a fixed power saving `q\le y^{3-\delta}`. It does not rule out `q=y^{3-o(1)}` or larger moduli without a sharper treatment of the auxiliary parameter and family size.
- **Bias energy, not family cardinality, is decisive.** A huge family of characters with individually vanishing shell biases can have bounded total energy and is not excluded merely because the family is large.
- **Distinctness is essential.** Repetition of one character cannot manufacture energy because `\Xi` is a set.
- **Prime localization is essential.** The estimate is for prime-supported coefficients; no inference from ordinary integer-interval cancellation is being made.
- **No primitivity, smoothness, or zero-free region is used.** Those structures may matter for other branches but not for `(3)`.
- **No RH or Mertens bound follows.** This remains a structural no-go for a reciprocal-endpoint mechanism, not progress on the global exponent of `M(x)` itself.

## Consequence for the research line

The `MC-321` conclusion should be read with a sharper frontier: the common-modulus escape is not available immediately above `y^{8/3}`. The same prime Halász–Montgomery mechanism continues to impose a bounded total bias-energy budget throughout every fixed-power range `q\le y^{3-\delta}`.

A surviving reciprocal-endpoint variant must therefore do at least one of the following before this branch deserves further analytic work: approach or exceed the cubic common-modulus scale, lose the common-modulus embedding, make the relevant character biases collectively `\ell^2`-small, or abandon dense dyadic prime-shell localization. Simply redistributing a fixed amount of endpoint defect unevenly among many characters does not evade the obstruction.