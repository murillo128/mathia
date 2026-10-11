# ANF-188 — Source-scale semicircle contrast survives growing harmonic cancellation on the exact carrier

**Status:** EXACT-DERIVED + CLASSICAL-DISCREPANCY-AND-DERIVATIVE-TEST + SOURCE-ALPHABET-MATCHED-CONTROL + GROWING-HARMONIC-BLINDNESS + DECISIVE-NEGATIVE-FOR-THE-STRONGER-ANF-187-TEST.

ANF-187 gives an exact one-sided reduction: a target-sized distinguished-height high-pass forces a target-sized real semicircle-prefix contrast, while the converse may fail. Its six-phase example only demonstrates that logical asymmetry for arbitrary phases. Here the failure is realized **on the exact logarithmic carrier**, uniformly over the bow height window, with the two prime/rough coefficient magnitudes, the corresponding total sign counts, near-zero mean, the correct square-mass scale, and prime-scale local absolute-mass bounds. In fact every harmonic prefix through a growing polynomial order is negligible. Thus imposing smallness of every semicircle-prefix contrast is quantitatively stronger than controlling even a growing family of distinguished-height Fourier modes, and can reject a harmless source-shaped control.

## 1. Statement and quantitative scope

Fix \(0<\varepsilon<1/16\), positive \(\delta,A_0,B_0\) with \(A_0<B_0\), and

\[
0<\eta<\frac16-2\varepsilon,\qquad
K=X^{1-2\varepsilon+o(1)},\qquad
A_0X^2\le U\le B_0X^2.
\tag{1}
\]

Let \(X\) be a sufficiently large integer, use the same rough cutoff and coefficient magnitudes as ANF-149/ANF-186,

\[
R=\exp((\log X)^{1/10}),\quad
B_X=\frac{P(R)}{\varphi(P(R))},\quad
A_X=\log X-B_X,\quad
a_X=\sqrt{\delta X\log X},
\tag{2}
\]

so \(B_X\to\infty\), \(B_X=o(A_X)\) and \(A_X\sim\log X\). Put

\[
\theta_j=U\log(1+j/X)\pmod{2\pi},\qquad
H_X=\lfloor X^{\eta/16}\rfloor.
\tag{3}
\]

For every \(U\) in (1), there exist real coefficients \(c_j\), \(0\le j<K\), whose nonzero entries are exclusively

\[
c_j=\log(X+j)-B_X>0\quad\text{or}\quad c_j=-B_X,
\tag{4}
\]

and whose nonzero physical sites are separated by at least \(\lceil\log X\rceil\), such that

\[
\begin{aligned}
&\sum_{j<K}c_j=o(a_X),\qquad
\sum_{j<K}|c_j|=(2+o(1))a_X,\\
&\sum_{j<K}c_j^2=(1+o(1))a_X\log X,\\
&\sum_{j\in I}|c_j|\ll |I|+\log X
\quad\text{for every physical integer interval }I,\\
&\boxed{\ \max_{0\le h\le H_X}\max_{0\le M<K}
\left|\sum_{j\le M}c_je^{-ih\theta_j}\right|=o(a_X)\ },\\
&\boxed{\ \Delta(c,\theta;K-1)=(2+o(1))a_X\ },
\end{aligned}
\tag{5}
\]

where \(\Delta\) is exactly the sign-of-cosine semicircle-prefix statistic of ANF-187. The positive and negative site counts are, respectively, \((1+o(1))a_X/\log X\) and \((1+o(1))a_X/B_X\).

All coefficients lie before a terminal offset \(L_X=o(K)\). Consequently the actual one-height high-pass from ANF-185 satisfies

\[
\mathcal D_T(c;U)=o(a_X)\quad\text{uniformly for every }T>0,
\tag{6}
\]

and the associated left-prefix completion satisfies \(E_-(c_je^{-i\theta_j})=o(XK\log X)\). This is a **false positive for the stronger semicircle test**, not a dangerous bow packet and not an assertion about actual primes.

## 2. Uniformly populate shrinking phase arcs inside physical blocks

Set

\[
W_X=\lfloor X^{1/3+\eta}\rfloor,\qquad
J_X=\lfloor X^{\eta/4}\rfloor,\qquad
\rho_X=X^{-\eta/8}.
\tag{7}
\]

Consider any block of \(W_X+O(1)\) consecutive offsets contained in \(0\le j=o(X)\). For \(1\le h\le J_X\), the phase \(f_h(j)=h\theta_j/(2\pi)\), with a continuous real lift, has a third derivative of fixed sign and size

\[
|f_h'''(j)|\asymp_{A_0,B_0}h/X
\tag{8}
\]

uniformly over the block and the full height window. The classical third-derivative van der Corput bound (the same normalized input as ANF-186, now with its constants uniform in \(h\)) gives

\[
\frac1{W_X}\left|\sum_{j\text{ in block}}e^{ih\theta_j}\right|
\ll
W_X^{-1/4}+(h/X)^{1/6}
+(hW_X^3/X)^{-1/4}
\ll X^{-3\eta/4}.
\tag{9}
\]

Here \(\eta<1/6\); all constants are uniform for \(1\le h\le J_X\) because the upper/lower derivative ratio in (8) is independent of \(h\). The Erdős–Turán discrepancy inequality for the **unweighted positive counting measure** therefore yields, uniformly over every angular arc \(I\) and every such block,

\[
\left|
\frac{\#\{j\text{ in block}:\theta_j\in I\}}{W_X}
-\frac{|I|}{2\pi}\right|
\ll J_X^{-1}
+\sum_{h=1}^{J_X}\frac{X^{-3\eta/4}}h
\ll X^{-\eta/4}
=o(\rho_X).
\tag{10}
\]

In particular, each of the two disjoint arcs

\[
I_+=(\pi/2-3\rho_X,\ \pi/2-\rho_X),\qquad
I_-=(\pi/2+\rho_X,\ \pi/2+3\rho_X)
\tag{11}
\]

contains \((1+o(1))(\rho_X/\pi)W_X\) offsets in **every** physical block, with no Diophantine assumption on \(U\). These counts are much larger than any fixed power of \(\log X\). Removing \(\lceil\log X\rceil\)-neighborhoods of previously selected sites and block endpoints leaves enough candidates to select \(O(\log X)\) mutually separated sites per block.

This step uses Erdős–Turán only for **nonnegative unweighted occupancy**. It does not apply an unsigned discrepancy theorem to the signed prime-minus-rough residual.

## 3. Build carrier-boundary dipoles with the source coefficient alphabet

Put

\[
t_X=\lfloor A_X/B_X\rfloor,\qquad
N_X=\lfloor a_X/A_X\rfloor,\qquad
L_X=N_XW_X.
\tag{12}
\]

Because \(N_X\asymp X^{1/2}/\sqrt{\log X}\),

\[
L_X\asymp\frac{X^{5/6+\eta}}{\sqrt{\log X}}=o(K)
\quad\text{by }\eta<1/6-2\varepsilon,
\qquad L_X=o(X).
\tag{13}
\]

Partition the initial \(L_X\) offsets into \(N_X\) consecutive blocks of width \(W_X\). In each block choose exactly one positive site with \(\theta_j\in I_+\) and exactly \(t_X\) negative sites with \(\theta_j\in I_-\), preserving mutual physical gaps of at least \(q_X=\lceil\log X\rceil\) across all blocks. Give the positive site coefficient \(\log(X+j)-B_X\), the negative sites coefficient \(-B_X\), and all other sites coefficient zero.

The arcs straddle the single semicircle boundary at \(\pi/2\): \(\cos\theta>0\) on \(I_+\) and \(\cos\theta<0\) on \(I_-\). Yet all selected phases are within \(3\rho_X\) of \(\pi/2\). Thus they are easily separated by the discontinuous sign test but are indistinguishable at harmonic frequencies \(h=o(\rho_X^{-1})\).

The positive count is \(N_X=(1+o(1))a_X/\log X\). Since \(t_X=(1+o(1))A_X/B_X\), the negative count is \(N_Xt_X=(1+o(1))a_X/B_X\), matching the **global** two-sign site counts at reference mass scale \(a_X\) in ANF-186. These are not claimed to be correct densities in every subinterval of the larger loading support \(L_X\).

## 4. Verify mean, diagonal and every local mass envelope

As \(j\le L_X=o(X)\), each positive coefficient equals \(A_X+o(1)\). Per block the signed mass and its absolute/square counterparts are

\[
A_X-t_XB_X+o(1)\in[0,B_X)+o(1),
\quad A_X+t_XB_X+o(1)=(2+o(1))A_X,
\tag{14}
\]

\[
A_X^2+t_XB_X^2+o(A_X)=(1+o(1))A_X^2.
\tag{15}
\]

Summing over \(N_X=(1+o(1))a_X/A_X\) blocks proves the first three assertions in (5). The \(q_X\)-separation and \(|c_j|\le\log X+o(1)\) give for every interval of integer offsets of length \(H\)

\[
\sum_{j\in I}|c_j|
\le(\log X+o(1))(H/q_X+1)
\ll H+\log X.
\tag{16}
\]

The construction thus obeys the same **coefficient-size, total sign-count, mean, square-mass and local mass-envelope scales** as the source-alphabet control in ANF-186. Its longer sparse support and carrier-dependent selection are deliberately retained as limitations.

## 5. Growing harmonic blindness versus maximal semicircle contrast

Write \(S_{b,h}\) for the signed \(h\)-th harmonic sum in one completed block. All its nonzero phase offsets have distance at most \(3\rho_X\) from \(\pi/2\). Therefore, for \(0\le h\le H_X\),

\[
\begin{aligned}
|S_{b,h}|
&\le\left|\sum_{j\text{ in block}}c_j\right|
+\sum_{j\text{ in block}}|c_j|
\left|e^{-ih\theta_j}-e^{-ih\pi/2}\right|\\
&\ll B_X+A_Xh\rho_X+o(1).
\end{aligned}
\tag{17}
\]

Any unfinished block contributes at most \((2+o(1))A_X\) in absolute value. Taking prefixes across the completed blocks gives

\[
\max_{\substack{0\le h\le H_X\\M<K}}
\left|\sum_{j\le M}c_je^{-ih\theta_j}\right|
\ll
N_X(B_X+A_XH_X\rho_X)+A_X
\ll
a_X\left(\frac{B_X}{A_X}+X^{-\eta/16}\right)+A_X
=o(a_X).
\tag{18}
\]

In sharp contrast, every nonzero coefficient satisfies \(c_j\operatorname{sgn}\cos\theta_j=|c_j|\). At the terminal prefix and orientation \(\psi=0\),

\[
\Delta(c,\theta;K-1)\ge\sum_{j<K}|c_j|
=(2+o(1))a_X.
\tag{19}
\]

The reverse bound \(\Delta\le\sum|c_j|\) is automatic, proving equality at this scale.

Finally ANF-185's bounded-variation identity gives, for any \(T>0\),

\[
|\mathcal D_T(c;U)|
\le C_W\max_{M<K}\left|\sum_{j\le M}c_je^{-i\theta_j}\right|
=o(a_X),
\tag{20}
\]

uniformly in \(T\). Also, with \(b_j=c_je^{-i\theta_j}\),

\[
E_-(b)=\sum_{M<K}\left|\sum_{j\le M}b_j\right|^2
\le K\,o(a_X^2)=o(XK\log X).
\tag{21}
\]

So the semicircle statistic is maximally large on a packet that does **not** load the first-harmonic endpoint memory and is invisible to the entire growing low-harmonic family.

## 6. Prior art, falsification boundary and live consequence

The two analytic ingredients are classical: van der Corput's third-derivative exponential-sum test and the nonnegative-measure Erdős–Turán discrepancy inequality (see H. L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, CBMS 84, 1994, chapters 1 and 3). Their use to populate shrinking arcs in all exact-logarithmic-carrier blocks is a quantitative strengthening of the fixed-arc step in ANF-186. Boundary-straddling signed dipoles are likewise a familiar general obstruction to recovering discontinuous observables from low Fourier modes. The line-specific additional statement is their simultaneous realization at bow scales with the prime/rough coefficient alphabet, natural total counts and diagonal, physical spacing, and a polynomially growing harmonic blind window.

This **does not** show that the actual arithmetic residual \(r_X=\vartheta-Q_R\) violates the ANF-187 condition; the constructed sites are chosen after looking at \(\theta_j\) and are not required to be actual primes or \(R\)-rough composites. It also does not preserve actual prime/rough spatial densities inside every subinterval of \(L_X\). It supplies no zero-location theorem. Its precise negative consequence is narrower and useful: the sufficient ANF-187 semicircle-prefix condition can register a full \(\Theta(a_X)\) failure while the *original* deterministic high-pass, the bow endpoint completion, and all prefixes of harmonics \(0\le h\le X^{\eta/16}\) are \(o(a_X)\). Therefore a future attempt to deduce the stronger sign criterion from finitely/gently growing many harmonic source estimates needs genuinely new control of **signed mass across arbitrarily narrow angular boundaries**; otherwise it is preferable to attack the exact first-harmonic high-pass or signed Fejér slope directly, without treating the stronger sign criterion as equivalent.
