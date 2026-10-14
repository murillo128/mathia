# AF-570 — Shrinking windows turn affine prime-edit separation into a curvature signal

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-EDIT · BOUNDED-WINDOW · AFFINE-CALIBRATION · SHARP-LOCAL-MINIMAX · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: a bounded channel changes both margin and sensing budget

Use AF-559's commonly registered critical prime-edit curves, not distinct ordinary-prime systems:
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
Q_p(s)=P(s)-h_p(s),\qquad
h_p(s)=p^{-s}-(p+1)^{-s},\qquad
\Phi_p(a)=Q_p^{-1}(E_1(a)).
\tag{1}
\]
Here \(p\) is an odd rational-prime **edit location** and
\(E_1(a)=\int_a^\infty e^{-v}dv/v\). Restrict the observation coordinate to
\(0<a\le A\), with one arbitrary output calibration
\(b_0+b_1a\) held fixed across all observations of the unknown source:
\[
y(a)=\Phi_p(a)+b_0+b_1a+\eta(a),\qquad |\eta(a)|\le\varepsilon.
\tag{2}
\]
The errors are adversarial pointwise errors; the candidate set is known.
As in AF-568/569, different hypothetical sources may have different shared nuisance parameters. Write \(\varepsilon_{\rm cal,full}(A,S)\),
\(\varepsilon_{\rm off,full}(A,S)\), and
\(\varepsilon_{\rm aff,full}(A,S)\) for the supremal unique-decoding noise radii from the entire interval, respectively with known calibration, an unrestricted shared constant offset, and the unrestricted shared affine law (2).
Write \(\varepsilon_{\rm aff,3}(A,S)\) for the best fixed three-query affine radius.

Let \(\gamma\) be Euler's constant, \(B_1\) the Meissel--Mertens prime-reciprocal constant, and write the analytic prime-zeta boundary expansion as
\[
P(1+x)=-\log x+C_0+C_1x+O(x^2),
\quad C_0=B_1-\gamma,\quad c=e^{B_1}.
\tag{3}
\]
For an odd prime \(p\), define the **exact** coefficients
\[
b_p=h_p(1)=\frac1{p(p+1)},\quad
d_p=h_p'(1),\quad K_p=ce^{-b_p},\quad
M_p=K_p\bigl[(C_1-d_p)K_p-1\bigr].
\tag{4}
\]
There exists an absolute \(P_0\) such that \(M_q-M_p<0\) whenever
\(q>p\ge P_0\) are odd primes. For any **fixed finite** candidate set
\(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), with \(\min S\ge P_0\), put
\[
\alpha(S)=\min_{i<m}(K_{p_{i+1}}-K_{p_i})>0,\qquad
\beta(S)=\min_{i<m}(M_{p_i}-M_{p_{i+1}})>0.
\tag{5}
\]
Then, in the limit \(A\downarrow0\) **with \(S\) fixed**,
\[
\boxed{\begin{aligned}
\varepsilon_{\rm cal,full}(A,S)
   &=\frac{\alpha(S)}2 A+O_S(A^2),\\
\varepsilon_{\rm off,full}(A,S)
   &=\frac{\alpha(S)}4 A+O_S(A^2),\\
\varepsilon_{\rm aff,full}(A,S)
   &=\frac{\beta(S)}{16}A^2+O_S(A^3),\\
\varepsilon_{\rm aff,3}(A,S)
   &=\frac{\beta(S)}{16}A^2+O_S(A^3).
\end{aligned}}\tag{6}
\]
In particular,
\[
\boxed{\lim_{A\downarrow0}
\frac{\varepsilon_{\rm aff,3}(A,S)}
     {\varepsilon_{\rm aff,full}(A,S)}=1.}
\tag{7}
\]
The fixed, source-independent triple
\[
(a_0,a_1,a_2)=(A^2,A/2,A),\qquad 0<A<1/2,
\tag{8}
\]
already achieves (7). Two or fewer observations cannot identify two sources even at zero noise under unrestricted affine calibration, because an affine nuisance fits any two distinct observed coordinates. Thus three fixed observations are **asymptotically** sufficient for the bounded-window full-curve margin, although AF-569 requires four adaptive observations for **exact universal full-margin attainment on the entire unbounded domain**. These are different experiments; no contradiction is involved.

## Exact source boundary jets

The prime-zeta normal form (3) follows from
\(P(s)=\log\zeta(s)-\sum_{k\ge2}P(ks)/k\): the second term and the regular part of \(\log\zeta\) are analytic near \(s=1\). The classical exponential integral satisfies
\[
E_1(a)=-\gamma-\log a+a+O(a^2).
\tag{9}
\]
For each fixed \(p\), insert \(x=\Phi_p(a)-1\) into
\(Q_p(1+x)=E_1(a)\). Its expansion is
\[
-\log x+(C_0-b_p)+(C_1-d_p)x+O_p(x^2)
=-\gamma-\log a+a+O(a^2).
\]
Exponentiating the logarithmic normal form, or applying the analytic implicit-function theorem to the exponentiated equation, gives
\[
\boxed{\Phi_p(a)=1+K_pa+M_pa^2+O_p(a^3).}
\tag{10}
\]
Indeed the constant term yields \(K_p=e^{C_0+\gamma-b_p}\), and the coefficient of \(a\) yields
\(M_p/K_p=(C_1-d_p)K_p-1\). The boundary value \(\Phi_p(0)=1\) is a continuous/analytic extension, not an additional allowed query.

For \(q>p\), let
\(\delta_{p,q}=b_p-b_q>0\),
\(G_{p,q}(a)=\Phi_q(a)-\Phi_p(a)\). Then
\[
G_{p,q}(a)=\Delta K_{p,q}\,a+\Delta M_{p,q}\,a^2+O_{p,q}(a^3),
\quad
\Delta K=K_q-K_p>0,\quad \Delta M=M_q-M_p.
\tag{11}
\]
The sign of \(\Delta M\) is not inferred by subtracting two uncontrolled asymptotics. AF-559's exact positive integral identity gives
\[
k_{p,q}(s):=h_p(s)-h_q(s)
=s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv,
\tag{12}
\]
so \(k_{p,q}(1)=\delta_{p,q}\) and
\[
\frac{d_p-d_q}{\delta_{p,q}}
=\frac32-
\frac{\int_p^q\int_v^{v+1}u^{-3}\log u\,du\,dv}
     {\int_p^q\int_v^{v+1}u^{-3}\,du\,dv}
=-\log p+O(1).
\tag{13}
\]
The last remainder is uniform over every \(q>p\): after writing
\(\log u=\log p+\log(u/p)\), the positive \(u^{-3}\) weight is supported above \(p\); its truncated mean of \(\log(u/p)\) is bounded by the full-tail mean up to \(O(1/p)\), which is \(O(1)\). This includes minimal prime gaps and \(q/p\to\infty\).

Now \(K_q-K_p=c\delta_{p,q}[1+O(p^{-2})]\),
\(K_q^2-K_p^2=O(\delta_{p,q})\), and \(d_q=O((\log q)/q^2)=O(1)\).
The exact rearrangement
\[
M_q-M_p
=(C_1-d_q)(K_q^2-K_p^2)
 +(d_p-d_q)K_p^2-(K_q-K_p)
\tag{14}
\]
therefore gives, **uniformly in all odd \(q>p\to\infty\)**,
\[
\boxed{
\Delta K_{p,q}=c\delta_{p,q}[1+O(p^{-2})],\qquad
-\Delta M_{p,q}
=c^2\delta_{p,q}\log p\,[1+O(1/\log p)]>0.
}
\tag{15}
\]
In particular the first non-affine source jet is quadratic and has a common sign across all large edit locations; it is not a spurious coordinate-relabeling difference.

## Chebyshev quotient and the three observations

For any two sources, full-interval observation under the affine nuisance identifies them exactly up to the distance of their gap from the affine subspace:
\[
\varepsilon_{\rm aff,full}(A,\{p,q\})
=\frac12\inf_{u,v\in\mathbb R}
\sup_{0<a\le A}|G_{p,q}(a)-u-va|.
\tag{16}
\]
The factor \(1/2\) comes from intersecting two pointwise \(L^\infty\) noise balls with independently chosen hypothetical affine calibrations. For a many-source experiment take the minimum of (16) over all source pairs.

A linear function absorbs the \(\Delta K\,a\) term in (11). Under \(a=At\), the remaining leading approximation problem is \(\Delta M A^2t^2\) versus affine functions of \(t\in[0,1]\). The elementary Chebyshev identity
\[
\inf_{u,v}\|t^2-u-vt\|_{L^\infty[0,1]}=\frac18
\tag{17}
\]
follows because \(t-1/8\) has alternating errors \(+1/8,-1/8,+1/8\) at \(0,1/2,1\); the functional
\(e(0)-2e(1/2)+e(1)\) supplies the matching lower bound.
The distance-to-subspace map is 1-Lipschitz under uniform perturbations. Thus (11), (16), and (17) yield
\[
\varepsilon_{\rm aff,full}(A,\{p,q\})
=\frac{|\Delta M_{p,q}|}{16}A^2+O_{p,q}(A^3).
\tag{18}
\]
Since every \(\Delta M_{p,q}\) is a sum of negative adjacent \(\Delta M\)'s for sufficiently large \(\min S\), the minimum over source pairs is attained to leading order by one of the adjacent pairs, proving the third line of (6).

For the fixed triple (8), put
\(w=(a_2-a_1)/(a_2-a_0)\). The unique affine-annihilating contrast is
\[
C(y)=y(a_1)-w\,y(a_0)-(1-w)y(a_2).
\tag{19}
\]
Its error is bounded by \(2\varepsilon\), and that bound is attainable; pairwise contrast-center intervals therefore overlap exactly when their centers differ by at most \(4\varepsilon\). Direct interpolation of a quadratic gives
\[
C(G_{p,q})=
\Delta M_{p,q}(a_1-a_0)(a_1-a_2)+O_{p,q}(A^3)
=-\frac{\Delta M_{p,q}}4 A^2+O_{p,q}(A^3).
\tag{20}
\]
The triple's pairwise unique-decoding radius is \(|C(G_{p,q})|/4\); minimizing over pairs and using the common sign in (15) gives
\(\beta(S)A^2/16+O_S(A^3)\). Because no three-query policy can exceed the entire-interval radius, this proves the final line of (6) and (7).

For known calibration the pointwise ordered gaps have
\(\sup_{0<a\le A}G_{p,q}(a)=\Delta K_{p,q}A+O_{p,q}(A^2)\).
A free constant offset changes the pairwise distance to half the oscillation of the gap on this interval; its noise radius is therefore
\(\Delta K_{p,q}A/4+O_{p,q}(A^2)\).
Positive adjacent \(\Delta K\)'s yield the first two lines of (6).

## Conditioning, prior art, and limitations

The coefficient comparison (15) quantifies the price of forgetting the affine output law. For any fixed pair, first take \(A\downarrow0\):
\[
\frac{\varepsilon_{\rm aff,full}(A,\{p,q\})}
     {\varepsilon_{\rm off,full}(A,\{p,q\})}
=\frac{|\Delta M_{p,q}|}{4\Delta K_{p,q}}A+O_{p,q}(A^2).
\tag{21}
\]
Then letting \(p\to\infty\), uniformly over \(q>p\), the leading coefficient is
\((c/4)\log p\,[1+O(1/\log p)]\).
This is a **sequential coefficient statement**, not a uniform joint \((p,A)\) limit. It exposes the natural critical scale \(A\asymp1/\log p\) while rigorously showing an extra small-window power of \(A\) under affine rather than constant-offset uncertainty.

Chebyshev best uniform approximation, finite-difference contrasts, and nuisance-resistant experimental design are classical. Equation (17) is proved directly, not presented as a new approximation theorem. The prime-zeta analytic expansion is classical (Fröberg 1968), with the 2026 Kawalec expansion a preprint; both are already documented under AF-552 in SOURCES.md. General nuisance and model-design precedents are documented under AF-568 (Atkinson--Cox 1974 and Rosa--Harman 2016). The source-specific delta is the **exact curvature coefficient, its uniform sign for rational-prime edit locations, and the sharp bounded-window three-query/full-curve fidelity ratio**. No new general-method priority is claimed.

The interval is \((0,A]\), the input coordinate \(a\) is fixed/common, the affine calibration is unbounded but shared across probes, and the errors are independent bounded adversarial errors. The asymptotics in (6)--(7) require **first fixing the finite candidate set** and then shrinking \(A\). They do not establish uniform error terms as the prime locations, candidate count, or logarithmic diameter vary jointly with \(A\), and do not assert exact three-query saturation at a fixed positive \(A\). No fixed nonzero absolute noise floor survives. Recalibrating independently at each point destroys the shared-nuisance contrast. These are generalized-prime matched controls indexed by genuine rational-prime edit locations, not a discriminator of ordinary rational primes against arbitrary generalized-prime systems. No RH consequence follows without a separate faithful and stable arithmetic-to-zeros transfer.

Decisive independent checks: expand \(E_1\) through its linear term and rederive \(K_p,M_p\); verify the \(3/2\) logarithmic-derivative coefficient in (13); check the uniform-in-\(q\) tail mean rather than differencing uncontrolled individual prime asymptotics; prove (17) at the three alternation sites; check the \(1/2\) pairwise ball radius and \(1/4\) three-contrast radius factors independently; confirm that all nonadjacent quadratic coefficients have the common sign; and do not import AF-569's unbounded-domain \(d(S)/4\) value into a finite window.

## Consequence for Arithmetic Fidelity

AF-569's unbounded-domain four-query theorem needs remote nuisance anchors and a global gap peak. When only a shrinking near-boundary window is retained, the same source family instead loses its affine-quotiented information at **quadratic**, rather than linear, rate in the window width; a simple fixed three-query second difference asymptotically preserves **all of that reduced information**. Thus exact recovery budget and absolute conditioning can move in opposite directions under restriction of the representation: one fewer probe suffices relative to a newly diminished quotient margin, not relative to AF-569's original full-domain margin.
