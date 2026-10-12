# AF-559 — All-pair prime-edit separation has a uniform sharp critical window

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · ALL-PAIR-IDENTIFICATION · UNIFORM-INVERSE-CONDITIONING · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Claim: the smaller edited prime governs every pairwise peak

Use the complete, common-output-calibration-invariant critical curves of AF-554. Let
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
E_1(a)=\int_a^\infty e^{-v}\frac{dv}{v},\quad
\Phi(a)=P^{-1}(E_1(a)).
\]
For each odd rational prime \(t\), replace the single generator \(t\) by \(t+1\), retaining all other prime generators and their order, and define
\[
h_t(s)=t^{-s}-(t+1)^{-s},\qquad
Q_t(s)=P(s)-h_t(s),\qquad
\Phi_t(a)=Q_t^{-1}(E_1(a)).
\tag{1}
\]
These are marked generalized-prime controls, not alternative sequences of rational primes. For all odd primes \(p<q\), the curves are strictly ordered
\(\Phi_p(a)<\Phi_q(a)<\Phi(a)\). Put
\[
B_{p,q}=p^{-2}-q^{-2}>0,\quad L=\log p,\quad
D_{p,q}=\max_{a>0}[\Phi_q(a)-\Phi_p(a)],
\]
and let \(B_1\) be the Meissel--Mertens prime-reciprocal constant, \(c=e^{B_1}\), and \(f(u)=u e^{1-u}\) for \(u\ge0\).

**Uniform all-pair theorem.** As odd \(p\to\infty\), *uniformly over every larger odd prime \(q>p\), with no bound on \(q/p\)*,
\[
\boxed{\quad D_{p,q}=
\frac{p^{-2}-q^{-2}}{e\log p}\,[1+o(1)] .\quad}
\tag{2}
\]
Moreover, uniformly over the same entire set of pairs,
\[
\boxed{\quad
\sup_{a>0}\left|
\frac{\Phi_q(a)-\Phi_p(a)}{D_{p,q}}
-f(ca\log p)
\right|\longrightarrow0.\quad}
\tag{3}
\]
In particular, the single source-natural observation location
\[
a_p^\star=\frac{e^{-B_1}}{\log p}
\tag{4}
\]
attains a \(1-o(1)\) fraction of the *optimal pairwise separation simultaneously for every \(q>p\)*. Every exact maximizing parameter, and every sequence with achieved separation \(D_{p,q}(1-o(1))\), satisfies
\[
a_{p,q}\log p\longrightarrow e^{-B_1}
\quad\text{uniformly over }q>p.
\tag{5}
\]
The term \(p^{-2}-q^{-2}\), not \(2(q-p)/p^3\), remains valid when \(q/p\) does not tend to one. Formulae (2)--(3) extend AF-557's nearby-prime regime without subtracting two nonuniform AF-555 approximations.

## Exact source difference and a gap-relative estimate

As in AF-557, write \(r_t(s)=Q_t^{-1}(P(s))<s\), so that
\(\Phi_t(a)=r_t(\Phi(a))\), and set \(k_{p,q}=h_p-h_q\). Continuous interpolation in the *generator position* yields
\[
k_{p,q}(s)=s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv>0.
\tag{6}
\]
The positivity proves the ordering of \(Q_t\) and the critical curves. Applying the mean-value theorem to the **same** \(Q_p\) between \(r_p(s)\) and \(r_q(s)\) gives, for
\(\xi_{p,q,s}\in(r_p(s),r_q(s))\),
\[
r_q(s)-r_p(s)=
\frac{k_{p,q}(r_q(s))}{-Q_p'(\xi_{p,q,s})}.
\tag{7}
\]
This exact cancellation is essential: the separate inverse perturbations have errors potentially larger than their small difference when \(q-p\) is small.

For \(s=1+x\), \(0\le x\le\delta\), with any fixed small \(\delta>0\), the inner integral in (6) differs from \(v^{-s-2}\) by relative \(O_\delta(1/p)\), *independently of the upper endpoint \(q\)*. Therefore
\[
k_{p,q}(1+x)
=(1+x)\big(p^{-2-x}-q^{-2-x}\big)
[1+O_\delta(p^{-1})].
\tag{8}
\]
Write \(b=\log(q/p)>0\). Then the crucial relative-gap comparison is the exact inequality
\[
1\le
\frac{p^{-2-x}-q^{-2-x}}
{B_{p,q}e^{-Lx}}
=\frac{1-e^{-(2+x)b}}{1-e^{-2b}}
\le 1+\frac{x}{2}.
\tag{9}
\]
Indeed, the excess over one is
\[
\frac{e^{-2b}(1-e^{-xb})}{1-e^{-2b}}
\le\frac{xb}{e^{2b}-1}\le\frac{x}{2}.
\]
Unlike an absolute-error subtraction of \(p^{-2-x}\) and \(q^{-2-x}\), (9) remains informative when \(q-p\) is minimal. Combining (8)--(9),
\[
\boxed{\quad
k_{p,q}(1+x)
=B_{p,q}e^{-Lx}[1+O_\delta(x+p^{-1})],
\qquad 0\le x\le\delta,
\quad}
\tag{10}
\]
with constants uniform in *all* \(q>p\).

For global tail control, (6) and \(u\ge p\) show that, for every \(x\ge0\),
\[
k_{p,q}(1+x)
\le\frac{(1+x)(2+x)}2 e^{-Lx}\,k_{p,q}(1).
\tag{11}
\]
The same integral comparison at \(s=1\) gives
\(k_{p,q}(1)=B_{p,q}[1+O(p^{-1})]\), uniformly over \(q>p\). Equations (10)--(11) are the missing global, **gap-relative** estimates: their relative errors do not grow like \(p/(q-p)\) when the two edit positions are close.

## Critical inverse layer, maximizing window, and full normalized profile

The prime-zeta boundary expansion recorded in AF-552 and used in AF-555 is
\[
-P'(1+x)=x^{-1}+O(1)\quad(x\downarrow0).
\tag{12}
\]
It follows from (10)--(12) that, uniformly in \(q>p\) and \(0<x\le\delta\),
\[
\frac{k_{p,q}(1+x)}{-P'(1+x)}
=B_{p,q}\,x e^{-Lx}[1+O_\delta(x+p^{-1})].
\tag{13}
\]
For \(L^{-1/2}\le x\le\delta\), the right side is \(o(B_{p,q}/L)\). For \(x\ge\delta\), (11) together with
\(-P'(1+x)\ge(\log2)\,2^{-1-x}\)
gives
\[
\frac{k_{p,q}(1+x)}{-P'(1+x)}
=O_\delta(B_{p,q}p^{-\delta})
=o(B_{p,q}/L).
\tag{14}
\]
Here the polynomial factor \((1+x)(2+x)\) is dominated by \((2/p)^x\), uniformly over the unbounded upper tail. Thus the scaled *linearized* response has the universal global profile \(u e^{-u}\), where \(u=Lx\), including both tails.

It remains to justify the inverse rather than silently linearize it. AF-555 proves
\[
\epsilon_p:=\sup_{s>1}\frac{|h_p'(s)|}{-P'(s)}
=O(L/p^2)=o(1),\qquad
0<s-r_t(s)\le D_t=O((t^2\log t)^{-1}).
\tag{15}
\]
Also \(P''>0\), so \(-P'\) decreases. Differentiating the positive integral (6) gives
\[
\left|\frac{d}{ds}\log k_{p,q}(s)\right|
\le\log(q+1)+2,\qquad s\ge1.
\]
Consequently
\[
\sup_{s>1}\left|
\frac{k_{p,q}(r_q(s))}{k_{p,q}(s)}-1\right|
\le e^{[\log(q+1)+2]D_q}-1=o(1)
\tag{16}
\]
**uniformly over \(q>p\)**: the exponent is \(O(q^{-2})\). With
\(-Q_p'(\xi)\ge(1-\epsilon_p)(-P'(s))\) in (7), we have the global one-sided bound
\[
0<r_q(s)-r_p(s)
\le [1+o(1)]\,\frac{k_{p,q}(s)}{-P'(s)}
\tag{17}
\]
uniformly in \(s>1\) and \(q>p\).

For \(s=1+u/L\), \(u\) in a fixed compact subset of \((0,\infty)\), both inverse displacements in (15) are \(O(p^{-2}/L)=o(1/L)\). Therefore \(\xi_{p,q,s}-1=(u/L)(1+o(1))\), and (12), (15)--(16) also give
\(-Q_p'(\xi_{p,q,s})/[-P'(s)]\to1\) uniformly. The exact identity (7) yields
\[
\frac{L}{B_{p,q}}
\big[r_q(1+u/L)-r_p(1+u/L)\big]
\longrightarrow ue^{-u}
\tag{18}
\]
locally uniformly in \(u>0\) **and uniformly in all \(q>p\)**. Its global majorant (17) and the two tails (13)--(14) promote (18) to
\[
\sup_{x>0}\left|
\frac{L}{B_{p,q}}[r_q(1+x)-r_p(1+x)]
-(Lx)e^{-Lx}
\right|\longrightarrow0
\tag{19}
\]
uniformly over \(q>p\). The comparison tends to zero as \(s\downarrow1\) and \(s\to\infty\) for each fixed pair (use (17) and the endpoint estimates), so its maximum is attained. Since \(ue^{-u}\) has unique maximum \(1/e\) at \(u=1\), (19) proves (2), and every asymptotically maximizing pair has \(L(s-1)\to1\), uniformly.

Finally \(E_1(a)=P(1+x)\) and the two standard boundary expansions
\[
E_1(a)=-\gamma-\log a+O(a),\qquad
P(1+x)=-\log x+(B_1-\gamma)+O(x)
\]
imply \(a=e^{-B_1}x[1+O(x)]\) as \(x\downarrow0\). Transporting (19) through the increasing critical-coordinate map \(s=\Phi(a)\), with a compact core and the two controlled tails, proves (3)--(5). This transport uses the **common** \(a\)-registration supplied by AF-554 and does not allow independent horizontal source warps.

## Consequences, prior art, and falsification boundaries

If \(q/p\to1\), then
\(B_{p,q}\sim2(q-p)/p^3\), recovering AF-557 exactly. If \(q/p\to\lambda>1\), then
\(D_{p,q}\sim(1-\lambda^{-2})/(e p^2\log p)\). If \(q/p\to\infty\), the separation tends to the AF-555 baseline detection scale \(D_p\sim1/(e p^2\log p)\). In **all** three regimes, and in arbitrary mixtures of them, the smaller edit position fixes the same optimal moving window.

For the deterministic full-curve observation model with a common additive \(L^\infty\)-noise bound \(\varepsilon\), the two-source balls centered at \(\Phi_p,\Phi_q\) are disjoint precisely when \(2\varepsilon<D_{p,q}\). Thus their sharp pairwise identification radius is
\[
\varepsilon_{\rm id}(p,q)
=\frac{p^{-2}-q^{-2}}{2e\log p}[1+o(1)]
\tag{20}
\]
uniformly in \(q>p\). This is **not** a uniform decoder for an unknown edit position and does not turn AF-556's finite-sample *detection coverage* into multiway identification.

The classical ingredients are the prime-zeta/Mertens boundary law (Mertens 1874, Fröberg 1968, and the recent expansion cited under AF-552), ordinary mean-value and Laplace-type estimates, and close-node inverse conditioning (Katz, Diab, and Batenkov, *Applied and Computational Harmonic Analysis* 73 (2024), 101687, DOI: 10.1016/j.acha.2024.101687; cited under AF-557). No general inverse-problem novelty is claimed. The line-specific contribution is the source-difference comparison (9)--(11), which closes AF-557's gap-relative asymptotic **uniformly over every larger edited prime** and proves that one peak location works simultaneously across those alternatives.

Decisive independent audits are to: (i) differentiate \(h_v(s)\) and check the sign/factor \(s(s+1)\) in (6); (ii) verify the ratio (9) without assuming \(q/p\to1\), especially for \(q-p=2\) and \(q/p\to\infty\); (iii) check that (16) uses \(D_q\), not a loose \(D_p\log q\), when \(q\) is very large; (iv) verify the denominator replacement only on the compact positive \(u\)-core, with tails controlled one-sidedly; (v) keep the two limits in order—form each fixed-source critical-index limit before letting the edit positions grow. No uniform finite-index approximation is established when \(p,q\) move jointly with the tail index.

Neither the calibrated critical-curve metric, these generalized-prime controls, nor the pairwise noise threshold proves RH, excludes any off-critical zero, or shows that an RH-facing downstream operation preserves this small source difference. The structural lesson is an exact-to-stable fidelity distinction: a complete nonlinear quotient can retain all edit locations while their worst-case pairwise margins vanish, and even unrestricted separation of the alternatives uses a shrinking critical-parameter window.