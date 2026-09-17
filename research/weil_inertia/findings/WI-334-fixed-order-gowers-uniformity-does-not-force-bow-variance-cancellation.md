# WI-334 — fixed-order Gowers uniformity does not force bow variance cancellation

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + PRIOR-ART-REDIRECT`.

The higher-uniformity theorems of Matomäki--Radziwiłł--Shao--Tao--Teräväinen (MRSTT) do not by themselves cross the bow `L^2` gate of WI-195. The obstruction is stronger than the logarithmic norm mismatch already recorded in WI-332 and the one-point polynomial-phase countermodel of WI-333: **arbitrarily high but fixed-order local Gowers uniformity, even with a power saving and on every interval at the bow scale, can coexist with full diagonal-scale sliding variance against a prescribed unit-modulus carrier.**

Precisely, fix

\[
0<\kappa<1,\qquad S\ge2,
\qquad K=\lfloor N^\kappa\rfloor,
\]

and any prescribed sequence `u_n` with `|u_n|=1`. For all sufficiently large `N` there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad \varepsilon_n\in\{-1,+1\},
\tag{1}
\]

such that simultaneously:

1. for every integer interval `I subset [1,N]` with `K <= |I| <= 2K` and every `2 <= s <= S`, using exactly the interval normalization adopted by MRSTT,

\[
\boxed{
\|b\|_{U^s(I)}
\ll_S
\sqrt{\log N}\,K^{-1/(4\cdot 2^s)}
=o(1);
}
\tag{2}
\]

2. the quadratic sliding statistic retains its whole diagonal scale,

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{3}
\]

The construction is the probabilistic method with independent Rademacher signs. Equation (2) follows from a cube-degeneracy count plus bounded-differences concentration, uniformly over all `K`-scale intervals and all fixed orders `s<=S`; equation (3) follows from the exact diagonal expectation and a fourth-moment overlap bound. The two high-probability events intersect.

Thus the published MRSTT statement

\[
\|\Lambda-\Lambda_w\|_{U^s(x,x+H]}=o_{w\to\infty}(1)
\]

for every **fixed** `s` in almost all intervals cannot, when used merely as a black-box Gowers-norm input, imply the source-level cancellation required by WI-195. The countermodel satisfies a substantially stronger interface -- all starts, all interval lengths between `K` and `2K`, finitely many arbitrary fixed orders at once, and explicit power decay -- while its prescribed-carrier sliding variance is still diagonal-sized.

This does **not** say that the actual prime source `Lambda-Lambda^sharp` has diagonal bow variance, nor does it obstruct an argument using its signed two-point arithmetic, a quantitatively much stronger norm at a `K`-dependent order, a source identity before Cauchy--Schwarz losses, or another invariant that is absent from (2). It closes only the tempting shortcut “invoke higher local Gowers uniformity, perhaps after a finite PET/Taylor reduction, and deduce the WI-195 `o(XK log X)` square from that norm information alone.”

## 1. Exact interface being tested

WI-195 reduces the unresolved bow source term, on a central dyadic prime block, to a short-interval square of the schematic form

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+K}
(\Lambda(n)-\Lambda_X^\sharp(n))n^{iU}
\right|^2dx,
\tag{4}
\]

with required bound `o(XK log X)`. The raw diagonal of (4) has size `asymp XK log X`. Therefore success requires a signed off-diagonal covariance of the same macroscopic order as the diagonal; mere decorrelation at an `o(1)` average scale is not automatically enough.

MRSTT's 2026 almost-all-interval theorem makes a natural stronger-uniformity route look attractive. Their Theorem 1.3 defines

\[
\|f\|_{U^s(I)}
:=
\frac{\|f1_I\|_{U^s(\mathbb Z)}}
     {\|1_I\|_{U^s(\mathbb Z)}}
\tag{5}
\]

and, in the prime case for interval lengths above `X^(1/3+epsilon)`, proves local `U^s` smallness for every fixed `s` outside an exceptional set of starts. In the surviving fixed-power bow range the natural short length is above that exponent threshold, so one might hope to Taylor-expand the distinguished carrier on `K`-blocks and then use sufficiently high fixed Gowers order or a finite PET argument.

The issue is logical before it is technical: a fixed-order Gowers norm controls specific finite-complexity additive patterns. The bow square needs a much finer statement -- a weighted sum of two-point covariances large enough in aggregate to cancel a diagonal of order `K log N` per ambient site. The following construction separates those two interfaces exactly.

## 2. Random signs have power-small local Gowers norms on every `K`-scale interval

Let `(epsilon_n)_{1<=n<=N}` be independent Rademacher variables. Fix an integer interval `I` of length `L` and `s>=2`. Write

\[
Q_{s,I}
:=\|\varepsilon 1_I\|_{U^s(\mathbb Z)}^{2^s},
\qquad
D_{s,I}
:=\|1_I\|_{U^s(\mathbb Z)}^{2^s}.
\tag{6}
\]

Thus

\[
\|\varepsilon\|_{U^s(I)}^{2^s}
=\frac{Q_{s,I}}{D_{s,I}}.
\tag{7}
\]

The denominator counts additive `s`-cubes whose vertices all lie in `I`. Restricting `x` to a fixed central subinterval and every `h_j` to a fixed symmetric interval of length `asymp_s L` gives

\[
c_sL^{s+1}\le D_{s,I}\le C_sL^{s+1}.
\tag{8}
\]

For the numerator, a cube contributes nonzero expectation only when every Rademacher variable occurring among its vertices occurs with even multiplicity. In particular the cube must be degenerate: two distinct vertices coincide. For a fixed pair `omega != omega'`, this imposes the nontrivial linear equation

\[
(\omega-\omega')\cdot h=0.
\tag{9}
\]

There are `O_s(L^{s-1})` choices of `h` satisfying one such equation and `O(L)` choices of the base point. Summing over the finitely many vertex pairs gives

\[
\mathbb E Q_{s,I}=O_s(L^s),
\qquad
\mathbb E\frac{Q_{s,I}}{D_{s,I}}=O_s(L^{-1}).
\tag{10}
\]

Now regard

\[
F_{s,I}:=Q_{s,I}/D_{s,I}
\tag{11}
\]

as a function of the `L` independent signs in `I`. Flipping one sign changes only cubes containing that site. There are `O_s(L^s)` such cubes, each monomial changes by at most `2`, and (8) therefore gives the bounded-difference estimate

\[
|\Delta F_{s,I}|\ll_s L^{-1}.
\tag{12}
\]

The bounded-differences inequality consequently yields, for every `t>0`,

\[
\mathbb P\!\left(
F_{s,I}-\mathbb EF_{s,I}>t
\right)
\le
\exp(-c_sLt^2).
\tag{13}
\]

Take `t=L^(-1/4)`. Uniformly for `K<=L<=2K`,

\[
\mathbb P\!\left(
F_{s,I}>C_sL^{-1/4}
\right)
\le
\exp(-c_sL^{1/2})
\tag{14}
\]

for large `L`. There are fewer than `2NK` integer intervals in `[1,N]` having a length in `[K,2K]`. Since `K=N^{kappa+o(1)}`, a union bound over all these intervals and the fixed finite set `2<=s<=S` gives, with probability `1-o(1)`,

\[
\|\varepsilon\|_{U^s(I)}
\ll_S K^{-1/(4\cdot2^s)}
\tag{15}
\]

simultaneously for every such `I` and every `s<=S`. Multiplication by the constant `sqrt(log N)` in (1) proves (2).

Two features are worth isolating. First, this is an **all-interval** statement, not merely an almost-all-start statement. Second, the norm tends to zero by a fixed power of `K`, far stronger than a qualitative `o(1)` interface. The exponent in (2) is not claimed optimal; it is chosen because the elementary concentration argument already suffices for the obstruction.

## 3. The same sequence retains diagonal sliding variance against any prescribed carrier

Fix now an arbitrary deterministic unit-modulus sequence `(u_n)`. Put

\[
S_x:=\sum_{j=1}^K\varepsilon_{x+j}u_{x+j},
\qquad
V:=\sum_{x=0}^{N-K}|S_x|^2.
\tag{16}
\]

Independence and `|u_n|=1` give the exact diagonal expectation

\[
\mathbb EV=(N-K+1)K.
\tag{17}
\]

A standard fourth-moment expansion for a Rademacher sum gives uniformly in `x`

\[
\mathbb E|S_x|^4\le3K^2.
\tag{18}
\]

If `|x-y|>=K`, then `S_x` and `S_y` depend on disjoint sign sets, so `|S_x|^2` and `|S_y|^2` are independent and their covariance vanishes. There are only `O(NK)` pairs of overlapping windows. By Cauchy--Schwarz and (18), every remaining covariance is `O(K^2)`. Hence

\[
\operatorname{Var}(V)=O(NK^3).
\tag{19}
\]

Because `K/N=N^{kappa-1+o(1)} -> 0`, equations (17)--(19) and Chebyshev imply

\[
V=(1+o(1))NK
\tag{20}
\]

with probability `1-o(1)`. The high-probability event (20) intersects the simultaneous Gowers event from Section 2. Choosing one realization in the intersection and rescaling by `sqrt(log N)` gives exactly (3).

The scaling in (1) is deliberate rather than cosmetic:

\[
\sum_{n\le N}|b_n|^2=N\log N,
\tag{21}
\]

so the model has the same `log N` quadratic-energy scale as the von-Mangoldt diagonal entering WI-195. What it deliberately does **not** reproduce is the signed arithmetic covariance of the primes. That missing information is precisely what the counterexample shows cannot be reconstructed from finitely many local Gowers norms alone.

For integer `K`, the corresponding continuous sliding integral over real `x` is piecewise constant between consecutive integers, so the same construction also gives the continuous-window analogue of (3), up to the harmless endpoint interval. Thus the obstruction is not an artifact of replacing WI-195's integrated square by a discrete sampling of starts.

## 4. Why finite PET or a bounded-degree Taylor expansion does not change the conclusion

On a `K`-block the distinguished bow phase `U log(1+h/n)` can, for each fixed-power bow exponent, be Taylor-expanded to any prescribed power accuracy by taking a sufficiently large but **fixed** degree. This observation does not make MRSTT's fixed-order Gowers conclusion strong enough by itself.

Indeed, `S` in the construction above is arbitrary before `N` tends to infinity. Any finite Cauchy--Schwarz/PET reduction that consumes only the local norms

\[
U^2,U^3,\ldots,U^S
\tag{22}
\]

therefore has an admissible model in which every one of those norms is power-small while the target sliding square is still `(1+o(1))NK log N`. Equivalently, there is no universal implication of the form

\[
\bigl(\|b\|_{U^s(I)}=o(1)
\text{ for every fixed }s\le S\bigr)
\Longrightarrow
V=o(NK\log N)
\tag{23}
\]

under only the diagonal-energy normalization (21).

This is fully consistent with generalized von Neumann theory. Fixed-order Gowers control forces cancellation for bounded-complexity averages at their **natural average scale**. The Fejer/sliding-square expansion carries overlap weights of order `K`, and WI-195 needs a signed covariance accurate enough to cancel a diagonal whose per-site size is `K log N`. A qualitative `o(1)` correlation statement loses the quantitative `1/K`-level information that such a cancellation can require.

The countermodel does not exclude a future theorem giving a much stronger `K`-dependent quantitative bound, a Gowers order growing with `N`, or a relative estimate carrying additional arithmetic linear-forms data. Those would be genuinely different inputs from the published fixed-`s` norm surface.

## 5. Relation to WI-332, WI-333, and the accepted bow clue

WI-332 showed that the currently exposed local `U^2` control remains at the wrong quantitative scale for the bow diagonal. WI-333 then constructed sequences with strong fixed-degree one-point polynomial-phase pseudorandomness but full diagonal sliding variance, proving that one-point decorrelation is structurally insufficient.

The present result closes the most immediate attempted escape from WI-333: “replace one-point phase tests by the full fixed-order Gowers hierarchy supplied by MRSTT.” For every finite hierarchy depth, the Rademacher construction satisfies an all-start, power-decaying version of that information and still fails the bow conclusion maximally at leading scale.

Therefore the accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` remains correctly posed. Its decisive target is not generic pseudorandomness but a **source-fixed signed two-point statement**, for example an asymptotic forcing the off-diagonal to be `-D+o(D)`, or a canonical source identity that subtracts the diagonal before absolute-value/norm losses. WI-334 does not decide whether that arithmetic statement is true; it shows that the published higher-uniformity norm information cannot decide it on its own.

## 6. Prior art and novelty boundary

The primary modern input being tested is Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. Their Section 1.2 gives exactly the normalized interval Gowers norm (5), and Theorem 1.3 proves small `U^s` norm for every fixed `s` in the relevant almost-all prime intervals. The theorem is a genuine arithmetic result; nothing here challenges it.

Small Gowers norms for random functions are standard in additive combinatorics. For example, the literature routinely treats random functions as the baseline small-uniformity model, and Fouvry--Kowalski--Michel, **An inverse theorem for Gowers norms of trace functions over F_p**, *Math. Proc. Cambridge Philos. Soc.* 155 (2013), 277--295, explicitly compares its examples with the Gowers norms of random functions. The bounded-differences proof above is included so that the particular all-short-interval statement needed here does not rely on a vague appeal to that heuristic.

A bounded prior-art audit did not locate a published statement combining all three features used here: simultaneous power-small interval `U^s` norms for every fixed `s<=S`, the `log N` diagonal-energy normalization, and preservation of diagonal-scale sliding variance against an arbitrary prescribed carrier. No priority claim is made for the probabilistic ingredients. The line-specific mathematical delta is the exact separation of the MRSTT fixed-order Gowers interface from the WI-195 bow `L^2` requirement.

## 7. Boundary conditions and falsification

The countermodel is an information-interface obstruction, not a model of the primes. It can be evaded by any theorem that uses arithmetic data not encoded in (2) and (21). In particular it does not obstruct:

- an exact or asymptotic signed shifted-prime covariance at the distinguished bow twist;
- a bilinear/dispersion identity that preserves the source before taking absolute values;
- a canonical source-fixed subtraction eliminating the diagonal term;
- local uniformity estimates with strength depending explicitly on `K` beyond the range realized in (2);
- Gowers order increasing with `N` together with a quantitatively effective theorem at that order;
- additional linear-forms/singular-series information tying the two prime factors together.

Conversely, any proposed proof that claims to derive the WI-195 `o(XK log X)` gate only from finitely many statements `||f||_{U^s(I)}=o(1)` (even uniformly in all `K`-scale intervals), plus an `L^2` diagonal of order `X log X`, is falsified by (1)--(3).

A direct audit of WI-334 therefore has two load-bearing checks: verify the degenerate-cube count and bounded-differences normalization in (8)--(15), and verify the overlap variance estimate (17)--(20). Both are finite elementary probability/combinatorics arguments and do not consume an unproved zeta or prime-correlation input.

## Research consequence

The fixed-order higher-Gowers shortcut is closed as a standalone route to the bow square. The live source-side problem is narrower: obtain genuinely **signed two-point information at the distinguished carrier and at the `K log X` covariance scale**, or expose a source identity that removes the diagonal before a generic uniformity norm is asked to act. This reinforces, rather than resolves, the current accepted bow clue.
