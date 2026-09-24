# WI-429 — Hardy projection isolates deeper Kunik defects without operator blow-up

Status: `CLASSICAL-IDENTITY + EXACT-DERIVED + STRUCTURAL-CONSTRAINT + PRIOR-ART-REDIRECT`

Parents: `WI-424`, `WI-425`, `WI-426`, `WI-428`

## Claim

`WI-428` proves that bounded signed/complex cross-scale processing on a **fixed safe strip** remains cubically blind to a shallow Kunik defect. The obstruction disappears in a different category: move the probe line inside the horizontal depth of the defect and apply the ordinary Hardy/Riesz projection onto one Fourier half-line.

For a finite Kunik Blaschke subproduct with right-half zeros

\[
\rho_j=\frac12+d_j+i\gamma_j,
\qquad d_j>0,
\]

of multiplicities \(m_j\), put

\[
G_{F,a}(t):=
\frac{B_F'(\frac12+a+it)}{B_F(\frac12+a+it)},
\qquad a>0,
\]

and assume \(a\ne d_j\) for every zero in the finite set. Under the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\]

let \(P_+\) denote the orthogonal Riesz projection with multiplier \(1_{\xi>0}\). Then exactly

\[
\boxed{
P_+G_{F,a}(t)
=
\sum_{d_j>a}
\frac{m_j}{a-d_j+i(t-\gamma_j)}.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\widehat{P_+G_{F,a}}(\xi)
=-2\pi 1_{\xi>0}
\sum_{d_j>a}
 m_j e^{-(d_j-a)\xi}e^{-i\gamma_j\xi}.
}
\tag{2}
\]

Thus a norm-one operator **annihilates every Blaschke zero shallower than the probe line and keeps every zero deeper than it**. There is no operator-norm singularity: \(\|P_+\|_{L^2\to L^2}=1\). The category change relative to `WI-428` is geometric, not functional-analytic: the line itself must approach the critical boundary closely enough to cross inside the unknown defect depth.

The surviving part has an exact positive energy:

\[
\boxed{
\|P_+G_{F,a}\|_2^2
=
2\pi
\sum_{\substack{j,k\\d_j,d_k>a}}
 m_jm_k
\frac{\delta_j+\delta_k}
{(\delta_j+\delta_k)^2+(\gamma_j-\gamma_k)^2},
\qquad
\delta_j=d_j-a.
}
\tag{3}
\]

Every term in (3) is nonnegative, so in particular

\[
\boxed{
\|P_+G_{F,a}\|_2^2
\ge
\pi\sum_{d_j>a}\frac{m_j^2}{d_j-a}.
}
\tag{4}
\]

For one defect of depth \(d>a\),

\[
\boxed{
\|P_+G_{d,\gamma;a}\|_2^2
=\frac{\pi}{d-a}
\ge \frac{\pi}{d}.
}
\tag{5}
\]

This recovers at least one half of the canonical boundary diagonal tariff \(2\pi/d\) from `WI-424` as soon as the probe is inside the defect. Moreover, if \(a\downarrow0\) below all depths of a finite subproduct, then

\[
\boxed{
\lim_{a\downarrow0}
\|P_+G_{F,a}\|_2^2
=\frac12\|h_F\|_2^2,
}
\tag{6}
\]

where \(h_F=-B_F'/B_F\) on the critical boundary is the positive Poisson defect counter of `WI-424`.

The consequence is a sharp refinement of the current frontier. `WI-428` rules out bounded processing while the line remains a fixed positive distance from the boundary. It does **not** force a singular operator once the probe line is allowed to move. The exact remaining requirement is instead a source-side theorem controlling a predetermined boundary-approaching family \(a_n\downarrow0\). A fixed line \(a>0\) can never detect all off-line defects, because every configuration with \(0<d_j<a\) lies identically in the kernel of (1).

No Riemann-hypothesis conclusion is obtained here. The missing estimate is precisely the hard part: the full zeta logarithmic derivative has poles and is not globally an ordinary \(L^2\) function on such lines, and a valid source-side control must be localized or distributional and must be proved independently of the off-line zero set.

## 1. Exact Fourier separation

Kunik's one-zero Blaschke logarithmic derivative, already used in `WI-424`, is

\[
\frac{B_\rho'(s)}{B_\rho(s)}
=
\frac1{s-\rho}
-
\frac1{s-(1-\bar\rho)}.
\tag{7}
\]

At \(s=1/2+a+it\), with \(u=t-\gamma\), this becomes

\[
g_{a;d,\gamma}(t)
=
\frac1{a-d+iu}
-
\frac1{a+d+iu}.
\tag{8}
\]

The Fourier orientation is elementary but important. For \(c>0\), contour integration or the Laplace representation gives

\[
\boxed{
\widehat{\frac1{c+i(t-\gamma)}}(\xi)
=2\pi e^{c\xi}e^{-i\gamma\xi}1_{\xi<0}.
}
\tag{9}
\]

For \(b>0\), the pole is in the lower half-plane and

\[
\boxed{
\widehat{\frac1{-b+i(t-\gamma)}}(\xi)
=-2\pi e^{-b\xi}e^{-i\gamma\xi}1_{\xi>0}.
}
\tag{10}
\]

If \(d<a\), both denominators in (8) have positive real part and (9) puts the entire response in negative frequencies. Hence \(P_+g_{a;d,\gamma}=0\). If \(d>a\), the first denominator has negative real part while the reflected denominator remains positive; (9)--(10) therefore split the two terms onto opposite Fourier half-lines and give

\[
P_+g_{a;d,\gamma}(t)
=\frac1{a-d+i(t-\gamma)}.
\tag{11}
\]

Summing (11) with multiplicities proves (1)--(2). Because the set is finite and \(a\ne d_j\), all functions involved are ordinary \(L^2(\mathbb R)\) functions and no distributional qualification is needed for this finite-product theorem.

This also identifies the unavoidable geometric threshold exactly. A probe family whose line depths satisfy \(a\ge a_0>0\) is completely blind, after \(P_+\), to every off-line configuration contained in \(0<d<a_0\). Therefore any complete defect-elimination program based on this Fourier separation must have \(\inf a=0\). This necessity is independent of norm estimates or arithmetic input.

## 2. Positive pair energy and boundary limit

By Plancherel and (2),

\[
\begin{aligned}
\|P_+G_{F,a}\|_2^2
&=\frac1{2\pi}\int_0^\infty
4\pi^2
\left|\sum_{d_j>a}
 m_j e^{-\delta_j\xi}e^{-i\gamma_j\xi}\right|^2d\xi.
\end{aligned}
\tag{12}
\]

Expanding the square and pairing the \((j,k)\) and \((k,j)\) terms gives exactly (3), since

\[
\Re\int_0^\infty
 e^{-(\delta_j+\delta_k)\xi}
 e^{-i(\gamma_j-\gamma_k)\xi}\,d\xi
=
\frac{\delta_j+\delta_k}
{(\delta_j+\delta_k)^2+(\gamma_j-\gamma_k)^2}.
\tag{13}
\]

The diagonal \(j=k\) contributes \(\pi m_j^2/\delta_j\), proving (4)--(5). In particular the singular growth as the moving line approaches a zero depth from below is not caused by the projection: it is the actual Cauchy pole crossing the line.

For \(a=0\), (8) reduces to

\[
\frac1{-d+iu}-\frac1{d+iu}
=-\frac{2d}{u^2+d^2},
\tag{14}
\]

so the boundary trace is \(G_{F,0}=-h_F\), with \(h_F\) from `WI-424`. A real \(L^2\) function has equal positive- and negative-frequency energies, and there is no zero-frequency atom here. Hence

\[
\|P_+G_{F,0}\|_2^2=\frac12\|h_F\|_2^2.
\tag{15}
\]

The same result follows termwise from (3): taking \(a\downarrow0\) gives

\[
2\pi\sum_{j,k}
 m_jm_k
\frac{d_j+d_k}
{(d_j+d_k)^2+(\gamma_j-\gamma_k)^2},
\tag{16}
\]

which is exactly one half of the boundary pair identity

\[
\|h_F\|_2^2
=4\pi\sum_{j,k}
 m_jm_k
\frac{d_j+d_k}
{(d_j+d_k)^2+(\gamma_j-\gamma_k)^2}
\tag{17}
\]

from `WI-424`. This proves (6) without any limiting ambiguity for finite products.

## 3. What this changes relative to the fixed-safe-strip barriers

The findings `WI-425`--`WI-428` study probes that stay in a safe region \(a>d\) for the target defect. There the one-defect response has size

\[
\|g_{a;d,\gamma}\|_2^2
=\frac{2\pi d^2}{a(a^2-d^2)},
\tag{18}
\]

and therefore becomes cubically negligible relative to the boundary tariff \(2\pi/d\) when \(a\) is fixed and \(d\downarrow0\). `WI-428` then shows that bounded signed, complex or non-diagonal processing cannot repair that loss on a fixed safe strip.

Equation (11) shows why that no-go theorem has a genuine boundary. Once \(a<d\), one Cauchy pole crosses to the opposite Hardy half-space. The orthogonal projection does not amplify anything; it simply discards the reflected/shallow half and retains the crossed pole. The diagonal energy jumps from the safe-side scaling \(O(d^2)\) at fixed \(a\) to the reciprocal-distance tariff \(\pi/(d-a)\).

This is therefore not a hidden violation of the operator budget in `WI-428`. The operator is fixed and contractive. What changes is the **probe geometry**, exactly one of the category changes left open there. The price has merely moved: a successful zeta argument now has to control source data on lines with \(a\to0\), not pay a norm growing like \(d^{-3/2}\) or \(d^{-3}\).

A deterministic sequence \(a_n\downarrow0\) is enough for target coverage. For every hypothetical off-line zero of fixed depth \(d>0\), all sufficiently large \(n\) satisfy \(a_n<d\), and then (5) gives

\[
\|P_+G_{F,a_n}\|_2^2\ge\frac{\pi}{d-a_n}\ge\frac\pi d.
\tag{19}
\]

Thus the line locations need not be chosen after inspecting the zero. What remains potentially oracular is any **upper bound** for the projected source term if that upper bound is derived using the same off-line zeros. Independence of the source estimate is therefore still the decisive publication gate for any future RH claim.

## 4. Kunik's identity suggests the correct source-side projection, but does not yet bound it

Kunik's interior logarithmic-derivative identity, recorded as equation (9) of `WI-424`, is

\[
\frac{B'(s)}{B(s)}
=
\frac{\zeta'(s)}{\zeta(s)}
-\frac1s+\frac1{s-1}
+\frac1\pi\int_{-\infty}^{\infty}
\frac{\log|\zeta(\frac12+iu)|}
{(s-\frac12-iu)^2}\,du,
\qquad \Re s>\frac12.
\tag{20}
\]

Put \(s=1/2+a+it\) with \(0<a<1/2\). The Fourier orientations in (9)--(10) show formally that the terms with a positive real-part Cauchy denominator live in the negative-frequency Hardy half-space. In particular, the differentiated Poisson--Schwarz integral has the same negative-frequency orientation, as does \(-1/s\). The pole term \(1/(s-1)\), whose real part relative to the line variable is \(a-1/2<0\), lives in the positive-frequency half-space.

This suggests the distributional/localized identity

\[
P_+\frac{B'}B
=
P_+\left(\frac{\zeta'}\zeta+\frac1{s-1}\right)
\tag{21}
\]

on such a line, with the outer Poisson--Schwarz term removed automatically. Equation (21) is **not** promoted here to an ordinary global \(L^2\) theorem for \(\zeta'/\zeta\). The latter has pole singularities and its full vertical-line norm need not be finite. A rigorous zeta-level use needs truncation/localization or a distribution/Hardy formulation that prices all boundary terms.

Still, (21) is useful as a falsifiable interface. The finite-Blaschke left side has the exact positive lower bound (4). A non-oracular arithmetic estimate on a localized version of the right side, uniform enough along a predetermined sequence \(a_n\downarrow0\), would couple prime/critical-line information directly to a reciprocal-depth off-line defect tariff. Conversely, if every such localization necessarily loses at least the same reciprocal-depth amount, that would close this route cleanly.

## 5. Prior art and novelty audit

No priority claim is made for the Hardy-space ingredients.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829v2 (2009), supplies the half-plane Blaschke factorization and the interior logarithmic-derivative identity used in (7) and (20). `WI-424` already audited the exact equation numbers and normalizations against that primary source.
- The Fourier support of Cauchy kernels in opposite half-planes, the Paley--Wiener characterization of half-plane Hardy spaces, and the Riesz projections \(P_\pm\) are classical harmonic analysis. Kunik explicitly places his representation in this Hardy/Poisson--Schwarz setting and cites the standard Hardy-space literature.
- The repository-local advance is narrower: applying that classical frequency split to the precise Kunik one-defect response shows that the bounded-operator obstruction of `WI-428` is a fixed-safe-strip obstruction, gives the exact deeper-zero pair energy (3), proves the half-boundary identity (6), and identifies \(a_n\downarrow0\) as a necessary geometric condition for complete defect detection.

A targeted literature/repository audit did not locate a source that packages this exact deeper-zero projection identity and its use against the current Kunik fixed-strip no-go chain. Absence from that audit is not used as a priority claim.

## Boundary, stress tests, and falsification

The statement is deliberately finite-product first. For the full zeta Blaschke product there may be infinitely many zeros with \(d>a\), and the global norm in (3) may diverge. Any extension must specify the mode of convergence and localization; divergence cannot simply be called a contradiction.

The threshold \(a=d_j\) is excluded because the vertical probe line passes through the zero and the Cauchy term ceases to be an \(L^2\) function. Approaching this threshold from below produces the genuine divergence \(\pi/(d_j-a)\). This agrees with, rather than evades, the singular behavior isolated in `WI-426`.

A fixed positive line depth is insufficient: if \(a\ge a_0>0\), arbitrarily shallow defects \(d<a_0\) are exactly invisible to \(P_+\). Integrating a positive continuum of line energies down to zero is also not justified by this finding and can reintroduce the blind-or-singular dichotomy of `WI-426`. The useful object is instead a predetermined boundary-approaching family together with an independently proved source-side estimate.

Finally, none of (1)--(21) separates multiple critical-line zeros from off-line defects in the Montgomery matrix count by itself, nor does it provide an unconditional upper bound for the zeta source term. The exact conclusion is structural: **bounded Hardy projection supplies a non-singular detector once the line crosses inside a defect, so the next obstruction is source-side control near the boundary, not operator amplification**.