# RE-244 — Fixed multicenter Taylor products have a max-plus failure envelope

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-COUPLED-PREDICTION + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDIT.

**Parent findings:** RE-218, RE-237, RE-240, RE-241, RE-242, RE-243.

RE-242 rules out below-threshold cancellation for a fixed, small conjugate center split near the far-edge critical depth; RE-243 makes its critical-boundary non-cancellation uniform under coalescing splits. Their two-tail comparison does not cover several unequal centers, arbitrary fixed phase spreads, or truncations far below a critical edge. The present result supplies a different argument: in the strictly geometric *first-omitted-term regime*, each exact Taylor section either tends to one or grows exponentially. No section can provide the exponentially *small multiplicative factor* needed to rescue another growing section. Thus finite serial coupling has an exact max-plus error-growth envelope, without a small-phase or equal-parameter hypothesis.

## 1. Statement and exact scope

Fix an observed unit-circle arc
\[
I_\alpha=\{e^{i\theta}:-\alpha\le\theta\le\alpha\},
\qquad 0<\alpha<\pi/2,
\]
and a fixed positive integer \(J\). For each \(1\le j\le J\), fix a center \(a_j=\rho_j e^{i\varphi_j}\ne0\), a scale \(s_j>0\), and a truncation ratio \(\lambda_j>0\). The centers need not lie on one ray or be paired, and the parameters may differ between stages; they are fixed as \(T\to\infty\).

With \(m_j=\lceil s_jT\rceil\), \(N_j=\lceil\lambda_jm_j\rceil\), set
\[
Q_{j,T}(z)=z^{m_j}a_j^{-m_j}
 \sum_{k=0}^{N_j}\binom{m_j+k-1}{k}(1-z/a_j)^k,
\qquad
G_T(z)=\prod_{j=1}^{J}\frac{Q_{j,T}(z)}{Q_{j,T}(1)}.
\tag{1}
\]
Put
\[
u_j(\theta)=1-e^{i\theta}/a_j,\quad
r_j=\max_{|\theta|\le\alpha}|u_j(\theta)|,\quad
h(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda.
\]
Assume the **strict geometric-tail condition**
\[
\boxed{\quad
c_jr_j<1,\qquad c_j=\frac{1+\lambda_j}{\lambda_j},
\qquad 1\le j\le J.
\quad}
\tag{2}
\]
In particular every Taylor/binomial series used below converges throughout the arc. Define the continuous positive-part rate
\[
\tau_j(\theta)=
-\log\rho_j+h(\lambda_j)
 +\lambda_j\log|u_j(\theta)|,
\quad
[x]_+=\max(x,0).
\tag{3}
\]
At a zero of \(u_j\), interpret \(\tau_j=-\infty\) and \([\tau_j]_+=0\). Finally impose **DC safety**
\[
\boxed{\quad \tau_j(0)\le0\quad\text{for every }j.\quad}
\tag{4}
\]
This is an individually checkable hypothesis, not the desired arc-prediction conclusion.

**Theorem.** Under (2) and (4), all \(Q_{j,T}(1)\) are nonzero for sufficiently large \(T\), and with
\[
P=\max_{|\theta|\le\alpha}
   \sum_{j=1}^J s_j[\tau_j(\theta)]_+\ \ge0,
\tag{5}
\]
one has the exact exponential envelope
\[
\boxed{\quad
\lim_{T\to\infty}\frac1T
\log\!\left(1+\sup_{z\in I_\alpha}|G_T(z)-1|\right)=P.
\quad}
\tag{6}
\]
In particular:
\[
\boxed{\quad
\sup_{z\in I_\alpha}|G_T(z)-1|\longrightarrow0
\quad\Longleftrightarrow\quad
\max_{|\theta|\le\alpha}\tau_j(\theta)\le0
\quad\text{for every }j.
\quad}
\tag{7}
\]
If (7) holds, the error is \(O(T^{-1/2})\), including the critical case of equality. If \(P>0\), then \(\sup_{I_\alpha}|G_T-1|=\exp(TP+o(T))\); in particular coupled cancellation cannot produce prediction. No real-coefficient condition is needed for the theorem. When the centers and truncation parameters occur in conjugate pairs, the product has real coefficients and falls within the real-polynomial interface of RE-218 and RE-242.

## 2. A first-omitted-term lemma uniform on the whole arc

For one stage suppress \(j\) and write \(m=m_j\), \(N=N_j\), \(K=N+1\), \(a=a_j\), \(u=1-z/a\). The binomial-series identity, valid for \(|u|<1\), is
\[
1-Q_{j,T}(z)=E_{j,T}(z)
=(z/a)^m\sum_{k=K}^{\infty}
 \binom{m+k-1}{k}u^k.
\tag{8}
\]
Factoring the first omitted term gives
\[
E_{j,T}(z)
=(z/a)^m\binom{m+K-1}{K}u^K S_{m,K}(u),
\]
\[
S_{m,K}(u)=\sum_{\ell\ge0} d_{m,K}(\ell)u^\ell,
\qquad
d_{m,K}(\ell)
=\prod_{v=0}^{\ell-1}\frac{m+K+v}{K+1+v}.
\tag{9}
\]
For fixed \(\ell\), \(d_{m,K}(\ell)\to c_j^\ell\), because \(K/m\to\lambda_j\). The successive ratios are nonincreasing in \(v\) for \(m\ge1\). By (2), for all sufficiently large \(T\) there is a common \(q_j<1\) for which
\[
d_{m,K}(\ell)|u|^\ell\le q_j^\ell
\qquad (|u|\le r_j,\ \ell\ge0).
\tag{10}
\]
The geometric majorant yields, uniformly on the closed disk \(|u|\le r_j\),
\[
S_{m,K}(u)\longrightarrow\frac1{1-c_ju}.
\tag{11}
\]
The limit is nowhere zero on that disk. Its modulus has a positive lower bound, so for large \(T\) both \(S_{m,K}\) and \(1/S_{m,K}\) are uniformly bounded there. This step excludes hidden exponential cancellation *inside* an individual complex Taylor remainder; no real-sign assumption is used.

Uniform Stirling at fixed \(\lambda_j>0\) and the bounded ceiling offsets gives
\[
\binom{m+K-1}{K}
=\Theta_j\!\left(m^{-1/2}e^{m h(\lambda_j)}\right).
\tag{12}
\]
Consequently, for any fixed \(\varepsilon>0\), there are constants \(0<A_{j,\varepsilon}<B_{j,\varepsilon}<\infty\) such that, for every sufficiently large \(T\) and every \(\theta\) with \(|u_j(\theta)|\ge\varepsilon\),
\[
A_{j,\varepsilon}m_j^{-1/2}e^{m_j\tau_j(\theta)}
\le |E_{j,T}(e^{i\theta})|
\le B_{j,\varepsilon}m_j^{-1/2}e^{m_j\tau_j(\theta)}.
\tag{13}
\]
The **upper** bound in fact holds uniformly on the entire observed arc, with a constant independent of \(\varepsilon\), where \(u_j(\theta)\ne0\). The lower bound is intentionally restricted away from \(u=0\): the bounded rounding offset \(K-\lambda_jm_j>0\) leaves a factor \(|u|^{K-\lambda_jm_j}\), which has no positive lower bound as \(u\to0\). The proof uses a lower bound only at a fixed nonzero \(u\), so this restriction loses no information. At \(u=0\) the remainder vanishes identically.

Specifically, for each **fixed** \(\theta\) with \(u_j(\theta)\ne0\),
\[
\frac1T\log|E_{j,T}(e^{i\theta})|
\longrightarrow s_j\tau_j(\theta),
\tag{14}
\]
while globally
\[
|E_{j,T}(e^{i\theta})|
\le C_jT^{-1/2}\exp(m_j\tau_j(\theta))
\quad (u_j(\theta)\ne0),
\tag{15}
\]
with the zero case interpreted as \(E_{j,T}=0\). The positive part of \(\tau_j\) is continuous on the arc, including at the zeros of \(u_j\).

## 3. The multiplicative max-plus envelope

By (4) and (15), every DC remainder satisfies \(E_{j,T}(1)=O(T^{-1/2})\), and hence
\[
Q_{j,T}(1)=1-E_{j,T}(1)=1+O(T^{-1/2}).
\tag{16}
\]
All normalizations exist and their product tends to one.

At a fixed point \(z=e^{i\theta}\) there are three cases. If \(\tau_j(\theta)>0\), (14) makes \(|E_{j,T}(z)|\to\infty\), so \(|Q_{j,T}(z)|=|1-E_{j,T}(z)|\sim|E_{j,T}(z)|\), giving logarithmic growth exponent \(s_j\tau_j(\theta)\). If \(\tau_j(\theta)\le0\), (15) gives \(E_{j,T}(z)\to0\) and \(Q_{j,T}(z)\to1\), giving exponent zero. The same is immediate when \(u_j(\theta)=0\). Thus
\[
\lim_{T\to\infty}\frac1T\log|Q_{j,T}(e^{i\theta})|
=s_j[\tau_j(\theta)]_+.
\tag{17}
\]
The modulus of the product is the product of moduli; *complex phases cannot cancel across multiplication*. For every fixed \(\theta\),
\[
\lim_{T\to\infty}\frac1T\log|G_T(e^{i\theta})|
=\sum_j s_j[\tau_j(\theta)]_+.
\tag{18}
\]

For the uniform upper bound, (15) gives
\[
|G_T(e^{i\theta})|
\le (1+o(1))
\prod_j\bigl(1+C_jT^{-1/2}e^{m_j\tau_j(\theta)}\bigr)
\le \exp(TP+o(T)),
\tag{19}
\]
where the final \(o(T)\) is uniform in \(\theta\), because \(J\) and all parameters are fixed and
\(\log(1+C T^{-1/2}e^{m\tau})\le m[\tau]_++O(1)\).
For \(P>0\), choose a maximizer \(\theta_*\) of the continuous positive-part envelope in (5). Equation (18) yields
\(|G_T(e^{i\theta_*})|=\exp(TP+o(T))\), so
\[
\sup_{I_\alpha}|G_T-1|
\ge |G_T(e^{i\theta_*})|-1
=\exp(TP+o(T)).
\tag{20}
\]
This and (19) prove (6) when \(P>0\).

For \(P=0\), nonnegativity in (5) and \(s_j>0\) imply \(\tau_j(\theta)\le0\) for every \(j,\theta\). The uniform bound (15) makes every \(E_{j,T}=O(T^{-1/2})\) on the arc. Equation (16) and the finite product expansion give
\[
\sup_{I_\alpha}|G_T-1|=O(T^{-1/2})\to0.
\tag{21}
\]
Conversely, if any factor has \(\max_{I_\alpha}\tau_j>0\), then \(P>0\) and (20) excludes convergence. This proves both (6) and (7), including equality at the critical depth.

## 4. Falsification controls and prior-art boundary

**Two identical co-phased stages.** When \(Q_1=Q_2\) and \(s_1=s_2=s\), the envelope is \(2s\max[\tau]_+\): if one polynomial grows, its square grows at twice the logarithmic rate, despite the normalization. This is consistent with RE-237, which concerns the *coefficient Wiener norm*, not arc prediction.

**Mixed phases.** With two conjugate centers \(\rho e^{\pm i\beta}\), common \(\lambda\), and positive \(s_j\), the exposed endpoint \(\theta=-\alpha\) supplies the **lower bound**
\[
P\ \ge\
s_1[\tau(\lambda,\alpha+\beta)]_+
+s_2[\tau(\lambda,\alpha-\beta)]_+,
\qquad 0\le\beta<\alpha.
\tag{22}
\]
The other endpoint interchanges the stages; the *actual* value of \(P\) is always the maximum in (5), and no unproved endpoint-maximization assertion is needed. For fixed nonzero \(\beta\), RE-242 identifies the locally sharp far-edge threshold by endpoint dominance; (7) extends factorwise necessity to all fixed depths satisfying (2) and an arbitrary finite constellation of centers. For moving \(\beta_T\to0\), the theorem is not uniform in parameters and RE-243 remains a distinct result.

**DC normalization cannot be ignored.** If (4) is dropped, a denominator may itself have exponential growth, and normalized factors can behave differently. The envelope (6) makes no claim in that regime. Likewise (2) is load-bearing: in the saddle-point or turning-point regime where the first omitted term no longer controls the tail, cancellation *within* a section may change the exponent. Neither failure of (2) nor failure of (4) is evidence that a coupled escape exists.

**Growth is not a Wiener cost.** RE-240 supplies a genuine exponential reduction of the product's Wiener norm at fixed mixed phases. That reduction is compatible with (6): coefficient convolution cancellation is not cancellation between values of the multiplicative factors. Even when (7) holds, no lower bound for the best Wiener exponent, optimal mixed-phase layout, or universal separated-prediction constant follows from this theorem. For the ordinary-prime transfer of RE-218, the critical \(O(T^{-1/2})\) error does not provide its required fixed exponential margin.

**Prior art.** Negative-binomial tails, incomplete-beta expansions, Stirling entropy, and first-omitted-term geometric bounds are classical; compare NIST DLMF §8.18 and G. Nemes–A. B. Olde Daalhuis, *Uniform Asymptotic Expansion for the Incomplete Beta Function*, SIGMA **12** (2016), 101, DOI 10.3842/SIGMA.2016.101. Equations (8)–(21) derive the special-case estimates without importing an external theorem. The line-specific mathematical delta is the full fixed-finite multicenter max-plus envelope and the resulting necessary-and-sufficient *factorwise* arc-prediction criterion, strengthening the limited conjugate near-threshold analysis of RE-242/RE-243. No new load-bearing literature dependency is required in SOURCES.md.

## Research consequence

Within fixed-parameter, finite-stage Taylor/negative-binomial cascades obeying the descending geometric-tail condition and DC safety, a coupled product predicts the arc **if and only if every stage separately predicts**; the exact leading failure exponent is (5). Arbitrary fixed inter-center phase geometry and unequal stages do not evade this obstruction. This closes a genuine coupled-only loophole *in that restricted sector*, not in moving-center families, growing numbers of stages, saddle-point truncations, additive/minimax synthesis, or arbitrary predictors. It gives no new unconditional inequality for Robin's divisor-sum functional and does not prove RH.
