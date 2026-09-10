# PF-263 — resonant mass Green tail keeps the pure recessive power

**Status:** `LITERATURE+DERIVED + RESONANT-FIXED-MASS-COMPLETION + GREEN-TAIL + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-262-massive-jacobi-resolvents-have-exact-double-root-indicial-law|PF-262]] derives the exact indicial roots for each parity block of the massive fixed-axis recurrence,

\[
\rho_\pm=-\frac12\pm\mu,
\qquad
\mu=\sqrt{1+a^2},
\]

and proves the fixed-source Green tail when `2\mu\notin\mathbb N`. Its remaining resonance caveat is not an obstruction for the Green column. In the integer-difference case, the standard coincident-root theorem preserves the ordinary asymptotic series for the **smaller/recessive indicial root**; the logarithm may enter only the independent dominant solution. Since a resolvent column belongs to `\ell^2`, it necessarily selects the pure recessive branch.

Consequently PF-262's fixed-source asymptotic extends to **every fixed mass `a>0`, including all resonant masses**:

\[
\boxed{
\langle e_{2j+\varepsilon},(L+a^2)^{-1}e_{2i+\varepsilon}\rangle
=C_{i,\varepsilon}(a)\,
j^{-1/2-\sqrt{1+a^2}}
\bigl(1+O(j^{-1})\bigr),
\qquad j\to\infty,
}
\]

for every fixed source index `i` and parity `\varepsilon\in\{0,1\}`. Thus resonance does not require deleting seam scales or weakening the decay exponent. The unresolved finite-seam problem is genuinely **family-uniform**: moving source index, mass-dependent connection coefficients, summation over the odd mass ladder, and preservation through the combined Robin map.

## Claim

Fix one parity block `L_\varepsilon` of the PF-247/PF-262 Jacobi operator and let `a>0` satisfy the resonant condition

\[
2\mu=m\in\mathbb N,
\qquad
\mu=\sqrt{1+a^2}.
\tag{1}
\]

Because `a>0`, one has `\mu>1` and therefore `m\ge3`. PF-262 reduces the homogeneous tail equation

\[
(L_\varepsilon+a^2)u=0
\tag{2}
\]

to the coincident-characteristic-value recurrence covered by DLMF §2.9(ii), with equal limiting characteristic root `1` and indicial roots

\[
\alpha_1=\rho_-=-\frac12-\mu,
\qquad
\alpha_2=\rho_+=-\frac12+\mu.
\tag{3}
\]

Their difference is exactly

\[
\alpha_2-\alpha_1=2\mu=m\in\mathbb N.
\tag{4}
\]

DLMF §2.9(ii), equations 2.9.12--2.9.13, states that in this integer-difference case the ordinary power asymptotic 2.9.12 still applies to the first solution, while the second independent solution may contain a logarithmic multiple of the first. With the ordering (3), this gives a genuine recessive solution

\[
\boxed{
u_-(j)=j^{-1/2-\mu}\left(1+O(j^{-1})\right),}
\tag{5}
\]

whereas an independent solution has leading dominant behavior

\[
u_+(j)=j^{-1/2+\mu}\left(1+O(j^{-1})\right)
+c\,u_-(j)\log j.
\tag{6}
\]

The logarithm in (6) is subordinate to the dominant power and does **not** contaminate (5).

For a fixed source index `i`, the column

\[
g_j=\langle e_{2j+\varepsilon},(L+a^2)^{-1}e_{2i+\varepsilon}\rangle
\tag{7}
\]

satisfies (2) for all sufficiently large `j`. Since `L+a^2\ge a^2>0`, the resolvent is bounded on `\ell^2`, so `(g_j)` is square summable. But

\[
\rho_+=-\frac12+\mu>\frac12,
\qquad
\rho_-=-\frac12-\mu<-\frac32.
\tag{8}
\]

Hence every solution with a nonzero dominant component fails to lie in `\ell^2`, while the recessive solution (5) lies in `\ell^2`. The Green column must therefore be a scalar multiple of `u_-` on the tail, proving the boxed asymptotic above in the resonant case.

The scalar is nonzero. If the recessive coefficient vanished, the Green column would vanish identically on a tail. The Jacobi off-diagonal coefficients are nonzero, so backward recurrence would then force the column to vanish up to the source, contradicting positivity of the diagonal resolvent matrix element

\[
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2i+\varepsilon}\rangle>0.
\tag{9}
\]

Combining this finding with PF-262 therefore gives the fixed-source power law for all `a>0`.

## Resonant seam scales are explicit but no longer exceptional

PF-261's finite-seam expansion uses

\[
a_k=\frac{(2k+1)\pi}{2rs},
\qquad k=0,1,2,\dots.
\tag{10}
\]

The `k`-th term is resonant precisely when

\[
2\sqrt{1+a_k^2}=m\in\mathbb N,
\qquad m\ge3.
\tag{11}
\]

Equivalently,

\[
\boxed{
rs=\frac{(2k+1)\pi}{\sqrt{m^2-4}}.
}
\tag{12}
\]

Equation (12) identifies the countable resonant seam scales exactly, but no exclusion is needed: the same recessive Green exponent applies there. This matters because the target in [[research/prime_flute/clues/CLUE-relative-seam-intrinsic-six-fractional-window|the accepted finite-seam clue]] requires a statement uniform in the physical seam scale; deleting a countable set would not have been an acceptable route to that target.

## Consequence for the finite-seam Green sum

PF-262 already shows that, for a fixed source row and a fixed nonresonant mass, larger mass improves the power exponent. The present result removes the only discrete exception to that statement. For every fixed `a>0`, resonant or not, the high-index Green column decays with exponent

\[
\frac12+\sqrt{1+a^2},
\tag{13}
\]

before PF-261's outer `A^{-1/4}` weight, and with exponent

\[
1+\sqrt{1+a^2}
\tag{14}
\]

on the high leg after that weight.

This still does **not** justify summing the odd-mass series termwise. The coefficient `C_{i,\varepsilon}(a)` is only pointwise in the fixed parameters. Nothing here controls it uniformly as `i` and `a` move, and a family of individually recessive solutions can have badly conditioned connection coefficients. The route therefore narrows to the exact missing quantity already exposed by PF-262: a uniform connection-coefficient estimate on a separated cone, strong enough to survive multiplication by the PF-261 mass weights and subsequent summation.

## Prior art and novelty audit

The resonance mechanism is classical. NIST DLMF §2.9(ii), *Difference Equations: Coincident Characteristic Values*, equations 2.9.11--2.9.13, gives the Birkhoff--Adams/Wong--Li integer-difference alternative used above. In particular, when the two indicial exponents differ by a nonnegative integer, the ordinary asymptotic expansion remains available for the first solution and the logarithmic term appears in the second independent solution. DLMF cites Wong and Li for proofs and Zhang et al. for error bounds.

Critical double-root Jacobi asymptotics are also standard; see J. Janas, S. Naboko, E. Sheronova, *Asymptotic Behavior of Generalized Eigenvectors of Jacobi Matrices in the Critical (Double Root) Case*, Z. Anal. Anwend. 28 (2009), 411--430, DOI `10.4171/ZAA/1391`.

No novelty is claimed for resonant Birkhoff--Adams theory, recessive-solution selection, or Green-function recurrence arguments. The project-specific content is the application of the integer-difference clause to PF-262's exact indicial pair, showing that the apparent resonance caveat in the precise massive Green family of PF-261 affects only the discarded dominant solution and therefore does not create an exceptional physical seam scale.

A targeted literature search found the general coincident-root and critical-Jacobi theory above, but no source for this Prime-Flute-specific substitution or for the subsequent family-uniform Green estimate. The latter remains open.

## Boundaries and falsification

1. **Fixed source and fixed mass.** The result is pointwise in `i` and `a`; it supplies no uniform bound for the connection coefficient `C_{i,\varepsilon}(a)`.
2. **No uniform resonance-neighborhood estimate.** Removing the exact integer-difference exception does not prove constants remain controlled as `a` varies through or between resonant values.
3. **No termwise mass summation.** PF-261's warning remains in force: the full odd-mass series must be estimated as a family before taking the weighted norm.
4. **No Robin-locality conclusion.** Even uniform locality of the relative seam must still be propagated through `X(I+X^*X)^{-1}` with source orientation retained.
5. **No actual-corridor or global conclusion.** Nothing here proves transport through the variable `K_a` corridor, the hypercycle deformation, PF-243 reassembly, scattering/determinants, a zeta-zero statement, or RH.

The claim would fail if the PF-262 recurrence did not satisfy the DLMF integer-difference hypotheses, if the smaller indicial branch acquired a leading logarithmic obstruction, or if a resolvent column could contain a nonzero dominant component while remaining in `\ell^2`. None occurs under the stated fixed-mass hypotheses.

## Decisive next test

Do not spend further effort separating resonant from nonresonant masses at the fixed-source level. Derive a **family-uniform connection-coefficient estimate** for

\[
\langle e_{2i+\varepsilon},(L+a^2)^{-1}e_{2j+\varepsilon}\rangle,
\qquad j\ge2i+2,
\]

with explicit dependence on `a` and `i` that remains controlled across the resonant values (12) and is summable after the PF-261 factor `a_k^2/(\sqrt{\kappa_i\kappa_j})`. The target remains preservation of some uniform strict `R>1` margin for the **summed** finite-seam operator and then for the combined Robin transform.