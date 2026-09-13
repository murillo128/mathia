# AF-322 — Prime middle-singular conditioning has a finite-height polynomial modulus

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `DIOPHANTINE-CONDITIONING`, `SOURCE-SPECIFIC-RECOVERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-320 proves that a centered eight-prime middle-singular phase configuration is exactly recoverable from low harmonics because the deeper denominator singularity `s_3=0` is arithmetically impossible. AF-321 then shows that the elementary rank-one character restriction used in that proof gives no uniform quantitative margin on the larger matched-control class.

For the **actual fixed rational-prime source**, the correct statement lies strictly between those two conclusions.

Fix eight distinct rational primes

\[
P=\{p_1,\ldots,p_8\},
\qquad
Z_P(t)=(p_1^{-it},\ldots,p_8^{-it})\in(S^1)^8.
\tag{1}
\]

Let `A_8` be the union, over all perfect matchings of the eight labelled coordinates, of the four-antipodal-pair strata. Thus `Z\in A_8` exactly when its coordinates can be partitioned into four pairs `(a,b)` with `z_b=-z_a`. Equip `(S^1)^8` with any fixed product metric and put

\[
\delta_P(t)=\operatorname{dist}(Z_P(t),A_8).
\tag{2}
\]

Then there exist constants `c_P>0` and `\kappa_P>0`, depending only on the fixed prime support, such that

\[
\boxed{
\delta_P(t)\ge c_P(1+|t|)^{-\kappa_P}
\qquad(|t|\ge1).
}
\tag{3}
\]

The constants arising from the linear-forms-in-logarithms step are effectively computable. The important point here is the **power-law height dependence**, not a useful numerical value of the exponent.

At the same time,

\[
\boxed{
\inf_{|t|\ge T}\delta_P(t)=0
\qquad\text{for every }T>0.
}
\tag{4}
\]

Indeed, for any fixed perfect matching the four logarithms of its disjoint prime ratios are rationally independent, so the corresponding Kronecker flow is dense in the four-torus and approaches the all-antipodal target arbitrarily closely at arbitrarily large times.

Thus rational-prime arithmetic does **not** restore a positive height-uniform gap from the deeper singular geometry. It supplies something more precise: the prime orbit may approach that geometry, but not faster than a fixed power of its time height.

This converts directly into a quantitative version of the AF-320 denominator exclusion. Define the compact middle-singular set

\[
\mathcal M
=\{Z\in(S^1)^8:s_1(Z)=0,\ e_4(Z)=0\}
\tag{5}
\]

and its deeper singular set

\[
\mathcal D
=\{Z\in\mathcal M:s_3(Z)=0\}.
\tag{6}
\]

AF-320 proves

\[
\mathcal D\subseteq A_8.
\tag{7}
\]

Because `\mathcal M` is compact semialgebraic and `|s_3|^2` is polynomial in the real and imaginary coordinates, the Łojasiewicz distance inequality gives constants `C>0` and `\nu>0` such that

\[
|s_3(Z)|\ge C\,\operatorname{dist}(Z,\mathcal D)^\nu
\qquad(Z\in\mathcal M).
\tag{8}
\]

Combining `(3)`, `(7)`, and `(8)` yields constants `c'_P>0` and `K_P>0` for which every hypothetical eight-prime centered middle-singular hit satisfies

\[
\boxed{
|F_P(3t)|=|s_3(Z_P(t))|
\ge c'_P(1+|t|)^{-K_P}.
}
\tag{9}
\]

Consequently the exact AF-320 product-phase formula

\[
E
=\frac{6s_5-5s_2s_3}{10\overline{s_3}}
\tag{10}
\]

has at worst polynomial denominator deterioration in `|t|` on a fixed rational-prime support. This is a genuine source-specific stability gain over AF-321's rank-one matched controls, while still falling short of uniform conditioning.

Nothing here proves that an exact hit satisfying `s_1=e_4=0` exists. Equation `(9)` is a conditional quantitative constraint on any such hit; the exact incidence problem remains separate.

## 1. Approaching four antipodal pairs produces two small linear forms

It is enough to prove `(3)` for the max chordal metric; all fixed product metrics on the compact torus are equivalent up to constants.

Fix a perfect matching `M`. Suppose first that `Z_P(t)` lies within `\varepsilon` of its antipodal stratum `A_M`, with `\varepsilon` smaller than a fixed absolute constant. For each matched pair `(a,b)`,

\[
|p_a^{-it}+p_b^{-it}|\ll\varepsilon.
\tag{11}
\]

Orient the pair so that

\[
\alpha_{ab}=\left|\log\frac{p_a}{p_b}\right|>0.
\tag{12}
\]

The elementary chord-angle relation then gives an odd integer `q_{ab}` with

\[
\left|t\alpha_{ab}-\pi q_{ab}\right|
\ll\varepsilon.
\tag{13}
\]

Choose any two distinct matched pairs, say `(a,b)` and `(c,d)`, and abbreviate

\[
\alpha=\alpha_{ab},\qquad
\beta=\alpha_{cd},\qquad
q=q_{ab},\qquad r=q_{cd}.
\tag{14}
\]

Write

\[
t\alpha=\pi q+\eta,
\qquad
t\beta=\pi r+\theta,
\qquad
|\eta|+|\theta|\ll\varepsilon.
\tag{15}
\]

Eliminating the common time gives

\[
t(r\alpha-q\beta)=r\eta-q\theta.
\tag{16}
\]

Moreover `(15)` gives

\[
|q|+|r|\ll_P 1+|t|,
\tag{17}
\]

so for `|t|\ge1`,

\[
|r\alpha-q\beta|
\ll_P\varepsilon.
\tag{18}
\]

The two positive rational numbers represented by the disjoint prime ratios are multiplicatively independent. Hence

\[
r\alpha-q\beta\ne0
\tag{19}
\]

for every nonzero integer pair `(q,r)`: exponentiating a zero relation would create a multiplicative relation among four distinct rational primes.

Thus geometric proximity to the four-antipodal stratum forces a **nonzero but small two-logarithm linear form** with coefficients of size `O_P(|t|)`.

## 2. Baker-type lower bounds force a polynomial exclusion tube

Classical lower bounds for linear forms in two logarithms imply the following fixed-source consequence. For multiplicatively independent positive algebraic numbers `u,v`, there are effectively computable constants `c(u,v)>0` and `\kappa(u,v)>0` such that

\[
|m\log u-n\log v|
\ge
c(u,v)\,B^{-\kappa(u,v)},
\qquad
B=\max\{3,|m|,|n|\},
\tag{20}
\]

whenever the linear form is nonzero.

Apply `(20)` to the two disjoint prime ratios in `(18)`. By `(17)`,

\[
|r\alpha-q\beta|
\gg_P(1+|t|)^{-\kappa_M}
\tag{21}
\]

for some exponent depending on the chosen matching. Comparing `(18)` and `(21)` gives

\[
\varepsilon\gg_P(1+|t|)^{-\kappa_M}.
\tag{22}
\]

There are only finitely many perfect matchings. Taking the weakest constants over them proves `(3)` whenever the distance is small; after decreasing `c_P`, the remaining region where the distance is bounded below by a fixed absolute constant is automatic.

This is the quantitative layer not used in AF-311. AF-311 invokes Baker theory to rule out **exact** algebraic-linear relations and shows that this remains generically compatible with pentagon closure. Here the same transcendence technology is used in its genuinely metric form: a nonzero linear form cannot be *too small relative to the integer winding height*. Exact independence and quantitative conditioning are therefore separate resources.

## 3. The polynomial lower bound cannot be upgraded to a positive constant

Fix one perfect matching

\[
M=\{(a_1,b_1),\ldots,(a_4,b_4)\}
\tag{23}
\]

and set

\[
\alpha_j=\log(p_{a_j}/p_{b_j}),
\qquad 1\le j\le4.
\tag{24}
\]

The four real numbers `\alpha_j` are rationally independent. If

\[
\sum_{j=1}^4 n_j\alpha_j=0,
\qquad n_j\in\mathbb Z,
\tag{25}
\]

then exponentiation produces

\[
\prod_{j=1}^4(p_{a_j}/p_{b_j})^{n_j}=1,
\tag{26}
\]

and unique factorization forces all `n_j=0` because the pairs use eight distinct primes.

Kronecker's approximation theorem therefore makes the continuous flow

\[
t\longmapsto
(t\alpha_1,\ldots,t\alpha_4)\pmod{2\pi}
\tag{27}
\]

dense in `(\mathbb R/2\pi\mathbb Z)^4`. In particular, for arbitrarily large `t`, all four coordinates approach

\[
(\pi,\pi,\pi,\pi),
\tag{28}
\]

so all four matched prime ratios approach `-1` simultaneously. Replacing one member of each almost-antipodal pair by the exact antipode of the other produces a point of `A_M` at arbitrarily small distance. This proves `(4)`.

Hence the fixed prime source has exactly the conditioning profile suggested by Arithmetic Fidelity:

\[
\text{no uniform margin}
\quad+\quad
\text{no super-polynomial approach at finite height}.
\tag{29}
\]

The first statement is recurrence; the second is Diophantine arithmetic. Neither can be substituted for the other.

## 4. Łojasiewicz transfers source separation to the AF-320 denominator

On `(S^1)^8`, the conditions defining `\mathcal M` in `(5)` are polynomial conditions in real and imaginary coordinates. Thus `\mathcal M` is compact semialgebraic. The function

\[
g(Z)=|s_3(Z)|^2
\tag{30}
\]

is also polynomial on those coordinates, with zero set inside `\mathcal M` exactly `\mathcal D`.

The classical Łojasiewicz distance inequality on a compact semialgebraic set gives an exponent `N>0` and a constant `C_0>0` such that

\[
\operatorname{dist}(Z,\mathcal D)^N
\le C_0|s_3(Z)|^2
\qquad(Z\in\mathcal M).
\tag{31}
\]

AF-320 proves that `s_1=e_4=s_3=0` forces an even root polynomial and therefore four antipodal pairs. Hence `\mathcal D\subseteq A_8`, so

\[
\operatorname{dist}(Z,\mathcal D)
\ge
\operatorname{dist}(Z,A_8).
\tag{32}
\]

If `Z=Z_P(t)` is an exact middle-singular prime hit, equations `(3)`, `(31)`, and `(32)` yield

\[
|s_3(Z_P(t))|
\ge
C_0^{-1/2}c_P^{N/2}(1+|t|)^{-N\kappa_P/2},
\tag{33}
\]

which is `(9)` after renaming the constants.

This is the same exact-recovery-versus-stable-recovery distinction developed abstractly in AF-246: analytic or semialgebraic exact separation upgrades to a Hölder-type metric relation, while the arithmetic source determines how quickly its orbit may approach the bad zero set. Here Baker-type arithmetic supplies the missing shrinking-target modulus.

For the product-phase map `(10)`, the numerator equals `10E\overline{s_3}` on the exact singular branch. Differentiating the rational expression therefore shows that its local sensitivity to the retained harmonic data is `O(1/|s_3|)` up to fixed bounded harmonic factors. Equation `(9)` consequently gives at most polynomial growth in `|t|` for this phase-recovery condition number on a fixed support. This does not assert uniform stability of the complete polynomial-root reconstruction or labelled-prime recovery.

## Prior art and novelty assessment

No novelty is claimed for any of the three general ingredients.

- Alan Baker's series on linear forms in logarithms, beginning with **“Linear forms in the logarithms of algebraic numbers,”** *Mathematika* 13 (1966), 204–216, DOI `10.1112/S0025579300003971`, establishes the foundational effective theory already used qualitatively in AF-311.
- E. M. Matveev, **“An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II,”** *Izvestiya: Mathematics* 64(6) (2000), 1217–1269, DOI `10.1070/im2000v064n06ABEH000314`, gives general explicit lower bounds. Nicolas Gouillon, **“Explicit lower bounds for linear forms in two logarithms,”** *Journal de théorie des nombres de Bordeaux* 18(1) (2006), 125–146, DOI `10.5802/jtnb.537`, gives a specialized two-logarithm treatment with logarithmic dependence on the coefficient height, hence the power-law form used in `(20)` for fixed algebraic inputs.
- Kronecker approximation is the classical density theorem for nonresonant linear flows on finite tori; it supplies `(4)` once the four disjoint prime-ratio logarithms are seen to be rationally independent.
- The Łojasiewicz distance inequality is classical. AF-246 already audits its use for converting exact analytic zero-set separation into quantitative Hölder stability; the present application is a finite-dimensional semialgebraic specialization.

A targeted literature search located these established components and standard quantitative Diophantine-approximation refinements, but no basis for presenting their combination here as a new theorem in transcendence theory or inverse problems. The durable contribution is the **source-relative conditioning classification** of the AF-320 singular repair: the actual prime-log orbit has zero uniform margin, yet its finite-height approach to the failure stratum is polynomially bounded below.

## Boundaries and failure modes

- The constants depend on the fixed set of eight primes. No bound uniform over growing prime supports is claimed.
- The exponent obtained from general linear-forms-in-logarithms and Łojasiewicz theory may be enormous. The theorem is structural; it does not claim a numerically practical conditioning constant.
- Equation `(4)` concerns approach of the unrestricted fixed-prime time orbit to antipodal geometry. It does **not** prove that exact middle-singular times exist, nor that such exact hits themselves approach `\mathcal D`.
- Equation `(9)` is therefore conditional on `s_1=e_4=0`. It constrains every such hit if one exists but does not settle incidence.
- The Baker argument uses two disjoint pairs. It proves separation from the full four-antipodal-pair union, not from every possible high-symmetry degeneration of an eight-point configuration.
- The result controls the `s_3` denominator in AF-320. It does not prove that `(s_2,s_3,s_4,s_5)` is a globally minimal representation or that all stages of root recovery have the same polynomial condition number.
- Kronecker density and Baker lower bounds are compatible: density says arbitrarily close returns occur, while the Baker estimate limits their speed as a function of return height.
- No zeta zero, critical-line statement, zero-density estimate, or RH implication follows.

## Consequence for the research line

AF-321 showed that **character rank alone** cannot provide quantitative conditioning: rank-one matched controls can approach the deeper singular boundary with no positive denominator margin. AF-322 identifies what the full rational-prime source contributes beyond that rank statement.

The prime-log flow itself also has no positive uniform separation from the four-antipodal geometry, so source arithmetic does not magically remove the instability. But its approach is Diophantine rather than arbitrary: linear forms in logarithms force a power-law finite-height exclusion tube. Combined with the semialgebraic geometry of the singular branch, this yields a power-law lower bound on the exact AF-320 denominator at every hypothetical prime hit.

The eight-point frontier therefore separates cleanly into three questions:

1. **incidence:** does the fixed prime orbit ever satisfy `s_1=e_4=0` exactly? — still open here;
2. **exact recovery:** if it does, is `s_3` nonzero and the product phase recoverable? — yes by AF-320;
3. **stable recovery:** how badly can that denominator deteriorate with source height? — AF-322 gives a fixed-support polynomial modulus, but no height-uniform constant.

This is the quantitative source-discriminator layer requested by the line mandate: the extra arithmetic information is not another exact relation, but a restriction on the **rate at which a compression-failure stratum can be approached**.