# WI-047 — level of distribution leaves positive welding mass outside a sublattice AP repair

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** change Mathia's current unconditional simple-critical proportion and does not prove that the Yang--Yang one-sided fourth-moment route fails. It closes one specific escape left open by `WI-040`: after a non-unimodular split that turns the large coefficients `r,q` into arithmetic-progression moduli, a black-box prime-distribution theorem of fixed level `theta<1` cannot cover all of the dominant Yang continuum. For the classical Bombieri--Vinogradov level `theta=1/2`, only one half of the raw source-support Mertens mass lies where **both** prime pairs are individually within their local AP ranges; even under the deliberately optimistic rule that controlling **either** pair is enough, only `7/10` of that mass is reached and `3/10` remains outside.

More generally, on the actual continuum support selected by the Yang deterministic source, for `1/2<=theta<1` the exact raw-Mertens coverage fractions are

\[
\boxed{
 f_{\rm both}(\theta)
 =\frac{3(2\theta^2+3\theta-1)}{2(\theta+1)(2\theta+1)},
}
\tag{1}
\]

and

\[
\boxed{
 f_{\rm either}(\theta)
 =1-\frac{(1-\theta)(\theta+4)}{2(\theta+1)(\theta+2)}.
}
\tag{2}
\]

Thus every fixed `theta<1` leaves positive raw source-support mass outside even the optimistic one-sided interface. An explicit rational box around `beta_1=beta_2=2/5` has strictly positive four-leg source geometry and lies outside **both** AP ranges even at `theta=66/107`, the strongest currently located unconditional level in the much more restrictive triply-well-factorable setting. The obstruction is therefore not an artifact of integrating over cells on which the Yang overlap geometry vanishes.

The conclusion is deliberately narrower than “large-index sublattices cannot work.” A source-specific anisotropic dispersion theorem, a theorem for the coupled four-prime object rather than two separate AP problems, or genuinely stronger coefficient/modulus uniformity may bypass this barrier. What is ruled out is the cheap repair “split into residue classes and invoke a generic known level-of-distribution theorem.”

## 1. Source system and the non-unimodular escape left by WI-040

The public Yang--Yang source remains pinned at

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

The exact equal-lock swap audited in `WI-039`, `WI-040`, `WI-045`, and `WI-046` is

\[
 m'=m-rk,
 \qquad
 n'=n-qk,
 \qquad
 r=\frac{b_1}{(b_1,b_2)},
 \qquad
 q=\frac{b_2}{(b_1,b_2)}.
\tag{3}
\]

On the asymptotically dominant coprime prime-power family,

\[
 r=b_1,
 \qquad
 q=b_2.
\tag{4}
\]

`WI-040` proves that no unimodular change of the three summation variables can remove these power-sized coefficients. Its surviving non-unimodular escape was to pass to large-index sublattices. For example, writing

\[
 m=a+r u
\tag{5}
\]

turns the first pair into

\[
 a+ru,
 \qquad
 a+r(u-k),
\tag{6}
\]

so the coefficient `r` has disappeared from the shift but reappeared as the modulus of an arithmetic progression. The same operation on the second pair introduces modulus `q`.

The physical scales already isolated in `WI-040`/`WI-046` are

\[
 rK\asymp M_m,
 \qquad
 qK\asymp M_n,
\tag{7}
\]

and, in the continuum-dominant coprime large-base range,

\[
 M_m\asymp\frac{X}{b_2},
 \qquad
 M_n\asymp\frac{X}{b_1},
 \qquad
 K\asymp\frac{X}{b_1b_2}.
\tag{8}
\]

The auxiliary `m<=X` edge and the cells with only polylogarithmically many `k`-shifts have `o(1)` normalized Mertens mass by `WI-046`; they are not used to manufacture the obstruction below.

## 2. A generic level `theta` imposes exact cell inequalities

Write

\[
 b_1=X^\alpha,
 \qquad
 b_2=X^\beta,
 \qquad
 0\le\alpha,\beta\le1.
\tag{9}
\]

Suppose one has a black-box prime-in-arithmetic-progressions theorem whose generic modulus range at physical scale `Y` is

\[
 Q\le Y^{\theta-o(1)}.
\tag{10}
\]

This formulation includes Bombieri--Vinogradov with `theta=1/2` at the level of exponent bookkeeping. It is intentionally optimistic: an average-over-moduli theorem may impose further hypotheses, so (10) is only a **necessary support condition** for a cell to be reachable by the proposed split.

For the first pair, modulus `r=b_1=X^\alpha` must fit inside the theorem applied at scale

\[
 M_m\asymp X^{1-\beta}.
\]

Ignoring logarithmic margins, this requires

\[
\boxed{
 \alpha\le\theta(1-\beta)
}
\quad\Longleftrightarrow\quad
\boxed{
 \alpha+\theta\beta\le\theta.
}
\tag{11}
\]

Similarly, separate AP control of the second pair requires

\[
\boxed{
 \beta\le\theta(1-\alpha)
}
\quad\Longleftrightarrow\quad
\boxed{
 \theta\alpha+\beta\le\theta.
}
\tag{12}
\]

Call the regions cut out by (11) and (12) `R_m(theta)` and `R_n(theta)`.

Two natural interfaces now have exact meanings:

- a **two-sided AP repair** needs the cell in `R_m(theta) cap R_n(theta)`;
- an **optimistic hybrid** that assumes one AP-controlled pair could somehow be combined with a different theorem for the other pair needs only the cell in `R_m(theta) union R_n(theta)`.

The second criterion is deliberately generous. A failure even for that union is a genuine support barrier for every fixed-level black-box AP repair of this type.

## 3. Eliminate the Yang source parameter: the actual continuum support has area `1/3`

`WI-033` reconstructed the exact scaled source selector. With

\[
 t=-\frac{\log(\theta_{\rm geom}/2\pi)}{\log X},
\]

where `theta_geom` is the source's geometric integration variable rather than the distribution exponent in (10), a selected prime-power pair obeys

\[
 t\le\min(\alpha,\beta),
 \qquad
 \max(\alpha,\beta)\le\frac{1+t}{2}.
\tag{13}
\]

Eliminating `t` gives

\[
 2\alpha-\beta\le1,
 \qquad
 2\beta-\alpha\le1.
\tag{14}
\]

The nontrivial off-diagonal range from (8) is

\[
 \alpha+\beta\le1
\tag{15}
\]

up to the `o(1)` boundary strip already removed in `WI-046`. Hence the exact two-base continuum support relevant to this audit is the pentagon

\[
\mathcal S=
\left\{
\alpha,\beta\ge0:
\alpha+\beta\le1,
\ 2\alpha-\beta\le1,
\ 2\beta-\alpha\le1
\right\},
\tag{16}
\]

with vertices

\[
 (0,0),
 \left(\frac12,0\right),
 \left(\frac23,\frac13\right),
 \left(\frac13,\frac23\right),
 \left(0,\frac12\right).
\tag{17}
\]

A shoelace calculation gives

\[
\boxed{|\mathcal S|=\frac13.}
\tag{18}
\]

By `WI-033`, the normalized prime-power measure

\[
 \frac1{\log X}
 \sum_{p^a\le X}
 \frac{\log p}{p^a}
 \delta_{\log(p^a)/\log X}
\tag{19}
\]

converges quantitatively to Lebesgue measure on `[0,1]`. Thus ordinary planar area in (16) is exactly the limiting **raw two-base Mertens mass** relevant here. This statement concerns support mass, not the final signed/weighted Yang remainder.

## 4. Exact coverage law on the source support

Assume

\[
 \frac12\le\theta<1.
\tag{20}
\]

### Both AP sides

Inside `mathcal S`, the polygon satisfying both (11) and (12) has vertices

\[
 (0,0),
 \left(0,\frac12\right),
 \left(\frac{2\theta-1}{2\theta+1},\frac{2\theta}{2\theta+1}\right),
 \left(\frac{\theta}{1+\theta},\frac{\theta}{1+\theta}\right),
 \left(\frac{2\theta}{2\theta+1},\frac{2\theta-1}{2\theta+1}\right),
 \left(\frac12,0\right).
\tag{21}
\]

Its exact area is

\[
 |\mathcal S\cap R_m(\theta)\cap R_n(\theta)|
 =
 \frac{2\theta^2+3\theta-1}
 {2(\theta+1)(2\theta+1)}.
\tag{22}
\]

Dividing by (18) gives (1).

### Either AP side

For the optimistic union, it is cleaner to compute the missed polygon. The complement of `R_m(theta) union R_n(theta)` inside `mathcal S` has vertices

\[
 \left(\frac13,\frac23\right),
 \left(\frac23,\frac13\right),
 \left(\frac{1+\theta}{2+\theta},\frac{\theta}{2+\theta}\right),
 \left(\frac{\theta}{1+\theta},\frac{\theta}{1+\theta}\right),
 \left(\frac{\theta}{2+\theta},\frac{1+\theta}{2+\theta}\right).
\tag{23}
\]

Its area is

\[
 |\mathcal S\setminus(R_m(\theta)\cup R_n(\theta))|
 =
 \boxed{
 \frac{(1-\theta)(\theta+4)}
 {6(\theta+1)(\theta+2)}
 }.
\tag{24}
\]

After division by `|mathcal S|=1/3`, the uncovered raw-Mertens fraction is

\[
\boxed{
 u_{\rm either}(\theta)
 =\frac{(1-\theta)(\theta+4)}
 {2(\theta+1)(\theta+2)}.
}
\tag{25}
\]

Equation (2) is `1-u_either(theta)`.

The important qualitative consequence is immediate:

\[
\boxed{
 \theta<1
 \quad\Longrightarrow\quad
 u_{\rm either}(\theta)>0.
}
\tag{26}
\]

Therefore no fixed generic level strictly below one covers all but `o(1)` of the raw source-support Mertens mass through this separate-AP sublattice interface. The obstruction disappears only in the limiting `theta -> 1` regime associated with Elliott--Halberstam strength, or if a theorem uses structure not represented by (11)--(12).

## 5. Classical Bombieri--Vinogradov leaves `30%` even under the optimistic interface

At the unconditional generic level

\[
 \theta=\frac12,
\tag{27}
\]

(1) and (2) give

\[
\boxed{
 f_{\rm both}(1/2)=\frac12,
 \qquad
 f_{\rm either}(1/2)=\frac7{10},
 \qquad
 u_{\rm either}(1/2)=\frac3{10}.
}
\tag{28}
\]

Thus a direct two-sided Bombieri--Vinogradov split can even meet the **necessary modulus-size condition** on only half of the raw source-support Mertens mass. If one grants the strongest optimistic hybrid interpretation -- that having just one of the two pairs in Bombieri--Vinogradov range is somehow sufficient -- a positive `30%` remains where neither pair is in range.

This is stronger than the ambient-triangle estimate one obtains from `alpha+beta<=1` alone. The exact Yang selector was used in (16)--(28), so the obstruction survives after restricting to the source's actual continuum support.

## 6. The missed region contains an explicit positive-geometry source box

A support-area obstruction would be weak if the source overlap vanished identically there. It does not.

Consider the rational box

\[
 \boxed{
 \frac{39}{100}\le\alpha,\beta\le\frac{41}{100},
 \qquad
 \frac{19}{100}\le t\le\frac{21}{100}.
 }
\tag{29}
\]

It lies strictly inside the selected off-diagonal source region because

\[
 t\le\frac{21}{100}<\frac{39}{100}\le\min(\alpha,\beta),
\]

\[
 \max(\alpha,\beta)\le\frac{41}{100}
 <\frac{1+19/100}{2},
\]

and

\[
 \alpha+\beta\le\frac{82}{100}<1.
\tag{30}
\]

Use the exact scaled `qvec/o4_triple` geometry from pinned `scripts/m1_suite.py`. Its four leg values are `beta_i` and

\[
 1-t-\beta_i,
\]

so throughout (29) every leg lies in

\[
 \left[\frac{38}{100},\frac{42}{100}\right].
\tag{31}
\]

For each of the four leg orderings, the first `o4` summand has arguments

\[
 u_3-u_2-u_4,
 \qquad
 u_3-u_4,
 \qquad
 -u_4.
\tag{32}
\]

From (31), these lie respectively in

\[
 \left[-\frac{46}{100},-\frac{34}{100}\right],
 \quad
 \left[-\frac4{100},\frac4{100}\right],
 \quad
 \left[-\frac{42}{100},-\frac{38}{100}\right].
\tag{33}
\]

Including the zero endpoint in the overlap definition, their total span is therefore at most `1/2`, so each of those four `o4` terms is at least `1/2`. Consequently the exact source geometry satisfies

\[
\boxed{
 Q_{\rm sym}(\alpha,\beta,t)\ge2
}
\tag{34}
\]

throughout the whole box.

Now compare with the strongest unconditional beyond-square-root level located in the prior-art audit, Lichtman's

\[
 \theta=\frac{66}{107},
\tag{35}
\]

which is **not** a generic theorem but a triply-well-factorable weighted result. Even if one counterfactually granted (35) as a generic black-box level, every point of (29) still fails both necessary AP conditions. Indeed the largest possible right side of the first inequality is

\[
 \frac{66}{107}\left(1-\frac{39}{100}\right)
 =\frac{4026}{10700}
 <\frac{4173}{10700}
 =\frac{39}{100}
 \le\alpha,
\tag{36}
\]

and the second side is symmetric.

So the gap in (25) contains a rational open box with strictly positive Yang overlap geometry. It is not merely area carried by source cells of zero geometric weight.

## 7. Prior-art audit: why known beyond-square-root theorems are not drop-ins

The classical generic reference is Enrico Bombieri, **On the large sieve**, *Mathematika* 12 (1965), 201--225, DOI `10.1112/S0025579300005313`, together with A. I. Vinogradov's independent 1965 density-method work. In modern level-of-distribution notation, Bombieri--Vinogradov gives the prime discrepancy averaged over moduli up to

\[
 x^{1/2}(\log x)^{-B},
\]

that is, every fixed exponent strictly below `1/2`. Elliott--Halberstam conjectures the corresponding range for every fixed exponent below one.

Modern work crosses the square-root barrier only with additional structure. In particular:

- James Maynard, **Primes in arithmetic progressions to large moduli II: Well-factorable estimates**, *Memoirs AMS* 306 (2025), no. 1543, proves level `3/5-epsilon` when the modulus sum is equipped with suitably well-factorable weights;
- Maynard's companion **III: Uniform residue classes** proves ranges beyond `1/2` for moduli having conveniently sized divisors;
- Jared Duker Lichtman, **Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root barrier**, arXiv:2309.08522, proves level `66/107` with **triply well-factorable** weights.

These hypotheses do not disappear in the Yang source. In fact the normalized prime-power base measure is asymptotically carried by genuine primes: higher powers contribute only

\[
 \frac1{\log X}
 \sum_{a\ge2}\sum_{p^a\le X}\frac{\log p}{p^a}
 \le
 \frac1{\log X}
 \sum_p\frac{\log p}{p(p-1)}
 =o(1).
\tag{37}
\]

Thus the dominant sublattice moduli `r,q` are themselves prime, not generic smoothly factorable composites.

There is also an elementary incompatibility with treating a well-factorable weighted theorem as a pointwise theorem for those prime moduli. If `lambda_q` is well-factorable of level `Q` and one chooses the defining factorization `Q=Q^{1/2}Q^{1/2}`, then for a prime `q` in the top dyadic range `q>Q^{1/2}` the convolution representation

\[
 \lambda=\gamma_1*\gamma_2,
 \qquad
 \operatorname{supp}\gamma_i\subset[1,Q^{1/2}],
\]

forces `lambda_q=0`: the only factorizations of a prime are `1*q` and `q*1`, and neither fits both support bounds. Triply well-factorable weights have the analogous obstruction after splitting `Q` into three comparable factors. This is exactly why the quoted beyond-square-root results cannot simply be substituted for the generic `theta` in (10) on the prime-modulus Yang family.

For perspective only, even if the restricted value `66/107` were incorrectly treated as generic, (1)--(2) would still give

\[
 f_{\rm both}\left(\frac{66}{107}\right)
 =\frac{55347}{82694}
 =0.6692988608\ldots,
\tag{38}
\]

and

\[
 f_{\rm either}\left(\frac{66}{107}\right)
 =\frac{38313}{48440}
 =0.7909372419\ldots,
\tag{39}
\]

leaving

\[
 \frac{10127}{48440}
 =0.2090627580\ldots
\tag{40}
\]

of the raw source-support Mertens mass outside even the optimistic interface.

Primary/authoritative anchors checked for this finding:

- Bombieri 1965: https://doi.org/10.1112/S0025579300005313
- Maynard II, published version / bibliographic record: https://doi.org/10.1090/memo/1543
- Maynard III: https://arxiv.org/abs/2006.08250
- Lichtman: https://arxiv.org/abs/2309.08522
- pinned Yang source: https://github.com/JoshuaHKU/zeta-0.7947-reproduction/tree/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8

No prior source located states the Yang-specific coverage laws (1)--(2). No priority claim is made: the new content recorded here is the exact application of classical level-of-distribution bookkeeping to the source scales and Mertens geometry already established in `WI-033`, `WI-040`, and `WI-046`.

## 8. Boundary conditions and falsification controls

This finding must **not** be read as a theorem that every large-index sublattice method fails.

1. Equations (11)--(12) are necessary exponent-range conditions for a scheme that reduces the two prime pairs to separate prime-in-AP problems. They are not sufficient: Bombieri--Vinogradov is an average-over-moduli theorem, and the Yang weight/residue dependence still has to match its hypotheses even inside the accessible polygons.
2. Fractions (1)--(2) are fractions of the **raw two-base Mertens support measure** on `mathcal S`. They are not fractions of the signed fourth-moment remainder and must not be inserted into the final `R(1)` ledger as though the source geometry were constant.
3. The explicit box (29)--(34) only proves that the missed set contains an open region with nonzero Yang geometric weight. It does not quantify the final signed contribution of that region after every arithmetic and oscillatory factor is restored.
4. Beyond-square-root theorems with well-factorable weights, convenient divisors, fixed residues, smooth moduli, or other special hypotheses must be checked against the actual Yang base/modulus family before use. Their nominal exponent alone is not evidence that (10) holds generically.
5. An anisotropic theorem for the coupled four-form average, a direct dispersion estimate using the `k`-average, a source-specific theorem uniform in prime moduli, or another argument that does not split the problem into (11) and (12) is outside the obstruction.
6. If the physical ranges in (8) are altered on a non-negligible source cell by an overlooked source cap, recompute the polygons. `WI-046` already isolates the known cap/boundary exceptions as `o(1)` in the normalization used here.

The most direct independent audit is finite and exact: eliminate `t` from (13), recover pentagon (16); intersect it with the two half-planes (11)--(12); verify the polygon vertices (21), (23) and shoelace areas (22), (24); then evaluate the rational box bounds (29)--(36) directly from the pinned `qvec/o4_triple` definitions.

## 9. Consequence for `weil_inertia`

`WI-040` left a controlled large-index sublattice decomposition as a plausible escape from the coefficient wall. This finding sharply narrows that escape:

\[
\boxed{
\text{non-unimodular split}
+\text{generic fixed level }\theta<1
\not\Rightarrow
\text{coverage of the full dominant Yang source support}.
}
\tag{41}
\]

At the actual unconditional generic level `1/2`, a positive `30%` of raw source-support Mertens mass lies outside even the optimistic “either side is enough” region, and that missed set contains explicit cells with uniformly positive source geometry. Known unconditional improvements past `1/2` are structurally restricted and are not drop-in substitutes; even their best nominal exponent located here would still leave positive support mass if granted generically.

The useful redirect is therefore away from a cheap Bombieri--Vinogradov repair of `WI-040`. The promising remaining interfaces are the ones already exposed by `WI-044`--`WI-046`: exploit the exact `S1-2S2+S3` centering, the finite local collision identity, and the `k`-interval transport to obtain a **source-specific coupled dispersion/covariance estimate**. Alternatively, a separate-AP strategy needs distribution strength tending to level one on the relevant prime-modulus family, which is qualitatively Elliott--Halberstam territory rather than an application of currently available generic input.