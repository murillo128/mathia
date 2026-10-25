# NB-360 — Almost every real third seed completes any fixed finite-type pair

- **Status:** proved (classical tools plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the real-orbit factors and projected target; NB-356 for the exact phase-series criterion; NB-358 for the return-spacing mechanism
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-MEMBERSHIP + QUANTITATIVE-METRIC-BOUND

## Claim and scope

Fix two real seeds \(p,q>1\), with irrational \(\alpha=\log p/\log q\), and assume a finite Diophantine type:
\[
\delta_n:=\|n\alpha\|_{\mathbb R/\mathbb Z}\ge\gamma n^{-\nu}
\quad(n\ge1),\qquad \gamma>0,\quad 1\le\nu<\infty.
\tag{1}
\]
In \(H=L^2(0,1;dx)\), put
\[
e=1,\quad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_j=\overline{\operatorname{span}}\{A_ag_j:a\ge1\text{ real}\}.
\]
Let \(\mathcal N\) be the full continuous Nyman space and \(t=P_{\mathcal N}e\). Then
\[
\boxed{t\in\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\text{for Lebesgue-almost every }\beta\in(1,2).}
\tag{2}
\]
This is an algebraic sum of three closed orbit spaces: each component has finite physical norm. It is stronger than their closed-span equality, but does not assert a finite sum of actual dilation generators.

The fixed pair can be **any multiplicatively independent integer pair**, by the classical logarithmic-forms estimate below. NB-356's joint almost-everywhere result allowed both ratios to vary; that result alone says nothing about a specified fixed pair. Equation (2) retains the pair before the third seed is chosen.

There is also a quantitative certificate. Define
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}.
\tag{3}
\]
For every exponent satisfying
\[
\frac12<s<1,\qquad 2s(1-1/\nu)<1,
\tag{4}
\]
one has
\[
\boxed{\int_1^2 S_\alpha(\beta)^s\,d\beta<\infty.}
\tag{5}
\]
Such an exponent exists for every finite \(\nu\), for example \(s=1/2+1/(4\nu)\). A measurable physical-energy certificate \(C(1+S_\alpha(\beta))\) therefore exceeds a squared-norm budget \(R\) on a set of measure \(O(R^{-s})\). Constants depend on the fixed pair, \(\gamma,\nu,s\), and the target factor; this is not an optimal tail law.

Despite (2), the minimum total squared component norm tends to infinity as \(\beta\) approaches any rational point of \((1,2)\). Thus no uniform physical budget exists on any nonempty open interval of third-seed parameters, even after ignoring a null set. No conclusion for a specified third integer seed, such as the triple \(2,3,5\), follows.

## 1. A uniform physical-cost comparison

Write \(b=B(1)>0\) for the normalized Burnol factor, and use the unitary Mellin model from NB-354:
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\qquad
\mathcal Mt=Bf,\quad f(s)=b/s,\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}}.
\tag{6}
\]
Here \(H^2=H^2(\Re s>1/2)\), with squared norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). Each \(\Theta_j\) is precisely the simple-zero Blaschke product at \(1+2\pi i\ell/\log j\), \(\ell\ne0\); its value at \(1\) is removable and nonzero. These statements hold for every real \(j>1\).

Set \(L=\log q\), \(\tau=2\pi/L\), \(z_\ell=1+i\tau\ell\), and \(r=q^\beta\). Define
\[
a_\ell=|\Theta_p(z_\ell)|^2+|\Theta_r(z_\ell)|^2,\qquad
T_\beta=\sum_{\ell\ne0}\frac{|f(z_\ell)|^2}{a_\ell}.
\]
The explicit factors give, uniformly for \(\beta\in[1,2]\),
\[
|f(z_\ell)|\asymp |\ell|^{-1},\qquad
a_\ell\asymp \delta_{|\ell|}^2+\||\ell|\beta\|^2,
\qquad T_\beta\asymp S_\alpha(\beta).
\tag{7}
\]
Uniformity uses \(q\le r\le q^2\): the denominators \(|1-r^{-1}e^{-2\pi i\ell\beta}|\) stay between \(1-q^{-1}\) and \(1+q^{-1}\), and \(|1-e^{-2\pi i x}|\asymp\|x\|\). Irrationality of \(\alpha\) ensures \(a_\ell>0\).

For completeness the physical comparison retains all three component norms. The lattice sampling and lifting bounds of NB-356 are
\[
\sum_{\ell\in\mathbb Z}|F(z_\ell)|^2\le C_q\|F\|^2,
\quad C_q=\frac L{1-q^{-1}},\qquad
\|R_qd\|^2\le\frac qL\|d\|_{\ell^2}^2,
\quad (R_qd)(z_\ell)=d_\ell.
\tag{8}
\]
The lift is explicit: if \(P_d(x)=L^{-1}\sum_\ell d_\ell e^{i\tau\ell x}\) in \(L^2(0,L)\), then \((R_qd)(s)=\int_0^L P_d(x)e^{-(s-1)x}dx\). Parseval bounds its norm by integrating \(e^x|P_d(x)|^2\) on \([0,L]\).

Let \(E_3(\beta)\) be the infimum of \(\|u_q\|^2+\|u_p\|^2+\|u_r\|^2\) over exact decompositions of \(t\) in the indicated orbit spaces, with infimum \(+\infty\) when none exists. Sampling an exact decomposition at every nonzero \(z_\ell\) and applying Cauchy--Schwarz gives
\[
T_\beta\le C_q(\|u_p\|^2+\|u_r\|^2).
\tag{9}
\]
If \(T_\beta<\infty\), take, for \(j=p,r\),
\[
d_{j,\ell}=\frac{f(z_\ell)\overline{\Theta_j(z_\ell)}}{a_\ell}
\quad(\ell\ne0),\qquad d_{j,0}=0,\qquad U_j=R_qd_j.
\]
Then \(H_\beta:=\|U_p\|^2+\|U_r\|^2\le(q/L)T_\beta\). The function
\[
U_q=\frac{f-\Theta_pU_p-\Theta_rU_r}{\Theta_q}
\]
belongs to \(H^2\): the numerator vanishes at every zero of the pure Blaschke factor \(\Theta_q\). Division is isometric on that range, and
\[
\|U_q\|\le b+\sqrt{2H_\beta},\qquad
\|U_q\|^2+H_\beta\le2b^2+5H_\beta.
\]
Multiplication by \(B\Theta_j\) preserves norms. Thus constants independent of \(\beta\in[1,2]\) give
\[
\boxed{cS_\alpha(\beta)\le E_3(\beta)
\le C(1+S_\alpha(\beta)).}
\tag{10}
\]
The upper statement is an explicit construction when the series is finite; the lower statement excludes finite-energy decomposition when it diverges. Repeated seed spaces at isolated parameter values do not invalidate the sampling argument.

## 2. Weighted return spacing for the fixed pair

For \(s>1/2\) and \(0<x\le1/2\), put
\[
F_s(x)=\sum_{\delta_n\le x}n^{-2s}.
\]
If \(n_1<n_2<\cdots\) are return indices, (1) gives
\[
n_1\ge(\gamma/x)^{1/\nu},\qquad
|n_j-n_i|\ge(\gamma/(2x))^{1/\nu}\quad(i\ne j).
\]
The second bound follows from \(\|(n_j-n_i)\alpha\|\le2x\); (1) must be applied to differences as well as to the first index. Therefore \(n_j\ge j(\gamma/(2x))^{1/\nu}\), and
\[
F_s(x)\le\zeta(2s)(2x/\gamma)^{2s/\nu}.
\tag{11}
\]
For \(t_0>0\), Tonelli and the elementary layer integral imply
\[
\sum_{n\ge1}n^{-2s}\delta_n^{-t_0}
=2^{t_0}\zeta(2s)+t_0\int_0^{1/2}F_s(x)x^{-t_0-1}dx<\infty
\quad\text{if }t_0<2s/\nu.
\tag{12}
\]
There is no equidistribution estimate or independence hypothesis in this step.

## 3. Integrate only the added seed

For every fixed positive integer \(n\), multiplication by \(n\) preserves Haar measure modulo one. Consequently, for \(a>0\) and \(s>1/2\),
\[
\int_1^2(a^2+\|n\beta\|^2)^{-s}d\beta
=2\int_0^{1/2}(a^2+y^2)^{-s}dy
\le D_s a^{1-2s},
\quad D_s=2\int_0^\infty(1+y^2)^{-s}dy<\infty.
\tag{13}
\]
For a finite partial sum of (3), use \((\sum x_n)^s\le\sum x_n^s\), valid for nonnegative terms and \(0<s<1\). Equations (12)--(13), with \(t_0=2s-1\), give
\[
\int_1^2\left(\sum_{n=1}^N
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}\right)^s d\beta
\le D_s\sum_{n\ge1}n^{-2s}\delta_n^{-(2s-1)}<\infty,
\tag{14}
\]
uniformly in \(N\). The required inequality \(2s-1<2s/\nu\) is exactly (4). Monotone convergence proves (5), hence finite series and (2) almost everywhere. Only one-variable integrals are used; the different events in \(\beta\) need not be independent.

The explicit majorant \(K(\beta)=C(1+S_\alpha(\beta))\) from (10) is measurable and has finite \(s\)-moment. Markov's inequality gives
\[
\operatorname{meas}\{\beta\in(1,2):K(\beta)>R\}
\le R^{-s}\int_1^2K(\beta)^s d\beta.
\tag{15}
\]
Outside this measurable exceptional set the constructed exact decomposition has total squared physical norm at most \(R\). This avoids assuming existence or regularity of a varying minimum-norm optimizer.

A direct first-moment estimate is not enough for arbitrary finite type: (12) with \(s=1,t_0=1\) only supplies that estimate when \(\nu<2\). The fractional power in (14) is what permits every finite \(\nu\). No necessity of (1), or optimality of the moment range, is claimed.

## 4. Integer-pair application and dense cost divergence

For fixed multiplicatively independent integers \(p,q\ge2\), let \(m\) be nearest to \(n\alpha\). The positive-rational Matveev bound in Languasco, Luca, Moree and Togbé, [Theorem 2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9), gives
\[
|p^nq^{-m}-1|\ge c n^{-\nu}
\]
for some effective finite exponent and positive constant: \(|m|=O_{p,q}(n)\), and multiplicative independence excludes zero. For large \(n\), both exponents are nonzero. If \(z=n\log p-m\log q\), then \(|z|\le\tfrac12\log q\) and \(|e^z-1|\le e^{|z|}|z|\). This gives (1), after adjusting the constants for finitely many initial indices and enlarging \(\nu\) to at least one. No sharp irrationality exponent is needed. Thus (2) holds with this particular integer pair kept fixed; changing variables \(r=q^\beta\) preserves null sets on \((q,q^2)\).

For the nonuniformity control fix \(\beta_0=a/D\in(1,2)\), with integers \(a,D\) and \(D\ge1\). On the sublattice \(n=Dk\),
\[
S_\alpha(\beta_0)\ge\frac1{D^2}
\sum_{k\ge1}\frac1{k^2\|kD\alpha\|^2}=\infty.
\tag{16}
\]
The last divergence is elementary: the distinct convergent denominators \(Q\) of the irrational \(D\alpha\) satisfy \(\|QD\alpha\|<1/Q\), so infinitely many terms exceed one. Each finite partial sum of (3) is continuous in \(\beta\), since \(\delta_n>0\). For every \(M\), choose a partial sum greater than \(M\) at \(\beta_0\); it remains greater than \(M\) in a neighborhood. Hence
\[
\lim_{\beta\to\beta_0}S_\alpha(\beta)=\infty,
\qquad \lim_{\beta\to\beta_0}E_3(\beta)=\infty
\tag{17}
\]
in the extended-real sense, by (10). Rationals are dense, so every nonempty interval has sets of positive measure requiring arbitrarily large budgets. Almost-everywhere finiteness is fully compatible with this obstruction.

## Prior art, mathematical delta, and boundaries

Burnol, [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the continuous-space factor and target projection in (6). NB-356 already proves the phase-series membership test and its lattice lift; those are reused, not counted as new interpolation results. NB-358 supplies the spacing idea, here applied to the different weight \(n^{-2s}\).

Beresnevich, Haynes and Velani, *Sums of reciprocals of fractional parts and multiplicative Diophantine approximation*, Memoirs Amer. Math. Soc. 263 (2020), no. 1276, [author manuscript, Section 2.2, Theorem 2.2 and Section 9.2](https://arxiv.org/pdf/1511.06862), is the close fixed-coordinate metric prior art. Its fiber convergence theorem concerns multiplicative inequalities under reciprocal-sum bounds on the fixed coordinate. The Euclidean denominator in (3), its fractional-moment estimate (14), and the physical lift (10) are proved here; no assertion about a new general metric theorem, or about unsettled questions discussed in that older manuscript, is made.

The local delta is a fixed-pair completion result, including every specified independent integer pair, with a measurable full-norm budget certificate. NB-356's two-variable almost-everywhere control cannot supply this quantifier order: its exceptional set could contain an entire chosen vertical line. Classical measure and interpolation tools close that gap without asserting any new estimate for a specified pair of simultaneous logarithmic phases.

- Every component belongs to \(\mathcal N\), and
  \(\|e-u_q-u_p-u_r\|^2=1-b^2+\|t-u_q-u_p-u_r\|^2\).
  Equation (2) attains the projected target; the Burnol floor \(1-b^2\) is unchanged. It does not prove RH or compute \(B\) without zero information.
- The added seed is real and varies over an interval. A null set can contain every admissible third integer seed. No convergence of the particular series for \(\{2,3,5\}\) is established.
- Full orbit vectors, with unrestricted real dilations, are used. The result gives no discrete Nyman-section rate, finite generator count, dilation range, or absolute-coefficient bound.
- Finite Diophantine type is a sufficient hypothesis. The proof does not classify Liouville fixed ratios or claim a necessary-and-sufficient fiber criterion.
- The positive moment range and tail estimate are sufficient bounds, not sharp thresholds. Constants are not uniform over the fixed pair or its type parameters, and (17) precludes a uniform bound over the added seed.

Evidence is the analytic derivation and the inspected primary sources. The decisive audit points are use of the fixed-ratio bound on return differences, the convergence inequality in (12), the concave-power direction in (14), uniform seed-factor constants in (7), and pricing the anchor component in (10). No numerical convergence claim, formal verification, independent adversarial approval, or new zero-exclusion consequence is asserted.
