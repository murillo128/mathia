# PL-335 — Odd parity reverses the threshold archimedean source and restores a Hopf boundary lower law

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-SOURCE-SPECIFIC-MECHANISM + ROUTE-NARROWING`

**Status:** `ODD-THRESHOLD-HOPF-NONCOLLAPSE + FIXED-C0-GATE-CLOSED-IN-ODD-SECTOR + UNIFORM-SOURCE-GATE-REMAINS`

## Precise claim

The first-prime threshold analysis in `PL-329`--`PL-334` leaves a fixed-aperture boundary-amplitude gate: a branchwise first-prime sign law needs the canonical half-log boundary coefficient not to collapse at

\[
a_0=\frac12\log2.
\]

`PL-333` shows that the ordinary positive-state Hopf route fails on the full space: at `a_0` the bounded archimedean remainder has a strictly positive kernel, so a globally nonnegative threshold eigenstate would satisfy a logarithmic-Laplacian equation with the **wrong** boundary forcing sign. The odd sector behaves oppositely.

Let `u_0` be a real lowest eigenfunction of Suzuki's localized Weil operator restricted to the odd subspace at `a=a_0`, represented on the fixed interval `(-1,1)` and extended by zero outside. Choose its sign so that

\[
u_0(x)\ge0\qquad(0<x<1).
\tag{PL335-1}
\]

Such a choice is available from the exact odd-sector Beurling--Deny inequality of `PL-324`: replacing an odd function by

\[
u^{\#}(x)=\operatorname{sgn}(x)|u(x)|
\]

does not increase the threshold Rayleigh quotient, so a lowest odd minimizer may be chosen nonnegative on the positive half-line.

At the threshold the `p=2` translation has zero-measure overlap, and `PL-333` gives

\[
L_\Delta u_0
=\alpha_0u_0-2K_0u_0,
\qquad
\alpha_0:=2(\lambda_0-c_0-\gamma),
\tag{PL335-2}
\]

with

\[
(K_0u)(x)
=-a_0\int_{-1}^{1}r''(a_0(x-y))u(y)\,dy.
\tag{PL335-3}
\]

Define

\[
q(t):=-r''(t),
\qquad 0\le t\le\log2.
\tag{PL335-4}
\]

Then `q` is strictly increasing on this whole interval. Folding (PL335-3) against odd parity gives, for `0<x<1`,

\[
\boxed{
(K_0u_0)(x)
=a_0\int_0^1
\bigl[q(a_0|x-y|)-q(a_0(x+y))\bigr]u_0(y)\,dy<0.
}
\tag{PL335-5}
\]

The inequality is strict because `x+y>|x-y|`, `a_0(x+y)<\log2`, `q` is strictly increasing, and the ground state is nonzero and nonnegative on `(0,1)`. Hence

\[
\boxed{
L_\Delta u_0\ge \alpha_0u_0
\quad\text{in }(0,1),
}
\tag{PL335-6}
\]

with a strictly positive excess `-2K_0u_0` in the interior.

This is exactly the sign required by the antisymmetric maximum/Hopf theory of Pollastro--Soave. Using the continuity and zero-exterior regularity of localized-Weil eigenstates already used in `PL-319`--`PL-320`, their antisymmetric strong maximum principle first gives

\[
u_0(x)>0\qquad(0<x<1).
\tag{PL335-7}
\]

Then their antisymmetric Hopf lemma, applied on a sufficiently small interval-ball tangent to `x=1`, yields

\[
\boxed{
\liminf_{t\downarrow0}
\frac{u_0(1-t)}{\ell(t)^{1/2}}>0,
\qquad
\ell(t)=\frac1{|\log(\min\{t,0.1\})|}.
}
\tag{PL335-8}
\]

Equivalently, in the logarithmic endpoint coordinate

\[
Q=\log\frac{2}{1-x},
\]

there is a constant `c>0` such that

\[
\boxed{
\liminf_{Q\to\infty}\sqrt Q\,u_0(1-2e^{-Q})\ge c>0.
}
\tag{PL335-9}
\]

Therefore the **fixed-threshold half-log amplitude cannot collapse in the odd ground sector**. Whenever the actual boundary quotient

\[
C_0=\lim_{Q\to\infty}\sqrt Q\,u_0(1-2e^{-Q})
\tag{PL335-10}
\]

exists through the source-trace mechanism of `PL-320` or another matched-asymptotic argument, one necessarily has

\[
\boxed{C_0>0.}
\tag{PL335-11}
\]

This closes the fixed `C_0!=0` gate in the RH-relevant odd sector. It does **not** close the branchwise first-prime problem: the remaining requirement from `PL-329` is still a source bound strong enough, uniformly as `a\downarrow a_0` from above, to suppress the critical antisymmetric edge layer.

## 1. The archimedean kernel is radially increasing on the threshold range

`PL-333` records Suzuki's exact formula

\[
r''(t)
=-2\cosh(t/2)
+\frac{e^{t/2}}{2\sinh t}
-\frac1{2t},
\qquad t>0.
\tag{PL335-12}
\]

Write

\[
r''(t)=-2\cosh(t/2)+r_1''(t),
\]

and put `z=t/2`. The second term has the useful exact form

\[
r_1''(t)
=\frac14\left(\operatorname{csch}z+\operatorname{sech}z-\frac1z\right).
\tag{PL335-13}
\]

Differentiating with respect to `t` gives

\[
r_1'''(t)
=\frac18\left[
\frac1{z^2}
-\operatorname{csch}z\,\operatorname{coth}z
-\operatorname{sech}z\,\operatorname{tanh}z
\right].
\tag{PL335-14}
\]

For the required range

\[
0<z\le\frac12\log2<1,
\]

we have

\[
\operatorname{csch}z\,\operatorname{coth}z>\frac1{z^2}.
\tag{PL335-15}
\]

A direct proof avoids any numerical monotonicity claim. Inequality (PL335-15) is equivalent to

\[
h(z):=z^2\cosh z-\sinh^2z>0.
\]

Now

\[
h'(z)=2\cosh z\,(z-\sinh z)+z^2\sinh z.
\]

Since

\[
\sinh z-z
=\int_0^z(\cosh s-1)\,ds
\le\frac{z^3\cosh z}{6}
\]

and `sinh z>=z`, it follows that

\[
h'(z)
\ge z^3\left(1-\frac{\cosh^2z}{3}\right)>0
\qquad(0<z<1),
\]

because `cosh^2(1)<3`. Since `h(0)=0`, (PL335-15) follows. Therefore (PL335-14) is strictly negative, and

\[
q'(t)
=\sinh(t/2)-r_1'''(t)>0
\qquad(0<t\le\log2).
\tag{PL335-16}
\]

Thus the sign in (PL335-5) is an exact consequence of Suzuki's archimedean formula, not a numerical observation.

## 2. Odd folding reverses the `PL-333` source sign

The apparent tension with `PL-333` is resolved entirely by parity. Since `q=-r''` is even, (PL335-3) can be written

\[
(K_0u)(x)
=a_0\int_{-1}^{1}q(a_0|x-y|)u(y)\,dy.
\tag{PL335-17}
\]

For an odd `u` and `x>0`, split the integral into the positive and negative halves and substitute `y=-s` on the latter. This gives exactly

\[
(K_0u)(x)
=a_0\int_0^1
\left[
q(a_0|x-s|)-q(a_0(x+s))
\right]u(s)\,ds.
\tag{PL335-18}
\]

For `0<x,s<1`,

\[
0\le a_0|x-s|<a_0(x+s)<2a_0=\log2,
\]

so the bracket is strictly negative by (PL335-16). Any nonzero nonnegative positive-half profile therefore satisfies

\[
K_0u(x)<0\qquad(0<x<1).
\tag{PL335-19}
\]

By contrast, for the globally nonnegative control in `PL-333` there is no negative reflected half, and the same positive kernel gives `K_0u>0`. The two findings are therefore complementary:

\[
\begin{array}{ll}
\text{globally nonnegative state:} & -2K_0u<0\quad\text{(Hopf-unfavorable)},\\
\text{odd, positive on }(0,1): & -2K_0u>0\quad\text{(Hopf-favorable)}.
\end{array}
\]

The sign reversal is source-specific. It uses the exact completed archimedean kernel and the odd reflection geometry; it is not a generic property of the logarithmic Laplacian.

## 3. The lowest odd threshold state may be chosen positive on the half interval

`PL-324` proves at the exact threshold

\[
Q_W^{a_0}(u^{\#})\le Q_W^{a_0}(u)
\tag{PL335-20}
\]

for every real odd form-domain vector. Let `v` minimize the odd-sector Rayleigh quotient. Since `||v#||_2=||v||_2`, the vector `v#` is another minimizer, hence an eigenfunction at the lowest odd eigenvalue. Taking

\[
u_0=v^{\#}
\]

gives (PL335-1).

The localized operator has compact resolvent, so the minimizer exists. The regularity framework already used in `PL-319`--`PL-320` gives interior continuity and continuous zero boundary trace for these localized-Weil eigenstates. Equation (PL335-6) then puts `u_0` under Corollary 3.6 of Pollastro--Soave with the constant potential `V=alpha_0`: `u_0` is antisymmetric about `0`, nonnegative on the half-space `H=(0,infinity)`, and nonzero. Therefore

\[
u_0>0\quad\text{throughout }(0,1).
\]

This strong positivity is being used only to obtain a compact interior ball `B'` on which `u_0` has a positive lower bound. No positivity-preserving claim is made for the full or even threshold operator, and no extension of the odd Beurling--Deny property beyond `a_0` is inferred.

## 4. Pollastro--Soave supplies exactly the missing antisymmetric Hopf lemma

Pollastro and Soave prove an antisymmetric Hopf lemma for the logarithmic Laplacian. In the notation relevant here, if an antisymmetric function satisfies

\[
L_\Delta u\ge V(x)u
\]

in a domain inside a half-space, is nonnegative on the half-space, and is positive on a separated interior ball, then on a sufficiently small comparison ball `B` one obtains

\[
u(x)\ge C\ell(\operatorname{dist}(x,\partial B))^{1/2},
\]

provided `||V||_infinity<=lambda_1^L(B)`. Their quantitative small-ball estimate makes

\[
\lambda_1^L(B)\to+\infty
\]

as the radius tends to zero. Hence for the fixed constant `V=alpha_0` one can always choose a one-dimensional ball

\[
B=(1-2r,1)\subset(0,1)
\]

tangent to the physical endpoint `x=1` and small enough that the spectral hypothesis holds. Choose a disjoint compact interior interval-ball `B'` where (PL335-7) and continuity give `inf_{B'}u_0>0`. Lemma 3.4 then yields (PL335-8).

This use is genuinely different from the ordinary Hopf theorem rejected in `PL-333`. The comparison function in Pollastro--Soave is antisymmetric across the central hyperplane and exploits the favorable difference between a point and its reflection. That is exactly the geometry responsible for the negative folded `K_0` term in (PL335-18).

## 5. Consequence for the first-prime continuation program

`PL-329` proves that the newly active `p=2` reflected correlation is eventually oriented if

\[
\frac{1+S_\delta}
{|C_\delta|\sqrt{L_\delta}}
\longrightarrow0,
\tag{PL335-21}
\]

where `C_delta` is the source-selected critical coefficient and `S_delta` is the endpoint source amplitude. `PL-332` shows that under the relevant uniform source/remainder control, branch continuity transfers `C_delta` to the threshold coefficient `C_0`. Before the present finding, `PL-333` and `PL-334` had removed the standard full/even positivity routes to proving `C_0!=0`.

For the **odd ground branch**, the fixed-threshold noncollapse issue is no longer independent: the antisymmetric Hopf lower law forces the half-log amplitude to stay bounded away from zero at `a_0`. If a genuine quotient exists, its coefficient is strictly positive. Thus, in this sector the remaining first-prime burden is principally uniform control of the branchwise source amplitude/remainder as the shrinking rational-prime channel turns on.

This is useful precisely because the odd sector is arithmetic-sensitive: `PL-324` shows that its generic order positivity survives all archimedean effects up to `a_0` and fails exactly when the rational-prime translation acquires positive-measure overlap. The present result says that the threshold state itself enters that event with a noncollapsed canonical boundary channel.

No conclusion is made for the global even ground branch studied around `a=0.8` in `PL-284`, nor for the even threshold sector of `PL-334`. The mechanism depends essentially on antisymmetry.

## 6. Prior art, novelty, and adversarial audit

The antisymmetric maximum principles and Hopf lemmas are established prior art: Pollastro--Soave prove the exact strong maximum and `ell^{1/2}` Hopf statements used above. Suzuki supplies the localized Weil form and archimedean kernel through source 56. `PL-324` supplies the line-local odd modulus theorem at the first-prime threshold, while `PL-333` supplies the exact threshold decomposition and the sign obstruction for globally nonnegative states.

A targeted literature search around Suzuki's localized Weil operator together with antisymmetric logarithmic-Laplacian Hopf/maximum principles did not locate the particular folded-kernel sign mechanism (PL335-18) or its application to the first rational-prime threshold. Search absence is not treated as evidence of broad novelty. The durable `EXACT-DERIVED` contribution is the bridge: on the exact threshold range, Suzuki's completed archimedean kernel is strictly increasing after the sign change `q=-r''`; odd reflection therefore changes the remainder from a Hopf obstruction into a strict supersource, placing the lowest odd state inside Pollastro--Soave's theorem.

Adversarial boundaries:

- **No RH proof.** A half-log Hopf lower law for one finite-window odd eigenstate does not establish Weil positivity for all support radii.
- **No post-threshold order positivity.** `PL-324` proves the opposite: the odd Beurling--Deny criterion fails immediately after the first rational-prime overlap becomes active.
- **No claim that the boundary quotient exists from Hopf alone.** The result is a positive `liminf`. The statement `C_0>0` is conditional on existence of the quotient, as supplied by the separate source-trace/matching mechanism of `PL-320` or a future theorem.
- **No conflict with `PL-333`.** Its bad sign concerns a globally nonnegative state. Antisymmetry introduces the reflected negative half and changes `K_0u` to a difference of kernel values with the opposite sign.
- **No conflict with `PL-334`.** Even reflection pairs the continuous kernel by addition and loses order positivity before the prime event. The present difference structure exists only in the odd sector.
- **Monotonicity is proved only where needed.** The argument uses `q'(t)>0` on `0<t<=log2`; no global monotonicity of `-r''` is claimed.
- **The prime term is absent exactly at the threshold.** At `2a_0=log2` its overlap has measure zero. The argument does not silently ignore an active rational-prime operator.
- **The Hopf potential may have either sign.** Pollastro--Soave allow bounded sign-changing potentials and impose a norm bound relative to the comparison-ball eigenvalue. Shrinking the ball makes that eigenvalue arbitrarily large, so the fixed constant `alpha_0` causes no sign restriction.
- **Source specificity remains downstream.** The bad layer of `PL-327` is still possible for arbitrary nearby states and is graph-small by `PL-330`. What remains to be shown for the actual odd branch is the uniform source control that prevents such a layer from forming after activation.

## Consequence for the line

The fixed-threshold boundary-amplitude gate has a genuine positive mechanism in the odd sector:

\[
\boxed{
\text{odd modulus at }a_0
\ +\
q=-r''\text{ increasing}
\ \Longrightarrow\
K_0u_0<0
\ \Longrightarrow\
L_\Delta u_0\ge\alpha_0u_0
\ \Longrightarrow\
\text{antisymmetric Hopf noncollapse}.
}
\]

The current first-prime target should therefore not spend further effort trying to prove `C_0!=0` for the lowest odd threshold state via ordinary positivity. The productive remaining gate is quantitative and moving: prove enough uniform control of the actual odd eigenbranch source/remainder for `a>a_0` to invoke `PL-329`, or derive an equivalent source-selected suppression of the critical reflected edge layer.

## Sources

- Luigi Pollastro, Nicola Soave, “Antisymmetric maximum principles and Hopf’s lemmas for the Logarithmic Laplacian, with applications to symmetry results,” *Annali di Matematica Pura ed Applicata* **204** (2025), 1827--1845. DOI: `10.1007/s10231-025-01549-0`; arXiv:`2407.11718`. Proposition 3.1, Lemma 3.4, Remark 3.5, and Corollary 3.6 are the load-bearing maximum/Hopf inputs.
- Source 56 in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2`; exact localized form, parity invariance, and archimedean kernel.
- Source 96: Huyuan Chen, Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*; principal Dirichlet realization and compact spectral framework.
- Source 97: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*; canonical `ell^{1/2}` boundary scale.
- `PL-324`: exact odd-sector Beurling--Deny threshold at the first rational-prime event.
- `PL-329`, `PL-332`: source-amplitude criterion and branchwise coefficient transport.
- `PL-333`, `PL-334`: full/even positivity and ordinary Hopf obstructions that the antisymmetric mechanism bypasses.
