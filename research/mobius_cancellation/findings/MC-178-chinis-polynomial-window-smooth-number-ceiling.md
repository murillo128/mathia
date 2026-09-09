# MC-178 — Chinis square-root blocks remain subpower at polynomial Gallagher windows

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `RATE-BUDGET`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

A natural source-side candidate for the live Gallagher frontier is the Matomäki–Radziwiłł/Chinis large-prime-factor decomposition: factor integers having a prime factor larger than the short-interval length, shorten the complementary Dirichlet polynomial to the mean-value scale, and dispose of the remaining smooth integers separately. Jake Chinis proved under RH that this mechanism gives square-root-order mean square for Liouville sums on a subpolynomial range. However, its published extension to polynomial interval lengths remains only **subpower better than coherent variance**, so in the power taxonomy of `MC-175` and `MC-177` it is still `eta=0`.

Write

\[
V_\lambda(X,h)
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+h}\lambda(n)
\right|^2\,dx.
\tag{1}
\]

Chinis proves, assuming RH,

\[
V_\lambda(X,h)
\ll Xh(\log X)^6
\tag{2}
\]

throughout

\[
h\le H_*(X),
\qquad
H_*(X)
:=
\exp\!\left(
\sqrt{\left(\frac12-o(1)\right)\log X\log\log X}
\right).
\tag{3}
\]

His block-splitting corollary gives for every `h<=X`

\[
\boxed{
V_\lambda(X,h)
\ll
Xh^2(\log X)^6
\left(
\frac1h+rac1{H_*(X)}
\right).
}
\tag{4}
\]

Now fix any `0<theta<1` and put `h=X^theta`. Since `H_*(X)=X^{o(1)}`, the second term in `(4)` dominates and yields only

\[
\frac{V_\lambda(X,X^\theta)}{X}
\ll
X^{2\theta-o(1)}
=
h^{2-o(1)}.
\tag{5}
\]

More sharply, for every fixed `eta>0`, the certified right-hand side of `(4)` satisfies

\[
\frac{h^2(\log X)^6/H_*(X)}{h^{2-\eta}}
=
\frac{X^{\theta\eta}(\log X)^6}{H_*(X)}
\longrightarrow\infty.
\tag{6}
\]

Therefore **Chinis's RH-conditional theorem plus its published block extension does not supply any fixed-power variance suppression `h^(2-eta)` at a fixed polynomial interval scale.** It supplies a very large subpower saving over coherent size, but that is exactly the rate class that `MC-175` shows is invisible to the fixed-power Gallagher phase diagram.

The ceiling is not an arbitrary artifact of the statement. Chinis's proof explains it through the `h`-smooth remainder. Integers having a prime divisor `p>h` can be written `n=pm`, leaving a complementary variable of length

\[
m\ll \frac Xp<\frac Xh,
\tag{7}
\]

which is the scale at which the Dirichlet-polynomial mean-value theorem becomes effective in the argument. The integers with no prime factor above `h` cannot use this one-large-prime shortening and are handled instead through smooth-number sparsity.

Let `Psi(X,h)` count `h`-smooth integers up to `X`, and put

\[
u=\frac{\log X}{\log h}.
\]

The classical Dickman–de Bruijn theory gives, for fixed `u>1`,

\[
\Psi(X,X^{1/u})\sim \rho(u)X,
\qquad \rho(u)>0.
\tag{8}
\]

Hence at a fixed polynomial cutoff `h=X^theta`,

\[
\boxed{
\Psi(X,h)\sim \rho(1/\theta)X,
}
\tag{9}
\]

whereas the complementary mean-value length in `(7)` is only

\[
\frac Xh=X^{1-\theta}.
\tag{10}
\]

Thus a cardinality treatment of the smooth sector loses a full fixed power: the smooth set has order `X`, not order `X/h` up to subpowers. At the subpolynomial scale `(3)`, by contrast, the Dickman decay of `rho(u)` is strong enough to make this counting strategy effective. Writing

\[
\log h=a\sqrt{\log X\log\log X},
\]

the leading Dickman exponent is

\[
\log\frac{\Psi(X,h)}X
=
-\left(\frac1{2a}+o(1)\right)
\sqrt{\log X\log\log X},
\tag{11}
\]

while

\[
\log\frac1h
=-a\sqrt{\log X\log\log X}.
\tag{12}
\]

The balance `1/(2a)=a` is exactly `a=1/sqrt(2)`, explaining the `sqrt(1/2)` boundary in `(3)` at exponential order. This is a method-level explanation, not a new smooth-number theorem.

Consequently, the most tempting existing square-root-variance machinery does **not** bridge the live Mathia gap merely by applying an RH-conditional theorem at longer intervals. To reach the polynomial scales selected by `MC-176`–`MC-177`, one must introduce a new ingredient that obtains signed cancellation inside the smooth sector, or iterates/factors the smooth sector without paying its cardinality. Simply enlarging the interval in the one-large-prime Chinis decomposition moves it into the dense-smooth regime and loses the fixed-power variance gain.

## 1. Chinis's block extension is exactly subpower at polynomial scale

Theorem 1.2 of Chinis gives `(2)` in the range `(3)`. The same paper explicitly records the longer-interval consequence `(4)`, obtained by splitting a long short sum into blocks at the admissible square-root-variance scale and applying Cauchy–Schwarz.

The rate classification is immediate. Since

\[
\log H_*(X)
=O\!\left(\sqrt{\log X\log\log X}\right)
=o(\log X),
\tag{13}
\]

one has `H_*(X)=X^{o(1)}`. For `h=X^theta`,

\[
\frac{h}{H_*(X)}\to\infty,
\]

so `(4)` becomes

\[
V_\lambda(X,h)
\ll
X\,h^2 X^{-o(1)}.
\tag{14}
\]

This is stronger than the coherent deterministic scale `Xh^2`, but weaker than

\[
X^{1+o(1)}h^{2-\eta}
\tag{15}
\]

for every fixed positive `eta`. Equation `(6)` is the exact comparison.

There is no contradiction with the square-root block theorem `(2)`. Cauchy–Schwarz over approximately `h/H_*` blocks pays exactly the number of blocks, so the diagonal variance of each individual block does not remain diagonal after the blocks are recombined without information about their relative signs.

This is the same local-to-global phenomenon already exposed abstractly elsewhere in this line, now occurring **inside a theorem that already assumes RH**: knowing square-root variance on all blocks up to a subpolynomial scale does not black-box transfer square-root variance to a polynomially longer block.

## 2. The smooth-number cutoff explains why the proof stops there

Chinis's Section 4 treats integers with a prime factor `p>h`. Factoring `n=pm` creates a short complementary polynomial, and the prime factor is handled by a pointwise prime Dirichlet-polynomial estimate under RH. Section 5 treats the complementary `h`-smooth integers by their scarcity and the mean-value theorem. Chinis explicitly states that square-root cancellation for larger `h` would require new ideas.

The smooth-number threshold can be read quantitatively from the standard estimate used there. For

\[
h=\exp\!\left(a\sqrt{L\log L}\right),
\qquad L=\log X,
\]

we have

\[
u=\frac{L}{\log h}
=\frac1a\sqrt{\frac{L}{\log L}}.
\]

The classical large-`u` asymptotic

\[
\log\rho(u)
=-u\bigl(\log u+\log\log u-1+o(1)\bigr)
\tag{16}
\]

gives `(11)`. A counting treatment of the smooth sector is competitive with the shortened scale `X/h` only while its relative density is at most roughly `1/h` up to logarithmic/subexponential factors. Comparing `(11)` and `(12)` gives

\[
\frac1{2a}\ge a,
\qquad	ext{i.e.}\qquad
a\le\frac1{\sqrt2}.
\tag{17}
\]

That is the same exponential boundary as Chinis's theorem.

At polynomial `h=X^theta`, the regime changes qualitatively: `u=1/theta` is fixed, so Dickman density no longer decays with `X`. Equation `(9)` then shows why the same smooth-cardinality step cannot possibly produce a polynomial saving. This does **not** prove that the smooth coefficients themselves fail to cancel; it proves that treating them only as a sparse exceptional set has exhausted its range.

## 3. Exact relation to the Gallagher frontier

`MC-176` shows that diagonal Gallagher heat type at horizon `tau` forces ordinary signed short-interval second moment of diagonal exponential order at

\[
H=X^{\,1-4\tau+o(1)}
\tag{18}
\]

for `1/8<=tau<1/4`. Every fixed `tau<1/4` therefore selects a fixed polynomial interval exponent. At the strongest twist-stable endpoint,

\[
\tau=\frac18,
\qquad H=X^{1/2+o(1)}.
\tag{19}
\]

This lies far beyond the subpolynomial range `(3)`. Applying Chinis's block extension at `h=X^(1/2)` gives only

\[
\frac{V_\lambda(X,h)}X
\ll
\frac{X(\log X)^6}{H_*(X)}
=
X^{1-o(1)},
\tag{20}
\]

rather than diagonal order `h=X^(1/2)` up to subpowers.

Likewise, the direct transfer optimum in `MC-177` occurs at a polynomial local scale `H=X^(2/3)`. Equation `(4)` at that scale again yields only `H^(2-o(1))`, not a fixed-power interpolation `H^(2-eta)`.

The comparison is deliberately made with Liouville because Chinis's theorem is stated for `lambda`, and the line uses Liouville as a mandatory multiplicative control. No Möbius variance theorem is inferred from it. The point is narrower and robust: **one of the strongest clean square-root-variance mechanisms available for a closely related prime-sign function already shows where the large-prime-factor decomposition ceases to buy polynomial information.** Any Möbius adaptation that wins at `(18)` must exploit structure absent from the cardinality treatment of the smooth sector.

## 4. Prior art and novelty assessment

The main literature input is Jake Chinis, *On the Liouville Function in Short Intervals*, International Mathematics Research Notices 2022, no. 2, 1299–1316, DOI `10.1093/imrn/rnab063`, arXiv:2007.06788. Theorem 1.2 is `(2)`–`(3)`, and the paper's longer-interval corollary is `(4)`. Chinis's proof also explicitly identifies the split into integers with a prime factor greater than `h` and the `h`-smooth remainder, and says that larger-`h` square-root cancellation needs new ideas.

The smooth-number input is classical Dickman–de Bruijn theory; a convenient authoritative survey is Adolf Hildebrand and Gerald Tenenbaum, *Integers without large prime factors*, Journal de théorie des nombres de Bordeaux 5 (1993), 411–484, DOI `10.5802/jtnb.101`. Chinis cites its Corollary 1.3 for the smooth-number estimate used in his Section 5.

A targeted search through current short-interval Liouville/Möbius literature found no later integer theorem replacing Chinis's polynomial-window block loss by a fixed-power diagonal variance estimate. Recent progress on all-interval Möbius cancellation and higher/Fourier uniformity supplies strong `o(1)` or logarithmic relative cancellation, but `MC-175` already prices those rate classes as `eta=0` at fixed polynomial resolution. No novelty is claimed for Chinis's theorem, its block corollary, the Dickman asymptotics, or the observation in Chinis that the smooth remainder is the large-`h` obstruction.

The Mathia-specific durable contribution is the **rate dictionary** connecting these established facts to `MC-175`–`MC-177`: the RH-conditional square-root block theorem, when transported by its own published longer-window mechanism, still lands in the `eta=0` class at every fixed polynomial Gallagher window, and the smooth-number asymptotic explains why the one-large-prime proof architecture crosses exactly into a dense remainder there.

## Boundaries and failure modes

This finding does not claim that RH fails to imply stronger polynomial-window Liouville variance by some other method. It classifies Chinis's theorem, its block extension, and the smooth-cardinality proof architecture only.

It also does not claim that `h`-smooth Möbius or Liouville coefficients have coherent signs. Equation `(9)` is a support-density statement. A phase-sensitive theorem proving cancellation within that dense smooth sector would evade the obstruction and would be exactly the kind of new source-side ingredient the live frontier seeks.

The fixed-`theta` Dickman asymptotic is used only to show the density transition at polynomial smoothness. The more precise `a=1/sqrt(2)` computation uses the standard large-`u` asymptotic for `rho`; logarithmic corrections do not alter the leading boundary.

The comparison from `(4)` to `eta=0` concerns the **strength certified by the theorem**, not a lower bound on the true variance. A weaker published upper bound cannot prove that stronger cancellation is false.

Finally, Liouville is not Möbius. The exact square-free zeros of `mu` could in principle be exploited by a Möbius-specific decomposition. Any such proposed improvement must demonstrate a fixed-power gain rather than merely replacing the dense smooth set by another `X^(1-o(1))` support class.

## Consequences for the live frontier

The next Dirichlet-polynomial attack should not treat the Chinis/MR large-prime extraction as if a modest quantitative sharpening of its existing smooth-number estimate could reach the Gallagher target. At every fixed polynomial window the remainder has crossed from sparse to positive-density smooth-number geometry, while the block extension loses all fixed-power variance gain.

A viable continuation must therefore do at least one of two genuinely stronger things: obtain **signed, phase-sensitive cancellation inside the polynomially smooth sector**, or replace the single-large-prime split by an iterated/multiscale factorization whose remaining polynomial is short without discarding Möbius orientation. The decisive audit for either route is whether it yields a fixed `eta>0` in the local second-moment currency of `MC-177`; logarithmic or `X^{-o(1)}` gains remain insufficient.