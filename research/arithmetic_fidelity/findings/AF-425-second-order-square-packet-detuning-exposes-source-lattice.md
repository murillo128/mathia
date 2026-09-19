# AF-425 — Second-order square-packet detuning exposes the source lattice

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `SCHUR-CAUCHY` · `DIOPHANTINE-GATE` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421--AF-424 on a fixed square-transition fiber. Fix `m>=1` and `a>0`, and write

\[
s_n=2n+d_n,
\qquad
\alpha_n=\frac{d_n}{n}\longrightarrow0,
\qquad
b_n=a n^{\alpha_n}\longrightarrow m^2.
\]

Retain AF-424's quantities

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

and

\[
Q_{n,m}
=
F_{n,m}\frac{G_{n,m}}{G_{n,m-1}}.
\]

Put

\[
x_n=-a e^{2+\alpha_n}.
\]

Then the complete residual packets satisfy

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

The exact rectangle ratio simultaneously gives

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

Thus cancellation through the displayed second polynomial order is equivalent to

\[
\boxed{
 n^2\Omega_{n,m}
+n B_1(\alpha_n)
+B_2(\alpha_n)
\longrightarrow0.
}
\tag{8}
\]

The new structural point is that `d_n` is an integer source coordinate. Since `b_n=a n^{d_n/n}`, the leading detuning is exactly affine in `d_n`:

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

Hence

\[
\boxed{
\Omega_{n,m}(d+1)-\Omega_{n,m}(d)
=L_{n,m}\sim\log n.
}
\tag{11}
\]

The full second-order cancellation function

\[
H_n(d)
=
\Omega_{n,m}(d)
+\frac{B_1(d/n)}{n}
+\frac{B_2(d/n)}{n^2}
\tag{12}
\]

has the same coarse lattice spacing:

\[
H_n(d+1)-H_n(d)
=
L_{n,m}+O(n^{-2})
\sim\log n,
\tag{13}
\]

because changing `d` by one changes `alpha=d/n` by `1/n`. The continuously tunable saddle hierarchy is therefore not automatically realizable by the original integer source. The remaining tuned square branch is an explicit inhomogeneous shrinking-target problem on a source lattice whose spacing grows like `log n`.

## 1. Second-order expansion of one residual partition

For a residual partition `mu` with `mu_n=0`, set

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

For row `j`, put `delta=mu_j` and `c=r+1-j`, so the active coordinate is `x=n+c`. The power cross-ratio expands as

\[
\log
\frac{(x+\delta)(x-1)}{x(x-1+\delta)}
=
-\frac{\delta}{n^2}
+
\frac{\delta(2c+\delta-1)}{n^3}
+O_\mu(n^{-4}),
\tag{14}
\]

while the squared odd-distance cross-ratio contributes

\[
-\frac{2\delta}{n^2}+O_\mu(n^{-3}).
\tag{15}
\]

The zeta cross-ratio is exponentially close to one because every active zeta argument is `2n+O_mu(1)`. Multiplying `(14)` by

\[
s_n-1=n(2+\alpha_n)-1
\]

and summing rows uses

\[
\sum_j\mu_j(2r+1-2j+\mu_j)
=2rD+\kappa_\mu.
\]

Therefore, uniformly for bounded `alpha_n`,

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
\tag{16}
\]

This is the first adjacent-ratio scale at which partition content appears explicitly.

## 2. Complete packet summation

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
\tag{17}
\]

Expanding `q-1` from `(16)` in

\[
G_{n,r}-G_{n,r-1}
=
\sum_{\mu_n=0}W_{n,r-1}(\mu)(q_{n,r,\mu}-1)
\]

needs only the first correction in `(17)`, since the packet difference starts at `n^{-1}`. Partition conjugation preserves `D` and `H_mu` and changes `kappa_mu` to `-kappa_mu`, so

\[
\sum_\mu\frac{x_n^D\kappa_\mu}{H_\mu^2}
=
\sum_\mu\frac{x_n^D D\kappa_\mu}{H_\mu^2}
=0.
\tag{18}
\]

The hook-length identity gives

\[
\sum_\mu\frac{x_n^D}{H_\mu^2}=e^{x_n},
\]

\[
\sum_\mu D\frac{x_n^D}{H_\mu^2}=x_n e^{x_n},
\qquad
\sum_\mu D^2\frac{x_n^D}{H_\mu^2}=(x_n^2+x_n)e^{x_n}.
\tag{19}
\]

After division by AF-424's first-order expansion of `G_{n,r-1}` and taking a logarithm, the quadratic `x_n^2` terms cancel and one obtains

\[
\boxed{
\log\frac{G_{n,r}}{G_{n,r-1}}
=
-\frac{(2+\alpha_n)x_n}{n}
+
\frac{x_n\left(r(2+\alpha_n)^2+2r(2+\alpha_n)-(2+\alpha_n)-1\right)}{n^2}
+o(n^{-2}).
}
\tag{20}
\]

Substituting `x_n=-a e^{2+\alpha_n}` and `r=m` gives `(1)`.

The exchange with the complete packet uses the AF-423--AF-424 decomposition. On the non-tall sector the next Taylor remainders are bounded by fixed polynomials in partition degree/content divided by `n^3`; the positive Schur--Cauchy majorant has uniformly finite polynomial degree moments, so a slowly growing degree cutoff gives `o(n^{-2})`. On the tall-column sector the AF-421 rate gap remains strict for `r=m-1,m` at `b=m^2`, hence the omitted contribution is exponentially small and also `o(n^{-2})`.

## 3. Rectangle ratio and the second cancellation coordinate

AF-424's exact rectangle factorization is

\[
F_{n,m}
=
n\left(\frac{b_n}{m^2}\right)^n
m^{1-d_n}
\left(1+\frac mn\right)^{2n+d_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(2+\frac{2m-1}{n}\right)^2
\frac1{(2m-1)^2}.
\tag{21}
\]

After subtracting `Omega_{n,m}`, the only algebraic remainder is

\[
(2n+d_n-1)\log\!\left(1+\frac mn\right)-2m
+2\log\!\left(1+\frac{2m-1}{2n}\right).
\]

Taylor expansion through `n^{-2}` yields `(2)--(4)`; `log zeta(2(n+m))` is exponentially small. Adding `(1)` gives `(5)--(8)`. At `alpha=0`,

\[
B_2(0)
=
\frac23m^3-\frac12m^2+m-\frac14
-ae^2(8m-3).
\tag{22}
\]

This coefficient is not a forced residual by itself because `Omega_{n,m}` may have its own second-order component. The correct question is whether the admissible integer source can realize the full condition `(8)`.

## 4. Integer depth as an exact shrinking-target gate

Using `b_n=a n^{d_n/n}` directly in `Xi` proves `(9)--(11)`. For any externally specified real target `T_n`, the best integer realization has the exact form

\[
\inf_{d\in\mathbb Z}|\Omega_{n,m}(d)-T_n|
=
L_{n,m}
\operatorname{dist}\!\left(
-\frac{C_{n,m}(a)-T_n}{L_{n,m}},\mathbb Z
\right).
\tag{23}
\]

Thus an `o(n^{-1})` target for the leading affine detuning corresponds to a fractional-part target of width `o((n\log n)^{-1})`, and an `o(n^{-2})` target corresponds to width `o((n^2\log n)^{-1})`. For the full corrected function `H_n`, the centers are weakly `d`-dependent through `B_1(d/n)` and `B_2(d/n)`, but `(13)` shows that this deforms the lattice spacing only by `O(n^{-2})`; the `log n` granularity remains decisive.

No equidistribution, scarcity, or impossibility theorem for these particular moving targets is proved here. The reduction matters because it removes a false free parameter: the formal saddle expansion permits continuous tuning, whereas the source construction supplies only integer derivative depth.

## Prior-art and novelty audit

The hook-content and hook-length formulas, Schur Cauchy identities, partition conjugation, and poissonized Plancherel organization are classical. Okounkov's *Infinite wedge and random partitions* (1999), arXiv `math/9907127`, develops the Schur measure and exact correlation/Toda structure: https://arxiv.org/abs/math/9907127 . Borodin--Okounkov--Olshanski's *Asymptotics of Plancherel measures for symmetric groups* (1999), arXiv `math/9905032`, gives the classical poissonized-Plancherel asymptotic setting: https://arxiv.org/abs/math/9905032 . Modern work continues to derive higher asymptotic expansions for nonlinear poissonized-Plancherel observables; see Cafasso--Mucciconi--Ruzza, *Multiplicative Averages of Plancherel Random Partitions* (2026), arXiv `2601.05164`: https://arxiv.org/abs/2601.05164 .

The source-lattice reformulation belongs to standard inhomogeneous Diophantine/shrinking-target language. No general shrinking-target theorem is invoked because the target center varies with `n`. A targeted search across Schur/Plancherel asymptotics, hook-content expansions, rectangular packets, and shrinking-target formulations did not locate the specific Euler-log derivative-Hankel formulas `(1)--(13)` or this integer-depth specialization. **No novelty claim is made**: the durable result is the direct second-order specialization and identification of the exact remaining source-realizability gate.

## Boundaries and falsification checks

- The result fixes `m` and `a` and assumes `alpha_n->0` and `b_n->m^2`. It does not cover a growing saddle index or the genuinely supercritical regime `s_n/n->sigma>2`.
- Equation `(8)` is a necessary and sufficient condition for cancellation through the displayed polynomial order, not for boundedness of the whole signed determinant sector.
- The packet exchange uses the strict tall-column rate gap from AF-421; it must not be transported to a boundary where that gap closes.
- The source-lattice spacing does not prove that arbitrarily accurate hits are impossible. Such a claim needs new Diophantine information about the moving targets.
- For `m>=2`, any uncancelled polynomial relative mismatch still multiplies the tied exponential saddle rate `Lambda_m>1` and therefore dominates neighboring exponentially smaller packets. For `m=1`, `Lambda_1=1`, so the exponential-divergence conclusion does not transfer.
- No statement here upgrades packet cancellation to prime discrimination, zero recovery, or RH.

## Consequence for the research line

The finite critical-window problem has moved from a free formal asymptotic cancellation problem to a source-realizability problem. AF-424 exposed the first derivative-offset coordinate; `(5)--(8)` expose the next polynomial layer, while `(9)--(23)` show that admissible derivative depths sample the leading detuning on an affine lattice of spacing asymptotic to `log n`.

The next decisive question is therefore not simply the third formal coefficient. Determine whether integer `d_n` can satisfy the shrinking-target condition required by `(8)` along infinitely many odd `n`. If the source lattice misses at polynomial scale, the `m>=2` tuned branch closes immediately. Only if the integer source can realize arbitrarily deep polynomial cancellation does the first beyond-all-orders residual/tall-column scale become the relevant comparison with the next full-column saddle.