# FD-313 — sublinear local gap-block inventories can remain noncoercive

**Status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GROWING-LOCAL-DEPTH + K-ABELIAN-CONTROL`. FD-013 proves that reflection, the complete one-gap multiset, and every ordered adjacent-pair count can agree while cumulative rank-grid quadratic discrepancy differs by an unbounded factor. That obstruction persists far beyond fixed first-order data: for every block depth `L`, one can construct two reflection-symmetric rational grids whose gap-sign words have exactly the same count of **every contiguous block of length at most `L`**, while their cumulative discrepancy energies differ by a factor asymptotic to the number of macroblocks.

More precisely, for every integers `m>=2`, `L>=1` and rational `0<epsilon<1`, there are two rational reflection-symmetric point grids with

\[
n=4m^2L
\tag{1}
\]

positive gaps such that their binary large/small gap words are `L`-Abelian equivalent in the standard combinatorics-on-words sense, yet

\[
\boxed{
\frac{\mathcal E_C}{\mathcal E_R}
=
m^2+O(1)
=
\frac{n}{4L}+O(1),
}
\tag{2}
\]

uniformly for `L>=1` as `m->infinity`. Consequently **any sublinear local block-depth inventory `L=o(n)` can remain noncoercive by an unbounded factor**. In particular, for every fixed `0<=alpha<1` there is a family with

\[
L=n^{\alpha+o(1)}
\quad\text{and}\quad
\frac{\mathcal E_C}{\mathcal E_R}
=
n^{1-\alpha+o(1)}.
\tag{3}
\]

Thus merely letting the preserved local gap-block depth grow polynomially below the full order does not create a universal bridge to cumulative Franel-type discrepancy. Any coercive mechanism must either reach essentially global order information or use additional Farey-specific structure such as denominator labels, mediant ancestry, or another nonlocal arithmetic relation.

## 1. Run-lifting the FD-013 matched pair

Use the two balanced palindromic sign words from FD-013. Their length is

\[
K:=4m^2,
\tag{4}
\]

and we denote them by `s_R=(s_{R,1},...,s_{R,K})` and `s_C=(s_{C,1},...,s_{C,K})`. FD-013 proves that both contain exactly `K/2` plus signs and `K/2` minus signs and have the same complete ordered adjacent-pair inventory

\[
N_{++}=2(m^2-m),
\qquad
N_{--}=2(m^2-m)+1,
\qquad
N_{+-}=N_{-+}=2m-1.
\tag{5}
\]

They are also palindromic.

For an integer `L>=1`, define the run lift

\[
\sigma_L(s_1\cdots s_K)
:=
s_1^L s_2^L\cdots s_K^L,
\tag{6}
\]

where `+^L` means `L` consecutive plus signs and similarly for minus. Put

\[
w_R:=\sigma_L(s_R),
\qquad
w_C:=\sigma_L(s_C).
\tag{7}
\]

Both lifted words have length `n=KL=4m^2L`, remain balanced, and remain palindromic.

## 2. Every local block count through depth L agrees exactly

Fix a block length `1<=ell<=L`. Because each macro-symbol in (6) occupies a run of length `L`, any length-`ell` factor of a lifted word crosses **at most one** macro boundary.

Therefore every factor count is determined only by:

- the number of `+` and `-` macro-symbols;
- the number of the four ordered macro adjacencies `++`, `--`, `+-`, and `-+`;
- the common run length `L`.

Indeed, a mixed factor must have exactly one transition and hence has the form

\[
+^r-^{\ell-r}
\quad\text{or}\quad
-^r+^{\ell-r},
\qquad
1\le r<\ell,
\tag{8}
\]

with one occurrence at each corresponding mixed macro boundary for the prescribed split `r`. Constant factors `+^ell` and `-^ell` receive the same within-run contribution in both words and the same additional crossing contribution from equal-sign macro boundaries. Factors with two or more transitions cannot occur because `ell<=L`.

Since FD-013 gives equality of all macro-symbol and adjacent-pair counts, it follows that for every binary word `v` with `|v|<=L`,

\[
\boxed{
\#_v(w_R)=\#_v(w_C).
}
\tag{9}
\]

In the terminology introduced by Karhumäki--Saarela--Zamboni, the words are therefore `L`-Abelian equivalent.

This is stronger than preserving one chosen depth: the **entire local factor inventory at every depth `1,...,L`** agrees exactly.

## 3. Rational reflection-symmetric point grids

For either lifted sign word `w=(w_1,...,w_n)`, define gaps

\[
g_j:=\frac{1+\varepsilon w_j}{n},
\qquad
1\le j\le n,
\tag{10}
\]

and points

\[
x_0:=0,
\qquad
x_k:=\sum_{j=1}^k g_j.
\tag{11}
\]

Because `0<epsilon<1`, all gaps are positive. Balance gives `x_n=1`. Palindromicity gives

\[
\boxed{
x_{n-k}=1-x_k
\qquad
(0\le k\le n).
}
\tag{12}
\]

For rational `epsilon`, every point is rational. Equation (9) with `|v|=1` also shows that the two grids have exactly the same large/small gap multiset.

Let

\[
S_k(w):=\sum_{j=1}^k w_j.
\tag{13}
\]

Then the rank-grid discrepancy is exactly

\[
x_k-\frac{k}{n}
=
\frac{\varepsilon}{n}S_k(w),
\tag{14}
\]

so the quadratic cumulative energy is

\[
\mathcal E(w)
:=
\sum_{k=1}^{n-1}
\left(x_k-\frac{k}{n}\right)^2
=
\frac{\varepsilon^2}{n^2}
\sum_{k=1}^{n}S_k(w)^2,
\tag{15}
\]

where the final term vanishes by balance.

## 4. Exact run-lift energy identity

Let `s=(s_1,...,s_K)` be any balanced sign word and write

\[
T_j:=\sum_{i=1}^j s_i,
\qquad
T_0=T_K=0,
\tag{16}
\]

and

\[
A(s):=\sum_{j=1}^{K}T_j^2.
\tag{17}
\]

Inside lifted macroblock `j`, after `r` microsteps,

\[
S_{(j-1)L+r}(\sigma_L s)
=
LT_{j-1}+rs_j,
\qquad
1\le r\le L.
\tag{18}
\]

Summing squares gives

\[
\sum_{r=1}^{L}
(LT_{j-1}+rs_j)^2
=
L^3T_{j-1}^2
+
L^2(L+1)T_{j-1}s_j
+
\frac{L(L+1)(2L+1)}6.
\tag{19}
\]

Because `s_j^2=1` and `T_K=0`,

\[
\sum_{j=1}^{K}T_{j-1}s_j
=
\frac12\sum_{j=1}^{K}(T_j^2-T_{j-1}^2-s_j^2)
=
-\frac K2.
\tag{20}
\]

Also `sum_{j=1}^K T_{j-1}^2=A(s)` because `T_0=T_K=0`. Therefore

\[
\boxed{
A(\sigma_L s)
=
L^3A(s)
-
\frac{KL(L^2-1)}6.
}
\tag{21}
\]

The correction depends only on `K` and `L`, not on the ordering of the macro-symbols.

## 5. The energy separation survives every run depth

FD-013 gives for the regular macro-word

\[
A(s_R)
=
\frac{2m^2(2m^2+1)}3.
\tag{22}
\]

For the clustered macro-word, with

\[
B:=m^2-m+1,
\tag{23}
\]

it gives

\[
A(s_C)
=
2\left[
\frac{B(2B^2+1)}3
+
(m-1)(2B^2-2B+1)
\right].
\tag{24}
\]

Substituting `K=4m^2` into (21) and simplifying yields

\[
\boxed{
A(w_R)
=
\frac{2Lm^2}{3}
\left(2L^2m^2+1\right),
}
\tag{25}
\]

and

\[
\boxed{
A(w_C)
=
\frac{2Lm}{3}
\left(
2L^2m^5
-6L^2m^3
+10L^2m^2
-6L^2m
+2L^2
+m
\right).
}
\tag{26}
\]

Hence, since the common factor `epsilon^2/n^2` in (15) cancels,

\[
\frac{\mathcal E_C}{\mathcal E_R}
=
\frac{
2L^2m^5
-6L^2m^3
+10L^2m^2
-6L^2m
+2L^2
+m
}{
m(2L^2m^2+1)
}.
\tag{27}
\]

Uniformly for `L>=1`,

\[
\boxed{
\frac{\mathcal E_C}{\mathcal E_R}
=
m^2+O(1).
}
\tag{28}
\]

Since `n=4m^2L`,

\[
\boxed{
\frac{\mathcal E_C}{\mathcal E_R}
=
\frac{n}{4L}+O(1).
}
\tag{29}
\]

Thus whenever `L=o(n)` along the constructed family, the ratio diverges.

For a fixed `0<=alpha<1`, choose for example

\[
L=\left\lfloor
m^{2\alpha/(1-\alpha)}
\right\rfloor
\tag{30}
\]

(with `L=1` at `alpha=0`). Then

\[
n=4m^2L
=
m^{2/(1-\alpha)+o(1)},
\tag{31}
\]

so

\[
L=n^{\alpha+o(1)}
\tag{32}
\]

and (28) becomes

\[
\boxed{
\frac{\mathcal E_C}{\mathcal E_R}
=
n^{1-\alpha+o(1)}.
}
\tag{33}
\]

The local observation depth may therefore grow as any fixed sublinear power of the grid size and still fail to control cumulative discrepancy by a bounded factor.

## 6. Prior art and novelty boundary

The relevant combinatorics-on-words notion is classical. Juhani Karhumäki, Aleksi Saarela and Luca Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, Journal of Combinatorial Theory, Series A **120**(8) (2013), 2189--2206, DOI `10.1016/j.jcta.2013.08.008`, defines `k`-Abelian equivalence exactly by equality of occurrence counts for every factor of length at most `k`. No novelty is claimed for that equivalence relation or for the general fact that local factor inventories need not determine a word.

The present construction is elementary and deliberately narrower. The Mathia-specific result is the quantitative matched-control obstruction: **within one exact growing `L`-Abelian class, while balance and ordinary reflection symmetry are also fixed, cumulative rank-grid quadratic discrepancy can vary by a factor `n/(4L)+O(1)`**. The closest `k`-Abelian literature located in the prior-art audit studies equivalence classes, complexity, switching, repetitions, periodicity, and palindromic variants; no theorem located there supplies or contradicts this cumulative prefix-square discrepancy comparison. Accordingly the classification is `LITERATURE+EXACT-DERIVED`, not a broad claim of novelty in word combinatorics.

The construction remains source-agnostic. The grids are rational matched controls, not Farey sequences. They do not preserve denominator labels, mediant parentage, Stern--Brocot ancestry, or other Farey arithmetic.

## 7. Consequence for the Farey branch

FD-013 ruled out first-order local gap type as a universal coercive explanation. The current result removes the natural repair “let the local block depth grow with the order” throughout the entire sublinear regime.

A statistic whose hypotheses retain only the complete contiguous gap-block inventory through depth `L=o(n)`, even together with exact reflection and the one-gap multiset, cannot by itself imply a fixed-factor bound on cumulative rank-grid energy: the two families above obey all those constraints while (29) diverges.

This does **not** show that local data are useless for the actual Farey sequence. It shows that local block counts alone are not the missing coercive bridge. The live alternatives are narrower:

- local depth comparable to the full order, where the observation is no longer genuinely local;
- local blocks augmented by denominator strata or mediant/Farey-parent ancestry;
- another long-range arithmetic relation that distinguishes configurations inside the same growing `L`-Abelian class.

For `CLUE-farey-gap-order-bridge-suppression`, this kills sublinear block-depth preservation as a standalone theorem-level bridge while leaving the genuinely Farey-specific denominator/mediant branch open.

## 8. Audit boundaries

The conclusion depends only on exact finite word combinatorics and the FD-013 macro construction.

- Equality (9) is exact for every factor length at most `L`; it is not a moment approximation.
- Reflection is ordinary word palindromicity transported through positive gaps.
- The energy ratio is exact through (27); (28)--(33) are asymptotic consequences.
- The theorem says nothing about the actual distribution of Farey local blocks.
- A control retaining symbol positions, denominator labels, ancestry, or blocks of linear depth is outside the obstruction.
- No RH consequence, Möbius cancellation estimate, or new Franel--Landau bound is claimed.
