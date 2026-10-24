# NB-354 — Finite-seed real-dilation spaces have an exact target-loss classification

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-351–NB-353 for the source-compression question; Burnol's factorization and the scalar Beurling–Lax theorem
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-DISTANCE + PRIOR-ART-CLASSICALIZATION

## Claim and scope

The real-dilation extension left open in NB-351–NB-353 has an exact classification. Two multiplicatively independent seed indices recover the whole **continuous** Nyman space. Commensurable seed indices retain an explicit additional target-loss factor. This determines the unrestricted closure and its target distance, while leaving coefficient cost and finite approximation rates separate.

In \(H=L^2(0,1;dx)\), write
\[
e(x)=1,\qquad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a}.
\]
For a nonempty finite set \(J\subset\mathbb N_{\ge2}\), define
\[
\mathcal C_J=\overline{\operatorname{span}}
\{A_ag_j:a\ge1\text{ real},\ j\in J\}.
\tag{1}
\]
The closure is in the full physical Hilbert norm; coefficients and the number and sizes of dilations are unrestricted. Let
\[
\mathcal N=\overline{\operatorname{span}}
\{\rho_\alpha:0<\alpha<1\},\qquad
\rho_\alpha(x)=\{\alpha/x\}-\alpha\{1/x\}.
\]
Let \(B\) be the half-plane Blaschke product of all zeta zeros with real part greater than \(1/2\), counted with multiplicity and normalized by \(b:=B(1)>0\). Burnol's theorem gives
\[
\mathcal M\mathcal N=B H^2(\Re s>1/2),\qquad
b^2=\prod_{\Re\rho>1/2}
\left|\frac{1-\rho}{\rho}\right|^{2m_\rho},\qquad
\operatorname{dist}(e,\mathcal N)^2=1-b^2.
\tag{2}
\]
An empty product is one. No value or effective evaluation of \(b\) is assumed.

There are exactly two cases:

1. If \(J\) contains \(p,q\) with \(\log p/\log q\notin\mathbb Q\), then
   \[
   \boxed{\mathcal C_J=\mathcal N,\qquad
   \operatorname{dist}(e,\mathcal C_J)^2=1-b^2.}
   \tag{3}
   \]
2. Otherwise there is a unique integer \(r\ge2\) such that every \(j\in J\) has the form
   \(j=r^{k_j}\), with positive integers \(k_j\) having greatest common divisor one. Then
   \[
   \boxed{\mathcal C_J=\mathcal C_{\{r\}},\qquad
   \operatorname{dist}(e,\mathcal C_J)^2
   =1-b^2\frac{r(\log r)^2}{(r-1)^2}.}
   \tag{4}
   \]
   The base \(r\) need not itself belong to \(J\).

In particular, the geometric space of NB-351 has the exact real-dilation distance
\[
d_q^2=(1-b^2)+b^2\varepsilon_q,\qquad
\varepsilon_q=1-\frac{q(\log q)^2}{(q-1)^2}.
\tag{5}
\]
Adding the entire real-dilation orbit of an independent seed recovers exactly \(b^2\varepsilon_q\) of squared target projection norm. This is positive unconditionally because \(b>0\). It is not a claim that the remaining distance \(1-b^2\) vanishes.

## 1. An explicit elementary inner factor

Use the unitary Mellin transform
\[
\mathcal Mf(s)=\int_0^1f(x)x^{s-1}\,dx,
\qquad
\|\mathcal Mf\|_{H^2}^2
=\frac1{2\pi}\int_{\mathbb R}|\mathcal Mf(1/2+it)|^2dt.
\]
It sends \(e\) to the unit-norm reproducing kernel \(k_1(s)=1/s\) and sends \(A_a\) to multiplication by \(a^{1/2-s}\). Put
\[
F(s)=\frac{(s-1)\zeta(s)}{s^2},\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
                 \frac{1-j^{1-s}}{1-j^{-s}}.
\tag{6}
\]
All apparent singularities at \(s=1\) are removable. In particular
\[
F(1)=1,\qquad \Theta_j(1)=\frac{\sqrt j\log j}{j-1}>0.
\tag{7}
\]
The exact factorization is
\[
\boxed{\mathcal Mg_j(s)
=\frac{\zeta(s)}s(j^{-1}-j^{-s})
=F(s)\Theta_j(s)\frac{1-j^{-s}}{\sqrt j}.}
\tag{8}
\]

To identify \(\Theta_j\), let \(w=j^{1/2-s}\) and \(a=j^{-1/2}\). The function
\[
J_j(s)=\frac{a-w}{1-aw}
=\frac1{\sqrt j}\frac{1-j^{1-s}}{1-j^{-s}}
\]
is inner: it is a disk Blaschke factor composed with a map into the disk, and its modulus is one on \(\Re s=1/2\). Its simple zeros are \(1+2\pi i\ell/\log j\), \(\ell\in\mathbb Z\). Dividing by the half-plane Blaschke factor \((s-1)/s\) removes precisely the zero with \(\ell=0\), so \(\Theta_j\) is inner with simple zeros
\[
\Lambda_j=\{1+2\pi i\ell/\log j:\ell\in\mathbb Z\setminus\{0\}\}.
\tag{9}
\]
There is no additional singular inner factor: \(\Theta_j\) extends holomorphically and nonvanishingly through every finite point of the boundary line, and \(\Theta_j(\sigma)\to j^{-1/2}>0\) as real \(\sigma\to\infty\), excluding an exponential delay factor. Thus it is the pure Blaschke product for (9), with the phase fixed by (7).

The last multiplier in (8) and its inverse are bounded analytic on the half-plane, since
\[
1-j^{-1/2}\le |1-j^{-s}|\le1+j^{-1/2}.
\tag{10}
\]
It is therefore outer. Burnol's factorization says that \(F\in H^2\) has inner factor exactly \(B\). Consequently the inner factor of \(\mathcal Mg_j\) is exactly \(B\Theta_j\), with no missing singular or exponential factor. The removed zero at \(s=1\) matters: retaining it would incorrectly make the target orthogonal to every seed orbit.

## 2. The orbit space is determined by common inner divisors

Under \(Uf(t)=e^{-t/2}f(e^{-t})\), the isometries \(A_a\) become all right translations by \(\log a\ge0\), with zero extension. The scalar Beurling–Lax theorem therefore applies to (1). Its Mellin image is \(I_JH^2\), where \(I_J\) is the greatest common inner divisor of the functions in (8).

For clarity, this use of the theorem includes minimality. An invariant space \(IH^2\) contains every seed exactly when \(I\) divides every seed's inner factor. The smallest such space is obtained from the greatest common inner divisor. Hence
\[
I_J=B\,\gcd_{j\in J}\Theta_j.
\tag{11}
\]
This step needs invariance under **all real dilations**. Integer-dilation invariance alone does not justify (11).

The factors \(\Theta_j\) are pure Blaschke products with simple zeros, so their common divisor is determined by the intersection of (9). A nonzero height \(t\) belongs to that intersection exactly when
\[
\frac{t\log j}{2\pi}\in\mathbb Z\qquad(j\in J).
\tag{12}
\]
If one log ratio is irrational, (12) is impossible and the common divisor is one.

If all ratios are rational, the prime-valuation vectors of the integers in \(J\) lie on one rational ray. Choose its primitive nonnegative integer vector \(v\), so each valuation vector is \(n_jv\) with \(n_j\in\mathbb N\). Put \(d=\gcd_j n_j\) and \(r=\prod_p p^{d v_p}\). Then \(j=r^{k_j}\), \(k_j=n_j/d\), and \(\gcd_j k_j=1\). Conversely this representation determines \(r\) uniquely. Bézout's identity shows that (12) is equivalent to
\[
\frac{t\log r}{2\pi}\in\mathbb Z.
\]
The common zeros are exactly \(\Lambda_r\), each still simple. Thus the common inner divisor is \(\Theta_r\), up to an irrelevant unit scalar. This proves the space classifications in (3)–(4).

## 3. Actual target projection and recovered energy

Take the inner product linear in its first argument. For any inner function \(I\), multiplication \(M_I\) is an isometry and the reproducing property gives
\[
M_I^*k_1=\overline{I(1)}k_1,\qquad
P_{IH^2}k_1=\overline{I(1)}\frac{I(s)}s.
\tag{13}
\]
Since \(\|k_1\|=1\),
\[
\operatorname{dist}(k_1,IH^2)^2=1-|I(1)|^2.
\tag{14}
\]
Substituting (7) and (11) proves the target-distance formulae. This also shows why removing a common inner factor from the generators without transporting its action on the target would lose the factor \(b^2\).

For \(\log p/\log q\notin\mathbb Q\), nested orthogonal projections give the exact gain
\[
\boxed{\|(P_{\mathcal C_{\{q,p\}}}-P_{\mathcal C_{\{q\}}})e\|^2
=b^2\varepsilon_q.}
\tag{15}
\]
The old elementary certificate \(\varepsilon_q\) remains valid: (5) differs from it by \((1-b^2)(1-\varepsilon_q)\ge0\). It is sharp for the actual real-dilation space precisely when \(b=1\), equivalently RH. This is a conditional equality characterization, not evidence for RH.

## Controls and implication for the coefficient obstruction

- A single seed gives (5). The sets \(\{4,8\}\) and \(\{4,16\}\) give primitive bases \(2\) and \(4\), respectively. The set \(\{2,3\}\) gives (3). These distinguish rational log dependence from the ordinary integer greatest common divisor of the seed indices.
- No claim is made that \(\mathcal C_{\{2,3\}}=H\) unconditionally: it equals \(\mathcal N\), which retains every interior zeta-zero obstruction. Zeros on the critical line are boundary zeros, not extra inner factors.
- No equality with the closed **discrete** arithmetic span is used. Replacing all real dilation parameters by integers, or bounding their range, removes a load-bearing hypothesis.
- These are closed-span statements with unrestricted coefficient cost. NB-353 still bounds every fixed-budget family. Under RH, for example, finite sums from the two real orbits \(g_2,g_3\) can approach \(e\), but every such sequence must have the added \(g_3\) cost \(R\) satisfying \((1+R)\log(e+R)\gtrsim1/\varepsilon\), where \(\varepsilon\) is its error. Equations (3) and (15) supply no rate or coefficient upper bound.

The substantive consequence is the sharp distinction between source exclusion and coefficient conditioning. A finite patch cannot remove NB-351's target obstruction (NB-352), but a whole independent seed orbit removes exactly its additional geometric component. A positive unrestricted seed-induced excess over the full continuous target distance for two independent real seed orbits would contradict (3); the common zeta-zero floor remains. Any constructive continuation must now price coefficient growth and dilation resolution, not merely rule out an exact common zero.

## Prior art and evidence boundary

This is a classical-factorization specialization, not a new invariant-subspace theorem or RH criterion. Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the factorization and full-space projection in (2), as well as the Mellin identity. Lax, *Translation invariant spaces*, Acta Math. 101 (1959), 163–178, DOI `10.1007/BF02559553`, [scalar representation theorem, Section 2.1](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5881-11511_2007_Article_BF02559553.pdf), supplies the invariant-space classification used in (11). The elementary factor (6), its common-zero arithmetic, and substitution into target projection give the stated finite-seed specialization.

The literature check covered restricted generators, finite families of dilation orbits, common inner divisors, and multiplicatively independent bases. Carvill's [2025 ladder preprint, Sections 3–4](https://arxiv.org/pdf/2510.18132) studies a discrete two-base parameter set and smoothed Gram entries; that is a different family from all real dilations of two fixed seeds. No result from it is used. No novelty is inferred from absence of a matching search result.

Locally, NB-052 already retains the Burnol factor in target comparisons. The present application determines the entire seed-dependent factor, closes the real-orbit alternative in NB-351–NB-353, and quantifies its recovered target mass. It does not reopen the accepted finite-section or source-access clues with a new name.

The evidence is the exact derivation (6)–(15) using the stated classical theorems. A counterexample would have to invalidate the elementary factorization, the absence of an additional inner factor, the real-translation hypothesis, or the target projection normalization. No numerical distance certificate, Lean proof, finite-section rate, or independent adversarial validation is asserted.
