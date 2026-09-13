# PF-322 — physical-low cuff packets retain critical compactified transverse energy

**Status:** `EXACT-DERIVED + PRIME-GEOMETRIC SCALE-COLLISION + DECISIVE-NEGATIVE/PROOF-STRATEGY-OBSTRUCTION + ROUTE-NARROWING`.

PF-321 shows that any fixed superlinear seam-scale decay of the shear-deleted local intrinsic `L/H` angle would already close the reference direct channel in trace class. PF-233 makes such a gain look formally plausible because, after its exact mass conjugation, the diagonal-corridor transverse operator has the scaling `T_{a_n}=s_n^2\widetilde T_n` and the transfer function `F(x)=x/\sinh x` has no linear term at the origin.

That Taylor heuristic is **not uniform on the whole physical-low sector before the projected angle is formed**. The obstruction can be made exact on one lifted cuff cell, without using the constant mode.

Fix a physical frequency cutoff `\kappa>0`. On the `n`th cuff of length `\ell_n`, let

\[
N_n:=\left\lfloor\frac{\kappa\ell_n}{2\pi}\right\rfloor
\]

and, for all sufficiently large `n`, define the normalized zero-mean trigonometric packet

\[
 f_n(\tau)
 :=\frac1{\sqrt{2N_n\ell_n}}
 \sum_{1\le |k|\le N_n}
 \exp\!\left(\frac{2\pi i k}{\ell_n}
 (\tau-\ell_n/2)\right),
 \qquad \tau\in\mathbb R/\ell_n\mathbb Z.
\]

Then `\|f_n\|_{L^2(d\tau)}=1`, its constant Fourier coefficient vanishes, and every frequency satisfies `0<|2\pi k/\ell_n|\le\kappa`. The packet is centered at the cell seam `\tau=\ell_n/2\equiv-\ell_n/2`.

For every fixed `R>0`, if `E_{n,R}` is the circular `R`-neighborhood of that seam, then

\[
\int_{E_{n,R}}|f_n|^2\,d\tau
\longrightarrow
m_{\kappa,R}
:=\int_{-R}^{R}
\frac{\sin^2(\kappa x)}{\pi\kappa x^2}\,dx
>0.
\]

Thus a fixed physical low band contains unit vectors carrying a nonzero asymptotic fraction of their mass in an `O(1)` window at the end of the increasingly long cuff cell.

Now use PF-235's fixed axis compactification

\[
\tau=\log\tan\frac\theta2,
\qquad
\sin\theta=\operatorname{sech}\tau,
\]

and the density-corrected cell transport

\[
y_n(\theta)=\sin(\theta)^{-1/2}f_n(\tau(\theta)).
\]

On the compactified image of one fundamental cell this transport is unitary from physical `L^2(d\tau)` to flat `L^2(d\theta)`. For the PF-231 transverse form

\[
A=-\partial_\theta^2+\csc^2\theta,
\]

the potential term alone gives

\[
\mathfrak a_{n,\mathrm{cell}}[y_n]
\ge
\int_{-\ell_n/2}^{\ell_n/2}
\cosh^2\tau\,|f_n(\tau)|^2\,d\tau.
\]

On `E_{n,R}`, `|\tau|\ge\ell_n/2-R`, hence

\[
\cosh|\tau|
\ge e^{-R}\cosh(\ell_n/2).
\]

PF-001 gives the exact cuff calibration

\[
e^{-\ell_n/2}=\tanh(h_n/4),
\]

which is equivalently

\[
\boxed{\cosh(\ell_n/2)=\coth(h_n/2).}
\]

PF-299 gives the neighboring-pant seam distance

\[
s_n=\frac{h_n+h_{n+1}}2\ge\frac{h_n}{2}.
\]

Therefore

\[
\boxed{
 s_n\cosh(\ell_n/2)
 \ge \frac{h_n}{2}\coth\frac{h_n}{2}>1,
}
\]

and consequently, for every fixed `R>0`,

\[
\boxed{
\liminf_{n\to\infty}
 s_n^2\,\mathfrak a_{n,\mathrm{cell}}[y_n]
\ge e^{-2R}m_{\kappa,R}>0.
}
\]

So the shrinking seam factor `s_n^2` is exactly critical against the fixed compactification on admissible **nonconstant physical-low packets**. The full physical-low cell form is not uniformly `o(1)` after multiplication by `s_n^2`.

PF-233's variable-width diagonal form inherits the same obstruction at the cell-energy level. Its uniform lower form comparison `T_{a_n}\ge c_0s_n^2A`, with `c_0>0` on the canonical tail, implies that the corresponding cell contribution on these packets also has a nonzero lower limit up to the same fixed comparison constant. Thus the issue is not removed by replacing the constant corridor width with the canonical diagonal width.

This is deliberately **not** a lower bound for the shear-deleted intrinsic `L/H` angle. The finite one-cusp-pant quotient, actual seam-energy normalization, physical `L/H` projections, and common positive completion have not been applied. They may cancel precisely the compactification-critical component exhibited here. PF-322 therefore kills only the proof strategy that applies the small-argument expansion of `F(s_n\widetilde T_n^{1/2})` uniformly on the entire retained physical-low sector before those operations.

## Claim

Fix `\kappa>0`. Let `\ell_n` be the canonical prime-flute cuff length, `h_n` the exact logarithmic mesh from PF-001, and `s_n=(h_n+h_{n+1})/2` the canonical neighboring-pant seam distance from PF-299. Then there are unit vectors `f_n` in the **nonconstant** physical Fourier band

\[
0<|\xi|\le\kappa
\]

such that, after density-corrected fixed-axis compactification on one fundamental cuff cell,

\[
\liminf_n s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf_n]>0.
\]

More explicitly, the `f_n` above satisfy, for every fixed `R>0`,

\[
\liminf_n s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf_n]
\ge e^{-2R}m_{\kappa,R},
\]

where `m_{\kappa,R}>0` is the explicit sinc-square mass above.

Hence no argument may infer

\[
\sup_{\substack{f\in P_{\le\kappa}^{\rm phys}\\f\perp1,\ \|f\|=1}}
 s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf]
\longrightarrow0
\]

merely from `s_n\to0`. In particular the formal even Taylor expansion of PF-233's transfer function cannot be used uniformly on the complete physical-low sector at the unprojected compactified-form stage.

## 1. Explicit low-band packet

The Fourier modes `\ell_n^{-1/2}e^{2\pi ik\tau/\ell_n}` are orthonormal on the physical cuff. By construction the packet `f_n` uses exactly `2N_n` nonzero modes with equal coefficients, so it has unit norm, zero mean, and fixed physical bandwidth.

Write `x` for circular distance from the chosen seam center. The numerator is the Dirichlet kernel with its constant term removed:

\[
 f_n(\ell_n/2+x)
 =\frac{D_{N_n}(2\pi x/\ell_n)-1}
 {\sqrt{2N_n\ell_n}}.
\]

PF-299 gives `h_n\to0`, so PF-001 gives `\ell_n\to\infty`; hence `N_n/\ell_n\to\kappa/(2\pi)`. On every fixed bounded `x`-interval,

\[
 f_n(\ell_n/2+x)
 \longrightarrow
 \frac{\sin(\kappa x)}{\sqrt{\pi\kappa}\,x}
\]

with the continuous value `\sqrt{\kappa/\pi}` at `x=0`. Uniform boundedness on fixed windows follows directly from the elementary Dirichlet-kernel formula, so dominated convergence gives the stated local mass limit `m_{\kappa,R}`. Removing the constant mode changes the packet by only one Fourier coefficient and does not affect the limit.

This is the exact version of the concentration warning in the accepted direct-angle clue: no prolate optimization is required. A simple zero-mean Dirichlet packet already has the necessary fixed-window mass.

## 2. Fixed compactification converts the cuff end into the critical weight

PF-235 gives

\[
d\theta=\sin\theta\,d\tau,
\qquad
\sin\theta=\operatorname{sech}\tau.
\]

Therefore the density correction `Uf=\sin^{-1/2}\theta\,f` satisfies

\[
\int|Uf|^2d\theta=\int|f|^2d\tau.
\]

For the potential piece of the PF-231 form,

\[
\int\csc^2\theta|Uf|^2d\theta
=\int\cosh^2\tau|f(\tau)|^2d\tau.
\]

The derivative piece is nonnegative and may be discarded for a lower bound. On a fixed circular window at the cell seam, both representatives near `+\ell_n/2` and `-\ell_n/2` have `|\tau|\ge\ell_n/2-R`, so

\[
\cosh^2\tau
\ge e^{-2R}\cosh^2(\ell_n/2).
\]

Combining this with the packet mass proves

\[
s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf_n]
\ge
 e^{-2R}
 \bigl(s_n\cosh(\ell_n/2)\bigr)^2
 \int_{E_{n,R}}|f_n|^2d\tau.
\]

The remaining coefficient is controlled **exactly**, not asymptotically. If `t=\tanh(h_n/4)=e^{-\ell_n/2}`, then

\[
\cosh(\ell_n/2)
=\frac{t+t^{-1}}2
=\coth(h_n/2).
\]

Since `s_n\ge h_n/2` and `x\coth x>1` for `x>0`, the coefficient is strictly larger than one. Taking the lower limit proves the claim.

## 3. Consequence for the PF-233 Taylor route

PF-233 writes the canonical diagonal width as `a_n=s_nb_n` and proves, uniformly on the tail,

\[
c_0s_n^2A\le T_{a_n}\le C_0s_n^2A.
\]

PF-322 shows why the factor `s_n^2` in this display is not by itself a small parameter on the entire physical-low sector after fixed compactification. The number of allowed low Fourier modes grows like `\ell_n`; that growing dimensionality permits a packet to follow the receding cell end where the compactification weight grows like `\cosh(\ell_n/2)\asymp s_n^{-1}`. The two scales cancel.

Accordingly, the identity

\[
F(x)=1-\frac{x^2}{6}+O(x^4)
\]

remains useful only after one proves that the **projected physical mixed corner** avoids this critical packet, or that seam normalization and the common finite-pant completion cancel it. A uniform estimate on the unprojected low-sector graph norm cannot supply PF-321's superlinear angle bound.

This does not invalidate PF-233's singular-value envelope, PF-318's Hilbert--Schmidt fallback, or PF-321's implication theorem. It identifies exactly where the local PDE proof must earn its cancellation.

## 4. Prior art and novelty audit

Time/band concentration of Fourier-limited functions is classical, with the Slepian--Landau--Pollak theory as the standard stronger optimization framework. No novelty is claimed for that phenomenon, for the Dirichlet kernel, or for the sinc scaling limit used here. The present proof deliberately uses only the elementary equal-coefficient packet, so it imports no external concentration theorem.

The project-specific statement is the scale match with the canonical prime-flute geometry: PF-001's exact cuff identity and PF-299's exact neighboring seam scale turn an ordinary fixed-band packet into the nonvanishing bound above. A structure-directed prior-art check found no external theorem addressing this particular prime-flute compactification/seam cancellation, and no standalone general harmonic-analysis novelty is claimed.

## 5. Boundaries and falsification

1. **Cell form, not completed pant angle.** The theorem concerns the compactified transverse energy contributed by one fundamental lifted cuff cell before the finite-pant quotient/completion is converted into the PF-320 intrinsic angle. It does not prove a lower bound for `T_{0,n}^{(r)}`.
2. **No constant-mode contamination.** The witness has exactly zero mean. PF-215's divergent cuff-constant channel is not being reused.
3. **Fixed physical band.** `\kappa` is fixed as in PF-212. The obstruction comes from the growing number `O(\ell_n)` of Fourier modes inside that fixed physical band, not from increasing the physical cutoff.
4. **Potential term already suffices.** The derivative contribution to the `A` form is nonnegative. Any correction there can only increase the unprojected cell energy; the unresolved cancellation must therefore come later, in projection/normalization/completion rather than by making the raw compactified form small.
5. **Variable width does not remove the cell-energy obstruction.** PF-233's uniform lower form comparison preserves it at this stage. This is still not a statement about the normalized off-diagonal angle.
6. **No conclusion about the conditional channel.** The independent post-low angle `T_H` from PF-315--PF-316 remains untouched.
7. **No RH conclusion.** This finding removes a proof shortcut inside one local operator-ideal gate only.

A refutation would have to break the explicit packet normalization/local limit, the density-corrected compactification identity, PF-001's exact cuff relation, or PF-299's exact seam definition. None of those steps uses a heuristic prime-gap law.

## Consequence for the research line

The accepted direct-angle clue should no longer spend effort asking whether `s_n^2\widetilde T_n` is uniformly small on every retained low mode before projection. PF-322 proves that it is not, already on zero-mean fixed-band packets at the cell-energy level.

The next useful calculation is therefore **strictly downstream of this obstruction**: propagate the explicit seam-centered packet through the actual one-cusp-pant quotient, the PF-205 seam-energy normalization, the physical `L/H` projections, and the common PF-320 completion. If those operations erase the critical component, quantify the surviving mixed angle and test PF-321's `O(s_n^{1+\varepsilon})` target. If they do not, measure the resulting singular-value/Hilbert--Schmidt leakage against PF-318 rather than returning to an unprojected Taylor estimate.