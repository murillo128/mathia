# ANF-146 — moving-window stable rank exposes the exact bow coherence gap

**Status:** `EXACT-DERIVED + CLASSICAL-CONVOLUTION + SHARP-MATCHED-CONTROL + NEGATIVE/OBSTRUCTION + SOURCE-SPECIFIC-GATE`. `ANF-145` isolates a full factor of the short-interval length `K` between the available componentwise `K^2` mean-square scale and the bow residual's diagonal scale `K log X` after normalization by the `x`-interval length. That factor cannot be recovered from the moving-window geometry alone. The unnormalized length-`K` moving-sum operator has average squared singular scale exactly `K` but top squared singular scale asymptotic to `K^2`; equivalently its stable rank is `N/K+O(1)` on `N` consecutive windows. More directly, for the exact moving diagonal `D(b)` one has the sharp coefficient-general inequality `0 <= V(b) <= K D(b)`, and unit-modulus plane waves attain both endpoints. Thus support, coefficient magnitudes, and diagonal `L^2` mass leave a complete factor-`K` coherence freedom. Any bow theorem that closes the `ANF-145` gap must use arithmetic phase/sign structure of the distinguished residual or preserve cancellation between decomposition pieces; a source-blind refinement of the box-convolution estimate cannot supply the missing `1/K`.

## 1. The finite moving-window operator has an exact factor-K spectral spread

Let `N>=1` and `1<=K<=N`, and define

\[
A_{N,K}:\mathbb C^{N+K-1}\longrightarrow\mathbb C^N,
\qquad
(A_{N,K}b)_j:=\sum_{r=1}^{K}b_{j+r},
\quad 0\le j<N.
\tag{1}
\]

This is the rectangular length-`K` convolution map restricted to `N` consecutive output windows. Every row contains exactly `K` entries equal to one, so

\[
\boxed{\|A_{N,K}\|_F^2=NK.}
\tag{2}
\]

The rows are linearly independent. Indeed, if a linear combination of the rows vanishes, column `1` forces the coefficient of row `0` to vanish, column `2` then forces the coefficient of row `1` to vanish, and induction through column `N` kills all row coefficients. Hence

\[
\boxed{\operatorname{rank}A_{N,K}=N.}
\tag{3}
\]

The coefficient-general operator norm has the box-convolution scale. Young's inequality on `ell^2(Z)`, or the Schur bound using maximal row and column sums, gives

\[
\|A_{N,K}\|_{2\to2}\le K.
\tag{4}
\]

For the constant vector `\mathbf 1` of length `N+K-1`, every output equals `K`, and therefore

\[
\frac{\|A_{N,K}\mathbf 1\|_2^2}{\|\mathbf 1\|_2^2}
=
\frac{NK^2}{N+K-1}.
\tag{5}
\]

Consequently

\[
\boxed{
\frac{NK^2}{N+K-1}
\le
\|A_{N,K}\|_{2\to2}^2
\le K^2.
}
\tag{6}
\]

In particular, whenever `K=o(N)`,

\[
\|A_{N,K}\|_{2\to2}^2
=K^2\left(1+O\!\left(\frac KN\right)\right)
\tag{7}
\]

in the two-sided sense furnished by (6). Since the average of the nonzero squared singular values is

\[
\frac{\|A_{N,K}\|_F^2}{\operatorname{rank}A_{N,K}}=K,
\tag{8}
\]

the coherent top mode is larger than the average singular scale by a full factor `K`. Equivalently the stable rank satisfies the exact bounds

\[
\boxed{
\frac NK
\le
\operatorname{sr}(A_{N,K})
:=\frac{\|A_{N,K}\|_F^2}{\|A_{N,K}\|_{2\to2}^2}
\le
\frac{N+K-1}{K},
}
\tag{9}
\]

so

\[
\operatorname{sr}(A_{N,K})=\frac NK+O(1).
\tag{10}
\]

The distinction is therefore intrinsic to the finite moving-window operator: its diagonal/Frobenius energy lives on `N/K` effective coherent directions, while one nearly constant direction carries squared gain `K^2`.

## 2. Identical-magnitude controls attain both zero and the sharp factor-K upper endpoint

For a coefficient vector `b`, define the exact moving diagonal

\[
D_{N,K}(b)
:=
\sum_{j=0}^{N-1}\sum_{r=1}^{K}|b_{j+r}|^2
\tag{11}
\]

and the moving-window energy

\[
V_{N,K}(b)
:=
\sum_{j=0}^{N-1}
\left|\sum_{r=1}^{K}b_{j+r}\right|^2
=
\|A_{N,K}b\|_2^2.
\tag{12}
\]

Pointwise Cauchy--Schwarz on each window gives the sharp universal inequality

\[
\boxed{0\le V_{N,K}(b)\le K D_{N,K}(b).}
\tag{13}
\]

Both endpoints occur among coefficient vectors having exactly the same support and exactly the same coefficient magnitudes. For the unit-modulus plane wave

\[
b_n=e^{in\theta},
\tag{14}
\]

one has

\[
(A_{N,K}b)_j
=e^{ij\theta}H_K(\theta),
\qquad
H_K(\theta):=\sum_{r=1}^{K}e^{ir\theta},
\tag{15}
\]

and therefore

\[
D_{N,K}(b)=NK,
\qquad
V_{N,K}(b)=N|H_K(\theta)|^2.
\tag{16}
\]

The familiar geometric-sum formula is

\[
|H_K(\theta)|
=
\left|\frac{\sin(K\theta/2)}{\sin(\theta/2)}\right|
\tag{17}
\]

away from multiples of `2 pi`, with the continuous value `K` at the origin. Hence the constant-phase choice `theta=0` gives

\[
V_{N,K}=NK^2=K D_{N,K},
\tag{18}
\]

while for every `K>=2` the equally spaced phase choice

\[
\theta=\frac{2\pi}{K}
\tag{19}
\]

gives

\[
H_K(2\pi/K)=0,
\qquad
\boxed{V_{N,K}=0}
\tag{20}
\]

with the **same** value `D_{N,K}=NK` and the same pointwise magnitudes `|b_n|=1`.

Thus the diagonal does not merely fail to determine the variance up to a constant. With all coefficient sizes frozen exactly, phase coherence can move the output through the entire natural factor-`K` window from zero to `K` times the diagonal. The Dirichlet-kernel response (17) is the classical frequency-domain form of this fact; the Mathia-specific consequence is that the missing factor isolated in `ANF-145` is precisely the amount of coherence that the box operator itself leaves unresolved.

## 3. The bow moving variance is exactly this operator on the twisted residual

For the residual of `ANF-102` and `ANF-145`,

\[
b_n(U):=a_X(n)n^{-iU},
\qquad
a_X(n)=\Lambda(n)-\Lambda^\sharp(n),
\tag{21}
\]

suppose first that `X` and `K` are integers. Except at the measure-zero integer endpoints, the short sum is constant while `x` traverses each unit interval. Therefore

\[
\begin{aligned}
V_X(U;K)
&=\int_X^{2X}
\left|\sum_{x<n\le x+K}b_n(U)\right|^2dx\\
&=\sum_{j=X}^{2X-1}
\left|\sum_{r=1}^{K}b_{j+r}(U)\right|^2.
\end{aligned}
\tag{22}
\]

After reindexing, (22) is exactly `V_{X,K}(b(U))`. Likewise, opening the square shows that the diagonal used in `ANF-102` is exactly

\[
D_X(K)
=
\sum_{j=X}^{2X-1}\sum_{r=1}^{K}|b_{j+r}(U)|^2,
\tag{23}
\]

which is independent of `U` because the Archimedean twist has unit modulus. Nonintegral endpoints only replace the first and last unit cells by partial weights and do not alter the asymptotic bow scales.

`ANF-102` proves for

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{24}
\]

that

\[
D_X(K)=(1+o(1))XK\log X.
\tag{25}
\]

The desired distinguished-twist cancellation would have to make `V_X(U;K)=o(D_X(K))`. But the moving-window map, viewed without arithmetic information about the phases and signs of `b_n(U)`, permits the whole sharp range

\[
0\le V_X\le K D_X.
\tag{26}
\]

This identifies the geometry underlying the power gap in `ANF-145`. A generic short-sum estimate at amplitude scale `K` naturally squares to the coherent operator scale `K^2`; the diagonal target sits at the average squared singular scale `K`. The extra factor `1/K` required by the bow argument is therefore not available from a better constant in the same coefficient-general moving-window inequality.

The statement is intentionally narrower than claiming that MRSTT Lemma 3.5 is sharp. Its type-II coefficients satisfy substantial arithmetic and bilinear structure absent from the matched controls above. The conclusion is instead an information boundary: **any proof that sees only interval length, support, coefficient magnitudes, and generic `ell^2` mass cannot supply the missing factor `1/K` uniformly.**

## 4. The missing input must distinguish coherent phase profiles

Equation (17) makes the missing information explicit. The box operator strongly amplifies additive phase profiles whose local frequency is close to zero modulo `2 pi`, and exactly annihilates the `K`th-root profile (19). Coefficient magnitudes cannot distinguish these cases. The distinguished bow vector (21) contains the arithmetic sign pattern of `Lambda-Lambda^sharp` multiplied by the logarithmic phase `e^{-iU\log n}`; whether it lies near a high-gain or low-gain direction is therefore an arithmetic question, not a moving-window norm question.

This sharpens the source-side alternatives left by `ANF-145`. A successful route can, for example, prove that the actual residual or each load-bearing bilinear component has sufficiently little projection onto high-gain box modes at the distinguished `U`, or it can retain cancellation between decomposition pieces whose individual box energies are large. What cannot work is a source-blind attempt to replace the `K^2` componentwise scale by `K` solely from support geometry or coefficient-size bookkeeping: (18) is an exact counterexample to such a theorem.

The result also complements `ANF-144` rather than duplicating it. `ANF-144` shows that the **twist-axis localization scale** `X` is coefficient-generally sharp by a two-term resonant control. The present finding concerns the orthogonal issue of the **short-window amplitude scale**: even at one fixed twist, a length-`K` box has a factor-`K` gap between its diagonal and coherent energy. A future bow theorem must beat both generic barriers simultaneously by using source arithmetic at the distinguished twist.

## 5. Prior-art boundary and consequences

The underlying operator is classical. A rectangular moving average is a boxcar finite-impulse-response filter, its response to a pure tone is the geometric sum/Dirichlet-kernel profile (17), and convolution admits the standard `ell^2` Young bound. The finite-rank and stable-rank estimates (2)--(10), the sharp diagonal inequality (13), and the two matched controls are proved directly above. A literature audit found the expected signal-processing treatment of boxcar filters and their regularly spaced Dirichlet-kernel zeros, but no additional theorem is load-bearing for the line-specific bow consequence. Accordingly no new source anchor is needed in `SOURCES.md`; the MRSTT and Montgomery--Vaughan anchors already stored there remain the relevant analytic-number-theory context.

The adversarial boundary is important. The constant and root-of-unity vectors are not models of `Lambda-Lambda^sharp`, so they do **not** show that the distinguished bow variance is large, small, or uncontrollable arithmetically. They do not prove sharpness of the MRSTT type-II estimate on its restricted coefficient class, and they do not rule out a diagonal-sensitive theorem exploiting primes, bilinear factorization, or the exact twist. They rule out only an architecture that attempts to manufacture the missing `1/K` from the generic moving-window operator after the source has already been compressed to coefficient magnitudes or `ell^2` size.

For `analytic_frontier`, this converts the qualitative instruction “use arithmetic structure” into an exact norm boundary. The next useful source theorem should expose a **phase-sensitive projection or cancellation statement** for the full residual at the distinguished bow twist, with enough strength to suppress the high-gain box directions by a factor `K`, rather than seek another coefficient-general short-interval inequality. Such a theorem would address the first unsupported step left by `ANF-145`; absent that extra information, the factor-`K` gap is sharp.