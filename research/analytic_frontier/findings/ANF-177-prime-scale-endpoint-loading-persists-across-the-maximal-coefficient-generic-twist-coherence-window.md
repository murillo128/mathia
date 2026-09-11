# ANF-177 — Prime-scale endpoint loading persists across the maximal coefficient-generic twist-coherence window

**Status:** `LITERATURE+DERIVED + MATCHED-CONTROL + LOCAL-TWIST-UNCERTAINTY + SHARP-COEFFICIENT-GENERIC-BARRIER`. `ANF-175` constructs a prime-scale packet which stores the critical endpoint charge

\[
a_X:=\sqrt{\delta X\log X}
\]

at the distinguished logarithmic twist `U`, using atoms of size `log X` on candidate sites separated by `log X`. `ANF-176` then shows that relative long-interval estimates cannot detect that packet until their absolute error crosses the `a_X` scale. A remaining possible escape is that the carrier-aligned packet might be an essentially pointwise-in-`U` pathology which disappears after even a modest local average in the twist variable.

It does not. The same `ANF-175` packet remains of size `Omega(a_X)` throughout a twist interval of width

\[
\boxed{W_X\asymp \frac{X}{a_X}\asymp\sqrt{\frac{X}{\log X}}.}
\]

Consequently its local twist mean square is `Omega(X a_X)`. On exactly that window, the classical Montgomery--Vaughan separated-frequency mean-value bound gives only `O(X a_X)` from the packet's coefficient `l^2` norm and its `log X` site spacing. Thus the dangerous packet matches the coefficient-generic Dirichlet-polynomial envelope up to constants. A local twist average cannot rule it out using only support span, site separation, and coefficient norms; a useful mean-square theorem at this scale must save arithmetically below the Montgomery--Vaughan envelope.

This is distinct from `ANF-144`. There the moving bow variance returns to its diagonal after averaging over `omega(X)` twist windows, and adjacent coefficients show that the coefficient-general `X` scale is sharp. Here the object is the **prime-scale endpoint loading packet itself**. Its physical span is only `Theta(a_X)`, its minimum site spacing is `Theta(log X)`, and its dangerous charge is provably stable on the much smaller dual window `X/a_X`; the corresponding `q`-separated mean-value envelope is already saturated there. The exact distinguished twist is therefore not the only issue: the matched obstruction has a power-sized neighborhood in twist space.

## 1. The prime-scale packet has matched `l^1`, `l^2`, span, and spacing scales

Use the packet from `ANF-175`. Fix `0<delta<1`, put

\[
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\qquad
a_X:=\sqrt{\delta X\log X},
\tag{1}
\]

and choose

\[
N:=\left\lceil\frac{4\sqrt3\,a_X}{A_X}\right\rceil,
\qquad
j_m:=m q_X,
\qquad 1\le m\le N.
\tag{2}
\]

At the distinguished twist `U`, partition the carrier rays

\[
v_j:=(X+j)^{-iU}
\tag{3}
\]

into six sectors of angular width `pi/3`, and retain a sector containing at least `N/6` candidate sites. Call its active set `S`. Define

\[
P_X(t):=A_X\sum_{j\in S}(X+j)^{-it}.
\tag{4}
\]

The sector argument of `ANF-175` gives

\[
\boxed{|P_X(U)|\ge a_X.}
\tag{5}
\]

Write

\[
M_X:=\sum_{j\in S}A_X=A_X|S|,
\qquad
Q_X:=\sum_{j\in S}A_X^2=A_X^2|S|.
\tag{6}
\]

Since `N/6<=|S|<=N`, equations (1)--(2) imply

\[
\boxed{M_X\asymp a_X,\qquad Q_X\asymp a_X\log X.}
\tag{7}
\]

The full candidate span is

\[
L_X:=Nq_X\asymp a_X,
\tag{8}
\]

and every two active indices differ by at least `q_X`. Thus the packet simultaneously has prime-sized atoms, prime-sized candidate spacing, total mass `Theta(a_X)`, quadratic mass `Theta(a_X log X)`, and physical diameter `Theta(a_X)`.

## 2. Any target-sized charge persists for `Theta(X/a_X)` in the twist variable

Let `tau` be real. After removing the irrelevant common phase `X^{-i tau}`,

\[
e^{i\tau\log X}P_X(U+\tau)
=A_X\sum_{j\in S}v_j
\exp\!\left(-i\tau\log\left(1+\frac jX\right)\right).
\tag{9}
\]

Subtracting `P_X(U)` and using `|e^{-iy}-1|<=|y|` gives

\[
\left|
e^{i\tau\log X}P_X(U+\tau)-P_X(U)
\right|
\le
M_X|\tau|\log\left(1+\frac{L_X}{X}\right)
\le
M_X|\tau|\frac{L_X}{X}.
\tag{10}
\]

Because `M_X,L_Xasymp a_X`, choose a fixed sufficiently small constant `c_delta>0` and set

\[
W_X:=c_\delta\frac{X}{a_X}.
\tag{11}
\]

Then (10), uniformly for `|tau|<=W_X`, is at most `a_X/2` for all sufficiently large `X`. Combining with (5),

\[
\boxed{
|P_X(U+\tau)|\ge\frac{a_X}{2}
\qquad(|\tau|\le W_X).
}
\tag{12}
\]

Therefore the carrier-sector obstruction is not concentrated at one twist. Since

\[
\frac{X}{a_X}
=\delta^{-1/2}\sqrt{\frac{X}{\log X}},
\tag{13}
\]

it survives on a twist interval whose width tends to infinity by a power of `X`.

Integrating (12) yields the deterministic lower bound

\[
\boxed{
\int_{U-W_X}^{U+W_X}|P_X(t)|^2\,dt
\gg_\delta W_Xa_X^2
\asymp_\delta Xa_X.
}
\tag{14}
\]

This lower bound uses only the already-persisted packet geometry. It does not invoke a distributional statement about the physical prime-minus-rough residual.

## 3. Montgomery--Vaughan gives exactly the same scale from spacing and `l^2` mass

The frequencies of `P_X` are

\[
\lambda_j:=\log(X+j),\qquad j\in S.
\tag{15}
\]

For distinct active indices, `|j-k|>=q_X`. Since `L_X=o(X)`, the mean-value theorem gives, uniformly for large `X`,

\[
|\lambda_j-\lambda_k|
=\left|\log\frac{X+j}{X+k}\right|
\gg\frac{|j-k|}{X}
\ge c\frac{q_X}{X}.
\tag{16}
\]

Hence the minimum logarithmic frequency spacing satisfies

\[
\Delta_X^{-1}\ll\frac{X}{q_X}.
\tag{17}
\]

The classical Montgomery--Vaughan Hilbert inequality, equivalently the standard mean-value theorem for separated exponential frequencies, therefore gives for every center `T` and every `W>0`

\[
\int_{T-W}^{T+W}|P_X(t)|^2\,dt
\ll
\left(W+\frac{X}{q_X}\right)Q_X.
\tag{18}
\]

At the coherence width (11), one has `W_Xasymp X/a_X`, while `a_X/log Xtoinfinity`, so

\[
W_X=o\!\left(\frac{X}{q_X}\right).
\tag{19}
\]

Using (7), (17)--(19),

\[
\boxed{
\int_{U-W_X}^{U+W_X}|P_X(t)|^2\,dt
\ll
\frac{X}{\log X}\,a_X\log X
\ll Xa_X.
}
\tag{20}
\]

Equations (14) and (20) match up to constants:

\[
\boxed{
\int_{U-W_X}^{U+W_X}|P_X(t)|^2\,dt
\asymp_\delta Xa_X.
}
\tag{21}
\]

Thus the matched packet reaches the full order of the **coarse `q_X`-separated Montgomery--Vaughan envelope** at the natural twist-coherence scale. This does not claim equality in the sharp frequency-by-frequency Hilbert constant, nor that every `q_X`-separated set is extremal. It says that no estimate which retains only the guaranteed site separation `q_Xasymp log X` and the quadratic coefficient mass `Q_Xasymp a_X log X` can improve (18) by an asymptotic factor on this class: the explicit packet already supplies the matching lower bound.

## 4. There are two different dual scales, and the dangerous packet lives far below orthogonality

The physical loading span and the candidate spacing induce two distinct twist scales. The first is the coherence width

\[
W_{\rm coh}
\asymp\frac{X}{L_X}
\asymp\frac{X}{a_X}
\asymp\sqrt{\frac{X}{\log X}},
\tag{22}
\]

on which a target-sized value cannot change substantially by the elementary Lipschitz estimate (10). The second is the spacing-resolution scale

\[
W_{\rm orth}
\asymp\frac{X}{q_X}
\asymp\frac{X}{\log X},
\tag{23}
\]

at which the generic separated-frequency mean value begins to resolve neighboring candidate frequencies individually.

Their ratio is

\[
\boxed{
\frac{W_{\rm orth}}{W_{\rm coh}}
\asymp
\frac{L_X}{q_X}
\asymp
\frac{a_X}{\log X}
\asymp
\sqrt{\frac{X}{\log X}}.
}
\tag{24}
\]

This is, up to constants, the number of candidate sites in the loading packet. The dangerous endpoint alignment therefore occupies a broad twist neighborhood while remaining far inside the non-orthogonal regime of its prime-scale frequency comb.

This also explains why `ANF-144` does not remove the present obstruction. The `omega(X)` averaging there concerns the full moving variance with arbitrary adjacent integer frequencies. Restricting to a prime-scale packet improves its guaranteed frequency spacing from `1/X` to `log X/X`, hence the generic diagonalization scale to `X/log X`; but the endpoint charge already persists on the much smaller scale `sqrt(X/log X)`, and its local `L^2` mass at that scale is exactly as large as coefficient-generic mean-value theory permits.

## 5. Consequence: local twist averaging is useful only with an arithmetic saving

A natural response to the activation-saving barrier of `ANF-176` is to replace pointwise control at the distinguished twist by a local twist mean square, hoping that an isolated carrier-sector alignment is washed out. Equations (12)--(21) show the precise limitation of that strategy.

For the prime-scale matched control, any theorem of the form

\[
\int_{U-W_X}^{U+W_X}|P_X(t)|^2dt
=o(Xa_X)
\tag{25}
\]

would indeed rule out the dangerous charge (5), because elementary phase continuity alone forces the lower bound (14). But (25) is **strictly stronger than coefficient-generic mean-value theory**: Montgomery--Vaughan gives only `O(Xa_X)`, and the matched packet attains that order.

Accordingly, local twist averaging creates a valid alternative interface only if the source contributes a genuine arithmetic saving below the generic separated-frequency envelope. Such a theorem would have to use the actual prime/rough placement or cancellation law, not merely the facts that the coefficients are prime-sized, lie on a `log X`-spaced support, and have the correct `l^1/l^2` scales. Without that additional input, replacing a pointwise distinguished-twist problem by a `sqrt(X/log X)`-wide local average does not cross the information boundary found in `ANF-175`--`ANF-176`.

The result does not assert that the physical residual realizes the matched sector selection, nor that an `o(Xa_X)` local-twist mean square is impossible for that residual. On the contrary, (25) is now a concrete source-specific target. It also does not say that averaging on much wider windows is useless; wider averaging can diagonalize the packet, but by itself it no longer recovers the pointwise endpoint charge at `U`. Any passage back to the distinguished twist must pay exactly the local coherence issue quantified above.

## 6. Prior-art and novelty audit

The mean-value input is classical. Montgomery and Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8:1 (1974), 73--82, supplies the generalized Hilbert inequality behind (18); the same source already anchors `ANF-144` and is recorded in `SOURCES.md`. The surrounding large-sieve principle for separated frequencies is likewise classical. The pointwise persistence estimate (10) is elementary and is a direct frequency-diameter uncertainty calculation, not a new harmonic-analysis theorem.

The Mathia-specific delta is the specialization to the source-matched endpoint packet of `ANF-175`: its critical charge, prime-scale spacing, coefficient norms, and physical loading span combine so that the forced local lower bound (14) and the classical separated-frequency upper envelope (20) coincide at `Xa_X`. A targeted literature audit found no source theorem that converts the current prime/rough information into an asymptotic saving below that local envelope at the distinguished `Uasymp X^2` scale. No new literature dependency is therefore needed.

## Verdict

The prime-scale endpoint obstruction is robust in the twist variable. A carrier-selected charge of size `sqrt(X log X)` assembled on the sharp `sqrt(X log X)` physical loading scale remains target-sized throughout a twist window of width `sqrt(X/log X)`. On that same window its mean square has order `X sqrt(X log X)`, exactly the order allowed by the classical Montgomery--Vaughan estimate using only the packet's `log X` spacing and `l^2` mass.

So local twist averaging does not provide a coefficient-generic escape from the endpoint-memory barrier. It does, however, expose a new source-faithful quantitative target: prove an arithmetic `o(Xa_X)` local-twist mean square on the `X/a_X` window, or return to direct control of the signed dyadic / Fejer scale-slope statistic. Either route must use information about actual prime/rough placement that the matched packet deliberately discards.