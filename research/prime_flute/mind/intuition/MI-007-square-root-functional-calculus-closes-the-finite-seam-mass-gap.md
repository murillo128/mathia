# MI-007 — Square-root functional calculus closes the finite-seam mass gap

**Evidence level:** exact sublinear seam asymptotics, complete-Bernstein/Stieltjes analysis of the square-root source, and exact continuous-Hahn diagonalization through PF-274

## Core intuition

Separated propagation genuinely changes the Prime-Flute endpoint problem to low-output leakage, and the naked finite seam satisfies a strict sublinear leakage exponent because its positive Green representation begins at a nonzero mass. But the physical normalized Robin source applies a square root to that seam operator. The square root preserves complete-Bernstein positivity while changing the representing spectrum qualitatively: its Green measure reaches zero mass.

A spectral gap in one operator therefore cannot be inherited through nonlinear functional calculus without computing the transformed measure. Here the gap closes exactly to the critical `mu=1` edge, but the fixed-axis operator is now explicitly diagonalizable, so the remaining question can be attacked in a concrete spectral basis rather than through abstract recurrence estimates alone.

## Strongest justified principle

PF-272 proves that for fixed seam parameters the naked relative seam maps an input block near `N` into an output window `N^theta`, `theta<1`, with norm `asymp N^{-alpha_s(theta)}` and `alpha_s(theta)>1`; for logarithmic output the exponent approaches `mu_0+1/2>1`. This validates the PF-271 post-propagation strategy at the raw seam level.

PF-273 writes the raw symbol `f_w(lambda)=sqrt(lambda)tanh(w sqrt(lambda))` as an atomic complete-Bernstein mixture with lowest mass `a_0^2>0`. For the source factor `g_w=sqrt(f_w)`, complete-Bernstein closure still holds, but Stieltjes inversion gives an absolutely continuous positive measure supported on alternating intervals beginning at `t=0`, with density `~ sqrt(w)/(pi sqrt(t))` at the lower edge. In Green coordinates the support therefore reaches `mu=sqrt(1+t)=1`, eliminating the discrete first-pole margin responsible for PF-272's strict exponent.

PF-274 identifies the underlying fixed-axis operator exactly. After the complete-axis unitary map and Fourier transform, the corridor Gegenbauer basis becomes the equal-parameter symmetric continuous-Hahn family, and the matrix of `L` is `I+4 H_*^2`. Hence every bounded `H(L)`, including massive resolvents and `g_w(L)`, has an exact continuous-Hahn spectral integral for its corridor matrix coefficients. This reframes the live low-mass boundary as a specific asymptotic transform problem without claiming that diagonalization itself supplies the needed decay.

## Program consequence

Estimate the full normalized source/conversion, not `Q_w^(1/2)` or the naked seam in isolation. Use the continuous-Hahn representation to determine whether `(I+XX*)^-1`, Robin reflections, or the exact composed source geometry suppresses the `mu=1` continuum enough to restore a strict high-to-low exponent in the PF-271 window. Only after that fixed-axis gate is settled should shear/corridor uniformity be charged.

Whenever a future route uses a nonlinear operator function, compute how its spectral/Green measure transforms and then evaluate the resulting matrix coefficients in the representation actually consumed by the endpoint map.

## Counterevidence / boundary

PF-273--PF-274 do not prove that the full normalized conversion fails or satisfies the required leakage bound. Exact continuous-Hahn diagonalization controls the scalar functional calculus of `L`, but the complete source composition may contain additional noncommuting factors. The results are fixed-axis and do not settle parameter uniformity, shear, density corrections, or the full corridor.

PF-272 remains a genuine positive result for the naked relative seam; the new boundary is specifically the invalid inheritance of its mass gap through the square root.

## Epistemic status

**Exact functional-calculus boundary with an exact spectral representation: the raw finite seam has supercritical sublinear leakage because of a positive lowest Green mass, its square-root source factor replaces that ladder by a continuum reaching zero mass, and the resulting fixed-axis matrix coefficients are explicitly continuous-Hahn transforms; the physical leakage theorem remains open for the full normalized conversion.**

## Falsification criterion

Show that the complete-Bernstein measure of `sqrt(f_w)` retains a positive lower mass gap contrary to PF-273, invalidate the continuous-Hahn representation in PF-274, or prove that the PF-272 exponent transfers to the complete normalized source without any mechanism that suppresses the newly exposed `t downarrow 0` continuum.
