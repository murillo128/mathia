# VIS-440 — directional level-crossing flux controls the exact-target quiet tail

## Claim

Let \(F\) be a nonzero finite Laurent polynomial on a \(k\)-torus, let \(A(z)=|F(z)|/\|F\|_\infty\), and let \(\tau(u)\) be torus translation with angular velocity \(\omega\). Haar measure \(m_H\) is normalized to one. Choose \(t\in(0,1)\) a **regular value** of \(A\), put \(E_t=\{z:A(z)\ge t\}\), \(\mu_t=m_H(E_t)\), and define the symmetric first-hit time

\[
H_t(z)=\inf\{|u|:z\tau(u)\in E_t\}.
\]

The **directional crossing flux** of this level is

\[
J_t=\frac{1}{(2\pi)^k}\int_{\partial E_t}
|\omega\cdot n(z)|\,d\mathcal H^{k-1}(z),
\]

where \(n\) is a unit normal in angular coordinates. Equivalently, in coarea-density notation, \(J_t=\int\delta(A-t)|D_\omega A|\,dm_H\). For every \(\rho\ge0\),

\[
\boxed{m_H\{H_t>\rho\}\ \ge\
       [1-\mu_t-\rho J_t]_+.}
\]

This is an **exact-target geometric rarity floor** complementary to the buffered amplitude/bandwidth floor of VIS-429 and to the Parseval/Cantelli upper certificate of VIS-439. It does not imply a complete hitting law, mixing, or an anomalous Wang selector.

In particular, **target mass and outer temporal bandwidth do not determine the pre-saturation Haar quiet tail**. Two explicit degree-two circle polynomials below have the same target mass \(1/3\) and same outer frequency radius \(2\), but different fluxes and cover radii.

**Evidence/status:** EXACT-DERIVED + CLASSICAL LEVEL-CROSSING / DIRECTIONAL-PERIMETER INPUT + MATCHED-REPRESENTATION CONTROL + NO-NOVELTY-CLAIM.

## Crossing-count derivation

Because \(t>0\), \(A\) is smooth in a neighborhood of its regular level, and \(\partial E_t\) is a compact smooth hypersurface. A constant torus-translation field is divergence free. By the divergence theorem, the inward and outward oriented boundary fluxes agree; each equals \(J_t/2\).

Fix \(\rho>0\). Except for Haar-null tangential boundary contacts, every phase starting outside \(E_t\) and hitting \(E_t\) during **forward** time \([0,\rho]\) makes an outside-to-inside crossing. The expected number of inward crossings for a Haar-distributed starting phase, counted with multiplicity, is exactly \(\rho J_t/2\): integrate the inward boundary flux along the stationary orbit ensemble. Hence the Haar probability of such a forward hit starting outside is at most \(\rho J_t/2\).

The same argument for the reversed velocity bounds backward hits by another \(\rho J_t/2\). A union bound, including the initial target mass \(\mu_t\), yields \(m_H\{H_t\le\rho\}\le\mu_t+\rho J_t\), proving the claim. The geometric directional-perimeter/swept-set argument gives the same bound when tangential pieces require approximation. No stochastic independence, mixing, or time-grid approximation is assumed.

The bound is sharp before distinct boundary neighborhoods overlap, and in the explicit circle controls it is exact for every radius. At larger \(\rho\) the floor may become zero while the true avoidance probability stays positive: it is only a **one-sided** control.

## Matched exact circle control: equal mass and bandwidth, unequal flux

On \(\mathbb T^1\), set \(z=e^{i\theta}\), \(\theta\mapsto\theta+u\), with Haar \(d\theta/(2\pi)\). Compare

\[
F_{\rm two}(z)=1+z^2,\quad
A_{\rm two}(\theta)=|\cos\theta|,\quad
t_{\rm two}=\sqrt3/2
\]

and

\[
F_{\rm one}(z)=2+z+\tfrac1{10}z^2,\quad
A_{\rm one}(\theta)=|F_{\rm one}(e^{i\theta})|/(31/10),\quad
t_{\rm one}=\sqrt{691}/31.
\]

Both normalized amplitudes lie in \([0,1]\), and both polynomials have a nonzero degree-two mode and **outer temporal frequency radius \(2\)**. Their support sets are not identical, which is intentional: the test holds mass and outer frequency fixed, not every Fourier coefficient.

The corresponding targets are

\[
E_{\rm two}=\{|\cos\theta|\ge\sqrt3/2\}
\ \text{(two arcs)},\qquad
E_{\rm one}=\{\cos\theta\ge1/2\}
\ \text{(one arc)},
\]

each of Haar mass \(\mu=1/3\). Indeed
\[
|2+e^{i\theta}+\tfrac1{10}e^{2i\theta}|^2
=4.61+4.2\cos\theta+0.8\cos^2\theta,
\]
strictly increasing in \(\cos\theta\in[-1,1]\) and equal to \(691/100\) at \(\cos\theta=1/2\). Thus both target sets are determined algebraically, not fitted from a plot.

The two targets have respectively four and two transverse crossing points, yielding \(J_{\rm two}=2/\pi\) and \(J_{\rm one}=1/\pi\). Their complement consists of respectively two gaps of length \(2\pi/3\), or one gap of length \(4\pi/3\). The uncovered gap lengths after symmetric radius-\(\rho\) thickening give the **exact Haar quiet tails**

\[
m_H\{H_{\rm two}>\rho\}
  =[2/3-2\rho/\pi]_+,\qquad
m_H\{H_{\rm one}>\rho\}
  =[2/3-\rho/\pi]_+.
\]

The cover radii are \(\pi/3\) and \(2\pi/3\). Both attain the flux bound exactly. Rotation, rephasing, change of plotting coordinates and resolution do not alter these identities. They are **abstract matched finite character controls**, not assertions about which supports occur as strict near-band Wang arithmetic shells.

## Wang consequence, prior art and falsification

VIS-419 represents each fixed Wang shell as a finite Laurent polynomial on its base-prime torus. For every regular positive amplitude threshold the theorem therefore applies with prime-log angular velocity \(\omega=(\pm\log p)_p\), whose common sign does not affect \(J_t\). VIS-428 proves eventual fixed-shell saturation; VIS-429 supplies a different **buffered** target-rarity floor from target mass and orbit-Lipschitz bandwidth. This **unbuffered** flux floor is an additional same-shell calibration, potentially stronger or weaker depending on level geometry. Neither lower bound universally dominates the other, and the flux for actual Wang source coefficients is not evaluated here.

For a selected quiet window the full same-shell Haar hitting law remains the definitive comparison. In particular, a long quiet interval may be common because of low directional boundary flux even when target mass and maximum temporal bandwidth are matched. A small \(J_t\) alone is not a distinguished-height effect. The finding gives neither an upper bound for the cover radius, a Gram-versus-Haar transport theorem, nor an implication for RH.

Level-crossing intensities are classical Rice theory; the directional geometric counterpart is standard boundary-flux/coarea calculus. See S. O. Rice, *Mathematical Analysis of Random Noise*, *Bell System Technical Journal* 23 (1944), 282–332, DOI 10.1002/j.1538-7305.1944.tb00874.x. No novelty is claimed for the general crossing formula or perimeter inequality; the Mathia delta is the Wang-compatible calibration and explicit matched-spectrum geometry obstruction.

Falsify the theorem by finding a regular positive level with positive-Haar-measure tangential-only hits from the exterior, or for which stationary inward crossing intensity is not \(J_t/2\). Falsify the controls by checking their normalized maxima, exact threshold algebra, component counts or uncovered-arc identities. Singular/critical amplitude thresholds are excluded; they require separate directional-perimeter limits.

## Dependencies

- VIS-419: base-prime torus and exact shell Haar self-null.
- VIS-425: shell temporal bandwidth and frequency conventions.
- VIS-428: uniform fixed-shell saturation.
- VIS-429: buffered target-rarity floor.
- VIS-430: autocorrelation/occupation upper-tail reduction.
- VIS-439: mass-aware Parseval/Cantelli upper certificate.
