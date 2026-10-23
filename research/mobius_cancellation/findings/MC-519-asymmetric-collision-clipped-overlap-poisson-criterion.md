# MC-519 — Clipped overlap characterizes asymmetric collision Poisson limits without moment convergence

**Evidence:** EXACT-DERIVED · CLASSICAL-PROBABILITY-SPECIALIZATION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH.

## Claim and scope

Use precisely MC-518's independent-label control. For each positive integer \(n\), let \(p=(p_a)\) and \(q=(q_a)\) be probability laws on a finite common label set, allowed to vary with \(n\). All draws in \(X_1,\ldots,X_n\sim p\) and \(Y_1,\ldots,Y_n\sim q\) are independent. Set

\[
T_n=\sum_{i,j\le n}\mathbf1_{\{X_i=Y_j\}},\qquad
u_a=np_a,\quad v_a=nq_a,\qquad
\lambda_n=\mathbb ET_n=\sum_a u_av_a,
\]

and define the **clipped overlap**

\[
R_n=\sum_a u_av_a\min\{u_a+v_a,1\}
   =n^2\sum_a p_aq_a\min\{n(p_a+q_a),1\}.
\tag{1}
\]

Writing \(d_n=d_{\rm TV}(\mathcal L(T_n),\operatorname{Poi}(\lambda_n))\), with \(d_{\rm TV}=\sup_A|P(A)-Q(A)|\), the following bounds hold for every \(n\):

\[
\boxed{\frac{e^{-\lambda_n}}8 R_n-\frac{2\lambda_n}{\sqrt n}
       \ \le\ d_n\ \le\ 2R_n+\frac{4\lambda_n^2}{n}.}
\tag{2}
\]

The constants are not asserted optimal. In particular, if \(\lambda_n\to c\in(0,\infty)\), then

\[
\boxed{T_n\Rightarrow\operatorname{Poi}(c)
\quad\Longleftrightarrow\quad R_n\longrightarrow0.}
\tag{3}
\]

The convergence in (3) is equivalently total-variation convergence. No equality of the two laws, upper bound on either largest atom, or uniform integrability of \(T_n^2\) is assumed.

This replaces MC-518's sufficient but not necessary untruncated cubic overlap by an exact criterion for the same control model. It does not replace that finding's variance identity or upgrade a distributional limit to a second-moment limit.

## Sufficiency: discard heavy labels at their first-moment cost

Suppress \(n\) in the notation. Split labels into

\[
L=\{a:u_a+v_a\le1\},\qquad H=L^c,
\quad R_L=\sum_{a\in L}u_av_a(u_a+v_a),\quad
\lambda_H=\sum_{a\in H}u_av_a.
\]

Thus \(R=R_L+\lambda_H\). Let \(T_L\) count only matches whose common label lies in \(L\), with mean \(\lambda_L=\lambda-\lambda_H\). Since the omitted count is nonnegative,

\[
d_{\rm TV}(\mathcal L(T),\mathcal L(T_L))
\le\Pr(T\ne T_L)\le\mathbb E(T-T_L)=\lambda_H.
\tag{4}
\]

Apply the Arratia–Goldstein–Gordon local-dependence theorem (MC-S64, Theorem 1) to the restricted edge indicators \(\mathbf1_{\{X_i=Y_j\in L\}}\). Use all edges sharing either endpoint as the dependency neighborhood, including the edge itself. With \(s_L=\sum_{a\in L}p_aq_a\), its quantities are

\[
b_1=n^2(2n-1)s_L^2\le\frac{2\lambda^2}{n},\qquad
b_2=n^2(n-1)\sum_{a\in L}p_aq_a(p_a+q_a)
    =\left(1-\frac1n\right)R_L,\qquad b_3=0.
\]

The safe bound \(d_{\rm TV}(T_L,\operatorname{Poi}(\lambda_L))\le2(b_1+b_2)\), together with \(d_{\rm TV}(\operatorname{Poi}(\lambda_L),\operatorname{Poi}(\lambda))\le\lambda_H\), proves the upper bound in (2). If \(\lambda_L=0\), \(T_L=0\) almost surely and the same conclusion holds without invoking a positive-mean theorem. Labels are deleted only from the count; neither sampling law is renormalized.

## Necessity: the zero-collision probability detects clipped overlap

### A uniform fixed-size/Poisson-size coupling

Take infinite independent streams with laws \(p,q\), and independent \(K,J\sim\operatorname{Poi}(n)\), independent also of the streams. Let \(\widetilde T\) count matches between the first \(K\) and first \(J\) draws. Change sample sizes in two stages, from \((n,n)\) to \((K,n)\) to \((K,J)\). If \(s=\sum_a p_aq_a\), the expected numbers of changed matching edges in these stages are respectively \(ns\,\mathbb E|K-n|\) and \(s\,\mathbb EK\,\mathbb E|J-n|\). Hence

\[
d_{\rm TV}(\mathcal L(T),\mathcal L(\widetilde T))
\le\mathbb E|T-\widetilde T|
\le 2ns\sqrt n=\frac{2\lambda}{\sqrt n}.
\tag{5}
\]

The first inequality uses the integer-valued coupling. The estimate needs only the overlap mean, so even a macroscopic one-sided atom is allowed.

Poisson splitting makes the label counts mutually independent:

\[
\widetilde T=\sum_a U_aV_a,\qquad
U_a\sim\operatorname{Poi}(u_a),\quad V_a\sim\operatorname{Poi}(v_a).
\]

Thus, with \(z(u,v)=e^{-u}+e^{-v}-e^{-(u+v)}>0\),

\[
P(\widetilde T=0)=\prod_a z(u_a,v_a),\qquad
D=\lambda+\log P(\widetilde T=0)
 =\sum_a\big[u_av_a+\log z(u_a,v_a)\big].
\tag{6}
\]

### A scalar lower bound

For \(u,v>0\), write \(z(u,v)=\mathbb E\exp(-v\mathbf1_{\{U>0\}})\), where \(U\sim\operatorname{Poi}(u)\). Jensen gives

\[
\log z(u,v)\ge-v(1-e^{-u}),\qquad
uv+\log z(u,v)\ge uv\,f(u),
\quad f(t)=1-\frac{1-e^{-t}}t.
\]

Interchanging \(u,v\) gives the analogous bound with \(f(v)\). Moreover,

\[
f(t)=\frac1t\int_0^t(1-e^{-x})\,dx
\ge\frac1t\int_0^t\frac{x}{1+t}\,dx
=\frac{t}{2(1+t)}\ge\frac14\min\{t,1\}.
\]

Here \(1-e^{-x}\ge x/(1+x)\ge x/(1+t)\) for \(0\le x\le t\). Since \(\max(u,v)\ge(u+v)/2\), this proves

\[
\boxed{uv+\log z(u,v)\ge\frac18uv\min\{u+v,1\}.}
\tag{7}
\]

The same inequality is exact with both sides zero when \(uv=0\). Summing (7) yields \(D\ge R/8\), so

\[
P(\widetilde T=0)-e^{-\lambda}
=e^{-\lambda}(e^D-1)\ge\frac18e^{-\lambda}R.
\tag{8}
\]

Test total variation on the event \(\{0\}\), and then use (5). This proves the lower bound in (2), with no appeal to variance convergence. For \(\lambda_n\to c\), convergence in law on the nonnegative integers implies total-variation convergence; Poisson laws are continuous in their parameter. Thus (2) proves both directions of (3). In this same mean regime, even the single condition \(P(T_n=0)\to e^{-c}\) forces \(R_n\to0\) by (5) and (8), and therefore forces the full Poisson limit. This implication is specific to the collision model and its overlap-mean constraint.

## Interpretation and adversarial controls

Under \(\lambda_n\to c>0\), (1) vanishes precisely when, for every fixed \(\varepsilon>0\),

\[
\sum_{a:u_a+v_a>\varepsilon}u_av_a\longrightarrow0.
\tag{9}
\]

Indeed this sum is at most \(R_n/\min\{\varepsilon,1\}\), while \(R_n\le\varepsilon\lambda_n+\sum_{u_a+v_a>\varepsilon}u_av_a\) for \(0<\varepsilon\le1\). Thus the relevant small-atom condition is measured under the **collision-biased law** \(w_a=u_av_a/\lambda_n\), not under either marginal law alone. Labels that are large on one side but absent on the other have zero cost.

There is an exact occupancy interpretation in the Poissonized model:

\[
\mathbb E\sum_a U_aV_a\mathbf1_{\{U_aV_a\ge2\}}
=\sum_a u_av_a(1-e^{-(u_a+v_a)}).
\tag{10}
\]

This lies between \((1-e^{-1})R_n\) and \(R_n\). Hence the criterion asks that collisions contributed by multiply occupied common labels have vanishing **first moment**, allowing their second moments to persist.

For MC-518's rare-burst control, \(p_0=1/2, q_0=n^{-3}\) and the other \(n^2\) labels have \(p_a=1/(2n^2), q_a=(1-n^{-3})/n^2\). For \(n\ge2\), direct substitution gives

\[
R_n=\frac1{2n}
 +\frac{(1-n^{-3})(3/2-n^{-3})}{2n}
\sim\frac5{4n}.
\tag{11}
\]

Equation (2) therefore gives \(d_n=O(1/n)\), even though the untruncated overlap \(\sum_a u_av_a(u_a+v_a)\to1/4\) and the variance tends to \(3/4\) rather than the limiting Poisson mean \(1/2\). This explicitly passes the obstruction that defeated the moment converse.

When \(p=q\), bounded \(\lambda_n=\sum_a u_a^2\) gives \(R_n\le2(\max_a u_a)\lambda_n\), while \(R_n\ge(\max_a u_a)^2\min\{2\max_a u_a,1\}\). Thus (3) recovers MC-517's exact largest-atom criterion. Disjoint supports give \(T_n=\lambda_n=R_n=0\) for every \(n\); (2) remains valid, though (3) was stated for a positive limiting mean.

As a numerical sign/constant check only, 80-digit decimal arithmetic tested (7) at all 2,401 pairs \(u=10^{i/4},v=10^{j/4}\), \(-24\le i,j\le24\), without a violation. Equation (11) and the untruncated overlap were also checked at \(n=10,100,1000,10000\). The analytical proofs above, not these finite checks, establish the theorem.

## Prior art and mathematical boundary

The local-dependence upper bound is a direct application of Arratia–Goldstein–Gordon (MC-S64); dissociated-comparison Poisson theory is classical (MC-S65). Bhattacharya's multicolor-urn paper (MC-S66, Theorem 1.3 and Section 4, arXiv v5) treats color-dependent label laws through Poisson embedding. Its equation (4.2), specialized to two colors, already supplies the zero-collision product in (6). That product, the embedding method, and the general nonuniform birthday framework are prior art. No general probabilistic novelty is claimed.

The durable delta here is the explicit clipped-overlap equivalence and quantitative bounds (2) for the fixed, balanced two-sample observable, including the asymmetric moment-leakage regime of MC-518. The proof does not assume vanishing largest marginal atoms or infer convergence of unbounded moments from a Poisson limit. It closes this control-model classification question; further distributional refinements alone do not supply new arithmetic input.

For the actual relation \(\ell\mid q+r\), the prime sources are deterministic and neither their independent sampling nor the physical first-exit weights are justified by this theorem. Lower-prime mask products, conductor pushforward, exceptional weighted mass, and any signed/complex pre-aggregation relation still require source-specific estimates. Even a verified value of \(R_n\) for an independently resampled residue control does not certify those arithmetic hypotheses. There is no bound here on \(M(x)\), no zero-free conclusion, and no RH implication.
