# PF-326 — seam normalization preserves fixed-band packet localization

**Status:** `EXACT-DERIVED + FIXED-BAND-ASYMPTOTIC + COORDINATE-BARRIER-NARROWING`.

PF-325 leaves one explicit coordinate ambiguity before its physical packet test can be applied to the shear-deleted direct angle. The translated packets in PF-322--PF-324 are written in raw boundary `L^2`, while the local pant crossing in PF-317 is conjugated by the canonical seam energy. A unit equal-amplitude packet in seam-normalized low coordinates therefore pulls back through `Lambda_Q^{-1/2}` with frequency-dependent amplitudes.

For the canonical shrinking seam this change of amplitudes is asymptotically explicit on every fixed physical band. In the symmetric face-parity channel the pullback multiplier, after removing its common scalar, converges uniformly to `(1+xi^2)^(-1/2)`; in the antisymmetric channel it converges uniformly to `1`. Both are bounded, strictly positive fixed-band multipliers. Since the seam DtN operator is tangentially translation invariant, the pullback still commutes exactly with physical translation. After raw `L^2` renormalization the resulting packet family therefore converges to a nonzero band-limited profile of fixed physical width.

Thus seam normalization can reweight the critical packet, but it cannot spread a fixed-band normalized packet over the full growing cuff or erase physical translation as the packet-position parameter. The remaining coordinate barrier in PF-325 is downstream: the one-cusp-pant crossing, the physical `L/H` projection, and the common positive completion must still be evaluated on this explicitly reweighted packet family.

## Claim

Let `L_n -> infinity` be a canonical cuff length and `w_n -> 0` the adjacent PF-205 seam half-width. Fix a physical cutoff `kappa>0`, put

\[
N_n=\left\lfloor\frac{\kappa L_n}{2\pi}\right\rfloor,
\qquad
\xi_{n,k}=\frac{2\pi k}{L_n},
\qquad
1\le |k|\le N_n,
\]

and let

\[
e_{n,k}(s)=L_n^{-1/2}e^{i\xi_{n,k}s}.
\]

PF-317 gives the flat shifted two-face seam DtN eigenvalues in the symmetric (`+`) and antisymmetric (`-`) face-parity channels:

\[
q_+(\xi,w)=\mu\tanh(\mu w),
\qquad
q_-(\xi,w)=\mu\coth(\mu w),
\qquad
\mu=\sqrt{1+\xi^2}.
\tag{1}
\]

Uniformly for `|xi|<=kappa`, as `w->0`,

\[
q_+(\xi,w)
=\mu^2w\left(1-\frac{\mu^2w^2}{3}+O_\kappa(w^4)\right),
\tag{2}
\]

and

\[
q_-(\xi,w)
=w^{-1}\left(1+\frac{\mu^2w^2}{3}+O_\kappa(w^4)\right).
\tag{3}
\]

Hence

\[
\boxed{
w^{1/2}q_+(\xi,w)^{-1/2}
=\mu^{-1}\bigl(1+O_\kappa(w^2)\bigr),
}
\tag{4}
\]

and

\[
\boxed{
w^{-1/2}q_-(\xi,w)^{-1/2}
=1+O_\kappa(w^2).
}
\tag{5}
\]

PF-317 also gives the two-sided form comparison between the actual hyperbolic seam DtN form and this flat model with relative factor `1+O(w_n^2)`. Because the seam metric is tangentially translation invariant and face-symmetric, Fourier frequency and face parity diagonalize both forms. Therefore the actual hyperbolic parity eigenvalues obey the same fixed-band conclusions (4)--(5), with the `O_kappa(w_n^2)` term changed only by a uniform constant.

Now start with the equal-amplitude translated packet in seam-normalized coordinates,

\[
\psi_{n,t}
=\frac1{\sqrt{2N_n}}
\sum_{1\le |k|\le N_n}
e^{-i\xi_{n,k}t}e_{n,k}.
\tag{6}
\]

In one parity channel its raw-trace pullback through the exact seam normalizer has Fourier weights

\[
a_{n,k}^{\pm}
=q_{n,\pm}(\xi_{n,k})^{-1/2}.
\tag{7}
\]

After raw `L^2` renormalization, common powers of `w_n` cancel. The normalized coefficient weights therefore converge uniformly on the fixed band, up to their common normalization, to

\[
\boxed{
b_+(\xi)=(1+\xi^2)^{-1/2},
\qquad
b_-(\xi)=1.
}
\tag{8}
\]

In particular, neither channel develops a singular or vanishing weight on `[-kappa,kappa]`.

Moreover `Lambda_Q^{-1/2}` is a tangential Fourier multiplier, so for every physical translation `tau_t`,

\[
\boxed{
\Lambda_Q^{-1/2}\tau_t
=\tau_t\Lambda_Q^{-1/2}
}
\tag{9}
\]

exactly. Seam normalization changes packet shape but does not destroy the translation orbit.

Finally let `g_{n,t}^{\pm}` be the raw `L^2`-unit pullback in one parity channel. For every fixed physical offset `x`, after identifying a fixed window around `t` with the real line,

\[
g_{n,t}^{\pm}(t+x)
\longrightarrow
G_\pm(x)
:=\frac{1}{\sqrt{2\pi S_\pm}}
\int_{-\kappa}^{\kappa}
b_\pm(\xi)e^{i\xi x}\,d\xi,
\tag{10}
\]

where

\[
S_\pm=\int_{-\kappa}^{\kappa}|b_\pm(\xi)|^2\,d\xi>0.
\tag{11}
\]

The convergence holds locally in `L^2` as well as pointwise after the harmless omission of the single zero Fourier mode. By Plancherel, `||G_\pm||_{L^2(R)}=1`, and `G_\pm` is nonzero. Consequently there exist constants `R<infinity` and `c>0`, depending only on the fixed cutoff and parity channel, such that for all sufficiently large `n` and every packet center whose `R`-window is interpreted without wrapping,

\[
\boxed{
\int_{|s-t|\le R}|g_{n,t}^{\pm}(s)|^2\,ds\ge c.
}
\tag{12}
\]

Thus the seam-normalized packet retains a fixed positive fraction of its raw-trace mass on a fixed physical window. It cannot become a cuff-scale-delocalized state merely because of `Lambda_Q^{-1/2}`.

## 1. The fixed-band asymptotics are uniform

The only expansion parameter in (2)--(5) is `mu w`. On the retained physical-low band,

\[
1\le\mu\le\sqrt{1+\kappa^2},
\]

so Taylor remainders for `tanh` and `coth` are uniform. The symmetric branch carries the common divergent factor `w^{-1/2}` in `q_+^{-1/2}` and the antisymmetric branch carries the common vanishing factor `w^{1/2}` in `q_-^{-1/2}`. Those factors affect raw amplitudes and energies, but disappear from the **shape** after raw `L^2` normalization.

The surviving symmetric shape multiplier `mu^{-1}` is bounded between `(1+kappa^2)^(-1/2)` and `1`; the antisymmetric multiplier is asymptotically constant. Therefore no fixed-band frequency is preferentially amplified or suppressed by an unbounded factor after the common parity scale is removed.

This conclusion is specific to a fixed absolute cutoff. If the retained band grew like `|xi|~1/w_n`, then `mu w_n` would no longer be uniformly small and equations (4)--(5) would not apply.

## 2. Translation survives exactly, not asymptotically

The localization statement does not require the pant to be translation invariant. It uses only the seam normalizer. Every canonical seam strip is invariant in the tangential cuff coordinate, so its two-face DtN map decomposes into physical Fourier modes. Hence every Borel function of that DtN map, including the inverse square root on the nonconstant retained band, commutes with tangential translation.

For coefficients `a_{n,k}^{\pm}`, the pullback of (6) is therefore

\[
\sum_k a_{n,k}^{\pm}e^{-i\xi_{n,k}t}e_{n,k},
\]

with `t` entering only through Fourier phase. The position variable in PF-325 is still a genuine physical translation parameter after seam normalization; only the reference packet profile has changed.

This matters for the PF-325 identity. One should not replace the normalized packet by the raw equal-amplitude Dirichlet packet, but neither must one abandon the packet-position representation. The correct raw representative is the translated **weighted** packet determined by (7)--(8).

## 3. The weighted packet has a fixed physical limiting profile

After removing the common parity scale and normalizing in raw `L^2`, the coefficient array is a Riemann-sum sampling of the positive continuous function `b_\pm` on the fixed interval `[-kappa,kappa]`. Since the frequency spacing is `2pi/L_n`, the normalized discrete Fourier sum converges on every fixed physical window to (10).

The limiting profile is not a delta function and need not equal the PF-322 Dirichlet kernel. What is load-bearing is that it is a nonzero `L^2(R)` band-limited function at a scale determined only by `kappa`. Choose `R` so that

\[
\int_{-R}^{R}|G_\pm(x)|^2dx>0.
\]

Local `L^2` convergence then gives (12) with a uniform positive lower bound after increasing `n`. This rules out the specific possibility left open in PF-325 that seam-energy normalization alone could smear a critical fixed-band packet over length comparable to the growing cuff.

For a packet initially supported on one seam face rather than a parity eigenchannel, decompose it into symmetric and antisymmetric components. The two parity channels are orthogonal in the two-face boundary space and each obeys the conclusion above. The resulting raw pullback is a vector-valued fixed-scale profile; no cross-parity cancellation can remove its total local two-face `L^2` mass.

## Prior-art and novelty audit

The finite-strip DtN diagonalization and the `tanh/coth` parity eigenvalues are classical separation-of-variables facts already derived explicitly in PF-317. Translation commutation for Fourier multipliers, the fixed-band Taylor expansions, and the Riemann-sum convergence to a band-limited Fourier profile are standard Fourier analysis. A targeted check of the finite-strip DtN/Fourier-multiplier literature found no need to import an additional theorem for this calculation, and no novelty is claimed for those ingredients. `SOURCES.md` therefore needs no new dependency.

The project-specific result is the coordinate conclusion for the live Prime-Flute endpoint: the exact seam-energy normalization singled out by PF-317/PF-325 **does not provide a delocalization escape route** for the critical fixed-band packet test. It replaces the raw equal-amplitude packet by an explicit fixed-band weighted translation orbit and leaves the genuinely geometric suppression question to the pant-side crossing and completion.

## Boundaries and falsification

1. **This is a shape/localization statement, not an angle estimate.** The common factors `w_n^{-1/2}` and `w_n^{1/2}` in the two parity channels are deliberately removed by raw `L^2` normalization. Their effect on the completed response magnitude must be tracked in the intrinsic-angle calculation.
2. **The cutoff must remain fixed in physical frequency.** A band reaching `|xi|~1/w_n` can see nonperturbative `tanh/coth` variation and is outside the claim.
3. **Pant-side completion remains open.** The one-cusp-pant form, physical `L/H` projection, and the positive diagonal completion from PF-320 are not translation invariant and can still suppress, redistribute, or erase the packet response.
4. **No exact PF-322 energy constant is transported.** Equation (12) preserves fixed-scale `L^2` localization, not the exact compactified transverse-energy value of the raw Dirichlet packet.
5. **The missing zero mode is harmless only for the limiting localization claim.** It is one Riemann-sum sample among `Theta(L_n)` retained frequencies; it should not be ignored in identities where constants or parity-zero behavior are load-bearing.
6. **Hyperbolic-versus-flat replacement is only used at fixed band.** PF-317's `1+O(w_n^2)` form comparison supplies the uniform perturbation needed here; no fixed-domain pseudodifferential calculus on collapsing collars is assumed.

## Consequence for the research line

PF-325's packet-position Hilbert--Schmidt diagnostic can now be carried into raw boundary coordinates without an unresolved seam-localization ambiguity. Use the weighted translation families (7)--(8), not the raw equal-amplitude Dirichlet packet, when comparing with the PF-323/PF-324 critical geometry.

The next direct calculation should therefore keep the exact seam multiplier but focus its uncertainty downstream: propagate these fixed-scale weighted packets through the actual one-cusp-pant quotient, physical `L/H` mixed corner, and PF-320 common completion, and evaluate the completed response profile in both PF-324 arithmetic boundary regimes. A difference between those regimes can no longer be dismissed as an artifact of seam normalization spreading the packet over the cuff.