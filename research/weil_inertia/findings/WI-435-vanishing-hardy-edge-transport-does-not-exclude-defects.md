# WI-435 — vanishing Hardy edge transport does not exclude defects

Status: `EXACT-DERIVED + DECISIVE-BARRIER + CORRECTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-430`, `WI-431`, `WI-433`, `WI-434`

## Claim

The live conclusion drawn after `WI-433`--`WI-434` needs a correction. Controlling the transported height-edge term, even all the way to `o(1)`, is **not by itself a defect-to-zero bootstrap**. In the exact transport identity, a vanishing safe-line term and a vanishing edge term force the interior positive Hardy component to converge to the residue/Blaschke defect signal; they do not force that signal to vanish.

Write the `WI-433` transport schematically as

\[
H_{\sigma,T}=S_{\sigma,T}+E_{\sigma,T}-R_{\sigma,T},
\tag{1}
\]

where, for a broad height window `chi_T`,

\[
S_{\sigma,T}
=e^{-(\sigma_0-\sigma)D}H_{\sigma_0,T},
\qquad
E_{\sigma,T}
=-i\int_\sigma^{\sigma_0}e^{-(u-\sigma)D}K_{u,T}\,du,
\tag{2}
\]

and

\[
R_{\sigma,T}(\xi)
=2\pi 1_{\xi>0}
\sum_{\sigma<\beta_\rho<\sigma_0}
 m_\rho\chi_T(\gamma_\rho)
 e^{-(\beta_\rho-\sigma)\xi}e^{-i\gamma_\rho\xi}
\tag{3}
\]

is the explicit crossed-zero residue signal. Equation (1) immediately gives

\[
S_{\sigma,T}=o(1),\quad E_{\sigma,T}=o(1)
\quad\Longrightarrow\quad
H_{\sigma,T}+R_{\sigma,T}=o(1),
\tag{4}
\]

not `R_{sigma,T}=o(1)`. The first-defect quantum of `WI-430` is a **lower bound on this same Hardy/Blaschke defect component**. It is perfectly compatible with (4): if a defect exists, the interior Hardy component simply retains the corresponding nonzero quantum.

This logical obstruction is realized exactly by every finite Kunik Blaschke block. Let

\[
\rho_j=\beta_j+i\gamma_j,
\qquad \beta_j>\frac12,
\]

with multiplicities `m_j`, and let

\[
G_Z(s)
:=
\sum_{j=1}^J m_j
\left(
\frac1{s-\rho_j}
-
\frac1{s-(1-\bar\rho_j)}
\right).
\tag{5}
\]

Fix

\[
\frac12<\sigma<1<\sigma_0,
\qquad
\sigma\ne\beta_j,
\tag{6}
\]

and take `chi in C_c^infty(R)` with `chi(0)=1`, `|chi|<=1`, and

\[
\chi_T(t)=\chi(t/T).
\tag{7}
\]

Define

\[
H_{u,T}
:=P_+\bigl(\chi_T(t)G_Z(u+it)\bigr)
\tag{8}
\]

with the Plancherel-normalized Hardy norm used in `WI-434`. Then, as `T -> infinity`,

\[
\boxed{
H_{\sigma_0,T}\longrightarrow0,
}
\tag{9}
\]

\[
\boxed{
H_{\sigma,T}\longrightarrow-R_\sigma,
}
\tag{10}
\]

where

\[
R_\sigma(\xi)
=2\pi 1_{\xi>0}
\sum_{\beta_j>\sigma}
 m_j e^{-(\beta_j-\sigma)\xi}e^{-i\gamma_j\xi},
\tag{11}
\]

and, crucially, the **entire transported edge term** satisfies

\[
\boxed{
E_{\sigma,T}\longrightarrow0
}
\tag{12}
\]

in `L^2(xi>0)`. Thus a nonzero deeper defect coexists with asymptotically zero safe-line leakage and asymptotically zero full edge transport. For one zero of depth

\[
\delta=\beta-\sigma>0,
\]

the surviving defect energy is exactly

\[
\boxed{
\|R_\sigma\|_{\mathcal H}^2
=
\frac{\pi m^2}{\delta}>0,
}
\tag{13}
\]

while both terms that `WI-433` proposed to make small tend to zero.

Therefore proving that the **regular remainder** left open in `WI-434` is `o(1)` would still not imply RH, exclude one off-line zero, or contradict the `WI-430` quantum. It would only recover, in the broad-window limit, the global Hardy/Blaschke identity already isolated in `WI-429`--`WI-431`.

The next viable gate must contain genuinely additional information: an independently justified upper bound on the interior localized Hardy component itself, or a mixed-frequency/source functional whose coercivity is not already saturated by the finite Blaschke model. Edge control can remain an auxiliary estimate, but it is not the missing bootstrap on its own.

## 1. Exact finite-Blaschke countermodel

For `c>0`, the Fourier convention of `WI-429` gives

\[
\widehat{\frac1{c+i(t-\gamma)}}(\xi)
=
2\pi e^{c\xi}e^{-i\gamma\xi}1_{\xi<0},
\tag{14}
\]

whereas for `b>0`,

\[
\widehat{\frac1{-b+i(t-\gamma)}}(\xi)
=
-2\pi e^{-b\xi}e^{-i\gamma\xi}1_{\xi>0}.
\tag{15}
\]

On the safe line `u=sigma_0>1`, both denominators in every summand of (5) have positive real part. Hence

\[
P_+G_Z(\sigma_0+i\,\cdot)=0.
\tag{16}
\]

On the interior line `u=sigma`, the reflected denominator still has positive real part, while the direct denominator changes Hardy orientation exactly when `beta_j>sigma`. Therefore

\[
\widehat{P_+G_Z(\sigma+i\,\cdot)}(\xi)
=-R_\sigma(\xi).
\tag{17}
\]

Because `Z` is finite and no endpoint line crosses a pole, both vertical-line functions in (16)--(17) belong to ordinary `L^2(dt)`. The windows satisfy `chi_T(t)->1` pointwise and `|chi_T|<=1`. Dominated convergence gives

\[
\|(\chi_T-1)G_Z(u+i\,\cdot)\|_2\to0
\qquad(u=\sigma,\sigma_0).
\tag{18}
\]

Since `P_+` has operator norm one, (18) and (16)--(17) prove (9)--(10).

For every fixed ordinate `gamma_j`, (7) gives

\[
\chi_T(\gamma_j)\to1.
\tag{19}
\]

Hence the finite residue sum in the localized `WI-433` identity converges in the Hardy norm:

\[
R_{\sigma,T}\to R_\sigma.
\tag{20}
\]

Now solve (1) for the full edge term:

\[
E_{\sigma,T}
=H_{\sigma,T}-S_{\sigma,T}+R_{\sigma,T}.
\tag{21}
\]

The semigroup in `S_{sigma,T}` is a contraction, so (9) gives `S_{sigma,T}->0`. Combining (10), (20), and (21) proves (12) without estimating `K_{u,T}` at all.

This point is stronger than the principal-part regularization in `WI-434`: for a finite Blaschke defect configuration, **the complete transported edge term, including the regular remainder, vanishes in the adiabatic limit**. That is not a victory against the defect. It is exactly what must happen for the localized transport identity to converge to the global Hardy factorization.

## 2. The first-defect quantum is compatible with vanishing edge forcing

For one zero with `delta=beta-sigma>0`, equation (15) gives

\[
R_\sigma(\xi)
=2\pi m e^{-\delta\xi}e^{-i\gamma\xi}1_{\xi>0}.
\tag{22}
\]

Thus

\[
\begin{aligned}
\|R_\sigma\|_{\mathcal H}^2
&=
\frac1{2\pi}\int_0^\infty
4\pi^2m^2e^{-2\delta\xi}\,d\xi\\
&=
\frac{\pi m^2}{\delta},
\end{aligned}
\tag{23}
\]

which is exactly the one-defect tariff behind `WI-429`--`WI-430`. Equations (9) and (12) simultaneously give

\[
\|S_{\sigma,T}\|_{\mathcal H}	o0,
\qquad
\|E_{\sigma,T}\|_{\mathcal H}	o0.
\tag{24}
\]

So there is no inequality of the form

\[
\text{small safe source}+
\text{small edge forcing}
\Longrightarrow
\text{small defect energy}
\tag{25}
\]

at the level of the `WI-433` transport interface. The countermodel has the left-hand side tending to zero while the right-hand defect energy stays at the positive value (23).

Algebraically the reason is already visible in (1). Rearranging gives

\[
R_{\sigma,T}
=S_{\sigma,T}+E_{\sigma,T}-H_{\sigma,T}.
\tag{26}
\]

An upper bound for `R` therefore requires control of **all three** terms on the right. Bounds only on `S` and `E` leave `H` free to equal `-R`, which is precisely what (10) says. In fact small `S` and `E` make the interior Hardy component a *better approximation* to the defect signal.

This also shows why `WI-430` does not supply the missing opposite inequality. Its quantum is a lower bound for the norm of the same positive-frequency defect component. Combining a lower bound for `R` with the asymptotic identity `H=-R+o(1)` gives a lower bound for `H`, not a contradiction.

## 3. Relation to `WI-431` and correction of the live frontier

`WI-431` had already identified the bare global positive-frequency component correctly:

\[
P_+F(\sigma_0+i\,\cdot)=0
\qquad(\sigma_0>1),
\tag{27}
\]

while on an interior line Kunik's factorization puts the opposite Hardy component entirely in the Blaschke/zero factor. The localization commutator was therefore identified there as the only place where an independent source-side mixing mechanism might enter.

`WI-433` then derived the exact horizontal transport and correctly exposed the edge forcing term. `WI-434` correctly proved that its crossed-pole singularities disappear after semigroup transport. What does **not** follow is the subsequent research heuristic that making the remaining edge term small could, by itself, be compared with the `WI-430` quantum to eliminate residues.

The finite-block limit above falsifies that heuristic in its strongest form: one may grant the desired conclusion

\[
E_{\sigma,T}=o(1)
\tag{28}
\]

for the entire edge term, not merely for its principal part, and a nonzero defect survives unchanged. Thus the regular-edge problem in `WI-434` is no longer the primary missing theorem by itself.

A productive continuation must add a source inequality not contained in the transport identity. Examples of logically adequate targets include:

- an independently established subquantum upper bound for a predetermined localized interior `P_+(chi_T F_sigma)` family;
- a coercive mixed positive/negative-frequency identity whose arithmetic side is fixed on a safe line and whose finite-Blaschke model cannot saturate it;
- a boundary or explicit-formula observable that bounds the interior Hardy norm without using reciprocal distances to the same right-half zeros.

Any such proposal must be stress-tested against (5)--(13). If the same finite Blaschke block can have vanishing source/edge errors while retaining its Hardy quantum, then the proposed quantity has not added independent information.

## 4. Symmetry, multiplicity, and scope

The countermodel is not relying on an isolated unsymmetrized Cauchy pole. Equation (5) is exactly the logarithmic derivative of a finite Kunik Blaschke subproduct: each right-half zero is paired with its functional-equation reflection `1-bar(rho)`. Conjugate ordinates may also be included in `Z` without changing the argument. Multiplicity enters linearly in the amplitudes and quadratically in the one-defect energy (23).

Critical-line zeros do not enter the right-half residue current and are not reclassified as off-line defects. The barrier concerns only the proposed inference from source/edge smallness to absence of right-half zeros.

The finite-block construction is not asserted to be the full zeta logarithmic derivative. That limitation does not weaken the logical no-go. A proof using only the transport identity plus bounds on `S` and `E` has no term capable of distinguishing the zeta object from (5). To escape the countermodel it must invoke an additional zeta-specific source constraint, and that additional constraint is exactly the missing mathematical content.

Nor does the result say that the full zeta edge term is `o(1)`. It says something sharper for proof design: **even if that estimate were granted, it would not close the defect-to-zero argument.** The only useful role of an edge estimate is inside a larger source inequality that also controls the interior detector independently.

## Prior art and novelty audit

No novelty or priority claim is made for the Hardy-space ingredients.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829, https://arxiv.org/abs/0804.4829, supplies the half-plane Poisson--Schwarz/Blaschke factorization used in `WI-429`--`WI-431`. Its factorization explicitly separates critical-line/outer data from Blaschke zero factors, which is the classical structural reason that the opposite Hardy component can simply be the zero divisor rather than an independent source bound.
- Jean-Francois Burnol, *An adelic causality problem related to abelian L-functions*, arXiv:math/0001013, https://arxiv.org/abs/math/0001013, gives classical neighboring prior art in which causality of a scattering construction is equivalent to RH. It reinforces the methodological warning that a Hardy/causality component produced by continuation can itself encode the bad zeros; causality is not a free source inequality.
- Paley--Wiener theory for half-plane Hardy spaces, the Cauchy-kernel Fourier supports (14)--(15), contractivity of the Riesz projection, and dominated convergence are classical.
- `WI-431` is the closest repository-local predecessor and already states that the bare positive Hardy source is residue-only and that a genuinely independent localization/mixing estimate is essential. The new content here is the exact **counterexample to the later edge-only bootstrap heuristic**: adiabatic localization of every finite Kunik Blaschke block has both safe-line leakage and full transported edge forcing tending to zero while its interior defect quantum remains nonzero.

A targeted prior-art search around Kunik factorization, half-plane Paley--Wiener/Riesz projection, Cauchy--Pompeiu transport, and Burnol causality did not locate this exact adiabatic finite-Blaschke no-go packaged as a theorem for the present transport program. Absence from that search is not evidence of priority.

## Stress tests and falsification

1. **Signs.** Under the Fourier convention of `WI-429`--`WI-434`, the deeper direct Cauchy pole has positive-frequency transform `-R_sigma`. Hence the transport identity tends to `H_sigma=-R_sigma`; the edge term tends to zero. Reversing the residue sign would destroy (21) and is a direct falsification test.

2. **No hidden noncompact window step.** The proof uses compactly supported `chi_T` for every finite `T`. The limit is justified in ordinary `L^2` for finite Blaschke blocks by dominated convergence and norm-one projection; `chi=1` is never inserted as a finite-stage cutoff.

3. **No uniform statement over growing zero sets.** The argument fixes a finite block before taking `T->infinity`. It does not prove that the full zeta edge term vanishes uniformly when the number of zeros in the window grows with `T`.

4. **That limitation is irrelevant to the no-go.** The claimed bootstrap was supposed to turn sufficiently small edge forcing into exclusion of even one defect. A one-block model with exactly that smallness and a surviving quantum disproves the implication unless additional zeta-specific data are used.

5. **`WI-434` remains mathematically valid.** Its semigroup cancellation and principal-part estimates are not contradicted. What changes is their consequence for the program: regularizing or even eliminating the edge forcing does not provide the missing upper bound on the interior defect detector.

6. **The escape condition is falsifiable.** A proposed continuation of this branch must identify an additional quantity that is independently controlled for zeta and fails, quantitatively, on a nonzero finite Blaschke block. If it cannot do so, it is another rewriting of the same residue identity.

## Consequence for the research line

The edge-only Hardy transport route is closed as a defect-to-zero mechanism. `WI-433` remains the correct bookkeeping identity and `WI-434` remains the correct pole-regularization result, but the previous live target was insufficient: **small edge forcing plus small safe-line leakage does not compete with the first-defect quantum; it reconstructs it.**

The next source-to-defect attempt should therefore return to the independence gate already visible in `WI-431`: obtain an unconditional source-side upper bound for the interior localized Hardy detector, or introduce a genuinely new mixed-frequency invariant that the finite Kunik Blaschke model cannot reproduce. Any future edge estimate should be treated only as an error-control lemma inside such a stronger argument.