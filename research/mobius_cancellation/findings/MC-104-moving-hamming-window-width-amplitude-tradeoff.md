# MC-104 — Moving Hamming windows obey a width–amplitude tradeoff

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation from `MC-092`--`MC-103` be

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad 0\le t\le1,
\tag{1}
\]

and let

\[
D_N:=\deg \mathcal Q_N.
\tag{2}
\]

`MC-100` proves that at the explicit source point

\[
s_N=\frac{\tau}{(\log N)^2},
\qquad \tau=\frac{c_2}{2}>0,
\tag{3}
\]

one has, for all sufficiently large `N`,

\[
|\mathcal Q_N(s_N)|
\ge c_*\frac{N^2}{(\log N)^6}
\tag{4}
\]

with an absolute `c_*>0`. `MC-103` shows that extrapolating from a polynomially shrinking low-bias window to the hard endpoint is superpolynomially ill-conditioned on the full degree-bounded class. A different escape remained open: perhaps the useful information lives on a **moving interval** that avoids the low-bias spike and follows a favorable region of the deformation as `N` changes.

There is an exact width-only obstruction to that escape. For every nondegenerate interval

\[
I_N=[a_N,b_N]\subset[0,1],
\qquad
\ell_N:=b_N-a_N>0,
\tag{5}
\]

one has

\[
\boxed{
\sup_{t\in I_N}|\mathcal Q_N(t)|
\ge
\frac{c_*N^2}{(\log N)^6\,
T_{D_N}(1+2/\ell_N)}
}
\tag{6}
\]

for all sufficiently large `N`, where `T_d` is the Chebyshev polynomial of the first kind. The estimate is independent of the location of `I_N`; only its width enters.

The source degree has the sharper classical ceiling

\[
\boxed{
D_N\le
(2+o(1))\frac{\log N}{\log\log N}.
}
\tag{7}
\]

Consequently:

1. if

\[
\log(1/\ell_N)=o(\log\log N),
\tag{8}
\]

then

\[
\boxed{
\sup_{t\in I_N}|\mathcal Q_N(t)|
\ge N^{2-o(1)};
}
\tag{9}
\]

2. more quantitatively, if for a fixed `A>=0`

\[
\ell_N=(\log N)^{-A+o(1)},
\tag{10}
\]

then

\[
\boxed{
\sup_{t\in I_N}|\mathcal Q_N(t)|
\ge N^{2-2A-o(1)};
}
\tag{11}
\]

3. therefore a moving-window strategy that hopes for a uniform critical source bound

\[
\sup_{t\in I_N}|\mathcal Q_N(t)|\le N^{1+o(1)}
\tag{12}
\]

must at least satisfy the necessary width condition

\[
\boxed{
\ell_N\le(\log N)^{-1/2+o(1)}.
}
\tag{13}
\]

In particular, moving the interval does not help while its width shrinks more slowly than every fixed power of `log N`, and even a logarithmic window of width `(log N)^{-A}` with `A<1/2` is still forced to contain a supercritical polynomial amplitude.

This does **not** show that windows satisfying `(13)` are useful. It only closes the broad moving-window escape in the regime where low degree makes the known source spike visible from the window with too little amplification. The narrower regimes remain subject to the reconstruction obstruction of `MC-103` when the window lies near zero, and a useful route elsewhere must still supply a source-specific signed relation rather than merely choose a favorable moving location.

No improved estimate for `M(x)` is claimed.

## 1. The source degree has maximal-order constant two

The product-fiber form from `MC-092` is

\[
\mathcal Q_N(t)
=\sum_{\substack{a\le N^2\\a\ \mathrm{squarefree}}}
W_N(a)(-t)^{\omega(a)}.
\tag{14}
\]

Therefore

\[
D_N
\le
K(N^2),
\qquad
K(X):=\max_{n\le X}\omega(n).
\tag{15}
\]

If `\omega(n)=k`, then `n` is at least the product of the first `k` primes,

\[
n\ge p_k\#:=\prod_{j\le k}p_j.
\tag{16}
\]

The prime number theorem gives the classical primorial asymptotic

\[
\log(p_k\#)
=\vartheta(p_k)
=(1+o(1))p_k
=(1+o(1))k\log k.
\tag{17}
\]

If `n<=N^2`, equations `(16)`--`(17)` imply

\[
k\log k\le(2+o(1))\log N,
\]

and inversion yields

\[
k\le(2+o(1))\frac{\log N}{\log\log N}.
\tag{18}
\]

Combining `(15)` and `(18)` proves `(7)`. Only an upper bound is needed: the actual degree of `\mathcal Q_N` could be smaller if some top source shells vanish.

The constant `2` is simply the `N^2` product-fiber cutoff expressed through the classical maximal order of the number of distinct prime factors. No arithmetic cancellation input enters this step.

## 2. Any interval sees the source spike through one-interval Chebyshev extrapolation

Fix `N` and write

\[
I_N=[a,b],\qquad \ell=b-a.
\]

Map the interval affinely to `[-1,1]` by

\[
x(t)=\frac{2t-a-b}{\ell}.
\tag{19}
\]

If the spike point `s_N` lies inside `I_N`, then `(6)` is immediate because the denominator on its right is at least one. Suppose instead that `s_N` lies outside. Its normalized distance satisfies

\[
|x(s_N)|
=1+\frac{2\,\operatorname{dist}(s_N,I_N)}{\ell}
\le1+\frac2\ell,
\tag{20}
\]

because both `s_N` and `I_N` lie in `[0,1]`.

For a real polynomial `P` of degree at most `D`, the one-interval Chebyshev extremal inequality gives, for `|x|>=1`,

\[
|P(x)|
\le
T_D(|x|)\|P\|_{[-1,1]}.
\tag{21}
\]

Apply `(21)` to `\mathcal Q_N` after the affine change `(19)`. Since `T_D(x)` is increasing for `x>=1`, `(20)` gives

\[
|\mathcal Q_N(s_N)|
\le
T_{D_N}(1+2/\ell_N)
\sup_{t\in I_N}|\mathcal Q_N(t)|.
\tag{22}
\]

Insert the source lower bound `(4)` to obtain `(6)`.

The important point is that `(22)` is a **location-free** transfer. An interval cannot evade the known spike merely by drifting with `N`; avoiding it geometrically makes the spike an exterior evaluation problem, and the only generic price is controlled by the interval width and the source degree.

## 3. Slowly shrinking windows still have almost-square amplitude

For `x>=1`,

\[
T_D(x)=\cosh(D\operatorname{arcosh}x)
\le
\exp(D\operatorname{arcosh}x)
\le(2x)^D.
\tag{23}
\]

Since `0<\ell_N<=1`,

\[
1+\frac2{\ell_N}\le\frac3{\ell_N},
\]

so `(23)` gives

\[
T_{D_N}(1+2/\ell_N)
\le
\left(\frac6{\ell_N}\right)^{D_N}.
\tag{24}
\]

Using `(7)`,

\[
\log T_{D_N}(1+2/\ell_N)
\le
(2+o(1))\frac{\log N}{\log\log N}
\left(\log\frac1{\ell_N}+O(1)\right).
\tag{25}
\]

Under `(8)`, the right side is `o(log N)`, hence

\[
T_{D_N}(1+2/\ell_N)=N^{o(1)}.
\tag{26}
\]

Equation `(6)` then gives `(9)`, since the fixed factor `(log N)^{-6}` is also `N^{-o(1)}`.

This extends `MC-100` from fixed intervals to every moving interval whose reciprocal width is only `(log N)^{o(1)}`. The location may drift all the way toward the hard endpoint; the conclusion is unchanged at polynomial scale.

## 4. Logarithmic windows have an explicit exponent ledger

Suppose `(10)` holds. Then

\[
\log\frac1{\ell_N}
=(A+o(1))\log\log N.
\tag{27}
\]

Substitute `(27)` into `(25)`:

\[
T_{D_N}(1+2/\ell_N)
\le
N^{2A+o(1)}.
\tag{28}
\]

Combining `(28)` with `(6)` proves `(11)`.

The threshold for a **possible** critical source amplitude follows immediately. If `(12)` held while

\[
\log\frac1{\ell_N}
\le\left(\frac12-\delta\right)\log\log N
\tag{29}
\]

along some infinite subsequence for a fixed `delta>0`, then `(25)` would give

\[
T_{D_N}(1+2/\ell_N)
\le N^{1-2\delta+o(1)},
\]

and `(6)` would force

\[
\sup_{I_N}|\mathcal Q_N|
\ge N^{1+2\delta-o(1)},
\]

contradicting `(12)`. Hence `(12)` requires

\[
\log(1/\ell_N)
\ge\left(\frac12-o(1)\right)\log\log N,
\]

which is equivalent to `(13)`.

This is only a necessary width condition. At the exact logarithmic threshold the estimate loses the whole one-power margin between the source spike and the desired critical scale, so it supplies no positive candidate theorem there.

## 5. Prior art and novelty boundary

The extrapolation mechanism is classical. B. Eichinger and P. Yuditskii, *Pointwise Remez inequality*, Constructive Approximation 54 (2021), 529--554, DOI `10.1007/s00365-021-09562-1`, describe the pointwise Remez problem and record that the one-interval extremal solution is the rescaled Chebyshev polynomial. A. A. Trembach, *Optimal extrapolation of polynomials given with error*, Trudy Instituta Matematiki i Mekhaniki UrO RAN 30 (2024), no. 4, 265--275, DOI `10.21538/0134-4889-2024-30-4-265-275`, treats the same exterior-evaluation phenomenon as an optimal-recovery problem and gives an exact interval-to-real-line solution. These are the same approximation-theoretic boundaries already audited in `MC-103`.

The maximal-order estimate for `omega(n)` used in `(7)` is the elementary primorial consequence of the prime number theorem; no new theorem about prime factors is asserted.

A targeted literature audit around pointwise Remez inequalities, moving/shrinking polynomial observation intervals, Möbius/Mertens Chebyshev interpolation, and the Huxley--Watt Möbius identities found no basis for claiming a new approximation theorem or a known arithmetic theorem equivalent to `(6)`. **No novelty claim is made.** The line-specific contribution is the combination of the classical interval extrapolation constant with the independently derived Hamming source spike and the `N^2` product-fiber degree ceiling, producing the explicit window-width ledger `(6)`--`(13)`.

## 6. Boundaries and falsification tests

- The theorem is an **amplitude obstruction**, not a cancellation theorem. A large value somewhere in `I_N` does not prevent a useful signed integral, derivative identity, oscillatory average, or recurrence from being small.
- The bound uses only the interval width and therefore deliberately discards location information. A source-specific mechanism may exploit a special moving location even though the uniform amplitude on the surrounding interval is large.
- The constant `2` in `(7)` comes from an upper bound on the available source degree. If the actual degree is materially smaller, `(6)` only strengthens; if a candidate uses a different deformation with a larger degree, the ledger must be recomputed.
- The spike `(4)` is source-specific and exact at the stated evidence level, but the transfer from that spike to `I_N` is generic polynomial approximation. A route that proves a relation on a smaller arithmetic coefficient manifold can evade the generic extrapolation cost only by using information beyond interval amplitude.
- Equation `(13)` does not assert that a window of width `(log N)^(-1/2)` or smaller admits a critical-power bound. It identifies the first width scale not excluded by this particular spike-plus-degree argument.
- Polynomially shrinking windows lie far outside the useful range of `(11)`. When such a window is anchored near zero, `MC-103` already proves that exact degree-only recovery of the endpoint is superpolynomially ill-conditioned. Elsewhere they remain open only if a source-specific relation is supplied.
- No estimate for `\mathcal Q_N(1)`, `M(N)`, or `M(N^2)` follows, and no zero-free region or RH input enters the derivation.

A decisive escape is now narrower: exhibit a signed observable on a window at or below the width threshold `(13)` whose source-specific relation transfers to the endpoint or to the `MC-027` scale iteration with a strict net power gain, and prove that its conditioning is controlled by arithmetic structure rather than by generic degree interpolation.

## Consequence for the research line

`MC-100` killed fixed positive-length interior windows by exhibiting a deterministic almost-square spike. `MC-101`--`MC-102` classified the low-bias amplitude transition down to the positive linear diagonal floor. `MC-103` killed generic endpoint recovery from polynomially shrinking low-bias values by the exact Chebyshev condition number.

`MC-104` closes the broad **moving-window-width** escape between those statements. Slowly shrinking windows cannot hide in a favorable part of the deformation: low source degree propagates the known spike into every interval with only the width-dependent Chebyshev cost. At logarithmic width `(log N)^{-A}`, the unavoidable amplitude exponent is at least `2-2A`; a critical-power uniform window is impossible unless the width has already shrunk to at most `(log N)^{-1/2+o(1)}`.

The surviving problem is therefore not to search for a wide moving interval with uniformly smaller values. It is to find a genuinely source-specific signed relation, non-point observable, or different coupling whose information is not summarized by the sup norm of a degree-bounded Hamming polynomial.