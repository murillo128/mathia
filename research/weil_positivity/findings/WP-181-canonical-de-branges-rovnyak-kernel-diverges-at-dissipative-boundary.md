# WP-181 — Canonical de Branges–Rovnyak positivity diverges at a dissipative boundary; the phase survives only in a sign-indefinite finite part

**Status:** `EXACT-BOUNDARY-ASYMPTOTIC + CANONICAL-POSITIVE-KERNEL + PASSIVE-MATCHED-CONTROL + SIGN-INDEFINITE-FINITE-PART + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION`.

`WP-180` shows that ordinary dissipative Schur passivity is too weak to force a one-sided boundary phase. It leaves a stricter possibility open: perhaps the **canonical positive kernel attached to the Schur function itself** supplies the missing geometric sign. The scalar de Branges–Rovnyak kernel on the right half-plane is the first canonical test of that escape.

The result is negative in a precise way. At a genuinely dissipative regular boundary point, the positive diagonal kernel is dominated by a universal positive **absorption pole**. The boundary phase derivative occurs one order lower. If that forced pole is subtracted asymptotically, the surviving finite term is exactly a weighted phase derivative and can change sign even for the elementary passive one-port of `WP-180`.

Thus

\[
\boxed{
\text{canonical Schur-kernel positivity}
\;\not\Longrightarrow\;
\text{a finite positive dissipative boundary-phase observable}
}
\tag{1}
\]

at the scalar regular-boundary level. The lossless case is different: there the absorption pole vanishes and the same kernel reduces to the classical Julia--Carathéodory one-sided boundary law.

## 1. Canonical positive kernel and exact boundary expansion

Let `S` be a scalar Schur function on the right half-plane

\[
\mathbb C_+=\{s:\operatorname{Re}s>0\},
\qquad |S(s)|\le 1,
\tag{2}
\]

and suppose `S` extends holomorphically through a boundary point `i\omega_0` with

\[
S(i\omega_0)\ne0.
\tag{3}
\]

The scalar right-half-plane de Branges--Rovnyak kernel is

\[
K_S(s,w)
=
\frac{1-S(s)\overline{S(w)}}{s+\overline w}.
\tag{4}
\]

For a Schur function this kernel is positive. In particular, on the diagonal `s=x+i\omega`, `x>0`,

\[
K_S(s,s)
=
\frac{1-|S(x+i\omega)|^2}{2x}
\ge0.
\tag{5}
\]

Because of (3), choose a local holomorphic logarithm

\[
\log S(s)=u(x,\omega)+iv(x,\omega),
\qquad s=x+i\omega.
\tag{6}
\]

Write the boundary modulus and a continuous local phase branch as

\[
r(\omega)=|S(i\omega)|,
\qquad
\theta(\omega)=\arg S(i\omega)=v(0,\omega).
\tag{7}
\]

The Cauchy--Riemann equations give

\[
u_x(0,\omega)=v_\omega(0,\omega)=\theta'(\omega).
\tag{8}
\]

Since `|S|^2=e^{2u}`,

\[
|S(x+i\omega)|^2
=
r(\omega)^2
+2x\,r(\omega)^2\theta'(\omega)
+O(x^2).
\tag{9}
\]

Substitution into (5) yields the exact first two boundary orders

\[
\boxed{
K_S(x+i\omega,x+i\omega)
=
\frac{1-r(\omega)^2}{2x}
-r(\omega)^2\theta'(\omega)
+O(x).
}
\tag{10}
\]

This formula separates two geometrically different pieces of the same canonical positive kernel:

\[
\underbrace{\frac{1-r^2}{2x}}_{\text{dissipative loss / absorption}}
\qquad\text{and}\qquad
\underbrace{-r^2\theta'}_{\text{finite phase term}}.
\tag{11}
\]

No zeta zero, Gamma factor, prime coefficient, determinant regularizer, or hand-picked kernel has entered the derivation.

## 2. Dissipation makes the positive kernel infinite before the phase is reached

At a genuinely dissipative boundary point,

\[
0<r(\omega)<1.
\tag{12}
\]

Then the first term in (10) is strictly positive and

\[
K_S(x+i\omega,x+i\omega)
\sim
\frac{1-r(\omega)^2}{2x}
\longrightarrow +\infty
\qquad(x\downarrow0).
\tag{13}
\]

So the canonical positive diagonal does **not** produce a finite boundary energy whose sign can be identified with the phase derivative. Its positivity is already exhausted by the divergent loss term.

By contrast, at a regular unimodular boundary point,

\[
r(\omega)=1,
\tag{14}
\]

the pole vanishes and (10) becomes

\[
\lim_{x\downarrow0}K_S(x+i\omega,x+i\omega)
=-\theta'(\omega)\ge0
\tag{15}
\]

whenever the finite boundary kernel exists. This is the right-half-plane orientation of the classical Julia--Carathéodory/de Branges--Rovnyak boundary mechanism. It is exactly the lossless rigidity already encountered in `WP-171`--`WP-179`: positivity reaches the phase only because there is no boundary loss to dominate it.

Equation (10) therefore identifies the structural change caused by dissipation. The positive object survives, but its leading boundary observable is `1-r^2`, not the signed phase required by the branch.

## 3. The forced finite part is not positive

A natural asymptotic question is whether one can remove only the forced leading absorption pole in (10) and inherit positivity in the remainder. Define the pointwise asymptotic finite part, when the regular expansion above applies, by

\[
\operatorname{FP}K_S(i\omega)
:=
\lim_{x\downarrow0}
\left[
K_S(x+i\omega,x+i\omega)
-
\frac{1-r(\omega)^2}{2x}
\right].
\tag{16}
\]

Then (10) gives

\[
\boxed{
\operatorname{FP}K_S(i\omega)
=-r(\omega)^2\theta'(\omega).
}
\tag{17}
\]

Nothing in positivity of the unrenormalized kernel forces the right-hand side of (17) to have one sign. Subtracting the positive divergent term is not a positivity-preserving operation. Therefore any proposal that uses this finite part as the desired boundary scalar needs a **new theorem of positivity after subtraction**; that theorem does not come from ordinary de Branges--Rovnyak kernel positivity.

This is stronger than the generic observation of `WP-180`. There the raw phase could change sign despite passivity. Here the candidate canonical positive RKHS object is inserted explicitly, and the same phase is shown to sit precisely in the sign-uncontrolled coefficient *behind* its divergent dissipative boundary term.

## 4. Exact passive matched control

Use the same arithmetic-free passive family as `WP-180`,

\[
S_{a,b}(s)=\frac{s+a}{s+b},
\qquad 0<a<b.
\tag{18}
\]

It is strict Schur on `Re s>0` and is the normalized reflection coefficient of the positive-real impedance

\[
Z_{a,b}(s)
=
\frac{1+S_{a,b}(s)}{1-S_{a,b}(s)}
=
\frac{a+b}{b-a}+\frac{2}{b-a}s,
\tag{19}
\]

so the control is an elementary positive resistor plus positive inductive term, not a target-fitted analytic function.

Its boundary modulus and phase derivative are

\[
r(\omega)^2
=
\frac{a^2+\omega^2}{b^2+\omega^2},
\tag{20}
\]

and

\[
\theta'_{a,b}(\omega)
=
\frac{(b-a)(ab-\omega^2)}
{(a^2+\omega^2)(b^2+\omega^2)}.
\tag{21}
\]

The canonical diagonal kernel can be evaluated exactly before taking any limit:

\[
\boxed{
K_{a,b}(x+i\omega,x+i\omega)
=
\frac{(b-a)(2x+a+b)}
{2x\bigl((x+b)^2+\omega^2\bigr)}.
}
\tag{22}
\]

Its forced leading loss pole is

\[
\frac{b^2-a^2}{2(b^2+\omega^2)}\,\frac1x.
\tag{23}
\]

Subtracting exactly that leading asymptotic term and taking `x\downarrow0` gives

\[
\boxed{
\operatorname{FP}K_{a,b}(i\omega)
=
-\frac{(b-a)(ab-\omega^2)}{(b^2+\omega^2)^2}
=-r(\omega)^2\theta'_{a,b}(\omega).
}
\tag{24}
\]

Consequently

\[
\operatorname{FP}K_{a,b}(i\omega)
\begin{cases}
<0,& |\omega|<\sqrt{ab},\\
=0,& |\omega|=\sqrt{ab},\\
>0,& |\omega|>\sqrt{ab}.
\end{cases}
\tag{25}
\]

while the full kernel (22) remains positive for every `x>0`. This is the decisive matched control: **canonical positivity and finite-part sign-indefiniteness coexist in the same elementary passive object**.

The crossover remains freely tunable as in `WP-180`: choosing `a=\Omega/c`, `b=c\Omega` with `c>1` places it at any prescribed `\Omega>0`. Hence the sign change of the finite term cannot itself be evidence that the canonical positive kernel has encoded the arithmetic real place.

## 5. Why this blocks the obvious de Branges--Rovnyak escape

The candidate escape after `WP-180` was attractive because it appeared to have all three ingredients missing from raw dissipative phase: a canonical Hilbert space, a positive reproducing kernel, and a direct connection to passive Schur transfer functions. Equations (10)--(25) show why those ingredients still do not yield the branch target.

For genuinely dissipative boundary data, the scalar RKHS norm seen by the diagonal blows up with the local absorption deficit. The signed phase occurs only in the next coefficient. Extracting that coefficient requires a subtraction/renormalization, and the exact passive control proves that the extracted scalar is not positive. Thus the route has merely moved the sign problem from `theta'` into a finite part of a positive kernel.

This also supplies a matched lossless control. When `r=1`, the divergent term is absent and the finite boundary kernel itself is positive, reproducing the classical one-sided law. Therefore the failure is not caused by a sign mistake or by choosing the wrong half-plane orientation. It is caused precisely by entering the dissipative class needed to evade the lossless Gamma-phase obstruction.

The resulting trilemma is:

\[
\boxed{
\begin{array}{ll}
\text{lossless / unimodular:}&\text{finite canonical boundary positivity, but rigid one-sided phase};\\[2mm]
\text{dissipative / non-inner:}&\text{phase can change sign, but canonical positive diagonal diverges};\\[2mm]
\text{finite-part extraction:}&\text{phase is recovered, but its sign is uncontrolled.}
\end{array}
}
\tag{26}
\]

This directly sharpens the source-to-destination conditioning gate in the current branch synthesis: category change alone is not enough. A viable dissipative geometry must explain how the loss sector and phase sector are combined **before** scalarization so that a finite positive object survives.

## 6. Aggressive falsification and exact scope

This finding does **not** prove that every de Branges--Rovnyak or dissipative realization is irrelevant. The calculation is deliberately scalar, diagonal, and regular at the boundary. It leaves open matrix-valued kernels whose nontrivial compressions carry additional information; off-diagonal pairings; source-derived quotients imposed before the boundary limit; distributional or singular boundary spaces; vector-valued channels; nonlinear finite--archimedean couplings; and geometries whose positive observable is not the raw de Branges--Rovnyak diagonal.

It also does not prove that no strict dissipative subclass can have a positive renormalized boundary form. Such a subclass would, however, need an **additional source-derived coercivity/order theorem** beyond Schur contractivity and ordinary kernel positivity. The theorem must canonically absorb or cancel the loss pole while keeping the resulting coupled object positive; it cannot simply declare the finite part (16) positive, because the passive family (18) falsifies that assertion.

Normalizing the kernel, choosing another subtraction, or compressing away the divergent direction are therefore not automatic escapes. They are new constructions and must pass the branch controls: the operation must be forced by Mathia-native geometry before comparison with zeta/Gamma data, survive arithmetic-free matched controls, and still generate the finite-prime and archimedean/global pieces from one object.

Finally, no claim is made at boundary zeros `S(i\omega)=0`, where the local phase used in (6)--(10) is not defined. Such points cannot directly implement the phase-encoding route tested here.

## 7. Prior-art and novelty audit

The underlying function theory is classical. Positivity of de Branges--Rovnyak kernels for Schur functions and their right-half-plane functional-model realization are standard. A direct right-half-plane reference is Joseph A. Ball, Mikael Kurula, Olof J. Staffans, and Hans Zwart, *De Branges--Rovnyak Realizations of Operator-Valued Schur Functions on the Complex Right Half-Plane*, Complex Analysis and Operator Theory 9(4), 723--792 (2015), DOI `10.1007/s11785-014-0358-2`, arXiv `1307.7408`. The later conservative model is Joseph A. Ball, Mikael Kurula, and Olof J. Staffans, *A Conservative de Branges--Rovnyak Functional Model for Operator Schur Functions on C+*, Complex Analysis and Operator Theory 12(4), 877--915 (2018), DOI `10.1007/s11785-017-0746-5`.

The boundary principle in the unimodular case is likewise classical Julia--Carathéodory theory. In disk normalization, the standard quantity `(1-|S(z)|^2)/(1-|z|^2)` is the diagonal de Branges--Rovnyak kernel norm, and finite boundary behavior at a unimodular point is equivalent to the appropriate angular-derivative condition. No novelty is claimed for that theorem, for kernel positivity, or for the local Cauchy--Riemann expansion itself.

The Mathia-specific delta is the **exact adversarial comparison of the live `WP-180` dissipative escape with its canonical positive RKHS kernel**. The calculation identifies where the candidate positivity goes at a lossy boundary and then tests the forced finite coefficient on the same physically passive rational control:

\[
\boxed{
\text{positive dBR kernel}
=
\text{divergent absorption}
+
\text{sign-indefinite phase finite part}
+o(1).
}
\tag{27}
\]

This does not constitute a new theorem about de Branges--Rovnyak spaces. It is a branch-specific no-go: **ordinary canonical Schur-kernel positivity does not repair the sign theorem lost when the Mathia boundary route moves from lossless to dissipative dynamics**.

## 8. Research consequence

`WP-179` shows that ordinary lossless passive determinant channels are too sign-rigid; `WP-180` shows that generic dissipative passivity is too flexible; `WP-181` now shows that attaching the canonical scalar de Branges--Rovnyak positive kernel to that dissipative class does not bridge the gap. Its positive boundary mass is the loss divergence, while the desired phase survives only after a sign-destroying finite-part extraction.

The next viable version of the dissipative route is therefore narrower:

> Find a **source-derived coupled positive object** in which the dissipative loss direction is quotiented, compressed, or paired with the finite-prime/archimedean sector *before* the boundary limit, and prove positivity of that resulting object independently of the Weil target.

A successful construction must derive that operation from Prime Circle, Prime Flute, Prime Lattice, or another Mathia-native geometry; it must not introduce the quotient or counterterm because (10) reveals what needs cancelling. It must also survive the passive control (18), or explain by a source-derived invariant why that control is excluded. Until such a theorem exists, de Branges--Rovnyak kernel positivity is another classical positive structure that does not yet become global Weil positivity.