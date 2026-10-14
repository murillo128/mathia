# AF-571 — Finite-degree output drift has exact minimal-probe saturation on small prime-edit windows

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · POLYNOMIAL-NUISANCE · PRIME-EDIT · SHARP-LOCAL-MINIMAX · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: every fixed polynomial calibration degree

Retain the commonly registered critical prime-edit curves of AF-559/AF-570:
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
h_p(s)=p^{-s}-(p+1)^{-s},\quad
\Phi_p(a)=(P-h_p)^{-1}(E_1(a)),
\quad E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\tag{1}
\]
The edit locations \(p\) are genuine odd rational primes; the resulting curves belong to *generalized-prime matched controls*, not alternative ordinary-prime systems. Fix a known finite candidate set \(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), and restrict observation to \(0<a\le A\). The unknown output calibration is one arbitrary polynomial \(b(a)\in\Pi_r\), degree at most \(r\), held fixed across every observation under a given source:
\[
y(a)=\Phi_{p_i}(a)+b(a)+\eta(a),\qquad |\eta(a)|\le\varepsilon.
\tag{2}
\]
Competing source hypotheses may use different polynomials. Let \(n=r+1\). The full-curve and fixed-\(k\)-query radii are the *supremal* deterministic-noise levels permitting unique source identification, denoted \(\varepsilon_{\rm full}^{[r]}(A,S)\) and \(\varepsilon_k^{[r]}(A,S)\).

**Theorem.** For every fixed integer \(n\ge1\), there is an absolute threshold \(P_n\) such that, whenever \(\min S\ge P_n\), an \(A_*(S,n)>0\) exists with
\[
\boxed{
\varepsilon_{\rm full}^{[n-1]}(A,S)
=\varepsilon_{n+1}^{[n-1]}(A,S)
=\frac12\,\operatorname{dist}_{C[0,A]}
       (G_{i_*},\Pi_{n-1})\quad(0<A<A_*(S,n)),
}
\tag{3}
\]
where \(G_i=\Phi_{p_{i+1}}-\Phi_{p_i}\), and \(i_*\) is an adjacent pair whose signed \(n\)th derivative is pointwise smallest on that interval. An optimal \(n+1\)-point design on the closed interval may use \(a=0\); legal positive-coordinate designs approach its radius arbitrarily closely. Hence (3) is an equality of suprema, not necessarily of attained maxima.

Writing \([a^n]G\) for the \(n\)th Taylor coefficient, set
\[
\beta_n(S)=\min_{i<m}|[a^n]G_i|>0 .
\tag{4}
\]
The sharp small-window radius is
\[
\boxed{
\varepsilon_{\rm full}^{[n-1]}(A,S)
=\varepsilon_{n+1}^{[n-1]}(A,S)
=\frac{\beta_n(S)}{4^n}\,A^n+O_{S,n}(A^{n+1}).
}
\tag{5}
\]
Every policy using at most \(n\) observations, including an adaptive policy, fails to identify even two sources **at zero noise** when the nuisance polynomial is unrestricted. Thus \(r+2=n+1\) is the smallest possible query count, and this minimal *nonadaptive* count captures the entire (already diminished) quotient margin on sufficiently small windows.

For the first genuinely new case \(r=2\), four fixed probes exactly saturate the full quadratic-calibration quotient radius, of order \(A^3\); the adjacent source coefficient has leading magnitude \(c^3\delta_{p,q}(\log p)^2/2\), where \(c=e^{B_1}\) and \(\delta_{p,q}=1/[p(p+1)]-1/[q(q+1)]\). The \(r=0,1\) cases recover the small-window constant-offset and affine results of AF-570. No assertion is uniform when the degree, source set or prime locations vary jointly with \(A\).

## General comparison lemma: ordered higher derivatives

Let \(f_1,\ldots,f_m\in C^n[0,A]\) with adjacent gaps \(g_i=f_{i+1}-f_i\). Suppose there are \(\sigma\in\{-1,1\}\) and \(i_*\) such that
\[
0<\sigma g_{i_*}^{(n)}(a)\le\sigma g_i^{(n)}(a)
\quad(0\le a\le A,\ 1\le i<m).
\tag{6}
\]
For any pair \(j>i\), its gap \(h=f_j-f_i=\sum_{k=i}^{j-1}g_k\) satisfies \(\sigma h^{(n)}\ge\sigma g_{i_*}^{(n)}\). Let \(d=\operatorname{dist}_{C[0,A]}(g_{i_*},\Pi_{n-1})>0\), and let \(q_*\in\Pi_{n-1}\) be its best uniform approximant.

The classical Chebyshev alternation theorem supplies \(n+1\) ordered nodes \(0\le t_0<\cdots<t_n\le A\) at which \(g_{i_*}-q_*\) has alternating values of magnitude \(d\). Define
\[
v_j=\left[\prod_{k\ne j}(t_j-t_k)\right]^{-1},
\qquad
\lambda_j=\frac{v_j}{\sum_{k=0}^n|v_k|}.
\tag{7}
\]
Then \(\sum_j\lambda_j q(t_j)=0\) for all \(q\in\Pi_{n-1}\), \(\sum_j|\lambda_j|=1\), and \(\operatorname{sign}\lambda_j=(-1)^{n-j}\). Positivity of \(g_{i_*}^{(n)}\) after multiplying by \(\sigma\) forces the alternating errors to have signs \(\sigma(-1)^{n-j}\): their divided difference has sign \(\sigma\). Consequently
\[
\sigma\sum_j\lambda_j g_{i_*}(t_j)=d.
\tag{8}
\]
For any gap \(h\) as above, the standard generalized mean-value theorem for divided differences applied to \(h-g_{i_*}\), whose signed \(n\)th derivative is nonnegative, yields
\[
\sigma\sum_j\lambda_j h(t_j)\ge d.
\tag{9}
\]
Because \(\lambda\) has total variation one and annihilates the nuisance polynomial, (9) implies both \(\operatorname{dist}(h,\Pi_{n-1})\ge d\) on the full interval and the same lower bound in the discrete \(n+1\)-point quotient norm. The pair \(g_{i_*}\) attains the full-interval minimum \(d\), while the common alternation-node design achieves at least \(d\) against *every* source pair. The two-source midpoint/noise-ball argument divides these distances by two, proving equality (3) on the closed interval.

A node equal to \(0\) can be moved into \((0,A]\) while the other nodes remain distinct. All the finite pairwise quotient distances depend continuously on distinct nodes; since \(S\) is finite, the optimal radius is approached by legal designs. No assumption that a particular legal design attains the supremum is used.

Minimality is also exact, even for adaptive queries. Fix any deterministic policy using at most \(n\) coordinates and feed it a hypothetical all-zero response transcript. Its selected coordinates are now fixed, with at most \(n\) distinct values. For **each** candidate source separately, a polynomial of degree at most \(n-1\) interpolates the values \(-f_i(a_j)\) at those coordinates. Thus that same noiseless zero transcript is realizable under every source, and the policy cannot identify the source. Randomization cannot give a guaranteed zero-error policy against every realization of its randomness.

The lemma is classical Chebyshev alternation plus positivity of divided differences, used here as a common-design minimax certificate. It does not assert a new general approximation theorem.

## Source-specific all-order prime-edit boundary jets

AF-570 established analyticity through the excluded endpoint for each \(\Phi_p\), and derived the first two jets. The same exact implicit equation controls **every fixed jet order**, without subtracting nonuniform asymptotic expansions of individual prime curves.

Extend the edit parameter temporarily to real \(v\ge P_n\). Put
\[
R(x)=P(1+x)+\log x,\quad
E(a)=E_1(a)+\gamma+\log a,\quad
B_v(a)=\Phi_v(a)-1.
\]
Both \(R\) and \(E\) extend analytically near zero. With \(b_v=h_v(1)=1/[v(v+1)]\), exponentiating the source identity gives
\[
B_v(a)=a\exp\{\gamma+R(B_v(a))-h_v(1+B_v(a))-E(a)\},
\quad
B_v'(0)=K_v=c e^{-b_v}.
\tag{10}
\]
Here the prime-zeta boundary constant is \(c=e^{B_1}\), as in AF-570. Differentiating (10) with respect to the *edit location* \(v\) gives the exact sensitivity
\[
\partial_v B_v(a)=
\frac{B_v(a)\,w_v(1+B_v(a))}
{1-B_v(a)\{R'(B_v(a))-\partial_s h_v(1+B_v(a))\}},
\quad
w_v(s)=-\partial_v h_v(s)
=s(s+1)\int_v^{v+1}u^{-s-2}\,du .
\tag{11}
\]
In particular \(w_v(1)=v^{-2}-(v+1)^{-2}>0\), and
\[
b_p-b_q=\int_p^q w_v(1)\,dv=:\delta_{p,q}.
\tag{12}
\]

For any fixed derivative order, the Taylor coefficients of \(B_v(a)\), of the denominator inverse in (11), and of
\[
m_v(z)=\frac{w_v(1+z)}{w_v(1)}e^{z\log v}
=\frac{(1+z)(2+z)}2
\frac{\int_v^{v+1}u^{-3}(u/v)^{-z}\,du}
{\int_v^{v+1}u^{-3}\,du}
\tag{13}
\]
are bounded uniformly for all large \(v\). This follows directly from the analytic implicit equation: all fixed derivatives \(\partial_s^k h_v(1)=O_k(v^{-2}(1+\log v)^k)\) are bounded, while \(|\log(u/v)|\le1/v\) in (13).

Extracting the coefficient of \(a^n\) in (11), the unique highest power \((\log v)^{n-1}\) comes from expanding \(e^{-B_v(a)\log v}\) using \(B_v(a)=K_va+O(a^2)\):
\[
[a^n]\partial_v B_v(a)
=w_v(1)\left\{
\frac{K_v^n(-\log v)^{n-1}}{(n-1)!}
+O_n((\log v)^{n-2})\right\}
\qquad(n\ge2),
\tag{14}
\]
uniformly for large \(v\); for \(n=1\), the exact expression is \(w_v(1)K_v\). Since \(K_v=c[1+O(v^{-2})]\), replacing \(K_v^n\) by \(c^n\) changes only the indicated lower-order remainder.

Integrate (14) from \(p\) to \(q\). The positive weight \(w_v(1)\asymp v^{-3}\) satisfies, for every fixed integer \(k\ge0\),
\[
\frac{\int_p^q w_v(1)(\log v)^k\,dv}
{\int_p^q w_v(1)\,dv}
=(\log p)^k\bigl[1+O_k(1/\log p)\bigr]
\quad(k\ge1),
\tag{15}
\]
uniformly for **all** \(q>p\): the conditional moments of \(\log(v/p)\) are bounded by the full \(v^{-3}\)-tail moments. The case \(k=0\) is exact. Hence, for every fixed \(n\ge1\),
\[
\boxed{
[a^n](\Phi_q-\Phi_p)
=(-1)^{n-1}\frac{c^n}{(n-1)!}
\delta_{p,q}(\log p)^{n-1}
\bigl[1+O_n(1/\log p)\bigr]
}
\quad(q>p\to\infty),
\tag{16}
\]
where for \(n=1\) the stronger relative error \(O(p^{-2})\) follows from \(K_q-K_p=c(e^{-b_q}-e^{-b_p})\).

Thus for every fixed \(n\), **all** sufficiently remote adjacent rational-prime edit gaps have the same strict sign \((-1)^{n-1}\) in their \(n\)th boundary derivative. For a fixed finite \(S\), analyticity of the finitely many \(G_i^{(n)}\) means that differences between two such functions either vanish as germs or have eventually constant sign near zero. After reducing \(A_*(S,n)\), the signed \(n\)th derivatives are positive and totally ordered pointwise. This supplies precisely (6), including tied leading coefficients resolved by higher jets.

Finally, Taylor expansion gives \(G_i(a)=q_i(a)+[a^n]G_i\,a^n+O_{S,n}(a^{n+1})\) with \(q_i\in\Pi_{n-1}\). The shifted monic Chebyshev polynomial on \([0,1]\) gives
\[
\operatorname{dist}_{C[0,1]}(t^n,\Pi_{n-1})=2^{1-2n}.
\tag{17}
\]
Scaling \(a=At\), using the 1-Lipschitz property of distance to a subspace, taking the least adjacent coefficient, and dividing the quotient distance by two proves (5).

## Prior art, falsification and boundary

Best uniform polynomial approximation by alternation, the divided-difference mean-value formula, and the Chebyshev constant (17) are classical (de Boor 2005; Elliott--Taylor 1991; standard Chebyshev alternation sources, anchored in SOURCES.md). The prime-zeta analytic regular part is classical and already anchored under AF-552/AF-570. The source-specific contribution is the **uniform-in-second-edit all-order alternating jet law (16)** and its finite-source **exact minimum nonadaptive query saturation for every fixed polynomial nuisance degree**. This is a derived specialization and a structural fidelity statement, not a priority claim for general approximation theory or sequential design.

Falsification gates: check the \(n=1\) and \(n=2\) signs and constants against AF-570; retain the factor \(1/2\) from two-source noise-ball intersection; ensure the positive divided-difference orientation in (8)--(9); control every \(q>p\), including near-neighbor primes and unbounded \(q/p\), through the integrated \(v^{-3}\) weight rather than differencing standalone \(O(a^{n+1})\) terms; and distinguish equality of suprema from an attained legal node set. The analytic order and the window threshold depend on \(S,n\). Nothing here allows independently recalibrated probes, a changing polynomial between queries, unbounded degree, a uniform positive *absolute* noise radius, or a joint limit in which \(n\), \(S\) or its prime scale varies with \(A\).

These generalized-prime edit curves do not distinguish the true prime system from all admissible generalized-prime controls. Nor does a full finite-source decoding radius supply a faithful bridge to zeta zeros or RH. The theorem shows a precise structural tradeoff: quotienting by one more smooth polynomial output direction suppresses one more boundary power of the visible source signal, while one more *fixed* observation recovers the entire reduced small-window quotient margin.
