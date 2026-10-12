# ANF-189 — Opposed prime–rough packets defeat every saturated critical high-pass

**Status:** EXACT-DERIVED + SOURCE-ALPHABET-MATCHED-CONTROL + UNIFORM-HIGH-PASS-OBSTRUCTION + TWO-SCALE-WITNESS + DECISIVE-NEGATIVE-FOR-GENERIC-SUFFICIENCY.

ANF-185 proves that its fixed-base triangular-aperture high-pass detects every **globally sector-aligned** dangerous packet. That hypothesis matters: two separated packets with opposite distinguished-height charge can create bow-scale endpoint completion while *every* high-pass with aperture at or above \(X/a_X\) is small. A smaller aperture \(X/K\), resolving the separation rather than packet widths, sees the hidden charge. The construction below is synthetic, uses the exact logarithmic carrier and the source-sized prime/rough coefficient alphabet, and deliberately does **not** claim actual prime positions.

## 1. Theorem

Fix \(0<\varepsilon<1/16\), \(\delta>0\), \(0<A_0<B_0<\infty\), and \(C>0\), with

\[
K=X^{1-2\varepsilon+o(1)}\in\mathbb N,\quad
A_0X^2\le U\le B_0X^2,\quad
a_X=\sqrt{\delta X\log X},\quad
\theta_j=U\log(1+j/X).
\tag{1}
\]

Use ANF-186's rough cutoff and source coefficient sizes,

\[
R=\exp((\log X)^{1/10}),\quad
B_X=P(R)/\varphi(P(R)),\quad A_X=\log X-B_X,
\tag{2}
\]

where \(B_X\to\infty\), \(B_X=o(\log X)\), and \(A_X\sim\log X\). There are real coefficients \(c_0,\ldots,c_{K-1}\), each belonging to the index-dependent alphabet \(\{0,\,-B_X,\,\log(X+j)-B_X\}\), with

\[
\sum c_j=o(a_X),\quad
\sum|c_j|=(4+o(1))a_X,\quad
\sum c_j^2=(2+o(1))a_X\log X,\quad
\sum_{j\in I}|c_j|\ll |I|+\log X
\tag{3}
\]

for every integer interval \(I\) of offsets. Write \(b_j=c_je^{-i\theta_j}\),

\[
E_-(b)=\sum_{M=0}^{K-1}\left|\sum_{j\le M}b_j\right|^2,\qquad
\mathcal D_T(c;U)=\sum_{j<K}b_j W(T\log(1+j/X)),\quad
W(y)=1-\operatorname{sinc}^2(y/2).
\tag{4}
\]

Then uniformly for \(U\) in (1),

\[
\boxed{
E_-(b)\asymp XK\log X,\qquad
K\sum_j|b_j|^2=o(XK\log X),\qquad
\sup_{T\ge CX/a_X}|\mathcal D_T(c;U)|=o(a_X),
}
\tag{5}
\]

whereas

\[
\boxed{\mathcal D_{4\pi X/K}(c;U)=-(2+o(1))a_X.}
\tag{6}
\]

The \(o(1)\) statements are uniform in \(U\) for any fixed admissible \(K(X)\). The source-shaped counts/moments are global; local prime and rough-composite densities are *not* asserted.

## 2. Quantitative exact-carrier shrinking-arc occupancy

Put

\[
\rho=(\log\log X)^{-1},\quad
L=\lfloor24\pi a_X/\rho\rfloor,\quad
q_+=2\lceil12A_X\rceil,\quad
q_-=2\lceil12B_X\rceil.
\tag{7}
\]

The even steps tend to infinity and are \(O(\log X)\). For a base \(s\) with \(0\le s<s+L<K\), use the disjoint relative-parity progressions

\[
\mathcal P_+(s)=\{s+q_+m:m\ge0\},\quad
\mathcal P_-(s)=\{s+1+q_-m:m\ge0\},
\tag{8}
\]

restricted to \([s,s+L)\). For **every** circular arc \(I\) of angular length \(2\rho\), the fraction of carrier rays \(e^{-i\theta_j}\) inside \(I\) on either progression is

\[
\frac{\rho}{\pi}+o(\rho),
\tag{9}
\]

uniformly over \(s,U,I\).

To prove the shrinking-arc (rather than just fixed-arc) assertion, let \(f_h(m)=hU\log(1+(s+r+qm)/X)/(2\pi)\), where \(q=q_\pm\), \(r=0\) or \(1\), and \(1\le h\le H_0=\lceil(\log X)^2\rceil\). On every such block, \(s+L<K=o(X)\) and

\[
|f_h'''(m)|\asymp hq^3/X
\tag{10}
\]

with uniform derivative comparison constants. The classical third-derivative bound with \(N=L/q+O(1)\) gives

\[
\frac1N\left|\sum_{m<N}e^{2\pi if_h(m)}\right|
\ll N^{-1/4}+(hq^3/X)^{1/6}
+(hq^3N^3/X)^{-1/4}\ll X^{-1/9}.
\tag{11}
\]

Indeed \(N\asymp\sqrt{X\log X}/(\rho q)\), \(hq^3\ll(\log X)^5\), and \(hq^3N^3/X\asymp hL^3/X\gg X^{1/2}\). Erdős–Turán, applied **only to the nonnegative unweighted carrier counting measure**, now gives arc discrepancy

\[
D_{\rm arc}\ll H_0^{-1}+
\sum_{1\le h\le H_0}\frac{X^{-1/9}}h
\ll(\log X)^{-2}=o(\rho),
\tag{12}
\]

proving (9). Neither input proves a signed prime-minus-rough estimate.

## 3. Put opposite carrier charges at two distant locations

Choose the packet bases

\[
s_+=\lfloor a_X/\rho^2\rfloor,\qquad
s_-=\lfloor K/2\rfloor.
\tag{13}
\]

Because \(K/a_X=X^{1/2-2\varepsilon+o(1)}(\log X)^{-1/2}\to\infty\), we have \(a_X\ll s_+\), \(L=o(s_+)\), \(s_++L=o(K)\), and \(s_-+L<K\). Thus both packets are far past the critical loading distance \(a_X\) and separated by \((1/2+o(1))K\) physical offsets.

In the packet based at \(s_\tau\), \(\tau\in\{+1,-1\}\), select positive source-shaped coefficients \(c_j=\log(X+j)-B_X\) on the progression \(\mathcal P_+(s_\tau)\) only where \(e^{-i\theta_j}\) lies within angle \(\rho\) of \(\tau\). Select negative coefficients \(c_j=-B_X\) on \(\mathcal P_-(s_\tau)\) only where that carrier lies within angle \(\rho\) of \(-\tau\). All other coefficients are zero.

From (9), the positive and negative counts **in each packet** are

\[
N_{\tau,+}=(1+o(1))a_X/A_X,\qquad
N_{\tau,-}=(1+o(1))a_X/B_X.
\tag{14}
\]

Every selected \(j=o(X)\), so the positive coefficient is \(A_X+o(1)\). Each packet therefore has untwisted sum \(o(a_X)\), total absolute mass \((2+o(1))a_X\), and square mass \((1+o(1))a_X(A_X+B_X)=(1+o(1))a_X\log X\). These prove the global claims in (3). The local mass envelope follows without estimating arithmetic positions: in an interval of length \(H\), either progression contributes at most \(H/q_\pm+1\) candidates per packet, so

\[
\sum_{j\in I}|c_j|
\le2\big[(A_X+o(1))(H/q_++1)+B_X(H/q_-+1)\big]
\ll H+\log X.
\tag{15}
\]

A negative source coefficient reverses the carrier angle. Thus all nonzero twisted contributions from packet \(\tau\) lie within angle \(\rho\) of \(\tau\). With \(Q_\tau\) its complete twisted charge,

\[
\left|Q_\tau-\tau\sum_{j\text{ in packet }\tau}|c_j|\right|
\le \rho\sum_{j\text{ in packet }\tau}|c_j|
=o(a_X).
\]

It follows that

\[
\boxed{Q_+=(2+o(1))a_X,\quad Q_-=-(2+o(1))a_X,\quad Q_++Q_-=o(a_X).}
\tag{16}
\]

The selection uses the right coefficient alphabet, correct *overall* sign-count and moment scales and a prime-scale absolute-mass envelope. It does not preserve actual prime/rough placement: the selected-site densities within the expanded spans \(L\asymp a_X/\rho\) are lower by a factor comparable to \(\rho\). This loss is explicit.

## 4. Endpoint memory survives saturation of every critical high-pass

Between the first and second packets, \((1/2+o(1))K\) consecutive prefixes equal \(Q_+\). Consequently

\[
E_-(b)\ge (s_--s_+-L-O(1))|Q_+|^2
=(2+o(1))K a_X^2\gg XK\log X.
\tag{17}
\]

The global \(l^1\) bound implies \(E_-(b)\ll K a_X^2\). The diagonal is

\[
K\sum|b_j|^2=(2+o(1))K a_X\log X=o(XK\log X).
\tag{18}
\]

For any \(T\ge CX/a_X\), every occupied index has \(j\ge s_+\) and \(\lambda_j=\log(1+j/X)\ge s_+/(2X)\). Therefore \(T\lambda_j\ge Cs_+/(2a_X)\asymp_C\rho^{-2}\). Since \(0\le1-W(y)=\operatorname{sinc}^2(y/2)\le4/y^2\),

\[
|\mathcal D_T(c;U)|
\le \left|\sum_jb_j\right|
+\sum_j|b_j|\,[1-W(T\lambda_j)]
\le |Q_++Q_-|+O_C(a_X\rho^4)
=o(a_X).
\tag{19}
\]

The same bound holds **simultaneously for all real \(T\ge CX/a_X\)**. At these apertures the high-pass is nearly the terminal charge, in which the two dangerous packets cancel.

## 5. An inverse-separation aperture detects the charge

Set \(T_*=4\pi X/K\). Since \(s_++L=o(K)\), on the early packet \(T_*\log(1+j/X)=o(1)\) and the multiplier is \(o(1)\) uniformly. On the later packet \(j=K/2+O(L)\), so

\[
T_*\log(1+j/X)=2\pi+o(1),\quad
W(T_*\log(1+j/X))=W(2\pi)+o(1)=1+o(1).
\tag{20}
\]

Using the \(O(a_X)\) absolute mass of either packet,

\[
\mathcal D_{4\pi X/K}(c;U)=Q_-+o(a_X)=-(2+o(1))a_X.
\tag{21}
\]

Here \(T_* /(X/a_X)=4\pi a_X/K\to0\). The smaller aperture distinguishes **locations** separated by \(\Theta(K)\), not individual site spacings; taking ever-larger critical apertures destroys this particular discriminatory information.

## 6. Prior art and exact boundary

The ingredients are classical: third-derivative van der Corput estimates and the Erdős–Turán inequality, already anchored in SOURCES.md for ANF-188; the triangular/Bartlett aperture identity from ANF-185; and cancellation of opposite signed masses under a saturated Fourier multiplier. No general harmonic-analysis theorem or new result about primes is claimed. The additional content is their exact-logarithmic-carrier construction at the bow endpoint scale with real source-sized sign amplitudes, global moment matching, a local mass envelope, and a complete aperture-family no-go.

ANF-185 is not contradicted: its global sector-alignment hypothesis fails across the opposing packets. ANF-187's stronger semicircle-prefix test detects the early charge; ANF-188 independently demonstrates why that sign test may reject harmless controls. The present coefficients are chosen *after* reading the carrier and need not occur on real prime or rough-composite sites; their local densities are diluted. No conclusion about the actual \(r_X=\vartheta-Q_R\) or RH follows.

The precisely falsified **coefficient-generic** implication is

\[
\left[\sup_{T\ge CX/a_X}|\mathcal D_T(c;U)|=o(a_X)\right]
\;\not\Longrightarrow\;
\left[E_-(b)=o(XK\log X)\right]
\tag{22}
\]

even after matching the alphabet, global sign counts, first-/second-moment scales and local absolute-mass envelope. A theorem for the actual source might exploit arithmetic no-cancellation restrictions; high-pass control alone is insufficient. The surviving mathematically faithful alternatives are physical-prefix localization or the multi-scale signed Fejér slope of ANF-172. This is an obstruction to an intermediate detector, not a proof or refutation of RH.
