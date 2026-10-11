# ANF-187 — Critical high-pass danger forces a semicircle-prefix prime–rough contrast

**Status:** EXACT-DERIVED + CLASSICAL-FOURIER-IDENTITY + SOURCE-PLACEMENT-REDUCTION + MATCHED-CONTROL + STRICTLY-STRONGER-SUFFICIENT-TEST. ANF-185 reduces the fixed-base critical-aperture detector to a weighted complex residual at one distinguished height, and ANF-186 shows that prime/rough one-point marginals do not control that residual. A further exact reduction produces a real, unweighted, one-bit witness: every target-sized critical high-pass forces a target-sized discrepancy on one physical prefix, partitioned by a semicircle of the *exact logarithmic carrier*. Conversely, an absolute small-discrepancy theorem for **all** such prefixes and semicircles would control the critical high-pass. The implication is deliberately one-sided; the real discrepancy criterion is stronger than the high-pass bound, not equivalent to it.

## 1. Semicircle-prefix domination for arbitrary real coefficients

Let \(K\ge0\), \(c_j\in\mathbb R\), \(\theta_j\in\mathbb R/(2\pi\mathbb Z)\), and \(w_j\in\mathbb R\) for \(0\le j\le K\). Define the binary semicircle contrast (with \(\operatorname{sgn}(0)=0\))

\[
\chi_\psi(\theta):=\operatorname{sgn}\cos(\theta-\psi),\qquad
\Delta(c,\theta;K):=
\sup_{\substack{0\le M\le K\\ \psi\in\mathbb R}}
\left|\sum_{j=0}^{M}c_j\chi_\psi(\theta_j)\right|.
\tag{1}
\]

For every fixed \(\theta\), a direct integral over the two half-circles gives

\[
\int_0^{2\pi}\chi_\psi(\theta)e^{-i\psi}\,d\psi
=4e^{-i\theta}.
\tag{2}
\]

The finitely many semicircle boundary orientations do not affect this identity. Setting \(F_M=\sum_{j=0}^{M}c_je^{-i\theta_j}\), multiplying (2) by each real \(c_j\), and summing yields

\[
F_M
=\frac14\int_0^{2\pi}
\left(\sum_{j=0}^{M}c_j\chi_\psi(\theta_j)\right)
e^{-i\psi}\,d\psi,
\qquad
|F_M|\le\frac{\pi}{2}\Delta(c,\theta;K).
\tag{3}
\]

Abel summation, with no assumption on the monotonicity or sign of \(w_j\), reads

\[
\sum_{j=0}^{K}c_jw_je^{-i\theta_j}
=w_KF_K+\sum_{M=0}^{K-1}(w_M-w_{M+1})F_M.
\tag{4}
\]

Consequently, for the discrete variation \(V_K(w):=|w_K|+\sum_{M=0}^{K-1}|w_{M+1}-w_M|\),

\[
\boxed{\left|\sum_{j=0}^{K}c_jw_je^{-i\theta_j}\right|
\le\frac{\pi}{2}\,V_K(w)\,\Delta(c,\theta;K).}
\tag{5}
\]

This is an elementary Fourier identity plus Abel summation; no prime or zeta theorem is being imported into (5).

## 2. Apply the lemma at ANF-185's deterministic critical aperture

Use the bow parameters of ANF-175 and ANF-185: \(0<\varepsilon<1/16\) fixed, \(K=X^{1-2\varepsilon+o(1)}=o(X)\), \(A_0X^2\le U\le B_0X^2\), fixed \(\delta>0\), and

\[
a_X:=\sqrt{\delta X\log X},\quad
\theta_j:=U\log(1+j/X)\pmod{2\pi},
\quad
T:=CX/a_X.
\tag{6}
\]

The exact high-pass of ANF-185 is

\[
\mathcal D_T(c;U)
=\sum_{j=0}^{K}c_je^{-i\theta_j}w_j,\qquad
w_j:=W(T\log(1+j/X)),\quad
W(y):=1-\operatorname{sinc}^2(y/2).
\tag{7}
\]

Here \(W(0)=0\), \(0\le W\le1\), and ANF-185 proves
\(\int_0^\infty|W'(y)|\,dy<\infty\). Since \(j\mapsto T\log(1+j/X)\) is increasing,

\[
V_K(w)\le1+\int_0^\infty|W'(y)|\,dy=:C_W<\infty,
\tag{8}
\]

uniformly in \(X,U,K,T\). Thus (5) yields the source-independent exact implication

\[
\boxed{
|\mathcal D_T(c;U)|
\le \frac{\pi C_W}{2}\,
\sup_{\substack{M\le K\\\psi\in\mathbb R}}
\left|\sum_{j\le M}c_j
\operatorname{sgn}\cos\!\left(U\log(1+j/X)-\psi\right)\right|.
}
\tag{9}
\]

In particular, if the left side is at least \(\eta a_X\), there must be a **single** physical prefix \(M\) and angular orientation \(\psi\) whose *real* contrast is at least \(2\eta a_X/(\pi C_W)\). This witness uses one bit of phase information at each site and no radial smoothing.

For the actual source \(r_X=\vartheta-Q_R\) from ANF-149/ANF-186, the sufficient source-side target is now

\[
\boxed{
\sup_{\substack{M\le K\\\psi\in\mathbb R}}
\left|
\sum_{j\le M}(\vartheta-Q_R)(X+j)
\operatorname{sgn}\cos\!\left(U\log(1+j/X)-\psi\right)
\right|=o(a_X).
}
\tag{10}
\]

If (10) holds uniformly in the bow parameters required downstream, it forces \(\mathcal D_{CX/a_X}(r_X;U)=o(a_X)\), the deterministic source gate isolated by ANF-185. In the opposite direction, a large high-pass *necessarily* makes (10) fail; a large semicircle contrast does not necessarily make the high-pass large.

The prime-power reduction is harmless at this absolute scale. The uniform prime-power counting bound in ANF-149 (equation (6)) and \(|\chi_\psi|\le1\) give

\[
\Delta(\Lambda-\vartheta,\theta;K)
\ll \log X\left(K/\sqrt X+\log X\right)
=o(a_X)
\tag{11}
\]

for \(K=X^{1-2\varepsilon+o(1)}\) and fixed \(\varepsilon>0\). Thus (10) is equivalent, up to \(o(a_X)\), to the same proposed criterion with \(\Lambda-Q_R\).

## 3. ANF-186 saturates precisely this scalar carrier-placement statistic

In the matched two-sign control of ANF-186, positive coefficients \(+A_X+o(1)\) are placed where \(e^{-i\theta_j}\) belongs to an arc of width \(\pi/3\) about \(+1\), and negative coefficients \(-B_X\) where it belongs to the opposite arc. At orientation \(\psi=0\), these selected sites satisfy

\[
c_j\chi_0(\theta_j)=|c_j|
\tag{12}
\]

for both signs. All nonzero sites lie in the loading prefix \(M=L_X\asymp a_X\), and ANF-186 proves that their total absolute mass is \((2+o(1))L_X\), with \(L_X=a_X\) in its construction. Therefore

\[
\Delta(c,\theta;K)\ge(2+o(1))a_X.
\tag{13}
\]

The source-alphabet, one-point sign densities, zero mean, correct diagonal second moment, and local mass envelope already built into that control do not prevent this one-bit contrast from being critical. Their missing feature is still actual arithmetic *placement* relative to the log carrier, not a scalar marginal.

## 4. Falsification boundary: the sufficient contrast is not equivalent to the high-pass

The logical asymmetry matters. Let six phases be \(\theta_k=k\pi/3\), \(0\le k<6\), with real coefficients \(c_k=(-1)^k\). Then

\[
\sum_{k=0}^{5}c_k=0,\qquad
\sum_{k=0}^{5}c_ke^{-i\theta_k}=0,\qquad
\sum_{k=0}^{5}c_k\chi_0(\theta_k)=-2.
\tag{14}
\]

Repeat this six-atom block \(B\) times, always in the same order. All complex prefix sums remain \(O(1)\), so (4) bounds the weighted first Fourier coefficient by \(O(V_K(w))\); but the final real semicircle contrast is \(-2B\). This is an abstract phase control, **not** a configuration asserted to occur on the physical logarithmic carrier. It proves that the stronger all-prefix, all-orientation condition (10) may fail for reasons invisible to the first harmonic. No converse to (9) is being claimed.

In particular, (10) should not be mislabeled as an equivalent RH criterion or as a theorem already available from source marginals. It is a sufficient arithmetic route to the ANF-185 high-pass gate and an unavoidable one-bit *witness* for any dangerous high-pass, but it can have false positives.

## 5. Prior art and consequence

Identity (2) is the classical first Fourier coefficient of a square wave, and (4) is standard partial summation. The broader signed-measure/bounded-variation discrepancy framework is classical; a primary reference is C. Aistleitner and J. Dick, *Functions of bounded variation, signed measures, and a general Koksma–Hlawka inequality*, Acta Arith. 167 (2015), 143–171, DOI 10.4064/aa167-2-4. This source is a prior-art boundary, not a theorem needed to establish (2)–(9).

Short-interval prime-phase discorrelation is a different and much harder input: K. Matomäki and X. Shao, *Discorrelation Between Primes in Short Intervals and Polynomial Phases*, IMRN 2021 (16), 12330–12355, DOI 10.1093/imrn/rnz188, treats polynomial prime phases for \(H\ge N^\theta\) with \(\theta>2/3\). The all-interval \(\Lambda-\Lambda^\sharp\) nilsequence estimate at \(H\ge X^{5/8+\eta}\) already recorded in SOURCES.md and ANF-164 remains relative to \(H\), and by itself does not give absolute \(o(\sqrt{X\log X})\) carrier-sector discrepancy at the critical physical scale. Neither paper is invoked as an estimate establishing (10).

The line-specific contribution is the composition of this classical one-bit Fourier duality with ANF-185's *fixed-base, critical-aperture, distinguished-height* high-pass and ANF-186's prime/rough matched control. The unknown arithmetic statement can now be posed as a real prefix-by-semicircle prime-minus-rough placement law. This neither proves the bow variance theorem nor resolves RH: a proof of (10), or a genuinely different signed Fejér-slope argument, is still missing.
