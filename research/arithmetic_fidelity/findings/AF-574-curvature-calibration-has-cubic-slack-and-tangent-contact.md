# AF-574 — Curvature calibration has a cubic slack law and a tangent-contact sampling certificate

## Status and experiment

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · CALIBRATION-MISSPECIFICATION · SHARP-LOCAL-MINIMAX · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

AF-572 leaves a transition outside its fixed-budget small-window theorem: the signed source curvature may cross the allowed calibration curvature inside the observed window. This finding resolves that transition for the second-derivative constraint. The surviving margin is cubic in the remaining curvature-budget slack. Near threshold, its optimal observation span ends at a tangent-contact point **after** the curvature crossing, so the first-derivative clipping rule of AF-573 does not extend by simply clipping one more derivative.

Retain the registered generalized-prime edit curves
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\tag{1}
\]
Fix a known finite set \(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), of sufficiently large odd rational-prime edit locations. Observe
\[
 y(a)=\Phi_p(a)+b(a)+\eta(a),\qquad 0<a\le A,
 \qquad b\in C^2[0,A],\quad \|b''\|_\infty\le L,
 \quad |\eta|\le\varepsilon.
\tag{2}
\]
The nuisance is shared across observations within an experiment; competing sources may have different nuisances. Its affine part is unrestricted. All derivative bounds refer to the retained coordinate \(a\). Let \(\varepsilon_{\rm full}\) and \(\varepsilon_3\) denote supremal deterministic-noise identification radii for the full window and the best fixed three-point design.

## Exact margin through the curvature transition

There is \(A_0(S)>0\), independent of \(L\), and an adjacent gap \(G_*\) such that, with \(f=-G_*\),
\[
 0<f''(a)\le-G_i''(a),\qquad G_i=\Phi_{p_{i+1}}-\Phi_{p_i},
 \qquad f'''(a)<0 \quad(0\le a\le A_0).
\tag{3}
\]
Put \(d=f''(0)>0\), \(k=-f'''(0)>0\), and \(C=2L\). The critical budget is \(L_{\rm crit}=d/2\).

Fix any \(0<A\le A_0\). If \(C\ge d\), the least-gap pair aliases exactly on the full window, and both radii are zero. If \(0\le C<d\), define
\[
 H(a)=f(a)-Ca^2/2,\qquad
 F(t)=tH'(t)-H(t)+H(0)
     =\int_0^t s\{f''(s)-C\}\,ds.
\tag{4}
\]
Choose
\[
 t=\begin{cases}
 A,&F(A)\ge0,\\
 \text{the unique positive root of }F(t)=0,&F(A)<0,
 \end{cases}
 \qquad m=\frac{H(t)-H(0)}t.
\tag{5}
\]
There is a unique interior point \(x\in(0,t)\) maximizing the chord deficit:
\[
 H'(x)=m,\qquad
 \Delta=H(0)+mx-H(x)>0.
\tag{6}
\]
Here the root in (6) is the interior one; when \(t<A\), \(H'(t)=m\) also holds at the endpoint. Then
\[
 \boxed{\displaystyle
 \varepsilon_3(A,S,L)=\varepsilon_{\rm full}(A,S,L)=\frac{\Delta}{4}.}
\tag{7}
\]
The closed-window certificate uses \((0,x,t)\). Legal designs move zero to a positive coordinate and approach (7); equality is of suprema. At most two queries, even adaptive ones, cannot identify the source at zero noise because a free affine nuisance interpolates any two response values. Thus the minimal query count still captures the entire reduced margin throughout the transition.

When the curvature crossing \(r\), defined by \(f''(r)=C\), lies inside the window, an interior contact point satisfies \(t>r\). The balance in (4), not the pointwise crossing, determines when enlarging the window stops adding margin. Once \(t<A\), the margin is unchanged by further enlargement within \([0,A_0]\).

## Proof: a concave envelope with a three-point certificate

For a signed source gap \(h\), its two noiseless observation classes have distance
\[
 D_C(h)=\inf_{b\in C^2[0,A],\ \|b''\|_\infty\le C}\|h-b\|_\infty.
\tag{8}
\]
Writing \(\mathcal B_{2,L}=\{b\in C^2[0,A]:\|b''\|_\infty\le L\}\), this uses \(\mathcal B_{2,L}-\mathcal B_{2,L}=\mathcal B_{2,2L}\). The supremal two-source noise radius is \(D_C(h)/2\); take the least pairwise distance for the finite source set. These two factors of two have different origins.

Since \(H''=f''-C\) is strictly decreasing and initially positive, it is either positive throughout or crosses once from positive to negative. The function \(F\) initially increases, and after any crossing strictly decreases. This proves the root assertion in (5). Moreover,
\[
 \frac{d}{da}\frac{H(a)-H(0)}a=\frac{F(a)}{a^2}.
\tag{9}
\]
Consequently the chord \(\ell(a)=H(0)+ma\) strictly majorizes \(H\) on \((0,t)\). If \(t<A\), it meets \(H\) tangentially in its concave region. Therefore
\[
 M(a)=\begin{cases}\ell(a),&0\le a\le t,\\H(a),&t\le a\le A\end{cases}
\tag{10}
\]
is the least concave majorant of \(H\). Any concave majorant must dominate the chord on \([0,t]\) and must dominate \(H\) elsewhere, proving minimality directly. The derivative \(H'\) first increases and then, if applicable, decreases; its crossing of \(m\) in \((0,t)\) is unique. Thus \(\|M-H\|_\infty=\Delta\).

Consider
\[
 b_0(a)=Ca^2/2+M(a)-\Delta/2.
\tag{11}
\]
It has uniform error \(\Delta/2\) against \(f\). It is \(C^1\), with bounded weak second derivative
\[
 b_0''=\begin{cases}C,&a<t,\\ f''(a),&a>t.\end{cases}
 \qquad 0\le b_0''\le C.
\tag{12}
\]
For an interior join, tangency ensures continuity of the first derivative, and \(0<f''(a)<C\) after the join. If \(t=A\), (11) is simply quadratic. In general (11) need not be \(C^2\), so it is not silently asserted to attain the infimum in (8). Extend it outside the interval by quadratics matching endpoint value and first derivative, with second derivatives in \([0,C]\). Convolution with nonnegative smooth unit-mass kernels yields smooth functions with second derivative still in \([0,C]\), converging uniformly on \([0,A]\) to (11). Thus \(D_C(f)\le\Delta/2\) in the stated \(C^2\) class as well. For \(C=0\), (11) is affine already.

For the converse, use the chord functional
\[
 Jv=(1-x/t)v(0)+(x/t)v(t)-v(x),
 \qquad \|J\|=2,\qquad J\Pi_1=0.
\tag{13}
\]
Convexity gives \(Jv\ge0\) whenever \(v''\ge0\). Every signed source gap \(h=-\sum G_i\) has \(h''\ge f''\), while \(b''\le C\) implies \(Jb\le C J(a^2/2)\). Hence
\[
 J(h-b)\ge Jf-CJ(a^2/2)=JH=\Delta,
 \qquad \|h-b\|_\infty\ge\Delta/2.
\tag{14}
\]
This holds already on the three nodes and against every candidate pair; the least pair has the matching upper bound (11). Dividing by the observation-noise factor proves (7). Perturbing the zero node preserves the convexity functional and nuisance bound, and its value tends to (14). With finitely many source pairs this proves the legal-design supremum.

For two adaptive queries, follow a hypothetical zero transcript and interpolate \(-\Phi_p\) separately at its at most two distinct queried coordinates with an affine function. Its second derivative is zero, so each source realizes the same transcript under (2). No guaranteed identification is possible. Finally, if \(C\ge d\), then \(\|G_*''\|_\infty=d\le C\); the nuisances \(G_*/2\) and \(-G_*/2\) give an exact full-curve alias.

## Cubic slack law and the observation span

Fix \(S,A\), and let \(\delta=d-C\downarrow0\). Modulo an affine function,
\[
 H(a)=\delta a^2/2-ka^3/6+O_S(a^4).
\tag{15}
\]
The contact equation is
\[
 F(t)=\delta t^2/2-kt^3/3+O_S(t^4)=0.
\]
After division by \(t^2\), the implicit-function theorem at \((\delta,t)=(0,0)\) gives the nonzero root. Substitution into (6) gives
\[
 \boxed{\displaystyle
 t=\frac{3\delta}{2k}+O_S(\delta^2),\qquad
 x=\frac{\delta}{2k}+O_S(\delta^2),\qquad
 \varepsilon_{\rm full}=\frac{\delta^3}{48k^2}+O_S(\delta^4).}
\tag{16}
\]
The curvature crossing is \(r=\delta/k+O_S(\delta^2)\), strictly between the inner node and the contact. For the leading cubic, the chord slope after affine normalization is \(3\delta^2/(8k)\) and its maximal deficit is \(\delta^3/(12k^2)\), checking both constants in (16).

One can also resolve the joint window/slack transition. Set \(\delta=kA\tau\). Uniformly for \(\tau\) in a fixed bounded interval as \(A\downarrow0\),
\[
 \varepsilon_{\rm full}=\frac{kA^3}{4}\Psi_2(\tau)+O_S(A^4),
\quad
 \Psi_2(\tau)=
 \begin{cases}
 0,&\tau\le0,\\
 \tau^3/12,&0<\tau\le2/3,\\
 \tau z_\tau^2/2-z_\tau^3/3,&\tau\ge2/3,
 \end{cases}
 \quad z_\tau=\tau-\sqrt{\tau^2-\tau+1/3}.
\tag{17}
\]
For \(\tau>0\), the normalized cubic \(U_\tau(z)=\tau z^2/2-z^3/6\) has contact \(\min(1,3\tau/2)\); when it is one, the inner extremum is \(z_\tau\). This proves the displayed profile. The remainder follows because taking a least concave majorant is 1-Lipschitz in the uniform norm: a constant shift of any majorant majorizes the correspondingly perturbed function. Hence \(\|\operatorname{LCM}(H)-H\|_\infty\) is 2-Lipschitz in \(H\). Formula (16), rather than the absolute remainder in (17), supplies relative precision as \(\tau\to0\). For \(\tau\le0\) the actual margin is exactly zero.

Every fixed legal finite design still loses identifiability before the full window. If its smallest coordinate is \(u>0\), then
\[
 f''(u)/2\le L<d/2
\tag{18}
\]
is a nonempty budget interval on which that design has an exact noiseless alias while (7) remains positive. Indeed extend \(f|_{[u,A]}\) backward by its second-order Taylor polynomial at \(u\). This is a \(C^2\) function with second-derivative norm \(f''(u)\), and it equals \(f\) at every queried point. With the appropriate signs, half this function supplies the two nuisance witnesses. This is a sufficient alias interval, not a claimed sharp threshold for every finite design. The three-point equality in (7) permits the design to depend on the known budget.

## Arithmetic instantiation and evidence boundary

AF-571's exact inverse sensitivity yields, uniformly over \(q>p\to\infty\) at each fixed order \(j\),
\[
 [a^j](\Phi_q-\Phi_p)
 =(-1)^{j-1}\frac{c^j}{(j-1)!}\Delta_{p,q}(\log p)^{j-1}
 [1+O_j(1/\log p)],
 \quad c=e^{B_1},\quad
 \Delta_{p,q}=\frac1{p(p+1)}-\frac1{q(q+1)}>0,
\tag{19}
\]
where \(B_1\) is the Meissel–Mertens constant. This is obtained by integrating the positive real-edit sensitivity, not by subtracting uncontrolled source remainders. Orders two and three give \(-G_i''(0)>0\) and \(G_i'''(0)>0\). For a fixed finite source set, continuity and analyticity yield a common window of positive decreasing signed curvatures and a pointwise least curvature germ, including tied endpoint values. This supplies (3) independently of \(L\).

For two sources, \(d=2c^2\Delta_{p,q}\log p[1+O(1/\log p)]\) and \(k=3c^3\Delta_{p,q}(\log p)^2[1+O(1/\log p)]\). Writing \(\theta=1-L/L_{\rm crit}\), first fix the source pair and let \(\theta\downarrow0\). Then
\[
 \varepsilon_{\rm full}\sim\theta^3\frac{d^3}{48k^2},\qquad
 \frac{d^3}{48k^2}=\frac{\Delta_{p,q}}{54\log p}
 [1+O(1/\log p)],\qquad
 \frac{3d}{2k}=\frac{1+O(1/\log p)}{c\log p}.
\tag{20}
\]
The last coefficient determines the contact span \(t\sim3\theta d/(2k)\). There is no asserted uniform simultaneous prime/window/slack limit.

## Prior art, controls and consequence

Least-concave-majorant chord geometry and interior tangency are classical; [Franců–Kerman–Sinnamon (2017), Introduction and Lemmas 1–2](https://arxiv.org/abs/1608.02581) state these properties explicitly. [Mironenko (2006)](https://www.mathnet.ru/eng/smj899) studies uniform approximation under a bounded second derivative via uniform and nonuniform three-point grids. His [2008 paper](https://www.mathnet.ru/eng/mzm4103) gives sharp general estimates through the second modulus of continuity; the bounded-derivative/perfect-spline literature already recorded under AF-572 is broader still. The envelope, derivative-constrained approximation problem, and use of three-point tests are not new mechanisms. Equations (4)–(14) independently prove the special ordered-curvature case needed here; no general approximation-theory priority is claimed.

An exact control is \(f(a)=a^2-a^3/3\) on \([0,1/2]\), with \(L=3/4\). It gives \(d=k=2\), \(\delta=1/2\), \(r=1/4\), \(x=1/8\), \(t=3/8\), \(\Delta=1/384\), and radius \(1/1536\). Direct rational substitution verifies both tangency and the dual lower bound. A separate numerical control \(f(a)=e^{-a}\) on \([0,1]\), at several curvature budgets, checks the endpoint/contact regimes and the envelope error; it is a diagnostic, not proof of any prime claim.

The mathematical delta is the exact all-budget curvature-transition certificate, including the tangent-contact span and cubic slack loss absent from AF-572. The sign and monotonicity in (3) are load-bearing: general oscillatory curvatures may require several contact intervals, and this three-node conclusion is not asserted for them. The \(C^2\) versus bounded-weak-curvature distinction is handled by approximation, not an unsupported attainment claim. Budget-dependent observation geometry remains necessary even though three probes suffice as a supremum.

These are generalized-prime matched controls with a fixed common input coordinate. The result does not transfer automatically through a physical nonlinear curvature decoder, unknown calibration law, input-coordinate error, or unknown source list. It yields no uniform absolute noise floor, general ordinary-prime discriminator, or RH consequence. The ordinary-prime application still needs a source-derived nuisance law and a stable bridge into this precise observation geometry.
