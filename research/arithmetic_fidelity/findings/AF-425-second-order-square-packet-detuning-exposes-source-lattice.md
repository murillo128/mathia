# AF-425 — Second-order square-packet detuning exposes the source lattice

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `SCHUR-CAUCHY` · `DIOPHANTINE-GATE` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421--AF-424 on a fixed square-transition fiber. Fix `m>=1` and `a>0`, write

\[
s_n=2n+d_n,
\qquad
\alpha_n=\frac{d_n}{n}\longrightarrow0,
\qquad
b_n=a n^{\alpha_n}\longrightarrow m^2,
\]

and retain AF-424's quantities

\[
\Xi_{n,m}
=
\log n+n\log\!\left(\frac{b_n}{m^2}\right)-d_n\log m,
\]

\[
K_m
=
\frac{4m e^{2m}}{(2m-1)^2\zeta(2m)},
\qquad
\Omega_{n,m}
=
\Xi_{n,m}+\log K_m+m\alpha_n,
\]

and the complete adjacent-packet ratio

\[
Q_{n,m}
=
F_{n,m}\frac{G_{n,m}}{G_{n,m-1}}.
\]

Put

\[
x_n=-a e^{2+\alpha_n}.
\]

Then the residual Schur--Cauchy packets admit the second-order adjacent-ratio expansion

\[
\boxed{
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{a e^{2+\alpha_n}(2+\alpha_n)}{n}
-
\frac{a e^{2+\alpha_n}
\left(m\alpha_n^2+6m\alpha_n-\alpha_n+8m-3\right)}{n^2}
+o(n^{-2}).
}
\tag{1}
\]

The exact rectangle ratio from AF-424 simultaneously gives

\[
\boxed{
\log F_{n,m}
=
\Omega_{n,m}
+
\frac{A_1(\alpha_n)}{n}
+
\frac{A_2(\alpha_n)}{n^2}
+O(n^{-3})+O(2^{-2n}),
}
\tag{2}
\]

where

\[
A_1(\alpha)
=-m^2+m-1-\frac12m^2\alpha,
\tag{3}
\]

\[
A_2(\alpha)
=
\frac23m^3-\frac12m^2+m-\frac14
+\frac13m^3\alpha.
\tag{4}
\]

Consequently

\[
\boxed{
\log Q_{n,m}
=
\Omega_{n,m}
+
\frac{B_1(\alpha_n)}{n}
+
\frac{B_2(\alpha_n)}{n^2}
+o(n^{-2}),
}
\tag{5}
\]

with

\[
B_1(\alpha)
=
-m^2+m-1-\frac12m^2\alpha
+a e^{2+\alpha}(2+\alpha),
\tag{6}
\]

and

\[
\boxed{
B_2(\alpha)
=
\frac23m^3-\frac12m^2+m-\frac14
+\frac13m^3\alpha
-
a e^{2+\alpha}
\left(m\alpha^2+6m\alpha-\alpha+8m-3\right).
}
\tag{7}
\]

Thus AF-424's first complete-packet interface has an explicit second layer. Cancellation through order `n^{-2}` is equivalent to

\[
\boxed{
 n^2\Omega_{n,m}
+n B_1(\alpha_n)
+B_2(\alpha_n)
\longrightarrow0.
}
\tag{8}
\]

The important new structural point is that `d_n` is an integer source coordinate. Since `b_n=a n^{d_n/n}`, the detuning is exactly affine in `d_n`:

\[
\boxed{
\Omega_{n,m}
=
C_{n,m}(a)+d_n L_{n,m},
}
\tag{9}
\]

where

\[
C_{n,m}(a)
=
\log n+n\log\!\left(\frac{a}{m^2}\right)+\log K_m,
\qquad
L_{n,m}
=
\log\!\left(\frac{n}{m}\right)+\frac{m}{n}.
\tag{10}
\]

Therefore one unit of derivative depth changes the leading complete-packet detuning by

\[
\boxed{
\Omega_{n,m}(d+1)-\Omega_{n,m}(d)
=L_{n,m}\sim\log n.
}
\tag{11}
\]

The continuously tunable asymptotic hierarchy is therefore not automatically realizable by the original integer source. Even AF-424's `O(n^{-1})` cancellation requires a shrinking-target hit of an affine lattice whose spacing grows like `log n`; the second-order interface `(8)` requires a correspondingly finer hit. This does not prove that such subsequences do not exist. It converts the remaining tuned square branch into an explicit inhomogeneous Diophantine/shrinking-target problem instead of another free real-parameter saddle cancellation.

## 1. Second-order expansion of one residual partition

For a residual partition `mu` with `mu_n=0`, write

\[
D=|\mu|,
\qquad
\kappa_\mu
=
\sum_{j\ge1}\mu_j(\mu_j-2j+1).
\]

AF-423 gives the exact adjacent residual factor

\[
q_{n,r,\mu}
=
\frac{\mathcal R_{n,r,\mu}^{(s_n)}}
     {\mathcal R_{n,r-1,\mu}^{(s_n)}}.
\]

For row `j`, put `delta=mu_j` and `c=r+1-j`, so the active coordinate is `x=n+c`. The power cross-ratio has

\[
\log
\frac{(x+\delta)(x-1)}{x(x-1+\delta)}
=
-\frac{\delta}{n^2}
+
\frac{\delta(2c+\delta-1)}{n^3}
+O_\mu(n^{-4}),
\tag{12}
\]

while the squared odd-distance cross-ratio contributes

\[
-\frac{2\delta}{n^2}+O_\mu(n^{-3}).
\tag{13}
\]

The zeta cross-ratio is exponentially close to one because every active zeta argument is `2n+O_mu(1)`. Multiplying `(12)` by

\[
s_n-1=n(2+\alpha_n)-1
\]

and summing over rows uses

\[
\sum_j\mu_j(2r+1-2j+\mu_j)
=2rD+\kappa_\mu.
\]

Hence, uniformly for bounded `alpha_n`,

\[
\boxed{
\log q_{n,r,\mu}
=
-\frac{(2+\alpha_n)D}{n}
+
\frac{
(4r-1+2r\alpha_n)D+(2+\alpha_n)\kappa_\mu
}{n^2}
+O_\mu(n^{-3}).
}
\tag{14}
\]

This is the first scale at which the adjacent ratio sees partition content directly.

## 2. Summing the second-order packet correction

AF-424 gives the signed packet weight around `r-1` as

\[
W_{n,r-1}(\mu)
=
\frac{x_n^D}{H_\mu^2}
\left[
1-
\frac{
\left(2(r-1)+\alpha_n(r-\tfrac12)\right)D
+\frac12\alpha_n\kappa_\mu
}{n}
+O_\mu(n^{-2})
\right].
\tag{15}
\]

Expanding `q-1` from `(14)` and inserting it into

\[
G_{n,r}-G_{n,r-1}
=
\sum_{\mu_n=0}W_{n,r-1}(\mu)(q_{n,r,\mu}-1)
\]

requires only the first correction in `(15)`, because the packet difference already begins at order `n^{-1}`.

Partition conjugation preserves `D` and `H_mu` and sends `kappa_mu` to `-kappa_mu`. Therefore both

\[
\sum_\mu\frac{x_n^D\kappa_\mu}{H_\mu^2}=0,
\qquad
\sum_\mu\frac{x_n^D D\kappa_\mu}{H_\mu^2}=0.
\tag{16}
\]

The hook-length identity gives the Poisson moments

\[
\sum_\mu\frac{x_n^D}{H_\mu^2}=e^{x_n},
\]

\[
\sum_\mu D\frac{x_n^D}{H_\mu^2}=x_n e^{x_n},
\qquad
\sum_\mu D^2\frac{x_n^D}{H_\mu^2}=(x_n^2+x_n)e^{x_n}.
\tag{17}
\]

After division by AF-424's first-order expansion of `G_{n,r-1}` and taking a logarithm, all `x_n^2` terms cancel. The result is

\[
\boxed{
\log\frac{G_{n,r}}{G_{n,r-1}}
=
-\frac{(2+\alpha_n)x_n}{n}
+
\frac{x_n\left(r(2+\alpha_n)^2+2r(2+\alpha_n)-(2+\alpha_n)-1\right)}{n^2}
+o(n^{-2}).
}
\tag{18}
\]

Substituting `x_n=-a e^{2+alpha_n}` and `r=m` gives `(1)`.

The exchange with the complete residual packet uses the same decomposition as AF-423--AF-424. On the non-tall sector, the next Taylor remainders in `(12)--(15)` are bounded by fixed polynomials in partition degree/content divided by `n^3`; the positive Schur--Cauchy majorant used there has uniformly finite polynomial degree moments. A slowly growing degree cutoff makes the remainder `o(n^{-2})`. On the tall-column sector the AF-421 gap `b<(r+2)^2` remains strict for `r=m-1,m` at `b=m^2`, so its contribution is exponentially small and therefore also `o(n^{-2})`.

## 3. Rectangle ratio at the same scale

AF-424's exact factorization is

\[
F_{n,m}
=
n\left(\frac{b_n}{m^2}\right)^n
m^{1-d_n}
\left(1+\frac mn\right)^{2n+d_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(2+\frac{2m-1}{n}\right)^2
\frac1{(2m-1)^2}.
\tag{19}
\]

After subtracting `Omega_{n,m}`, the only algebraic terms are

\[
(2n+d_n-1)\log\!\left(1+\frac mn\right)-2m
+2\log\!\left(1+\frac{2m-1}{2n}\right).
\]

Taylor expansion through `n^{-2}` yields `(2)--(4)`; the remaining `log zeta(2(n+m))` is exponentially small. Adding `(1)` gives `(5)--(7)`.

Equation `(8)` is consequently the exact next polynomial cancellation coordinate. In particular,

\[
B_2(0)
=
\frac23m^3-\frac12m^2+m-\frac14
-ae^2(8m-3),
\tag{20}
\]

but this coefficient is not a forced residual by itself: the source detuning `Omega_{n,m}` may also have a second-order component. The correct question is whether the integer source can realize `(8)`, not whether `B_2(0)` happens to vanish.

## 4. Integer derivative depth turns fine tuning into a shrinking target

Using `b_n=a n^{d_n/n}` directly in `Xi` gives

\[
\Xi_{n,m}
=
\log n+n\log\!\left(\frac{a}{m^2}\right)
+d_n\log\!\left(\frac{n}{m}\right).
\]

Adding `log K_m+m d_n/n` proves `(9)--(11)`.

For any real target `T_n`, the best integer realization therefore satisfies the exact identity

\[
\inf_{d\in\mathbb Z}|\Omega_{n,m}(d)-T_n|
=
L_{n,m}
\operatorname{dist}\!\left(
-\frac{C_{n,m}(a)-T_n}{L_{n,m}},\mathbb Z
\right).
\tag{21}
\]

Thus first packet cancellation with error `o(n^{-1})` requires the fractional part in `(21)` to enter a target of width `o((n\log n)^{-1})`; second-order cancellation with error `o(n^{-2})` requires width `o((n^2\log n)^{-1})`, after incorporating the slowly varying `B_1(alpha_n)` and `B_2(alpha_n)` corrections into `T_n`.

No equidistribution or impossibility statement for these particular targets is proved here. The exact reduction matters because it removes a false degree of freedom: the formal saddle expansion has a continuously tunable `d`, while the source construction supplies only an integer lattice whose spacing in detuning coordinates grows rather than shrinks.

## Prior-art and novelty audit

The hook-content and hook-length formulas, Schur Cauchy identities, partition conjugation, and poissonized Plancherel organization are classical. Okounkov's *Infinite wedge and random partitions* (1999), arXiv `math/9907127`, develops the Schur measure and its exact correlation/Toda structure: https://arxiv.org/abs/math/9907127 . Borodin--Okounkov--Olshanski's *Asymptotics of Plancherel measures for symmetric groups* (1999), arXiv `math/9905032`, gives the classical poissonized-Plancherel asymptotic setting: https://arxiv.org/abs/math/9905032 . Modern work continues to derive higher asymptotic expansions for nonlinear observables of poissonized Plancherel measures; for example Cafasso--Mucciconi--Ruzza, *Multiplicative Averages of Plancherel Random Partitions* (2026), arXiv `2601.05164`: https://arxiv.org/abs/2601.05164 .

The source-lattice reformulation `(21)` belongs to the standard language of inhomogeneous Diophantine approximation and shrinking targets; no general shrinking-target theorem is invoked because the center itself varies with `n`. A targeted search across Schur/Plancherel asymptotics, hook-content expansions, rectangular packets, and shrinking-target formulations did not locate the specific Euler-log derivative-Hankel formulas `(1)--(11)` or this integer-depth reduction. **No novelty claim is made**: the durable result is the direct second-order specialization and the identification of the exact remaining source-realizability gate.

## Boundaries and falsification checks

- The result fixes `m` and `a` and assumes `alpha_n->0` and `b_n->m^2`. It does not cover a growing saddle index or the genuinely supercritical regime `s_n/n->sigma>2`.
- Equation `(8)` is a necessary and sufficient condition for cancellation through the displayed polynomial order, not for boundedness of the whole signed determinant sector.
- The packet exchange uses the strict tall-column gap from AF-421. It must not be transported to a boundary where that gap closes.
- The integer-lattice spacing `(11)` does not by itself prove that arbitrarily accurate hits are impossible. Such a claim would require new Diophantine information about the moving target in `(21)`.
- For `m>=2`, any uncancelled polynomial relative mismatch still has the tied exponential saddle rate `Lambda_m>1` and therefore dominates neighboring exponentially smaller packets. For `m=1`, `Lambda_1=1`, so the same exponential-divergence conclusion does not apply.
- No statement here upgrades packet cancellation to prime discrimination, zero recovery, or RH.

## Consequence for the research line

The finite critical-window problem has moved from a free formal asymptotic cancellation problem to a source-realizability problem. AF-424 exposed the first derivative-offset coordinate; `(5)--(8)` expose the next polynomial layer, while `(9)--(21)` show that the admissible derivative depth samples those detuning coordinates on an affine lattice of spacing asymptotic to `log n`.

The next decisive question is therefore not simply the third formal coefficient. First determine whether the integer sequence `d_n` can satisfy the shrinking-target condition required by `(8)` along infinitely many odd `n`. If the lattice misses at polynomial scale, the `m>=2` tuned branch closes immediately. Only if the integer source can realize arbitrarily deep polynomial cancellation does it become necessary to compute the first beyond-all-orders residual/tall-column scale and compare it with the next full-column saddle.