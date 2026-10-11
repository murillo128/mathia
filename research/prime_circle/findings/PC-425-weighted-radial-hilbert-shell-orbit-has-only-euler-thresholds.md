# PC-425 — weighted completion of the radial Hilbert shell orbit has only Euler thresholds

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for the standard diagonal weighted-Hilbert completion of the infinite-family loophole explicitly left open in PC-424. For every fixed \(0<\sigma<1\), both its relative translation orbit and its actual primitive-shell Hilbert commutators belong to the weighted coefficient space precisely for \(\alpha>3/2-\sigma\). On this same space, the infinite Möbius change of basis is the Hilbert-space amplification of the operator classified in PC-055, boundedly invertible exactly for \(\alpha>1\). At \(\sigma=1/2\), the orbit exists only in the already-invertible range. The identical threshold holds for PC-424's explicitly zero-free matched seed.

This is **not** an obstruction for arbitrary non-diagonal, source-dependent, or renormalized completions. It closes the particular claim that a *standard diagonal weighted \(\ell^2\) completion* of PC-424's actual operator orbit might create a new critical-line Möbius-basis anomaly.

## 1. Exact operator family and coefficient space

Fix \(0<\sigma<1\) and let \(H\) be the real-line Hilbert transform. PC-424 constructs the nonconstant regularized Bose symbol
\[
b_\sigma(u)=e^{\sigma u}\left(\frac1{e^{e^u}-1}-e^{-u}\right)
\]
and the nonzero Hilbert--Schmidt operator
\[
B_\sigma=[H,M_{b_\sigma}]\in\mathcal S_2(L^2(\mathbb R)).
\]
For the unitary translation \((\tau_a f)(u)=f(u+a)\), put
\[
B_{d,\sigma}=d^{1-\sigma}\tau_{\log d}B_\sigma\tau_{-\log d},
\qquad
E_{d,\sigma}=B_{d,\sigma}-B_{1,\sigma}\quad(d>1).
\]
The genuine primitive-shell operator is, for \(n>1\),
\[
\boxed{C_{n,\sigma}=-\sum_{\substack{d\mid n\\d>1}}\mu(n/d)E_{d,\sigma}.}\tag{1}
\]
In particular, \(C_{p,\sigma}=-E_{p,\sigma}\) for every prime \(p\). The \(n=1\) relative and primitive coordinates are both set to zero, as required by the cancellation \(\sum_{d\mid n}\mu(n/d)=0\).

Let \(\mathcal K=\mathcal S_2(L^2(\mathbb R))\), and for real \(\alpha\) define
\[
\boxed{
\mathscr H_\alpha^0(\mathcal K)
=
\left\{X=(X_n)_{n\ge2}:
\sum_{n\ge2}n^{-2\alpha}\|X_n\|_{\mathcal S_2}^2<\infty
\right\}.}\tag{2}
\]
This is the ordinary diagonal Hardy--Dirichlet coefficient completion, with a Hilbert-valued coefficient instead of a scalar coefficient. No new geometry or off-diagonal norm is inserted.

## 2. Exact membership threshold for the relative orbit

Unitary conjugation gives
\[
\|B_{d,\sigma}\|_{\mathcal S_2}
=d^{1-\sigma}\|B_\sigma\|_{\mathcal S_2}.
\]
The triangle and reverse-triangle inequalities therefore give the exact two-sided estimates
\[
\boxed{
(d^{1-\sigma}-1)\|B_\sigma\|_{\mathcal S_2}
\le\|E_{d,\sigma}\|_{\mathcal S_2}
\le(d^{1-\sigma}+1)\|B_\sigma\|_{\mathcal S_2}.}\tag{3}
\]
The constant \(\|B_\sigma\|_{\mathcal S_2}\) is strictly positive: PC-421's commutator kernel vanishes only for almost-everywhere constant symbols, whereas \(b_\sigma\) is nonconstant and vanishes at both ends of the log-radius line.

Because \(1-\sigma>0\), (3) yields comparison, after discarding finitely many indices, with a plain power series:
\[
\sum_{d\ge2}d^{-2\alpha}\|E_{d,\sigma}\|_{\mathcal S_2}^2
\asymp_\sigma
\sum_{d\ge2}d^{-2(\alpha+\sigma-1)}.
\]
Consequently
\[
\boxed{
(E_{d,\sigma})_{d\ge2}\in\mathscr H_\alpha^0(\mathcal K)
\iff \alpha>\frac32-\sigma.}\tag{4}
\]
The endpoint equality does not converge.

## 3. The actual primitive-shell family has exactly the same threshold

For arbitrary \(n>1\), equation (1) and the unitarily invariant norm give
\[
\begin{aligned}
\|C_{n,\sigma}\|_{\mathcal S_2}
&=\left\|\sum_{d\mid n}\mu(n/d)B_{d,\sigma}\right\|_{\mathcal S_2}\\
&\le\|B_\sigma\|_{\mathcal S_2}\sum_{d\mid n}d^{1-\sigma}\\
&\le\|B_\sigma\|_{\mathcal S_2}\,n^{1-\sigma}\tau(n),
\end{aligned}\tag{5}
\]
where \(\tau(n)\) is the divisor-counting function. Hence
\[
\sum_{n\ge2}n^{-2\alpha}\|C_{n,\sigma}\|_{\mathcal S_2}^2
\le\|B_\sigma\|_{\mathcal S_2}^2
\sum_{n\ge2}\frac{\tau(n)^2}
{n^{2(\alpha+\sigma-1)}}.
\tag{6}
\]
The classical identity
\[
\sum_{n\ge1}\frac{\tau(n)^2}{n^w}
=\frac{\zeta(w)^4}{\zeta(2w)},\qquad \Re w>1,
\tag{7}
\]
proves sufficiency for \(\alpha>3/2-\sigma\).

For necessity, restrict to primes. From (1) and (3),
\[
\sum_{n\ge2}n^{-2\alpha}\|C_{n,\sigma}\|_{\mathcal S_2}^2
\ge\|B_\sigma\|_{\mathcal S_2}^2
\sum_{p}p^{-2\alpha}(p^{1-\sigma}-1)^2.
\tag{8}
\]
For sufficiently large primes the summand is bounded below by a positive multiple of \(p^{-2(\alpha+\sigma-1)}\). The prime sum diverges whenever \(2(\alpha+\sigma-1)\le1\), using the classical divergence of \(\sum_p1/p\), with smaller exponents only larger. Thus
\[
\boxed{
(C_{n,\sigma})_{n\ge2}\in\mathscr H_\alpha^0(\mathcal K)
\iff \alpha>\frac32-\sigma.}\tag{9}
\]
This lower bound concerns the **actual Möbius-combined operators**, not merely their unrecombined translation orbit. No unproved boundedness of Möbius inversion was used to establish (9).

## 4. Vector-valued Möbius inversion: no improved threshold after removing \(n=1\)

On finitely supported \(\mathcal K\)-valued coefficient vectors, define
\[
(T_\mu X)_n=\sum_{d\mid n}\mu(n/d)X_d,
\qquad
(T_1X)_n=\sum_{d\mid n}X_d.
\]
Equation (1) is exactly \(C=-T_\mu E\) on the \(n>1\) invariant subspace. Since the divisor coefficients are scalars and \(\mathcal K\) is a Hilbert space, these operators on \(\mathscr H_\alpha(\mathcal K)\) are the Hilbert-space amplifications
\[
\boxed{T_\mu^{(\mathcal K)}=T_\mu^{(\mathbb C)}\otimes I_{\mathcal K},
\qquad T_1^{(\mathcal K)}=T_1^{(\mathbb C)}\otimes I_{\mathcal K}.}\tag{10}
\]
PC-055, via the Hedenmalm--Lindqvist--Seip multiplier theorem and the Bohr/Euler-product symbols, gives bounded invertibility for **exactly** \(\alpha>1\). The same operator-norm bounds apply after amplification.

Deleting the coordinate \(n=1\) does **not** improve that threshold. For any fixed integer \(q>1\), define the weighted divisor shift
\[
(S_qX)_n=
\begin{cases}
q^\alpha X_{n/q},&q\mid n,\\
0,&q\nmid n.
\end{cases}
\]
It is an isometry of \(\mathscr H_\alpha(\mathcal K)\) into the invariant subspace \(X_1=0\), and Dirichlet-convolution commutativity yields
\[
\boxed{T_\mu S_q=S_qT_\mu,\qquad T_1S_q=S_qT_1.}\tag{11}
\]
If either restricted transform were bounded on \(X_1=0\), (11) and isometry would imply boundedness of the corresponding full transform, contradicting PC-055 when \(\alpha\le1\). When \(\alpha\le1/2\), already the image of a shifted coordinate vector may leave the coefficient Hilbert space; for \(1/2<\alpha\le1\), the transforms are defined on finite sequences but unbounded. Therefore
\[
\boxed{
T_\mu\text{ is boundedly invertible on }\mathscr H_\alpha^0(\mathcal K)
\iff\alpha>1.}\tag{12}
\]
The algebraic inverse remains \(T_1\) on finite vectors; no analytic invertibility at smaller weights is asserted.

## 5. Critical half-density and matched zero-free control

At the natural unweighted radial half-density \(\sigma=1/2\), (4) and (9) reduce to
\[
\boxed{
E^{(1/2)},\,C^{(1/2)}\in\mathscr H_\alpha^0(\mathcal K)
\iff\alpha>1.}\tag{13}
\]
Exactly in that regime, (12) says their Möbius basis change is already boundedly invertible. There is no interval of standard diagonal weights in which the **critical** orbit is a vector in the completed Hilbert space but the primitive/full change of basis is singular or unbounded.

For \(\sigma>1/2\), the nonempty interval \(3/2-\sigma<\alpha\le1\) does have convergent orbit and shell vectors with unbounded ambient Möbius transform. It is **off-critical**, so the completion anomaly is not a mechanism selecting \(1/2\).

To check source specificity, replace PC-424's Bose seed \(b_\sigma\) by its matched regularized zero-free seed \(\widetilde b_\sigma\). Its nonconstant symbol also gives a nonzero \(\widetilde B_\sigma\in\mathcal S_2\), and the same translation covariance, divisor incidence, triangle estimates, and prime lower bounds prove (4), (9), and (13) verbatim with tildes. The control has no critical-strip Mellin zeros by PC-424, so none of these thresholds can imply an RH zero-placement condition.

## 6. Novelty, audit, and exact boundary

The operator-multiplier theorem is classical: Hedenmalm, Lindqvist and Seip, *A Hilbert space of Dirichlet series and systems of dilated functions in \(L^2(0,1)\)*, Duke Math. J. 86 (1997), 1–37, Theorem 3.1; PC-055 applies it to the scalar Möbius transform and gives the exact Euler-product bounds. The Hilbert--Schmidt commutator/Hankel model and its translation covariance are classical operator theory already audited in PC-421 and PC-424. The divisor-square Dirichlet identity (7) and divergence of the prime harmonic series are standard. No novelty is claimed for those ingredients.

The **line-local result** is the sharp classification (4) and (9) for the *actual* PC-424 radial Hilbert operator families, the no-improvement lemma (11) on nontrivial-shell coordinates, and the zero-free matched comparison. Together they close the explicitly named standard diagonal weighted completion left undecided in PC-424, without claiming that all conceivable infinite-dimensional constructions have been excluded.

Decisive audit points are: the exact translation factor \(d^{1-\sigma}\); the lower bound on \(E_d\); the divisor-square upper estimate; the prime-index necessity test; the isometric shift/intertwining identity; and the same estimates for the zero-free seed. A counterexample to any of these would invalidate the relevant threshold.

Still outside this result are **source-forced non-diagonal coefficient metrics**, shell-dependent operator domains/kernels, angular/old--new geometric couplings before radial scalarization, and independently defined renormalized determinant or cross-level limits whose topology is not equivalent to the diagonal \(\ell^2\) class. Any proposed escape must specify and justify that topology from the original geometry and survive the zero-free control, rather than merely invoking infinitely many levels.
