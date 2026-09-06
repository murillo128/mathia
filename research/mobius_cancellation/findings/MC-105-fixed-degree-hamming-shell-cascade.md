# MC-105 — Every fixed Hamming degree has a positive Landau main term, forcing cancellation to escape to growing degree

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation from `MC-092` be

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
C_{k,N}=\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a),
\tag{1}
\]

with the exact pair-level representation

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right).
\tag{2}
\]

`MC-097` proves the positive degree-two asymptotic

\[
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\qquad
c_2=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0.
\tag{3}
\]

That phenomenon is not special to degree two. For **every fixed integer `k>=2`**,

\[
\boxed{
C_{k,N}
\sim
c_2\,
\frac{2^{k-2}}{(k-2)!}
\frac{N^2(\log\log N)^{k-2}}{(\log N)^2}.
}
\tag{4}
\]

Hence every fixed Hamming shell of degree at least two is eventually positive. More sharply, for each fixed `k>=2`,

\[
\boxed{
\frac{C_{k+1,N}}{C_{k,N}}
\sim
\frac{2\log\log N}{k-1}
\longrightarrow\infty.
}
\tag{5}
\]

Consequently, for every fixed `K>=2`, the signed partial radial sum is dominated by its highest retained shell:

\[
\boxed{
\sum_{k=2}^{K}(-1)^k C_{k,N}
\sim
(-1)^K C_{K,N}.
}
\tag{6}
\]

The hard endpoint is nevertheless logarithmically smaller than every one of these fixed-shell scales. By the unconditional Korobov--Vinogradov input used in `MC-098`,

\[
\mathcal Q_N(1)=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\quad\text{for every fixed }A>0,
\tag{7}
\]

while `C_{0,N}=O(N)` and `C_{1,N}=O(N\log\log N)`. Therefore the complementary tail beyond **any fixed degree** must cancel the dominant fixed partial sum:

\[
\boxed{
\sum_{k>K}(-1)^k C_{k,N}
\sim
-(-1)^K C_{K,N}
}
\qquad(K\ge2\text{ fixed}).
\tag{8}
\]

Thus the cancellation already known to occur in the actual source is a genuine **growing-degree cascade**. It cannot be localized to degree two versus one fixed higher shell, to any fixed finite Taylor jet, or to a recurrence involving only finitely many Hamming degrees independent of `N`. Any source-specific signed cross-degree mechanism that hopes to explain or transport the endpoint cancellation must reach degrees tending to infinity with `N`, or use a non-radial relation that bypasses this fixed-degree hierarchy.

No improved estimate for `M(x)` is claimed.

## 1. Pairwise square-free coordinates separate the common support from the Hamming degree

Every nonzero pair in `(2)` has square-free `m,n`. Write uniquely

\[
b=(m,n),
\qquad
m=bd,
\qquad
n=be.
\tag{9}
\]

Then `b,d,e` are pairwise coprime and square-free. The primes of `b` occur in both coordinates and therefore disappear from the symmetric difference, while the primes of `d` and `e` occur in exactly one coordinate. Hence

\[
d_\triangle(m,n)=\omega(d)+\omega(e).
\tag{10}
\]

If `x=N/b`, the sawtooth phase becomes

\[
z\!\left(\frac{N^2}{mn}\right)
=z\!\left(\frac{x^2}{de}\right).
\tag{11}
\]

Therefore, for every fixed `k`,

\[
\boxed{
C_{k,N}
=
\sum_{\substack{b\le N\\b\ \mathrm{squarefree}}}
\sum_{j=0}^{k}
\sum_{\substack{d,e\le N/b\\d,e\ \mathrm{squarefree}\\(d,e)=1\\(de,b)=1\\\omega(d)=j\\\omega(e)=k-j}}
 z\!\left(\frac{(N/b)^2}{de}\right).
}
\tag{12}
\]

This is only a reindexing of the exact source sum. It introduces no probabilistic independence and no new smoothing.

The edge splits `j=0` or `j=k` have one of `d,e` equal to one. Their total contribution is negligible at the scale in `(4)`. Indeed, the classical fixed-`k` almost-prime upper bound gives at most `N^{1+o(1)}` such pairs after summing over `b`, whereas the main scale in `(4)` is `N^{2-o(1)}`.

## 2. Fixed products of distinct primes become Lebesgue-distributed after scaling

For fixed `r>=1`, let

\[
A_r(x)
:=
\#\{n\le x:n\text{ square-free},\ \omega(n)=r\}.
\tag{13}
\]

Landau's classical fixed-`r` theorem for products of `r` distinct primes gives

\[
\boxed{
A_r(x)
\sim
\frac{x(\log\log x)^{r-1}}{(r-1)!\log x}.
}
\tag{14}
\]

For each fixed `0<u<=1`, applying `(14)` at `ux` gives

\[
\frac{(r-1)!\log x}{x(\log\log x)^{r-1}}
A_r(ux)
\longrightarrow u.
\tag{15}
\]

Thus the normalized counting measures

\[
\nu_{r,x}
:=
\frac{(r-1)!\log x}{x(\log\log x)^{r-1}}
\sum_{\substack{n\le x\\n\ \mathrm{squarefree}\\\omega(n)=r}}
\delta_{n/x}
\tag{16}
\]

converge weakly on `[0,1]` to Lebesgue measure.

The bounded kernel

\[
f(u,v)=z\!\left(\frac1{uv}\right)
\tag{17}
\]

may be defined arbitrarily on the axes. Away from the axes its only discontinuities lie on the countable family `uv=1/m`, each of two-dimensional Lebesgue measure zero. Product weak convergence therefore gives, for fixed `j,l>=1`,

\[
\sum_{\substack{d,e\le x\\d,e\ \mathrm{squarefree}\\\omega(d)=j\\\omega(e)=l}}
 z\!\left(\frac{x^2}{de}\right)
\sim
J\,
\frac{x^2(\log\log x)^{j+l-2}}
{(j-1)!(l-1)!(\log x)^2},
\tag{18}
\]

where the same kernel integral as in `MC-097` appears:

\[
J:=\int_0^1\!\int_0^1 z\!\left(\frac1{uv}\right)\,du\,dv
=\gamma+\gamma_1-\frac12>0.
\tag{19}
\]

The pairwise-coprime restriction in `(12)` does not change `(18)` at leading order. For a fixed prime `p`, requiring `p|d` removes one freely varying prime factor and therefore one power of `log log x`; summing common-prime pairs can be handled by first restricting `p<=Y` and then using the convergent `sum_{p>Y}p^{-2}` tail together with the Hardy--Ramanujan fixed-degree upper bound. The boundary cases with `j=1` or `l=1` are smaller still. The same argument shows that, for each fixed square-free `b`, excluding the finitely many primes dividing `b` from `d,e` changes only a lower-order term.

Hence, for fixed `b` and fixed interior split `j+l=k`, `j,l>=1`, putting `x=N/b` in `(18)` yields

\[
\boxed{
S_{j,l}^{(b)}(N)
\sim
\frac{J}{b^2}
\frac{N^2(\log\log N)^{k-2}}
{(j-1)!(l-1)!(\log N)^2},
}
\tag{20}
\]

where `S_{j,l}^{(b)}` denotes the corresponding restricted inner sum in `(12)`.

## 3. The common square-free factor contributes exactly the degree-two Euler constant

It remains to sum `(20)` over `b`. This passage is uniform enough for dominated convergence.

For `b<=sqrt(N)`, the Hardy--Ramanujan upper bound for fixed-degree almost-prime counts and `|z|<=1/2` give, after normalization by the right-hand scale of `(4)`, a bound `O_k(1/b^2)`. For `b>sqrt(N)`, the crude pair bound `O((N/b)^2)` sums to `O(N^{3/2})`, which is negligible compared with `N^2(\log\log N)^{k-2}/(\log N)^2`. Therefore one may first truncate the `b`-sum, apply `(20)` termwise, and then let the truncation tend to infinity.

The square-free common-factor mass is

\[
\sum_{b\ \mathrm{squarefree}}\frac1{b^2}
=\prod_p(1+p^{-2})
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
\tag{21}
\]

Summing the interior degree splits gives

\[
\sum_{j=1}^{k-1}
\frac1{(j-1)!(k-j-1)!}
=
\frac{2^{k-2}}{(k-2)!}.
\tag{22}
\]

Combining `(20)`--`(22)` gives

\[
C_{k,N}
\sim
\frac{15J}{\pi^2}
\frac{2^{k-2}}{(k-2)!}
\frac{N^2(\log\log N)^{k-2}}{(\log N)^2}.
\tag{23}
\]

By `MC-097`, `15J/pi^2=c_2`, proving `(4)`. Equation `(5)` follows by dividing the asymptotics for consecutive fixed degrees.

## 4. Any fixed finite radial truncation is asymptotically dominated by its last shell

Fix `K>=2`. Repeated use of `(5)` shows that

\[
C_{2,N}+\cdots+C_{K-1,N}=o(C_{K,N}).
\tag{24}
\]

All the terms in `(24)` are eventually positive, so signs only enter when the endpoint recombines the shells. Equation `(24)` immediately yields `(6)`.

The degree-zero and degree-one bounds from `MC-098` are also `o(C_{K,N})`. Choosing `A>2` in the unconditional endpoint estimate `(7)` gives

\[
\mathcal Q_N(1)=o(C_{K,N}).
\tag{25}
\]

Subtracting the fixed partial sum from the exact endpoint identity

\[
\mathcal Q_N(1)
=C_{0,N}-C_{1,N}
+\sum_{k=2}^{K}(-1)^kC_{k,N}
+\sum_{k>K}(-1)^kC_{k,N}
\tag{26}
\]

then proves `(8)`.

This strengthens `MC-098`. There the higher-degree tail was shown to cancel the positive degree-two main term. Here the same statement holds after **every fixed cutoff**: once degree three is included, degree four eventually dominates it; once degree four is included, degree five eventually dominates; and so on. The compensating signed mass is never confined to a fixed finite set of degrees as `N` grows.

## 5. Prior art and novelty boundary

The fixed-`k` almost-prime asymptotic `(14)` is classical Landau theory. A modern authoritative reference is Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, American Mathematical Society (2019), Chapter 15, Exercise 15.4, which states Landau's fixed-`k` formula for `omega(n)` together with a Hardy--Ramanujan uniform upper bound. For the square-free/distinct-prime formulation used here, Christian Elsholtz and Stefan Planitzer, *On Erdős and Sárközy's sequences with Property P*, Monatshefte für Mathematik 182 (2017), 565--575, DOI `10.1007/s00605-016-0995-9`, explicitly records Landau's asymptotic for products of `k` distinct primes.

The weak-convergence step `(15)`--`(18)` is an immediate scaling consequence of that classical asymptotic. The kernel integral `J`, its positivity, and the square-free common-factor constant were already derived and audited in `MC-097` for degree two. A targeted search around fixed-`k` almost-prime weighted sums, scaled almost-prime distributions, Hamming-shell Möbius decompositions, and Landau/Sathe--Selberg radial coefficients found no basis for claiming a new external theorem corresponding to `(4)`.

**No novelty claim is made.** The durable line-specific result is the application of classical fixed-degree almost-prime distribution to the exact source decomposition `(12)`, showing that the `MC-097` positive shell is the first member of an entire fixed-degree hierarchy and deriving the growing-degree cancellation consequence `(8)`.

## 6. Boundaries and falsification tests

- Equation `(4)` is a **fixed-`k` asymptotic**. It is not uniform for `k` growing with `N`. Extrapolating the factorial coefficient into the central range `k~log log N` would require a Sathe--Selberg-type uniform analysis and is not asserted here.
- The resemblance of `(4)` to a Poisson coefficient does not establish that the full Hamming shell profile is Poisson, nor that one may sum the fixed-`k` asymptotics over all degrees.
- Positivity of every fixed shell does not imply positivity of `mathcal Q_N(t)` at a fixed `t`, because degrees growing with `N` may already contribute at the same or larger scale.
- The proof uses only classical almost-prime distribution plus the exact source kernel. It supplies no power saving for the endpoint and no new zero-free region.
- Equation `(8)` does not identify which growing degrees carry the compensating mass or how they interact. It only proves that no `N`-independent finite cutoff contains the cancellation.
- A source-specific recurrence whose order grows with `N`, a relation coupling many degrees at once, or a non-radial observable may evade this obstruction. A fixed-order differential/Taylor identity can remain useful only if its coefficients or evaluation points implicitly access the growing-degree tail rather than close on finitely many fixed shells.

The decisive continuation is therefore to determine the first growing-degree regime in which `(4)` ceases to be a valid approximation and whether a Sathe--Selberg-scale description of the **signed source kernel**, not merely almost-prime counts, exposes a controlled cross-degree relation. Any such continuation must preserve the actual sawtooth/product-fiber weights and must not replace them by an unsigned Poisson model.

## Consequence for the research line

`MC-103` and `MC-104` show that generic degree-only reconstruction from favorable Hamming windows is too ill-conditioned unless extra source structure is used. `MC-105` identifies one such source-specific structure exactly enough to sharpen the frontier: the actual low-degree coefficients obey a classical almost-prime hierarchy, but that hierarchy is itself an obstruction to any **fixed-order** rescue.

The missing signed relation must now be genuinely multiscale in Hamming degree. It must either control a degree range that grows with `N`, connect the growing radial tail to a cheaper arithmetic observable, or leave the radial quotient. Fixed finite Taylor jets, fixed-order curvature identities, and finitely many explicitly subtracted low shells cannot contain the endpoint cancellation already forced by the source.