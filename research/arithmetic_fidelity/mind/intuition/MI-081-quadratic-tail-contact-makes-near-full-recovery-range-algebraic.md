# MI-081 — Growing calibration degree costs a quadratic increase in recovery range

**Evidence level:** supported synthesis of [AF-582](../../findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic.md), [AF-583](../../findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order.md), [AF-584](../../findings/AF-584-growing-calibration-degree-has-sharp-quadratic-range-cost.md), and [AF-585](../../findings/AF-585-cubic-calibration-has-sharp-range-constant-from-endpoint-curvature.md). Classical alternation, Markov bounds and explicit Chebyshev witnesses give a degree-uniform range law and sharp quadratic/cubic constants for a non-arithmetic profile. The prime-edit transfer has a quantitative sufficient approximation-error gate; no general novelty is claimed.

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
Higher fixed degrees cannot change this algebraic order. Write
\[
\Delta_r(B)=1-2E_r(B),\qquad A_r=\frac{2r^2(r^2-1)}3.
\]
For a best approximant \(p\), the admissible constant \(1/2\) gives \(E_r\le1/2\), hence \(\|p-1/2\|_\infty\le1\). The second-derivative Markov bound on \([0,B]\) gives \(\|p''\|_\infty\le2A_r/B^2\). For any \(1<t\le B\), interpolation at the source peak yields
\[
1-E_r\le p(1)
\le(1-1/t)p(0)+p(t)/t+A_r(t-1)/B^2
\le E_r+e^{1-t}+A_r(t-1)/B^2.
\]
Polynomial-space inclusion supplies the other direction:
\[
\Delta_2(B)\le\Delta_r(B)
\le e^{1-t}+A_r(t-1)/B^2,\qquad r\ge2.
\]
Taking \(t=2\log B\) for \(B\ge e\) and using the quadratic certificate proves, for every **fixed** \(r\ge2\),
\[
\Delta_r(B)=\Theta_r(\log B/B^2),\qquad
1\le\liminf_{\delta\downarrow0}\frac{R_r(\delta)}{\sqrt{\log(1/\delta)/\delta}}
\le\limsup_{\delta\downarrow0}\frac{R_r(\delta)}{\sqrt{\log(1/\delta)/\delta}}
\le\sqrt{A_r}.
\]
Thus bounded curvature, the peak and one decaying-tail value control the fixed-degree hierarchy without solving each alternation system. The Markov constant is only a bound; the cubic sharp constant instead uses the saturated endpoint forced by the source peak.

For \(r=3\), every coefficientwise limit of a rescaled best approximant
\(P_B(y)=p_B(By)\) satisfies
\[
|P|\le\tfrac12\quad(0\le y\le1),\qquad P(0)=\tfrac12,
\qquad P'(0)=0.
\]
Indeed \(f(By)\to0\) for fixed \(y>0\), while
\(p_B(1)\ge1-E_3(B)\) forces endpoint saturation; comparison with
\(p_B(0)\le E_3(B)\) forces the zero slope in the limit, not at finite
\(B\). Write \(P=1/2+dy+ay^2+by^3\). Even without assuming zero
slope, endpoint maximality gives \(d\le0\); the values at \(1\) and
\(2/3\) imply
\[
d+a+b\le0,\qquad
-1\le\tfrac23d+\tfrac49a+\tfrac8{27}b
\le\tfrac{10}{27}d+\tfrac4{27}a.
\]
Hence \(P''(0)=2a\ge-27/2\), with equality only at
\[
P_*(y)=\tfrac12-\tfrac{27}{4}y^2(1-y)
=-\tfrac12T_3((1-3y)/2).
\]
Its minimum is \(-1/2\) at \(y=2/3\). Interpolating the finite
approximant at \(0,1,s_B\), \(s_B=2\log B+\log\log B\), gives
\(\limsup B^2\Delta_3(B)/\log B\le-2a\le27/2\) along each
convergent subsequence. Compactness yields the global upper bound.
For sufficiently large \(B\), the matching whole-window witness is
\[
c_B=\frac{27}{4B^2}(1-B^{-1/2}),\quad
t_B=2+\log(1/c_B),\quad Q_B(x)=c_Bx(t_B-x)(1-x/B).
\]
Its residual \(f-Q_B\) is nonnegative on \([0,B]\), has minimum
zero, and maximum \(1-(1+o(1))c_Bt_B\); centering this range proves
the reverse bound. Consequently
\[
\Delta_3(B)\sim\frac{27}{2}\frac{\log B}{B^2},\qquad
R_3(\delta)\sim\frac{3\sqrt3}{2}
\sqrt{\frac{\log(1/\delta)}{\delta}},\qquad P_B\to P_*.
\]
The cubic pays \(3\sqrt3/2\) times the quadratic range. The endpoint
value is essential: a cubic with the same norm but value \(-1/2\)
at zero can have second derivative \(-48\), so a norm-only extremum
would give the wrong coefficient. Exact finite-\(B\) contact locations
and sharp coefficients for \(r\ge4\) are not supplied.

For growing known degree, AF-584 optimizes the tail point at
\(t=1+\log(B^2/A_r)\) and supplies the missing converse. Put
\(\nu=r^2/B\). Uniformly for \(r\ge2\), \(B\ge16r^2\),
\[
\frac{\nu^2\log(1/\nu)}{20736}
\le\Delta_r(B)\le2\nu^2\log(1/\nu).
\]
The lower bound uses \(n=\lfloor r/2\rfloor\), \(k=n^2/B\),
\(t=\log(1/k)\), and
\[
D(x)=1-T_n(1-2x/B),\quad
Q(x)=(t/x-1)D(x)^2,\quad d=k^2\log(1/k)/256.
\]
Here \(T_n\) is the Chebyshev polynomial. Since \(D(0)=0\),
\(Q\) is a polynomial of degree at most \(2n\), including at zero.
For \(k\le1/64\), the global certificate
\(0\le f-Q/64\le1-d\) makes \((1-d)/2+Q/64\) an admissible
approximant. Near the peak, \(kx\le D(x)\le2kx\); beyond \(t\),
\(-4\le Q\le0\). Thus the witness retains the gain while controlling
every remote Chebyshev oscillation, not merely selected contacts.

If \(B\ge64\) and \(r^2/B\ge1/16\), choosing instead
\(n=\lfloor\sqrt B/8\rfloor\) gives
\(\Delta_r(B)\ge\log(256)/2^{24}\). Consequently, as \(B\to\infty\),
\[
\Delta_{r(B)}(B)\to0\ \Longleftrightarrow\ r(B)^2/B\to0,
\qquad
R_r(\delta)=\Theta\!\left(r^2\sqrt{\log(1/\delta)/\delta}\right),
\quad r\ge2.
\]
The range constants and the small-\(\delta\) threshold are independent
of \(r\); the degree may grow arbitrarily along this limit. This removes
the extra \(\log B\) in the earlier sufficient condition. It does not
determine the limiting deficit when \(r^2/B\) approaches a positive
constant. At a fixed compact window, unbounded degree still makes
\(E_r(B)\to0\).

Extra readings or adaptivity inside the window cannot beat its whole-curve quotient distance. Conversely the \(r+2\) alternation nodes, with polynomial-annihilating divided-difference weights normalized by \(\sum|\lambda_j|=1\), have \(|\sum\lambda_j f(x_j)|=E_r(B)\) and observation error at most \(\varepsilon\). Hence \(r+2\) fixed readings approach the corresponding radius at every known fixed degree; if zero is a node, replace it by a positive node tending to zero. At most \(r+1\) distinct readings admit a noiseless interpolation alias. These are binary supremal radii, with no recovery at a midpoint tie or common optimal multiway bank asserted. [MI-080](MI-080-escaping-anchors-cancel-known-degree-at-constant-noise-cost.md)'s multiway adaptive budget and its unrestricted anchors address a different resource.

For [AF-559](../../findings/AF-559-all-pair-prime-edit-separation-has-uniform-sharp-critical-window.md)'s ordered prime-edit curves, let \(D_{p,q}=\sup_a(\Phi_q-\Phi_p)(a)\), \(c=e^{B_1}\), with \(B_1\) the prime-reciprocal Meissel--Mertens constant, and
\[
g_{p,q}(x)=\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}},\qquad
\alpha_p=\sup_{q>p}\|g_{p,q}-f\|_{\infty,(0,\infty)}=O(1/\log p).
\]
The primes \(p<q\) are odd. AF-583 obtains this uniform rate from the exact positive gap integral, including neighboring edit locations; it also gives
\[
D_{p,q}=\frac{p^{-2}-q^{-2}}{e\log p}\{1+O(1/\log p)\}.
\]
Subtracting separate source asymptotics would not establish a gap-relative estimate uniform in \(q>p\). Coordinate rescaling preserves \(\Pi_r\); distance to this subspace is 1-Lipschitz. On the physical window \(0<a\le B/(c\log p)\), the binary radius therefore obeys
\[
\left|\frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}-2E_r(B)\right|\le2\alpha_p.
\]
The same TV-one contrast transfers the finite-bank lower bound \(D_{p,q}(E_r(B)-\alpha_p)/2\). This quotient comparison is uniform in the degree: no factor of \(r\) amplifies \(\alpha_p\). In particular, as \(p,B\to\infty\), for any supplied finite degrees \(r=r(p)\) and labels \(q(p)>p\),
\[
1-\frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}\to0
\quad\Longleftrightarrow\quad r^2/B\to0.
\]
For fixed \(r\ge2\), the explicit rate suffices to transport the loss order along \(B\to\infty\) whenever
\[
B^2=o((\log p)\log B).
\]
Equivalently at a desired loss \(\delta=\delta(p)\downarrow0\), \(\delta\log p\to\infty\) suffices for the actual minimum normalized range to satisfy
\[
R_{r;p,q}(\delta)=\Theta\!\left(r^2\sqrt{\log(1/\delta)/\delta}\right),\qquad r\ge2,
\]
uniformly over the growing known degree and larger prime labels \(q\). For \(r=2,3\), the sharper ratio \(R_{r;p,q}(\delta)/\sqrt{\log(1/\delta)/\delta}\) tends respectively to \(1\) and \(3\sqrt3/2\). Indeed the quotient comparison sandwiches the range between \(R_r(\delta+C/\log p)\) and \(R_r(\delta-C/\log p)\). The condition \(\delta\log p\to\infty\) is sufficient for this relative-loss law; the qualitative threshold above needs only \(\alpha_p\to0\). The affine leading loss still needs its separate comparison \(\alpha_p=o(e^{1-B})\). These conditions are sufficient, not necessary, and the profile error rate is not known sharp. The range law is in \(x\), so its physical coordinate cost includes \(1/(c\log p)\). These are the exact limiting prime-edit curves; no simultaneous finite-critical-index error is supplied.

No sharp leading constant for degree four and above, relative-observation-error guarantee or finite-precision cost follows. The matched generalized-prime sources do not certify ordinary-prime provenance or imply RH. The retained distinction is exact: a known degree can make the query count finite while its square prices the coordinate range needed for a near-full noise margin.
