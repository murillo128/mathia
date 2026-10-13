# AF-562 — Multiway prime-edit identification: one-sample locality and a sharp two-scale obstruction

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · MULTIWAY-IDENTIFICATION · PRIME-TAIL · NONADAPTIVE-SAMPLING · MINIMAX-NOISE · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Exact experiment and adjacent-pair reduction

Work with AF-554's common-output-calibration-invariant critical coordinate and AF-559's prime-edit controls:
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad E_1(a)=\int_a^\infty e^{-v}\frac{dv}{v},\quad
\Phi_p(a)=Q_p^{-1}(E_1(a)),\quad
Q_p(s)=P(s)-[p^{-s}-(p+1)^{-s}].
\tag{1}
\]
Each odd prime \(p\) is a genuine rational-prime *edit location*; the corresponding order-preserving modified generator system is a generalized-prime control, not another rational-prime sequence. For \(p<q\), AF-559 proves strict pointwise ordering \(\Phi_p<\Phi_q\). Write
\[
G_{p,q}(a)=\Phi_q(a)-\Phi_p(a)>0,\quad
D_{p,q}=\sup_{a>0}G_{p,q}(a),\quad
c=e^{B_1},\quad f(u)=u e^{1-u},
\tag{2}
\]
where \(B_1\) is the Meissel--Mertens prime-reciprocal constant.

Let \(S=\{p_1<\cdots<p_m\}\) be a finite set of at least two odd-prime edit locations. A single unknown \(p\in S\) is observed at a predetermined parameter set \(A\subset(0,\infty)\) with additive adversarial error bounded by \(\varepsilon\) in \(L^\infty(A)\). The *supremal worst-case unique-decoding radius* is
\[
\varepsilon(A,S)=\frac12\min_{p\ne q\in S}
  \|\Phi_p-\Phi_q\|_{L^\infty(A)}.
\tag{3}
\]
The two noise balls overlap exactly at \(2\varepsilon\ge\|\Phi_p-\Phi_q\|_\infty\) (midpoint witness); thus equality is a tie, not guaranteed unique decoding. Define \(\varepsilon_k(S)=\sup_{|A|\le k}\varepsilon(A,S)\) and \(\varepsilon_{\rm full}(S)=\varepsilon((0,\infty),S)\).

Because a nonadjacent curve difference is the sum of *positive* adjacent differences, its sup norm is at least the sup norm of each constituent gap. Hence, exactly,
\[
\begin{aligned}
2\varepsilon_{\rm full}(S)&=\min_{1\le i<m}D_{p_i,p_{i+1}},\\
2\varepsilon_1(S)&=\sup_{a>0}\min_{1\le i<m}G_{p_i,p_{i+1}}(a),\\
2\varepsilon_k(S)&=\sup_{a_1,\ldots,a_k>0}\min_{1\le i<m}
                    \max_{1\le j\le k}G_{p_i,p_{i+1}}(a_j).
\end{aligned}
\tag{4}
\]
This is a deterministic *absolute noise* criterion, distinct from AF-556's normalized detection coverage.

## Theorem A: logarithmically localized sources need only one sample

Let \(S_n\) be any finite sets of at least two odd primes satisfying
\[
P_n=\min S_n\to\infty,\qquad
\log(\max S_n)/\log P_n\to1.
\tag{5}
\]
No bound on \(|S_n|\) is required. The common single sample \(a_n=c^{-1}/\log P_n\) obeys
\[
\boxed{\frac{\varepsilon(\{a_n\},S_n)}
{\varepsilon_{\rm full}(S_n)}\to1,
\qquad
\frac{\varepsilon_1(S_n)}
{\varepsilon_{\rm full}(S_n)}\to1.}
\tag{6}
\]

**Proof.** The *globally and all-pair uniform* result AF-559 states
\[
D_{p,q}=\frac{p^{-2}-q^{-2}}{e\log p}[1+o(1)],\qquad
\sup_{a>0}\left|\frac{G_{p,q}(a)}{D_{p,q}}-f(ca\log p)\right|=o(1)
\tag{7}
\]
uniformly over all odd primes \(q>p\) as \(p\to\infty\). At \(a_n\), every adjacent pair has argument \(ca_n\log p_i=\log p_i/\log P_n=1+o(1)\), uniformly even when the number of candidates grows. Since \(f(1)=1\), every adjacent gap simultaneously reaches \((1-o(1))\) of its own maximum. Formula (4) and \(\varepsilon_1\le\varepsilon_{\rm full}\) give (6). \(\square\)

## Theorem B: four prime locations can force a strict one-sample penalty

There exists a sequence of sets \(S_n\) of exactly four odd rational primes for which
\[
\boxed{\frac{\varepsilon_1(S_n)}{\varepsilon_{\rm full}(S_n)}
\longrightarrow \rho=\frac{8e}{9}\log\frac32
=0.9797052759\ldots<1,\qquad
\frac{\varepsilon_2(S_n)}{\varepsilon_{\rm full}(S_n)}
\longrightarrow1.}
\tag{8}
\]
The constant is the *sharp ratio for this family*, not a claimed universal loss lower bound.

**Construction with only PNT.** There exist arbitrarily large *consecutive* odd primes \(p<r\) with \(g=r-p=O(\log p)\). Indeed, PNT gives \(\asymp X/\log X\) primes in \([X,2X]\), while their consecutive interior gaps sum to at most \(X\); at least one gap is \(O(\log X)\). Thus \(2\le g\le C\log p\) on an infinite sequence. Set
\[
Q=\frac{p^{3/2}}{2\sqrt g}.
\tag{9}
\]
Then \(Q/p\to\infty\) and \(\log Q/\log p\to3/2\). Ordinary PNT also provides actual odd primes \(q\sim Q\) and \(t\sim2Q\); eventually \(S=\{p,r,q,t\}\) is strictly ordered.

With
\[
d=\frac{2g}{e p^3\log p},
\tag{10}
\]
the uniform pairwise formula (7) gives
\[
D_{p,r}\sim d,\qquad
D_{q,t}\sim
\frac{3/(4Q^2)}{e\log Q}\sim d,\qquad
D_{r,q}\sim\frac{1}{e p^2\log p}\gg d.
\tag{11}
\]
Indeed \(Q^2=p^3/(4g)\) and \(\log Q/\log p\to3/2\), so the second numerator equals \(3g/p^3\), giving the same \(d\). The two *outer* adjacent pairs are therefore the sole full-curve bottlenecks, and \(2\varepsilon_{\rm full}(S)\sim d\).

**Exact maximin limit.** Put \(x=ca\log p\) and \(\lambda_p=\log q/\log p\to3/2\). Applying (7) to the two bottleneck pairs yields *uniformly over all \(x>0\)*,
\[
G_{p,r}(a)/d=f(x)+o(1),\qquad
G_{q,t}(a)/d=f(\lambda_px)+o(1).
\tag{12}
\]
Moreover \(\sup_{x>0}|f(\lambda_px)-f(3x/2)|\to0\): use continuity on compact \(x\)-intervals and the common decay at both endpoints. Dropping the middle gap gives the upper bound
\[
\limsup 2\varepsilon_1(S)/d
\le\sup_{x>0}\min\{f(x),f(3x/2)\}.
\tag{13}
\]
The nonzero crossing is \(x_0=2\log(3/2)\), because \(f(x_0)=f(3x_0/2)\). Since \(x_0<1<(3/2)x_0\) and \(f\) increases until \(1\) and decreases thereafter, the maximum of the lower envelope is uniquely at \(x_0\), with value
\[
f(x_0)=2\log(3/2)\,e^{1-2\log(3/2)}
=\frac{8e}{9}\log(3/2)=\rho.
\tag{14}
\]
At \(a=x_0/(c\log p)\), (7) for the middle pair shows \(G_{r,q}(a)/D_{r,q}\to f(x_0)>0\), while \(D_{r,q}/d\to\infty\). The omitted gap is thus not limiting at the crossing, so (13) is attained asymptotically. This proves the first ratio in (8).

**Two-sample recovery.** Take the nonadaptive pair
\[
A_2=\left\{\frac1{c\log p},\frac1{c\log q}\right\}.
\tag{15}
\]
The first coordinate captures the \((p,r)\) gap at \(d[1+o(1)]\), the second captures the \((q,t)\) gap at \(d[1+o(1)]\), and the middle pair already separates by \(\gg d\) at the first coordinate. Equations (4) and (11) yield \(2\varepsilon(A_2,S)\sim d\sim2\varepsilon_{\rm full}(S)\), proving the second ratio. \(\square\)

## Prior-art check, stress tests and boundaries

Atkinson and Fedorov (1975) established model-discriminating and several-model optimal experimental design, and Braess--Dette (2013) studied several-model discriminating designs. This is genuine prior art for competing-model design, but their standard \(T\)-type average-design criteria are not identified with the deterministic \(L^\infty\)-ball intersection criterion (3). PNT, nearest-neighbor reduction for ordered curves, and maximin peak balancing are classical elementary ingredients. The source-specific new implication is the application of AF-559's uniform rational-prime-edit response to establish (6) and construct the actual-prime two-scale example (8).

The result does **not** use unproved twin-prime or bounded-gap conjectures, primes in intervals of prescribed power length, or a simultaneous finite-index limit. The edits remain generalized-prime controls even though their locations \(p,r,q,t\) are rational primes. Two samples recover the *existing* full-curve absolute margin, but the margin still tends to zero like \(g/(p^3\log p)\); the result is not uniform recovery at fixed noise. The common critical coordinate and additive observation-noise norm are assumed; independently warped or unknown-calibration sample coordinates change the problem. No RH consequence is asserted.

Decisive independent audits: check (3) at equality and derive adjacent-pair formula (4); inspect the *all-pair and all-parameter* quantifiers of AF-559 before using them for growing \(S_n\); verify the PNT average-gap argument, \(Q^2=p^3/(4g)\), \(\log Q/\log p\to3/2\), and each normalization in (11); check uniform control of the two \(f\)-tails in (12); and confirm the middle adjacent gap is never the limiting pair at the proposed crossing and two sample points.

## Consequence for Arithmetic Fidelity

AF-559's simultaneous optimum for *each pair with a fixed smaller prime* does not imply one sample is optimal for an unknown source selected across arbitrary logarithmic scales. The new exact distinction is that logarithmic localization guarantees one-sample asymptotic sufficiency regardless of candidate count, whereas two separated scales can produce a provable \(\sim2.03\%\) one-sample identification-margin loss with only four candidate sources. Two sample coordinates recover the full-curve margin for that family. AF-556's detection-coverage cost and the present multiway identification cost are different observation resources; any transfer to RH needs a separately faithful and stable arithmetic-to-zeros bridge.
