# ANF-198 — Fejér profiles force vanishing real improvement amplitudes

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + VARYING-PROFILE + REAL-LATTICE-CONTROL + NONCOMMUTING-LIMITS. ANF-197 classifies exactly zero source-zero exposure as a source rescaling. That classification does not give a uniform stability modulus or a uniform improving amplitude for profiles with small positive exposure. Even profiles converging in every finite \(L^p\) norm to a fixed nonzero rescaling, with uniformly converging Fourier transforms and with each profile in \(H^1\), can have real near-extremizers whose notch exposure tends to the full source budget. The construction uses the classical Fejér kernel; the consequence concerns the quantifiers in ANF-195 and ANF-197, not a new Fourier kernel.

## Statement and conventions

Use ANF-087's source, with Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}f(\alpha)e^{-2\pi i\alpha t}\,d\alpha,
\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,\qquad F(0)=1,
\]
\[
g(\alpha)=\frac{\cos(\sqrt2\alpha)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(\alpha),\qquad
K(t)=\frac{\cos(\pi t)-a t\sin(\pi t)}{1-2\pi^2t^2},
\quad a=\sqrt2\pi\cot(1/\sqrt2).
\tag{1}
\]

The removable points are continued. The positive zeros of \(K\) are
\(r_j\in(j,j+1/2)\), \(j\ge1\). For a finite nonempty real multiset \(W\),
write

\[
L(W)=2|W|-\sigma(W),\quad S_W(\alpha)=\sum_{x\in W}e^{-2\pi i\alpha x},
\quad e(W)=\frac{\int J_0|S_W|^2}{L(W)}-1,
\quad h_\phi(W)=\frac{\int\phi|S_W|^2}{L(W)},
\tag{2}
\]

where \(\sigma\) counts simple real support sites. For a fixed admissible
profile \(\phi\), let \(\Phi=\widehat\phi\),

\[
M_\phi=\max_{j\ge1}\Phi(r_j),\qquad
\beta_\phi^{\mathbb R}
=\lim_{\epsilon\downarrow0}
\sup_{\substack{W\subset\mathbb R\text{ finite},\ W\ne\varnothing\\ e(W)\le\epsilon}}h_\phi(W).
\tag{3}
\]

Freeze \(0\le c<1\); taking \(c=1/2\) gives a nonzero limiting profile.
For integers \(N\ge2\), \(R\ge1\), define the entire shape before varying
any ray amplitude:

\[
D_N(x)=\sum_{j=0}^{N-1}e^{2\pi ijx},\qquad
\psi_{N,R}(\alpha)=J_0(\alpha)\frac{|D_N(R\alpha)|^2}{N^2},
\qquad \phi_{N,R}=cJ_0+(1-c)\psi_{N,R}.
\tag{4}
\]

These profiles are continuous, even, supported in \([-1,1]\), belong
individually to \(H^1(\mathbb R)\), and satisfy

\[
0\le cJ_0\le\phi_{N,R}\le J_0,\qquad
\widehat\phi_{N,R}\ge0.
\tag{5}
\]

They are nonscalar: the ratio \(\phi_{N,R}/J_0\) equals one at zero
and equals \(c\) at \(\alpha=1/(NR)\), where \(D_N(R\alpha)=0\)
and \(J_0(\alpha)>0\).

Uniformly in the integer \(R\ge1\), as \(N\to\infty\),

\[
M_{\phi_{N,R}}=O_c(N^{-1}),\qquad
\beta_{\phi_{N,R}}^{\mathbb R}=c+O_c(N^{-1}),
\tag{6}
\]
\[
\phi_{N,R}\longrightarrow cJ_0\text{ in every }L^p,\ 1\le p<\infty,
\qquad
\|\widehat\phi_{N,R}-cF\|_\infty=O_c(N^{-1}).
\tag{7}
\]

Nevertheless, for the simple real lattice

\[
W_{m,R}=\{0,R,\ldots,(m-1)R\},\qquad m\ge N,
\]

one has, with constants independent of \(N,m,R\),

\[
e(W_{m,R})\asymp R^{-4},\qquad
h_{\phi_{N,R}}(W_{m,R})
\ge1-(1-c)\frac{N^2-1}{3mN}.
\tag{8}
\]

Thus \(m=N^2\), \(N\to\infty\), and any integer \(R=R_N\to\infty\)
give source excess tending to zero and exposure tending to one, while
the corresponding fixed-profile real envelopes tend to \(c\). No modulus
vanishing jointly with excess and \(M_\phi\) can bound
\(h_\phi(W)-\beta_\phi^{\mathbb R}\) throughout this profile class.

## Positive Fourier coefficients and small individual exposures

The elementary Fejér identity is

\[
|D_N(x)|^2=\sum_{|k|<N}(N-|k|)e^{2\pi ikx}.
\tag{9}
\]

Since \(|D_N|\le N\), (4) is dominated by \(J_0\). Fourier modulation
gives the exact nonnegative sum

\[
\Psi_{N,R}(t):=\widehat\psi_{N,R}(t)
=\sum_{|k|<N}\frac{N-|k|}{N^2}F(t-kR)\ge0.
\tag{10}
\]

Equation (1), including boundedness at its removable points, implies
\(0\le F(t)\le C_F/(1+t^2)\). Any lattice of spacing at least one
therefore satisfies

\[
\sup_t\sum_{k\in\mathbb Z}F(t-kR)\le A<\infty
\qquad(R\ge1).
\tag{11}
\]

For example, choose the lattice point nearest to \(t\); the remaining
distances are at least \((j-1/2)R\), and sum the inverse-square bound.
Each coefficient in (10) is at most \(1/N\), whence

\[
0\le\Psi_{N,R}(t)\le A/N\qquad(t\in\mathbb R).
\tag{12}
\]

At source zeros the \(cF\) term vanishes. ANF-195's exact real envelope
for dominated nonnegative-Fourier profiles now gives

\[
\beta_{\phi_{N,R}}^{\mathbb R}
=\widehat\phi_{N,R}(0)+M_{\phi_{N,R}}
=c+(1-c)\{\Psi_{N,R}(0)+\max_j\Psi_{N,R}(r_j)\},
\tag{13}
\]

proving (6). Both maxima exist by Fourier decay; they are positive for
these nonscalar profiles, also by ANF-197.

Positivity and (12) give
\(\|\psi_{N,R}\|_1=\Psi_{N,R}(0)\le A/N\). Since
\(0\le\psi_{N,R}\le J_0\in L^\infty\),

\[
\|\psi_{N,R}\|_p^p\le\|J_0\|_\infty^{p-1}A/N
\qquad(1\le p<\infty),
\tag{14}
\]

which proves (7). Each profile is in \(H^1\): the zero-extended \(g\)
is of bounded variation and in \(L^2\), so the distributional identity
\(J_0'=g'*g\in L^2\) follows by convolution with a finite measure.
Multiplication by the finite smooth polynomial in (9) preserves \(H^1\).
This gives no uniform \(H^1\) bound as \(N,R\) vary.

## A longer physical lattice collects the distributed exposure

All \(m\) sites in \(W_{m,R}\) are simple, so \(L(W_{m,R})=m\).
At nonzero integer arguments, (1) gives

\[
F(kR)=\frac1{(1-2\pi^2k^2R^2)^2}.
\tag{15}
\]

The exact source excess and a uniform bound are

\[
e(W_{m,R})=\frac2m\sum_{k=1}^{m-1}(m-k)F(kR)
\le C_eR^{-4},\quad
C_e=\frac{2}{(2\pi^2-1)^2}\sum_{k\ge1}k^{-4}.
\tag{16}
\]

The \(k=1\) term is at least \(F(R)\ge(4\pi^4R^4)^{-1}\)
when \(m\ge2\), proving the two-sided scale in (8).

Every Fourier coefficient of \(|D_N|^2|D_m|^2\) is nonnegative.
Since \(F(kR)\ge0\), retaining just its constant coefficient in
the source integral gives

\[
\begin{aligned}
h_{\psi_{N,R}}(W_{m,R})
&=\frac1{mN^2}\int J_0(\alpha)
 |D_N(R\alpha)|^2|D_m(R\alpha)|^2\,d\alpha\\
&\ge\frac1{mN^2}\sum_{|k|<N}(N-|k|)(m-|k|)\\
&=1-\frac{N^2-1}{3mN}.
\end{aligned}
\tag{17}
\]

Here the finite sum is \(mN^2-(N^3-N)/3\). The source normalization
\(\int J_0=1\) is essential. Using
\(h_{cJ_0}=c(1+e)\) proves (8), while domination also gives
\(h_{\phi_{N,R}}\le1+e\). Thus the limiting exposure is exactly one.
There is no sign cancellation or unproved equidistribution in (17).

## The improving amplitudes cannot stay uniformly positive

Use ANF-099's linear analytic normalization

\[
C(J)=J(0)+\int_{-1}^1|\alpha|J(\alpha)\,d\alpha,
\qquad C_0=C(J_0),\qquad b_*:=J_0(0)/C_0\in(0,1).
\tag{18}
\]

Since \(\psi_{N,R}(0)=J_0(0)\) and its \(L^1\) norm is \(O(N^{-1})\),

\[
B_{N,R}:=\frac{C(\phi_{N,R})}{C_0}
=c+(1-c)b_*+O_c(N^{-1}).
\tag{19}
\]

Domination and positivity of \(C\) also give \(0<B_{N,R}\le1\).

In particular, the analytic normalization does not converge to that of
\(cJ_0\), despite (7). These are continuous profiles: the discrepancy
comes from narrow peaks at the origin, not from changing a value on a null set.

Define the **real** affine floor

\[
q_{N,R}^{\mathbb R}(t)
=\inf_{W\subset\mathbb R}\{1+e(W)-t h_{\phi_{N,R}}(W)\},
\qquad 0\le t<1,
\tag{20}
\]

over nonempty finite multisets. ANF-099's elementary envelope proof
applies unchanged to this restricted class, since \(e\ge0\),
\(0\le h\le1+e\), and real equality configurations exist. Hence

\[
(q_{N,R}^{\mathbb R})'(0+)=-\beta_{\phi_{N,R}}^{\mathbb R},\qquad
\exists t\in(0,1):q_{N,R}^{\mathbb R}(t)>1-tB_{N,R}
\iff\beta_{\phi_{N,R}}^{\mathbb R}<B_{N,R}.
\tag{21}
\]

The right side holds for all sufficiently large \(N\), uniformly in \(R\).
But set \(m=N^2\). Equations (8) and (19) give, for sufficiently large \(N\),

\[
h_{\phi_{N,R}}(W_{N^2,R})-B_{N,R}
\ge\tfrac12(1-c)(1-b_*)=:d_c>0.
\]

Inserting this one actual multiset into (20) proves the necessary condition

\[
\boxed{\quad
q_{N,R}^{\mathbb R}(t)>1-tB_{N,R}
\quad\Longrightarrow\quad
0<t<\frac{e(W_{N^2,R})}{d_c}\le\frac{C_e}{d_c}R^{-4}.
\quad}
\tag{22}
\]

Thus the real improving rays exist separately, but their admissible
improvement amplitudes shrink to zero. Any improving certificate over
**all complex** configurations must also satisfy (22), because that
larger class includes this real witness. Existence for the complex class
does not follow from (21).

More explicitly, along \(N\to\infty\), \(R_N\to\infty\), domination
and the same lattice give

\[
1-t\le q_{N,R_N}^{\mathbb R}(t)
\le1+C_eR_N^{-4}-t\left[1-(1-c)\frac{N^2-1}{3N^3}\right].
\tag{23}
\]

For every fixed \(0<t<1\), the floors converge to \(1-t\), whereas their
right derivatives at zero converge to \(-c\). The profile limit,
near-extremizer limit and small-amplitude limit cannot be interchanged.

## Prior art, falsification controls and consequence

The Fejér polynomial (9), its positivity and its concentration are
classical; see Casey Rodriguez, MIT 18.102 (Spring 2021),
[Lecture 16: Fejér's theorem and convergence of Fourier series](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/resources/18102-sp21-lecture-16/).
The Montgomery--Taylor extremizer is the classical kernel in
[Carneiro--Chandee--Littmann--Milinovich, section 3.5, Corollary 14](https://arxiv.org/pdf/1406.5462).
No conditional zeta-zero statistics from that paper enter this argument.
Searches by Fejér concentration, positive bandlimited sampling stability,
and Montgomery--Taylor extremality identify these standard ingredients;
no general novelty claim is made. All additional estimates above are
proved directly. The local delta is the failure of profile-uniform real
stability and amplitude selection even as the source-zero exposure
vanishes near a nonzero source rescaling.

The controls distinguish this result from nearby claims:

- Each profile is fixed before varying \(t\), but the sequence varies
  \(N,R\). This does not refute ANF-195's fixed-profile convergence or
  square-root theorem. Its \(H^1\) constants need not remain bounded.
- ANF-196 constructs one fixed rough profile with no power stability
  rate. Here every individual profile is in \(H^1\); the obstruction is
  uniformity across the class and persists with \(\phi\ge cJ_0\).
- ANF-197's exact statement \(M_\phi=0\iff\phi=cJ_0\) is unchanged.
  This construction has small positive \(M_\phi\), and (7) actually
  confirms strong finite-\(L^p\) convergence to a rescaling. It refutes
  continuity in the exposure/analytic-normalization topology, not that
  finite-\(L^p\) convergence itself.
- The profiles occupy the full source support and have oscillations
  throughout it. They are not the fixed proper central triangular notch
  of the accepted exposure-envelope clue. That complex-envelope question
  remains open; no clue disposition is changed.

The decisive checks are the positive triangular coefficients in (10),
the exact integer source values (15), and the constant coefficient in
(17). Direct finite convolution checks for \(2\le N\le17\) and
\(m\in\{N,N+1,N^2\}\) verified the coefficient identity; evaluations at
\(R\in\{1,2,8,32\}\) checked the energy inequalities in all 192 cases.
These are arithmetic sanity checks, not the proof of the quantified result.
No Lean certification, zero-density improvement, unconditional critical-line
proportion improvement, or RH consequence is asserted.
