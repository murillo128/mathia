# PC-189 — finite polynomial local jets Mellinize to colored Tornheim cone functions

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for fixed finite-degree, shell-independent polynomial interactions of scale-normalized local cyclotomic jets followed by a Mellin scalarization. The result does not say that every colored Mordell--Tornheim function is analytically trivial; it says that this entire local nonlinear escape route produces a classical cyclotomic cone-zeta class rather than a new source-derived Prime-Circle spectral object.

PC-184 showed that every finite radial Euler jet of the cyclotomic log-potential has Mellin fiber rank one, and PC-188 showed that finite angular/radial anchored local derivatives add no second linear carrier because holomorphicity and Cauchy--Riemann reduce them to the same radial jet. Both results deliberately left **nonlinear products of local jets** outside their linear no-go theorems.

The first nonlinear repair can now be classified exactly. Multiplying finitely many local jets does create additive mode coupling, so the answer is not another rank-one statement. But after Mellinization the coupling is always a finite Möbius/divisor combination of root-of-unity-colored Mordell--Tornheim/conical Dirichlet functions. In the potential-only sector this is literally the classical cyclotomic conical-zeta class of Terasoma; at depth two it is the colored Tornheim class treated explicitly by Zhao. Thus finite local polynomial nonlinearity changes the **depth** of the classical cyclotomic period, not the underlying arithmetic source.

## 1. Scale-normalized local jets

For `n>1`, put

\[
F_n(x):=\log\Phi_n(e^{-x}),\qquad x>0.
\]

Cyclotomic Möbius inversion gives

\[
F_n(x)=\sum_{d\mid n}\mu(n/d)V_d(x),
\qquad
V_d(x):=\log(1-e^{-dx}).
\tag{1}
\]

For every integer `j>=0`, the elementary exponential expansion is

\[
\boxed{
V_d^{(j)}(x)
=(-1)^{j+1}d^j
\sum_{k\ge1} k^{j-1}e^{-dkx}.
}
\tag{2}
\]

The formula includes `j=0`, where the right side is `-sum e^{-dkx}/k`.

The natural dimensionless derivative is

\[
J_{n,j}(x):=x^jF_n^{(j)}(x).
\tag{3}
\]

Every finite Euler jet `P(D)F_n`, with `D=x d/dx`, is a fixed linear combination of the `J_{n,j}` because

\[
D^a=\sum_{j=0}^a S(a,j)x^j\frac{d^j}{dx^j},
\tag{4}
\]

where `S(a,j)` are Stirling numbers of the second kind. PC-188 also implies that every scale-normalized finite angular/radial derivative of the analytic field on the anchored ray differs from one of these radial derivatives only by a universal phase and a fixed linear recombination. Therefore a fixed polynomial in finite anchored local two-dimensional jets expands into finitely many products of the form studied below.

## 2. Exact Mellin formula for an arbitrary local monomial

Choose shell labels `n_1,...,n_r>1` and derivative orders `j_1,...,j_r>=0`. Set

\[
J:=j_1+\cdots+j_r
\]

and consider the nonlinear local monomial

\[
M_{\mathbf n,\mathbf j}(x)
:=\prod_{i=1}^r J_{n_i,j_i}(x).
\tag{5}
\]

For `Re(s)>0`, its Mellin transform converges absolutely. Indeed each `x^jV_d^{(j)}` is bounded at `0+` for `j>=1`, while `V_d(x)=O(|\log x|)` for `j=0`; all terms decay exponentially at infinity. Hence the finite divisor expansion and the positive exponential series may be interchanged with the integral term by term.

Substituting (1)--(2) and using

\[
\int_0^\infty x^{s+J-1}e^{-Ax}\,dx
=\Gamma(s+J)A^{-s-J}
\]

gives the exact formula

\[
\begin{aligned}
\mathcal M_{\mathbf n,\mathbf j}(s)
&:=\int_0^\infty M_{\mathbf n,\mathbf j}(x)x^{s-1}\,dx\\
&=(-1)^{J+r}\Gamma(s+J)
\sum_{d_i\mid n_i}
\left(\prod_{i=1}^r\mu(n_i/d_i)\right)
\sum_{k_1,\ldots,k_r\ge1}
\frac{\prod_i d_i^{j_i}k_i^{j_i-1}}
     {(d_1k_1+\cdots+d_rk_r)^{s+J}}.
\end{aligned}
\tag{6}
\]

This already shows the structural boundary: all shell dependence is finite Möbius/divisor data, while the nonlinear mode mixing is a universal additive-cone Dirichlet series.

## 3. Root-of-unity filtering removes the divisor scales

Equation (6) has an even cleaner cyclotomic form. Put `m_i=d_i k_i`. Then

\[
d_i^{j_i}k_i^{j_i-1}=d_i m_i^{j_i-1}.
\]

The divisibility restriction is represented exactly by the root-of-unity filter

\[
\boxed{
d\,\mathbf 1_{d\mid m}=\sum_{\alpha\in\mu_d}\alpha^m.}
\tag{7}
\]

Define the colored Tornheim/cone function

\[
\boxed{
T_{\mathbf j}(\boldsymbol\alpha;w)
:=
\sum_{m_1,\ldots,m_r\ge1}
\frac{\prod_{i=1}^r\alpha_i^{m_i}m_i^{j_i-1}}
     {(m_1+\cdots+m_r)^w}.
}
\tag{8}
\]

In the convergence region relevant here, (6) becomes

\[
\boxed{
\mathcal M_{\mathbf n,\mathbf j}(s)
=(-1)^{J+r}\Gamma(s+J)
\sum_{d_i\mid n_i}
\left(\prod_i\mu(n_i/d_i)\right)
\sum_{\alpha_i\in\mu_{d_i}}
T_{\mathbf j}(\boldsymbol\alpha;s+J).
}
\tag{9}
\]

The important cancellation in (7) is exact: **no new continuous scale depending on the divisors survives**. The divisors only choose finite root-of-unity colors and Möbius signs. If `N=lcm(n_1,...,n_r)`, every color appearing in (9) lies in `mu_N`.

For `j_i=0` for all `i`, (8) is the standard root-of-unity-colored conical/Mordell--Tornheim series with side denominators `m_i` and the additional linear form `m_1+...+m_r`. For general `j_i`, it is the corresponding colored Mordell--Tornheim function with side parameters `1-j_i`; equivalently the numerator powers are obtained by finite logarithmic color derivatives `alpha_i d/d alpha_i` of the same colored generating family. Thus finite differential order changes parameters inside the same classical multi-zeta architecture.

## 4. The first nonlinear case is already colored Tornheim

The simplest genuine nonlinear product is two undifferentiated shell potentials. From (9), for `Re(s)>0`,

\[
\boxed{
\begin{aligned}
\int_0^\infty F_m(x)F_n(x)x^{s-1}\,dx
&=\Gamma(s)
\sum_{d\mid m}\sum_{e\mid n}
\mu(m/d)\mu(n/e)\\
&\quad\times
\sum_{\alpha\in\mu_d}\sum_{\beta\in\mu_e}
\sum_{a,b\ge1}
\frac{\alpha^a\beta^b}{ab(a+b)^s}.
\end{aligned}
}
\tag{10}
\]

So the very first quadratic local nonlinearity that escapes the rank-one *linear* theorem of PC-184 is not an unknown two-carrier object. It is a finite cyclotomic combination of colored double Tornheim functions.

At positive integral Mellin weight, this lies in the classical cyclotomic conical-period setting. The higher-degree potential products similarly give higher-dimensional root-of-unity cone sums. Derivative insertions only shift the Mordell--Tornheim side parameters as in (8)--(9).

## 5. Fixed local polynomials therefore stay in a finite classical cone span

Let `P` be any fixed polynomial, with shell-independent coefficients, in finitely many scale-normalized local jet components of finitely many shells. Expanding `P`, using (4) and PC-188's Cauchy--Riemann reduction, and applying (9) monomial by monomial gives:

\[
\boxed{
\mathcal M[P(\text{finite local cyclotomic jets})](s)
\in
\operatorname{span}_{\mathrm{finite}}
\{\Gamma(s+A)T_{\mathbf j}(\boldsymbol\alpha;s+A)\},
}
\tag{11}
\]

where `A` is a nonnegative integer and every `alpha_i` is a root of unity of order dividing the lcm of the finitely many shell labels used by `P`.

This is the exact boundary left open by PC-184/PC-188. Nonlinearity **does** break Mellin rank one by convolving modes, but for any fixed finite polynomial it can only move from depth one cyclotomic Mellin data to finite-depth colored additive-cone data. There is no second independently supplied geometric field hidden in the local jet: the extra indices come from multiplying copies of the same exponential/cyclotomic source.

A matched composite shell has exactly the same architecture. Primality or prime-power support can only enter through the finite Möbius coefficients and cancellations in (9), not through a new nonlinear period class.

## 6. Positive nonlinear local self-energies still destroy the prime-power selector

The classicalization above allows signed cancellations, so it should not be overread as a theorem that every nonlinear polynomial is prime-blind. But the most natural positive repair fails more strongly.

Let `P` be a nonzero polynomial and `q>=1`. For `sigma>0`, define

\[
E_{n,P,q}(\sigma)
:=\int_0^\infty
|P(D)F_n(x)|^{2q}x^{\sigma-1}\,dx.
\tag{12}
\]

The integral is finite: finite Euler jets are bounded at `0+` and decay exponentially at infinity. It is also strictly positive for **every** `n>1`. If `P(D)F_n` vanished identically, PC-184's Mellin identity would give

\[
P(-s)\mathcal F_n(s)=0
\qquad(\operatorname{Re}s>0),
\]

but `\mathcal F_n(s)` is zero-free there and a nonzero polynomial cannot vanish on an open set. Hence

\[
\boxed{
E_{n,P,q}(\sigma)>0
\qquad
\text{for every }n>1.
}
\tag{13}
\]

Thus taking squares, fourth powers, or any other positive even local polynomial of a nontrivial finite jet cannot retain the exact common-vertex Mangoldt support. In particular it cannot be positive on prime powers while vanishing on matched mixed-prime shells such as `n=6`.

This does not exclude indefinite polynomial combinations engineered to cancel on selected shells; equation (9) says only that any such cancellation occurs inside the classical colored Tornheim/conical family.

## 7. Prior art and novelty audit

The analytic and number-theoretic ingredients are classical, and no historical novelty is claimed for the cone functions themselves.

1. The exponential expansion of `log(1-e^{-dx})`, Möbius inversion of cyclotomic logarithms, Mellin integration of exponentials, and root-of-unity divisibility filter are standard.
2. Tomohide Terasoma, *Rational convex cones and cyclotomic multiple zeta values* (arXiv:math/0410306), already recorded in `SOURCES.md`, defines rational-cone zeta values with finite-order characters and proves that absolutely convergent conical values lie in the cyclotomic multiple-zeta span. The potential-only specialization of (9) is directly in that terrain.
3. Jianqiang Zhao, *A Note on Colored Tornheim's Double Series*, *Integers* 10:6 (2010), 879--882, DOI 10.1515/integ.2010.059, also already recorded in `SOURCES.md`, explicitly reduces colored double Tornheim series to double polylogarithm values at roots of unity. Equation (10) lands exactly on this depth-two boundary.
4. Directed novelty searches also returned the established Mordell--Tornheim literature on functional relations with the Riemann zeta function. Therefore the mere appearance of zeta relations after (9) would not be evidence of a new Prime-Circle/RH bridge.

The durable contribution is the **Prime-Circle reduction theorem** (9)--(11): the finite nonlinear local-jet loophole left by the preceding linear rank-one results has a precise classical target class. The geometric construction does not supply a new independent analytic spectrum at finite polynomial depth.

## 8. What this rules out and what remains open

This finding rules out treating a fixed finite local polynomial of the anchored cyclotomic jet, followed by a Mellin transform, as a new spectral mechanism merely because nonlinear products mix Fourier/Lambert modes. Their exact output is already a finite cyclotomic colored Mordell--Tornheim/cone family. It also rules out positive even-power local jet energies as a way to preserve the exact prime-power selector.

It does **not** classify:

- non-polynomial or infinite-degree nonlinearities whose degree grows with the conductor or refinement depth;
- genuinely nonlocal two-depth or angular/radial kernels before multiplication;
- shell-dependent operators forced by old/new geometry rather than a fixed local polynomial;
- infinite all-shell limits in which the finite Möbius sum itself becomes an operator or renormalized determinant;
- singular boundary/domain data not represented by `sigma>0` Mellin integrals;
- global uniformization, monodromy, Liouville, or Weil--Petersson data.

Those are structurally different ways to escape the theorem. In particular, the accepted signed-radial-flux frontier still requires an additional geometry-forced carrier **before** positive local polynomial scalarization, or a genuinely nonlocal/infinite organization that is not a fixed finite colored cone sum.

## 9. Falsification checks

The exact theorem can be audited without any RH assumption.

- For any chosen `n_i,j_i` and `Re(s)>0`, numerical quadrature of the left side of (6) must agree with the absolutely convergent divisor/exponential series on the right.
- Substituting `m_i=d_i k_i` and using `d 1_{d|m}=sum_{alpha in mu_d} alpha^m` must reproduce (9) exactly; a residual divisor-scale coefficient would falsify the root-of-unity reduction.
- For `r=1`, (9) reduces to the PC-184 formula `mathcal F_n(s)=-Gamma(s)zeta(s+1)n^{-s}prod_{p|n}(1-p^s)`, providing an independent consistency check.
- For `r=2,j_1=j_2=0`, (10) is a direct colored double Tornheim sum, providing the closest literature cross-check.

## Research consequence

PC-188 left finite nonlinear local cross-jet relations as an obvious possible escape from linear Mellin rank one. PC-189 shows exactly what that escape buys: **finite additive depth, not a new arithmetic source**. A fixed-degree local polynomial moves Prime Circle from single cyclotomic Mellin factors into the classical colored Mordell--Tornheim/conical hierarchy, while positive versions lose the prime-power selector altogether.

The surviving local-to-global frontier therefore has to use structure that is not representable by a fixed finite local polynomial followed by one Mellin readout: a source-forced nonlocal kernel, shell-dependent old/new operator, growing/infinite nonlinear depth, or genuinely global geometric data.