# AF-430 — Supercritical residual packets preserve the shrinking saddle window

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `SUPERCRITICAL` · `MOVING-SADDLE` · `SCHUR-PACKET` · `SIGNED-RESUMMATION` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421, AF-423 and AF-429 inside the normalized exceptional-`1` Cauchy--Binet sector. Fix `a>0`, let

\[
q_n=\frac{s_n}{n}\longrightarrow\sigma>2,
\qquad
R_n=a^{1/q_n}n^{1-2/q_n},
\]

and let `tau_n` be AF-429's real zero of the exact adjacent full-column ratio

\[
F_{n,r}=\frac{C_{n,r}}{C_{n,r-1}},
\qquad
\Phi_n(r)=\log F_{n,r}.
\]

For every integer `r>=0`, use AF-421's exact decomposition

\[
S_n^{(s_n)}(a)
=
\sum_{r\ge0}(-1)^{rn}C_{n,r}G_{n,r},
\]

where

\[
G_{n,r}
=
\sum_{\mu_n=0}
(-1)^{|\mu|}
\left(\frac{a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)}
\tag{1}
\]

is the **complete residual partition packet** attached to the rectangle `(r^n)`.

Assume that an integer sequence `r_n` reaches AF-429's rectangle-comparability window,

\[
\boxed{
|r_n-\tau_n|=O(R_n/n).
}
\tag{2}
\]

Then the two adjacent complete residual packets have the same positive leading limit,

\[
\boxed{
G_{n,r_n-1},\;G_{n,r_n}
\longrightarrow
E_\sigma(a):=\exp(-a e^\sigma),
}
\tag{3}
\]

and their first relative mismatch is explicit:

\[
\boxed{
n\left(\frac{G_{n,r_n}}{G_{n,r_n-1}}-1\right)
\longrightarrow
\sigma a e^\sigma,
}
\tag{4}
\]

or equivalently

\[
\boxed{
\log\frac{G_{n,r_n}}{G_{n,r_n-1}}
=
\frac{\sigma a e^\sigma}{n}+o(n^{-1}).
}
\tag{5}
\]

Therefore the adjacent **complete packet** ratio

\[
Q_{n,r_n}
:=
\frac{C_{n,r_n}G_{n,r_n}}
     {C_{n,r_n-1}G_{n,r_n-1}}
\]

satisfies

\[
\boxed{
\log Q_{n,r_n}
=
\Phi_n(r_n)
+
\frac{\sigma a e^\sigma}{n}
+o(n^{-1}).
}
\tag{6}
\]

AF-429 gives, uniformly for `|r-tau_n|<=1`,

\[
\Phi_n(r)
=-\frac{q_n n}{R_n}(r-\tau_n)(1+o(1)).
\]

Combining this with `(6)` shows that the residual partition packet does **not** enlarge or wash out the rectangular lattice window. Adjacent complete packets can have order-one comparable magnitudes only on the same scale

\[
\boxed{
|r_n-\tau_n|=O(R_n/n).
}
\tag{7}
\]

At the first finer balancing scale, the packet correction moves the real center only by

\[
\boxed{
\widehat\tau_n-\tau_n
=
a e^\sigma\frac{R_n}{n^2}(1+o(1)).
}
\tag{8}
\]

More precisely, `log Q_{n,r_n}=o(n^{-1})` forces

\[
r_n-\tau_n
=
\frac{\sigma}{q_n}a e^\sigma\frac{R_n}{n^2}
+o(R_n/n^2).
\tag{9}
\]

Since `R_n/n^2=o(R_n/n)`, the complete residual packet contributes a genuine sub-window correction but leaves AF-429's shrinking-target obstruction intact at leading order.

For odd `n`, the factors `(-1)^{rn}` alternate between adjacent rectangle packets while `(3)` makes `G_{n,r}` eventually positive in the candidate window. Hence the same integer-resolution gate remains necessary before the two complete packets can cancel. This theorem does **not** prove that the source supplies such integers, nor that cancellation of the two leading packets controls the omitted determinant sectors or the full determinant.

## 1. Fixed residual shapes retain the supercritical derivative coordinate

For a residual partition `mu` with `mu_n=0`, write

\[
\delta_i=\mu_{n+1-i}.
\]

AF-421 gives

\[
\mathcal R_{n,r,\mu}^{(s)}
=
\prod_{i=1}^{n}
\left(
\frac{i+r+\delta_i}{i+r}
\right)^{s-1}
\frac{\zeta(2(i+r+\delta_i))}
     {\zeta(2(i+r))}
\left(
\frac{2(i+r+\delta_i)-1}
     {2(i+r)-1}
\right)^2.
\tag{10}
\]

Under `(2)`, AF-429 gives `r_n/R_n->1`, while `R_n/n->0`. For a fixed `mu` of degree `d`, only indices `i=n+O_mu(1)` have `delta_i>0`. Therefore, uniformly for `r=r_n` or `r_n-1`,

\[
\sum_i\log\left(1+\frac{\delta_i}{i+r}\right)
=
\frac{d}{n}+o_\mu(n^{-1}).
\tag{11}
\]

Since `s_n/n->sigma`, the power block in `(10)` tends to `e^{sigma d}`. The zeta ratios tend to one exponentially fast on these active indices, and the odd-distance block also tends to one. Together with the hook-content asymptotic

\[
\frac{s_\mu(1^n)}{n^d}\to\frac1{H_\mu},
\]

the signed residual summand in `(1)` has the fixed-shape limit

\[
(-1)^d
\left(\frac{a}{n^2}\right)^d
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)}
\longrightarrow
\frac{(-a e^\sigma)^d}{H_\mu^2}.
\tag{12}
\]

Thus the moving full-column saddle does not change the fixed residual Schur parameter: the packet sees the same derivative-depth coordinate `a e^sigma` already suggested by AF-417.

## 2. Tall residual columns vanish inside the candidate lattice window

The fixed-shape limit is not enough because `G_{n,r}` sums over unbounded partitions. The key point is that AF-421's tall-column obstruction changes character once the base rectangle itself sits at the AF-429 saddle.

Fix `eta` with `1/2<eta<1`. For residual columns of height at most `eta n`, AF-421's shifted column product

\[
P_{n,r,\mu}
=
\prod_{m\ge1}
\frac{n+r+m}{n-h_m+r+m}
\]

satisfies

\[
P_{n,r,\mu}
\le
\exp\left(\frac{|\mu|}{(1-\eta)n}\right)
\tag{13}
\]

uniformly in `r>=0`. Since `q_n` stays bounded, the elementary bound

\[
\mathcal R_{n,r,\mu}^{(s_n)}
\le
9^{|\mu|}P_{n,r,\mu}^{s_n-1}
\]

turns `(13)` into `A_eta^{|mu|}` with `A_eta` independent of `n` and of `r` in the present window. The positive Schur Cauchy identity

\[
\sum_\mu
\left(\frac{A_\eta a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
=
\left(1-\frac{A_\eta a}{n^2}\right)^{-n^2}
\tag{14}
\]

then supplies a uniformly summable degree majorant.

It remains to exclude residual columns with height `h>eta n`. Because `mu_n=0`, write such a height as

\[
h=n-j,
\qquad
1\le j<(1-\eta)n.
\]

The same Pieri bound used in AF-420--AF-421 reduces each tall column to

\[
B_{n,u,m}(n-j;a)
=
\left(\frac{a}{n^2}\right)^{n-j}
\binom nj^2
\left(
\frac{n+u+m}{j+u+m}
\right)^{s_n+1},
\tag{15}
\]

where the base width is `u=r_n-1` or `r_n`. For fixed `j`, `(15)` decreases with the column index `m`, so `m=1` is worst.

First adjoin the forbidden `j=0` value only as a comparison quantity. For `u=r_n-1`,

\[
B_{n,r_n-1,1}(n;a)
=
F_{n,r_n}(1+o(1)),
\tag{16}
\]

because the extra ordinary square ratio in `B` cancels AF-429's odd-distance square ratio and the zeta ratio tends to one as `r_n->infinity`. Condition `(2)` and AF-429 imply `F_{n,r_n}=e^{O(1)}`. For `u=r_n`, the analogous comparison is with `F_{n,r_n+1}`; AF-429's slope gives

\[
\log F_{n,r_n+1}
=-\frac{q_n n}{R_n}(1+o(1))+O(1),
\tag{17}
\]

so this comparison value is even smaller. Hence the `j=0` reference is uniformly bounded for both packets.

For `m=1` and `j>=1`, divide `(15)` by its `j=0` counterpart. Since

\[
\frac{n^2}{a}=\left(\frac n{R_n}\right)^{q_n},
\]

one obtains exactly

\[
\frac{B_{n,u,1}(n-j;a)}{B_{n,u,1}(n;a)}
=
\left(\frac n{R_n}\right)^{q_nj}
\binom nj^2
\left(\frac{u+1}{u+j+1}\right)^{s_n+1}.
\tag{18}
\]

Put `M_n=n/R_n`. Then `M_n=n^{2/sigma+o(1)}->infinity` and in particular `M_n/log n->infinity`.

If `1<=j<=u+1`, use `log(1+j/(u+1))>=j/(2(u+1))`. The negative logarithm contributed by the last factor in `(18)` is then `-(sigma+o(1))M_n j/2`, which dominates all `O(j log n)` positive terms.

If `u+1<j<=n/(log n)^2`, the last factor contributes at most `-(sigma+o(1))n log 2`, whereas the remaining logarithm is `O(j log n)=o(n)`.

Finally, for `n/(log n)^2<=j<(1-eta)n`, use `(15)` directly: `n-j>=eta n`, `binom(n,j)<=2^n`, and

\[
\frac{n+u+1}{j+u+1}
\le 2(\log n)^2
\]

for large `n`. Thus

\[
\log B_{n,u,1}(n-j;a)
\le
-2\eta n\log n+O(n\log\log n),
\tag{19}
\]

uniformly in the range.

Equations `(16)`--`(19)` show that the maximum tall-column factor decays faster than every inverse power of `n`. As in AF-420, summing over possible tall-column heights and then over the no-tall residual partition through `(14)` therefore gives

\[
\sum_{\substack{\mu_n=0\\\mu\text{ has a tall column}}}
\left|
(-1)^{|\mu|}
\left(\frac{a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\mathcal R_{n,u,\mu}^{(s_n)}
\right|
=o(n^{-M})
\tag{20}
\]

for every fixed `M>0` and for `u=r_n-1,r_n`.

The non-tall majorant `(14)`, the fixed-shape limit `(12)`, and `(20)` justify dominated convergence. Using

\[
\sum_{\mu\vdash d}\frac1{H_\mu^2}=\frac1{d!}
\]

gives `(3)`.

## 3. The adjacent residual drift is still inverse-`n`

To compare the two neighboring packets, define for one residual shape

\[
q_{n,r,\mu}
=
\frac{\mathcal R_{n,r,\mu}^{(s_n)}}
     {\mathcal R_{n,r-1,\mu}^{(s_n)}}.
\]

AF-423 gives the exact rowwise ratio. If `x=i+r`, the power part at an active row is

\[
\left[
\frac{(x+\delta_i)(x-1)}
{x(x-1+\delta_i)}
\right]^{s_n-1}
=
\left[
1-\frac{\delta_i}{x(x-1+\delta_i)}
\right]^{s_n-1}.
\tag{21}
\]

For fixed `mu`, all active rows have `x=n+r_n+O_mu(1)=n(1+o(1))`. Hence

\[
\log q_{n,r_n,\mu}
=-\frac{\sigma|\mu|}{n}+o_\mu(n^{-1}).
\tag{22}
\]

The odd-distance cross-ratio contributes only `O_mu(n^-2)` and the zeta cross-ratio is exponentially smaller.

On the no-tall sector, the same exact factor `(21)` gives the uniform estimate

\[
n|q_{n,r_n,\mu}-1|
\le
C_\eta|\mu|\exp(C_\eta|\mu|/n),
\tag{23}
\]

so the degree-weighted form of the Schur-Cauchy majorant permits dominated convergence. The tall contribution remains `o(1)` even after multiplication by `n` because of `(20)`.

Writing the signed summand of `G_{n,r_n-1}` as `W_n(mu)`, equations `(12)`, `(22)` and `(23)` yield

\[
\begin{aligned}
 n(G_{n,r_n}-G_{n,r_n-1})
&\longrightarrow
-\sigma
\sum_\mu
|\mu|\frac{(-a e^\sigma)^{|\mu|}}{H_\mu^2}\\
&=
\sigma a e^\sigma e^{-a e^\sigma}.
\end{aligned}
\tag{24}
\]

The last equality uses the classical poissonized-Plancherel identity

\[
\sum_\mu\frac{x^{|\mu|}}{H_\mu^2}=e^x,
\qquad
\sum_\mu|\mu|\frac{x^{|\mu|}}{H_\mu^2}=xe^x.
\]

Dividing `(24)` by `(3)` proves `(4)`, and `(5)` follows because the ratio tends to one.

## 4. The packet correction is below the lattice-resolution scale

Equation `(6)` separates the two effects cleanly. AF-429's rectangle ratio varies by order one when `r` moves only `R_n/n`, while the whole nonrectangular residual packet changes the adjacent logarithmic ratio by only `O(1/n)`.

Therefore the packet correction cannot create a new order-one balancing window. Combining `(5)` with AF-429's local slope gives the first refined balance equation

\[
-\frac{q_n n}{R_n}(r_n-\tau_n)
+
\frac{\sigma a e^\sigma}{n}
=
o(n^{-1}),
\]

which is exactly `(9)`.

The ratio between the center correction and the original lattice window is

\[
\frac{R_n/n^2}{R_n/n}=\frac1n.
\]

Thus, inside the exceptional-`1` sector, the complete residual packet **preserves** the discrete shrinking-target obstruction discovered by AF-429. It adds a finer deterministic displacement rather than smoothing the lattice or introducing a wider cancellation scale.

This also identifies the next admissibility question. Once an actual source sequence supplies `q_n`, `a` and the allowed parity/depths, one must decide whether the corresponding `tau_n` approaches the integer lattice on the `R_n/n` scale at all. Only after such a hit is established does the `R_n/n^2` correction in `(9)` become load-bearing for first inverse-`n` packet balance.

## Prior-art and novelty audit

The representation-theoretic ingredients are classical. Okounkov's *Infinite wedge and random partitions*, Selecta Mathematica 7 (2001), 57--81, DOI `10.1007/PL00001398`, develops the Schur measure and its relation to Plancherel-type partition weights. Borodin, Okounkov and Olshanski, *Asymptotics of Plancherel measures for symmetric groups*, Journal of the American Mathematical Society 13 (2000), 481--515, DOI `10.1090/S0894-0347-00-00337-4`, gives the standard poissonized-Plancherel asymptotic framework. Macdonald's *Symmetric Functions and Hall Polynomials* remains the standard source for the Schur, Pieri, determinant-twist and hook identities used by AF-421.

Varying-parameter and double-scaling Hankel asymptotics are likewise established territory. Charlier and Deaño, *Asymptotics for Hankel Determinants Associated to a Hermite Weight with a Varying Discontinuity*, SIGMA 14 (2018), 018, DOI `10.3842/SIGMA.2018.018`, is one representative example in which an `n`-dependent parameter creates a critical transition.

A targeted search across Schur-measure/poissonized-Plancherel asymptotics, rectangular-partition scaling and varying-parameter Hankel determinants did not locate the exact Euler-log derivative-Hankel specialization `(3)`--`(9)`. **No novelty claim is made** for Schur measures, hook identities, Pieri bounds, dominated-convergence resummation, double scaling, or discrete saddle analysis. The durable content is the exact specialization showing that AF-429's complete residual packet has an inverse-`n` adjacent drift while its rectangle saddle has slope `n/R_n`, forcing the packet-induced center shift down to `R_n/n^2`.

## Boundaries and falsification checks

- The theorem is conditional on an integer sequence already reaching AF-429's candidate window `(2)`. It does not prove that such integers occur infinitely often for any source-forced `q_n` or amplitude `a`.
- `G_{n,r}` is the complete residual partition packet **inside the exceptional-`1` Cauchy--Binet sector**. The omitted-`1` sector and the one-/zero-singular-block contributions of the full Euler determinant are not controlled here.
- The hypotheses require fixed `a>0` and finite `sigma>2`. The argument does not cover `q_n->infinity`.
- Equation `(5)` is a first adjacent-packet correction. Because the saddle magnitude is exponentially large on the `nR_n` scale, first-order balancing is not sufficient to prove that the total signed sector is bounded or convergent.
- The tall-column suppression uses the fact that residual packets have `mu_n=0`; a full-height column is absorbed into the neighboring rectangle and must not be counted as a residual shape.
- Even when `(9)` is met, farther packet corrections, omitted determinant sectors, or source restrictions may prevent cancellation. Conversely, failure of `(2)` already rules out adjacent complete-packet balance in this sector.
- Nothing here supplies a rational-prime discriminator or implies a statement about zeta zeros or RH.

## Consequence for the research line

AF-429's main unresolved packet-shape question is now closed inside the exceptional-`1` sector: the **complete nonrectangular residual packet inherits the moving supercritical saddle window instead of washing it out**. Its first effect is the deterministic drift `sigma a e^sigma/n`, corresponding to the much smaller center displacement `a e^sigma R_n/n^2`.

The live supercritical gate therefore moves from partition-shape control to **source realizability of the shrinking target**. For a concrete source-forced sequence, the next decisive theorem should decide whether `dist(tau_n,Z)` can reach `R_n/n` infinitely often (with the required parity), and only on a surviving subsequence refine the test to the corrected `R_n/n^2` center. Independently, the omitted determinant sectors still require control before any conclusion about the full Euler determinant can be drawn.