# MC-039 — Strong aperiodicity and logarithmic Elliott cancellation still permit near-linear partial sums

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The exact-support multiplicative comparator family from `MC-005` satisfies substantially more qualitative cancellation structure than that finding used. For every fixed prime `q>=5`, let

\[
\sigma_q(p)=
\begin{cases}
-1,&p\equiv1\pmod q,\\
+1,&p\not\equiv1\pmod q,
\end{cases}
\tag{1}
\]

extend `sigma_q` completely multiplicatively, and set

\[
a_q(n)=\mu(n)^2\sigma_q(n).
\tag{2}
\]

Then:

1. `a_q` is multiplicative and has exactly Möbius square-free support,
   \[
   |a_q(n)|=\mu(n)^2;
   \tag{3}
   \]
2. the completely multiplicative prime-sign lift `sigma_q` is nonpretentious and, being finitely generated, is strongly aperiodic in the corrected pretentious-distance sense;
3. because `a_q(p)=sigma_q(p)` at every prime, `a_q` satisfies the same strong nonpretentiousness hypothesis in Tao's logarithmically averaged Elliott theorem. Consequently, for every `1`-bounded multiplicative function `g`, every fixed integer linear forms
   \[
   L_1(n)=a_1n+b_1,\qquad L_2(n)=a_2n+b_2
   \]
   with `a_1,a_2>0` and `a_1 b_2-a_2 b_1 != 0`, and every function `1<=omega(x)<=x` with `omega(x)->infinity`, one has
   \[
   \boxed{
   \sum_{x/\omega(x)<n\le x}
   \frac{a_q(L_1(n))g(L_2(n))}{n}
   =o(\log\omega(x))
   }
   \tag{4}
   \]
   whenever the linear forms are positive on the summation range. In particular, taking `g=a_q` gives qualitative logarithmically averaged two-point Elliott/Chowla cancellation for every fixed nonzero shift;
4. nevertheless `MC-005` gives the positive asymptotic
   \[
   \boxed{
   \sum_{n\le x}a_q(n)
   \sim C_q\frac{x}{(\log x)^{2/(q-1)}}
   }
   \qquad(C_q>0),
   \tag{5}
   \]
   and hence these partial sums violate `O(x^(1-c))` for every fixed `c>0`.

Therefore **exact Möbius support, multiplicativity, corrected strong aperiodicity, and all qualitative logarithmically averaged two-point Elliott tests against bounded multiplicative comparators still do not contain a polynomial global-cancellation budget.** Any route from correlation information to an RH-relevant Mertens exponent must use quantitatively stronger information, a non-logarithmic/growing-complexity regime, higher-order structure, or an additional arithmetic mechanism specific enough to exclude this family.

This is stronger than either of the earlier black-box obstructions separately. `MC-004` allowed full qualitative fixed-shift Chowla behavior but discarded multiplicativity; `MC-005` retained exact support and multiplicativity but used only one-point qualitative mean cancellation. The present result places the explicit multiplicative family of `MC-005` inside the corrected strong-aperiodic regime and then imports Tao's full qualitative logarithmic two-point Elliott conclusion.

## 1. The comparator is nonpretentious

Only the prime-sign lift is needed for the pretentiousness audit. Suppose, for contradiction, that for some Dirichlet character `chi` and real `t`,

\[
\mathbb D(\sigma_q,\chi(n)n^{it};\infty)^2
=
\sum_p
\frac{1-\operatorname{Re}(\sigma_q(p)\overline{\chi(p)}p^{-it})}{p}
<\infty,
\tag{6}
\]

where the finitely many primes dividing the conductor of `chi` are harmless.

For unit complex `z`,

\[
1-\operatorname{Re}(z^2)\le4(1-\operatorname{Re}z).
\tag{7}
\]

Since `sigma_q(p)^2=1`, squaring the prime phases in (6) therefore gives

\[
\sum_p
\frac{1-\operatorname{Re}(\overline{\chi(p)}^{\,2}p^{-2it})}{p}
<\infty.
\tag{8}
\]

The classical prime-harmonic form of character orthogonality now forces `t=0` and `chi^2` to be principal. Indeed, unless both conditions hold, the twisted prime reciprocal sum

\[
\sum_{p\le x}\frac{\chi(p)^2p^{2it}}p
\]

has bounded real part as `x->infinity`, whereas `sum_(p<=x)1/p` diverges, making (8) impossible. Thus `chi(p)` is `+1` or `-1` away from its conductor.

Let `r` be the conductor of `chi` and `Q=lcm(q,r)`. Every prime

\[
p\equiv1\pmod Q
\tag{9}
\]

satisfies `chi(p)=1` and `sigma_q(p)=-1`. Mertens' theorem in arithmetic progressions gives

\[
\sum_{\substack{p\le x\\p\equiv1\ (\mathrm{mod}\ Q)}}\frac1p
\sim\frac1{\varphi(Q)}\log\log x,
\tag{10}
\]

so this residue class alone contributes a divergent amount to (6). This contradiction proves that `sigma_q` is nonpretentious.

The argument is deliberately qualitative. For example, against the principal character at `t=0`, the distance grows only at logarithmic-prime scale,

\[
\mathbb D(\sigma_q,1;x)^2
=2\sum_{\substack{p\le x\\p\equiv1\ (\mathrm{mod}\ q)}}\frac1p
=\frac{2}{q-1}\log\log x+O_q(1).
\tag{11}
\]

Thus ordinary nonpretentiousness does not itself supply a power-sized information parameter, in agreement with the ceiling isolated in `MC-002`.

## 2. Finitely generated nonpretentiousness upgrades to strong aperiodicity

The prime values of `sigma_q` lie in the finite set `{-1,+1}`. Charamaras, Mountakis and Tsinas (`MC-S27`, Proposition 2.5) prove that a nonpretentious finitely generated completely multiplicative function on the unit circle is strongly aperiodic. Applied to `sigma_q`, this gives, for every fixed `A>=1` and every Dirichlet character `chi`,

\[
\inf_{|t|\le Ax}
\sum_{p\le x}
\frac{1-\operatorname{Re}(\sigma_q(p)\overline{\chi(p)}p^{-it})}{p}
\longrightarrow\infty.
\tag{12}
\]

The distinction matters because the corrected Elliott conjecture requires this uniform-in-`t` divergence rather than mere nonpretentiousness for each fixed twist.

Although `a_q` itself is not completely multiplicative—its prime powers of exponent at least two vanish—it has **exactly the same prime values** as `sigma_q`. Condition (12), and hence Tao's hypothesis below, depends only on prime values. Therefore (12) holds verbatim with `a_q(p)` in place of `sigma_q(p)`.

## 3. Tao's logarithmic Elliott theorem gives every fixed two-point multiplicative test

Tao's logarithmically averaged Elliott theorem (`MC-S26`, Corollary 1.5) applies to arbitrary `1`-bounded multiplicative functions `g_1,g_2` when `g_1` satisfies precisely the corrected strong nonpretentiousness condition (12). Taking

\[
g_1=a_q,\qquad g_2=g
\tag{13}
\]

proves (4) for every fixed non-proportional pair of linear forms and every `omega(x)->infinity`.

For the self-correlation, take `g=a_q`, `L_1(n)=n` and `L_2(n)=n+h` with fixed positive `h`. Then

\[
\sum_{x/\omega(x)<n\le x}
\frac{a_q(n)a_q(n+h)}n
=o(\log\omega(x)).
\tag{14}
\]

In particular `omega(x)=x` gives

\[
\frac1{\log x}
\sum_{n\le x}\frac{a_q(n)a_q(n+h)}n
\longrightarrow0.
\tag{15}
\]

Thus this is not merely a multiplicative sequence with a slowly vanishing one-point mean. It passes the entire qualitative family of **logarithmically averaged two-point multiplicative-correlation tests** supplied by the corrected Elliott theorem.

## 4. Yet the anchored partial sum remains almost linear

Nothing in Sections 1–3 changes the Landau–Selberg–Delange asymptotic already proved in `MC-005`. With

\[
\beta_q=\frac{2}{q-1}>0,
\tag{16}
\]

that result gives (5). Hence for every fixed `c>0`,

\[
\frac{x/(\log x)^{\beta_q}}{x^{1-c}}
=
\frac{x^c}{(\log x)^{\beta_q}}
\longrightarrow\infty.
\tag{17}
\]

So no black-box theorem whose hypotheses consist only of the structural properties above can conclude a fixed power saving for the anchored sum.

This also explains why there is no tension with `MC-006`. That finding quantified what van der Corput needs from averaged correlations: a power saving in the global sum requires polynomially small normalized correlation mass at a polynomial shift range. Equation (4) is qualitative `o(log omega)` information. Strong aperiodicity ensures that the logarithmic correlation eventually vanishes after normalization, but neither Tao's theorem nor the present construction supplies a polynomial rate in `x` capable of meeting the budget in `MC-006`.

## 5. Prior art and novelty assessment

Every theorem-level ingredient is established prior art.

- The explicit family, its exact support, and the asymptotic (5) are already persisted in `MC-005`; the asymptotic is a standard Landau–Selberg–Delange consequence anchored by `MC-S14` and the prime number theorem in arithmetic progressions `MC-S15`.
- Tao's `MC-S26` proves the corrected logarithmically averaged two-point Elliott theorem for strongly nonpretentious bounded multiplicative functions.
- Charamaras–Mountakis–Tsinas `MC-S27` proves that a nonpretentious finitely generated completely multiplicative function is strongly aperiodic.
- `MC-S16` is direct adjacent literature on the same square-free-supported multiplicative class.

A targeted audit across these sources and adjacent square-free-supported multiplicative-function literature did not identify a basis for claiming a new theorem about the comparator class itself. **No novelty is claimed for the component results or terminology.** The durable contribution here is the line-specific information audit: the same explicit matched-control family that defeats power cancellation in `MC-005` also survives the corrected strong-aperiodicity gate and therefore inherits all qualitative logarithmic two-point Elliott correlations.

## 6. Boundaries and falsification controls

The obstruction is strong but specific.

- It concerns **logarithmically averaged** two-point correlations. It does not show that the ordinary unweighted Elliott/Chowla correlation holds for `a_q`.
- The theorem is qualitative in its final `o(log omega)` decay. It does not provide a polynomial rate uniform over a growing family of shifts.
- It is a two-point result. No claim is made here that `a_q` satisfies all higher-order Chowla correlations.
- The prime signs do not match Möbius: `a_q(p)` is usually `+1`, whereas `mu(p)=-1` for every prime. Requiring exact prime values together with exact support and multiplicativity reconstructs Möbius and is not an intermediate explanation.
- Strong aperiodicity excludes every bounded-conductor character/Archimedean twist, but it does not prohibit a slowly accumulating prime bias of the type in (11). Thus qualitative strong aperiodicity should not be confused with a power-sized quantitative distance.
- Nothing here models an off-critical zero, proves a new bound for `M(x)`, or weakens the RH-equivalent Mertens target.

The decisive falsification test for any proposed correlation-based escape is now sharper than after `MC-005`: the proposed input must exclude this family **for a quantitative reason that survives after exact support, multiplicativity, strong aperiodicity, and qualitative logarithmic two-point Elliott cancellation have all been matched**. Examples that remain genuinely outside this obstruction include polynomially quantitative growing-shift correlation estimates, ordinary unweighted correlations with a sufficiently strong rate, higher-order information with a proved polynomial transfer, or an arithmetic coupling that uses Möbius's exact all-minus prime law without simply encoding Möbius itself.

## Consequence for the research line

The natural idea "combine multiplicativity with qualitative correlation randomness" is now substantially narrowed. The intersection of those two qualitative properties is still large enough to contain explicit exact-support functions with summatory size `x/log^beta x`.

Accordingly, the live local-to-global problem should not spend further effort proving additional **qualitative fixed-complexity logarithmic decorrelation** and expecting a power exponent to emerge automatically. A viable continuation must identify where polynomial information enters: a quantitative correlation norm, a growing-scale constraint, a signed multiscale coupling, or another Möbius-specific mechanism whose strength can be audited before it is used to control the anchored sum.