# MC-005 — Exact-support multiplicativity permits arbitrarily slow mean cancellation

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`.

## Claim

There is an explicit family of multiplicative functions

\[
a_q:\mathbb N\to\{-1,0,1\}
\]

indexed by primes `q >= 5` such that all three of the following hold:

1. `a_q` has **exactly the Möbius square-free support**,
   \[
   |a_q(n)|=\mu(n)^2;
   \tag{1}
   \]
2. `a_q` has qualitative mean cancellation,
   \[
   \frac1x\sum_{n\le x}a_q(n)\longrightarrow0;
   \tag{2}
   \]
3. its cancellation can nevertheless be only logarithmic:
   \[
   \sum_{n\le x}a_q(n)
   \sim C_q\,\frac{x}{(\log x)^{2/(q-1)}}
   \qquad(C_q>0).
   \tag{3}
   \]

As `q -> infinity`, the exponent `2/(q-1)` tends to zero. Thus even within **multiplicative** sequences with Möbius's exact zero set and vanishing normalized mean, the convergence to zero may be arbitrarily slow. In particular, these data do not imply

\[
\sum_{n\le x}a(n)=O(x^{1-c})
\tag{4}
\]

for any fixed `c>0`.

This strengthens the information audit after `MC-004` in one precise direction. `MC-004` showed that exact square-free support plus all qualitative fixed-shift Chowla limits permit near-linear partial sums when multiplicativity is discarded. The present control shows that **adding multiplicativity to exact support and one-point qualitative cancellation still does not provide a power-saving information budget**. It does not combine multiplicativity with the full higher Chowla property; that joint condition remains outside this result.

## Explicit construction

Fix a prime `q>=5`. Define signs on primes by

\[
\sigma_q(p)=
\begin{cases}
-1,&p\equiv1\pmod q,\\
+1,&p\not\equiv1\pmod q,
\end{cases}
\tag{5}
\]

where the exceptional prime `p=q` is included in the `+1` case. Extend `\sigma_q` completely multiplicatively, and set

\[
a_q(n)=\mu(n)^2\sigma_q(n).
\tag{6}
\]

Both factors in (6) are multiplicative, hence so is `a_q`. Moreover

\[
a_q(p)=\sigma_q(p),
\qquad
a_q(p^k)=0\quad(k\ge2),
\tag{7}
\]

which proves the exact support identity (1).

Among the `q-1` reduced residue classes modulo `q`, one class contributes prime sign `-1` and the remaining `q-2` classes contribute `+1`. Put

\[
\alpha_q=1-\frac{2}{q-1}=\frac{q-3}{q-1},
\qquad
\beta_q=1-\alpha_q=\frac{2}{q-1}.
\tag{8}
\]

The prime number theorem in arithmetic progressions for the fixed modulus `q` gives, for every fixed `A>0`,

\[
\sum_{p\le x}a_q(p)\log p
=\alpha_q x+O_{q,A}\!\left(\frac{x}{(\log x)^A}\right).
\tag{9}
\]

Indeed this is the ordinary weighted prime sum minus twice the contribution of primes `p congruent 1 (mod q)`; the single prime `q` changes only the bounded term.

## Selberg–Delange transfer

The hypotheses of the Granville–Koukoulopoulos Landau–Selberg–Delange theorem (`MC-S14`) apply to `a_q`: it is multiplicative, `|a_q|<=1=tau_1`, and (9) supplies the required prime-average estimate with arbitrarily large fixed `A`.

Let

\[
F_q(s)=\sum_{n\ge1}\frac{a_q(n)}{n^s}
      =\prod_p\left(1+\frac{\sigma_q(p)}{p^s}\right)
\qquad(\operatorname{Re}s>1).
\tag{10}
\]

The leading Selberg–Delange coefficient is

\[
c_{q,0}
=\prod_p
 \left(1+\frac{\sigma_q(p)}p\right)
 \left(1-\frac1p\right)^{\alpha_q}.
\tag{11}
\]

This product converges to a positive finite number. Every Euler factor is positive, and

\[
\log\!\left[
 \left(1+\frac{\sigma_q(p)}p\right)
 \left(1-\frac1p\right)^{\alpha_q}
\right]
=\frac{\sigma_q(p)-\alpha_q}{p}+O(p^{-2}).
\tag{12}
\]

The sum of the first terms converges by the fixed-modulus prime number theorem in arithmetic progressions and partial summation, while `sum_p p^-2` converges absolutely. Hence `c_{q,0}>0`.

Since `0<alpha_q<1`, `Gamma(alpha_q)>0`. Taking enough terms in `MC-S14` therefore yields

\[
\sum_{n\le x}a_q(n)
=\frac{c_{q,0}}{\Gamma(\alpha_q)}
  x(\log x)^{\alpha_q-1}
  \left(1+O_q\!\left(\frac1{\log x}\right)\right),
\tag{13}
\]

which is (3) with

\[
C_q=\frac{c_{q,0}}{\Gamma(\alpha_q)}>0.
\]

Because `beta_q>0`, (13) implies (2). But for every fixed `c>0`,

\[
\frac{x/(\log x)^{\beta_q}}{x^{1-c}}
=\frac{x^c}{(\log x)^{\beta_q}}
\longrightarrow\infty,
\tag{14}
\]

so even one fixed member of the family violates every fixed power-saving conclusion (4). Letting `q` grow additionally shows that the logarithmic decay exponent itself can be made arbitrarily small.

## Why this is a relevant matched control

The construction retains two pieces of Möbius structure that a generic bounded-sequence counterexample lacks:

- the zero set is **exactly** the nonsquare-free integers;
- the nonzero values obey multiplicative consistency across coprime factors.

It also retains the one-point qualitative consequence that would follow from Chowla, namely normalized mean zero. Yet these properties coexist with partial sums of order `x/log^beta x`, far above `x^(1-c)` for every fixed `c>0`.

The mechanism is transparent: `a_q` is strongly biased toward `+1` at the primes. Its prime-average parameter `alpha_q` is positive and arbitrarily close to `1`; Selberg–Delange converts that prime-level bias into a logarithmic singularity and hence an almost-linear summatory function. Multiplicativity propagates the bias rather than destroying it.

This identifies a sharper boundary than the statement "multiplicativity may matter" left by `MC-004`. **Multiplicativity by itself is not the missing quantitative datum.** An RH-relevant escape from `MC-004` must use multiplicativity together with substantially stronger prime-local or correlation information that excludes this biased Euler-factor regime.

At the opposite extreme, matching all prime values as well as support and multiplicativity would be tautological: if a multiplicative `a` satisfies `a(p)=-1` for every prime and vanishes exactly on nonsquare-free integers, then `a=mu`. The useful research question is therefore about intermediate, quantitative prime-local constraints rather than exact prime-value matching.

## Prior art and novelty assessment

The asymptotic mechanism in (13) is standard Landau–Selberg–Delange theory. `MC-S14` explicitly gives asymptotic expansions for multiplicative functions from a prime-value average of the form (9), and fixed-modulus prime distribution in arithmetic progressions is classical (`MC-S15`). **No novelty is claimed for the asymptotic formula or for the residue-class construction as a theorem of multiplicative number theory.**

There is also direct adjacent prior art on the same structural class. Klurman, Mangerel, Pohoata and Teräväinen (`MC-S16`) study sums `sum_{n<=x} mu(n)^2 g(n)` for multiplicative `{-1,+1}`-valued `g` and prove that their discrepancy is always unbounded. Our `a_q` is exactly such a square-free-supported multiplicative sequence, with a deliberately biased prime pattern for which the much larger asymptotic (13) follows immediately from Selberg–Delange. Their theorem therefore prevents treating square-free-supported multiplicative controls themselves as a new object here.

The durable contribution of this finding is instead the **Mathia-specific information audit**: the obvious proposed repair to `MC-004` — retain exact support and additionally impose multiplicativity — still cannot turn qualitative mean cancellation into polynomial cancellation. The counterexample is arithmetic rather than a density-zero sign overwrite, and its failure mode is explicitly localized at the prime-value distribution.

## Boundaries and failure modes

This finding does **not** show that multiplicativity is irrelevant to Möbius cancellation. It shows only that multiplicativity is insufficient when coupled with exact support and qualitative one-point cancellation.

In particular:

- the family is not asserted to satisfy the full higher fixed-shift Chowla property from `MC-004`;
- its prime signs do not match Möbius's exact law `mu(p)=-1`;
- it is highly pretentious toward the constant function compared with Möbius, so a sufficiently strong quantitative non-pretentiousness hypothesis can exclude it;
- it does not address quantitative correlations uniform over growing shifts;
- it does not model an off-critical zero or provide evidence about actual values of `M(x)`.

The decisive audit for a proposed multiplicative escape is now:

> identify a prime-local, multiscale, or correlation condition actually known for Möbius that rules out the family (5)–(6), and prove that the surviving information has polynomial rather than merely logarithmic strength.

A condition that simply hard-codes `a(p)=-1` for every prime while also imposing exact support and multiplicativity reconstructs Möbius itself and is not an explanatory intermediate mechanism.

## Relation to the existing obstruction chain

`MC-001` ruled out black-box aggregation of short-interval magnitude and exceptional mass. `MC-002` showed that a single standard pretentious scalar has only `O(log log x)` dynamic range. `MC-003` showed that the natural Möbius/Liouville prime-power enrichment hits the same one-half transfer boundary. `MC-004` showed that exact support plus every qualitative fixed-shift Chowla limit is still compatible with near-linear bias when multiplicativity is absent.

`MC-005` isolates a complementary failure mode: **exact support plus multiplicativity plus qualitative mean cancellation is also compatible with near-linear logarithmic bias.** Thus neither higher qualitative correlations without multiplicativity (`MC-004`) nor multiplicativity without sufficiently strong prime/correlation control (`MC-005`) closes the information gap on its own.

The remaining potentially meaningful frontier is their quantitative interaction: multiplicative structure strong enough to prohibit coherent prime bias, combined with correlation or multiscale estimates strong enough to constrain anchored sums at a polynomial scale.