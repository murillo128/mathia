# WI-055 — Zheng's simultaneous-AP theorems do not black-box close the Yang locked covariance

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** change Mathia's current unconditional simple-critical proportion and does not disprove the Yang--Yang one-sided fourth-moment route. It audits the closest recent dedicated two-modulus prime-distribution theorem located for the power-coefficient welding problem. Zongkun Zheng's 2025 preprint proves genuine mean-value theorems for primes in two simultaneous arithmetic progressions, including a related quadrilinear form, but its printed hypotheses do not match the Yang locked pair--pair covariance.

There are three independent black-box mismatches. First, Zheng controls one prime `p` (or one product `mn`) carrying **both** congruence conditions, whereas the Yang source contains four additive prime forms `(m,m-rk,n,n-qk)` coupled through the common shift `k`. Second, Zheng requires one residue `a1` to satisfy `|a1| <= log^B x`, whereas the source-faithful Yang localization averages over all residue classes modulo the power-sized coefficients. Third, one of Zheng's modulus weights must be well-factorable. The dominant Yang coefficient ledger is instead prime-modulus Mertens mass on both sides. An elementary consequence of the definition is that a well-factorable sequence of level `D` vanishes at every prime `p` with `sqrt(D) < p <= D`; therefore the Yang prime-base weight cannot simply be inserted as Zheng's well-factorable weight at a comparable full support level.

The negative conclusion is deliberately narrow: **Zheng's theorems cannot be cited as the missing Yang welding theorem.** Their dispersion/Kloosterman/`q`-van-der-Corput machinery is nevertheless materially relevant method-level prior art. It is the closest located framework designed specifically to survive a residue class that moves with two moduli, and therefore redirects any attempt beyond WI-054 toward a Yang-specific two-modulus dispersion theorem rather than toward another generic level-of-distribution citation.

## 1. Primary source and exact theorem surface

The source is:

Zongkun Zheng, **Primes in simultaneous arithmetic progressions**, arXiv:2512.22798v1, submitted 28 December 2025,
https://arxiv.org/abs/2512.22798.

This is a recent unrefereed preprint, so only its printed theorem statements are used here.

Zheng's Theorem 1.1 fixes `epsilon>0`, `0 <= theta <= 7/36`, residues satisfying

\[
|a_1|\le \log^B x,\qquad |a_2|\le x,\qquad a_1\ne a_2,
\tag{1}
\]

and divisor-bounded coefficient sequences `gamma_q`, `lambda_d` with

\[
q\asymp x^\theta,\qquad d\le x^{\mathcal L(\theta)-\varepsilon},
\tag{2}
\]

subject to the squarefree/coprimality conditions printed in the theorem. Crucially, `lambda` must be **well-factorable** of level `x^{L(theta)-epsilon}`. The conclusion is

\[
\sum_q\sum_{\substack{d\\(q,d)=1}}
\gamma_q\lambda_d
\left(
\sum_{\substack{p\le x\\p\equiv a_1\pmod d\\p\equiv a_2\pmod q}}1
-\frac{\pi(x)}{\varphi(qd)}
\right)
\ll_{A,\varepsilon,B}\frac{x}{\log^A x}.
\tag{3}
\]

The admissible function `L(theta)` is piecewise; in particular the theorem genuinely enters regimes in which the combined modulus exceeds the classical square-root scale. That is why it is a serious candidate prior-art input rather than a cosmetic nearby citation.

Theorem 1.2 is described in the paper as a quadrilinear form. It takes divisor-bounded `alpha_m,beta_n,gamma_q,lambda_d`, with

\[
m\asymp x^{1-\nu},\qquad n\asymp x^\nu,
\tag{4}
\]

again requires the `d`-weight `lambda` to be well-factorable, requires `beta` to satisfy a Siegel--Walfisz condition, and imposes a lower bound on the least prime factor of `n`. Its arithmetic object is

\[
\sum_q\sum_{\substack{d\\(q,d)=1}}
\gamma_q\lambda_d
\left(
\sum_{\substack{mn\equiv a_1\pmod d\\mn\equiv a_2\pmod q}}
\alpha_m\beta_n
-
\frac1{\varphi(qd)}
\sum_{(mn,qd)=1}\alpha_m\beta_n
\right),
\tag{5}
\]

with a power-saving logarithmic mean-value bound in the printed piecewise `(theta,nu)` ranges. The word **quadrilinear** here refers to the four coefficient sequences `alpha,beta,gamma,lambda`; it is not a theorem for four affine prime forms.

## 2. Why this looked like the right prior art

The live Yang clue after WI-049--WI-054 is a two-modulus, power-coefficient arithmetic problem. On the dominant coprime family the exact source forms are

\[
L_1=m,\qquad L_2=m-rk,\qquad
L_3=n,\qquad L_4=n-qk,
\tag{6}
\]

with `r,q` power-sized on a positive-mass part of the source ledger. WI-051 shows that localizing to the physical scales turns those coefficients into large-index residue-class fibers. WI-054 then uses Shao--Teräväinen nilsequence Bombieri--Vinogradov plus Parseval to control the complete analytic nonzero-frequency residual on

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1,
\tag{7}
\]

for `r=X^alpha`, `q=X^beta`, away from endpoints by fixed margins. Outside that region a coefficient-aware two-modulus input is exactly what one would like.

Zheng's paper is explicitly designed for a different but nearby obstruction: a prime satisfying two congruences whose combined CRT residue depends nontrivially on both varying moduli. Its proof uses dispersion, spectral estimates for Kloosterman sums, and a `q`-analogue of van der Corput. This is therefore the strongest recent **methodological** match found in the bounded audit.

The theorem surface, however, does not match (6).

## 3. First obstruction: simultaneous congruences on one multiplicative variable are not the Yang additive lock

Zheng Theorem 1.1 controls a single prime `p` obeying

\[
p\equiv a_1\pmod d,
\qquad
p\equiv a_2\pmod q.
\tag{8}
\]

Theorem 1.2 replaces `p` by the single product `mn` and imposes the same two simultaneous congruences on that product.

In contrast, after the exact Yang dispersion swap, modulus `r` belongs to the first additive pair and modulus `q` belongs to the second:

\[
m' = m-rk,
\qquad
n' = n-qk.
\tag{9}
\]

There is no source identity placing one of `m,m',n,n'`, or one fixed product of two independent source variables, simultaneously in prescribed classes modulo both `r` and `q`. The coupling is through the common shift `k`, not through a CRT condition on a single multiplicative variable.

One can formally set, for fixed `k`,

\[
a_m(k)=\Lambda(m)\Lambda(m-rk),
\qquad
b_n(k)=\Lambda(n)\Lambda(n-qk),
\tag{10}
\]

but then the coefficient sequences themselves depend on `k` and on the source interval/lock geometry. Equation (5) does not state a theorem uniform for such a moving family, and its congruence conditions on `mn` are still absent. Thus the printed quadrilinear theorem is not the four-prime covariance theorem needed by the source.

This mismatch alone blocks a black-box invocation.

## 4. Second obstruction: the small-residue hypothesis is incompatible with the source-faithful residue average

WI-054 gives the exact localized Yang pair fiber in residue-class coordinates. For the `r` side,

\[
A_r(t)
=
\mathbb E_{c\bmod r}
\widehat{f_{1,c}}(-t)\widehat{f_{2,c}}(t),
\qquad
f_{i,c}(u)=f_i(c+ru).
\tag{11}
\]

The residue `c` is therefore not one fixed small integer. The arithmetic object averages over **all** classes modulo `r`; the same is true for `q` on the other side. When `r=X^{\Omega(1)}`, all but a vanishing proportion of those classes have representatives larger than every fixed power of `log X`.

Zheng's Theorems 1.1 and 1.2 require the residue attached to the well-factorable modulus to obey

\[
|a_1|\le\log^B x.
\tag{12}
\]

Although the second residue `a2` may be large, swapping the two moduli only moves the problem from one Yang side to the other. Translating `m=c+ru` so that the residue label becomes zero does not preserve the von Mangoldt sequence as a fixed arithmetic function: it replaces it by `Lambda(c+ru)`, exactly the progression whose residue dependence has to be controlled. Hence (12) is not removable by a coordinate relabeling.

A theorem maximal or averaged over all residues would be a materially stronger and more source-faithful interface. Zheng's printed theorem is not such a statement.

## 5. Third obstruction: a well-factorable level cannot carry the full prime-modulus Mertens ledger

The well-factorable hypothesis has an elementary support consequence that is useful independently of the Yang application.

Let `(lambda_d)` be well-factorable of level `D` in Zheng's Definition 1.1. By definition, for **every** factorization

\[
D=D_1D_2
\tag{13}
\]

there are sequences `lambda'`, `lambda''`, supported on `d1<=D1` and `d2<=D2`, such that

\[
\lambda_d=\sum_{d_1d_2=d}\lambda'_{d_1}\lambda''_{d_2}.
\tag{14}
\]

Choose the balanced factorization

\[
D_1=D_2=\sqrt D.
\tag{15}
\]

For any prime

\[
\sqrt D<p\le D,
\tag{16}
\]

the only multiplicative factorizations of `p` are `(1,p)` and `(p,1)`. In each term one factor exceeds `sqrt D`, outside the relevant support. Therefore

\[
\boxed{\lambda_p=0\qquad(\sqrt D<p\le D).}
\tag{17}
\]

This is an exact consequence of the definition, not an estimate.

The Yang base measure is qualitatively different. WI-052 proves that proper prime powers contribute only `O(1/log X)` to the normalized base measure; actual primes dominate. Moreover the prime Mertens law

\[
\sum_{p\le Y}\frac{\log p}{p}=\log Y+O(1)
\tag{18}
\]

shows that primes in the upper exponent half of any macroscopic support range carry positive normalized mass. Therefore, if one takes Zheng's well-factorable level `D` comparable to the full endpoint of a Yang prime-modulus range and tries to identify `lambda_d` with that Mertens base weight, (17) deletes a positive chunk of precisely the dominant prime support.

This does **not** say that no well-factorable decomposition can help on a smaller subrange. For example, if one only needs prime moduli well below `sqrt D`, the support obstruction (17) no longer decides the question, and a nontrivial sieve decomposition could conceivably be useful. It does say that the full Yang prime-base ledger is not itself the well-factorable sequence required by Zheng, and that assigning the other Yang base to `gamma_q` does not solve the problem because the two sides are symmetric.

## 6. Theorem 1.2 has additional sequence hypotheses, not a hidden four-prime escape

Theorem 1.2 might look more promising because it is explicitly called quadrilinear and permits divisor-bounded `alpha_m` and `beta_n`. But its load-bearing object remains the multiplicative bilinear sequence `alpha_m beta_n` under congruence conditions on the product `mn`. It additionally requires `beta` to satisfy a Siegel--Walfisz condition and imposes `P^-(n)>log^C x`.

The natural Yang attempt (10) does not produce a fixed `beta_n`: it produces a shifted-prime pair depending on `k`, `q`, and the moving source interval. Proving the required Siegel--Walfisz-type uniformity for that family would already amount to a substantial part of the missing welding theorem. Thus Theorem 1.2 does not hide the required four-prime estimate inside a relabeling of its coefficients.

This is the same general warning established earlier by WI-037 and WI-051 in more source-specific forms: a theorem for a broad-looking coefficient class cannot be consumed after inserting a new correlated prime-pair weight unless the theorem's actual structural hypotheses survive that insertion.

## 7. What Zheng does contribute: a method-level redirection

The negative theorem-interface audit should not be read as irrelevance. Zheng explicitly addresses the failure of naive variable separation when two moduli create a moving CRT residue. The proof combines:

- Linnik-style dispersion;
- spectral bounds for averages of Kloosterman sums;
- algebraic exponential-sum estimates of Weil--Deligne type;
- `q`-van-der-Corput factorizations in parameter ranges where the spectral separation loses too much.

That is much closer to the **kind** of coefficient-aware arithmetic input the live Yang clue needs than a generic one-modulus level-of-distribution theorem. WI-047 already showed that any fixed generic AP level `<1` leaves positive Yang support mass uncovered. WI-053 showed that the 2026 AP-maximal nilsequence theorem is ambient-normalized and therefore loses the progression-density factor at power spacing. WI-054 recovers a genuine positive-power region by using modulus-averaged nilsequence Bombieri--Vinogradov plus the exact pair-fiber factorization.

Zheng therefore changes the next literature-facing question from

\[
\text{``is there a stronger generic AP theorem to cite?''}
\]

to

\[
\boxed{
\text{``can two-modulus dispersion/Kloosterman technology be rebuilt for the additive locked}\
\text{pair--pair object with arbitrary residue averaging and Mertens prime-modulus weights?''}
}
\tag{19}
\]

That would be a genuinely new theorem obligation. Nothing in the present finding asserts that Zheng's proof machinery can meet it without new ideas.

## 8. Prior-art and novelty audit

The primary recent source is Zheng 2025 above. Its method explicitly builds on Bombieri--Friedlander--Iwaniec/Fouvry--Iwaniec large-modulus dispersion, Deshouillers--Iwaniec Kloosterman-spectral estimates, and the `q`-analogue of van der Corput. Nearby modern large-modulus results of Maynard, Lichtman, Pascadi and Assing--Blomer--Li concern structured weights or one-modulus prime distribution and were already part of the WI-047/WI-053 audit surface.

A bounded search for unconditional results simultaneously matching all of the Yang features

\[
\text{four affine prime forms}
+\text{two power-sized independent coefficients}
+\text{arbitrary residue averaging}
+\text{Mertens prime-modulus weights}
\tag{20}
\]

did not locate a theorem with those printed hypotheses. This absence is **not** a novelty or impossibility claim.

No novelty is claimed for well-factorable weights, the balanced-factorization observation (17), CRT, dispersion, Kloosterman sums, or `q`-van-der-Corput. The Mathia contribution is the exact source-interface audit: separate the recent two-modulus theorem from the superficially similar Yang object and identify three independent hypotheses that prevent a black-box citation.

## 9. Falsification / reopening conditions

Narrow or withdraw the negative conclusion if any of the following is supplied:

1. a corollary of Zheng's Theorem 1.1 or 1.2 in which the Yang locked four-prime covariance is explicitly represented without introducing a coefficient sequence depending on the common shift;
2. a version uniform/maximal over the source's full residue classes rather than requiring one polylogarithmically small residue;
3. a decomposition of the Yang prime-modulus Mertens ledger into Zheng-admissible well-factorable pieces with the exact source normalization and no power-scale mass loss;
4. a direct theorem, whether by Zheng's methods or otherwise, for the additive system `(m,m-rk,n,n-qk)` averaged over the required `r,q,k` family;
5. an argument showing that only a Zheng-compatible subregion is needed because the complement is already `o(1)` under WI-049--WI-054 and the source boundary/collision bookkeeping.

Until one of these bridges is written, citing “simultaneous arithmetic progressions” or the word “quadrilinear” does not close the Yang welding gate.

## 10. Consequence for `weil_inertia`

The current unconditional simple-critical bound is unchanged. The arithmetic frontier of the one-sided fourth-moment route is sharper:

- WI-050 closes every fixed polylogarithmic coefficient range;
- WI-054 closes the complete analytic nonzero-frequency residual in the doubly-small power region (7), modulo the separately identified deterministic `W`-main/full-local-main splice and source boundary/collision bookkeeping;
- Zheng 2025 supplies relevant two-modulus **technology**, but not a theorem whose hypotheses cover the remaining Yang cells.

The efficient next route is therefore not another black-box substitution. Either enlarge the WI-054 nilsequence-BV region by a source-faithful hybrid argument, or derive a Yang-specific two-modulus dispersion estimate modeled on the recent simultaneous-AP machinery. The present finding closes the cheap inference that the latter theorem already exists in usable form.