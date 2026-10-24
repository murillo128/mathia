# MI-081 — Quadratic tail contact makes near-full recovery range algebraic

**Evidence level:** supported synthesis of [AF-582](../../findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic.md). The mechanism is a classical best-uniform-approximation certificate applied to an explicit non-arithmetic profile; its prime-edit transfer has a separate approximation-error gate.

For binary sources \(F_0=0\), \(F_1=f\), \(f(x)=xe^{1-x}\), observe
\[
y(x)=F_i(x)+b(x)+\eta(x),\qquad
b\in\Pi_r,\quad |\eta(x)|\le\varepsilon,\quad 0<x\le B.
\]
Here \(\Pi_r\) is the space of real polynomials of degree at most the known integer \(r\ge0\). Coefficients are unrestricted, and one polynomial is shared by all readings of each input. Competing labels may use different polynomials. The whole-window quotient and supremal identification radius are
\[
E_r(B)=\inf_{p\in\Pi_r}\|f-p\|_{C[0,B]},\qquad
\varepsilon_r(B)=E_r(B)/2.
\]
Continuity permits the closed norm even though zero is not queryable. On the full ray only constant approximants have finite error, so \(E_r(\infty)=1/2\) and \(\varepsilon_r(\infty)=1/4\) for every fixed degree. This degree independence does **not** survive a coordinate cap.

For affine calibration and \(B>1\), subtract the endpoint chord \(s x\), \(s=e^{1-B}\). Its residual profile vanishes at \(0,B\) and peaks at \(x_1=1-w\), where \(we^w=s\). Three alternating contacts give, with the asymptotic as \(B\to\infty\),
\[
2E_1(B)=e^w(1-w)^2,
\qquad 1-4\varepsilon_1(B)=e^{1-B}+O(e^{2-2B}).
\]
The quadratic approximant instead creates an additional tail contact. Put
\[
v=e^{1-t},\quad H_t(x)=f(x)-v\{(t+1)x-x^2\},\quad t>2.
\]
It has a local maximum at \(x(t)\in(0,1)\), a zero local minimum at \(t\), and \(H_t(0)=0\). The critical equation and curvature are
\[
(1-x(t))e^{1-x(t)}=v(t+1-2x(t)),\qquad
H_t''(x)=e^{1-x}(x-2)+2v.
\]
The curvature crosses zero once before two and stays positive thereafter, giving exactly those two stationary points and controlling the residual between contacts. For sufficiently large \(B\), choose \(t=t_B\) so
\[
h(t):=H_t(x(t))=H_t(B),\qquad
E_2(B)=h(t_B)/2.
\]
The polynomial \(h(t_B)/2+v\{(t_B+1)x-x^2\}\) then has residual \(-E_2,+E_2,-E_2,+E_2\) at \(0,x(t_B),t_B,B\). These four contacts certify the optimum over **all** quadratics. Their balance forces
\[
vB^2\to1,\quad t_B=1+2\log B+O(\log B/B),\quad
h(t_B)=1-vt_B+O(v^2t_B^2).
\]
Thus a logarithmically moving contact in the exponential tail produces an algebraic loss:
\[
1-4\varepsilon_2(B)=\frac{1+2\log B}{B^2}
+O\!\left(\frac{(\log B)^2}{B^3}\right).
\]
To retain fraction \(1-\delta\) of the full-ray radius, define \(R_r(\delta)=\inf\{B>1:4\varepsilon_r(B)\ge1-\delta\}\). As \(\delta\downarrow0\),
\[
R_1(\delta)=1+\log(1/\delta)+o(1),\qquad
R_2(\delta)\sim\sqrt{\log(1/\delta)/\delta}.
\]
Extra readings or adaptivity inside the window cannot beat its whole-curve quotient distance. Conversely the \(r+2\) alternation nodes, with polynomial-annihilating divided-difference weights normalized by \(\sum|\lambda_j|=1\), have \(|\sum\lambda_j f(x_j)|=E_r(B)\) and observation error at most \(\varepsilon\). Hence three affine or four quadratic fixed readings approach the corresponding radius; replace the zero node by a positive node tending to zero. At most \(r+1\) distinct readings admit a noiseless interpolation alias. These are binary supremal radii, with no recovery at a midpoint tie or common optimal multiway bank asserted. [MI-080](MI-080-escaping-anchors-cancel-known-degree-at-constant-noise-cost.md)'s multiway adaptive budget and its unrestricted anchors address a different resource.

For [AF-559](../../findings/AF-559-all-pair-prime-edit-separation-has-uniform-sharp-critical-window.md)'s ordered prime-edit curves, let \(D_{p,q}=\sup_a(\Phi_q-\Phi_p)(a)\), \(c=e^{B_1}\), with \(B_1\) the prime-reciprocal Meissel--Mertens constant, and
\[
g_{p,q}(x)=\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}},\qquad
\alpha_p=\sup_{q>p}\|g_{p,q}-f\|_{\infty,(0,\infty)}\to0.
\]
The primes \(p<q\) are odd. Coordinate rescaling preserves \(\Pi_r\); distance to this subspace is 1-Lipschitz. On the physical window \(0<a\le B/(c\log p)\), the binary radius therefore obeys
\[
\left|\frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}-2E_r(B)\right|\le2\alpha_p.
\]
The same TV-one contrast transfers the finite-bank lower bound \(D_{p,q}(E_r(B)-\alpha_p)/2\). A leading quadratic loss along growing windows requires an error comparison: \(\alpha_p=o(\log B/B^2)\) suffices; the affine counterpart is \(\alpha_p=o(e^{1-B})\). These sufficient conditions are not claimed necessary. The persisted uniform convergence supports fixed-window limits, iterated limits and suitably chosen diagonals, but gives no explicit joint prime/range/precision rate. The range law is in \(x\), so its physical coordinate cost includes \(1/(c\log p)\).

No higher-degree range asymptotic, relative-error guarantee or finite-precision cost follows. The matched generalized-prime sources do not certify ordinary-prime provenance or imply RH. The retained distinction is exact: a known degree can make the query count finite while the desired noise fraction still forces a large accessible coordinate range.
