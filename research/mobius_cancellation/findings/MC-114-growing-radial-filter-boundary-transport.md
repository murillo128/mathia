# MC-114 — Logarithmic-range radial filters suppress the physical shells by transporting parity into the boundary

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the finite Hamming-shell polynomial used in `MC-093` and `MC-107`--`MC-113`:

\[
\mathcal Q_N(t)=\sum_{n=0}^{D_N}(-t)^n C_{n,N},
\qquad
D_N=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{1}
\]

Let

\[
A_N(z)=\sum_{j=0}^{r_N}a_{j,N}z^j
\tag{2}
\]

be an arbitrary real forward shell filter and extend the shell sequence by zero outside `0<=n<=D_N`. Define the full filtered sequence on the integer shell axis by

\[
T_{k,N}^{A}
:=
\sum_{j=0}^{r_N}a_{j,N}C_{k+j,N},
\qquad k\in\mathbb Z.
\tag{3}
\]

Then the exact parity transfer used in `MC-111`--`MC-113` is a Laurent-polynomial identity:

\[
\boxed{
\sum_{k\in\mathbb Z}(-1)^kT_{k,N}^{A}
=A_N(-1)\mathcal Q_N(1).
}
\tag{4}
\]

The important boundary fact is that `(4)` is generally **not** an identity on the physical shell range `0<=k<=D_N`. Writing

\[
A_{N,\le n}(-1)
:=
\sum_{j=0}^{\min(r_N,n)}a_{j,N}(-1)^j,
\tag{5}
\]

one has exactly

\[
\boxed{
\sum_{k=0}^{D_N}(-1)^kT_{k,N}^{A}
=
\sum_{n=0}^{D_N}(-1)^nC_{n,N}A_{N,\le n}(-1),
}
\tag{6}
\]

and therefore the negative-index boundary carries

\[
\boxed{
\sum_{k=-r_N}^{-1}(-1)^kT_{k,N}^{A}
=
\sum_{n=0}^{D_N}(-1)^nC_{n,N}
\bigl(A_N(-1)-A_{N,\le n}(-1)\bigr).
}
\tag{7}
\]

Consequently, after normalizing `A_N(-1)=1`, the physical-shell parity sum `(6)` reconstructs `mathcal Q_N(1)` for **every** finite shell vector `C_0,...,C_{D_N}` if and only if

\[
a_{0,N}=1,
\qquad
a_{j,N}=0\quad(1\le j\le D_N),
\tag{8}
\]

with any coefficients of degree `j>D_N` necessarily invisible on the physical outputs and having zero total alternating contribution. Thus every universal parity-preserving forward filter that uses only the physical shell outputs is trivial there:

\[
T_{k,N}^{A}=C_{k,N}
\qquad(0\le k\le D_N).
\tag{9}
\]

Any nontrivial forward filter can preserve the parity endpoint only by keeping the negative-index boundary term `(7)` or by proving a source-specific signed relation that replaces it. This becomes decisive for the growing-filter escape left by `MC-113`. That finding proves that a parity-normalized polynomial needs degree `Theta(log N)` to suppress the whole fixed proportional ratio band by a fixed power. But `(1)` gives

\[
D_N=o(\log N).
\tag{10}
\]

Hence every such logarithmic-range design eventually extends far beyond the entire physical radial dimension. A naive growing-shift Sathe--Selberg transfer law cannot bridge that gap: the source sequence is already identically zero before the required filter range ends. The missing issue is not merely a harder uniform asymptotic; it is an exact finite-support/boundary transition.

There is also no universal coefficient-conditioning obstruction that rescues this branch. The explicit binomial high-pass family

\[
A_r(z)=\left(\frac{1-z}{2}\right)^r
=2^{-r}\sum_{j=0}^{r}(-1)^j\binom rj z^j
\tag{11}
\]

satisfies simultaneously

\[
A_r(-1)=1,
\qquad
\sum_{j=0}^{r}|a_j|=1,
\qquad
\sup_{x\in[1/2,2]}|A_r(x)|\le2^{-r}.
\tag{12}
\]

Thus `r=c log N` already gives ideal-band attenuation

\[
\sup_{x\in[1/2,2]}|A_r(x)|
\le N^{-c\log 2+o(1)}
\tag{13}
\]

with perfectly bounded coefficient `ell^1` norm. Yet when `D_N=o(r)`, the total coefficient mass that can touch any physical shell is only

\[
\Lambda_{r,D_N}
:=2^{-r}\sum_{j=0}^{D_N}\binom rj
=\exp(-r\log2+o(r)).
\tag{14}
\]

Therefore, for **every** finite shell vector, arithmetic or not,

\[
\boxed{
\sup_{0\le k\le D_N}|T_{k,N}^{A_r}|
\le
\Lambda_{r,D_N}
\sum_{n=0}^{D_N}|C_{n,N}|.
}
\tag{15}
\]

So a logarithmic-range binomial filter can make every physical output polynomially tiny relative to the total shell mass without using any Möbius cancellation at all. The effect is a universal finite-support artifact: most of the filter lives beyond the radial support, and exact parity is transported into the negative-index boundary.

The extreme monomial control makes this explicit. If `r>D_N` and

\[
A_r(z)=(-1)^r z^r,
\tag{16}
\]

then `A_r(-1)=1` but

\[
T_{k,N}^{A_r}=0
\qquad(0\le k\le D_N),
\tag{17}
\]

while

\[
T_{n-r,N}^{A_r}=(-1)^rC_{n,N}
\qquad(0\le n\le D_N).
\tag{18}
\]

The entire parity endpoint has merely been translated into negative indices. Thus **small filtered coefficients on the physical Hamming shells are not evidence of arithmetic cancellation once the filter range is allowed to outrun the source degree**.

No estimate for `M(x)` is improved here. The result closes physical-shell attenuation itself as evidence for the growing one-sided radial filter route. A surviving method must control the signed boundary/source relation, use a source-justified two-sided or nonlocal reconstruction, or retain finer non-radial information.

## 1. Laurent multiplication exposes the missing boundary

Define the ordinary source polynomial

\[
C_N(z):=\sum_{n=0}^{D_N}C_{n,N}z^n.
\tag{19}
\]

From `(3)`, changing variables `n=k+j` gives

\[
\begin{aligned}
\sum_{k\in\mathbb Z}T_{k,N}^{A}z^k
&=
\sum_{j=0}^{r_N}a_{j,N}
\sum_{k\in\mathbb Z}C_{k+j,N}z^k\\
&=
\sum_{j=0}^{r_N}a_{j,N}z^{-j}C_N(z)\\
&=
A_N(z^{-1})C_N(z).
\end{aligned}
\tag{20}
\]

At `z=-1`, equation `(20)` is exactly `(4)` because

\[
C_N(-1)=\mathcal Q_N(1).
\tag{21}
\]

The Laurent support of `(20)` is `[-r_N,D_N]`. The negative powers are not cosmetic bookkeeping: they are exactly the boundary outputs generated when a forward shift reaches past shell zero.

Restricting `(3)` to `k>=0` and exchanging `k,j` instead gives

\[
\begin{aligned}
\sum_{k=0}^{D_N}(-1)^kT_{k,N}^{A}
&=
\sum_{k=0}^{D_N}(-1)^k
\sum_{j=0}^{r_N}a_{j,N}C_{k+j,N}\\
&=
\sum_{n=0}^{D_N}C_{n,N}
\sum_{j=0}^{\min(r_N,n)}a_{j,N}(-1)^{n-j}\\
&=
\sum_{n=0}^{D_N}(-1)^nC_{n,N}A_{N,\le n}(-1),
\end{aligned}
\tag{22}
\]

which proves `(6)`. Subtracting `(22)` from the full identity `(4)` proves `(7)`.

## 2. Universal interior parity preservation forces the identity filter

Suppose

\[
\sum_{k=0}^{D_N}(-1)^kT_{k,N}^{A}
=A_N(-1)\sum_{n=0}^{D_N}(-1)^nC_{n,N}
\tag{23}
\]

for every real shell vector `C_0,...,C_{D_N}`. Comparing the coefficient of each independent `C_n` in `(6)` yields

\[
A_{N,\le n}(-1)=A_N(-1)
\qquad(0\le n\le D_N).
\tag{24}
\]

At `n=0`, `(24)` says

\[
a_{0,N}=A_N(-1).
\tag{25}
\]

Subtracting the relation at `n-1` from that at `n` then gives successively

\[
(-1)^n a_{n,N}=0
\qquad(1\le n\le\min(r_N,D_N)).
\tag{26}
\]

Therefore all coefficients that can act nontrivially on physical shells vanish. If `r_N>D_N`, equation `(25)` together with the definition of `A_N(-1)` also forces

\[
\sum_{j>D_N}a_{j,N}(-1)^j=0,
\tag{27}
\]

but those high-degree coefficients never appear in any output with `k>=0`. This proves `(8)`--`(9)`.

The quantifier is important. A special arithmetic shell vector could satisfy an accidental cancellation in `(7)` for a nontrivial filter. But establishing that cancellation is then a **source-specific signed theorem**, not an automatic consequence of transfer-polynomial design. The universal algebraic carrier has been classified.

## 3. The filter range required by MC-113 exceeds the source dimension

`MC-093` proves from the product-fiber source itself that

\[
D_N
=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{28}
\]

The proof is elementary: if a square-free product `a<=N^2` has `d` distinct prime factors, then `a` is at least the product of the first `d` primes, hence at least `d!`; Stirling gives `(28)`.

By contrast, `MC-113` solves the ideal transfer-polynomial minimax problem on the fixed proportional ratio band `[1/2,2]`. A parity-normalized polynomial satisfying

\[
\sup_{x\in[1/2,2]}|A_N(x)|\le N^{-\delta}
\qquad(\delta>0)
\tag{29}
\]

must have

\[
r_N\ge
\frac{\delta}{\log(3+\sqrt8)}\log N+O(1).
\tag{30}
\]

Combining `(28)` and `(30)` gives

\[
\frac{r_N}{D_N}\to\infty
\tag{31}
\]

for every fixed `delta>0`. Thus the filter range demanded by fixed-power uniform attenuation is parametrically longer than the whole radial source.

This changes the interpretation of the open proof obligation after `MC-113`. One cannot seek a source asymptotic

\[
C_{k+j,N}/C_{k,N}\approx \beta^{-j}
\]

uniformly for all `j<=r_N` on that logarithmic range: for central or proportional `k=O(log log N)`, the numerator is exactly zero once `k+j>D_N`, while `beta^{-j}` is not. Any viable growing-filter argument must therefore leave the ideal infinite-geometric transfer picture before it reaches the degree needed for fixed-power attenuation and analyze the finite-support boundary exactly.

## 4. Stable binomial filtering shows conditioning is not the unavoidable obstruction

For `(11)`, the coefficient `ell^1` norm is exactly

\[
2^{-r}\sum_{j=0}^{r}\binom rj=1.
\tag{32}
\]

On `[1/2,2]`,

\[
|1-x|\le1,
\]

so `(12)` follows immediately. This family is not the Chebyshev minimizer from `MC-113`; it spends a larger constant multiple of `log N` for the same target attenuation. But it proves that exponential transfer attenuation does **not** intrinsically require an exponentially ill-conditioned coefficient vector.

Now assume `D=D_N=o(r)` and `D<=r/2`. The standard binomial bound

\[
\sum_{j=0}^{D}\binom rj
\le
(D+1)\left(\frac{er}{D}\right)^D
\tag{33}
\]

gives

\[
\log\Lambda_{r,D}
\le
-r\log2
+O\!\left(D\log\frac{er}{D}\right).
\tag{34}
\]

For `r=c log N` and `(28)`,

\[
D\log\frac{er}{D}
=O\!\left(
\frac{\log N\,\log\log\log N}{\log\log N}
\right)
=o(\log N),
\tag{35}
\]

which proves `(14)`.

Finally, every `k>=0` sees only coefficients with `j<=D-k`, so

\[
\begin{aligned}
|T_{k,N}^{A_r}|
&\le
\sum_{j=0}^{D-k}|a_j|\,|C_{k+j,N}|\\
&\le
\left(\sum_{j=0}^{D}|a_j|\right)
\sum_{n=0}^{D}|C_{n,N}|\\
&=
\Lambda_{r,D}\sum_{n=0}^{D}|C_{n,N}|.
\end{aligned}
\tag{36}
\]

This proves `(15)`. The estimate used only finite support, not the Sathe--Selberg profile, multiplicativity, prime locations, or any property of Möbius signs. It is therefore an adversarial matched-control explanation of the apparent gain.

## 5. Prior art and novelty boundary

The algebra in this finding is classical finite-sequence convolution. The Laurent identity `(20)` is the standard `z`-transform rule that convolution/shift filtering becomes multiplication of transforms; the binomial filter `(11)` is the ordinary normalized repeated finite-difference/high-pass filter. Boundary outputs for zero-extended finite sequences are standard finite-impulse-response behavior. No signal-processing, finite-difference, or approximation-theory novelty is claimed.

The Mathia-specific delta is the conjunction of three already-fixed properties of this source: the exact parity endpoint `z=-1`, the sublogarithmic source degree from `MC-093`, and the logarithmic ideal transfer range forced by `MC-113`. Together they show that the previously open `Theta(log N)` filter route crosses out of the physical Hamming shell space before reaching its required attenuation scale. Targeted prior-art searches found only the generic convolution/`z`-transform and FIR-filter mechanisms, not an arithmetic theorem that removes this source-specific boundary accounting.

As a classical orientation anchor, MIT OpenCourseWare's Signals and Systems materials treat discrete-time convolution and the `z`-transform as the polynomial/algebraic representation of finite sequences and systems; Oppenheim--Willsky, *Signals and Systems*, is the course's standard reference. The proof above is self-contained and does not depend on an external theorem beyond the elementary binomial estimate.

## 6. Boundaries and falsification tests

- The universal reconstruction theorem `(23)` concerns the **same parity functional on the physical filtered shells**. It does not rule out an arbitrary source-dependent inverse transform using other weights.
- The result applies to the one-sided forward filters `T_k=sum_j a_j C_{k+j}` studied in `MC-111`--`MC-113`. Two-sided, cyclic, reflected, or source-adapted transforms require their own boundary analysis.
- Negative shell indices are not claimed to be intrinsically meaningless. They are auxiliary outputs created by the filter. A method may use them, but then they must be included in the certificate and estimated rather than silently discarded.
- Equation `(15)` does not show that the Möbius endpoint is small. It shows the opposite methodological point: physical-shell attenuation can occur for every finite input sequence, including matched non-arithmetic controls, while the parity information survives in the boundary.
- The binomial family is a counterexample only to the idea that coefficient `ell^1` blow-up is an unavoidable obstruction. It is not claimed to be an optimal arithmetic filter.
- A source-specific theorem making the boundary term `(7)` independently small could still create a viable route. Such a theorem would have to preserve signed information and survive the line's circularity controls; it cannot be inferred from local transfer attenuation alone.
- No claim is made against non-radial product-fiber, bilinear, prime-factor, or other source-coupled representations.

A decisive falsifier of the universal interior classification would be a nontrivial coefficient `a_j` with `1<=j<=D_N` for which `(23)` holds for every shell vector. Coefficient comparison in `(24)`--`(26)` rules this out exactly.

## Consequence for the research line

`MC-113` left three apparent obligations for a growing local filter: growing-shift source asymptotics, coefficient conditioning, and signed reconstruction. The present result sharpens that list.

The first obligation cannot hold in the naive uniform form at the `Theta(log N)` range required for fixed-power attenuation because the entire shell source has degree only `o(log N)`. The second is not a universal blocker: stable `ell^1` binomial filters already achieve exponential ideal attenuation. The decisive unavoidable transition is the third: **once the filter outruns the source, apparent suppression of the physical shells can be pure transport into an auxiliary boundary layer**.

Accordingly, further work should not treat small positive-index filtered shell coefficients as progress by themselves. A surviving radial mechanism must exhibit a signed, source-specific reconstruction that controls the boundary without assuming the desired endpoint estimate, or else move to a genuinely nonlocal/non-radial information carrier.