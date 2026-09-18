# FD-189 — Dyadic Fourier bands have a sharp square-root tail-recovery threshold

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** observation scheduling / Fourier-band identifiability / sharp square-root threshold
- **Depends on:** FD-117, FD-182

## Claim

`FD-182` rules out recovering the source-side prime-extension energy from the exact dyadic midpoint ladder alone on the unrestricted formal-source class. At the other extreme, `FD-117` shows that the full Farey discrepancy field at horizon `H` is invertibly equivalent to the quotient-Mertens staircase. There is a sharp intermediate threshold if one retains a growing **signed low-frequency Fourier band** at each dyadic horizon.

Let `a` be an arbitrary formal increment source and

\[
A(t):=\sum_{n\le t}a(n),
\qquad A(0):=0.
\tag{1}
\]

For integer `H>=1` define the Fourier-compatible arithmetic observable

\[
\mathcal F_H^a(k)
:=
\sum_{d\mid k} d\,A(\lfloor H/d\rfloor),
\qquad 1\le k\le H.
\tag{2}
\]

For the physical Möbius source, `FD-117` identifies

\[
\mathcal F_H^\mu(k)
=
1+2\pi i k\,\widehat D_H(k),
\tag{3}
\]

where `D_H` is the Farey discrepancy field. Thus (2) is exactly the source-side coordinate exposed by the signed Farey Fourier coefficient, not a new source observable.

Fix `0<alpha<=1` and, at every dyadic horizon `H=2^m`, retain all modes

\[
1\le k\le K_\alpha(H):=\lfloor H^\alpha\rfloor.
\tag{4}
\]

Then `alpha=1/2` is the exact threshold for tail recovery on the unrestricted formal-source class:

1. If `alpha>1/2`, every sufficiently large integer `n` occurs as

\[
n=\left\lfloor\frac{2^m}{k}\right\rfloor
\tag{5}
\]

for some `m` and some `1<=k<=2^{alpha m}`. Consequently the complete dyadic low-band history determines `A(n)` for every sufficiently large `n`, and hence determines the increment source outside a finite prefix. If that finite prefix is fixed independently, the source is recovered exactly.

2. If `alpha<=1/2`, infinitely many cumulative coordinates are never sampled. Explicitly,

\[
n_r:=2^r-1,\qquad r\ge2,
\tag{6}
\]

never equals `floor(2^m/k)` with `k<=2^{alpha m}`. Therefore, after any prescribed finite prefix, there are distinct formal sources with identical complete dyadic low-band data.

So the square-root band is genuinely critical: retaining all signed Fourier modes through `H^(1/2)` is still noninjective, while any fixed power `H^(1/2+epsilon)` is tail-injective.

This is an exact identifiability theorem, not a stability estimate and not a Franel--Landau/RH consequence. It applies first to the unrestricted formal-source relaxation. The explicit null perturbation below is **not** claimed to preserve squarefree support, Möbius signs, multiplicativity, or any other physical-source constraint.

## 1. The signed Fourier band is exactly a truncated quotient-source staircase

Write

\[
G_H(k):=k\,A(\lfloor H/k\rfloor).
\tag{7}
\]

Then (2) is simply the divisor zeta transform

\[
\mathcal F_H^a(k)=\sum_{d\mid k}G_H(d).
\tag{8}
\]

Möbius inversion on divisors gives, for every `k`,

\[
\boxed{
A(\lfloor H/k\rfloor)
=
\frac1k
\sum_{d\mid k}
\mu(k/d)\,\mathcal F_H^a(d).
}
\tag{9}
\]

Therefore knowing all signed modes `F_H^a(d)` for `d<=K` is exactly equivalent to knowing the quotient samples

\[
\left\{
A(\lfloor H/k\rfloor):1\le k\le K
\right\}.
\tag{10}
\]

There is no hidden gain in passing to Fourier coordinates. The threshold problem is purely the coverage problem for the dyadic quotient map `(H,k) -> floor(H/k)` under the budget `k<=H^alpha`.

This also explains why scalar Fourier energy is a different object. Squaring and summing coefficients discards their identities and phases; (9) requires the signed coefficient vector itself.

## 2. Every large coordinate is hit above the square-root threshold

Fix an integer `n>=1` and choose `H` to be the least power of two satisfying

\[
H\ge n(n+1).
\tag{11}
\]

Then

\[
n(n+1)\le H<2n(n+1).
\tag{12}
\]

The condition `floor(H/k)=n` is equivalent to

\[
\frac{H}{n+1}<k\le\frac Hn.
\tag{13}
\]

The interval in (13) has length

\[
\frac Hn-\frac{H}{n+1}
=
\frac{H}{n(n+1)}
\ge1,
\tag{14}
\]

so it contains an integer `k`. Any such integer satisfies

\[
k\le\frac Hn<2(n+1).
\tag{15}
\]

If `alpha>1/2`, then

\[
\frac{[n(n+1)]^\alpha}{2(n+1)}
\sim
\frac12 n^{2\alpha-1}
\longrightarrow\infty.
\tag{16}
\]

Hence, for every sufficiently large `n`,

\[
2(n+1)\le H^\alpha.
\tag{17}
\]

Combining (13)--(17) produces an admissible `k<=H^alpha`, proving (5). Equation (9) then reconstructs `A(n)` from the retained Fourier band at that dyadic horizon.

Thus if two formal sources have identical dyadic low-band histories with `alpha>1/2`, their cumulative functions agree at every sufficiently large integer. Their increments consequently agree outside a finite prefix. If the prefix is fixed as part of the admissible class, the two sources coincide everywhere.

The proof is constructive at finite scale: recovering a coordinate `n` never requires a horizon larger than

\[
H<2n(n+1)=O(n^2).
\tag{18}
\]

## 3. Mersenne coordinates are exact holes at and below square root

Now set

\[
n_r=2^r-1,
\qquad r\ge2,
\tag{19}
\]

and let `H=2^m`. We show that `n_r` is never of the form `floor(H/k)` with `k<=sqrt(H)`.

If `m<r`, then `H<n_r`, so the quotient cannot equal `n_r`.

Suppose next that

\[
r\le m\le2r-1.
\tag{20}
\]

Put `L=2^(m-r)`. The interval of possible `k` is

\[
\left(
\frac{H}{n_r+1},
\frac{H}{n_r}
\right]
=
\left(
L,
L+\frac{L}{2^r-1}
\right].
\tag{21}
\]

Here `L` is an integer and `L<=2^(r-1)`, so

\[
0<\frac{L}{2^r-1}<1.
\tag{22}
\]

The interval (21) therefore contains no integer: its integer left endpoint is excluded and its width is strictly less than one.

Finally suppose `m>=2r`. Any `k` with `floor(H/k)=n_r` would have to satisfy

\[
k>
\frac{H}{n_r+1}
=
2^{m-r}
\ge
2^{m/2}
=
\sqrt H.
\tag{23}
\]

So no such `k` is admitted by the square-root cutoff. If `alpha<=1/2`, then `H^alpha<=sqrt(H)`, and the same obstruction applies. This proves that every `n_r` in (19) is an unsampled cumulative coordinate.

The endpoint `alpha=1/2` is therefore genuinely on the noninjective side; there is no logarithmic ambiguity hidden in the proof.

## 4. An explicit formal null direction after any finite prefix

Let `X` be any prescribed finite prefix. Choose `r` so large that

\[
n_r=2^r-1>X.
\tag{24}
\]

Given any formal source `a`, define a perturbed source `a_epsilon` by

\[
a_\varepsilon(n_r)=a(n_r)+\varepsilon,
\qquad
 a_\varepsilon(n_r+1)=a(n_r+1)-\varepsilon,
\tag{25}
\]

with all other increments unchanged. The cumulative perturbation is then

\[
A_\varepsilon(t)-A(t)
=
\begin{cases}
\varepsilon,&t=n_r,\\
0,&t\ne n_r.
\end{cases}
\tag{26}
\]

Because `n_r` never appears among the sampled quotient coordinates for `alpha<=1/2`, equations (9)--(10) show that

\[
\mathcal F_H^{a_\varepsilon}(k)
=
\mathcal F_H^a(k)
\tag{27}
\]

for every dyadic `H` and every retained `k<=H^alpha`, despite `a_epsilon!=a`. The perturbation also leaves every increment through `X` unchanged.

This is a formal-source null direction only. In particular, `n_r+1=2^r` is nonsquarefree, while `n_r` need not be squarefree. The construction therefore does **not** show noninjectivity inside the physical squarefree Möbius fibre. Its role is to identify the information threshold before arithmetic admissibility is imposed.

## 5. Finite-scale information cost

For `alpha>1/2`, coordinates through scale `X` are recovered, apart from a fixed small prefix, using dyadic horizons only up to `O(X^2)`. The total number of retained signed coefficients over all such horizons is bounded by a geometric series:

\[
\sum_{2^m\ll X^2}(2^m)^\alpha
=
O_\alpha(X^{2\alpha}).
\tag{28}
\]

Thus choosing `alpha=1/2+epsilon` gives an exact formal tail-recovery schedule with

\[
O_\varepsilon(X^{1+2\varepsilon})
\tag{29}
\]

signed Fourier values through coordinate scale `X`, at the cost of allowing the largest physical horizon to grow quadratically in `X`.

This count is a sampling upper bound, not an optimality theorem for total data volume. The sharp statement proved here concerns the **power-law frequency cutoff at every dyadic horizon**, not arbitrary nonuniform mode selection.

## Representation audit

The observable has not been strengthened by an arithmetic inversion hidden in the proof. For each fixed horizon, `FD-117` already proves that the physical signed Fourier coefficient is the divisor zeta transform (8) of the quotient-Mertens samples, and (9) is its exact inverse. Retaining a low Fourier band is therefore equivalent to retaining the corresponding low-`k` quotient-source coordinates; the only new ingredient is their scheduling over dyadic horizons.

The threshold is consequently representation-stable within this signed-coefficient model. It would be misleading, however, to transfer the result to a scalar norm or band energy: those observables discard information before (9) can be applied. Nor does exact formal-source recovery imply a Franel--Landau discrepancy bound or RH. It gives source identifiability, not the analytic cancellation estimate required by the RH-equivalent norm statements.

## Prior-art and novelty boundary

The fixed-horizon quotient set `{floor(H/k)}` is classical. Randell Heyman, *Cardinality of a Floor Function Set*, Integers **19** (2019), A67, arXiv:`1905.00533`, studies the cardinal structure of such floor-function sets, and subsequent work studies primes inside related sets. Those results are useful prior-art boundaries but are not used in the proof above.

On the Farey side, `FD-117` supplies the exact signed Fourier/quotient-staircase equivalence. A targeted search did not surface a theorem identifying the sharp `alpha=1/2` threshold for **dyadic multihorizon low-frequency Farey data**, nor the explicit Mersenne null coordinates (19) as the matching obstruction. The proof here is elementary once `FD-117` is available, so no new external theorem is load-bearing and `SOURCES.md` needs no update.

No global novelty claim is made. The statement is intentionally scoped to the dyadic schedule, the initial frequency segment `1<=k<=H^alpha`, and unrestricted formal cumulative sources.

## Research consequence

This gives the first sharp observation-side power threshold between the midpoint no-go of `FD-182` and the full-field invertibility of `FD-117`. The amount of spatial Farey information matters qualitatively: a square-root signed band still leaves infinitely many exact formal null directions, whereas every fixed super-square-root band eventually exposes every cumulative source coordinate.

It also sharpens the interpretation of the accepted spectral-allocation clue. A cutoff on the order of `sqrt(H)` is exactly critical and incomplete even if one keeps **every signed Fourier coefficient**, which is strictly more information than a scalar band energy. A cutoff on the order of `H^(2/3)` lies above the exact-recovery threshold for signed coefficients. This does not resolve that clue, because its statistic is scalar spectral energy and therefore lacks the coefficient identities needed by (9).

The next useful question is now more precise. On the unrestricted formal class, super-square-root signed spatial data is already complete, so any genuinely sparser Farey bridge must exploit arithmetic admissibility rather than generic quotient coverage. On the physical squarefree/Möbius-adjacent classes, one should ask whether the square-root barrier moves, or whether a much thinner denominator/mediant statistic can control the source currencies `D_(a,q)` and `M_(a,q)` without reconstructing the whole source.
