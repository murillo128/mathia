# MC-091 — Prime-symmetric-difference deformation exposes a rectangular large-prime variation

**Status:** `EXACT-DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-090` shows that every retained mask depending only on `gcd(m,n)` keeps the unsifted Huxley--Watt top block unless it also cancels the scale-doubling target. There is nevertheless a source-compatible way to leave the gcd-mask class without inventing an external geometric coordinate: deform the **exclusive prime membership** of the two square-free arguments.

For square-free `n`, write

\[
\mathcal P(n):=\{p:p\mid n\},
\]

and for square-free `m,n` let

\[
d_\triangle(m,n)
:=|\mathcal P(m)\triangle\mathcal P(n)|
=\omega(m)+\omega(n)-2\omega(\gcd(m,n)).
\tag{1}
\]

With the Huxley--Watt sawtooth

\[
z(x)=\lfloor x\rfloor+\frac12-x,
\]

define, for `0<=t<=1`,

\[
\mathcal Q_N(t)
:=
\sum_{m,n\le N}
\mu(m)^2\mu(n)^2
(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right).
\tag{2}
\]

The two endpoints are exact:

\[
\boxed{\mathcal Q_N(1)=Q_1(N)}
\tag{3}
\]

for the Möbius Huxley--Watt block `Q_1(N)` of `MC-090`, because on square-free support

\[
(-1)^{d_\triangle(m,n)}=\mu(m)\mu(n),
\]

while

\[
\boxed{
\mathcal Q_N(0)
=
\sum_{\substack{m\le N\\m\ \mathrm{squarefree}}}
 z\!\left(\frac{N^2}{m^2}\right)
}
\tag{4}
\]

is purely diagonal. Thus `(2)` is an exact prime-coordinate interpolation from a diagonal form to the hard Möbius bilinear form.

More importantly, its first variation at the Möbius endpoint has a completely explicit arithmetic decomposition. Put

\[
\nu_p(a):=\mu(a)\mathbf 1_{p\nmid a}
\]

and, for real `X,Y>=1`, define the p-sifted rectangular sawtooth block

\[
Q_p(X,Y)
:=
\sum_{a\le X}\sum_{b\le Y}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{XY}{ab}\right).
\tag{5}
\]

Then

\[
\boxed{
\mathcal Q_N'(1)
=-2\sum_{p\le N} Q_p(N/p,N).
}
\tag{6}
\]

Each prime-coordinate variation is therefore a **lower-product-scale rectangular Huxley--Watt block**, of natural product scale `N^2/p`. This crosses the exact hypothesis of `MC-090`: the deformation depends on primes dividing exactly one coordinate, not only on their common divisor.

However, termwise recursive control is still not a contraction mechanism. Assume a prior Mertens exponent

\[
M(x)=O(x^\beta),
\qquad \frac12<\beta<1.
\tag{7}
\]

Then uniformly in `p<=N`,

\[
\boxed{
Q_p(N/p,N)
=O_\beta\!\left((N^2/p)^\beta\right).
}
\tag{8}
\]

Consequently separate absolute estimation of the prime layers gives only

\[
|\mathcal Q_N'(1)|
\ll_\beta
N^{2\beta}\sum_{p\le N}p^{-\beta}
\ll_\beta N^{1+\beta},
\tag{9}
\]

whose power `1+beta` is strictly larger than the old square-scale power `2beta` for every `beta<1`. The first variation cannot be made useful merely by recursively estimating each lower-scale prime block and taking a triangle inequality.

The same decomposition also exposes a sharper surviving target. The **square-sum scale** of the large-prime layers is different. For `P>=2`,

\[
\boxed{
\left(
\sum_{p>P}
\bigl((N^2/p)^\beta\bigr)^2
\right)^{1/2}
\ll_\beta
N^{2\beta}P^{1/2-\beta}.
}
\tag{10}
\]

Hence at a moving threshold `P=N^\delta`, `delta>0`, the formal ell-2 budget is

\[
N^{\,2\beta-\delta(\beta-1/2)},
\tag{11}
\]

which is a strict power improvement over `N^{2 beta}` precisely when `beta>1/2`. At the half exponent the power gain disappears. Equation `(10)` is **not** a bound for the signed prime sum in `(6)`; it is the exact quantitative benchmark that a genuine cross-prime orthogonality or large-sieve-type estimate would have to realize.

Thus this deformation identifies a new, sharply delimited escape route from `MC-090`: not another divisor mask and not termwise p-adic recursion, but a joint estimate across the prime-indexed rectangular blocks. The route survives only if the source supplies cancellation across those blocks strong enough to approach the ell-2 scale while the small-prime part and the interpolation/reconstruction ledger remain subordinate.

No improved estimate for `M(x)` is claimed.

## 1. Endpoint identities

For square-free `m,n`, the parity identity

\[
|\mathcal P(m)\triangle\mathcal P(n)|
\equiv
|\mathcal P(m)|+|\mathcal P(n)|\pmod 2
\]

gives

\[
(-1)^{d_\triangle(m,n)}
=(-1)^{\omega(m)+\omega(n)}
=\mu(m)\mu(n).
\]

Since `mu^2` restricts `(2)` to square-free arguments, setting `t=1` proves `(3)`.

At `t=0`, the factor `0^{d_triangle}` vanishes unless the two prime-support sets are equal. Two square-free positive integers with the same prime support are equal, so only `m=n` survives, proving `(4)`.

Prime by prime, the local weight in `(2)` has the two-coordinate matrix

\[
\begin{pmatrix}
1&-t\\
-t&1
\end{pmatrix}.
\tag{12}
\]

The tensor-product/Hamming-kernel interpretation of such matrices is classical. It is used here only as an exact coordinate description; no Boolean-cube theorem is needed for the arithmetic claims below.

## 2. Exact endpoint derivative

Differentiate `(2)` at `t=1`. If `d=d_triangle(m,n)`, then

\[
\left.\frac{d}{dt}(-t)^d\right|_{t=1}
=d(-1)^d.
\]

Therefore

\[
\mathcal Q_N'(1)
=
\sum_{m,n\le N}
\mu(m)\mu(n)
 d_\triangle(m,n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{13}
\]

Expand

\[
d_\triangle(m,n)
=
\sum_p \mathbf 1_{p\mid m,\ p\nmid n}
+
\sum_p \mathbf 1_{p\mid n,\ p\nmid m}.
\tag{14}
\]

In the first orientation write `m=pa`. Nonzero Möbius weight forces `p\nmid a` and `p\nmid n`, while

\[
\mu(pa)\mu(n)=-\nu_p(a)\nu_p(n).
\]

The cutoff is `a<=N/p`, `n<=N`, and

\[
z\!\left(\frac{N^2}{pan}\right)
=
z\!\left(\frac{(N/p)N}{an}\right).
\]

Thus the first orientation contributes `-Q_p(N/p,N)`. Symmetry gives the same contribution from the second orientation, proving `(6)`.

This is the exact point at which the construction escapes `MC-090`. A gcd mask can only ask which primes divide **both** coordinates. Equation `(14)` responds to primes dividing **exactly one** coordinate, so its divisor-basis top-mode theorem does not apply.

## 3. Rectangular Huxley--Watt control under a prior Mertens exponent

For real `X,Y>=1`, define the ordinary rectangular Möbius block

\[
Q(X,Y)
:=
\sum_{a\le X}\sum_{b\le Y}
\mu(a)\mu(b)
 z\!\left(\frac{XY}{ab}\right).
\tag{15}
\]

The arbitrary-range `d=2` Huxley--Watt identity (`MC-S24`) gives the exact floor part, and hence

\[
\boxed{
Q(X,Y)
=
M(X)+M(Y)-M(XY)
-XYH(X)H(Y)
+\frac12M(X)M(Y),
}
\tag{16}
\]

where

\[
H(x)=\sum_{n\le x}\frac{\mu(n)}n.
\]

For nonintegral cutoffs the inequalities are interpreted with floors. The numerator causes no ambiguity because `floor(XY/(ab))=floor(floor(XY)/(ab))`, and the Huxley--Watt admissibility `floor(XY)<(floor X+1)(floor Y+1)` is automatic.

Under `(7)`, convergence of `sum mu(n)/n` at `s=1` and partial summation give

\[
H(x)=O_\beta(x^{\beta-1}).
\tag{17}
\]

Every term in `(16)` is consequently

\[
O_\beta((XY)^\beta)
\]

for `X,Y>=1`, so

\[
\boxed{Q(X,Y)=O_\beta((XY)^\beta).}
\tag{18}
\]

The Euler-deletion identity already used in `MC-089`,

\[
\nu_p(n)
=
\sum_{\substack{i\ge0\\p^i\mid n}}
\mu(n/p^i),
\tag{19}
\]

gives, after substitution into `(5)`, the exact finite stack

\[
\boxed{
Q_p(X,Y)
=
\sum_{i,j\ge0}
Q(X/p^i,Y/p^j),
}
\tag{20}
\]

where terms with a cutoff below one vanish. Combining `(18)` and `(20)` yields

\[
|Q_p(X,Y)|
\ll_\beta
(XY)^\beta
\sum_{i,j\ge0}p^{-\beta(i+j)}
\ll_\beta (XY)^\beta,
\tag{21}
\]

uniformly for every prime `p`. Taking `X=N/p`, `Y=N` proves `(8)`.

## 4. The ell-1 barrier and the half-exponent ell-2 threshold

Insert `(8)` into `(6)`. The elementary estimate

\[
\sum_{p\le N}p^{-\beta}
\le
\sum_{n\le N}n^{-\beta}
=O_\beta(N^{1-\beta})
\]

proves `(9)`. Prime-number-theorem summation improves this by a logarithm but does not change the power. Since

\[
1+\beta-2\beta=1-\beta>0,
\]

the triangle inequality loses a fixed power relative to the old `N^{2 beta}` target.

For the square-sum benchmark and `beta>1/2`,

\[
\sum_{p>P}p^{-2\beta}
\le
\sum_{n>P}n^{-2\beta}
\ll_\beta P^{1-2\beta}.
\]

This proves `(10)` and `(11)`. The threshold `beta=1/2` is exact at the level of this power ledger: above it, the large-prime block scales are square summable with a power-decaying tail; at it, only non-power behavior remains.

If a future theorem supplied a source-compatible joint bound at essentially the square-sum scale for `p>N^delta`, the formal square-scale exponent of that tail would be

\[
2\beta-\delta(\beta-1/2),
\]

corresponding to the Mertens exponent

\[
\beta-\frac\delta2(\beta-1/2)
\tag{22}
\]

after the substitution `x=N^2`. Equation `(22)` is only a **conditional power ledger**, not a proved Mertens improvement: the full source identity still contains the small-prime part, and an endpoint derivative estimate by itself does not reconstruct `Q_1(N)`.

## 5. Prior art and novelty boundary

The arbitrary-cutoff Mertens identities and the rectangular coefficient-extraction mechanism are classical Huxley--Watt prior art (`MC-S24`). Product Hamming/noise kernels such as `(12)` are standard finite-product harmonic-analysis objects. The sieve parity phenomenon is also classical (`MC-S39`), and parity-sensitive sieve work demonstrates that extra bilinear or harmonic information can matter (`MC-S40`).

Within this line, `MC-034` already uses Walsh orthogonality of random prime-sign characters to obtain a critical RMS scale for the Huxley--Watt annulus. The present result is different: it differentiates the **deterministic all-minus Möbius endpoint itself** and shows that its prime-coordinate first variation is a sum of p-sifted rectangular source blocks.

A targeted literature search around Huxley--Watt arbitrary ranges, sieve parity, prime-factor Boolean/Hamming coordinates, and Möbius bilinear decompositions did not supply a basis for claiming a new external theorem. **No novelty claim is made.** The durable contribution is the exact line-specific reduction `(6)` together with the power ledger `(9)`--`(11)`, which tells the accepted annular clue what kind of estimate would actually be additional information.

## 6. Boundaries and decisive continuation

This finding does **not** prove cancellation among the prime blocks in `(6)`. In particular, `(10)` is not permission to replace an ell-1 sum of scalar quantities by its ell-2 norm. Any such step needs an independent orthogonality, large-sieve, bilinear, spectral, or other arithmetic theorem that applies to these exact p-sifted rectangular Huxley--Watt blocks.

It also does not prove that controlling `mathcal Q_N'(1)` controls `mathcal Q_N(1)`. A usable deformation argument must quantify the whole interpolation interval or provide a separate reconstruction identity. Fixed `t<1` may change the arithmetic cancellation class substantially, so analyticity in the finite parameter by itself is not a transfer theorem.

Finally, a large-prime estimate must be combined with a treatment of `p<=N^delta`. If that small-prime part is restored by termwise absolute estimates, it can erase the gain in `(11)`. The decisive next test is therefore two-sided:

1. derive a source-compatible joint inequality for the **large-prime sum** in `(6)` and determine whether it reaches a square-function scale rather than the triangle scale;
2. write the complete small-prime plus interpolation/reconstruction ledger and verify that the large-prime gain survives without importing an improved Mertens estimate.

Failure of either test kills this deformation as a contraction mechanism. Success would supply exactly the kind of joint signed information that remains outside the gcd-sieve obstruction of `MC-090`.

## Consequence for the research line

The common-prime route of `MC-088`--`MC-090` showed that a recursively cheap omitted block is possible but that gcd-only retention leaves the top mode untouched. `MC-091` supplies the first exact non-gcd prime-coordinate variation of that source carrier: the hard endpoint can be differentiated into lower-product-scale rectangular p-sifted blocks.

The price is now quantified. **Independent block estimates are power-expansive; a genuinely joint prime-index estimate has a half-exponent square-summability threshold and is the only surviving reason this deformation is interesting.** This narrows the accepted parity-sensitive annular clue from a generic request for a non-gcd coupling to one concrete falsifiable arithmetic target.