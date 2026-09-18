# WI-344 — fixed source aperture compresses every fixed linear bank of bow-height windows

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + NON-RH`.

## Claim

WI-343 proves that the bow-height carriers on one natural Gallagher window have bounded approximate dimension. The same obstruction is not tied to one window. It survives **every fixed, height-independent linear bank of source windows or statistics whose total logarithmic source aperture is bounded**.

Let `S` be a finite set of positive integers contained in one logarithmic interval

\[
\log n\in[x_c-\Delta/2,x_c+\Delta/2]\qquad(n\in S),
\tag{1}
\]

let `a=(a_n)_{n\in S}\neq0` be arbitrary complex coefficients, and let the height parameter range over

\[
U\in[U_c-H/2,U_c+H/2].
\tag{2}
\]

Define

\[
v_U(n):=a_n n^{iU}\in\ell^2(S).
\tag{3}
\]

For every integer `d>=0` there is a subspace `V_d\subset\ell^2(S)` of dimension at most `d+1`, independent of `U`, such that

\[
\boxed{
\operatorname{dist}(v_U,V_d)
\le
\varepsilon_d\,\|a\|_2,
\qquad
\varepsilon_d:=
\frac{(H\Delta/4)^{d+1}}{(d+1)!}.
}
\tag{4}
\]

Now let

\[
A:\ell^2(S)\longrightarrow\mathcal K
\tag{5}
\]

be **any bounded linear map independent of `U`**, into any Hilbert space. It may encode arbitrarily many fixed masks, translated source windows, linear filters, or joint linear source statistics at once. Then

\[
\boxed{
\operatorname{dist}(Av_U,AV_d)
\le
\|A\|\varepsilon_d\|a\|_2,
\qquad
\dim(AV_d)\le d+1.
}
\tag{6}
\]

Thus channel count by itself cannot create new height directions. There is one essential qualification: a badly conditioned `A` can suppress the low-rank part and make the residual look large after normalization. This costs transmitted scale exactly. For sampled heights `U_1,...,U_m`, suppose

\[
\eta:=
\min_k
\frac{\|Av_{U_k}\|}
     {\|A\|\,\|a\|_2}
>0,
\tag{7}
\]

and normalize `h_k=Av_{U_k}/\|Av_{U_k}\|`. If `G_A=(\langle h_j,h_k\rangle)` has eigenvalues in decreasing order, then

\[
\boxed{
\sum_{j>d+1}\lambda_j(G_A)
\le
m\left(\frac{\varepsilon_d}{\eta}\right)^2.
}
\tag{8}
\]

Consequently, if a fixed linear bank produces an extensive normalized spectral tail

\[
\sum_{j>d+1}\lambda_j(G_A)\ge c m
\tag{9}
\]

for some `c>0`, it must satisfy the sharp scale implication

\[
\boxed{
\eta\le\frac{\varepsilon_d}{\sqrt c}.
}
\tag{10}
\]

At the exact Gallagher aperture of WI-195, `H\Delta=1`. Centering both intervals therefore strengthens WI-343's rank-seven Taylor error from `1/5040` to

\[
\boxed{
\varepsilon_6
=\frac{(1/4)^7}{7!}
=\frac1{82\,575\,360},
}
\tag{11}
\]

and for the unprocessed carrier bank (`A=I`, `eta=1`)

\[
\boxed{
\sum_{j>7}\lambda_j(G)
\le
\frac{m}{82\,575\,360^2}
<1.467\times10^{-16}m.
}
\tag{12}
\]

More generally, the scale-preserving effective linear height dimension is `O(H Delta)`. In particular, on a fixed dyadic source block `S\subset[X,2X]`, where `Delta=log 2`, every fixed height-independent linear bank has only `O(H)` generic carrier dimension unless it pays a vanishing transmission factor. Merely proliferating source windows or starts **inside the same fixed logarithmic aperture** therefore does not manufacture a number of independent bow-height tests comparable to their channel count.

This is a route restriction, not an RH result. It does not prove the signed `Lambda-Lambda^sharp` cancellation requested by the live bow clue, improve the unconditional simple-critical-zero proportion, or exclude any off-critical zero. It redirects the linear multiwindow escape left by WI-343 toward genuinely growing logarithmic aperture, height-dependent/arithmetic source selection, nonlinear observables, or direct signed covariance.

## 1. Centered carrier expansion gives the exact aperture product

Write

\[
\xi_n:=\log n-x_c,
\qquad
\delta_U:=U-U_c.
\tag{13}
\]

Then

\[
|\xi_n|\le\Delta/2,
\qquad
|\delta_U|\le H/2,
\qquad
|\delta_U\xi_n|\le\frac{H\Delta}{4}.
\tag{14}
\]

Factor the carrier as

\[
v_U(n)
=e^{i\delta_Ux_c}
 a_n n^{iU_c}e^{i\delta_U\xi_n}.
\tag{15}
\]

The first factor is a scalar phase and has no effect on distance to a linear subspace. For real `z`, Taylor's formula with integral remainder gives

\[
\left|
 e^{iz}-\sum_{r=0}^{d}\frac{(iz)^r}{r!}
\right|
\le\frac{|z|^{d+1}}{(d+1)!}.
\tag{16}
\]

Define

\[
b_r(n):=a_n n^{iU_c}\xi_n^r,
\qquad
V_d:=\operatorname{span}\{b_0,\ldots,b_d\}.
\tag{17}
\]

The Taylor polynomial in (16), multiplied by the harmless scalar `e^{i\delta_Ux_c}`, is an element of `V_d`. Equations (14)--(16) therefore give pointwise

\[
|v_U(n)-p_{U,d}(n)|
\le
|a_n|\frac{(H\Delta/4)^{d+1}}{(d+1)!}.
\tag{18}
\]

Squaring and summing over `S` proves (4). No positivity of the coefficients, prime distribution, zero-spacing input, or asymptotic approximation is used.

The factor `1/4` is the gain from centering **both** the height interval and the logarithmic source aperture. WI-343 expanded from a left endpoint on the exact Gallagher window, where only `|delta_U xi_n|<=1` was used. That older estimate remains correct; (4) is a strict quantitative refinement and, more importantly, applies to an arbitrary finite logarithmic aperture `Delta`.

## 2. Gram-tail bound and the fixed-linear-bank extension

Take sampled heights `U_1,...,U_m` and normalize the unprocessed vectors by

\[
g_k:=\frac{v_{U_k}}{\|a\|_2}.
\tag{19}
\]

Let `P_d` be orthogonal projection onto `V_d`. From (4),

\[
\sum_{k=1}^{m}\|(I-P_d)g_k\|^2
\le m\varepsilon_d^2.
\tag{20}
\]

If `C:\mathbf C^m\to\ell^2(S)` is the column operator `Ce_k=g_k`, then `P_dC` has rank at most `d+1` and

\[
\|C-P_dC\|_F^2\le m\varepsilon_d^2.
\tag{21}
\]

By the variational characterization of best low-rank approximation, the squared singular-value tail of `C` is at most the right side. Since the squared singular values of `C` are the eigenvalues of its Gram matrix,

\[
\sum_{j>d+1}\lambda_j(G)
\le m\varepsilon_d^2.
\tag{22}
\]

Now apply an arbitrary bounded fixed linear map `A`. Equation (6) is immediate from

\[
\operatorname{dist}(Av_U,AV_d)
\le
\|A\|\operatorname{dist}(v_U,V_d).
\tag{23}
\]

Under the scale-retention hypothesis (7), divide (23) by `\|Av_{U_k}\|`. Every normalized output then lies within distance at most `epsilon_d/eta` of the common subspace `AV_d`, whose dimension is at most `d+1`. Repeating (20)--(22) proves (8).

This formulation is deliberately conditioning-aware. Without (7), the stronger statement that every fixed `A` preserves low normalized rank would be false: an ill-conditioned operator can annihilate or heavily suppress the dominant Taylor modes and expose a tiny residual. Equation (10) records the price. It is the source-aperture analogue of the conditioning--transmission principle already isolated in WI-110 for a different full-packed Ramanujan operator: conditioning can be improved only by paying in the natural transmitted scale.

There is also an unnormalized statement with no lower-scale hypothesis. If `C_Ae_k=Av_{U_k}`, then

\[
\boxed{
\sum_{j>d+1}s_j(C_A)^2
\le
m\|A\|^2\|a\|_2^2\varepsilon_d^2.
}
\tag{24}
\]

Thus (7) is needed only when one wishes to interpret the output after normalizing away its absolute size.

## 3. The effective dimension is controlled by `H Delta`, not channel count

Put

\[
B:=\frac{H\Delta}{4},
\qquad
N:=d+1.
\tag{25}
\]

The elementary factorial bound `N!>=(N/e)^N` gives

\[
\varepsilon_{N-1}
=\frac{B^N}{N!}
\le
\left(\frac{eB}{N}\right)^N.
\tag{26}
\]

Choose

\[
N\ge 2eB=\frac{eH\Delta}{2}.
\tag{27}
\]

Then

\[
\boxed{
\varepsilon_{N-1}\le2^{-N}.
}
\tag{28}
\]

Therefore, for every fixed lower transmission `eta_0>0`, taking

\[
N=\max\!\left(1,\left\lceil\frac{eH\Delta}{2}\right\rceil\right)
\tag{29}
\]

already gives an exponentially small normalized spectral tail `m eta_0^{-2}4^{-N}`. The constant is not meant as an optimal prolate-spheroidal dimension estimate; the relevant conclusion is the exact scaling

\[
\boxed{\text{scale-preserving linear carrier dimension}=O(H\Delta).}
\tag{30}
\]

For the natural WI-195 multiplicative window, `Delta=1/H`, so `H Delta=1` and (11)--(12) give a particularly strong constant-dimensional version. For any collection of fixed linear windows, masks, or starts whose **union of source support** remains in one dyadic block `[X,2X]`, one may take

\[
\Delta=\log2,
\tag{31}
\]

and the generic carrier dimension is `O(H)`, irrespective of how many channels the bank contains.

At a count-saturating bow the zero population has an additional logarithmic density relative to the vertical height scale. Equation (31) therefore prevents a proof from identifying raw channel count inside one dyadic block with the much larger portfolio of bow ordinates. This does not say that `O(H)` source directions are useless; it says that **window proliferation inside fixed aperture is not itself a de-exceptionalization mechanism**.

## 4. Relation to the exact Montgomery/Gallagher source

The conclusion must not be overstated as a theorem about the entire Montgomery prime polynomial. WI-188 records the source

\[
a_x(n)=\frac{\Lambda(n)}{\sqrt n}
\min\!\left(\frac nx,\frac xn\right),
\tag{32}
\]

whose support is all positive integers. The theorem above applies exactly to any finite/log-aperture component of that source, for example a dyadic block, or to a finite bank of Gallagher windows whose union lies in such a component. A global decomposition into many source scales increases the total logarithmic aperture and is intentionally not compressed by (30) to the one-block dimension.

This identifies the correct linear escape from WI-343. If one wants generic carrier dimension comparable to `H log T` solely from source aperture, (30) requires a total logarithmic aperture of order `log T`, not merely more channels inside one fixed dyadic block. Such a logarithmic stack is a genuinely cross-scale construction and can interact with the decay and arithmetic structure of (32); it is not ruled out here. WI-218 supplies a separate example in the bow program where stacking `O(log T)` multiplicative slabs changes a screen-complexity conclusion, so treating cross-scale organization as distinct from same-aperture channel proliferation is already structurally motivated inside the line.

The theorem also leaves open a bank whose coefficients themselves depend on `U`. In that case there is no single operator `A` acting on the common carrier family, and the conclusion need not hold. Any such dependence must come from a justified arithmetic/source relation rather than being inserted after seeing the target ordinate if it is to feed an unconditional proof.

## 5. Prior art and novelty boundary

The mechanism is classical time--bandwidth concentration. No novelty is claimed for the principle that a Fourier kernel restricted to bounded time and frequency boxes is approximately low rank.

- D. Slepian and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — I**, *Bell System Technical Journal* 40 (1961), 43--63, DOI `10.1002/j.1538-7305.1961.tb03976.x`, construct the classical prolate-spheroidal concentration framework.
- H. J. Landau and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — III: The Dimension of the Space of Essentially Time- and Band-Limited Signals**, *Bell System Technical Journal* 41 (1962), 1295--1336, DOI `10.1002/j.1538-7305.1962.tb03279.x`, explicitly relates the number of essentially independent signals to the time--bandwidth product.
- E. Candès, L. Demanet and L. Ying, **A Fast Butterfly Algorithm for the Computation of Fourier Integral Operators**, *Multiscale Modeling & Simulation* 7 (2009), 1727--1750, DOI `10.1137/080734339`, develops the modern complementary-low-rank viewpoint for oscillatory kernels restricted to suitable time/frequency subsets.

The proof here does not invoke those theorems: (4) is the elementary centered Taylor separated expansion of the discrete multiplicative Fourier kernel `e^{iU log n}`, and (8) is the corresponding Hilbert-space low-rank tail estimate after a fixed linear map. The prior art fixes the classification of the mechanism and prevents a false novelty claim.

A bounded line-local novelty audit checked WI-343, which treats one fixed Gallagher source window; WI-207, which gives a dimension-free **positive-PSD packet-residue** bound for multiwindow Gallagher lifts; WI-144, which treats positive-Hilbert/Frobenius lifts of the zero-side Lamzouri kernel; WI-110, which gives a conditioning--transmission product law for a different full-packed Ramanujan interface; and WI-218, which uses stacked multiplicative slabs in the screen-complexity program. None contains the present fixed-aperture theorem (4)--(10). Targeted searches for a bow/source-aperture linear-bank statement also found no duplicate in the line. Absence from those searches is not evidence of external priority.

The durable Mathia claim is therefore narrow: **the exact bow/source carrier family over logarithmic aperture `Delta` admits the explicit centered rank bound (4), and every fixed height-independent linear source-window bank inherits it with the scale-sensitive transmission law (8)--(10).**

## 6. Boundary conditions and falsification controls

The result has several deliberate boundaries.

First, `A` must be common to the sampled heights. A family of unrelated operators `A_U` can encode the height label itself and need not have any common low-dimensional image. Second, the normalized conclusion requires nonvanishing transmission as measured by `eta`; without it, a near-annihilator can magnify the residual after normalization. Third, the aperture `Delta` is the diameter of the **union** of source support. Spreading windows across more source scales increases `Delta`, exactly as time--bandwidth intuition predicts.

Fourth, the theorem is purely linear. Nonlinear statistics of several source outputs, sign-sensitive products, source-dependent adaptive coefficients, or a direct estimate of the signed off-diagonal covariance lie outside it. Fifth, it uses no zeta-zero equation or off-critical residue structure and hence says nothing by itself about whether the uncertified zero complement consists of multiple critical-line zeros, off-line functional-equation blocks, or proof slack.

A falsification of the stated theorem would therefore have to exhibit a fixed bounded linear map `A`, a finite source set satisfying (1), sampled heights satisfying (2), and a normalized Gram tail violating (8) while retaining the transmission lower bound (7). Equations (14)--(23) reduce such a counterexample to a failure of the scalar Taylor remainder or of the standard best-rank approximation inequality.

## Research consequence

The `many bow ordinates -> many source tests` program cannot be revived merely by replacing the single WI-343 Gallagher window with an arbitrarily large **fixed linear bank** of windows or starts that all live in one bounded logarithmic source aperture. The common carrier kernel already has approximate dimension `O(H Delta)`, and fixed linear postprocessing cannot add scale-preserving directions; if it exposes the tiny residual, (10) records the lost transmission.

The live distinguished-twist clue should therefore keep as genuinely different possibilities: a logarithmically growing source aperture/cross-scale construction; height-dependent coefficients forced by arithmetic rather than chosen freely; a nonlinear or sign-indefinite joint observable whose control is not inherited from fixed linear geometry; or the original direct attack on the signed `Lambda-Lambda^sharp` covariance. None is supplied by this finding, but same-aperture linear window proliferation is now closed as a free source of bow-height independence.