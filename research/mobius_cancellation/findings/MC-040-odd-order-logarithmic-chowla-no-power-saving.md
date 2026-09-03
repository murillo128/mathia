# MC-040 — all fixed odd-order logarithmic self-correlations can vanish while partial sums remain near-linear

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The exact-support multiplicative comparator family from `MC-005` and `MC-039` passes a substantially larger qualitative correlation family than previously recorded while retaining almost-linear anchored partial sums.

Fix a prime `q>=5`. Define the completely multiplicative prime-sign lift

\[
\sigma_q(p)=
\begin{cases}
-1,&p\equiv1\pmod q,\\
+1,&p\not\equiv1\pmod q,
\end{cases}
\]

and the square-free-supported multiplicative function

\[
a_q(n)=\mu(n)^2\sigma_q(n).
\tag{1}
\]

Then for every odd integer `r>=1` and every fixed integer shifts `h_1,...,h_r`,

\[
\boxed{
\sum_{n\le x}\frac{a_q(n+h_1)\cdots a_q(n+h_r)}{n}
=o(\log x)
}
\qquad(x\to\infty),
\tag{2}
\]

with the usual convention that the functions vanish when an argument is non-positive. More generally the corresponding normalized logarithmic average over every moving range `x_m/omega_m <= n <= x_m`, with `omega_m,x_m -> infinity`, tends to zero.

Nevertheless `MC-005` gives

\[
\boxed{
\sum_{n\le x}a_q(n)
\sim C_q\frac{x}{(\log x)^{2/(q-1)}}
}
\qquad(C_q>0),
\tag{3}
\]

so these partial sums violate `O(x^(1-c))` for every fixed `c>0`.

Thus **exact Möbius square-free support, multiplicativity, and every fixed odd-number-of-factors qualitative logarithmic self-correlation still do not contain a polynomial global-cancellation budget.** This strengthens `MC-039`, which supplied all qualitative logarithmically averaged two-point Elliott tests but did not cover arbitrarily high odd numbers of factors.

## 1. Tao–Teräväinen reduce the higher correlation to a product function

Tao and Teräväinen (`MC-S28`, Corollary 1.6) consider `1`-bounded multiplicative functions `g_1,...,g_r`. If their pointwise product

\[
G=g_1\cdots g_r
\tag{4}
\]

does not weakly pretend to any Dirichlet character, then for arbitrary fixed shifts and arbitrary moving logarithmic windows with both endpoints tending to infinity, the normalized logarithmic correlation tends to zero. In particular,

\[
\sum_{n\le x}\frac{g_1(n+h_1)\cdots g_r(n+h_r)}n=o(\log x).
\tag{5}
\]

Their weak-pretence relation is precisely the prime-harmonic condition

\[
\sum_{p\le x}
\frac{1-\operatorname{Re}(G(p)\overline{\chi(p)})}{p}
=o(\log\log x).
\tag{6}
\]

For the self-correlation take every `g_j=a_q`. Since `a_q(n)` takes only the values `-1,0,+1`, an odd number `r` of factors gives the pointwise identity

\[
a_q^r=a_q.
\tag{7}
\]

It therefore remains only to check that `a_q` does not weakly pretend to any Dirichlet character.

## 2. The comparator fails weak pretence by a positive fraction of prime-harmonic mass

Let `chi` be any Dirichlet character of conductor `d`, and put

\[
Q=\operatorname{lcm}(q,d).
\tag{8}
\]

For every prime `p` with

\[
p\equiv1\pmod Q,
\tag{9}
\]

one has `chi(p)=1` and `a_q(p)=sigma_q(p)=-1`. Hence each such prime contributes exactly `2/p` to the weak-pretence sum. Mertens' theorem in arithmetic progressions gives

\[
\sum_{\substack{p\le x\\p\equiv1\pmod Q}}\frac1p
=\frac1{\varphi(Q)}\log\log x+O_Q(1),
\tag{10}
\]

and consequently

\[
\sum_{p\le x}
\frac{1-\operatorname{Re}(a_q(p)\overline{\chi(p)})}{p}
\ge
\left(\frac{2}{\varphi(Q)}+o(1)\right)\log\log x.
\tag{11}
\]

The right-hand side is not `o(log log x)`. Since `chi` was arbitrary, `a_q` does not weakly pretend to any Dirichlet character.

Combining (7), (11), and `MC-S28` proves (2). No zero-free region, analytic continuation of `1/zeta`, or Mertens estimate enters this correlation deduction.

## 3. The correlation hierarchy still coexists with near-linear bias

The higher-correlation conclusion changes none of the Landau–Selberg–Delange calculation in `MC-005`. For

\[
\beta_q=\frac{2}{q-1}>0,
\tag{12}
\]

one still has (3). Therefore for every fixed `c>0`,

\[
\frac{x/(\log x)^{\beta_q}}{x^{1-c}}
=\frac{x^c}{(\log x)^{\beta_q}}
\longrightarrow\infty.
\tag{13}
\]

The obstruction is stronger than simply saying that one-point or two-point qualitative randomness lacks a rate. A single explicit exact-support multiplicative family simultaneously satisfies an **unbounded hierarchy of fixed odd-order logarithmic decorrelation statements** while its anchored mean decays only by a power of `log x`.

This rules out any black-box implication whose hypotheses are exhausted by exact support, multiplicativity, and the collection of qualitative relations (2), and whose conclusion is a fixed power saving for the summatory function.

## 4. Why the odd/even boundary is structural here

The argument deliberately stops at odd `r`. If `r` is even, then

\[
a_q(n)^r=\mu(n)^2,
\tag{14}
\]

so at every prime the product function has value `1`. It therefore weakly pretends to the principal character, and the Tao–Teräväinen product criterion does not force the corresponding even-number-of-factors correlation to vanish.

This is exactly the parity phenomenon behind the odd-order logarithmic Chowla cases in `MC-S28`: their theorem supplies a powerful qualitative hierarchy, but not the missing even-order hierarchy. `MC-039` separately retains the two-factor logarithmic Elliott conclusion because Tao's earlier two-point theorem (`MC-S26`) uses the stronger nonpretentiousness hypothesis on one factor rather than the product criterion used here.

Accordingly, (2) must not be paraphrased as “all higher Chowla correlations”. It covers all **fixed odd numbers of self-correlation factors**. Even numbers of four or more factors, quantitative rates, and growing-complexity correlation families remain outside this finding.

## 5. Prior art and novelty assessment

The theorem-level ingredients are established prior art.

- `MC-S28` proves the general weak-pretence product criterion and explicitly derives the odd-number-of-factors logarithmic Chowla cases.
- `MC-005`, using `MC-S14` and `MC-S15`, already constructs the comparator family and proves the asymptotic (3).
- `MC-039` already establishes exact support, multiplicativity, nonpretentiousness/strong aperiodicity, and qualitative two-point logarithmic Elliott cancellation for the same family.
- `MC-S16` is adjacent literature on square-free-supported multiplicative functions of the form `mu^2 g`.

A targeted audit of the higher-correlation theorem and the adjacent square-free-supported multiplicative-function literature gives no basis for a novelty claim about the component mathematics. **No novelty is claimed.** The durable contribution is the line-specific information audit obtained by composing the explicit comparator with the higher-order product criterion: arbitrarily high fixed odd-order logarithmic decorrelation does not repair the polynomial information deficit already exposed at lower order.

## 6. Boundaries and falsification controls

This obstruction has precise limits.

- It is logarithmically averaged. It says nothing by itself about the same fixed correlations with ordinary Cesàro averaging.
- It is qualitative. The `o(log x)` statement has no polynomial rate uniform in `x`.
- The number of factors and shifts are fixed before `x` tends to infinity. No uniformity in growing order or growing shift complexity is established.
- It covers odd numbers of factors only. The even-factor product collapses to the square-free support and falls outside the weak-pretence vanishing criterion.
- The comparator does not have Möbius's exact prime values: requiring `a(p)=-1` at every prime together with multiplicativity and exact square-free support would simply identify Möbius itself and would not constitute an intermediate explanation.
- No claim is made about Gowers uniformity, polynomially quantitative Chowla, an off-critical-zero model, or a new estimate for the true Mertens function.

The decisive falsification test for a proposed correlation-based route is therefore sharper: it must use information absent from this comparator **and quantify how that information produces polynomial global gain**. Candidate escapes include even-order information with a proved transfer, polynomially quantitative correlation norms over growing shift ranges, local Gowers-type uniformity with an explicit local-to-global bridge, or another Möbius-specific coupling that is independently weaker than the desired Mertens estimate.

## Consequence for the research line

The qualitative-correlation branch is now narrowed beyond fixed two-point testing. Raising correlation order through all fixed odd orders still leaves explicit exact-support multiplicative functions with summatory size `x/log^beta x`.

Further work should therefore not treat “more fixed qualitative logarithmic Chowla identities” as a route toward an RH-scale exponent. A viable correlation mechanism must introduce a **quantitative polynomial information budget**, exploit a genuinely different even-order or growing-scale structure, or identify a Möbius-specific arithmetic coupling whose strength can be audited independently of the target summatory bound.