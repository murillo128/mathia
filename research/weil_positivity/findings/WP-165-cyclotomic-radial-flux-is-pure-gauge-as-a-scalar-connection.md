# WP-165 — cyclotomic radial flux is pure gauge as a scalar connection, while factorized positivity has full shell support

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE-BRIDGE + SIGNED-RADIAL-FLUX + SCALAR-CONNECTION + PURE-GAUGE + BASED-HOLONOMY + FACTORIZATION-OBSTRUCTION + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-162`--`WP-164` leave a precise operator-level escape. The intrinsic cyclotomic inward flux

\[
\rho_n(s)
:=
-\frac{d}{ds}\log\Phi_n(e^{-s}),
\qquad n>1,\ s>0,
\tag{1}
\]

should not be made positive shell by shell: its signed total mass is exactly `Lambda(n)`, mixed-prime shells need cancellation, and even the everywhere-positive prime-power profiles are not positive semigroup coefficients. A natural next move is therefore to keep the signed function itself as a **connection coefficient**, form a covariant first-order operator, and ask whether positivity of its energy is the missing independent geometric sign theorem.

For the direct scalar construction, the answer is exact and negative. Put

\[
G_n(s):=\log\Phi_n(e^{-s}),
\qquad
\rho_n=-G_n'.
\tag{2}
\]

On the radial half-line, the unitary line connection

\[
\boxed{\nabla_n=d+i\rho_n(s)\,ds}
\tag{3}
\]

is globally pure gauge:

\[
\boxed{
\nabla_n
=
U_n^{-1}d\,U_n,
\qquad
U_n(s):=e^{-iG_n(s)}.
}
\tag{4}
\]

Consequently every gauge-covariant Dirichlet energy built directly from (3) is unitarily equivalent to the free half-line energy. The entire interior signed profile disappears from the positive form. For a mixed-prime shell, where `Lambda(n)=0`, the trivializing gauge is even **based at both radial ends**:

\[
U_n(0)=U_n(\infty)=1.
\tag{5}
\]

Thus the exact positive/negative cancellation exhibited by `n=6` in `WP-162` becomes completely gauge-trivial, including relative to the endpoints.

If the two radial endpoints are given fixed frames, prime powers leave one based-gauge datum: endpoint transport,

\[
\operatorname{Hol}_n
=
\exp\!\left(-i\int_0^\infty \rho_n(s)\,ds\right)
=
e^{-i\Lambda(n)}
=
p^{-i}
\quad(n=p^a).
\tag{6}
\]

This can give bounded nonnegative readouts such as `|1-Hol_n|^2`, which in particular vanish on all mixed-prime shells. But any continuous class-function readout is periodic in `Lambda(n)` and cannot equal the unbounded linear coefficient `Lambda(p)=log p` on all prime shells. The critically attenuated coefficient also cannot be recovered from this endpoint phase alone, because `Hol_{p^a}` is independent of the depth `a` whereas `log p/p^{a/2}` is not. Recovering `log p` itself requires choosing an additional lift/branch or otherwise reintroducing arithmetic information not forced by the compact phase.

The obvious nonunitary alternative does not rescue the sign mechanism. On fixed `L^2(ds)`, define

\[
D_n:=\frac d{ds}+\rho_n(s).
\tag{7}
\]

Then

\[
D_n^*D_n
=
-\frac{d^2}{ds^2}
+\rho_n(s)^2-\rho_n'(s)
\ge0
\tag{8}
\]

as a quadratic-form factorization. But this positivity is universal: the same construction is nonnegative for **every** real coefficient function `h(s)` after replacing `rho_n` by `h`. Worse for Mangoldt support, the induced local potential is already strictly positive at the radial boundary on every shell:

\[
\boxed{
\bigl(\rho_n^2-\rho_n'\bigr)(0^+)
=
\frac{\varphi(n)^2}{4}
+
\frac{J_2(n)}{12}
>0.
}
\tag{9}
\]

So the direct first-order factorization preserves neither the mixed-prime zero nor a source-specific positivity theorem. If one instead supplies the real connection with its compatible metric, it is again exactly flattened by multiplication by `e^{-G_n}`.

This closes the most direct attempt to promote the surviving signed radial flux into geometry **before** positivity is taken. It does not rule out a genuinely off-diagonal cross-shell connection, a matrix-valued finite--archimedean boundary operator, nontrivial topology imposed by an independently forced global construction, or a cohomological pairing whose curvature/intersection data exist before the one-dimensional radial restriction. Those would add exactly the nonseparable structure that the current research mandate still requires.

## 1. The cyclotomic radial connection is exact

For `n>1`, `Phi_n(x)` has no zero on `0<x<1` and `Phi_n(0)=1`, so `G_n` in (2) is a real smooth function on `[0,\infty)`. `WP-162` gives the endpoints

\[
G_n(0)=\log\Phi_n(1)=\Lambda(n),
\qquad
G_n(\infty)=0,
\tag{10}
\]

and

\[
\rho_n(s)=-G_n'(s).
\tag{11}
\]

Now set `U_n=e^{-iG_n}`. Direct differentiation gives

\[
U_n^{-1}U_n'
=
-iG_n'
=
i\rho_n.
\tag{12}
\]

Hence for every smooth compactly supported scalar function `f`,

\[
U_n^{-1}\frac d{ds}(U_nf)
=
f'+i\rho_nf
=
\nabla_nf,
\tag{13}
\]

which proves (4).

Equivalently, the `U(1)` connection one-form `i rho_n(s) ds` has zero curvature. This is automatic in one dimension, but here the primitive is not abstract: it is exactly the source-native cyclotomic chord potential already derived in `WP-161`--`WP-162`.

The important point is not that a one-dimensional connection is locally flat. It is that the **entire candidate arithmetic profile is itself an exact gauge derivative with a canonical primitive already present in the Mathia construction**.

## 2. Covariant Dirichlet positivity becomes the free energy

On `L^2(0,\infty;ds)`, multiplication by `U_n` is unitary. For the Dirichlet form on `H_0^1(0,\infty)`,

\[
\mathcal E_n^{\rm cov}(f)
:=
\int_0^\infty
|f'(s)+i\rho_n(s)f(s)|^2\,ds,
\tag{14}
\]

equation (13) gives

\[
\boxed{
\mathcal E_n^{\rm cov}(f)
=
\int_0^\infty |(U_nf)'|^2\,ds
=
\mathcal E_0(U_nf).
}
\tag{15}
\]

Because `rho_n` is bounded near zero and decays exponentially at infinity, `U_n` and `U_n^{-1}` preserve the usual `H^1` and Dirichlet domains. Thus the associated nonnegative covariant Laplacian is unitarily equivalent to the free Dirichlet Laplacian.

The same conclusion holds on any finite shell set `S` for the diagonal connection

\[
\nabla_S
=
d+i\,\operatorname{diag}(\rho_n)_{n\in S}\,ds:
\tag{16}
\]

the diagonal unitary `diag(U_n)` removes the whole connection. Merely taking more shell copies therefore does not create cross-shell geometry.

This is a stronger failure than the positive scalarizations excluded in `WP-162`. There the sign information was destroyed because one took an absolute value, square, or positive density of each profile. Here the signed profile is kept intact until after a first-order operator is formed, but **gauge invariance removes it before the positive energy can see it**.

## 3. Mixed-prime shells are based-gauge trivial

For every mixed-prime `n`, `Lambda(n)=0`. Equations (10) and (4) then give

\[
U_n(0)=e^{-iG_n(0)}=1,
\qquad
U_n(\infty)=e^{-iG_n(\infty)}=1.
\tag{17}
\]

So the gauge transformation is trivial at both radial endpoints.

The smallest control is `n=6`. `WP-162` derives

\[
\rho_6(s)
=
\frac{e^{-s}(2e^{-s}-1)}
{e^{-2s}-e^{-s}+1},
\tag{18}
\]

which is positive for `0<s<log 2`, negative afterward, and has exactly cancelling positive and negative masses. Yet

\[
G_6(0)=G_6(\infty)=0,
\tag{19}
\]

so the associated unitary connection is based-gauge equivalent to the zero connection.

This is a decisive matched control for the proposed mechanism. The detailed radial sign reversal is real and source-forced, but a scalar gauge geometry regards it as no geometry at all once endpoints are fixed.

Therefore a successful use of the signed cancellation cannot consist merely of declaring `rho_n ds` to be an Abelian connection on the same radial interval.

## 4. Prime powers leave only compact endpoint holonomy

For `n=p^a`, equation (10) gives

\[
\int_0^\infty\rho_{p^a}(s)\,ds
=
\log p.
\tag{20}
\]

If endpoint frames are held fixed, the unitary Wilson transport is

\[
\boxed{
\operatorname{Hol}_{p^a}=e^{-i\log p}.
}
\tag{21}
\]

The depth `a` disappears, consistently with `Lambda(p^a)=log p`. Hence the scalar connection does retain a prime-power invariant, but only as a compact phase.

For example,

\[
P_n:=|1-\operatorname{Hol}_n|^2
=
2-2\cos\Lambda(n)
\ge0
\tag{22}
\]

vanishes on every mixed-prime shell and gives a bounded phase-sensitive prime-power readout. This shows that endpoint transport need not erase the prime-power distinction completely, so the obstruction must not be overstated.

However, (22) has the wrong amplitude. More generally any continuous class function on `U(1)` is a continuous `2 pi`-periodic function of `Lambda`. Such a readout is bounded on the compact group, whereas

\[
\Lambda(p)=\log p\longrightarrow\infty.
\tag{23}
\]

Thus no continuous compact-phase readout can reproduce the linear prime coefficient on all primes. Independently, the critically attenuated coefficient `log p/sqrt(p^a)` depends on the depth `a`, which the transport (21) has already forgotten.

One could define a discontinuous or arithmetic-set-specific inverse from the phases `p^{-i}` back to `log p`, or choose a lift of the phase to a real angle. But that lift is not supplied by the `U(1)` connection itself. It reintroduces precisely the unwrapped scalar `G_n(0)=Lambda(n)` from which the connection was built, so it is not a new positivity mechanism.

Closing the radial interval into a loop does not change this conclusion for the direct scalar unitary route. A flat connection on a non-simply-connected loop can carry nontrivial holonomy, but the gauge-invariant datum remains the same compact phase (21), with the same periodic-amplitude obstruction.

## 5. The real first-order factorization has a universal sign theorem

A different idea is to avoid the compact phase and use the real coefficient directly. On the unweighted space `L^2(ds)`, take

\[
D_n=\partial_s+\rho_n.
\tag{24}
\]

On compactly supported smooth functions its formal adjoint is `D_n^*=-partial_s+rho_n`, so

\[
\boxed{
D_n^*D_n
=
-\partial_s^2
+\rho_n^2-\rho_n'.
}
\tag{25}
\]

Its quadratic form is

\[
\langle f,D_n^*D_nf\rangle
=
\|D_nf\|_2^2
\ge0.
\tag{26}
\]

This is the standard one-dimensional first-order/SUSY-Darboux factorization. It supplies an independent analytic proof of nonnegativity, but not an arithmetic one: for every sufficiently regular real function `h`,

\[
(-\partial_s+h)(\partial_s+h)
=
-\partial_s^2+h^2-h'
\tag{27}
\]

has exactly the same factorized sign.

The line-specific falsification is immediate from the source-forced boundary jet. `WP-164` gives

\[
\rho_n(0^+)=\frac{\varphi(n)}2,
\qquad
\rho_n'(0^+)=-\frac{J_2(n)}{12}.
\tag{28}
\]

Therefore

\[
\boxed{
V_n(0^+)
:=
\bigl(\rho_n^2-\rho_n'\bigr)(0^+)
=
\frac{\varphi(n)^2}{4}
+\frac{J_2(n)}{12}
>0
}
\tag{29}
\]

for every `n>1`.

In particular the mixed-prime control `n=6` has

\[
\rho_6(0^+)=1,
\qquad
\rho_6'(0^+)=-2,
\qquad
V_6(0^+)=3.
\tag{30}
\]

So the positive Schrödinger potential produced by the factorization has full shell support already at the boundary. The exact Mangoldt zero is not inherited by the local positive operator.

This does not prove that every spectral invariant of `D_n^*D_n` is useless. It proves the narrower claim relevant to the mandate: **its nonnegativity is a generic factorization theorem and does not explain the finite arithmetic cancellation that distinguished the cyclotomic flux.**

## 6. Giving the real connection its compatible metric flattens it again

There is a useful way to separate genuine geometry from the fixed-background factorization. Since `rho_n=-G_n'`, define the positive metric density

\[
w_n(s):=e^{-2G_n(s)}.
\tag{31}
\]

Multiplication by

\[
M_n(s):=e^{-G_n(s)}
\tag{32}
\]

is unitary from `L^2(w_n ds)` to ordinary `L^2(ds)`. Moreover,

\[
(M_nf)'
=
e^{-G_n}(f'-G_n'f)
=
M_n(f'+\rho_nf)
=
M_nD_nf.
\tag{33}
\]

Hence the metric-compatible energy is exactly

\[
\boxed{
\int_0^\infty
w_n(s)|D_nf(s)|^2\,ds
=
\int_0^\infty |(M_nf)'|^2\,ds.
}
\tag{34}
\]

Thus there is a sharp dichotomy.

If the scalar connection is treated geometrically together with the metric that makes its transport compatible, it is just the free derivative in a different frame. If one freezes an external flat `L^2(ds)` metric so that `D_n^*D_n` develops the potential (29), positivity is the universal factorization (27), and the first local invariant has full shell support.

Neither branch yields the desired Mathia-specific global Weil sign.

## 7. What survives: off-diagonal or genuinely global structure must be added before positivity

The result closes only the **direct diagonal scalar-connection** promotion of the signed radial flux:

\[
\rho_n(s)\,ds
\longrightarrow
\text{scalar covariant derivative}
\longrightarrow
\text{positive covariant/factorized energy}.
\tag{35}
\]

It does not close the accepted finite--archimedean incidence direction. Rather, it makes its missing ingredient more explicit.

An off-diagonal cross-shell operator could prevent the independent shell gauges from being simultaneously irrelevant: after diagonal trivialization, the off-diagonal coupling would acquire relative factors `U_m^{-1}U_n`. But that coupling is new mathematical structure. It must be forced independently by Prime Circle/Prime Flute/Prime Lattice or by a genuine finite--archimedean construction and must pass the `n=6` and global normalization controls. The scalar radial flux alone does not supply it.

Likewise, a matrix-valued boundary response, nontrivial global topology, intersection/cohomological pairing, or finite--archimedean superconnection may retain information not present in the direct line connection. Such a candidate must derive its curvature, endpoint coupling, or off-diagonal incidence before invoking positivity.

This is exactly the remaining burden imposed by the canonical research mandate: nonnegativity must follow from the assembled geometry, not from applying a universal square to independent shell coefficients after the arithmetic selector is already known.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed for the ambient gauge or factorization facts.

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Vol. I, originally Interscience (1963), Wiley Classics reprint (1996), develops connections, curvature, parallel transport, holonomy, and flat connections. The fact that a flat connection on an interval is gauge-trivial is standard connection theory.
- Fred Cooper, Avinash Khare, and Uday Sukhatme, *Supersymmetry and Quantum Mechanics*, Physics Reports **251** (1995), 267--385, DOI `10.1016/0370-1573(94)00080-M`, arXiv `hep-th/9405029`, reviews the one-dimensional factorization `A^\dagger A` with superpotential `W` and the associated partner Schrödinger operators.
- The possibility of nontrivial flat `U(1)` holonomy after changing the base from an interval to a loop is standard gauge/Aharonov--Bohm geometry. It is included here only as an adversarial boundary: it leaves the compact phase (21), not the linear Mangoldt amplitude.

Targeted searches for the structural combinations “cyclotomic logarithmic derivative + gauge connection”, “cyclotomic polynomial + superpotential”, and “cyclotomic + Darboux/SUSY quantum mechanics” did not identify a source asserting this exact Prime-Circle specialization. That absence is **not** used as a novelty claim.

The branch-local contribution is the synthesis with `WP-161`--`WP-164`: the strongest surviving source-native finite object, the signed inward cyclotomic flux, becomes exact gauge on its own radial interval; the mixed-prime cancellation is based-gauge trivial; compact holonomy retains only a bounded phase of the prime-power mass; and the direct real factorization replaces the sparse selector by a universal positive operator with full shell support.

This is not a restatement of Weil positivity, Hilbert--Polya, or a zero-based criterion. No zeta zeros, Weil kernel, regularization, or RH assumption enters the proof.

## 9. Exact audit surface and consequence

The claim can be checked without numerical approximation.

1. Verify the endpoint identities `G_n(0)=Lambda(n)` and `G_n(infinity)=0` from `WP-162`.
2. Differentiate `U_n=e^{-iG_n}` and recover `U_n^{-1}dU_n=d+i rho_n ds`.
3. Check the unitary energy identity (15).
4. For every mixed-prime shell, use `Lambda(n)=0` to obtain the based gauge (17); verify it explicitly for `n=6`.
5. For prime powers, compute the endpoint transport (21) and observe that continuous `U(1)` class functions are periodic/bounded in `log p`.
6. Expand `D_n^*D_n` to obtain (25).
7. Insert the exact boundary jet from `WP-164` and recover the strictly positive full-support value (29).
8. Check the compatible weighted flattening (34).

Failure of items 2--4 would invalidate the pure-gauge obstruction. Failure of items 6--7 would invalidate the fixed-metric factorization control. The remaining escapes are deliberately structural rather than technical: a successful continuation must introduce a source-forced off-diagonal/global coupling before positivity is taken.

The research frontier therefore narrows from

\[
\text{retain signed radial flux until an operator is formed}
\]

to

\[
\boxed{
\text{retain signed radial flux inside a genuinely coupled finite--archimedean or cross-shell operator whose nontrivial geometry survives gauge reduction.}
}
\]

A direct scalar covariant derivative does not meet that bar.

## Internal dependencies

- `research/weil_positivity/findings/WP-161-radial-cyclotomic-boundary-value-is-mangoldt-but-its-differential-jet-is-jordan-totient.md`
- `research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md`
- `research/weil_positivity/findings/WP-163-mellin-radial-readouts-have-a-unique-mangoldt-support-critical-exponent-at-alpha-one.md`
- `research/weil_positivity/findings/WP-164-positive-cyclotomic-radial-flux-is-never-a-positive-semigroup-coefficient.md`
- `research/weil_positivity/findings/WP-019-decoupled-supersymmetric-archimedean-completion-collapses-to-an-index.md`
