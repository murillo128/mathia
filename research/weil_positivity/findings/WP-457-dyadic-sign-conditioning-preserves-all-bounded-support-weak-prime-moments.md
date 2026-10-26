---
title: "WP-457: Dyadic sign conditioning preserves all bounded-support weak prime moments"
type: research-finding
status: verified
research_question: "Do the weak prime-orbit limits forced by closability suffice to exclude positive growing Weil blocks?"
claim_strength: exact_matched_unitary_countermodel_with_uniform_fixed_marginal_estimates
scope: necessary weak-moment conditions on an abstract energy representation; no closable Maharam realization asserted
finding_id: WP-457
related_findings:
  - WP-453
  - WP-454
  - WP-455
  - WP-456
created: 2026-10-26
updated: 2026-10-26
tags:
  - weil-positivity
  - prime-blocks
  - weak-convergence
  - conditional-measure
  - sign-selection
---

# WP-457: Weak prime moments cannot replace the missing block-domain theorem

## Claim and evidence boundary

**LITERATURE+DERIVED; EXACT MATCHED CONTROL; OBSTRUCTION TO A
WEAK-MOMENT PROOF STRATEGY.** Fix a finite constant \(c>0\). For
all sufficiently late dyadic prime blocks
\[
 B_j=\{p:2^j\le p<2^{j+1}\},\qquad
 V_j=2\sum_{p\in B_j}\frac{(\log p)^2}{p-1},
 \tag{1}
\]
there are two nonzero Hilbert spaces \(E_+\), \(E_-\) carrying
commuting unitaries \(S_p^+\), \(S_p^-\), one for every prime,
with the following properties.

1. For every fixed \(k\ge1\), \((S_p^\pm)^k\to0\) weakly as
   \(p\to\infty\). More strongly, every sequence of nontrivial
   characters involving at most a fixed number of distinct primes
   tends weakly to zero when its entire prime support escapes to
   infinity. The integer exponents need not remain bounded.
2. With the unchanged critical coefficients and actual adjoints,
   \[
   D_{B_j}^\pm=-\sum_{p\in B_j}(\log p)
      \sum_{k\ge1}p^{-k/2}
        \big((S_p^\pm)^k+(S_p^{\pm *})^k\big),
   \qquad
   D_{B_j}^+\ge c\sqrt{V_j}\,I,\quad
   D_{B_j}^-\le-c\sqrt{V_j}\,I.
   \tag{2}
   \]
3. The orbit measures of the constant unit vectors are singular
   relative to full product Haar measure, although every marginal
   on a fixed number of primes in late blocks approaches product
   Haar in total variation, uniformly over those prime choices.

The two signs are selected by conditioning on the desired block
sign. This is deliberately target-dependent. No densely defined
closable intertwiner from the fixed Maharam source to either
model is constructed or asserted to exist. In particular this is
**not** a counterexample to WP-453, WP-454, or an extension of
WP-454 to unbounded closable energies.

The precise consequence is that even the strengthened family of
weak moment conditions in item 1, together with commuting
isometries and the exact ray coefficients, cannot prove that
extension. A proof must use additional information from the
source and the form domain. The missing source-realization
question, archimedean/polar completion, and RH remain open.

## Independent Haar block and its small-influence scale

Let \(m_B\) be product normalized Haar measure on \(\mathbb T^B\).
Set
\[
 r_p=p^{-1/2},\quad
 w_p(z)=(\log p)\left(1-\frac{1-r_p^2}{|1-r_pz|^2}\right),
 \qquad X_B=\sum_{p\in B}w_p(z_p).
 \tag{3}
\]
The absolutely convergent Fourier series is
\[
 w_p(z)=-(\log p)\sum_{k\ge1}r_p^k(z^k+\bar z^k).
\]
Thus the independent summands are centered, with
\[
 v_p=\int w_p^2\,dm=\frac{2(\log p)^2}{p-1},\qquad
 \|w_p\|_\infty=\frac{2\log p}{\sqrt p-1}.
 \tag{4}
\]
For a block define
\[
 V_B=\sum_{p\in B}v_p,\qquad
 M_B=\max_{p\in B}\|w_p\|_\infty,\qquad
 \varepsilon_B=M_B/\sqrt{V_B}.
 \tag{5}
\]
Since \(|w_p|^3\le M_Bw_p^2\),
\[
 V_B^{-3/2}\sum_{p\in B}\int|w_p|^3\,dm
 \le\varepsilon_B.
 \tag{6}
\]
The classical independent-summand Berry--Esseen inequality gives
an absolute constant \(C\) such that
\[
 \sup_t\left|m_B\{X_B/\sqrt{V_B}\le t\}-\Phi(t)\right|
 \le C\varepsilon_B,
 \tag{7}
\]
where \(\Phi\) is the standard normal distribution function. No
claim about the optimal constant is needed.

For \(B=B_j\) and \(x=2^j\), the prime number theorem and
partial summation give
\[
 V_j\sim2(\log2)\log x,\qquad
 M_{B_j}=O((\log x)/\sqrt x),\qquad
 \varepsilon_j=O(\sqrt{(\log x)/x})\longrightarrow0.
 \tag{8}
\]
For the first relation, replace \(1/(p-1)\) by \(1/p\), at
an error \(O((\log x)^2/x)\), and integrate
\(2(\log t)^2/t\) against \(d\pi(t)\). The leading term is
\(2\int_x^{2x}(\log t)/t\,dt\). This is the same normalization
as WP-454; no RH estimate is used.

## Conditioning is invisible on every fixed-size marginal

Write \(a_c=1-\Phi(c)>0\), and define
\[
 A_B^+=\{X_B\ge c\sqrt{V_B}\},\qquad
 A_B^-=\{X_B\le-c\sqrt{V_B}\},\qquad
 \pi_B^\pm=m_B(A_B^\pm).
 \tag{9}
\]
Each \(w_p\) has an atomless distribution: every level set of
its nonconstant function of \(\cos\theta\) is finite. A nonempty
sum is atomless as well. There is consequently no endpoint-atom
issue in applying (7), and
\[
 \pi_B^\pm=a_c+O(\varepsilon_B).
 \tag{10}
\]
In particular both conditioning events have positive probability
for all sufficiently late dyadic blocks.

Fix an integer \(K\). For \(A\subset B\), \(|A|\le K\),
split \(X_B=s_A+R_A\), where \(s_A=\sum_{p\in A}w_p(z_p)\)
and \(R_A\) is the independent sum over \(B\setminus A\).
Uniformly in the exposed phases,
\[
 |s_A|\le K M_B,\qquad
 V_R:=\operatorname{Var}R_A\ge V_B-KM_B^2.
 \tag{11}
\]
For \(K\varepsilon_B^2<1/2\), the remainder is nonempty and
Berry--Esseen applied to it has error at most
\(C M_B/\sqrt{V_R}=O(\varepsilon_B)\). The normal threshold
satisfies
\[
 \left|\frac{c\sqrt{V_B}-s_A}{\sqrt{V_R}}-c\right|
 \le
 c\left((1-K\varepsilon_B^2)^{-1/2}-1\right)
 +\frac{K\varepsilon_B}{\sqrt{1-K\varepsilon_B^2}}
 =O_{c,K}(\varepsilon_B).
 \tag{12}
\]
The normal distribution function is globally Lipschitz.
Consequently
\[
 \mathbb P(R_A\ge c\sqrt{V_B}-s_A)
       =a_c+O_{c,K}(\varepsilon_B)
 \tag{13}
\]
uniformly on \(\mathbb T^A\). Dividing by (10) gives the
Radon--Nikodym density of the \(A\)-marginal of the conditioned
law \(\mu_B^+=1_{A_B^+}m_B/\pi_B^+\). Applying the same argument
to \(-X_B\) gives
\[
 \boxed{\left\|\frac{d(\mu_B^\pm)_A}{dm_A}-1\right\|_\infty
          =O_{c,K}(\varepsilon_B),\qquad |A|\le K.}
 \tag{14}
\]
The constants are uniform in the block, subset, and phases, for
late enough blocks; they may depend on the fixed \(c,K\).
This also bounds total variation. It does not give a bound when
\(K\) grows with the block size.

For any nonzero integer vector \(h\) supported on at most \(K\)
coordinates in one block, Haar character orthogonality now yields
\[
 \left|\int z^h\,d\mu_B^\pm\right|
 \le O_{c,K}(\varepsilon_B).
 \tag{15}
\]
There is no dependence on the magnitudes of the nonzero entries
of \(h\), since the character has modulus one. Equations
(11)--(14), rather than an assumption of independence after
conditioning, are the essential argument.

## Infinite models and their weak operator limits

Choose \(j_0\) so that both probabilities in (10) are positive
for \(j\ge j_0\). On the full prime torus take the probability
measures
\[
 \mu^\pm=
 m_{\{p<2^{j_0}\}}\otimes
       \bigotimes_{j\ge j_0}\mu_{B_j}^\pm,
 \qquad E_\pm=L^2(\mathbb T^{\mathbb P},\mu^\pm).
 \tag{16}
\]
These are ordinary countable product measures. Let
\(S_p^\pm=M_{z_p}\). They are commuting unitaries, with
\(S_p^{\pm *}=M_{\bar z_p}\). The constant function has norm
one. Norm convergence of each geometric ray series in (2)
identifies \(D_{B_j}^\pm\) with multiplication by \(X_{B_j}\),
so (9) proves both operator inequalities in (2) exactly.

If a set of at most \(K\) exposed primes intersects several
blocks, its marginal is the product of the respective block
marginals. At most \(K\) factors occur. Equation (14) therefore
gives convergence to Haar uniformly when all those blocks go to
infinity. In particular all their nontrivial character means
tend to zero, uniformly in the integer exponents.

To obtain **weak operator**, rather than just constant-vector,
convergence, let \(h_n\ne0\) be finitely supported integer
vectors with \(|\operatorname{supp}h_n|\le K\) and
\(\min\operatorname{supp}h_n\to\infty\). Let \(f,g\) be
square-integrable cylinder functions depending on finitely many
whole blocks and the finite initial panel. Eventually the support
of \(h_n\) misses these blocks. Product independence in (16)
then gives
\[
 \langle g,M_{z^{h_n}}f\rangle
   =\langle g,f\rangle\int z^{h_n}\,d\mu^\pm
   \longrightarrow0.
 \tag{17}
\]
Cylinder functions are dense. Since \(\|M_{z^{h_n}}\|=1\),
(17) extends to arbitrary \(f,g\in E_\pm\). This proves item 1.
It uses independence **between** blocks only, not within them.

Finally, let \(A^\pm=\bigcap_{j\ge j_0}A_{B_j}^\pm\).
The measures in (16) give their respective events mass one.
Under full product Haar, finite intersections have probabilities
\(\prod_{j=j_0}^N\pi_{B_j}^\pm\), tending to zero because
\(\pi_{B_j}^\pm\to a_c<1\). Thus
\[
 \mu^\pm(A^\pm)=1,\qquad m(A^\pm)=0.
 \tag{18}
\]
Local convergence to Haar is fully compatible with global
singularity and an order-one sign restriction on every late block.

## Audit, prior art and the remaining source gate

WP-453 proves that a closable covariant Maharam quotient transports
the source limits \(W_p^k\to0\) to its energy shifts. It then uses
a fixed quadratic polynomial to contradict **separate-ray**
positivity. Equations (2) and (17) show that this information,
even augmented by every bounded-support weak character limit,
cannot contradict **growing-block** positivity. The fixed-size
and growing-size quantifiers cannot be exchanged.

WP-454 has genuinely more input: bounded energy gives domination
of joint orbit measures by the source orbit measures. That is
not supplied by (17). WP-455--WP-456 already demonstrate why
closedness alone cannot simply be substituted into that domination
step. None of these statements establishes whether the particular
positive model (16) admits a nonzero closable dense-range source
intertwiner. Such an intertwiner would be a separate theorem
with a specified dense invariant domain, not a consequence of
the necessary limits checked here.

The countermodel is stronger than choosing finitely many favorable
arcs: it orients every late block with a fixed variance-scale
margin while preserving all bounded-support weak tests. It is
weaker in source realization: WP-456 constructs an actual closed
Maharam form for its finite panel, whereas (16) constructs only
an abstract energy representation. This distinction is essential.

The probability mechanism is classical. Esseen's 1942 paper,
Section 3, remark (b), equation (29), supplies the independent,
nonidentically distributed normal-approximation bound used in
(7). Conditioning a sum whose individual summands are negligible
compared with its standard deviation leads to (14) by the
displayed elementary calculation. Product-measure existence,
character orthogonality, and multiplication-operator calculus
are standard. Searches on conditioned sums, asymptotic
independence, closable Toeplitz forms and multiplicative Toeplitz
positivity supply no basis for a historical novelty claim.

The derived local contribution is this exact critical-Weil-block
control and the resulting limit on a proposed extension of the
weak-intertwiner argument. The same proof works for independent
centered bounded coordinate observables whenever
\(M_B/\sqrt{V_B}\to0\), so the sign selection is not arithmetic.
Both signs are chosen after inspecting the target observable.
It supplies no intrinsic positive geometry, zero information,
Gamma/polar term, formal verification or independent adversarial
approval. The proof uses the cited probability theorem and the
exact estimates above; no numerical asymptotic fit is evidence
for the infinite assertions.

## References

- [WP-453](WP-453-closability-forbids-infinite-prime-ray-orientation.md), the closable weak-intertwiner theorem and separate-ray obstruction.
- [WP-454](WP-454-bounded-covariant-energies-retain-negative-dyadic-prime-blocks.md), the bounded source-measure block obstruction and its normalization.
- [WP-455](WP-455-closed-diagonal-trace-energies-lock-prime-phases-but-retain-both-weil-signs.md), singular joint measures in actual closed finite-panel energies.
- [WP-456](WP-456-closed-singular-arc-traces-can-select-either-finite-weil-sign.md), closed finite-panel sign-selection controls.
- C.-G. Esseen, *On the Liapounoff limit of error in the theory of probability*, Arkiv för Matematik, Astronomi och Fysik **28A** (1942), no. 9, 1--19, Section 3, remark (b), equation (29), printed page 13, [original-paper scan](https://jugander.github.io/rare/Esseen1942_OnTheLiapounoffLimitOfError.pdf).
- NIST Digital Library of Mathematical Functions, [§27.2(i), equation 27.2.3](https://dlmf.nist.gov/27.2.E3), the prime number theorem used in (8).
