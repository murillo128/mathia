# WP-205 — Fractional extension geometry realizes the critical Gamma bath but leaves an infinite mod-four ladder

**Status:** `DERIVED + EXACT + ARCHIMEDEAN-GAMMA-EXTENSION + POSITIVE-BOUNDARY-RESPONSE + CRITICAL-FRACTIONAL-CALCULUS + IDENTICAL-CHANNEL-RIGIDITY + ORDER-NONSELECTION + MATCHED-CONTROL + SOURCE-FORCING-NARROWING + PRIOR-ART-AUDITED + NOT-A-WEIL-BRIDGE`.

`WP-204` leaves one specific escape open: the singular fractional power required at the reciprocal-floor boundary might arise from an independent geometric theorem rather than from a hand-picked functional calculus. That escape is real. The Gamma number operator admits the standard Caffarelli--Silvestre/Stinga--Torrea extension geometry, and its critical inverse fractional power is a positive Neumann-to-Dirichlet boundary response.

But this does not yet source-force a Weil mechanism. Combining the exact Gamma determinant normalization of `WP-203` with the sharp `WP-200`/`WP-202` reciprocal-floor condition gives a discrete rigidity statement only **after** a higher spectral-shift order has already been chosen. For order

\[
n=4k\ge4,
\]

an equal-channel extension completion with exact unscaled Gamma determinant, natural `S^n` membership, and the reciprocal floor is forced to have exactly

\[
M=n-1,
\qquad
s=\frac1{n-1}.
\]

Thus fractional extension geometry explains how the singular critical bath can be geometrically positive, and equal-channel symmetry removes the continuous exponent freedom of `WP-203`. However, every `n=4k` produces a different valid geometry. The source therefore leaves an infinite ladder

\[
(n,M,s)=(4k,\,4k-1,\,1/(4k-1)),
\qquad k=1,2,3,\ldots,
\]

all carrying the same exact Gamma determinant normalization and the same kind of independent boundary positivity. Nothing in the Gamma source or extension theorem selects `k`.

The surviving requirement is sharper: a genuine Mathia completion must contain extra intrinsic structure that selects the relevant order/channel multiplicity **before** positivity is interpreted arithmetically, and it must still produce the finite Mangoldt and polar sectors in the same ordered object.

## 1. The Gamma inverse power is a genuine positive boundary response

Use the canonical positive operator from `WP-203` and `WP-204`,

\[
D_a=N+a,
\qquad
L_a=\frac{D_a}{\pi},
\qquad a>0,
\]

on `ell^2(N_0)`. Its spectrum is

\[
L_a e_j=\lambda_j e_j,
\qquad
\lambda_j=\frac{j+a}{\pi}>0.
\]

Fix `0<s<1`. For a positive self-adjoint operator, the standard extension problem realizes `L_a^s` as a Dirichlet-to-Neumann map. In abstract form the extension `U(y)` satisfies

\[
U''(y)+\frac{1-2s}{y}U'(y)-L_aU(y)=0,
\qquad
U(0)=f.
\tag{1}
\]

With the standard positive normalization of the weighted conormal derivative,

\[
\operatorname{DtN}_s f=L_a^s f.
\tag{2}
\]

The minimizing weighted bulk energy is, up to the same positive normalization constant,

\[
\mathcal E_s(U)
=
\int_0^\infty
 y^{1-2s}
 \left(
 \|U'(y)\|^2+\|L_a^{1/2}U(y)\|^2
 \right)dy,
\tag{3}
\]

and its boundary value is

\[
\inf_{U(0)=f}\mathcal E_s(U)
=c_s\langle f,L_a^s f\rangle,
\qquad c_s>0.
\tag{4}
\]

Since `L_a` is strictly positive, the normalized Neumann-to-Dirichlet response is therefore

\[
\boxed{
\operatorname{NtD}_s=L_a^{-s}\succeq0.
}
\tag{5}
\]

This positivity is independent of RH, zeta zeros, the Weil functional, or a chosen arithmetic kernel. It comes from a positive weighted extension energy. Moreover

\[
L_a^{-s}e_j
=
\pi^s(j+a)^{-s}e_j,
\tag{6}
\]

so the response is exactly the shifted power bath studied in `WP-203`, not merely an asymptotic surrogate.

Consequently the explicit escape left by `WP-204` cannot be dismissed as arbitrary spectral notation: the critical non-`C^1` power can indeed be the compliance operator of a local one-higher-dimensional positive geometry.

## 2. Exact Gamma normalization plus identical channels discretizes the exponent

Now retain the same complex family

\[
L_q=\frac{N+q}{\pi},
\qquad \Re q>0.
\]

`WP-203` proves the exact relative determinant identity

\[
\frac{\det_\zeta L_a}{\det_\zeta L_{a+z}}
=
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}.
\tag{7}
\]

For one fractional channel `L_q^s`, zeta determinants scale by `s`, so its relative determinant is the `s`th power of (7). Take `M` **identical** extension channels, each with the same exponent `s`. Direct-sum multiplicativity gives

\[
\frac{
\det_\zeta (L_a^s)^{\oplus M}
}{
\det_\zeta (L_{a+z}^s)^{\oplus M}
}
=
\left(
\pi^{-z}\frac{\Gamma(a+z)}{\Gamma(a)}
\right)^{Ms}.
\tag{8}
\]

Hence exact unscaled Gamma normalization forces

\[
\boxed{Ms=1.}
\tag{9}
\]

This is stronger than the arbitrary unequal-channel simplex of `WP-203`: once identical-channel symmetry is imposed, there is only the discrete freedom `s=1/M`.

At the positive anchor, the associated centered bath is

\[
V_{M,s}
=
(L_a^{-s})^{\oplus M}.
\tag{10}
\]

Finite multiplicity does not affect the Schatten threshold. From (6),

\[
V_{M,s}\in\mathcal S^q
\quad\Longleftrightarrow\quad
sq>1.
\tag{11}
\]

## 3. For a fixed Weil-compatible order, all gates force `M=n-1`

Fix an order allowed by the `WP-193` autocorrelation parity gate,

\[
n=4k\ge4.
\tag{12}
\]

Three requirements now act simultaneously.

First, exact Gamma normalization gives `s=1/M` by (9). Second, the natural order-`n` perturbation category requires

\[
V_{M,s}\in\mathcal S^n
\quad\Longleftrightarrow\quad
ns>1
\quad\Longleftrightarrow\quad
M<n.
\tag{13}
\]

Third, `WP-200` and `WP-203` give the exact reciprocal-floor phase boundary for this shifted power sequence. Inside `S^n`, universal finite-payload stabilization requires

\[
\frac1n<s\le\frac1{n-1}.
\tag{14}
\]

After `s=1/M`, the upper inequality in (14) is

\[
M\ge n-1.
\tag{15}
\]

Combining (13), (15), and integrality of the channel count yields

\[
\boxed{
M=n-1,
\qquad
s=\frac1{n-1}.
}
\tag{16}
\]

Thus the endpoint that looked hand-picked in `WP-203` becomes rigid **conditional on a chosen order and identical-channel completion**. The bath lies exactly at

\[
V_{n-1,1/(n-1)}
\in
\mathcal S^n\setminus\mathcal S^{n-1},
\tag{17}
\]

with harmonic divergence of the `(n-1)`st singular-value moment. Its extension weight is

\[
y^{1-2/(n-1)},
\tag{18}
\]

so the nonsmooth spectral endpoint has a concrete local geometric realization rather than being inserted only as a fractional matrix function.

For one channel, `WP-203` computes

\[
\lim_{\xi\to\infty}
\xi F_{a,1/(n-1)}(\xi)
=
\frac{\pi^2}{2(n-2)!}>0.
\tag{19}
\]

Direct sums add the higher-order spectral-shift multiplier, so the forced equal-channel bath has

\[
\boxed{
\lim_{\xi\to\infty}
\xi F_{M,s}(\xi)
=
\frac{(n-1)\pi^2}{2(n-2)!}>0.
}
\tag{20}
\]

It therefore satisfies the exact `WP-202` reciprocal-floor criterion.

## 4. The source still fails to choose the order

Equation (16) might appear to solve the source-forcing problem, but it only transfers the freedom from the exponent to the higher spectral-shift order. `WP-193` does not select one order; it admits every

\[
n=4k.
\tag{21}
\]

For every `k>=1`, equations (16)--(20) give a valid extension completion

\[
\boxed{
(n,M,s)
=(4k,\,4k-1,\,1/(4k-1)).
}
\tag{22}
\]

The first two members are already distinct:

\[
(4,3,1/3),
\qquad
(8,7,1/7).
\tag{23}
\]

Both have all of the following properties:

- a positive weighted extension energy independent of RH;
- positive compact NtD channels;
- exact unscaled relative Gamma determinant after the identical-channel direct sum;
- membership in the natural order-`n` Schatten class but not `S^{n-1}`;
- a positive reciprocal Fourier floor and hence the `WP-202` stabilization resource.

Yet their channel multiplicities, fractional powers, extension weights, and higher-order trace remainders are different. They are not two coordinate descriptions of one fixed extension problem.

The Riemann shift does not break this degeneracy. The reciprocal constant (19) is independent of the Hurwitz anchor `a>0`, as already computed in `WP-203`. The special value `a=1/4` fixes the Riemann Gamma factor in (7), but it does not select `n`, `M`, or the boundary weight (18).

Therefore

\[
\boxed{
\text{Gamma determinant + fractional extension positivity + reciprocal floor}
\not\Rightarrow
\text{a unique Riemann/Weil ordered geometry}.
}
\tag{24}
\]

## 5. Aggressive falsification and exact scope

**Could the lowest allowed order `n=4` be declared canonical?** It could be imposed, but that is an additional minimal-regularization principle, not a consequence of the Gamma determinant, the extension theorem, or the Weil autocorrelation parity calculation. If a Mathia construction independently produces a three-channel `s=1/3` geometry or an order-four trace theorem, that would be genuinely new input and lies outside this obstruction.

**Does equal-channel symmetry itself follow from the source?** No. It is deliberately the strongest simple symmetry that can remove the continuous exponent simplex of `WP-203`. The result is therefore conditional rigidity: equal channels force (16) once `n` is fixed, but neither the channel count nor the spectral-shift order is supplied by the Gamma source. Dropping equal-channel symmetry restores the larger nonuniqueness already proved in `WP-203`.

**Could a single geometric channel carry the exact Gamma determinant?** Exact normalization then forces `s=1`. Its inverse response is the ordinary inverse resolvent, which is in `S^{n-1}` for every `n>=4` and fails the reciprocal-floor gate by `WP-204`. The successful fractional geometry therefore necessarily introduces extra channel structure in this architecture.

**Does geometric extension positivity itself imply the Weil sign?** No. The extension proves positivity of `L_a^{-s}` as a compliance operator. `WP-202` then says that enough copies can stabilize arbitrary finite positive payloads; that very universality is a matched-control warning. No Mangoldt selector, mixed-prime incidence, pole term, or finite--archimedean relation is generated by equations (1)--(24).

**Could a non-diagonal or source-coupled extension evade the ladder?** Yes. The theorem concerns identical spectral extension channels of the canonical Gamma number operator and their centered direct-sum bath. A geometry that couples different Gamma levels or couples finite primes to the extension bulk before diagonalization may leave this class. Such a proposal must derive its coupling and order theorem independently and survive the nonarithmetic bath controls of `WP-201`--`WP-202`.

## 6. Prior art and novelty boundary

No novelty is claimed for realizing fractional powers by extension problems or for positivity of the associated weighted energy. Caffarelli and Silvestre, *An Extension Problem Related to the Fractional Laplacian*, Communications in Partial Differential Equations 32 (2007), DOI `10.1080/03605300600987306`, gives the foundational Dirichlet-to-Neumann realization of fractional Laplacians. Stinga and Torrea, *Extension Problem and Harnack's Inequality for Some Fractional Operators*, Communications in Partial Differential Equations 35 (2010), DOI `10.1080/03605301003735680`, extends the characterization to broad classes of positive operators. Galé, Miana, and Stinga, *Extension problem and fractional operators: semigroups and wave equations*, Journal of Evolution Equations 13 (2013), DOI `10.1007/s00028-013-0182-6`, gives the abstract semigroup framework applicable to generators of bounded `C_0` semigroups; `-L_a` generates the positive contraction semigroup `e^{-tL_a}`.

The inverse response in (5) is then elementary because `L_a^s` is strictly positive and invertible: the normalized Neumann-to-Dirichlet map is the inverse of the Dirichlet-to-Neumann map. The Gamma determinant identity, shifted power spectrum, exact reciprocal-floor threshold, and endpoint constant are the persisted internal results `WP-200`, `WP-202`, `WP-203`, and `WP-204`.

A targeted literature audit found the classical extension machinery and abstract fractional-operator theory, but no external theorem is needed for the Mathia-specific arithmetic consequence. No historical novelty is inferred from search absence. The durable new content is the exact combination of three already-audited Mathia gates: exact Gamma determinant normalization, positive extension geometry, and the full-cone reciprocal-floor threshold. Their conjunction gives the integer rigidity `M=n-1` and simultaneously exposes the residual infinite `4k` order ladder.

## 7. Consequence for the research line

The archimedean side has moved one step closer to the mandate but not across it. The critical singular power required by `WP-202` can be realized as an independently positive geometric boundary response; it is not intrinsically incompatible with geometry. Under identical-channel symmetry, its exponent is even forced once a higher trace order is fixed.

The remaining failure is now more specific than the smooth-calculus obstruction of `WP-204`: **the Gamma source does not choose the sign-producing order/channel architecture**. A surviving construction must provide a source-forced reason for one member of the ladder (22), or leave the centered higher-order spectral-shift architecture entirely. In either case it must also place the finite Mangoldt data and the archimedean/polar terms inside the same ordered object before the final sign theorem. Until those two obligations are met, fractional extension positivity remains a geometric realization of a generic stabilization resource, not a global Weil positivity mechanism.