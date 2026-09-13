# AF-327 — Prime height-time separation keeps the lacunary moment Gram quantitatively interior

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-CONSEQUENCE`, `ARITHMETIC-FIDELITY`, `TRIGONOMETRIC-MOMENT`, `DIOPHANTINE-CONDITIONING`, `SOURCE-SPECIFIC-RECOVERY`, `QUANTITATIVE-FIDELITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Let

\[
P=\{p_1,\ldots,p_8\},\qquad p_j\le H,
\]

be eight distinct rational primes, let `t\ne0`, and write

\[
z_j=p_j^{-it},
\qquad
F_P(u)=\sum_{j=1}^8p_j^{-iu},
\qquad
s_k=\sum_{j=1}^8z_j^k=F_P(kt),
\qquad
m_k=\frac{s_k}{8}.
\tag{1}
\]

Consider the four-feature moment Gram matrix indexed by the lacunary monomials `1,z,z^2,z^4`,

\[
G_{0124}(Z)
=
\left(m_{a-b}\right)_{a,b\in\{0,1,2,4\}},
\qquad m_{-k}=\overline{m_k},
\tag{2}
\]

and put

\[
D_{0124}(Z)=\det G_{0124}(Z)\ge0.
\tag{3}
\]

Then two distinct statements hold.

First, at every nonzero common prime time,

\[
\boxed{D_{0124}(Z_P(t))>0.}
\tag{4}
\]

Thus the rational-prime source never reaches the rank-deficient boundary of this retained four-feature moment representation.

Second, the strictness has a uniform finite-resource modulus. There is an absolute constant `C>0` such that, for all sufficiently large `H` and every `|t|\ge1`,

\[
\boxed{
D_{0124}(Z_P(t))
\ge
\exp\!\left[-C(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
}
\tag{5}
\]

The exponent and constant are structural rather than optimized. The point is that the support-height/time-height resource law from AF-325 propagates to the **whole Gram-boundary slack**, not only to the AF-320 denominator `|s_3|` or the extremal second-harmonic gap of AF-326.

For a hypothetical exact centered middle-singular hit

\[
s_1=0,\qquad e_4=0,
\tag{6}
\]

put

\[
x=|s_2|,\qquad y=|s_3|.
\]

AF-326's moment matrix is the same `G_{0124}` up to the harmless transpose convention for moments. After a common rotation and direct rescaling,

\[
4096D_{0124}
=
8(16-x^2)(32+x^2)-(64-x^2)y^2.
\tag{7}
\]

Hence every such prime hit with `p_j\le H`, `|t|\ge1` obeys the quantitatively strict form of the AF-326 tradeoff

\[
\boxed{
8(16-|F_P(2t)|^2)(32+|F_P(2t)|^2)
-
(64-|F_P(2t)|^2)|F_P(3t)|^2
\ge
\exp\!\left[-C(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
}
\tag{8}
\]

After enlarging `C`, the fixed numerical factor `4096` is absorbed into the same envelope.

Equation `(8)` is stronger in direction than merely combining the AF-325 lower bound on `|s_3|` with `|s_2|<4`: it separates the prime source from the **entire equality face** of AF-326's exact curved moment inequality.

There is also an operator-conditioning consequence. Since `G_{0124}` is positive semidefinite with trace `4`,

\[
\lambda_{\min}(G_{0124})
\ge \frac{27}{64}D_{0124},
\tag{9}
\]

so the four retained monomial features have condition number at most the reciprocal of the same height-time envelope, up to an absolute factor. This controls only this feature Gram; it is not a condition-number theorem for complete root or prime recovery.

## 1. Cauchy--Binet exposes the exact boundary certificate

Let `V` be the `4\times8` feature matrix

\[
V_{a,j}=z_j^a,
\qquad a\in\{0,1,2,4\}.
\tag{10}
\]

Then

\[
G_{0124}=\frac18VV^*.
\tag{11}
\]

Cauchy--Binet therefore gives

\[
D_{0124}(Z)
=
\frac1{8^4}
\sum_{\substack{I\subset\{1,\ldots,8\}\\|I|=4}}
|\det V_I|^2.
\tag{12}
\]

For four variables `w_1,\ldots,w_4`, the generalized Vandermonde determinant with exponents `0,1,2,4` is the first Schur alternant beyond the ordinary Vandermonde:

\[
\det\!
\begin{pmatrix}
1&1&1&1\\
w_1&w_2&w_3&w_4\\
w_1^2&w_2^2&w_3^2&w_4^2\\
w_1^4&w_2^4&w_3^4&w_4^4
\end{pmatrix}
=
\left(\sum_{j=1}^4w_j\right)
\prod_{1\le a<b\le4}(w_b-w_a),
\tag{13}
\]

up to the irrelevant sign convention for the Vandermonde factor. Thus `(12)` becomes the explicit positive certificate

\[
\boxed{
D_{0124}(Z)
=
\frac1{8^4}
\sum_{|I|=4}
\left|\sum_{i\in I}z_i\right|^2
\prod_{\substack{a<b\\a,b\in I}}|z_b-z_a|^2.
}
\tag{14}
\]

This formula separates two ways in which a four-subset can fail to witness rank: collision of support points through the Vandermonde factor, or exact four-point closure through the marked sum. No arithmetic input has entered yet.

## 2. Rank deficiency forces support collapse

Let

\[
\mathcal C=\{Z\in(S^1)^8:D_{0124}(Z)=0\}.
\tag{15}
\]

If `Z\in\mathcal C`, then `V` has row rank below four. Hence there is a nonzero lacunary polynomial

\[
q(w)=c_0+c_1w+c_2w^2+c_4w^4
\tag{16}
\]

such that

\[
q(z_j)=0
\qquad(1\le j\le8).
\tag{17}
\]

A nonzero polynomial of degree at most four has at most four distinct roots. Therefore

\[
\boxed{
Z\in\mathcal C
\Longrightarrow
\#\{z_1,\ldots,z_8\}\le4.
}
\tag{18}
\]

The converse is not asserted: four distinct support points need not make `(16)` possible because the cubic coefficient is constrained to vanish. Only the implication `(18)` is needed.

Eight labels occupying at most four phase values necessarily contain at least two **disjoint** equal-coordinate pairs. Let

\[
\mathcal E_2
=
\bigcup_{\substack{\{a,b\},\{c,d\}\text{ disjoint}}}
\{Z:z_a=z_b,\ z_c=z_d\}.
\tag{19}
\]

Then

\[
\boxed{\mathcal C\subseteq\mathcal E_2.}
\tag{20}
\]

For a distinct-prime common-time point, membership in `\mathcal E_2` would provide two independent normalized character relations. AF-310 proves that the relation lattice of such a prime phase point is cyclic. Hence `Z_P(t)\notin\mathcal E_2`, and `(20)` proves the exact strictness `(4)`.

This argument is source-specific in precisely the intended sense. The Gram boundary itself is large and classical; rational-prime multiplicative independence prevents the source orbit from entering the part of that boundary compatible with eight labelled coordinates.

## 3. Two near-collisions give a uniform logarithmic-form obstruction

The exact relation-rank argument has no metric content by itself. To obtain `(5)`, first quantify distance from the larger collision set `\mathcal E_2`.

Use the max chordal product metric; any other fixed product metric changes only absolute constants. Suppose `Z_P(t)` lies within `\varepsilon` of one component of `\mathcal E_2`. Then for four distinct indices `a,b,c,d`,

\[
|p_a^{-it}-p_b^{-it}|\ll\varepsilon,
\qquad
|p_c^{-it}-p_d^{-it}|\ll\varepsilon.
\tag{21}
\]

Orient the two ratios above `1` and put

\[
u=\frac{\max(p_a,p_b)}{\min(p_a,p_b)},
\qquad
v=\frac{\max(p_c,p_d)}{\min(p_c,p_d)},
\qquad
\alpha=\log u,
\qquad
\beta=\log v.
\tag{22}
\]

For sufficiently small `\varepsilon`, the chord-angle comparison gives integers `q,r` and errors `\eta,\theta` with

\[
t\alpha=2\pi q+\eta,
\qquad
t\beta=2\pi r+\theta,
\qquad
|\eta|+|\theta|\ll\varepsilon.
\tag{23}
\]

Moreover

\[
|q|+|r|\ll1+|t|\log H.
\tag{24}
\]

If one winding, say `q`, is zero, then

\[
|t|\alpha\ll\varepsilon.
\]

Distinct primes below `H` satisfy

\[
\alpha\ge\log(1+H^{-1})\gg H^{-1},
\]

so `\varepsilon\gg H^{-1}`. For sufficiently large `H`, this is already stronger than the envelope claimed below.

Assume therefore that both windings are nonzero. Eliminating the common time from `(23)` gives

\[
t(r\alpha-q\beta)=r\eta-q\theta,
\tag{25}
\]

and hence, using `(24)` and `|t|\ge1`,

\[
|r\alpha-q\beta|
\ll (1+\log H)\varepsilon.
\tag{26}
\]

The rational numbers `u` and `v` have disjoint prime supports and are multiplicatively independent. Thus the logarithmic form in `(26)` is nonzero. Their logarithmic heights are `O(\log H)`, while the integer coefficient height is at most `O(e+|t|\log H)`. The Baker--Wüstholz lower bound used in AF-325 therefore yields an absolute `C_0>0` such that

\[
|r\alpha-q\beta|
\ge
\exp\!\left[-C_0(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
\tag{27}
\]

Comparing `(26)` and `(27)`, and absorbing the harmless `1+\log H` factor into the exponent, gives

\[
\boxed{
\operatorname{dist}(Z_P(t),\mathcal E_2)
\ge
\exp\!\left[-C_1(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
}
\tag{28}
\]

There are only finitely many choices of two disjoint pairs, so one absolute constant handles the full union. If the distance is not in the small-angle regime, `(28)` is automatic after enlarging the constant.

The difference from AF-325 is geometric. There the two small logarithmic forms were extracted from a four-antipodal-pair target. Here they arise from the collision geometry forced by rank loss of the retained lacunary features.

## 4. Łojasiewicz transfers source separation to Gram slack

The torus `(S^1)^8` is compact semialgebraic and `D_{0124}` is a nonnegative polynomial in the real and imaginary coordinates restricted to that torus. Its zero set is `\mathcal C` from `(15)`. The compact semialgebraic Łojasiewicz distance inequality supplies absolute constants `A>0` and `N>0` such that

\[
D_{0124}(Z)
\ge
A\,\operatorname{dist}(Z,\mathcal C)^N.
\tag{29}
\]

Because `\mathcal C\subseteq\mathcal E_2`,

\[
\operatorname{dist}(Z,\mathcal C)
\ge
\operatorname{dist}(Z,\mathcal E_2).
\tag{30}
\]

Equations `(28)--(30)` give

\[
D_{0124}(Z_P(t))
\ge
A\exp\!\left[-NC_1(\log H)^2
\log\!\bigl(e+|t|\log H\bigr)\right].
\tag{31}
\]

Absorbing `A` and `N` into one absolute constant proves `(5)`.

This is the same two-stage fidelity pattern used in AF-322 and AF-325, now with a different target defect: arithmetic excludes rapid approach to a source-incompatible relation stratum, and semialgebraic target geometry converts that source separation into a quantitative observable margin.

## 5. The singular tradeoff gains an interior margin

Assume now `(6)`. As in AF-326, rotate all phases by a common unit scalar so that

\[
m_2=r\ge0.
\]

The middle-singular Newton identity gives

\[
m_4=4r^2,
\]

and the Gram matrix `(2)` becomes

\[
G_{0124}
=
\begin{pmatrix}
1&0&r&4r^2\\
0&1&0&\overline{m_3}\\
r&0&1&r\\
4r^2&m_3&r&1
\end{pmatrix}.
\tag{32}
\]

AF-326 computes

\[
D_{0124}
=
(1-4r^2)(1+2r^2)-(1-r^2)|m_3|^2.
\tag{33}
\]

With

\[
r=\frac{|s_2|}{8},
\qquad
|m_3|=\frac{|s_3|}{8},
\]

this is exactly `(7)`. Combining `(5)` with `(7)` proves `(8)`.

AF-326 already showed that moment positivity forces the left side of `(8)` to be nonnegative. AF-327 adds the source-specific statement that a bounded-height rational-prime orbit cannot make that slack arbitrarily small at finite time. The previously transferred margin `4-|s_2|` sees only one extremal face; `D_{0124}` sees failure of the complete four-feature Gram.

For the eigenvalue claim, write the four eigenvalues of `G_{0124}` as

\[
0<\lambda_1\le\lambda_2\le\lambda_3\le\lambda_4,
\qquad
\sum_{j=1}^4\lambda_j=4.
\]

The arithmetic-geometric mean inequality gives

\[
\lambda_2\lambda_3\lambda_4
\le
\left(\frac{4-\lambda_1}{3}\right)^3
\le\left(\frac43\right)^3.
\]

Therefore

\[
D_{0124}
=\lambda_1\lambda_2\lambda_3\lambda_4
\le\frac{64}{27}\lambda_1,
\]

which is `(9)`. Since `\lambda_{\max}\le4`, the spectral condition number satisfies

\[
\kappa_2(G_{0124})
\le\frac{256}{27D_{0124}}.
\tag{34}
\]

Thus the same retained source resources control a genuine matrix-conditioning quantity, not only a scalar reconstruction denominator.

## 6. No positive time-uniform margin is available

Equation `(5)` should not be misread as a fixed gap. For a fixed prime support `P`, the seven normalized logarithmic frequencies

\[
\log(p_j/p_8),\qquad 1\le j\le7,
\]

are rationally independent. Kronecker's theorem makes the normalized common-time orbit dense in `(S^1)^7`. Hence there are arbitrarily large times at which all eight phases become arbitrarily close to one common phase.

The diagonal configuration has rank one in `(10)`, so `D_{0124}=0` there. By continuity,

\[
\boxed{
\inf_{|t|\ge T}D_{0124}(Z_P(t))=0
\qquad\text{for every }T>0.
}
\tag{35}
\]

For fixed `H`, `(5)` is therefore correctly interpreted as an inverse-power-type finite-height barrier, not a uniform positive separation. Recurrence supplies arbitrarily poor conditioning; arithmetic controls how fast that degeneration can occur as the time height grows.

## Prior art and novelty assessment

Every general ingredient is classical, and no broad novelty claim is made.

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2012/2013), is standard background for Gram matrices, rank, eigenvalue conditioning and Cauchy--Binet determinant identities.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), is standard background for alternants and Schur-polynomial factorizations; `(13)` is the elementary partition-`(1)` bialternant identity.
- Barry Simon, *Orthogonal Polynomials on the Unit Circle*, AMS Colloquium Publications 54, Part 2 (2005), DOI `10.1090/coll/054.2`, and Nikolaï Nikolski, *Toeplitz Matrices and Operators*, Cambridge University Press (2020), Chapter 5, DOI `10.1017/9781108182577.006`, are direct prior art for unit-circle moment Gram/Toeplitz positivity.
- A. Baker and G. Wüstholz, **“Logarithmic forms and group varieties,”** *Journal für die reine und angewandte Mathematik* 442 (1993), 19--62, DOI `10.1515/crll.1993.442.19`, supply the height-sensitive logarithmic-form estimate used in `(27)`; AF-325 already audits its specialization to bounded rational-prime supports.
- The Łojasiewicz distance inequality for compact semialgebraic sets is classical real algebraic geometry and is already audited in AF-322 for the same type of source-to-target margin transfer.

A targeted literature search also located the standard Cauchy--Binet Gram determinant formula and the generalized-Vandermonde/Schur bialternant framework, but no basis for treating `(12)--(14)` or the Baker/Łojasiewicz composition as a new theorem of matrix analysis, moment theory, or transcendence theory. The durable Arithmetic Fidelity result is the narrower source-relative statement `(5)`: the rational-prime height/time budget forces a quantitative interior margin for the particular retained feature Gram that generated AF-326's singular tradeoff.

## Boundaries and failure modes

- The exact strictness `(4)` uses eight **distinct rational primes** and a common nonzero time through AF-310's cyclic relation-lattice theorem. Generic eight-point unit-circle configurations need not enjoy the same source restriction.
- The quantitative bound `(5)` assumes `p_j\le H` and `|t|\ge1`. The constant/exponent are not optimized and may be numerically useless.
- `D_{0124}>0` means only that the four monomial features `1,z,z^2,z^4` are linearly independent in the empirical `L^2` space. It does not by itself reconstruct all eight phases, their prime labels, or `t`.
- The implication `\mathcal C\subseteq\mathcal E_2` is intentionally one-way. Two coordinate collisions do not in general force `D_{0124}=0`.
- Equation `(8)` is conditional on exact middle-singular incidence `s_1=e_4=0`; it neither proves nor disproves the existence of such a prime time.
- The Gram condition number `(34)` is not the condition number of the AF-320 root-reconstruction map. Root separation and the `s_3` denominator remain additional conditioning layers.
- Kronecker recurrence `(35)` rules out replacing the finite-height modulus by a positive constant even for one fixed prime support.
- Nothing here establishes a zeta zero, critical-line, zero-density or RH consequence.

## Consequence for the research line

AF-325 priced the arithmetic source separation in support height and time height; AF-326 transferred it into the extremal second-harmonic margin. AF-327 shows that the same resource survives one level more structurally: it keeps the **entire lacunary moment Gram** quantitatively away from rank loss and therefore keeps the exact AF-326 curved inequality away from equality.

The live frontier remains the exact incidence question `s_1=e_4=0`. What has changed is the conditioning picture of any hypothetical hit. At bounded support height and finite time it must lie not merely away from the deeper `s_3=0` denominator singularity and the face `|s_2|=4`, but quantitatively inside the full four-feature moment cone. A downstream compression that claims to retain equivalent stability now has a sharper target to preserve: the Gram interior margin `(5)`, not only one scalar harmonic gap.