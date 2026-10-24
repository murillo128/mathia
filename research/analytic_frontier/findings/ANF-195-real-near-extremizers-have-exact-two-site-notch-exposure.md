# ANF-195 — Real near-extremizers have exactly the two-site notch-exposure envelope

**Status:** EXACT-DERIVED + SHARP-REAL-ENVELOPE + ZERO-SET-PACKING + SOURCE-SPECIFIC-LOCALIZATION + POSITIVE-FOURIER-PROFILE-CLASS + FINITE-EXCESS-MODULUS + AUTOMATIC-FOURIER-TAIL + SQUARE-ROOT-REAL-STABILITY + GENERIC-SHARP-RATE + SOBOLEV-PROFILE-EXTENSION. This is a theorem for real conjugation-invariant multisets only, not the unrestricted complex near-extremizer envelope of ANF-099.

## 1. Sharp statement for every fixed triangular notch

Use the Montgomery--Taylor conventions of ANF-087 and ANF-099:
\[
J_0=g*g,\quad K=\widehat g,\quad F_{\rm MT}(t)=K(t)^2\ge0
\quad(t\in\mathbb R),\quad K(0)=1,
\]
where \(g(u)=\cos(\sqrt2u)/(\sqrt2\sin(1/\sqrt2))\) on \([-1/2,1/2]\), zero elsewhere. Let \(0<\eta<1\), and freeze an admissible triangular notch
\[
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,\qquad
b_\eta>0,\qquad 0\le\phi_\eta\le J_0.
\]
Its real Fourier kernel is nonnegative and summably decaying:
\[
\Phi_\eta(t)=\widehat{\phi_\eta}(t)
=b_\eta\eta\,\operatorname{sinc}^2(\eta t)
\ge0,\quad
\Phi_\eta(0)=b_\eta\eta,\quad
0\le\Phi_\eta(t)\ll_\eta(1+t^2)^{-1},
\]
with \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\).

For any finite nonempty **real** multiset \(W\), write
\[
L(W)=2|W|-\sigma(W),\quad
e(W)=\frac{\int J_0|S_W|^2}{L(W)}-1,\quad
h_\eta(W)=\frac{\int\phi_\eta|S_W|^2}{L(W)},
\qquad
S_W(\alpha)=\sum_{x\in W}e^{-2\pi i\alpha x}.
\]
Here \(\sigma(W)\) counts distinct real support sites of multiplicity one. Restrict ANF-099's envelope to real multisets:
\[
\beta_\eta^{\mathbb R}
:=\lim_{\varepsilon\downarrow0}
\sup_{\substack{W\subset\mathbb R\ {\rm finite}\\e(W)\le\varepsilon}}
h_\eta(W).
\]
Let \(Z_+(K)=\{r>0:K(r)=0\}\). Then the exact all-cardinality, all-multiplicity identity is
\[
\boxed{\displaystyle
\beta_\eta^{\mathbb R}
=\Phi_\eta(0)+\max_{r\in Z_+(K)}\Phi_\eta(r)
=b_\eta\eta\left[1+
\max_{n\ge1}\operatorname{sinc}^2(\eta r_n)\right],
}\tag{1}
\]
where \(r_n=n+\delta_n\), \(0<\delta_n<1/2\), are the positive zeros identified in ANF-087. The maximum exists: \(\Phi_\eta(r_n)\to0\), and at least one value is positive.

In particular, **growing real cardinality, unbounded real span, and unbounded real multiplicities cannot increase the limiting normalized notch exposure beyond an exact two-site real equality configuration**. This does not bound the corresponding envelope over complex multisets.

For each fixed triangular notch the convergence has the uniform rate
\(h_\eta(W)\le\beta_\eta^{\mathbb R}+C_\eta\sqrt{e(W)}\) for
\(0\le e(W)\le1\), proved in section 9. Section 8 shows that the exponent
\(1/2\) is optimal outside an at-most-countable set of notch widths.
Section 10 extends the square-root upper rate to every fixed dominated
positive-Fourier profile with one square-integrable weak derivative and
positive maximum exposure on the source zero set. This includes profiles
without any inverse-square pointwise Fourier bound.

## 2. Exact excess and removal of exceptional real sites

Write the distinct real support sites as \(x_i\) with multiplicities \(m_i\ge1\). Define
\[
\ell(m)=\begin{cases}1,&m=1,\\2m,&m\ge2.\end{cases}
\qquad L=\sum_i\ell(m_i).
\]
The positivity of \(K(t)^2\) on the real line gives the exact identity
\[
\Delta:=L e(W)
=\sum_{m_i\ge3}m_i(m_i-2)
+2\sum_{i<j}m_i m_jK(x_i-x_j)^2
\ge0.
\tag{2}
\]
Moreover,
\[
E_\eta(W):=\int\phi_\eta|S_W|^2
=\Phi_\eta(0)\sum_i m_i^2
+2\sum_{i<j}m_i m_j\Phi_\eta(x_i-x_j).
\tag{3}
\]
Every summand in (3) is nonnegative. The portion \(B_0\) of \(W\) at sites of multiplicity at least three has
\[
L(B_0)\le2\Delta,\qquad
E_0(B_0):=\int J_0|S_{B_0}|^2\le L(B_0)+\Delta.
\tag{4}
\]
The second inequality holds because the diagonal integer surplus and all off-diagonal \(K^2\) interactions of \(B_0\) are subterms of the nonnegative right side of (2).

On the remaining \(m_i\in\{1,2\}\) sites let
\[
D_i=\sum_{j\ne i}m_j K(x_i-x_j)^2.
\]
The corresponding excess \(\Delta_1\le\Delta\) obeys
\(\sum_i m_iD_i=\Delta_1\). Fix any \(\gamma>0\). Mark vertices with \(D_i>\gamma\) as \(B_1\). Since \(m_i^2\le2m_i\) for \(m_i=1,2\),
\[
L(B_1)=\sum_{i\in B_1}m_i^2
\le\frac{2\Delta_1}{\gamma}\le\frac{2\Delta}{\gamma}.
\tag{5}
\]
For the union \(B=B_0\sqcup B_1\) (whole support fibers, so \(L\) is additive),
\[
L(B)\le(2+2/\gamma)\Delta,\qquad
E_0(B)\le L(B)+\Delta,\qquad E_\eta(B)\le E_0(B).
\tag{6}
\]
The last inequality is the spectral domination \(0\le\phi_\eta\le J_0\). Write \(G=W\setminus B\). Positivity of every real \(K^2\) pair gives
\[
E_\eta(G)\le E_0(G)\le L(G)+\Delta.
\tag{7}
\]
The norm triangle inequality for the \(\phi_\eta\)-weighted exponential sums yields
\[
\sqrt{E_\eta(W)}
\le\sqrt{E_\eta(G)}+\sqrt{E_\eta(B)}.
\tag{8}
\]
Consequently, along any family with \(e(W)=\Delta/L\to0\), for each *fixed* \(\gamma>0\),
\[
L(G)/L\to1,\qquad
E_\eta(W)/L\le E_\eta(G)/L+o_\gamma(1).
\tag{9}
\]
No bounded-cardinality or compact-support assumption entered this removal. Every surviving site has multiplicity one or two and \(D_i\le\gamma\); in particular each distinct surviving pair obeys \(K(x_i-x_j)^2\le\gamma\).

## 3. The far notch tail is uniformly negligible

Choose a small fixed cell width \(h>0\) and \(\kappa>0\) such that
\(K(t)^2\ge\kappa\) whenever \(|t|\le h\); this is possible by continuity and \(K(0)=1\). Divide the real axis into half-open cells \(I_k=[kh,(k+1)h)\). For \(G\), set \(M_k=\sum_{x_i\in I_k}m_i\). Since the surviving multiplicities are one or two, its diagonal source energy equals \(L(G)=\sum_i m_i^2\). The within-cell part of (2) proves
\[
\sum_k M_k^2
\le L(G)+\frac{\Delta(G)}{\kappa}
\le L(G)+\frac{\Delta}{\kappa}.
\tag{10}
\]
For a fixed \(T>2h\), two sites separated by more than \(T\) must lie in cells at offset \(|k-l|>T/h-1\). Using \(\Phi_\eta(t)\ll_\eta(1+t^2)^{-1}\), cellwise Cauchy--Schwarz, and the summable inverse-square tail gives
\[
2\!\sum_{\substack{i<j\ {\rm in}\ G\\|x_i-x_j|>T}}
m_i m_j\Phi_\eta(x_i-x_j)
\ll_{\eta,h}
\frac{L(G)+\Delta/\kappa}{T}
\quad (T>4h).
\tag{11}
\]
This includes arbitrarily dense starting configurations: their square occupancy was paid for by the actual positive \(K^2\) source energy in (10).

## 4. Sum-free zero geometry makes the remaining near graph a matching

Fix \(T>4h\). ANF-087 proved that \(Z_+(K)\) is *sum-free*: no positive \(u,v\) have \(u,v,u+v\in Z_+(K)\). Therefore no three distinct real points have all their nonzero pairwise differences in the zero set. By continuity and compactness,
\[
c_T:=\min_{u,v\in[-T,T]}
\max\{K(u)^2,K(v)^2,K(u-v)^2\}>0.
\tag{12}
\]
The minimum cannot be zero: if it were, the triple \(\{0,u,v\}\) would have zero interaction on all three differences; the degenerate cases \(u=0\), \(v=0\), \(u=v\) are excluded automatically by \(K(0)=1\).

For any fixed \(\xi>0\), compactness also gives a \(\gamma_{T,\xi}>0\) such that
\[
0<|t|\le T,\ K(t)^2\le\gamma_{T,\xi}
\quad\Longrightarrow\quad
\Phi_\eta(t)\le M_\eta+\xi,\qquad
M_\eta:=\max_{r\in Z_+(K)}\Phi_\eta(r).
\tag{13}
\]
Choose \(0<\gamma<\min(c_T,\gamma_{T,\xi})\) in the removal of section 2. Join surviving vertices when their distance is at most \(T\). Every vertex has degree at most one: if \(x_i\) had distinct neighbors \(x_j,x_k\), then \(u=x_j-x_i\) and \(v=x_k-x_i\) lie in \([-T,T]\), and all three values of \(K^2\) in (12) would be at most \(\gamma\), because every good-site pair has \(K^2\le\gamma\). This contradicts (12). The near graph is a matching.

Each near edge thus satisfies (13), and \(2m_i m_j\le m_i^2+m_j^2\). Since the matching edges are vertex-disjoint,
\[
2\!\sum_{\substack{i<j\ {\rm in}\ G\\|x_i-x_j|\le T}}
m_i m_j\Phi_\eta(x_i-x_j)
\le(M_\eta+\xi)\sum_i m_i^2
=(M_\eta+\xi)L(G).
\tag{14}
\]
Combine (3), (11) and (14):
\[
E_\eta(G)
\le\left[\Phi_\eta(0)+M_\eta+\xi+
O_{\eta,h}(1/T)(1+\Delta/(\kappa L(G)))\right]L(G).
\tag{15}
\]
Now take a near-extremizing family \(e(W)\to0\), using the fixed \(\gamma\) chosen after \(T,\xi\). Equations (9) and (15) give
\[
\limsup h_\eta(W)\le\Phi_\eta(0)+M_\eta+\xi+O_{\eta,h}(1/T).
\]
First let \(T\to\infty\), then \(\xi\downarrow0\), proving
\[
\beta_\eta^{\mathbb R}\le\Phi_\eta(0)+M_\eta.
\tag{16}
\]

For the opposite inequality, choose any \(r\in Z_+(K)\) and take the two distinct simple real sites \(W=\{0,r\}\). They have \(L(W)=2\), \(E_0(W)=2\), and therefore \(e(W)=0\), while (3) gives
\[
h_\eta(\{0,r\})=\Phi_\eta(0)+\Phi_\eta(r).
\tag{17}
\]
Choosing a maximizing zero gives equality in (16), completing (1).


## 5. Automatic Fourier-tail control and a finite-excess envelope

The two-site mechanism is not tied to a triangular notch. Let \(\phi\) be any **fixed**, real, even, integrable profile satisfying \(0\le\phi\le J_0\) almost everywhere, and write \(\Phi=\widehat\phi\). Assume only \(\Phi(t)\ge0\) for every real \(t\), and fix any sufficiently small \(h>0\) for which \(\kappa:=\inf_{|t|\le h}K(t)^2>0\). The cellwise Fourier-tail hypothesis previously needed for the proof is **automatic**:
\[
\boxed{\displaystyle
\sum_{n\in\mathbb Z}\sup_{|s-nh|\le h}\Phi(s)<\infty.}
\tag{18}
\]
No pointwise polynomial-decay or smoothness assumption on \(\phi\) is needed.

Here is a direct proof, including the absence of any hidden regularity condition. Since \(0\le\phi\le J_0\), the profile is bounded and supported in \([-1,1]\). For \(R>0\), Fourier inversion against a Gaussian gives
\[
0\le\int_{\mathbb R}\Phi(t)e^{-\pi t^2/R^2}\,dt
=\int_{\mathbb R}\phi(u)R e^{-\pi R^2u^2}\,du
\le\|\phi\|_\infty\le\|J_0\|_\infty.
\tag{18a}
\]
As \(R\to\infty\), monotone convergence and \(\Phi\ge0\) imply
\(\|\Phi\|_{L^1}\le\|\phi\|_\infty\). Choose a Schwartz function \(\psi\) whose Fourier transform equals one on a neighborhood of \([-1,1]\). Because the inverse Fourier transform of \(\Phi\) is supported there, the bandlimited reproduction identity holds (first distributionally and then pointwise):
\[
\Phi=\Phi*\psi.
\tag{18b}
\]
For every fixed \(h>0\), rapid decay of \(\psi\) gives the finite constant
\[
C_{h,\psi}:=\sup_{y\in\mathbb R}
\sum_{n\in\mathbb Z}\sup_{|s-nh|\le h}|\psi(s-y)|<\infty.
\]
Using positivity to take the integral before the discrete sum,
\[
\sum_{n\in\mathbb Z}\sup_{|s-nh|\le h}\Phi(s)
\le\int_{\mathbb R}\Phi(y)
\sum_{n\in\mathbb Z}\sup_{|s-nh|\le h}|\psi(s-y)|\,dy
\le C_{h,\psi}\|J_0\|_\infty.
\tag{18c}
\]
This establishes (18) for **every** dominated nonnegative-Fourier profile. The argument is the standard bandlimited \(L^1\)-to-local-supremum (Wiener-amalgam) estimate, proved here in the exact normalization required for the source-energy tail. Define \(h_\phi(W)\) and \(\beta_\phi^{\mathbb R}\) as in section 1, replacing \(\phi_\eta\) by \(\phi\), and put

\[
M_\phi:=\max_{r\in Z_+(K)}\Phi(r).
\]
The maximum exists because the positive zeros \(r_n\to\infty\) are discrete, \(\Phi(r_n)\to0\), and \(\Phi\ge0\) (if every value vanishes, any zero maximizes). Then

\[
\boxed{\displaystyle
\beta_\phi^{\mathbb R}=\Phi(0)+M_\phi.}
\tag{19}
\]

There is also a **uniform finite-excess inequality**. For \(T>4h\) let

\[
\omega_{\Phi,h}(T):=
\sum_{\substack{n\in\mathbb Z\\|n|>T/h-1}}
\sup_{|s-nh|\le h}\Phi(s),
\qquad \omega_{\Phi,h}(T)\longrightarrow0.
\tag{20}
\]
For any \(\xi>0\), compactness and the sum-free zero-set result of ANF-087 allow a number
\(\gamma=\gamma(T,\xi,\Phi,K)>0\) such that

\[
\gamma<c_T,\qquad
0<|t|\le T,\ K(t)^2\le\gamma
\ \Longrightarrow\ \Phi(t)\le M_\phi+\xi,
\tag{21}
\]
where \(c_T>0\) is defined by (12). For **every** nonempty finite real multiset \(W\), of arbitrary size, span and multiplicities, write \(e=e(W)\ge0\). Then

\[
\boxed{\displaystyle
h_\phi(W)\le
\left[
\sqrt{\Phi(0)+M_\phi+\xi+
          \omega_{\Phi,h}(T)(1+e/\kappa)}
+\sqrt{(3+2/\gamma)e}
\right]^2.}
\tag{22}
\]

**Proof.** The integer diagonal surplus and positive \(K^2\) terms in (2) do not depend on the notch. Apply exactly the whole-site deletion in section 2 at threshold \(\gamma\), obtaining \(W=G\sqcup B\) and
\[
L(B)\le(2+2/\gamma)\Delta,\qquad
E_\phi(B)\le E_0(B)\le L(B)+\Delta
\le(3+2/\gamma)\Delta.
\tag{23}
\]
Here \(E_\phi=\int\phi|S|^2\), and the first inequality for \(E_\phi\) uses pointwise domination \(0\le\phi\le J_0\), not merely Fourier positivity.

For the good sites, the cell-mass argument (10) remains
\(\sum_k M_k^2\le L(G)+\Delta/\kappa\).
If \(x_i\) lies in cell \(k\) and \(x_j\) in cell \(k+n\), their distance differs from \(nh\) by at most \(h\). A pair at distance \(>T\) necessarily has \(|n|>T/h-1\). Therefore the ordered far-pair energy, including both orientations, satisfies

\[
2\!\!\sum_{\substack{i<j\ {\rm in}\ G\\|x_i-x_j|>T}}
m_im_j\Phi(x_i-x_j)
\le\omega_{\Phi,h}(T)\sum_k M_k^2
\le\omega_{\Phi,h}(T)\bigl(L(G)+\Delta/\kappa\bigr).
\tag{24}
\]

By (12) and (21), the near graph is still a matching and each of its edges has \(\Phi(x_i-x_j)\le M_\phi+\xi\). Equation (14), with \(\Phi\) in place of \(\Phi_\eta\), consequently gives

\[
E_\phi(G)\le
(\Phi(0)+M_\phi+\xi)L(G)
+\omega_{\Phi,h}(T)(L(G)+\Delta/\kappa).
\tag{25}
\]
The \(L^2(\phi\,d\alpha)\) triangle inequality for \(S_W=S_G+S_B\), (23), \(L(G)\le L(W)\), and \(\Delta=eL(W)\) prove (22). Let \(e\downarrow0\) at fixed \(T,\xi,\gamma\), then \(T\to\infty\) and \(\xi\downarrow0\). This proves the upper bound in (19) uniformly over all real configurations; the real two-site equality configurations \(W=\{0,r\}\) attain \(\Phi(0)+\Phi(r)\) at \(e=0\), proving sharpness. No new zero-set or compactness theorem is assumed.

The admissible cone contains genuinely nontriangular profiles. If \(f\ge0\) is nonzero, even and \(C_c^\infty(-\eta/2,\eta/2)\), \(0<\eta<1\), take
\[
\phi=c(f*\widetilde f),\quad \widetilde f(u)=f(-u),\quad
\Phi(t)=c|\widehat f(t)|^2\ge0,
\tag{26}
\]
with \(c>0\) small enough that \(\phi\le J_0\). This is possible because \(J_0>0\) on \([-\eta,\eta]\), and \(\Phi\) decays faster than any power. For positive mixtures that still satisfy domination and (18), the sharp formula reads
\[
\beta_{\sum_j a_j\phi_j}^{\mathbb R}
=\sum_j a_j\Phi_j(0)
+\max_{r\in Z_+(K)}\sum_j a_j\Phi_j(r)
\le\sum_j a_j\beta_{\phi_j}^{\mathbb R}
\quad(a_j\ge0).
\tag{27}
\]
Thus optimizing a *fixed real* notch shape uses a shared zero location, not separate optimal locations for its components.

**Boundary and novelty.** Equations (19)--(27) strengthen the same real two-site envelope claim from triangular notches to a summable positive-Fourier profile class and expose a finite-excess bound. They reuse the ANF-087 sum-free zeros and ANF-195 deletion/matching proof; they do not establish a new classical zeta theorem. The summable local Fourier envelope (18) is a consequence of compact support, bounded domination and Fourier nonnegativity, not an extra hypothesis. The Fourier reproduction/amalgam estimate is classical; the local improvement is removing an artificial condition from the full real two-site envelope and its finite-excess bound. The profile is fixed before \(e\downarrow0\): neither \(\gamma(T,\xi)\) nor the proof is asserted uniform for profile families with changing support or Fourier tails. Most importantly, the extension remains **real-only**; it does not control the unrestricted complex near-extremizer envelope in ANF-099 or supply an improved unconditional critical-zero proportion.

## 6. Relevance, prior art and audit boundary

The exact two-site equality class and sum-free Montgomery--Taylor zero set are existing Mathia results (ANF-087), based on the classical extremizer and Lamzouri's positive Hilbert-space inequality already anchored in SOURCES.md. The scalar near-extremizer envelope is ANF-099; ANF-081 previously certified one improving notch against *all* real multiplicity profiles, while ANF-105--ANF-106 supply related profile-decoupling and bounded-strip localization. The **local conclusions** are the exact real-restricted all-cardinality envelope (1), its positive-Fourier extension (19), and the finite-excess modulus (22), not a new classical pair-correlation, point-process or zero-free theorem. The proof adds a direct local matching extraction from small positive \(K^2\) excess, with a source-paid cell-occupancy tail, so no new external theorem is load-bearing. The relevant external literature audit by zero-set packing, near-extremal positive-type pair energies and Montgomery--Taylor notch language did not identify a direct version; this is not a global novelty claim.

To falsify (1), check the integer multiplicity surplus and the coefficient \(2m_i m_j\) in (2)--(3), the weighted incident-energy identity before discarding exceptional sites, the positivity/decay of \(\widehat{\phi_\eta}\), the \(\ell^2\) occupancy estimate (10), the compact no-zero-triple implication (12), and the matching normalization \(2m_i m_j\le m_i^2+m_j^2\). The order of limits is essential: first \(e\to0\) with \(T,\xi,\gamma\) fixed, then \(T\to\infty\), then \(\xi\to0\).

This **does not** show that the unrestricted \(\beta_\eta\) of ANF-099 equals its real restriction. Real multisets form only a subclass of conjugation-invariant complex multisets, and the near-extremal Hilbert deficit need not control the height or physical source tensor uniformly when cardinality and span grow. Thus the fixed-notch RH-facing obstruction remains: rule out genuinely nonreal near-extremizers with exposure at least \(B_\eta\), or construct one. No new proportion of critical zeta zeros, global zeta-zero exclusion or RH result follows.

## 7. Uniform cubic-root finite-excess stability for a fixed triangular notch

The qualitative envelope (1) admits a rate uniform in the number of real sites, their multiplicities, and their diameter. For each **fixed** admissible triangular notch from section 1, there is a constant \(C_\eta<\infty\) such that every nonempty finite real multiset \(W\) with \(0\le e(W)\le1\) satisfies

\[
\boxed{\displaystyle
h_\eta(W)\le \Phi_\eta(0)+M_\eta+C_\eta e(W)^{1/3}.}
\tag{28}
\]

This gives a direct scale-dependent version of the general finite-excess bound (22). Section 9 strengthens the exponent to \(1/2\) by controlling interactions with both endpoints of each bounded pair.

**Uniform near-zero estimate.** The triangular Fourier kernel has \(\Phi_\eta(t)\to0\) as \(|t|\to\infty\), and \(M_\eta>0\). All real zeros of \(K\) are simple and locally finite (ANF-087; its removable numerator zero is *not* a zero of \(K\)). Consequently there exists \(A_\eta<\infty\) such that

\[
\Phi_\eta(t)\le M_\eta+A_\eta|K(t)|
\qquad(t\in\mathbb R).
\tag{29}
\]

For completeness, choose \(R\) with \(\Phi_\eta(t)\le M_\eta\) outside \([-R,R]\). Near each zero \(r\) inside this compact interval, the Lipschitz continuity of \(\Phi_\eta\), the inequality \(\Phi_\eta(r)\le M_\eta\), and the simple-zero bound \(|K(t)|\ge c_r|t-r|\) prove (29). On the compact set remaining after those neighborhoods are removed, \(|K|\) has a positive minimum. This also covers negative zeros by evenness.

**Effective deletion and matching.** Fix \(T\ge1\) and take

\[
\gamma_T=\frac{1}{96(1+8\pi^2T^2)^2},\qquad
\Delta=L(W)e(W).
\tag{30}
\]

Apply the whole-support-fiber deletion in (2)--(6), with \(\gamma=\gamma_T\), writing \(W=G\sqcup B\). All surviving multiplicities are one or two, every distinct surviving pair has \(K(x_i-x_j)^2\le\gamma_T\), and

\[
L(B)\le(2+2/\gamma_T)\Delta,\qquad
E_\eta(B)\le(3+2/\gamma_T)\Delta.
\tag{31}
\]

ANF-114 gives the quantitative triple gap
\[
\inf_{\substack{u,v\ge0\\u+v\le2T}}
\bigl(K(u)^2+K(v)^2+K(u+v)^2\bigr)
\ge\frac{1}{16(1+8\pi^2T^2)^2}
=6\gamma_T.
\tag{32}
\]
If one surviving site had two other surviving sites at distance at most \(T\), the three sites would have span at most \(2T\), and all three pair-kernel squares would be at most \(\gamma_T\). Their sum would be at most \(3\gamma_T\), contradicting (32). The distance-\(T\) graph on the good sites is therefore a matching. In particular *every interval of length \(T\) contains at most two distinct good sites*.

**Sparse Fourier potentials.** Since \(\Phi_\eta(t)\ll_\eta(1+t^2)^{-1}\) and every good site has multiplicity at most two, the preceding interval packing gives, uniformly for \(T\ge1\),

\[
\sup_{y\in\mathbb R}\sum_{j\in G}m_j\Phi_\eta(y-x_j)
\ll_\eta1,\qquad
\sup_{i\in G}\sum_{\substack{j\in G\\|x_i-x_j|>T}}
m_j\Phi_\eta(x_i-x_j)
\ll_\eta T^{-2}.
\tag{33}
\]

Indeed, partition each half-line from the chosen center into intervals of length \(T\). Each interval contains at most two sites of multiplicity at most two. The two nearest intervals contribute \(O_\eta(1)\) to the first sum, and the remaining intervals contribute \(O_\eta(\sum_{n\ge1}(nT)^{-2})\). In the second sum the nearest retained interval is already at distance \(T\), giving \(O_\eta(T^{-2})\).

**Direct cross-interaction bound and optimization.** All terms of (3) are nonnegative, so the mixed good--bad interaction can be estimated *without* using the norm triangle inequality. By (33) and \(m_i\le\ell(m_i)\),

\[
2\sum_{i\in B,\ j\in G}m_im_j\Phi_\eta(x_i-x_j)
\ll_\eta\sum_{i\in B}m_i
\le L(B)\ll\Delta/\gamma_T.
\tag{34}
\]

Each edge of the good matching has \(\Phi_\eta(x_i-x_j)\le M_\eta+A_\eta\sqrt{\gamma_T}\) by (29). As \(2m_im_j\le m_i^2+m_j^2\) and matching edges are disjoint, their total ordered off-diagonal energy is at most \((M_\eta+A_\eta\sqrt{\gamma_T})L(G)\). The second part of (33) bounds every farther pair, yielding

\[
E_\eta(G)\le
\bigl[\Phi_\eta(0)+M_\eta+
O_\eta(\sqrt{\gamma_T}+T^{-2})\bigr]L(G).
\tag{35}
\]

Use (31), (34), (35), \(L(G)\le L(W)\), and \(\Delta=e(W)L(W)\). Since \(\sqrt{\gamma_T}\ll T^{-2}\) and \(\gamma_T^{-1}\ll T^4\) for \(T\ge1\),

\[
h_\eta(W)-\Phi_\eta(0)-M_\eta
\ll_\eta T^{-2}+e(W)T^4.
\tag{36}
\]

For \(0<e(W)\le1\), set \(T=e(W)^{-1/6}\); both terms become \(e(W)^{1/3}\). For \(e(W)=0\), (1) already gives the exact upper bound (alternatively let \(T\to\infty\) in (36)). This completes (28).

**Audit and scope.** The improvement over (22) has two load-bearing ingredients: ANF-114's explicit \(T^{-4}\) triple-gap scale forces a \(T\)-matching after deletion at cost \(O(eT^4)\); the resulting good-site packing makes the far triangular Fourier potential \(O(T^{-2})\) and the bad--good potential bounded linearly by deleted source mass. Neither ingredient follows from arbitrary positive-definite kernels without the actual Montgomery--Taylor zero geometry. The estimate is restricted to the fixed triangular notch and **real** multisets: a general positive-Fourier profile in section 5 need not have a quadratic pointwise tail, and nonreal near-extremizers are not controlled by this positive real pair-energy decomposition. The background Hilbert inequality is Lamzouri's Proposition 2.1, and the remaining packing and potential estimates are elementary; no new external theorem or RH-facing zero-location consequence is claimed. A targeted check of the Montgomery--Taylor/Hilbert-space pair-correlation literature and quantitative near-extremal packing did not locate this exact finite-real stability modulus, without establishing a global novelty claim.

## 8. Generic square-root lower obstruction for the real stability rate

The uniform exponent cannot exceed \(1/2\) for a full-measure set of fixed triangular-notch widths \(\eta\), **even if one restricts to two distinct simple real points**. Together with section 9 this proves generic sharpness of the square-root rate.

Let \(s(y)=\operatorname{sinc}(y)=\sin(\pi y)/(\pi y)\), and choose a maximizing positive zero \(r_*\in Z_+(K)\) with
\[
\Phi_\eta(r_*)=M_\eta>0.
\]
If \(\Phi_\eta'(r_*)\ne0\), take \(W_\delta=\{0,r_*+\delta\}\) with \(\delta\) tending to zero from the side on which \(\delta\Phi_\eta'(r_*)>0\). The exact two-site normalizations from (2)--(3) are
\[
L(W_\delta)=2,\qquad
e(W_\delta)=K(r_*+\delta)^2,\qquad
h_\eta(W_\delta)=\Phi_\eta(0)+\Phi_\eta(r_*+\delta).
\tag{37}
\]
Every *true* positive zero \(r\) of \(K\) is simple. Indeed, with the numerator and denominator of ANF-114,
\[
N(t)=\cos(\pi t)-a t\sin(\pi t),\quad
D(t)=1-2\pi^2t^2,\quad
a=\sqrt2\pi\cot(1/\sqrt2)>0,
\]
the equality \(N(r)=0\) forces \(\sin(\pi r)\ne0\), while
\[
N'(r)=-\bigl(\pi+a+a^2\pi r^2\bigr)\sin(\pi r)\ne0.
\]
The removable numerator/denominator coincidence is not a zero of \(K\), so \(D(r)\ne0\) at every true zero and \(K'(r)=N'(r)/D(r)\ne0\). Taylor expansion in (37) therefore yields
\[
e(W_\delta)=K'(r_*)^2\delta^2+O(\delta^3),\qquad
h_\eta(W_\delta)-\beta_\eta^{\mathbb R}
=\Phi_\eta'(r_*)\delta+O(\delta^2),
\]
and hence the **positive** limiting ratio
\[
\boxed{\displaystyle
\lim_{\substack{\delta\to0\\ \delta\Phi_\eta'(r_*)>0}}
\frac{h_\eta(W_\delta)-\beta_\eta^{\mathbb R}}
{\sqrt{e(W_\delta)}}=
\frac{|\Phi_\eta'(r_*)|}{|K'(r_*)|}>0.}
\tag{38}
\]
Consequently no bound \(h_\eta(W)\le\beta_\eta^{\mathbb R}+C_\eta e(W)^p\) with \(p>1/2\) and finite \(C_\eta\) can hold uniformly over finite real multisets for such a notch.

This nonstationarity is generic in \(\eta\). Since
\[
\Phi_\eta'(t)=2b_\eta\eta^2s(\eta t)s'(\eta t),
\]
a maximizing zero always has \(s(\eta r_*)\ne0\). The positive zeros of \(s'\), equivalently the nonzero solutions of \(\tan(\pi y)=\pi y\), form a discrete countable set. The positive zeros \(r_n\) of \(K\) are also countable. Thus all widths for which **any** maximizing zero could have \(\Phi_\eta'(r_n)=0\) lie in the at-most-countable set
\[
\mathcal E=\{\eta\in(0,1):\eta r_n\text{ is a positive zero of }s'
\text{ for some }n\}.
\tag{39}
\]
For every \(\eta\in(0,1)\setminus\mathcal E\), (38) holds at each maximizing zero. There is an explicit nonempty interval without exceptions: for \(0<\eta<1/(2r_1)\), \(r_1\) is the unique maximizing positive zero, because \(s(y)^2\) decreases strictly on \(0<y<1\), while \(s(y)^2\le1/\pi^2<4/\pi^2\le s(\eta r_1)^2\) for \(y\ge1\). Here \(s'(\eta r_1)<0\).

**Audit and significance.** The mechanism is elementary first-order perturbation of the *actual equality pair*, not a high-cardinality construction or a new zeta theorem. It identifies the ceiling \(p=1/2\) attained by section 9 at generic fixed widths. The argument requires a **fixed** notch width and real two-site configurations; it does not transfer to nonreal multisets or improve unconditional critical-zero proportions. The two-site normalization and zero simplicity are already available in ANF-195 and ANF-114, and the Taylor/sharpness mechanism is elementary; no separate claim of literature novelty is made.

## 9. Paired source control gives the sharp square-root upper rate

For every fixed admissible triangular notch there are finite constants
\(A_\eta,B_\eta^*>0\), independent of cardinality, multiplicity and span, such that
every nonempty finite real multiset satisfies
\[
\boxed{\displaystyle
h_\eta(W)\le\beta_\eta^{\mathbb R}
 +A_\eta\sqrt{e(W)}+B_\eta^*e(W).}
\tag{40}
\]
Here \(A_\eta\) may be the constant in (29); \(B_\eta^*\) is unrelated to
ANF-099's analytic notch threshold. In particular (40) gives a uniform
\(O_\eta(\sqrt e)\) modulus for \(0\le e\le1\). The exponent is optimal
whenever a maximizing zero is nonstationary for \(\Phi_\eta\), including every
width outside the countable exceptional set (39).

### Two translates of the source kernel control the full inverse-square tail

Freeze \(R>r_1\). There are a neighborhood \(\mathcal U_R\) of the finitely
many positive zeros of \(K\) in \([0,R]\) and a constant \(d_R>0\) such that
\[
K(t)^2+K(t-r)^2\ge\frac{d_R}{1+t^2}
\qquad(t\in\mathbb R,\ r\in\mathcal U_R).
\tag{41}
\]
The neighborhood can be chosen bounded in \((0,R+1)\).

To prove this, use the exact kernel formula from section 8. With
\(c=a/(2\pi^2)>0\), it gives
\[
K(t)=c\frac{\sin(\pi t)}{t}+O(t^{-2}),\qquad |t|\to\infty.
\tag{42}
\]
Uniformly for bounded \(r\), therefore,
\[
t^2\bigl(K(t)^2+K(t-r)^2\bigr)
=c^2\bigl(\sin^2(\pi t)+\sin^2(\pi(t-r))\bigr)
 +O_R(|t|^{-1}).
\tag{43}
\]
The elementary phase identity gives
\[
\sin^2\theta+\sin^2(\theta-\pi r)
=1-\cos(\pi r)\cos(2\theta-\pi r)
\ge1-|\cos(\pi r)|.
\tag{44}
\]
Every true positive zero \(r_n=n+\delta_n\) is nonintegral. The right side
of (44) is consequently bounded below by a positive number in sufficiently
small neighborhoods of the finitely many selected roots. Equations (43)--(44)
prove (41) for all sufficiently large \(|t|\), uniformly in those neighborhoods.

At an exact root \(r\), \(K(t)\) and \(K(t-r)\) cannot both vanish: otherwise
the three real sites \(0,r,t\) would have all differences in the zero set,
contradicting ANF-087. The cases \(t=0,r\) also cannot vanish because
\(K(0)=1\). On the remaining compact \(t\)-interval, continuity gives a
positive minimum for each selected root; shrinking the finite neighborhoods
preserves that minimum. This completes (41), including the removable points
of the explicit formula, where the continuous kernel is used.

Since \(\Phi_\eta(t)\ll_\eta(1+t^2)^{-1}\) and \(r\) stays bounded, (41)
implies
\[
\Phi_\eta(t)+\Phi_\eta(t-r)
\le C_{\eta,R}\bigl(K(t)^2+K(t-r)^2\bigr)
\qquad(r\in\mathcal U_R,\ t\in\mathbb R).
\tag{45}
\]
This is a source estimate for a *pair*. An individual translate of \(K^2\)
cannot dominate the notch tail at its infinitely many real zeros.

### Freeze one matching scale and use the unused allowance of isolated sites

Write \(M=M_\eta>0\), \(\Phi=\Phi_\eta\), \(L=L(W)\), and
\(\Delta=Le(W)\). Positivity of \(M\) also follows directly from the zero
spacing: if every \(\Phi_\eta(r_n)\) vanished, all \(\eta r_n\) would be
integers, so the integers \(\eta(r_{n+1}-r_n)\) would converge to
\(\eta\in(0,1)\), which is impossible.
Choose \(R\ge1\), \(R>r_1\), sufficiently large that
\[
\frac{2b_\eta}{3\eta R^2}\le\frac M2.
\tag{46}
\]
This choice depends only on the fixed notch, not on \(e\) or \(W\).
Choose a fixed \(\gamma>0\) below the compact triple gap (12) at scale \(R\)
and small enough that
\[
0<r\le R,\ K(r)^2\le\gamma\quad\Longrightarrow\quad
r\in\mathcal U_R.
\tag{47}
\]
Such a \(\gamma\) exists because \(K^2\) has a positive minimum on the
compact complement of \(\mathcal U_R\) in \([0,R]\), including zero.

Apply the whole-site deletion of section 2 at this fixed threshold. For
\(W=G\sqcup B\), equations (6)--(7) give
\[
L(B)\ll_\eta\Delta,\qquad E_\eta(B)\ll_\eta\Delta,
\tag{48}
\]
and all sites of \(G\) have multiplicity one or two. Its distance-\(R\)
graph is a matching by the compact triple-gap argument of section 4.
Let \(P\) be the union of its two-site components and \(U\) its isolated
sites. Thus \(L(G)=L(P)+L(U)=\sum_{i\in G}m_i^2\).

The sites in \(U\) are mutually more than \(R\) apart. From each such site,
the \(n\)-th other site on either side is at distance greater than \(nR\),
and has multiplicity at most two. Since
\(\Phi(t)\le b_\eta/(\pi^2\eta t^2)\) for \(t\ne0\),
\[
\sup_{i\in U}\sum_{\substack{j\in U\\j\ne i}}m_j\Phi(x_i-x_j)
\le\frac{4b_\eta}{\pi^2\eta R^2}\sum_{n\ge1}n^{-2}
=\frac{2b_\eta}{3\eta R^2}\le\frac M2.
\tag{49}
\]
Multiplying by \(m_i\), summing, and using \(\sum m_i\le\sum m_i^2=L(U)\)
shows that the entire ordered off-diagonal \(U\)--\(U\) energy is at most
\((M/2)L(U)\). It is absorbed by the unused \(M L(U)\) in the two-site
envelope.

For each matched pair \(\{i,j\}\), (29) gives
\(\Phi(x_i-x_j)\le M+A_\eta|K(x_i-x_j)|\). Weighted Cauchy--Schwarz and
disjointness of the matching give
\[
\begin{aligned}
2\sum_{\{i,j\}\ {\rm matched}}m_im_j\Phi(x_i-x_j)
&\le M L(P)
 +2A_\eta
 \sqrt{\sum_{\{i,j\}\ {\rm matched}}m_im_j}
 \sqrt{\sum_{\{i,j\}\ {\rm matched}}m_im_jK(x_i-x_j)^2}\\
&\le M L(P)+A_\eta\sqrt{L(P)\Delta}.
\end{aligned}
\tag{50}
\]
The last line uses \(\sum_{\rm matched}m_im_j\le L(P)/2\) and
\(2\sum_{\rm matched}m_im_jK^2\le\Delta\).

All remaining good-site interactions involve a matched pair and a site
outside that pair. Translate its endpoints to \(0,r\), with
\(r\in\mathcal U_R\) by (47). For endpoint multiplicities
\(\mu,\nu\in\{1,2\}\), (45) implies
\[
\mu\Phi(t)+\nu\Phi(t-r)
\le2C_{\eta,R}\bigl(\mu K(t)^2+\nu K(t-r)^2\bigr).
\tag{51}
\]
Multiply by the outside multiplicity and sum over pairs and outside sites.
Each interaction between different matching components is charged at most
twice; an interaction with an isolated site is charged once. Thus their
total ordered notch energy is \(O_\eta(\Delta)\), with no factor depending
on the number of sites. Combining the diagonal, (49), (50) and (51),
\[
E_\eta(G)\le[\Phi(0)+M]L(G)-\frac M2L(U)
 +A_\eta\sqrt{L(P)\Delta}+O_\eta(\Delta).
\tag{52}
\]

Finally every interval of length \(R\) contains at most two good sites.
The same summable-potential argument as (33) therefore yields
\(\sup_y\sum_{j\in G}m_j\Phi(y-x_j)\ll_\eta1\). Hence
\[
2\sum_{i\in B,\ j\in G}m_im_j\Phi(x_i-x_j)
\ll_\eta\sum_{i\in B}m_i\le L(B)\ll_\eta\Delta.
\tag{53}
\]
Together with (48), (52), \(L(P)\le L(G)\le L\), and \(\beta_\eta^{\mathbb R}
=\Phi(0)+M\), this gives
\[
E_\eta(W)\le\beta_\eta^{\mathbb R}L
 +A_\eta\sqrt{L\Delta}+O_\eta(\Delta),
\tag{54}
\]
which proves (40). Empty good, paired, or isolated subsets cause no problem:
their sums vanish and the same inequalities apply.

### Scope, prior art and stress tests

The load-bearing improvement is (41)--(45): the noninteger separation of a
bounded near-zero pair prevents both source translates from losing their
leading sine term at the same distant location. The isolated-site allowance
then permits a **fixed** matching scale. There is no balance of an expanding
cutoff against the \(R^{-4}\) triple gap, and no cardinality-dependent deletion
or norm-triangle loss.

The classical kernel is the extremizer in Corollary 14 of
[Carneiro--Chandee--Littmann--Milinovich](https://arxiv.org/pdf/1406.5462).
[Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v1) supplies the
background multiset inequality; neither source is being used as a theorem
about this notch stability modulus. The two-delta optimization in the former
paper concerns bandlimited functions satisfying two point constraints, not
the all-cardinality finite-multiset exposure here.
[Suto's compact-Fourier ground-state theory](https://arxiv.org/abs/math-ph/0508004)
provides a neighboring infinite-volume, fixed-density comparison, not the
finite normalized estimate (40). A targeted search through these mechanisms
and quantitative near-extremal pair-potential formulations did not identify
the same bound. This is a local strengthening of ANF-195, with elementary
phase, compactness, packing and Cauchy--Schwarz steps; no global literature
novelty claim is made.

The uniformity in (41) is only over neighborhoods of finitely many roots at
the fixed scale \(R\). It would fail with one constant over all root
separations, since \(r_n\) approaches integers. The proof neither asserts
nor needs such uniformity. The actual removable points are not roots;
the true roots' sum-free property handles compact \(t\), while their
nonintegrality separately handles infinity. Counting interactions with
both endpoints and charging each cross-pair edge at most twice are essential
to the independence from cardinality. Arbitrarily large original
multiplicities remain covered by (48), not by the two-endpoint argument.

The result controls a fixed triangular notch on real multisets. General
positive-Fourier profiles in section 5 need not satisfy the inverse-square
majorant used in (45) and (49). No claim is made that the generic sharp rate
also gives the optimal leading constant or settles exceptional stationary
widths. Nonreal configurations lose the nonnegative real pair-energy
decomposition, so the unrestricted complex envelope in ANF-099 and its
RH-facing application remain unresolved.

## 10. One square-integrable weak derivative suffices for the square-root rate

Let \(\phi\) satisfy section 5's hypotheses: it is fixed, real and even,
\(0\le\phi\le J_0\) almost everywhere, and \(\Phi=\widehat\phi\ge0\) on
the real axis. Assume additionally
\[
\phi\in H^1(\mathbb R),\qquad
M:=\max_{r\in Z_+(K)}\Phi(r)>0.
\tag{55}
\]
Here \(H^1(\mathbb R)\) means that the profile, extended by zero outside
its support, and its weak first derivative belong to \(L^2(\mathbb R)\).
Then there are constants \(C_\phi,D_\phi<\infty\), independent of the
number of sites, their multiplicities and their span, such that every
nonempty finite real multiset \(W\) satisfies
\[
\boxed{\displaystyle
h_\phi(W)\le\beta_\phi^{\mathbb R}
  +C_\phi\sqrt{e(W)}+D_\phi e(W),\qquad
\beta_\phi^{\mathbb R}=\Phi(0)+M.}
\tag{56}
\]
The maximum-zero hypothesis in (55) is explicit; this argument uses its
positive allowance for isolated sites. ANF-197 classifies the remaining
case \(M=0\) exactly: \(\phi=cJ_0\), \(0\le c\le1\), and
\(h_\phi(W)=c(1+e(W))\). Consequently the square-root conclusion covers
every dominated nonnegative-Fourier \(H^1\) profile, with a linear modulus
on that exceptional rescaling branch.

### An integrable squared interaction cost replaces pointwise domination

Plancherel in the stated Fourier convention gives
\[
Q(t):=(1+t^2)\Phi(t)^2\ge0,\qquad
\|Q\|_1=\|\phi\|_2^2+(2\pi)^{-2}\|\phi'\|_2^2<\infty.
\tag{57}
\]
The inverse Fourier transform of \(\Phi^2\) is \(\phi*\phi\), supported
in \([-2,2]\). Multiplication by \(1+t^2\) differentiates this compactly
supported distribution, so \(Q\) is bandlimited to the same interval.
Choose a Schwartz function \(\psi\) with \(\widehat\psi=1\) near
\([-2,2]\). The distributional identity \(Q=Q*\psi\) holds pointwise
because both sides are continuous. Consequently
\[
\mathcal A(Q):=\sum_{k\in\mathbb Z}\sup_{t\in[k,k+1]}Q(t)
\le \|Q\|_1\sup_y\sum_k\sup_{t\in[k,k+1]}|\psi(t-y)|<\infty.
\tag{58}
\]
This is the same elementary bandlimited reproduction argument as (18b)--(18c).
Section 5 also gives \(\mathcal A(\Phi)<\infty\). In particular, on any
point set with at most two sites per unit interval and multiplicities at
most two, the sums of \(Q\), or of \(\Phi\), translated to any center are
bounded by \(4\mathcal A(Q)\), or \(4\mathcal A(\Phi)\), respectively.
This assertion uses cells for the translated differences themselves; it
is uniform over every real translation.

Choose a fixed \(R>\max(1,r_1)\) sufficiently large that the local-supremum
tail \(\sum_{|k|>R-2}\sup_{t\in[k,k+1]}\Phi(t)\), multiplied by
four, is at most \(M/2\). Equations (41)--(44), which concern only the source kernel,
provide neighborhoods \(\mathcal U_R\) of its finitely many roots in
\([0,R]\) and \(d_R>0\) such that
\[
K(t)^2+K(t-r)^2\ge d_R/(1+t^2)
\qquad(r\in\mathcal U_R,\ t\in\mathbb R).
\tag{59}
\]
Shrink the neighborhoods to stay in \((0,R+1)\). For any
\(\mu,\nu\in\{1,2\}\), (59) implies the squared-cost estimate
\[
\frac{[\mu\Phi(t)+\nu\Phi(t-r)]^2}
     {\mu K(t)^2+\nu K(t-r)^2}
\le C_R\{Q(t)+Q(t-r)\}.
\tag{60}
\]
Indeed the numerator is at most \(8[\Phi(t)^2+\Phi(t-r)^2]\), and
\(1+t^2\ll_R1+(t-r)^2\). The denominator is strictly positive by (59).
Unlike (45), (60) does not require \(\Phi(t)\ll(1+t^2)^{-1}\).

### Sum the squared cost before applying Cauchy--Schwarz

Select a fixed \(\gamma>0\) as in (47), also below the compact triple gap
at scale \(R\), and perform the deletion of section 2. Put
\(\Delta=L(W)e(W)\) and \(W=G\sqcup B\). Then
\[
L(B)+E_\phi(B)\ll_\phi\Delta,
\tag{61}
\]
the distance-\(R\) graph on \(G\) is a matching, and every interval of
length \(R\) contains at most two good sites. Write \(P\) for the union
of matched pairs and \(U\) for the isolated sites. All multiplicities in
\(G\) are one or two. The isolated sites are mutually more than \(R\)
apart. Our tail choice and (58)'s cell argument give ordered
\(U\)--\(U\) notch energy at most \((M/2)L(U)\).

The near-zero estimate (29) remains valid with \(\Phi,M\) in place of
\(\Phi_\eta,M_\eta\): compact support of \(\phi\) makes \(\Phi\)
Lipschitz, its decay makes \(\Phi\le M\) outside a compact interval,
and the finitely many source zeros there are simple. Thus the matching
edges contribute at most
\[
M L(P)+A_\phi\sqrt{L(P)\Delta}
\tag{62}
\]
by the weighted Cauchy--Schwarz calculation in (50).

For a matched pair with endpoints \(a<b\), set \(r=b-a\),
\(\mu=m_a,\nu=m_b\). For every good site \(j\) outside this pair put
\(t=x_j-a\) and define
\[
A_{p,j}=m_j[\mu K(t)^2+\nu K(t-r)^2],\qquad
B_{p,j}=m_j[\mu\Phi(t)+\nu\Phi(t-r)].
\tag{63}
\]
The positive real source decomposition gives
\(\sum_{p,j}A_{p,j}\le\Delta\): an edge between two paired components
is counted twice, and an edge from a pair to an isolated site once, while
the ordered source excess counts each edge twice. By (58)--(60), for
each fixed pair
\[
\sum_{j\notin p}\frac{B_{p,j}^2}{A_{p,j}}
\le C_R\sum_{j\notin p}m_j[Q(x_j-a)+Q(x_j-b)]
\ll_\phi\mathcal A(Q).
\tag{64}
\]
There are at most \(L(G)/2\) pairs. The total ordered notch interaction
between different components involving at least one pair is therefore
\[
\le2\sum_{p,j}B_{p,j}
\le2\left(\sum_{p,j}A_{p,j}\right)^{1/2}
       \left(\sum_{p,j}\frac{B_{p,j}^2}{A_{p,j}}\right)^{1/2}
\ll_\phi\sqrt{L(G)\Delta}.
\tag{65}
\]
This includes pair--pair and pair--isolated interactions with the stated
counting multiplicities; no factor proportional to the total number of
site pairs is introduced.

Adding the diagonal, (62), (65) and the isolated-site allowance gives
\[
E_\phi(G)\le[\Phi(0)+M]L(G)+O_\phi(\sqrt{L(G)\Delta}).
\tag{66}
\]
The bound \(\mathcal A(\Phi)<\infty\) and the good-site occupancy imply
\(\sup_y\sum_{j\in G}m_j\Phi(y-x_j)\ll_\phi1\). Hence the mixed
\(B\)--\(G\) notch energy is \(O_\phi(L(B))=O_\phi(\Delta)\), even
for unbounded bad-site multiplicities. Combine this with (61), (66) and
\(L(G)\le L(W)\), then divide by \(L(W)\), proving (56).

### The admissible regime is strictly larger than inverse-square decay

Freeze a triangular \(\tau\le J_0\) of width
\(0<\eta<1/(2r_1)\), and write \(T=\widehat\tau\ge0\). Put
\[
R_n=2^{n^2},\quad Z=\sum_{n\ge1}(n^2R_n)^{-1},\quad
w_n=(Zn^2R_n)^{-1},\quad 0<\lambda<1,
\]
\[
\phi(\alpha)=\frac{\tau(\alpha)}{1+\lambda}
 \left(1+\lambda\sum_{n\ge1}w_n\cos(2\pi R_n\alpha)\right).
\tag{67}
\]
Since \(\sum w_n=1\) and \(\sum w_nR_n=Z^{-1}\sum n^{-2}<\infty\),
the modulation factor is bounded and continuously differentiable.
The zero-extended tent \(\tau\) is Lipschitz with compact support, so
\(\phi\in H^1(\mathbb R)\). The positive shifted-transform formula (9)
of ANF-196 applies with these weights, and proves
\[
\frac{1-\lambda}{1+\lambda}\tau\le\phi\le\tau\le J_0,
\quad\Phi\ge0,\quad M\ge\Phi(r_1)\ge T(r_1)/(1+\lambda)>0.
\tag{68}
\]
Nevertheless
\[
R_n^2\Phi(R_n)\ge
\frac{\lambda T(0)}{2(1+\lambda)Z}\frac{R_n}{n^2}
\longrightarrow\infty.
\tag{69}
\]
Thus (56) applies to a fixed profile for which the pointwise majorant used
in section 9 fails. Taking \(\lambda\) small preserves the unique
maximizing source root \(r_1\) and its nonzero notch derivative: the tent
has a positive gap to all other root values, and both \(\Phi-T\) and
\(\Phi'-T'\) tend uniformly to zero with \(\lambda\), by integration
against \(\phi-\tau\) and \(\alpha(\phi-\tau)\). Section 8's two-site
Taylor test then shows that the square-root exponent can remain sharp
even in this added regime.

**Prior art and boundary.** The local-supremum estimate is classical
Plancherel–Pólya/Nikol'skii sampling theory; see the one-dimensional
inequalities (2)--(4) in [Pogány, *On multivariable Plancherel–Pólya
inequality and truncation error upper bounds in irregular sampling*](https://doi.org/10.1007/s43670-022-00044-4)
(2023). Equations (57)--(58) give the complete version needed here rather
than importing an unspecified sampling theorem. The Montgomery--Taylor
kernel and positive pair-energy prior art remain those of section 9.
The additional result is the squared paired-source cost (60)--(65), which
replaces pointwise Fourier domination by an integrated derivative condition
in the same all-cardinality real stability theorem. Targeted checks of
sampling inequalities, near-extremal positive pair energies and
Montgomery--Taylor stability did not identify this exact implication;
no general literature novelty is claimed.

This is a sufficient regularity condition, not a necessary one or a sharp
Sobolev threshold. ANF-196's continuous no-power-rate profile is not covered:
its positive Fourier peaks have too much weighted square mass. Indeed each
shifted tent-transform peak stays above a fixed multiple of its weight on
a fixed-width neighborhood of \(R_n\), and those disjoint neighborhoods
make \(\int t^2\Phi(t)^2dt\) diverge for its weights \(2^{-n}\).
No uniformity over changing profiles, no nonreal stability theorem, and no
new zero proportion or RH implication follows from (56).
