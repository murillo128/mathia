# AF-423 — Adjacent residual packets have a universal inverse-`n` drift

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `SCHUR-CAUCHY` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421--AF-422 on a fixed square-transition fiber. Fix `m>=1` and `a>0`, let

\[
s_n=2n+d_n,
\qquad d_n=o(n),
\]

and assume

\[
b_n=a\,n^{d_n/n}\longrightarrow m^2.
\]

For the AF-421 residual packets

\[
G_{n,r}
=
\sum_{\mu_n=0}
(-1)^{|\mu|}
\left(\frac{a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)},
\]

one has

\[
\boxed{
 n\left(\frac{G_{n,m}}{G_{n,m-1}}-1\right)
 \longrightarrow
 2ae^2.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{2ae^2}{n}+o(n^{-1}).
}
\tag{2}
\]

Thus the two residual Schur--Cauchy packets do not agree to first subleading order. The `m`-column packet is larger by the universal relative factor

\[
1+\frac{2ae^2}{n}+o(n^{-1}).
\]

Let AF-422's exact adjacent rectangle ratio be

\[
F_{n,m}=\frac{C_{n,m}}{C_{n,m-1}}
\]

and define the complete adjacent-packet ratio

\[
Q_{n,m}
:=
F_{n,m}\frac{G_{n,m}}{G_{n,m-1}}.
\]

Then

\[
\boxed{
\log Q_{n,m}
=
\log F_{n,m}
+
\frac{2ae^2}{n}
+
o(n^{-1}).
}
\tag{3}
\]

Consequently AF-422's rectangle-level tuning `F_{n,m}->1` is still not enough to cancel the complete adjacent packets. If, along odd `n`,

\[
F_{n,m}\to1,
\qquad
n\log F_{n,m}\to\theta\in\mathbb R,
\]

then

\[
\boxed{
 n(Q_{n,m}-1)
 \longrightarrow
 \theta+2ae^2.
}
\tag{4}
\]

The first packet-level cancellation condition is therefore

\[
\boxed{
 n\log F_{n,m}\longrightarrow-2ae^2.
}
\tag{5}
\]

For `m>=2`, if `(5)` fails while `F_{n,m}->1`, the uncancelled adjacent-packet residual is only polynomially smaller than the tied saddle amplitude. Since the common AF-421 saddle rate

\[
\Lambda_m
=
\frac{m^{2m-2}}{((m-1)!)^2}
>1,
\]

that residual still has nth-root rate `Lambda_m` and hence diverges exponentially. The fine-tuned square interface is therefore narrower than AF-422's condition `Xi_{n,m}->-log K_m`: complete first-order packet cancellation requires the additional inverse-`n` condition `(5)`.

The theorem does **not** claim that `(5)` is sufficient for boundedness or recovery of the fixed-partition exponential. Once `(5)` holds, the `o(n^{-1})` packet difference, the exact finer asymptotics of `F_{n,m}`, and lower saddle packets can become decisive.

## 1. Exact adjacent residual ratio for one partition

For a partition `mu` with `mu_n=0`, put

\[
\delta_i=\mu_{n+1-i}.
\]

AF-421 writes

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
\tag{6}
\]

For fixed `r>=1`, define

\[
q_{n,r,\mu}
:=
\frac{\mathcal R_{n,r,\mu}^{(s_n)}}
     {\mathcal R_{n,r-1,\mu}^{(s_n)}}.
\tag{7}
\]

Writing `x=i+r`, the contribution of index `i` to `(7)` is

\[
\left[
\frac{(x+\delta_i)(x-1)}
{x(x-1+\delta_i)}
\right]^{s_n-1}
\frac{\zeta(2(x+\delta_i))\zeta(2x-2)}
     {\zeta(2x)\zeta(2(x-1+\delta_i))}
\left[
\frac{(2(x+\delta_i)-1)(2x-3)}
     {(2x-1)(2(x+\delta_i)-3)}
\right]^2.
\tag{8}
\]

Fix `mu`. If its `j`-th row is nonzero, the corresponding index is `i=n+1-j`, so every nontrivial factor in `(8)` has `x=n+O_\mu(1)`. Hence

\[
\log
\frac{(x+\delta)(x-1)}
{x(x-1+\delta)}
=
-\frac{\delta}{n^2}+O_\mu(n^{-3}).
\tag{9}
\]

Because `s_n=2n+o(n)`, the power term contributes

\[
-\frac{2\delta}{n}+o_\mu(n^{-1}).
\tag{10}
\]

The odd-distance cross-ratio in `(8)` contributes only `O_\mu(n^{-2})` to the logarithm, while the zeta cross-ratio is exponentially close to one. Summing over the rows of `mu` gives

\[
\boxed{
\log q_{n,r,\mu}
=
-\frac{2|\mu|}{n}+o_\mu(n^{-1}),
}
\tag{11}
\]

and therefore

\[
\boxed{
 n(q_{n,r,\mu}-1)
 \longrightarrow
 -2|\mu|.
}
\tag{12}
\]

The first adjacent-packet difference depends only on the total residual degree, not on the partition shape or on `r`.

## 2. Summing the first-order drift over the Schur packet

Write the `(r-1)` packet summand as

\[
W_{n,r-1}(\mu)
=
(-1)^{|\mu|}
\left(\frac{a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2
\mathcal R_{n,r-1,\mu}^{(s_n)}.
\tag{13}
\]

Then

\[
G_{n,r}-G_{n,r-1}
=
\sum_{\mu_n=0}
W_{n,r-1}(\mu)
(q_{n,r,\mu}-1).
\tag{14}
\]

For every fixed partition `mu`, AF-421's fixed-shape limit gives

\[
W_{n,r-1}(\mu)
\longrightarrow
\frac{(-ae^2)^{|\mu|}}{H_\mu^2},
\tag{15}
\]

where `H_mu` is the hook product.

It remains to justify multiplying `(14)` by `n` and passing the limit through the full packet. Use the same column-height split as AF-421. Fix `eta` with `1/2<eta<1` and first restrict to residual partitions whose columns all have height at most `eta n`. Every nonzero `delta_i` then occurs at

\[
i\ge(1-\eta)n,
\]

so `x=i+r` is uniformly comparable with `n`. The rational factor in `(8)` has the exact form

\[
\frac{(x+\delta)(x-1)}{x(x-1+\delta)}
=
1-\frac{\delta}{x(x-1+\delta)}.
\tag{16}
\]

Since `s_n/n` is bounded, `(16)` gives on this sector

\[
|\log q_{n,r,\mu}|
\le
C_\eta\frac{|\mu|}{n}
\tag{17}
\]

for fixed `r`; the odd-distance cross-ratio contributes the same or a smaller bound and the zeta cross-ratio is exponentially smaller because all active arguments are `\gg n`. Therefore

\[
n|q_{n,r,\mu}-1|
\le
C_\eta |\mu|\exp\!\left(C_\eta\frac{|\mu|}{n}\right).
\tag{18}
\]

AF-421's non-tall-column estimate gives, for another constant `A_eta` independent of `n`,

\[
|W_{n,r-1}(\mu)|
\le
\left(\frac{A_\eta a}{n^2}\right)^{|\mu|}
s_\mu(1^n)^2.
\tag{19}
\]

Combining `(18)`--`(19)` merely replaces `A_eta a` in the positive Schur--Cauchy majorant by `A_eta a\,e^{C_\eta/n}` and inserts one degree factor. The corresponding positive degree moment is uniformly finite. Thus the non-tall part of `nW(q-1)` is dominated by a summable degree-weighted Schur--Cauchy family, and `(12)` may be summed by dominated convergence.

For the complementary tall-column sector, AF-421's fixed-`r` estimate is exponentially decaying whenever

\[
b<(r+2)^2.
\tag{20}
\]

At the square fiber `b=m^2`, `(20)` is strict for both adjacent packets: for `r=m-1`, `m^2<(m+1)^2`, and for `r=m` the gap is larger. The same estimate remains exponentially small after multiplication by `n`, so the tall sector contributes zero to the first-order limit.

Consequently

\[
\lim_{n\to\infty}
 n(G_{n,m}-G_{n,m-1})
=
-2
\sum_{\mu}
|\mu|\frac{(-ae^2)^{|\mu|}}{H_\mu^2}.
\tag{21}
\]

The hook-length identity

\[
\sum_{\mu\vdash d}\frac1{H_\mu^2}=\frac1{d!}
\tag{22}
\]

implies, with `x=-ae^2`,

\[
\sum_\mu \frac{x^{|\mu|}}{H_\mu^2}=e^x,
\qquad
\sum_\mu |\mu|\frac{x^{|\mu|}}{H_\mu^2}=xe^x.
\tag{23}
\]

Therefore `(21)` becomes

\[
\boxed{
 n(G_{n,m}-G_{n,m-1})
 \longrightarrow
 2ae^2 e^{-ae^2}.
}
\tag{24}
\]

AF-421 already proves

\[
G_{n,m-1},G_{n,m}\longrightarrow e^{-ae^2}>0.
\tag{25}
\]

Dividing `(24)` by `(25)` proves `(1)`, and `(2)` follows because the ratio tends to one.

## 3. The tuned square fiber acquires another retained coordinate

AF-422 showed that the nth-root square condition `b_n->m^2` loses the next rectangle-amplitude scale, recovered by

\[
\Xi_{n,m}
=
\log n+n\log(b_n/m^2)-d_n\log m.
\]

Its tuning `Xi_{n,m}->-log K_m` is exactly the condition `F_{n,m}->1` at leading order. Equations `(2)--(3)` show that this still compresses away the first shape-summed packet asymmetry. At the next scale the retained datum is not another partition-shape statistic: it is the inverse-`n` mismatch of the **complete** adjacent ratio,

\[
n\log F_{n,m}+2ae^2.
\tag{26}
\]

Thus the hierarchy on the square collision fiber is now

\[
 b_n=m^2+o(1)
 \quad\leadsto\quad
 F_{n,m}=1+o(1)
 \quad\leadsto\quad
 n\log F_{n,m}=-2ae^2+o(1),
\]

with each stage retaining information discarded by the previous compression.

For `m>=2`, any mismatch surviving at order `1/n` remains exponentially large after multiplication by the tied saddle amplitude. Hence polynomially accurate cancellation is not enough to recover an order-one limit. If the route survives `(5)`, later work must compare the next packet correction against the exponentially smaller neighboring saddle scales rather than infer success from cancellation of the two leading rectangles.

## Prior-art and novelty audit

The ingredients used in the summation are classical. The hook-content and hook-length formulas, the Schur Cauchy identity, and determinant twists are standard symmetric-function theory; AF-421 already audits them against Macdonald's *Symmetric Functions and Hall Polynomials*. Okounkov's **“Infinite wedge and random partitions,”** arXiv `math/9907127`, places Schur measures and their Toda structure in the standard literature, while Borodin--Okounkov--Olshanski's **“Asymptotics of Plancherel measures for symmetric groups,”** arXiv `math/9905032`, gives the classical poissonized-Plancherel asymptotic setting.

A targeted search of Schur-measure, poissonized-Plancherel, rectangular-partition, and hook-content asymptotics did not locate the specific adjacent residual-packet limit `(1)` for the Euler-log derivative-Hankel normalization used in AF-421--AF-422. **No novelty claim is made**: the durable content is the exact first-order specialization and the resulting narrowing of the current square-transition gate.

## Boundaries and falsification checks

- The result assumes fixed `m` and fixed `a>0`, with `s_n=2n+o(n)` and `b_n->m^2`. It does not cover a growing saddle index or the genuinely supercritical regime `s_n/n>2`.
- Equation `(1)` compares the two AF-421 residual packets only. It does not by itself control the whole signed sum after those packets have been tuned to cancel more accurately than order `1/n`.
- The strict residual tall-column gap is essential to the first-order exchange. The argument must not be reused at a parameter boundary where that gap closes.
- The coefficient `2ae^2` comes from summing the degree statistic under the limiting signed Schur packet. It is not a universal coefficient for arbitrary compressions or arbitrary Schur measures.
- For `m=1`, `(1)--(5)` remain valid, but `Lambda_1=1`; the exponential-divergence consequence stated for `m>=2` does not apply.
- Condition `(5)` is necessary only for first packet-level cancellation. It is not sufficient for boundedness, convergence, recovery of `e^{-ae^2}`, a zeta-zero discriminator, or RH.

## Consequence for the research line

The odd tuned square-transition problem has moved one scale deeper. AF-422's condition `Xi_{n,m}->-log K_m` cancels only the rectangle amplitudes. The complete residual packets carry a deterministic relative drift `2ae^2/n`, so first packet-level cancellation additionally requires `(5)`.

The next decisive question is now genuinely finer: under `(5)`, derive the next asymptotic of `Q_{n,m}-1` and compare its scale with the first subleading full-column saddle. For `m>=2`, any mismatch larger than the neighboring-saddle ratio still forces exponential divergence; only after that comparison can the finite-window square fiber be declared closed or shown to support a deeper cancellation mechanism.