# WI-449 — Noncommensurate Wang lattices incur an endpoint tariff, with a sharp quartic crossover

**Status:** EXACT-DERIVED + PRIMARY-SOURCE-SPECIALIZATION + SHARP-ASYMPTOTIC/OBSTRUCTION + CLASSICAL-FOURIER-TOOLS + NON-RH + NO-PRIORITY-CLAIM

**Primary source:** Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2 (6 October 2026), Proposition 4.1 (cosine variational minimizer and smooth admissible tests), https://arxiv.org/html/2609.07918v2.

**Local dependencies:** WI-442 (finite multiset and real Gram defect), WI-445 (rigidity at the exact cosine optimizer), WI-446 (exact smooth reciprocal-lattice orthogonality), WI-447 (triple-Gram quartic decay), and WI-448 (sharp cost on commensurate lattices).

## Exact object and results

Fix \(0<\lambda\le1\), put \(a=\lambda/2\), and use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt.
\]
Wang's normalized optimizer, its endpoint height, and its cost are
\[
f_*(t)=\frac{\cos(\sqrt2t)}{\sqrt2\sin(\lambda/\sqrt2)}
           {\bf1}_{[-a,a]}(t),\qquad
A_\lambda=f_*(a-)=\frac1{\sqrt2}\cot\frac{\lambda}{\sqrt2}>0,
\]
\[
C(f)=\|f\|_2^2+\iint|t-v|f(t)f(v)\,dt\,dv,\qquad
C_\lambda=C(f_*).
\]
The source-admissible class is
\[
\mathcal F_\lambda=
 \{\eta^2:\eta\in C_c^\infty((-a,a);\mathbb R),\
   \eta\text{ even},\ \int\eta^2=1\}.
\]
For \(p>0\), let \(I_\lambda(p)\) be the infimum of \(C(f)-C_\lambda\) over
\(f\in\mathcal F_\lambda\) satisfying
\(\widehat f(k/p)=0\) for **every** nonzero integer \(k\); an empty
feasible set has infimum \(+\infty\). The corresponding exponentials
form an infinite pairwise orthonormal lattice in \(L^2(f(t)\,dt)\).
WI-448 computed \(I_\lambda(\lambda/q)=p^4/(180\lambda)+O_\lambda(p^5)\).

**Theorem A (uniform phase-dependent endpoint tariff).** Set
\[
q_p=\lfloor\lambda/p\rfloor,\qquad
\theta_p=\{\lambda/p\}\in[0,1).
\]
For every sufficiently small \(p>0\), the smooth feasible set is
nonempty, and uniformly in the fractional phase,
\[
\boxed{\quad I_\lambda(p)=
 \frac{A_\lambda^2}{\lambda}\,
       \theta_p(1-\theta_p)p^2
 +O_\lambda\bigl(p^3\theta_p(1-\theta_p)+p^4\bigr).\quad} \tag{1}
\]
In particular, if \(\theta_p\to\theta_0\in(0,1)\), then
\[
\lim_{p\downarrow0}\frac{I_\lambda(p)}{p^2}
=\frac{\cot^2(\lambda/\sqrt2)}{2\lambda}\,
\theta_0(1-\theta_0)>0. \tag{2}
\]
Thus WI-448's quartic law is **not** the generic high-frequency lattice
cost: exact fractional endpoint mismatch incurs a quadratic leading
charge. The nonnegative charge is genuinely due to the optimizer's
nonzero support-endpoint value, not a Fourier normalization artifact.

**Theorem B (sharp near-resonant crossover).** Let
\(d_p=\operatorname{dist}(\lambda/p,\mathbb Z)
=\min(\theta_p,1-\theta_p)\). Along any sequence \(p\downarrow0\)
for which
\[
d_p/p^2\longrightarrow\tau\in[0,\infty),
\]
one has the sharp source-admissible asymptotic
\[
\boxed{\quad
\lim_{p\downarrow0}\frac{I_\lambda(p)}{p^4}
=\frac1{180\lambda}+\frac{A_\lambda^2}{\lambda}\tau
=\frac1{180\lambda}
 +\frac{\cot^2(\lambda/\sqrt2)}{2\lambda}\tau.\quad} \tag{3}
\]
The \(\tau=0\) case extends the commensurate coefficient of WI-448
to periods within \(o(p^2)\) in **fractional phase** of an integer
number of support periods. For \(\tau>0\), the smooth-transform
contribution and the endpoint-jump contribution survive together.
For \(d_p\to0\) but \(d_p\gg p^2\), the quadratic endpoint term again
dominates and \(I_\lambda(p)\sim A_\lambda^2p^2d_p/\lambda\).
No assertion uniform in \(\lambda\downarrow0\) is made.

## 1. Exact lattice constraint and least-norm fiber correction

For \(f\) supported in \([-a,a]\), Fourier uniqueness on the period
circle gives the exact equivalence
\[
\widehat f(k/p)={\bf1}_{\{k=0\}}\ (k\in\mathbb Z)
\quad\Longleftrightarrow\quad
p\sum_{j\in\mathbb Z}f(s+jp)=1
\quad\text{for a.e. }s\bmod p. \tag{4}
\]
Define the periodic support-count, optimizer periodization, and
periodization error by
\[
M_p(s)=\sum_j{\bf1}_{[-a,a]}(s+jp),\quad
G_p(s)=p\sum_j f_*(s+jp),\quad E_p(s)=G_p(s)-1.
\]
For small \(p\), \(M_p\) takes only \(q_p\) and \(q_p+1\):
a fraction \(\theta_p\) of each period has \(q_p+1\) support
preimages; the remainder has \(q_p\). In particular,
\(pM_p=\lambda+O(p)\) uniformly and \(M_p\ge1\).

Writing \(g=f-f_*\), the constraint is \(p\sum_jg(s+jp)=-E_p(s)\).
Its **unique least-\(L^2([-a,a])\)-norm solution** is constant
on each residue fiber:
\[
h_p(t)=-\frac{E_p(t\bmod p)}{pM_p(t\bmod p)}
        {\bf1}_{[-a,a]}(t). \tag{5}
\]
Every other signed \(L^2\) solution decomposes as \(g=h_p+w\), with
\(p\sum_jw(s+jp)=0\), \(\langle h_p,w\rangle_{L^2}=0\), and
\(\int h_p=\int w=0\). The exact fiber-integral formula is
\[
\boxed{\quad
\|h_p\|_2^2=
\frac1p\int_0^p\frac{|E_p(s)|^2}{pM_p(s)}\,ds.\quad} \tag{6}
\]
Replacing \(pM_p\) by \(\lambda\) is an approximation, not an exact
identity away from commensurability. This distinction matters for
the error terms in the theorem.

## 2. Endpoint discrepancy and the two leading scales

Split the discontinuous optimizer into its endpoint rectangle and a
continuous remainder:
\[
f_*=A_\lambda{\bf1}_{[-a,a]}+b_\lambda,\qquad
b_\lambda(\pm a)=0.
\]
The compactly supported \(b_\lambda\) is continuous and piecewise
\(C^2\) with derivative of bounded variation. Integration by parts
twice gives \(\widehat b_\lambda(\xi)=O_\lambda(|\xi|^{-2})\).
Thus its centered periodization
\[
B_p(s)=p\sum_jb_\lambda(s+jp)-\int b_\lambda
\]
has an absolutely convergent Fourier series and
\(\|B_p\|_\infty=O_\lambda(p^2)\). Since \(\int f_*=1\),
\[
E_p(s)=A_\lambda[pM_p(s)-\lambda]+B_p(s). \tag{7}
\]
Both summands in (7) have period mean zero. The first takes the
two values \(A_\lambda p(1-\theta_p)\) and
\(-A_\lambda p\theta_p\), with respective proportions
\(\theta_p\) and \(1-\theta_p\). Consequently,
\[
\frac1p\int_0^p|pM_p-\lambda|^2\,ds
=p^2\theta_p(1-\theta_p),\qquad
\frac1p\int_0^p|pM_p-\lambda|\,ds
=2p\theta_p(1-\theta_p). \tag{8}
\]
By (7)--(8) and the \(O(p^2)\) uniform bound for \(B_p\),
\[
\frac1p\int_0^p|E_p|^2\,ds
=A_\lambda^2p^2\theta_p(1-\theta_p)
+O_\lambda\!\left(p^3\theta_p(1-\theta_p)+p^4\right). \tag{9}
\]
The positive quadratic coefficient is therefore the exact
two-valued count variance times the **squared endpoint height**.

For the finer resonant regime, Parseval gives
\[
\frac1p\int_0^p|B_p|^2\,ds
=\sum_{k\ne0}|\widehat b_\lambda(k/p)|^2. \tag{10}
\]
Direct cosine integration, with \(q=q_p,\theta=\theta_p\),
gives for \(k\ge1\) the *exact* identity
\[
\widehat f_*(k/p)=(-1)^{qk}
\frac{\displaystyle
 A_\lambda\frac{p}{\pi k}\sin(\pi k\theta)
       -\frac{p^2}{2\pi^2k^2}\cos(\pi k\theta)}
     {\displaystyle1-\frac{p^2}{2\pi^2k^2}}. \tag{11}
\]
On subtracting the rectangle transform,
\[
\widehat b_\lambda(k/p)=(-1)^{qk}\left[
 -\frac{p^2}{2\pi^2 k^2}\cos(\pi k\theta)
 +O_\lambda\!\left(\frac{p^3|\sin(\pi k\theta)|}{k^3}
                    +\frac{p^4}{k^4}\right)\right]. \tag{12}
\]
If \(d_p\to0\), the squared normalized coefficients in (12)
converge termwise to \(1/(4\pi^4k^4)\), even when the parity
of \(q_p\) varies. The uniform \(O_\lambda(k^{-2})\) bound
permits dominated convergence in (10); using
\(2\sum_{k\ge1}(4\pi^4k^4)^{-1}=1/180\) gives
\[
\frac1p\int_0^p|B_p|^2\,ds
=\frac{p^4}{180}+o_\lambda(p^4)
\quad(d_p\to0). \tag{13}
\]
When \(d_p=O(p^2)\), the mixed term in the square of (7) is
\(O_\lambda(p^3d_p)=O_\lambda(p^5)\). Hence
\[
\frac1p\int_0^p|E_p|^2\,ds
=A_\lambda^2p^2\theta_p(1-\theta_p)
+\frac{p^4}{180}+o_\lambda(p^4). \tag{14}
\]
Equations (6), (9), (14), and
\((pM_p)^{-1}=\lambda^{-1}+O_\lambda(p)\)
show that
\[
\|h_p\|_2^2=
\frac{A_\lambda^2}{\lambda}p^2\theta_p(1-\theta_p)
 +O_\lambda\!\left(p^3\theta_p(1-\theta_p)+p^4\right), \tag{15}
\]
and, when \(d_p=O(p^2)\),
\[
\|h_p\|_2^2=
\frac{A_\lambda^2}{\lambda}p^2\theta_p(1-\theta_p)
+\frac{p^4}{180\lambda}+o_\lambda(p^4). \tag{16}
\]

## 3. Wang's primitive energy cannot change the leading terms

For any zero-mean \(v\in L^2([-a,a])\), put
\(Pv(t)=\int_{-a}^t v(u)\,du\). Wang's exact second-variation
identity and Dirichlet Poincare inequality are
\[
C(f)-C_\lambda=Q(f-f_*),\quad
Q(v)=\|v\|_2^2-2\|Pv\|_2^2,\quad
Q(v)\ge\sigma_\lambda\|v\|_2^2,\quad
\sigma_\lambda=1-\frac{2\lambda^2}{\pi^2}>0. \tag{17}
\]
The centered \(E_p\) has period mean zero. From (7)--(8),
its mean absolute size is
\(O_\lambda(p\theta_p(1-\theta_p)+p^2)\).
Because \((pM_p)^{-1}=\lambda^{-1}+O(p)\), integrating
(5) over complete periods and at most two partial periods
proves the *uniform primitive estimate*
\[
\|Ph_p\|_\infty=
O_\lambda\!\left(p^2\theta_p(1-\theta_p)+p^3\right). \tag{18}
\]
In particular, \(\|Ph_p\|_2=O_\lambda(p^2)\) always,
and \(O_\lambda(p^3)\) if \(d_p=O(p^2)\).

For any signed competitor \(g=h_p+w\), fiber orthogonality,
(17), \(\|Pw\|_2\le(\lambda/\pi)\|w\|_2\), and completing
a square yield
\[
\begin{aligned}
Q(g)&=Q(h_p)+Q(w)-4\langle Ph_p,Pw\rangle\\
&\ge\|h_p\|_2^2-
\left(2+\frac{4\lambda^2}{\sigma_\lambda\pi^2}\right)
\|Ph_p\|_2^2. 
\end{aligned}\tag{19}
\]
This lower bound is valid even in the larger class of signed
\(L^2\) densities. Thus the primitive correction costs at most
\(O_\lambda(p^4)\) in the general regime and \(O_\lambda(p^6)\)
at \(d_p=O(p^2)\). No indefinite off-critical zeta block
is being replaced by a positive real Gram form here; this is
solely Wang's *test-density variational problem*.

## 4. Exact smooth nonnegative upper construction

The affine minimum \(f_*+h_p\) is discontinuous and therefore
does **not** itself establish the claimed infimum in Wang's smooth
admissible class. Choose an even smooth cutoff \(\chi_\varepsilon\),
equal to \(1\) outside endpoint collars of total width
\(O(\varepsilon)\), supported strictly in \((-a,a)\), with
\(0\le\chi_\varepsilon\le1\), and set
\[
\varepsilon=p^6,\quad \varphi=\chi_\varepsilon^2,\quad
Z=\int\varphi f_*,\quad
f_0=\frac{\varphi f_*}{Z},\quad
G_{0,p}(s)=p\sum_j f_0(s+jp),\quad
W_p(s)=p\sum_j\varphi(s+jp). \tag{20}
\]
For all sufficiently small \(p\), \(W_p(s)\ge\lambda/2\)
uniformly. Define
\[
f_p(t)=
\varphi(t)\left[
\frac{f_*(t)}Z-\frac{G_{0,p}(t)-1}{W_p(t)}
\right]\quad(t\in(-a,a)),\qquad f_p=0\text{ outside}. \tag{21}
\]
The bracket is even, smooth and strictly positive on
\([-a,a]\) for small \(p\). Indeed \(\min_{[-a,a]}f_*>0\),
\(Z=1+O_\lambda(\varepsilon)\), and the bounded-variation
Riemann-sum estimate gives
\(G_{0,p}-1=O_\lambda(p)\) uniformly, independently of the
fractional phase. Therefore \(f_p=\eta_p^2\) for an even
real \(\eta_p\in C_c^\infty((-a,a))\).

Unlike an approximate Fourier interpolation, this construction
makes the periodization identically constant:
\[
p\sum_j f_p(t+jp)=G_{0,p}(t)
 -[G_{0,p}(t)-1]\frac{W_p(t)}{W_p(t)}=1. \tag{22}
\]
It follows that \(f_p\) is normalized and *all* the reciprocal
lattice Fourier coefficients vanish exactly.

A quantitative collar audit also retains the leading constant.
The baseline truncation satisfies
\(\|f_0-f_*\|_2=O_\lambda(\sqrt\varepsilon)=O_\lambda(p^3)\).
The periodized collar error \(G_{0,p}-G_p\), measured on
the physical support, has \(L^2\) norm
\(O_\lambda(\varepsilon+\sqrt{p\varepsilon})=O_\lambda(p^{7/2})\):
a residue fiber meets an endpoint collar only on a residue
set of length \(O(\varepsilon)\), and there are
\(O_\lambda(1/p)\) copies. Similarly \(W_p-pM_p\) is
\(O(p)\) only on those residue sets. Subtracting (5) from
(21), with \(W_p,pM_p\ge\lambda/2\), gives uniformly in phase
\[
\|(f_p-f_*)-h_p\|_2=O_\lambda(p^3). \tag{23}
\]
Since \(Q\) is a bounded quadratic form on zero-mean \(L^2\),
\[
C(f_p)-C_\lambda
=Q(h_p)+O_\lambda(p^3\|h_p\|_2+p^6). \tag{24}
\]
Equation (15) implies \(\|h_p\|_2=O_\lambda(p)\) in general,
and (16) gives \(\|h_p\|_2=O_\lambda(p^2)\) at
\(d_p=O(p^2)\). Combining (19), (23)--(24) gives
\[
I_\lambda(p)=\|h_p\|_2^2+O_\lambda(p^4)
\quad\text{uniformly in phase}, \tag{25}
\]
and the *stronger* \(I_\lambda(p)=\|h_p\|_2^2+O_\lambda(p^5)\)
when \(d_p=O(p^2)\). Equations (15)--(16) now prove
Theorems A and B. All upper-bound competitors are exactly
source-admissible, smooth, positive, even and normalized.

## 5. Stress tests, prior art, and the RH-facing boundary

**Algebraic controls.** At \(\theta_p=0\), (11) reduces to
\(K_*(k/p)=(-1)^{q_pk+1}p^2/(2\pi^2k^2-p^2)\), exactly
the commensurate identity of WI-448; (3) recovers its
\(1/(180\lambda)\) leading constant. At \(\theta_p=1/2\),
(8) has maximal phase discrepancy, and the quadratic
coefficient is strictly positive. A generic claim of a universal
quartic lattice cost is therefore false. The proof keeps
\(pM_p\) instead of replacing it silently by \(\lambda\), and
keeps both positive and negative Fourier modes in (13).
Changing the Fourier convention or forgetting the second sign
would alter the constant.

**Independent numerical falsification checks.** Using the exact
fiber formula (6) and Gauss--Legendre quadrature of each of the
two support-count sectors, at \(\lambda=0.75\),
\(A_\lambda=1.2059249870\ldots\), and
\(\theta_p=0.3\), the computed ratios
\(\|h_p\|_2^2/p^2\) for \(q_p=10,30,60,100\) are
\(0.38971,0.40090,0.40398,0.40525\), approaching the
predicted \(0.40719142\ldots\). Along
\(\theta_p=4(0.75/q_p)^2\), the ratios
\(\|h_p\|_2^2/p^4\) for \(q_p=10,30,80,200\) are
\(6.82469,7.44548,7.64529,7.71642\), approaching
the predicted \(7.76343447\ldots\). These are checks of
the explicit least-\(L^2\) **proxy**, not numerical
optimization over all smooth competitors; sharpness itself
comes from (19)--(25).

**Literature boundary.** Wang supplies \(f_*,C\), the exact
second variation and source-admissible smooth test class.
Periodization/Poisson summation, fiberwise Hilbert projection,
endpoint quadrature discrepancy, Fourier-series Parseval and
the \(\zeta(4)\) sum are classical tools; see, for example,
E. M. Stein and R. Shakarchi, *Fourier Analysis: An
Introduction* (Princeton, 2003). The general spectral-set/
tiling literature is neighboring prior art, not evidence
that this source-specific cost has independent priority.
A targeted search did not identify this exact Wang-window
fractional-phase coefficient; no novelty or priority claim
is made. This is an exact specialization/assembly of classical
Fourier machinery, not a new zeta theorem.

**Scope.** The asymptotic fixes \(\lambda\) and sends
\(p\downarrow0\); in the zeta application, Wang first fixes
each admissible smooth test and lets \(T\to\infty\).
No uniform estimate for a \(T\)-dependent choice \(p(T)\),
no source-justified zeta-zero lattice geometry, no extra
prime-side correlation moment, and no treatment of the
indefinite conjugate off-line Weil blocks is supplied.
The quadratic endpoint tariff and its quartic crossover
therefore exclude no individual off-critical zero, do not
improve the unconditional simple-critical proportion,
and **do not establish RH**.

**Consequence for Weil inertia.** WI-448's commensurate
\(p^4/(180\lambda)\) escape is a thin arithmetic resonance
in the ratio of support length to lattice period, not a
general law for near-optimal smooth Fourier-lattice tests.
The exact obstruction is a support-fiber count variance
controlled by the optimizer's nonzero endpoint height.
Even that positive tariff remains a real-frequency
model cost: preserving it through the source-side
short-interval estimate and off-line indefinite blocks
would require an additional arithmetic coercivity argument.
