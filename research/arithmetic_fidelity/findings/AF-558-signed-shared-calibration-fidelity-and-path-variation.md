# AF-558 — Signed shared-calibration fidelity and path variation

## Status

EXACT-DERIVED · CLASSICAL-INGREDIENTS · CORRECTED-CLAIM · NONLINEAR-RECOVERY · SHARED-NUISANCE · CONDITIONING · NO-NOVELTY-CLAIM

## Claim

A common nuisance calibration affects a decoded *contrast* through the signed difference of the inverse sensitivities of its two branches. The exact **endpoint** accuracy criterion is a signed integral; the integral of its absolute value is a **sufficient variation bound**, not in general a necessary accuracy condition. Equality, and hence necessity of the variation test, holds along a decoder path on which that sensitivity difference keeps one sign. This distinction matters even for globally invertible smooth observation maps.

Let \(G(z,u)\) be \(C^2\), with \(G_z\ne0\), on a region admitting one common local inverse branch in \(z\) for all calibration values considered. Let \(u_0\) be the true calibration, and let \(q\in C^1\) be a real readout. Write
\[
G(\Phi_v(z),v)=G(z,u_0),\qquad \Phi_{u_0}(z)=z,
\]
and define
\[
K_q(w,v)=-q'(w)\frac{G_u(w,v)}{G_z(w,v)},\qquad
\Delta K(v)=K_q(\Phi_v(z_2),v)-K_q(\Phi_v(z_1),v).
\]
For \(u_1=u_0+\varepsilon\), with the full path inside that inverse region, set
\[
C_v=q(\Phi_v(z_2))-q(\Phi_v(z_1)),\qquad
E=C_{u_1}-C_{u_0}.
\]
Then
\[
\boxed{E=\int_{u_0}^{u_1}\Delta K(v)\,dv.}\tag{1}
\]
The integral is **oriented**; its sign changes when its endpoints are exchanged. If
\(I=[\min(u_0,u_1),\max(u_0,u_1)]\), the nonnegative path variation is
\[
\boxed{V=\int_I|\Delta K(v)|\,dv,\qquad |E|\le V.}\tag{2}
\]
For any sequence of instances \(A\) and positive target scales \(\sigma_A\), the exact condition for endpoint recovery is
\[
\boxed{\left|\int_{u_{0,A}}^{u_{1,A}}\Delta K_A(v)\,dv\right|
=o(\sigma_A).}\tag{3}
\]
The stronger requirement \(V_A=o(\sigma_A)\) suffices, but cannot be inferred from (3) without a noncancellation hypothesis. If \(\Delta K_A\) has constant sign on \(I_A\), then \(|E_A|=V_A\) and the two conditions are equivalent. More generally, a uniform lower bound \(|E_A|\ge cV_A\) with \(c>0\) makes them equivalent; this explicitly encodes the necessary absence of large path cancellation.

This preserves the exact local-inverse sensitivity law and the translation-quotient characterization, while correcting the fidelity inference. The result is about calibration geometry, not a prime-specific theorem or an implication toward RH.

## Derivation and exact invariance

Implicit differentiation of \(G(\Phi_v(z),v)=G(z,u_0)\) yields
\[
\partial_v\Phi_v(z)=-\frac{G_u}{G_z}(\Phi_v(z),v),\qquad
\partial_v q(\Phi_v(z))=K_q(\Phi_v(z),v).
\]
Subtracting two branches and using the fundamental theorem of calculus proves (1). Applying the triangle inequality proves (2). Continuity of \(\Delta K\) ensures that equality in (2), for a nontrivial interval, holds precisely when \(\Delta K\) does not change sign (apart from zeros); this is the equality criterion for the integral triangle inequality.

On a connected inverse tube, all pairwise contrasts \(C_v\) are independent of \(v\) for every ordered source pair if and only if \(K_q(\cdot,v)\) is source-independent on the attained decoder image for each \(v\). Indeed the forward direction follows by subtraction. Conversely, vanishing contrast derivatives imply that \(K_q(\Phi_v(z),v)\) has the same value for every source \(z\); each \(\Phi_v\) is a local diffeomorphism, so \(K_q(w,v)=k(v)\) on its connected image. Equivalently,
\[
q(\Phi_v(z))=q(z)+a(v),\qquad
a(v)=\int_{u_0}^{v} k(s)\,ds.
\tag{4}
\]
Thus exact *all-calibration* invariance is much stronger than accidental endpoint cancellation along one finite excursion.

When \(|\partial_wK_q|\le M\) and \(|\partial_z\Phi_v|\le L\) uniformly on the decoder tube, the mean-value estimate applied inside (2) gives the **sufficient** stable bound
\[
V\le |\varepsilon|ML|z_2-z_1|.
\tag{5}
\]
The signed integral in (1), rather than this upper bound, remains the exact endpoint error.

Under a smooth reparameterization \(w=\varphi(z)\) with the readout transported as \(\widetilde q=q\circ\varphi^{-1}\) and observation \(\widetilde G=G\circ(\varphi^{-1},\mathrm{id})\), the scalar \(-q'G_u/G_z\) is unchanged. Equations (1)--(4) are therefore coordinate-invariant statements about the specified readout, although the auxiliary Lipschitz constants in (5) depend on coordinates.

## Two counterexamples fixing the accuracy and regularity boundaries

**Finite-path sign cancellation.** Take the smooth, globally invertible model
\[
G(z,u)=e^{u^2}z,\qquad q(z)=z,\qquad z_1=0,\quad z_2=1.
\]
For \(t>0\), choose true calibration \(u_0=-t\) and applied calibration \(u_1=t\). Direct inversion gives
\[
\Phi_v(z)=e^{t^2-v^2}z,\qquad
\Delta K(v)=-2ve^{t^2-v^2}.
\]
The endpoint calibration returns to its initial value, hence \(E=0\), while
\[
V=2(e^{t^2}-1)\sim2t^2.
\]
With \(\sigma_t=t^3\), equation (3) holds identically but \(V/\sigma_t\to\infty\). Therefore no exact necessary precision threshold follows from absolute variation for unrestricted calibration excursions. This counterexample has \(G_z=e^{u^2}>0\) everywhere, so singular inverses and branch switching play no role.

**The quadratic-remainder regularity gap.** The hypotheses \(G\in C^2,\ q\in C^1\) imply, for each fixed source pair,
\[
E=\varepsilon\,[K_q(z_2,u_0)-K_q(z_1,u_0)]+o(|\varepsilon|),
\tag{6}
\]
but they do not justify a universal \(O(\varepsilon^2)\) remainder. To see this while keeping \(q\) a valid monotone coordinate, take
\[
G(z,u)=z+u,\qquad q(z)=z+z\sqrt{|z|},\qquad
u_0=0,\quad z_1=0,\quad z_2=1.
\]
Here \(q\in C^1,\ q'(z)=1+\tfrac32\sqrt{|z|}>0\), and \(\Phi_\varepsilon(z)=z-\varepsilon\). For \(\varepsilon>0\),
\[
C_\varepsilon-C_0
=-\frac32\varepsilon+\varepsilon^{3/2}+O(\varepsilon^2).
\]
The displayed \(\varepsilon^{3/2}\) term is not \(O(\varepsilon^2)\). The same issue affects the branchwise differential-calibration expansion when only \(q\in C^1\) is assumed.

A valid quadratic remainder follows if \(v\mapsto\Delta K(v)\) is Lipschitz on \(I\), with constant \(B\):
\[
\left|E-\varepsilon\Delta K(u_0)\right|
\le \frac{B}{2}\varepsilon^2.
\tag{7}
\]
On a compact regular decoder tube, \(G\in C^2,\ q\in C^2,\ |G_z|\) bounded away from zero are sufficient for such a bound. In a varying family indexed by \(A\), \(B_A\) may grow: a first-order precision claim at scale \(\sigma_A\) additionally requires \(B_A\varepsilon_A^2=o(\sigma_A)\), not merely pointwise differentiability.

For independent errors \(\varepsilon_1,\varepsilon_2\), write \(K_i=K_q(z_i,u_0)\). Under the corresponding branchwise Lipschitz bounds,
\[
\widetilde C-C_{u_0}
= (K_2-K_1)\bar\varepsilon
+\tfrac12(K_2+K_1)(\varepsilon_2-\varepsilon_1)
+R,
\quad
|R|\le\tfrac12(B_1\varepsilon_1^2+B_2\varepsilon_2^2),
\tag{8}
\]
where \(\bar\varepsilon=(\varepsilon_1+\varepsilon_2)/2\). With merely \(C^1\) readout, replace the displayed quadratic bound by a pointwise little-\(o(|\varepsilon_1|+|\varepsilon_2|)\) statement. The common mode is weighted by a sensitivity **difference**, while differential mode is weighted by its **average**.

## Specialization: the AF-543/AF-544 curvature decoder is sign-regular

The curvature-normal-form observation and logarithmic readout from AF-543 are
\[
G(D,u)=\frac{D[(1-2u)+(1-u)D]}{(1-u)(1+D)^2},
\qquad q(D)=\log D.
\tag{9}
\]
Direct differentiation gives
\[
G_D=\frac{1+D-2u}{(1-u)(1+D)^3},\quad
K_q(D,u)=\frac{1+D}{(1-u)(1+D-2u)},\quad
\partial_DK_q=-\frac{2u}{(1-u)(1+D-2u)^2}.
\tag{10}
\]
In the physical decoder region \(D>0,\ 0<u<\tfrac12\), the inverse exists with \(G_D>0\) and \(\partial_DK_q<0\). Hence the common transport \(\Phi_v\) preserves the ordering of any two distinct source branches, and their \(\Delta K(v)\) has **fixed sign throughout every admissible calibration path contained in this positive-\(u\) region**. Consequently
\[
\boxed{|C_{u_1}-C_{u_0}|=V\quad
\text{for such paths}.}
\tag{11}
\]
The counterexample's endpoint cancellation is not available in this physical AF-544 regime. Thus an absolute-variation budget becomes both necessary and sufficient **for this specific fixed-sign decoder family**, not as a theorem for arbitrary shared calibration. For endpoint expansions used in AF-544, the derivative and path bounds must also be checked uniformly at its shrinking target scale.

This restores the precise local mechanism behind AF-544's extra common-mode suppression: each branch has order-one inverse sensitivity, while their sensitivity difference is small because \(\partial_DK_q\) includes a factor \(u\) and the decoded source branches are close. Independent calibration errors still lack that suppression.

## Prior art, scope, and decisive audits

Equations (1)--(8) are standard implicit differentiation, the fundamental theorem of calculus, total variation, and Taylor remainder estimates; no theorem-level novelty is claimed. Cornell's *Numerical Methods for Data Science*, section 5.3 (https://www.cs.cornell.edu/~bindel/nmds/00-Background/04-Calculus.html), is an accessible reference distinguishing endpoint increments from total variation for differentiable curves. The general local-inverse and transformation-invariance setting is the classical background already identified in AF-545's original formulation; AF-546 and AF-547 use the exact field and group invariance rather than the invalid necessary-variation inference.

The correction is materially important for Arithmetic Fidelity because a purported impossibility or necessary numerical-resolution threshold based on \(\int|\Delta K|\) may be false when calibration sensitivities oscillate or reverse sign. It does not invalidate the exact derivative identity, the all-calibration translation classification, the common-versus-differential first-order split with correct regularity, or AF-544's fixed-sign physical specialization.

The decisive independent checks are: (i) evaluate both integrals in the smooth \(e^{u^2}z\) counterexample; (ii) verify the \(C^1\), non-\(C^2\) readout's \(\varepsilon^{3/2}\) remainder; (iii) differentiate (9) to establish both signs in (10); (iv) test any later precision assertion against the *destination* scale using signed endpoint error, a justified noncancellation hypothesis, and a uniform remainder budget. Neither exact calibration-fidelity geometry nor these matched controls by themselves distinguish rational primes or prove RH.
