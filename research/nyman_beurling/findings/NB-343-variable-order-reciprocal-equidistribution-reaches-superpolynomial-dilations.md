# NB-343 — Variable-order reciprocal equidistribution reaches superpolynomial dilation windows

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-338, NB-340, NB-341, NB-342
- **Classification:** LITERATURE+DERIVED + SOURCE-SIDE + GROWING-DERIVATIVE-ORDER + SUPERPOLYNOMIAL-DILATION-WINDOW + WEIGHTED-LOGARITHMIC-OBSTRUCTION + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Use the actual Nyman section, compressed integer dilation, and rank-one operator of NB-314:
\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\quad
T_{n,m}=P_{U_n}A_m|_{U_n},\quad E_{n,m}=\sqrt m\,T_{n,m}-R_n.
\]
Let \(\log\) denote the natural logarithm and
\[
L_n=\log_2(\log n)=\frac{\log\log n}{\log 2},\qquad
M_n(\eta)=\left\lfloor n^{(1-\eta)L_n}\right\rfloor,
\quad 0<\eta<1.
\tag{1}
\]

There is an **absolute** constant \(c>0\), independent of \(\eta\), such that for **every fixed** \(0<\eta<1\) and all sufficiently large \(n\) (threshold dependent on \(\eta\)),
\[
\boxed{
\inf_{\substack{m\in\mathbb Z\\n\le m\le M_n(\eta)}}
\left(1+\frac m{n^2}\right)\sqrt{\log n}\,
\|E_{n,m}\|\ge c.
}
\tag{2}
\]
In particular, for \(n^2\ll m\le M_n(\eta)\), this gives
\[
\|E_{n,m}\|\gg \frac{n^2}{m\sqrt{\log n}}
\tag{3}
\]
with an absolute implied constant. The upper cutoff is **superpolynomial**:
\[
M_n(\eta)=
\exp\!\left(\frac{1-\eta}{\log2}
              (\log n)(\log\log n)+O(1)\right)
\]
(where the \(O(1)\) in the logarithm is only from integer rounding). Thus (2) is not a substitution of a growing exponent into the fixed-exponent quantifiers of NB-342; it requires a uniform derivative-order audit.

More precisely, let
\[
\mathfrak D(x)=\sum_{j\ge1}\frac{\|jx\|_{\mathbb Z}^{\,2}}{j^2},
\quad I_n=\{q\in\mathbb Z:\lceil n/2\rceil\le q\le\lfloor 3n/4\rfloor\},
\quad V=\int_{[0,1]^2}[\mathfrak D(x)-\mathfrak D(y)]^2\,dx\,dy>0.
\tag{4}
\]
For every fixed \(\epsilon>0\) and \(0<\eta<1\),
\[
\boxed{
\sup_{\substack{m\in\mathbb Z\\\epsilon n^3\le m\le M_n(\eta)}}
\left|
\frac1{|I_n|}\sum_{q\in I_n}
\left[\mathfrak D\!\left(\frac mq\right)-
      \mathfrak D\!\left(\frac m{q-1}\right)\right]^2-V
\right|\longrightarrow0.
}
\tag{5}
\]
The assertion is vacuous when the integer interval is empty.

## 1. Uniform Weyl sums with a derivative order growing with \(n\)

Fix \(\eta,\epsilon\) and a nonzero fixed integer pair \((h,k)\). Set
\[
p_n=(1-\eta)L_n,\qquad
\ell_n=\left\lfloor(1-\eta/2)L_n\right\rfloor,\qquad
D_n=2^{\ell_n}\le(\log n)^{1-\eta/2}.
\tag{6}
\]
For large \(n\), \(\ell_n\ge3\), \(\ell_n-p_n\to\infty\),
\(\ell_n=O(\log\log n)\), and \(\ell_n\log(\ell_n+2)=o(\log n)\).
We prove the uniform two-dimensional Weyl condition
\[
\sup_{\epsilon n^3\le m\le M_n(\eta)}
\left|\frac1{|I_n|}\sum_{q\in I_n}
e\!\left(m\left(\frac hq+\frac k{q-1}\right)\right)\right|
\longrightarrow0,\qquad e(z)=e^{2\pi iz}.
\tag{7}
\]
Here and below the supremum is over integers \(m\).

Write \(f(x)=m(h/x+k/(x-1))\) and \(\ell=\ell_n\). Exactly,
\[
f^{(\ell)}(x)=(-1)^\ell\ell!m
\left(\frac h{x^{\ell+1}}+\frac k{(x-1)^{\ell+1}}\right).
\tag{8}
\]
Introduce \(s=0\) if \(h+k\ne0\), and \(s=1\) if \(h+k=0\).
In the first case, uniformly on \(n/2\le x\le3n/4\),
\[
\frac h{x^{\ell+1}}+\frac k{(x-1)^{\ell+1}}
=(h+k)x^{-\ell-1}(1+O_{h,k}(\ell/n)).
\tag{9}
\]
In the second case \(k=-h\ne0\). The mean-value theorem applied to
\(x\mapsto x^{-\ell-1}\) gives a fixed sign and magnitude
\[
\left|\frac h{x^{\ell+1}}+\frac k{(x-1)^{\ell+1}}\right|
=|h|(\ell+1)x^{-\ell-2}(1+O(\ell/n)).
\tag{10}
\]
Both errors are uniform because \(\ell=o(n)\). Thus \(f^{(\ell)}\) has a fixed nonzero sign for all large \(n\), and there are positive \(\lambda\le\Lambda\), uniform across the complete admitted \(m\)-range, with
\[
\lambda\le |f^{(\ell)}(x)|\le\Lambda,\qquad
\frac{\Lambda}{\lambda}\le\exp(O_{h,k}(\ell)).
\tag{11}
\]
The interval length \(Y\asymp n\) and the endpoint ratios give the quantitative bounds
\[
\Lambda\le \exp(O_{h,k}(\ell\log(\ell+2)))\,
             m\,n^{-\ell-1-s},
\quad
\lambda Y^\ell\ge
\epsilon n^{\,2-s}\exp(-O_{h,k}(\ell)),
\quad
\frac{\Lambda}{\lambda Y}\le\frac{\exp(O_{h,k}(\ell))}{n}.
\tag{12}
\]
The middle inequality follows by retaining the factor \(\ell!\ell^s\) in the lower derivative estimate; a crude factor \(3^{-\ell}\) from the real interval suffices. In particular, the case \(s=1\), arising from \(h+k=0\), still has \(\lambda Y^\ell\gg\epsilon n\exp(-O(\ell))\). **This cancellation case is the scale-determining one.**

Since \(m\le n^{p_n}\), equations (11)--(12) also give
\[
\frac{\Lambda^2}{\lambda}
\le\exp(O_{h,k}(\ell\log(\ell+2)))\,
n^{p_n-\ell-1-s}.
\tag{13}
\]
The exponent \(p_n-\ell-1-s\) is eventually strictly less than \(-1\); the exponential prefactor is \(n^{o(1)}\).

Apply the theorem of Juan Arias de Reyna, *Explicit van der Corput's d-th derivative estimate* (2024, arXiv:2407.02094), to \(f\) or \(-f\) according to the derivative sign. For \(D=2^\ell\), it gives
\[
\frac1Y\left|\sum e(f(q))\right|
\le\max\left\{
A_\ell\left(\frac{\Lambda}{\lambda Y}\right)^{2/D},
B_\ell\left(\frac{\Lambda^2}{\lambda}\right)^{1/(D-2)},
C_\ell(\lambda Y^\ell)^{-2/D}
\right\},
\tag{14}
\]
provided \(\lfloor Y\rfloor>\ell\), which holds eventually. **Crucially the cited theorem supplies \(A_\ell<7.5\), \(B_\ell<5.8\), \(C_\ell<10.9\) uniformly in the order**; invoking only an unspecified fixed-order derivative test would not justify this step.

Put \(L=\log n\). From (6), \(D\le L^{1-\eta/2}\), and from (12)--(13), the logarithms of all three unpowered bases in (14) are at most
\[
-L+o(L),\quad -L+o(L),\quad -L+o(L)
\]
respectively (the third after inversion). Consequently each term in (14) tends to zero, in fact at most
\(\exp(-c_\eta L^{\eta/2})\) for some \(c_\eta>0\) and sufficiently large \(n\), with constants and thresholds allowed to depend on the fixed Fourier pair and on \(\epsilon,\eta\). The endpoint rounding between the derivative interval and \(I_n\) changes the normalized sum by \(O(1/n)\). This proves (7).

For each fixed trigonometric polynomial on the two-torus, (7) implies uniform convergence of its average over the reciprocal pairs to its Haar integral. Uniform approximation of a **fixed** continuous torus function by such polynomials extends this to every continuous function, including
\(G(x,y)=[\mathfrak D(x)-\mathfrak D(y)]^2\). This proves (5). No uniformity over Fourier orders \(h,k\) growing with \(n\) is claimed or needed.

## 2. Transfer the phase contrast to the physical Nyman section

The uniformly convergent series in (4) makes \(\mathfrak D\) continuous and periodic, with
\(\mathfrak D(0)=0\) and \(\mathfrak D(1/2)=\pi^2/32\).
Thus \(V>0\). Formula (5) implies, uniformly for the high-dilation range and all sufficiently large \(n\), that some \(q\in I_n\) has
\[
\left|\mathfrak D\!\left(\frac mq\right)-
      \mathfrak D\!\left(\frac m{q-1}\right)\right|
\ge\Delta,\qquad\Delta=\sqrt{V/2}>0.
\tag{15}
\]

For the selected \(q\asymp n\), put \(d=\lfloor m/q\rfloor\),
\(r=m-dq\), and \(\delta=d/q\). When \(m\ge\epsilon n^3\), all sufficiently large \(n\) satisfy \(d\ge q\), \(0\le r<q\le d\). Therefore the **unbounded-aspect** Bernoulli/selector identity NB-341(11) applies, without assuming \(\delta\) remains fixed:
\[
q\langle E_{n,m}g_2,\nu_q\rangle
=\frac{\mathfrak D(m/q)-\mathfrak D(m/(q-1))}
{4\delta}+O\!\left(\frac1{q\delta}\right),
\quad
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\tag{16}
\]
All error constants in (16) are absolute. By (15), its leading term dominates that error for large \(n\). As \(\delta\le m/q^2\) and \(q\ge n/2\),
\[
\left|q\langle E_{n,m}g_2,\nu_q\rangle\right|
\ge\frac{\Delta}{8\delta}\ge\frac{\Delta n^2}{32m}.
\tag{17}
\]
The genuine physical norms satisfy
\(\|g_2\|_2=\sqrt{\log2}/2\) and
\(\|\nu_q\|_2\le C\sqrt{\log n}/q\), by NB-304. Cauchy--Schwarz yields
\[
\|E_{n,m}\|\ge c_{\rm high}
\frac{n^2}{m\sqrt{\log n}}
\quad(\epsilon n^3\le m\le M_n(\eta)),
\tag{18}
\]
where \(c_{\rm high}>0\) is **absolute**; only the large-\(n\) threshold depends on \(\epsilon,\eta\). The observer \(q\) is inside the original \(U_n\).

Finally, use NB-341 for moving subcubic sequences. If (2) failed for a fixed \(\eta\) and an absolute \(c<\min(c_{\rm high},c_{\rm low})\), take bad pairs \(n_j\to\infty\), \(m_j\in[n_j,M_{n_j}(\eta)]\). On a subsequence either \(m_j/n_j^3\to0\), when NB-341 (taking \(H_{n_j}=\max(1,m_j/n_j^2)\), \(H_n=1\) elsewhere) rules out the bad weighted value, or \(m_j/n_j^3\ge\epsilon>0\), when (18) rules it out. Here \(c_{\rm low}>0\) is the absolute constant in NB-341, and \(c_{\rm high}>0\) comes from \(\Delta\) and fixed Hilbert constants, so the same \(c\) works for every fixed \(\eta\). This proves (2).

## 3. Stress tests, prior art, and boundary

**Growing-order audit.** The proof explicitly retains the \(\ell\)-dependence of the derivative ratio, the factorial, and the lost derivative power when \(h+k=0\). The uniform bound on \(A_\ell,B_\ell,C_\ell\) in the **actual cited theorem** is load-bearing. Merely asserting NB-342's fixed-\(p\) result for \(p=p_n\to\infty\) would be an invalid interchange of quantifiers. The condition \(D_n=2^{\ell_n}=o(\log n)\) is what makes the derivative estimates decay even as the order grows.

**Arithmetic endpoint.** This is a uniform statement over every integer dilation up to one specified superpolynomial function \(M_n(\eta)\), not an all-\(m\) theorem. The exact common-divisibility obstruction \(m=n!\) from NB-342 makes both reciprocal phases integral for every \(q\in I_n\), so the positive-contrast lemma itself fails at that much larger scale. It does not establish a vanishing Nyman operator error.

**Numerical scope.** The logarithmically growing derivative order only becomes numerically substantial at very large \(n\). The theorem is derived analytically from uniform constants in the cited exponential-sum bound, not from extrapolating computations at accessible sample sizes.

**Prior-art boundary.** The all-orders estimate of Arias de Reyna (2024, arXiv:2407.02094) and the Weyl criterion are established external inputs, already anchored in this line's SOURCES.md. NB-342 previously specialized a *fixed* derivative order to each fixed polynomial exponent. The additional line-local derivation is the **explicit variable-order parameter budget** (6), (11)--(14), and its transfer through NB-341 into (2). Structural searches of variable-order van der Corput applications and reciprocal fractional-part exponential sums did not identify this exact Nyman source-operator formulation; no claim of independent bibliographic novelty is made. SOURCES.md needs no new citation.

**Target/RH boundary.** The result lower-bounds a centered compressed-dilation **source operator**, witnessed by \(g_2\) and an adaptively selected adjacent direction. It does not prove that the actual moving first-free datum occupies this sector, does not control the best Nyman approximation distance \(d_n\), and gives neither RH nor its negation. In the high window the lower bound still tends to zero. Physical target-occupation, inverse-section conditioning and off-critical sample contraction remain missing.

## Research consequence

The fixed-polynomial restriction in NB-342 is not the arithmetic transition: the same reciprocal-pair mechanism survives into the explicitly superpolynomial window
\(\log m\le(1-\eta)(\log n)(\log\log n)/\log2\).
The real limitation of this proof is the derivative-test order budget \(2^\ell\ll\log n\), not a newly discovered source mixing threshold. At scales with exceptional common divisibility the phase-contrast observer can fail; any further growth or RH-facing application requires additional structure rather than another fixed-exponent substitution.
