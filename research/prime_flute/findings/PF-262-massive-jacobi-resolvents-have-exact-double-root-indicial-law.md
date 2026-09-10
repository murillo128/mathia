# PF-262 — massive Jacobi resolvents have an exact double-root indicial law

**Status:** `EXACT-DERIVED + LITERATURE-BIRKHOFF-ADAMS + FIXED-MASS-GREEN-TAIL + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] gives the exact parity-Jacobi matrix of the compactified complete-axis operator `L`, while [[research/prime_flute/findings/PF-261-finite-seam-crossover-is-a-bounded-positive-mixture-of-massive-axis-resolvents|PF-261]] reduces every off-diagonal finite-seam matrix element to a sum of Green matrices `(L+a_k^2)^{-1}`. The first unresolved question in PF-261 is therefore the mode-index tail of one massive Green matrix before attempting uniformity in the mass ladder and in two moving mode indices.

That single-mass problem has an exact asymptotic calibration. After passing to either parity chain, the recurrence for `(L+a^2)u=0` is a **coincident-characteristic-value (double-root) difference equation**. The first-order perturbation is exactly degenerate in the Birkhoff--Adams sense, and the second-order indicial equation is

\[
\boxed{
\left(\rho+\frac12\right)^2=1+a^2.
}
\]

Thus, with `\mu=\sqrt{1+a^2}`, the two formal power indices are

\[
\boxed{
\rho_\pm=-\frac12\pm\mu.
}
\]

For nonresonant fixed mass `2\mu\notin\mathbb N`, the standard coincident-root theorem recorded in NIST DLMF §2.9(ii) upgrades these indices to two genuine asymptotic solutions. Since a resolvent column is in `\ell^2`, its tail selects the decaying branch, so for every fixed source index in one parity sector

\[
\boxed{
\langle e_{2j+\varepsilon},(L+a^2)^{-1}e_{2i+\varepsilon}\rangle
=C_{i,\varepsilon}(a)\,j^{-1/2-\sqrt{1+a^2}}\bigl(1+O(j^{-1})\bigr),
\qquad j\to\infty,
}
\]

for nonresonant `a>0`. After PF-261's outer `A^{-1/4}` factor on the high mode, a fixed-mass contribution to the finite-seam relative operator therefore has fixed-low-row tail `j^{-1-\sqrt{1+a^2}}`.

This is strong decay, and the exponent grows monotonically with mass. It shows that **one fixed low row and one fixed massive resolvent are not the finite-seam obstruction**. The live difficulty is now sharply localized to what this theorem does not provide: constants uniform in a moving low index, uniformity through the odd mass ladder, resonant masses, summation before the weighted norm, and preservation through the combined Robin source map.

## Claim

Let

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad n_j=2j+\varepsilon,
\qquad \varepsilon\in\{0,1\},
\]

and write the PF-247 parity block of `L` as

\[
(L_\varepsilon u)_j
=p_{j-1}^{(\varepsilon)}u_{j-1}
+q_j^{(\varepsilon)}u_j
+p_j^{(\varepsilon)}u_{j+1},
\]

with negative off-diagonal entries. Direct expansion of PF-247's exact rational/Gegenbauer coefficients gives

\[
p_j^{(\varepsilon)}
=-j^2-c_\varepsilon j-d_\varepsilon+O(j^{-1}),
\qquad
q_j^{(\varepsilon)}
=2j^2+2(\alpha+\varepsilon)j+f_\varepsilon+O(j^{-1}),
\]

where

\[
c_\varepsilon=\alpha+1+\varepsilon,
\]

\[
d_0=\frac{3+12\alpha}{16},\qquad
d_1=\frac{15+20\alpha}{16},
\]

and

\[
f_0=\frac{9+4\alpha}{8},\qquad
f_1=\frac{13+12\alpha}{8}.
\]

The load-bearing cancellation is parity independent:

\[
\boxed{
c_\varepsilon-1-2d_\varepsilon+f_\varepsilon=\frac34.}
\]

For fixed `a>0`, divide `(L_\varepsilon+a^2)u=0` by `p_j^{(\varepsilon)}`. It becomes

\[
u_{j+1}+F_j u_j+G_j u_{j-1}=0,
\]

with

\[
F_j=-2+\frac2j-\frac{c_\varepsilon+7/4+a^2}{j^2}+O(j^{-3}),
\]

\[
G_j=1-\frac2j+\frac{c_\varepsilon+1}{j^2}+O(j^{-3}).
\]

The limiting characteristic polynomial is `(z-1)^2`. In the notation of DLMF §2.9(ii), `f_0=-2`, `f_1=2`, `g_0=1`, `g_1=-2`, so

\[
2g_1=f_0f_1=-4.
\]

This is exactly the degenerate coincident-root case rather than the generic `\exp(\pm c\sqrt j)` case. DLMF equation 2.9.11 gives the index equation

\[
2\rho^2+2\rho-\frac32-2a^2=0,
\]

which is equivalent to the boxed indicial law above.

When `2\sqrt{1+a^2}\notin\mathbb N`, DLMF equation 2.9.12 gives two independent solutions with the corresponding power asymptotics. A resolvent column is square-summable, while the `\rho_+` branch grows because `\mu>1`; hence the Green tail is proportional to the `\rho_-` branch. This proves the displayed fixed-source asymptotic in the nonresonant case.

## Why this matters for the finite-seam sum

PF-261's odd masses are

\[
a_k=\frac{(2k+1)\pi}{2rs},
\qquad
\mu_k=\sqrt{1+a_k^2}.
\]

At the level of the indicial exponent, every higher `k` is **more local** in mode index than the first mass. In particular, for a fixed source row the slowest individual power is associated with `k=0`, and the external high-mode `A^{-1/4}` factor improves `j^{-1/2-\mu_k}` to `j^{-1-\mu_k}`.

This does not permit termwise summation of PF-261's series. The constants `C_{i,\varepsilon}(a)` are not controlled here uniformly in `i` or `a`, and the PF-261 summands carry the additional factor `a_k^2`. A family of individually fast tails can still fail to give the required weighted operator estimate if those constants deteriorate in the coupled region `i,j,a_k\to\infty`.

The result therefore changes the decisive test rather than completing it: the next estimate should target **uniform Green-function connection coefficients** in the separated cone, not rediscover fixed-row decay.

## Prior art and novelty audit

The asymptotic theory is classical. NIST DLMF §2.9(ii), *Difference Equations: Coincident Characteristic Values*, records the Birkhoff--Adams/Wong--Li classification. In the degenerate condition `2g_1=f_0f_1`, its equation 2.9.11 gives the power indices and equation 2.9.12 gives the corresponding asymptotic solutions away from integer index resonance; DLMF cites Wong and Li for proofs and Zhang et al. for error bounds.

The same critical double-root phenomenon is standard in spectral theory of unbounded Jacobi matrices; see J. Janas, S. Naboko, E. Sheronova, *Asymptotic Behavior of Generalized Eigenvectors of Jacobi Matrices in the Critical (Double Root) Case*, Z. Anal. Anwend. 28 (2009), 411--430, DOI `10.4171/ZAA/1391`.

No novelty is claimed for Birkhoff--Adams theory or for power asymptotics of critical Jacobi recurrences. The project-specific content is the exact substitution of PF-247's compactified-axis coefficients, the parity-independent `3/4` cancellation, and the resulting mass law `\rho_\pm=-1/2\pm\sqrt{1+a^2}` for the precise Green family that PF-261 identified as the finite-seam crossover.

## Boundaries and falsification

1. **Nonresonant theorem only.** The displayed two-branch Green asymptotic uses `2\mu\notin\mathbb N`. DLMF treats integer index differences separately and allows a logarithmic term in one independent solution. The resonant case must be handled before claiming a family-uniform mass theorem.
2. **Fixed source only.** The deduction that the Green column selects the decaying branch holds for fixed `i`. It gives no uniform control when `i` grows with `j` or with `a`.
3. **No termwise norm summation.** The result does not override PF-261's warning that the odd-mass series must be summed with control of its mass-dependent constants.
4. **Relative seam is not the Robin source map.** Even a uniform theorem for `\mathcal R_{s,r}^0` would still have to be propagated through `X(I+X^*X)^{-1}` without discarding source orientation.
5. **No actual-corridor or global conclusion.** Nothing here transfers to the variable `K_a` corridor, the hypercycle deformation, PF-243 reassembly, scattering/determinants, zeta zeros, or RH.

## Decisive next test

Use the exact recurrence above to derive a **uniform connection-coefficient estimate** for

\[
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle
\]

when `j\ge2i+2`, with constants explicit enough in `a` and `i` to sum PF-261's odd mass ladder after multiplication by `a_k^2/(\sqrt{\kappa_i\kappa_j})`. Treat the resonant set `2\sqrt{1+a^2}\in\mathbb N` rather than deleting it. The route advances only if the **summed** estimate retains some uniform strict `R>1` margin through the combined Robin transform.