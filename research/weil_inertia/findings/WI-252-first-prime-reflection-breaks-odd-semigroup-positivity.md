# WI-252 — The first prime reflection breaks odd-semigroup positivity before any RH-failure crossing

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-BEURLING-DENY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.
- **Scope:** this closes a natural phase-rigidity shortcut for the first-odd-zero-mode program of `WI-247`--`WI-251`. Once the first von Mangoldt atom is active, the localized Weil form restricted to odd functions does not generate a positivity-preserving semigroup after transfer to the positive half-interval. Consequently the hypothetical first odd zero mode cannot be forced to have one sign on `(0,a)` by the usual Perron--Frobenius/Krein--Rutman/Beurling--Deny mechanism. This does **not** prove that the mode changes sign, and it does not exclude some different zeta-specific argument proving phase rigidity.
- **Literature input:** Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law*, arXiv:2608.24827v2 (2 Sep 2026), proves by certified computation that the full Weil form is strictly positive on support `[-0.8,0.8]`; its odd-sector lower bound is positive as well. The interval certificate is imported here at theorem level and was not independently replayed in Mathia.
- **Novelty boundary:** the first Beurling--Deny criterion and the implication from positivity-improving semigroups to one-signed simple ground states are classical. Suzuki uses that machinery for the small-radius unrestricted logarithmic/archimedean regime. The exact obstruction below is the elementary but zeta-specific reflected `p=2` atom produced by passing the odd Weil form to the half interval. A targeted audit found no source stating this odd-sector obstruction. No priority claim is made.

## Claim

Let `q_a^-` be the real odd restriction of Suzuki's localized Weil form on `(-a,a)`, transferred unitarily to `L^2(0,a)` by

\[
(Ug)(x)=2^{-1/2}\operatorname{sgn}(x)g(|x|).
\]

Then:

1. for every
   \[
   a>\frac{\log 2}{2},
   \]
   the self-adjoint operator associated with `q_a^-` does **not** generate a positivity-preserving semigroup on `L^2(0,a)`;
2. Zhu's certified compact-window theorem gives `lambda^-_{0.8}>0`, so the first odd zero radius forced by `WI-247` under `not RH` satisfies
   \[
   a_*^->0.8>\frac{\log2}{2};
   \]
3. therefore, at every hypothetical RH-failure first odd crossing, standard cone-positivity arguments cannot imply that the positive-half profile of the zero mode has constant sign.

The obstruction is already carried by the first prime `p=2`. In half-line coordinates its odd reflection turns the negative prime translation in the Weil form into a **positive Hankel/anti-diagonal interaction** on

\[
u+t=\log2.
\]

That positive off-diagonal interaction violates the first Beurling--Deny criterion.

## 1. Exact odd half-line decomposition of one source atom

For a real `g` on `(0,a)`, extend it by zero outside the interval and put `v=Ug`. For `h>0`, define

\[
A_h(g):=\int_0^\infty g(u+h)g(u)\,du,
\]

and

\[
H_h(g):=\int_{I_h}g(h-u)g(u)\,du,
\qquad
I_h=[\max(0,h-a),\min(a,h)].
\]

Splitting the full-line autocorrelation of the odd extension into the two same-sign pieces and the sign-changing crossing piece gives the exact identity

\[
\boxed{
C_{Ug}(h)=A_h(g)-\frac12H_h(g).
}
\tag{1}
\]

Indeed, without the unitary factor `2^{-1/2}` the two same-side pieces contribute `2A_h`, while the interval on which `x` and `x+h` have opposite signs contributes `-H_h`; multiplication by `1/2` gives (1).

`WI-241` writes the discrete arithmetic contribution to the odd Weil form as

\[
-2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}C_v(\log n).
\]

Hence a prime-power atom `h=log n`, `w_n=Lambda(n)/sqrt n`, contributes on the half interval

\[
\boxed{
-2w_nA_h(g)+w_nH_h(g).
}
\tag{2}
\]

The first term is the familiar attractive same-side translation. The second is a reflected Hankel term with **positive** coefficient. Its support is the anti-diagonal `u+t=h`.

For later use, polarize (2). Writing

\[
H_h(f,g)=\int_{I_h}f(h-u)g(u)\,du,
\]

the reflected part of the bilinear form is `+w_n H_h(f,g)`.

## 2. A pair of disjoint positive bumps sees only the positive p=2 reflection

Fix

\[
h_2=\log2,
\qquad
a>h_2/2.
\]

Choose `delta>0` so small that

\[
u_0=h_2/2-\delta>0,
\qquad
t_0=h_2/2+\delta<a.
\]

Then

\[
u_0+t_0=h_2,
\qquad
0<t_0-u_0=2\delta<h_2.
\tag{3}
\]

Let `phi` be a nonnegative smooth bump supported in `(-1,1)` with `||phi||_2=1`. For sufficiently small `epsilon`, define disjoint nonnegative functions

\[
f_\epsilon(u)=\epsilon^{-1/2}
\phi\!\left(\frac{u-u_0}{\epsilon}\right),
\]

\[
g_\epsilon(u)=\epsilon^{-1/2}
\phi\!\left(\frac{t_0-u}{\epsilon}\right).
\]

They lie in the smooth half-interval form core, their supports are disjoint, and the mirrored choice gives

\[
H_{h_2}(f_\epsilon,g_\epsilon)=1
\tag{4}
\]

for all sufficiently small `epsilon`.

No same-side prime-power translation couples these two bumps. Their center separation is `2delta<h_2`, whereas every nonzero von Mangoldt atom has shift at least `log2=h_2`. For the reflected terms, the sum of the centers is exactly `h_2`; since `log n=h_2` only for `n=2`, the `p=2` atom is the unique discrete source interaction surviving between the two supports when `epsilon` is sufficiently small. Thus the entire discrete prime contribution to the cross form is

\[
\frac{\log2}{\sqrt2}+o(1),
\]

and in fact the non-`2` discrete terms vanish exactly once the bump supports are small enough.

## 3. Every non-atomic cross term is o(1)

It remains to check that no continuous part can cancel the fixed positive atom in the bump limit.

The supports of the odd extensions of `f_epsilon` and `g_epsilon` remain separated by a fixed positive distance: the relevant center differences are `2delta` and `h_2`. The identity/diagonal part of the mean form has zero cross term because the supports are disjoint. `WI-245` gives the remaining mean part as a convergent sum of exponential-resolvent kernels. Away from the diagonal those kernels, and their locally uniform sum, are bounded and continuous. The continuum comparison term in `WI-241` likewise has a locally bounded integral kernel on the fixed compact support rectangle, and the polar contribution is finite rank/smooth there.

Because each `L^2`-normalized bump has `L^1` norm `O(epsilon^{1/2})`, any such bounded-kernel cross term is `O(epsilon)`. Consequently

\[
\boxed{
q_a^-(f_\epsilon,g_\epsilon)
=\frac{\log2}{\sqrt2}+O(\epsilon)>0
}
\tag{5}
\]

for all sufficiently small `epsilon`.

This is the decisive sign. It does not use an asymptotic prime estimate, RH, a zero sum, or any numerical property of the candidate eigenfunction.

## 4. Beurling--Deny forbids positivity preservation

For a lower-bounded real symmetric closed form `q`, shift by a scalar if needed so that `q+c||.||_2^2` is nonnegative. The first Beurling--Deny criterion says that the generated self-adjoint semigroup is positivity preserving if and only if the form domain is stable under absolute value and

\[
q(|u|)\le q(u).
\]

Equivalently, taking disjoint nonnegative `f,g` and `u=f-g`, positivity preservation requires

\[
q(f,g)\le0.
\tag{6}
\]

The scalar shift does not affect this cross term because `<f,g>=0`.

But (5) supplies disjoint nonnegative smooth `f_epsilon,g_epsilon` with

\[
q_a^-(f_\epsilon,g_\epsilon)>0.
\]

Therefore (6) fails and

\[
\boxed{
e^{-tA_a^-}\text{ is not positivity preserving for any }a>\frac{\log2}{2}.
}
\tag{7}
\]

In particular it cannot be positivity improving. The standard Perron--Frobenius/Krein--Rutman route from an order-preserving semigroup to a one-signed simple ground state is unavailable in this regime.

Classical references for this implication include the first Beurling--Deny criterion as presented, for example, in Reed--Simon, *Methods of Modern Mathematical Physics IV*, Theorem XIII.50; modern form-theoretic statements give the equivalent condition `q(|u|)<=q(u)` for a positivity-preserving semigroup.

## 5. The obstruction necessarily applies at a hypothetical first odd RH-failure crossing

`WI-247` proves that `not RH` forces a finite first odd radius

\[
a_*^-:=\inf\{a>0:\lambda_a^-\le0\}
\]

with `lambda_a^->0` for `a<a_*^-`, `lambda_{a_*^-}^-=0`, and an attained odd zero mode.

The only possible loophole in applying (7) would be a first crossing before the first prime reflection becomes active. Recent prior art removes that loophole. Zhu's arXiv:2608.24827v2 proves by a finite, interval-certified reduction that the Weil form is strictly positive for every complex test supported in `[-0.8,0.8]`; its parity analysis gives a positive odd-sector lower bound as well. Therefore, by monotonicity of the localized variational minimum,

\[
\boxed{
a_*^->0.8.}
\tag{8}
\]

Since

\[
0.8>\frac{\log2}{2}=0.3465735902\ldots,
\]

the `p=2` reflected interaction is already active long before any hypothetical first odd zero mode can appear. Combining (7) and (8),

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\text{the forced first odd zero mode lies in a regime where the odd half-line semigroup is not positivity preserving.}
}
\tag{9}
\]

The numerical value `0.8` is not essential to the structural obstruction; any proved strict-positivity radius beyond `(log2)/2` would suffice. Zhu's certified theorem supplies a large explicit margin.

## 6. Consequence for the radial-flux clue

For a real odd profile `v=Ug`, direct splitting also gives, for `h>=0`,

\[
C_v(h)=A_h(g)-\frac12H_h(g),
\]

and

\[
R_v(h)=hA_h(g)-\frac12
\int_{I_h}|h-2u|g(h-u)g(u)\,du.
\]

If one somehow knew independently that `g` had one sign, then

\[
R_v(h)-hC_v(h)
=\frac12\int_{I_h}
\bigl(h-|h-2u|\bigr)g(h-u)g(u)\,du
\ge0.
\tag{10}
\]

Thus constant phase would indeed give useful sign information for the exact layer-cake flux in `WI-251`. The present finding identifies why that tempting shortcut is not free: **the arithmetic source that one is trying to control is itself what destroys the order structure needed to deduce constant phase.**

Accordingly the live `CLUE-first-odd-mode-cutoff-flux-constraint` cannot close by importing the usual statement that a ground state is positive. Any phase/nodal restriction on the first odd zero mode must instead be proved from additional zeta-specific structure, from the eigen-equation together with the signed source, or from a different cone/order not contradicted by the reflected prime atoms.

## 7. Prior-art and novelty audit

Three neighboring bodies of work were checked.

1. **Suzuki's localized Weil operator.** Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, uses Dirichlet-form/positivity-improving machinery in the sufficiently-small-radius regime to prove simplicity and positivity of the unrestricted ground state. That does not imply positivity preservation of the odd half-line realization once prime atoms enter.
2. **Certified compact-window positivity.** Zhu, arXiv:2608.24827v2, proves strict positivity through radius `0.8` and explicitly treats the odd sector. This is the literature input used only to locate the hypothetical first odd crossing beyond the first-prime threshold. Its computer-assisted certificate has not been independently replayed here.
3. **Krein--Rutman claims around prime operators.** A targeted search found the recent public draft by Brendan Siche, *Spectral Simplicity of the Weil Quadratic Form via Krein-Rutman Positivity*, whose repository describes a prime-sum operator `P_lambda` in a different truncated/Galerkin decomposition as positive, compact and irreducible. That statement concerns `P_lambda`, not the semigroup generated by Suzuki's full localized odd Weil operator `A_a^-`; it therefore neither supplies the desired half-line phase theorem nor conflicts with (7).

The classical mathematical input is Beurling--Deny. The Mathia contribution is the exact odd-reflection calculation (1)--(5) and its application to the first-crossing program. Search absence is recorded only as audit context, not as a priority claim.

## 8. Stress tests and boundaries

1. **Sign of the reflected atom.** The sign is fixed by `q=Q_mean-2 Delta_Lambda` and the minus sign acquired when an odd function is translated across the origin. The two negatives produce the positive `+w_n H_h` term in (2).
2. **Unitary normalization.** The factor `2^{-1/2}` changes the full-line identity from `2A-H` to `A-H/2`; it does not change the positive sign of the Hankel atom. Equation (2) keeps the resulting coefficient exactly.
3. **No hidden competing atom.** The two centers have sum `log2` and separation strictly below `log2`. Hence no other von Mangoldt atom can couple the bump pair, either by same-side translation or by reflection, for sufficiently small support.
4. **Continuous singularities.** The bump supports never approach one another or the reflected diagonal. The logarithmic/mean singularity is therefore irrelevant to the cross limit; all continuous off-diagonal pieces contribute `O(epsilon)`.
5. **Lower-bounded rather than positive operator.** Beurling--Deny is applied after a scalar shift. The shift has zero cross term on disjoint supports, so the obstruction survives unchanged.
6. **Failure of semigroup positivity is not a nodal theorem.** The ground state might still happen to be one-signed for another reason. What is ruled out is the standard order-preserving-semigroup implication.
7. **Unrestricted versus odd sector.** Suzuki's small-radius positive/even unrestricted ground state is not contradicted. The obstruction concerns the odd sector represented on `(0,a)`, where crossing the origin converts a prime translation into a positive reflection.
8. **Dependence on Zhu's certificate.** The exact theorem (7) is independent of Zhu. Only the corollary that every hypothetical first odd RH-failure crossing lies in the obstructed regime uses the literature-certified radius `0.8`. If that computer-assisted theorem were withdrawn, (7) would remain valid and the application would revert to requiring any independent proof that `a_*^->log2/2`.

## Falsification test

The structural theorem is falsified if any of the following occurs: the half-line identity (1) has the wrong normalization or sign; the `p=2` reflected cross term is canceled by another `O(1)` contribution on the chosen disjoint bump pair; the localized odd form does not satisfy the closed real-form hypotheses needed for Beurling--Deny after scalar shift; or the support convention in Zhu's `L=0.8` theorem does not match Suzuki's radius `a` used in `WI-247`.

The key audit is finite and local: polarize the exact `p=2` term on the two bump supports and verify that every other piece is `o(1)`. No limiting statement about zeta zeros is involved.

## Consequences

- The first-odd-mode program gains a sharp structural boundary: prime activation destroys the most obvious cone positivity exactly where arithmetic begins to matter.
- Zhu's certified radius places any RH-failure first odd crossing safely on the arithmetic side of that boundary.
- `WI-251`'s radial-flux inequality remains the live object, but constant phase cannot be assumed from generic ground-state theory. A useful next step must control the signed radial source directly or find a genuinely zeta-specific replacement for the lost order structure.
- This is a no-go result, not a percentage improvement and not an RH proof.