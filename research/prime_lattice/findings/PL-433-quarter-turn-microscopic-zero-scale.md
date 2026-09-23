# PL-433 — The shrinking quarter-turn is a fixed microscopic zero displacement on polynomial short-interval scales

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PAIR-CORRELATION-SCALING + ANALYTIC-BARRIER-REFINEMENT`.

**Parent findings:** `PL-421`, `PL-428`, `PL-429`, `PL-431`, `PL-432`.

## Claim

`PL-431` and `PL-432` reduce recovery of the three hidden mod-5 coherences to one oriented vertical sample at

\[
t_X=-\frac{\pi}{2\log X}.
\tag{1}
\]

Because `t_X -> 0`, it is tempting to regard the remaining shifted arithmetic estimate as a perturbative continuity problem around the unshifted variance. That interpretation is misleading on the zero-correlation scale naturally associated with short intervals.

At the power scale

\[
h=X^{\theta+o(1)},\qquad 0<\theta<1,
\tag{2}
\]

the classical Goldston--Montgomery / Selberg-class variance--pair-correlation dictionary places the relevant zero height at

\[
T=X^{1-\theta+o(1)}\asymp X/h
\quad\text{at exponent scale}.
\tag{3}
\]

Zeros of a fixed-conductor degree-one `L`-function near height `T` have mean ordinate spacing

\[
\Delta_T\sim\frac{2\pi}{\log T}.
\tag{4}
\]

Therefore the quarter-turn shift (1), measured in local zero spacings, satisfies

\[
\boxed{
\frac{t_X}{\Delta_T}
= -\frac{\log T}{4\log X}+o(1)
\longrightarrow
-\frac{1-\theta}{4}.
}
\tag{5}
\]

Thus the second scalar sample approaches the unshifted point in the original `t` coordinate while remaining a **nonzero fixed microscopic displacement of the zero process** whenever the short interval is polynomially shorter than `X`.

Equivalently, the remaining analytic target after `PL-432` is not naturally a first-order continuity estimate in the zero statistics. In the standard microscopic normalization it asks for control of a mixed zero-correlation observable at a fixed offset. This does not prove that such control is necessary for every possible prime-side proof, but it rules out the heuristic that `t_X=o(1)` alone makes the zero-side deformation negligible.

## 1. Vertical translation moves the zero-difference variable exactly

For a character channel `chi_k`, the shifted factor used in `PL-429` is

\[
L(s+it,\chi_k).
\tag{6}
\]

If `rho_k=beta_k+i gamma_k` is a zero of `L(s,chi_k)`, then the corresponding zero of (6) is

\[
rho_k-it=\beta_k+i(\gamma_k-t).
\tag{7}
\]

Hence, when this channel is paired with an unshifted zero `rho_j=beta_j+i gamma_j`, the ordinate difference changes by

\[
\gamma_j-(\gamma_k-t)
=(\gamma_j-\gamma_k)+t.
\tag{8}
\]

No RH or GRH is needed for this translation identity. Those hypotheses enter only if one identifies all nontrivial zeros with ordinates on the critical line and invokes the standard pair-correlation theorems formulated there.

For the mod-5 route, Kandhil--Languasco--Moree use precisely mixed Dirichlet-`L` zero differences `gamma_1-gamma_2`. Their microscopic pair-correlation normalization counts differences on intervals of the form

\[
\frac{2\pi\alpha}{\log T}
\le
\gamma_1-\gamma_2
\le
\frac{2\pi\beta}{\log T}.
\tag{9}
\]

Thus the natural dimensionless displacement produced by a vertical translation is

\[
u(t,T):=\frac{t\log T}{2\pi}.
\tag{10}
\]

At the quarter turn,

\[
\boxed{
u(t_X,T)=-\frac{\log T}{4\log X}.}
\tag{11}
\]

The fixed modulus only changes lower-order terms in the zero density; replacing `log T` by `log(qT)` gives the same limit for fixed `q=5`.

## 2. The short-interval dictionary makes the displacement macroscopic in local units

The classical variance--pair-correlation correspondence is most transparent at the exponent level. Write the relative interval length as

\[
\delta=\frac{h}{X}=X^{-B+o(1)},
\qquad B=1-\theta.
\tag{12}
\]

Bui--Keating--Smith formulate the Selberg-class transfer with pair-correlation ranges

\[
T^{A_1}\ll X\ll T^{A_2}
\tag{13}
\]

corresponding to relative short-interval ranges

\[
X^{-B_2}\ll\delta\ll X^{-B_1},
\qquad B\simeq A^{-1}.
\tag{14}
\]

Consequently, at a fixed power scale `delta=X^{-B+o(1)}`, the associated zero height obeys

\[
T=X^{B+o(1)}=X^{1-\theta+o(1)}.
\tag{15}
\]

Substituting (15) into (11) gives

\[
u(t_X,T)
=-\frac{B}{4}+o(1)
=-\frac{1-\theta}{4}+o(1),
\tag{16}
\]

which proves (5).

The important distinction is between absolute and microscopic scales:

\[
|t_X|\asymp\frac1{\log X}\to0,
\qquad
\Delta_T\asymp\frac1{\log T}\asymp\frac1{\log X},
\tag{17}
\]

so their ratio does not tend to zero at a polynomial short-interval scale. The quarter-turn becomes small only because the entire local zero spacing is shrinking at the same logarithmic rate.

This also identifies the exceptional regime. If

\[
\log(X/h)=o(\log X),
\tag{18}
\]

for example `h=X^{1-o(1)}`, then `log T=o(log X)` in this scale dictionary and `u(t_X,T)->0`. Only there does the second sample become perturbatively close on the microscopic zero scale. The current statement deliberately does not claim a fixed nonzero displacement in that near-macroscopic interval regime.

## 3. Consequence for the PL-421 / PL-432 route

`PL-432` shows that the **prime-side transport** from the unshifted complex covariance to the quarter-turn source is well conditioned: after Abel--Stieltjes summation its deterministic error is controlled by ordinary multiscale short-interval `L^2` norms, with the artificial coefficient `ell^1` mass removed.

The present calculation shows that the **zero-side interpretation** has a different character. If a proof tries to obtain the required oriented sample by transferring the scalar statistic to zero correlations, then the deformation it must control is not infinitesimal after the natural local rescaling. For `h=X^{theta+o(1)}` it is a mixed correlation at the fixed normalized offset

\[
u_*=-\frac{1-\theta}{4}.
\tag{19}
\]

Therefore a theorem known only at `t=0` cannot be promoted to the quarter-turn sample merely from ordinary continuity in an unscaled `t` variable. Any such promotion needs a modulus of continuity strong enough on the `1/log T` microscopic scale, or a direct estimate at the shifted point. This sharpens the warning already present in `PL-431`: the required second point tends to zero, but it does so at exactly the scale on which zero differences remain nontrivial.

For mixed character channels this calibration is especially apt. Kandhil--Languasco--Moree define a cross-pair statistic over zeros of `L(s,chi_1)` and `L(s,chi_2)`, so (8) acts directly as a translation of their pair-difference variable. Their analysis, however, assumes GRH. Likewise, the Bui--Keating--Smith variance/pair-correlation transfer is formulated under GRH on the zero side. These results therefore calibrate the missing theorem but cannot serve as non-circular proof-level input for the principal mod-5 channel, which contains zeta.

The line can still avoid this zero-side burden by proving the oriented prime-side scalar response directly. The conclusion here is narrower: **smallness of `t_X` is not itself a shortcut through the zero-correlation step.**

## 4. Prior art and novelty audit

The ingredients are classical and no novelty is claimed for them separately.

- Goldston--Montgomery pair correlation relates prime short-interval variance to zero statistics at reciprocal relative scales. Bui, Keating and Smith extend this framework to Selberg-class `L`-functions and make the power-range correspondence explicit; for degree one the relevant variance is governed by `log(X/h)` and their pair-correlation statements are under GRH.
- The local spacing `2pi/log T` is the standard microscopic normalization for zeta and fixed-conductor Dirichlet-`L` zeros.
- Kandhil, Languasco and Moree formulate mixed Dirichlet-`L` pair correlation using `gamma_1-gamma_2` and explicitly normalize finite difference intervals by `2pi/log T`.
- Translating `L(s,chi)` to `L(s+it,chi)` translates its zero ordinates by `-t`; this is immediate and classical.

The line-specific derived content is the scale comparison between those classical facts and the specific quarter-turn `t_X=-pi/(2 log X)` forced by `PL-431`. Targeted searches around vertically shifted `L`-values, zero pair correlation, microscopic spacing, and short-interval variance did not locate a source making this exact route-level observation. The claim is therefore not that a new zero-statistics theorem has been proved, but that the current Mathia deformation has been placed on the correct classical microscopic scale.

Literature anchors already recorded in `research/prime_lattice/SOURCES.md`:

- H. M. Bui, J. P. Keating, D. J. Smith, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *J. London Math. Soc.* **94** (2016), 161–185, DOI `10.1112/jlms/jdw030`, arXiv `1506.03741`.
- N. Kandhil, A. Languasco, P. Moree, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Math. Ann.* **394** (2026), Article 43, DOI `10.1007/s00208-026-03383-y`.

## 5. Adversarial audit and boundaries

1. **The scale dictionary is not an unconditional RH implication.** Bui--Keating--Smith's zero-side equivalences assume GRH, and the classical zeta pair-correlation equivalence is stated under RH. Equations (12)--(16) are a calibration of the analytic regime, not permission to import those conditional theorems into an RH proof.

2. **`T~X/h` is meant at power scale here.** The precise transfer theorems use ranges with slack and different variables. The robust statement is `log T/log X -> 1-theta` for `h=X^{theta+o(1)}` within the corresponding degree-one range, which is all that (5) requires.

3. **The fixed offset disappears for nearly macroscopic intervals.** If `log(X/h)=o(log X)`, then the normalized displacement tends to zero. The finding therefore does not claim a universal nonzero microscopic shift for every `h<=X` allowed in `PL-432`.

4. **The principal character is imprimitive.** For modulus `5`, `L(s,chi_0)=zeta(s)(1-5^{-s})`. The finite Euler factor does not change the leading high-zero density on the critical strip, but an exact zero formula must keep its extra zeros separate. The scale statement uses only the leading degree-one density.

5. **A direct prime-side proof need not pass through pair correlation.** `PL-432` remains an exact unconditional source-side identity. This finding obstructs only the proposed continuity intuition for a zero-side transfer; it does not say that pair correlation is logically necessary for all approaches to the oriented sample.

6. **A fixed microscopic offset is not automatically harder than zero offset.** Some future theorem could control both uniformly. The point is that such uniformity is substantive arithmetic information and cannot be inferred from `t_X=o(1)` alone.

7. **No new information about horizontal zero locations is obtained.** The translation (7) preserves real parts. The RH relevance remains through the earlier PL-421 source/positivity transfer, whose non-circular analytic input is still missing.

## Consequence for the line

The representation and conditioning stages of the mod-5 route are now better separated from its analytic bottleneck. `PL-429` removes the scalar information obstruction, `PL-431` reduces tomography to two samples, and `PL-432` makes the quarter-turn transport compatible with ordinary short-interval norms. The present scale audit shows why the remaining sample is nevertheless not a trivial perturbation of the unshifted zero statistic.

For polynomial short intervals, the useful next target is therefore one of two genuinely arithmetic statements:

\[
\boxed{
\begin{gathered}
\text{directly control the oriented prime-side response at }t_X=-\pi/(2\log X),\\
\text{or control the corresponding mixed zero correlation uniformly at the fixed microscopic offset }\\
u_*=-\frac{1-\theta}{4},
\end{gathered}}
\]

with the first route preferable for a non-circular RH argument unless the second can be established without assuming RH/GRH. Ordinary continuity at the unshifted point is no longer a meaningful substitute for either target.