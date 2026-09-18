# RE-200 — Vertical Euler phase supports linear stable dimension on one prime shell

**Status:** `EXACT-DERIVED + COMPLEX-EULER-SAMPLING + VERTICAL-FOURIER-FRAME + ORDINARY-PRIME-REALIZATION + LINEAR-EUCLIDEAN-DIMENSION + POSITIVE-REAL-CONTRAST + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-193, RE-199.

The positive-real Euler channel studied in `RE-190`--`RE-199` is Laplace-like in logarithmic prime location and can be extremely compressible. Complex vertical sampling has a different representation. On a fixed multiplicative prime shell, the first Euler harmonic has essentially constant amplitude while the imaginary part of `s` rotates each prime by the Fourier phase `exp(-it log q)`.

This difference already produces a sharp finite-dimensional statement with honest ordinary primes. Put

\[
V(Q):=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}}.
\]

Fix `W>0` and `Sigma<infinity`. Let `K=K(Q)->infinity` satisfy

\[
\log K=o(V(Q)).
\tag{1}
\]

Then, for all sufficiently large `Q`, there exist distinct ordinary primes

\[
q_0,\ldots,q_{K-1}\in[Q,e^WQ]
\tag{2}
\]

such that the following holds uniformly for every `0<=sigma<=Sigma`. Define

\[
t_k:=\frac{2\pi k}{W},
\qquad 0\le k<K,
\tag{3}
\]

and the exact Euler atom

\[
H_q(s):=\log(1-q^{-s})^{-1}.
\tag{4}
\]

Form the `K x K` response matrix

\[
M_{kj}
:=
Q^{1+\sigma}e^{it_k\log Q}
H_{q_j}(1+\sigma+it_k).
\tag{5}
\]

Then

\[
\boxed{
\frac1{\sqrt K}s_{\min}(M)
\ge
 e^{-(1+\Sigma)W}-o(1)
}
\tag{6}
\]

and

\[
\boxed{
\frac1{\sqrt K}s_{\max}(M)
\le
1+o(1).
}
\tag{7}
\]

In particular, after the common shell normalization `Q^(1+sigma)`, the exact complex Euler responses of `K` actual one-prime edits carry `K` uniformly conditioned Euclidean source directions. The largest sampled height is only

\[
t_{K-1}<\frac{2\pi K}{W}.
\tag{8}
\]

For `K asy c log Q`, which satisfies (1), a vertical segment of height `O(log Q)` therefore carries `Theta(log Q)` stable directions on one fixed shell.

This is qualitatively different from the positive-real channel. On the same shell and over a positive-real span `U=Theta(K)`, `RE-193` has `R=UW=Theta(K)`. Taking its uniform kernel tolerance `epsilon=K^-2` and sampling at any `K` real temperatures gives, after the same common shell normalization and `1/sqrt(K)` Euclidean normalization, a response matrix with an `o(1)` operator-norm approximation of rank

\[
O((\log K)^2).
\tag{9}
\]

By (6), every rank `<K` approximation to the vertical matrix has normalized Euclidean error at least `e^(-(1+Sigma)W)-o(1)`. Thus **the logarithmic positive-real compression does not extend to complex vertical phase**. The distinction is representation-level and survives the exact prime-power Euler factors.

## 1. Ordinary primes can realize an almost uniform log grid

Let

\[
x_j:=\frac{(j+1/2)W}{K},
\qquad
\eta:=K^{-3}.
\tag{10}
\]

The standard Korobov--Vinogradov PNT input already used throughout this line gives, for some absolute `a>0`,

\[
\vartheta(X)=X+O(Xe^{-aV(X)}).
\tag{11}
\]

Because `log K=o(V(Q))`, one has

\[
e^{-aV(Q)}=o(K^{-3}).
\tag{12}
\]

Uniformly for `X` in the fixed multiplicative shell `[Q,e^WQ]`, (11)--(12) imply

\[
\vartheta(Xe^\eta)-\vartheta(Xe^{-\eta})
=2\eta X(1+o(1))>0.
\tag{13}
\]

Hence each logarithmic bin centered at `Qe^(x_j)` with half-width `eta` contains an ordinary prime. The bins are disjoint because their centers are separated by `W/K` while `eta=o(1/K)`. Choose `q_j` in the `j`th bin and write

\[
y_j:=\log(q_j/Q)=x_j+\delta_j,
\qquad
|\delta_j|\le\eta.
\tag{14}
\]

No pseudo-primes, continuous source atoms or prime-density heuristic is being used here. The weak condition (1) is enough to quantize the desired log grid with actual primes.

## 2. The first Euler harmonic is a diagonally weighted DFT

Expand the exact atom at `s=1+sigma+it_k`:

\[
H_{q_j}(s)
=
q_j^{-s}
+
\sum_{m\ge2}\frac{q_j^{-ms}}m.
\tag{15}
\]

The normalized first harmonic is

\[
Q^{1+\sigma}e^{it_k\log Q}q_j^{-1-\sigma-it_k}
=
e^{-(1+\sigma)y_j}e^{-it_ky_j}.
\tag{16}
\]

If `delta_j` were zero, the resulting matrix would be

\[
A_{kj}
=
e^{-(1+\sigma)x_j}
 e^{-2\pi i k(j+1/2)/K}.
\tag{17}
\]

Thus

\[
A=F_KD_\sigma,
\tag{18}
\]

where `F_K` is an unnormalized discrete Fourier matrix, up to harmless row/column phases, and

\[
D_\sigma
=\operatorname{diag}(e^{-(1+\sigma)x_j}).
\tag{19}
\]

Since `F_K/sqrt(K)` is unitary,

\[
e^{-(1+\Sigma)W}\sqrt K
\le
s_{\min}(A)
\le
s_{\max}(A)
\le
\sqrt K.
\tag{20}
\]

The prime-placement error is tiny even at the largest sampled frequency. From (3), (14) and the derivative of `e^{-(1+sigma)y}e^{-ity}`,

\[
\max_{k,j}
\left|
 e^{-(1+\sigma)y_j}e^{-it_ky_j}
-
 e^{-(1+\sigma)x_j}e^{-it_kx_j}
\right|
\ll_{W,\Sigma}K\eta
\ll K^{-2}.
\tag{21}
\]

Hence the operator norm of the entire `K x K` placement perturbation is `O(K^-1)`.

## 3. Exact prime powers stay below the Fourier scale

The higher Euler harmonics in (15) are uniform in the imaginary part because only `Re(s)` enters their absolute value. After the normalization in (5),

\[
\left|
Q^{1+\sigma}
\sum_{m\ge2}\frac{q_j^{-m(1+\sigma+it_k)}}m
\right|
\ll
Q^{-(1+\sigma)}.
\tag{22}
\]

Therefore their full matrix has operator norm at most

\[
O(KQ^{-1-\sigma}).
\tag{23}
\]

Condition (1) implies `K=Q^o(1)`, so (23) is `o(1)`. Combining (21) and (23),

\[
\|M-A\|_{2\to2}=o(1).
\tag{24}
\]

Weyl's singular-value inequality with (20) now gives (6)--(7). The argument works equally for real source coefficient vectors: the Fourier matrix is unitary on the complexification, so restricting its domain to `R^K` does not weaken the lower norm bound.

## 4. Positive-real and vertical-complex sampling have different stable geometry

The same logarithmic source coordinate `x=log(q/Q)` produces two kernels. On the positive real ray, after the standard shell normalization, the first harmonic is

\[
e^{-ux}.
\tag{25}
\]

On a vertical line it is

\[
e^{-\sigma x}e^{-itx}.
\tag{26}
\]

The first is a positive Laplace kernel: large `ux` is damped and dyadic source scales become increasingly redundant. `RE-193` exploits exactly that geometry to obtain logarithmic stable rank. The second retains a unit-modulus oscillatory phase. Choosing equally spaced log locations and dual frequencies turns it into the DFT frame above.

For the quantitative comparison in (9), take `U=Theta(K)` in `RE-193`, so `R=Theta(K)`, and request kernel error `epsilon=K^-2`. Its rank bound is

\[
O(\log(1+K)\log K)=O((\log K)^2).
\tag{27}
\]

The prime-power floor `O(Q^-1)` is smaller because `K=Q^o(1)`. Restricting that finite-rank approximation to any `K` source atoms and any `K` real sample points gives entrywise error `O(K^-2+Q^-1)`. After dividing the sampled matrix by `sqrt(K)`, its Euclidean operator error is `o(1)`. The vertical matrix, by contrast, has all `K` normalized singular values bounded below by a fixed positive constant. This is an actual conditioning separation, not merely a statement that complex samples are numerous.

## Representation audit

The generic mechanism is Fourier, not specifically arithmetic. Dirichlet-polynomial values on vertical lines are trigonometric sums because `n^(-it)=exp(-it log n)`, and the classical time--bandwidth literature already explains why oscillatory Fourier windows can support a number of independent modes proportional to phase-space area. No novelty is claimed for DFT orthogonality or for the general Fourier time--bandwidth principle.

The source-specific step is that the exact ordinary-prime Euler atoms used by this line realize that Fourier frame without replacing the source. The KV PNT places actual primes at the required logarithmic nodes, the common normalization is the same for all columns on the fixed shell, and the exact `m>=2` prime-power harmonics are uniformly negligible. Thus the contrast with `RE-193` is a property of the actual Euler representation: positive-real damping is compressive, while vertical phase preserves log-location information.

This finding is deliberately about **representation capacity**, not Robin rigidity. A high-rank observation family need not detect the particular matched controls of `RE-188`--`RE-199`; those controls could conceivably be extended to cancel a selected vertical frame as well. Nor does (6) identify which complex samples are source-native in a future Robin argument. The theorem only rules out extending the positive-real low-rank heuristic to vertical complex sampling.

## Adversarial self-review

**Is the Fourier frame obtained only by pretending arbitrary real nodes are primes?** No. Equation (13) uses the same unconditional KV PNT source control already anchored in this line. The requested relative log-bin width `K^-3` dominates the PNT error under (1), so every node can be quantized by an ordinary prime, with disjoint bins.

**Can the phase error accumulate across `K` rows and columns?** The maximum pointwise phase/amplitude error is `O(K^-2)`, while a `K x K` matrix with that entrywise bound has operator norm at most `O(K^-1)`. This is negligible compared with the ideal smallest singular value `asymp sqrt(K)`.

**Do prime powers destroy orthogonality at heights `t=O(K)`?** No. Their modulus depends only on the real part of `s`. After the common shell normalization their entire matrix has norm `O(KQ^(-1-sigma))=o(1)`.

**Is the conditioning an artifact of column-by-column rescaling?** No. Every column is multiplied by the same `Q^(1+sigma)`. Fixed shell width makes `Q/q_j` stay between two constants, which is exactly why the diagonal factor in (19) has bounded condition number.

**Does the singular-value statement require nonphysical complex multiplicities?** No. The response values are complex, but the same lower norm estimate holds for real coefficient vectors. What is not proved is an integer-multiplicity matched-control theorem: stable linear separation of the atoms does not by itself show that a `{0,1,2}` repair satisfying all the existing moment constraints must leave a large vertical residual.

**Does this contradict `RE-199`?** No. `RE-199` concerns the complete **positive real** Euler ray and exploits Laplace damping after exact moment cancellation. `RE-200` shows that adding imaginary phase changes the representation enough that the same low-rank compression argument cannot be transferred. It does not evaluate the `RE-199` repair on the complex line.

## Prior-art audit

A targeted search was run for finite/truncated Fourier time--bandwidth dimension and for Dirichlet polynomials on vertical lines. Landau--Pollak's classical prolate-spheroidal work identifies the linear time--bandwidth dimension of essentially time- and band-limited Fourier data. Standard analytic-number-theory treatments write vertical Dirichlet polynomials as trigonometric polynomials in the phases `n^(it)` or `exp(it log n)`.

That generic Fourier geometry is prior art and is not claimed as new. The present proof is elementary DFT algebra plus the line's existing KV PNT. The Mathia-specific contribution is the exact ordinary-prime Euler-factor realization, the uniform prime-power remainder control, and the explicit comparison with the positive-real stable compression already proved in `RE-193`. No external theorem beyond already anchored PNT input is load-bearing, so `SOURCES.md` needs no new durable dependency.

## Literature status

The abstract Fourier time--bandwidth principle is classical. The line-specific result is an exact bridge from the ordinary-prime Euler source to a well-conditioned vertical Fourier frame, showing that the severe stable noncoercivity established on the positive real ray is representation-specific and cannot be promoted to the complex direction merely by analogy.

## Caveats

The shell width `W` is fixed in the theorem. Letting the source span grow changes amplitude conditioning unless the real offset and source normalization are adjusted; no growing-width claim is made here. The sampled height grows like `K/W`, so the theorem does not show that a bounded vertical segment resolves arbitrarily many honest one-prime edits on a fixed shell. It also gives no lower bound for the vertical discrepancy of the actual `RE-188`/`RE-199` matched controls.

The finding does not prove RH, Robin's inequality, a zero-free statement, or source rigidity. It identifies a complex observation channel with enough stable representation rank to be worth testing against the matched-control constructions that defeated the positive-real channel.

## Next experiment

Evaluate the `RE-188`/`RE-199` ordinary-prime `{0,1,2}` matched controls on a vertical frame with `t` up to `Theta(log p)` and isolate the first repair shell. Either extend the repair construction to match a growing set of complex Fourier samples while preserving KV fidelity and the Robin transient, which would push non-rigidity into the complex channel, or prove that the selector debt forces a non-negligible vertical Fourier coefficient. The latter would be the first scalar source-discrimination mechanism in this branch that survives the positive-real Laplace near-kernels.

In parallel, the real-ray branch can still try to reduce the `RE-188` effective width constant `4` and cross the quarter-linear threshold of `RE-199`; the two directions now test genuinely different representation geometry.

## Sources

- `RE-193`, *Dyadic Laplace compression makes Euler stable dimension logarithmic*.
- `RE-199`, *Full-real Euler collapse persists through sub-quarter-linear depth*.
- `RE-015`, for the standard Korobov--Vinogradov PNT envelope already anchored in `SOURCES.md`.
- H. J. Landau and H. O. Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty—III: The Dimension of the Space of Essentially Time- and Band-Limited Signals*, Bell System Technical Journal **41** (1962), 1295--1336, DOI `10.1002/j.1538-7305.1962.tb03279.x`.
