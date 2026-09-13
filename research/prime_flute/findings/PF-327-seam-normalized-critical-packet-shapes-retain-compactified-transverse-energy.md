# PF-327 — seam-normalized critical packet shapes retain compactified transverse energy

**Status:** `EXACT-DERIVED + FIXED-BAND-ASYMPTOTIC + COORDINATE-BARRIER-NARROWING`.

PF-326 proves that the exact PF-205 seam-energy normalization does not delocalize a fixed physical-band packet over the growing cuff. After removing the common parity scale and normalizing in raw boundary `L^2`, the pulled-back packet remains a translated fixed-width profile whose Fourier multiplier converges uniformly to

\[
b_+(\xi)=(1+\xi^2)^{-1/2},
\qquad
b_-(\xi)=1
\]

on every fixed physical band. PF-326 deliberately leaves open whether this frequency reweighting could nevertheless destroy the **compactification-critical transverse energy** exhibited by PF-322--PF-323.

It cannot. Center the exact seam-normalized pullback at PF-323's intrinsic critical point

\[
s_n\cosh\tau_{n,\lambda}=\lambda,
\qquad 0<\lambda<1.
\]

For either seam face-parity channel, the raw-`L^2` unit packet converges locally to the nonzero band-limited profile `G_\pm` from PF-326, while PF-323 gives

\[
s_n^2\cosh^2(\tau_{n,\lambda}+x)
\longrightarrow
\lambda^2e^{2x}
\]

uniformly on every fixed bounded `x`-window. Therefore every fixed interior window carries a strictly positive limiting fraction of the scaled Pöschl--Teller potential energy:

\[
\boxed{
\lim_{n\to\infty}
 s_n^2
 \int_{|\tau-\tau_{n,\lambda}|\le R}
 \cosh^2\tau\,
 |g_{n,\lambda}^{\pm}(\tau)|^2\,d\tau
 =
 \lambda^2
 \int_{-R}^{R}e^{2x}|G_\pm(x)|^2\,dx
 >0
}
\]

for every fixed `0<R<\log(1/\lambda)`.

The derivative part of PF-323's exact compactified `A=-\partial_\theta^2+\csc^2\theta` form is nonnegative, so the full scaled `A` energy has the same positive lower bound. PF-233's uniform comparison

\[
T_{a_n}\ge c_0s_n^2A
\]

then transfers a positive order-one lower bound to the canonical variable-width diagonal corridor at the same **unprojected transverse-form stage**.

Thus seam normalization removes neither the physical localization nor the compactification-critical energy of the fixed-band witness after shape normalization. The remaining possibility of superlinear decay in the PF-320 intrinsic local angle must be created downstream by the one-cusp-pant crossing, the physical `L/H` projection, the common positive completion, and the final intrinsic diagonal normalization. This finding still does **not** prove a lower bound for that completed angle.

## Claim

Fix a physical cutoff `\kappa>0`, choose `0<\lambda<1`, and choose

\[
0<R<\log(1/\lambda).
\]

Let `s_n`, `\ell_n`, and `\tau_{n,\lambda}` be the canonical quantities of PF-323, with

\[
s_n\cosh\tau_{n,\lambda}=\lambda.
\tag{1}
\]

Let `N_n=\lfloor\kappa\ell_n/(2\pi)\rfloor`, and start in one seam face-parity channel with PF-325's equal-amplitude unit packet in the exact seam-normalized low Hilbert coordinates, centered at `t=\tau_{n,\lambda}`. Pull it back through the exact seam normalizer `\Lambda_Q^{-1/2}` and normalize the resulting boundary trace to unit raw `L^2`. Denote that packet by

\[
g_{n,\lambda}^{\sigma},
\qquad \sigma\in\{+,-\}.
\tag{2}
\]

PF-326 gives the locally `L^2` convergent fixed-window limits

\[
g_{n,\lambda}^{\sigma}(\tau_{n,\lambda}+x)
\longrightarrow
G_\sigma(x),
\tag{3}
\]

where

\[
G_\sigma(x)
=\frac1{\sqrt{2\pi S_\sigma}}
\int_{-\kappa}^{\kappa}b_\sigma(\xi)e^{i\xi x}\,d\xi,
\qquad
S_\sigma=\int_{-\kappa}^{\kappa}|b_\sigma(\xi)|^2d\xi,
\tag{4}
\]

with

\[
b_+(\xi)=(1+\xi^2)^{-1/2},
\qquad
b_-(\xi)=1.
\tag{5}
\]

Then:

1. for every fixed `R` as above,
   \[
   \boxed{
   \lim_{n\to\infty}
   s_n^2
   \int_{|\tau-\tau_{n,\lambda}|\le R}
   \cosh^2\tau\,
   |g_{n,\lambda}^{\sigma}(\tau)|^2d\tau
   =c_{\sigma,\kappa,\lambda,R}>0,
   }
   \tag{6}
   \]
   where
   \[
   \boxed{
   c_{\sigma,\kappa,\lambda,R}
   =\lambda^2
   \int_{-R}^{R}e^{2x}|G_\sigma(x)|^2dx;
   }
   \tag{7}
   \]
2. if `U` is PF-235's density-corrected compactification, then PF-323's exact physical-coordinate formula gives
   \[
   \boxed{
   \liminf_{n\to\infty}
   s_n^2\,\mathfrak a_{n,\mathrm{cell}}[Ug_{n,\lambda}^{\sigma}]
   \ge c_{\sigma,\kappa,\lambda,R}>0;
   }
   \tag{8}
   \]
3. for the canonical PF-233 variable-width diagonal transverse operator `T_{a_n}` one consequently has
   \[
   \boxed{
   \liminf_{n\to\infty}
   \langle Ug_{n,\lambda}^{\sigma},
   T_{a_n}Ug_{n,\lambda}^{\sigma}\rangle
   \ge c_0c_{\sigma,\kappa,\lambda,R}>0,
   }
   \tag{9}
   \]
   with the uniform comparison constant `c_0>0` from PF-233.

Equations (6)--(9) concern the **raw-`L^2` normalized packet shape after exact seam pullback**. They deliberately remove the common parity-dependent seam scalar in order to test whether the normalization changes the packet's critical geometry. They do not assert that those common scalars disappear from the final intrinsic-angle magnitude.

## 1. PF-326 gives a nonzero fixed-scale limit after seam normalization

On the retained physical band `|\xi|\le\kappa`, PF-326 proves that after removal of the common parity scale the exact seam-pullback coefficients converge uniformly to (5). Both limiting weights are continuous, positive, and bounded above and below on the fixed band. Their normalized Fourier transforms `G_\sigma` are therefore nonzero band-limited functions.

More concretely,

\[
G_\sigma(0)
=\frac1{\sqrt{2\pi S_\sigma}}
\int_{-\kappa}^{\kappa}b_\sigma(\xi)d\xi
>0.
\tag{10}
\]

Hence for every `R>0`,

\[
\int_{-R}^{R}e^{2x}|G_\sigma(x)|^2dx>0.
\tag{11}
\]

PF-326 proves local `L^2` convergence of the exact hyperbolic-seam pullbacks, not merely of the flat model. No further replacement of the actual seam energy is required here.

## 2. The critical compactification coefficient converges uniformly on the same window

PF-323 gives the exact identity

\[
s_n\cosh(\tau_{n,\lambda}+x)
=\lambda\cosh x
+\sqrt{\lambda^2-s_n^2}\,\sinh x.
\tag{12}
\]

Therefore, uniformly for `|x|\le R`,

\[
s_n^2\cosh^2(\tau_{n,\lambda}+x)
\longrightarrow
\lambda^2e^{2x}.
\tag{13}
\]

The restriction `R<\log(1/\lambda)` guarantees by PF-323 that this whole window lies strictly inside the cuff cell for all sufficiently large `n`. Thus the limit is obtained before the outgoing quotient seam is encountered and is independent of whether PF-324 places that seam at finite or escaping distance farther to the right.

## 3. Local `L^2` convergence is enough to pass the weighted energy

Put

\[
f_n(x)=g_{n,\lambda}^{\sigma}(\tau_{n,\lambda}+x),
\qquad
f(x)=G_\sigma(x),
\tag{14}
\]

and

\[
c_n(x)=s_n^2\cosh^2(\tau_{n,\lambda}+x).
\tag{15}
\]

PF-326 gives `f_n\to f` in `L^2([-R,R])`. Hence

\[
\||f_n|^2-|f|^2\|_{L^1([-R,R])}
\le
\|f_n-f\|_2(\|f_n\|_2+\|f\|_2)
\longrightarrow0.
\tag{16}
\]

By (13), `c_n\to\lambda^2e^{2x}` uniformly and the sequence `c_n` is uniformly bounded on the fixed window. Therefore

\[
\int_{-R}^{R}c_n(x)|f_n(x)|^2dx
\longrightarrow
\lambda^2\int_{-R}^{R}e^{2x}|G_\sigma(x)|^2dx,
\tag{17}
\]

which proves (6)--(7).

This step is the entire new bridge. PF-326 supplied the correct seam-normalized packet profile; PF-323 supplied the exact critical compactification coefficient. Their limits live in the same physical coordinate and therefore combine without any additional pseudodifferential or semiclassical approximation.

## 4. The potential term already forces an order-one transverse-form floor

PF-323 records the exact compactified cell form

\[
\mathfrak a[Uf]
=\int
\cosh^2\tau
\left(
\left|f'(\tau)+\frac12\tanh\tau\,f(\tau)\right|^2
+|f(\tau)|^2
\right)d\tau.
\tag{18}
\]

The first term is nonnegative. Restricting only the second term to the fixed critical window and applying (6) gives (8). No derivative convergence of the seam-normalized packet is needed.

PF-233 then gives the uniform form inequality

\[
T_{a_n}\ge c_0s_n^2A.
\tag{19}
\]

Applying it to the compactified packet `Ug_{n,\lambda}^{\sigma}` and using (8) proves (9). Thus the canonical variable-width diagonal corridor also retains a compactification-critical fixed-band witness at the unprojected form level.

This sharpens the interpretation of PF-322--PF-326. The failure of a uniform small-argument treatment is not repaired by using the **correct seam-energy coordinates**. Seam normalization changes the fixed-band packet by a bounded nonvanishing Fourier weight, but that weight cannot suppress the critical physical window once the packet shape is normalized.

## 5. Consequence for the accepted direct-angle clue

PF-327 removes one remaining coordinate-level escape route from the accepted direct-angle clue. The next calculation no longer has to ask whether the PF-323 critical family was an artifact of writing packets in raw boundary `L^2` rather than seam-energy coordinates. After the exact pullback, a shape-normalized packet still carries a positive order-one `s_n^2A` contribution and a positive order-one PF-233 diagonal-corridor transverse energy.

The unresolved operations are therefore genuinely downstream:

- the exact one-cusp-pant crossing from the seam boundary into the pant core;
- the physical `L/H` projection;
- the common positive finite-pant/cusp-side completion retained by PF-320;
- the final intrinsic diagonal normalization defining the local angle.

PF-324's two arithmetic boundary regimes remain useful because the same pre-pant critical packet now survives seam normalization in both. If the completed response differs between finite-boundary and escaping-boundary subsequences, that difference cannot be blamed on seam normalization erasing the critical packet before it reaches the pant-side problem.

## Prior-art and novelty audit

No standalone novelty is claimed for the analytic ingredients. Local `L^2` convergence implying `L^1` convergence of squared magnitudes, uniform convergence of bounded weights, positivity of the Pöschl--Teller potential term, and Fourier transforms of compactly supported frequency weights are standard analysis. PF-323 and PF-326 already derive the project-specific geometric and seam-normalization inputs used here.

A targeted literature check around hyperbolic Dirichlet-to-Neumann maps, the boundary-Laplacian correspondence, Pöschl--Teller compactification, and band-limited Fourier concentration found only the expected general background; no external theorem is needed for (6)--(9), and no source was found whose content is this prime-flute critical-window composition. `SOURCES.md` therefore requires no new dependency.

The project-specific result is the exact synthesis of two previously separate barriers: the PF-323 critical compactification scale and the PF-326 exact seam-normalized packet shape. It establishes that **coordinate-correct seam normalization does not remove the critical transverse-energy witness**.

## Boundaries and falsification

1. **Shape-normalized statement.** PF-326 removes a common parity-dependent seam scalar before raw-`L^2` normalization. PF-327 proves that the resulting shape remains compactification-critical. It does not claim that the common scalar is irrelevant to the final intrinsic response magnitude.
2. **Still pre-angle.** Equations (8)--(9) are unprojected transverse-form lower bounds. They do not imply a lower bound for `T_{0,n}^{(r)}`, `K_{LH}`, or the completed PF-320 direct angle.
3. **Fixed physical bandwidth.** `\kappa`, `\lambda`, and `R` are fixed before taking the tail. A band growing with `1/w_n` is outside PF-326 and therefore outside this finding.
4. **Interior window only.** The proof deliberately uses `R<\log(1/\lambda)` so the positive contribution is separated from the quotient seam. It does not require compact support of the packet outside that window.
5. **No exact PF-322 constant is recovered.** The limiting profile is `G_\sigma`, not the raw Dirichlet kernel. The conclusion is a strictly positive critical-energy floor, not equality with PF-322's earlier constant.
6. **Completion may still suppress the angle.** A positive unprojected energy floor can coexist with a small low/high correlation after the pant crossing and intrinsic diagonal normalization. PF-320's superlinear-angle route remains open.
7. **No new arithmetic invariant.** The result holds before PF-324's outgoing seam position matters. It does not establish recovery of the prime-gap ratio by a spectral or scattering invariant.
8. **No RH conclusion.** This only narrows one local operator-ideal gate inside Prime Flute.

A refutation would have to break PF-326's local `L^2` packet limit, PF-323's exact critical coefficient, or the elementary passage (16)--(17).

## Consequence for the research line

The accepted direct-angle calculation should now begin **after** seam-normalization criticality has been established. Use the exact PF-326 weighted packet family at PF-323's critical centers, retaining the common seam-scale amplitudes, and propagate it through the real one-cusp-pant crossing, physical `L/H` split, common positive completion, and intrinsic angle normalization. PF-327 shows that any eventual superlinear seam gain cannot come from seam normalization merely smoothing or energetically diluting the fixed-band critical packet; it must be generated by those downstream pant-side operations.