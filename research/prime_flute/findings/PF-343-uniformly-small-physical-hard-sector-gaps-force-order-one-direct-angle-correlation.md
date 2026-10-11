# PF-343 — uniformly small physical hard-sector gaps force order-one direct-angle correlation

**Status:** \`EXACT-DERIVED + HARD-SECTOR-SEPARATION-OBSTRUCTION + NONCOMPACT-DIRECT-ANGLE + DECISIVE-NEGATIVE\`.

PF-342 proves noncompactness for the canonical sharp fixed physical cutoff by placing two adjacent Fourier modes, separated by exactly one lattice step \`2pi/L\`, on opposite sides of the cutoff. The lattice-step formula is not the real threshold.

The PF-342 corridor argument is uniform for bounded physical frequencies. If two normalized Fourier traces have physical frequencies \`alpha,beta\` in one fixed bounded band and

\[
0<|\beta-\alpha|\le \delta_*,
\]

for a sufficiently small **fixed** constant \`\delta_*>0\`, then their sum still pays the full collapsing-corridor conductance \`1/(sL)\`, whereas their difference pays at most

\[
O\!\left(1+\frac{|\beta-\alpha|^2}{sL}\right).
\]

Since \`sL->0\`, choosing \`\delta_*\` small enough makes the difference energy a fixed fraction of the sum energy, uniformly on the tail. Polarization therefore forces a positive \`1/(sL)\` mixed DtN coefficient and hence an order-one energy-normalized canonical correlation.

Thus the PF-342 obstruction is not specific to a fixed cutoff and does not require the physical separation to tend to zero. Any hard low/high architecture that, on infinitely many tail modules, assigns two bounded physical Fourier modes to opposite sectors while their physical separation is at most one sufficiently small fixed constant has a noncompact direct angle.

In particular:

- moving hard cutoffs do not help;
- a binary scale-dependent hard partition does not help if opposite sectors remain physically close;
- a transition band whose retained low/high sides are separated by a width tending to zero does not help at the **direct** angle level;
- the next genuine escape must create a uniformly positive physical separation larger than the obstruction scale and retain the intermediate sector through the completed operator, rather than merely relabeling or discarding it.

The natural unresolved operation is therefore a three-sector \`L/T/H\` decomposition with a positive-width transition band \`T\`, followed by exact positive Schur-complement/shorting elimination of \`T\`. That operation is not covered by this finding.

## Claim

Fix \`K>0\`. On a tail one-cusp pant let the chosen finite boundary have period \`L\`, let \`s\` be the finite-finite core separation, and assume the canonical Prime-Flute tail regime

\[
L\to\infty,
\qquad
sL\to0.
\]

Let

\[
\alpha=\frac{2\pi a}{L},
\qquad
\beta=\frac{2\pi b}{L},
\qquad
a,b\in\mathbb Z_{\ge0},
\]

satisfy

\[
0\le \alpha,\beta\le K.
\]

Use normalized cosine traces centered at the finite-finite common-perpendicular foot,

\[
c_\alpha(t)=\sqrt{\frac2L}\cos(\alpha t),
\qquad
c_\beta(t)=\sqrt{\frac2L}\cos(\beta t).
\]

Let \`A(s,L)\` be the positive \`\Delta+1\` self-DtN block used in PF-341/PF-342. Then there are constants

\[
\delta_*=\delta_*(K)>0,
\qquad
c_K,C_K>0,
\]

depending only on the fixed bounded frequency band and the canonical corridor constants, such that whenever

\[
0<\delta:=|\beta-\alpha|\le\delta_*,
\]

one has, after a finite tail,

\[
\boxed{
\operatorname{Re}\langle c_\beta,A(s,L)c_\alpha\rangle
\ge \frac{c_K}{sL},
}
\]

and

\[
\boxed{
\langle c_\alpha,A(s,L)c_\alpha\rangle+
\langle c_\beta,A(s,L)c_\beta\rangle
\le \frac{C_K}{sL}.
}
\]

Consequently the scalar canonical correlation of the two traces in the pant energy is bounded below by a constant

\[
\rho_K>0
\]

independent of the tail module.

For a Prime-Flute cuff module \`n\`, suppose two bounded physical Fourier modes \`c_{n,L}\` and \`c_{n,H}\` are assigned to opposite hard sectors and satisfy

\[
|\xi_{n,H}-\xi_{n,L}|\le\delta_*
\]

on infinitely many tail modules. In the symmetric seam-parity channel, zero twist makes the two adjacent pant contributions have the same positive sign, while the Fourier-diagonal seam form contributes no low/high numerator and is negligible compared with the diverging pant scale.

After passing to a subsequence of modules separated by at least three indices, PF-214 finite-range support yields arbitrarily large orthogonal families with canonical correlations at least some fixed \`\rho_0>0\`. Therefore the corresponding direct hard-sector angle \`Z_{LH}\` has arbitrarily many singular values bounded below by \`\rho_0\` and is not compact on any finite-section-compatible realization.

## 1. The sum mode still pays the full corridor conductance

Set

\[
g_+=\frac{c_\alpha+c_\beta}{\sqrt2},
\qquad
g_-=\frac{c_\beta-c_\alpha}{\sqrt2}.
\]

PF-341/PF-342 provide a growing embedded finite-finite corridor whose remaining ray length satisfies

\[
c_0s\cosh t\le \ell(t)\le C_0s\cosh t
\]

on the canonical corridor.

Because both physical frequencies lie in \`[0,K]\`, choose \`t_0=t_0(K)>0\` so small that both cosines are uniformly positive on \`|t|\le t_0\`. Hence

\[
|g_+(t)|^2\ge \frac{c_K}{L}
\qquad (|t|\le t_0).
\]

The same one-dimensional conductance lower bound used in PF-341/PF-342 gives

\[
\mathcal E_A(g_+)
\ge
c\int_{-t_0}^{t_0}
\frac{|g_+(t)|^2}{s\cosh t}\,dt
\ge
\frac{c_K}{sL}.
\tag{1}
\]

Nothing here uses that \`\alpha,\beta\` are adjacent lattice frequencies.

## 2. The difference energy is quadratic in physical frequency separation

By the mean-value theorem in the frequency variable,

\[
|g_-(t)|
\le
\frac{C_K\delta |t|}{\sqrt L},
\]

and

\[
|g_-'(t)|
\le
\frac{C_K\delta(1+|t|)}{\sqrt L}
\]

throughout the collapsing corridor.

Using the same raywise linear trial as PF-342,

\[
u(t,r)=g_-(t)\left(1-\frac r{\ell(t)}\right),
\]

the singular transverse contribution obeys

\[
\int
\frac{|g_-(t)|^2}{s\cosh t}\,dt
\le
C_K\frac{\delta^2}{sL}.
\tag{2}
\]

The tangential, positive-shift, and noncollapsing completion costs are uniformly \`O_K(1)\` for bounded physical frequencies, exactly as in PF-342. Therefore

\[
\boxed{
\mathcal E_A(g_-)
\le
C_K\left(
1+\frac{\delta^2}{sL}
\right).
}
\tag{3}
\]

PF-342 is the special case \`\delta=2\pi/L\`.

Choose \`\delta_*>0\` so that

\[
C_K\delta_*^2\le \frac{c_K}{4},
\]

with \`c_K\` from (1). Since \`sL->0\`, after a finite tail also

\[
C_K\le \frac{c_K}{4sL}.
\]

Hence for \`\delta\le\delta_*\`,

\[
\mathcal E_A(g_-)
\le
\frac{c_K}{2sL}.
\tag{4}
\]

Polarization gives

\[
2\operatorname{Re}\langle c_\beta,Ac_\alpha\rangle
=
\mathcal E_A(g_+)-\mathcal E_A(g_-),
\]

so (1) and (4) imply

\[
\operatorname{Re}\langle c_\beta,Ac_\alpha\rangle
\ge
\frac{c'_K}{sL}.
\tag{5}
\]

For each individual bounded-frequency mode, PF-342's fixed-band extension trial is uniform on \`[0,K]\` and gives

\[
\mathcal E_A(c_\alpha)+\mathcal E_A(c_\beta)
\le
\frac{C'_K}{sL}.
\tag{6}
\]

Combining (5), (6), and the arithmetic-geometric mean inequality yields a fixed positive lower bound for the energy-normalized correlation.

## 3. Two-pant assembly and noncompactness are unchanged

PF-340/PF-342 identify the symmetric seam-parity self response as the average of the two adjacent pant self blocks. Zero twist identifies the same physical Fourier origin at the finite-finite seam foot on both sides.

Therefore the one-pant lower bound (5) applies with the same sign to both adjacent pants. The two-pant mixed coefficient is bounded below by

\[
c_K D_n,
\qquad
D_n=
\frac1{L_n}
\left(
\frac1{s_{n-1}}+\frac1{s_n}
\right),
\]

while the corresponding pant diagonal energies are \`O_K(D_n)\`.

On bounded physical frequencies the symmetric seam eigenvalue remains \`O_K(w_n)\`, whereas PF-341 gives \`D_n->infinity\`. The seam form is Fourier diagonal and adds no mixed numerator. Thus the raw total positive form has a canonical correlation bounded below uniformly on every module carrying such a hard-sector pair.

PF-214 finite-range support then gives the same separated-module singular-value argument as PF-342. If infinitely many modules admit opposite hard-sector modes with physical separation at most \`\delta_*\`, the direct angle is noncompact.

## 4. What changes relative to PF-342

PF-342 used the canonical fixed threshold \`\kappa\` and the neighboring modes immediately below and above it, so

\[
\delta_n=\frac{2\pi}{L_n}\to0.
\]

The present argument shows that the vanishing lattice step was stronger than necessary. The actual local obstruction is

\[
\boxed{
\text{bounded physical frequency}
+
\text{opposite hard sectors}
+
\text{sufficiently small physical separation}.
}
\]

This has three immediate consequences.

First, a moving hard threshold \`\kappa_n\` inside a bounded physical interval is still obstructed whenever the nearest retained/excluded modes lie on opposite sides, because their spacing is again at most one lattice step.

Second, replacing one cutoff by a binary hard partition with a narrow physical gap does not help. The gap may even stay at a small positive constant; it need not shrink with \`n\`.

Third, a transition region can escape this theorem only if it creates a genuinely positive physical separation between the retained low and high sectors that stays outside the small-separation obstruction scale. Even then, merely discarding the transition sector does not prove a useful endpoint theorem. The transition degrees of freedom belong to the positive DtN form and can feed back into the effective low/high response.

That last point is why the natural next test is a genuine three-sector Schur complement rather than another direct binary angle estimate.

## Prior-art and novelty audit

The ingredients used here are classical in isolation.

The Steklov spectrum is the spectrum of the Dirichlet-to-Neumann operator, and variational characterizations of DtN/Steklov energies are standard; see A. Girouard and I. Polterovich, *Spectral geometry of the Steklov problem*, J. Spectr. Theory 7 (2017), 321--359, DOI \`10.4171/JST/164\`.

Thin-neck Steklov degeneration is also classical. D. Bucur, A. Henrot and M. Michetti, *Asymptotic behaviour of the Steklov spectrum on dumbbell domains*, Comm. PDE 46 (2021), 362--393, DOI \`10.1080/03605302.2020.1840587\`, analyze Steklov eigenpairs when two domains are connected by a vanishing tube and obtain lower-dimensional limiting behavior.

Neither source states the present result. The Mathia-specific content is the uniform comparison between two nearby **bounded physical Fourier traces** on the exact PF-341 hyperbolic pant corridor, followed by zero-twist two-pant sign coherence, seam normalization, and PF-214 finite-range assembly into a noncompact canonical-correlation operator.

No external theorem is load-bearing beyond standard variational background; the quantitative constants and the noncompactness conclusion are derived from persisted Prime-Flute geometry. No historical novelty is claimed for DtN variational principles, thin-domain asymptotics, hard projections, or Schur complements.

For the surviving transition-band route, Schur-complement realizations of DtN maps are themselves classical; see L. Knockaert, D. De Zutter, G. Lippens and H. Rogier, *On the Schur complement form of the Dirichlet-to-Neumann operator*, Wave Motion 45 (2008), 309--324, DOI \`10.1016/j.wavemoti.2007.07.004\`. That literature does not decide the Prime-Flute transition-band estimate proposed below.

## Boundaries and falsification

1. **Bounded physical frequency is load-bearing.** The constants are uniform only on a fixed compact frequency band.
2. **The separation threshold is existential, not identified sharply.** The proof produces some \`\delta_*(K)>0\`; it does not optimize it.
3. **Hard opposite sectors are load-bearing.** A smooth partition of unity does not create two disjoint hard subspaces in the same way and requires a different operator formulation.
4. **A genuine transition-band Schur complement is outside the theorem.** Eliminating intermediate modes can change the effective low/high form.
5. **Symmetric seam parity and zero twist remain load-bearing** exactly as in PF-342.
6. **The result is an operator-architecture obstruction, not an RH theorem.** It gives no zeta-zero correspondence, critical-line theorem, scattering determinant, or RH implication.

A falsification may exhibit a failure of the uniform PF-342 fixed-band upper trial for arbitrary bounded lattice frequencies, a failure of the quadratic difference estimate (3), loss of same-sign two-pant assembly under the canonical zero-twist marking, or an incompatibility between the separated-module compressions and PF-214 finite-range support.

## Consequence for the research line

The sharp-cutoff obstruction is now a **small physical separation obstruction**. Moving the hard boundary, making it scale-dependent, or inserting a transition gap that remains too narrow does not restore compactness.

Any surviving completed-angle construction must therefore alter the representation at finite physical scale. The cleanest remaining question is whether a transition band of uniformly positive width can absorb the collapsing-corridor rank-one response when that band is retained and then eliminated by the exact positive Schur complement. That is a materially different operator and is not settled here.
