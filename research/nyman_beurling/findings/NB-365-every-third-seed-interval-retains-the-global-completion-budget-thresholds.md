# NB-365 — Every third-seed interval retains the global completion-budget thresholds

- **Status:** proved (classical tools plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 and NB-360 for exact orbit membership and full physical cost; NB-363 and NB-364 only for the stated applications
- **Classification:** EXACT-DERIVED + LOCAL-TO-GLOBAL-COST + NEGATIVE/OBSTRUCTION

## Claim and scope

Restricting the added real seed to a fixed nonempty open interval cannot improve the power-moment or stretched-exponential integrability class of its exact completion budget. A rational reindexing comparison transfers the entire scalar cost tail to every interval, up to fixed multiplicative constants. This settles the interval-localization boundary left open in NB-363; it does not determine the optimal exponential constant or classify which irrational pairs admit completion.

Fix real seeds \(p,q>1\) with irrational \(\alpha=\log p/\log q\). In \(H=L^2(0,1;dx)\), set
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},\qquad
\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},\qquad t=P_{\mathcal N}e.
\]
Write \(\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z}>0\) and define the measurable, extended-valued, one-periodic function
\[
S(\beta)=\sum_{n\ge1}\frac1{n^2(\delta_n^2+\|n\beta\|^2)}.
\tag{1}
\]
Let \(I\subset(1,2)\) be any nonempty open interval, with length \(\ell\), and choose an integer \(D\ge1\) with \(D\ell>1\). Lebesgue measure is denoted by \(m\). Then, for every \(R\ge0\),
\[
\boxed{\frac1D m\{\beta\in(1,2):S(\beta)>D^4R\}
\le m\{\beta\in I:S(\beta)>R\}
\le m\{\beta\in(1,2):S(\beta)>R\}.}
\tag{2}
\]
The constants in (2) are independent of the fixed irrational ratio. The factor \(D^4\) is a proved comparison, not a sharp constant.

A measurable budget \(K_I:I\to[0,\infty]\) is admissible if for almost every \(\beta\in I\) there are vectors
\[
t=u_q+u_p+u_{q^\beta},\qquad u_v\in\mathcal C_v,\qquad
\|u_q\|^2+\|u_p\|^2+\|u_{q^\beta}\|^2\le K_I(\beta).
\tag{3}
\]
All costs are sums of **squared physical norms**. For every \(s>0\), existence of such a budget with \(\int_I K_I^s<\infty\) is equivalent to existence of an admissible budget with finite \(s\)-moment on the whole interval \((1,2)\). For every \(r>0\), the same equivalence holds for
\[
\int_I\exp(\lambda K_I^r)<\infty\quad\text{for some }\lambda>0,
\tag{4}
\]
allowing \(\lambda\) to change between intervals.

In addition, for every fixed irrational \(\alpha\), the set of third-seed ratios admitting an exact decomposition (3) has measure either zero or one in \((1,2)\). This is a zero-one law, not a decision between its two alternatives.

## 1. Rational shifts preserve the full series up to a fixed factor

For every integer \(a\) and positive integer \(D\),
\[
\boxed{D^{-4}S(\beta)\le S(\beta+a/D)\le D^4S(\beta).}
\tag{5}
\]
Indeed, keep just the indices \(Dn\) in the shifted nonnegative series. The elementary inequalities \(\|Dx\|\le D\|x\|\) give
\[
\begin{aligned}
S(\beta+a/D)
&\ge\sum_{n\ge1}
\frac1{D^2n^2(\|Dn\alpha\|^2+\|Dn\beta+na\|^2)}\\
&\ge D^{-4}\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}.
\end{aligned}
\tag{6}
\]
The argument applies first to the finite subset \(D,2D,\ldots,DN\), then passes to the limit by monotonicity. Applying the same lower bound with base point \(\beta+a/D\) and shift \(-a/D\) proves the upper bound. Thus (5) also holds when either side is infinite. There is no interchange of conditionally convergent sums, independence assumption, or estimate for the distribution of \(n\alpha\).

The cutoff changes: if \(S_N\) denotes the first \(N\) terms, the directly proved finite inequalities are
\[
S_{DN}(\beta+a/D)\ge D^{-4}S_N(\beta),\qquad
S_{DN}(\beta)\ge D^{-4}S_N(\beta+a/D).
\tag{7}
\]
No comparison with the same cutoff on both sides is asserted.

## 2. A finite rational cover transports every cost tail

Work on \(\mathbb T=\mathbb R/\mathbb Z\), identifying \(I\) with its image there. The \(D\) translates \(I+j/D\), \(0\le j<D\), cover \(\mathbb T\): an interval longer than \(1/D\) contains a member of every translated grid with mesh \(1/D\). For any \(x\) in a covering translate, put \(y=x-j/D\in I\). By (5), \(S(x)\le D^4 S(y)\). Consequently,
\[
\{S>D^4R\}\subseteq
\bigcup_{j=0}^{D-1}\bigl((I\cap\{S>R\})+j/D\bigr).
\tag{8}
\]
Translation invariance of measure proves the lower bound in (2); the upper bound is inclusion.

More generally, for every nonnegative increasing Borel function \(\Phi\), defined also at infinity by its increasing limit,
\[
\boxed{\int_{\mathbb T}\Phi(S/D^4)\le D\int_I\Phi(S)
\le D\int_{\mathbb T}\Phi(S).}
\tag{9}
\]
To prove the first inequality, integrate over the covering translates, allowing overlaps, and use (5) after translation back to \(I\). All integrals may be infinite. Taking \(\Phi(u)=u^s\) yields
\[
\int_I S^s\le\int_{\mathbb T}S^s
\le D^{4s+1}\int_I S^s.
\tag{10}
\]
Taking \(\Phi(u)=\exp(\lambda u^r)\) shows that finiteness on \(I\) at parameter \(\lambda\) implies finiteness on \(\mathbb T\) at parameter \(\lambda/D^{4r}\). The converse follows by restriction. This retains the exponent \(r\), not the largest possible \(\lambda\).

## 3. Transport to the physical target retains all three norms

NB-356 and NB-360 give constants \(c,C>0\), uniform for \(\beta\in[1,2]\), such that every exact decomposition in (3) has squared cost at least \(cS(\beta)\). If \(S(\beta)<\infty\), their construction supplies an exact decomposition of cost at most \(C(1+S(\beta))\).

The relevant normalization is
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bb/s,\quad b=B(1)>0,\qquad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})},
\tag{11}
\]
where \(H^2=H^2(\Re s>1/2)\) has boundary squared norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). Removing \(B\) on its range is isometric. At the nonzero zero lattice \(z_k=1+2\pi ik/\log q\) of \(\Theta_q\), target squared samples are comparable to \(k^{-2}\), and
\[
|\Theta_p(z_k)|^2+|\Theta_{q^\beta}(z_k)|^2
\asymp\delta_{|k|}^2+\||k|\beta\|^2.
\]
The constants are uniform because \(q\le q^\beta\le q^2\). Bounded lattice sampling gives the lower cost. Its explicit bounded right inverse lifts the minimum-norm split of these samples to the two non-anchor components with squared norm sum \(H_\beta\ll S(\beta)\). The remaining numerator vanishes at all zeros of the pure Blaschke factor \(\Theta_q\), so division supplies the anchor component, of norm at most \(b+\sqrt{2H_\beta}\). Thus the upper bound prices all three components. The removable point \(s=1\) is not a zero.

It follows, on either parameter domain \(J=I\) or \(J=(1,2)\), that
\[
\exists K_J\text{ admissible with }\int_JK_J^s<\infty
\quad\Longleftrightarrow\quad\int_JS^s<\infty.
\tag{12}
\]
Necessity uses \(cS\le K_J\); sufficiency uses the measurable certificate \(K_J=C(1+S)\). The same equivalence holds for existence of a positive stretched-exponential parameter: for any \(r>0\), \((1+u)^r\le\max(1,2^{r-1})(1+u^r)\), so constants can be absorbed by reducing \(\lambda\). Equations (9)–(12) prove the claimed local/global budget equivalences without assuming measurability or attainment of a varying energy optimizer.

## 4. Completion itself obeys a zero-one law

Let \(\mathcal A=\{\beta\in\mathbb T:S(\beta)<\infty\}\). It is measurable, since the partial sums are continuous and increase to \(S\). Equation (5) gives exact invariance under every rational translation.

For a direct ergodic argument, put \(h=\mathbf1_{\mathcal A}\in L^2(\mathbb T)\). For every nonzero Fourier index \(k\), choose \(D>|k|\). Invariance under translation by \(1/D\) gives
\[
\widehat h(k)=e^{2\pi ik/D}\widehat h(k),
\]
so \(\widehat h(k)=0\). Completeness of the Fourier basis makes \(h\) constant almost everywhere. Since it is an indicator, \(m(\mathcal A)\in\{0,1\}\). Exact membership from NB-356 identifies this with the completion assertion.

Positive-measure existence anywhere therefore implies almost-everywhere completion. This argument does not promote existence at a single seed to measure one: its rational translates supply only a countable dense set. No example of a nonempty null completion set is established here. Nor does measure one mean every seed completes. At a rational \(\beta=a/D\), the sublattice \(n=Dk\) gives
\[
S(a/D)\ge D^{-2}\sum_{k\ge1}\frac1{k^2\|kD\alpha\|^2}=\infty,
\tag{13}
\]
because infinitely many convergent denominators of the irrational \(D\alpha\) have \(\|kD\alpha\|<1/k\). This is the existing NB-360 rational obstruction, consistent with the new zero-one conclusion.

## Consequences, prior art, and boundaries

The full-interval criteria now hold on **every fixed nonempty open interval** of third-seed ratios:

- NB-363's logarithmic-power condition \(W(N)=\sum_{n\le N}(n^2\delta_n^2)^{-1}=O((\log(eN))^\kappa)\) is equivalent to a local physical budget satisfying \(\int_I\exp(\lambda K_I^{1/\kappa})<\infty\) for some \(\lambda>0\). In particular, the bounded quadratic mean of the continued-fraction digits still characterizes ordinary exponential budgets even when \(I\) stays away from the repeated seed at \(\beta=1\).
- NB-364's open power-moment range and its exact mean criterion \(\sum_jQ_{j+1}/Q_j^2<\infty\) remain unchanged on \(I\). Localizing cannot repair a divergent endpoint moment. No new classification of the undecided other endpoints is supplied.

Beresnevich and Velani, *A note on zero-one laws in metrical Diophantine approximation*, Acta Arith. 133 (2008), 363–374, DOI `10.4064/aa133-4-5`, [author manuscript, Introduction and Lemma 2](https://arxiv.org/pdf/0803.2355), treats classical Cassels–Gallagher-type laws and the ergodic role of rational transformations. Beresnevich, Haynes and Velani, [Section 10.1, Lemma 10.1](https://arxiv.org/pdf/1511.06862), uses a classical zero-one law for a fixed-coordinate approximation limsup set. Those are the neighboring metric mechanisms; a convergence set for the entire positive series (1) is not identified with a limsup set here. Its invariance and its quantitative local tail comparison are proved directly in (5)–(10). The zero-one principle itself is classical, not a novelty claim.

Burnol's [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055) give the common factor and target projection retained in (11). The physical interpolation bridge is already in NB-356 and NB-360. The local delta is the universal rational-shift comparison for this cost series and the resulting impossibility of improving a global budget-integrability threshold by selecting an open interval. No new general ergodic or Hardy interpolation theorem is claimed from absence of a search match.

- The interval is fixed before the budget limit. Its comparison constants deteriorate when its length shrinks; moving or budget-dependent intervals are not covered by a uniform claim.
- An arbitrary positive-measure parameter subset need not contain an interval. Equation (2) is not asserted for such a subset. The separate zero-one membership statement does apply to existence on a positive-measure subset, without giving its budget moments.
- The scalar comparison does not identify the optimal physical energy distribution, its sharp tail constant, or the largest exponential parameter. It also does not determine which side of the zero-one alternative holds for a general irrational pair.
- Only full closed real-dilation orbit vectors are priced. No finite generator count, dilation-range bound, absolute-coefficient bound, discrete Nyman-section rate, or conclusion for a specified integer third seed follows.
- Every orbit sum \(w\) still satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The common Burnol floor is unchanged; no zeta-zero exclusion or RH conclusion is obtained.

Evidence is the analytic derivation and the inspected primary sources. Ephemeral exact-rational controls passed 2,280 instances of the reindexed inequalities (7) and 3,988 rational-grid cover checks. They test finite inequalities and coverage, not convergence of an irrational series or any measure-theoretic limit. The decisive audits are retaining the changed cutoff, using both directions of (5), permitting a reduced exponential parameter, pricing the anchor component, and distinguishing a positive-measure set from a single completing seed. No Lean verification or independent adversarial approval is asserted.
