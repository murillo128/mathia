# PC-378 — Chebyshev Euler-product assembly collapses to the classical zeta divisor multiplier

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the most direct multiplicative completion of the infinite Chebyshev transfer family left open by PC-377. The algebraic Euler product of the source-derived prime backward shifts is exactly a weighted divisor-sum operator. Its adjoint is the classical Bohr multiplier with Euler-product symbol `zeta(w+conj(s)-1)`. The operator is closable exactly for `Re(s)>3/2` and bounded exactly for `Re(s)>2`; at the half-density line it is nonclosable. A matched prime-power control moves both thresholds, so neither boundary is an RH invariant.

The zeta appearance is therefore not a new spectral mechanism. It is the classical divisor/Euler-product multiplier already represented line-locally by PC-055, now reached canonically from the PC-372--PC-377 Chebyshev refinement quotient.

## 1. The full algebraic Euler product is well-defined on every finite mode

Let

\[
\mathcal H_+=\ell^2(\mathbb N),
\qquad
\mathcal D_0=\operatorname{span}_{\mathrm{fin}}\{e_n:n\ge1\},
\]

and use the Chebyshev backward shifts of PC-374--PC-377,

\[
P_m e_n=
\begin{cases}
e_{n/m},&m\mid n,\\
0,&m\nmid n.
\end{cases}
\tag{1}
\]

For a complex parameter `s`, consider the most direct multiplicative completion of the prime channels with the Jacobian degree factor inherited from PC-373--PC-374:

\[
\mathcal Z_s
:=
\prod_p^{\mathrm{alg}}
\left(I-p^{1-s}P_p\right)^{-1}
\quad\text{on }\mathcal D_0.
\tag{2}
\]

No analytic convergence prescription is needed to define (2) on the algebraic core. For a fixed basis vector `e_n`, only the finitely many primes dividing `n` act nontrivially, and each `P_p` is locally nilpotent on that vector:

\[
P_p^j e_n=0\qquad(j>\nu_p(n)).
\]

Hence every local inverse truncates exactly,

\[
(I-aP_p)^{-1}e_n
=
\sum_{j=0}^{\nu_p(n)}a^jP_p^j e_n,
\]

and unique factorization gives

\[
\boxed{
\mathcal Z_s e_n
=
\sum_{d\mid n} d^{1-s}e_{n/d}.
}
\tag{3}
\]

Thus the full prime Euler product has not created a new interaction among refinement channels: before any completion is chosen it is already the classical weighted divisor transform.

## 2. Closability has the same sharp `Re(s)>3/2` barrier as the linear aggregate

Write `sigma=Re(s)`. From (3), the formal adjoint action on a basis vector is

\[
\mathcal Z_s^*e_m
=
\sum_{d\ge1}d^{1-\overline s}e_{dm}.
\tag{4}
\]

The terms are orthogonal, so

\[
\|\mathcal Z_s^*e_m\|^2
=
\sum_{d\ge1}d^{2-2\sigma}
=
\zeta(2\sigma-2).
\tag{5}
\]

If `sigma>3/2`, every basis vector belongs to the adjoint domain; therefore `D_0 subset D(Z_s^*)`, the adjoint is densely defined, and `Z_s` is closable.

The converse has an elementary graph witness and does not rely on multiplier theory. For a finite set of primes `F`, put

\[
S_F:=\sum_{p\in F}|p^{1-s}|^2,
\qquad
x_F:=\frac1{S_F}\sum_{p\in F}\overline{p^{1-s}}e_p.
\tag{6}
\]

Since

\[
\mathcal Z_s e_p=e_p+p^{1-s}e_1,
\]

we obtain

\[
\|x_F\|^2=\frac1{S_F},
\qquad
\mathcal Z_s x_F=x_F+e_1.
\tag{7}
\]

For `sigma<=3/2`, Euler's reciprocal-prime divergence and comparison imply `S_F -> infinity` along increasing prime sets. Hence `x_F -> 0` while `Z_s x_F -> e_1`. The graph closure contains `(0,e_1)`, so `Z_s` is not closable. Therefore

\[
\boxed{
\mathcal Z_s\text{ is closable}
\iff
\operatorname{Re}s>\frac32.
}
\tag{8}
\]

The passage from the linear prime sum of PC-377 to the complete multiplicative Euler product does not repair its first functional-analytic obstruction.

## 3. The Bohr lift is literally a shifted zeta multiplier

Under the Bohr identification used in PC-376--PC-377,

\[
e_n\longleftrightarrow z^{\nu(n)},
\qquad
P_p^*\longleftrightarrow M_{z_p}.
\tag{9}
\]

Consequently the adjoint of (2), whenever interpreted on its natural polynomial domain, is multiplication by

\[
G_s(z)
=
\prod_p\left(1-p^{1-\overline s}z_p\right)^{-1}
=
\sum_{d\ge1}d^{1-\overline s}z^{\nu(d)}.
\tag{10}
\]

Under the usual Dirichlet-series representative `z_p=p^{-w}`, this becomes exactly

\[
\boxed{
G_s\longleftrightarrow
\sum_{d\ge1}d^{-(w+\overline s-1)}
=
\zeta(w+\overline s-1).
}
\tag{11}
\]

This is the decisive classical-collapse check. Zeta has not emerged as the spectrum or determinant of a new Prime-Circle operator. The chosen Euler-product assembly is simply the standard zeta Euler product in Bohr coordinates. After the parameter shift by `s-1` and adjoint orientation, this is the same divisor-sum multiplier mechanism classified in PC-055.

## 4. Boundedness is exactly `Re(s)>2`, with zeta norm

For `sigma>2`, the multiplier (10) is bounded and its norm is

\[
\boxed{
\|\mathcal Z_s\|
=
\|G_s\|_{H^\infty}
=
\prod_p(1-p^{1-\sigma})^{-1}
=
\zeta(\sigma-1).
}
\tag{12}
\]

The upper bound follows from the Euler product. For the reverse inequality, restrict to any finite prime set and choose the coordinate phases so that `p^{1-conj(s)}z_p` is positive real; then let the coordinate radii tend to one and enlarge the finite set. Thus the product itself is the exact multiplier norm.

If `3/2<sigma<=2`, the operator is closable by (8) but the multiplier cannot be bounded. The same finite-coordinate phase alignment gives partial products

\[
\prod_{p\in F}(1-p^{1-\sigma})^{-1},
\]

which are unbounded as `F` exhausts the primes when `sigma<=2`. Hence

\[
\boxed{
\mathcal Z_s\text{ is bounded}
\iff
\operatorname{Re}s>2.
}
\tag{13}
\]

The three regimes are therefore

\[
\begin{array}{c|c}
\operatorname{Re}s\le3/2&\text{nonclosable}\\
3/2<\operatorname{Re}s\le2&\text{closable but unbounded}\\
\operatorname{Re}s>2&\text{bounded, norm }\zeta(\operatorname{Re}s-1).
\end{array}
\tag{14}
\]

In particular the source-derived half-density regime `Re(s)=1/2` is not rescued by replacing the direct prime sum with its canonical geometric-series/Euler-product completion: the latter is still nonclosable on the finite-mode core.

## 5. Prime-power controls move both thresholds

The threshold locations are not intrinsic arithmetic critical lines. Replace the prime refinement degrees by the pairwise-coprime composite degrees `p^r`, `r>=2`, and form the matched operator

\[
\mathcal Z_s^{(r)}
=
\prod_p^{\mathrm{alg}}
\left(I-p^{r(1-s)}P_{p^r}\right)^{-1}.
\tag{15}
\]

Under the Bohr lift its adjoint multiplier is

\[
G_s^{(r)}(z)
=
\prod_p
\left(1-p^{r(1-\overline s)}z_p^r\right)^{-1}.
\tag{16}
\]

Its coefficient-square sum is

\[
\prod_p\left(1-p^{-2r(\sigma-1)}\right)^{-1}
=
\zeta(2r(\sigma-1)),
\tag{17}
\]

and the same prime-column graph witness used above proves the converse at the endpoint. Therefore

\[
\boxed{
\mathcal Z_s^{(r)}\text{ is closable}
\iff
\sigma>1+\frac1{2r}.
}
\tag{18}
\]

Finite-coordinate phase alignment similarly yields

\[
\boxed{
\mathcal Z_s^{(r)}\text{ is bounded}
\iff
\sigma>1+\frac1r,
\qquad
\|\mathcal Z_s^{(r)}\|=\zeta(r(\sigma-1)).
}
\tag{19}
\]

Thus the two vertical boundaries are ordinary summability/multiplier thresholds determined by degree growth. They move under a matched composite control and cannot by themselves encode the Riemann critical line.

## 6. Prior-art and novelty audit

The analytic object in (10)--(11) is classical. Håkan Hedenmalm, Peter Lindqvist and Kristian Seip, *A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)*, Duke Math. J. 86 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, supplies the Hardy/Dirichlet-series and infinite-polydisk multiplier framework already anchored in `SOURCES.md`. The Euler product and divisor coefficients in (11) are standard zeta theory. PC-055 already records the corresponding weighted divisor-sum/zeta multiplier and its Euler-product domain thresholds in the project.

Targeted literature checks around Hardy spaces of Dirichlet series, Bohr lifts, infinite-polydisk multipliers, zeta multipliers and unbounded multiplication operators did not reveal a distinct nonclassical mechanism behind (10). No historical novelty is claimed for the divisor transform, the zeta symbol, or the Hardy-space thresholds.

The project-local result is narrower and useful: PC-377 left multiplicative or all-depth assembly as a natural possible escape from the failure of the direct infinite linear sum. Equations (3), (8), (11), (13), and the control (18)--(19) show that the most canonical Euler-product completion closes back onto the already-classical PC-055 mechanism. Literal multiplication of all prime Chebyshev refinement channels therefore does not create a new RH-facing operator.

## 7. Boundary of the negative result

This finding closes the **canonical commuting Euler-product assembly** of the PC-376--PC-377 Chebyshev quotient. It does not rule out nonlinear interactions before that quotient, matrix-valued or noncommuting cross-shell couplings, source-forced boundary/domain conditions not given by closure of `D_0`, or a global topology in which the prime channels do not factor into independent commuting coordinates.

Those surviving routes must retain information destroyed by the divisor/Bohr reduction. Merely replacing the prime sum by its full geometric-series product, even though that product writes zeta explicitly, adds no such information and reproduces a classical divisor multiplier rather than a new mechanism for the zeta zero set or the critical line.

## Research consequence

The finite-polydisk collapse of PC-376 and the linear infinite-family obstruction of PC-377 now extend through the canonical multiplicative completion. The direct sum and the full commuting Euler product both exhaust into classical Hardy/Dirichlet objects with summability boundaries far to the right of `Re(s)=1/2`. Any surviving Prime-Circle route beyond the Chebyshev quotient therefore needs genuinely non-factorizing cross-shell or pre-quotient structure, not a different scalar packaging of the same commuting refinement shifts.