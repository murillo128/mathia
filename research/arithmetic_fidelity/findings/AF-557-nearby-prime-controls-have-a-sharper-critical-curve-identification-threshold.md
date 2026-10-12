# AF-557 — Nearby prime controls have a sharper critical-curve identification threshold

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · PAIRWISE-IDENTIFICATION · INVERSE-CONDITIONING · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Claim: identifying the changed prime is harder than detecting a change

Let
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
\Phi(a)=P^{-1}(E_1(a)),\qquad a>0,
\]
with the source-critical coordinate and common-output-calibration quotient of AF-554. For every odd rational prime \(t\), form the order-preserving integer-generator control that replaces only \(t\) by \(t+1\):
\[
h_t(s)=t^{-s}-(t+1)^{-s},\qquad
Q_t(s)=P(s)-h_t(s),\qquad
\Phi_t(a)=Q_t^{-1}(E_1(a)).
\tag{1}
\]
These are matched generalized-prime controls, not two alternative rational-prime sequences.

Consider odd primes \(p<q\) with \(p\to\infty\), \(q/p\to1\), and \(g=q-p>0\). Their critical curves satisfy \(\Phi_p(a)<\Phi_q(a)<\Phi(a)\) for every \(a>0\). Define the *pairwise identification distance*
\[
D_{p,q}:=\max_{a>0}\big[\Phi_q(a)-\Phi_p(a)\big].
\tag{2}
\]
Then
\[
\boxed{D_{p,q}=\frac{2g}{e\,p^3\log p}(1+o(1)).}
\tag{3}
\]
The normalized whole-curve response also has a sharp moving boundary profile. With \(B_1\) the Meissel--Mertens reciprocal-prime constant, \(c=e^{B_1}\), and \(f(u)=ue^{1-u}\) for \(u\ge0\),
\[
\boxed{\lim_{\substack{p\to\infty,\ q/p\to1\\p<q\ {\rm odd\ primes}}}
\ \sup_{a>0}
\left|\frac{\Phi_q(a)-\Phi_p(a)}{D_{p,q}}
-f(ca\log p)\right|=0.}
\tag{4}
\]
The limit is uniform for **every** sequence of prime pairs obeying \(q/p\to1\), not only for a bounded gap.

For the consecutive prime \(q=p^+\), write \(g_p=p^+-p\). The prime number theorem implies \(g_p=o(p)\). AF-555's baseline detection distance \(D_p=\max_a[\Phi(a)-\Phi_p(a)]\sim(e p^2\log p)^{-1}\) therefore obeys
\[
\boxed{\frac{D_{p,p^+}}{D_p}\sim\frac{2g_p}{p}\longrightarrow0.}
\tag{5}
\]
Thus the full calibrated curve can detect a remote prime-to-composite edit at a noise scale where it still cannot resolve **which of two neighboring primes** was edited. The additional attenuation comes from cancelling two nearby source defects, not from omitting the optimal moving window.

## Exact comparison identity: subtract the sources before inverting

For \(s>1\), let \(r_t(s)=Q_t^{-1}(P(s))<s\). The common source-coordinate \(s=\Phi(a)\) gives
\[
\Phi_q(a)-\Phi_p(a)=r_q(s)-r_p(s).
\tag{6}
\]
Put \(k_{p,q}(s)=h_p(s)-h_q(s)\). Differentiating the continuous-position atom defect
\[
h_v(s)=s\int_v^{v+1}u^{-s-1}\,du
\]
with respect to \(v\), then integrating from \(p\) to \(q\), gives the **positive exact identity**
\[
\boxed{k_{p,q}(s)
=s(s+1)\int_p^q\!\int_v^{v+1}u^{-s-2}\,du\,dv>0.}
\tag{7}
\]
In particular \(Q_p=Q_q-k_{p,q}<Q_q\), proving the ordering of the curves.

Since \(Q_q(r_q(s))=P(s)\) while
\(Q_p(r_q(s))=P(s)-k_{p,q}(r_q(s))\), the ordinary mean-value theorem, applied to the *same* function \(Q_p\) between \(r_p(s)\) and \(r_q(s)\), yields an exact \(\xi_{p,q,s}\in(r_p(s),r_q(s))\) with
\[
\boxed{r_q(s)-r_p(s)
=\frac{k_{p,q}(r_q(s))}{-Q_p'(\xi_{p,q,s})}.}
\tag{8}
\]
Subtracting the two separate AF-555 first-order asymptotics is **not** justified at the smaller scale (3): their independent errors may dominate the desired difference. Equation (8) cancels the common response first and then bounds the remaining inverse perturbation.

AF-555 proves
\[
\epsilon_p:=\sup_{s>1}\frac{|h_p'(s)|}{-P'(s)}
=O(\log p/p^2)=o(1),
\quad
0<s-r_t(s)\le D_t=O((t^2\log t)^{-1}).
\tag{9}
\]
Also \(P''>0\), so \(-P'\) is decreasing. Since
\(-Q_p'(v)\ge(1-\epsilon_p)(-P'(v))\), (8) gives
\[
0<r_q(s)-r_p(s)
\le\frac{k_{p,q}(r_q(s))}
{(1-\epsilon_p)(-P'(s))}.
\tag{10}
\]

The integral in (7) is supported on \(u\in[p,q+1]\). Its logarithmic \(s\)-derivative equals
\[
\frac{d}{ds}\log k_{p,q}(s)
=\frac1s+\frac1{s+1}
-\frac{\int_p^q\int_v^{v+1}(\log u)u^{-s-2}\,du\,dv}
{\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv}.
\tag{11}
\]
For all \(s\ge1\), its absolute value is at most \(\log(q+1)+2\). Since
\(s-r_q(s)\le D_q=O((q^2\log q)^{-1})\),
\[
\sup_{s>1}\left|\frac{k_{p,q}(r_q(s))}{k_{p,q}(s)}-1\right|
\le\exp\!\big((\log(q+1)+2)D_q\big)-1=o(1).
\tag{12}
\]
Consequently the **global** majorant
\[
0<r_q(s)-r_p(s)\le(1+o(1))
\frac{k_{p,q}(s)}{-P'(s)}
\qquad(s>1)
\tag{13}
\]
holds with an error independent of \(s\), and uniformly in the stipulated near-pair regime.

## Sharp boundary layer and global maximization

Write \(L=\log p\), \(s=1+x\). The prime-zeta boundary expansion from AF-552/AF-555 is
\[
-P'(1+x)=x^{-1}+O(1)\qquad(x\downarrow0).
\tag{14}
\]
For \(0<x\le L^{-1/2}\), \(q/p\to1\) and (7) imply uniformly
\[
k_{p,q}(1+x)
=2g\,p^{-3}e^{-Lx}
\left(1+O\!\left(x+\frac{g+1}{p}\right)\right).
\tag{15}
\]
Combining with (14),
\[
\frac{k_{p,q}(1+x)}{-P'(1+x)}
=2g\,p^{-3}x e^{-Lx}(1+o(1)).
\tag{16}
\]
The error in (16) is uniform on \(0<x\le L^{-1/2}\).

On \(L^{-1/2}\le x\le\delta\), for any fixed sufficiently small \(\delta>0\), (13)--(16) bound the displacement by
\(o(g/(p^3L))\), because \(Lx\,e^{-Lx}\to0\) uniformly. For \(x\ge\delta\), the elementary inequalities
\[
k_{p,q}(s)\le s(s+1)g\,p^{-s-2},
\qquad -P'(s)\ge(\log2)\,2^{-s}
\tag{17}
\]
give a uniform bound \(O_\delta(g\,p^{-3-\delta})=o(g/(p^3L))\): the envelope \(s(s+1)(2/p)^s\) decreases for \(s\ge1+\delta\) once \(p\) is large. This excludes a hidden maximizer away from the boundary.

For \(x=u/L\) and \(u\) in a compact subinterval of \((0,\infty)\), AF-555's uniform displacement bound in (9) shows that
\(\xi_{p,q,s}-1=x(1+o(1))\). Hence (8), (12), and (14)--(16) sharpen (13) to
\[
\frac{p^3L}{2g}\,[r_q(1+u/L)-r_p(1+u/L)]
\longrightarrow ue^{-u}
\tag{18}
\]
locally uniformly for \(u>0\). The matching tails above make this convergence uniform on \(u\in(0,\infty)\) after comparison with the function \(ue^{-u}\), whose unique maximum is \(1/e\) at \(u=1\). This proves (3), with every asymptotic maximizer satisfying
\[
\log p\,(\Phi(a_{p,q})-1)\longrightarrow1.
\tag{19}
\]

For each fixed \(p,q\), the displacement in (8) tends to zero at both ends \(s\downarrow1\) and \(s\to\infty\): at the first endpoint both inverses tend to \(1\), and at the second (13), (17) tend to zero. Therefore the positive maximum in (2) is attained.

Finally the Mertens matching of AF-555 yields, near \(a=0\),
\[
a=e^{-B_1}(\Phi(a)-1)+O((\Phi(a)-1)^2).
\tag{20}
\]
Thus \(L(\Phi(a)-1)-cLa=o(1)\) in the moving layer \(L(\Phi(a)-1)=O(1)\). A compact-core/two-tail decomposition using (13), (16)--(18) transfers the uniform normalized response to the source-natural \(a\)-coordinate and proves (4). In particular every maximizing critical parameter satisfies
\[
a_{p,q}\log p\longrightarrow e^{-B_1}.
\tag{21}
\]

## Exact two-hypothesis noise threshold and source distinction

Equip complete *already-calibrated* critical curves with the \(L^\infty(0,\infty)\) distance in the common \(a\)-coordinate. Suppose the only two admitted source hypotheses are \(Q_p\) and \(Q_q\), and an adversary may perturb either observed curve by any function of sup norm at most \(\varepsilon\). Their closed noise balls are disjoint exactly when \(2\varepsilon<D_{p,q}\): if \(2\varepsilon\ge D_{p,q}\), the midpoint \((\Phi_p+\Phi_q)/2\) belongs to both balls; if \(2\varepsilon<D_{p,q}\), the triangle inequality forbids overlap. Therefore the sharp deterministic full-curve two-source identification threshold is
\[
\varepsilon_{\rm id}(p,q)=\frac12D_{p,q}
\sim\frac{g}{e\,p^3\log p}.
\tag{22}
\]

Against the unmodified reference curve, the corresponding detection threshold is \(D_p/2\sim(2e p^2\log p)^{-1}\). For consecutive-prime alternatives, their ratio tends to zero at the explicit relative-gap rate \(2g_p/p\). This is *not* a stochastic minimax law or an identification guarantee among all possible generalized-prime systems. Nor does it imply that a bounded number of samples locates the edit: AF-556's \(\Theta(\log\log P)\) theorem concerns fixed-fraction capture relative to a known reference, not pairwise identification under absolute noise.

The two source controls differ in a genuine marked source property: \(Q_p\) replaces generator \(p\), while \(Q_q\) leaves \(p\) untouched and replaces \(q\); they are not reparameterizations or relabelings of the same generator multiset. The pairs are admissible for odd primes since \(t+1\) is composite and falls strictly between \(t\) and the next prime. They share the leading Mertens coefficient, all reference source data outside two remote positions, and the common calibration quotient; no extra arithmetic mark is supplied to the decoder.

## Prior art, audit, and boundary

The analytic inputs are the classical prime-zeta/Mertens boundary expansion, AF-554's critical-limit map, AF-555's *uniform* inverse-displacement control, and AF-556's globally normalized moving-window framework. The prime number theorem supplies \(p^+-p=o(p)\). Two-point metric/noise-ball arguments and close-node inverse-conditioning are classical; the Prony/super-resolution literature already recorded under AF-487 and AF-511 is relevant context. No priority is claimed for these tools or for generic ill-conditioning of neighboring exponential sources.

The new *line-specific* step is (7)--(8): **difference the two source defects before inverse linearization**. That proves the additional gap-sensitive cancellation which separate baseline approximations do not control and places its exact supremum threshold and whole-curve geometry in the same AF-554 representation as AF-555/AF-556.

Decisive falsification checks and scope restrictions:

1. Verify the sign and the factor \(s(s+1)\) in (7); omitting the derivative of the continuous generator-position defect would change the leading constant \(2/e\).
2. Verify (12) **uniformly in \(s>1\)** using AF-555's global displacement bound; a fixed-\(s\) Taylor subtraction would not establish (3).
3. Use the exact mean-value point \(\xi\in(r_p,r_q)\) in (8), not a subtraction of independent \(1+o(1)\) displacement formulas.
4. Require \(q/p\to1\). No sharp \(2g/p^3\) law is claimed for macroscopically separated controls, and the consecutive-prime specialization uses the prime number theorem, not an unproved bounded-gap conjecture.
5. Form each fixed-source critical-index limit before taking \(p,q\to\infty\). No uniform finite-index theorem is claimed when the changed generator moves jointly with the tail index.
6. Retain the common source \(a\)-registration, the \(s\)-coordinate, and the complete calibrated limiting curves. Independent horizontal warps, raw uncalibrated noise, pointwise derivative probes, or an additional marked-prime oracle change the experiment.
7. Neither a finite edit of a generalized-prime generator system nor this observation-distance bound establishes a changed zero divisor or an obstruction to RH itself.

**Arithmetic Fidelity consequence.** AF-555 quantified how a remote source edit fades against the rational-prime baseline, and AF-556 quantified where finitely many nonadaptive observations can intercept it. AF-557 separates **detection** from **identification** inside precisely that retained channel: two remote edits at adjacent prime locations become an additional relative-gap factor closer, despite sharing the same globally optimally located critical window. Exact source injectivity is therefore compatible with distinct and strictly nested quantitative tariffs for detecting an edit and locating which source coordinate was edited.