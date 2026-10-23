# MC-521 — Smooth deconvolution removes the endpoint loss from the variance-to-zero-free transfer

**Status:** `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`, `LITERATURE+DERIVED`, `NO-NOVELTY-CLAIM`.

## Claim

Fix \(0<\theta<1\), \(0<\eta\le1\), and put

\[
H=X^\theta,\qquad \alpha=1-\frac{\theta\eta}{2}.
\]

Suppose that for every \(\varepsilon>0\), uniformly for all sufficiently large real \(X\), the **complete, uncentered** Möbius moment satisfies

\[
\int_X^{2X}|M(y+H)-M(y)|^2\,dy
\ll_\varepsilon X^{1+\varepsilon}H^{2-\eta}.
\tag{1}
\]

Then

\[
\boxed{\zeta(s)\ne0\quad\text{for }\Re s>\alpha.}
\tag{2}
\]

The same conclusion follows from the multiplicative-window hypothesis used in [MC-177](MC-177-gallagher-diagonal-energy-direct-mertens-power.md): with \(b=H/X\),

\[
\int_X^{2X}|M(e^b y)-M(y)|^2\frac{dy}{y}
\ll_\varepsilon X^\varepsilon H^{2-\eta}.
\tag{3}
\]

For Möbius, (2) also gives the sharp-cutoff consequence

\[
\boxed{M(x)\ll_\varepsilon x^{\alpha+\varepsilon}
\quad\text{for every }\varepsilon>0.}
\tag{2a}
\]

No RH or zero-free hypothesis is used as an input to either variance implication. Neither (1) nor (3) is established here for Möbius. The passage from the derived (2) to (2a) uses the classical Littlewood–Titchmarsh argument, supplied for a general fixed half-plane in Section 4; it is not an inversion of the smooth weights at a sharp endpoint.

The mathematical delta is the removal of the sharp-endpoint term from the variance consequence. MC-177's direct boundary reconstruction gives the Mertens exponent \(\max(\alpha,\theta)\), and hence only that zero-free boundary. Finite approximate deconvolution on smooth test functions gives (2), including when \(\theta>\alpha\); the classical reciprocal-zeta bridge then gives (2a). For example, diagonal variance at \(\theta=4/5\) forces both nonvanishing to the right of \(3/5\) and \(M(x)\ll_\varepsilon x^{3/5+\varepsilon}\), whereas that direct reconstruction yields only \(4/5\). This preserves MC-177's explicitly method-specific optimum while showing that its endpoint cost is not a limitation of the variance premise for Möbius.

## 1. Recover smooth sums before reconstructing endpoints

The argument first applies to any coefficients \(|a_n|\le1\). Write

\[
S_{X,H}(y)=\sum_{y<n\le y+H}a_n,\qquad
A_w(X)=\sum_{n\ge1}a_n w(n/X),
\]

where \(w\in C_c^\infty((1,2);\mathbb C)\), extended by zero to the real line. Set \(h=H/X\), and define the one-sided box average

\[
(B_hv)(z)=\frac1h\int_0^h v(z-u)\,du.
\]

For any compactly supported smooth \(v\), Fubini gives the exact signed identity

\[
\frac1H\int_{\mathbb R}S_{X,H}(y)v(y/X)\,dy
=\sum_n a_n(B_hv)(n/X).
\tag{4}
\]

Choose a fixed positive integer \(K\), and use the finite van Cittert/Neumann polynomial

\[
v_h=\sum_{j=0}^{K-1}(I-B_h)^jw.
\]

There is no infinite inversion or convergence assumption:

\[
B_hv_h=w-(I-B_h)^Kw.
\tag{5}
\]

Since \(B_h\) commutes with differentiation and
\(\|(I-B_h)f\|_\infty\le h\|f'\|_\infty\), iteration gives

\[
\|(I-B_h)^Kw\|_\infty\le h^K\|w^{(K)}\|_\infty.
\tag{6}
\]

If \(\operatorname{supp}w\subset[a,c]\Subset(1,2)\), then
\(\operatorname{supp}v_h\subset[a,c+(K-1)h]\). Thus \(v_h\) remains supported inside \((1,2)\) for all sufficiently large \(X\). Also
\(\|v_h\|_2\le\sum_{j<K}2^j\|w\|_2\), uniformly in \(h\), because translations and their averages contract the real-line \(L^2\) norm. The remainder in (5) has bounded compact support and therefore meets only \(O_{K,w}(X)\) integers after rescaling.

Consequently (4)–(6) and Cauchy–Schwarz imply the quantitative estimate

\[
\boxed{
|A_w(X)|
\ll_{K,w}
\frac{X^{1/2}}H
\left(\int_X^{2X}|S_{X,H}(y)|^2dy\right)^{1/2}
+X(H/X)^K.
}
\tag{7}
\]

Under (1), with \(a_n=\mu(n)\), the first term is
\(O_{K,w,\varepsilon}(X^{1+\varepsilon/2}H^{-\eta/2})\).
Choose \(K\) once and for all so that

\[
K(1-\theta)>\frac{\theta\eta}{2}.
\tag{8}
\]

Then the remainder is smaller than \(X^\alpha\), and for every fixed smooth \(w\) and every \(\varepsilon>0\),

\[
\boxed{A_w(X)\ll_{w,\theta,\eta,\varepsilon}X^{\alpha+\varepsilon}.}
\tag{9}
\]

Using only \(v_h=w\) would leave an \(O(H)\) error. The finite correction is exactly what removes that loss. It acts on the known test weight, not on the unknown Möbius coefficients, and uses the original unweighted second moment only once.

## 2. The multiplicative version has the same remainder budget

For (3) use the dilation average

\[
(C_bv)(z)=\frac1b\int_0^b v(ze^{-u})\,du,
\qquad D=z\frac{d}{dz}.
\]

The corresponding exact identity is

\[
\frac1b\int_0^\infty
\left(\sum_{y<n\le e^b y}a_n\right)v(y/X)\frac{dy}{y}
=\sum_n a_n(C_bv)(n/X).
\tag{10}
\]

Now \(C_b\) contracts \(L^2(dz/z)\), commutes with \(D\), and
\(\|(I-C_b)f\|_\infty\le b\|Df\|_\infty\).
Take \(v_b=\sum_{j<K}(I-C_b)^jw\). Its support lies in
\([a,ce^{(K-1)b}]\Subset(1,2)\) eventually. Equations (5)–(7) become

\[
|A_w(X)|\ll_{K,w}
\frac1b
\left(\int_X^{2X}\left|\sum_{y<n\le e^b y}a_n\right|^2\frac{dy}{y}\right)^{1/2}
+Xb^K.
\tag{11}
\]

Since \(b=H/X\), (3) and the same fixed choice (8) again imply (9). No additive/multiplicative window-conversion theorem or larger family of window lengths is needed for this implication.

## 3. A family of smooth Mellin tests cannot hide a zero

Return to \(a_n=\mu(n)\). For each fixed \(w\), (9) makes

\[
F_w(s)=\int_0^\infty A_w(X)X^{-s-1}\,dX
\tag{12}
\]

holomorphic on \(\Re s>\alpha\). There is no issue at zero, since \(A_w(X)=0\) for \(X<1/2\). On a compact subset of that half-plane, choose the exponent loss in (9) smaller than its distance to the boundary; this also dominates all logarithmic factors from differentiating (12).

For \(\Re s>1\), absolute convergence and \(u=n/X\) give

\[
F_w(s)=\widehat w(s)\sum_{n\ge1}\frac{\mu(n)}{n^s}
=\frac{\widehat w(s)}{\zeta(s)},\qquad
\widehat w(s)=\int_1^2w(u)u^{s-1}du.
\tag{13}
\]

Both sides of

\[
(s-1)\zeta(s)F_w(s)=(s-1)\widehat w(s)
\tag{14}
\]

are holomorphic on \(\Re s>\alpha\), so the identity theorem extends (14) there. If \(\rho=\beta+i\gamma\) were a zeta zero with \(\beta>\alpha\), choose any nonzero nonnegative \(\psi\in C_c^\infty((1,2))\) and set

\[
w(u)=\psi(u)u^{-i\gamma}.
\]

Then
\(\widehat w(\rho)=\int_1^2\psi(u)u^{\beta-1}du>0\), contradicting (14) at \(\rho\ne1\). This proves (2).

The weight may depend on the one putative zero being excluded. Its derivative constants need not be uniform in \(\gamma\); this test argument alone supplies no reciprocal-zeta bound at growing height. Section 4 obtains that additional bound from the resulting zero-free half-plane and the classical growth properties of zeta. A single preselected weight might have a Mellin zero that masks a zeta zero, which is why (9) is proved for every compact smooth test.

## 4. The Möbius sharp cutoff follows from the derived zero-free half-plane

For any fixed \(1/2\le\beta<1\), the classical bridge is

\[
\zeta(s)\ne0\ (\Re s>\beta)
\quad\Longleftrightarrow\quad
M(x)\ll_\varepsilon x^{\beta+\varepsilon}
\quad(\varepsilon>0).
\tag{15}
\]

Only the forward direction needs additional work here. Its proof uses more than abstract holomorphic continuation of an arbitrary Dirichlet series: it uses polynomial vertical growth of \(\zeta\), a bounded Euler-product logarithm on \(\Re s>1\), and the exact reciprocal whose coefficients are \(\mu\).

Fix
\(\beta<\beta_0<\beta_1<\sigma_0<1\).
For large positive \(t\), the disk centered at \(2+it\) with radius
\(R=2-\beta_0\) contains no zero or pole of \(\zeta\).
Choose the analytic logarithm \(g=\log\zeta\) there by its absolutely convergent value at the center. Polynomial growth of zeta on the fixed strip containing this disk gives
\(\Re g\le C\log t\), while \(g(2+it)=O(1)\).
Borel–Carathéodory therefore gives

\[
\max_{|s-(2+it)|\le r_3}|g(s)|\ll\log t,
\qquad r_3=2-\beta_1<R.
\tag{16}
\]

On the disk of radius \(r_1=1/2\), the Euler-product logarithm is uniformly bounded, since \(\Re s\ge3/2\). Put
\(r_2=2-\sigma_0\); then \(r_1<r_2<r_3\).
Hadamard's three-circles theorem applied to this same logarithm yields

\[
\max_{|s-(2+it)|\le r_2}|g(s)|
\ll(\log t)^q,
\qquad
q=\frac{\log(r_2/r_1)}{\log(r_3/r_1)}<1.
\tag{17}
\]

Consequently, for every fixed \(\nu>0\),

\[
\frac1{\zeta(\sigma+it)}
\ll_{\beta,\sigma_0,\nu}(1+|t|)^\nu
\qquad(\sigma\ge\sigma_0).
\tag{18}
\]

Indeed, the modulus is at most \(\exp(C(\log t)^q)\) on \(\sigma_0\le\sigma\le2\), and this is \(O_\nu(t^\nu)\). Conjugation treats negative heights, the absolutely convergent reciprocal series treats \(\sigma\ge2\), and compactness treats bounded heights. The pole of \(\zeta\) at \(1\) is a removable zero of \(1/\zeta\), not an obstruction. All radii and constants are fixed before \(t\) varies; no uniform boundary limit \(\sigma_0\downarrow\beta\) is taken.

For a half-integer \(x\ge2\), truncated Perron on \(\Re s=2\), with \(T\ge x\), gives

\[
M(x)=\frac1{2\pi i}\int_{2-iT}^{2+iT}
\frac{x^s}{s\zeta(s)}\,ds+O(x^2/T).
\tag{19}
\]

The error follows directly from \(|\mu(n)|\le1\): outside \([x/2,2x]\) the Perron error sum is \(O(x^2/T)\); inside it is \(O(x\log x/T)\), using \(|n-x|\ge1/2\). Shift the finite rectangle to \(\Re s=\sigma_0\). There are no enclosed poles: \(\sigma_0>0\), zeta has no zero there, and its pole at \(1\) gives no residue in the reciprocal. Equation (18) bounds the vertical and horizontal integrals respectively, giving

\[
M(x)\ll_{\sigma_0,\nu}
x^{\sigma_0}T^\nu+x^2T^{\nu-1}+x^2/T.
\tag{20}
\]

Take \(T=x^3\), \(0<\nu<1/3\), and choose \(\sigma_0>\beta\), \(\nu>0\) so that
\(\sigma_0+3\nu<\beta+\varepsilon\).
This proves the forward implication in (15), first at half-integers and then for all real \(x\) because \(M(x)=M(\lfloor x\rfloor+1/2)\). Conversely, the integral
\(s\int_1^\infty M(x)x^{-s-1}dx\)
is holomorphic on \(\Re s>\beta\) under the right side of (15), and equals \(1/\zeta(s)\) initially on \(\Re s>1\). The identity theorem then excludes a zero in \(\Re s>\beta\), as in Section 3.

Apply (15) with \(\beta=\alpha\) **after** deriving (2) from the variance input. This proves (2a) without circularly assuming a reciprocal-zeta bound. The boundary \(\alpha\) is equivalent in these two conclusions; the variance hypothesis is only proved sufficient, not equivalent to either one. In particular, this argument does not infer the original short-window moment back from the Mertens estimate.

## 5. Sharpness of the generic analytic boundary

The exponent \(\alpha\) cannot be improved using only the stated second-moment budget and bounded coefficients. Take

\[
a_n=n^{\alpha-1}.
\]

This is bounded and completely multiplicative. Uniformly for \(X\le y\le2X\), its additive and multiplicative short sums are
\(O(HX^{\alpha-1})\). Hence their moments have respective bounds

\[
O(X^{2\alpha-1}H^2)=O(XH^{2-\eta}),
\qquad
O(X^{2\alpha-2}H^2)=O(H^{2-\eta}).
\]

But its Dirichlet series is \(\zeta(s+1-\alpha)\), with a pole exactly at \(s=\alpha\). The squarefree-supported multiplicative control
\(a_n=\mu(n)^2n^{\alpha-1}\) satisfies the same upper bounds and has series

\[
\frac{\zeta(s+1-\alpha)}{\zeta(2s+2-2\alpha)},
\]

again with a pole at \(\alpha\). These controls certify sharpness for generic bounded-coefficient analytic continuation, including exact squarefree support. They do not match Möbius prime signs and do not prove that the Möbius-specific conclusion is optimal.

## 6. Consequences and evidence boundaries

- The zero-free improvement over MC-177's direct transfer is strict precisely when \(\theta>2/(2+\eta)\). For \(\theta=1/2\), the analytic boundary remains \(1-\eta/4\); this does not give a stronger estimate in the balanced Farey window of MC-520.
- Diagonal variance, \(\eta=1\), at a sequence of fixed exponents \(\theta_j\uparrow1\), with the full quantifiers of (1) for each \(j\), implies RH: every hypothetical zero with real part greater than \(1/2\) is excluded by some \(1-\theta_j/2\). Conversely, [[research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target|MC-520]] proves those moment bounds under RH. Constants may depend on \(j\); no uniform \(\theta\uparrow1\) limit is needed. This is a difficulty calibration, not a new route that proves the variance input.
- The fixed restriction \(\theta<1\) is load-bearing in (8). The correction depth can grow when choosing a different fixed \(\theta\), but it is fixed before \(X\) varies. No assertion is made at \(H=X\) by this deconvolution proof.
- Complete second moments are essential. Almost-all cancellation without paying the exceptional starts, or variance centered by an uncontrolled local mean, does not imply (7)'s input. The all-plus coefficients have moment of order \(XH^2\), not (1) with positive \(\eta\), and are correctly excluded.
- Uniformity over all sufficiently large scales is used to make (12) converge. A source-selected shell or a sparse unquantified subsequence cannot replace it. No extra variance theorem for neighboring lengths is silently assumed.
- The sharp Mertens conclusion uses Section 4's reciprocal-zeta structure; the generic bounded-coefficient part of Sections 1–2 only proves smooth-sum bounds. No unrestricted sharp-cutoff recovery theorem for arbitrary bounded coefficients is asserted. The result does not give an unconditional variance estimate, an endpoint \(O(x^\alpha)\) bound without epsilon, an asymptotic constant, zero simplicity, a bound for \(1/\zeta'(\rho)\), numerical evidence, or formal verification.

## Prior art and novelty assessment

The operator polynomial in (5) is classical [[research/prior_art/incremental/PA-van-cittert-approximate-deconvolution|van Cittert approximate deconvolution]], explicitly described by William Layton, *The Interior Error of Van Cittert Deconvolution of Differential Filters Is Optimal*, Applied Mathematics E-Notes 12 (2012), 88–93; see also the [expanded author manuscript, equation (1.1)](https://www.mathematics.pitt.edu/sites/default/files/research-pdfs/vancitterterrorexpanded.pdf). Its differential-filter estimates are not imported: (6) is the separate elementary box-filter proof needed here.

The Mellin/Dirichlet-series bridge is standard; see Don Zagier, [*The Mellin Transform and Related Analytic Techniques*, Sections 1–2](https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf). The nonmasking test and identity-theorem argument are supplied explicitly rather than presumed from continuation of a single smoothed observable.

The surrounding short-interval/zero-location relationship is classical. [Zaccagnini, Section 3.3](https://arxiv.org/abs/1603.02952), discusses Selberg integrals and quasi-RH for prime counts; that is adjacent context, not a signed Möbius estimate transferred here. [Matomäki–Radziwiłł, Theorem 1](https://doi.org/10.4007/annals.2016.183.3.6), gives an almost-all short/long-average comparison with explicit errors and exceptional starts; it is not the uncentered fixed-power hypothesis (1).

Section 4 is the fixed-half-plane version of Littlewood's classical method: [Titchmarsh, second edition, Sections 14.2 and 14.25(C)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), pp. 336–337 and 370, proves the logarithm/reciprocal bound and Mertens equivalence at the RH boundary; Lemma 3.12 supplies truncated Perron. The fixed-radius proof (16)–(20) records explicitly why the same mechanism works with any \(1/2\le\beta<1\). No novelty is claimed for (15), or for its composition with the zero-free conclusion already proved here.

Targeted checks covered Möbius short-interval moments, variance/zero-free implications, smooth Mellin continuation, finite approximate deconvolution, and the classical zero-free-to-Mertens bridge. No novelty of these tools or of a general variance/RH connection is claimed. The durable local contribution is the explicit composition (7)–(20), with its sharp generic analytic control: **the endpoint exponent in the previous direct reconstruction obstructs neither the stronger zero-free consequence nor its equivalent Möbius sharp-sum consequence from the same multiplicative-window variance premise.** The missing arithmetic input remains the actual uniform fixed-power moment bound.
