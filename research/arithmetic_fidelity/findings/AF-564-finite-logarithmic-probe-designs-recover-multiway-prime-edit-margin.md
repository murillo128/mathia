# AF-564 — Finite logarithmic probe designs recover nearly the full multiway prime-edit margin

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · MULTIWAY-IDENTIFICATION · NONADAPTIVE-SAMPLING · UNIFORM-IN-CANDIDATE-COUNT · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: an arbitrary relative precision is attained with a bounded probe budget

Use exactly the commonly registered critical curves, prime-edit controls, and deterministic additive \(L^\infty\)-noise experiment of AF-559, AF-562, and AF-563. For any finite ordered set \(S=\{p_1<\cdots<p_m\}\) of at least two odd rational-prime *edit locations*, put
\[
G_i(a)=\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)>0,\quad
D_i=\sup_{a>0}G_i(a),\quad
d=d(S)=\min_{i<m}D_i=2\varepsilon_{\rm full}(S),\quad
H=\log(1/d).
\tag{1}
\]
The modified sources themselves are marked generalized-prime controls, not alternative rational-prime sequences. AF-562's exact ordered-curve reduction says
\[
2\varepsilon(A,S)=\min_{i<m}\max_{a\in A}G_i(a)
\tag{2}
\]
for a finite nonadaptive sampling set \(A\).

For an integer \(k\ge1\), define
\[
r_k=(3/2)^{1/k},\qquad
u_k=\frac{\log r_k}{r_k-1},\qquad
\vartheta_k=u_k\exp(1-u_k),
\tag{3}
\]
and, writing \(c=e^{B_1}\) for the fixed prime-zeta boundary registration,
\[
\boxed{\quad A_k(S)=
\left\{\frac{3u_k}{cH\,r_k^j}: j=0,1,\ldots,k-1\right\}.\quad}
\tag{4}
\]

**Uniform finite-probe theorem.** There is a single error function \(\delta(P)\to0\) as \(P\to\infty\) such that, for **every** finite \(S\) with \(\min S\ge P\) and **every** integer \(k\ge1\),
\[
\boxed{\qquad
\frac{\varepsilon(A_k(S),S)}{\varepsilon_{\rm full}(S)}
\ge\vartheta_k-\delta(P).
\qquad}
\tag{5}
\]
Here \(S\) and \(k\) may both vary with \(P\) without cardinality or scale-diameter restrictions. In particular,
\[
\vartheta_1=\frac{8e}{9}\log(3/2)=0.9797052759\ldots,\qquad
\vartheta_2=0.9948785286\ldots,
\tag{6}
\]
and, as \(k\to\infty\),
\[
\boxed{\qquad
\vartheta_k
=1-\frac{\log^2(3/2)}{8k^2}+O(k^{-4}).
\qquad}
\tag{7}
\]
Thus, for any prescribed relative loss \(\eta>0\), a **fixed** number \(k=k(\eta)\) of predetermined samples, independent of the number and range of candidate primes, achieves at least \(1-\eta-o(1)\) of the complete-curve minimax identification margin. For any sequence \(k=k(S)\to\infty\), however slowly,
\[
\frac{\varepsilon(A_{k(S)}(S),S)}
{\varepsilon_{\rm full}(S)}\longrightarrow1.
\tag{8}
\]
The sampling locations depend on the *known candidate set* through the theoretical full-curve margin \(d(S)\), not on the unknown realized edited prime or an observed noisy curve.

## Uniform reduction to a compact multiplicative scale interval

Write \(B_i=p_i^{-2}-p_{i+1}^{-2}\), \(L_i=\log p_i\), and \(t_i=L_i/H\). AF-559's all-pair estimate and AF-563's multiplicative, small-boundary-parameter estimate supply, uniformly over all adjacent pairs,
\[
D_i=\frac{B_i}{eL_i}[1+o(1)],\qquad
\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)
=B_i x e^{-L_i x}[1+O(x+p_i^{-1})],
\quad x=\Phi(a)-1\downarrow0.
\tag{9}
\]
The latter is *relative* even when \(L_ix\) tends to zero; the weaker additive convergence of normalized response profiles would not suffice below the scale interval.

Since \(d\le D_i\le(1+o(1))p_i^{-2}/(eL_i)\), uniformly in \(i\),
\[
2L_i+\log L_i\le H+O(1),\qquad
0<t_i\le\tfrac12+o(1),\qquad H\to\infty.
\tag{10}
\]
Put \(v_j=3u_k r_k^{-j}\). Elementary bounds from (3) give
\[
2\le v_j\le3 \quad(0\le j<k,\;k\ge1).
\tag{11}
\]
The common boundary registration \(a=c^{-1}x[1+O(x)]\) implies that at the probe \(a_j=v_j/(cH)\),
\[
x_j=\Phi(a_j)-1=\frac{v_j}{H}[1+O(H^{-1})].
\]
Because \(L_i/H\le1/2+o(1)\) and \(v_j\in[2,3]\), (9) now gives **uniformly in \(i,j,S,k\)**,
\[
G_i(a_j)=\frac{B_iv_j}{H}e^{-v_jt_i}[1+o(1)],
\qquad
\frac{G_i(a_j)}{d}
\ge[1-o(1)]\,f(v_jt_i),
\quad f(u)=ue^{1-u}.
\tag{12}
\]

The apparent problem is that \(t_i\) may lie well below \(1/3\), where \(f(v_jt_i)\) is small. This cannot create a bottleneck because distinct odd prime edit locations satisfy \(p_{i+1}\ge p_i+2\), hence
\[
B_i\ge p_i^{-2}-(p_i+2)^{-2}
=(4+O(p_i^{-1}))p_i^{-3}.
\tag{13}
\]
Equations (12)--(13) and \(d=e^{-H}\) yield, at **every** chosen probe,
\[
\frac{G_i(a_j)}d
\ge \frac{(4-o(1))v_j}{H}
\exp\{H-3L_i-v_jt_i\}.
\tag{14}
\]
Choose a shrinking buffer \(\eta_H=H^{-1/2}\). If \(t_i\le1/3-\eta_H\), then \(H-3L_i\ge3\sqrt H\), while (10)--(11) bound \(v_jt_i\). The right-hand side of (14) tends to infinity, uniformly in the number of candidate pairs and in \(k\). **Every pair below this logarithmic scale is harmless in absolute noise units.**

## Exact multiplicative interval covering

The remaining \(t_i\) lie in
\[
[1/3-\eta_H,\;1/2+o(1)].
\tag{15}
\]
On the central interval \([1/3,1/2]\), partition into the multiplicative cells
\[
I_j=[r_k^j/3,\;r_k^{j+1}/3],\qquad j=0,\ldots,k-1.
\tag{16}
\]
If \(t\in I_j\), the corresponding probe obeys
\[
u_k\le v_j t\le r_ku_k.
\tag{17}
\]
The peak \(f(u)=ue^{1-u}\) increases to \(1\) at \(u=1\) and then decreases. The defining identity
\[
f(u_k)=f(r_ku_k)=\vartheta_k
\tag{18}
\]
follows exactly from \((r_k-1)u_k=\log r_k\). Therefore
\[
\min_{1/3\le t\le1/2}\max_{0\le j<k}f(v_jt)
=\vartheta_k.
\tag{19}
\]
For \(t\) in the \(o(1)\) boundary layers of (15), using the nearest endpoint probe and the uniform bounds \(v_j\in[2,3]\) reduces the lower bound by at most \(O(\eta_H)+o(1)\), uniformly in \(k\). Combining (12), (14), (19), and then the exact adjacent-pair formula (2) proves (5), with a single error independent of \(k\) and \(|S|\).

For completeness, the asymptotic expansion (7) follows by setting \(z=\log(3/2)/k\) and writing
\[
u_k=\frac{z}{e^z-1}=1-\frac z2+\frac{z^2}{12}+O(z^4).
\]
The identity \(\vartheta(-z)=\vartheta(z)\), obtained by exchanging \(u_k\) with \(e^z u_k\) in (18), cancels the odd powers; Taylor expansion of \(\log u_k+1-u_k\) gives
\(\log\vartheta_k=-z^2/8+O(z^4)\).
This completes the proof. \(\square\)

## Sharpness of the profile-covering constant and limits of the assertion

Equation (19) is sharp **for the universal continuum-profile covering surrogate**. Indeed, for \(0<\theta<1\), the superlevel set of \(f\) is exactly
\([u_-(\theta),u_+(\theta)]\) with \(0<u_-<1<u_+\). One probe \(v\) covers a multiplicative interval of \(t\)-scales with ratio \(R(\theta)=u_+(\theta)/u_-(\theta)\). Any \(k\) such intervals can cover \([1/3,1/2]\) only if \(R(\theta)^k\ge3/2\): in \(\log t\), the sum of the \(k\) interval lengths must exceed the target length \(\log(3/2)\). The probes in (4) meet equality at \(\theta=\vartheta_k\), proving optimality of this **surrogate coverage**.

This is **not** a proof that \(\vartheta_k\) is the sharp worst-family minimax constant among actual odd-prime sets for every \(k\ge2\). Such an assertion would require constructions with enough simultaneously tight intermediate prime-edit gaps; AF-562 supplies the sharp \(k=1\) example but not those extra source realizations. AF-563 already proves the globally sharp \(k=1\) result. AF-564's mathematical delta is instead the explicit uniform all-\(k\) guarantee, the bounded relative-resolution sampling budget, and its optimal multiplicative-profile grid. The fact that the grid is an elementary covering/equioscillation calculation is not presented as a new general theorem.

## Prior art, stress tests, and arithmetic boundary

The analytic inputs, the close-pair relative-gap estimate, the discrete edit-position spacing floor, and the original two-scale construction are precisely AF-559, AF-562, and AF-563. Classical many-model experimental design is represented by Atkinson--Fedorov (1975, *Biometrika* 62(2), 289--303, DOI: 10.1093/biomet/62.2.289) and Braess--Dette (2013, *Annals of Statistics* 41(2), 897--922; arXiv:1306.1320), already recorded in this line's SOURCES.md. Those works use different model-discrimination criteria; no equivalence to this adversarial \(L^\infty\) margin is assumed. Interval covering on a log scale and equalizing the two endpoints of a unimodal response are classical elementary steps; no general-design novelty is claimed.

The decisive falsification checks are: (i) verify the \(j\)-index in (16)--(17), especially \(k=1\) reducing (4) to AF-563's \(\kappa/H\) sampler; (ii) use the *relative* small-\(x\) estimate of AF-563 in (12), not normalized-profile additive errors; (iii) test pairs with edit gap exactly \(2\), arbitrary far-separated \(q\), and \(t\ll1/3\); (iv) check that the low-scale estimate (14) is uniform in \(k\), since all \(v_j\) stay in \([2,3]\); (v) distinguish optimality of the continuous covering problem from sharp prime-family lower examples for \(k>1\).

The guarantee is about a **relative fraction of a shrinking complete-curve margin**, not stable identification at any fixed positive noise level. Sampling coordinates are shared across sources and prechosen with exact knowledge of \(S\) and \(d(S)\); independently warped source coordinates, unknown registration, finite-index approximations with growing edit locations, and uncertain theoretical margins are outside the result. The gap floor also holds for some non-prime integer edit grids, so the conclusion is not by itself a rational-prime discriminator. Nothing here proves RH or certifies recovery of an RH-sensitive observable through another compression map.
