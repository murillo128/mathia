---
type: negative
research_line: xi_flow
finding_id: XF-166
status: canonical
---

# XF-166 — Real-axis Jacobi inversion plus a positive prekernel does not fix the Xi heat origin

**Confidence:** high. The Jacobi identity used below is derived directly from the periodized Gaussian, the Xi source factorization is an exact differentiation, and the counterexample is the Gaussian heat-origin tilt already controlled in XF-163. The only external Xi fact needed for the zero statement is the established Rodgers--Tao bound `Lambda_Xi >= 0`, already anchored in `SOURCES.md`.

## Statement

XF-165 left an exact global theta/modular identity as one of the few source-side structures not defeated by finite interpolation and tail splicing. The first natural candidate is the real-axis Jacobi inversion law itself. In the Xi normalization used by this line, that law is still too weak.

Let

\[
F_\Xi(x):=\sum_{n\ge1}e^{-\pi n^2x},
\qquad
\Theta_\Xi(x):=1+2F_\Xi(x),
\qquad x>0,
\tag{1}
\]

and introduce the prekernel coordinate

\[
S_\Xi(u):=e^uF_\Xi(e^{4u}).
\tag{2}
\]

Then the Xi source of XF-162 satisfies the exact differential extraction

\[
\boxed{
\Phi(u)=\frac18\bigl(S_\Xi''(u)-S_\Xi(u)\bigr).
}
\tag{3}
\]

The Jacobi inversion formula

\[
\Theta_\Xi(x)=x^{-1/2}\Theta_\Xi(1/x)
\tag{4}
\]

is equivalent under `x=e^(4u)` to

\[
\boxed{
S_\Xi(u)-S_\Xi(-u)=-\sinh u.
}
\tag{5}
\]

Applying `D_u^2-1` to `(5)` immediately gives the familiar evenness `Phi(u)=Phi(-u)` because `sinh u` lies in the homogeneous kernel of that operator.

The converse direction is the obstruction. Let `rho` be any even real-analytic source with all finite exponential moments, and define

\[
\boxed{
S_\rho(u)
:=\frac12e^{-u}
-4\int_{\mathbb R}e^{-|u-v|}\rho(v)\,dv.
}
\tag{6}
\]

Then

\[
\boxed{
S_\rho''-S_\rho=8\rho,
\qquad
S_\rho(u)-S_\rho(-u)=-\sinh u.
}
\tag{7}
\]

Consequently, if

\[
F_\rho(x):=x^{-1/4}
S_\rho\!\left(\frac14\log x\right),
\qquad
\Theta_\rho(x):=1+2F_\rho(x),
\tag{8}
\]

then **every such even source admits a real-axis prekernel satisfying the same Jacobi inversion law**:

\[
\boxed{
\Theta_\rho(x)=x^{-1/2}\Theta_\rho(1/x).
}
\tag{9}
\]

It also has exactly the same differential source extraction,

\[
\boxed{
\rho\!\left(\frac14\log x\right)
=x^{5/4}\bigl(2xF_\rho''(x)+3F_\rho'(x)\bigr).
}
\tag{10}
\]

There is a stronger positivity statement for the controls relevant to XF-163--XF-165. If

\[
0<\rho(u)\le\Phi(u)
\qquad(u\in\mathbb R),
\tag{11}
\]

then

\[
\boxed{
S_\rho(u)\ge S_\Xi(u)>0,
\qquad
F_\rho(x)>0,
\qquad
\Theta_\rho(x)>1.
}
\tag{12}
\]

Moreover `F_rho(x)->0` and hence `Theta_rho(x)->1` as `x->infinity`. Thus real-axis Jacobi inversion, positivity of the prekernel, the usual cusp-side normalization, and the Xi differential extraction can all coexist with a non-Xi source.

Taking the exact Gaussian tilt

\[
\rho_\tau(u):=e^{-\tau u^2}\Phi(u),
\qquad \tau>0,
\tag{13}
\]

provides the decisive counterexample. It obeys `(11)`, so its reconstructed `Theta_tau` satisfies `(9)--(12)`, but its heat orbit is exactly

\[
\mathcal H_t^{(\tau)}(z)=H_{t-\tau}(z).
\tag{14}
\]

Since `Lambda_Xi>=0`, `H_{-tau}` has a nonreal zero. Therefore

\[
\boxed{
\mathcal H_0^{(\tau)}
\text{ has a nonreal zero even though its positive prekernel obeys the exact real-axis Jacobi inversion law.}
}
\tag{15}
\]

The same Green reconstruction applies to the analytic soft-splice and finite-notch sources of XF-164--XF-165 because those multipliers are even and keep `0<rho<=Phi`.

Hence **the real-axis modular reflection law is not the global Xi rigidity still missing after XF-165**. What survives must use information that is lost when the actual theta series is replaced by an arbitrary positive reciprocal prekernel: coefficient-level or complex-modular structure, not reflection symmetry alone.

## 1. The Xi source is a differential projection of the theta prekernel

For a single summand in `(1)`, put `a=pi n^2` and

\[
f_a(u):=e^u e^{-ae^{4u}}.
\tag{16}
\]

A direct differentiation gives

\[
f_a'(u)=f_a(u)(1-4ae^{4u})
\tag{17}
\]

and

\[
f_a''(u)-f_a(u)
=8a e^{4u}f_a(u)(2ae^{4u}-3).
\tag{18}
\]

Therefore

\[
\frac18(f_a''-f_a)
=a e^{5u}(2ae^{4u}-3)e^{-ae^{4u}},
\tag{19}
\]

which is exactly the `n`th term of the source normalization used in XF-162. The theta series and all differentiated series converge absolutely on compact `u`-sets, so summing `(19)` proves `(3)`.

Equivalently, if `x=e^(4u)` and `S=e^uF(x)`, then elementary differentiation gives

\[
S''-S
=8x^{5/4}(2xF''+3F'),
\tag{20}
\]

which proves `(10)` whenever `(7)` holds.

This factorization is useful because it separates two logically different pieces of the true source: the second-order projector `D_u^2-1`, and the much more rigid statement that its preimage is specifically the square-lattice theta series `(1)`.

## 2. Jacobi inversion becomes a one-dimensional reflection identity

For completeness, the needed Jacobi identity can be obtained directly from the Gaussian. Periodize

\[
P_x(t):=\sum_{n\in\mathbb Z}e^{-\pi x(t+n)^2},
\qquad x>0.
\tag{21}
\]

Its `k`th Fourier coefficient is the elementary Gaussian transform

\[
\int_{\mathbb R}e^{-\pi xy^2}e^{-2\pi iky}\,dy
=x^{-1/2}e^{-\pi k^2/x}.
\tag{22}
\]

Absolute convergence of the periodization and its Fourier series therefore gives, at `t=0`,

\[
\sum_{n\in\mathbb Z}e^{-\pi n^2x}
=x^{-1/2}
\sum_{k\in\mathbb Z}e^{-\pi k^2/x},
\tag{23}
\]

which is `(4)`.

Now set `x=e^(4u)`. From `(4)`,

\[
1+2F_\Xi(e^{4u})
=e^{-2u}\bigl(1+2F_\Xi(e^{-4u})\bigr).
\tag{24}
\]

Multiplying by `e^u/2` and using `(2)` yields

\[
S_\Xi(u)=S_\Xi(-u)-\sinh u,
\tag{25}
\]

which is `(5)`.

The key point is that the differential projector in `(3)` kills the entire inhomogeneous term in `(25)`. At the level of the source itself, the directly visible shadow of Jacobi inversion is therefore only evenness. The next section shows that even lifting back to a positive prekernel does not restore uniqueness.

## 3. Every even source has a synthetic Jacobi-reflecting prekernel

The distributional Green identity

\[
(D_u^2-1)e^{-|u-v|}=-2\delta_v
\tag{26}
\]

implies immediately from `(6)` that

\[
(D_u^2-1)S_\rho=8\rho.
\tag{27}
\]

Because both `rho` and `e^{-|u|}` are even, their convolution is even. Hence

\[
\begin{aligned}
S_\rho(u)-S_\rho(-u)
&=\frac12(e^{-u}-e^u)\\
&=-\sinh u,
\end{aligned}
\tag{28}
\]

which proves `(7)`. Although the Green kernel has a cusp, `(27)` and analyticity of `rho` imply that `S_rho` is real analytic by the ordinary differential equation.

Insert `(8)` into `(28)`. Since `x=e^(4u)`, one has

\[
F_\rho(x)=e^{-u}S_\rho(u),
\qquad
F_\rho(1/x)=e^uS_\rho(-u).
\tag{29}
\]

Then

\[
\begin{aligned}
1+2F_\rho(x)
&=1+2e^{-u}S_\rho(-u)-2e^{-u}\sinh u\\
&=e^{-2u}+2e^{-u}S_\rho(-u)\\
&=x^{-1/2}\bigl(1+2F_\rho(1/x)\bigr),
\end{aligned}
\tag{30}
\]

proving `(9)`.

Thus the real-axis functional equation is not a uniqueness condition on the prekernel once the square-lattice expansion is forgotten. It can be synthesized from any even source by solving one linear ODE with the reflection normalization built into the homogeneous term.

## 4. The entire current counterexample family can keep the prekernel positive

It remains possible that `(9)` is weak only because the synthetic prekernel changes sign. For the controls actually produced by this line, even that repair fails.

First observe that the genuine `S_Xi` from `(2)` also equals the Green representation `(6)` with `rho=Phi`. Both functions satisfy `(3)`, both satisfy the reflection law `(5)`, and both tend to zero as `u->+infinity`. Their difference therefore solves

\[
Y''-Y=0
\tag{31}
\]

and is even. Hence it is `C cosh u`; decay at `+infinity` forces `C=0`.

If `(11)` holds, subtracting the two Green formulas gives

\[
S_\rho(u)-S_\Xi(u)
=4\int_{\mathbb R}e^{-|u-v|}
\bigl(\Phi(v)-\rho(v)\bigr)\,dv
\ge0.
\tag{32}
\]

But `(1)--(2)` give `S_Xi(u)>0`, so `(12)` follows. The all-exponential-moment hypothesis also implies from `(6)` that `S_rho(u)=O(e^{-u})` as `u->+infinity` for the present double-exponentially decaying controls, and hence

\[
F_\rho(x)=O(x^{-1/2}),
\qquad
\Theta_\rho(x)\to1.
\tag{33}
\]

The Gaussian tilt `(13)` satisfies all these hypotheses. So do the XF-164 soft splice and the XF-165 finite-jet notch construction: their multipliers are even, lie in `(0,1]`, and preserve the Xi double-exponential envelope. Real-axis inversion plus positivity and the standard `x->infinity` normalization therefore do not distinguish any of these controls from Xi.

## 5. The surviving rigidity is coefficient-level, not reflection-level

The genuine Xi prekernel has a feature absent from the argument above:

\[
\boxed{
F_\Xi(x)=\sum_{n\ge1}e^{-\pi n^2x}.
}
\tag{34}
\]

This is not merely a positive function satisfying `(4)`. It is an exact Laplace superposition with unit masses on the arithmetic square lattice

\[
\{\pi n^2:n\ge1\}.
\tag{35}
\]

For a general source, the reconstruction is explicit:

\[
\boxed{
F_\rho(x)
=\frac12x^{-1/2}
-4x^{-1/4}
\int_{\mathbb R}
\exp\!\left(-\left|\frac14\log x-v\right|\right)
\rho(v)\,dv.
}
\tag{36}
\]

Equation `(36)` gives a concrete next test rather than the vague instruction to “use modularity”. Apply it first to the exact tilted source `rho_tau=e^(-tau u^2)Phi`. Determine whether `F_{rho_tau}` already fails a finite-order complete-monotonicity inequality. If it does, complete monotonicity is a genuine global gauge-breaking discriminator not covered by XF-165. If it does not, inspect the inverse-Laplace spectrum and test whether mass necessarily leaves the square lattice `(35)`.

Either outcome sharpens the source frontier. The eventual theorem still needs more than an Xi-specific classifier: the coefficient/spectral restriction must be propagated quantitatively to the mesoscopic mass or collision geometry that controls the de Bruijn--Newman transition.

## Relation to prior findings

XF-162 identified an Xi-specific tail hazard. XF-163 showed that it is blind to Gaussian heat-origin translation. XF-164 showed that beyond-all-orders Xi tail agreement remains noncoercive, and XF-165 showed that adding any fixed finite bank of exact local source jets does not repair the problem.

XF-166 tests the first genuinely global-looking candidate suggested by that sequence. The answer is negative but more selective: **the real-axis Jacobi inversion law itself, even with a positive normalized prekernel and the exact differential extraction of the source, is still compatible with the same shifted-Xi counterexamples**.

The surviving distinction is therefore pushed one level deeper, from modular reflection to the arithmetic representation that realizes that reflection. This is exactly the kind of infinite-dimensional constraint the finite-notch construction of XF-165 cannot trivially interpolate.

## Prior-art and novelty audit

The Jacobi theta transformation is classical; a targeted audit confirmed the standard lattice-parameter transformation for `theta_3` and the conventional derivation of Xi-kernel evenness from it. The proof above derives the needed real-axis identity directly from the periodized Gaussian, so no newly located theorem is load-bearing. `SOURCES.md` therefore requires no update.

The targeted search did not locate a source formulating the project-specific no-go used here: invert the Xi differential projector by the one-dimensional Green kernel, show that every even sub-Xi source acquires a **positive** normalized reciprocal prekernel, and then apply the exact Gaussian heat-origin tilt to retain nonreal zero geometry. That obstruction, and the resulting separation between reflection-level and coefficient-level theta rigidity, are the derived contribution of this finding.

There is a classical conceptual analogue in converse-theorem work: a functional equation becomes genuinely characterizing only when accompanied by additional analytic/coefficient structure. XF-166 does not invoke any converse theorem; it reaches the narrower source-level statement directly.

## Falsification boundary

This finding does **not** construct a second Jacobi theta function in the full modular-form sense. `Theta_rho` is proved only on the positive real axis and is not claimed to possess the complex `tau -> tau+1` transformation, a holomorphic modular extension, the theta `q`-expansion, or square-lattice Fourier coefficients.

It also does not show that complete monotonicity of `F_rho` fails for the Gaussian tilt; that is deliberately left as the next discriminating test. Nor does it prove that the exact square-lattice representation `(34)` is coercive for the transition. If that structure merely labels Xi without controlling the transition-forming mesoscopic mass, the source program would still need an additional bridge.

Finally, the Green lift is a post-source reconstruction. Any proof that uses the **a priori** theta coefficient representation before applying the differential projector is outside the no-go class and remains viable.

## Consequence for `xi_flow`

Do not spend the next pass trying to turn `Phi(u)=Phi(-u)` or the real-axis Jacobi inversion formula into the missing source theorem. Those properties are now explicitly realizable by the existing shifted-Xi controls, even with positivity and normalization of the reconstructed prekernel.

The immediate gate is to test the reconstructed `F_{rho_tau}` from `(36)` against stronger genuinely arithmetic/global theta properties. Complete monotonicity is the cheapest first discriminator; if it survives, move directly to the inverse-Laplace support and the exact square lattice `(35)`. Only after locating a property that the Gaussian tilt and XF-164--XF-165 controls actually violate should the line attempt to transport that property into zero-collision or transition bounds.
