# NB-355 — Two independent seed orbits require divergent physical components

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the exact real-orbit spaces and Burnol target projection; NB-351 for the logarithmic periodization model
- **Classification:** LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + TARGET-SPECIFIC-HILBERT-CONDITIONING

## Claim and scope

Two multiplicatively independent seed orbits recover the continuous Nyman space in closure, but their algebraic sum does not contain the projection of the actual target onto that space. Approaching the optimal target distance forces both orbit components to diverge in the physical Hilbert norm, with squared component norm at least a seed-dependent constant times the logarithm of inverse projection error. This strengthens the coefficient-cost obstruction of NB-353: cancellations within each seed orbit have already been taken before the cost is measured.

In \(H=L^2(0,1;dx)\), set
\[
e(x)=1,\qquad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},
\]
and let
\[
\mathcal C_j=\overline{\operatorname{span}}
\{A_ag_j:a\ge1\text{ real}\}.
\]
Fix integers \(p,q\ge2\) with \(\alpha=\log p/\log q\notin\mathbb Q\).
Let \(\mathcal N\) be the full continuous Nyman space, and let \(B\) be its zeta-zero inner factor, normalized by \(b=B(1)>0\), as in NB-354. Write \(t=P_{\mathcal N}e\). Then
\[
\boxed{\overline{\mathcal C_q+\mathcal C_p}=\mathcal N,
\qquad t\notin\mathcal C_q+\mathcal C_p.}
\tag{1}
\]
Thus the sum is not closed. More specifically,
\[
\inf_{u\in\mathcal C_q,\ v\in\mathcal C_p}\|e-u-v\|_2^2
=1-b^2
\tag{2}
\]
is not attained by any pair of finite-norm vectors. If a sequence of such pairs satisfies
\(\|e-u_n-v_n\|_2^2\to1-b^2\), then
\[
\boxed{\|u_n\|_2\longrightarrow\infty,
\qquad \|v_n\|_2\longrightarrow\infty.}
\tag{3}
\]
All statements are unconditional, including when \(b<1\). Under RH, \(b=1\) and \(t=e\); without RH the same obstruction concerns attaining the best available projection, not approximating \(e\) to zero error.

## 1. Remove the common inner factor while retaining the target

Use the unitary Mellin map \(\mathcal M:H\to H^2(\Re s>1/2)\), with squared boundary norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). NB-354 establishes
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}},\qquad
\mathcal Mt(s)=\frac{bB(s)}s.
\tag{4}
\]
Each \(\Theta_j\) is inner, with simple zeros
\(1+2\pi i\ell/\log j\), \(\ell\in\mathbb Z\setminus\{0\}\).
Its apparent singularity at \(s=1\) is removable and nonzero. The irrational log ratio makes the two zero lattices disjoint; the greatest common inner divisor is one. This gives the closure in (1), but says nothing by itself about the algebraic sum or its target membership.

For arbitrary \(u\in\mathcal C_q\), \(v\in\mathcal C_p\), write uniquely
\[
\mathcal Mu=B\Theta_q U,\qquad \mathcal Mv=B\Theta_p V,
\qquad U,V\in H^2.
\]
Inner multiplication is isometric, so \(\|U\|=\|u\|_2\) and \(\|V\|=\|v\|_2\). Define
\[
r(s)=\frac bs-\Theta_q(s)U(s)-\Theta_p(s)V(s),
\qquad \varepsilon=\|r\|=\|t-u-v\|_2.
\]
Orthogonality of \(e-t\) to \(\mathcal N\) gives the exact error identity
\[
\boxed{\|e-u-v\|_2^2=1-b^2+\varepsilon^2.}
\tag{5}
\]
No pointwise lower bound for \(B\), bounded inverse of \(B\) on the whole Hardy space, or assumption about RH is used: division is only on its actual invariant range.

## 2. A lattice sampling bound in the physical norm

Put \(L=\log q\), \(\tau=2\pi/L\), and \(s_\ell=1+i\tau\ell\). For every \(F\in H^2\),
\[
\boxed{\sum_{\ell\in\mathbb Z}|F(s_\ell)|^2
\le C_q\|F\|^2,\qquad C_q=\frac{L}{1-e^{-L}}.}
\tag{6}
\]
Here is a direct normalization check. Write
\(F(s)=\int_0^\infty h(t)e^{-(s-1/2)t}dt\) with
\(h\in L^2(0,\infty)\) and \(\|h\|_2=\|F\|\). On \(0\le t<L\), periodize
\[
P(t)=\sum_{k\ge0}h(t+kL)e^{-(t+kL)/2}.
\]
Cauchy--Schwarz gives
\[
|P(t)|^2\le\frac{e^{-t}}{1-e^{-L}}
\sum_{k\ge0}|h(t+kL)|^2.
\]
Thus \(P\in L^2(0,L)\). Its Fourier integrals are exactly \(F(s_\ell)\); this follows also by absolute integrability of \(h(t)e^{-t/2}\). Parseval yields
\(\sum_\ell|F(s_\ell)|^2=L\int_0^L|P(t)|^2dt\), proving (6).
Individual evaluation at \(s_\ell\) has norm one, since
\(\int_0^\infty|e^{-(s_\ell-1/2)t}|^2dt=1\).

At every positive lattice index, \(\Theta_q(s_\ell)=0\) and \(\Theta_p(s_\ell)\ne0\). Hence
\[
V(s_\ell)=\frac{b/s_\ell-r(s_\ell)}{\Theta_p(s_\ell)},
\qquad |r(s_\ell)|\le\varepsilon.
\]
For every finite \(K\ge1\), (6) therefore gives the explicit target certificate
\[
\boxed{\|v\|_2^2\ge\frac1{C_q}
\sum_{\ell=1}^{K}
\frac{[b/|s_\ell|-\varepsilon]_+^2}
{|\Theta_p(s_\ell)|^2}.}
\tag{7}
\]
It is a lower bound, not an interpolation sufficiency assertion or an equality for optimal component cost.

## 3. Near collisions force a growing number of nonvanishing samples

Let \(\|x\|_{\mathbb R/\mathbb Z}\) denote distance to the nearest integer and define the finite return count
\[
D_\alpha(X)=\#\{\ell\in\mathbb N_{\ge1}: \ell\le X,
\ \|\ell\alpha\|_{\mathbb R/\mathbb Z}\le1/\ell\}.
\tag{8}
\]
For irrational \(\alpha\), \(D_\alpha(X)\to\infty\). This needs only Dirichlet's elementary pigeonhole argument: for every integer \(Q\ge1\), two of the \(Q+1\) phases \(0,\alpha,\ldots,Q\alpha\) lie in one of \(Q\) equal bins, producing \(1\le\ell\le Q\) with \(\|\ell\alpha\|\le1/Q\le1/\ell\). Finitely many possible positive \(\ell\) would have a strictly positive minimum phase distance, contradicting arbitrarily large \(Q\).

Set
\[
S_q=\sqrt{1+\tau^2},\qquad
K_{p,q}=\frac{2\pi\sqrt p}{p-1}\frac{S_q}{\tau}.
\]
For each return in (8), the explicit factor (4) gives
\[
|\Theta_p(s_\ell)|
=\frac{|s_\ell|}{\tau\ell\sqrt p}
\frac{|1-e^{-2\pi i\ell\alpha}|}
{|1-p^{-1}e^{-2\pi i\ell\alpha}|}
\le\frac{K_{p,q}}\ell,
\qquad |s_\ell|\le S_q\ell.
\tag{9}
\]
If \(\varepsilon>0\) and \(\ell\le b/(2S_q\varepsilon)\), these estimates imply
\[
|V(s_\ell)|\ge\frac{b}{2S_qK_{p,q}}.
\]
Summing only over these returns in (6) proves
\[
\boxed{\|v\|_2^2\ge
\frac{b^2}{4C_qS_q^2K_{p,q}^2}
D_\alpha\!\left(\frac{b}{2S_q\varepsilon}\right).}
\tag{10}
\]
The count is zero when its argument is less than one. No unproved regular spacing of returns, bounded partial quotients, or irrationality measure for \(\log p/\log q\) is assumed.

If \(\varepsilon=0\), every return instead has
\(|V(s_\ell)|\ge b/(S_qK_{p,q})>0\). Infinitely many such samples contradict (6), proving target exclusion in (1). If \(\varepsilon_n\to0\), (10) forces \(\|v_n\|_2\to\infty\). Also
\[
\|u_n\|_2\ge\|v_n\|_2-\|u_n+v_n\|_2
\ge\|v_n\|_2-b-\varepsilon_n,
\]
which proves divergence of the other component. Together with (5) and the closure statement, this proves (2)--(3).

## 4. Weighted returns give an explicit logarithmic norm cost

The return count in (10) can be replaced by a lower bound that needs no information about the spacing of good approximations. For any irrational \(\alpha\) and real \(X\ge1\), define
\[
W_\alpha(X)=\sum_{1\le\ell\le X}
\frac1{\ell^2\|\ell\alpha\|_{\mathbb R/\mathbb Z}^2}.
\tag{11}
\]
An elementary dyadic form of Dirichlet's argument gives
\[
\boxed{W_\alpha(X)\ge1+\lfloor\log_2 X\rfloor.}
\tag{12}
\]
To prove this without assuming distinct returns at successive scales, put \(m=\lfloor\log_2 X\rfloor\). For every \(0\le k\le m\), choose a Dirichlet return \(1\le n_k\le2^k\) with \(\|n_k\alpha\|\le2^{-k}\). If the same integer \(n\) is selected at \(r\) scales \(k_1<\cdots<k_r\), then
\[
\frac1{n^2\|n\alpha\|^2}
\ge\left(\frac{2^{k_r}}n\right)^2
\ge4^{k_r-k_1}\ge4^{r-1}\ge r.
\]
Sum this inequality over the distinct selected integers, all at most \(2^m\). Their scale counts sum to \(m+1\), proving (12). A very sparse return sequence therefore does not defeat the estimate: a return used for many scales has enough reciprocal-square weight to pay for every reuse. No lower bound of order \(\log X\) for the *unweighted* count \(D_\alpha(X)\) is being assumed.

The estimate in (9) before restricting to returns is
\[
|\Theta_p(s_\ell)|\le K_{p,q}\|\ell\alpha\|_{\mathbb R/\mathbb Z}
\qquad(\ell\ge1).
\]
Set
\[
a_q=\frac b{2S_q},\qquad
\kappa_{p,q}=\frac{b^2}{4C_qS_q^2K_{p,q}^2}>0.
\]
For \(0<\varepsilon\le a_q\), put \(X=a_q/\varepsilon\). At every integer \(1\le\ell\le X\),
\(b/|s_\ell|-\varepsilon\ge b/(2S_q\ell)\). Applying (7) with \(K=\lfloor X\rfloor\), and then (11)--(12), gives
\[
\boxed{\|v\|_2^2\ge\kappa_{p,q}W_\alpha(a_q/\varepsilon)
\ge\kappa_{p,q}\left(1+\left\lfloor
\log_2\frac{a_q}{\varepsilon}\right\rfloor\right).}
\tag{13}
\]
Interchanging the seeds gives the corresponding bound for \(u\), with \(a_p\) and \(\kappa_{q,p}\). Thus each physical component is at least of order \(\sqrt{\log(1/\varepsilon)}\) as the projection error tends to zero, for every fixed independent seed pair, unconditionally.

In particular, a bound \(\|v\|_2\le R\), with \(R\ge0\), implies the explicit target-error floor
\[
\boxed{\|e-u-v\|_2^2
\ge1-b^2+a_q^2\,2^{-2R^2/\kappa_{p,q}}.}
\tag{14}
\]
Indeed, (13) implies \(\varepsilon\ge a_q2^{-R^2/\kappa_{p,q}}\) when \(\varepsilon\le a_q\); the same weak inequality is automatic when \(\varepsilon>a_q\), and \(\varepsilon=0\) has already been excluded. Use (5) to square this bound. There is an analogous bound under \(\|u\|_2\le R\).

The constants retain the unknown positive Burnol factor \(b\). Formula (14) is a necessary lower bound; it does not construct approximants with exponentially small error at a given norm budget. Nor does a lower bound on a reciprocal sum turn the sampling inequality (6) into a sufficient interpolation theorem.

## Consequences and controls

- Both components already range over complete closed real-dilation orbit spaces. Replacing a seed's generator list by an equivalent basis, or canceling coefficients within that orbit, cannot remove the bound on its resulting physical vector. The decomposition between the two spaces need not be unique; (7)--(14) hold for every decomposition.
- Any fixed bound on either component norm leaves the explicit positive excess (14) over the squared Burnol floor. The constants depend on the seeds and on \(b\); no effective lower estimate for \(b\), bounded partial quotients, or irrationality measure for the log ratio is assumed.
- The two total components must cancel increasingly large physical energy while their sum converges to the fixed vector \(t\). Nonclosedness alone would only show that some vector lacks a decomposition; the lattice argument identifies the actual projected Nyman target as such a vector.
- The result is compatible with NB-354: a sequence of finite sums from the two orbits approaches \(t\), while the separately grouped orbit sums have unbounded norms. It is also distinct from NB-353's weighted absolute-coefficient cost, which is not a physical norm and cannot be substituted for it.
- Rational log ratios do not satisfy the theorem's hypotheses: exact common zeros then survive, and NB-354 gives a smaller closure with extra target loss. Allowing three or more independent seed types also changes the interpolation equation at a zero of one seed; the present two-component contradiction does not establish the corresponding claim for that larger family.
- Integer-only dilations form smaller spaces. Every represented pair inherits (7), but no claim that their sum has closure \(\mathcal N\) follows here. There is no rate for finite arithmetic sections or a conclusion about zeros on or off the critical line.

The source-compression boundary is therefore stronger than absence of a uniform inverse for arbitrary data: the particular best target projection itself cannot be assembled from two finite-energy orbit vectors. A constructive two-seed scheme must manage cross-orbit norm growth even after all internal coefficient cancellation.

## Prior art and evidence boundary

Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the Hardy realization and target projection used in (4)--(5). NB-354 supplies the exact elementary inner factors and their coprime real-orbit closure. Parseval and Dirichlet approximation are classical; their required forms are proved above. No new Hardy-space, sampling, Diophantine-approximation, or invariant-subspace theorem is claimed.

For the surrounding operator mechanism, Douglas, *Variations on a theme of Beurling*, New York J. Math. 17a (2011), 1--10, [Section 6, Theorem 6.1](https://nyjm.albany.edu/j/2011/17a-1v.pdf), records the classical corona lower bound controlling similarity for a two-function Hardy quotient. Our pair, divided by \(\sqrt2\), satisfies its boundary normalization but fails the interior lower bound along (9). That identifies the usual conditioning mechanism; it does not itself prove that the specified target is outside the algebraic sum. The target-specific step here is the non-square-summability forced by \(b/s\), quantified in (7)--(10).

Borda, *On the theorem of Davenport and generalized Dedekind sums*, J. Number Theory 172 (2017), 1--20, [Section 4, Theorem 3](https://arxiv.org/pdf/1606.07946), studies exactly the family of reciprocal sums containing (11), with continued-fraction estimates at convergent cutoffs. His *Remarks on sums of reciprocals of fractional parts*, Acta Arith. 212 (2024), 373--389, [Introduction](https://arxiv.org/pdf/2305.07394), places the squared case in the older Beck/Kruse literature. The scalar sum and its Diophantine mechanism are established prior art. The self-contained dyadic proof (12) supplies the coarse all-cutoff bound needed here; the line-specific consequence is its transfer into the physical target budget (13)--(14). No new reciprocal-sum theorem or sharp asymptotic for the arithmetic log ratio is claimed.

The literature audit covered finite generator families, dilation-invariant Nyman subspaces, coprime inner factors, corona bounds, and sums of invariant subspaces. Yang's *A fundamental set in \(L^2(0,1)\)*, Acta Arith. 199 (2021), 269--274, DOI `10.4064/aa200216-31-8`, was inspected at publisher-abstract level only; no detailed theorem comparison is inferred from that abstract. No matching-search absence is treated as a novelty claim. Locally, NB-004 already uses logarithmic phase recurrence for target-orthogonal approximate aliases; its control does not imply the present obstruction for the actual target after inner-factor removal.

The mathematical delta is the failure of exact two-orbit assembly of \(P_{\mathcal N}e\), with a logarithmic lower bound on squared physical component norms and the explicit budget-dependent excess (14), not a new closure criterion. The evidence is the analytic proof above. Its decisive audit points are the retained factor \(b\), the sampling normalization \(C_q\), the removed zero at \(s=1\), the balance of target decay \(1/\ell\) with near-collision decay in (9), and correct counting of repeated dyadic returns in (12). No numerical estimate of the optimum, Lean verification, independent adversarial approval, matching upper bound, or finite-section approximation rate is asserted.
