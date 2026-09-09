# FD-013 — reflection and adjacent gap type do not control cumulative rank discrepancy

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MATCHED-LOCAL-ORDER-CONTROL + FIRST-ORDER-MARKOV-NONCOERCIVITY`. The live ordered Farey branch asks whether local gap order can explain suppression that survives the one-gap multiset, exact reflection, endpoint controls, and the scalar/global discrepancy factorization. `FD-011` already shows that raw fixed-lag Plücker minors remain inside classical Farey-index algebra. There is a more basic obstruction on the matched-control side: even preserving the **entire one-gap multiset, exact reflection symmetry, and every ordered adjacent gap-pair count** does not control cumulative rank-grid quadratic discrepancy up to any fixed factor.

For every integer `m>=2` and rational `0<epsilon<1`, there are two reflection-symmetric rational point grids with `n=4m^2` positive gaps, the same `n/2` large and `n/2` small gaps, and the same complete `2 x 2` adjacent transition-count matrix, but whose cumulative quadratic discrepancy energies differ by a factor asymptotic to `m^2=n/4`. Thus a first-order local-order null can be a useful empirical control, but it cannot by itself support a universal coercive bridge to Franel-type cumulative energy. Any such bridge must retain deeper/growing order or genuinely Farey-specific denominator, mediant, or ancestry information.

## 1. Two symmetric binary gap words with identical adjacent type

Fix `m>=2`, put

\[
n:=4m^2,
\qquad
A:=m^2-m+1,
\tag{1}
\]

and use signs `+1` and `-1`. Define two half-words of length `2m^2` by

\[
H_R:=(+^m-^m)^m,
\tag{2}
\]

and

\[
H_C:=+^A(-+)^{m-1}-^A.
\tag{3}
\]

Both halves contain exactly `m^2` plus signs and `m^2` minus signs. Form the full palindromic words

\[
s_R:=H_R\,\operatorname{rev}(H_R),
\qquad
s_C:=H_C\,\operatorname{rev}(H_C).
\tag{4}
\]

For either word `s=(s_1,...,s_n)`, define positive gaps

\[
g_j:=\frac{1+\varepsilon s_j}{n},
\qquad
1\le j\le n,
\tag{5}
\]

and cumulative points

\[
x_0:=0,
\qquad
x_k:=\sum_{j=1}^k g_j,
\qquad
1\le k\le n.
\tag{6}
\]

Because each word is balanced, `x_n=1`. Because it is palindromic,

\[
\boxed{x_{n-k}=1-x_k\qquad(0\le k\le n).}
\tag{7}
\]

Thus both point grids have exact reflection symmetry. If `epsilon` is rational, every `x_k` is rational. The gap multiset is also identical in both cases: exactly `n/2` gaps equal `(1+epsilon)/n` and `n/2` equal `(1-epsilon)/n`.

The half-words have the same linear adjacent transition counts. Direct inspection gives

\[
N_{++}(H_R)=N_{++}(H_C)=m(m-1),
\]

\[
N_{--}(H_R)=N_{--}(H_C)=m(m-1),
\]

\[
N_{+-}(H_R)=N_{+-}(H_C)=m,
\qquad
N_{-+}(H_R)=N_{-+}(H_C)=m-1.
\tag{8}
\]

Reversal swaps the mixed transition counts and preserves the equal-sign counts. Since each half ends with `-`, the central join in (4) contributes one additional `--`. Therefore the two full words have exactly the same ordered adjacent-pair inventory:

\[
\boxed{
N_{++}=2(m^2-m),
\quad
N_{--}=2(m^2-m)+1,
\quad
N_{+-}=N_{-+}=2m-1.
}
\tag{9}
\]

If one uses cyclic rather than linear adjacent counts, the closing edge contributes one `++` to both words, so equality of the complete transition matrix still holds. Hence the two controls agree on the one-gap empirical law, the complete first-order ordered pair law, and reflection.

## 2. The cumulative quadratic energies separate by an unbounded factor

Let

\[
S_k:=\sum_{j=1}^k s_j.
\tag{10}
\]

Equation (5) gives the exact rank-grid discrepancy

\[
x_k-\frac{k}{n}
=\frac{\varepsilon}{n}S_k.
\tag{11}
\]

Define

\[
\mathcal E(s)
:=\sum_{k=1}^{n-1}
\left(x_k-\frac{k}{n}\right)^2.
\tag{12}
\]

Since `S_n=0`,

\[
\boxed{
\mathcal E(s)
=\frac{\varepsilon^2}{n^2}
\sum_{k=1}^n S_k^2.
}
\tag{13}
\]

For the regular half-word, one `+^m-^m` block has squared-prefix sum

\[
m^2+2\sum_{j=1}^{m-1}j^2
=\frac{m(2m^2+1)}3.
\]

There are `m` such blocks, each returning to zero. The reflected second half contributes the same amount. Hence

\[
\sum_{k=1}^n S_k(s_R)^2
=\frac{2m^2(2m^2+1)}3,
\tag{14}
\]

and therefore

\[
\boxed{
\mathcal E_R
=\frac{\varepsilon^2(2m^2+1)}{24m^2}
\longrightarrow\frac{\varepsilon^2}{12}.
}
\tag{15}
\]

For the clustered half-word, the initial `+^A` ramp and final `-^A` ramp contribute together

\[
\frac{A(2A^2+1)}3,
\]

while each of the `m-1` middle `-+` pairs contributes

\[
(A-1)^2+A^2=2A^2-2A+1.
\]

Reflection again doubles the half-word energy, giving

\[
\sum_{k=1}^n S_k(s_C)^2
=2\left[
\frac{A(2A^2+1)}3
+(m-1)(2A^2-2A+1)
\right].
\tag{16}
\]

Since `n=4m^2`,

\[
\boxed{
\mathcal E_C
=\frac{\varepsilon^2}{8m^4}
\left[
\frac{A(2A^2+1)}3
+(m-1)(2A^2-2A+1)
\right].
}
\tag{17}
\]

With `A=m^2-m+1`, the leading term is

\[
\boxed{
\mathcal E_C
=\frac{\varepsilon^2m^2}{12}
+O(\varepsilon^2m)
=\frac{\varepsilon^2 n}{48}
+O(\varepsilon^2\sqrt n).
}
\tag{18}
\]

Combining (15) and (18),

\[
\boxed{
\frac{\mathcal E_C}{\mathcal E_R}
=m^2+O(m)
=\frac n4+O(\sqrt n).
}
\tag{19}
\]

The separation is therefore unbounded although all data in (7), the full gap multiset, and (9) agree exactly.

## 3. Consequence for local-order Farey controls

The construction is deliberately source-agnostic. It does **not** say that actual Farey gaps behave like either word, and it does not preserve denominator labels, mediant ancestry, or higher local blocks. Its role is to calibrate what a proposed matched null can logically prove.

Any statistic or theorem whose hypotheses see only

1. the multiset of two gap values (or equivalently the one-step empirical gap law),
2. exact reflection symmetry, and
3. the complete ordered adjacent-pair count matrix,

cannot give a uniform upper or lower comparison for the cumulative rank-grid energy (12): the two families satisfy all three hypotheses while their energies differ by (19). In first-order Markov terminology, the local transition type is identical while the integrated path geometry is not.

This sharpens `CLUE-farey-gap-order-bridge-suppression.md`. Preserving adjacent-gap pairs is a legitimate stronger finite null than preserving only the gap multiset, but **adjacent-pair preservation is not itself a coercive mechanism**. If actual Farey spectral allocation remains exceptional under such a null, the mathematical explanation must use information the pair matrix discards: growing-depth blocks, long-range order, denominator strata, mediant/refinement ancestry, or another source-conditioned relation. Conversely, disappearance under that null would still be useful empirical evidence that first-order order explains the diagnostic; the present theorem does not predict the actual Farey outcome.

The result also stays outside `FD-011`'s raw Plücker classification. No determinant carrier is introduced here. Instead, (19) is an exact matched-control obstruction showing that a first-order local inventory can fail before any exterior-algebra scalarization is attempted.

## 4. Prior art and evidence boundary

Fixed-`h` local Farey spacing laws are classical; Augustin, Boca, Cobeli and Zaharescu, *The h-spacing distribution between Farey points*, Mathematical Proceedings of the Cambridge Philosophical Society **131**(1) (2001), 23--38, DOI `10.1017/S0305004101005187`, is a primary boundary for that literature. Exact adjacent-pair frequency data are the standard first-order Markov-type statistic; Jacquet, Knessl and Szpankowski, *Counting Markov Types*, DMTCS Proceedings vol. AM, AofA'10 (2010), DOI `10.46298/dmtcs.2768`, is a convenient terminology boundary. García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI `10.3390/math14142543`, explicitly studies how a fixed Farey gap multiset and its ordering affect average local discrepancy, so neither gap-order sensitivity nor same-gap permutation controls are claimed as new.

The construction (2)--(19) is elementary and self-contained. The Mathia-specific contribution is the exact control boundary needed by the current Farey program: **even after reflection and the entire first-order ordered gap type are fixed, cumulative quadratic rank discrepancy remains noncoercive by an unbounded factor**. No broad novelty claim is made for binary-word constructions, Markov types, or local Farey statistics.

Nothing here proves an asymptotic law for actual Farey discrepancy, an `S_q` spectral-allocation deficit, a stronger Franel--Landau estimate, Möbius cancellation, or RH. The controls are rational point grids, not Farey sequences. A theorem using denominator/mediant labels, growing local depth, or another genuinely Farey-specific relation is not touched by this counterexample.
