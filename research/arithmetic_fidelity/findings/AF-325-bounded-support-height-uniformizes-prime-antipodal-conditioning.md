# AF-325 — Bounded support height uniformizes prime antipodal conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-CONSEQUENCE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `DIOPHANTINE-CONDITIONING`, `SUPPORT-HEIGHT`, `SOURCE-SPECIFIC-RECOVERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-322 gives a polynomial-in-time exclusion tube from four-antipodal geometry for each **fixed** eight-prime support, but with support-dependent constants. AF-323 proves that no positive modulus depending on time alone can hold uniformly over unrestricted supports, and AF-324 prices the opposite direction by showing that supports of height at most `H` can approach every fixed phase geometry at a polynomial rate in `H`.

The missing joint resource statement is quantitative and unconditional: once the largest prime is retained as a height parameter, the Baker--Wüstholz lower bound can be made uniform over **all** supports below that height.

Let

\[
P=\{p_1,\ldots,p_8\},\qquad p_j\le H,
\]

be eight distinct rational primes, let

\[
Z_P(t)=(p_1^{-it},\ldots,p_8^{-it})\in(S^1)^8,
\]

and let `A_8` be the union of the four-antipodal-pair strata from AF-322. Put

\[
\delta_P(t)=\operatorname{dist}(Z_P(t),A_8)
\]

for any fixed product metric on the torus. There is an absolute constant `C>0` such that, for all sufficiently large `H` and all `|t|\ge1`,

\[
\boxed{
\delta_P(t)
\ge
\exp\!\left[-C(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right]
}
\tag{1}
\]

uniformly over every eight-prime support `P\subset[2,H]`.

Thus the support dependence in AF-322 can be priced explicitly. A finite prime-height budget does not restore a fixed open gap, but it converts the unspecified constants `c_P,\kappa_P` into one joint modulus in **time height and support height**.

At fixed nonzero time `\tau`, define

\[
\Delta_\tau(H)
=
\inf_{\substack{P:\ |P|=8\\ \max P\le H}}
\delta_P(\tau).
\tag{2}
\]

Combining `(1)` with the constructive upper bound of AF-324 gives, for sufficiently large `H`,

\[
\boxed{
\exp\!\left[-C(\log H)^2
\log\!\bigl(e+|\tau|\log H\bigr)\right]
\le
\Delta_\tau(H)
\ll_\tau H^{-19/40}.
}
\tag{3}
\]

The gap is enormous and no sharp asymptotic is claimed. What `(3)` establishes is the correct **two-resource topology**: support height makes the prime family finite and therefore separated from the exact antipodal locus, while classical logarithmic-form estimates quantify how badly that separation may deteriorate as both support and time grow.

There is also a direct consequence for the AF-320 denominator. Let

\[
\mathcal M=\{Z:s_1(Z)=e_4(Z)=0\},\qquad
\mathcal D=\{Z\in\mathcal M:s_3(Z)=0\}.
\]

AF-320 proves `\mathcal D\subseteq A_8`. The compact semialgebraic Łojasiewicz inequality used in AF-322 is support-independent, so there is another absolute constant `C_1>0` such that every hypothetical exact middle-singular prime hit with `\max P\le H` and `|t|\ge1` obeys

\[
\boxed{
|s_3(Z_P(t))|
\ge
\exp\!\left[-C_1(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
}
\tag{4}
\]

Consequently the denominator deterioration in the exact AF-320 product-phase recovery formula is at worst the reciprocal of this joint modulus. This does **not** prove that an exact hit `s_1=e_4=0` exists or does not exist.

## 1. Near an antipodal matching, two small logarithmic forms appear

Work first with the max chordal metric; changing to another fixed product metric only changes absolute constants. Suppose `Z_P(t)` is within a sufficiently small `\varepsilon` of one antipodal matching `M`. Choose two disjoint matched pairs `(a,b)` and `(c,d)`. Orient them so that

\[
u=\frac{\max(p_a,p_b)}{\min(p_a,p_b)}>1,
\qquad
v=\frac{\max(p_c,p_d)}{\min(p_c,p_d)}>1,
\]

and write

\[
\alpha=\log u,\qquad \beta=\log v.
\]

The chord-angle comparison gives odd integers `q,r` and errors `\eta,\theta` with

\[
t\alpha=\pi q+\eta,
\qquad
t\beta=\pi r+\theta,
\qquad
|\eta|+|\theta|\ll\varepsilon.
\tag{5}
\]

Because `u,v\le H`,

\[
|q|+|r|\ll 1+|t|\log H.
\tag{6}
\]

Eliminating the common time gives

\[
t(r\alpha-q\beta)=r\eta-q\theta,
\]

and therefore, for `|t|\ge1`,

\[
|r\alpha-q\beta|
\ll (\log H)\varepsilon.
\tag{7}
\]

The rational numbers `u` and `v` are multiplicatively independent: their prime supports are disjoint, so a relation `u^r=v^q` would contradict unique factorization. Hence the linear form in `(7)` is nonzero.

## 2. Baker--Wüstholz makes the support dependence explicit

For a reduced positive rational `a/b`, its logarithmic Weil height is

\[
h(a/b)=\log\max(a,b).
\]

Thus both rational inputs above have modified logarithmic height bounded by `O(\log H)`. The Baker--Wüstholz theorem for a nonzero integer linear form in two logarithms gives an absolute constant `C_0` such that

\[
\log|r\log u-q\log v|
\ge
-C_0(\log H)^2\log B,
\tag{8}
\]

where one may take

\[
B\ll e+|t|\log H
\tag{9}
\]

by `(6)`. Equivalently,

\[
|r\alpha-q\beta|
\ge
\exp\!\left[-C_2(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
\tag{10}
\]

Comparing `(7)` and `(10)`, and absorbing the extra factor `\log H` by enlarging the absolute constant, yields `(1)` whenever the distance to `A_8` is small. If the distance is bounded below by a fixed absolute constant, `(1)` is automatic after the same enlargement of `C`. Taking the minimum over the finitely many perfect matchings costs only another absolute constant.

This is precisely the dependence hidden in AF-322. There the algebraic inputs were fixed, so their heights disappeared into `c_P,\kappa_P`. Bounding every prime by `H` keeps the same proof but makes the algebraic-height factor uniform: two logarithms contribute the product `O((\log H)^2)`.

## 3. Support height and time height are genuinely different resources

For fixed `H`, equation `(1)` is an inverse-power bound in `|t|`, recovering the qualitative shape of AF-322 uniformly across the finitely many supports below `H`.

For fixed nonzero `\tau`, AF-324 constructs supports below `H` with

\[
\delta_P(\tau)\ll_\tau H^{-19/40}.
\tag{11}
\]

Equation `(1)` supplies the simultaneous lower bound in `(3)`. The two statements are compatible because the Baker--Wüstholz lower envelope decays much faster in `H` than the currently available constructive upper envelope.

The point is not the numerical width of `(3)`. It is that the vague statement “retain the support” can now be split into an explicit resource question. If a downstream compression discards the exact prime labels but retains only a bound `H`, then every stability theorem must consume a modulus at least as weak as the joint envelope allowed by `(1)--(3)`. A claim of support-uniform conditioning without such a resource is already excluded by AF-323.

## 4. Transfer to the middle-singular denominator

On the compact semialgebraic set `\mathcal M`, the zero set of `|s_3|` is `\mathcal D`. As in AF-322, a global Łojasiewicz distance inequality supplies constants `A>0` and `N>0`, independent of the prime support, with

\[
|s_3(Z)|\ge A\,\operatorname{dist}(Z,\mathcal D)^N
\qquad(Z\in\mathcal M).
\tag{12}
\]

Since `\mathcal D\subseteq A_8`,

\[
\operatorname{dist}(Z,\mathcal D)
\ge
\operatorname{dist}(Z,A_8).
\tag{13}
\]

For an exact prime middle-singular hit, `(1)`, `(12)`, and `(13)` imply `(4)` after absorbing `A,N` into the absolute constant. Thus the source-height mark does more than restore set-theoretic finiteness: it gives a quantitative condition-number budget for the harmonic recovery step.

The theorem still stops before the exact incidence question. Near-incidence is abundant by AF-324; exact middle-singular incidence remains the decisive arithmetic boundary.

## Prior art and novelty assessment

No novelty is claimed for the Diophantine ingredient or for effective Kronecker methods.

- A. Baker and G. Wüstholz, **“Logarithmic forms and group varieties,”** *Journal für die reine und angewandte Mathematik* 442 (1993), 19--62, DOI `10.1515/crll.1993.442.19`, give the effective lower bound whose rational two-logarithm specialization has logarithmic coefficient-height dependence and product dependence on the modified heights of the algebraic inputs.
- E. M. Matveev, **“An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II,”** *Izvestiya: Mathematics* 64(6) (2000), 1217--1269, DOI `10.1070/im2000v064n06ABEH000314`, gives another standard explicit form of the same general height-sensitive technology.
- G. J. Rieger, **“Effective simultaneous approximation of complex numbers by conjugate algebraic integers,”** *Acta Arithmetica* 63(4) (1993), 325--334, DOI `10.4064/aa-63-4-325-334`, explicitly develops an effective Kronecker approximation theorem using Baker estimates for logarithms of primes. This is direct prior art for the general strategy of turning logarithmic-form bounds into quantitative torus-approximation control.

The literature search therefore gives no basis for claiming a new transcendence or effective-Kronecker theorem. The durable Arithmetic Fidelity contribution is narrower: combining the classical height dependence with AF-322's antipodal reduction and AF-324's support-height covering theorem yields a **joint source-resource window** for the exact singular-recovery problem. It replaces an unspecified support-dependent modulus by an explicit `H,t` dependence.

## Boundaries and failure modes

- The exponent and constants are structural, not numerically optimized. Specialized two-logarithm estimates can improve constants without changing the resource law used here.
- The bound is for eight distinct rational primes below `H`; it does not cover repeated coordinates, generalized primes, or support families with a different height notion.
- Equation `(1)` controls distance to the union of four-antipodal-pair strata. It does not lower-bound distance to every possible singular or high-symmetry subset of the torus.
- Equation `(4)` is conditional on an exact middle-singular hit `s_1=e_4=0`; the theorem neither proves nor disproves such incidence.
- AF-324 supplies only a near-incidence upper bound, so `(3)` is not an asymptotic formula and does not close the large gap between current lower and upper scales.
- The support-height mark `H` is weaker than retaining the exact prime support. A downstream representation that keeps more provenance may admit better conditioning, but that improvement must be demonstrated in the target metric actually consumed.
- No Riemann zero, critical-line, zero-density, or RH consequence follows directly.

## Consequence for the research line

AF-322 and AF-323 separated fixed-support recovery from support-uniform recovery. AF-324 then quantified how fast bounded-height supports can reproduce bad ambient geometry. AF-325 closes the complementary quantitative side: **bounded support height also uniformizes the Baker exclusion modulus**, producing an explicit two-resource window in `H` and `t`.

The remaining frontier is no longer “do support-dependent constants exist?” but whether exact rational-prime incidence `s_1=e_4=0` occurs at all, and, if it does, whether the joint modulus `(4)` is strong enough for the downstream analytic operation that would have to consume the recovered arithmetic discriminator.