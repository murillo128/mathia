# MC-110 — Diagonal shell norms have an almost-square source floor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact Hamming shell decomposition from `MC-095` and `MC-107`--`MC-109`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
L:=\log\log N.
\tag{1}
\]

`MC-095` left open a potentially useful route: control an `L^2` or other norm of the degree-shell vector and transfer that control to the Möbius endpoint with only a small reconstruction cost. The later Sathe--Selberg shell profile closes that route for every certificate that takes absolute values shell by shell before recombining the endpoint.

Let `1<=p<=infinity`, let `q` be its Hölder conjugate, and let

\[
w_{k,N}>0
\]

be arbitrary finite diagonal weights on the occurring shells. Define the corresponding diagonal Hölder certificate

\[
\mathfrak H_{p,w}(N)
:=
\left\|(w_{k,N}C_{k,N})_k\right\|_{\ell^p}
\left\|(w_{k,N}^{-1})_k\right\|_{\ell^q}.
\tag{2}
\]

Hölder gives

\[
|\mathcal Q_N(1)|\le \mathfrak H_{p,w}(N).
\tag{3}
\]

But for **every** occurring shell `K`, the same two norms satisfy the exact coordinate floor

\[
\boxed{
\mathfrak H_{p,w}(N)\ge |C_{K,N}|.
}
\tag{4}
\]

Indeed, the first factor is at least `w_{K,N}|C_{K,N}|` and the second is at least `w_{K,N}^{-1}`. Thus no choice of diagonal preconditioner can hide a single large shell: the inverse dual weight pays back exactly what the primal weight suppresses.

Now choose an integer `K_N` with

\[
K_N-2=2L+O(1).
\tag{5}
\]

The critical Sathe--Selberg profile of `MC-107` gives

\[
C_{K_N,N}
\sim
\frac{36J}{\pi^4\sqrt{4\pi L}}N^2,
\qquad
J=\gamma+\gamma_1-\frac12>0.
\tag{6}
\]

Therefore every diagonal Hölder certificate `(2)` obeys

\[
\boxed{
\mathfrak H_{p,w}(N)
\ge
\left(\frac{36J}{\pi^4\sqrt{4\pi}}+o(1)\right)
\frac{N^2}{\sqrt{\log\log N}}
=N^{2-o(1)}.
}
\tag{7}
\]

This is a source-level obstruction, not merely a generic norm bound. It applies simultaneously to `L^1`, `L^2`, `L^infinity`, every intermediate Hölder pair, every fixed noise radius from `MC-095`, and arbitrary `N`-dependent positive diagonal shell weights. Such an absolute shell certificate cannot by itself yield **any fixed polynomial power saving below `N^2`**, even though the exact signed endpoint has the unconditional all-logarithmic saving

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\qquad(A>0\text{ fixed})
\tag{8}
\]

used in `MC-107`--`MC-109`.

The gap is therefore not an issue of choosing a better radial weight or a better shell norm. The missing information is the **signed cancellation between different Hamming degrees before absoluteization**. A surviving radial method must use a genuinely non-diagonal signed transform or recurrence. A surviving non-radial method may retain additional product-fiber information, but it cannot obtain the endpoint merely by compressing to shell magnitudes and applying a dual norm.

No improved estimate for `M(x)` is claimed.

## 1. The diagonal no-go is independent of the norm and of the weights

For finite sequences `x=(x_k)` and `y=(y_k)`, Hölder's inequality gives

\[
\left|\sum_k x_ky_k\right|
\le \|x\|_p\|y\|_q.
\tag{9}
\]

Set

\[
x_k=w_{k,N}C_{k,N},
\qquad
y_k=(-1)^kw_{k,N}^{-1}.
\tag{10}
\]

Then `(9)` is exactly `(3)`. For any fixed occurring `K`,

\[
\|x\|_p\ge |x_K|=w_{K,N}|C_{K,N}|,
\qquad
\|y\|_q\ge |y_K|=w_{K,N}^{-1},
\tag{11}
\]

with the same statement under the usual endpoint conventions for `p=1,infinity`. Multiplying `(11)` proves `(4)`.

The argument also shows why choosing an `N`-dependent radial noise parameter cannot help this class of proof. For the geometric choice `w_k=r_N^k`, making the central shell small in the primal norm automatically makes the same coordinate large by the inverse factor `r_N^{-K}` in the endpoint functional. This is the shell-level analogue of the collision--reconstruction tradeoff in `MC-096`, but here the lower bound is tied to the **actual source coefficient** rather than to the dimension of an ambient quotient class.

## 2. The central window contains many almost-square positive shells

The obstruction is not concentrated in one accidentally selected degree. `MC-107` gives, in the Gaussian central window

\[
\frac{k-2-2L}{\sqrt{2L}}\to y,
\tag{12}
\]

the uniform profile

\[
C_{k,N}
\sim
\frac{36J}{\pi^4\sqrt{4\pi L}}
 e^{-y^2/2}N^2.
\tag{13}
\]

Hence for every fixed `R>0`, there are `Theta_R(sqrt(L))` consecutive shells with

\[
|k-2-2L|\le R\sqrt{2L}
\tag{14}
\]

and each has size comparable to `N^2/sqrt(L)`. Removing finitely many, or more generally `o(sqrt(L))`, exceptional degrees before applying a diagonal shell norm therefore does not remove the obstruction: at least one central shell of the same power scale remains.

This materially strengthens the earlier degree-two warning. `MC-097` already showed that a low shell has a positive `N^2/(log N)^2` main term. The proportional profile now shows that the shell-energy obstruction becomes much larger near the natural `2 log log N` turning scale and occupies a growing window of degrees.

## 3. The ordinary shell `L^2` energy is itself almost square

The same central profile quantifies the exact scale of the shell-square-function proposed in `MC-095`. Put

\[
c_*:=\frac{36J}{\pi^4}.
\tag{15}
\]

For `k` in `(12)`, equation `(13)` can be written as

\[
C_{k,N}
\sim
\frac{c_*}{\sqrt{4\pi L}}
 e^{-y^2/2}N^2.
\tag{16}
\]

Summing squares over any fixed Gaussian window and then letting its width tend to infinity gives the source-energy lower asymptotic

\[
\boxed{
\sum_{k=0}^{D_N}|C_{k,N}|^2
\ge
\left(\frac{c_*^2}{\sqrt{8\pi L}}+o\!\left(L^{-1/2}\right)\right)N^4.
}
\tag{17}
\]

Equivalently,

\[
\boxed{
\|(C_{k,N})_k\|_2
\ge
\left(c_*+o(1)\right)
\frac{N^2}{(8\pi L)^{1/4}}.
}
\tag{18}
\]

To see the constant, set `lambda=2L` and `n=k-2`. The squared central profile has the same local mass as

\[
\frac{c_*^2N^4}{(\log N)^4}
\frac{\lambda^{2n}}{(n!)^2}.
\tag{19}
\]

The classical modified-Bessel identity

\[
I_0(2\lambda)=\sum_{n\ge0}\frac{\lambda^{2n}}{(n!)^2}
\tag{20}
\]

and the large-argument asymptotic

\[
I_0(2\lambda)\sim\frac{e^{2\lambda}}{\sqrt{4\pi\lambda}}
\tag{21}
\]

give `e^{2 lambda}=(log N)^4` and the constant in `(17)`. Only a lower bound is needed here: the uniform central-window form of `MC-107` already supplies it, so no unproved global tail asymptotic is being inserted.

The identities `(20)`--`(21)` are classical modified-Bessel facts; see NIST DLMF §§10.25/10.31 and 10.30. No novelty is claimed for this calculation.

## 4. Radial Fourier Parseval exposes the same obstruction

Let `M_N>D_N` and sample the unit circle at the `M_N`-th roots of unity,

\[
t_j=e^{2\pi i j/M_N}.
\tag{22}
\]

Discrete Fourier orthogonality gives the exact identity

\[
\boxed{
\frac1{M_N}\sum_{j=0}^{M_N-1}
|\mathcal Q_N(t_j)|^2
=
\sum_{k=0}^{D_N}|C_{k,N}|^2.
}
\tag{23}
\]

The minus sign in `(-t)^k` is immaterial to orthogonality. Combining `(17)` and `(23)` gives an RMS floor

\[
\boxed{
\left(
\frac1{M_N}\sum_j|\mathcal Q_N(t_j)|^2
\right)^{1/2}
\ge
(c_*+o(1))\frac{N^2}{(8\pi L)^{1/4}}.
}
\tag{24}
\]

Thus the small Möbius value `mathcal Q_N(1)` is not representative of the radial Fourier energy. The endpoint is produced by an exceptionally coherent alternating cancellation across the large positive shell profile. Parseval faithfully measures the shell energy, but exactly for that reason it cannot explain the tiny distinguished phase after the signs have been squared away.

This closes the specific conditional escape left in `MC-095`: a strict-power `L^2` estimate for the actual degree-shell vector is not merely missing from the literature; it is false for this source at the required power scale.

## Prior art and novelty boundary

The norm argument is ordinary Hölder/Cauchy duality, and `(23)` is finite discrete Fourier Parseval. The central shell input is the source-specific Sathe--Selberg profile already established in `MC-107`, whose analytic ingredients come from classical Landau--Selberg--Delange/Sathe--Selberg theory. The modified-Bessel summation used only to calibrate the `L^2` scale is classical.

A targeted search for combinations of Möbius parity, Sathe--Selberg shell norms, Hamming radialization, and weighted `L^p` certificates did not identify this source-specific no-go as a standard named theorem. That absence is not used as evidence of novelty. **No novelty claim is made.** The durable result is the exact closure of a live Mathia route: once the Hamming source has been quotiented to degree shells, every positive diagonal norm/dual-norm certificate necessarily discards the cross-degree sign cancellation it is supposed to explain.

## Boundaries and falsification tests

- The theorem rules out **diagonal shell absoluteization**, not all radial analysis. A signed non-diagonal transform can mix different degrees before taking a norm and is not covered by `(4)`.
- It does not rule out non-radial product-fiber, bilinear, prime-factor, or source-coupled information that is absent from the shell vector.
- The weights in `(2)` must be finite and positive on the shells retained by the certificate. Setting a weight to zero merely makes the inverse endpoint functional undefined; it does not evade the tradeoff.
- Exact subtraction of a set of shell contributions changes the problem. But by `(13)`--`(14)`, subtracting only `o(sqrt(log log N))` degrees from a fixed central window still leaves an almost-square shell and therefore the same power obstruction.
- Equation `(17)` is stated as a lower asymptotic because that is all the no-go requires. No claim about the complete far-tail contribution to the shell `L^2` norm is needed.
- The endpoint estimate `(8)` is the existing unconditional bound for this Hamming source. It is not derived from the shell norm and no stronger Mertens exponent is inferred.

## Consequence for the research line

The radial frontier is now narrower than after `MC-109`. Direct truncation fails below, above, and through the `2 log log N` turning window, while this finding shows that replacing truncation by a positively weighted shell `L^p`/square-function estimate also cannot recover a fixed power gain. The large shells are real source mass, not a poor choice of norm.

The surviving radial possibility must preserve cancellation **between** degrees before any absolute value is taken. Otherwise the route must leave radialization and retain a genuinely source-specific non-radial coupling. This is the same residual demanded by the accepted parity-sensitive annular clue, now with its proposed shell-square-function branch closed.