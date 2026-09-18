---
id: WP-359
title: Smooth Hecke height cutoffs add only p²-orbit interference and retain the 1/p boundary scale
branch: weil_positivity
status: supported
kind: smooth-hecke-height-commutator-half-density-no-go
claim_strength: exact smooth-height commutator decomposition; exact p²-orbit interference classification; exact nonconstant Fourier-Følner scalarization; asymptotic fixed-width cutoff obstruction
created: 2026-09-18
related: [WP-216, WP-226, WP-255, WP-356, WP-357, WP-358]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical self-adjoint normalized Hecke algebra on the modular surface
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - classical Fourier-mode action of Hecke operators on automorphic forms
  - classical Maaß-Selberg and Arthur cusp truncation as the neighboring nonlocal truncation framework
---

# WP-359 — Smooth Hecke height cutoffs add only p²-orbit interference and retain the 1/p boundary scale

## Claim

`WP-358` left smooth cusp-height truncation open because smoothing destroys the disjoint-support argument that made the sharp Hecke boundary square diagonal. That escape can be classified for every fixed bounded height multiplier.

On the full cusp Hilbert space, keep the exact prime-Hecke representation from `WP-358`,

\[
\mathcal U T_p\mathcal U^{-1}=V_pS_L+V_p^*S_{-L},
\qquad L=\log p,
\tag{1}
\]

where `V_p e_r=e_{pr}` on `L^2(\mathbb T)` and `S_a f(x)=f(x+a)` on log-height. For any real bounded height profile `q`, let `M_q` be multiplication by `q`. Writing

\[
A_L=[M_q,S_L],
\qquad
B_L=[M_q,S_{-L}],
\tag{2}
\]

gives the exact smooth boundary commutator

\[
\boxed{
D_{p,q}:=[M_q,\mathcal U T_p\mathcal U^{-1}]
=V_pA_L+V_p^*B_L.
}
\tag{3}
\]

Unlike the sharp case, `A_L` and `B_L` may have overlapping height support. The resulting positive square contains cross terms, but their arithmetic structure is completely rigid:

\[
\boxed{
D_{p,q}^*D_{p,q}
=
I\otimes A_L^*A_L
+Q_p\otimes B_L^*B_L
+(V_p^*)^2\otimes A_L^*B_L
+V_p^2\otimes B_L^*A_L,
}
\tag{4}
\]

with `Q_p=V_pV_p^*`. Thus smoothing introduces no new diagonal prime weight. Its only new information is **off-diagonal coherence along the multiplicative `p^2` orbits of Fourier indices**.

Two exact consequences sharply narrow the escape.

First, on every single nonzero Fourier mode the two Hecke branches remain orthogonal regardless of how much their height supports overlap:

\[
\boxed{
\|D_{p,q}(e_r\otimes f)\|^2
=
\|A_Lf\|^2
+\mathbf 1_{p\mid r}\,\|B_Lf\|^2,
\qquad r\ne0.
}
\tag{5}
\]

Second, the canonical symmetric nonconstant Fourier Følner scalarization kills the new cross terms exactly and retains the same divisibility density as the sharp boundary. If `F_N^\circ` projects onto `0<|r|\le N` and

\[
\tau_N^\circ(X)
=\frac1{2N}\operatorname{Tr}(F_N^\circ X F_N^\circ),
\tag{6}
\]

then

\[
\tau_N^\circ(V_p^2)
=\tau_N^\circ((V_p^*)^2)=0,
\qquad
\tau_N^\circ(Q_p)=\frac{\lfloor N/p\rfloor}{N},
\tag{7}
\]

so

\[
\boxed{
(\tau_N^\circ\otimes\mathrm{id})(D_{p,q}^*D_{p,q})
=A_L^*A_L
+\frac{\lfloor N/p\rfloor}{N}B_L^*B_L
\longrightarrow
A_L^*A_L+\frac1pB_L^*B_L.
}
\tag{8}
\]

Therefore a fixed smooth height cutoff cannot manufacture the missing critical half-density by overlap of its two local branches. In the natural diagonal/Følner readout, the angular arithmetic is still `1/p`, not `p^{-1/2}`.

For the standard class of fixed-width smooth cutoffs this becomes an asymptotic no-go with the logarithmic scale included. Suppose `q=q_-` for `x\le-R` and `q=q_+` for `x\ge R`. Define the flat boundary mass

\[
m_q(L)
:=\int_{\mathbb R}|q(x)-q(x+L)|^2\,dx.
\tag{9}
\]

Then, with `c=q_+-q_-`,

\[
\boxed{
m_q(L)=c^2L+O_q(1)
\qquad(L\to\infty).
}
\tag{10}
\]

The prime-specific backward contribution of (8) is consequently

\[
\boxed{
\frac{m_q(\log p)}p
=
\frac{c^2\log p}{p}+O_q(p^{-1}),
}
\tag{11}
\]

whereas the critical Weil finite-prime coefficient has scale `(\log p)/\sqrt p`. Their ratio tends to zero. Smoothing a source-fixed finite-width cusp boundary therefore changes only the height profile; it does not change the arithmetic exponent inherited from the positive quadratic square.

The only local-multiplier escape left by (4) is deliberately more specific than “use a smooth truncation”: one must exploit coherent off-diagonal correlations between Fourier modes `r` and `p^2r` **before** diagonal scalarization, or leave the multiplier category entirely. Genuine Arthur/Maaß-Selberg truncation with constant-term subtraction, scattering coupling, an infinite all-prime completion, or another nonlocal global operation is not ruled out here.

## 1. Exact smooth commutator algebra

For real bounded `q`, define

\[
\delta_Lq(x)=q(x)-q(x+L),
\qquad
\delta_{-L}q(x)=q(x)-q(x-L).
\tag{12}
\]

Then

\[
A_L=M_{\delta_Lq}S_L,
\qquad
B_L=M_{\delta_{-L}q}S_{-L}.
\tag{13}
\]

Because `q` is real,

\[
A_L^*
=S_{-L}M_{\delta_Lq}
=-M_{\delta_{-L}q}S_{-L}
=-B_L.
\tag{14}
\]

Equation (3) follows by commuting `M_q` through the two terms of (1). Multiplying out and using

\[
V_p^*V_p=I,
\qquad
V_pV_p^*=Q_p
\tag{15}
\]

gives (4). Positivity is automatic because (4) is exactly `D_{p,q}^*D_{p,q}`; no sign has been inferred from the target Weil form.

The new cross terms are

\[
(V_p^*)^2\otimes A_L^*B_L
\quad\text{and}\quad
V_p^2\otimes B_L^*A_L.
\tag{16}
\]

They are the only difference from the sharp-support calculation of `WP-358`. Smoothness affects the height factors in (16), but the angular operators are forced to be the two-step Hecke shifts `V_p^{\pm2}`. No scalar `p^{-1/2}` appears.

## 2. The interference graph is exactly the `p²` orbit graph

For a pure Fourier mode,

\[
D_{p,q}(e_r\otimes f)
=
e_{pr}\otimes A_Lf
+\mathbf 1_{p\mid r}\,e_{r/p}\otimes B_Lf.
\tag{17}
\]

If `r\ne0`, then `pr=r/p` would imply `(p^2-1)r=0`, impossible. The two angular outputs are therefore orthogonal, proving (5). The disappearance of interference on a single nonzero mode is independent of the choice, width, monotonicity, or smoothness of `q`.

For a general finite Fourier superposition

\[
\psi=\sum_r e_r\otimes f_r,
\tag{18}
\]

the only possible collision between the forward and backward outputs occurs when

\[
pr=s/p,
\qquad\text{i.e.}\qquad
s=p^2r.
\tag{19}
\]

Accordingly,

\[
\begin{aligned}
\|D_{p,q}\psi\|^2
={}&\sum_r\|A_Lf_r\|^2
+\sum_{p\mid r}\|B_Lf_r\|^2\\
&+2\operatorname{Re}\sum_r
\langle A_Lf_r,B_Lf_{p^2r}\rangle.
\end{aligned}
\tag{20}
\]

This identifies the exact surviving coherence channel. A proposed smooth-boundary rescue that is diagonal in Fourier modes cannot use it. A non-diagonal rescue must explain why the source selects correlations on precisely these `p^2` links, how they assemble consistently for all primes, and why their sign is controlled independently of the desired Weil coefficient.

The constant mode `r=0` is exceptional because it is a fixed point of every `p^2` map. There (17) becomes `e_0\otimes(A_L+B_L)f`, returning to the constant-term/scattering frontier already separated in `WP-356`--`WP-357`. The present claim concerns the nonconstant escape opened by `WP-358`.

## 3. Nonconstant Fourier averaging removes all smooth interference

For `F_N^\circ` in (6), the range projection has exact finite density

\[
\tau_N^\circ(Q_p)
=\frac{\#\{r:0<|r|\le N,\ p\mid r\}}{2N}
=\frac{\lfloor N/p\rfloor}{N}.
\tag{21}
\]

On the other hand, `V_p^2e_r=e_{p^2r}` has no nonzero diagonal matrix element, so

\[
\operatorname{Tr}(F_N^\circ V_p^2F_N^\circ)=0.
\tag{22}
\]

The same is true for `(V_p^*)^2`. Applying `\tau_N^\circ` to (4) proves (8) exactly for every `N`, apart from the explicit finite density in (21).

This matters because smoothing does create genuine off-diagonal operator terms; simply saying “positive squares square amplitudes” would miss that new structure. Equation (8) shows why the most canonical diagonal scalarization nevertheless cannot benefit from it. The interference lives entirely off the Fourier diagonal, while the surviving arithmetic diagonal is still the density of `p\mathbb Z`.

More generally, any angular state that is diagonal in the Fourier basis annihilates the `V_p^{\pm2}` cross terms on the nonconstant sector. Such a state may assign a different mass to `Q_p`, but then the burden moves to the state itself: a critical mass `p^{-1/2}` must be independently source-forced. Smoothing the height boundary supplies no such law.

## 4. Fixed-width smoothings cannot repair the exponent through height mass

Assume now that `q` is a fixed bounded transition with constant tails:

\[
q(x)=q_-
\quad(x\le-R),
\qquad
q(x)=q_+
\quad(x\ge R).
\tag{23}
\]

For `L>2R`, the difference `q(x)-q(x+L)` is supported inside an interval of length `L+2R`. On the central interval

\[
R-L\le x\le -R,
\tag{24}
\]

of length `L-2R`, its value is exactly `q_- - q_+=-c`. The two remaining transition pieces have total length at most `4R` and bounded integrand. Hence

\[
m_q(L)=c^2(L-2R)+O_q(1)=c^2L+O_q(1),
\tag{25}
\]

proving (10). If `c=0`, the same argument gives the stronger `m_q(L)=O_q(1)`.

The height masses of the forward and backward pieces are equal by translation:

\[
\int|\delta_Lq(x)|^2dx
=
\int|\delta_{-L}q(x)|^2dx
=m_q(L).
\tag{26}
\]

Thus the flat local scalarization of (8) is

\[
m_q(L)\left(1+\frac1p\right).
\tag{27}
\]

The first term is the same forward boundary contribution present without the divisibility projection. The genuinely prime-specific angular correction is (11). Neither term carries the critical square-root density: the first has no decaying prime density at all, while the second has `p^{-1}`.

Allowing a different profile `q_p` for each prime could of course tune `m_{q_p}(\log p)` to almost any desired sequence. That is not a rescue inside this category unless the prime dependence is forced independently by the source. In particular, choosing transition widths or amplitudes so that `m_{q_p}(\log p)\asymp\sqrt p\log p` would simply reinsert the missing half-density through the cutoff.

## 5. Matched controls and aggressive falsification

**Independent displacement control.** Replace `L=\log p` in (1) by an arbitrary `L'>0` while keeping `V_p`. Equations (3)--(8) remain valid verbatim with `L'`. The positive commutator algebra therefore does not force the arithmetic relation between logarithmic displacement and divisibility density.

**Generic covering control.** Replace `V_p` by the circle covering isometry `V_m h(u)=h(mu)` for an arbitrary integer `m\ge2`. The same calculation gives a range projection of Fourier density `1/m` and cross interference only along `m^2` orbits. The operator mechanism is covering geometry, not a Riemann-specific positivity theorem.

**Sharp-cutoff limit.** Taking `q` to the characteristic cusp step makes `A_L` and `B_L` have disjoint output supports; the `p^2` cross terms vanish as operators and (4) reduces exactly to the `WP-358` square. The present theorem is therefore an extension of that result, not a competing normalization.

**Single-mode control.** Equation (5) shows that no amount of local smoothing changes the positive energy seen by a single nonconstant Fourier mode: one still gets a unit forward branch and a divisibility-gated unit backward branch.

**Coherent-superposition boundary.** Equation (20) is the genuine escape not killed here. A source-defined automorphic state may correlate modes `r` and `p^2r`; such correlations can contribute linearly before the final square is scalarized. Their coefficient and sign must be computed from that state rather than inferred from the present diagonal average.

**Nonlocal truncation boundary.** Arthur truncation is not merely multiplication by a fixed smooth function of cusp height: it acts through constant terms and subtraction operators tied to parabolic/scattering data. This finding does not identify it with `M_q` and does not claim to rule it out. It closes the local fixed-multiplier smoothing of the `WP-358` boundary response.

## 6. Prior-art and novelty audit

The normalized Hecke formula, its Fourier action, the self-adjoint Hecke algebra, and cusp-coordinate truncations are classical. The representation (1) and the divisibility projection `Q_p` were already recorded in `WP-358` from that standard automorphic technology. Classical Maaß-Selberg/Arthur theory is the relevant neighboring framework once one leaves local height multiplication and retains scattering/constant-term subtraction.

A bounded literature audit against Hecke Fourier formulas, cusp truncation, Arthur-Selberg truncation, transfer/isometry realizations, Bost-Connes divisibility projections, and Weil-positivity/trace-formula constructions found the classical ingredients but no independent theorem asserting the present Mathia-specific no-go. No novelty is claimed for Hecke theory, smooth multiplication commutators, or Fourier-density calculations separately.

The substantive contribution is the exact classification of the escape deliberately left open by `WP-358`: smoothing does create new terms, but those terms are forced onto `p^2` Fourier-orbit coherences; they vanish on every single nonzero mode and under the canonical nonconstant Fourier Følner readout, while the remaining fixed-width boundary mass is `O(\log p/p)` on the prime-specific branch. This is recorded as a negative route classification, not as a new positivity criterion.

## 7. Consequence for the Weil-positivity mandate

The direct cusp-boundary program now has a sharper fork. The constant mode is Brownian/universal (`WP-357`). The sharp nonconstant mode retains exact prime divisibility but its positive boundary square reads density `1/p` (`WP-358`). Fixed smooth height multipliers do not change that diagonal arithmetic exponent: they only add off-diagonal `p^2`-orbit interference, and fixed-width smoothing leaves the prime-specific flat boundary scale at `(\log p)/p`.

Therefore a useful continuation cannot merely replace the sharp cusp wall by a smoother local wall. It must either exploit a **source-forced coherent `p^2`-orbit state before diagonalization**, couple the Hecke boundary to scattering/constant-term data through genuine Maaß-Selberg/Arthur structure, or leave this local multiplier category for a global/adelic construction. Any surviving route still has to produce the archimedean Gamma and polar terms from the same structure and prove the final sign independently of RH or inserted zero data.
