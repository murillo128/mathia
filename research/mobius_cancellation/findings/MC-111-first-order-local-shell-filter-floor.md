# MC-111 — First-order local shell filters retain an almost-square parity floor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact Hamming-shell decomposition of `MC-095` and `MC-107`--`MC-110`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
L:=\log\log N,
\qquad
\lambda:=2L.
\tag{1}
\]

`MC-110` showed that every diagonal shell norm loses the decisive cross-degree signs. The first natural non-diagonal repair is to apply a fixed local signed filter before taking absolute values. This entire first-order class still has an almost-square source floor.

Let

\[
A(z)=\sum_{j=0}^{r}a_jz^j
\tag{2}
\]

be a fixed nonzero polynomial with real coefficients, independent of `N`, and extend `C_{k,N}` by zero outside its finite support. Define the filtered shell sequence

\[
T^{A}_{k,N}:=\sum_{j=0}^{r}a_j C_{k+j,N}.
\tag{3}
\]

The parity endpoint passes through this filter exactly:

\[
\boxed{
\sum_{k\in\mathbb Z}(-1)^kT^{A}_{k,N}
=A(-1)\,\mathcal Q_N(1).
}
\tag{4}
\]

Thus a local filter can carry the endpoint only if `A(-1)\ne0`. If also `A(1)\ne0`, then it does not cancel the positive central shell bulk: in the critical window it has `T^A_{k,N}\sim A(1)C_{k,N}` and therefore retains coefficients of size `N^2/\sqrt{L}`.

The genuinely canceling first-order case is

\[
A(1)=0,
\qquad
A'(1)\ne0,
\qquad
A(-1)\ne0.
\tag{5}
\]

Fix any nonzero real `y`, and choose integers `k=k_N` with

\[
\frac{k-2-\lambda}{\sqrt\lambda}\longrightarrow y.
\tag{6}
\]

The quantitative critical Sathe--Selberg saddle underlying `MC-109` gives, uniformly for every fixed shift `j` and for `y` in compact sets,

\[
\frac{C_{k+j,N}}{C_{k,N}}
=1-\frac{jy}{\sqrt\lambda}+O_A\!\left(\frac1L\right).
\tag{7}
\]

Using `\sum_j a_j=A(1)=0` and `\sum_j ja_j=A'(1)`, equation `(7)` yields

\[
\boxed{
T^A_{k,N}
=-\frac{yA'(1)}{\sqrt\lambda}\,C_{k,N}
+O_A\!\left(\frac{C_{k,N}}L\right).
}
\tag{8}
\]

With

\[
c_*:=\frac{36J}{\pi^4},
\qquad
J=\gamma+\gamma_1-\frac12>0,
\tag{9}
\]

`MC-109` gives the central shell profile

\[
C_{k,N}
\sim
\frac{c_*}{\sqrt{4\pi L}}e^{-y^2/2}N^2.
\tag{10}
\]

Hence every fixed first-order local canceling filter has an explicit central response

\[
\boxed{
T^A_{k,N}
\sim
-\frac{c_*A'(1)y}{\sqrt{8\pi}}
 e^{-y^2/2}\frac{N^2}{L}.
}
\tag{11}
\]

In particular, the filtered sequence still contains actual source coefficients of size

\[
\boxed{|T^A_{k,N}|\asymp_A \frac{N^2}{\log\log N}=N^{2-o(1)}.}
\tag{12}
\]

Therefore applying any positive diagonal Hölder certificate after such a filter cannot produce a fixed polynomial saving. If `1\le p\le\infty`, `q` is conjugate to `p`, and `w_{k,N}>0`, then the exact reconstruction `(4)` gives

\[
|\mathcal Q_N(1)|
\le
\frac1{|A(-1)|}
\left\|(w_{k,N}T^A_{k,N})_k\right\|_p
\left\|(w_{k,N}^{-1})_k\right\|_q.
\tag{13}
\]

The same one-coordinate argument as `MC-110` implies

\[
\boxed{
\frac1{|A(-1)|}
\left\|wT^A\right\|_p
\left\|w^{-1}\right\|_q
\gg_A \frac{N^2}{\log\log N}.
}
\tag{14}
\]

The ordinary `L^1` certificate is larger still. On any fixed right-flank window, for example `1\le y\le2`, equation `(11)` holds on `\Theta(\sqrt L)` consecutive degrees, so

\[
\boxed{
\frac1{|A(-1)|}\sum_k|T^A_{k,N}|
\gg_A \frac{N^2}{\sqrt{\log\log N}}.
}
\tag{15}
\]

Thus a first local signed difference merely moves the cancellation problem from the original positive shells into cancellation among the filtered degrees; absoluteizing after that step restores an almost-square obstruction.

The simplest example is adjacent pairing,

\[
A(z)=1-z,
\qquad
T^A_{k,N}=C_{k,N}-C_{k+1,N},
\qquad
A(-1)=2.
\tag{16}
\]

Equation `(4)` becomes

\[
2\mathcal Q_N(1)=\sum_k(-1)^k(C_{k,N}-C_{k+1,N}),
\tag{17}
\]

while `(15)` shows that the total absolute adjacent variation is still at least `N^2/\sqrt{\log\log N}` up to a filter-dependent constant. Pairing neighboring even/odd shells therefore does not expose the super-logarithmically small endpoint; it only transfers the required cancellation to the variation sequence.

This closes a concrete part of the signed non-diagonal escape left by `MC-110`. For a **fixed finite local filter** that still carries parity, the only unresolved radial case now begins with a zero of order at least two at `z=1`:

\[
A(1)=A'(1)=0,
\qquad
A(-1)\ne0,
\tag{18}
\]

or with filters whose range or coefficients genuinely depend on `N`. Nonlocal recurrences and finer non-radial/source-coupled quotients also remain open. No improved estimate for `M(x)` is claimed.

## 1. Exact parity transfer is a frequency test

Because the zero-extended sequence has finite support, shifts can be changed without boundary terms:

\[
\begin{aligned}
\sum_{k\in\mathbb Z}(-1)^kT^A_{k,N}
&=\sum_j a_j\sum_k(-1)^kC_{k+j,N}\\
&=\sum_j a_j(-1)^j\sum_n(-1)^nC_{n,N}\\
&=A(-1)\mathcal Q_N(1).
\end{aligned}
\tag{19}
\]

So `z=-1` is exactly the parity frequency. A filter with `A(-1)=0` annihilates the target and cannot be a lossless endpoint carrier. By contrast `z=1` measures its response to a locally flat positive shell profile. This immediately explains why a useful local filter should vanish at `1` but not at `-1`.

If `A(1)\ne0`, the fixed-shift central ratios tend to one, hence

\[
T^A_{k,N}=(A(1)+o(1))C_{k,N},
\tag{20}
\]

and `MC-110`'s almost-square shell obstruction survives unchanged. The simple-zero case `(5)` is therefore the first genuinely different possibility.

## 2. The central saddle turns a simple zero into a first derivative

Write `n=k-2`. In the central window `(6)`, `n=\lambda+y\sqrt\lambda+O(1)`. The coefficient extraction in `MC-109` is quantitative: the Sathe--Selberg relative error is `O(1/L)`, while the analytic arithmetic factor varies by only `O(1/L)` under any fixed shift of `k`; the source-kernel and common-factor truncation errors carry fixed powers of `1/\log N` and are smaller still.

For fixed `j`, the factorial part therefore gives

\[
\frac{C_{k+j,N}}{C_{k,N}}
=
\frac{\lambda^j}{(n+1)\cdots(n+j)}
\left(1+O_A\!\left(\frac1L\right)\right)
\tag{21}
\]

for `j>0`, with the analogous reciprocal expression for negative fixed shifts. Since

\[
\frac{\lambda}{n+1}
=1-\frac{y}{\sqrt\lambda}+O\!\left(\frac1L\right),
\tag{22}
\]

multiplying finitely many factors proves `(7)`. Substitution into `(3)` then proves `(8)`, and `(10)` gives `(11)`.

The restriction `y\ne0` is essential only for displaying a nonzero first-derivative coefficient at one selected central location. There is no claim that the first difference is large exactly at the mode, where a first derivative should vanish.

## 3. Absoluteization after the filter still destroys the needed signs

Equation `(13)` is just Hölder applied after the exact parity transfer `(4)`. For every `K`,

\[
\|wT^A\|_p\ge w_K|T^A_K|,
\qquad
\|w^{-1}\|_q\ge w_K^{-1},
\tag{23}
\]

so the product is at least `|T^A_K|`. Choosing a central `K` with fixed nonzero `y` and using `(11)` proves `(14)`.

For `(15)`, restrict to the `\Theta(\sqrt L)` integers with

\[
1\le\frac{k-2-\lambda}{\sqrt\lambda}\le2.
\tag{24}
\]

Uniformity of `(7)`--`(11)` on this compact interval gives `|T^A_{k,N}|\gg_A N^2/L` on every retained degree once `N` is large. Summing those terms gives `(15)`. No global unimodality of the entire shell sequence is required.

This is stronger than observing that one derivative-scale coefficient remains large: the full absolute first-variation on a single central flank already returns to the same `N^2/\sqrt L` scale as the original peak shell.

## 4. Prior art and novelty boundary

The analytic input is the same classical Landau--Selberg--Delange/Sathe--Selberg machinery already audited in `MC-107` and `MC-109`. Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, AMS (2019), Theorem 16.2, supplies the quantitative Sathe--Selberg coefficient extraction used there; the AMS record is `https://bookstore.ams.org/GSM/203`, and the author-approved preliminary text is `https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf`.

Finite-difference and Poisson-orthogonal-polynomial language is classical. NIST DLMF §18.22 records the Charlier forward-difference relation, and §18.21 records the Charlier-to-Hermite central limit; see `https://dlmf.nist.gov/18.22` and `https://dlmf.nist.gov/18.21`. These facts are adjacent prior art only: equations `(4)` and `(7)`--`(15)` are derived directly from the exact Mathia shell sequence and do not require a Charlier expansion.

A targeted search for Möbius Hamming shells, Sathe--Selberg shell finite differences, parity filters, and Charlier/Möbius combinations did not identify the source-specific obstruction `(11)`--`(15)` as a standard named result. **No novelty claim is made.** The durable content is the exact classification of the first local signed filter class for this already-derived source deformation.

## 5. Boundaries and falsification tests

- The filter `A` is fixed as `N\to\infty`. An `N`-dependent filter with growing range, growing coefficients, or a zero order at `1` that increases with scale is not covered.
- The proof closes only the cases `A(1)\ne0` and `A(1)=0`, `A'(1)\ne0`. A fixed filter with a second- or higher-order zero at `1` remains live; proving its central response requires correspondingly higher-order uniform saddle control rather than extrapolating `(8)`.
- The condition `A(-1)\ne0` is not cosmetic. When `A(-1)=0`, the filter destroys the parity endpoint, so any recovery would need extra information outside the filtered sequence.
- The norm obstruction concerns certificates that absoluteize the filtered coefficients through diagonal Hölder/`L^1` control. A theorem giving **signed cancellation among the `T^A_k` themselves** could still be useful; equation `(4)` shows that this is exactly where the endpoint difficulty has moved.
- The central estimate uses actual positive source coefficients and the quantitative Sathe--Selberg saddle, not a probabilistic Poisson surrogate. Charlier/Poisson language is only a prior-art comparison.
- No statement here transfers the `N^2` shell scale directly to an exponent for `M(N)`; the separate annular identity and `MC-027` iteration ledger remain necessary.

## Consequence for the research line

`MC-110` left signed non-diagonal radial transforms as a genuine escape from the diagonal norm no-go. The first such family is now classified. Any fixed finite filter that carries parity and does not cancel the local mean keeps the original central bulk; any fixed filter that cancels the local mean only to first order still has `N^{2-o(1)}` coefficients and an `N^2/\sqrt{\log\log N}` absolute-variation floor. Adjacent even/odd shell pairing is therefore not the missing mechanism.

The next radial test should target **higher-order or genuinely nonlocal signed structure**: a fixed filter with at least a double zero at `1`, an `N`-dependent/growing-order transform, or a recurrence whose signed estimate is not reduced to absolute filtered coefficients. In parallel, the non-radial option from the accepted parity-sensitive annular clue remains live: retain a finer source-forced quotient that preserves useful orthogonality without paying full endpoint reconstruction.