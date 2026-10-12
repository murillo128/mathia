# NB-342 — Reciprocal-pair equidistribution preserves the weighted obstruction through polynomial dilations

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-338, NB-340, NB-341
- **Classification:** LITERATURE+DERIVED + SOURCE-SIDE + JOINT-RECIPROCAL-PHASE-EQUIDISTRIBUTION + POLYNOMIAL-DILATION-WINDOWS + WEIGHTED-LOGARITHMIC-OBSTRUCTION + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Keep the actual Nyman finite section, compressed integer dilation, and rank-one comparison of NB-314:

\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\qquad
T_{n,m}=P_{U_n}A_m|_{U_n},\qquad
E_{n,m}=\sqrt m\,T_{n,m}-R_n.
\]

There exists an **absolute** constant \(c>0\) such that for **every fixed real \(p\ge3\)**, all sufficiently large integers \(n\) (with threshold permitted to depend on \(p\)) satisfy

\[
\boxed{
\inf_{\substack{m\in\mathbb Z\\n\le m\le n^p}}
\left(1+\frac{m}{n^2}\right)\sqrt{\log n}\,
\|E_{n,m}\|\ \ge c.
}
\tag{1}
\]

Thus the NB-341 obstruction, previously uniform only for \(m=o(n^3)\), persists, with the same absolute weight, on **every predeclared polynomial dilation window**. For \(m\gg n^2\), it yields the source/operator lower bound

\[
\|E_{n,m}\|\gg \frac{n^2}{m\sqrt{\log n}},
\tag{2}
\]

where the implied positive constant can be chosen independently of the polynomial exponent, although the large-\(n\) threshold cannot. This is not a nonzero limiting norm gap: the right side of (2) can tend to zero.

The new ingredient is a uniform two-dimensional phase statement. With

\[
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2},
\qquad
I_n=\{q\in\mathbb Z:\lceil n/2\rceil\le q\le\lfloor3n/4\rfloor\},
\tag{3}
\]

define the strictly positive constant

\[
V=\int_0^1\int_0^1
  [\mathfrak D(x)-\mathfrak D(y)]^2\,dx\,dy>0.
\tag{4}
\]

For each fixed \(p\ge3\) and each fixed \(\epsilon>0\), one has

\[
\boxed{
\sup_{\substack{m\in\mathbb Z\\\epsilon n^3\le m\le n^p}}
\left|
\frac1{|I_n|}\sum_{q\in I_n}
\left[\mathfrak D\!\left(\frac mq\right)
-\mathfrak D\!\left(\frac m{q-1}\right)\right]^2
-V\right|\longrightarrow0.
}
\tag{5}
\]

For an empty integer \(m\)-interval, the assertion is vacuous. The squared difference in (5) is **not** presumed independent for neighboring indices: its limiting joint Haar law is derived.

## 1. Uniform equidistribution of adjacent reciprocal phases

The series (3) converges uniformly, so \(\mathfrak D\) is continuous, even and \(1\)-periodic. Also

\[
\mathfrak D(0)=0,\qquad
\mathfrak D(1/2)=\frac{\pi^2}{32}>0,
\tag{6}
\]

which proves \(V>0\) by continuity.

We prove joint equidistribution of

\[
\left(\frac mq\bmod1,\frac m{q-1}\bmod1\right),
\qquad q\in I_n,
\tag{7}
\]

**uniformly** over \(\epsilon n^3\le m\le n^p\). By the two-dimensional Weyl criterion, it suffices to show that for every fixed nonzero integer pair \((h,k)\),

\[
\sup_{\epsilon n^3\le m\le n^p}
\left|\frac1{|I_n|}\sum_{q\in I_n}
 e\!\left(m\left(\frac hq+\frac k{q-1}\right)\right)\right|
\longrightarrow0,\qquad e(t)=e^{2\pi it}.
\tag{8}
\]

Fix an **integer derivative order** \(\ell>\max\{3,p\}\). For

\[
f(x)=m\left(\frac hx+\frac k{x-1}\right)
\]

we have the exact derivative

\[
f^{(\ell)}(x)=(-1)^\ell\ell!m
\left(\frac h{x^{\ell+1}}+\frac k{(x-1)^{\ell+1}}\right).
\tag{9}
\]

On \(n/2\le x\le3n/4\), there are precisely two cases.

If \(h+k\ne0\), the leading term in the parenthesis is
\((h+k)x^{-\ell-1}\); the relative remainder is \(O_{h,k,\ell}(n^{-1})\). Consequently \(f^{(\ell)}\) has a fixed sign for sufficiently large \(n\), with magnitude

\[
|f^{(\ell)}(x)|\asymp_{h,k,\ell}m/n^{\ell+1}.
\tag{10}
\]

If \(h+k=0\), then \(k=-h\ne0\), and the first term cancels. The mean-value theorem (or Taylor expansion at \(1/x=0\)) gives a fixed sign and

\[
|f^{(\ell)}(x)|\asymp_{h,\ell}m/n^{\ell+2}.
\tag{11}
\]

For clarity, the apparent one-power derivative loss in (11) is essential: it is why the **cubic** lower scale is enough for the joint, rather than merely marginal, phase limit.

Apply the all-orders van der Corput derivative estimate of Juan Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*, arXiv:2407.02094 (2024), whose theorem is already listed in this line's SOURCES.md. For an interval of length \(Y\asymp n\) and \(0<\lambda\le (\pm f)^{(\ell)}\le\Lambda\) with \(D_\ell=2^\ell\), it states

\[
\frac1Y\left|\sum e(f(q))\right|
\le
\max\left\{
 A_\ell\left(\frac{\Lambda}{\lambda Y}\right)^{2/D_\ell},
 B_\ell\left(\frac{\Lambda^2}{\lambda}\right)^{1/(D_\ell-2)},
 C_\ell(\lambda Y^\ell)^{-2/D_\ell}
\right\}.
\tag{12}
\]

The sign \(\pm\) is chosen so that the \(\ell\)-th derivative is positive; complex conjugation does not change the absolute value. The constants depend only on the fixed order. The interval \(I_n\) differs from the real interval only by harmless endpoint rounding.

Equations (10)--(11) allow \(\Lambda/\lambda=O_{h,k,\ell}(1)\), uniformly in admissible \(m\). Moreover,

\[
\sup_{\epsilon n^3\le m\le n^p}\Lambda
\ll_{h,k,\ell}n^{p-\ell-1}=o(1)
\quad\text{in case (10),}
\tag{13}
\]

and even one extra factor \(n^{-1}\) in case (11). The other required parameter diverges:

\[
\lambda Y^\ell\gg_{h,k,\ell}
\begin{cases}
m/n\ge\epsilon n^2,&h+k\ne0,\\[2pt]
m/n^2\ge\epsilon n,&h+k=0.
\end{cases}
\tag{14}
\]

Each of the three terms in (12) therefore tends to zero **uniformly in \(m\)**: the first because \(Y\to\infty\), the second because \(\Lambda^2/\lambda=O(\Lambda)\to0\), and the third by (14). This proves (8).

Uniform approximation of a fixed continuous torus function by trigonometric polynomials then upgrades (8) to uniform joint Haar equidistribution. Apply it to the continuous function \((x,y)\mapsto[\mathfrak D(x)-\mathfrak D(y)]^2\) to obtain (5). There is no assumption of random or independent samples.

In particular, for each fixed \(p,\epsilon\), sufficiently large \(n\), and **every** admitted integer \(m\), some \(q=q(n,m)\in I_n\) satisfies

\[
\left|\mathfrak D\!\left(\frac mq\right)
-\mathfrak D\!\left(\frac m{q-1}\right)\right|
\ge \Delta,\qquad
\Delta:=\sqrt{V/2}>0.
\tag{15}
\]

The positive contrast \(\Delta\) is absolute: neither \(p\), \(\epsilon\), \(n\), nor \(m\) enters it.

## 2. Transfer to the actual compressed Nyman dilation

Take a \(q\) supplied by (15). Since \(q\asymp n\) and \(m\ge\epsilon n^3\), put

\[
d=\lfloor m/q\rfloor,\qquad r=m-dq,\qquad
\delta=d/q.
\tag{16}
\]

For large \(n\), \(d\ge q\), \(0\le r<q\le d\), and the **growing-aspect** identity (11) of NB-341 applies with an absolute error constant:

\[
q\left\langle E_{n,m}g_2,\nu_q\right\rangle
=\frac{\mathfrak D(m/q)-\mathfrak D(m/(q-1))}
{4\delta}+O\!\left(\frac1{q\delta}\right),
\quad
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\tag{17}
\]

This identity was derived from NB-338's exact alternating selector blocks, retaining the finite normalization; it did **not** assume that \(\delta\) stays in a compact set. By (15), for sufficiently large \(n\) its error is less than half its main magnitude, uniformly in \(m\), giving

\[
q\left|\langle E_{n,m}g_2,\nu_q\rangle\right|
\ge\frac{\Delta}{8\delta}
\ge\frac{\Delta n^2}{32m},
\tag{18}
\]

where the second inequality uses \(q\ge n/2\) and
\(\delta=d/q\le m/q^2\).

The actual Hilbert-space bounds of NB-304/NB-341 are

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2,\qquad
\|\nu_q\|_2\le C\frac{\sqrt{\log n}}q
\qquad(q\in I_n),
\tag{19}
\]

for an absolute constant \(C\). Cauchy--Schwarz, with the actual full ambient \(U_n\), therefore turns (18) into

\[
\boxed{
\|E_{n,m}\|\ge c_{\rm high}
\frac{n^2}{m\sqrt{\log n}},
\qquad
\epsilon n^3\le m\le n^p,
}
\tag{20}
\]

where \(c_{\rm high}>0\) is absolute; only the large-\(n\) threshold depends on the fixed parameters \(p,\epsilon\). The chosen observer belongs to \(U_n\) and is not a substitute smaller section.

## 3. Joining the subcubic and polynomial windows

NB-341 proves an **absolute** weighted lower constant \(c_{\rm low}>0\) for every moving family

\[
n\le m\le H_n n^2,\qquad H_n\ge1,\quad H_n=o(n).
\tag{21}
\]

The threshold for that result can depend on the rate \(H_n/n\to0\), but \(c_{\rm low}\) is independent of the sequence. It is essential **not** to apply (20) to the unaddressed intermediate regime \(m/n^3\to0\).

We can instead prove (1) by contradiction. Fix \(p\ge3\) and any
\(0<c<\min(c_{\rm low},c_{\rm high})\). If arbitrarily large \(n\) admitted \(m\in[n,n^p]\) with

\[
\left(1+\frac m{n^2}\right)\sqrt{\log n}\,
\|E_{n,m}\|<c,
\tag{22}
\]

choose a sequence \(n_j\to\infty\) and corresponding \(m_j\). Either a subsequence has \(m_j/n_j^3\to0\), or a subsequence satisfies \(m_j/n_j^3\ge\epsilon>0\).

In the first case, define \(H_{n_j}=\max(1,m_j/n_j^2)\) on the selected subsequence and \(H_n=1\) elsewhere. Then \(H_n\ge1\), \(H_n=o(n)\), and \(m_j\le H_{n_j}n_j^2\); (21) contradicts (22), because \(1+m_j/n_j^2\ge1\). In the second case apply (20), which gives

\[
\left(1+\frac{m_j}{n_j^2}\right)
\sqrt{\log n_j}\|E_{n_j,m_j}\|
\ge c_{\rm high}\left(1+\frac{n_j^2}{m_j}\right)
\ge c_{\rm high},
\tag{23}
\]

again contradicting (22). Thus (1) holds. Both lower constants are absolute and independent of \(p\), so a single \(c>0\) works for all fixed exponents, with \(n_0(p)\) allowed to vary.

## 4. Audits, failure controls, and scientific boundary

**Derivative audit.** The cancellation case \(h+k=0\) was kept explicitly. Replacing its true order \(m/n^{\ell+2}\) by the generic order \(m/n^{\ell+1}\) would make the joint-equidistribution argument invalid. The lower cutoff \(\epsilon n^3\) guarantees \(\lambda n^\ell\gg n\) even in this worst case, while choosing \(\ell>p\) ensures the derivative-size term tends to zero at the upper cutoff.

**Finite-section and scale audit.** The interval \(I_n\) stays inside \(U_n\), all \(q\asymp n\), and the NB-341 coefficient identity controls unbounded \(\delta\) without dropping its \(q-1\) phase or its \(O((q\delta)^{-1})\) normalization remainder. The observed lower bound decays in the polynomial superquadratic regime, as required by compatibility with the far-external rank-one limit of NB-315.

**No unrestricted ultra-large-scale claim.** The polynomial upper condition matters to this proof, and phase contrast can actually fail at superpolynomial dilations. For instance, choose the integer \(m=n!\). Every \(q\in I_n\) and \(q-1\) divides \(m\), so both \(\mathfrak D(m/q)\) and \(\mathfrak D(m/(q-1))\) vanish **exactly**. This falsifies any proposed all-\(m\) strengthening of the phase-contrast lemma (15); it does not show \(E_{n,n!}=0\), since the coefficient identity still has a finite-normalization remainder.

**Numerical sanity checks.** Computing (3) with a positive finite cutoff \(K=1500\) gives an absolute tail error at most \(1/(4K)\) in each value. On \(I_n\), the largest adjacent contrasts for \((n,m)=(500,500^3+17),(500,500^4+17),(500,500^6+17)\) were approximately \(0.2767,0.2456,0.2592\); at \(n=1000\) they were approximately \(0.2753,0.2589,0.2795\). These are consistency checks, not evidence for the uniform theorem, which rests on (9)--(14).

**Prior art and novelty.** The quantitative high-derivative exponential-sum theorem is external, classical-method literature, not an invented source result: Juan Arias de Reyna (2024), arXiv:2407.02094, already recorded in this line's SOURCES.md. The conversion into the reciprocal-pair phase contrast and the actual Nyman finite-section coefficient is derived above from NB-341. The original discrete Nyman setting is given by Báez-Duarte and the fractional-part correlation literature already cited by NB-341. A targeted search of equivalent reciprocal exponential-sum and Nyman approximation formulations did not establish an exact earlier occurrence of (1), but **no claim of independent bibliographic novelty is made**. SOURCES.md requires no amendment.

**Target/RH boundary.** Equations (1)--(2) concern the operator/source test \(g_2\) against an **adaptive adjacent witness**. They neither show that the actual moving first-free Ford target occupies this direction nor control the Nyman best-approximation distance \(d_n\). The sampling/null decomposition, small-section conditioning, and off-critical contraction remain separate unresolved bridges. In particular (1) proves neither RH nor its negation.

## Research consequence

The cubic limit of NB-341 is **a limit of its fixed finite rotation-grid proof**, not a demonstrated mixing transition. Arbitrarily rapid (but predeclared polynomial) growth of the dilation still admits a high-derivative reciprocal-pair witness with the same \(n^2/m\) weighted obstruction. Superpolynomial sequences of extreme common divisibility can remove this specific phase contrast, so extending the argument beyond polynomial windows would require genuinely different arithmetic assumptions or observers. The principal RH-facing bottleneck remains target occupation, not the existence of further source-side lower bounds.
