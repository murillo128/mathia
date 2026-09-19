# AF-427 — Displaced square-packet cancellation is metrically exceptional

## Status

`EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `DIOPHANTINE-GATE` · `METRIC-DIOPHANTINE` · `HAUSDORFF-DIMENSION` · `SIGNED-RESUMMATION` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-425--AF-426 with fixed packet index `m>=1`. Reparameterize the source amplitude by

\[
A=\log\!\left(\frac{m^2}{a}\right),
\qquad
a(A)=m^2e^{-A}.
\tag{1}
\]

For odd `n`, integer derivative offset `d`, and

\[
\alpha=\frac dn,
\qquad
L_{n,m}=\log\!\left(\frac nm\right)+\frac mn,
\tag{2}
\]

define AF-425's displayed second-order cancellation function

\[
\begin{aligned}
H_{n,m}(d;A)
={}&\log n-nA+\log K_m+dL_{n,m}\\
&+\frac{B_1(d/n;a(A))}{n}
+\frac{B_2(d/n;a(A))}{n^2},
\end{aligned}
\tag{3}
\]

where

\[
K_m=\frac{4me^{2m}}{(2m-1)^2\zeta(2m)},
\tag{4}
\]

and `B_1,B_2` are the explicit AF-425 coefficients, now displaying their amplitude argument.

Let `\mathcal E_m` be the set of real displacements `A` for which there are odd integers `n_j->infinity` and integers `d_j` such that

\[
\frac{d_j\log n_j}{n_j}\longrightarrow A
\tag{5}
\]

and

\[
H_{n_j,m}(d_j;A)=o(n_j^{-2}).
\tag{6}
\]

Then

\[
\boxed{\operatorname{Leb}(\mathcal E_m)=0}
\tag{7}
\]

and, more sharply,

\[
\boxed{\dim_{\mathrm H}(\mathcal E_m)\le\frac23.}
\tag{8}
\]

Because `(1)` is a smooth locally bi-Lipschitz bijection from `A in R` to `a>0`, the corresponding exceptional set of positive amplitudes also has Lebesgue measure zero and Hausdorff dimension at most `2/3`.

Thus AF-426's pointwise obstruction at the exact amplitude `a=m^2` extends in a different sense to displaced amplitudes: **for Lebesgue-almost every `a>0`, the integer source cannot hit AF-425's second-order square-packet cancellation target infinitely often.** Any surviving displaced finite-window escape is confined to a metrically thin exceptional amplitude set.

## 1. Source compatibility bounds the relevant integer depths

The square-transition condition is

\[
b_n=a n^{d/n}\longrightarrow m^2.
\]

Under `(1)` this is exactly

\[
\frac{d\log n}{n}\longrightarrow A.
\tag{9}
\]

Fix a compact displacement interval `J=[-R,R]`. Every sequence contributing to `\mathcal E_m\cap J` therefore satisfies, eventually,

\[
|d|\le M\frac{n}{\log n}
\tag{10}
\]

for some fixed `M=M(R)`. Hence at scale `n` only `O_R(n/\log n)` integer depths can participate. In particular

\[
\alpha=\frac dn=O_R\!\left(\frac1{\log n}\right).
\tag{11}
\]

This count is the first place where the admissible source category matters. Treating `d` as a free real parameter would erase the finite number of source cells available at each scale.

## 2. The cancellation target is transverse to amplitude

AF-425 gives

\[
B_1(\alpha;a)
=-m^2+m-1-\frac12m^2\alpha
+a e^{2+\alpha}(2+\alpha),
\tag{12}
\]

and

\[
\begin{aligned}
B_2(\alpha;a)
={}&\frac23m^3-\frac12m^2+m-\frac14
+\frac13m^3\alpha\\
&-a e^{2+\alpha}
\left(m\alpha^2+6m\alpha-\alpha+8m-3\right).
\end{aligned}
\tag{13}
\]

For fixed `n,d`, differentiation with respect to `A` uses `\partial_A a=-a` and gives

\[
\partial_A H_{n,m}(d;A)
=-n
-\frac{a e^{2+\alpha}(2+\alpha)}{n}
+\frac{a e^{2+\alpha}P_m(\alpha)}{n^2},
\tag{14}
\]

where

\[
P_m(\alpha)=m\alpha^2+6m\alpha-\alpha+8m-3.
\]

On `A in J` and the source range `(10)`, both correction terms are uniformly bounded by `O_{J,m}(n^{-1})`. Therefore, for all sufficiently large `n`,

\[
\boxed{
|\partial_A H_{n,m}(d;A)|\ge \frac n2
}
\tag{15}
\]

uniformly over every relevant integer depth.

Consequently, for each such `n,d`, the target set

\[
I_{n,d}
=\left\{A\in J:\ |H_{n,m}(d;A)|\le n^{-2}\right\}
\tag{16}
\]

is either empty or one interval, and the mean-value theorem gives

\[
\boxed{|I_{n,d}|\le 4n^{-3}.}
\tag{17}
\]

No distribution or independence hypothesis is used: this is a deterministic transversality estimate in the amplitude coordinate.

## 3. Limsup covering closes almost every displaced amplitude

At odd scale `n`, `(10)` supplies at most `C_R n/\log n` candidate depths. Therefore the total length of the scale-`n` target cover is at most

\[
C_{R,m}\frac{n}{\log n}\,n^{-3}
=
O_{R,m}\!\left(\frac1{n^2\log n}\right).
\tag{18}
\]

The series converges. Hence the elementary convergence half of the Borel--Cantelli/limsup covering argument gives

\[
\operatorname{Leb}\left(
\limsup_{\substack{n\to\infty\\n\ \mathrm{odd}}}
\bigcup_{|d|\le Mn/\log n} I_{n,d}
\right)=0.
\tag{19}
\]

Every `A in \mathcal E_m\cap J` belongs to this limsup set because `(6)` implies `|H|\le n^{-2}` eventually along the witnessing subsequence. Thus `\operatorname{Leb}(\mathcal E_m\cap J)=0`. A countable exhaustion by compact `J` proves `(7)`.

For Hausdorff dimension, let `s>2/3`. The same intervals satisfy

\[
\sum_n\sum_d |I_{n,d}|^s
\ll_{R,m,s}
\sum_n \frac{n}{\log n}\,n^{-3s}
=
\sum_n\frac{n^{1-3s}}{\log n}
<\infty.
\tag{20}
\]

The Hausdorff covering criterion therefore gives

\[
\mathcal H^s(\mathcal E_m\cap J)=0
\]

for every `s>2/3`, proving `(8)`.

More generally, the same proof shows that if the target tolerance is a positive sequence `epsilon_n`, then each source cell has amplitude width `O(epsilon_n/n)`. Thus the convergence-side measure test is

\[
\sum_n\frac{\epsilon_n}{\log n}<\infty,
\tag{21}
\]

and the corresponding Hausdorff upper-bound test is

\[
\sum_n\frac{n}{\log n}
\left(\frac{\epsilon_n}{n}\right)^s<\infty.
\tag{22}
\]

The `2/3` bound is the specialization `epsilon_n=n^{-2}` required by AF-425's displayed second-order target.

## 4. Consequence for complete packet cancellation

Along every square-compatible source sequence `(9)`, one has `d/n=O(1/\log n)->0`, so AF-425's square-transition expansion applies:

\[
\log Q_{n,m}
=
H_{n,m}(d;A)+o(n^{-2}).
\tag{23}
\]

Therefore any attempt to cancel the two tied complete packets through the displayed second polynomial order necessarily places its amplitude in `\mathcal E_m`. AF-427 does not say that `Q_{n,m}->1` by itself requires `(6)`; rather, it closes the much stronger tuning needed to suppress polynomial relative mismatch before the exponentially smaller packet/saddle scales can become relevant.

For `m>=2`, AF-421's tied packet rate is `Lambda_m>1`. Hence outside `\mathcal E_m`, an infinitely recurring second-order cancellation route is unavailable, so the displaced finite-window escape cannot reach a beyond-all-orders packet comparison through this mechanism. For `m=1`, the same metric source obstruction holds, but the `Lambda_m>1` divergence conclusion must not be imported.

## Prior-art and novelty audit

The convergence Borel--Cantelli lemma, Hausdorff covering criterion, and their organization as limsup-set methods in metric Diophantine approximation are classical. A broad reference is Victor Beresnevich, Detta Dickinson, and Sanju Velani, *Measure theoretic laws for lim sup sets*, **Memoirs of the American Mathematical Society** 179(846), 2006, DOI `10.1090/MEMO/0846`, arXiv `math/0401118`: https://arxiv.org/abs/math/0401118 . Maurice Dodson, *Diophantine approximation, Khintchine's theorem, torus geometry and Hausdorff dimension*, arXiv `0710.4264`, gives a direct expository bridge among Borel--Cantelli, Diophantine limsup sets, and Hausdorff dimension: https://arxiv.org/abs/0710.4264 .

Modern shrinking-target literature treats much more general moving and inhomogeneous limsup systems; for example Tomas Persson, *Inhomogeneous potentials, Hausdorff dimension and shrinking targets*, **Annales Henri Lebesgue** 2 (2019), 1--37, DOI `10.5802/ahl.15`, studies Hausdorff dimension for inhomogeneous shrinking-target sets: https://doi.org/10.5802/ahl.15 .

No novelty is claimed for the measure or Hausdorff machinery, nor is `(8)` claimed sharp. A targeted search did not locate AF-425's specific Euler-log derivative-Hankel source grid as an existing Diophantine system. The durable delta here is the direct pullback of that exact cancellation target to its original integer source, where the number of admissible cells and the amplitude transversality make the surviving displaced branch metrically exceptional.

## Boundaries and falsification checks

- This is a metric statement in the amplitude/displacement parameter. It does **not** prove that `\mathcal E_m` is empty, countable, or of Hausdorff dimension exactly `2/3`.
- A fixed distinguished arithmetic amplitude could lie in the exceptional set. Such a point requires pointwise Diophantine analysis; an almost-everywhere theorem cannot rule it out.
- The proof uses AF-425's explicit second-order target `H`, not a uniform estimate for the undisplayed remainder over every amplitude and integer depth. Equation `(23)` is invoked only along square-compatible sequences where AF-425's hypotheses hold.
- The compatibility condition `(5)` is essential. The broad cover `(10)` is only a convenient superset of admissible source cells on a compact displacement interval.
- Odd `n` are the relevant signed square-transition subsequence; including all `n` would only enlarge the cover and leaves the upper bounds unchanged.
- For `m>=2`, failure of second-order tuning blocks this particular path toward beyond-all-orders adjacent-packet cancellation. It does not by itself control lower saddles, tall-column effects outside the AF-425 regime, the omitted-`1` sector, one-/zero-singular-block sectors, or the genuinely supercritical `s_n/n->sigma>2` branch.
- No conclusion here upgrades packet cancellation to rational-prime discrimination, zeta-zero recovery, or RH.

## Consequence for the research line

The live finite-window source gate has narrowed again. AF-426 removes the exact-amplitude fiber pointwise; AF-427 removes almost every displaced amplitude metrically and confines any remaining second-order cancellation to a set of Hausdorff dimension at most `2/3`.

The next finite-window question should therefore be **exceptional-set arithmetic rather than generic source spacing**: determine whether the exact moving centers generated by AF-425 admit any distinguished amplitudes with infinitely many `o(n^{-2})` hits, and in particular whether amplitudes forced by the original source construction can lie in that exceptional set. Beyond-all-orders packet analysis is warranted only after such a specific exceptional amplitude survives this pointwise gate.