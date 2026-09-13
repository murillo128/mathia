# PF-323 — compactification-critical physical-low packets can be recentered strictly inside each cuff cell

**Status:** `EXACT-DERIVED + PRIME-GEOMETRIC INTERIOR SCALE-COLLISION + ROUTE-NARROWING`.

PF-322 proves that the fixed physical-low sector is not uniformly small for the compactified transverse form after multiplication by the shrinking pant scale `s_n^2`: a zero-mean Dirichlet packet centered at the end of the increasingly long cuff cell retains order-one scaled Pöschl--Teller energy. That leaves one avoidable ambiguity in the adversarial interpretation. The PF-322 packet is centered exactly at the cell seam, so one could still wonder whether its critical energy is inseparable from the endpoint identification used to form the finite cuff/pant quotient.

It is not. The scale collision can be placed on a **fixed physical window strictly inside the cuff cell**, while keeping the packet entirely in the same nonconstant fixed physical Fourier band.

Fix `0<lambda<1`. On the canonical tail there is a unique point

\[
\tau_{n,\lambda}\in(0,\ell_n/2)
\]

satisfying

\[
\boxed{s_n\cosh\tau_{n,\lambda}=\lambda.}
\]

This follows only from `s_n\to0` and PF-322's exact endpoint inequality

\[
s_n\cosh(\ell_n/2)>1.
\]

Moreover the critical point stays a fixed positive distance from the seam:

\[
\boxed{
\frac{\ell_n}{2}-\tau_{n,\lambda}>\log\frac1\lambda.
}
\]

Hence, for every fixed

\[
0<R<\log(1/\lambda),
\]

the interval `|tau-tau_{n,lambda}|<=R` lies strictly inside the positive half-cell for all sufficiently large `n`.

Center the same zero-mean fixed-band Dirichlet packet used in PF-322 at this interior point:

\[
f_{n,\lambda}(\tau)
:=\frac1{\sqrt{2N_n\ell_n}}
\sum_{1\le |k|\le N_n}
\exp\!\left(
\frac{2\pi i k}{\ell_n}
(\tau-\tau_{n,\lambda})
\right),
\qquad
N_n=\left\lfloor\frac{\kappa\ell_n}{2\pi}\right\rfloor .
\]

Then `||f_{n,lambda}||_2=1`, its constant Fourier coefficient is zero, and all frequencies obey `0<|xi|<=kappa`. On the fixed interior coordinate `x=tau-tau_{n,lambda}` one has the exact identity

\[
\boxed{
 s_n\cosh(\tau_{n,\lambda}+x)
 =\lambda\cosh x
 +\sqrt{\lambda^2-s_n^2}\,\sinh x,
}
\]

so uniformly on every fixed bounded `x`-interval,

\[
 s_n\cosh(\tau_{n,\lambda}+x)
 \longrightarrow
 \lambda e^x.
\]

After PF-235's density-corrected fixed-axis compactification, the potential part of

\[
A=-\partial_\theta^2+\csc^2\theta
\]

therefore has the explicit local limit

\[
\boxed{
\lim_{n\to\infty}
 s_n^2
 \int_{|\tau-\tau_{n,\lambda}|\le R}
 \cosh^2\tau\,|f_{n,\lambda}(\tau)|^2\,d\tau
 =
 \lambda^2
 \int_{-R}^{R}
 e^{2x}
 \frac{\sin^2(\kappa x)}{\pi\kappa x^2}\,dx
 >0.
}
\]

The derivative part of the `A` form is nonnegative, so the complete compactified cell form has the same positive lower bound. PF-233's uniform comparison `T_{a_n}>=c_0s_n^2A` transfers the obstruction to the canonical variable-width diagonal corridor at this unprojected cell-energy stage.

Thus PF-322's critical scale is **not an endpoint/seam artifact**. For any prescribed fixed interior radius `R_0`, choosing `lambda<e^{-R_0}` places an order-one scaled-energy physical-low packet on a window of radius `R_0` that does not touch the cell seam. Any cancellation needed for the PF-321 superlinear local-angle route must therefore come from the actual physical `L/H` projection, seam-energy normalization, and common finite-pant completion; merely moving away from the quotient seam does not restore a uniform small-argument regime.

This is still deliberately not a lower bound for the completed intrinsic angle `T_{0,n}^{(r)}`. The new result sharpens the adversarial family and removes one geometric escape hatch; it does not prove that the interior critical component survives the downstream quotient/normalization/completion.

## Claim

Fix a physical cutoff `kappa>0`, choose `0<lambda<1`, and choose

\[
0<R<\log(1/\lambda).
\]

Let `ell_n`, `h_n`, and

\[
s_n=\frac{h_n+h_{n+1}}2
\]

be the canonical prime-flute quantities from PF-001/PF-299. Then for every sufficiently large `n`:

1. there is a unique `tau_{n,lambda}` in `(0,ell_n/2)` with
   \[
   s_n\cosh\tau_{n,\lambda}=\lambda;
   \]
2. the fixed interval
   \[
   [\tau_{n,\lambda}-R,\tau_{n,\lambda}+R]
   \]
   lies strictly inside `(0,ell_n/2)`;
3. the shifted Dirichlet packets `f_{n,lambda}` above are unit, zero-mean, and supported spectrally in the nonconstant physical band `0<|xi|<=kappa`;
4. writing `U` for PF-235's density-corrected compactification and `a_{n,cell}` for the PF-231 `A`-form on the fundamental cell,
   \[
   \boxed{
   \liminf_{n\to\infty}
   s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf_{n,\lambda}]
   \ge
   c_{\kappa,R,\lambda}>0,
   }
   \]
   where one may take
   \[
   \boxed{
   c_{\kappa,R,\lambda}
   =\lambda^2
   \int_{-R}^{R}
   e^{2x}
   \frac{\sin^2(\kappa x)}{\pi\kappa x^2}\,dx.
   }
   \]

More strongly, the displayed constant is the exact limit of the **potential contribution restricted to that interior window**.

Consequently the critical compactification scale persists on a fixed window that is separated from the cell seam by a positive distance independent of `n`. By taking `lambda` smaller, that guaranteed separation may be made arbitrarily large but fixed before the tail is taken.

## 1. The critical point exists inside the cell

PF-299 gives `s_n->0`. Hence, for fixed `lambda>0`, eventually

\[
s_n<\lambda.
\]

At the cell center,

\[
s_n\cosh0=s_n<\lambda.
\]

PF-322 proves from PF-001's exact cuff calibration and `s_n>=h_n/2` that

\[
s_n\cosh(\ell_n/2)>1>\lambda.
\]

Since `cosh tau` is strictly increasing for `tau>0`, there is a unique `tau_{n,lambda}` in `(0,ell_n/2)` satisfying the critical equation.

Also `tau_{n,lambda}->infinity`, because

\[
\cosh\tau_{n,\lambda}=\frac\lambda{s_n}\longrightarrow\infty.
\]

Put

\[
d_n^{(\lambda)}:=\frac{\ell_n}{2}-\tau_{n,\lambda}>0.
\]

Then

\[
\frac{\cosh(\ell_n/2)}{\cosh\tau_{n,\lambda}}
=\frac{s_n\cosh(\ell_n/2)}\lambda
>\frac1\lambda.
\]

But

\[
\frac{\cosh(\tau+d)}{\cosh\tau}
=\cosh d+\tanh\tau\sinh d
<e^d
\]

for finite `tau,d>0`. Therefore

\[
e^{d_n^{(\lambda)}}>\frac1\lambda,
\]

which proves

\[
\boxed{d_n^{(\lambda)}>\log(1/\lambda).}
\]

For fixed `R<log(1/lambda)`, the right side of the packet window is therefore strictly before the cell seam. Since `tau_{n,lambda}->infinity`, its left side is also positive for all sufficiently large `n`.

## 2. The scaled compactification has a universal interior profile

From the defining equation,

\[
s_n\cosh\tau_{n,\lambda}=\lambda,
\]

and hence

\[
s_n\sinh\tau_{n,\lambda}
=\sqrt{\lambda^2-s_n^2}.
\]

The hyperbolic addition formula gives exactly

\[
\begin{aligned}
 s_n\cosh(\tau_{n,\lambda}+x)
 &=s_n\cosh\tau_{n,\lambda}\cosh x
 +s_n\sinh\tau_{n,\lambda}\sinh x\\
 &=\lambda\cosh x
 +\sqrt{\lambda^2-s_n^2}\sinh x.
\end{aligned}
\]

Since `s_n->0`, the right side converges uniformly on bounded `x` sets to

\[
\lambda(\cosh x+\sinh x)=\lambda e^x.
\]

This is the useful normalization missing from the seam-centered PF-322 witness. It fixes the local compactification scale before any adjacent-gap ratio can enter the calculation.

For completeness, under the PF-235 density unitary

\[
y(\theta)=\sin(\theta)^{-1/2}f(\tau(\theta)),
\qquad
\sin\theta=\operatorname{sech}\tau,
\]

the full PF-231 quadratic form has the exact physical-coordinate representation

\[
\boxed{
\mathfrak a[Uf]
=\int
\cosh^2\tau
\left(
\left|f'(\tau)+\frac12\tanh\tau\,f(\tau)\right|^2
+|f(\tau)|^2
\right)d\tau.
}
\]

The present lower bound needs only the second nonnegative term. The exact formula nevertheless shows the local limiting differential scale explicitly: after translation by `tau_{n,lambda}`, the coefficient `s_n^2cosh^2 tau` tends to `lambda^2e^{2x}` and `tanh tau` tends to `1` on every fixed interior window.

## 3. The same fixed physical-low packet can be centered at the critical point

Translation on the physical cuff changes only the phases of its Fourier coefficients. Therefore the PF-322 packet may be centered at `tau_{n,lambda}` without changing its norm, mean, or frequency support.

For `x` in a fixed bounded interval,

\[
f_{n,\lambda}(\tau_{n,\lambda}+x)
=\frac{D_{N_n}(2\pi x/\ell_n)-1}
{\sqrt{2N_n\ell_n}}
\longrightarrow
\frac{\sin(\kappa x)}{\sqrt{\pi\kappa}\,x},
\]

with the continuous value `sqrt(kappa/pi)` at `x=0`, exactly as in PF-322. Uniform boundedness on `[-R,R]` and the coefficient convergence from section 2 give dominated convergence:

\[
\begin{aligned}
&s_n^2
\int_{\tau_{n,\lambda}-R}^{\tau_{n,\lambda}+R}
\cosh^2\tau\,|f_{n,\lambda}(\tau)|^2d\tau\\
&\qquad\longrightarrow
\lambda^2\int_{-R}^{R}
e^{2x}
\frac{\sin^2(\kappa x)}{\pi\kappa x^2}\,dx.
\end{aligned}
\]

The limit is strictly positive for every `kappa,R,lambda>0`. Since this is only the potential part of the positive `A` form, it gives the claimed lower bound for the complete cell energy.

PF-233's comparison

\[
T_{a_n}\ge c_0s_n^2A
\]

then preserves a positive lower bound at the same unprojected variable-width stage.

## 4. What this removes from the live direct-angle problem

PF-322 already rules out uniform use of the small-argument expansion of

\[
F(s_n\widetilde T_n^{1/2})
\]

on the whole retained physical-low space. PF-323 shows that the witness does not owe its criticality to being centered at the seam identification.

For any desired fixed radius `R_0`, choose one `lambda<e^{-R_0}`. The packet's decisive scaled-energy contribution then comes from an `R_0`-window strictly inside the cuff cell. The quotient seam lies outside that window. Thus a future proof cannot dismiss PF-322 merely by arguing that seam-centered concentration is removed by gluing the two representatives of `+-ell_n/2`.

What remains possible is genuinely downstream cancellation. The actual seam-energy diagonal normalization may change the relevant energy geometry; the physical `L/H` projection may annihilate the critical component after corridor propagation; and the common finite-pant/cusp-side completion retained by PF-320 may reduce the intrinsic mixed angle. PF-323 does not rule out any of those mechanisms.

The practical gain is a better adversarial normalization for the accepted direct-angle clue: first place the low packet at a fixed critical level `s_n cosh tau=lambda`, so the local compactification coefficient has the stable profile `lambda e^x`; only then ask what the full completed projected angle does to it. This removes uncontrolled variation in the seam-end value `s_n cosh(ell_n/2)` from the next calculation.

## 5. Prior art and novelty audit

The harmonic-analysis ingredient is the same elementary fixed-band Dirichlet-kernel scaling already audited in PF-322; stronger band-concentration theory is classical and unnecessary here. Hyperbolic addition formulas, the Liouville compactification `tau=log tan(theta/2)`, and recentering at a prescribed level of a monotone weight are elementary. No novelty is claimed for any of those ingredients in isolation.

A structure-directed literature check around Pöschl--Teller/Liouville compactifications, hyperbolic Dirichlet-to-Neumann models, and boundary spectral asymptotics did not identify an external theorem whose content is this canonical prime-flute interior scale match. The closest general literature concerns the classical Pöschl--Teller model and standard DtN/boundary-Laplacian asymptotics; neither supplies the prime-dependent relation used here. No new external theorem is imported, so `SOURCES.md` requires no additional dependency.

The project-specific contribution is the combination of PF-001/PF-299/PF-322 that produces a canonical **movable critical window** inside the actual growing cuff cell, together with the explicit limiting coefficient `lambda e^x`. The claim is therefore an exact refinement of the PF-322 proof-strategy obstruction, not a new general harmonic-analysis theorem.

## 6. Boundaries and falsification

1. **Still a cell-form result.** The theorem does not lower-bound the PF-320 completed intrinsic local `L/H` angle. It only strengthens the adversarial family at the unprojected transverse-energy stage.
2. **Interior contribution, not compact support.** The Dirichlet packet is globally defined on the cuff. The theorem states that a positive order-one scaled-energy contribution already comes from a fixed window that does not touch the seam; it does not claim the packet has no tail elsewhere.
3. **Fixed physical bandwidth.** `kappa` and `lambda` are fixed before taking the tail. No growing cutoff is used.
4. **Arbitrarily large but fixed separation.** Making the guaranteed seam separation large requires choosing a smaller fixed `lambda`; the positive limiting constant then changes by the explicit factor `lambda^2`. No separation growing with `n` is claimed.
5. **Variable-width inheritance is one-sided.** PF-233's lower form comparison preserves the cell-energy obstruction, but it does not by itself imply a corresponding lower bound after seam normalization or angle formation.
6. **No direct-channel closure or refutation.** PF-321's superlinear positive criterion and PF-318's Hilbert--Schmidt fallback remain open for the completed shear-deleted angle. PF-323 only rules out treating the PF-322 witness as an artifact of the seam location.

## Consequence for the research line

The next decisive direct-angle calculation should recenter the adversarial physical-low packet at

\[
s_n\cosh\tau_{n,\lambda}=\lambda
\]

for one fixed `lambda`, rather than at the quotient seam. In that coordinate the dangerous compactification scale has the stable local profile `lambda e^x`, while the test window remains strictly inside the cuff cell. Any disappearance of the packet at intrinsic-angle level can then be attributed to the actual seam normalization, physical `L/H` projection, or common completion, rather than to seam identification or an uncontrolled adjacent-gap ratio.