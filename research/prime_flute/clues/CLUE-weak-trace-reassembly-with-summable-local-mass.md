---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-220-coefficient-adjacent-low-recoupling-is-weak-trace-without-schur-locality.md
  - research/prime_flute/findings/PF-221-coefficient-weight-transfer-reduces-to-a-reciprocal-prime-schur-commutator.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-223-qualitative-cut-smoothing-does-not-force-weak-trace-schur-transport.md
  - research/prime_flute/findings/PF-225-one-seam-resolvent-dressing-saturates-raw-pant-hopping.md
  - research/prime_flute/findings/PF-226-thin-pants-force-inverse-seam-saturated-channel-multiplicity.md
  - research/prime_flute/findings/PF-227-fixed-physical-high-pass-does-not-remove-thin-pant-channel-multiplicity.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-230-hyperbolic-corridor-has-pi-over-s-axis-inverse-width-budget.md
  - research/prime_flute/findings/PF-231-ultraparallel-corridor-is-exactly-separable-in-logarithmic-coordinates.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent is not trace class by PF-112, while the remaining smooth decomposition-interface term has now been reduced to a much narrower operator. PF-220 closes coefficient-adjacent low sectors. PF-221 moves the physical reciprocal-prime envelope to the low endpoint except for

\[
P[D,\Omega]H
\quad\text{and its adjoint},
\qquad
\Omega=\bigoplus_nP_n^{-1}I_{\mathcal B_n},
\]

and PF-222 gives the exact norm-convergent prefix-flux expansion

\[
P[D,\Omega]H
=
\sum_{j\ge1}
\delta_j P[D,E_j]H,
\qquad
\delta_j=P_j^{-1}-P_{j+1}^{-1}>0.
\]

PF-223 proves that compactness, fixed-cut smoothing, finite-rank approximability, and qualitative low-rank information do not force the weak endpoint. PF-225 then supplies the exact dressed one-cut factorization and universal `1/2` cap, but PF-226 shows that the actual thin pant has order `s_j^{-1}` raw channels above a fixed threshold. PF-227 sharpens this: removing any fixed, or sufficiently slowly growing, physical-frequency sector does not remove that inverse-seam multiplicity. The endpoint therefore cannot be closed by raw channel counting or by declaring the dangerous band low frequency.

PF-228 changes the scale of the positive target. In the exact straight-corridor control, Schur dressing suppresses the inverse-seam band from order-one raw transmission to

\[
\rho_j:=\frac{\sqrt{w_jw_{j+1}}}{s_j},
\]

with the quantitative envelope `rho_j z/sinh(z)` in the scaled tangential frequency `z`. At canonical PF scales this makes the reciprocal-weighted top singular scale at most order `P_j^{-2}` and the orthogonal control family weak trace class even with the full inverse-seam channel population.

PF-229 removes generic scalar global shorting as the next obstruction: repeating a frozen PF-228 channel along a complete serial chain changes the isolated transmission by only a fixed factor, so the full prefix-to-tail cut block retains the same `w/s` scale and frequency envelope.

PF-230 then makes the neighboring-axis geometry exact in Fermi coordinates. It proves the nonconstant `cosh(t)` scaled width, survives PF-205 trimming on fixed windows, and calibrates the untrimmed axis inverse-width integral as `(pi+o(1))/s`. That rules out a naive claim that the actual fixed-window geometry itself becomes a constant-width strip.

PF-231 now removes the **axis fanout itself** from the list of candidate operator obstructions. The same complete ultraparallel corridor is exactly the logarithmic rectangle `(0,s) x (0,pi)` with metric `csc^2(theta)(dx^2+dtheta^2)`. For `-Delta+1`, its energy is exactly separable with transverse operator

\[
A=-\partial_\theta^2+\csc^2\theta,
\qquad
\sqrt{\lambda_m(A)}=m+\frac{1+\sqrt5}{2},
\]

and its form DtN matrix has the exact cylinder functional calculus

\[
K
\begin{pmatrix}
\coth(sK)&-\operatorname{csch}(sK)\\
-\operatorname{csch}(sK)&\coth(sK)
\end{pmatrix}.
\]

Thus the untrimmed hyperbolic axis corridor already has the same scaled `z/sinh(z)` transfer shape and an exact `O(s^{-1})` critical population. More importantly for the actual PF-205 interfaces, PF-231 gives their **global** logarithmic-coordinate equations

\[
x=f_{\rho_1}(\theta),
\qquad
x=s-f_{\rho_2}(\theta),
\qquad
f_\rho(\theta)=\operatorname{arsinh}(\sinh\rho\sin\theta),
\]

with width uniformly comparable to `s` on the entire `0<theta<pi` interval and an exact fixed-domain energy after straightening. The remaining one-cut geometry is therefore no longer an unspecified variable hyperbolic pant. It is a concrete thin Euclidean graph strip with explicit hypercycle boundaries, a singular but fixed transverse potential, and order-one tangential/transverse coupling after rescaling.

The smooth frontier remains two-stage, but the first stage is now sharper: prove or refute stability of PF-228's **normalized `w_j/s_j` Schur gain** under the explicit PF-205 hypercycle graph trim and real boundary-energy normalization; only after that solve the genuinely nested weak-`S_1` reassembly. The unsmoothed PF-204 route and the independent PF-183 true-short-collar route remain live alternatives.

## Research question

Can the exact prime/shift first relative resolvent be placed in

\[
\mathcal S_{1,\infty}
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, start from PF-231's exact logarithmic reduction rather than an abstract variable-width pant. Does replacing the separated axis boundaries by the explicit PF-205 hypercycle graphs preserve, after the real neighboring boundary-energy normalization, a dressed one-cut singular-value envelope with top scale `O(w_j/s_j)` on the inverse-seam band and sufficient decay beyond it? The comparison must be uniform through the critical tangential population `m=O(s_j^{-1})`, where the straightened coefficient `b_s/a_s` is only bounded, not small.

If such a one-cut estimate holds, can the overlapping nested expansion

\[
\sum_j\delta_jP[D,E_j]H
\]

then be reassembled in weak trace class without replacing the cuts by an artificial orthogonal direct sum? If the one-cut estimate fails, what concrete PF mechanism in the hypercycle trim, boundary normalizer, physical `P/H` split, neighboring-cell inhomogeneity, or global Schur inverse destroys the favorable dressed scale?

For the competing unsmoothed route, can PF-204's exact native two-Hilbert factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 excludes trace class, while the accumulated sector estimates would place the full comparison at the natural two-dimensional weak endpoint.

A negative answer is now more discriminating. Raw conductance, qualitative compactness, universal resolvent saturation, fixed-frequency truncation, generic scalar global shorting, and the apparent Fermi-coordinate fanout of the untrimmed hyperbolic axes have all been separated from the live obstruction. PF-231 shows that the complete axis corridor is exactly separable and that PF-205 trimming stays globally `O(s)`-thin without a hidden logarithmic width supply. Failure must therefore be traced to the actual normalized trimmed-boundary problem or to nested reassembly, rather than attributed generically to hyperbolic variable width.

## Decisive test

Start from PF-222's exact one-seam decoupling identity and retain PF-212's physical low/high split in its actual noncommutative order. Do not return to raw `B_j` trace budgets: PF-225--PF-227 show why those budgets are too crude.

For the first gate, use PF-231's logarithmic coordinates. The untrimmed axis problem is already diagonal in the Pöschl--Teller basis with exact cross-DtN factor `K csch(sK)`. Replace the axes by the actual PF-205 hypercycle graphs

\[
x=f_{\rho_j}(\theta),
\qquad
x=s_j-f_{\rho_{j+1}}(\theta),
\]

or equivalently use PF-231's fixed-domain quadratic form

\[
a_s^{-1}|v_X|^2
+a_s\left|v_\theta-(b_s/a_s)v_X\right|^2
+a_s\csc^2\theta|v|^2.
\]

The decisive comparison is a **uniform boundary-to-boundary estimate at the critical band `m=O(1/s_j)`**. It must show either that the real normalized Schur block still pays the `w_j/s_j` factor with corridor-type high-mode decay, or identify a canonical coupling in this explicit form that creates a larger dressed population. Since `a_s\asymp s` but `b_s/a_s=O(1)` rather than `o(1)`, a small-coefficient perturbation argument is not enough. The correct theorem may instead use coercive form comparison, a variable-strip Poisson estimate, microlocal diagonalization in the Pöschl--Teller basis, or another mechanism that is uniform at scaled frequency one.

PF-231 supplies two audit controls. First, the untrimmed problem already has exactly `O(s_j^{-1})` channels in each fixed scaled band, so an extra logarithmic multiplicity cannot be blamed on the axis fanout. Second, the trimmed logarithmic width satisfies `c s_j<=a_s(theta)<=s_j` globally. Neither statement by itself is a singular-value bound for the normalized trimmed operator.

A decisive negative result must exhibit the missing mechanism **inside this canonical PF geometry**. It is not enough to perturb an abstract positive matrix, repeat PF-223's generic multiplicity countermodel, or point again to PF-230's Fermi `cosh(t)` profile; PF-231 shows that profile is exactly conformally straightenable before the artificial trim.

If the actual one-cut envelope survives, attack the second gate separately: the PF-222 cuts are nested and overlap. Prove a direct Lorentz/weak-ideal estimate for the weighted flux series, exploit cancellation/commutator structure genuinely present, or derive another exact reassembly mechanism. PF-228's orthogonal direct-sum count and PF-229's single-cut serial theorem remain controls, not a proof of this final step.

As alternatives, attack PF-204's unsmoothed native factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately use one coherent global identification and one exact first-relative-resolvent identity; incompatible smooth and unsmoothed architectures cannot simply be combined to cover missing terms.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-228 proves the favorable `w/s` amplitude and frequency envelope only for an isolated straight-corridor control. PF-229 proves that the same envelope survives the full global cut only for a frozen scalar mode-preserving serial completion. PF-230 proves exact Fermi fanout and geometric inverse-width calibration. PF-231 proves that the **untrimmed** ultraparallel `-Delta+1` corridor is exactly separable in logarithmic coordinates and gives exact global equations for the PF-205 hypercycle trims; it does not prove that the normalized trimmed DtN/Poisson operator retains the PF-228 `w/s` factor.

In particular, PF-231's exact axis cross-DtN spectrum is stated in the conformal energy pairing and is not silently identified with the physical `P/H` boundary Hilbert spaces. Its trimmed fixed-domain form contains order-one tangential/transverse coupling at the critical scaled frequency, so exact axis separability does not remove the need for a genuine variable-boundary operator theorem.

Conversely, PF-226/PF-227 prove large raw channel multiplicity in the actual pant but do not show that those channels survive Schur dressing at order one. PF-225's universal `1/2` cap is an upper bound, not evidence that saturation is attained. The current clue therefore asserts only that the explicit PF-205 hypercycle-normalized dressed cut comparison and subsequent nested reassembly are precise, evidence-backed targets.

PF-204's unsmoothed endpoint and the PF-183 true-short-collar endpoint remain unresolved. Clue acceptance does not imply wave-operator completeness, scattering-matrix or determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`, with the smooth one-cut gate narrowed from a generic variable-hyperbolic comparison to an explicit hypercycle-boundary problem. PF-231 shows that before PF-205 trimming the neighboring-axis corridor is exactly separable and already has the corridor `z/sinh(z)` transfer law with `O(s^{-1})` scaled channel count. The next Research Watch step is therefore to control the **PF-205 trimmed logarithmic graph strip plus its actual boundary normalizers** uniformly through `m=O(1/s)`, and decide whether PF-228's normalized `w/s` gain survives. Nested weak-`S_1` reassembly remains a separate second gate after that comparison.