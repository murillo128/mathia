---
title: "WP-434: Logarithmic coanalytic prime smoothing has a sharp compactness threshold but no Schatten gain"
type: research-finding
status: verified
research_question: "Can logarithmic Hamiltonian smoothing rescue the critical coanalytic prime field in a noncompact or Schatten-controlled category?"
claim_strength: exact_logarithmic_coanalytic_closability_boundedness_compactness_and_no_finite_schatten_threshold
scope: standard positive-energy Bost--Connes representation on l2(N); minimal coanalytic prime field preconditioned by a power of 1+H; no assertion about cancellation before smoothing, other KMS/GNS sectors, source-forced global coupling, or archimedean completion
finding_id: WP-434
related_findings:
  - WP-433
  - WP-432
  - WP-431
  - WP-218
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-12
updated: 2026-10-12
tags:
  - weil-positivity
  - bost-connes
  - logarithmic-regularization
  - coanalytic
  - compactness
  - closability
  - schatten
  - essential-spectrum
---

# WP-434: Logarithmic coanalytic prime smoothing has a sharp compactness threshold but no Schatten gain

## Exact claim and status

**EXACT-DERIVED; NEGATIVE/OPERATOR-CATEGORY CLASSIFICATION.** Work on \(\mathcal H=\ell^2(\mathbb N)\) with
\[
\mu_p e_n=e_{pn},\quad H e_n=(\log n)e_n,\quad
R_a e_m=\sum_{p\mid m}\overline{a_p}\,e_{m/p}
\quad\text{on }c_{00}(\mathbb N).
\]
For \(\kappa,s\geq0\) define
\[
a_{\kappa,p}=\frac{(\log p)^\kappa}{\sqrt p},\qquad
D_s=(1+H)^{-s/2},\qquad
B_{\kappa,s}=R_{a_\kappa}D_s|_{c_{00}}.
\tag{1}
\]
The exact classification of these *minimal* operators is
\[
\boxed{\begin{array}{c|l}
s\leq 2\kappa & \text{nonclosable; norm-square form nonclosable}\\
2\kappa<s<1 & \text{closable, but unbounded}\\
s>2\kappa,\ s\geq1 & \text{bounded and compact extension}.
\end{array}}
\tag{2}
\]
In the middle regime the norm-square form is closable, even though its operator is unbounded. In the compact regime the extension belongs to **no Schatten class \(\mathcal S_q\) of any finite order \(q>0\)**. Its compact positive energy \(B_{\kappa,s}^*B_{\kappa,s}\) likewise belongs to no finite Schatten class and cannot alter the negative essential prime-ray Weil spectrum of WP-218.

For critical Bost--Connes half-density \(\kappa=0\), every \(s>0\) gives closability, but compactness begins **exactly at \(s=1\)**. For the extra Weil logarithm \(\kappa=1\), the operator is nonclosable for \(s\leq2\) and compact for \(s>2\). This is not an independently derived global Weil sign.

## Vacuum row gives the sharp closability boundary

For a prime basis vector,
\[
B_{\kappa,s}e_p=\overline{b_p}\,e_1,\qquad
b_p=\frac{(\log p)^\kappa}{\sqrt p(1+\log p)^{s/2}}.
\tag{3}
\]
By the prime number theorem and partial summation,
\[
\sum_p|b_p|^2<\infty
\iff\sum_p\frac{(\log p)^{2\kappa-s}}p<\infty
\iff s>2\kappa.
\tag{4}
\]
The prime-density integral is comparable in its tail to
\(\int^\infty u^{2\kappa-s-1}\,du\), so equality \(s=2\kappa\) diverges.

If the sum in (4) is infinite, choose finite prime sets \(F\) with
\(S_F=\sum_{p\in F}|b_p|^2\to\infty\), and put
\(x_F=S_F^{-1}\sum_{p\in F}b_pe_p\). Then
\(\|x_F\|^2=S_F^{-1}\to0\) but \(B_{\kappa,s}x_F=e_1\).
Also \(B_{\kappa,s}(x_F-x_G)=0\) while
\(\|B_{\kappa,s}x_F\|^2=1\); therefore both the operator and its positive norm-square form are nonclosable.

Conversely, when (4) is finite, the formal adjoint of the minimal operator satisfies
\[
B_{\kappa,s}^*e_n
=\sum_p a_{\kappa,p}(1+\log(np))^{-s/2}e_{np}.
\tag{5}
\]
Distinct prime indices give orthogonal terms, and the squared norm is at most \(\sum_p|b_p|^2\), since \(np\geq p\). Every \(e_n\) is therefore in the adjoint domain; finite linear combinations are as well. The adjoint domain is dense, proving closability for all \(s>2\kappa\), including \(s<1\). The associated form is closable by the closed-operator graph norm.

## Weighted divisibility proves compactness at and above one logarithmic derivative

Assume \(s\geq1\) and \(s>2\kappa\). Set \(g=D_sf\) for a finitely supported \(f\). Weighted Cauchy--Schwarz gives
\[
\begin{aligned}
\|B_{\kappa,s}f\|^2
&=\sum_n\left|\sum_p\overline{a_{\kappa,p}}g(np)\right|^2\\
&\leq A_{\kappa,s}\sum_m\frac{|f(m)|^2}{(1+\log m)^s}
                  \sum_{p\mid m}(\log p)^s,
\end{aligned}
\tag{6}
\]
where
\[
A_{\kappa,s}
=\sum_p\frac{|a_{\kappa,p}|^2}{(\log p)^s}
=\sum_p\frac{(\log p)^{2\kappa-s}}p<\infty.
\]
For \(s\geq1\), unique factorization and convexity yield
\[
\sum_{p\mid m}(\log p)^s
\leq\left(\sum_{p\mid m}\log p\right)^s
\leq(\log m)^s\leq(1+\log m)^s.
\tag{7}
\]
Thus \(\|B_{\kappa,s}\|\leq\sqrt{A_{\kappa,s}}\).
For a finite prime set \(F\), the same bound applied to the tail shows
\[
\|B_{\kappa,s}-B_{\kappa,s,F}\|
\leq\left(\sum_{p\notin F}\frac{(\log p)^{2\kappa-s}}p\right)^{1/2}
\longrightarrow0.
\tag{8}
\]
Each summand \(\mu_p^*D_s\) is compact because \(D_s\) is diagonal with weights tending to zero for \(s>0\). Hence the bounded extension is a norm limit of finite sums of compact operators and is compact.

## A squarefree prime block proves unboundedness below one derivative

Let \(2\kappa<s<1\). For large \(X\), take the \(M\asymp X/\log X\) primes \(F_X\) in \([X,2X]\), and put \(k=\lfloor M/2\rfloor\). The packet
\[
f_X=\binom Mk^{-1/2}
\sum_{\substack{S\subseteq F_X\\|S|=k}}e_{\prod_{p\in S}p}
\tag{9}
\]
has unit norm. Every output coefficient at a product of \(k-1\) distinct primes from \(F_X\) receives \(M-k+1\) positive summands. Each is bounded below, up to an absolute constant, by
\((\log X)^\kappa X^{-1/2}[1+k\log(2X)]^{-s/2}\binom Mk^{-1/2}\).
Since
\(\binom M{k-1}/\binom Mk=k/(M-k+1)\), the output norm satisfies
\[
\|B_{\kappa,s}f_X\|
\gtrsim
\frac{(\log X)^\kappa}{\sqrt X}\,
\frac{\sqrt{k(M-k+1)}}{[1+k\log(2X)]^{s/2}}
\asymp X^{(1-s)/2}(\log X)^{\kappa-1}
\longrightarrow\infty.
\tag{10}
\]
The last limit holds for every fixed \(\kappa\geq0\) when \(s<1\). This also shows why the concave \(s<1\) case cannot be absorbed by the convex divisibility bound (7).

## No finite Schatten class, even at arbitrarily high finite order

Fix any prime \(p\). Compress the compact extension from the closed span of \(e_{pn}\), with \((n,p)=1\), onto the closed span of \(e_n\), with \((n,p)=1\). The \(p\)-divisor term is the only one landing in the latter space; all other divisor terms remain divisible by \(p\). The compression is therefore a weighted partial shift with singular values
\[
|a_{\kappa,p}|[1+\log(pn)]^{-s/2},
\qquad (n,p)=1.
\tag{11}
\]
For every finite \(q>0\),
\[
\sum_{\substack{n\geq1\\(n,p)=1}}
|a_{\kappa,p}|^q[1+\log(pn)]^{-sq/2}
=\infty,
\tag{12}
\]
since integers coprime to \(p\) have positive density and no finite power of \(\log n\) is summable over them. Schatten ideals are preserved under bounded compressions; (12) rules out \(\mathcal S_q\) for every finite \(q\), and rules out finite Schatten membership of \(B_{\kappa,s}^*B_{\kappa,s}\) by the square relation between singular values.

This sharply contrasts with WP-433: exponential \(e^{-tH}\) damping can be Hilbert--Schmidt at \(t>1/2\), whereas finite logarithmic-power damping is never in a finite Schatten class, despite producing a compact operator.

## Essential sign, matched controls, and prior-art boundary

In the compact regime let \(K_{\kappa,s}=B_{\kappa,s}^*B_{\kappa,s}\) and let \(P_p\) project onto the prime-power ray. Then \(P_pK_{\kappa,s}P_p\) is compact. WP-218 gives the independent critical Weil-oriented ray defect
\[
W_p=(\log p)(I-T(P_{p^{-1/2}})),\qquad
\inf\sigma_{\rm ess}(W_p)
=-\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}<0.
\tag{13}
\]
Weyl's theorem therefore implies
\(W_p+P_pK_{\kappa,s}P_p\not\succeq0\).
This excludes additive compact repairs of the unchanged prime ray, not noncompact cancellation-bearing, relative/form-level, or finite--archimedean completions.

The proof uses the prime number theorem, a weighted divisibility Cauchy--Schwarz bound, squarefree combinatorics, and standard compact/Schatten ideal theory. The Bohr--Hardy Dirichlet realization (Hedenmalm--Lindqvist--Seip, 1997), Bost--Connes Hamiltonian (1995), and Hardy--Dirichlet multipliers (Fernández Vidal--Galicer--Sevilla-Peris, 2025) are already anchored in SOURCES.md. Weighted logarithmic Dirichlet spaces and related composition operators are also established subjects, not claimed as new. No new general operator-theoretic theorem or RH progress is claimed: the line-specific result is the exact threshold and non-Schatten obstruction for this previously open coanalytic smoothing family.

The squarefree packet mechanism uses many generators in a dyadic interval and extends to matched free-generator controls with comparable counting. The compact bound uses only positive logarithmic generator lengths and multiplicative labeling, not zero data. The construction still lacks exact global Mangoldt prime-power selection, the archimedean Gamma contribution, polar normalization, and a sign mechanism selected independently of the Weil target.

## References

- research/weil_positivity/findings/WP-433-thermal-coanalytic-prime-regularization-is-compact-and-sign-inert.md
- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
