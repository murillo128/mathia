# NB-346 — Fixed rational offsets reveal a parity law at arbitrarily large dilations

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-336, NB-338, NB-339, NB-344, NB-345
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + RATIONAL-OFFSET-PARITY + UNBOUNDED-DILATION-UNIFORMITY + EVEN-DENOMINATOR-LOG-ENHANCEMENT + ODD-DENOMINATOR-FINITE-LIMIT + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Retain the canonical finite Nyman section, integer dilation, rank-one comparator and physical adjacent witness:
\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\qquad
T_{n,m}=P_{U_n}A_m|_{U_n},\qquad
E_{n,m}=\sqrt m\,T_{n,m}-R_n,\qquad
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\]
Fix a reduced nonintegral rational number
\[
t=\frac{p}{B},\qquad B\ge2,\quad \gcd(|p|,B)=1,\quad
0<|t|\le\frac12.
\]
Let \(q\to\infty\) through multiples of \(B\), choose **any** integers \(A_q\ge2\), without any upper growth restriction, and set
\[
m_q=A_q q(q-1)+tq,\qquad n\ge q,\qquad
\mathcal F_{n;q,m_q}=\langle E_{n,m_q}g_2,\nu_q\rangle .
\tag{1}
\]
All \(m_q\) are positive integers and the exact adjacent selector of NB-338 is admissible for large \(q\), for either sign of \(t\).

**Even denominator.** If \(B\) is even, then, uniformly over the complete sequence \(A_q\ge2\) and every \(n\ge q\),
\[
\boxed{\displaystyle
m_q\mathcal F_{n;q,m_q}
=\frac{|p|}{4B^2}\log q+O_{p,B}(1).
}
\tag{2}
\]
In particular the leading logarithmic coefficient is positive and does not depend on the multiple \(A_q\). Taking \(q=n\) and applying the *physical* Hilbert norm bound of NB-304,
\[
\boxed{\displaystyle
\liminf_{\substack{n\to\infty\\B\mid n}}
\frac{m_n}{n\sqrt{\log n}}\,
\|E_{n,m_n}\|
\ge\frac{|p|}{2B^2\sqrt{2\log2}}>0.
}
\tag{3}
\]
At the half-cell \(t=\pm1/2\), this reads \(m_q\mathcal F=(\log q)/16+O(1)\) and the right side of (3) is \(1/(8\sqrt{2\log2})\).

**Odd denominator.** If \(B\) is odd, write
\[
H=\frac{\pi^2}{72},\quad
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^{2}}{k^2},\quad
S_2(x)=H-\mathfrak D(x),\quad
\Lambda_{p,B}
=\sum_{k\ge1}\frac{f'(kp/B)}{k},
\qquad f(x)=\|x\|_{\mathbb Z}^2 .
\]
The slopes are well-defined for odd \(B\), have zero mean over residues and make the last series convergent by Dirichlet's test, exactly as in NB-339. Then, uniformly in \(A_q\ge2\) and \(n\ge q\),
\[
\boxed{\displaystyle
m_q\mathcal F_{n;q,m_q}
=-\frac12 S_2(t)
-\frac14\left(t\Lambda_{p,B}
+\frac{|t|\log2}{B}\right)
+O_{p,B}(q^{-1}).
}
\tag{4}
\]
Thus at fixed rational offsets from arbitrarily large common multiples, **even denominators produce logarithmic growth of the normalized coefficient, while odd denominators have a finite explicit limit**. This dichotomy is about the physical source/observer coefficient, not the target approximation distance.

## Exact uniform reduction

Set
\[
u=\frac{m_q}{q}=A_q(q-1)+t,\qquad
v=\frac{m_q}{q-1}=A_q q+\frac{tq}{q-1},
\qquad c=\frac{q-1}{q}.
\]
Then \(cv=u\) and, modulo integers,
\[
u\equiv t,\qquad
v\equiv t+\delta_q,\qquad
\delta_q=\frac{t}{q-1}.
\tag{5}
\]
The crucial point is that **the fractional displacement is exactly independent of \(A_q\)**, even if the latter grows superpolynomially. Moreover \(u\ge q\) for all sufficiently large \(q\).

The exact alternating selector identity NB-338(13) and the uniform Bernoulli expansion NB-339(13) yield the identity-with-error NB-345(5):
\[
m_q\mathcal F_{n;q,m_q}
=\frac q4\,[c^2S_2(v)-S_2(u)]
+\frac q{6u}\,[c^3S_3(v)-S_3(u)]
+O(q/u^2),
\tag{6}
\]
where
\[
S_j(x)=\sum_{k\ge1}\frac{(-1)^{k+1}B_j(kx)}{k^j},
\qquad j=2,3.
\]
All sums and Bernoulli-tail errors in (6) are controlled absolutely and uniformly across integer folds; no differentiation under the fractional-part series occurs. In particular \(S_3\) is periodic, bounded and globally Lipschitz. Since \(v-u=A_q+\delta_q\) modulo integers and \(c^3-1=O(q^{-1})\),
\[
|c^3S_3(v)-S_3(u)|=O_{t}(q^{-1}).
\]
Thus the second term in (6) and its remainder are each \(O_t(q^{-1})\), with a constant independent of \(A_q\) and \(n\).

The exact finite normalization must **not** be suppressed:
\[
\frac q4(c^2-1)=-\frac12+\frac1{4q}.
\tag{7}
\]
Use periodicity, (5), and the global modulus
\(\left|\mathfrak D(x+h)-\mathfrak D(x)\right|
\ll|h|\log(e/|h|)\) from NB-337. Equations (6)--(7) give the common master formula
\[
\boxed{\displaystyle
m_q\mathcal F_{n;q,m_q}
=-\frac q4\left[\mathfrak D(t+\delta_q)-\mathfrak D(t)\right]
-\frac12\left[H-\mathfrak D(t)\right]
+O_t\left(\frac{\log q}{q}\right).
}
\tag{8}
\]
This error is uniform in **all** integers \(A_q\ge2\) and \(n\ge q\). For odd denominator, NB-339's quadratic local remainder improves it to \(O_{p,B}(q^{-1})\).

## Rational cusp evaluation

For even reduced denominator \(B\), NB-336(2) proves the two-sided local expansion
\[
\mathfrak D(t+h)-\mathfrak D(t)
=-\frac{|h|}{B}\log\frac1{|h|}+O_B(|h|).
\tag{9}
\]
Since \(|\delta_q|=|t|/(q-1)\),
\[
-\frac q4[\mathfrak D(t+\delta_q)-\mathfrak D(t)]
=\frac{q|t|}{4B(q-1)}
\log\frac{q-1}{|t|}+O_{p,B}(1)
=\frac{|p|}{4B^2}\log q+O_{p,B}(1).
\]
The remaining normalization term of (8) is bounded, so (2) follows. The sign is positive for either \(p>0\) or \(p<0\), since the even-denominator cusp is two-sided.

For odd reduced denominator, NB-339(2) supplies the sharper two-sided formula
\[
\mathfrak D(t+h)
=\mathfrak D(t)+\Lambda_{p,B}h+\frac{\log2}{B}|h|
+O_{p,B}(h^2).
\tag{10}
\]
Substitution of \(h=\delta_q=t/(q-1)\) into (8), using
\(q\delta_q=t+O_t(q^{-1})\) and
\(q|\delta_q|=|t|+O_t(q^{-1})\), gives (4).
There is no hidden logarithm in the odd-denominator limit.

The parity contrast cannot be inferred from NB-345's global Lipschitz-modulus estimate alone: for \(|h|\asymp q\), its error is \(O(\log q)\), precisely as large as the even-denominator main term. Fixed-\(A_q\) specializations also follow from NB-338 and NB-339; the additional conclusion here is the **same asymptotic with no restriction whatsoever on \(A_q\)**, obtained by retaining the uniform inverse-dilation Bernoulli errors from NB-345. Formula (8) is the reusable finite-normalization bridge.

## Physical norm and falsification controls

NB-304 gives the actual Hilbert-space estimates
\[
\|g_2\|_2=\frac{\sqrt{\log2}}2,\qquad
\|\nu_n\|_2^2\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2}
\quad(H_j=\textstyle\sum_{k=1}^j1/k).
\]
Cauchy--Schwarz yields
\[
\|E_{n,m_n}\|\ge
\frac{2n|\mathcal F_{n;n,m_n}|}
{\sqrt{\log2}\sqrt{2H_{n-2}+1+\pi^2/18}}.
\tag{11}
\]
For even \(B\), (2) and \(H_{n-2}/\log n\to1\) give
\[
\liminf_{B\mid n}\frac{m_n\|E_{n,m_n}\|}{n\sqrt{\log n}}
\ge\frac{2}{\sqrt{2\log2}}\frac{|p|}{4B^2},
\]
which is exactly (3). No uncontrolled Gram whitening or coefficient norm is substituted for the physical Nyman metric.

As an arithmetic sign check, the leading \(S_2\) term of (6) can be evaluated at rational arguments using
\[
\mathfrak D(P/Q)=Q^{-2}
\sum_{r=1}^{Q}
\left\|\frac{Pr}{Q}\right\|_{\mathbb Z}^2
\psi_1(r/Q),
\]
where \(\psi_1\) denotes trigamma. For \(t=1/2\), this Bernoulli main term gives \(m_q\mathcal F\) approximately \(0.33501,0.38190,0.42729,0.47178\) at \(q=40,80,160,320\), versus the asymptotic \((\log q)/16+O(1)\). For the odd control \(t=1/3\), it gives \(-0.03912,-0.03964,-0.03990\) at \(q=60,120,240\), converging toward the explicit limit \(-0.04015057\ldots\) from (4). These are checks of the **leading Bernoulli approximation**, not evaluations of the complete exact series, and neither replaces (6)--(10).

The requirement that \(t=p/B\) be fixed matters. No uniform estimate in growing \(B\), moving \(p/B\), or offsets approaching a rational at a variable rate is asserted. At \(t=0\), equation (8) instead reproduces NB-344's exact-divisibility finite constant \(-\pi^2/144\); the \(t\ne0\) even-denominator law is therefore **not** a continuous uniform limit as \(t\to0\) with \(q\). For odd \(B\), the limit in (4) may have either sign or vanish; (4) is not an automatic norm lower bound.

## Prior art and scientific boundary

Báez-Duarte--Balazard--Landreau--Saias, *Étude de l'autocorrélation multiplicative de la fonction partie fractionnaire*, Ramanujan Journal 9 (2005), 215--240, DOI 10.1007/s11139-005-0834-4, and Balazard--Martin, *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et une fonction définie par J. R. Wilton*, arXiv:1305.4395, establish the surrounding fractional-part autocorrelation and rational-regularity setting. Burrin--Lee--Marmi, *The Brjuno and Wilton functions*, Mathematika 72 (2026), DOI 10.1112/mtk.70068, is a more recent related rational-regularity reference. None is invoked as the theorem proving (2)--(4); the load-bearing ingredients are the exact local derivations NB-336, NB-338, NB-339 and NB-345. No bibliographic priority is claimed and no external result requiring a new SOURCES.md dependency is imported.

This is an **operator source/witness** result. It does not bound the true approximation distance \(\operatorname{dist}(\mathbf1,U_n)\), control occupation by the first-free Ford target, or address inverse-section conditioning or off-critical-zero contraction. The lower bound (3) remains \(O(n\sqrt{\log n}/m_n)\) in unweighted terms and tends to zero since \(m_n\ge n^2\). It gives neither a nonzero limiting mixing gap nor an implication for RH.

## Research consequence

The normalization residue at exact local common multiples (NB-344) has two sharply different arithmetic continuations. Perturbations \(h=o(q/\log q)\) preserve its finite coefficient (NB-345), but **fixed nonintegral rational fractions of \(q\)** reveal a different regime: even denominators generate a logarithmically amplified physical coefficient while odd denominators settle to an explicitly computable finite value, both uniformly over arbitrarily rapid dilation growth. This settles the parity and scale-uniformity of that adjacent source channel; the genuinely target-sensitive Nyman approximation bridge remains open.
