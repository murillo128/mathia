# WI-311 — Smooth frequency multiplexing can flatten the capped tail arbitrarily close to a scalar source shift

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-307, WI-308, WI-309, WI-310.

WI-309 obtained an aperture-independent retained-tail floor by driving one unit-window localizer toward the `L^2` endpoint singularity. WI-310 then showed that the full uncapped tail overcharges the complementary comparison and replaced it by the bounded source-valid cap

\[
\widehat q_B(t)=\min\{(\sigma_1(t)-B)_+,1/2\}.
\]

The remaining presentation made the endpoint-singular localizer look load-bearing for a uniform tail witness. It is not. At every fixed outer aperture one can instead use a **finite family of smooth real unit-window localizers with widely separated carrier frequencies**. The summed localization identity is still exact, the prime-translation reserve can be chosen before the carriers are selected, and the capped retained-tail multiplier can be made arbitrarily close in operator norm to the scalar `1/2 I`.

More precisely, for every fixed outer aperture `L`, every integer `N>=1`, and every `epsilon>0`, there is an explicit finite family of real smooth localizers supported in `(-1/2,1/2)` and a source-valid reserve `B_L` such that

\[
\boxed{
Q=\widehat{\mathcal D}_{L,N,\epsilon}
 +\widehat{\mathcal T}_{L,N,\epsilon},
}
\]

with finite negative index for `Dhat` and

\[
\boxed{
\frac12\left(1-\frac1{2N}-\epsilon\right)I
\preceq
\widehat{\mathcal T}_{L,N,\epsilon}
\preceq \frac12 I.
}
\tag{1}
\]

Consequently

\[
\boxed{
\left\|
\widehat{\mathcal T}_{L,N,\epsilon}-\frac12I
\right\|
\le
\frac1{4N}+\frac\epsilon2,
}
\tag{2}
\]

and therefore

\[
\boxed{
\left\|
\widehat{\mathcal D}_{L,N,\epsilon}
-\left(Q-\frac12I\right)
\right\|
\le
\frac1{4N}+\frac\epsilon2
}
\tag{3}
\]

in the bounded-form sense on the fixed-aperture Weil form domain.

Thus the best possible scalar floor for the cap is not merely uniform: it is asymptotically **saturable** by smooth localization. But this closes the idea that a stronger retained-tail floor, by itself, is progress toward eliminating the finite negative sector. In the saturating regime the capped comparison becomes an arbitrarily small bounded perturbation of the original unknown source shifted by `-1/2 I`. The RH-relevant difficulty has not been reduced; it has merely been repackaged.

The endpoint singularity of WI-309 is therefore one convenient one-window way to prevent the tail floor from collapsing, not a structural necessity. Frequency multiplexing trades that singularity for very large modulation scales. It does **not** provide uniform compact-sector control: derivatives and autocorrelation oscillations of the smooth windows deteriorate with the carrier scale, so the finite-sector problem remains live.

## 1. Multiwindow localization is source-exact

Let `g_1,...,g_J` be real functions supported in `(-1/2,1/2)` satisfying

\[
\sum_{\nu=1}^J\|g_\nu\|_2^2=1.
\tag{4}
\]

For an outer-aperture test `f`, define

\[
f_{\nu,y}(u)=g_\nu(u)f(u+y).
\]

The single-window sliding identity used in WI-307--WI-310 is quadratic in the localizer. For an unnormalized window `g`, direct Fubini gives

\[
\int \|g(\cdot)f(\cdot+y)\|_2^2dy
=\|g\|_2^2\|f\|_2^2,
\]

and every translated source term acquires the autocorrelation

\[
\rho_g(a)=\int g(u+a)g(u)\,du.
\]

Summing over `nu` and using (4) therefore gives the exact same localization identity with aggregate autocorrelation

\[
R(a):=\sum_{\nu=1}^J\rho_{g_\nu}(a):
\]

\[
Q(f)
=
\sum_{\nu=1}^J\int Q(f_{\nu,y})\,dy
-\mathcal E_R(f),
\tag{5}
\]

where the continuous and prime-power localization defects are the WI-307 defects with `1-rho_chi(a)` replaced by `1-R(a)`.

Cauchy--Schwarz and (4) give

\[
|R(a)|
\le
\sum_\nu\|g_\nu(\cdot+a)\|_2\|g_\nu\|_2
\le1.
\tag{6}
\]

Hence every prime-power coefficient

\[
c_n(1-R(\log n))
\]

is nonnegative and at most `2c_n`.

Let

\[
P_L:=\sum_{\log n<2L}c_n,
\qquad
B_L:=2P_L+1.
\tag{7}
\]

The noncompact prime-translation operator of the aggregate comparison therefore obeys

\[
\|A_{L,R}\|
\le2P_L<B_L,
\tag{8}
\]

**independently of the later carrier-frequency choices**. Thus the reserve can be fixed first. This removes a possible circularity in the construction below.

Apply the WI-308 clipping at level `B_L` to every localized source term and then the WI-310 cap. Summing the source identities gives

\[
Q=\widehat{\mathcal D}+\widehat{\mathcal T}.
\tag{9}
\]

For smooth windows the continuous localization defect is again compact on a fixed bounded aperture, and the averaged compact-frequency part is Hilbert--Schmidt. The uncapped reserve-lifted comparison has positive essential spectrum by (8); the capped comparison is larger in form order because it retains less of the positive tail. Hence

\[
n_-(\widehat{\mathcal D})<\infty.
\tag{10}
\]

No endpoint singular localizer is used in (5)--(10).

## 2. Cosine--sine pairs give an interference-free smooth frequency comb

Fix once and for all a real

\[
\phi\in C_c^\infty((-1/2,1/2)),
\qquad
\|\phi\|_2=1,
\]

and write `Phi=F_phi` in the Fourier convention of WI-308.

Choose positive carrier frequencies `omega_1,...,omega_N` and define two real windows per carrier,

\[
g_{j,c}(u)=N^{-1/2}\phi(u)\cos(\omega_j u),
\qquad
 g_{j,s}(u)=N^{-1/2}\phi(u)\sin(\omega_j u).
\tag{11}
\]

They satisfy the normalization (4) **exactly**, since

\[
\sum_{j=1}^N
\bigl(\|g_{j,c}\|_2^2+\|g_{j,s}\|_2^2\bigr)
=
\frac1N\sum_{j=1}^N
\int\phi(u)^2(\cos^2+\sin^2)du
=1.
\tag{12}
\]

The cosine--sine pairing removes Fourier cross-interference exactly. If

\[
W_N(s):=
\sum_{j=1}^N
\left(
|F_{g_{j,c}}(s)|^2+|F_{g_{j,s}}(s)|^2
\right),
\]

then

\[
\boxed{
W_N(s)
=
\frac1{2N}\sum_{j=1}^N
\left(
|\Phi(s-\omega_j)|^2
+|\Phi(s+\omega_j)|^2
\right).
}
\tag{13}
\]

In particular

\[
\frac1{2\pi}\int_\mathbb R W_N(s)\,ds=1.
\tag{14}
\]

The aggregate autocorrelation is just as explicit. Writing

\[
\rho_\phi(a)=\int\phi(u+a)\phi(u)du,
\]

the trigonometric identity

\[
\cos(x+y)\cos x+\sin(x+y)\sin x=\cos y
\]

gives

\[
\boxed{
R_N(a)
=
\frac{\rho_\phi(a)}N
\sum_{j=1}^N\cos(\omega_j a).
}
\tag{15}
\]

Thus `|R_N(a)|<=1`, as required by (6), while the Fourier energy is an exact positive mixture of `2N` translated copies of `|Phi|^2`.

## 3. No interval of the clipped-source width need capture appreciable Fourier mass

Let `T=T_{B_L}` be the explicit exterior radius from WI-309, so that

\[
(\sigma_1(t)-B_L)_+>\frac12
\qquad(|t|>T),
\tag{16}
\]

and therefore

\[
\widehat q_{B_L}(t)=\frac12
\qquad(|t|>T).
\tag{17}
\]

Fix `epsilon>0`. Since `Phi in L^2`, choose `R_0>0` such that

\[
\frac1{2\pi}
\int_{|s|>R_0}|\Phi(s)|^2ds
<\epsilon.
\tag{18}
\]

Now choose the `2N` centers

\[
\{-\omega_N,\ldots,-\omega_1,
\omega_1,\ldots,\omega_N\}
\]

with pairwise separation strictly larger than

\[
2(T+R_0).
\tag{19}
\]

This is always possible because the carrier frequencies are unconstrained finite parameters after `B_L` and `T` have been fixed.

Consider any interval `I` of length `2T`. By (19), `I` can intersect the core interval

\[
[c-R_0,c+R_0]
\]

of at most one carrier center `c`. The corresponding packet has weight `1/(2N)` in (13), so its contribution to the normalized `W_N` mass of `I` is at most `1/(2N)`. For every other packet, `I-c` lies outside `[-R_0,R_0]`, and (18) bounds its contribution by its weight times `epsilon`. Summing yields the uniform interval-concentration estimate

\[
\boxed{
\sup_{|I|=2T}
\frac1{2\pi}\int_I W_N(s)ds
<
\frac1{2N}+\epsilon.
}
\tag{20}
\]

Equivalently, for every translation `xi`,

\[
\frac1{2\pi}
\int_{|t|>T}W_N(t-\xi)dt
>
1-\frac1{2N}-\epsilon.
\tag{21}
\]

This is the precise replacement for the power-law Fourier-tail estimate in WI-309. Instead of forcing one window to retain a fixed fraction of its Fourier mass beyond every translated exterior threshold, a smooth frequency comb distributes the total localization energy over many packets so widely separated that no interval of the forbidden width can catch more than one packet core.

## 4. The capped retained tail becomes almost `1/2 I`

The multiwindow version of the WI-308 Moyal marginal follows by summing the single-window identity:

\[
\widehat{\mathcal T}(f)
=
\frac1{2\pi}
\int_\mathbb R
\widehat r(\xi)|F_f(\xi)|^2d\xi,
\]

where

\[
\widehat r(\xi)
=
\frac1{2\pi}
\int_\mathbb R
\widehat q_{B_L}(t)W_N(t-\xi)dt.
\tag{22}
\]

Since `0<=qhat<=1/2`, (14) gives

\[
\widehat r(\xi)\le\frac12.
\tag{23}
\]

On the exterior region (17), equations (21)--(22) give

\[
\widehat r(\xi)
>
\frac12
\left(1-\frac1{2N}-\epsilon\right)
\qquad\text{for every }\xi.
\tag{24}
\]

Plancherel now proves (1). Since the multiplier is self-adjoint and bounded, (1) immediately implies (2).

Finally, the exact source split (9) gives

\[
\widehat{\mathcal D}
-\left(Q-\frac12I\right)
=
\frac12I-\widehat{\mathcal T},
\tag{25}
\]

so (2) proves (3).

The conclusion can be stated sharply:

\[
\boxed{
\sup_{\text{finite smooth real multiwindow families}}
\inf_\xi\widehat r(\xi)
=rac12,
}
\tag{26}
\]

where the supremum is taken at a fixed aperture with the reserve allowed to satisfy the source-valid gate (8). The upper bound is trivial from the cap; the construction above approaches it arbitrarily closely.

## 5. What this does and does not buy for the finite negative sector

If RH fails and WI-247 supplies a first-crossing vector `v_*` with `Q(v_*)=0`, then (1) forces

\[
\langle v_*,\widehat{\mathcal D}v_*\rangle
\le
-rac12
\left(1-\frac1{2N}-\epsilon\right)
\|v_*\|^2.
\tag{27}
\]

Thus the discrete RH-failure witness can be made arbitrarily close to depth `1/2`, much larger than the one-window constant `1/(64 pi e)` of WI-309--WI-310.

But equation (3) explains why this is **not an RH advance**. In the same limit that makes (27) strong,

\[
\widehat{\mathcal D}
\longrightarrow Q-\frac12I
\]

in bounded perturbation norm at each fixed aperture. Ruling out spectrum of `Dhat` below the corresponding tail floor therefore approaches the original problem of proving `Q>=0` itself. A larger retained-tail gap is not independent information; the complementary comparison tracks the same change exactly.

This gives a decisive falsification test for future variants of the WI-308--WI-310 architecture. If a proposal improves only the scalar retained-tail floor while preserving the identity

\[
Q=D+T,
\]

then one must also show that the new `D` is easier to control for a reason **not equivalent to subtracting a more nearly constant positive operator from `Q`**. Otherwise the stronger witness is purely representational.

The smooth construction also corrects a narrower interpretation of WI-309. An endpoint singularity is not necessary for a uniform retained-tail witness. However, the multiwindow alternative is not uniformly regular in the aperture either. The carrier scale required by (19) lies beyond the already enormous `T_{B_L}`, and derivatives of the windows grow with the carriers. The aggregate autocorrelation (15) becomes rapidly oscillatory. Therefore the norms/Schatten complexity of the compact localization defect are not controlled uniformly by this finding. The degeneration has moved from endpoint regularity to modulation scale; it has not disappeared.

In particular, this finding does **not** prove a uniform bound on `n_-(Dhat)`, does not show `Dhat >= -cI`, and does not prove RH. Its substantive content is a sharp classification of the tail-floor subproblem: the cap floor can be saturated by smooth source-valid localization, so the next theorem must control the finite negative sector using structure that survives the near-scalar shift limit.

## 6. Prior art and novelty audit

The time-frequency ingredients are classical.

- Cordero and Gröchenig, **Time--Frequency analysis of localization operators**, *J. Funct. Anal.* 205 (2003), 107--131, DOI `10.1016/S0022-1236(03)00166-6`, develops localization/anti-Wick operators with time-frequency windows and is relevant background for the multiplier viewpoint.
- Dörfler and Gröchenig, **Time-frequency partitions and characterizations of modulation spaces with localization operators**, *J. Funct. Anal.* 260 (2011), 1903--1924, DOI `10.1016/j.jfa.2010.12.021`, gives classical multiwindow Gabor/localization-operator prior art.
- Balazs, Bastianoni, Cordero, Feichtinger and Schweighofer, **Comparisons between Fourier and STFT multipliers: the smoothing effect of the short-time Fourier transform**, arXiv:2203.01142 / *J. Math. Anal. Appl.* (2024), studies explicitly how a frequency-only STFT symbol becomes a smoothed Fourier multiplier through the window spectrum.
- WI-308 already derives the exact single-window Moyal marginal in the present Fourier normalization, so no convention-dependent identity is imported here.
- WI-207 is Mathia's earlier `multiwindow` result, but it concerns positive Gallagher/source energies for prime sums and proves a dimension-free residue-visibility barrier. It does not use sliding Weil localization, clipped source tails, cosine--sine carrier pairs, or the finite-sector comparison studied here.

The new application-specific deduction is the combination of: the source-exact summed localization identity; the carrier-independent worst-case reserve (7)--(8); the interference-free real cosine--sine packet identity (13); the arbitrary interval anti-concentration (20); and the resulting norm convergence (3) of the capped Weil comparison to `Q-1/2 I`. A targeted literature search located standard multiwindow Gabor/STFT and localization-operator theory but no prior source applying this frequency-multiplexed construction to the clipped Weil-form decomposition or deriving the representation barrier (3). This is a novelty audit, not a priority claim.

## 7. Evidence boundary and next gate

Every estimate in the finding is exact apart from the freely chosen `epsilon`, which comes only from the `L^2` Fourier tail of the fixed smooth base window. No zeta-zero statistics, RH hypothesis, numerical certificate, or unproved arithmetic estimate enters the construction. The only zeta-specific inputs are the source identity and large-frequency clipping inequality already audited in WI-307--WI-310.

The immediate research consequence is negative but useful: **do not spend further effort optimizing the capped-tail scalar floor.** It can already be driven arbitrarily close to its absolute maximum `1/2` without singular windows, and doing so drives the comparison toward a scalar shift of the original Weil source.

The live target remains source-specific control of the finite negative sector, but a successful control must now demonstrate a quantity that is not invariantly lost in the near-scalar-tail limit. Plausible load-bearing candidates are correlations between the compact sector and the prime-translation operator, first-crossing eigenfunction constraints, signed-density information from WI-241, or a source-derived finite-dimensional Schur/Birman--Schwinger quantity whose bound does not collapse to `Q>=0` under (3).