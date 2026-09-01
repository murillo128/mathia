# WI-070 — aggregating the Yang base family crosses the multivariate polynomial-pattern gap

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes one attractive black-box escape left open by WI-069: promoting the varying reduced bases to summation variables does remove the power-sized coefficients from the *definition* of the polynomial system, but the resulting source average is a genuinely multivariate polynomial prime-pattern problem. The strongest directly relevant 2026 quantitative theorem of Matthiesen--Teräväinen--Wang is explicitly one-parameter on the polynomial side; its authors state that a multivariate extension would require an extension of their generalized von Neumann input that they do not prove. The actual Yang ledger also carries prime/Mertens weights on the promoted base variables and highly anisotropic ranges, so even that advertised multivariate extension would need an additional source-faithful weighted/rectangular interface.

The durable conclusion is narrow but useful:

\[
\boxed{
\text{aggregate the changing Yang slopes first}
\not\stackrel{\text{MTW 2026 black box}}{\Longrightarrow}
\text{a quantitative four-prime asymptotic}.}
\]

This does **not** rule out proving the needed multivariate/anisotropic theorem, adapting the MTW/Peluse machinery, or exploiting a more special identity of the Yang source. It identifies exactly which theorem boundary the aggregation strategy crosses.

## 1. Exact source reduction after the bases are promoted

WI-069 reconstructs the coprime reduced-base cell of the pinned Yang source as

\[
(m,\ m-rk,\ n,\ n-qk),
\tag{1}
\]

with source shift lock

\[
(h_1,h_2)=(rk,qk),
\tag{2}
\]

and long-range scale

\[
K\asymp \frac{Y}{\max(r,q)}.
\tag{3}
\]

Cellwise, keeping `r,q` fixed leaves the power-coefficient wall of WI-039--WI-040; freeing `h_1,h_2` instead produces the power-index slope selector of WI-069. The remaining natural thought is to sum over the changing base family **before** invoking a prime-pattern theorem, so that `r,q` themselves become theorem variables rather than coefficients.

That algebra is exact. Put

\[
d:=n-m.
\tag{4}
\]

Then the four inner von-Mangoldt factors in (1) become the common-base polynomial progression

\[
\boxed{
 m+P_1(\mathbf y),\quad
 m+P_2(\mathbf y),\quad
 m+P_3(\mathbf y),\quad
 m+P_4(\mathbf y),
}
\tag{5}
\]

with parameter vector

\[
\mathbf y=(r,q,k,d)
\tag{6}
\]

and fixed integer polynomials

\[
\boxed{
P_1=0,\qquad
P_2=-rk,\qquad
P_3=d,\qquad
P_4=d-qk.
}
\tag{7}
\]

The coefficient size in (7) is now literally `1`; the former large coefficients `r,q` have become variables. Thus aggregating slopes is not merely a vague averaging idea: it converts the cellwise linear-form problem into a fixed-coefficient **multivariate degree-two polynomial progression**.

The same reduction also shows why this is not covered by the earlier fixed-coefficient linear theory. If `r,q` are held fixed, (7) is linear in `(k,d)` but has coefficients `r,q`, returning to WI-039--WI-040. If they are varied, the terms `rk` and `qk` are bilinear, so the system is no longer affine-linear in the full source variables.

## 2. The obvious 2026 quantitative theorem stops exactly here

The closest current theorem is Lilian Matthiesen, Joni Teräväinen and Mengdi Wang, **Quantitative asymptotics for polynomial patterns in the primes**, *Mathematika* 72 (2026), e70103, DOI `10.1112/mtk.70103`, first published 12 May 2026.

Their Theorem 1.1 gives arbitrary-power logarithmic savings for averages of

\[
\Lambda(n+P_1(m))\cdots\Lambda(n+P_t(m))
\tag{8}
\]

for a fixed collection of **one-variable** integer polynomials `P_i in Z[m]` satisfying the paper's degree/leading-coefficient hypotheses. The theorem is quantitative enough that, if its interface matched (7), it would be an exceptionally attractive way around the power-coefficient wall.

But the paper itself records the missing interface immediately after Theorem 1.1:

> the Tao--Ziegler result also works for multivariate polynomials, and if Proposition 3.1 could be extended to multivariate polynomials, it seems likely that Theorem 1.1 could also be extended to them.

This is a theorem-boundary statement by the authors, not an inference from absence of a search hit. Proposition 3.1 is the quantitative generalized von Neumann input used in their proof and is stated for one-variable polynomials. The multivariate quantitative extension needed for (7) is therefore **not part of the printed MTW theorem**.

The exact mismatch is

\[
\boxed{
\text{MTW 2026: } P_i=P_i(m)
\qquad\text{versus}\qquad
\text{Yang aggregate: }P_i=P_i(r,q,k,d).
}
\tag{9}
\]

No choice of one scalar polynomial parameter can represent the independent source variables `r,q,k,d` while preserving their source average. Fixing `r,q` to recover a one-dimensional parameter immediately restores the large coefficients that the aggregation was meant to remove.

## 3. The qualitative Tao--Ziegler antecedent is not the missing quantitative consumer

MTW explicitly notes that the earlier Tao--Ziegler polynomial-prime machinery has a multivariate extension at the qualitative level. That does not make the present splice automatic.

First, the Yang argument is not asking only for existence of prime configurations. It needs a source-normalized asymptotic/error estimate strong enough to survive summation over dyadic base cells, Mertens weights, moving strips, local-main subtraction, and the final fourth-moment remainder budget. The entire appeal of MTW is its arbitrary fixed power of logarithmic saving; the paper does not supply that quantitative saving for the multivariate system (7).

Second, the source ranges are intrinsically anisotropic. On a dyadic cell

\[
r\asymp R,\qquad q\asymp Q,
\qquad K\asymp \frac{Y}{\max(R,Q)},
\qquad |d|\asymp Y,
\tag{10}
\]

the parameter box has volume on the order of

\[
RQKY
\asymp
Y^2\min(R,Q).
\tag{11}
\]

Embedding this box into a common four-dimensional box of side `Y` has relative density

\[
\boxed{
\asymp \frac{\min(R,Q)}{Y^2}\le \frac1Y.
}
\tag{12}
\]

Thus an ambient estimate with only logarithmic *relative* error on a full `Y^4` parameter box cannot be localized to (10) by a trivial cutoff: the desired source box is power-sparse in that embedding. A useful extension must be normalized to the anisotropic rectangle (or provide a quantitatively equivalent weighted form), not merely state a multivariate full-box asymptotic.

Equation (12) is not a claim about the optimal formulation of a future multivariate theorem. It is the exact reason that one cannot repair the mismatch by padding the shorter source variables to the largest scale and absorbing the difference with the arbitrary logarithmic saving.

## 4. Promoting the bases also promotes their arithmetic weights

There is a second source-level gate even after the inner four-prime system (7) is recognized. The Yang base ledger is not an unweighted integer average over `r,q`. In the dominant coprime prime/prime-power sector it carries the Mertens-type base factors inherited from

\[
\frac{\Lambda(b_1)}{b_1}\frac{\Lambda(b_2)}{b_2},
\tag{13}
\]

with the reduced bases `r,q` obtained from `b_1,b_2` after their gcd booking. Prime-power corrections are lower-order in several earlier source decompositions, but the dominant promoted variables are still prime-weighted rather than arbitrary uniform integer parameters.

There are two conceptually different ways a future theorem might absorb this.

1. Prove a multivariate polynomial-progression estimate for the four inner factors (7) **uniformly enough** over rectangular `(r,q,k,d)` domains that partial summation and the outer prime/Mertens measure can be performed afterwards.
2. Promote the base primality into the pattern itself, producing a six-von-Mangoldt polynomial system containing the forms `r`, `q`, `m`, `m-rk`, `n`, `n-qk` and prove a quantitative asymptotic for that general multivariate polynomial system.

Neither is the printed MTW Theorem 1.1. In particular, its useful extra-weight version of the generalized von Neumann argument does not by itself turn the two unbounded prime weights `Lambda(r),Lambda(q)` on independent polynomial parameters into a theorem for the Yang ledger.

Therefore the exact aggregation move does not simply trade the WI-069 slope selector for an already-solved polynomial-pattern theorem; it trades it for a more specific **multivariate, anisotropic and source-weighted polynomial-prime problem**.

## 5. Why this is a real redirection rather than another coefficient restatement

WI-039--WI-040 say that the source-faithful three-variable linear system cannot remove the power coefficients by a lattice-preserving reparameterization. WI-069 says that introducing two independent physical shifts removes those coefficients only by placing the source on a power-index slope slice.

The present calculation identifies a third representation:

\[
\boxed{
\begin{array}{ccl}
\text{fixed }(r,q) &:& \text{linear forms with large coefficients},\\
\text{free }(h_1,h_2) &:& \text{fixed coefficients + thin slope selector},\\
\text{free }(r,q) &:& \text{fixed-coefficient multivariate degree-2 polynomials}.
\end{array}}
\tag{14}
\]

The third representation is genuinely different. It may be the right route if the required multivariate theorem can be proved. What the prior-art audit establishes is that **the most obvious recent quantitative polynomial-pattern citation stops precisely at the transition from the first line to the third**.

This also changes the productive theorem-search target. Searching for ever stronger bounded-coefficient *linear*-forms theorems or ordinary one-parameter polynomial progressions will not consume (7). The missing established interface is closer to

\[
\boxed{
\text{quantitative multivariate polynomial von-Mangoldt averages}
+
\text{anisotropic box uniformity}
+
\text{source-compatible prime/Mertens parameter weights}.}
\tag{15}
\]

A source-specific argument may need less than the full generality of (15), but it must address all the structure actually used in (7), (10), and (13).

## 6. Prior-art audit

No novelty is claimed for polynomial progressions in the primes, generalized von Neumann inequalities, Gowers-uniformity transference, the qualitative Tao--Ziegler polynomial-prime theorem, multivariate polynomial systems, dyadic decomposition, or the observation that a bilinear expression becomes fixed-coefficient when both factors are promoted to variables.

The load-bearing recent primary source is:

- Lilian Matthiesen, Joni Teräväinen and Mengdi Wang, **Quantitative asymptotics for polynomial patterns in the primes**, *Mathematika* 72 (2026), e70103, DOI `10.1112/mtk.70103`. Theorem 1.1 is the arbitrary-log-saving one-parameter polynomial-prime asymptotic; the remark immediately following it explicitly marks extension of Proposition 3.1 to multivariate polynomials as a missing step toward a multivariate quantitative theorem.

The relevant qualitative antecedent is:

- Terence Tao and Tamar Ziegler, **Polynomial patterns in the primes**, *Forum of Mathematics, Pi* 6 (2018), e1, DOI `10.1017/fmp.2017.3`. Its published theorem gives qualitative/asymptotic polynomial-prime patterns in the one-parameter presentation and is the antecedent explicitly cited by MTW when discussing multivariate extensions; it does not supply the 2026 arbitrary-log-saving multivariate consumer needed here.

A targeted search through current quantitative polynomial-prime, multidimensional-prime-pattern, nilsequence/Gowers, and prime-values-of-polynomials literature did not locate a theorem whose printed interface simultaneously provides (15) for the Yang source family. That bounded negative search is **not** used as an impossibility or priority claim. The decisive-negative claim is only against the black-box use of MTW 2026 (or a trivial full-box padding of it), whose mismatch is explicit in the source and in equations (9)--(13).

## 7. Falsification / narrowing gate

Narrow or retire this finding if any of the following is established.

1. A theorem already in the literature is located whose printed hypotheses give a quantitative asymptotic for the fixed polynomial family (7) over the anisotropic ranges (10), with a source-normalized error strong enough for the Yang Mertens aggregation.
2. The MTW generalized von Neumann input is extended to the required multivariate polynomial family and the resulting constants/ranges are shown to survive (10)--(13).
3. An exact Yang regrouping removes the need to average independently over all four parameters `(r,q,k,d)` and reduces the source to a one-parameter polynomial progression without restoring power-sized coefficients.
4. A source identity or orthogonality argument absorbs the `Lambda(r)Lambda(q)/(rq)` base weights before the polynomial theorem is applied and leaves a theorem surface already covered by an established result.
5. A different quantitative prime-pattern theorem directly treats the six-form promoted-base system and its source domains.

Conversely, citing MTW Theorem 1.1 without supplying a multivariate extension cannot pass the gate because the authors themselves distinguish exactly that extension from their proved theorem.

## 8. Consequence for `weil_inertia`

The global-base aggregation escape from WI-069 remains alive **as a research program**, but its next step is no longer “apply the new quantitative polynomial-pattern theorem.” The precise obligation is now to prove or locate a source-faithful theorem at (15), or find a Yang-specific simplification that avoids it.

The current arithmetic frontier can therefore be summarized as

\[
\boxed{
\text{cellwise linear route: coefficient wall}
\quad\longrightarrow\quad
\text{free-shift route: slope-slice wall}
\quad\longrightarrow\quad
\text{base-aggregated route: multivariate polynomial-pattern gap}.}
\tag{16}
\]

This is a decisive closure of a cheap prior-art shortcut, not a no-go theorem for the base-aggregated Yang strategy itself.