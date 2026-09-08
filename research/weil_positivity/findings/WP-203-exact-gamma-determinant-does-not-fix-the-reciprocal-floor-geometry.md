# WP-203 — The exact Gamma determinant does not fix the reciprocal-floor geometry

**Status:** `DERIVED + EXACT + ARCHIMEDEAN-GAMMA-DETERMINANT + HIGHER-ORDER-SPECTRAL-SHIFT + TWO-CHANNEL-MATCHED-CONTROL + RECIPROCAL-FLOOR-SEPARATION + SOURCE-FORCING-FAILURE + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-202` identifies the exact analytic resource behind the centered-diagonal higher-order spectral-shift escape: at order `n=4k`, a bath universally stabilizes arbitrary finite positive payloads after finite amplification exactly when its even multiplier has a uniform reciprocal-frequency floor. The current research synthesis therefore asks whether that resource can be **source-forced**, rather than chosen as an unrelated rough reservoir.

The most direct archimedean attempt is stronger than it first appears. The Riemann Gamma factor itself has a canonical number-operator determinant realization. But that realization does **not** determine the roughness of the associated compact inverse-power bath.

In fact, for every `n=4k>=4` there are two positive two-channel baths built from the **same Gamma number operator**, with the **same exact completed-Gamma relative zeta determinant**, the **same channel count**, and both lying in the natural `S^n` class, such that one has the `WP-202` reciprocal floor and the other does not.

Thus even exact archimedean determinant provenance is insufficient to source-force the sign-producing reservoir:

\[
\boxed{
\text{same exact Gamma determinant data}
\not\Rightarrow
\text{same Weil-cone positivity resource}.
}
\tag{1}
\]

This is a matched-control obstruction, not a claim that every Gamma-derived infinite geometry fails. A surviving construction must specify additional geometry that canonically fixes the fractional functional calculus or couples it nonseparably to the finite-prime sector before positivity is tested.

## 1. The completed Gamma factor is an exact relative determinant of the number operator

Let `N` be the number operator on `ell^2(N_0)`,

\[
Ne_j=j e_j,
\qquad j=0,1,2,\ldots,
\tag{2}
\]

and for `q` in the right half-plane define

\[
D_q=N+q,
\qquad
L_q=\frac{D_q}{\pi}.
\tag{3}
\]

Its spectral zeta function is the Hurwitz zeta function with the elementary scale included:

\[
\zeta_{L_q}(s)
=\operatorname{Tr}(L_q^{-s})
=\pi^s\zeta(s,q).
\tag{4}
\]

The classical Hurwitz identities

\[
\zeta(0,q)=\frac12-q,
\qquad
\zeta'(0,q)
=\log\Gamma(q)-\frac12\log(2\pi)
\tag{5}
\]

therefore give

\[
\log\det_\zeta L_q
=-\log\pi\left(\frac12-q\right)
-\log\Gamma(q)
+\frac12\log(2\pi).
\tag{6}
\]

Fix a real anchor `a>0` and write `q=a+z`. Taking the inverse relative determinant cancels the constant terms exactly:

\[
\boxed{
\frac{\det_\zeta L_a}{\det_\zeta L_{a+z}}
=\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}.
}
\tag{7}
\]

For the Riemann critical line take

\[
a=\frac14,
\qquad
z=\frac{it}{2}.
\tag{8}
\]

Then the right side of (7) is precisely the relative archimedean factor

\[
\frac{\pi^{-(1/2+it)/2}\Gamma((1/2+it)/2)}
     {\pi^{-1/4}\Gamma(1/4)}.
\tag{9}
\]

Thus the normalization by `pi` in (3) is not cosmetic: it supplies the elementary `pi^{-s/2}` part together with the Gamma function, rather than leaving it as an external linear counterterm.

No RH input or zeta-zero data enters (4)--(9).

## 2. Fractional powers preserve the exact determinant up to their exponent

For `beta>0`, use the principal positive power at the real anchor and the corresponding holomorphic power for `Re(q)>0`. Then

\[
\zeta_{L_q^\beta}(s)
=\zeta_{L_q}(\beta s),
\tag{10}
\]

so zeta determinants scale linearly in `beta`:

\[
\log\det_\zeta L_q^\beta
=\beta\log\det_\zeta L_q.
\tag{11}
\]

Consequently

\[
\boxed{
\frac{\det_\zeta L_a^\beta}
     {\det_\zeta L_{a+z}^\beta}
=
\left(
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}
\right)^\beta.
}
\tag{12}
\]

For a finite direct sum of channels with exponents

\[
\beta_1,\ldots,\beta_M>0,
\tag{13}
\]

determinants multiply, hence the inverse relative determinant is

\[
\left(
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}
\right)^{\beta_1+\cdots+\beta_M}.
\tag{14}
\]

Therefore the **exact unscaled** completed-Gamma normalization is equivalent simply to

\[
\boxed{
\sum_{r=1}^M\beta_r=1.
}
\tag{15}
\]

Equation (15) remembers only the total fractional exponent. It does not remember how that exponent is distributed among channels.

That loss of information is exactly where the positivity matched control enters.

## 3. The associated centered baths remember the exponent distribution

At the positive anchor `a`, associate to each determinant channel the compact positive inverse-power perturbation

\[
V_{a,\beta}
=L_a^{-\beta}
=\pi^\beta(N+a)^{-\beta},
\qquad H_0=0.
\tag{16}
\]

Its singular values are

\[
v_j
=\pi^\beta(j+a)^{-\beta}.
\tag{17}
\]

Hence

\[
V_{a,\beta}\in\mathcal S^q
\quad\Longleftrightarrow\quad
\beta q>1.
\tag{18}
\]

In particular the natural order-`n` higher-order spectral-shift category requires

\[
\beta>\frac1n.
\tag{19}
\]

The shift `a` affects finitely scaled low modes but not this summability boundary.

For a scalar centered singular value `v`, `WP-198` gives the exact even order-`n` multiplier

\[
F_v(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^v
(1-\cos(t\xi))(v-t)^{n-3}\,dt.
\tag{20}
\]

The shifted power sequence in (17) has the same threshold as the unshifted family of `WP-200`. Inside `S^n`,

\[
\boxed{
\frac1n<\beta\le\frac1{n-1}
\quad\Longrightarrow\quad
\liminf_{|\xi|\to\infty}|\xi|F_{a,\beta}(\xi)>0,
}
\tag{21}
\]

while

\[
\boxed{
\beta>\frac1{n-1}
\quad\Longrightarrow\quad
V_{a,\beta}\in\mathcal S^{n-1}
\quad\text{and the `WP-202` reciprocal floor fails.}
}
\tag{22}
\]

For (21), the proof of `WP-200` is unchanged after replacing `j` by `j+a`: the truncated `(n-2)`nd moment has the same regular-variation exponent. For (22), `WP-198` already shows that an `S^{n-1}` centered bath cannot universally absorb even one fixed off-zero scalar positive source; equivalently `WP-202` forbids a reciprocal floor in this centered-diagonal class.

Thus determinant normalization sees only `sum beta_r`, whereas the sign-producing Fourier tail sees the individual `beta_r`.

## 4. At the critical exponent the reciprocal constant can be computed exactly

The endpoint

\[
\beta_c=\frac1{n-1}
\tag{23}
\]

is particularly rigid. Write

\[
C=\pi^{1/(n-1)},
\qquad
v_j=C(j+a)^{-1/(n-1)}.
\tag{24}
\]

From (20),

\[
F_v(\xi)=v^n\Phi_n(v\xi),
\tag{25}
\]

where

\[
\Phi_n(y)
=
\frac1{(n-3)!\,y^2}
\int_0^1(1-\cos(yu))(1-u)^{n-3}\,du.
\tag{26}
\]

The function needed for the regular-variation Riemann sum is integrable at both endpoints: `Phi_n(y)` is bounded as `y->0` and is `O(y^{-2})` as `y->infinity`. Therefore the shifted sequence `j+a` has the same continuum limit as `j`, and

\[
\lim_{\xi\to\infty}
\xi F_{a,\beta_c}(\xi)
=(n-1)C^{n-1}
\int_0^\infty\Phi_n(y)\,dy.
\tag{27}
\]

Using

\[
\int_0^\infty\frac{1-\cos(yu)}{y^2}\,dy
=\frac{\pi u}{2}
\qquad(u\ge0),
\tag{28}
\]

and Tonelli's theorem in (26),

\[
\int_0^\infty\Phi_n(y)\,dy
=
\frac{\pi}{2(n-1)!}.
\tag{29}
\]

Since `C^{n-1}=pi`,

\[
\boxed{
\lim_{\xi\to\infty}
\xi F_{a,1/(n-1)}(\xi)
=
\frac{\pi^2}{2(n-2)!}>0.
}
\tag{30}
\]

The constant is independent of the Hurwitz shift `a`. In particular the Riemann value `a=1/4` does not create the reciprocal floor; the floor comes from the chosen fractional exponent and the common `pi` scale.

## 5. Two exact-Gamma baths lie on opposite sides of the positivity boundary

Now fix any surviving spectral-shift order

\[
n=4k\ge4
\tag{31}
\]

and use **two channels** in both controls.

### Smooth split

Take

\[
\beta_1=\beta_2=\frac12.
\tag{32}
\]

Their sum is one, so by (14)--(15) the two-channel inverse relative determinant is exactly (7), with no change of Gamma normalization.

Because `n>=4`,

\[
\frac12>\frac1{n-1},
\tag{33}
\]

so both compact perturbations lie in `S^{n-1}`. Their finite direct sum does as well. Hence the reciprocal-floor condition of `WP-202` fails, and some fixed scalar positive payload defeats every finite amplification of this bath.

### Critical split

Take instead

\[
\beta_1=\frac1{n-1},
\qquad
\beta_2=\frac{n-2}{n-1}.
\tag{34}
\]

Again

\[
\beta_1+\beta_2=1,
\tag{35}
\]

so the exact two-channel Gamma determinant is **identical** to the smooth split.

But the first channel now supplies the explicit reciprocal floor (30), while the second contributes another nonnegative centered multiplier. Therefore the two-channel bath satisfies

\[
\boxed{
\liminf_{|\xi|\to\infty}
|\xi|F_{\rm critical}(\xi)>0.
}
\tag{36}
\]

By `WP-202`, this bath is a universal finite-payload stabilizer after a sufficiently large finite replication.

The matched comparison is therefore exact:

\[
\boxed{
\begin{array}{c|c|c|c}
& \text{channels} & \text{exact Gamma determinant} & \text{reciprocal floor}\\
\hline
(1/2,1/2) & 2 & \text{yes} & \text{no}\\
(1/(n-1),(n-2)/(n-1)) & 2 & \text{yes} & \text{yes}
\end{array}
}
\tag{37}
\]

Both use the same `N+a`, the same `pi` normalization, the same determinant identity, positive centered compact perturbations, and the same higher-order `S^n` category. Only the fractional-power split changes.

## 6. Aggressive falsification and exact scope

**Does exact Gamma normalization select the critical split?** No. Equation (15) leaves an entire simplex of exponent decompositions. The two controls in (37) are enough to prove nonuniqueness even with the channel count fixed.

**Could one insist on a single channel?** Yes, but then exact Gamma normalization forces `beta=1`. For every `n>=4`, that ordinary inverse-resolvent bath lies in `S^{n-1}` and fails the reciprocal-floor gate. A successful one-channel proposal therefore needs a different mechanism, not merely the standard inverse of the Gamma number operator.

**Could one insist on permutation-symmetric replicated channels?** If all `M` exponents are equal and exact normalization is imposed, then `beta=1/M`. Requiring both `S^n` membership and the reciprocal floor forces `n-1<=M<n`, hence the unique symmetric endpoint `M=n-1`, `beta=1/(n-1)`. This is a mathematically neat subcase, but the asymmetry control (37) shows that the determinant itself does not force that symmetry.

**Does the critical split already give the Weil form?** No. `WP-202` says only that its centered Fourier floor can dominate arbitrary finite positive payloads after further finite replication. That very universality is a warning: no Mangoldt selector, finite-prime incidence, pole term, or arithmetic distinction has yet entered.

**Does further replication preserve exact Gamma normalization?** No. Replicating the whole critical bath raises the relative determinant (7) to the replication power. Hence the `WP-202` existence of a payload-dependent stabilizing multiplicity cannot simply be used as the global construction while claiming the exact archimedean factor is unchanged. A genuine candidate would have to pass the sign test at its source-fixed multiplicity or generate compensating structure intrinsically, not renormalize the Gamma exponent afterward by hand.

**Is `a=1/4` selected by the positivity threshold?** No. The Schatten threshold and (30) are independent of `a`. The same contrast exists for every positive Hurwitz shift, providing a direct non-Riemann matched control.

**Could a coupled, non-diagonal, noncommuting, or non-power functional calculus evade the result?** Yes. The finding classifies only this natural route from the Gamma number operator to centered inverse-power baths. Such category exits remain legitimate, but they need their own source-forcing and sign theorem.

## 7. Prior art and novelty boundary

No novelty is claimed for the Hurwitz zeta function, zeta-regularized determinants, fractional powers of positive operators, Schatten membership of power-law sequences, or higher-order spectral-shift theory.

The determinant calculation uses the classical Hurwitz values recorded in NIST DLMF §25.11: equation 25.11.13 gives `zeta(0,q)=1/2-q`, while equation 25.11.18 gives `zeta'(0,q)=log Gamma(q)-(1/2)log(2pi)`. The former source is already present in `research/weil_positivity/SOURCES.md`; the latter is on the same durable DLMF Hurwitz-zeta source page.

The order-`n` positivity boundary is internal to the current line: `WP-198` gives the `S^{n-1}` source-variation obstruction, `WP-200` gives the exact power-law threshold, and `WP-202` upgrades the reciprocal Fourier floor to a necessary-and-sufficient criterion for universal centered-bath stabilization.

A targeted literature search for Gamma/Hurwitz zeta determinants, fractional powers, and spectral determinants found the standard regularized-determinant infrastructure but no reason that the Gamma determinant should determine a unique fractional inverse-power decomposition. No external novelty claim is inferred from that absence.

The durable Mathia delta is the exact matched control (37): **the same exact normalized Gamma relative determinant can sit over centered `S^n` baths on opposite sides of the precise `WP-202` sign-resource boundary**.

## 8. Consequence for `weil_positivity`

`WP-202` left one obvious hope: perhaps the archimedean source itself canonically supplies the rough infinite reservoir that an arbitrary nonarithmetic bath could only imitate. The number-operator realization shows why determinant provenance alone cannot do that job.

The completed Gamma factor fixes the sum of fractional determinant exponents, but the Weil-cone sign resource depends on how those exponents are distributed. The exact Riemann archimedean factor therefore does not distinguish the smooth two-channel bath from the critical one in (37), even though `WP-202` distinguishes them decisively.

Accordingly a future candidate cannot justify its reciprocal floor merely by saying that its infinite spectrum has the right Gamma regularized determinant. It must provide an additional **source-forced geometric principle** selecting the relevant functional calculus, multiplicity, coupling, or domain, and that principle must survive the matched alternative decompositions above.

Even that would settle only the real-place reservoir. The research mandate still requires the same completed object to generate the finite Mangoldt structure and polar/global counterterms and to prove the final assembled sign independently. A separated Gamma bath plus an arbitrary finite arithmetic payload remains the generic stabilization architecture rejected by `WP-199`--`WP-202`.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-198-rough-infinite-centered-bath-defeats-finite-positive-source-4k-no-go.md`
- `research/weil_positivity/findings/WP-200-power-law-centered-baths-have-a-sharp-source-variation-stabilization-threshold.md`
- `research/weil_positivity/findings/WP-202-universal-centered-bath-stabilization-is-equivalent-to-a-reciprocal-fourier-floor.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

The normalized number operator `L_q=(N+q)/pi` has inverse relative zeta determinant

\[
\pi^{-z}\Gamma(a+z)/\Gamma(a),
\]

which at `a=1/4`, `z=it/2` is exactly the relative Riemann archimedean Gamma factor. Splitting that determinant into two fractional-power channels preserves it exactly whenever the exponents sum to one. Yet the equal split `(1/2,1/2)` is too smooth to have the `WP-202` reciprocal floor, while the split `(1/(n-1),(n-2)/(n-1))` has the same exact determinant and does have that floor.

Therefore the Gamma determinant does not source-force the higher-order spectral-shift positivity resource. Any explanatory use of the critical bath must derive the fractional-power split or a stronger finite--archimedean coupling from additional geometry rather than from the Gamma factor itself.