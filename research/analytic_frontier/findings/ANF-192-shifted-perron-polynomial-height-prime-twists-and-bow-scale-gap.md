# ANF-192 — Shifted Perron controls polynomial-height prime twists but not the bow endpoint scale

**Status:** CONDITIONAL-CLASSICAL-COROLLARY + LITERATURE+DERIVED + UNIFORM-PREFIX-AND-HIGH-PASS-BOUND + QUANTIFIED-SCALE-OBSTRUCTION. The analytic zero-free hypothesis is taken from an external preprint and has **not** been independently verified here.

## 1. Precise conditional claim

Suppose that the Riemann zeta function has no nontrivial zeros in \(\Re s>B\), for one fixed \(1/2\le B<1\). For fixed \(A>0\) and \(\eta>0\), uniformly in real \(U\) and \(x\) satisfying
\[
X\le x\le 3X,\qquad |U|\le X^A,\qquad X\ge 3,
\]
one has
\[
\boxed{\displaystyle
\Psi_U(x):=\sum_{n\le x}\Lambda(n)n^{-iU}
=\frac{x^{1-iU}}{1-iU}+O_{A,B,\eta}(X^{B+\eta}).
}\tag{1}
\]
The endpoint convention for integer \(x\) changes the sum by at most \(O(\log X)\), which is absorbed in (1). The exponent in the error does **not** acquire a factor \(X^A\). Equation (1) follows by shifting the Perron integral for \(-\zeta'/\zeta(s+iU)\), rather than integrating the untwisted prime-number-theorem error by parts.

Consequently, for integers \(0\le m\le K\le X/4\), and uniformly over the same twist range,
\[
\sum_{X<n\le X+m}\Lambda(n)n^{-iU}
=\frac{(X+m)^{1-iU}-X^{1-iU}}{1-iU}
+O_{A,B,\eta}(X^{B+\eta}).\tag{2}
\]
For the actual prime weight \(\vartheta(n)=(\log n)\mathbf1_{\{n\ {\rm prime}\}}\), prime powers contribute \(O(\sqrt X\log^2 X)\) on the full dyadic range and hence (2) remains true with \(\Lambda\) replaced by \(\vartheta\). The bound is simultaneous for all prefixes \(m\), not just for a selected interval.

## 2. Perron shift with a height-uniform error

For \(\Re s>1\), set
\[
F_U(s)=-\frac{\zeta'}{\zeta}(s+iU)
=\sum_{n\ge1}\Lambda(n)n^{-iU}n^{-s}.
\]
Choose \(c=1+1/\log X\) and a truncation height \(H=X^{A+4}\), so \(H\gg |U|+X^3\). Effective Perron summation gives
\[
\Psi_U(x)=\frac1{2\pi i}\int_{c-iH}^{c+iH}
F_U(s)\frac{x^s}{s}\,ds
+O(\log^C X)\tag{3}
\]
with an absolute fixed \(C\), uniformly for \(x\in[X,3X]\). To see the endpoint uniformity, the standard Perron remainder is bounded by
\(\sum_n\Lambda(n)(x/n)^c\min(1,[H|\log(x/n)|]^{-1})\).
Since \(x/H\ll X^{-3}\), at most one integer contributes a near-endpoint \(O(\log X)\) term; the remaining dyadic/harmonic tail is \(O(X\log^C X/H)\). Only \(|\Lambda(n)n^{-iU}|=\Lambda(n)\) is used in this step.

Fix \(0<\delta<\min(\eta/2,(1-B)/2)\) and put \(\sigma_0=B+\delta<1\). The assumed fixed zero-free half-plane and the classical local zero-counting formula imply, away from the pole at \(1\),
\[
\frac{\zeta'}{\zeta}(\sigma+iv)
\ll_{B,\delta}\log^C(|v|+3)
\quad(\sigma\ge B+\delta,\ |v|\ge2),\tag{4}
\]
for an absolute fixed power \(C\). The bounded-height part is handled by an \(O_{B,\delta}(1)\) bound off the pole. One standard proof of (4) uses the partial-fraction/local-zero formula and the fixed horizontal separation \(\delta\) from every nontrivial zero; no extra zero-density or RH hypothesis is used.

Move the contour in (3) to \(\Re s=\sigma_0\), keeping horizontal sides at \(\Im s=\pm H\). The only enclosed singularity of \(F_U(s)\) is the simple pole at \(s=1-iU\), with residue \(+1\); it lies within the rectangle because \(|U|\ll H\). Its contribution is exactly \(x^{1-iU}/(1-iU)\). On the left side, (4) and \(|s|^{-1}\ll(1+|\Im s|)^{-1}\) give
\[
\int_{\sigma_0-iH}^{\sigma_0+iH}
F_U(s)\frac{x^s}{s}\,ds
\ll_{A,B,\delta}X^{B+\delta}(\log X)^{C+1}.\tag{5}
\]
On the horizontal sides, \(U\pm H\asymp H\) and (4) bounds the total contribution by
\[
O_{A,B,\delta}\!\left(X^c(\log X)^C/H\right).\tag{6}
\]
Absorbing powers of \(\log X\) into \(X^{\eta-\delta}\) proves (1). If \(\eta\) is large, use the result for a smaller positive \(\eta\) and weaken the exponent. This establishes uniformity for **any fixed polynomial-height range**, with constants depending on its exponent \(A\). It is a classical contour-shift argument in a translated variable, not a new zeta theorem.

## 3. Distinguished bow twist and all triangular high-passes

Use the Mathia bow regime \(0<\varepsilon<1/16\),
\[
K=X^{1-2\varepsilon+o(1)},\quad
a_X=\sqrt{\Delta X\log X}\ \ (\Delta>0\ {\rm fixed}),\quad
U\asymp X^2.\tag{7}
\]
Since
\[
\left|\frac{(X+m)^{1-iU}-X^{1-iU}}{1-iU}\right|
\le\frac{2(X+K)}{\sqrt{1+U^2}}\ll X^{-1},\tag{8}
\]
equation (2) gives the **uniform prime-prefix bound**
\[
\max_{0\le m\le K}\left|
\sum_{j=0}^{m}\vartheta(X+j)
e^{-iU\log(1+j/X)}\right|
\ll_{\eta}X^{B+\eta}.\tag{9}
\]
Assume \(X\) is an integer for this discrete form; otherwise replace \(X+j\) by the corresponding integer endpoints. The fixed phase \(X^{iU}\) has modulus one.

For the ANF-185 triangular high-pass,
\[
\mathcal D_T(\vartheta;U)=
\sum_{j=0}^{K}\vartheta(X+j)e^{-iU\log(1+j/X)}
W\!\left(T\log(1+j/X)\right),\quad
W(y)=1-\operatorname{sinc}^2(y/2),\tag{10}
\]
ANF-185 proved that the sequence of weights has bounded variation independently of \(T>0\). Abel summation and (9) therefore give
\[
\boxed{\ \sup_{T>0}|\mathcal D_T(\vartheta;U)|
\ll_\eta X^{B+\eta}.\ }\tag{11}
\]
The same applies to reversed prime endpoint blocks after the harmless dyadic change of base.

Now specialize **conditionally** to Liu's October 8, 2026 assertion (ANF-191):
\[
B=B_*=\frac{1507-2\sqrt{921}}{1653}
=0.874957069799\ldots.\tag{12}
\]
Because \(1-2\varepsilon>7/8>B_*\), choose \(0<\eta<1-2\varepsilon-B_*\). Equations (9)–(11) imply \(o(K)\) cancellation for the prime component at every prescribed \(U\asymp X^2\), uniformly over prefixes and triangular apertures. This is stronger in its *twist quantifier* than the untwisted explicit-formula consequence in ANF-191; it is not a new consequence about zeta-zero locations.

The desired **absolute** endpoint amplitude is much smaller:
\[
\frac{X^{B_*+\eta}}{a_X}
\asymp_\Delta\frac{X^{B_*-1/2+\eta}}{\sqrt{\log X}}
\longrightarrow\infty.\tag{13}
\]
This is a comparison of the *available upper bound* with the target, not evidence that the true prime sum is large. In fact, the analogous elementary contour estimate under **RH**, \(O(X^{1/2+\eta})\), would still not yield \(o(a_X)\) by itself. The bow residual is \(r_X=\vartheta-Q_R\); neither (9) nor (11) estimates the rough term \(Q_R\) or its carrier-aligned correlation with the prime component. Subtracting \(Q_R\) without a new arithmetic cancellation theorem therefore cannot close the source gate.

## 4. Prior art, failure modes and decisive boundary

**Prior art:** The underlying Perron formula, zero-free contour shift and log-derivative estimates are classical; the only recent hypothesis is the **unverified here** zero-free claim stated in Baiying Liu, *Slightly improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v1, Theorem 21.1 (already recorded in `SOURCES.md` and audited algebraically in ANF-191). The translated-series argument is a specialization of this classical machinery; no novelty is claimed for the general uniform twisted prime estimate. The local addition is its explicit polynomial-height/prefix/high-pass instantiation and its exponent-versus-endpoint-memory separation for the fixed bow source.

**Controls:** (i) Applying partial summation to \(\psi(x)=x+O(x^{B+\eta})\) costs a factor \(|U|\) and does **not** prove (1); the direct contour shift is essential. (ii) The pole residue must be retained for \(U=0\) and \(|U|\ll1\), even though it is \(O(X^{-1})\) in (8). (iii) Uniformity requires polynomially bounded \(|U|\), since the logarithmic factor in the shifted zero-free contour depends on \(\log(|U|+H)\). (iv) The claim uses the **full fixed zero-free half-plane**, not just a zero-density or critical-line proportion result. (v) Prime powers are removed only by the displayed \(O(\sqrt X\log^2 X)\) allowance. (vi) Neither a small bound relative to \(K\) nor an almost-everywhere height estimate (ANF-190) bounds a prescribed \(U\) at scale \(a_X\).

**Consequence:** This closes the narrow question whether a fixed global zero-free strip can control polynomial-height *prime* twists at its usual exponent without the spurious \(|U|\) loss. It cannot by this method deliver the bow source's \(o(a_X)\) requirement. A meaningful next analytic input would need finer cancellation among zero contributions at the prescribed height, a genuinely sharper signed prime–rough estimate at that height, or a coupled Fejér-scale slope bound; repeating the shifted contour estimate does not supply one. This finding does **not** prove RH, a zero-free theorem, or bow variance.
