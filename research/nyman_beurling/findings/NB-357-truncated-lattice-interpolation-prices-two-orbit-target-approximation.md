# NB-357 — Truncated lattice interpolation prices two-orbit target approximation

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the orbit factors and target projection; NB-355 for the necessary component cost; NB-356 for the bounded lattice lift
- **Classification:** LITERATURE+DERIVED + CONSTRUCTIVE-UPPER-BOUND + CONDITIONAL-SHARP-RATE

## Claim and scope

The two-orbit physical-norm obstruction has a constructive converse controlled by a truncated reciprocal-phase sum. It yields a matching logarithmic energy law for badly approximable log ratios and a weaker, unconditional polynomial energy upper bound for every fixed multiplicatively independent integer seed pair. The construction approximates the **projected** Nyman target using vectors in two complete real-dilation orbit spaces; it does not price finite generator count, dilation range, or absolute coefficients.

In \(H=L^2(0,1;dx)\), put
\[
e=1,\quad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\quad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_j=\overline{\operatorname{span}}\{A_ag_j:a\ge1\text{ real}\}.
\]
Fix real \(p,q>1\) with irrational \(\alpha=\log p/\log q\). Let \(\mathcal N\) be the full continuous Nyman space, \(t=P_{\mathcal N}e\), and \(b=B(1)>0\) its Burnol factor. Define
\[
\mathcal E_{p,q}(\varepsilon)=\inf\{\|u\|^2+\|v\|^2:
 u\in\mathcal C_q,\ v\in\mathcal C_p,\ \|t-u-v\|\le\varepsilon\},
\qquad
W_\alpha(X)=\sum_{1\le n\le X}\frac1{n^2\|n\alpha\|_{\mathbb R/\mathbb Z}^2}.
\tag{1}
\]
For sufficiently small \(\varepsilon>0\), there are positive constants depending only on \(p,q,b\) such that
\[
\boxed{c_1 W_\alpha(c_2/\varepsilon)
\ \le\ \mathcal E_{p,q}(\varepsilon)
\ \le\ C_1\bigl(1+W_\alpha(\lceil C_2/\varepsilon^2\rceil)\bigr).}
\tag{2}
\]
The different cutoff scales in (2) are intentional; this is not a two-sided equivalence with one common truncated sum.

Consequently:

1. If \(\|n\alpha\|\ge\gamma/n\) for every \(n\ge1\), with \(\gamma>0\), then
   \[
   \boxed{\mathcal E_{p,q}(\varepsilon)\asymp_{p,q,b,\gamma}\log(1/\varepsilon).}
   \tag{3}
   \]
   This proves the sharp order of squared physical component cost for this real-seed class. For example, \(q>1, p=q^{\sqrt2}\) belongs to it.
2. More generally, if \(\|n\alpha\|\ge\gamma n^{-\nu}\) for every \(n\ge1\), with \(\nu>1\), then
   \[
   \boxed{\mathcal E_{p,q}(\varepsilon)
   \ll_{p,q,b,\gamma,\nu}\varepsilon^{-4(\nu-1)}.}
   \tag{4}
   \]
   Every multiplicatively independent integer pair \(p,q\ge2\) satisfies such a bound for some effective finite \(\nu>1,\gamma>0\), by linear forms in logarithms. No claim of sharpness is made for (4), and no bounded-type assertion is made for any specified integer log ratio.

For all the vectors here,
\[
\|e-u-v\|^2=1-b^2+\|t-u-v\|^2.
\tag{5}
\]
Thus these are rates toward the existing Burnol floor, unconditionally. They do not make that floor vanish.

## 1. The physical interpolation construction

Use the unitary Mellin map to \(H^2(\Re s>1/2)\), with boundary squared norm \(\frac1{2\pi}\int|F(1/2+iy)|^2dy\). NB-354 and NB-356 give
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}},\qquad
\mathcal Mt=Bf,\quad f(s)=b/s.
\tag{6}
\]
These identities also hold for real \(j>1\). Each \(\Theta_j\) is precisely the simple-zero Blaschke product at \(1+2\pi i\ell/\log j\), \(\ell\ne0\); \(s=1\) is not a zero. Multiplication by \(B\) or \(\Theta_j\) is isometric on \(H^2\).

Set \(L=\log q, \tau=2\pi/L, s_\ell=1+i\tau\ell\). For \(d\in\ell^2(\mathbb Z)\), the explicit right inverse from NB-356 is
\[
P_d(x)=\frac1L\sum_{\ell\in\mathbb Z}d_\ell e^{i\tau\ell x},\qquad
(R_qd)(s)=\int_0^L P_d(x)e^{-(s-1)x}\,dx.
\tag{7}
\]
The Fourier series is interpreted in \(L^2(0,L)\). Taking the Laplace density \(e^{x/2}P_d(x)\mathbf1_{[0,L)}\) proves
\[
(R_qd)(s_\ell)=d_\ell,\qquad
\|R_qd\|^2=\int_0^L e^x|P_d(x)|^2dx
\le\frac qL\sum_\ell|d_\ell|^2.
\tag{8}
\]
In particular, (8) controls the full boundary norm, not merely the samples.

For an integer \(K\ge1\), choose two data sequences, both zero at index \(0\):
\[
d^{(K)}_\ell=
\begin{cases}f(s_\ell)/\Theta_p(s_\ell),&0<|\ell|\le K,\\0,&\text{otherwise},\end{cases}
\qquad
a^{(K)}_\ell=
\begin{cases}f(s_\ell),&|\ell|>K,\\0,&\text{otherwise}.\end{cases}
\tag{9}
\]
Irrationality of \(\alpha\) ensures the denominators in (9) are nonzero. The first sequence has finite support; the second is square summable. Define
\[
V_K=R_qd^{(K)},\quad r_K=R_qa^{(K)},\quad
U_K=\frac{f-r_K-\Theta_pV_K}{\Theta_q}.
\tag{10}
\]
At every zero \(s_\ell\), \(\ell\ne0\), of \(\Theta_q\), the numerator in (10) vanishes: the low indices are matched by \(V_K\), the high indices by \(r_K\). Hardy factorization therefore gives \(U_K\in H^2\) and
\[
f=\Theta_q U_K+\Theta_p V_K+r_K.
\tag{11}
\]
This uses division by an actual inner divisor, not a bounded pointwise reciprocal. No condition at \(s_0=1\) is needed.

Let \(u_K=\mathcal M^{-1}(B\Theta_qU_K)\), \(v_K=\mathcal M^{-1}(B\Theta_pV_K)\). Put
\[
T_K=\sum_{0<|\ell|\le K}\frac{|f(s_\ell)|^2}{|\Theta_p(s_\ell)|^2},\qquad
A_q=\frac{2qb^2}{L\tau^2}.
\]
Then (8)--(11) give the explicit bounds
\[
\boxed{\|t-u_K-v_K\|^2=\|r_K\|^2\le\frac{A_q}{K},\qquad
\|v_K\|^2\le\frac qL T_K,}
\tag{12}
\]
because \(\sum_{|\ell|>K}|f(s_\ell)|^2\le2b^2/(\tau^2K)\). Also
\[
\|u_K\|\le b+\|r_K\|+\|v_K\|,\qquad
\|u_K\|^2+\|v_K\|^2
\le2(b+\sqrt{A_q/K})^2+3(q/L)T_K.
\tag{13}
\]
Thus both physical components are controlled. A small interpolation residual has not been purchased with an unpriced first component.

From (6), with \(\delta_\ell=\|\ell\alpha\|\),
\[
|\Theta_p(s_\ell)|=
\frac{|s_\ell|}{\tau|\ell|\sqrt p}
\frac{|1-e^{-2\pi i\ell\alpha}|}{|1-p^{-1}e^{-2\pi i\ell\alpha}|}
\asymp_{p,q}\delta_\ell,\qquad
|f(s_\ell)|\asymp_{q,b}|\ell|^{-1}.
\tag{14}
\]
The numerator lies between \(4\delta_\ell\) and \(2\pi\delta_\ell\), and the denominator between \(1-p^{-1}\) and \(1+p^{-1}\). Hence \(T_K\asymp_{p,q,b}W_\alpha(K)\). Choosing \(K=\lceil A_q/\varepsilon^2\rceil\) for small \(\varepsilon\) proves the upper bound in (2).

For the lower bound, the lattice sampler satisfies
\[
\sum_\ell|F(s_\ell)|^2\le\frac L{1-q^{-1}}\|F\|^2,
\qquad |F(s_\ell)|\le\|F\|.
\tag{15}
\]
For any admissible pair with residual norm at most \(\varepsilon\), at positive indices \(\ell\le c_2/\varepsilon\), choosing \(c_2=b/(2\sqrt{1+\tau^2})\) leaves at least half the sample \(b/|s_\ell|\) to be supplied by \(\Theta_p V\). Equations (14)--(15) imply \(\|v\|^2\ge c_1W_\alpha(c_2/\varepsilon)\), exactly the NB-355 certificate. Taking the infimum proves (2). This derivation is unchanged for real seeds.

## 2. Diophantine separation prices the reciprocal sum

Assume \(\|n\alpha\|\ge\gamma n^{-\nu}\), \(n\ge1\), with \(\nu\ge1\). Decrease \(\gamma\), if necessary, to at most \(1/2\). In a dyadic block \(M\le n<2M\), the phases \(n\alpha\pmod1\), together with zero, are mutually separated by at least
\[
\Delta_M=\gamma(2M)^{-\nu}.
\tag{16}
\]
For two phases this follows by applying the hypothesis to their nonzero index difference; distance from zero uses \(n<2M\). On either side of zero the ordered distances are at least \(\Delta_M,2\Delta_M,\ldots\). Consequently
\[
\sum_{M\le n<2M}\frac1{\|n\alpha\|^2}
\le 2\Delta_M^{-2}\sum_{r\ge1}r^{-2},\qquad
\sum_{M\le n<2M}\frac1{n^2\|n\alpha\|^2}
\ll_{\gamma,\nu} M^{2\nu-2}.
\tag{17}
\]
Summing dyadic blocks, including a possibly incomplete final block, proves
\[
W_\alpha(K)\ll_{\gamma,\nu}
\begin{cases}\log(2K),&\nu=1,\\ K^{2\nu-2},&\nu>1.\end{cases}
\tag{18}
\]
The \(\nu>1\) constant is not uniform as \(\nu\downarrow1\). NB-355's weighted Dirichlet argument gives \(W_\alpha(K)\ge1+\lfloor\log_2K\rfloor\) for every irrational \(\alpha\). Combining this with (2) and (18) proves (3)--(4).

The badly approximable example needs no arithmetic assumption about logarithms: for \(\alpha=\sqrt2\), let \(m\) be the nearest integer to \(n\sqrt2\). Then
\[
1\le|2n^2-m^2|=|n\sqrt2-m|(n\sqrt2+m),\qquad
n\sqrt2+m\le(2\sqrt2+1/2)n,
\]
giving the required \(\gamma/n\) bound. This is a continuous-family control with the actual target and physical norm, not a claim about the integer seed pair \(2,3\).

## 3. Integer seeds have a finite polynomial upper bound

For fixed multiplicatively independent integers \(p,q\ge2\), take \(m\) nearest to \(n\alpha\) and put \(\Lambda_n=n\log p-m\log q\). Independence makes \(p^nq^{-m}-1\ne0\). Matveev's theorem gives
\[
|p^nq^{-m}-1|\ge c_{p,q}n^{-\nu}
\tag{19}
\]
for some effective finite \(\nu>1\), since \(\max(n,|m|)\ll_{p,q}n\). The finitely many cases \(m=0\) can be absorbed into the constant. Since
\[
|\Lambda_n|=(\log q)\|n\alpha\|\le\tfrac12\log q,
\qquad |e^{\Lambda_n}-1|\le\sqrt q\,|\Lambda_n|,
\]
(19) implies \(\|n\alpha\|\ge\gamma_{p,q}n^{-\nu}\). This supplies (4) for every such integer pair, without RH or an assumption of bounded partial quotients. The exponent is only a coarse finite bound; no optimal irrationality measure is needed or claimed.

Equivalently, if the total squared component budget is at most \(R^2\), (4) constructs projection errors at most \(C R^{-1/(2(\nu-1))}\) for sufficiently large \(R\). Under the stronger badly approximable hypothesis, (3) gives upper and lower exponential-in-\(R^2\) bounds, with potentially different constants in the exponents. It does not give an exact asymptotic constant.

## Prior art and mathematical delta

Burnol's [projection theorem, Section 2, Lemma 2.4](https://arxiv.org/pdf/math/9910055) supplies the common inner factor and the transported target. The classical Hardy interpolation boundary is Shapiro--Shields, as reviewed by Arcozzi, Rochberg and Sawyer in their [author manuscript, Introduction pp. 3--4](https://math.mcmaster.ca/~sawyer/Publications/arsball17.pdf). The particular lift (7)--(8) is proved explicitly, rather than relying on a qualitative interpolation assertion.

Borda, *On the theorem of Davenport and generalized Dedekind sums*, J. Number Theory 172 (2017), 1--20, [Section 4, Theorem 3 and equation (9)](https://arxiv.org/pdf/1606.07946), places the squared reciprocal sum in established Diophantine literature and records stronger quadratic-irrational asymptotics. The coarse separation proof (16)--(18) is classical in mechanism; no new reciprocal-sum result is claimed.

The load-bearing finite-type input is Matveev's linear-forms theorem. The exact positive-rational version used in (19) is stated as Theorem 2.1 in Languasco, Luca, Moree and Togbé, *Sequences of integers generated by two fixed primes*, Abh. Math. Semin. Univ. Hambg. 95 (2025), 123--148, [DOI 10.1007/s12188-025-00293-9](https://link.springer.com/article/10.1007/s12188-025-00293-9). That theorem allows positive rational inputs, so its use here does not require \(p,q\) to be prime. The original Matveev paper was identified bibliographically; its full text was not accessible in this audit. No claim depends on an uninspected sharper version.

The local delta beyond NB-355--NB-356 is the norm-controlled **approximate** decomposition (9)--(13), the resulting two-cutoff bracket (2), and the sharp logarithmic cost regime (3). NB-355 gave necessary costs; NB-356's sufficient construction applied to a convergent full series, which always fails for two independent seeds. Truncation plus an independently lifted residual supplies the missing quantitative upper construction even in that divergent regime. These are specializations of classical tools, not a claim of a new Hardy theorem, new number-theoretic bound, or new RH criterion.

## Boundaries and falsification controls

- The residual is controlled in the full physical norm by (8). Matching finitely many samples without lifting the omitted tail would not justify (12).
- Both seed components are priced in (13), after all cancellation internal to each closed orbit. Their mutual cancellation is allowed and is necessary as error tends to zero.
- Removing \(B\) is an isometry only on its invariant range. The final vectors include \(B\), and (5) retains the unconditional target floor. Under RH \(t=e\); that additional equality was not used.
- The polynomial upper bound for integer seeds is not a matching rate. General irrational real ratios can have much larger reciprocal sums; irrationality alone supplies no polynomial upper bound through this argument.
- These vectors may require infinitely many real dilations. Density permits finite orbit sums to approximate each fixed pair with arbitrarily small added norm/error, but gives no quantitative generator count, dilation range, or absolute-coefficient budget. There is no rate for the canonical discrete Nyman sections.
- The explicit formula includes the generally unknown \(B\) and \(b\). It is a Hilbert-space existence/construction theorem, not an algorithm for evaluating the target projection without zeta-zero information.

The decisive audit checks are the \(q/L\) lift constant, the \(K^{-1}\) squared-tail bound, cancellation at **every** nonzero lattice index, division by the pure Blaschke factor, the estimate for the first component, and the squared-norm versus norm exponents in (4). Evidence is the analytic derivation and the cited classical theorem. No numerical optimum, Lean verification, independent adversarial approval, finite-section rate, or progress toward proving \(b=1\) is asserted.
