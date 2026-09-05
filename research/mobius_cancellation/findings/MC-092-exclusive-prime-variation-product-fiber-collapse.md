# MC-092 — Exclusive-prime variation collapses to a degree-weighted product-fiber parity correlation

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-091` rewrites the first variation of the prime-symmetric-difference deformation as a sum of rectangular p-sifted Huxley--Watt blocks,

\[
\mathcal Q_N'(1)
=-2\sum_{p\le N}Q_p(N/p,N),
\tag{1}
\]

and observes that the individual old-exponent block scales have an ell-2 tail that is power-improving above the half exponent. The prime index in `(1)` is nevertheless **not an independent orthogonal coordinate of the source**. After the exact product-fiber quotient already used in `MC-033`, every exclusive-prime contribution on one fiber has the same Möbius sign and the same sawtooth phase, so the prime sum collapses to a single degree-weighted parity correlation.

For square-free coprime `a,b`, let

\[
R_N(a,b)
:=
\#\left\{d\mid a:\frac{ab}{N}\le d\le\frac{N}{b}\right\},
\tag{2}
\]

and put

\[
\omega_{>P}(a):=\#\{p\mid a:p>P\}.
\tag{3}
\]

Then the full deformation of `MC-091` has the exact fiber form

\[
\boxed{
\mathcal Q_N(t)
=
\sum_{\substack{a,b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)(-t)^{\omega(a)}
 z\!\left(\frac{N^2}{ab^2}\right).
}
\tag{4}
\]

Consequently

\[
\boxed{
\mathcal Q_N'(1)
=
\sum_{\substack{a,b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
\mu(a)\omega(a)R_N(a,b)
 z\!\left(\frac{N^2}{ab^2}\right).
}
\tag{5}
\]

More sharply, for every threshold `P>=1`, the large-prime part of `(1)` satisfies

\[
\boxed{
-2\sum_{P<p\le N}Q_p(N/p,N)
=
\sum_{\substack{a,b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
\mu(a)\omega_{>P}(a)R_N(a,b)
 z\!\left(\frac{N^2}{ab^2}\right).
}
\tag{6}
\]

Thus a source-compatible estimate for the large-prime sum is exactly an estimate for an `omega_{>P}`-weighted version of the same product-fiber parity character isolated by `MC-033` and `MC-034`. The individual p-block decomposition is useful algebraically, but **blockwise ell-2 cancellation does not follow from the fact that the blocks have different prime labels**: on a fixed product fiber, all labels `p|a` contribute coherently and are already combined by the scalar multiplicity `omega_{>P}(a)`.

This does not kill the `MC-091` route. It identifies the correct joint target. If a large-sieve, bilinear, spectral, or other theorem proves cancellation in the p-sum, it must in particular control the weighted deterministic parity correlation in `(6)`; it cannot be justified by assigning independent signs to the p-blocks.

There is also a matched-control calibration that removes a possible power-budget objection. Define

\[
W_N(a)
:=
\sum_{\substack{b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)
 z\!\left(\frac{N^2}{ab^2}\right),
\tag{7}
\]

so `(6)` is

\[
D_{N,P}:=-2\sum_{P<p\le N}Q_p(N/p,N)
=
\sum_a\mu(a)\omega_{>P}(a)W_N(a).
\tag{8}
\]

For independent Rademacher prime signs `xi_p`, let

\[
f_\xi(a)=\prod_{p\mid a}\xi_p
\]

on square-free `a`, and consider the matched multiplicative control

\[
D_{N,P}(\xi)
:=
\sum_a f_\xi(a)\omega_{>P}(a)W_N(a).
\tag{9}
\]

Square-free Walsh orthogonality gives exactly

\[
\boxed{
\mathbb E D_{N,P}(\xi)=0,
\qquad
\operatorname{Var}D_{N,P}(\xi)
=
\sum_{a>1}\omega_{>P}(a)^2W_N(a)^2.
}
\tag{10}
\]

If `P>1`, put

\[
L_{N,P}:=\left\lfloor\frac{2\log N}{\log P}\right\rfloor.
\tag{11}
\]

Since every relevant `a` is at most `N^2`, `omega_{>P}(a)<=L_{N,P}`. Using `|z|<=1/2`, `R_N(a,b)<=2^{omega(a)}`, and at most `N/sqrt(a)` possible `b`,

\[
|W_N(a)|
\le
\frac{N}{2\sqrt a}2^{\omega(a)}.
\tag{12}
\]

The same elementary Euler-product estimate used in `MC-034`,

\[
\sum_{\substack{a\le N^2\\a\ \mathrm{squarefree}}}
\frac{4^{\omega(a)}}a
=O((\log N)^4),
\tag{13}
\]

therefore yields

\[
\boxed{
\operatorname{sd}D_{N,P}(\xi)
=O\!\left(NL_{N,P}(\log N)^2\right).
}
\tag{14}
\]

In particular, for every fixed `delta>0` and `P=N^delta`,

\[
\boxed{
\operatorname{sd}D_{N,N^\delta}(\xi)
=O_\delta(N(\log N)^2).
}
\tag{15}
\]

The whole large-prime variation therefore already has the critical square-scale **power** in the matched random multiplicative ensemble. The remaining difficulty is deterministic: actual Möbius is the all-minus Walsh point `f_{-1}(a)=mu(a)`, and the variance in `(10)` does not bound that point.

A clean normalized target is

\[
Z^{\rm deg}_{N,P}
:=
\frac{
\sum_a\mu(a)\omega_{>P}(a)W_N(a)
}{
\left(\sum_{a>1}\omega_{>P}(a)^2W_N(a)^2\right)^{1/2}
},
\tag{16}
\]

when the denominator is nonzero. For fixed `delta>0`, a deterministic theorem `Z^{deg}_{N,N^delta}=N^{o(1)}` would put the large-prime first variation itself at `N^{1+o(1)}`. No such theorem is proved here, and even such a bound would still leave the small-prime and interpolation/reconstruction obligations identified in `MC-091`.

## 1. Product fibers diagonalize the deformation parameter

A nonzero pair in `mathcal Q_N(t)` has square-free `m,n`. Write its product uniquely as

\[
mn=ab^2,
\]

with `a,b` square-free and coprime. As in `MC-033`, every admissible pair is

\[
m=bd,
\qquad
n=b\frac ad,
\qquad d\mid a,
\tag{17}
\]

subject to the two cutoffs `m,n<=N`. The primes of `b` occur in both coordinates and the primes of `a` occur in exactly one coordinate. Hence, for **every** admissible representation of the same product fiber,

\[
d_\triangle(m,n)=\omega(a).
\tag{18}
\]

There are exactly `R_N(a,b)` such representations. Grouping the finite sum by `(a,b)` therefore proves `(4)`.

At `t=1`, `(-1)^{omega(a)}=mu(a)`, recovering the `MC-033` product-fiber coefficient. Differentiating the finite identity `(4)` gives `(5)` immediately. This also shows conceptually what the deformation does after the product quotient: it damps each square-free kernel only according to its prime-support degree. The apparent coordinate-by-coordinate deformation becomes a degree weighting on the already existing parity carrier.

## 2. A thresholded prime sum is exactly a truncated degree weight

For a fixed prime `p`, the p-contribution to the derivative before product grouping is

\[
\sum_{m,n\le N}
\mu(m)\mu(n)
\mathbf 1_{\{p\mid m\}\triangle\{p\mid n\}}
 z\!\left(\frac{N^2}{mn}\right).
\tag{19}
\]

`MC-091` proves that `(19)=-2Q_p(N/p,N)`. On a product fiber `ab^2`, the exclusive-prime indicator in `(19)` is one exactly when `p|a`. Every admissible factorization of that fiber has the same sign `mu(a)` and the same sawtooth value. Summing `(19)` over `P<p<=N` therefore counts each representation exactly `omega_{>P}(a)` times and proves `(6)`.

This is the precise coherence missing from a naive prime-block square-function interpretation. Two distinct primes `p,q|a` do not supply independent signed contributions on that fiber: both add the same scalar `mu(a)z(N^2/(ab^2))`. Any useful joint estimate must obtain cancellation **between different square-free kernels/product fibers or against another source term**, not from independent signs attached to the prime labels themselves.

The formal ell-2 tail in `MC-091`,

\[
N^{2\beta}P^{1/2-\beta},
\]

remains a valid conditional ledger for the magnitudes of separately bounded rectangular blocks under a prior Mertens exponent `beta>1/2`. Equation `(6)` shows that this ledger is not an intrinsic orthogonality norm supplied by the decomposition. Replacing the prime sum by that ell-2 norm requires an additional theorem.

## 3. Matched multiplicative RMS survives the degree weight

Equation `(8)` is a Walsh expansion over square-free prime-support characters. Under independent Rademacher prime signs,

\[
\mathbb E[f_\xi(a)f_\xi(a')]=\mathbf 1_{a=a'}.
\tag{20}
\]

Because `omega_{>P}(1)=0`, the control functional `(9)` has zero mean, and `(10)` follows exactly.

For `(12)`, the number of admissible `b` is at most `N/sqrt(a)`, while `R_N(a,b)` counts divisors of square-free `a` and is at most `2^{omega(a)}`. The sawtooth has absolute value at most one half. Since `a<=N^2`, `(11)` bounds the number of its prime factors exceeding `P`. Combining these observations with `(13)` proves `(14)` and `(15)`.

The estimate `(13)` is the same robust reciprocal-prime Euler-product bound already audited in `MC-034`; no independence of product fibers or p-blocks is inserted. Orthogonality occurs only after the exact source quotient, among the distinct square-free kernel characters `f_xi(a)`.

This distinction matters. The random control shows that the degree weight does **not** create a generic polynomial obstruction to critical-scale cancellation. But it simultaneously shows where the randomness actually lives: in the parity characters indexed by `a`, not in an independently randomized copy of each rectangular p-block.

## 4. Prior art and novelty boundary

The Huxley--Watt finite identity and arbitrary rectangular cutoffs are classical prior art (`MC-S24`). The square-free product-fiber normal form and its central-divisor weight are `MC-033`; the exact random multiplicative Walsh orthogonality and `N^{1+o(1)}` RMS mechanism for bounded radial Huxley--Watt kernels are already established in `MC-034`. The prime-symmetric-difference deformation and rectangular p-block identity are `MC-091`.

The product Hamming kernel and the fact that differentiating a coordinate-symmetric Hamming weight introduces the support degree are standard Boolean/Walsh mechanisms. A targeted literature check around Hamming/noise kernels, `mu(n)omega(n)` weights, Huxley--Watt sums, and exponential sums with an auxiliary parameter supplied no basis for claiming a new external theorem here. In particular, the classical Huxley--Watt parameter-averaging literature can produce savings for suitable exponential-sum families, but it does not by itself establish an estimate for the exact deterministic weighted parity correlation `(8)`.

**No novelty claim is made.** The durable line-specific content is the exact identification `(4)`--`(6)` of what the new p-indexed route is actually measuring, together with the matched-control power calibration `(10)`--`(15)`.

## 5. Boundaries and decisive continuation

Equation `(6)` does not prove that a large-sieve or bilinear argument cannot estimate the p-sum. It says only that such an argument must exploit arithmetic structure strong enough to control the same degree-weighted product-fiber correlation; prime labels alone do not confer orthogonality.

Equation `(15)` is a matched-control statement, not a transfer theorem for Möbius. The all-minus prime-sign assignment is one distinguished deterministic Walsh point and can be much larger than its ensemble RMS without contradiction.

The weight `omega_{>P}(a)` is bounded when `P=N^delta` with fixed `delta`, but it is not constant. A theorem for the unweighted parity statistic of `MC-034` does not automatically imply one for `(8)` unless it is uniform enough to survive this degree weighting.

Finally, control of `D_{N,P}` is only the **large-prime first-variation** obligation. It does not control the small-prime part of `mathcal Q_N'(1)`, and an endpoint derivative estimate does not reconstruct `mathcal Q_N(1)` from easier values of `t`. The full interpolation and scale-doubling ledger from `MC-091` remains mandatory.

The decisive next test is therefore sharper than “find orthogonality across the p-blocks.” One must prove or refute a source-natural deterministic estimate for the normalized weighted parity correlation `(16)`—or an equivalent coupled statistic—using hypotheses independently weaker than the desired Mertens gain. If that succeeds, the result must then be inserted into the complete small-prime plus interpolation/reconstruction ledger. A matched multiplicative comparator with the proposed auxiliary hypotheses but polynomially large `(16)`, or an exact reduction of the required estimate back to an improved Mertens bound, kills that version of the route.

## Consequence for the research line

`MC-091` escaped the gcd-mask obstruction by differentiating exclusive prime membership, but its surviving hope was phrased as a joint estimate across prime-indexed rectangular blocks. `MC-092` identifies the exact quotient of that hope: the whole large-prime block sum is already one `omega_{>P}`-weighted product-fiber parity correlation.

This removes **prime-block index orthogonality as a free source of information** while preserving a nontrivial route. Matched random multiplicative signs achieve the critical power for the entire weighted variation, so the target is not generically overconstrained. The unresolved arithmetic burden is now deterministic and explicit: control the all-minus parity point against the degree-weighted Huxley--Watt product-fiber weights, then show that the interpolation/iteration ledger retains a strict gain.