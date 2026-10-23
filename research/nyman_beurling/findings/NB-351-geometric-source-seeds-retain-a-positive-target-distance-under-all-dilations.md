# NB-351 — Geometric source seeds retain a positive target distance under all dilations

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-350; classical Mellin and dilation framework
- **Classification:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + EXPLICIT-NORMED-DUAL + CLASSICAL-COMMON-ZERO-MECHANISM

## Claim and scope

NB-350 recovers the entire early-shell kernel by allowing the source index to grow with the integer dilation. An infinite geometric source family cannot replace that freedom: it reduces to one seed and retains an explicit positive distance from the actual Nyman target, even after allowing every real dilation.

In \(L^2(0,1;dx)\), write
\[
g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad e(x)=1,
\quad A_af(x)=\sqrt a\,f(ax)\mathbf1_{(0,1/a]}(x).
\]
Fix an integer \(q\ge2\). For an integer \(M\ge1\), put
\[
\mathcal C_{q,M}
=\overline{\operatorname{span}}\{A_mg_{q^k}:m\ge M,
\ m\in\mathbb N,\ k\ge1\}.
\]
Then
\[
\boxed{\mathcal C_{q,M}
=\overline{\operatorname{span}}\{A_mg_q:m\ge M,\ m\in\mathbb N\}.}
\tag{1}
\]
For the larger real-dilation space
\[
\mathcal C_q^{\mathrm{real}}
=\overline{\operatorname{span}}\{A_ag_{q^k}:a\ge1,\ k\ge1\},
\]
one has the unconditional target bound
\[
\boxed{\operatorname{dist}(e,\mathcal C_{q,M})^2
\ge \operatorname{dist}(e,\mathcal C_q^{\mathrm{real}})^2
\ge \varepsilon_q:=1-\frac{q(\log q)^2}{(q-1)^2}>0.}
\tag{2}
\]
The constant is the exact squared distance to the relaxation imposing only the common Mellin-zero lattice, not an asserted exact distance to either arithmetic or real-dilation source space.

Moreover, if \(\mathcal V=\overline{\operatorname{span}}\{g_j:j\ge2\}\), then
\[
\boxed{\operatorname{codim}_{\mathcal V}\mathcal C_{q,M}=\infty.}
\tag{3}
\]
For \(M\ge2\), NB-350's unrestricted late aggregate has codimension \(M-1\). This distinction concerns genuine closed source spaces, not a finite rank count. Adding a finite old section to \(\mathcal C_{q,M}\) cannot recover all of \(\mathcal V\); a target-distance bound for that enlarged space does not follow from (2) or (3).

## 1. Geometric seeds collapse to one seed

The integer-dilation identity gives
\[
g_{ab}=b^{-1}g_a+a^{-1/2}A_ag_b.
\]
Induction yields the exact finite expansion
\[
g_{q^k}=\sum_{r=0}^{k-1}q^{-(k-1)+r/2}A_{q^r}g_q.
\tag{4}
\]
After applying \(A_m\), every resulting dilation \(mq^r\) is still an integer at least \(M\). The reverse inclusion follows from \(k=1\), proving (1). The same argument works with real dilation factors. No coefficient bound or closure equivalence is assumed.

## 2. A bounded dual witness in physical space

Let \(L=\log q\). Define \(h_q\) on \((1/q,1]\) and extend it multiplicatively periodically to \((0,1]\):
\[
h_q(u)=1-\frac{L}{(q-1)u},\qquad
h_q(q^{-r}u)=h_q(u)\quad(r\ge0).
\tag{5}
\]
Endpoint values do not affect the Hilbert-space statements. This is a bounded measurable function, and
\[
\int_{1/q}^1 h_q(u)\frac{du}{u}=0.
\tag{6}
\]
More generally, every multiplicatively \(q\)-periodic bounded function \(H\) with zero logarithmic mean satisfies
\[
\int_0^1H(x)g_q(x)\,dx=0.
\tag{7}
\]
Indeed, with \(r(x)=\{1/x\}\), including the support cutoff gives
\[
g_q(x)=r(qx)\mathbf1_{x\le1/q}
 +\frac{\mathbf1_{x>1/q}}{qx}-q^{-1}r(x).
\]
In the first integral substitute \(y=qx\). Periodicity cancels it against the last integral, leaving exactly
\(q^{-1}\int_{1/q}^1H(x)\,dx/x=0\).
All integrals converge absolutely; no separate integration of an unbounded fractional-part surrogate is used.

For any real \(a\ge1\), the function \(H(y)=h_q(y/a)\) is again \(q\)-periodic with zero logarithmic mean. Thus
\[
\langle h_q,A_ag_q\rangle
=a^{-1/2}\int_0^1h_q(y/a)g_q(y)\,dy=0.
\tag{8}
\]
Equation (4) extends this to all geometric seeds and their closed span.

Summing the geometric cells in (5) gives, by elementary integration,
\[
\langle e,h_q\rangle
=\frac{q}{q-1}\int_{1/q}^1
\left(1-\frac{L}{(q-1)u}\right)du=\varepsilon_q,
\]
\[
\|h_q\|_2^2
=\frac{q}{q-1}\int_{1/q}^1
\left(1-\frac{L}{(q-1)u}\right)^2du=\varepsilon_q.
\tag{9}
\]
Consequently \(h_q/\sqrt{\varepsilon_q}\) is a unit dual certificate with target pairing \(\sqrt{\varepsilon_q}\), proving (2) by Cauchy--Schwarz. Positivity follows from
\(L<2\sinh(L/2)=(q-1)/\sqrt q\) for \(L>0\).

## 3. Exact relaxation and its Mellin meaning

The unitary logarithmic representation is
\(Uf(t)=e^{-t/2}f(e^{-t})\), \(t\ge0\).
For \(0\le t<L\), define the bounded periodization map
\[
Q_qf(t)=\sum_{r\ge0}e^{-(t+rL)/2}Uf(t+rL),\qquad
a(t)=\sum_{r\ge0}e^{-(t+rL)}=\frac{e^{-t}}{1-q^{-1}}.
\tag{10}
\]
Cauchy--Schwarz on each fiber proves convergence almost everywhere and
\(\|Q_qf\|_{L^2(0,L)}^2\le(1-q^{-1})^{-1}\|f\|_2^2\).
The closed relaxation
\[
\mathcal X_q=\{f:Q_qf\text{ is constant a.e.}\}
\]
has an explicitly solved target projection. Since \(Q_qe=a(t)\), for a prescribed constant \(c\) the minimum squared error on each fiber is
\(|a(t)-c|^2/a(t)\). Equality is attained by the fiber vector
\(Uf(t+rL)=c\,e^{-(t+rL)/2}/a(t)\).
Therefore
\[
\operatorname{dist}(e,\mathcal X_q)^2
=\min_{c\in\mathbb C}\left(1-2L\Re c+
\frac{(q-1)^2}{q}|c|^2\right)=\varepsilon_q.
\tag{11}
\]
The optimizer is \(c=qL/(q-1)^2\); its residual is precisely (5).

Let \(\mathcal Mf(s)=\int_0^1f(x)x^{s-1}dx\). The Fourier coefficients of (10) are, up to the factor \(L^{-1}\),
\[
\mathcal Mf(s_\ell),\qquad
s_\ell=1+\frac{2\pi i\ell}{L},\quad \ell\in\mathbb Z.
\]
This interchange is legitimate because
\(\int_0^\infty e^{-t/2}|Uf(t)|dt<\infty\).
Hence \(\mathcal X_q\) is exactly the joint kernel of the bounded Mellin evaluations at \(s_\ell\), \(\ell\ne0\).
The classical identity
\[
\mathcal Mg_j(s)=\frac{\zeta(s)}s(j^{-1}-j^{-s})
\tag{12}
\]
shows that every geometric seed has these zeros. Multiplication by
\(a^{1/2-s}\) preserves them, proving
\(\mathcal C_q^{\mathrm{real}}\subseteq\mathcal X_q\).
At \(s=1\), the zero in the elementary factor is canceled by the zeta pole:
\(\mathcal Mg_j(1)=\log j/j\ne0\). Including \(s=1\) among the constraints would give an incorrect target floor.

Thus the obstruction is classical common-zero geometry with an explicit physical dual and exact relaxation cost. The points \(s_\ell\) are zeros of the selected generators, not zeros of zeta.

## 4. Infinitely many independent restrictions on the arithmetic closure

Choose a prime \(p\nmid q\), so \(\log p/\log q\) is irrational. Fix any \(K\ge1\) and use the evaluations at \(s_1,\ldots,s_K\). Each has norm at most one on \(L^2(0,1)\), since \(\|x^{s_\ell-1}\|_2=1\). The classical zero-free line theorem gives \(\zeta(s_\ell)\ne0\). On the sources \(g_{p^a}\), \(1\le a\le K\), their evaluation matrix is
\[
\frac{\zeta(s_\ell)}{s_\ell}\,p^{-a}(1-z_\ell^a),
\qquad z_\ell=\exp(-2\pi i\ell\log p/\log q).
\tag{13}
\]
The \(z_\ell\) are distinct and none equals one. After removing nonzero row and column factors, invertibility follows from
\[
\frac{1-z^a}{1-z}=1+z+\cdots+z^{a-1}:
\]
these are monic polynomials of successive degrees, whose evaluation matrix is Vandermonde. Thus the \(K\) continuous functionals are independent on \(\mathcal V\), while all annihilate \(\mathcal C_{q,M}\). Since \(K\) is arbitrary, (3) follows. No identification of \(\mathcal V\) with the full harmonic step space is needed.

## Controls, prior art, and consequence

The bound uses the physical \(L^2(dx)\) norm and the actual target. It survives arbitrary numbers of dilations, unbounded coefficients, dependent columns, closure, and real dilation factors. For \(q=2\), the squared floor is \(1-2(\log2)^2\approx0.039094\). The witness itself need not be a harmonic step function to certify distance from a subspace of harmonic step functions.

The claim does not cover a finite seed set containing multiplicatively independent indices such as \(2\) and \(3\). Their elementary nonreal zero lattices have empty intersection, which removes this particular certificate but does not prove density. Nor does the infinite codimension in (3) alone imply that the target stays separated after adjoining an arbitrary finite section. The elementary floor is sharp for \(\mathcal X_q\) only; further arithmetic or zeta-zero constraints can increase the source distance.

The classical inputs were checked against Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146, [Theorem 7 and its proof](https://arxiv.org/pdf/math/0607733), and Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2, especially (2.3) and Lemma 2.4](https://arxiv.org/pdf/math/9910055). Burnol's common-inner-factor and target-projection mechanism is the prior-art boundary; no new general principle is claimed. Nonvanishing on \(\Re s=1\) is the classical Hadamard--de la Vallée Poussin theorem, recorded in [DLMF §25.10(i)](https://dlmf.nist.gov/25.10.i).

The external audit also checked geometric-generator, single-seed dilation, and common-zero formulations. Yang's *A fundamental set in \(L^2(0,1)\)*, Acta Arith. 199 (2021), 269--274, DOI `10.4064/aa200216-31-8`, concerns necessary conditions for generator subfamilies; only its publisher abstract was available in this audit, so no theorem or priority comparison is attributed to it. Absence of a matching formula in the inspected sources is not a novelty claim.

Locally, NB-017 concerns finite multiplication-graph blind modes and NB-084 concerns prediction along a dilation ray. Neither is a replacement for the present target certificate: here the dilation family is unrestricted and the restriction is on source indices. Relative to NB-350, the result rules out a precise proposed source compression and identifies an infinite, norm-continuous obstruction instead of extrapolating finite graph nullity to closure.

As a secondary sanity check, 18 pairs with \(q\in\{2,3,5\}\), \(m\in\{1,2,7\}\), and \(k\in\{1,2\}\) were summed through 30,000 harmonic cells using the exact cell antiderivative of (5). Each truncated pairing lay inside the analytic omitted-tail bound
\(\sqrt m(1-q^{-k})\|h_q\|_\infty/30001\), with maximum ratio below \(0.025\). Floating-point summation was not interval-certified and is only a diagnostic. The evidence for (1)--(3) is the analytic proof above, not the numerical check or a Lean verification. No RH conclusion or approximation rate for the full generator family follows.
