# PF-235 — hypercycle boundary compactification has only a quadratic prime-dependent defect

**Status:** `EXACT-DERIVED + COORDINATE-FACTORIZATION + SUMMABLE-GEOMETRIC-DEFECT + POSITIVE/ROUTE-NARROWING`. PF-231 puts the complete neighboring-axis corridor in logarithmic coordinates `z=e^{x+i\theta}` and PF-234 controls the actual PF-205 symmetric seam normalizer in its intrinsic Fermi coordinate. The remaining conformal-transfer clue still has to put those objects into one boundary representation, where the physical hypercycle density has the singular endpoint factor `1/\sin\theta`.

The singular factor is not a new seam-dependent degeneration. Let

\[
\tau=\log\tan\frac\theta2,
\qquad \frac{d\tau}{d\theta}=\frac1{\sin\theta},
\]

be signed arclength on the untrimmed axis, and let the inward hypercycle be at distance `\rho`, with `w=\sinh\rho`. If `t` is the Fermi footpoint arclength on that axis for the hypercycle point whose logarithmic angular coordinate is `\theta`, then, after setting `t=\tau=0` at `\theta=\pi/2`,

\[
\boxed{
 t=T_\rho(\tau)
 =\operatorname{arsinh}\!\left(\frac{\sinh\tau}{\cosh\rho}\right),
 }
\]

and therefore

\[
\boxed{
 T_\rho'(\tau)
 =\frac1{\sqrt{1+w^2\operatorname{sech}^2\tau}}.
 }
\]

Thus the exact boundary identification factors as

\[
\theta\longmapsto \tau=\log\tan(\theta/2)
\longmapsto t=T_\rho(\tau),
\]

where the first map carries the entire cusp-end singularity and is independent of the seam width, while the second map is globally bi-Lipschitz with a **quadratic** defect:

\[
\boxed{
\operatorname{sech}\rho\le T_\rho'\le1,
\qquad
\|T_\rho-\mathrm{id}\|_{L^\infty(\mathbb R)}=\log\cosh\rho
=\frac12\log(1+w^2).
}
\]

More sharply, its full Jacobian deficit is exactly

\[
\boxed{
\int_{\mathbb R}(1-T_\rho'(\tau))\,d\tau
=2\log\cosh\rho
=\log(1+w^2).
}
\]

The physical hypercycle arclength also factorizes cleanly:

\[
\boxed{
 d\sigma=\cosh\rho\,dt,
\qquad
\frac{d\sigma}{d\tau}
=\frac{\cosh\rho}{\sqrt{1+w^2\operatorname{sech}^2\tau}},
}
\]

so `1<=d\sigma/d\tau<=\cosh\rho=\sqrt{1+w^2}`. Equivalently,

\[
\frac{d\sigma}{d\theta}
=\frac{\cosh\rho}
{\sin\theta\sqrt{1+w^2\sin^2\theta}},
\]

and the singular `\csc\theta` factor is exactly the untrimmed-axis compactification; all `w`-dependent density distortion is uniformly `1+O(w^2)`.

For the canonical PF-205 widths `w_n=\kappa d_n=O(P_n^{-1})`, every seam-dependent part of this boundary reparameterization is therefore `1+O(P_n^{-2})`, and

\[
\sum_n \log(1+w_n^2)<\infty.
\]

In particular, the **prime-dependent boundary-coordinate defect is already strongly summable** before any weak-trace counting. This does not prove the desired dressed `\sqrt{w_nw_{n+1}}/s_n` transfer. The fixed axis compactification `\tau\leftrightarrow\theta`, its singular trace density, the noncommutation with PF-233's `T_a`, the inverse-level two-boundary cancellation, PF-232's off-diagonal shear response, physical `P/H` projections, and finite pant completion all remain genuine gates. What is removed is the possibility that the inward hypercycle identification itself introduces a first-order `O(w_n)` or nonsummable prime-dependent loss.

## Claim

Work in the PF-231 logarithmic corridor model around the unit semicircle axis

\[
\gamma_0=\{|z|=1,\ \Im z>0\},
\qquad z=e^{x+i\theta},
\quad 0<\theta<\pi.
\tag{1}
\]

Let `\rho>=0`, put `w=\sinh\rho`, and let the inward equidistant curve be

\[
x=f_\rho(\theta)
=\operatorname{arsinh}(w\sin\theta).
\tag{2}
\]

Define the axis logarithmic arclength coordinate

\[
\tau(\theta)=\log\tan\frac\theta2,
\qquad d\tau=\frac{d\theta}{\sin\theta}.
\tag{3}
\]

Let `t` denote the signed Fermi footpoint coordinate on `\gamma_0`, normalized so that the common-perpendicular point has `t=0`. Then:

1. the exact hypercycle-to-axis boundary map is
   \[
   \boxed{
   t=T_\rho(\tau)
   =\operatorname{arsinh}\left(\frac{\sinh\tau}{\cosh\rho}\right);
   }
   \tag{4}
   \]
2. its derivative is
   \[
   \boxed{
   J_\rho(\tau):=T_\rho'(\tau)
   =\frac1{\sqrt{1+w^2\operatorname{sech}^2\tau}};
   }
   \tag{5}
   \]
3. globally,
   \[
   \boxed{
   \operatorname{sech}\rho\le J_\rho\le1,
   \qquad
   \sup_\tau|T_\rho(\tau)-\tau|=\log\cosh\rho;
   }
   \tag{6}
   \]
4. the Jacobian defect is integrable with exact mass
   \[
   \boxed{
   \int_{\mathbb R}(1-J_\rho)\,d\tau
   =2\log\cosh\rho
   =\log(1+w^2);
   }
   \tag{7}
   \]
5. physical arclength satisfies
   \[
   \boxed{
   d\sigma=\cosh\rho\,dt,
   \qquad
   1\le\frac{d\sigma}{d\tau}\le\cosh\rho,
   }
   \tag{8}
   \]
   and, in the PF-233 `\theta` parameter,
   \[
   \boxed{
   \frac{dt}{d\theta}
   =\frac1{\sin\theta\sqrt{1+w^2\sin^2\theta}},
   \qquad
   \frac{d\sigma}{d\theta}
   =\frac{\cosh\rho}
   {\sin\theta\sqrt{1+w^2\sin^2\theta}};
   }
   \tag{9}
   \]
6. for any scalar `G(\tau)=F(T_\rho(\tau))`, the longitudinal shifted `H^1` energy obeys
   \[
   \int_{\mathbb R}(|F_t|^2+|F|^2)\,dt
   =\int_{\mathbb R}
   \left(J_\rho^{-1}|G_\tau|^2+J_\rho|G|^2\right)d\tau,
   \tag{10}
   \]
   and therefore
   \[
   \boxed{
   \operatorname{sech}\rho\,\|G\|_{H^1_\tau}^2
   \le
   \|F\|_{H^1_t}^2
   \le
   \cosh\rho\,\|G\|_{H^1_\tau}^2.
   }
   \tag{11}
   \]

The same coefficient comparison applies after adding a transverse strip variable and then taking the infimum over extensions with fixed traces. Consequently, on the **complete lifted seam control** used to compare with the complete-axis PF-233 stage, the flat symmetric seam form pulled from Fermi `t` into axis `\tau` differs from the corresponding flat `\tau`-strip form by at most `\cosh^{\pm1}\rho`. Combining this with PF-234's intrinsic actual-versus-flat seam comparison gives the lifted scalar-trace form bound

\[
\boxed{
\cosh^{-3}\rho\,Q^{\rm axis,+}_w
\le_{\rm form}
\widetilde Q^{\rm hyp,+}_{\rho,w}
\le_{\rm form}
\cosh^3\rho\,Q^{\rm axis,+}_w,
}
\tag{12}
\]

where on the complete axis

\[
Q^{\rm axis,+}_w=M_\tau\tanh(wM_\tau),
\qquad
M_\tau=(1-\partial_\tau^2)^{1/2}.
\tag{13}
\]

Equation (12) is a lifted/control-stage statement. It does **not** identify the nonlocal closed-cuff seam operator with the finite one-cusp-pant boundary arc, and it does not remove the fixed `\tau\leftrightarrow\theta` trace-space conversion.

For canonical widths `w_n=O(P_n^{-1})`,

\[
\cosh^3\rho_n=(1+w_n^2)^{3/2}=1+O(P_n^{-2}),
\tag{14}
\]

and both the logarithmic distortion `\log\cosh\rho_n` and the exact Jacobian-defect mass in (7) are `O(P_n^{-2})`. Since the primes form a subset of the integers,

\[
\boxed{
\sum_n\log(1+w_n^2)<\infty.
}
\tag{15}
\]

No average prime-gap input is used.

## 1. Exact footpoint map from the hypercycle arclength density

PF-231 gives the graph (2). Differentiating,

\[
f_\rho'(\theta)
=\frac{w\cos\theta}{\sqrt{1+w^2\sin^2\theta}}.
\tag{16}
\]

Because the logarithmic metric is `\csc^2\theta(dx^2+d\theta^2)`, the physical arclength of the graph is

\[
\begin{aligned}
\frac{d\sigma}{d\theta}
&=\frac{\sqrt{1+|f_\rho'|^2}}{\sin\theta}\\
&=\frac{\sqrt{1+w^2}}
{\sin\theta\sqrt{1+w^2\sin^2\theta}}\\
&=\frac{\cosh\rho}
{\sin\theta\sqrt{1+w^2\sin^2\theta}}.
\end{aligned}
\tag{17}
\]

PF-234's intrinsic Fermi metric gives `d\sigma=\cosh\rho\,dt` along `r=\rho`. Dividing (17) by `\cosh\rho` and using (3) yields

\[
\frac{dt}{d\tau}
=\frac1{\sqrt{1+w^2\sin^2\theta}}.
\tag{18}
\]

The elementary identity `\sin\theta=\operatorname{sech}\tau` turns (18) into (5). Integrating from `\tau=0` gives (4), because

\[
\frac d{d\tau}
\operatorname{arsinh}\left(\frac{\sinh\tau}{\cosh\rho}\right)
=\frac1{\sqrt{1+w^2\operatorname{sech}^2\tau}}.
\tag{19}
\]

This also verifies (9) directly.

## 2. The seam-dependent map is quadratically close on the whole axis

Equation (5) immediately gives

\[
\operatorname{sech}\rho\le J_\rho\le1.
\tag{20}
\]

The asymptotics of (4) at the two ideal ends are

\[
T_\rho(\tau)
=\tau-\log\cosh\rho+o(1),
\qquad \tau\to+\infty,
\tag{21}
\]

and

\[
T_\rho(\tau)
=\tau+\log\cosh\rho+o(1),
\qquad \tau\to-\infty.
\tag{22}
\]

Since `1-J_\rho>=0`, the function `\tau-T_\rho(\tau)` is monotone increasing from `-\log\cosh\rho` to `+\log\cosh\rho`. This proves the sup norm statement in (6) and, by the fundamental theorem of calculus, the exact integral (7).

For small `w`,

\[
\log\cosh\rho=\frac12\log(1+w^2)=O(w^2),
\qquad
1-\operatorname{sech}\rho=O(w^2).
\tag{23}
\]

There is therefore no hidden `O(w)` boundary-coordinate effect near `\theta=0,\pi`; the apparent singularity there belongs to the fixed map `d\tau=\csc\theta\,d\theta`.

## 3. Energy pullback preserves the seam scale up to `1+O(w^2)`

For `G(\tau)=F(T_\rho(\tau))`, one has

\[
F_t=\frac{G_\tau}{J_\rho},
\qquad
dt=J_\rho\,d\tau.
\tag{24}
\]

Substitution gives (10), and (20) gives (11). The same change in a flat seam strip `(-w,w)_x\times\mathbb R_t` gives

\[
\int
\left(
J_\rho|v_x|^2
+J_\rho^{-1}|v_\tau|^2
+J_\rho|v|^2
\right)d\tau\,dx.
\tag{25}
\]

Every coefficient lies between `\operatorname{sech}\rho` and `\cosh\rho` times its unwarped counterpart. Taking the infimum over extensions with equal traces on the two `x`-boundaries preserves the same form comparison.

PF-234 independently proves that the actual intrinsic hyperbolic seam energy is between `\cosh^{-2}\rho` and `\cosh^2\rho` times the flat strip energy because `1+w^2=\cosh^2\rho`. Multiplying the two independent comparisons gives (12).

The important point is what (12) does and does not say. It eliminates a seam-width-dependent loss in transporting the local normalizer to the **axis compactification**. It does not diagonalize that normalizer with PF-233's Pöschl--Teller operator, because the fixed conversion from `\tau` to `\theta` is singular in `d\theta` representation and the corridor operator is built from `A=-\partial_\theta^2+\csc^2\theta` and its variable-width conjugate `T_a`.

## 4. Canonical prime widths make the coordinate defect strongly summable

PF-205 fixes

\[
w_n=\kappa d_n,
\qquad d_n=P_n^{-1}(1+o(1)).
\tag{26}
\]

Hence `w_n^2=O(P_n^{-2})`. Equations (7), (14), and the elementary bound `\log(1+x)<=x` give

\[
\sum_n\int_{\mathbb R}(1-J_{\rho_n})\,d\tau
=\sum_n\log(1+w_n^2)
\le\sum_n w_n^2<\infty.
\tag{27}
\]

This is stronger than the weak-trace endpoint bookkeeping that motivates PF-222/PF-228, but only for the **geometric reparameterization defect**. It is not an operator-ideal theorem for the full seam/corridor inverse. In particular the baseline compactification and the number of tangential channels remain infinite and must still be controlled at the inverse level.

## 5. Prior-art and novelty audit

Fermi coordinates around a hyperbolic geodesic, the cylinder metric `dr^2+\cosh^2(r)dt^2`, equidistant curves, and logarithmic conformal coordinates in `\mathbb H^2` are classical. Guillarmou and Guillopé, *The determinant of the Dirichlet-to-Neumann map for surfaces with boundary*, IMRN 2007, rnm099, DOI `10.1093/imrn/rnm099`, explicitly use the hyperbolic cylinder in Fermi form and the logarithmic conformal model of the cylinder. Buser's *Geometry and Spectra of Compact Riemann Surfaces* is standard background for collar/Fermi geometry.

No novelty is claimed for those coordinate systems or for the elementary change-of-variables inequalities. A structure-directed search did not identify a source whose theorem is the PF-specific use made here: factoring the PF-205 inward-hypercycle trace map through the PF-231 logarithmic compactification, identifying its exact `L^1` Jacobian defect as `\log(1+w_n^2)`, and observing that the canonical prime-width family makes this **prime-dependent** boundary-identification defect summable. The proof is self-contained from PF-231/PF-234 and elementary calculus; the literature is novelty context, not a theorem dependency.

## 6. Falsification and boundary checks

1. The sign/orientation on the opposite corridor face may reverse the longitudinal parameter. Equations (5)--(9) concern the absolute Jacobian and are unchanged by that orientation choice.
2. The complete-axis map `T_\rho` is a statement on a lift. It does not by itself descend to a common periodic coordinate for the entire closed cuff while simultaneously representing the finite pant arc; that nonlocal completion remains open.
3. Equation (12) is a **form comparison after scalar trace pullback**, not an operator equality in `L^2(d\theta)`. It does not permit commuting square roots with `A`, `T_a`, or multiplication by the variable width.
4. The physical density relative to `d\tau` tends to the constant `\cosh\rho` at the two ideal ends, so its difference from one is not `L^1(\mathbb R)`. The integrable quantity in (7) is the **nonconstant footpoint-Jacobian defect** `1-J_\rho`. The constant physical stretch is nevertheless uniformly `1+O(w^2)` and harmless at the coefficient-comparison level.
5. PF-228's `w/s` factor occurs in the off-diagonal of the **inverse** `D=(I+K)^{-1}`, not in the raw normalized corridor cross block itself. Nothing in this finding upgrades form comparability to that inverse-level cancellation.
6. PF-232's full DtN Loewner comparison still does not imply an off-diagonal perturbation estimate. `P/H` projections and one-cusp-pant end completion remain outside this result.
7. The summability in (27) uses only `w_n=O(P_n^{-1})`; it does not encode prime-gap order and is not itself an arithmetic spectral signature or RH mechanism.

## Consequences for the research line

The boundary-representation obstruction is now more sharply localized. PF-234 eliminates loss of intrinsic seam coercivity; PF-235 shows that moving from the inward hypercycle to the **untrimmed axis compactification** adds only a quadratic, strongly summable prime-dependent distortion. Therefore an `O(w_n)` or nonsummable failure of the PF-228 dressing cannot be blamed on the hypercycle footpoint map or its physical arclength density.

The remaining local gate is the fixed but singular axis compactification `\tau=\log\tan(\theta/2)` together with genuine operator noncommutation. The next estimate must keep the complete two-boundary precision matrix, transport the axis-reference seam forms into the PF-233 `d\theta` trace realization, and estimate the off-diagonal block of the **inverse** `D=(I+K)^{-1}`. Only after that can PF-232 shear, physical `P/H` projections, and finite-pant completion be charged separately. The raw normalized cross block `Q_2^{-1/2}C Q_1^{-1/2}` is not itself expected to have PF-228's `w/s` scale; that scale is created by the full inverse-level diagonal/cross cancellation.