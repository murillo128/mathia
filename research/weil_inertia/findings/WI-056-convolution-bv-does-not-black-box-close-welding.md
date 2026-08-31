# WI-056 — Zhiyuan Yang's convolution Bombieri--Vinogradov theorem does not black-box close the locked welding gap

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** change Mathia's current unconditional simple-critical proportion and does not show that the Yang--Yang one-sided fourth-moment route is false. It audits a particularly tempting fresh repair for the live welding gap: Zhiyuan Yang's August 2026 convolution-type Bombieri--Vinogradov theorem. The new theorem is genuinely closer to the missing arithmetic interface than an ordinary prime-in-progressions result, but its printed theorem surface still does not accept the locked four-prime object required by the Yang--Yang source. In particular, its arbitrary divisor-bounded factor is an **external modulus weight**, not the internal shifted-prime-pair welding coefficient from WI-037; its inner arithmetic relation is the multiplicative congruence `l p = a (mod d q)`, not the additive four-form lock `(m,m-rk,n,n-qk)`; its residue `a` is fixed; and if both Yang coefficient bases are assigned to the two modulus slots then one of their prime-Mertens ledgers must occupy a well-factorable slot, which WI-055 already rules out as an exact full-support identification.

The paper is nevertheless useful method-level prior art. Its proof combines Bombieri--Friedlander--Iwaniec/Maynard-style well-factorability with Pascadi's triply-well-factorable convolution and incomplete-Kloosterman machinery. A future source-specific dispersion reduction of the Yang locked covariance could conceivably land in that analytic technology. What is closed here is the cheaper step “the new convolution-BV theorem already proves the welding estimate by citation.”

## 1. Primary source and exact theorem surface

The fresh primary source is

Zhiyuan Yang, *Convolution-type Bombieri--Vinogradov theorem with well-factorable Weights, and its applications*, arXiv:2608.13299v1, submitted 13 Aug 2026.

The paper begins from a convolution discrepancy of the form

\[
\mathcal E
=
\sum_d\sum_q \gamma_d\lambda_q
\left(
 \sum_{\ell\sim L}
 \sum_{\substack{p<x/\ell\\ \ell p\equiv a\pmod{dq}}}1
 -
 \frac1{\varphi(dq)}
 \sum_{\ell\sim L}
 \sum_{\substack{p<x/\ell\\ (\ell p,dq)=1}}1
\right),
\tag{1}
\]

with `L=x^nu`. In the two-modulus form used in Theorem 1.2, `D=x^theta` with `0<theta<nu-epsilon`; `gamma_d` is divisor-bounded on the `d`-range, while `lambda_q` is required to be well-factorable at the theorem's admissible level. The conclusion is a powerfully averaged logarithmic-saving estimate

\[
\mathcal E\ll_{\varepsilon,A,a}\frac{x}{(\log x)^A}.
\tag{2}
\]

The residue parameter `a` is a fixed nonzero integer; the displayed implied constant is allowed to depend on it. Theorem 1.1 is the corresponding `d=1` convolution form. The paper explicitly says that the proof uses Pascadi's triply-well-factorable convolution estimate and incomplete Kloosterman estimates, and its detailed reduction introduces several factorable modulus pieces before applying those spectral/Kloosterman inputs.

This is a recent unrefereed preprint. For the negative interface claim below, no unreviewed numerical constant is imported: even granting (1)--(2) exactly as stated, its hypotheses and variable roles do not coincide with the Yang welding object.

Primary source:

- https://arxiv.org/abs/2608.13299

## 2. The live Yang object is an additive locked four-prime correlation

The source-faithful welding system audited in WI-037--WI-055 has the equal-lock swap

\[
 m'=m-rk,
 \qquad
 n'=n-qk,
\tag{3}
\]

with power-sized reduced coefficients `r,q` on the dominant continuum. Before the final glue estimate, one encounters shifted-prime-pair weights such as

\[
 w_{r,k}(n)
 =
 \sum_{m\in I(n)}
 \Lambda(m)\Lambda(m-rk),
\tag{4}
\]

and, after the two sides are exposed simultaneously, the affine four-prime pattern

\[
\boxed{
(m,\ m-rk,\ n,\ n-qk).
}
\tag{5}
\]

WI-049 removes the deterministic four-prime singular-series local-main bias. WI-050 controls fixed polylogarithmic coefficient regimes. WI-054 controls the entire nonzero pair-frequency residual on the genuine power region where both reduced moduli fit the Shao--Teräväinen nilsequence-BV range,

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1.
\tag{6}
\]

The accepted clue remains the complementary positive-power region. Thus a useful new theorem has to control the **post-local-main locked covariance** of (5), not merely distribute a product sequence in one congruence class.

## 3. “Divisor-bounded” occurs in the wrong variable to repair WI-037

The closest-looking feature of Zhiyuan Yang's Theorem 1.2 is that `gamma_d` may be divisor-bounded. But in (1), `gamma_d` is indexed by the modulus `d` and sits **outside** the inner `ell,p` sum:

\[
\sum_d \gamma_d\,[\text{prime-convolution discrepancy modulo }d q].
\tag{7}
\]

The missing Yang coefficient (4) is qualitatively different. It depends on an inner prime variable, the common shift `k`, the coefficient `r`, and the moving interval `I(n)`. The theorem does not state that one may replace the inner summand in (1) by

\[
 a_{\ell,p,k}\,1_{\ell p\equiv a\pmod{dq}}
\tag{8}
\]

for an arbitrary divisor-bounded or prime-correlation weight `a_{ell,p,k}`. In particular there is no theorem-level operation that reinterprets `w_{r,k}(n)` as `gamma_d`: doing so changes an inner correlation coefficient into an external modulus coefficient and loses its dependence on the source variables.

Therefore the exact obstruction of WI-037 survives unchanged:

\[
\boxed{
\text{divisor-bounded external modulus weight}
\neq
\text{divisor-bounded internal welding weight}.
}
\tag{9}
\]

This matters because WI-037's elementary adversarial example already proves that pointwise divisor-boundedness alone cannot force minor-arc cancellation for an internal coefficient. The new paper proves a strong theorem for a **specific convolution architecture**; it does not turn divisor-boundedness into a generic stability principle for weighted prime exponential sums.

## 4. A product congruence is not the locked additive four-form system

Equation (1) constrains the single multiplicative object

\[
\ell p\equiv a\pmod{dq}.
\tag{10}
\]

Even though the modulus has two factors `d` and `q`, there remains one inner product and one congruence. By contrast, (5) asks for four prime values of three additive variables with two independent coefficient directions sharing the same `k`.

There is no direct identification

\[
\{\ell p\equiv a\pmod{dq}\}
\longleftrightarrow
\{m,m-rk,n,n-qk\text{ prime}\}
\tag{11}
\]

that preserves either primality or the Yang source weights. Assigning `d=r` and `q=q` does not create the two shifted-prime pairs. Assigning `ell` or `p` to one of the prime legs does not create the other three legs or the common-lock covariance.

A useful stress test is the specialization `q=1`. Then the well-factorable requirement is vacuous and Theorem 1.2 can indeed average an arbitrary divisor-bounded `gamma_d` over one modulus family. But exactly for that reason it no longer contains the second independent Yang coefficient. So this specialization shows why the conclusion here must be narrow:

\[
\boxed{
\text{the theorem may be useful for one derived modulus problem,}
\quad
\text{but it is not already the two-base welding theorem.}
}
\tag{12}
\]

A new dispersion identity could still reduce (5) to multilinear Kloosterman forms resembling the proof of (1). That would be a new analytic argument, not a black-box invocation of Theorem 1.2.

## 5. The fixed-residue interface still misses the localized all-residue fibers

The estimate (2) is stated for a fixed nonzero residue `a`, with the implied constant depending on `a`. The Yang pair-fiber decomposition instead localizes over all residue classes

\[
 c\pmod r,
 \qquad
 d\pmod q,
\tag{13}
\]

and the Parseval identity in WI-054 uses those complete residue-class families. The residues vary with the growing moduli; they are not one fixed integer independent of `X`.

Relabeling a nonzero class to `1` modulo a prime does not solve this at theorem level. Such a relabeling is a statement in the finite quotient; it does not transform the actual prime sequence `Lambda(c+r u)` into the fixed-residue sequence appearing in (1) with a uniform constant. A usable black-box theorem would need a max/sup over the relevant growing residues, or a source-specific averaging argument that proves the required uniformity.

Thus Zhiyuan Yang's theorem removes neither the all-residue gate of WI-055 nor the modulus-dependent pair-frequency gate already handled only in the smaller WI-054 region.

## 6. Using both Yang coefficient bases revives the well-factorable-support obstruction

There is another exact interface issue if one tries to map the two Yang base coefficients to the two modulus slots of (1). The `q`-weight `lambda_q` must be well-factorable.

WI-055 already extracted the elementary support consequence of the definition. If `lambda` is well-factorable of level `Q`, use the balanced factorization `Q=Q_1Q_2` with `Q_i` of square-root size. For a prime

\[
\sqrt Q<p\le Q,
\tag{14}
\]

neither factorization `p=1\cdot p` nor `p=p\cdot1` has both factors inside the balanced supports. Hence

\[
\boxed{\lambda_p=0\qquad(\sqrt Q<p\le Q).}
\tag{15}
\]

The Yang base ledger is supported on prime powers and its dominant prime part has Mertens weight. On a macroscopic prime range,

\[
\sum_{\sqrt Q<p\le Q}\frac{\log p}{p}
=
\frac12\log Q+O(1),
\tag{16}
\]

so (15) deletes positive normalized source mass. Therefore a full prime-Mertens coefficient family cannot simply be inserted into the well-factorable `lambda_q` slot.

This is not a theorem that every use of (1) is impossible: one can set `q=1`, use a sieve decomposition, or attempt a more elaborate factorization. It is the exact statement needed for the black-box audit:

\[
\boxed{
\text{both Yang prime-base ledgers}
\not\equiv
(\text{arbitrary }\gamma_d,\ \text{well-factorable }\lambda_q)
}
\tag{17}
\]

without a nontrivial new decomposition and a proof that its discarded/remainder mass is negligible in the Yang normalization.

## 7. What the fresh paper does contribute to the program

The negative theorem-interface result should not hide the real methodological relevance. Zhiyuan Yang's proof is built precisely from machinery that has repeatedly appeared at the edge of this clue:

1. well-factorable and triply-well-factorable modulus decompositions;
2. Pascadi's exceptional-large-sieve technology;
3. truncated Poisson summation;
4. incomplete Kloosterman estimates;
5. multilinear splitting of modulus and convolution variables.

The paper therefore gives a concrete recent template for what a **source-specific repair** could look like. The right next question is not “can Theorem 1.2 be cited?”, but:

\[
\boxed{
\text{can the exact Yang post-local-main covariance be dispersed into a}
\text{ Pascadi/Yang-admissible multilinear Kloosterman form?}
}
\tag{18}
\]

For that to count as progress, the reduction has to retain the two prime-base Mertens ledgers, the common `k` lock, all relevant residues, the source smoothing/collar, and the exact normalization. If the only way to obtain a theorem-shaped form is to replace a prime ledger by a well-factorable sieve weight on positive source mass, or to apply the across-family Cauchy--Schwarz step whose Poisson floor is already over budget in WI-042, then the repair fails for a substantive reason.

This is a useful redirection: the fresh paper strengthens the case for **adapting its dispersion/Kloosterman proof technology**, while closing the much cheaper claim that its stated convolution-BV theorem is already the missing welding lemma.

## 8. Prior-art and novelty audit

No novelty is claimed for Bombieri--Friedlander--Iwaniec well-factorable estimates, Maynard/Pascadi large-modulus technology, Zhiyuan Yang's theorem, truncated Poisson summation, Kloosterman estimates, or the support property of well-factorable weights already recorded in WI-055.

The Mathia contribution in this finding is a source-specific theorem-interface audit:

- distinguish the external divisor-bounded modulus coefficient in arXiv:2608.13299 from the internal divisor-bounded shifted-prime-pair weight required by WI-037;
- distinguish the multiplicative one-product congruence from the additive four-prime lock;
- retain the fixed-residue and well-factorability gates instead of treating the word “convolution” as sufficient;
- identify the new paper's proof machinery, rather than its theorem statement, as the relevant prior-art direction for the accepted clue.

A targeted search located no public theorem that combines all of the features required here: two power-sized prime-Mertens coefficient families, all localized residues, the additive system (5), a common shift variable, and a post-local-main logarithmic-saving covariance bound. Absence of such a source is not a priority claim and is not evidence that such a theorem is impossible.

## 9. Decisive verification / falsification gate

This finding should be narrowed or retired if one of the following is supplied with the Yang source scales checked explicitly:

1. an exact algebraic reduction of the post-local-main four-prime covariance (5) to the discrepancy in Zhiyuan Yang's Theorem 1.1 or 1.2, without replacing the internal welding weight by an unsupported divisor-bounded envelope;
2. a theorem-level extension of arXiv:2608.13299 allowing the needed additive four-form or internal shifted-prime correlation, uniformly over the growing residue families;
3. a decomposition of the prime-Mertens coefficient ledger into admissible well-factorable pieces plus a remainder whose total Yang-normalized contribution is `o(1)`;
4. a source-faithful dispersion/Kloosterman proof, possibly using Zhiyuan Yang/Pascadi technology, that closes the complementary power region left by WI-054 without the forbidden WI-042 family Cauchy loss.

Until then the live chain remains

\[
\text{exact local main}
\to
\text{WI-054 nilsequence-BV region}
\to
\boxed{\text{uncontrolled complementary locked covariance}}
\to
\text{one-sided fourth-moment remainder}.
\tag{19}
\]

The new convolution-BV paper is now recorded as a high-value **method source**, not as evidence that the boxed step has been proved.