# PL-194 — Arbitrary scalar prime-shift covariance is diagonal under normality, and self-adjoint resolvents force trivial weights

**Status:** negative result / structural collapse  
**Evidence class:** DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let \(\mathcal H=\ell^2(\mathbb N)\) with basis \(e_n\), and let \(S_p e_n=e_{pn}\) for each prime \(p\). Suppose a bounded nonzero normal operator \(T\) satisfies
\[
T S_p=\lambda_p S_pT,\qquad \lambda_p\in\mathbb C.
\]
Then there is \(c\neq0\) such that
\[
T e_n=c\,\lambda(n)e_n,\qquad
\lambda(n)=\prod_p\lambda_p^{v_p(n)},
\]
and boundedness forces \(|\lambda_p|\le1\) for every prime.

Thus allowing non-unit scalar weights enlarges the phase case only to diagonal completely-multiplicative contractions; it does not create nontrivial prime-direction mixing.

If, more specifically, \(T=(H-i)^{-1}\) is the resolvent of a self-adjoint operator \(H\), then every \(\lambda_p=1\). Hence \(T=cI\) and \(H\) is scalar. In particular, the non-unit scalar-weight loophole left open by PL-193 does not provide a Hilbert–Pólya escape.

## Derivation

Put \(x=Te_1\). Covariance and unique factorization give
\[
Te_n=\lambda(n)S_nx.
\]
For \(n>1\), \(S_nx\) is supported on multiples of \(n\), so \(\langle Te_n,e_1\rangle=0\). Therefore
\[
T^*e_1=\overline{x_1}e_1.
\]
Normality yields
\[
\|x\|=\|Te_1\|=\|T^*e_1\|=|x_1|,
\]
hence \(x=x_1e_1\). Writing \(c=x_1\) gives the diagonal formula. Since \(p^k\) occurs for every \(k\ge0\),
\[
\|T e_{p^k}\|=|c|\,|\lambda_p|^k\le\|T\|,
\]
so \(|\lambda_p|\le1\).

Now take \(T=R=(H-i)^{-1}\). Since \(R\) is the resolvent of a self-adjoint \(H\), every diagonal value
\[
r_n=c\,\lambda(n)
\]
satisfies the resolvent-circle identity
\[
\operatorname{Im}r_n=|r_n|^2>0.
\]
Fix \(p\), set \(a=\lambda_p=q e^{i\theta}\), and write \(c=\rho e^{i\phi}\). Then for all \(k\ge0\),
\[
\sin(\phi+k\theta)=\rho q^k.
\]
The resolvent has no zero eigenvalue, so \(q>0\), and boundedness gives \(q\le1\).

If \(q<1\), the right side tends to zero. Hence the fixed-step sequence \(\phi+k\theta\) approaches \(0\) modulo \(\pi\), forcing \(\theta=0\) modulo \(\pi\); then the left side is constant or alternates sign, impossible because the right side is strictly positive and decays.

If \(q=1\), \(\sin(\phi+k\theta)=\rho>0\) for every \(k\). Applying
\[
\sin(x+2\theta)=2\cos\theta\,\sin(x+\theta)-\sin x
\]
to three consecutive terms gives \(\cos\theta=1\), hence \(a=1\).

Therefore \(\lambda_p=1\) for every prime. The covariance becomes exact commutation, and the diagonal formula gives \(R=cI\); consequently \(H\) is scalar.

## Adversarial audit

- This does **not** say arbitrary scalar covariance is impossible for bounded normal operators. If \(|\lambda_p|\le1\), the diagonal multiplier \(e_n\mapsto c\lambda(n)e_n\) is a genuine normal example. The collapse to \(\lambda_p=1\) uses the resolvent-circle geometry of a self-adjoint \(H\).
- The proof is tied to the standard one-sided prime shifts on \(\ell^2(\mathbb N)\)/Bohr \(\mathcal H^2\), especially the vacuum vector \(e_1\) and the support separation \(S_nx\perp e_1\) for \(n>1\).
- No claim is made for operator-valued cocycles, non-scalar \(K_p\), target-relative Nyman/model-space operators, different Hilbert weights, or covariance imposed only modulo compact/Schatten errors.
- The relation \(XS=\lambda SX\) for one unilateral shift belongs to the classical extended-commuting / weighted-composition literature; see source [62]. PL-193 already used that literature to treat unit phases. The present result is a derived many-prime normality/resolvent obstruction, not a claim that scalar covariance itself is novel.
- Source [26] classifies the exact commutant at \(\lambda_p=1\); the argument above does not rely on extending that theorem to \(|\lambda_p|<1\).

## Novelty assessment

The exact one-shift \(\lambda\)-commuting problem is prior art, and the phase case was already recorded in PL-193. I did not find a source in the line's prior-art surface stating this exact arbitrary-complex, simultaneous-prime, normal/resolvent collapse. The contribution here should therefore be read narrowly as a derived obstruction that closes a loophole in the line, not as a new general theorem about extended eigenoperators.

## Consequence for the line

After PL-193, one possible escape was to replace unit phases by attenuating or otherwise non-unit scalar weights. For a generic bounded normal operator that only produces diagonal, completely multiplicative contractions; for a self-adjoint resolvent even those weights collapse to \(1\). A viable spectral mechanism must therefore leave the scalar-covariance class altogether: genuinely operator-valued prime cocycles, target-sensitive couplings, or weaker relative relations are the remaining structurally distinct possibilities.
