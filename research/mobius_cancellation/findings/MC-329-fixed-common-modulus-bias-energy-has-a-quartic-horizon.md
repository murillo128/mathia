# MC-329 — Fixed-common-modulus bias energy has a quartic horizon

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The fixed-modulus prime Halász–Montgomery input used in `MC-321`–`MC-323` has one further consequence that becomes visible only after using the full cubefree flexibility in Schlage-Puchta's primary theorem.

Let

\[
\mathcal A_y\subset\{p:y<p\le2y\}
\]

be a dense prime shell with

\[
A_y:=|\mathcal A_y|\asymp \frac{y}{\log y},
\tag{1}
\]

let `q` be cubefree, and let `\Xi` be any finite set of distinct Dirichlet characters modulo the same `q`. Write

\[
\beta_\chi
:=\frac1{A_y}\sum_{p\in\mathcal A_y}\chi(p),
\qquad
E_y(\Xi):=\sum_{\chi\in\Xi}|\beta_\chi|^2,
\qquad
m:=|\Xi|.
\tag{2}
\]

Then for every fixed `\delta\in(0,4)` there are constants `c_\delta>0` and `C_\delta>0` such that

\[
q\le y^{4-\delta}
\quad\Longrightarrow\quad
\boxed{
E_y(\Xi)
\le
C_\delta\left(1+m y^{-c_\delta}\log y\right).
}
\tag{3}
\]

Thus the common-modulus energy horizon is not merely the cubic range recorded in `MC-322`. For a **cubefree common modulus**, Schlage-Puchta's permission to choose an arbitrary fixed Burgess parameter `k>=2` pushes the fixed-power horizon through every exponent strictly below `4`.

This interacts sharply with the reciprocal endpoint. Continue its common lower-prime source package and put

\[
P:=\prod_{p\in U}p,
\qquad
q:=4P.
\tag{4}
\]

Because `P` is odd squarefree, `q=4P` is cubefree. For the `R` independent endpoint generators, every nonzero

\[
a\in\mathbf F_2^R
\]

gives a distinct character modulo `q` with exact prime-shell bias

\[
x(a)=(-1)^{|a|}\left(1-\frac{2|a|}{R}\right).
\tag{5}
\]

Taking all nonzero endpoint modes gives the exact total bias energy

\[
\boxed{
\sum_{a\ne0}|x(a)|^2
=
\frac{2^R}{R}-1.
}
\tag{6}
\]

Consequently, if `R\to\infty` and, for each fixed `\delta>0`,

\[
R\,y^{-c_\delta}\log y\longrightarrow0,
\tag{7}
\]

then the reciprocal endpoint cannot have

\[
q\le y^{4-\delta}.
\tag{8}
\]

Indeed `(3)` and `(6)` are incompatible. Therefore

\[
\boxed{
\liminf\frac{\log P}{\log y}\ge4.
}
\tag{9}
\]

In particular `(7)` holds throughout any regime with `R=y^{o(1)}`.

This recovers the quartic common-source floor of `MC-324` by a **different mechanism**: no pair-distance/Plotkin averaging, source-column loading estimate, or individual primitive-conductor summation is needed. The whole endpoint bias vector already exhausts the fixed-common-modulus cubefree prime Halász–Montgomery inequality at the same exponent `4`.

The coincidence is structurally important. The quartic boundary is simultaneously

- the source-incidence ceiling reached in `MC-324`–`MC-328` from near-quadratic individual conductor bills and asymptotic half loading; and
- the fixed-common-modulus analytic horizon obtained directly from the arbitrary-`k` cubefree Burgess exponent in Schlage-Puchta's theorem.

Thus merely replacing pair averaging by the full endpoint family does **not** create a hidden exponent gain. Any fixed-power improvement beyond `4` must strengthen the prime-character input itself, exploit information not captured by the positive bias energy `(2)`, or abandon the controlled cubefree common-modulus package. No estimate for `M(x)` follows.

## 1. Arbitrary fixed `k` moves the common-modulus threshold from three to four

Schlage-Puchta's Theorem 3, already audited in `MC-323`, gives for prime-supported coefficients `a_p`, a set `\Xi` of characters modulo one `q`, an auxiliary parameter `B`, and any fixed `k>=2` when `q` is cubefree,

\[
\sum_{\chi\in\Xi}
\left|\sum_{p\le N}a_p\chi(p)\right|^2
\ll_{k,\varepsilon}
\left(
\frac{N}{\log B}
+
N^{1-1/k}
q^{(k+1)/(4k^2)+\varepsilon}
 m B^{2/k}
\right)
\sum_{p\le N}|a_p|^2.
\tag{10}
\]

`MC-322` used the later KMT formulation, which exposes only `k\in\{2,3\}`, and therefore stopped at the cubic fixed-modulus horizon. The primary theorem's cubefree clause allows arbitrary fixed `k`.

Apply `(10)` with

\[
N=2y,
\qquad
a_p=\mathbf1_{p\in\mathcal A_y}.
\]

After dividing by `A_y^2` and using `(1)`,

\[
E_y(\Xi)
\ll
\frac{\log y}{\log B}
+
y^{-1/k}
q^{(k+1)/(4k^2)+\varepsilon}
 mB^{2/k}\log y.
\tag{11}
\]

Fix `\delta\in(0,4)` and choose an integer

\[
k\ge \frac8\delta.
\tag{12}
\]

Ignoring the `\varepsilon` and `B` losses for a moment, the power of `y` in the second term under `q\le y^{4-\delta}` is

\[
-\frac1k
+(4-\delta)\frac{k+1}{4k^2}
=
\frac{(4-\delta)-\delta k}{4k^2}
\le -\frac{\delta}{8k}.
\tag{13}
\]

Now take, for example,

\[
\varepsilon:=\frac{\delta}{64k},
\qquad
B:=y^{\delta/64}.
\tag{14}
\]

For fixed `\delta`, these are admissible for all sufficiently large `y`. The extra modulus loss contributes at most

\[
q^\varepsilon\le y^{\delta/(16k)},
\]

and

\[
B^{2/k}=y^{\delta/(32k)}.
\]

Together with `(13)` this leaves a power saving at least

\[
y^{-\delta/(32k)}.
\tag{15}
\]

The first term of `(11)` is `O_\delta(1)`. Hence `(3)` follows, for instance with

\[
c_\delta=\frac{\delta}{32k}.
\tag{16}
\]

No optimization of `c_\delta` is intended.

The neutral exponent is visible directly from `(11)`. For large fixed `k`, the balance

\[
y^{-1/k}q^{(k+1)/(4k^2)}
\]

changes sign at a modulus exponent tending to

\[
\frac{4k}{k+1}\longrightarrow4.
\tag{17}
\]

The number `4` here comes from the classical Burgess-type exponent inside the prime Halász–Montgomery theorem, not from the source-incidence combinatorics of `MC-324`.

## 2. The full reciprocal endpoint has divergent exact bias energy

Let `K` be binomial with parameters `(R,1/2)`. Under uniform `a\in\mathbf F_2^R`, equation `(5)` gives

\[
|x(a)|^2
=\left(1-\frac{2|a|}{R}\right)^2.
\]

Since

\[
\mathbb E K=\frac R2,
\qquad
\operatorname{Var}(K)=\frac R4,
\]

one has exactly

\[
2^{-R}
\sum_{a\in\mathbf F_2^R}|x(a)|^2
=
\mathbb E\left(1-\frac{2K}{R}\right)^2
=
\frac1R.
\tag{18}
\]

Therefore

\[
\sum_{a\in\mathbf F_2^R}|x(a)|^2
=
\frac{2^R}{R}.
\tag{19}
\]

The zero mode has `x(0)=1`, so deleting it gives `(6)`.

Let

\[
m=2^R-1.
\]

If `(8)` held, `(3)` would imply

\[
\frac{2^R}{R}-1
\le
C_\delta\left(
1+(2^R-1)y^{-c_\delta}\log y
\right).
\tag{20}
\]

Divide by `2^R/R`. Because `R\to\infty`,

\[
\frac{R}{2^R}\to0.
\]

Under `(7)`, the right side of the normalized `(20)` tends to zero, whereas the left side tends to one. This contradiction proves that `(8)` fails for all sufficiently large `y`.

A useful point is that **the full family need not satisfy `2^R=y^{o(1)}`**. The factor `m` in the error term of `(3)` cancels against the endpoint's extensive energy `2^R/R`; the only residual growth condition is `(7)`. Thus the direct whole-family obstruction applies in a wider `R`-range than a crude use of `E_y(\Xi)=O(1)` would suggest.

## 3. Why this is not the same proof as the quartic Plotkin floor

`MC-324` begins from the varying-modulus result of `MC-323`: all but `O_\delta(1)` fixed-bias pair modes have minimum primitive conductor above `y^{2-\delta}`. It then sums those independent conductor bills through one common source incidence matrix. A source column can serve asymptotically one half of the pair modes, producing

\[
2\div\frac12=4.
\]

`MC-326` proves that this half-loading factor is the universal optimum for every positive independent-bill incidence average, and `MC-327`–`MC-328` describe the rigidity of a package that saturates it.

The present argument never separates the characters into primitive conductors and never charges individual modes to source columns. Instead it embeds the entire endpoint family in the one cubefree modulus `q=4P` and applies the fixed-modulus theorem before any source-side decomposition. The full endpoint energy `(6)` then contradicts every fixed subquartic common modulus directly.

The matching exponent therefore survives two mathematically different reductions. This is evidence of a genuine **method boundary**, not evidence for RH: the current classical prime-family input and the current positive source-incidence machinery both become neutral at exponent four.

It also sharpens the live next question. A new selection or nonnegative endpoint reweighting cannot matter merely because it uses more modes: the complete family already reaches the strongest fixed-power modulus range available from this Burgess/Halász–Montgomery mechanism. To cross the boundary one needs at least one of:

- a prime-supported character-family estimate improving the fixed-modulus Burgess exponent;
- quantitative control of Schlage-Puchta's constants strong enough to let `k` grow with `y` and resolve a genuinely `y^{4-o(1)}` boundary, rather than only every fixed `y^{4-\delta}` range;
- a signed or joint invariant that retains information discarded by total squared bias;
- an arithmetic obstruction to the common source package not expressible solely through its modulus size.

## 4. Prior art and novelty boundary

The analytic theorem is classical prior art. The primary source is Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, Theorem 3. The paper gives a large-sieve-type inequality for prime-supported coefficients; its theorem permits arbitrary fixed `k` when the modulus is cubefree. The publisher record and the public arXiv record were rechecked on 16 September 2026.

`MC-322` already extracted the cubic common-modulus consequence from the `k=3` specialization recorded by Klurman–Mangerel–Teräväinen, while `MC-323` audited the stronger primary-source cubefree and varying-modulus clauses. No new large-sieve, Burgess, or Halász–Montgomery estimate is claimed here.

The exact energy identity `(18)` is elementary binomial variance/Parseval-level arithmetic. No novelty is claimed for it either.

The durable line-specific delta is the composition: the **full reciprocal endpoint energy** and the **arbitrary-`k` fixed cubefree modulus theorem** meet at exponent four. This gives a direct analytic proof of the same quartic source floor previously reached through pair-mode conductor summation, and identifies the quartic frontier as a shared boundary of two distinct proof architectures.

## Boundaries and falsification tests

- **Cubefreeness is load-bearing for arbitrary `k`.** Without it, the cited theorem exposes only bounded choices of `k`, and the subquartic conclusion does not follow from this argument.
- **One common controlled modulus is load-bearing.** For genuinely different individual moduli, Schlage-Puchta's theorem replaces the modulus parameter by `Q^2`; `MC-323` shows that this moves the analogous fixed-power horizon back to exponent `2`.
- **Dense prime support is load-bearing.** The normalization `(11)` uses `A_y\asymp y/\log y`.
- **Distinct endpoint characters are load-bearing.** Independence of the endpoint generators supplies `2^R` distinct functionals; repetitions cannot manufacture the energy `(6)` inside a set of characters.
- **The growth condition `(7)` is explicit.** The theorem does not justify letting `k=k(y)` grow with no control on the `k`-dependent constant. For every fixed `\delta`, `k=k(\delta)` is fixed first.
- **The conclusion is fixed-subquartic, not strictly superquartic.** Equation `(9)` means every fixed exponent below four is eventually excluded. Nothing here rules out `P=y^{4+o(1)}` or proves `P\ge y^{4+\eta}` for any fixed `\eta>0`.
- **No source-incidence rigidity follows from this proof.** The half-loading and near-equality conclusions of `MC-327` remain genuinely additional information supplied by the Plotkin/source representation.
- **No Möbius or RH bound follows.** This is a structural obstruction for the reciprocal-endpoint realization, not an estimate for `M(x)`.

A direct falsification is available at every step: `(3)` fails if the arbitrary-`k` cubefree specialization of Schlage-Puchta does not yield the power balance `(13)`–`(15)`; `(6)` fails if the binomial second moment is miscomputed; the endpoint application fails if the nonzero modes are not distinct characters modulo `4P` or if `4P` is not cubefree. Those are exactly the hypotheses that should be rechecked before any downstream use.

## Consequence for the research line

The quartic source barrier is now overdetermined rather than representation-specific. Pairwise conductor bills plus source incidence reach exponent four from below; the full common-modulus endpoint energy independently reaches exponent four from the analytic side. Both stop there for known reasons.

Accordingly, another rearrangement of the same positive endpoint modes is unlikely to buy a fixed-power gain. The sharper live targets are now the **quartic boundary itself**—especially whether the `k`-dependence in the prime Halász–Montgomery/Burgess input can be quantified well enough to approach `y^{4-o(1)}` with moving parameters—or a genuinely joint/signed arithmetic invariant that is not summarized by total bias energy or positive conductor incidence.