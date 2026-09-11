# MC-220 — Every fixed square-free degree grows along the first square-defect shell, so cancellation must escape to moving degree

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-218` isolates a coherent negative prime layer on the first active square-defect shell, and `MC-219` shows that the positive semiprime layer is larger by a factor

\[
L_X
=
\log\!\left(\frac{\log T-\log y}{\log y}\right)
=
\log\log X-\log\log\log X+o(1).
\]

The same growth persists through **every fixed square-free Hamming degree** on that exact shell.

Keep

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
q=\prod_{p\le y}p,
\qquad
T=X-q,
\]

and let `d` be prime with `y<d\le2y`. Put `a_d=-q mod d^2`. For fixed `k>=1`, define

\[
B_{k,d}(X)
:=
\#\left\{
 n\le T:
 \mu^2(n)=1,
 \omega(n)=k,
 (n,q)=1,
 n\equiv a_d\pmod{d^2}
\right\}.
\]

Thus the degree-`k` contribution to

\[
A_d(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a_d\pmod{d^2}}}\mu(n)
\]

is exactly `(-1)^k B_{k,d}(X)`. In particular `B_{1,d}=P_d` from `MC-218` and `B_{2,d}=Q_d` from `MC-219`.

For every fixed integer `k>=1`, uniformly for all shell primes `d`,

\[
\boxed{
B_{k,d}(X)
=
\frac{T}{\varphi(d^2)\log T}
\left(
\frac{L_X^{k-1}}{(k-1)!}
+O_k(L_X^{k-2}+1)
\right).
}
\tag{1}
\]

For `k=1`, the bracket is interpreted as `1+o(1)` and recovers `MC-218`; for `k=2`, `(1)` recovers `MC-219`. Consequently, for every fixed `k>=1`,

\[
\boxed{
\frac{B_{k+1,d}(X)}{B_{k,d}(X)}
=
\frac{L_X}{k}\left(1+O_k(L_X^{-1})\right)
\longrightarrow\infty
}
\tag{2}
\]

uniformly over the shell.

Hence no fixed finite collection of Hamming degrees can contain the required deterministic cancellation. For fixed `K>=1`, let

\[
C_{K,d}(X)
:=
\sum_{k=1}^{K}(-1)^k B_{k,d}(X).
\]

Then

\[
\boxed{
C_{K,d}(X)
=
(-1)^K
\frac{L_X^{K-1}}{(K-1)!}
P_d(X)
\left(1+O_K(L_X^{-1})\right).
}
\tag{3}
\]

In particular the signed truncation is asymptotically dominated by its **last** retained degree and alternates sign each time one more fixed degree is added.

Using the prime-layer energy from `MC-218`,

\[
\mathcal P_1(X)
:=
\sum_{y<d\le2y\atop d\text{ prime}}dP_d(X)^2
\sim
\frac{3}{8c^2}
\frac{X^2}{(\log X)^4\log\log X},
\]

we obtain for every fixed `K>=1`

\[
\boxed{
\sum_{y<d\le2y\atop d\text{ prime}}
 d|C_{K,d}(X)|^2
\sim
\frac{3}{8c^2((K-1)!)^2}
\frac{L_X^{2K-2}X^2}{(\log X)^4\log\log X}.
}
\tag{4}
\]

This remains `X^{2-o(1)}` for every fixed `K`, polynomially larger than the `MC-209` diagonal target `X^{1+o(1)}`.

Let `H_{K,d}(X)` contain the possible degree-zero term `n=1` and all square-free degrees greater than `K`, so that

\[
A_d(T)=C_{K,d}(X)+H_{K,d}(X).
\]

If the first-shell target

\[
W_y(X)
:=
\sum_{y<d\le2y\atop d\text{ prime}}d|A_d(T)|^2
\le X^{1+o(1)}
\]

holds, then `(4)` forces

\[
\boxed{
\frac{
\left(\sum_d d|H_{K,d}+C_{K,d}|^2\right)^{1/2}}
{
\left(\sum_d d|C_{K,d}|^2\right)^{1/2}}
\le X^{-1/2+o(1)}
}
\tag{5}
\]

for **every fixed `K`**. Therefore the live square-defect theorem cannot be proved by a cancellation mechanism confined to primes versus semiprimes, any bounded set of almost-prime layers, or any fixed finite Hamming jet. The compensating degree must move to infinity with `X`, or the proof must use a genuinely non-degree-local relation that couples the entire parity hierarchy at once.

No estimate for the actual `W_y`, `A_d`, `M(X)`, or the zeta zero set is proved here.

## 1. The fixed-degree count is a rough Landau problem in a polylogarithmic progression

Because `(n,q)=1`, every prime factor of a number counted by `B_{k,d}` exceeds `y`. Because `a_d` is reduced modulo `d`, no contributing number is divisible by `d`. Thus `B_{k,d}` is the standard fixed-`k` distinct-prime counting problem with lower prime cutoff `y`, restricted to one reduced residue class modulo

\[
d^2=O((\log X)^2).
\]

Landau's fixed-`k` almost-prime argument gives the unrestricted rough count by selecting one large prime and summing reciprocal mass over the remaining `k-1` prime factors. On the present progression, the same decomposition may be made with the largest prime factor `P` distinguished. Writing `n=rP`, the congruence is

\[
P\equiv a_d\bar r\pmod{d^2},
\]

and the upper endpoint is `P\le T/r`.

The part where every prime factor is at most `T^{1/(2k)}` contains only `T^{1/2+o(1)}` integers and is negligible against the main `T/(d^2\log T)` scale. On the complementary part the distinguished prime endpoint is at least `T^{1/(2k)}`. Since `d^2=O((\log X)^2)`, Siegel--Walfisz applies uniformly to that prime count, with an error smaller than any fixed inverse power of `log X` after summing the fixed number of reciprocal-prime variables.

The lower endpoint enforcing that `P` is the largest factor contributes one fewer free reciprocal-prime logarithm. Repeated-prime configurations are absent because `B_{k,d}` is square-free; the corresponding collision corrections are also lower by at least one reciprocal-prime logarithm because `sum_p p^{-2}` converges.

Thus the standard fixed-`k` Landau recursion survives uniformly in `d` and gives

\[
B_{k,d}(X)
=
\frac{T}{\varphi(d^2)\log T}
\left(
\frac{R_X^{k-1}}{(k-1)!}
+O_k(R_X^{k-2}+1)
\right),
\tag{6}
\]

where the available reciprocal-prime mass is

\[
R_X
:=
\sum_{y<p\le T}\frac1p
=
\log\log T-\log\log y+O(1).
\tag{7}
\]

More precisely, retaining the varying final-prime denominator `log(T/r)` replaces `R_X` by the `MC-219` parameter `L_X` up to an additive `O(1)` term. Since `L_X\to\infty`, replacing `R_X` by `L_X` in the leading degree-`k-1` polynomial changes only the `O_k(L_X^{k-2})` term. This proves `(1)`.

## 2. Every fixed signed truncation is dominated by its newest degree

Equation `(2)` implies, for fixed `K`,

\[
B_{1,d}+\cdots+B_{K-1,d}=O_K(B_{K,d}/L_X)
\]

uniformly in `d`. Therefore

\[
C_{K,d}
=(-1)^K B_{K,d}\left(1+O_K(L_X^{-1})\right),
\]

which together with `(1)` and `B_{1,d}=P_d` proves `(3)`.

The uniformity matters. It allows the pointwise asymptotic to be squared and summed over the same weighted shell used by `MC-209` without losing the leading term. Substitution of the `MC-218` asymptotic for `\mathcal P_1` gives `(4)`.

The degree-zero term cannot alter the conclusion. It is at most one in each selected progression, so its entire weighted shell energy is only polylogarithmic. It may therefore be absorbed into `H_{K,d}` in `(5)`.

## 3. This identifies a moving-degree, not bounded-degree, source obligation

`MC-219` left open whether the semiprime overcompensation might be repaired by one or two further square-free degrees. Equations `(1)`--`(3)` rule out that entire bounded-depth scenario.

At every fixed depth, the next unsigned layer is larger than the preceding one by roughly `L_X/k`. The alternating Möbius signs therefore produce increasingly large oscillating fixed-depth truncations rather than convergence toward the target. If diagonal square-defect energy is true, the cancellation onset must occur only after `k` itself grows with `X` far enough that the factorial in `(1)` competes with powers of `L_X`.

The natural crossover suggested by the fixed-degree coefficients is therefore around a moving degree `k` comparable to `L_X`, not at any bounded Hamming depth. Equation `(1)` is **not** asserted uniformly in that moving regime, so this observation is only a localization of the next theorem surface, not a Sathe--Selberg theorem for `k\asymp L_X`.

The next genuinely new source question is consequently sharper: determine the signed degree profile in the moving window where `k` grows with `L_X`, and test whether the actual lifted residue condition forces cancellation there beyond what positive almost-prime counting or generic sieve parity can see.

## 4. Prior art and novelty boundary

The fixed-`k` asymptotic underlying `(6)` is classical Landau theory. `MC-105` already used the classical distinct-prime Landau formula to prove a growing fixed-degree cascade for an **earlier Huxley--Watt radial functional**. That result is an important internal boundary: the present finding does not claim that fixed-degree almost-prime growth or factorial coefficients are new.

The arithmetic-progression input is also classical. Siegel--Walfisz gives uniform prime equidistribution for moduli bounded by powers of `log X`; `MC-S15` is the retained line source for this regime. Heath-Brown's 1978 work on almost-primes in arithmetic progressions treats substantially harder distribution questions and is broader prior art than the elementary polylog-modulus specialization used here. `MC-S6` supplies the reciprocal-prime asymptotic underlying `(7)`.

A targeted literature check around fixed-`k` almost-primes in progressions, square-free almost-prime counts, Landau/Sathe--Selberg asymptotics, and rough-number restrictions found no basis for a new external theorem claim. The mathematical delta is the **specialization to the current source-prescribed first square-defect shell**, where the fixed-degree asymptotic can be compared directly with the `MC-209` weighted energy and turns the two-layer obstruction of `MC-219` into the all-fixed-depth statement `(5)`.

## 5. Boundaries and falsification tests

- The asymptotic `(1)` is for each **fixed** `k`. It is not uniform for `k` growing with `L_X`; extending into the crossover window requires Sathe--Selberg-type uniformity with the progression and rough cutoff retained.
- The result is confined to the first shell `y<d\le2y`, where `d` is prime and `d^2` is polylogarithmic. No corresponding fixed-degree formula is asserted for root moduli near `X^{1/2}`.
- Positive fixed-degree counting does not estimate the signed full sum `A_d`. The point of `(5)` is precisely that the uncontrolled moving-degree tail must cancel the fixed truncation if the diagonal target is true.
- The standard Landau/Siegel--Walfisz derivation must retain the lower cutoff `p>y`, the reduced residue `a_d`, square-freeness, and uniformity in all shell primes. Dropping any of these before deriving `(1)` would no longer establish the stated source-specific shell result.
- The `k\asymp L_X` crossover is a heuristic location suggested by the factorial profile, not a theorem here. No central-limit, Poisson, or random-walk model is promoted to evidence for Möbius cancellation.
- Generic sieve estimates that control only the positive counts `B_{k,d}` do not resolve the parity-sensitive sum over all degrees. This is consistent with the classical sieve parity barrier and with the earlier line findings that positive support control does not recover the deterministic Möbius sign.
- Equation `(4)` is not a lower bound for the full `W_y`; higher degrees may cancel the fixed truncation. Equation `(5)` records the exact compensation required if they do.

This finding is falsified if the fixed-`k` rough Landau asymptotic fails uniformly at the polylogarithmic moduli `d^2`, if the progression-dependent main term is not `1/phi(d^2)` at leading order, or if the lower/largest-prime and square-collision corrections can contribute at the same `L_X^{k-1}` order. Those are the load-bearing analytic points.