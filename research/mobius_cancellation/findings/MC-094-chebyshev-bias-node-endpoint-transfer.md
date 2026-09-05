# MC-094 — Chebyshev bias nodes transfer fixed-gap power to the Möbius endpoint

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-093` proves that the Hamming deformation

\[
\mathcal Q_N(t)
=
\sum_{m,n\le N}
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad 0\le t\le1,
\tag{1}
\]

has degree only `O(log N/log log N)` and that a **uniform** bound on any fixed interval `0<=t<=1-eta` transfers to the Möbius endpoint `t=1` with only `N^{o(1)}` loss. Uniform continuum control is stronger than necessary. The same power transfer already follows from values at only a sublogarithmic number of deterministic interior bias parameters, and even from an averaged bound over those values.

Let

\[
K_N:=\max_{\substack{a\le N^2\\a\ \mathrm{squarefree}}}\omega(a).
\tag{2}
\]

Then `deg mathcal Q_N <= K_N` and

\[
K_N=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{3}
\]

Fix `0<eta<1`. For `j=0,...,K_N`, define the Chebyshev-root nodes

\[
x_{j,N}
:=\cos\!\left(\frac{(2j+1)\pi}{2(K_N+1)}\right)
\tag{4}
\]

and map them into the fixed-gap bias interval by

\[
t_{j,N}
:=\frac{1-\eta}{2}(1+x_{j,N})
\in(0,1-\eta).
\tag{5}
\]

Let `Lambda_K` denote the Lebesgue constant for interpolation at the `K+1` roots of the Chebyshev polynomial `T_{K+1}`. Classical Chebyshev interpolation theory gives

\[
\Lambda_K=O(\log(K+1)).
\tag{6}
\]

Put

\[
x_\eta:=\frac{1+\eta}{1-\eta}>1.
\tag{7}
\]

Then the exact interpolation plus pointwise Chebyshev extremal bound gives

\[
\boxed{
|\mathcal Q_N(1)|
\le
\Lambda_{K_N}
T_{K_N}(x_\eta)
\max_{0\le j\le K_N}|\mathcal Q_N(t_{j,N})|.
}
\tag{8}
\]

For every fixed `1<=p<infinity`, define the normalized sampled `ell_p` mean

\[
A_{p,N}(\eta)
:=
\left(
\frac1{K_N+1}
\sum_{j=0}^{K_N}|\mathcal Q_N(t_{j,N})|^p
\right)^{1/p}.
\tag{9}
\]

Since the largest sampled value is at most `(K_N+1)^(1/p) A_{p,N}(eta)`, equation `(8)` yields

\[
\boxed{
|\mathcal Q_N(1)|
\le
\Lambda_{K_N}T_{K_N}(x_\eta)
(K_N+1)^{1/p}A_{p,N}(\eta).
}
\tag{10}
\]

For fixed `eta` and fixed `p`, all factors outside `A_{p,N}` are subpolynomial:

\[
\Lambda_{K_N}T_{K_N}(x_\eta)(K_N+1)^{1/p}
=N^{o_\eta(1)}.
\tag{11}
\]

Therefore

\[
\boxed{
A_{p,N}(\eta)\le N^{\gamma+o(1)}
\quad\Longrightarrow\quad
\mathcal Q_N(1)\le N^{\gamma+o(1)}.
}
\tag{12}
\]

The converse holds at the level of polynomial powers: if along a subsequence

\[
|\mathcal Q_N(1)|\ge N^{\gamma-o(1)},
\tag{13}
\]

then for every fixed `p`

\[
A_{p,N}(\eta)\ge N^{\gamma-o(1)}.
\tag{14}
\]

Thus the Möbius endpoint cannot hide a different fixed power not only from a whole fixed-gap interval, as in `MC-093`, but also from a carefully chosen family of only

\[
K_N+1=O\!\left(\frac{\log N}{\log\log N}\right)
\tag{15}
\]

interior bias samples. A strict power gain averaged across these Chebyshev bias nodes already transfers to the endpoint with subpolynomial loss.

No estimate of the sampled values is proved here, and no improved Mertens bound is claimed.

## 1. Exact discrete interpolation

Define the affine pullback

\[
P_N(x)
:=
\mathcal Q_N\!\left(\frac{1-\eta}{2}(1+x)\right).
\tag{16}
\]

By `MC-092`--`MC-093`, the product-fiber representation of `mathcal Q_N` contains only powers `t^{omega(a)}` with square-free `a<=N^2`. Hence

\[
\deg P_N=\deg\mathcal Q_N\le K_N.
\tag{17}
\]

The `K_N+1` points in `(4)` are distinct. Lagrange interpolation at these nodes is therefore exact for `P_N`:

\[
P_N(x)
=
\sum_{j=0}^{K_N}P_N(x_{j,N})\ell_{j,N}(x),
\tag{18}
\]

where `ell_{j,N}` are the fundamental Lagrange polynomials. By definition of the Lebesgue constant,

\[
\sup_{-1\le x\le1}|P_N(x)|
\le
\Lambda_{K_N}
\max_j|P_N(x_{j,N})|.
\tag{19}
\]

For the roots of a Chebyshev polynomial the classical interpolation norm grows only logarithmically, giving `(6)`. This logarithmic stability is the reason for using Chebyshev nodes rather than an arbitrary equally spaced grid; a poorly conditioned interpolation family could spend a polynomial-scale margin.

The endpoint `t=1` corresponds under `(16)` to `x=x_eta` from `(7)`. The one-interval Chebyshev extremal theorem used in `MC-093` gives for every real polynomial of degree at most `K_N`

\[
|P_N(x_\eta)|
\le
T_{K_N}(x_\eta)
\sup_{[-1,1]}|P_N|.
\tag{20}
\]

Combining `(19)` and `(20)`, and noting that `P_N(x_{j,N})=mathcal Q_N(t_{j,N})`, proves `(8)`.

## 2. The interpolation cost is subpolynomial

For `x>1`,

\[
T_K(x)
\le
\left(x+\sqrt{x^2-1}\right)^K.
\tag{21}
\]

At `x=x_eta`, the base is the fixed constant

\[
x_\eta+\sqrt{x_\eta^2-1}
=
\frac{1+\sqrt\eta}{1-\sqrt\eta}
=:C_\eta>1.
\tag{22}
\]

Thus

\[
T_{K_N}(x_\eta)\le C_\eta^{K_N}.
\tag{23}
\]

The elementary primorial/factorial argument in `MC-093` gives `(3)`. Therefore

\[
\log T_{K_N}(x_\eta)
=O_\eta\!\left(\frac{\log N}{\log\log N}\right)
=o(\log N).
\tag{24}
\]

The factors `Lambda_{K_N}=O(log K_N)` and `(K_N+1)^(1/p)` contribute still less. This proves `(11)`.

The power transfer `(12)` is immediate. Rearranging `(10)` proves `(14)` from `(13)`. Hence the discrete sampled family and the endpoint have the same possible fixed polynomial exponent, up to `N^{o(1)}`.

## 3. Averaged bias control is enough

The `ell_p` form matters because the live route need not establish the same pointwise estimate independently at every bias. A theorem controlling the normalized mean `(9)` at a strict power scale is sufficient. In particular,

\[
A_{2,N}(\eta)
=
\left(
\frac1{K_N+1}
\sum_j|\mathcal Q_N(t_{j,N})|^2
\right)^{1/2}
\tag{25}
\]

may be a more natural target for a second-moment, large-sieve, orthogonality, or bilinear argument than the continuum supremum required in the initial reading of `MC-093`.

This observation does not manufacture such an argument. It only removes unnecessary reconstruction strength: one does **not** need to control every `t` in a continuum, and one does not even need a uniform pointwise bound across the selected nodes if an `ell_p` mean is available.

The sample locations move with `N` through `K_N`; this is essential. A fixed finite set of interior biases cannot determine polynomials of unbounded degree. Conversely, using `K_N+1` stable Chebyshev nodes is enough for exact reconstruction because the arithmetic source itself limits the degree to `K_N`.

## 4. Relation to biased random-multiplicative expectations

`MC-093` gives the exact representation

\[
\mathcal Q_N(t)
=
\mathbb E_t\!\left[
\sum_{m,n\le N}
 f_\xi(m)f_\xi(n)
 z\!\left(\frac{N^2}{mn}\right)
\right],
\tag{26}
\]

where the independent prime signs satisfy `E_t xi_p=-t`. Each node `t_{j,N}` is therefore one explicit biased random-multiplicative ensemble, while `t=1` is the deterministic all-minus Möbius point.

Equation `(10)` says that power control of the **expectations** at a sublogarithmic Chebyshev family of biases is enough to control the deterministic endpoint. It does not say that typical random realizations, their variances, or high-probability estimates control these expectations. The distinction from `MC-034` and `MC-092` remains strict: random multiplicative RMS is a matched-control calibration, not a transfer theorem for the all-minus point.

The potentially useful reformulation is narrower. If a source-natural arithmetic method can average the deterministic quantities `mathcal Q_N(t_{j,N})` over bias at a strict power scale, the endpoint reconstruction ledger is already closed up to `N^{o(1)}`. The method no longer needs a theorem uniform over the entire parameter interval.

## 5. Prior art and novelty boundary

The ingredients are classical approximation theory. R. Günttner, *Evaluation of Lebesgue Constants*, SIAM Journal on Numerical Analysis 17 (1980), no. 4, 512--520, DOI `10.1137/0717043`, studies the Chebyshev-node Lebesgue constants and their logarithmic asymptotics. B. Eichinger and P. Yuditskii, *Pointwise Remez inequality*, Constructive Approximation 54 (2021), 529--554, DOI `10.1007/s00365-021-09562-1`, records the one-interval Chebyshev extremal mechanism used for pointwise extrapolation outside a controlled interval.

The source-specific low-degree statement and Hamming deformation are already `MC-091`--`MC-093`. A targeted literature check around Chebyshev-node interpolation, Lebesgue constants, pointwise Remez inequalities, and Möbius/Hamming deformations supplied no basis for claiming a new approximation-theoretic theorem. **No novelty claim is made.** The durable line-specific contribution is the exact composition of these classical interpolation bounds with the arithmetic degree ceiling, reducing the live fixed-gap transfer obligation from continuum control to a sublogarithmic sampled family.

## 6. Boundaries and decisive continuation

The fixed-gap parameter `eta` remains essential. If `eta=eta_N` tends to zero, the Chebyshev extrapolation factor in `(22)` must be retained explicitly; it need not remain subpolynomial. This finding does not extend `(11)` automatically to a shrinking gap.

The node family is also structured. Arbitrary samples can have exponentially worse Lebesgue constants, so the statement does not justify replacing the Chebyshev grid by any convenient set of `K_N+1` biases without a conditioning audit.

A sampled second moment controls only the deformation block `mathcal Q_N`. As in `MC-093`, turning a bound for `mathcal Q_N(1)=Q_1(N)` into an improved global Mertens exponent still requires the complete Huxley--Watt source identity, subordinate coarse/residual terms, and an iterable strict gain satisfying the conditions of `MC-027`.

Most importantly, `(10)` is a reconstruction theorem, not the missing signed arithmetic estimate. The decisive next test is now weaker and more concrete than after `MC-093`: determine whether the degree-weighted product-fiber structure of `MC-092`, or another source-natural decomposition, yields a strict-power bound for an `ell_p` average of `mathcal Q_N(t_{j,N})` over the Chebyshev bias nodes, with all small-prime/coarse terms controlled independently of the desired Mertens improvement. An exact reduction of that sampled average back to an improved Mertens bound would close this escape route as tautological; a genuinely weaker arithmetic theorem with a strict exponent margin would survive the reconstruction step by `(10)`.

## Consequence for the research line

`MC-093` showed that a uniform fixed-gap interior estimate cannot be polynomially easier than the Möbius endpoint. `MC-094` sharpens the reconstruction boundary: **uniform continuum control is unnecessary**. Because the deformation has only `O(log N/log log N)` arithmetic degrees, values at a correspondingly small Chebyshev family determine the whole polynomial with subpolynomial power loss, and an averaged `ell_p` estimate across those samples already suffices.

This materially narrows the remaining search. The unresolved input may be sought as a finite bias-averaged signed estimate rather than a continuum-uniform theorem, while retaining the same endpoint power consequence and the same prohibition against importing the improved Mertens estimate itself.