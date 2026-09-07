# WI-193 — fixed-shift square-root cancellation has a quarter-scale bow barrier

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-188 reduces the count-saturating Maynard--Pratt bow escape to a height-localized, chirped shifted-von-Mangoldt covariance. WI-189--WI-192 then show that the lattice aliases are genuine, that generic almost-all short-interval information can miss the deterministic alias family, that one B-process reorganizes the phase into the classical Atkinson transform, and that a second pure B-process only undoes that geometry.

There is a further scale barrier before attempting a more elaborate fixed-shift exponential-sum estimate. Let `X=T^(1/2+o(1))` be the count-saturating prime length, let

\[
H=\frac{T^\varepsilon}{\log T},
\qquad 0<\varepsilon<\frac12,
\qquad
K=\frac XH,
\]

and write the central-block source target as in WI-188,

\[
\mathcal S(U;X,H)
:=
\sum_{1\le h\lesssim K}
S_h(U;X),
\qquad
S_h(U;X)
:=
\sum_{m\asymp X}
\Lambda(m)\Lambda(m+h)w(m,h)
 e\!\left(\frac{U}{2\pi}\log\left(1+\frac hm\right)\right),
\tag{1}
\]

where the bounded smooth localizer/source factors are absorbed into `w`. The local Montgomery square needs

\[
\boxed{\mathcal S(U;X,H)=o(X\log X).}
\tag{2}
\]

The exact new point is an information barrier for any route that first proves fixed-shift bounds and then assembles the shifts without exploiting their relative complex phases. Even granting the highly optimistic uniform envelope

\[
\boxed{|S_h(U;X)|\le X^{1/2+o(1)}}
\tag{3}
\]

for every required shift, triangle inequality gives only

\[
|\mathcal S|
\le KX^{1/2+o(1)}
=\frac{X^{3/2+o(1)}}H.
\tag{4}
\]

At `X=T^(1/2+o(1))` and `H=T^epsilon/log T`, the ratio of (4) to the target scale in (2) is

\[
\boxed{
\frac{KX^{1/2+o(1)}}{X\log X}
=T^{1/4-\varepsilon+o(1)}.
}
\tag{5}
\]

Hence **uniform square-root cancellation in every individual shifted-prime sum still cannot certify the bow-local target by shiftwise absolute assembly whenever `epsilon<1/4`**. The endpoint `epsilon=1/4` is logarithm/rate sensitive and is not claimed here. For every fixed `epsilon>1/4`, an actually proved square-root fixed-shift estimate with sufficiently controlled logarithms would be strong enough at the scale level.

More generally, if one has only a uniform fixed-shift saving

\[
|S_h|\le X^{1-\delta+o(1)},
\qquad 0<\delta\le1,
\tag{6}
\]

and then sums shifts absolutely, the resulting source estimate has ratio

\[
\frac{KX^{1-\delta+o(1)}}{X\log X}
=T^{(1-\delta)/2-\varepsilon+o(1)}.
\tag{7}
\]

Thus this architecture can close the bow target only above the exponent threshold

\[
\boxed{\varepsilon>\frac{1-\delta}{2}.}
\tag{8}
\]

To cover arbitrarily small fixed bow exponents by fixed-shift bounds plus triangle inequality, one would need `delta` arbitrarily close to `1`, i.e. individual sums of essentially subpolynomial size. This is far stronger than the natural square-root target and is not what classical one-dimensional phase technology is designed to supply uniformly through a family containing stationary lattice aliases.

The escape is equally sharp. If a theorem could retain square-root scale in `m` **and** gain square-root cancellation across the `K` shifts, then schematically

\[
|\mathcal S|
\le K^{1/2}X^{1/2+o(1)}
=\frac{X^{1+o(1)}}{\sqrt H}
=o(X\log X)
\tag{9}
\]

for every fixed `epsilon>0`. Therefore the missing arithmetic content is not necessarily a miraculous super-square-root estimate for each fixed `h`. A genuinely two-dimensional estimate that saves across the shift family can cross the entire small-bow regime. This identifies the precise direction in which WI-188's source target must be strengthened.

No bound for the actual zeta covariance is proved here and no simple-critical-zero proportion changes. Equation (3) is deliberately a favorable hypothetical input used to prove a negative statement about **how fixed-shift information is assembled**. Actual prime weights may create additional cancellation, and a joint bilinear/dispersion/spectral argument can evade this barrier by never taking absolute values in `h`.

## 1. Exact source normalization

WI-188 starts from the BGSTB prime polynomial

\[
A_2(x,t)
=-\sum_n \frac{\Lambda(n)}{\sqrt n}q_x(n)n^{-it}
\]

and localizes its second moment to a height window centered at `U\asymp T` of length `H`. On the dyadic block `m,n\asymp X`, Fourier localization forces

\[
n=m+h,
\qquad |h|\lesssim K:=\frac XH.
\tag{10}
\]

After pairing positive and negative shifts, the normalized off-diagonal is `2H/X` times a sum of the form (1). Since the diagonal is `asymp H log X`, diagonal dominance reduces exactly to (2). This finding changes none of that arithmetic reduction; it only asks what strength of information about the individual `S_h` could possibly imply (2).

At a count-saturating source-compatible bow, WI-184 and WI-188 give

\[
X=T^{1/2+o(1)},
\qquad
H=\frac{T^\varepsilon}{\log T},
\qquad
K=T^{1/2-\varepsilon+o(1)}\log T.
\tag{11}
\]

The unknown `o(1)` in the reciprocal length does not affect any strict exponent comparison below: whenever `epsilon<1/4` by a fixed margin, the power `T^(1/4-epsilon)` in (5) dominates all `T^o(1)` factors.

## 2. Fixed-shift square-root information is still too weak below one quarter

Assume, only for the purpose of testing the route, that every required shift satisfies (3). This is intentionally much stronger than the positive prime-pair input of WI-188 and should be read as an idealized square-root cancellation envelope for the complete weighted chirped sum, not as a theorem currently available for the von-Mangoldt pair sequence.

There are `K=X/H` shifts. If their relative phases are discarded, then

\[
\left|\sum_{h\lesssim K}S_h\right|
\le
\sum_{h\lesssim K}|S_h|
\le
KX^{1/2+o(1)}.
\tag{12}
\]

Dividing by the required `X log X` scale and using (11),

\[
\begin{aligned}
\frac{KX^{1/2+o(1)}}{X\log X}
&=
\frac{X^{1/2+o(1)}}{H\log X}\\
&=
T^{1/4-\varepsilon+o(1)}.
\end{aligned}
\tag{13}
\]

For every fixed `0<epsilon<1/4`, (13) tends to infinity. Therefore a proof whose final source step consists of **uniform square-root cancellation for each fixed shift plus triangle inequality in the shift variable** still misses the needed local diagonal by a polynomial factor.

The same conclusion survives an average-square fixed-shift theorem if it is consumed only through Cauchy--Schwarz. Suppose one knows the natural square-function estimate

\[
\sum_{h\lesssim K}|S_h|^2
\le KX^{1+o(1)}.
\tag{14}
\]

Then

\[
\left|\sum_hS_h\right|
\le
K^{1/2}\left(\sum_h|S_h|^2\right)^{1/2}
\le
KX^{1/2+o(1)},
\tag{15}
\]

which is exactly the same scale as (12). Thus an `L^2` statement about the **sizes** of the fixed-shift sums is not by itself the cross-shift cancellation needed here. The phases/signs of the `S_h` must remain visible to the estimate.

## 3. General fixed-shift saving law

Write a hypothetical fixed-shift estimate as (6). Then absolute assembly gives

\[
|\mathcal S|
\le
\frac XH X^{1-\delta+o(1)}.
\tag{16}
\]

At the count-saturating scale,

\[
\frac{|\mathcal S|}{X\log X}
\le
T^{(1-\delta)/2-\varepsilon+o(1)}.
\tag{17}
\]

This proves (8). Three cases are worth separating.

For `delta=0`, corresponding to no polynomial cancellation inside a fixed shift, one recovers the `epsilon>1/2` black-box scale obstruction already visible in WI-187--WI-188. For `delta=1/2`, even perfect square-root fixed-shift control lowers the threshold only to `epsilon>1/4`. More generally, every fixed `delta<1` leaves a positive interval of small bow exponents that cannot be reached by this architecture.

This is an **information barrier**, not a lower bound for the true source covariance. The collection of statements `|S_h|<=X^(1-delta+o(1))` contains no relative-phase information, so a formal family with all `S_h` aligned saturates the worst-case scale (16). Any proof that closes (2) below the threshold (8) must use information not present in those individual modulus bounds.

## 4. Joint cancellation is quantitatively sufficient

The previous section also says exactly how to escape. Introduce a cross-shift gain `K^theta` beyond absolute assembly, schematically

\[
\left|\sum_{h\lesssim K}S_h\right|
\le
K^{1-\theta}X^{1/2+o(1)}.
\tag{18}
\]

For `0<epsilon<1/2`, comparison with `X log X` gives the exponent condition

\[
\frac14-\varepsilon
-\theta\left(\frac12-\varepsilon\right)<0.
\tag{19}
\]

Hence, when `epsilon<1/4`, it is enough that

\[
\boxed{
\theta>
\frac{1/4-\varepsilon}{1/2-\varepsilon}.
}
\tag{20}
\]

A full square-root gain in the shift family, `theta=1/2`, gives exponent `-epsilon/2` in (19) and therefore succeeds for **every fixed `epsilon>0`**. Equivalently, the joint square-root scale is

\[
(KX)^{1/2+o(1)}
=
\frac{X^{1+o(1)}}{\sqrt H},
\tag{21}
\]

which is polynomially below `X log X` for every fixed positive bow exponent.

The point is not that (21) should hold automatically. The source phase has the lattice resonances identified in WI-188--WI-191, and the prime coefficients are highly structured. Equation (21) merely quantifies the missing dimensional gain: **the small-bow obstruction disappears once cancellation is proved jointly across the physical shift family instead of one shift at a time**.

## 5. Relation to the A/B-process and Atkinson prior art

The phase in (1) is itself an exact first van-der-Corput difference of the classical logarithmic zeta phase. If

\[
F(m):=\frac{U}{2\pi}\log m,
\]

then

\[
\boxed{
F(m+h)-F(m)
=
\frac{U}{2\pi}\log\left(1+\frac hm\right).
}
\tag{22}
\]

Thus, at the **phase-only** level, the fixed-shift object of WI-188 is already the A-process phase for the classical logarithmic exponential sum. Olivier Robert, *On van der Corput's k-th derivative test for exponential sums*, Indagationes Mathematicae 27:2 (2016), 559--589, DOI `10.1016/j.indag.2015.11.009`, Section 3.3, reviews precisely this Weyl--van-der-Corput A-process for logarithmic phases; Section 4 gives the B-transform used in WI-191--WI-192. Graham--Kolesnik's classical monograph is the broader exponent-pair framework.

That prior art is useful here mainly as a warning against overvaluing a more sophisticated **one-dimensional** phase estimate. WI-191 shows that the first B-transform of (22) is exactly an Atkinson phase after product regrouping, while WI-192 shows that a second pure B-transform only returns to the source chirp. The present scale calculation is orthogonal to those phase identities: even if a one-dimensional fixed-`h` treatment were pushed all the way to the natural square-root scale, discarding the `h` phases afterward still loses a factor large enough to fail for `epsilon<1/4`.

The closest arithmetic prior art remains Matomaki--Radziwill--Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. London Math. Soc. 118 (2019), 284--350, DOI `10.1112/plms.12181`. Their theorem gives Hardy--Littlewood asymptotics for almost all **untwisted** shifts in sufficiently long ranges. As already stressed in WI-034, WI-188 and WI-190, that is not a deterministic estimate for the complex chirped aggregate (1), and the exceptional-set formulation does not control the structured stationary alias locus. The present finding adds a different obstruction: even replacing almost-all control by an ideal uniform square-root **modulus** bound still leaves the small-bow range unresolved if the shifts are then assembled absolutely.

Guth--Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`, is powerful prior art for global large-value distributions of Dirichlet polynomials. Its theorem surface controls how often large values occur and yields zero-density and prime-short-interval consequences; it does not provide the deterministic, one-height two-variable covariance estimate (2). No theorem located in the bounded audit supplies the joint chirped shifted-prime estimate (18) at the count-saturating bow scale. Absence from this search is not evidence of priority.

## 6. Research consequence

WI-188 left three broad arithmetic escape routes: better cancellation inside each shifted-prime sum, cancellation between shifts, or a different source coupling. WI-193 now separates the first two by exponent. **Fixed-shift cancellation, even at square-root strength, is not enough for the full Maynard--Pratt obstruction family if its outputs are combined only through magnitudes.** Below `epsilon=1/4`, the proof must obtain a polynomial amount of cancellation across shifts, prove much stronger-than-square-root individual estimates, or avoid this decomposition.

This materially redirects the post-WI-191/192 program. The natural next target is not another sharper estimate for one Atkinson/fixed-shift fiber in isolation. It is a theorem that keeps the `(h,k)` or `(h,m)` family coupled long enough to exploit relative phase: a bilinear/dispersion estimate, a two-variable stationary transform, an arithmetic large sieve preserving the hyperbolic labels, or a source-specific coefficient decomposition whose final norm sees cancellation across shifts. In the product-grouped WI-191 language, the same requirement is to use the arithmetic fiber information in `B_n` rather than estimate each source fiber independently and sum its modulus.

The falsification rule is now explicit. Any proposed source escape that ends with a bound `|S_h|<=X^(1-delta+o(1))` for each `h` and then takes absolute values over `h` cannot handle bow exponents below `(1-delta)/2`. In particular, a fixed-shift square-root theorem by itself does not close the RH-facing bow obstruction. A joint square-root estimate across the physical shift family would.